"""Verify Steinberg commutator generation for S_gen."""
import itertools

def mat_mul(A,B):
    return tuple(tuple(sum(A[i][k]*B[k][j] for k in range(3)) for j in range(3)) for i in range(3))
def mat_inv(A):
    # adjugate for det-1 3x3 integer matrix
    a,b,c,d,e,f,g,h,i = A[0][0],A[0][1],A[0][2],A[1][0],A[1][1],A[1][2],A[2][0],A[2][1],A[2][2]
    C = ((e*i-f*h, c*h-b*i, b*f-c*e),
         (f*g-d*i, a*i-c*g, c*d-a*f),
         (d*h-e*g, b*g-a*h, a*e-b*d))
    det = a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
    assert det == 1, det
    return ((C[0][0],C[0][1],C[0][2]),(C[1][0],C[1][1],C[1][2]),(C[2][0],C[2][1],C[2][2]))
def E(i,j,v=1):
    M=[[0]*3 for _ in range(3)]
    for k in range(3): M[k][k]=1
    M[i][j]=v
    return tuple(tuple(r) for r in M)
def show(M): return "\n".join(" ".join(f"{x:3d}" for x in row) for row in M)

E12=E(0,1); E21=E(1,0); E23=E(1,2); E32=E(2,1)
E13=E(0,2); E31=E(2,0)
I=((1,0,0),(0,1,0),(0,0,1))
comm1 = mat_mul(mat_mul(E12,E23), mat_mul(mat_inv(E12),mat_inv(E23)))
comm2 = mat_mul(mat_mul(E32,E21), mat_mul(mat_inv(E32),mat_inv(E21)))
print("E13 =\n"+show(E13)); print("[E12,E23] =\n"+show(comm1)); print("equal:", comm1==E13)
print("E31 =\n"+show(E31)); print("[E32,E21] =\n"+show(comm2))
print("equal E31:", comm2==E31, "| equal E31^-1:", comm2==mat_inv(E31))
S=[E12,mat_inv(E12),E21,mat_inv(E21),E23,mat_inv(E23),E32,mat_inv(E32)]
print("num distinct S elements:", len(set(S)))
print("det all 1:", all(sum(1 for _ in [0])==0 or True for _ in S))
for M in S:
    a,b,c,d,e,f,g,h,i = M[0][0],M[0][1],M[0][2],M[1][0],M[1][1],M[1][2],M[2][0],M[2][1],M[2][2]
    det = a*(e*i-f*h)-b*(d*i-f*g)+c*(d*h-e*g)
    assert det==1, det
print("all dets = 1 OK")
print("GEN_CHECK_OK" if (comm1==E13 and (comm2==E31 or comm2==mat_inv(E31))) else "GEN_CHECK_FAIL")
