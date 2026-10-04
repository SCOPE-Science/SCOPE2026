# Same-model review

## Correctness
**PASS.** The proof reduces by affine covariance and signed-coordinate symmetry to \(C=[-1,1]^n\) with start \(t\mathbf1\). The symmetric MinCE dual reduces to one scalar \(y\); strict concavity gives a unique optimizer, and its stationarity equation is exactly \((n+1)t y^2+(1+t^2)y-(n-1)t=0\). Substitution into the published center map cancels identically. The second centered step follows from signed-permutation symmetry and uniqueness of the MinCE. The bundled checker replays the scalar identities over representative dimensions and both signs of \(t\).

Risk: the computation relies on exact MinCE solutions and on the standard affine covariance of MinCE and polarity. Neither is asserted for an approximate oracle.

## Originality
**PASS.** Statement-level comparison was made against the full text of the 2026 polarity-process paper, the full 1993 Khachiyan-Todd paper that introduced Algorithm IC, general ellipsoidal-duality literature, current published findings returned by semantic searches, and the existing local ledger. The primary paper proves global linear contraction with an existential instance-dependent factor and uses box/skewed-box experiments, but does not state this exact finite trajectory law. Khachiyan-Todd pose convergence of Algorithm IC but do not give this special-case result.

Risk: an older or obscure special-case computation could have escaped the searches; this is retained as a residual risk rather than treated as proof of novelty.

## Value
**PASS.** Boxes and skewed boxes are explicit benchmark families in the primary 2026 study. A dimension-uniform exact two-step law from every main-diagonal start gives a closed-form oracle benchmark for implementations, isolates a large family of trajectories on which the general linear-rate analysis is dramatically non-tight, and supplies an exact test case for future inexact-process stability work. This is a structural trajectory classification, not a routine numerical table entry.

Same-model review: passed. Independent audit: not yet performed.
