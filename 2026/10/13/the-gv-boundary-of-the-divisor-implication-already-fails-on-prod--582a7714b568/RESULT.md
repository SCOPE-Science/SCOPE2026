# The GV boundary of the divisor implication already fails on product principally polarized abelian varieties
## Finding
For every integer \(g\ge 2\), Meng's divisor implication has a sharp failure at the natural GV boundary. There is a principally polarized complex abelian variety \((A,H)\) and an effective nef divisor \(D\) for which \(\mathcal O_A(2H-D)\) is GV but \(\mathcal O_A(H-D)\) is not GV.

Take elliptic curves \(E_1,\ldots,E_g\), put
\[
A=E_1\times\cdots\times E_g,
\qquad
F_i=\operatorname{pr}_i^*([0_{E_i}]),
\]
and set
\[
H=F_1+\cdots+F_g,
\qquad
D=2F_1.
\]
Then \(H\) is the product principal polarization, \(D\) is effective and nef,
\[
2H-D=2(F_2+\cdots+F_g)
\]
is nef and therefore defines a GV line bundle, whereas \(H-D\) is not nef and therefore does not define a GV line bundle.

Thus the IT hypothesis in Meng's theorem cannot be replaced by the formally weaker GV hypothesis, even for a product principally polarized abelian variety and an effective divisor.
## Assumptions and scope
The base field is \(\mathbf C\). The dimension satisfies \(g\ge 2\). Each \(E_i\) is an elliptic curve with chosen origin \(0_{E_i}\), and \(F_i\) denotes the pullback of that degree-one divisor from the \(i\)-th factor. The statement concerns the natural attempted weakening of Meng's theorem from IT to GV for the line bundle \(\mathcal O_A(2H-D)\).

For line bundles on a complex abelian variety, the positivity dictionary used here is the standard one recalled in Meng's paper: IT of index zero is equivalent to ampleness, while GV is equivalent to nefness. No assertion is made for higher-rank sheaves.
## Proof
The line bundle of \(H\) is
\[
\mathcal O_A(H)\cong
\mathcal O_{E_1}([0_{E_1}])\boxtimes\cdots\boxtimes
\mathcal O_{E_g}([0_{E_g}]).
\]
Every factor has degree one, so this is the product principal polarization. The divisor \(D=2F_1\) is effective and nef.

Moreover,
\[
2H-D=2F_2+\cdots+2F_g.
\]
This divisor is the pullback under \(A\to E_2\times\cdots\times E_g\) of an ample divisor on the product of the last \(g-1\) elliptic curves. It is therefore nef. Equivalently, \(\mathcal O_A(2H-D)\) is a GV line bundle. It is not ample because it has degree zero on every curve contained in the first elliptic factor, which is exactly why this example lies on the boundary excluded by the IT hypothesis.

Choose arbitrary points \(q_i\in E_i\) for \(i\ge2\) and consider
\[
C_1=E_1\times\{q_2\}\times\cdots\times\{q_g\}.
\]
One has \(F_1\cdot C_1=1\) and \(F_i\cdot C_1=0\) for \(i\ge2\). Hence
\[
(H-D)\cdot C_1
=(-F_1+F_2+\cdots+F_g)\cdot C_1=-1.
\]
Thus \(H-D\) is not nef. By the same line-bundle positivity dictionary, \(\mathcal O_A(H-D)\) is not GV.

Therefore the implication
\[
\mathcal O_A(2H-D)\text{ GV}
\Longrightarrow
\mathcal O_A(H-D)\text{ GV}
\]
fails in every dimension \(g\ge2\), even with \(H\) principal and \(D\) effective nef. This isolates the strict IT/ample hypothesis in Meng's theorem as essential for that implication.
## Verification
The verification is entirely intersection-theoretic. On the product, \(F_i\) is nef because it is the pullback of an ample divisor from an elliptic curve. Therefore \(D\) and \(2H-D\) are nef. Restricting \(H-D\) to \(C_1\) gives a line bundle of degree \(-1\), so \(H-D\) is not nef.

The only non-elementary input is the standard equivalence for line bundles on abelian varieties between GV and nefness, and between IT of index zero and ampleness. Meng recalls this equivalence in the setup used to formulate and prove the divisor theorem. The displayed construction can also be checked from the numerical polynomial
\[
\frac{(tH-D)^g}{g!}=t^{g-1}(t-2),
\]
whose root at \(2\) records exactly the boundary direction where \(2H-D\) is nef but not ample.
## Relationship to prior work
Meng proves that if \((A,H)\) is principally polarized, \(D\) is nef, and \(\mathcal O_A(2H-D)\) satisfies IT, then \(\mathcal O_A(H-D)\) is GV. For line bundles this is the implication from an ample \(2H-D\) to a nef \(H-D\). The source proof uses the strict upper root bound coming from ampleness. The example above sits precisely on the missing boundary: \(2H-D\) is nef but not ample, and \(H-D\) immediately leaves the nef cone.

Pareschi--Popa's generic-vanishing theory supplies the broader positivity framework relating GV sheaves and nefness. The present statement is not a counterexample to Meng's theorem; it proves that its hypothesis cannot simply be weakened from IT to GV.

Targeted searches for the source identifier, the divisor classes \(2H-D\) and \(H-D\), product principal polarizations, and the proposed IT-to-GV weakening did not locate an earlier explicit statement of this counterexample. Because the construction is elementary, an unindexed folklore occurrence remains a residual originality risk.
## Limitations
The construction uses decomposable principally polarized abelian varieties. It does not decide whether an analogous boundary counterexample exists under an indecomposability hypothesis. It also concerns only line bundles and the specific divisor implication; it does not address the higher-codimension generic-vanishing conjecture.

The result is a sharp boundary counterexample, not a classification of all pairs \((H,D)\) for which the weakened implication succeeds.
## References
1. Fanjun Meng, *Generic vanishing conjecture for divisors*, arXiv:2609.11377v1, first public 2026-09-10, MSC 14F17, 14K05.
2. Giuseppe Pareschi and Mihnea Popa, *Regularity on abelian varieties III: relationship with Generic Vanishing and applications*, arXiv:0802.1021.
3. Giuseppe Pareschi and Mihnea Popa, *GV-sheaves, Fourier--Mukai transform, and generic vanishing*, American Journal of Mathematics 133 (2011), arXiv:math/0608127.
