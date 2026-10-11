# The woven \(K\)-frame perturbation denominator must be \(1+\mu\), not \(1-\mu\)

## Finding
Theorem 5.4 of Gang Wang's 2024 paper gives a perturbation criterion for two \(K\)-frames in an \(n\)-Hilbert space. Its printed universal lower bound is
\[
A_p\min\left\{1,\left(\frac{1-\lambda}{1-\mu}\right)^2\right\}.
\]
The proof instead derives
\[
(1+\mu)\,E_q(I)^{1/2}\ge(1-\lambda)\,E_p(I)^{1/2},
\]
so the valid bound furnished by that proof is
\[
A_p\min\left\{1,\left(\frac{1-\lambda}{1+\mu}\right)^2\right\}.
\]
The printed \(1-\mu\) denominator is false. A one-parameter family makes the corrected constant exact.

## Assumptions and scope
Use the standard \(2\)-inner product on
\[
H=\mathbb C^2
\]
and fix \(c_2=e_2\). The induced Hilbert space \(H_C\) is one-dimensional and may be identified with \(\mathbb C e_1\), with
\[
\|x,e_2\|=|x_1|.
\]
Let \(K=I\). Fix \(t\in(0,1)\) and put
\[
r=\frac{1-t}{1+t}.
\]
Set
\[
f_{p1}=e_1,\qquad f_{q1}=r e_1,
\]
and \(f_{pj}=f_{qj}=0\) for \(j\ge2\). Then \(F_p\) has exact \(K\)-frame bounds \(1\) and \(F_q\) has exact bounds \(r^2\).

The result corrects the quantitative lower bound in Theorem 5.4. It does not claim that the theorem's perturbation hypothesis is necessary.

## Proof
Take
\[
\lambda=\mu=t.
\]
For \(I\subset\mathbb N\), if \(1\notin I\) both sides of the source perturbation inequality vanish. If \(1\in I\), after cancelling \(|f_1|\) the inequality becomes
\[
1-r\le t(1+r).
\]
For the chosen \(r\),
\[
1-r=\frac{2t}{1+t}=t(1+r),
\]
so the hypothesis holds with equality.

The printed theorem assigns lower bound
\[
1\cdot\min\left\{1,\left(\frac{1-t}{1-t}\right)^2\right\}=1.
\]
The weave selecting \(F_q\) at index \(1\) has energy
\[
r^2|f_1|^2,
\]
so its exact lower \(K\)-frame bound is \(r^2<1\). This disproves the printed constant.

For the repair, write the coefficient energies on \(I\) as \(E_p(I)\), \(E_q(I)\), and \(E_{p-q}(I)\). The triangle inequality and the source hypothesis give
\[
E_p(I)^{1/2}
\le E_q(I)^{1/2}+E_{p-q}(I)^{1/2}
\le(1+\mu)E_q(I)^{1/2}+\lambda E_p(I)^{1/2}.
\]
Hence
\[
E_q(I)^{1/2}\ge\frac{1-\lambda}{1+\mu}E_p(I)^{1/2}.
\]
Applying this on the complementary part of an arbitrary weave yields
\[
E_{\mathrm{weave}}(f)\ge
A_p\min\left\{1,\left(\frac{1-\lambda}{1+\mu}\right)^2\right\}
\|K^*f\|^2.
\]
On the counterexample family, this factor is exactly \(r^2\), the exact lower bound of the worst weave.

## Verification
The publisher PDF was inspected at the complete statement and proof of Theorem 5.4. The statement displays \(1-\mu\) in the denominator. The proof explicitly rearranges the estimate as
\[
(1+\mu)E_q(I)^{1/2}\ge(1-\lambda)E_p(I)^{1/2},
\]
which forces \(1+\mu\).

The counterexample is symbolic and covers every subset \(I\) by the cases \(1\in I\) and \(1\notin I\). No numerical experiment is used.

The article was published on 30 August 2024 and lists \(42C15\) first in its Mathematics Subject Classification.

## Relationship to prior work
Deepshikha and Vashisht's earlier full-text paper on weaving \(K\)-frames proves a Paley--Wiener type perturbation theorem with a different hypothesis and separately derived quantitative constants. It does not imply the erroneous \(1-\mu\) denominator in Wang's theorem.

Exact-title, theorem-number, DOI, denominator, perturbation, correction, and erratum searches located no indexed correction containing the sharp family above. Nearby results on woven \(K\)-frame reconstruction and controlled-\(K\)-frame perturbations concern different hypotheses and implications.

## Limitations
The corrected theorem is a sufficient perturbation result. No necessity claim is made for its subsetwise hypothesis.

The sharpness statement concerns the universal constant furnished by this theorem. Additional geometry of particular frames can yield stronger bounds.

An unindexed author note or informal correction could contain the same denominator observation.

## References
1. G. Wang, *Some properties of weaving \(K\)-frames in \(n\)-Hilbert space*, AIMS Mathematics 9(9) (2024), 25438--25456, DOI 10.3934/math.20241242.
2. Deepshikha and L. K. Vashisht, *Weaving \(K\)-Frames in Hilbert Spaces*, arXiv:1710.09562v4.
