# Independent mathematical audit

## correctness

PASS

A=diag(a,b,c), a>b>c>0, E=(e1e2^T+e2e1^T)/sqrt(2), d=t/sqrt(2a) in (0,sqrt(b)). The scaled SPD matrix is direct sum of c and a 2x2 symmetric block [[theta,d sqrt(theta)],[d sqrt(theta),b]]. Its eigenvalues Lpm=(theta+b ± sqrt((theta-b)^2+4d²theta))/2. Since L+>b>c and L- is strictly increasing, κ=L+/min(c,L-). The within-block ratio L+/L- is strictly minimized at theta=b by AM–GM; the c-crossing theta0=c(b-c)/(b-c-d²) is before b precisely when d≤(b-c)/sqrt(b). Global monotonic branches yield unique theta*=theta0 below threshold, b above; values b/c+d²/(b-c-d²) and (sqrt(b)+d)/(sqrt(b)-d). At t=0 theta in [c,b] all minimize, so uniqueness exclusion is essential. I independently computed full eigenspectrum and checked prescribed optimizers against 801 log-spaced alternatives in each of 16 parameter cases, and traced the exact analytic proof; finite samples are not the continuum proof.

## originality

PASS

PASS qualified. The motivating Diouane–Gürol–Mouhtal–Orban 2026 article studies this recycled spectral scaling framework but its inspected Section 3.3 works with a fixed separation of selected placements from untouched eigenvalues and uses eigenpair asymptotics/energy-error bounds. The closed global all-positive-theta condition-number minimizer here approaches and then reaches untouched modes. General optimal diagonal preconditioning algorithms and older spectral sensitivity theory do not state the specific two-branch symbolic theorem in inspected sections. A specialized older arrowhead/2x2-congruence theorem could imply it; priority is not certified.

## value

PASS

The smallest SPD spectral recycling model with one selected and two untouched eigenmodes has an exact nontrivial optimizer crossover at one explicit perturbation threshold. The quadratic approach to a nominally excluded eigenvalue tests limits of fixed-gap perturbative scaling recommendations. This is a motivated sharp structural diagnostic, not a claimed general PCG iteration speedup.

The dated certificate retains the supplied scientific assessment, sources and limitations.
