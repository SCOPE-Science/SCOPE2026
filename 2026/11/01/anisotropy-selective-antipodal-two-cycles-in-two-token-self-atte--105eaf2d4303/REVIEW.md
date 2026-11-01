# Anisotropy-selective antipodal two-cycles in two-token self-attention

## Correctness
**PASS.** A direct normalized-map calculation gives a least-period-two antipodal eigencycle whenever \(\eta s_j\tanh\alpha>1\). At both orbit states the softmax score derivative vanishes on the tangent bundle; the entire tangent Jacobian decomposes into explicit two-by-two spectral blocks. The original map's sign equivariance squares their eigenvalues into the exact Floquet multipliers. Algebraic unit-disk inequalities establish the sharp necessary-and-sufficient temperature and gain conditions, including strict-instability and nonhyperbolic boundaries. Rational and original-map finite-difference checks agree, but are auxiliary to the proof.

## Originality
**PASS under inspected evidence.** Altafini's discrete normalized attention paper arXiv:2610.13518v1 uses a simple positive leading value eigenvalue and classifies equilibria, not this negative-definite flip cycle. Gao–Yang–Chen arXiv:2609.28448v1 already proves repulsive period-two cluster exchange in an isotropic, self-masked map; that existence phenomenon is not claimed as new. Kuehn–Yoon arXiv:2604.26085v1 proves negative-definite two-token spectral selection for a continuous-time gradient flow whose query–key metric is tied to the value matrix. The present independent positive score matrix and discrete step are outside their hypotheses, and none establishes the two-edge iff criterion. Targeted record queries did not reveal decisive coverage, but historical priority remains provisional. The exact search comparisons, source material read, and residual risks are in AUDIT.json.

## Mathematical value
**PASS.** The theorem distinguishes a temperature gap controlled by the second-strongest negative value eigenmode from a sharp gain onset controlled by the weakest mode, giving a genuine finite-step phase diagram. At isotropy no antipodal eigencycle can be exponentially attracting. A dimension-three example has exact nonzero Floquet multipliers \(1/4,1/4,9/16\), making the threshold reproducible and independently testable.

## Scope and risks
Only the explicit antipodal eigenvector two-cycle is classified, locally, with two labeled tokens and self-inclusive softmax weights. Other cycles, global basins, undefined normalization states, and nonlinear dynamics at neutral thresholds are outside the claim. Full historical priority and independent mathematics verification remain outstanding.

Self-review: passed. Independent audit: not yet performed.
