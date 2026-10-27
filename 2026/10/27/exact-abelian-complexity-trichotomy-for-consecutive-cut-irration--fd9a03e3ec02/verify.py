q=10007
for m in range(2,12):
 for p in range(1,min(q//m,70)):
  if p*m>=q: continue
  for n in range(1,32):
   t=(n*p)%q
   ends=sorted(set((j*p)%q for j in range(m+1)) | set(((j*p - k*p)%q) for j in range(m+1) for k in range(n)))
   # each interval use midpoint with x in [0,1)
   words=set(); vectors=set()
   for idx,left in enumerate(ends):
    right=ends[idx+1] if idx+1<len(ends) else ends[0]+q
    x2=(left+right) % (2*q) # coordinate 2*q with x2 = left+right
    word=tuple(min((x2+2*k*p)%(2*q)//(2*p),m) for k in range(n))
    words.add(word)
    vectors.add(tuple(word.count(j) for j in range(m+1)))
   v=(m+n if n<m else (2*m if p<t<q-p else m+1))
   if len(vectors)!=v or len(words)!=n+m:
    print('FAIL',m,p,n,t,len(words),n+m,len(vectors),v)
    raise SystemExit(1)
 print('passed m=',m)
print('VERIFY_OK')
