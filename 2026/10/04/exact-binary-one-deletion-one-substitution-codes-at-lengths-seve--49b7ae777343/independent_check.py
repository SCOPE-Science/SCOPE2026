from itertools import combinations

def outputs(word):
    n=len(word)
    ans=set()
    for d in range(n):
        y=word[:d]+word[d+1:]
        ans.add(y)
        for s in range(n-1):
            z=list(y)
            z[s]='1' if z[s]=='0' else '0'
            ans.add(''.join(z))
    return ans

def compatible_words(n):
    words=[format(i,f'0{n}b') for i in range(2**n)]
    balls={w:outputs(w) for w in words}
    nbr={w:set() for w in words}
    for i,w in enumerate(words):
        for v in words[i+1:]:
            if balls[w].isdisjoint(balls[v]):
                nbr[w].add(v); nbr[v].add(w)
    return words,balls,nbr

def all_k_cliques(words,nbr,k):
    found=[]
    def visit(prefix,candidates):
        if len(prefix)==k:
            found.append(tuple(prefix)); return
        if len(prefix)+len(candidates)<k:return
        while candidates:
            v=candidates.pop(0)
            nxt=[u for u in candidates if u in nbr[v]]
            visit(prefix+[v],nxt)
    visit([],words[:])
    return found

w7,b7,n7=compatible_words(7)
assert all(b7[a].isdisjoint(b7[b]) for a,b in combinations(['0010110','1110000','1111111'],2))
assert len(all_k_cliques(w7,n7,4))==0
w8,b8,n8=compatible_words(8)
c5=all_k_cliques(w8,n8,5)
assert len(c5)==12
assert all('00000000' in c and '11111111' in c for c in c5)
assert all(not set.intersection(*(n8[v] for v in c)) for c in c5)
print('INDEPENDENT_OK 3 5 12')
