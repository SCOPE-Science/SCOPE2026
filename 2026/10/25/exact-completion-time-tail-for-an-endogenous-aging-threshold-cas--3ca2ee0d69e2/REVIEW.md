# Independent mathematical audit

## correctness

PASS

For adjacent initial adopters and threshold 0<theta<1/2, the nonadopter set remains one contiguous arc. Given k≥2 remaining, two boundary sites are eligible; for k=1 exactly one. During sweep s there are N=m+2 independent with-replacement draws and per-draw activation probability 1/(s+2), so the one-draw transition is I+Q/[N(s+2)] and the exact t-sweep survival is e_m^T F_t(Q)u. The transient lower-bidiagonal generator has simple eigenvalue -1, right eigenvector v_k=2^(k-1), left e_1, and all others -2, hence leading spectral projection amplitude 2^(m-1). Gamma product identity gives F_t(z)=t^z/Gamma(2+z/N)^N(1+O(t^-1)); its derivatives at -2 contribute only O(t^-2 log^(m-2)t). Thus tail exactly 2^(m-1)/Gamma(2-1/N)^N /t, almost sure absorption, E[T^q]<infinity iff q<1. Independent exact rational Markov simulation checked 63 (m,t) instances m=1..7, t=0..8, and m=2,3 closed forms. The distinction between synchronous per-sweep aging and node-specific attempt aging is explicit in hypotheses.

## originality

PASS

The 2023 Abella–San Miguel–Ramasco primary paper introduces the endogenous-aging threshold activation p_A(j)=1/(j+2), and observes reciprocal-time nonadopter density; it does not state a finite seeded cycle full-completion hitting-time distribution or sharp Gamma-amplitude. The new model explicitly synchronizes the age of remaining nonadopters at each complete sweep, a restricted but materially different clock convention from some source asynchronous aging implementations. Standard absorbing Markov spectral methods are not new. The exact finite-chain law and order-one heavy tail amplitude provide the surviving specialized result; literature on time-inhomogeneous absorption may implicitly cover it.

## value

PASS

Full adoption time on a finite graph is a natural observable distinct from density relaxation or time to 90% adoption. The exact all-m finite-time law, positive 1/t tail with explicit geometry-dependent amplitude, and universal moment cutoff show almost-sure completion can coexist with an infinite mean; the two-front factor 2^(m-1) has structural meaning. The synchronized clock is a specific exactly solvable aging variant, not a theorem for every asynchronous aging implementation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
