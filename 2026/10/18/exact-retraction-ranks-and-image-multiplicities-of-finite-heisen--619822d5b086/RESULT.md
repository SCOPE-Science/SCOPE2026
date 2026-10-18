# Exact retraction ranks and image multiplicities of finite Heisenberg Lie algebras

## Finding

For every prime power \(q\) and integer \(n\ge1\), the complete rank enumerator of composition-idempotent \(\mathbb F_q\)-linear Lie endomorphisms of the Heisenberg algebra \(H_n(q)\) is
\[
P_{n,q}(X)=X^{2n+1}+\sum_{r=0}^{n}I_{n,r}(q)q^{r(2n-r+1)}X^r,
\qquad I_{n,r}(q)=\prod_{i=0}^{r-1}\frac{q^{2n-2i}-1}{q^{r-i}-1}.
\]
The empty product gives \(I_{n,0}(q)=1\). Thus exactly the ranks \(0,1,\ldots,n,2n+1\) occur. Every proper retraction has abelian image disjoint from the nonzero derived center; in particular no retraction has rank strictly between \(n\) and \(2n+1\).

For each \(0\le r\le n\), the proper rank-\(r\) images are the graphs \(\Gamma_\eta(U)=\{u+\eta(u)z:u\in U\}\) with \(U\) totally isotropic of dimension \(r\) and \(\eta\in U^*\). There are exactly \(I_{n,r}(q)q^r\) such images. A **particular specified graph** supports exactly \(q^{r(2n-r)}\) retractions. The whole algebra is the remaining retract image, supporting only the identity.

For illustration,
\[
P_{1,2}(X)=1+12X+X^3,\qquad
P_{2,2}(X)=1+240X+960X^2+X^5.
\]
Here rank means vector-space dimension, not cardinality (the latter is \(q^{\operatorname{rank}F}\)).

## Assumptions and scope

Let \(V\) be a \(2n\)-dimensional vector space over \(\mathbb F_q\) endowed with a fixed nondegenerate alternating bilinear form \(\omega\). Let \(H=V\oplus\mathbb F_qz\) with Lie bracket
\[
[v+az,w+bz]=\omega(v,w)z.
\]
The center and derived algebra are both \(\mathbb F_qz\). An endomorphism is an \(\mathbb F_q\)-linear map preserving this bracket. A retraction means a composition-idempotent Lie endomorphism \(F\circ F=F\), not an element \(x\in H\) with an algebraic idempotence condition. The zero homomorphism and the identity are included. All prime powers, including characteristic two, are allowed. A subspace is *totally isotropic* when \(\omega\) vanishes on all of its pairs. The known symplectic count \(I_{n,r}(q)\) is background input, not itself asserted as new.

## Proof

**1. General Lie endomorphism normal form.** Since \([H,H]=\mathbb F_qz\), every Lie endomorphism satisfies \(F(z)=\lambda z\) for some \(\lambda\in\mathbb F_q\). Thus unique \(A\in\operatorname{End}_{\mathbb F_q}(V)\) and \(c\in V^*\) satisfy
\[
F(v+tz)=Av+(c(v)+\lambda t)z.
\]
Bracket preservation is equivalent to
\[
\omega(Av,Aw)=\lambda\omega(v,w)\quad\text{for all }v,w\in V.
\]
Composition-idempotence is equivalent to the simultaneous conditions
\[
A^2=A,\qquad \lambda^2=\lambda,\qquad c\circ A+\lambda c=c.
\]
Because the coefficient field has no nontrivial idempotent scalar, \(\lambda\in\{0,1\}\).

**2. Center-preserving branch.** If \(\lambda=1\), nondegeneracy of \(\omega\) implies \(A\) is injective, hence invertible. An invertible idempotent is \(A=1_V\), and the last displayed relation then gives \(c=0\). Hence \(F=1_H\). In particular the only retraction with nonzero restriction to the center is the identity.

**3. Proper branch.** If \(\lambda=0\), the bracket condition becomes \(\omega(Ax,Ay)=0\), so the image \(U=\operatorname{im}A\) is totally isotropic. Conversely, any projection \(A\) of \(V\) onto a totally isotropic subspace \(U\) and any linear functional \(c\) with \(c=c\circ A\) define a Lie retraction. The relation \(c=c\circ A\) is precisely that \(c=\eta\circ A\) for a unique \(\eta\in U^*\). Its image is exactly \(\Gamma_\eta(U)\), and it has rank \(\dim U=r\). Since a totally isotropic subspace has dimension at most \(n\), these are all possible proper ranks. Each \(0\le r\le n\) is realized by choosing an isotropic subspace of the desired dimension and a projection onto it. Their graphs meet \(\mathbb F_qz\) trivially and are abelian.

