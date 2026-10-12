# Review: sharp sampling-collapse transition for constant-step stochastic proximal quadratics

## Correctness — PASS
The two update maps are contractions with affine coefficients \(1/(\kappa+1)\) and \(1/2\). Direct stationary first- and centered-second-moment equations give the displayed risk; symbolic differentiation yields a polynomial whose derivative is positive on the full probability interval and whose endpoint sign crosses at \(1+2\sqrt2\). This establishes a unique global optimizer, including the boundary. Exact rational enumeration and symbolic checks in `verify.py` independently diagnose the algebra; finite experiments are not used as infinite-horizon proof.

## Originality — PASS, with residual priority risk
Inspected sections of Asi–Duchi, Bianchi–Hachem–Salim, and Patrăşcu–Necoara contain general stochastic proximal convergence and stationary principles, not this sharp optimization of the uncorrected sampling law against a fixed equal-weight objective. Défossez–Bach addresses a related sample-allocation bias–variance theme but works with explicit averaged SGD and importance corrections. Targeted searches of published mathematical records did not surface this exact switching polynomial, and related sampling findings concern different algorithms or performance criteria. Search incompleteness and specialized unpublished work remain risks; no priority or independent certification is claimed.

## Value — PASS
The complete policy classification answers a natural finite-dimensional question about how component-selection bias interacts with stationary variance in fixed-step stochastic proximal point. The nontrivial interior-to-deterministic threshold, uniqueness, and distinction between unbiased stationary mean and minimum stationary squared error are mathematically motivated diagnostics for stochastic resolvent algorithms. The phenomenon is not a recommendation to abandon objective components in general; limitations of the deliberately uncorrected toy model are material.

## Closest literature and limitations
The motivating source is Asi–Duchi (arXiv:1810.05633, earliest public 2018-10-12). Further checks include Bianchi–Hachem–Salim (arXiv:1702.04144), Patrăşcu–Necoara (arXiv:1706.06297), and Défossez–Bach (arXiv:1412.0156). The proof assumes two scalar strongly convex quadratics, fixed step, independent samples, and a fixed equal-weight evaluation objective. No broader stochastic optimization or finite-time rate theorem follows.

Self-review: passed. Independent audit: not yet performed.
