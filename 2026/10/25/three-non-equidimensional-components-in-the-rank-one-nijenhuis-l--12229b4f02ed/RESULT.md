# Three non-equidimensional components in the rank-one Nijenhuis locus of \(\mathfrak n_4\)

## Finding
Let \(k\) be **any** field and let \(\mathfrak g=\mathfrak n_4(k)\) be the six-dimensional Lie algebra of strictly upper-triangular \(4\times4\) matrices. A Nijenhuis operator is a linear endomorphism \(N\) satisfying
\[
[Nx,Ny]=N([Nx,y]+[x,Ny]-N[x,y])\qquad(x,y\in\mathfrak g).
\]
For \(N\) of vector-space rank one, write \(N(x)=f(x)Y\), where \(0\ne f\in\mathfrak g^*\) and \(0\ne Y\in\mathfrak g\). The classification below gives the **complete** admissible subspace \(K_f\) of image generators \(Y\), with no characteristic restriction.

Choose the basis \(a=E_{12},b=E_{23},c=E_{34},d=E_{13},e=E_{24},z=E_{14}\), and write
\[
f=(u,v,w,s,t,h),\qquad Y=Aa+Bb+Cc+Dd+Ee+Fz.
\]
The coordinates of \(f\) are evaluations in the displayed basis. Then \(N\) is Nijenhuis **if and only if** \(Y\in K_f\), where:

1. If \(h\ne0\), then
\[
K_f=k\left(b-\frac{t}{h}d-\frac{s}{h}e+\frac{2st-hv}{h^2}z\right),\qquad\dim K_f=1.
\]
2. If \(h=0\) and \((s,t)\ne(0,0)\), then
\[
K_f=\left\{t\lambda a+s\lambda c+Dd+Ee+Fz:\ sD+tE=-(sw+tu)\lambda\right\},\qquad\dim K_f=3.
\]
3. If \(h=s=t=0\), then \(K_f=\mathfrak g\) and \(\dim K_f=6\).

Consequently the **reduced projectivized rank-one Nijenhuis locus** has exactly three irreducible components, of dimensions \(5,6,7\). Equivalently, the reduced affine locus of Nijenhuis operators of rank at most one has three irreducible components, of dimensions \(6,7,8\). These dimensions and the classification hold over every field, including characteristic two.

For every prime power \(q\), the exact number \(T(q)\) of **nonzero rank-one** Nijenhuis endomorphisms is
\[
\boxed{T(q)=\frac{(q^3-1)(q^6-1)}{q-1}+\frac{q^3(q^2-1)(q^3-1)}{q-1}+q^5(q-1).}
\]
Precisely \((q^3-1)q^5\) have \(N^2\ne0\); the other \(T(q)-(q^3-1)q^5\) satisfy \(N^2=0\). In particular, \(T(2)=641\), of which \(417\) square to zero, and \(T(3)=12758\).

## Assumptions and scope
The Lie bracket is the ordinary matrix commutator \([X,Y]=XY-YX\), which is alternating even in characteristic two. The only nonzero independent basis brackets are
\[
[a,b]=d,\quad[b,c]=e,\quad[a,e]=z,\quad[d,c]=z.
\]
The operator rank is the rank of \(N\colon\mathfrak g\to\mathfrak g\), not the matrix rank of its values. Every nonzero rank-one map admits a factorization \(N=Y\otimes f\), unique up to \((Y,f)\mapsto(\alpha Y,\alpha^{-1}f)\) for \(\alpha\in k^\times\). Projectivization and irreducible components refer to reduced algebraic varieties after base change to an algebraic closure; the explicit strata are defined over the original field. The numerical count requires a finite field, but the fiber and geometric theorems do not.

## Proof
**1. A scalar torsion equation.** Put \(g_Y(x)=f([Y,x])\). Since \([f(x)Y,f(y)Y]=0\), substituting \(N(x)=f(x)Y\) in the defining identity shows that the Nijenhuis condition is exactly
\[
 f(x)g_Y(y)-f(y)g_Y(x)-f(Y)f([x,y])=0
 \quad\text{for all }x,y\in\mathfrak g.\tag{1}
\]
For fixed \(f\), the left side is linear in \(Y\); thus its solution space is a linear subspace \(K_f\). The alternating condition need only be checked on the \(15\) unordered pairs of distinct basis vectors, including in characteristic two.

**2. The top-derived-coordinate stratum.** Suppose \(h=f(z)\ne0\). Substitution in (1) on the pairs \((d,z),(e,z),(a,z),(c,z),(a,e)\) gives, respectively,
\[
h^2C=0,\quad h^2A=0,\quad hsB+h^2E=0,\quad htB+h^2D=0,
\]
\[
 (-hv+st)B-hsD-h^2F=0.
\]
Therefore \(A=C=0\), \(D=-tB/h\), \(E=-sB/h\), and \(F=(2st-hv)B/h^2\). Direct substitution into the remaining ten pairs verifies that all equations (1) vanish, so these necessary conditions are also sufficient. This proves the first formula and dimension \(1\).

