# A two-dimensional obstruction to unrestricted subspace intersection of woven controlled \(K\)-\(g\)-fusion frames
## Finding
Theorem 2.9 of Ghosh and Samanta asserts that intersecting every component of two woven continuous controlled \(K\)-\(g\)-fusion frames with an arbitrary closed subspace again gives woven continuous controlled \(K\)-\(g\)-fusion frames for that subspace. The assertion is false even in the elementary specialization \(K=T=U=I\), with a two-point counting measure and two identical Parseval families.

Let \(H=\mathbb{R}^2\) with orthonormal basis \(e_1,e_2\). Let the measure space be \(X=\{1,2\}\) with counting measure, use unit weights, and define
\[
F_1=G_1=\operatorname{span}\{e_1\},\qquad F_2=G_2=\operatorname{span}\{e_2\}.
\]
For each component take the coefficient Hilbert space to be that component and take the coefficient map to be the identity on it. Because the two families are identical, every weaving has energy
\[
\|P_{F_1}f\|^2+\|P_{F_2}f\|^2=\|f\|^2,
\]
so every weaving is Parseval.

Now let
\[
W=\operatorname{span}\{e_1+e_2\}.
\]
Then \(F_1\cap W=F_2\cap W=G_1\cap W=G_2\cap W=\{0\}\). Hence every intersected weaving has energy zero on every nonzero vector of \(W\), and therefore cannot have a positive lower frame bound.

## Assumptions and scope
The counterexample is entirely inside the source's discrete specialization of the continuous framework: a finite counting measure is used, \(K=T=U=I\), all weights are one, and the two woven families are identical. Thus no subtlety about measurable fields, unbounded operators, or nontrivial control operators is needed.

The claim corrected here is the unrestricted inheritance statement in Theorem 2.9. The result does not assert that projection commutation is necessary for every individual family to survive a particular restriction. It identifies the exact condition under which the projection identity used in the published proof is valid and gives a sufficient repair in the ordinary fusion-frame specialization.

## Proof
For any choice of measurable subset \(\sigma\subseteq X\), the weaving chooses the \(F\)-component on \(\sigma\) and the \(G\)-component on its complement. Since \(F_i=G_i\) for both indices, every weaving consists of the same two coordinate lines. Therefore, for every \(f=f_1e_1+f_2e_2\),
\[
\sum_{i=1}^2\|P_{F_i}f\|^2=|f_1|^2+|f_2|^2=\|f\|^2.
\]
This proves the original families have universal lower and upper weaving bounds equal to one.

The line \(W\) contains no nonzero multiple of either \(e_1\) or \(e_2\), so each component intersection with \(W\) is \(\{0\}\). Hence for nonzero \(f\in W\), the energy of every intersected weaving is zero, contradicting any inequality with a positive lower bound.

The source proof asserts, for a closed component \(M\), that
\[
P_{M\cap W}=P_M P_W.
\]
For orthogonal projections this identity holds if and only if \(P_M\) and \(P_W\) commute. Indeed, if the identity holds, then \(P_M P_W\) is self-adjoint, so
\[
P_M P_W=(P_M P_W)^*=P_W P_M.
\]
Conversely, if the projections commute, then \(P_M P_W\) is an orthogonal projection, and its range is exactly \(M\cap W\).

In the counterexample,
\[
P_W=\frac12\begin{pmatrix}1&1\\1&1\end{pmatrix},\qquad
P_{F_1}=\begin{pmatrix}1&0\\0&0\end{pmatrix},
\]
so
\[
P_{F_1}P_W=\frac12\begin{pmatrix}1&1\\0&0\end{pmatrix}\neq0=P_{F_1\cap W}.
\]
This pinpoints the failed step.

For a repaired ordinary fusion-frame statement, suppose every component projection of both woven families commutes with \(P_W\). Then for every \(f\in W\),
\[
P_Mf=P_MP_Wf=P_{M\cap W}f.
\]
Thus each restricted weaving has exactly the same energy on \(W\) as the corresponding original weaving, and the original universal lower and upper bounds are inherited unchanged.

## Verification
The calculation is symbolic and finite-dimensional. The Parseval identity is exact, all four intersections with \(W\) are exactly zero, and the displayed matrices directly verify that the product of the two noncommuting orthogonal projections is not the intersection projection. No finite experiment is being used as evidence for an infinite-dimensional assertion.

The projection-product equivalence is proved abstractly above. The source's theorem and proof were checked in the full text, including the sentence that identifies \(P_{F(x)\cap W}\) with \(P_{F(x)}P_W\). Earlier fusion-frame literature was checked for the same intersection mechanism.

## Relationship to prior work
Bhandari and Mukherjee's 2017 work on atomic subspaces explicitly records that commuting orthogonal projections multiply to the projection onto the intersection and assumes this commutation in its fusion-frame and \(K\)-fusion-frame intersection theorems. This is prior coverage of the sufficient commutation mechanism, not of the present counterexample to the later unrestricted statement.

A 2025 Hilbert \(C^*\)-module analogue by Ouahidi and Rossafi includes explicit commutation hypotheses between each component projection and the subspace projection before asserting the analogous intersection inheritance property. That later formulation is consistent with the obstruction exhibited here.

Targeted searches for the source identifier, theorem number, closed-subspace intersection, projection-product aliases, and counterexample formulations found no indexed correction containing this explicit two-dimensional obstruction. This does not exclude an unindexed erratum, thesis remark, or informal observation.

## Limitations
Only Theorem 2.9's unrestricted closed-subspace conclusion is assessed. No claim is made about unrelated results in the paper. The clean bound-preserving repair proved here is stated for the ordinary specialization \(K=T=U=I\); a fully controlled restriction theorem can require additional compatibility of the control and \(K\)-operators with the subspace, so projection commutation alone is not claimed to repair every generalized formulation.

## References
Prasenjit Ghosh and T. K. Samanta, *Weaving continuous controlled K-g-fusion frames in Hilbert spaces*, arXiv:2111.03389v1, first posted 2021-11-05.

Animesh Bhandari and Saikat Mukherjee, *Atomic subspaces for operators*, arXiv:1705.06042, 2017.

El Houcine Ouahidi and Mohamed Rossafi, *Weaving Continuous Controlled K-G-Fusion Frames in Hilbert C*-Modules*, International Journal of Analysis and Applications 23 (2025), 278, doi:10.28924/2291-8639-23-2025-278.
