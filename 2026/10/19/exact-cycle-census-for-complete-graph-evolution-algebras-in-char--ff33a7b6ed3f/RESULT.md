# Exact cycle census for complete-graph evolution algebras in characteristic two

## Finding
Let \(n\ge3\) and \(f\ge2\), with \(K=\mathbb F_{2^f}\). In the graph evolution algebra for the complete graph on \(n\) vertices, the squaring map has an exact periodic-point census over every finite extension of characteristic two, and a parity dichotomy between one-step transients and permutations.

Write \(P_k=|\operatorname{Fix}(T^k)|\), \(g=\gcd(f,k)\), and \(t=f/g\). For every integer \(k\ge1\),
\[
P_k=\begin{cases}
2^{g(n-1)},&n\text{ odd},\\
2^{gn},&n\text{ even and }(k\text{ even or }t\text{ even}),\\
2^{g(n-1)},&n\text{ even, }k\text{ odd, }t\text{ odd}.
\end{cases}
\]
The exact number of cycles of least period \(d\) is
\[
C_d=\frac1d\sum_{k\mid d}\mu(d/k)P_k.
\]
If \(n\) is odd, exactly \(2^{f(n-1)}\) points are periodic and every other point enters the periodic hyperplane after one update. If \(n\) is even, all \(2^{fn}\) points are periodic. For odd \(n\), all periods divide \(f\); for even \(n\), they divide \(2f\).

## Assumptions and scope
The field is \(\mathbb F_{2^f}\) for \(f\ge2\), and \(n\ge3\). The evolution algebra has natural basis \(e_i\) satisfying \(e_i e_j=0\) for \(i\ne j\) and \(e_i^2=\sum_{j\ne i}e_j\). Points are algebra elements with coordinate vectors in \(K^n\). Here \(T(x)=x^2\) is a (nonlinear over \(K\), linear over \(\mathbb F_2\)) polynomial self-map. \(P_k\) counts points fixed by the \(k\)-fold iterate, not necessarily points of least period \(k\). \(\mu\) denotes the integer Möbius function. The formulas include all such \(n,f,k\), not merely tested configurations.

## Proof
Put \(F(x_1,\ldots,x_n)=(x_1^2,\ldots,x_n^2)\), let \(s(x)=\sum_i x_i\), let \(\mathbf1=(1,\ldots,1)\), and set \(A(x)=x+s(x)\mathbf1\). In characteristic two, \(T=A\circ F\). The maps \(A\) and \(F\) commute because their matrices have coefficients in \(\mathbb F_2\). Writing \(Jx=s(x)\mathbf1\), one has \(J^2=nJ\) and thus \(A^2=I+nJ\).

If \(n\) is odd, \(A^2=A\), \(\operatorname{im}(A)=H=\ker s\), and \(A\) restricts to the identity on \(H\). The Frobenius automorphism \(F\) preserves \(H\). Thus \(T^k=A F^k\) for all \(k\ge1\), and \(T^k(x)=x\) holds exactly when \(x\in H\) and each coordinate lies in the fixed field \(\mathbb F_{2^g}\). This set has \(2^{g(n-1)}\) elements. As \(T\) maps onto \(H\), every point outside \(H\) has preperiod exactly one, while every point of \(H\) is periodic under the Frobenius permutation.

If \(n\) is even, \(A^2=I\), and \(T\) is a permutation. For even \(k\), \(T^k=F^k\), so its fixed points are all vectors in \(\mathbb F_{2^g}^n\), numbering \(2^{gn}\). For odd \(k\), write \(\sigma=F^k\), \(K_0=\operatorname{Fix}(\sigma)=\mathbb F_{2^g}\), and \(t=f/g\). Any solution of \(A\sigma(x)=x\) satisfies \(\sigma(x_i)+x_i=c\) independent of \(i\). Therefore \(x_i=y+c_i\) with \(y=x_1\), \(c_1=0\), and \(c_2,\ldots,c_n\in K_0\). Because \(n\) is even, \(s(x)=c=\sum_{i=2}^n c_i\), and the fixed-point equation is exactly \(\sigma(y)+y=c\). By the additive Hilbert-90/trace criterion, the map \(y\mapsto\sigma(y)+y\) has kernel of size \(2^g\), and its image consists of elements with relative trace zero. Since \(c\in K_0\), the trace is \(tc\). If \(t\) is odd, exactly \(2^{g(n-2)}\) tuples \((c_2,\ldots,c_n)\) have \(c=0\), each with \(2^g\) values of \(y\), giving \(2^{g(n-1)}\). If \(t\) is even, every one of the \(2^{g(n-1)}\) tuples is allowed and each has \(2^g\) choices, giving \(2^{gn}\).

Finally the number of points of least period \(d\) is \(\sum_{k\mid d}\mu(d/k)P_k\) by Möbius inversion, and each such orbit contains exactly \(d\) points. Since \(F^f=I\), \(T^f\) restricts to the identity on \(H\) when \(n\) is odd, and \(T^{2f}=I\) when \(n\) is even; the stated period divisibility follows.

## Verification
The standalone `verify.py` independently implements arithmetic over \(\mathbb F_2\), \(\mathbb F_4\), \(\mathbb F_8\), and \(\mathbb F_{16}\), iterates the actual squaring map over every vector in nine small field/dimension pairs, and compares all fixed-point counts for every \(1\le k\le2f\). The output was `VERIFY_OK 9 field/dimension cases; fixed-points for all k <= 2f`. The symbolic proof, rather than finite testing, establishes the arbitrary-field-degree and dimension assertions.

## Relationship to prior work
Giacomelli (2026, arXiv:2605.12672v1), Example 10.2, introduces the complete-graph evolution algebra in its study of expander evolution algebras and considers algebraic growth, but the inspected full text does not give this finite-field periodic-point census. The earlier literature on S-graphicable algebras includes idempotent characterizations; this theorem counts every iterate and every least-period orbit, not only idempotents. A published binary complete-multipartite parity-automaton census covers the base field \(\mathbb F_2\) in a more general graph setting; the claimed result restricts to \(f\ge2\), and addresses extension-field Frobenius dynamics and its dependence on \(\gcd(f,k)\) and extension parity. Those older related contributions are not claimed as new.

## Limitations
These formulas apply to the unweighted complete graph in characteristic two; they do not classify weighted graph evolution algebras, odd characteristic, or arbitrary adjacency graphs. The counting theorem is checked by the same mathematical assessment, not an independent audit. An equivalent exact periodic-point theorem in unindexed literature cannot be ruled out solely by targeted searches; in particular, a relevant 2026 S-graphicable paper was only available in abstract-level detail during this review.

## References
1. P. Giacomelli, *Expander Evolution Algebras*, arXiv:2605.12672v1, posted 2026-05-12; especially Example 10.2 and Section 11. https://arxiv.org/abs/2605.12672
2. M. Ceballos, *S-Graphicable Algebras and Specific Graph Families*, Math. Methods Appl. Sci., 2026, DOI:10.1002/mma.70534.
3. *Sharp period-four census for complete multipartite parity automata*, published 2026-10-11, published public indexed finding, 2026-10-11 .
