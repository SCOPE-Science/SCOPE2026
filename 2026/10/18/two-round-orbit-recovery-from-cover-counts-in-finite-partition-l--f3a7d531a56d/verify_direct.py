"""Direct Hasse-arc enumeration for finite partition lattices.
Usage: python verify_direct.py
"""
from collections import Counter, defaultdict

def set_partitions(n):
    if n == 0: return [()]
    words=[(0,)]
    for _ in range(1,n):
        words=[w+(v,) for w in words for v in range(max(w)+2)]
    return words

def coarsen(w,a,b):
    labels=[a if x==b else x for x in w]
    names={x:i for i,x in enumerate(sorted(set(labels)))}
    return tuple(names[x] for x in labels)

def colors_after_two(n):
    words=set_partitions(n)
    index={w:i for i,w in enumerate(words)}
    outgoing=[[] for _ in words]
    incoming=[[] for _ in words]
    for i,w in enumerate(words):
        for a in range(max(w)+1):
            for b in range(a+1,max(w)+1):
                j=index[coarsen(w,a,b)]
                outgoing[i].append(j)
                incoming[j].append(i)
    def compress(signatures):
        dictionary={s:i for i,s in enumerate(sorted(set(signatures)))}
        return [dictionary[s] for s in signatures]
    c0=[0]*len(words)
    def step(colors):
        return compress([(colors[i],tuple(sorted(Counter(colors[j] for j in outgoing[i]).items())),
                          tuple(sorted(Counter(colors[j] for j in incoming[i]).items())))
                         for i in range(len(words))])
    c1=step(c0)
    c2=step(c1)
    typ=[tuple(sorted(Counter(w).values())) for w in words]
    classes=defaultdict(set)
    for cc,tp in zip(c2,typ):classes[cc].add(tp)
    assert len(classes)==len(set(typ)) and all(len(v)==1 for v in classes.values())
    return len(words),len(set(c1)),len(set(c2))

def split_degree(parts):
    return sum(2**(s-1)-1 for s in parts)

def first_signature(parts):
    return (len(parts)*(len(parts)-1)//2,split_degree(parts))

def main():
    counts=[]
    for n in range(1,9):
        size,a,b=colors_after_two(n)
        counts.append((n,size,a,b))
    bad_a=(1,1,3,3,3,3)
    bad_b=(2,2,2,2,2,4)
    assert sum(bad_a)==sum(bad_b)==14
    assert first_signature(bad_a)==first_signature(bad_b)==(15,12)
    assert sorted(bad_a)!=sorted(bad_b)
    for a in range(1,90):
        for b in range(a,90):
            v=(2**a-1)*(2**b-1)
            if (a,b)==(1,1):assert v==1
            else:
                low=(v-1)&-(v-1)
                assert low.bit_length()-1==(a if a<b else a+1)
    print('DIRECT_HASSE_REFINEMENT_PASS')
    print('n,vertices,round1_classes,round2_classes')
    for z in counts:print(','.join(map(str,z)))
    print('n14_round1_collision',bad_a,bad_b,'signature',(15,12))
    print('two_adic_product_lemma_checked_pairs',89*90//2)
if __name__=='__main__':main()
