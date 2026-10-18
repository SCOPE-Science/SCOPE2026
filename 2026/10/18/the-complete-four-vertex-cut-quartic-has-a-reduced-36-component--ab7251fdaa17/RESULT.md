# The complete-four-vertex cut quartic has a reduced, 36-component Cohen–Macaulay singular scheme

## Finding
Let \(k\) be an algebraically closed field of arbitrary characteristic. Let \(X\subset\mathbb P^7_k\) be the cut variety of the complete graph on four vertices, with its eight standard cut coordinates. With a permutation of those coordinates, its defining equation is
\[
F=x_1x_2x_3x_4-y_1y_2y_3y_4=0.
\]
The full **Jacobian singular scheme** \(\Sigma\), not merely its reduced support, is a reduced, arithmetically Cohen–Macaulay projective threefold. Its minimal primary decomposition is
\[
J(F)=\bigcap_{\substack{I,K\subseteq\{1,2,3,4\}\\ |I|=|K|=2}}(x_i:i\in I,\ y_j:j\in K).
\]
Consequently \(\Sigma\) is the union of precisely \(36\) reduced coordinate \(\mathbb P^3\)'s, has degree \(36\) and arithmetic genus \(9\), and has no embedded associated primes or infinitesimal structure. Its homogeneous coordinate ring has Hilbert series
\[
\operatorname{Hilb}_{k[x_1,\ldots,x_4,y_1,\ldots,y_4]/J(F)}(t)
=\frac{(1+2t+3t^2)^2}{(1-t)^4}.
\]
Its complete nonzero graded Betti numbers are
\[
\beta_{0,0}=1,\ \beta_{1,3}=8,\ \beta_{2,4}=6,\ \beta_{2,6}=16,\ \beta_{3,7}=24,\ \beta_{4,8}=9.
\]
In particular, the singular-scheme coordinate ring has Cohen–Macaulay type \(9\) and is not Gorenstein. Generically on every irreducible singular component, the transverse local equation of \(X\) is the threefold ordinary double point \(uv-st=0\).

## Assumptions and scope
All equations are in the standard-graded polynomial ring \(S=k[x_1,\ldots,x_4,y_1,\ldots,y_4]\), with each coordinate of degree one. The Jacobian ideal \(J(F)\) means the ideal of **all eight ordinary partial derivatives**; including \(F\) does not change the ideal because each of its two monomials belongs to it. The saturated homogeneous ideal defines the projective Jacobian singular scheme. The statements hold over every algebraically closed field, including characteristics two and three. For a projective pure threefold, arithmetic genus is \(p_a=1-\chi(\mathcal O)\).

## Proof
**Jacobian and primary decomposition.** Differentiating the two disjoint monomials gives, up to signs, four squarefree triple products in the \(x\)-variables and four in the \(y\)-variables. Set
\[
L_x=(x_2x_3x_4,x_1x_3x_4,x_1x_2x_4,x_1x_2x_3),\quad
L_y=(y_2y_3y_4,y_1y_3y_4,y_1y_2y_4,y_1y_2y_3).
\]
Then \(J(F)=L_xS+L_yS\). Each \(L_x\) is the squarefree degree-three Veronese ideal in four variables. A monomial is killed at a coordinate point with some zero pattern if and only if at least two of the four variables are zero; equivalently
\[
L_x=\bigcap_{|I|=2}(x_i:i\in I),\qquad
L_y=\bigcap_{|K|=2}(y_j:j\in K).
\]
Since the two ideals are in disjoint variable sets, their sum is the squarefree monomial ideal with the claimed \(36\) distinct minimal primes. No monomial power is needed: the ideal itself is radical. In particular it is already saturated with respect to the irrelevant ideal, and these primes are all its associated primes. Each gives a \(\mathbb P^3\) in \(\mathbb P^7\); hence the support is pure of dimension three and has degree \(36\).

