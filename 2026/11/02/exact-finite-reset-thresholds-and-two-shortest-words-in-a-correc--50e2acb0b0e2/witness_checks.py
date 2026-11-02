from forward_bfs import trans

def word(p,v):
 return 'ba'*p+'ab'*(p-1)+v+'ba'*(p-2)+''.join('a'+'ba'*j for j in range(2*p-2,p-1,-1))+'ab'*p

def check(p,v):
 a,b=trans(p); W=word(p,v);states=set(range(3*p))
 for ch in W:
  T=a if ch=='a' else b
  states={T[x] for x in states}
 return len(W), sorted(states)
for p in range(3,16):
 print(p,3*p*p+4*p-1,check(p,'aaaa'),check(p,'abba'))
 assert check(p,'aaaa')==check(p,'abba')==(3*p*p+4*p-1,[2])
