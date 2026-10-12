# Exact Frobenius degree of every additive map on a split finite algebra

## Finding
Let \(p\) be a prime and let
\[
A=\mathbb F_p^r
\]
with coordinate idempotents \(e_1,\ldots,e_r\). Every additive map \(f:A\to\mathbb F_p\) has a unique expression
\[
f(x_1,\ldots,x_r)=\sum_{i=1}^r c_i x_i,
\]
because additivity is automatically \(\mathbb F_p\)-linearity. For each coefficient \(c_i\), let \(a_i\in\{0,1,\ldots,p-1\}\) denote its standard integer representative, and set
\[
w(f)=\sum_{i=1}^r a_i.
\]
Using the normalization-free notion of Frobenius \(n\)-homomorphism in Grinberg's 2026 paper, the exact classification is
\[
f\text{ is an }n\text{-homomorphism}\quad\Longleftrightarrow\quad n\ge w(f).
\]
Thus the least Frobenius degree of \(f\) is exactly \(w(f)\). In particular, every additive map \(A\to\mathbb F_p\) has finite Frobenius degree, the maximum possible least degree is \(r(p-1)\), and the number of maps of exact least degree \(d\) is
\[
[t^d](1+t+\cdots+t^{p-1})^r.
\]
The maximal degree \(r(p-1)\) is attained only by the functional with every coefficient equal to \(-1\).

## Assumptions and scope
The source notion is the following. For a ring \(A\), a commutative ring \(B\), and a central \(\mathbb Z\)-linear map \(f:A\to B\), its \(m\)-Frobenius map is
\[
f_m(a_1,\ldots,a_m)=\sum_{\sigma\in S_m}\operatorname{sgn}(\sigma)
\prod_{C=(i_1,\ldots,i_k)\text{ cycle of }\sigma}f(a_{i_1}\cdots a_{i_k}).
\]
Grinberg calls \(f\) an \(n\)-homomorphism when \(f_{n+1}=0\) identically, without imposing the older normalization \(f(1)=n\). The present theorem concerns exactly this generalized definition and the split algebra \(\mathbb F_p^r\). It does not assert the same classification for determinant-law pseudocharacters or for arbitrary finite-dimensional \(\mathbb F_p\)-algebras.

## Proof
Write \(c_i=f(e_i)\). Fix \(m\ge1\) and a tuple of coordinate idempotents
\[
(e_{i_1},\ldots,e_{i_m}).
\]
For \(1\le j\le r\), let \(n_j\) be the number of occurrences of \(e_j\) in the tuple, so that \(n_1+\cdots+n_r=m\).

