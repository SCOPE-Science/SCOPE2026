# Independent mathematical audit

## correctness

PASS

For positive X the affine first-coordinate recurrence X_{j+2}=R X_{j+1}−R X_j+1, X0=1, X1=1+R is solved by H_j=1+R^((j+1)/2) sin(jθ)/sinθ, θ=acos(sqrtR/2). At r_n=4cos²(π/n), H_n(r_n)=1 and independently differentiating at θ=π/n yields D_n=n q_n^n/(4 sin²(π/n))>0. Since D_n~q_n^n n³, a radius 3/D_n yields H_n(r_n−c/D_n)=1−c+O(q_n^-n) and strict positive derivative. Both levels 0 and 1/R are crossed exactly once; for j<n the angle satisfies 0<jθ<π throughout, hence X_j=H_j>1 and the first n−1 branch decisions genuinely coincide with the positive affine recurrence. Mean-value theorem gives gap ΔR=(r_nD_n)^−1(1+O(q_n^-n))=tan²(π/n)/(n q_n^n)(1+O(q_n^-n)); q_n=2cos(π/n) implies π² 2^-n n^-3(1+O(n^-1)). The neighboring r_n−r_{n−1}~8π²/n³ yields ratio 2^-n/8. High-precision independent derivative checks at n=6,10,20 matched exact D_n; finite checks only corroborate infinite Taylor estimates.

## originality

PASS

The exact max-plus model, oscillatory recurrence, exit inequalities and numerical branch-boundary tables all appeared in Yamazaki–Ohmori 2021 and its 2024 generalization. This final claim does not rebrand those facts: it proves an asymptotically EXPLICIT exponential gap with sharp π² constant and its 2^-n/8 ratio to adjacent polynomial windows. Both relevant full primary manuscripts were read, and no corresponding asymptotic was located; possible equivalent unstated Taylor corollary is acknowledged, not treated as a known published result.

## value

PASS

The parameter windows are intrinsic to a concrete reset oscillator. Determining exponentially small inter-window gaps compared with adjacent O(n^-3) widths resolves a genuine scale separation and limits numerical bifurcation resolution; the precise coefficient is useful for large-n parameter estimates, without claiming attractor classification in the gap.

The dated certificate retains the supplied scientific assessment, sources and limitations.