**Minimal resolution and Hilbert series.** The four generators of \(L_x\), ordered by their omitted index, are the maximal minors of the following \(4\times3\) Hilbert–Burch matrix (up to sign):
\[
\begin{pmatrix}
x_1&0&0\\-x_2&x_2&0\\0&-x_3&x_3\\0&0&-x_4
\end{pmatrix}.
\]
The ideal has height two; Hilbert–Burch gives the exact minimal free resolution
\[
0\to k[x](-4)^3\to k[x](-3)^4\to k[x]\to k[x]/L_x\to0.
\]
The analogous resolution holds in \(y\). The quotient \(S/J(F)\) is their tensor product over \(k\); consequently the tensor-product complex is a minimal exact free resolution over \(S\). Its alternating Betti numerator is \((1-4t^3+3t^4)^2\), and its graded Betti numbers are exactly those in the finding. Since
\[
1-4t^3+3t^4=(1-t)^2(1+2t+3t^2),
\]
the Hilbert series is as stated. The projective dimension is four, the ambient regular ring has dimension eight, and Auslander–Buchsbaum gives depth four, equal to the Krull dimension. Thus the ring is Cohen–Macaulay. The terminal free module has rank nine, giving type nine; the scheme is not arithmetically Gorenstein. The numerator at \(t=1\) gives degree \(36\).

**Arithmetic genus.** The Hilbert polynomial is
\[
P(d)=\sum_{i=0}^4h_i\binom{d+3-i}{3},\qquad (h_0,h_1,h_2,h_3,h_4)=(1,4,10,12,9),
\]
with the binomial interpreted as its polynomial extension to all integers. In particular \(\chi(\mathcal O_\Sigma)=P(0)=1-9=-8\), and therefore \(p_a(\Sigma)=9\).

**Generic transverse singularity.** A dense open part of any coordinate component has exactly two vanished \(x\)'s and exactly two vanished \(y\)'s, with all other coordinates invertible. After rescaling the four vanishing local coordinates by units, the defining equation becomes \(uv-st=0\), with three further smooth coordinates along that component. This is the ordinary threefold node in the transverse four-dimensional ambient slice. The calculation uses no characteristic restriction.

## Verification
The standalone checker `artifacts/verify.py` independently verifies the Hilbert–Burch maximal-minor identities, the exact free-resolution numerator and Betti table, the Hilbert coefficients in degrees zero through twenty-three, the prime-component count and the genus computation. It also enumerates every projective point over \(\mathbb F_2\) and \(\mathbb F_3\), confirming that the ordinary derivatives vanish precisely for zero patterns with two zeros in each coordinate block. Execute from the directory containing this file with `python3 artifacts/verify.py`; expected final line: `VERIFY_OK K4 singular scheme / Hilbert / resolution / finite fields`. Finite-field tests are corroboration, not the proof over arbitrary fields.

## Relationship to prior work
Sturmfels–Sullivant, *Toric Geometry of Cuts and Splits*, Example 1.1, identify the complete-four-vertex cut ideal as the single quartic above. Their Corollary 2.4 gives a graph-minor criterion for smoothness and describes the singular three-planes of the distinct graph obtained by deleting an edge. Engström proves the generator-degree characterization for cut ideals of graphs without complete-four-vertex minors. Olteanu's *Monomial Cut Ideals* concerns a different monomial ideal in edge variables, not the Jacobian ideal of this projective quartic. These established results are credited here, not asserted as new. The present exact description concerns the reducedness, all components, graded resolution, type and arithmetic genus of the **Jacobian singular scheme** of the complete-four-vertex model itself.

## Limitations
This statement concerns the four-vertex complete graph only; it does not classify Jacobian singular schemes of arbitrary cut varieties or describe completed local rings at non-generic intersections of the \(36\) components. The formulas are elementary enough that equivalent implicit or explicit treatments in general binomial-hypersurface literature cannot be ruled out by the literature inspection performed.

## References
1. Bernd Sturmfels and Seth Sullivant, *Toric Geometry of Cuts and Splits*, arXiv:math/0606683, first posted 2006-06-27, especially Example 1.1 and Corollary 2.4; https://arxiv.org/abs/math/0606683 .
2. Alexander Engström, *Cut Ideals of K4-Minor Free Graphs Are Generated by Quadrics*, arXiv:0805.1762, first posted 2008-05-13; https://arxiv.org/abs/0805.1762 .
3. Anda Olteanu, *Monomial Cut Ideals*, arXiv:1105.3564, first posted 2011-05-18; https://arxiv.org/abs/1105.3564 .
