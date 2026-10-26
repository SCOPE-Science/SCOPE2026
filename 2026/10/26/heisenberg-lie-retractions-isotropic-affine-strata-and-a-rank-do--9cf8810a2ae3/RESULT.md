# Heisenberg Lie retractions: isotropic affine strata and a rank-dominance transition

## Finding

Let \(k\) be any field, let \(n\geq1\), and let \(H_n=V\oplus kz\) be the \((2n+1)\)-dimensional Heisenberg Lie algebra associated to a nondegenerate alternating form \(\omega\) on \(V\), with \([u+az,v+bz]=\omega(u,v)z\). Let \(\mathscr I_n\) denote the affine scheme of \(k\)-linear Lie algebra endomorphisms \(F:H_n\to H_n\) satisfying \(F^2=F\).

**Theorem.** Over every field and in every characteristic, \(\mathscr I_n\) is a disjoint union of \(n+2\) smooth, geometrically irreducible, open-and-closed components: the identity point and \(X_{n,r}\) for \(0\leq r\leq n\). Every \(F\in X_{n,r}\) has image dimension \(r\), annihilates \(z\), and has abelian image. There is a Zariski-locally trivial affine-space bundle
\[
X_{n,r}\longrightarrow \operatorname{IGr}(r,V,\omega),\qquad
\text{fiber }\mathbb A^{r(2n-r+1)},
\]
where \(\operatorname{IGr}\) parametrizes totally isotropic \(r\)-planes. Its dimension is
\[
d_{n,r}=\frac{8nr-5r^2+3r}{2}.
\]
In particular, there are no proper retractions onto nonabelian Lie subalgebras. Their possible ranks are precisely \(0,1,\ldots,n\), whereas the identity has rank \(2n+1\).

For every finite field \(\mathbb F_q\), the exact number of rank-\(r\) proper Lie retractions is
\[
N_{n,r}(q)=q^{r(2n-r+1)}{n\brack r}_q
\prod_{i=0}^{r-1}(q^{n-i}+1),\qquad 0\leq r\leq n,
\]
where \({n\brack r}_q=\prod_{i=0}^{r-1}(q^{n-i}-1)/(q^{r-i}-1)\). Thus the total number of idempotent Lie endomorphisms is \(1+\sum_{r=0}^n N_{n,r}(q)\); the extra \(1\) is the identity.

The maximum-dimensional proper-retraction components occur exactly at integral ranks satisfying
\[
0\leq r\leq n,\qquad \frac{4n-1}{5}\leq r\leq\frac{4n+4}{5}.
\]
For \(1\leq n\leq3\), the unique maximum is the largest possible proper rank \(n\). At \(n=4\), ranks \(3\) and \(4\) tie. For every \(n\geq5\), the largest possible proper rank \(n\) is **not** of maximal dimension; the dominant rank is approximately \(4n/5\). In the limit \(q\to\infty\) with \(n\) fixed, the uniformly sampled proper retractions concentrate on the listed maximal-dimensional rank strata, equally between the two ranks in a tie.

## Assumptions and scope

A Lie endomorphism is a \(k\)-linear map preserving the bracket. Its idempotence refers to composition, not to a product of Lie-algebra elements. The scheme \(\mathscr I_n\) is defined by the polynomial bracket-preservation and composition equations on the affine space of all \((2n+1)\)-square matrices. The classification includes characteristic two, because the form is alternating and nondegenerate there as well. Rank is the dimension of the image of the linear map, and rank strata are taken in this scheme.

## Proof

**1. Matrix reduction.** Because \(z=[x_1,y_1]\) for any symplectic basis, bracket preservation forces \(F(z)=cz\) even over an arbitrary commutative coefficient algebra. Hence every Lie endomorphism has a unique expression
\[
F(v+tz)=Av+(\ell(v)+ct)z,
\quad A\in\operatorname{End}(V),\ \ell\in V^*,\ c\in k.
\]
Preservation of \([v,w]=\omega(v,w)z\) is equivalent to
\[
\omega(Av,Aw)=c\omega(v,w)\quad\text{for every }v,w\in V.
\]
In a symplectic basis this is \(A^TJA=cJ\). Idempotence is equivalent to
\[
A^2=A,\qquad c^2=c,\qquad \ell A+c\ell=\ell.
\]

**2. The identity component and proper retracts.** Since \(c^2=c\), the endomorphism scheme splits into the open-and-closed loci \(c=0\) and \(c=1\). On \(c=1\), \(A\) preserves a nondegenerate symplectic form and is invertible. Idempotence then gives \(A=I\), and the last equation gives \(\ell=0\): this is the single identity point, scheme-theoretically. On \(c=0\), \(A\) is a projection, \(U=\operatorname{im}A\) is totally isotropic (by the bracket equation), and \(\ell A=\ell\). Conversely, any isotropic subspace \(U\), any complementary subspace \(K\) with \(V=U\oplus K\), and any \(\lambda\in U^*\) determine exactly one such retraction by
\[
F(u+w+tz)=u+\lambda(u)z\quad(u\in U,\ w\in K).
\]
Its image is the graph of \(\lambda:U\to kz\), which is abelian of dimension \(\dim U\leq n\). This establishes both necessity and sufficiency.

