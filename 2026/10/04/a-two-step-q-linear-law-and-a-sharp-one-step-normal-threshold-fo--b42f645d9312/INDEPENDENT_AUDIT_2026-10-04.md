# Independent mathematical audit

## correctness

PASS

The exact short-step identities were reconstructed. With \(n=ux^2\), one curvature-matched step gives \(x^+=x(1+2n-2x^2/a)\) and \(n^+=x^4(4/a-4u)+O(x^6)\); an independent symbolic expansion reproduces these coefficients exactly. A second short step therefore resets the leading normal coefficient to \(4/a\). At a pre-Polyak state \(n=cx^4+O(x^6)\), expanding the exact Polyak step gives \(X=3x/4+O(x^3)\) and \(N=(7/16-ac/8)x^2+O(x^4)\); substituting \(c=4/a\) returns to a bounded parabolic wedge and yields the Q-factor. With one short step, \(c=4/a-4u+O(x^2)\), hence the affine multiplier \(8a/9\) and the threshold \(a=9/8\). The summable \(O(x_m^2)\) perturbation closes the attracting case.

## originality

PASS

The Davis--Drusvyatskiy--Jiang primary paper introduces GDPolyak, uses the Rosenbrock example \(a=10\), and illustrates it with \(K=100\); its generic theorem does not state the exact fixed-\(K=2\) Q-factor or the \(9/8\) one-step normal threshold. The 2026 follow-up gives a different Lyapunov analysis under convexity and public figures include a one-step nonconvex quartic baseline equivalent to \(a=1/2\), but no checked source states the parameter-wide exact recurrence.

## value

PASS

The theorem gives an exact dynamical explanation for why a tiny fixed block can work on the canonical quartic ravine, identifies a sharp one-step stability boundary, and separates that failure from the robust two-step mechanism. Exact local laws and stability thresholds for a standard benchmark are natural, reusable facts for adaptive first-order-method analysis.

The dated certificate retains the supplied scientific assessment, sources and limitations.
