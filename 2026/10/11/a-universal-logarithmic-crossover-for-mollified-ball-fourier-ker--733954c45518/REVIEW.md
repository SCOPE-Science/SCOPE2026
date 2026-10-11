# Scientific review: universal logarithmic crossover for mollified-ball Fourier kernels

## Correctness — PASS

The assertion is uniform for each fixed dimension and for profile families with bounded \(W^{2,1}\) norm, not for dimensions tending to infinity or arbitrary rough smoothings. The ball-transform formula is exact; its uniform fixed-order Bessel expansion produces the correct \(r^{-(d+1)/2}\) oscillatory term and an integrable remainder. Uniform Fourier decay of the boundary profile bounds the spatial tail beyond \(\delta^{-1}\). On intermediate logarithmic annuli, the profile tends uniformly to one and periodic averaging of the cosine power reduces the integral to \(\int_0^1 e^{(d+1)\lambda t/2}dt\). Inner/outer edge contributions can be made arbitrarily small relative to \(\log(1/\delta)\). The endpoint coefficient agrees algebraically with the published planar trapezoidal endpoint value. Supplementary exact-normalization checks were executed from `verify_crossover.py`; they are not treated as proofs of the limiting theorem.

## Originality — PASS, with residual risk

Carbery–Seeger's *Mollified disc multipliers* (arXiv:2609.32919v1, full text inspected) treats fixed-exponent multiplier norms and mentions comparability of the planar endpoint kernel norm, not a varying-exponent crossover. The published *Exact leading constant for the endpoint kernel norm of a trapezoidal disc mollifier* (complete RESULT.md inspected) proves just the \((d,\lambda)=(2,0)\) coefficient for a single profile; the present theorem includes it without presenting that old number as new. The new statement quantifies the complete near-critical window, includes all fixed dimensions at least two, and is uniform even when normalized smooth profiles vary with the cutoff. Neither cited fixed-exponent result logically supplies this joint uniform limit. Semantic searches for double-scaling, endpoint Bessel norms, critical windows, arbitrary profiles and Fourier balls found no equivalent published formula. Kanghui Guo's 1997 uniform Bessel \(L^p\) estimates are potentially relevant but only an abstract was inspected, so any detailed relation remains a residual risk; absence from search results is not proof of novelty.

## Value — PASS

At the natural endpoint \(p_c=2d/(d+1)\), the Fourier kernel is exactly at the logarithmic-integrability transition. Fixed-exponent \(L^p\) comparisons on either side do not say how the logarithm interpolates when the exponent moves by the critical \(1/\log(1/\delta)\) width. The universal crossover identifies this scale and its exact all-dimensional shape, independent of a broad class of smoothing profiles. That is a motivated sharp boundary law for spectral cutoff kernels, beyond a routine fixed-parameter constant evaluation.

## Closest literature and limitations

The strongest direct predecessor is the complete published fixed-exponent endpoint coefficient for one planar radial profile. The 2026 Carbery–Seeger manuscript treats the same smoothing family but primarily multiplier-operator bounds. Standard Bessel asymptotics are classical and are not claimed as new. The new theorem addresses kernel \(L^p\)-mass only, and an older equivalence in uniform oscillatory-integral literature cannot be excluded. Independent replication or external audit of this result has not yet occurred.

Same-model review: passed. Independent audit: not yet performed.
