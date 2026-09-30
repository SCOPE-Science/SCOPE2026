# Connectedness of the Heisenberg-quotient truncated point scheme V_3(Q) with singular intersection certificate

## Context

Let k be algebraically closed of characteristic different from 2 and 3 and contain a primitive cube root of unity w.  Let

S=k<x,y,z>/(x^2,y^2,z^2)

and let Q=T_1 be the t=1 diagonal Heisenberg quotient considered by De Laet, with the two cubic relations

v_1=(zxy+w xyz+w^2 yzx)+(yxz+w zyx+w^2 xzy),

v_2=(zxy+w^2 xyz+w yzx)+(yxz+w^2 zyx+w xzy).

The cited De Laet paper describes the quotient and its infinite point modules, while Walton studies truncated point schemes for the unquotiented degenerate Sklyanin algebra.  The finite-level computation below is for this fixed quotient Q.

## Result

The reduced length-4 truncated point scheme (V_3(Q))_red in (P^2)^3 is the union of six smooth rational curves

E_0,E_1,E_2,D_0,D_1,D_2.

Their incidence graph is K_{3,3} minus a perfect matching: E_i meets D_j exactly when i != j, and all other pairwise intersections are empty.  Hence the reduced scheme is connected; its incidence graph is a 6-cycle.

The point

P=([0:1:0],[1:0:0],[0:1:0])

lies on exactly E_0 and D_1.  In the affine chart Y_0=X_1=Y_2=1, the Jacobian of the defining equations at P has rank exactly 4 in six affine variables, so the Zariski tangent space has dimension 2 whereas the local dimension is 1.  Thus P is singular.

## Proof

Let q_0=[1:0:0], q_1=[0:1:0], q_2=[0:0:1], and L_0=V(X), L_1=V(Y), L_2=V(Z).

The six multilinearized quadratic relations are

X_jX_{j+1}=Y_jY_{j+1}=Z_jZ_{j+1}=0,  j=0,1.

For a pair of points, these equations give the six components {q_i}xL_i and L_i x {q_i}.  For triples, the quadratic locus is therefore the union of

C_i=L_i x {q_i} x L_i,
D_i={q_i} x L_i x {q_i},   i=0,1,2.

Restricting the two multilinearized cubic relations to C_i gives the same equation up to a nonzero scalar:

C_0:  Z_0Y_2+Y_0Z_2=0,
C_1:  X_0Z_2+Z_0X_2=0,
C_2:  X_0Y_2+Y_0X_2=0.

Each is a smooth (1,1)-curve in P^1 x P^1; call it E_i.  Every cubic monomial contains one x, one y and one z, so on D_i at least one endpoint factor vanishes in every monomial.  Hence every D_i lies in V_3(Q).

For i != j the unique intersection point of C_i and D_j is (q_j,q_i,q_j), and it satisfies the corresponding bilinear equation, so E_i meets D_j there.  If i=j, q_i is not on L_i, so E_i and D_i are disjoint.  Different E_i have different middle vertices and different D_i have different endpoints, so there are no other pairwise intersections.  This proves the stated 6-cycle incidence and connectedness.

At P=(q_1,q_0,q_1), use affine variables

a_0=X_0, b_1=Y_1, c_0=Z_0, c_1=Z_1, a_2=X_2, c_2=Z_2

in the chart Y_0=X_1=Y_2=1.  The linear parts include

d(X_0X_1)=a_0,
d(Y_0Y_1)=b_1,
d(X_1X_2)=a_2,
d(F_1)=d(F_2)=c_0+c_2,

while the remaining quadratic rows vanish to first order or duplicate these rows.  The rows X_0X_1, Y_0Y_1, F_1, X_1X_2 and columns a_0,b_1,c_0,a_2 form an identity minor, so the rank is exactly 4.  Thus the tangent dimension is 6-4=2.  Since P lies on exactly two one-dimensional components, the local dimension is 1, proving singularity.

## Reproducibility

Run

`python3 artifacts/verify_v3.py`

The exact zero-dependency script checks all cubic restrictions, D_i containment, the full incidence table, membership of P, and the rank-4 Jacobian certificate.  Its recorded output is `artifacts/verify_results.txt`.

## Limitations

Only Q=T_1 and d=3 are treated.  Other diagonal parameters, Zhang-twisted quotients, SL_2(3)-orbit translates and higher truncation levels are outside this result.  The argument assumes characteristic different from 2 and 3 and a primitive cube root of unity.

## References

- K. De Laet, Quotients of degenerate Sklyanin algebras, arXiv:1510.04024.
- C. Walton, Degenerate Sklyanin algebras and Generalized Twisted Homogeneous Coordinate rings, arXiv:0812.0609; corrigendum arXiv:1112.5211.
