# Nef and big non-movable divisors of fixed square \(4\) on one surface
## Finding
There exists one smooth projective complex surface \(\widetilde X\) and, for every odd integer \(n\ge 3\), a reduced simple-normal-crossings divisor
\[
D_n\subset\widetilde X
\]
such that
\[
D_n\ \text{is nef and big},\qquad D_n^2=4,
\]
and
\[
h^0\!\left(\widetilde X,\mathcal O_{\widetilde X}(mD_n)\right)=1
\quad\text{for every integer}\quad
1\le m<\frac{n^2}{4}+1.
\]
Consequently, on this one fixed surface, the first moving multiple of nef and big divisors with fixed self-intersection \(4\) is unbounded.

With Liu's notation, the branch divisor can be chosen once and for all so that
\[
D_n=\widetilde C_F+\widetilde C_n,
\]
where the two components are smooth and meet transversely in exactly five points. Their intersection data are
\[
\widetilde C_F^2=\widetilde C_n^2=-3,\qquad
\widetilde C_F\cdot\widetilde C_n=5,
\]
so
\[
D_n\cdot\widetilde C_F=D_n\cdot\widetilde C_n=2.
\]
Their genera are
\[
g(\widetilde C_F)=2,\qquad g(\widetilde C_n)=n^2+5.
\]

## Assumptions and scope
Work over \(\mathbf C\). Let \(E\) be a smooth elliptic curve,
\[
Y=E\times E,\qquad F=\{0\}\times E,\qquad G=E\times\{0\}.
\]
For each odd integer \(n\ge3\), set
\[
\Gamma_n=\ker\!\bigl((x,y)\mapsto nx+2y\bigr),\qquad A_n=F+\Gamma_n.
\]
Liu proves
\[
F\cap\Gamma_n=\{0\}\times E[2],\qquad
F\cdot\Gamma_n=4,\qquad G\cdot\Gamma_n=n^2,
\]
and fixes three points
\[
S=\{p_1,p_2,p_3\}\subset\{0\}\times E[2]
\]
independently of \(n\).

Put \(R=F+G\). We choose one branch divisor \(B\in|2R|\) satisfying the simultaneous genericity conditions below. The resulting double cover \(f:X\to Y\), the three chosen lifts \(q_i\in f^{-1}(p_i)\), and the blowup
\[
\pi:\widetilde X\to X
\]
are therefore independent of \(n\).

The result does not make \(D_n\) prime or irreducible. It strengthens the positivity of Liu's reducible examples from positive self-intersection to nef and big while preserving their long non-moving range.

## Proof
The line bundle \(\mathcal O_Y(2R)\) is basepoint-free, and
\[
h^0(Y,\mathcal O_Y(2R))=4,
\]
so \(|2R|\cong\mathbf P^3\). For each fixed smooth curve among
\[
F,\Gamma_3,\Gamma_5,\Gamma_7,\ldots,
\]
Bertini's theorem gives a dense Zariski-open set of members of \(|2R|\) that are smooth and meet that curve transversely. Avoiding the four fixed points \(\{0\}\times E[2]\) is also a dense open condition. A projective space over the uncountable field \(\mathbf C\) is not the union of countably many proper closed subsets. Hence one may choose a single
\[
B\in|2R|
\]
that is smooth, avoids all four points of \(\{0\}\times E[2]\), and is transverse to \(F\) and to every \(\Gamma_n\) for odd \(n\ge3\).

Let \(f:X\to Y\) be the double cover branched along \(B\), and put
\[
C_F=f^{-1}(F),\qquad C_n=f^{-1}(\Gamma_n).
\]
Transversality makes these curves smooth. Their branch degrees are
\[
B\cdot F=2
\]
and
\[
B\cdot\Gamma_n=2(F+G)\cdot\Gamma_n=2(n^2+4).
\]
Both are positive, so the double covers are connected and \(C_F,C_n\) are irreducible. Riemann--Hurwitz gives
\[
g(C_F)=2,\qquad g(C_n)=n^2+5.
\]

Since \(B\) avoids \(F\cap\Gamma_n\), the cover is étale over the four common points. Each has two lifts, hence
\[
C_F\cdot C_n=2(F\cdot\Gamma_n)=8,
\]
and all eight intersections are transverse.

