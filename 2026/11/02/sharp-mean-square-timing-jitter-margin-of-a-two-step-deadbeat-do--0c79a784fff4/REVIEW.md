# Independent mathematical audit

## correctness

PASS

For the exact double integrator with fixed u=-q-3v/2, h=1±delta iid equiprobable, 0<=delta<1, direct hold integration gives A(h) as in RESULT.md and A(1)^2=0. Independently formed the symmetric covariance lift K(delta^2) and checked every polynomial coefficient, det(I-K)=-(3z^3-11z^2+12z-2)/2 and det commutator=-delta^2(1-delta^2)^2. For delta>0 both step matrices invertible and their commutator has nonzero determinant; a positive-semidefinite Perron eigenmatrix of the adjoint cannot have rank one, hence is positive definite. The exact expected P-energy identity and norm equivalence establish the same all-initial-state trichotomy. The cubic has exactly one zero z*=0.202014738674272 in (0,1): r(0)=0, r(1)=5 and continuity, no other unit crossing. Thus delta*=0.449460497345731. The h=7/5 branch fails the Schur test (stable iff 0<h<4/3), while at delta=2/5 an exact rational P with entries 69675/10916,92725/21832,204927/43664 satisfies P-(A_-^T P A_- + A_+^T P A_+)/2=I with positive principal minors. Independently recomputed these identities symbolically. This is sampled-instant second-moment stability, not worst-case branch or almost-sure stability.

## originality

PASS

Random-sampling moment stability and spectral vectorization are established prior theory; the asserted result is the evaluated all-parameter cubic threshold for this particular fixed two-step deadbeat double-integrator law plus the mixing-stable/branch-unstable interval and exact rational witness. Open sources did not expose this exact specialization. The highly relevant Sun–Sun–Chen 2021 article remains inaccessible in full, so its potential specific worked example is an explicit priority risk, not a C or O automatic failure.

## value

PASS

A sharp stochastic robustness margin for a canonical elementary sampled controller, with an explicit range where random switching stabilizes although one branch is unstable, is a meaningful quantitative control invariant. The result supplies a closed algebraic boundary and a concrete Lyapunov certificate; it is not merely a restatement of the generic second-moment test.

The dated certificate retains the supplied scientific assessment, sources and limitations.
