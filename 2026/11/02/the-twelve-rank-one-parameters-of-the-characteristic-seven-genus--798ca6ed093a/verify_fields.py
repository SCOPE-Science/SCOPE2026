#!/usr/bin/env python3
"""Independent coefficient extraction on all marked F7 and F49 Howe curves."""
P=7

def gf_add(x,y):return ((x%P+y%P)%P)+P*((x//P+y//P)%P)
def gf_neg(x):return (-x)%P+P*((-(x//P))%P)
def gf_mul(x,y):
 a,b=x%P,x//P;c,d=y%P,y//P
 return (a*c+3*b*d)%P+P*((a*d+b*c)%P)
def gf_sub(x,y):return gf_add(x,gf_neg(y))
def gf_scale(x,m):return gf_mul(x,m%P)
def mulpoly(f,g):
 h=[0]*(len(f)+len(g)-1)
 for i,x in enumerate(f):
  for j,y in enumerate(g):h[i+j]=gf_add(h[i+j],gf_mul(x,y))
 return h

def powerpoly(f,k):
 out=[1]
 for _ in range(k):out=mulpoly(out,f)
 return out

def quotient_p7(a,b):
 f0=mulpoly([1,gf_neg(a),1],[1,gf_neg(b),1])
 fp=mulpoly([gf_neg(gf_add(a,2)),0,1],[gf_neg(gf_add(b,2)),0,1])
 fm=mulpoly([gf_neg(gf_sub(a,2)),0,1],[gf_neg(gf_sub(b,2)),0,1])
 return [powerpoly(f,3)[6] for f in (f0,fp,fm)]

def smooth(a,b):return a not in (2,5) and b not in (2,5) and a!=b

for n in (7,49):
 h=[0,0,0,0]
 r0=[];r1=[]
 for a in range(n):
  for b in range(n):
   if not smooth(a,b):continue
   f=mulpoly([1,0,gf_neg(a),0,1],[1,0,gf_neg(b),0,1]); cube=powerpoly(f,3)
   hw=[[cube[7*(i+1)-(j+1)] for j in range(3)] for i in range(3)]
   assert hw[0][1]==hw[1][0]==hw[1][2]==hw[2][1]==0
   assert hw[0][0]==hw[2][2] and hw[0][2]==hw[2][0]
   eig=[gf_add(hw[0][0],hw[0][2]), hw[1][1],gf_sub(hw[0][0],hw[0][2])]
   quot=quotient_p7(a,b)
   assert eig == [quot[2],quot[0],quot[1]]
   rank=sum(int(x!=0) for x in quot)
   h[rank]+=1
   if rank==0:r0.append((a,b))
   if rank==1:r1.append((a,b))
 if n==7:assert h==[2,12,6,0]
 if n==49:assert h[0]==2 and h[1]==12 and sum(h)==(n-2)*(n-3)
 print('HOWE_7_FIELD_OK field=',n,'rank_counts=',h,'rank0=',r0,'rank1_count=',len(r1))
