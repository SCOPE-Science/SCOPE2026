from collections import Counter
N=32;MASK=(1<<N)-1

def canonical(w):return min(w[i:]+w[:i] for i in range(N))

def d(w):
 p=[0]
 for a in w:p.append(p[-1]+(1 if a else -1))
 return max(p)-min(p)

allhist=Counter();crhist=Counter();orbit_hist=Counter();found=[]
for g in range(1<<16):
 state=0;seen=0;w=[]
 for _ in range(N):
  if seen>>state&1:break
  seen|=1<<state
  first=state>>4;w.append(first)
  state=((state&15)<<1)|(first^((g>>(state&15))&1))
 if len(w)!=N or state!=0:continue
 w=tuple(w)
 disc=d(w);allhist[disc]+=1
 c=tuple(1-v for v in w);rev=w[::-1]
 cr=(canonical(c)==canonical(rev))
 if cr:crhist[disc]+=1
 S={canonical(w),canonical(c),canonical(rev),canonical(tuple(1-v for v in rev))}
 orbit_hist[(disc,len(S))]+=1
 found.append((g,w,disc,cr,len(S)))
print('FSM ALL',sum(allhist.values()),sorted(allhist.items()))
print('FSM CR',sum(crhist.values()),sorted(crhist.items()))
print('FSM ORBITS',[((d,s),ct//s) for (d,s),ct in sorted(orbit_hist.items())])
print('FSM ORBIT CLASS MULTIPLICITIES',sorted(orbit_hist.items()))
assert allhist=={5:224,6:688,7:912,8:224}
assert crhist=={5:16,6:16,7:24,8:8}
assert orbit_hist=={(5,2):16,(5,4):208,(6,2):16,(6,4):672,(7,2):24,(7,4):888,(8,2):8,(8,4):216}
print('FSR_OK')
