# Review

## Correctness
PASS. The encoder path is exactly isometric, its canonical angle is obtained from the polar decomposition of the source matrix, and the Kraus-trace evaluation reduces the entanglement fidelity to a closed one-variable expression. At the canonical point \(T'(\theta_p)=0\), while the remaining derivative factor has sign determined by the exact positive identity
\[
(1-g)^2-(d-1)^2a^2g=\frac{p(d^2-1+p)}{d(d+1)^2}>0.
\]
The argument covers every integer \(d\ge2\) and every \(0<p<1\), with the excluded endpoint and unproved global optimum stated explicitly.

## Originality
PASS. The closest primary source constructs this comparator and explicitly leaves its fixed-positive-noise exact optimality open. Targeted searches over the source title, canonical polar encoder, fixed-noise rank-one optimality, stationarity, and equivalent AQEC terminology found no statement implying the all-parameter derivative obstruction. Broader iterative AQEC optimization does not imply this source-specific identity.

## Value
PASS. The finding resolves a concrete open finite-noise question about the comparator underlying a recent high-rank AQEC separation. It replaces a numerical/perturbative uncertainty with an explicit analytic improving direction valid uniformly in dimension and noise strength.

## Closest literature and limitations
The closest work is arXiv:2609.00778v1 itself: it proves the leading quadratic high-rank advantage but states that higher-order rank-one corrections and fixed-\(p\) exact optimality of the displayed pair are unresolved. The present theorem does not solve global rank-one optimization or produce \(F_1^{\mathrm{opt}}\); it only proves the displayed pair is not stationary for any \(0<p<1\).

Same-model review: passed. Independent audit: not yet performed.
