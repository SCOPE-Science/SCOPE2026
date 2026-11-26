# Independent mathematical audit

## correctness

PASS

For H_eff with the stated loss normalization, the rate of norm loss is κ times the boundary occupancy. The retarded boundary resolvent from site m is -(2/Ω)z^m/(1-iηz), where E=Ω[1-(z+z^{-1})/2] and |z|<1 above the real axis. Plancherel gives the two integrals: z=e^{ik} on the band and z=±q off it. This also checks the factors of two and that the objective is total eventual absorption. In RESULT.md proof steps 1–4 differentiation gives P'_m>0 for η≤1, both second derivatives strictly negative on [1,√3], and P'_m<0 on [√3,2] by comparing the bulk lower bound on -B' to 2/(3πη³). For η≥2 the elementary C'_2 formula has negative sign: g(2)>0 and g'=ηh with h(2)>0 and h'>0; weighting its integrand by the increasing q^{2(m-2)} at the one sign change preserves negativity. This proves the unique global crossing for every integer m≥2. Subtraction yields the positive reciprocal integral; the kernel's beta mass is asymptotic to m^-3. For C'_m(1), expanding (1+z)^-2 as (1+(1-z)+O((1-z)^2))/4 gives 1/(2πm³)+3/(4πm⁴)+O(m^-5). With B''(1)=-2/(3π) and C''_m=O(m^-2) uniformly near 1, the stationary displacement and the quadratic improvement give the stated two terms and 3/(16πm⁶). The frozen verification file and inspected verify.py report finite quadrature and truncated-chain checks; the uploaded code was not executed or used as proof. The record does not cover m=1, finite-time optima, or other geometries.

## originality

PASS

The distinct contribution is strict, globally unique optimality with a uniform strong-side bracket for every finite m≥2, plus sharp refinements of the large-distance location and value. The exact probability and limiting η=1 optimizer are prior, the leading cubic shift materially overlaps a distinct indexed result, and algebraic subtraction from the prior integral already implies the bias formula and sign. The bias should not be credited as an independent new absorption law. Neither inspected source supplies the full finite-distance classification or both sharp refinements. This is a bounded assessment, not a priority claim.

## value

PASS

The question is optimization of a physically defined eventual-capture probability, not numerical improvement alone. The theorem rules out competing maxima on both sides of the boundary-mode transition for every permitted localized start. It explains how a finite-distance optimum differs from the reciprocal limiting optimum and why its gain is parametrically smaller than its displacement. The finite-site classification is the principal value.

The dated certificate retains the supplied scientific assessment, sources and limitations.
