# Retraction orbits and finite-field rank spectra of free two-step nilpotent Lie algebras

## Finding
Let \(K\) be any field and \(n\ge2\). For an \(n\)-dimensional \(K\)-vector space \(V\), let
\[
L_n(K)=V\oplus\bigwedge^2 V,\qquad [v+z,w+z']=v\wedge w.
\]
An **endomorphism retraction** is a Lie algebra endomorphism \(F:L_n(K)\to L_n(K)\) with \(F^2=F\) under composition. Every such \(F\) is conjugate by a Lie algebra automorphism to exactly one of the \(n+1\) normal forms \(F_r\), \(0\le r\le n\), induced by the linear projection \(T_r\) onto the first \(r\) basis vectors of \(V\), with zero central shear. The image of \(F_r\) is isomorphic to the free two-step nilpotent Lie algebra \(L_r(K)\), with \(L_0(K)=0\) and \(L_1(K)\) one-dimensional abelian. The ordinary linear rank of every member of this conjugacy class is \(\binom{r+1}{2}\).

For every finite field \(K=\mathbb F_q\), write \({n\brack r}_q\) for the Gaussian coefficient, with \({n\brack0}_q=1\). The full rank enumerator of **labeled** endomorphism retractions is
\[
\boxed{\quad\mathcal R_{n,q}(X)=\sum_{r=0}^{n}{n\brack r}_q\,q^{\frac{r(n-r)(n+2r)}2}\,X^{\binom{r+1}{2}}.\quad}
\]
Thus the exact size of the conjugacy class indexed by \(r\) is \({n\brack r}_q q^{r(n-r)(n+2r)/2}\); no other ranks occur. This formula holds for every prime power \(q\), including characteristic two.

In particular, \(\mathcal R_{2,2}(X)=1+12X+X^3\), \(\mathcal R_{2,3}(X)=1+36X+X^3\), and \(\mathcal R_{3,2}(X)=1+224X+896X^3+X^6\).

## Assumptions and scope
The bracket is the alternating exterior product and is a Lie bracket in all characteristics. An endomorphism is \(K\)-linear and bracket preserving. Conjugation is by the full group of \(K\)-linear Lie automorphisms, not merely by linear changes of the first-degree generators. The symbol \({n\brack r}_q\) denotes the number of \(r\)-dimensional subspaces of \(\mathbb F_q^n\), explicitly
\[
{n\brack r}_q=\prod_{j=0}^{r-1}\frac{q^{n-j}-1}{q^{r-j}-1}.
\]
Exponents are nonnegative integers, including at the boundaries \(r=0,n\). No assertions are made about higher nilpotency classes, non-free quotients, or endomorphism rings of groups.

## Proof
**1. All endomorphisms.** Every linear Lie endomorphism \(F\) is uniquely determined by its restriction to \(V\), which decomposes as \(v\mapsto Tv+\phi(v)\) for a linear map \(T:V\to V\) and a linear map \(\phi:V\to\bigwedge^2 V\). Indeed, \(\bigwedge^2 V=[L_n,L_n]\) is spanned by brackets and is preserved by any endomorphism; on a bracket \(v\wedge w\) the homomorphism equation gives \(F(v\wedge w)=Tv\wedge Tw\). Conversely any pair \((T,\phi)\) defines an endomorphism by
\[
F(v+z)=Tv+\phi(v)+(\bigwedge^2 T)(z).
\]
Put \(P=\bigwedge^2 T\). The equation \(F^2=F\) is therefore exactly
\[
T^2=T,\qquad \phi T+P\phi=\phi.
\]
The third block equation \(P^2=P\) follows automatically from \(T^2=T\).

**2. Classification of the central shear.** For an idempotent \(T\) of rank \(r\), set \(U=\operatorname{im}T\) and \(W=\ker T\), with \(w=n-r\). Thus \(V=U\oplus W\). We have the direct decomposition
\[
\bigwedge^2 V=(\bigwedge^2 U)\oplus(U\wedge W)\oplus(\bigwedge^2 W),
\]
and \(P\) is projection onto \(\bigwedge^2U\) along the last two summands. The equation on \(\phi\) means precisely
\[
\phi(U)\subseteq (U\wedge W)\oplus\bigwedge^2W,
\qquad \phi(W)\subseteq\bigwedge^2U.
\]
Both inclusions are necessary and sufficient; no further restrictions exist. For fixed \(T\), their parameter-space dimension is
\[
d_\phi=r\left(rw+\binom w2\right)+w\binom r2.
\]

**3. Conjugacy.** Any two projections \(T\) on \(V\) of the same rank are conjugate in \(\operatorname{GL}(V)\). Such a change of generators extends to an automorphism of \(L_n\). For a fixed \(T\), every linear \(\psi:V\to\bigwedge^2V\) defines the shear automorphism \(G_\psi(v+z)=v+\psi(v)+z\). Let \(F_T\) denote the endomorphism with generator map \(T\) and zero central shear. A direct calculation on generators gives
\[
G_\psi F_T G_\psi^{-1}(v)=Tv+(\psi T-P\psi)(v).
\]
Given an allowed \(\phi\) from Step 2, take \(\psi|_U=\phi|_U\) and \(\psi|_W=-\phi|_W\). Then \(\psi T-P\psi=\phi\). Hence every retraction with linear part \(T\) is conjugate to \(F_T\), and all rank-\(r\) retractions are conjugate. Conversely \(r\) is the rank of the induced projection on the characteristic abelianization \(L_n/[L_n,L_n]\cong V\); it cannot change under conjugation. This gives exactly \(n+1\) classes.

**4. Ranks.** The image of \(F\) projects onto \(U\) and its intersection with the commutator ideal is \(\bigwedge^2U\). The latter equality follows because \(F(V)\) projects injectively onto \(U\), while \(F(\bigwedge^2V)=\bigwedge^2U\). Thus
\[
\operatorname{rank}F=r+\binom r2=\binom{r+1}{2}.
\]
The bracket structure of the image agrees with \(U\oplus\bigwedge^2U\), proving that it is \(L_r(K)\).

**5. Counting.** Over \(\mathbb F_q\), there are \({n\brack r}_q\) choices for the image \(U\) of a rank-\(r\) projection, and exactly \(q^{rw}\) complementary subspaces \(W\) to a fixed \(U\). Step 2 then gives \(q^{d_\phi}\) central shears for each \(T\). The total exponent simplifies by the identity
\[
rw+r\left(rw+\binom w2\right)+w\binom r2=\frac{rw(n+2r)}2.
\]
Distinct pairs \((T,\phi)\) give distinct endomorphisms, completing the formula and each orbit size. The identity is integral because \(rw(n+2r)\) is even for every integer \(n,r\) with \(0\le r\le n\).

## Verification
The standalone script `verify.py` directly enumerates generator maps over prime fields, extends them to the full block matrices of Lie endomorphisms, checks \(F^2=F\) by matrix multiplication, checks the exterior-product bracket on every generator pair, computes ordinary ranks by modular elimination, and compares rank-by-rank with the derived polynomial. It exhausts all \(64\) generator maps at \((n,q)=(2,2)\), all \(729\) at \((2,3)\), and all \(262144\) at \((3,2)\), with output `VERIFY_OK`. These checks are finite examples; the proof above is valid for arbitrary \(n\) and all fields.

As a separate algebraic consistency check, \(\operatorname{Aut}(L_n)\) has order \(|\operatorname{GL}_n(\mathbb F_q)|q^{n\binom n2}\). The stabilizer of the standard rank-\(r\) retraction consists of block-diagonal generator changes \(\operatorname{GL}_r\times\operatorname{GL}_{n-r}\) and those shears \(\psi\) for which \(\psi T=P\psi\); it has order \(|\operatorname{GL}_r(\mathbb F_q)|\,|\operatorname{GL}_{n-r}(\mathbb F_q)|q^{r\binom r2+(n-r)(\binom n2-\binom r2)}\). The quotient agrees with the coefficient in Step 5.

## Relationship to prior work
Benito and Roldán-López, arXiv:1911.01897v1 (November 5, 2019), Proposition 1 and Remark 2, give the universal homomorphism and automorphism parameterizations of free nilpotent Lie algebras, assuming characteristic zero. Their parameterization motivates Step 1, and its content is explicitly acknowledged as known. The present result imposes the nonlinear idempotence condition, isolates the shear-space dimensions, proves the single-orbit theorem for each generator rank, and determines exact labeled finite-field rank multiplicities in all characteristics. No claim of novelty is made for the universal mapping property itself.

Cagliero, Gutiérrez Frez, and Szechtman (arXiv:1703.06214) study uniserial representations of a semidirect extension of the same free two-step Lie algebra. Cagliero and Rojas (arXiv:2006.04676) compute minimal faithful representation dimensions. Neither problem is a census of idempotent endomorphisms. Mikhalev and Yu (1997) study retracts of unrestricted free Lie algebras, making retractions a classical topic, but the accessible abstract does not supply the class-two finite-field rank polynomial.

## Limitations
This is a labeled point count and a classification under Lie algebra automorphisms. It does not enumerate arbitrary subalgebra embeddings, all endomorphisms by rank, or retracts of nonfree nilpotent quotients. The computational checks do not establish the unrestricted theorem. Literature comparison is not a proof of absolute novelty: equivalent enumerative results may appear under alternate language such as split idempotents or retract-counting, and the full 1997 retract article was not accessible in this inspection.

## References
1. P. Benito and J. Roldán-López, *Derivations and automorphisms of free nilpotent Lie algebras and their quotients*, arXiv:1911.01897v1 (2019-11-05), full text https://arxiv.org/html/1911.01897v2 , Proposition 1 and Remark 2.
2. L. Cagliero, L. Gutiérrez Frez, and F. Szechtman, *Free 2-step nilpotent Lie algebras and indecomposable representations*, arXiv:1703.06214v1 (2017-03-17), https://arxiv.org/html/1703.06214v1 .
3. L. Cagliero and N. Rojas, *Minimal faithful representations of the free 2-step nilpotent Lie algebra of rank \(r\)*, arXiv:2006.04676v1 (2020-06-08), https://arxiv.org/html/2006.04676v1 .
4. A. A. Mikhalev and J.-T. Yu, *Test elements and retracts of free Lie algebras*, Comm. Algebra 25 (1997), 3283–3289, DOI:10.1080/00927879708826054 (abstract accessed; publisher full text not accessed).
