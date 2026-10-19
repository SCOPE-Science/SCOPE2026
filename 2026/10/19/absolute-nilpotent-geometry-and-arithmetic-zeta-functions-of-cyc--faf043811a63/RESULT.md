# Absolute-nilpotent geometry and arithmetic zeta functions of cycle evolution algebras

## Finding
For each integer \(n\ge3\) and finite field \(k=\mathbb F_q\), let \(E_n(k)\) be the graph evolution algebra of the simple undirected cycle \(C_n\). Its natural basis is \(e_1,\ldots,e_n\), with indices modulo \(n\), and multiplication
\[
e_ie_j=0\quad(i\ne j),\qquad e_i^2=e_{i-1}+e_{i+1}.
\]
Define the absolute-nilpotent locus \(Z_n(k)=\{x\in E_n(k):x^2=0\}\), and let \(X_n\) denote the *reduced* affine variety cut out set-theoretically by this equation. Then its geometric irreducible components, point counts over every extension field, and Hasse–Weil zeta function are as follows.

**Geometric classification.** In characteristic two, \(X_n\) is a linear space of dimension one when \(n\) is odd, and of dimension two when \(n\) is even. In odd characteristic, \(X_n\) is a single reduced point unless \(4\mid n\). If \(4\mid n\), it is a union of exactly \(2^{n-2}\) distinct linear two-planes over an algebraic closure, and these are precisely its geometric irreducible components. They are all defined over \(k\) if \(-1\) is a square in \(k\); otherwise they split over \(k(\sqrt{-1})\).

**Exact field counts.** For every prime power \(q\),
\[
|Z_n(\mathbb F_q)|=
\begin{cases}
q,& q\text{ even and }n\text{ odd},\\
q^2,&q\text{ even and }n\text{ even},\\
1,&q\text{ odd and }4\nmid n,\\
1,&q\equiv3\pmod4\text{ and }4\mid n,\\
\bigl(1+2^{n/2-1}(q-1)\bigr)^2,&q\equiv1\pmod4\text{ and }4\mid n.
\end{cases}
\]
In particular, when \(4\mid n\) and \(q\equiv3\pmod4\), the variety has exponentially many geometric plane components but only its origin is \(\mathbb F_q\)-rational.

**Complete zeta function.** Set
\[
\mathcal Z_{n,q}(T)=\exp\!\left(\sum_{r\ge1}|Z_n(\mathbb F_{q^r})|\frac{T^r}{r}\right).
\]
In characteristic two it is \((1-qT)^{-1}\) for odd \(n\), or \((1-q^2T)^{-1}\) for even \(n\). In odd characteristic with \(4\nmid n\), it is \((1-T)^{-1}\). In the remaining cases write \(L=2^{n/2-1}\) and \(B=(L-1)^2\). If \(q\equiv1\pmod4\), then
\[
\mathcal Z_{n,q}(T)=
(1-q^2T)^{-L^2}(1-qT)^{2L(L-1)}(1-T)^{-B}.
\]
If \(q\equiv3\pmod4\), then
\[
\mathcal Z_{n,q}(T)=
(1-q^4T^2)^{-L^2/2}(1-q^2T^2)^{L(L-1)}
(1-T)^{-(B+1)/2}(1+T)^{-(B-1)/2}.
\]
All exponents in these rational expressions are integers because \(4\mid n\) implies \(L\) is even and \(B\) is odd.

## Assumptions and scope
The cycle is the *simple undirected* graph \(C_n\) with \(n\ge3\); it is not the directed one-outgoing-edge permutation evolution algebra. The algebra may be nonassociative. The notation \(x^2\) means the single product \(x\cdot x\), not a claim of associative nilpotency. The geometric assertions concern reduced affine varieties over algebraic closures and do **not** assert that the original quadratic defining ideal is radical. The field-count assertions are for finite fields, including nonprime extensions and characteristic two. The zeta series is the usual exponential generating function of extension-field rational points of this reduced locus, with the same points as the original equations over every field.

