# Self-review

## Correctness
PASS. Matching the closed-loop trace and determinant to the deadbeat polynomial gives a unique feedback for each admissible scalar actuator. The feedback-norm minimization is a sharp Cauchy--Schwarz inequality. The closed-loop matrix is rank-one nilpotent, so its single nonzero singular value equals its Frobenius norm, and a second sharp square inequality minimizes that transient norm. Both equality conditions give the same squared actuator coordinates.

The exact rational witness
\[
A=\operatorname{diag}\!\left(\frac45,\frac35\right),
\qquad
b=\left(\frac45,\frac35\right)^{\mathsf T},
\qquad
k=(4,-3)^{\mathsf T}
\]
replays all identities exactly and gives
\[
\|A-bk^{\mathsf T}\|_2=\frac{24}{5},
\qquad
(A-bk^{\mathsf T})^2=0.
\]

## Originality
PASS with explicit residual risk. Minimum-gain minimum-time deadbeat control is classical, and the 1988 article with that title is treated as prior work rather than novelty. Full inspection of later robust-deadbeat and arbitrary-pole-placement sources shows that they optimize feedback or robustness for a fixed reachable pair. A later input-assignment/gain paper does co-design the input matrix, but for a different objective that shifts one dominant eigenvalue while preserving the remaining eigenstructure.

Targeted searches did not locate the joint two-mode statement that the actuator minimizing deadbeat gain also exactly minimizes the nilpotent one-step transient, nor the sharp formulas or modal-gap asymptotic. The inaccessible body of the 1988 paper remains the main residual risk and is not treated as whole-document noncoverage.

## Value
PASS. Minimum feedback gain and transient robustness are standard concerns in pole assignment, and deadbeat matrices can be strongly nonnormal despite having all poles at zero. The finding solves the minimal continuous actuator-direction problem exactly and identifies an unavoidable reciprocal modal-gap cost. The example shows a large transient even for a stable diagonal plant and even after optimizing the actuator direction, so the fact is more than a routine pole-placement calculation.

## Closest literature and limitations
The closest literature includes classical minimum-gain deadbeat design, robust deadbeat regulation, minimum-gain exact pole placement, and later joint input-assignment/gain design. The theorem is restricted to two orthogonal stable modes, one unit scalar actuator, exact state feedback, and Euclidean norms. Higher-dimensional, nonnormal, constrained, noisy, and finite-precision settings are not covered.

Self-review: passed. Independent audit: not yet performed.
