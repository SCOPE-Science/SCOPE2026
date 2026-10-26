# Scientific review: first-harmonic semicircle projection

## Correctness — PASS
The analytic Gram covariance has mutually orthogonal centered Cartesian coordinates; this yields the explicit symmetric projector kernel. Pairing opposite arc points reduces the global absolute row integral to a maximum of two scalar expressions. For \(0\le\sin\theta\le1/3\), concavity in the paired source coordinate and pointwise monotonicity prove the endpoint comparison. For \(1/3\le\sin\theta\le1\), a convex Cauchy--Schwarz diagonal bound is strictly below \(2\), while a rationally certified negative-kernel witness makes the endpoint norm strictly greater than \(2\). Two analytic zeros give the exact split integral and the claimed sharp value. Sign inputs attain it on \(L^\infty\). The symmetric kernel gives the matching \(L^1\) norm. Replayed standalone `verify.py`: 48 checks passed. Numerical samples do not substitute for continuum proofs.

## Originality — PASS within inspected evidence
Full-text reading of Huybrechs (2010), especially half-range orthogonal-polynomial bases, Fourier-extension stability and numerical sections, identifies the same approximation setting but no explicit sharp degree-one endpoint norm. Full-text sections on \(L^p\) least-squares projector stability in Hangelbroek et al. (arXiv:1005.2424) provide general bounds for other kernel-generated spaces, not a covering exact constant. The published cyclic three-frequency projection calculation applies to a full finite Fourier group rather than continuous arclength on a semicircle, with a distinct Gram kernel. Targeted publication and mathematical-record searches found no stronger implication. Residual risk: unindexed half-range Fourier-extension calculations and a month-dated 2009 technical report. Search failure alone is not treated as proof of global novelty.

## Value — PASS
This sharp constant measures the worst-case amplification of the lowest nontrivial continuous Fourier-extension least-squares fit on a natural half-period interval. The result identifies the extremal evaluation geometry and exhibits a rigorous \(>2\) instability even though the corresponding full-period projector has norm about \(1.436\). Endpoint localization requires a nontrivial continuum comparison, not merely integrating a known kernel. It offers a precise baseline for boundary effects in nonperiodic Fourier least squares, without claiming higher-degree consequences.

## Boundaries and status
No general arc-opening-angle or higher-degree theorem is asserted. Bibliographic priority is provisional. Independent mathematical and bibliographic assessment remains open.

Self-review: passed. Independent audit: not yet performed.
