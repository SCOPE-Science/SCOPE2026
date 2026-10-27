"""Independent finite checks of the minimum restrained double Roman cycle census.
Standard library only. This does not replace the infinite combinatorial proof.
"""
from itertools import product

def admissible(triple):
    a,b,c=triple
    if b==0:
        return (a==0 or c==0) and (a==3 or c==3 or (a==2 and c==2))
    if b==1:
        return (a>=2 or c>=2)
    return True

def valid(labels):
    n=len(labels)
    return all(admissible((labels[(i-1)%n], labels[i], labels[(i+1)%n])) for i in range(n))

def predicted(n):
    minimum = n if n%3==0 else n+2
    count = 3 if n%3==0 else (10 if n in (4,5) else n)
    return minimum,count

def orbit_key(word):
    word=tuple(word)
    n=len(word)
    rotations=[word[j:]+word[:j] for j in range(n)]
    reversed_word=word[::-1]
    rotations += [reversed_word[j:]+reversed_word[:j] for j in range(n)]
    return min(rotations)

def brute(n):
    best=None; count=0; optimal_words=[]
    for labels in product(range(4),repeat=n):
        w=sum(labels)
        if best is not None and w>best: continue
        if not valid(labels):continue
        if best is None or w<best:
            best,count=w,1
            optimal_words=[labels]
        elif w==best:
            count+=1
            optimal_words.append(labels)
    return best,count,len(set(map(orbit_key,optimal_words)))

def transfer(n):
    # Cyclic 2-site de Bruijn automaton; count the min-weight closed walks.
    states=list(product(range(4),repeat=2))
    transitions={s:[(t,t[1]) for t in states
        if s[1]==t[0] and admissible((s[0],s[1],t[1]))]
        for s in states}
    optimum=None;ways=0
    for start in states:
        dp={start:(0,1)}
        for _ in range(n):
            nd={}
            for state,(weight,count) in dp.items():
                for nxt,label in transitions[state]:
                    new_weight=weight+label
                    if nxt not in nd or new_weight<nd[nxt][0]:
                        nd[nxt]=(new_weight,count)
                    elif new_weight==nd[nxt][0]:
                        nd[nxt]=(new_weight,nd[nxt][1]+count)
            dp=nd
        if start in dp:
            w,c=dp[start]
            if optimum is None or w<optimum:optimum,ways=w,c
            elif w==optimum:ways+=c
    return optimum,ways

def verify():
    brute_n=range(3,10)
    transfer_n=range(3,121)
    for n in brute_n:
        obs=brute(n)
        expected_orbits = 3 if n==4 else 2 if n==5 else 1
        assert obs==(*predicted(n),expected_orbits),(n,'brute-orbits',obs,predicted(n))
    for n in transfer_n:
        obs=transfer(n)
        assert obs==predicted(n),(n,'transfer',obs,predicted(n))
    print('PASS direct exhaustive enumeration and dihedral orbits: n=3..9')
    print('PASS independent weighted cyclic automaton: n=3..120')
    print('checkpoints:', [(n,transfer(n)) for n in (3,4,5,6,7,8,9,10,11,12,29,120)])
if __name__=='__main__':verify()
