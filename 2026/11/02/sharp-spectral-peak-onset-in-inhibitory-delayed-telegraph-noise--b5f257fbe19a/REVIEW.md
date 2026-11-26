# Independent mathematical audit

## correctness

PASS

Poisson updates at rate c yield the claimed flip intensity: refreshing causes a flip with probability 1/2, and an inhibitory copy causes a flip precisely for matching signs. Backward ancestry strictly retreats through update times and stops at a refresh almost surely, yielding a stationary sign-symmetric law and uniqueness by coupling from the remote past on any finite set of observation times. A flip changes σ by −2σ, so its compensator gives drift −cσ−hσ_delayed and expected bracket rate A=2(c+hC(T)). The inequality |C(T)|≤1 gives A≥2(c−h)>0; the strict version in the record follows because no updates in an interval of length T has positive probability, so C(T)>−1. Convolving the drift equation with the causal exponential kernel gives the stationary innovation equation. The delayed convolution has norm at most h/c<1; its Neumann series yields G∈L¹∩L² and, by the martingale isometry, the stationary σ representation. Then C is the autocorrelation of the kernel times A and its Fourier transform is A/F_T, with angle ωT and the stated sign of the sine term. On (0,T), the covariance equation and evenness give C''=(c²−h²)C; C(0)=1 and C'(0+)=-c-hC(T) yield the stated C(T). Subtracting F_T(0) and bounding 1−cos u≤u²/2 and sin u≤u for u>0 gives a strict positive difference for every nonzero ω at and below the positive root of b(T)=1−2hT−chT². Above the root b<0, and F_T is coercive uniformly in T for fixed c,h, so a global minimum exists off zero. At criticality a compact annulus away from zero has a positive gap, and uniform coercivity excludes the tail. Hence just above criticality every global minimizer is near zero. The derivative divided by 2ω is analytic in x=ω² and has x-derivative 2a₄(T*)>0 there; the simple positive root satisfies x=−b'(T*)(T−T*)/(2a₄(T*))+O((T−T*)²), with the exact constant in the Finding. Taking the square root gives the asserted pair and error.

## originality

PASS

The delayed telegraph model and its covariance equation are established; the record credits a general Fourier transfer formula and does not claim either ingredient as new. The strongest same-model accessible source establishes the delayed covariance equation, not an exact zero-to-nonzero global peak threshold or the two-peak onset law. Inspected related catalogue records treat different models or observables. The supported distinct claim is the global optimization and local uniqueness and coefficient, not the spectrum formula itself.

## value

PASS

The threshold gives an exact criterion for when delay changes the dominant stationary frequency. A curvature test alone cannot rule out a discontinuous relocation of the global peak before the curvature changes. The global envelope rules this out for this natural model and the near-critical uniqueness and coefficient quantify the transition without confusing it with instability of the process.

The dated certificate retains the supplied scientific assessment, sources and limitations.