**4. Images and fibers.** For fixed \(r\), the number of totally isotropic \(r\)-subspaces of a \(2n\)-dimensional symplectic space is
\[
I_{n,r}(q)=\prod_{j=0}^{r-1}\frac{q^{2n-2j}-1}{q^{r-j}-1}.
\]
One elementary count: build an ordered isotropic basis successively; after a \(j\)-dimensional isotropic span has been selected, the next vector may be any vector in its perpendicular complement but not its span, giving \(q^{2n-j}-q^j\) choices. Divide the resulting product by the number \(\prod_{j=0}^{r-1}(q^r-q^j)\) of ordered bases of a fixed \(r\)-space, giving the product above. For each \(U\), there are \(q^r\) linear functionals \(\eta:U\to\mathbb F_q\) and their graphs are pairwise distinct. Thus there are \(I_{n,r}(q)q^r\) possible rank-\(r\) images.

A projection onto a fixed \(U\) is determined by a complementary subspace \(K\) with \(V=U\oplus K\): its kernel is \(K\). Relative to one fixed complement, every other complement is the graph of a unique linear map \(V/U\to U\). Therefore the number of such projections is \(q^{r(2n-r)}\). For a fixed graph \(\Gamma_\eta(U)\), each projection gives **exactly one** retraction \(F(v+tz)=Av+\eta(Av)z\), and different projections give different retractions. Multiplying the image count by this fiber count gives \(I_{n,r}(q)q^{r(2n-r+1)}\). Adding the identity proves the rank polynomial, sharp gaps, and specified-image multiplicity formula.

## Verification

The standalone script `artifacts/check_heisenberg.py` uses field arithmetic for \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5\), including a polynomial basis for \(\mathbb F_4\). It independently tests every candidate matrix in the parametrized form for dimensions \(2n=2\) with all four fields and \(2n=4\) with \(q=2\); it checks bracket preservation, idempotence, rank, and every predicted coefficient. Separately, for \(n=1\) and \(q=2,3,4\), it enumerates **all** \(3\times3\) matrices, without imposing the endomorphism normal form, and checks bracket preservation and idempotence directly. Finally, it enumerates actual reduced-row-echelon subspaces to confirm the isotropic-space formula at \((n,q)=(2,3)\) and \((3,2)\). The script prints `ALL_EXACT_CHECKS_PASSED`; direct enumeration verifies finite instances, while the proof above establishes the unbounded parameters.

## Relationship to prior work

Barrionuevo and Tirao [1] give the classical Heisenberg Lie-algebra presentation and study deformation and rigidity, not composition-idempotent finite-field endomorphisms. Liu and Tang [2] study *automorphism* groups of Heisenberg Lie (super)algebras, a different invertible portion of the endomorphism monoid. The classical isotropic-subspace count and characterization of abelian graph subalgebras are **not novel**: related explicit finite-field Lie-subalgebra counts are given in [3]. The present claim is instead that the only non-identity **Lie retractions** have those graphs as images, with exact per-image fiber sizes and the complete rank polynomial. Work on fixed-point-free **automorphisms** [4] does not imply these results: the only invertible idempotent endomorphism is the identity.

## Limitations

The theorem concerns only \(\mathbb F_q\)-linear Lie endomorphisms of ordinary, one-dimensional-center Heisenberg Lie algebras. It says nothing about nonlinear set maps, finite Heisenberg *group* endomorphisms, or generalized non-Heisenberg two-step nilpotent Lie algebras. It is not a classification of all Lie subalgebras; some contain the center and are not retraction images. The symplectic-space counting ingredient and the characterization of isotropic graph *subalgebras* occur in earlier literature, and are acknowledged rather than claimed as new. Unindexed endomorphism-semigroup literature may contain an equivalent retraction enumeration; this remains a residual originality risk. No independent mathematical audit has been performed.

## References

1. J. Barrionuevo and P. Tirao, *Deformations and rigidity in varieties of Lie algebras*, arXiv:2101.09670v1 (first public 2021-01-24), https://arxiv.org/abs/2101.09670 ; §5 gives Heisenberg definitions and deformation results.
2. L. Liu and L. Tang, *The automorphism groups of Heisenberg Lie (super)algebras*, Journal of Mathematics 38 (2018), 502–510, DOI:10.13548/J.SXZZ.20170518.003, https://sxzz.whu.edu.cn/html/2018/3/20180314.htm.
3. *Exact subalgebra commutativity degree of finite Heisenberg Lie algebras*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/9/18/SCOPE-heisenberg-subalgebra-commutativity-degree--e3fb5b5762fa ; its Section 1 explicitly counts isotropic graph subalgebras, not Lie retractions.
4. *Exact fixed-point-free automorphism count for the three-dimensional Heisenberg Lie algebra*, published mathematical research record, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-fixed-point-free-automorphism-count-for-the-three-dimensio--17f0de4cb789 ; concerns invertible automorphisms, not composition-idempotent endomorphisms.
