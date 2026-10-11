# Review of the exact cubic-aperture fourth-moment theorem

## Correctness

**PASS.** All eight coefficient magnitudes are fixed at one, normalized Haar measure is explicit, and every quantifier is bounded or specified. The core identity \(\mathcal M=104+4|S_1|^2+8\operatorname{Re}(D\overline{S_2})\) follows from exact convolution arithmetic, independently checked by `checker.py`. Newton's identity for the four numbers \(1,A,B,C\) proves the lower bound and forces precisely two negative normalized pair phases and \(D=1\). All convolution terms are separately bounded for the maximum, with equality forcing all normalized coefficients to one. The root-alphabet counts use a free \(q^4\)-element modulation action. The finite-sampling claim requires all three cyclic orders at least three so Fourier-convolution exponents remain unaliased. Aperiodic parity and maximum checks were executed; finite enumerations are not used as universal proof.

## Originality

**PASS with residual bibliographic risk.** The relevant exact objects are *one* \(2\times2\times2\) unimodular array and its full aperiodic autocorrelation-square sum. Pai--Chen (arXiv:2102.04043v1, Sections II--IV and Theorem 9) and Zhang--Fan--Mesnager (arXiv:2107.11599v1, Sections 2--4 and Theorems 1--2) construct *pairs* of 2-D arrays with cancelling summed correlations. Their conclusions neither upper nor lower bound the single-array three-dimensional fourth moment, nor classify its minimizers. The inspected Barker-array sources consider 2-D small-correlation binary arrays rather than global unimodular optimization of this support. Closest retrieved published mathematical findings involve four-point single-variable moment minima, Walsh four-point phase flatness, and three-sparse Fourier support: the supports, groups, and invariants do not yield the present claim. An unlocated classical three-dimensional single-array calculation remains a risk; no exhaustive novelty claim is made.

## Value

**PASS.** The complete \(2\times2\times2\) Fourier cube is the smallest fully three-dimensional Cartesian aperture. Its exact single-array fourth moment governs total aperiodic autocorrelation sidelobe energy and the merit factor. The theorem gives a nontrivial sharp lower value \(88\) (rather than the unmodulated \(216\)), identifies all minimizing phases by a three-orbit quadratic-Boolean path structure, shows no complex-phase improvement over binary phases, and determines exactly when restricted polyphase alphabets achieve the optimum. This is a structurally motivated exact extremal classification, not an arbitrary fixed numerical instance. The result does not extend to larger cubes or determine optimal odd-alphabet moments.

Same-model review: passed. Independent audit: not yet performed.
