# Independent mathematical audit

## correctness

PASS

Reconstructed the Wigner polynomial independently by differentiating the normalized Fourier–Gaussian generating function exp(a²−2iap) for the y-moments and using the explicit h₂. Verified the factorization, saddle Hessian and lower-bound test point exactly (python review_evidence/finite_checks.py, section labelled 5). In polar variables the discriminant has no positive-root upper branch; two distinct positive roots occur exactly for cos(2θ)<√2t−√(1+t²). The threshold increases strictly from −1 and crosses 1 only at 2√2. Below the crossing the open radial interval over each of the two angular arcs is diffeomorphic to an open rectangle by radial interpolation, and each boundary closes into a single simple loop where the roots coalesce. The angular derivative is nonzero at those coalescences, so the loop is smooth. Above the crossing the roots are smooth everywhere and bound the one annulus. At the threshold the exact factor 16[(q²+p²−3/4)²−p²] gives the two unit circles, transverse at (±√3/2,0) with polynomial Hessian diag(96,−32); the sign criterion or the two open polar arcs give precisely two crescents. Radial and angular derivatives can vanish on the nodal set only at these saddles; the origin is positive. For the logarithmic limit the earliest negative radius is on the p-axis, with tR_min²→1/√2. The uniform degree-four Gaussian tail bound then gives the required upper logarithmic bound. At p₀²=1/(√2t), q=0, the polynomial is t²−2√2t, and its gradient is O(√t) on a disk of radius t² there. The sign remains uniformly ≤−ct, giving a lower bound of constant × t⁵ × exp(−1/(√2t)−O(t^(3/2))). The bounds squeeze the stated rate, not a prefactor. The Gaussian envelope is positive; the stated Hessian eigenvalues are for the polynomial, not W itself. Both circles are allowed by the corrected prior ellipse restriction in arXiv:2504.20324v2 Corollary 2.

## originality

PASS

The phase diagram with a finite circle junction and the logarithmic rate is not a restatement of the classical Hermite Wigner polynomial or negativity convention. The strongest later indexed weak-amplitude theorem exactly covers the logarithmic rate and small-amplitude part by n=2 specialization, but not the finite-amplitude transition; its reference to earlier n=2 work is unnamed. The inspected earlier mixed-state and nodal-rigidity results do not settle the transition or exponent. The v2 ellipse corollary allows same-radius translated circles but does not predict their existence or location in this family. The search supports the distinct frozen result without establishing unrestricted historical priority.

## value

PASS

The lowest nontrivial even two-mode oscillator family shows how the topology of negativity can change without the negative volume ever vanishing. The critical state gives a concrete transverse, equal-radius nodal junction in the setting of the corrected general ellipse restrictions. The sharp weak-amplitude exponent quantifies why negativity can be undetectably small despite being present. These exact structural statements are useful benchmarks for mathematical phase-space analysis beyond a quartic evaluation or sampled plot.

The dated certificate retains the supplied scientific assessment, sources and limitations.
