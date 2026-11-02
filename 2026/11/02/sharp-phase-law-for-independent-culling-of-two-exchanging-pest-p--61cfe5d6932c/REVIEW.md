# Scientific review — sharp phase law for two-patch culling

## Correctness: PASS

The model, positive parameter domain, order of jumps, and one-period return map are explicit in `RESULT.md`. Matrix-exponential algebra establishes the exact trace defect \(B\sinh(\kappa\delta)\sinh(\kappa(T-\delta))\) and invariant determinant. Strict positivity and the positive determinant yield two distinct positive Floquet eigenvalues; trace monotonicity at fixed determinant and hyperbolic reflection prove the unique minimizing and maximizing phases. The threshold law \(H=1+\Delta\) follows for \(\Delta<1\). The exact rational half-period example independently proves genuine phase-induced stability reversal. Replaying `check.py` gave 9,005 successful finite assertions; this code is supplemental to, not a replacement for, the analytic proof. Degenerate zero migration or absent culling is outside the strict claim.

## Originality: PASS within inspected evidence, with residual priority risk

Terry (2010) treats independent culls for a delayed, stage-structured two-patch pest population. Georgescu, Dimitriu and Sinclair (2010) develop a simultaneous two-patch impulse and Floquet framework for an SI pest model. The full texts of both works were inspected; neither contained the exact universal phase trace identity and stability interval for the claimed constant-generator local-cull setting. Browne, Smith and Bourouiba (2014, Theorem 5) prove a local synchrony optimum for a different pulse-vaccination SIR model under identical-patch/no-infected-movement assumptions, with numerical phase effects in broader settings. Their full text was inspected and does not imply the present all-asymmetric direct-cull constant matrix trace identity. Ives and Settle (1997) and Byers and Castle (2005) establish qualitative synchrony and pest dispersal ideas, including simulation evidence for stronger synchronized control; these are acknowledged as already known. Ranked searches of published mathematical results  showed no directly covering theorem. The 2005 and 1997 full articles were not available, and an unknown stronger general positive-matrix result remains a historical-priority risk; search absence is not novelty proof.

## Value: PASS

This classification provides a sharp all-parameter finite-form intervention-timing law for two exchanging patches and an exact culling-phase threshold at which pest eradication becomes pest growth without changing overall spray strength or frequency. That is a substantive, interpretable consequence for a classical spatial pest-management model, not a parameter substitution or bare illustrative computation. The result does not make empirical, nonlinear eradication, or economic-cost claims.

## Limits of verification

Analytical arguments were checked directly; numerical and rational evidence were reproduced from the standalone package. The scientific review is not independent and cannot certify complete historical priority. The proof controls a constant-coefficient, two-patch linearization only.

Self-review: passed. Independent audit: not yet performed.