Choose one lift \(q_i\in f^{-1}(p_i)\) for each of the three fixed points and blow up these three points. Let \(\widetilde C_F,\widetilde C_n\) be the strict transforms. Since
\[
C_F^2=2F^2=0,\qquad C_n^2=2\Gamma_n^2=0,
\]
the three common blowups give
\[
\widetilde C_F^2=\widetilde C_n^2=-3,\qquad
\widetilde C_F\cdot\widetilde C_n=8-3=5.
\]
Moreover Liu's divisor
\[
D_n=\pi^*f^*A_n-2(E_1+E_2+E_3)
\]
is exactly
\[
D_n=\widetilde C_F+\widetilde C_n.
\]
The two smooth components retain the five unblown transverse intersections, so \(D_n\) is reduced and simple normal crossings.

Now
\[
D_n\cdot\widetilde C_F=-3+5=2,\qquad
D_n\cdot\widetilde C_n=-3+5=2.
\]
If \(Z\) is any irreducible curve on \(\widetilde X\) different from both components, intersection multiplicities on a smooth surface give
\[
\widetilde C_F\cdot Z\ge0,\qquad \widetilde C_n\cdot Z\ge0.
\]
Thus \(D_n\cdot Z\ge0\), proving that \(D_n\) is nef. Its square is
\[
D_n^2=(-3)+(-3)+2\cdot5=4.
\]
A nef divisor of positive square on a smooth projective surface is big.

Finally, Liu's section calculation applies unchanged to this more generic branch choice: it uses the double-cover decomposition, the fixed set \(S\), and divisor classes. It gives
\[
h^0\!\left(\widetilde X,\mathcal O_{\widetilde X}(mD_n)\right)=1
\quad\text{for}\quad
1\le m<\frac{n^2}{4}+1.
\]
As \(n\) grows while \(\widetilde X\) stays fixed, the non-moving range is unbounded.

## Verification
The simultaneous genericity, irreducibility, and nefness arguments are symbolic and apply to every odd \(n\ge3\); they are not inferred from finite experiments.

The accompanying `verify.py` independently checks the intersection identities, branch degrees, component genera, post-blowup intersection matrix, intersections of \(D_n\) with its two components, and \(D_n^2=4\) over a large finite regression range. It also checks the integer range corresponding to
\[
1\le m<\frac{n^2}{4}+1
\]
for sample odd values. The saved output in `verification_output.txt` ends in `VERIFY_OK`.

The source cohomology calculation is not replaced by the script; it is used as a proved input after inspection of the actual source proof.

## Relationship to prior work
Liu constructs the same fixed-surface family \(D_n\), proves
\[
D_n^2=4
\]
and
\[
h^0\!\left(\widetilde X,\mathcal O_{\widetilde X}(mD_n)\right)=1
\quad\text{for}\quad
1\le m<\frac{n^2}{4}+1,
\]
and notes that the divisors are reducible. His paper does not state that the \(D_n\) can be chosen nef or simple normal crossings. The explicit non-nef divisor in the section calculation is a different auxiliary divisor on the abelian surface.

Ciliberto--Knutsen--Lesieutre--Lozovanu--Miranda--Mustopa--Testa formulate the moving-multiple question and discuss positivity hypotheses, including nef and big cones, but their work predates Liu's counterexample and does not contain this fixed-square nef-and-big strengthening.

The new step is to exploit the freedom in Liu's branch member: one simultaneous transverse choice makes the two pullback components smooth, after which their post-blowup intersection matrix forces nefness.

## Limitations
The divisors \(D_n\) remain reducible, so this does not answer Liu's question of whether the counterexample can be made prime or irreducible. It also does not compute the exact first integer \(m\) for which \(|mD_n|\) moves; only the proven lower range is asserted.

Literature searches can miss unindexed or differently phrased observations. The originality conclusion is limited to the inspected primary texts and the targeted searches recorded in the review data.

## References
1. J. Liu, *An example of a very non-movable effective divisor*, arXiv:2605.20594v1, first posted 20 May 2026, primary MSC 14J29.
2. C. Ciliberto, A. L. Knutsen, J. Lesieutre, V. Lozovanu, R. Miranda, Y. Mustopa, and D. Testa, *A few questions about curves on surfaces*, arXiv:1511.06618v1; Rend. Circ. Mat. Palermo 66 (2017), 195--204.
