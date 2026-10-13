# Review

## Correctness
PASS. The final claim is a direct all-parameter consequence of the source's displayed packet and complement costs. For every odd \(d\ge3\) and every \(1\le n<d\), the complement contains \(d-n\ge1\) local edges. Under \(0<p_{\mathrm{gate}}\le p_{\mathrm{net}}<1\), monotonicity of \(-\log\) gives \(w_{\mathrm{net}}\le w_{\mathrm{gate}}\), and positivity gives \(w_{\mathrm{gate}}\le(d-n)w_{\mathrm{gate}}\). The strict and tie boundaries are fully stated. No simulation is used to extend a finite check to an infinite claim.

## Originality
PASS. Exact-source, alias, parameter, and implication searches did not locate the all-\(n\) consequence. The closest public source-specific review already observes that the half-distance rule is heuristic because other matching classes are not excluded, but it does not notice that the displayed packet-versus-complement comparison itself has no half-distance threshold. Earlier correlated surface-code work does not contain the multi-gate-teleportation object or this logical-complement parameterization.

## Value
PASS. The source elevates \(n_{\max}^{\mathrm{corr}}=\lceil d/2\rceil\) to a central design rule. The finding identifies a structural mismatch between that ceiling and its stated local rationale: the rationale continues to favor the packet edge all the way to \(n=d-1\). This cleanly separates what the local argument proves from what would require a global detector-error-model theorem and therefore changes how the proposed design rule should be interpreted.

## Closest literature and limitations
The anchor itself is the closest source and openly warns that a third matching class could be cheaper. That unresolved global issue is preserved, not dismissed. Fowler's correlated surface-code decoding work is broader background but does not imply the packet-specific statement. The result does not claim fault tolerance for packets above half distance; it proves only that the logical-complement comparison cannot establish a half-distance upper bound.

Self-review: passed. Independent audit: not yet performed.