**3. Geometry and components.** For any fixed \(U\in\operatorname{IGr}(r,V)\), the complements to \(U\) form the affine space of splittings of \(0\to U\to V\to V/U\to0\), a torsor under \(\operatorname{Hom}(V/U,U)\) of dimension \(r(2n-r)\). The choice of \(\lambda\in U^*\) contributes another \(r\) affine dimensions. These parameters vary Zariski-locally trivially with \(U\), proving the affine-bundle assertion.

The symplectic isotropic Grassmannian is smooth and geometrically irreducible of dimension \(r(2n-r)-\binom r2\). For example, the ordinary Grassmannian has tangent space \(\operatorname{Hom}(U,V/U)\), and the linearized isotropy constraints map surjectively onto \(\bigwedge^2 U^*\), giving codimension \(\binom r2\) in every characteristic. Thus \(X_{n,r}\) is smooth and geometrically irreducible with dimension
\[
r(2n-r)-\binom r2+r(2n-r+1)=\frac{8nr-5r^2+3r}{2}.
\]
In a family of idempotent matrices the image is locally a direct summand of constant rank, so the rank strata are open and closed; the classification above is valid scheme-theoretically. Therefore these strata, together with the identity point, are precisely the irreducible components.

**4. Finite fields.** Over \(\mathbb F_q\), an ordered isotropic independent \(r\)-tuple can be chosen in
\[
\prod_{i=0}^{r-1}(q^{2n-i}-q^i)
\]
ways: after \(i\) choices, the next vector lies in the \((2n-i)\)-dimensional orthogonal complement but outside the existing \(i\)-space. Dividing by the number \(\prod_{i=0}^{r-1}(q^r-q^i)\) of ordered bases of a given \(r\)-space gives
\[
\#\operatorname{IGr}(r,V)(\mathbb F_q)
={n\brack r}_q\prod_{i=0}^{r-1}(q^{n-i}+1).
\]
Each such isotropic image admits \(q^{r(2n-r)}\) complements and \(q^r\) functionals \(\lambda\), producing the asserted formula for \(N_{n,r}(q)\). Its leading coefficient as a polynomial in \(q\) is \(1\), and its degree is \(d_{n,r}\).

**5. Rank-dominance transition.** Direct subtraction gives
\[
d_{n,r}-d_{n,r-1}=4n-5r+4.
\]
Since these differences strictly decrease with \(r\), the maximal dimensions occur exactly at the stated integer ranks. Every \(N_{n,r}(q)\) is a monic polynomial of degree \(d_{n,r}\), which proves the asymptotic concentration and equal proportions in a tie.

## Verification

Run `python3 verify.py` using the accompanying standalone source. Exhaustive tests of the endomorphism and idempotence equations for the three-dimensional algebra over \(\mathbb F_2,\mathbb F_3,\mathbb F_5\) give rank profiles respectively \((1,12,1)\), \((1,36,1)\), and \((1,150,1)\), listing ranks \(0,1,3\). Exhaustive enumeration of the \(2^{16}\) projected \(4\times4\) binary matrices, with algebraic counting of admissible functionals, gives the five-dimensional proper-retraction rank profile \((1,240,960)\), for ranks \(0,1,2\). The checker separately tests the dimension finite-difference identity for \(1\leq n<30\). Successful execution prints `HEISENBERG_RETRACTIONS_OK`.

These finite tests are sanity checks. The infinite-field, all-dimension, scheme-theoretic statements follow from the proof, not from the enumeration.

## Relationship to prior work

Fisher, Gray and Hydon [1] classify automorphisms of low-dimensional real Lie algebras and discuss normal idempotent projections arising from ideal direct sums. Their setting does not classify arbitrary (usually non-normal) Lie retractions: the image of a proper nonzero Heisenberg retraction is typically a nonideal abelian subalgebra. Bergman and Nahlus [2, §11.1] study almost-direct decompositions and commuting projections related to ideals, rather than isotropic-image retractions or their rank-counting geometry. Facchini and Heidari Zadeh [3] investigate idempotent endomorphisms through unital algebra splittings and bilinear-form categories, not the rank-stratified nonunital Heisenberg Lie endomorphism scheme. The isotropic Grassmannian and its finite-field subspace counts are classical; the specific retraction-to-isotropic-affine-bundle identification and rank-dominance transition constitute the present observation.

## Limitations

Only idempotent Lie algebra **homomorphisms** of the standard Heisenberg Lie algebra are classified, not arbitrary linear idempotents, idempotent derivations, group homomorphisms, or generalized two-step nilpotent algebras. The formula counts embedded retractions, not isomorphism classes of image subalgebras. The asymptotic assertion fixes \(n\) and lets the finite-field size grow; it does not assert dominance for every small finite field. The published-literature search does not establish absolute priority, and no independent mathematical validation is claimed.

## References

1. David J. Fisher, Robert J. Gray and Peter E. Hydon, *Automorphisms of real Lie algebras of dimension five or less*, arXiv:1303.3376 (first posted 2013-03-14), https://arxiv.org/abs/1303.3376.
2. George M. Bergman and Nazih Nahlus, *Homomorphisms on infinite direct product algebras, especially Lie algebras*, arXiv:0910.5181 (first posted 2009-10-27), https://arxiv.org/abs/0910.5181.
3. Alberto Facchini and Leila Heidari Zadeh, *Algebras with a bilinear form, and Idempotent endomorphisms*, arXiv:2210.08230 (first posted 2022-10-15), https://arxiv.org/abs/2210.08230.