**3. The middle-derived-coordinate stratum.** Suppose \(h=0\) but \((s,t)\ne(0,0)\). The pairs \((a,d),(c,e)\) give \(s^2B=t^2B=0\), hence \(B=0\). The pairs \((b,d),(b,e)\) require \(sA=tC\), so uniquely \(A=t\lambda\), \(C=s\lambda\). The pairs \((a,b),(b,c)\) reduce to the one remaining equation
\[
 sD+tE=-(sw+tu)\lambda.
\]
All other pairs vanish once these relations hold. There is one free \(\lambda\), one free coordinate among \(D,E\), and free \(F\). Thus \(\dim K_f=3\), as asserted. No division by \(2\) was used.

**4. The abelianization stratum.** If \(h=s=t=0\), the functional annihilates \([\mathfrak g,\mathfrak g]=\langle d,e,z\rangle\). Accordingly \(g_Y=0\) and \(f([x,y])=0\) for all \(x,y,Y\), and (1) is vacuous. Thus \(K_f=\mathfrak g\).

**5. Components.** The projectivized rank-one operators are the Segre variety \(\mathbb P(\mathfrak g)\times\mathbb P(\mathfrak g^*)\) in \(\mathbb P(\operatorname{End}\mathfrak g)\). The projective Nijenhuis subvariety is the closed incidence locus \(\{([Y],[f]):Y\in K_f\}\). Projection to \([f]\in\mathbb P^5\) stratifies this variety into: the chart \(h\ne0\), whose base has dimension \(5\) and fibers \(\mathbb P^0\); the subset \(h=0,(s,t)\ne0\), whose base has dimension \(4\) and fibers \(\mathbb P^2\); and the closed base \(h=s=t=0\cong\mathbb P^2\), with full fibers \(\mathbb P^5\). Each stratum is irreducible because the constant-rank kernels are algebraic vector bundles over an irreducible base, with total dimensions \(5,6,7\). Their closures are distinct components: the first meets the open chart \(h\ne0\), the second meets \(h=0,(s,t)\ne0\) and has greater dimension than the first, and the third is closed and has greater dimension than both. Every point belongs to one of the three strata, so there are no additional components. Passing to affine cones adds one to each dimension.

**6. Exact counts and squares.** Among nonzero \(f\in\mathbb F_q^6\), the three strata have respectively \((q-1)q^5\), \(q^3(q^2-1)\), and \(q^3-1\) choices. For a fixed \(f\), exactly \(q^{\dim K_f}-1\) nonzero \(Y\) work. Each nonzero operator is represented by exactly \(q-1\) pairs \((Y,f)\), proving the displayed \(T(q)\). Furthermore
\[
N^2=f(Y)N.
\]
The formulas in steps 2 and 3 give \(f(Y)=0\). On the third stratum, each nonzero \(f\) has exactly \(q^6-q^5\) vectors \(Y\) with \(f(Y)\ne0\). Dividing the resulting pair count by \(q-1\) gives \((q^3-1)q^5\) non-square-zero operators. This also proves the complementary square-zero count.

## Verification
A standalone standard-library program `verify_n4.py` reconstructs the Lie brackets from \(4\times4\) matrix units, reconstructs the fifteen rank-one Nijenhuis equations independently from the full torsion identity, and computes their kernels using finite-field elimination. It checks every nonzero functional over \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\) and additionally checks all nonzero \((f,Y)\) pairs over \(\mathbb F_2\). It verifies fiber dimensions \(1,3,6\), the stratum sizes, and the total counts \(641,12758,109227,589844\). Run `python3 verify_n4.py` from the directory containing this result. These finite tests are independent checks, not a replacement for the all-field algebraic proof.

## Relationship to prior work
Azimi, Laurent-Gengoux and Nunes da Costa (arXiv:1308.6119, first public version 2013-08-28) give the standard Lie Nijenhuis torsion identity as part of the broader theory of Nijenhuis forms and deformations; see their equation (11). Hu, Liu and Sheng (arXiv:2004.10065) study Nijenhuis operators together with representations and Kupershmidt structures; their introductory equation (1) uses the same operator identity. Their results on general deformations and compatible structures are not presented here as new. Neither inspected work gives the characteristic-independent three-stratum fiber classification, component dimensions, or exact finite-field rank-one census of the class-three algebra \(\mathfrak n_4\). This comparison does not certify absolute publication priority: a broader low-dimensional classification or a different equivalent formulation could subsume the present specialized result. Results for two-step nilpotent Lie algebras do not automatically cover this class-three algebra, since \([\mathfrak g,[\mathfrak g,\mathfrak g]]\ne0\).

## Limitations
The theorem classifies only rank-one Nijenhuis endomorphisms, not arbitrary-rank operators, conjugacy orbits, or the potentially nonreduced Nijenhuis scheme. The geometric assertion is explicitly about reduced varieties. Exact finite-field formulas are deduced from the proof and separately checked for four field sizes; no computation can establish the all-field conclusion on its own. Historical novelty beyond the sources actually inspected remains subject to independent assessment.

## References
1. M. J. Azimi, C. Laurent-Gengoux and J. M. Nunes da Costa, *Nijenhuis forms on \(L_\infty\)-algebras and Poisson geometry*, arXiv:1308.6119, first posted 2013-08-28, https://arxiv.org/abs/1308.6119.
2. Y. Hu, J. Liu and Y. Sheng, *Kupershmidt-(dual-)Nijenhuis structures on a Lie algebra with a representation*, arXiv:2004.10065, first posted 2020-04-21, https://arxiv.org/abs/2004.10065.
