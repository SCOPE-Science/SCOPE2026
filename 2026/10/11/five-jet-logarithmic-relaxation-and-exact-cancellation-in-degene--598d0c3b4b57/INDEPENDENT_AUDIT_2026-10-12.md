# Independent mathematical audit

## correctness

PASS

Frozen RESULT.md 36a5a4f26e0f9f521bf6770306a3f08396bae3ac and exact checker 8f4aa0d99fa711493089acae4570b533e3ee7f0d inspected. For smooth odd restoring f(x)=cx^3+dx^5+O(x^7), c>0, even damping g(x)=a+bx^2+O(x^4), a>0, with global g>=g0>0, xf>0, coercive U, energy E=v²/2+U gives E_dot=-g(x)v²<=0; compact LaSalle ensures all solutions tend to (0,0). Eigenvalues 0,-a give a one-dimensional slow center graph and unique fast strong-stable manifold. Invariance h h_prime=-g h-f gives h=-(c/a)x³+[-d/a+bc/a²-3c²/a³]x⁵+O(x⁷). Independently differentiated this polynomial with SymPy, obtaining Γ=-h5/(c/a)=d/c-b/a+3c/a². Along slow trajectories u=x^-2 obeys u_prime=2c/a-2h5/u+O(u^-2), integrating with u~(2c/a)t gives u=(2c/a)t+Γ log t+C+o(1), with integrable error and stable-fiber exponential tracking. For polynomial f=cx³+dx⁵, g=a+bx², exact W=v+(c/a)x³ obeys W_dot=-(a+ad x²/c)W iff b=ad/c+3c/a; symbolic independent check gives residual proportional to Γ x⁵. No singular claim is made on x=0 at finite crossings; eventual sign is fixed for nonstrong-stable trajectories. Logs/finite tests alone do not establish global convergence; energy and center/strong-stable arguments provide that proof.

## originality

PASS

Best-of-knowledge PASS with attribution: Darboux polynomial invariant curve under cancellation was pre-existing (Demina), as were global Liénard attraction/leading rates (Llibre–Valls and Bárta). Neither inspected full source supplies this particular all-nonfast-orbits two-term physical-time inverse-square logarithm with coefficient d/c-b/a+3c/a², plus exact algebraic cancellation equivalence. Generic center-manifold machinery is used transparently, not claimed new.

## value

PASS

PASS. The sign and exact vanishing of the first logarithmic correction to algebraic relaxation are motivated measurable asymptotic invariants of a globally damped degenerate oscillator, and the exact cancellation parameter identifies an invariant slow curve. The full all-initial-data except one strong-stable manifold statement distinguishes this from mere local Taylor algebra or an unmotivated substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.
