# Review summary

## Correctness — PASS

The ensemble inequality is equivalent to concavity of \(g_c(\mathbf v)=h(\|\mathbf v\|)-h(x)-ch(z)\). On the open Bloch ball, the Schur complement reduces concavity to a two-by-two matrix whose determinant is \(\delta a(Y+Z)(1-Z)+\delta^2Ys-(1-2\delta)XZ\). The determinant threshold has the exact supremum \(a_*\), and a limiting family with \(Y=0\), \(X=s-Z\), \(Z\downarrow0\) proves sharpness. Continuity covers boundary states. The displayed decimal is not a proof premise.

## Originality — PASS

The fully inspected 2026 qubit CQC paper proves the same one-sided ensemble inequality with coefficient \(1/2\) but does not optimize it in the inspected text. The exact optimal coefficient here is defined by a variational formula and shown to be necessary and sufficient. Qian's 2026 state-dependent corrected CQC bound was also inspected; it is incomparable with CQC at two qubits and does not state the one-sided coefficient optimization. Searches of related CQC, information-exclusion, and sharp-constant literature did not identify a statement implying this optimization. This is a best-knowledge assessment; one older related full text remained inaccessible.

## Value — PASS

The coefficient is a natural sharp constant for the central entropy inequality underlying complementary-correlation bounds. Improving it yields the explicit additional term \((2c_*-1)I(X_A:Z_B)\), in a two-qubit lower bound for total mutual information whenever the cross-basis table is available. This is more than a numerical refinement: the proof identifies the exact continuous optimization and proves no larger coefficient is universal.

Self-review: passed. Independent audit: not yet performed.
