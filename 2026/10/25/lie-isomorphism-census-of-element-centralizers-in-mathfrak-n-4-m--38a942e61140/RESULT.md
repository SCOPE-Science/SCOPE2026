# Lie-isomorphism census of element centralizers in \(\mathfrak n_4(\mathbb F_q)\)

## Finding

Let \(L=\mathfrak n_4(k)\) be the six-dimensional Lie algebra of strictly upper-triangular four-by-four matrices over a finite field \(k=\mathbb F_q\), with bracket \([X,Y]=XY-YX\). Write \(C_L(X)=\{Y\in L:[X,Y]=0\}\). The following table is the **complete census by abstract Lie-isomorphism type**. In the final column all unspecified multiplicities are valid for every characteristic.

| Lie isomorphism type of \(C_L(X)\) | Dimension | Number of \(X\) |
| --- | --- | --- |
| \(L\) | 6 | \(q\) |
| \(\mathfrak s_5\) | 5 | \(q(q^2-1)\) if \(q\) even; \(2q(q-1)\) if \(q\) odd |
| \(\mathfrak f_4\oplus k\) | 5 | \(0\) if \(q\) even; \(q(q-1)^2\) if \(q\) odd |
| \(\mathfrak h_3\oplus k\) | 4 | \(q^3(q^2-1)\) |
| abelian \(k^4\) | 4 | \(q^3(q-1)\) |
| abelian \(k^3\) | 3 | \(q^3(q-1)(q^2-1)\) |

Here \(\mathfrak s_5\) has a basis \(t,u,v,z_1,z_2\) with only nonzero basis brackets \([t,u]=z_1\) and \([t,v]=z_2\). The algebra \(\mathfrak f_4\) has a basis \(t,u,w,z\) with only nonzero basis brackets \([t,u]=w\), \([t,w]=z\), and \(\mathfrak h_3\) has a basis \(u,v,z\) with only nonzero basis bracket \([u,v]=z\). All stated brackets are interpreted as alternating Lie brackets, including in characteristic two.

The characteristic-two phenomenon is stronger than a change in cardinality: the five-dimensional class-three centralizers disappear entirely and are replaced by two-step centralizers. Over odd characteristic, both five-dimensional isomorphism types occur **inside the same rank-one stratum** of \(\operatorname{ad}_X\), so centralizer dimension and adjoint Jordan type do not distinguish them.

## Assumptions and scope

The field \(k\) is any finite field, including nonprime finite fields and characteristic two. We count **elements** \(X\in L\), not conjugacy orbits or group centralizers. Isomorphism is as a Lie algebra over \(k\), not as an associative algebra, embedded subalgebra, or scheme. The dimension and bracket of the centralizer are the full Lie-algebra structure. No assertion is made about sizes of automorphism groups, or about \(\mathfrak n_n\) for \(n>4\).

Fix matrix units \(E_{ij}\) and write
\[
X=aE_{12}+bE_{13}+cE_{14}+dE_{23}+eE_{24}+fE_{34},\qquad
Y=A E_{12}+B E_{13}+C E_{14}+D E_{23}+E E_{24}+F E_{34}.
\]

## Proof

Multiplication of matrix units gives precisely three possibly nonzero bracket coordinates:
\[
[X,Y]_{13}=aD-dA,\qquad
[X,Y]_{24}=dF-fD,\qquad
[X,Y]_{14}=aE+bF-eA-fB.
\tag{1}
\]
We solve (1) and evaluate brackets *inside* its solution space, not merely its dimension.

**I. \(d\ne0\).** The first two equations imply \((A,D,F)=t(a,d,f)\). Subtracting \(tX\) from \(Y\), the residual has only the \(E_{13},E_{24},E_{14}\) coordinates and satisfies \(aE-fB=0\).

If \((a,f)\ne(0,0)\), this residual is exactly \(s(aE_{13}+fE_{24})+CE_{14}\), so
\[
C_L(X)=\operatorname{span}\{X,aE_{13}+fE_{24},E_{14}\}\cong k^3.
\]
The three generators commute. Counting \(d\ne0\), \((a,f)\ne(0,0)\) and the free \((b,c,e)\) gives \(q^3(q-1)(q^2-1)\).

If \((a,f)=(0,0)\), equation (1) forces \(A=F=0\) and leaves \(B,C,D,E\) arbitrary; their basis \(E_{13},E_{14},E_{23},E_{24}\) commutes pairwise, giving \(k^4\). This occurs \(q^3(q-1)\) times.

**II. \(d=0\), \((a,f)\ne(0,0)\).** The first two equations force \(D=0\); the third is a single nonzero equation in \(A,B,E,F\). The four-dimensional space
\[
V=\operatorname{span}\{E_{12},E_{13},E_{24},E_{34}\}
\]
has the nondegenerate alternating bracket form \(\Omega\), valued in \(kE_{14}\), defined by \([E_{12},E_{24}]=[E_{13},E_{34}]=E_{14}\). Hence \(C_L(X)/kE_{14}\) is the symplectic orthogonal hyperplane to the nonzero vector \(aE_{12}+bE_{13}+eE_{24}+fE_{34}\). The restricted alternating form has rank two and a one-dimensional radical over *every* field, including characteristic two. Thus \(C_L(X)\cong\mathfrak h_3\oplus k\). There are \(q^3(q^2-1)\) such elements (free \(b,c,e\)).