In the explicit permutation formula for \(f_m\), a cycle contributes zero unless all idempotents indexed by that cycle are equal, because distinct coordinate idempotents multiply to zero. Hence only permutations that preserve each label class contribute. Such permutations form the direct product \(S_{n_1}\times\cdots\times S_{n_r}\), and the sum factorizes as
\[
f_m(e_{i_1},\ldots,e_{i_m})
=
\prod_{j=1}^r
\left(\sum_{\sigma\in S_{n_j}}\operatorname{sgn}(\sigma)c_j^{\#\operatorname{cycles}(\sigma)}\right).
\]
The standard signed cycle-index identity gives
\[
\sum_{\sigma\in S_s}\operatorname{sgn}(\sigma)c^{\#\operatorname{cycles}(\sigma)}
=c(c-1)\cdots(c-s+1).
\]
This identity is integral, so it remains valid after reduction modulo \(p\). Therefore
\[
f_m(e_{i_1},\ldots,e_{i_m})
=
\prod_{j=1}^r(c_j)_{n_j},
\]
where \((c)_s=c(c-1)\cdots(c-s+1)\) and \((c)_0=1\).

If \(a_j\in\{0,\ldots,p-1\}\) represents \(c_j\), then in \(\mathbb F_p\)
\[
(c_j)_s\ne0\quad\Longleftrightarrow\quad s\le a_j.
\]
Consequently a basis value of \(f_m\) is nonzero exactly when every multiplicity satisfies \(n_j\le a_j\). Such nonnegative multiplicities with total \(m\) exist exactly when
\[
m\le a_1+\cdots+a_r=w(f).
\]
Since \(f_m\) is multilinear and the \(e_j\) form a basis, this proves
\[
f_m\ne0\quad\Longleftrightarrow\quad 1\le m\le w(f),
\]
while \(f_m=0\) for every \(m>w(f)\). By definition, \(f\) is an \(n\)-homomorphism exactly when \(f_{n+1}=0\), which is equivalent to \(n\ge w(f)\).

Finally, coefficient vectors \((c_1,\ldots,c_r)\in\mathbb F_p^r\) are in bijection with integer vectors \((a_1,\ldots,a_r)\in\{0,\ldots,p-1\}^r\). Hence the number of maps of exact degree \(d\) is the coefficient of \(t^d\) in \((1+t+\cdots+t^{p-1})^r\).

## Verification
The proof determines every Frobenius map on basis tuples, so no finite experiment is needed for the infinite statement. Two boundary checks are built into the formula. For one coordinate, a scalar multiple \(c\,\mathrm{id}\) has least degree equal to the standard representative of \(c\); in particular every scalar multiple has degree at most \(p-1\). For the zero functional, all \(a_i\) vanish and the least degree is \(0\), agreeing with Grinberg's statement that the zero map is the unique \(0\)-homomorphism.

A direct small-case permutation expansion was also used as a regression check for primes \(2,3,5\), ranks up to \(3\), and Frobenius orders up to \(5\). It agreed with the symbolic basis formula in every tested case. This finite check is not used as proof.

## Relationship to prior work
Grinberg's 2026 paper extends Frobenius \(n\)-homomorphisms to arbitrary source rings and arbitrary commutative target rings, explicitly noting that much of the pseudocharacter literature assumes a \(\mathbb Q\)-algebra or invertibility of \(n!\). His main sum theorem gives upper bounds when a map is expressed as a sum of lower-degree maps, but the paper does not state the exact finite-characteristic degree profile above; searches of the full text found no discussion under “characteristic”, “scalar”, or \(f(1)\).

The classical Buchstaber--Rees definition imposes \(f(1)=n\) in addition to the vanishing of the next Frobenius map. Their 2008 paper proves the useful identity
\[
\Phi_{n+1}(f)(a,1,\ldots,1)=f(a)(f(1)-1)\cdots(f(1)-n),
\]
and works with commutative complex algebras. That normalization and characteristic-zero setting exclude the finite-characteristic collapse classified here. The present result instead exploits the normalization-free 2026 definition and resolves all additive maps on the basic split algebra.

## Limitations
The theorem is specific to the normalization-free generalized Frobenius maps and to \(\mathbb F_p^r\to\mathbb F_p\). It does not classify maps to larger coefficient rings, nonsplit semisimple algebras, nonsemisimple algebras, or determinant-law pseudocharacters. Although targeted searches found no equivalent exact weight classification, older small-characteristic Taylor-pseudocharacter literature may contain an equivalent statement under different terminology; this remains the principal originality risk.

## References
1. Darij Grinberg, *Compositions of \(n\)-homomorphisms*, arXiv:2604.13619v1, first submitted 15 April 2026; Definition 0.1, Theorems 0.3--0.4, and Remark 0.5.
2. V. M. Buchstaber and E. G. Rees, *Frobenius \(n\)-homomorphisms, transfers and branched coverings*, Math. Proc. Cambridge Philos. Soc. 144 (2008), 1--12, doi:10.1017/S0305004107000539; Definition 2.1 and Lemma 2.1.
3. H. M. Khudaverdian and Th. Th. Voronov, *On the Buchstaber--Rees theory of “Frobenius \(n\)-homomorphisms” and its generalization*, arXiv:2002.02395.
