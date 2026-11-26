# Independent mathematical audit

## correctness

PASS

In the stated model the energy integral gives lambda'=sqrt(2) omega sqrt(1-1/lambda); its inverse clock is the stated expression. For U=1/lambda and G=U(1-z^2 U^2)_+, the covariance is K^2 Cov(U,G), K=3/(4x0). On 0<=z<=1/sqrt(3), both functions of the common age strictly decrease for positive ages, and the independent-copy product of differences is positive almost surely. For small r, U,G=O((1+t)^-1), so the product of their expectations is O(r^2 log^2(1/r))=o(r). Dominated convergence on UG and the substitution y=1/lambda yield the positive A_z integral; the two beta integrals give 2 and 16/15. For rapid reset within z<=1, write U-1=-(omega^2/2)t^2+O(t^4). Independent moment checks give Var(T^2)=20/r^4 and Cov(T^2,T^4)=672/r^6, yielding the factors 5 and 84, the latter after exact cancellation of the linear term in G at the critical radius. The formula also applies at the initial edge z=1, since the positive part there does not modify the polynomial for any positive age. Beyond that edge, G vanishes up to t_z and has right derivative 2 lambda'(t_z)/z^2; the Laplace integral is b_z exp(-rt_z)/r and the ratio E[UG]/E[G] tends to 1/z while E[U] tends to 1. This verifies the coefficient and its negative sign. The covariance is analytic for positive r (Laplace transforms of bounded functions), so opposite endpoint signs imply a crossing, not uniqueness. Replay: RESULT.md lines 55–133 and the two factorial moment identities; the finite quadrature script and reported output were inspected, not rerun. Radii are fixed in the limits, and the randomness is reset age of a normalized hydrodynamic profile, not microscopic noise.

## originality

PASS

The deterministic Thomas–Fermi profile and reset-age mixture are known inputs. The strongest same-observable catalogue comparison gives real coverage of the spatial sign conclusion, fixed-radius endpoint sign reversal, and generic in-support coefficient, but is a subsequent spatial-front result and does not supply the critical sixth-order, off-support exponential, and slow-rate covariance amplitudes. The inspected preceding primary statements do not establish that sharp classification and those asymptotics.

## value

PASS

The boundary gives a radius-independent-of-rate answer to whether a common reset age makes local macroscopic fluctuations move together. At the boundary the fourth-order term vanishes but positivity persists with a computable sixth-order law. The negative outside-support amplitude instead measures a first-arrival event. These distinct observable-level predictions provide precise checks for the same hydrodynamic model and are not contained merely in its one-point stationary profile or the location of a spatial front.

The dated certificate retains the supplied scientific assessment, sources and limitations.
