# Rational rotation obstructions and fixed-space spectra of weighted cyclic evolution algebras

## Finding
For an integer \(n\geq2\), a finite field \(k=\mathbb F_q\), and \(t\in k^\times\), let \(E_t\) be the commutative, generally nonassociative algebra with natural basis \(e_0,\ldots,e_{n-1}\), pairwise products \(e_i e_j=0\) for \(i\ne j\), and
\[
e_i^2=e_{i+1}\quad(0\leq i<n-1),\qquad e_{n-1}^2=t e_0.
\]
Every \(E_t\) is simple. Its rational automorphism group and the complete distribution of automorphism fixed-space dimensions are governed by explicit multiplicative power obstructions, including situations where a rational rotation exists but none of its lifts fixes a nonzero vector.

Put \(M=q-1\), \(N=2^n-1\), \(d=\gcd(M,N)\). For each \(s\in\{0,1,\ldots,n-1\}\), set
\[
g_s=\gcd(n,s),\quad H_s=\frac{2^n-1}{2^{g_s}-1},\quad J_s=\frac{2^s-1}{2^{g_s}-1},\quad b_s=\gcd(M,H_s).
\]
Here \(g_0=n\), \(H_0=1\), and \(J_0=0\). Let \(A_s\) and \(B_s\) be the integers
\[
A_s=\begin{cases}d,&t^{(2^s-1)M/d}=1,\\0,&\text{otherwise},\end{cases}
\qquad
B_s=\begin{cases}b_s,&t^{J_s M/b_s}=1,\\0,&\text{otherwise}.\end{cases}
\]
All exponents are integers, and the equalities are taken in \(k^\times\). Then \(0\leq B_s\leq A_s\) and the exact fixed-space enumerator is
\[
\boxed{P_{n,q,t}(T)=\sum_{\phi\in\operatorname{Aut}_k(E_t)}T^{\dim_k\ker(\phi-I)}
=\sum_{s=0}^{n-1}\left[(A_s-B_s)+B_sT^{g_s}\right].}
\]
Consequently, \(\lvert\operatorname{Aut}_k(E_t)\rvert=\sum_s A_s\). If \(t=\zeta^h\) for a primitive generator \(\zeta\) of \(k^\times\), define \(m=d/\gcd(d,h)\), with \(m=1\) when \(h=0\), and \(\operatorname{ord}_1(2)=1\). Then
\[
\boxed{\lvert\operatorname{Aut}_k(E_t)\rvert=d\frac{n}{\operatorname{ord}_{m}(2)}.}
\]
For each ordered tuple length \(r\geq1\), the number of automorphism orbits on \(E_t^r\) is exactly \(P_{n,q,t}(q^r)/\lvert\operatorname{Aut}_k(E_t)\rvert\). The action on \(E_t\setminus\{0\}\) is free if and only if \(B_s=0\) for every \(1\leq s<n\).

In particular, choose \(q=43\), \(n=6\), and \(t=37=3^7\) in \(\mathbb F_{43}\), where \(3\) has multiplicative order \(42\). Then
\[
\boxed{\lvert\operatorname{Aut}(E_{37})\rvert=63,\qquad P_{6,43,37}(T)=62+T^6.}
\]
The group is nonabelian, yet every nonidentity automorphism fixes **only the zero vector**. Thus a nonabelian group of order \(63\) acts freely on the \(43^6-1\) nonzero elements of this six-dimensional simple evolution algebra. The number of orbits on its underlying vector space is \(1+(43^6-1)/63=100339097\).

## Assumptions and scope
All statements concern ordinary \(k\)-linear algebra automorphisms and fixed \(k\)-vector subspaces, not automorphism group schemes or infinitesimal automorphisms. No restriction on the characteristic is imposed. Every algebra \(E_t\) is regular because the \(e_i^2\) form a basis, and simple because every nonzero ideal contains some \(e_{i+1}\) (multiply a nonzero vector with nonzero \(e_i\)-coordinate by \(e_i\)) and therefore contains the whole cyclic basis.

Every weighted directed cycle with nonzero edge weights \(\lambda_i\in k^\times\), i.e. \(e_i^2=\lambda_i e_{i+1\bmod n}\), is isomorphic over \(k\) to some \(E_t\): successive diagonal basis rescalings make the first \(n-1\) edge weights equal to one. For \(t,u\in k^\times\), the familiar monomial isomorphism criterion specializes to \(E_t\cong E_u\) exactly when there exists \(0\leq s<n\) for which \(t/u^{2^s}\) is an \(N\)-th power in \(k^\times\). This is background for the rational-form parameter, not an independent novelty claim.