**III. \(d=a=f=0\).** If \(b=e=0\), the element is \(cE_{14}\) and is central in \(L\), so \(C_L(X)=L\); exactly \(q\) choices occur.

Otherwise \((b,e)\ne(0,0)\) and the last equation is \(bF=eA\). Every solution has a unique expression in the five-dimensional space
\[
C_L(X)=\operatorname{span}\{T,D_0,B_0,E_0,Z\},\quad
T=bE_{12}+eE_{34},\ D_0=E_{23},\ B_0=E_{13},\ E_0=E_{24},\ Z=E_{14}.
\]
The only possibly nonzero brackets among these generators are
\[
[T,D_0]=bB_0-eE_0=:W,\qquad
[T,B_0]=-eZ,\qquad
[T,E_0]=bZ,
\]
and hence \([T,W]=-2beZ\).

If \(2be=0\), the nonzero vector \(W\) spans the kernel of the functional \(sB_0+tE_0\mapsto(-es+bt)Z\). Choose \(V_0\in\operatorname{span}(B_0,E_0)\) with \([T,V_0]=Z\). Then \(T,D_0,V_0,W,Z\) is a basis, with only nonzero brackets \([T,D_0]=W\) and \([T,V_0]=Z\). This is \(\mathfrak s_5\).

If \(2be\ne0\), then \(W\) and \(U=bB_0+eE_0\) form a basis of \(\operatorname{span}(B_0,E_0)\) (determinant nonzero), and \([T,U]=0\). The basis \(T,D_0,W,Z,U\) has only nonzero brackets \([T,D_0]=W\), \([T,W]=-2beZ\), with \(U\) central. Rescale \(Z\) to obtain \(\mathfrak f_4\oplus k\).

In even characteristic \(2be=0\) always: all \(q(q^2-1)\) choices of \((b,e,c)\) yield \(\mathfrak s_5\). In odd characteristic \(2be=0\) precisely when exactly one of \(b,e\) is nonzero, giving \(2q(q-1)\) elements; both nonzero gives \(q(q-1)^2\) of type \(\mathfrak f_4\oplus k\).

**Exhaustiveness and separation.** The four coordinate regimes are disjoint and exhaustive. Their counts sum to
\[
q+q(q^2-1)+q^3(q^2-1)+q^3(q-1)+q^3(q-1)(q^2-1)=q^6.
\]
All displayed types are pairwise nonisomorphic when they co-occur. They have distinct dimensions except for the two five-dimensional types, whose lower-central nilpotency classes are respectively two and three, and the two four-dimensional types, which are respectively nonabelian and abelian. The proof uses no restriction beyond field axioms.

## Verification

The accompanying standalone `verify.py` independently solves the matrix for \(C_L(X)\) using exact Gaussian elimination, computes the derived subalgebra \([C_L(X),C_L(X)]\) and its next lower-central term \([C_L(X),[C_L(X),C_L(X)]]\), and identifies each type using the triple of dimensions. It exhaustively checks every element over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\). The triples, respectively, are \((6,3,1)\), \((5,2,0)\), \((5,2,1)\), \((4,1,0)\), \((4,0,0)\), and \((3,0,0)\). Each observed multiplicity matches the formula. These finite experiments verify examples but do not replace the all-field classification proof.

## Relationship to prior work

Goodwin and Röhrle, arXiv:1209.1289v1, §3.3, explicitly list the 16 Borel-orbit representatives in the type-\(A_3\) nilradical and prove a geometric two-component result for its commuting variety, in characteristic zero. They work with centralizer dimensions and Borel orbit geometry, not an abstract-isomorphism-type census with exact counts over every finite field. The orbit representatives can be used as a starting point for such a calculation, but neither the all-characteristic multiplicities nor the characteristic-two collapse are stated.

Soffer, arXiv:1411.5389v1, analyzes conjugacy-class counts in unitriangular groups, using centralizer dimensions and recursions. Such cardinality data do not determine the Lie-isomorphism types in this table. Indeed, in odd characteristic the two nonisomorphic five-dimensional centralizers arise for elements with the same \(\operatorname{rank}(\operatorname{ad}_X)=1\) and the same \(\operatorname{ad}_X^2=0\).

Bhunia, arXiv:1901.07869v1, studies **conjugacy classes of group centralizers** (z-classes) in the invertible triangular group and gives the finite-orbit boundary; this differs from the abstract Lie-isomorphism census inside the strictly triangular **Lie** algebra, and provides no characteristic-two count of the six listed possibilities. The proof above is independent of these orbit classifications.

## Limitations

No absolute claim of publication priority is possible from bounded literature and record searches; a specialized classification could overlap. The result does not classify conjugacy orbits of centralizers, nor centralizers inside the full upper-triangular algebra or the full \(\mathfrak{gl}_4\). Finite checks are restricted to fields of orders 2, 3, 4, and 5, while the proof covers every finite field. Independent audit and independent validation have not been performed.

## References

1. S. M. Goodwin and G. Röhrle, *On commuting varieties of nilradicals of Borel subalgebras of reductive Lie algebras*, arXiv:1209.1289v1, first publicly available 2012-09-06, §3.3. The preprint specifies primary MSC 20G15.
2. A. Soffer, *Upper bounds on the number of conjugacy classes in unitriangular groups*, arXiv:1411.5389v1, first publicly available 2014-11-19, §§2–4.
3. S. Bhunia, *Conjugacy classes of centralizers in the group of upper triangular matrices*, arXiv:1901.07869v1, first publicly available 2019-01-23, §3.