## Proof
Write \(x=\sum_{i=1}^n x_i e_i\). Orthogonality of distinct natural-basis elements gives
\[
x^2=\sum_{i=1}^n(x_{i-1}^2+x_{i+1}^2)e_i.
\]
Thus \(x^2=0\) if and only if \(u_{i+2}=-u_i\) for all cyclic indices, where \(u_i=x_i^2\). Applying this recurrence twice gives \(u_{i+4}=u_i\). If \(n\) is odd, the recurrence forces all \(u_i\) to be equal; then \(2u_i=0\). If \(n\equiv2\pmod4\), the odd and even subsequences each have odd length, again forcing \(2u_i=0\). Accordingly, when the characteristic is odd and \(4\nmid n\), all \(u_i=0\), hence all \(x_i=0\).

If the characteristic is two, \(u_{i+2}=u_i\). Over every perfect field, including algebraic closures and finite fields, squaring is injective, so \(x_{i+2}=x_i\). More precisely, each quadratic defining polynomial is \((x_{i-1}+x_{i+1})^2\), so the reduced locus is exactly the linear subspace defined by \(x_{i+2}=x_i\). Cyclic periodicity leaves one free coordinate for odd \(n\) and two for even \(n\). This proves both the component assertion and the characteristic-two counts.

Assume now that the characteristic is odd and \(n=4h\), and put \(m=n/2=2h\). The recurrence determines the squares on odd and even positions independently:
\[
x_{2j+1}^2=(-1)^j x_1^2,\qquad
x_{2j+2}^2=(-1)^j x_2^2
\quad(0\le j<m).
\]
Over an algebraic closure, choose \(\iota\) with \(\iota^2=-1\). For each parity, and each of the \(m-1\) positions beyond the first, choose one of the two square roots of \((-1)^j\). This yields \(2^{m-1}\) distinct lines in that parity's coordinate space. Their pairwise products are \(2^{2m-2}=2^{n-2}\) distinct linear two-planes, each parameterized by freely choosing \(x_1\) and \(x_2\). Their union is the complete reduced zero set; none of the planes contains another. These therefore are exactly the geometric irreducible components. All choices have coefficients in \(k\) if \(\iota\in k\); otherwise the field of definition is the quadratic extension obtained by adjoining \(\iota\).

Over odd \(\mathbb F_q\), the element \(-1\) is a square exactly when \(q\equiv1\pmod4\). If it is not a square, the relations \(x_3^2=-x_1^2\) and \(x_4^2=-x_2^2\) force both initial coordinates, hence every coordinate, to vanish. If it is a square, for either parity there is one all-zero string and, for each of the \(q-1\) nonzero initial coordinates, two choices at each of the remaining \(m-1\) positions. Consequently each parity has \(1+2^{m-1}(q-1)\) admissible strings. Multiplying the two independent counts yields the stated formula.

Finally the field counts remain valid with \(q\) replaced by \(q^r\). When \(q\equiv1\pmod4\), expanding the square gives
\[
|Z_n(\mathbb F_{q^r})|=L^2 q^{2r}-2L(L-1)q^r+B.
\]
Termwise exponential summation yields the first odd-characteristic rational zeta expression. When \(q\equiv3\pmod4\), odd-degree extensions still have one point, whereas for even degrees \(r=2s\) the count is \(L^2q^{4s}-2L(L-1)q^{2s}+B\). Summing the odd-degree contribution and the even-degree geometric series gives
\[
\log\mathcal Z_{n,q}(T)
=-\tfrac{L^2}{2}\log(1-q^4T^2)
+L(L-1)\log(1-q^2T^2)
-\tfrac{B+1}{2}\log(1-T)
-\tfrac{B-1}{2}\log(1+T),
\]
which proves the second expression. The other zeta formulas follow directly from the one-point, affine-line, and affine-plane counts.