## Proof
**1. All automorphisms are weighted rotations.** Since \(E_t^2=E_t\), the squares of the natural basis are linearly independent. For distinct basis elements \(e_i,e_j\), the supports of their images under any automorphism must be disjoint: their product is zero, and distinct basis squares are independent. Hence the automorphism matrix is monomial. Its permutation preserves the directed cycle and therefore is a rotation \(i\mapsto i+s\bmod n\), for one unique \(s\in\{0,\ldots,n-1\}\). Write its nonzero coefficients as \(\phi(e_i)=c_i e_{i+s\bmod n}\). The multiplicativity equations are
\[
\lambda_i c_{i+1\bmod n}=c_i^2\lambda_{i+s\bmod n},
\quad\text{where}\quad\lambda_i=\begin{cases}1,&i<n-1,\\t,&i=n-1.\end{cases}
\]
For \(s=0\), they yield \(c_i=c_0^{2^i}\), and the closing condition is \(c_0^N=1\). For \(1\leq s<n\), the only exceptional ratios \(\lambda_{i+s}/\lambda_i\) occur at \(i=n-1-s\) (ratio \(t\)) and \(i=n-1\) (ratio \(t^{-1}\)). Thus the unique recursive solution for given \(c_0\ne0\) is
\[
c_i=\begin{cases}c_0^{2^i},&0\leq i<n-s,\\c_0^{2^i}t^{2^{i-(n-s)}},&n-s\leq i<n,\end{cases}
\]
with closing condition \(c_0^N=t^{1-2^s}\). The same closing equation works for \(s=0\). Since \(k^\times\) is cyclic of order \(M\), the equation \(x^N=a\) has \(d=\gcd(M,N)\) solutions exactly when \(a^{M/d}=1\), otherwise none. This proves that precisely \(A_s\) automorphisms induce rotation \(s\).

**2. Fixed spaces of weighted rotations.** Put \(g=g_s\) and \(L=n/g\). Rotation by \(s\) consists of \(g\) cycles of length \(L\). A weighted cyclic-permutation matrix on one such cycle has a one-dimensional fixed space if the product of its weights is one, and a zero-dimensional fixed space otherwise. The \(L\)-th power \(\phi^L\) is diagonal, with diagonal entries \(\alpha_i\) satisfying \(\alpha_{i+1}=\alpha_i^2\) because \(\phi^L\) is an algebra automorphism. Since \(\alpha_0^N=1\) and \(N\) is odd, either all \(g\) cycle products equal one or none does. Hence every automorphism with rotation \(s\) has fixed-space dimension exactly \(g\) or zero.

The cycle of rotation \(s\) containing index zero consists of the multiples of \(g\) in \(\{0,\ldots,n-1\}\). Multiplying the coefficients \(c_i\) from step 1 over those indices shows that its weight product is
\[
\alpha_0=c_0^{H_s}t^{J_s},\qquad
H_s=1+2^g+\cdots+2^{n-g},\quad
J_s=1+2^g+\cdots+2^{s-g}
\]
(the second sum is empty when \(s=0\)). Therefore the fixed-space dimension equals \(g\) exactly when \(c_0^{H_s}=t^{-J_s}\). Over a cyclic group of order \(M\), this equation has precisely \(b_s=\gcd(M,H_s)\) solutions when \(t^{J_sM/b_s}=1\), and none otherwise. Any such solution automatically satisfies the automorphism closing condition upon raising the equation to \(2^g-1\), because \((2^g-1)H_s=N\) and \((2^g-1)J_s=2^s-1\). Thus \(B_s\) counts exactly the automorphisms of rotation \(s\) with \(g\)-dimensional fixed space; the other \(A_s-B_s\) have no nonzero fixed vector. Summing proves the polynomial.

