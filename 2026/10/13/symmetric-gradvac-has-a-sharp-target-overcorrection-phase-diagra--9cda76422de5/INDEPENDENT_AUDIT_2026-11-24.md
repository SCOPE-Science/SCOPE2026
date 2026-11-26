# Independent mathematical audit

## correctness

PASS

For normalized gradients on angles 0 and θ, the published coefficient after removing the original norm ratio is λ=sin(θ−γ)/sin γ>0, where γ=arccos τ lies in (0,θ). The normalized-coordinate sum e₁+λe₂ is the vector on angle θ−γ multiplied by sin θ/sin γ>0; swapping gradients reflects it to angle γ. The final separation |θ−2γ| lies in [0,θ) and gives the claimed cosine formula by the double-angle identities. As τ increases, γ decreases, so the separation has a unique minimum at γ=θ/2, with the claimed strict monotonicity of the cosine on the two sides. The endpoint γ→0 swaps directions and gives C→c, not a defined update at τ=1. Equating |θ−2γ| with γ gives only γ=θ/3 in the active range and the inactive γ=θ at its boundary. For the inequality signs use C−τ=−2 sin((θ−γ)/2) sin((θ−3γ)/2), with these arguments in ranges where the signs are as stated. An independent rational spot check with orthogonal originals found that τ=3/5 and τ=4/5, on opposite sides of the peak, both give C=24/25. The bundled random and deterministic checker was inspected, not run; it is a numerical transcription guard, not a proof.

## originality

PASS

The defining one-sided law and the two-task use of both ordered updates are prior work. The distinct result computes the mutual alignment of their two outputs, and resolves its monotonicity and its comparison with the target on the full active interval. Actual source comparisons did not establish coverage of that phase diagram by a prior theorem. The closest catalogue threshold comparison concerns CAGrad, not GradVac.

## value

PASS

The target cosine is central to what GradVac controls, but the two corrected gradients are what enters aggregation. The exact distinction between the peak and target-equality boundary shows that larger targets can already reduce actual final alignment even while it remains above the target, and that near the singular endpoint alignment returns to its original value. This is a concrete diagnostic for interpreting the idealized update, not a claimed training failure or empirical tuning optimum.

The dated certificate retains the supplied scientific assessment, sources and limitations.