## Verification
The standalone standard-library script `verify.py` constructs finite fields \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), \(\mathbb F_5\), \(\mathbb F_7\), and \(\mathbb F_9\) using explicit polynomial residue arithmetic when needed. It exhaustively enumerates coordinate vectors, evaluates the multiplication rule directly, and compares the counts to the theorem for 38 field/length pairs. It also verifies the rational zeta factors by their formal logarithmic coefficients for multiple lengths and extension degrees. Run `python3 verify.py`; successful output ends in `VERIFY_OK 38 exhaustive finite-field and zeta checks`.

Representative exhaustive counts: \(n=4\) gives \(1\) over \(\mathbb F_3\), \(289\) over \(\mathbb F_9\), and \(81\) over \(\mathbb F_5\); \(n=8\) gives \(1089\) over \(\mathbb F_5\). These finite computations are cross-checks, not substitutes for the uniform algebraic proof.

## Relationship to prior work
Elduque and Labra (initial arXiv posting 17 December 2013) define the graph attached to an evolution algebra and study nilpotency and automorphisms; their nilpotency theorem concerns the *entire algebra*, not the zero-square locus of individual elements. Khudoyberdiyev, Omirov, and Qaralleh (2013, *Few Remarks on Evolution Algebras*) give a general complex-field criterion for existence of a nonzero absolute nilpotent in terms of singularity of the structure matrix (Proposition 4.1). That prior criterion predicts geometric existence for the singular adjacency cases, but it does not determine finite-field rational points, geometric components, splitting fields, or zeta functions for the cycle family. Its permutation-algebra results concern a different one-successor multiplication law.

A later paper by Ceballos (2026, Proposition 2, on S-graphicable algebras over the complex numbers) states that absolute nilpotents lie in the annihilator. That statement is not a valid covering implication for the present zero-square locus: in the undirected four-cycle algebra over \(\mathbb C\), the explicitly nonzero element \(e_1+\mathrm i e_3\), with \(\mathrm i^2=-1\), has square zero even though the annihilator is zero. Its proof invokes positivity of complex squared coefficients, which does not hold. The classification here instead uses the exact coordinate-square recurrence.

The new content is the exact arithmetic-geometric classification of a natural family: an abundance of geometric components can coexist with the complete absence of nonzero base-field points, and the resulting quadratic splitting is visible explicitly in the Hasse–Weil zeta function. The familiar recurrence for adjacency-matrix kernels and standard finite-field square-root facts are used, not claimed as novel.

## Limitations
This classification concerns simple undirected cycles, not arbitrary graphs or weighted cycles. It is set-theoretic/reduced: the defining quadratic scheme in characteristic two is generally nonreduced, and no scheme-theoretic radicality assertion is made. The full automorphism action on the absolute-nilpotent locus is not classified. An independent literature audit has not been performed; obscure graph-algebra classifications or general rational-point enumeration results could imply some of these formulas.

## References
1. Alberto Elduque and Alicia Labra, *Evolution algebras and graphs*, arXiv:1312.4685v1, publicly posted 17 December 2013, https://arxiv.org/abs/1312.4685 .
2. Abror Kh. Khudoyberdiyev, Bakhrom A. Omirov, and Izzat Qaralleh, *Few Remarks on Evolution Algebras* (2013), Proposition 4.1, https://www.researchgate.net/publication/244989408_Few_remarks_on_evolution_algebras .
3. Jianjun Paul Tian, *Evolution Algebras and Their Applications*, Lecture Notes in Mathematics 1921, Springer (2008), https://doi.org/10.1007/978-3-540-74284-5 .
4. Manuel Ceballos, *S-Graphicable Algebras and Specific Graph Families*, Mathematical Methods in the Applied Sciences (2026), Proposition 2, https://doi.org/10.1002/mma.70534 .