**3. Group order and tuple orbits.** Choose a generator \(\zeta\) and write \(t=\zeta^h\). The criterion for \(A_s=d\) is \(d\mid h(2^s-1)\), equivalently \(2^s\equiv1\pmod m\) for \(m=d/\gcd(d,h)\). As \(m\mid 2^n-1\), the order \(\operatorname{ord}_m(2)\) divides \(n\), and exactly \(n/\operatorname{ord}_m(2)\) shifts are allowed. Burnside's lemma applied to the diagonal action on \(E_t^r\) gives \(\lvert E_t^r/\operatorname{Aut}(E_t)\rvert=P_{n,q,t}(q^r)/\lvert\operatorname{Aut}(E_t)\rvert\). The nonidentity diagonal automorphisms (rotation zero) all have fixed-space dimension zero; hence freeness on nonzero vectors is equivalent to all \(B_s\) for \(s\ne0\) vanishing.

**4. The nonabelian free-action example.** In \(\mathbb F_{43}\), \(3\) has multiplicative order \(42\), \(t=3^7=37\), \(N=63\), \(d=\gcd(42,63)=21\), and \(h=7\). The allowed shifts are exactly \(s\in\{0,2,4\}\), each admitting \(21\) automorphisms. For \(s=2,4\), one has \(g_s=2\), \(H_s=21\), \(b_s=21\), while \(J_2=1\), \(J_4=5\). Neither \(7\) nor \(35\) is divisible by \(21\), so \(B_2=B_4=0\). For \(s=0\), \(B_0=1\), proving \(P(T)=62+T^6\). The diagonal subgroup is cyclic of order \(21\). A lift of rotation \(2\) acts on this subgroup by conjugation through the exponent \(2^{n-2}=16\) on the coordinate at \(e_0\), nontrivially modulo \(21\); thus the automorphism group is nonabelian. The finite orbit count follows by division of \(43^6-1\) by \(63\).

## Verification
The independent enumeration in `verify.py` reconstructs the weighted monomial candidates directly from the multiplication table and their closing equations, computes the rank of \(\phi-I\) by finite-field Gaussian elimination, and compares with the predicted polynomial. It tests prime fields and nonprime fields, varying both \(n\) and \(t\). The special \(\mathbb F_{43}\) example is checked separately, including all automorphism matrices and their fixed-space dimensions. Run with `python3 verify.py` from a directory containing this file. A successful run prints `VERIFY_OK`. These finite tests are consistency checks; the preceding argument proves the formulas for all stated finite fields and dimensions.

## Relationship to prior work
Elduque and Labra's 2013 paper *Evolution algebras and graphs* establishes monomiality of automorphisms of regular evolution algebras (Theorem 4.4 and Corollary 4.7) and finiteness (Theorem 4.8). Its results imply the starting reduction to weighted rotations. Their 2019 paper *Evolution algebras, automorphisms, and graphs* identifies diagonal group schemes and the exact sequence relating automorphisms to graph symmetries (Theorem 3.2); Example 3.5 explicitly shows a two-dimensional nonsplit situation. Wei and Zou's *Isomorphism Classes of Idempotent Evolution Algebras* (2023) provides a general isomorphism-orbit framework that covers the underlying monomial isomorphism criterion. None of these starting results is claimed as new. The result here is the full **rational fixed-space multiplicity polynomial** in every dimension, its exact arithmetic obstruction and the explicit nonabelian fixed-point-free instance in a simple algebra. General monomiality, diagonal root groups, nonsplitting in dimension two, and general isomorphism-orbit correspondences are prior knowledge.

## Limitations
This is a classification only for nonzero-weight directed cycles, not general evolution algebras or arbitrary weighted digraphs. It is a finite-field rational-point statement; it makes no assertion about smoothness of automorphism group schemes, especially in positive characteristic dividing \(2^n-1\). It does not assert that the abstract group action identified at \(q=43\) is novel outside the setting of evolution algebras. The literature comparison is bounded by the inspected sources and mathematical search results, so an unlocated equivalent specialized theorem remains possible. There has been no independent external mathematical audit.

## References
1. A. Elduque and A. Labra, *Evolution algebras and graphs*, arXiv:1312.4685, first submitted 17 December 2013, Theorem 4.4, Corollary 4.7, Theorem 4.8. https://arxiv.org/abs/1312.4685.
2. A. Elduque and A. Labra, *Evolution algebras, automorphisms, and graphs*, arXiv:1902.02191, first submitted 6 February 2019, Theorem 3.2 and Example 3.5. https://arxiv.org/abs/1902.02191.
3. Y. Wei and Y. M. Zou, *Isomorphism Classes of Idempotent Evolution Algebras*, arXiv:2310.12368, first submitted 18 October 2023, Theorem 1.1 and Corollary 1.1. https://arxiv.org/abs/2310.12368.
