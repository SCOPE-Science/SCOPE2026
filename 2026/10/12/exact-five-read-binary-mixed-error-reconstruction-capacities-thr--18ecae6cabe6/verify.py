#!/usr/bin/env python3
"""Self-contained exact verification for binary mixed-error five-read codes.
Uses two channel representations and an exact coloring-bound clique search.
"""
from itertools import combinations

WITNESSES = {
    4: ('0000','0001','0111','1100','1111'),
    5: ('00000','00111','10001','11100','11111'),
    6: ('000000','000111','011110','100001','111000','111111'),
    7: ('0000000','0000011','0001100','0011111','1100000','1110011','1111100','1111111'),
    8: ('00000000','00000111','00011111','00110010','01001100','01111110','10000001','11001111','11100000','11110011','11111000','11111111'),
}

def ball_del_then_sub(x):
    n=len(x);out=set()
    for d in range(n):
        word=x[:d]+x[d+1:]
        out.add(word)
        for j in range(n-1):
            out.add(word[:j]+str(1-int(word[j]))+word[j+1:])
    return out

def ball_sub_then_del(x):
    n=len(x);out=set()
    changes=[x]+[x[:i]+str(1-int(x[i]))+x[i+1:] for i in range(n)]
    for w in changes:
        for d in range(n):out.add(w[:d]+w[d+1:])
    return out

def maximum_clique(adj):
    m=len(adj);best=0;nodes=0
    def search(candidates,depth):
        nonlocal best,nodes
        nodes+=1
        if not candidates:
            if depth>best:best=depth
            return
        order=[];colors=[];curcolor=0;unused=candidates
        while unused:
            curcolor+=1
            free=unused
            while free:
                bit=free&-free;v=bit.bit_length()-1
                order.append(v);colors.append(curcolor)
                unused ^=bit
                free=(free^bit)&~adj[v]
        mask_before=[0]*len(order);prefix=0
        for i,v in enumerate(order):
            mask_before[i]=prefix;prefix|=1<<v
        for i in range(len(order)-1,-1,-1):
            if depth+colors[i]<=best:return
            v=order[i]
            search(adj[v]&mask_before[i],depth+1)
    search((1<<m)-1,0)
    return best,nodes

def run():
    for n,words in WITNESSES.items():
        V=[format(x, f'0{n}b') for x in range(1<<n)]
        B=[ball_del_then_sub(x) for x in V]
        assert all(B[i]==ball_sub_then_del(V[i]) for i in range(len(V)))
        idx={word:i for i,word in enumerate(V)}
        assert len(set(words))==len(words) and all(len(s)==n for s in words)
        overlaps=[len(B[idx[a]]&B[idx[b]]) for a,b in combinations(words,2)]
        assert max(overlaps)<5
        adj=[0]*len(V); edges=0
        for i in range(len(V)):
            for j in range(i):
                if len(B[i]&B[j])<5:
                    adj[i]|=1<<j;adj[j]|=1<<i;edges+=1
        optimum,nodes=maximum_clique(adj)
        assert optimum==len(words), (n,optimum,len(words))
        print(f'n={n} optimum={optimum} admissible_edges={edges} proof_nodes={nodes} witness_max_overlap={max(overlaps)}')
    print('VERIFY_OK')
if __name__=='__main__':run()
