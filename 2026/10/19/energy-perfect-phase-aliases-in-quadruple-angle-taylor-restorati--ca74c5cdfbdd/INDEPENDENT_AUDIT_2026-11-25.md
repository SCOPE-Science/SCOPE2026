# Independent mathematical audit

## correctness

PASS

The quantified claim in RESULT.md lines 24–55 is exact energy preservation at every constructed point, with seed errors tending to zero and norm error tending to 2; the introductory shorthand does not mean either seed error is identically zero or the limit is attained at finite s. Expanding 1−C_{j+1}²−4^{j+1}xS_{j+1}² gives 4C_j²D_j, and the cosine update is Chebyshev T_{2^j}. Write f(u)=cos(sqrt(u)) near zero; f'(0)=−1/2, so u=θ_m(x)²=f^{-1}(P_m(x)) exists on the real small positive branch. If a=(-1)^m/(2m+2)!, the seed expansion gives u=x−2ax^(m+1)+O_m(x^(m+2)); taking square roots gives sqrt(x)−θ_m(x)=ax^(m+1/2)+O_m(x^(m+3/2)). The bounded nearest-odd rounding error gives x_s~β_m 2^(−2s/(2m+1)); the odd q_s makes C_{s−1}=0 and hence the restored matrix is exactly −I regardless of the sinc seed. Meanwhile 2^s(sqrt(x_s)−α_s)→(-1)^m π, so the true rotation tends to I modulo 2π. The omitted sinc term and cosine term give the two orders, and 2 is the maximal possible operator distance of rotations. For m=1 direct expansion gives D_0=x²(3−x)/36. All positive zeros of D_s are this seed root x=3 plus the zeros of T_{2^j}(1−x/2) for 0≤j<s. Distinct odd-numerator dyadic angles in (0,π) cannot equal 2π/3, so there are exactly 2^s distinct roots. At Chebyshev zeros the output is ±I; at x=3 the seed is a rotation through 2π/3 doubled s times. In both cases a correct phase would equate a strictly positive algebraic angle 2^s sqrt(x) to a rational multiple of π, impossible. As small exact checks, s=1 gives {2,3}, and s=2 gives {2−sqrt(2),2,2+sqrt(2),3}. Frozen verify.py, requirements.txt and VERIFICATION.md were inspected, not executed; the recorded 250-digit checks and 11669 count do not prove the limit or transcendence step. Replay: frozen RESULT.md lines 61–111.

## originality

PASS

The Taylor/Chebyshev restoration method, the basic doubling identities, and the distinction between energy preservation and phase accuracy are not new. The distinct supported statements are the resonant all-degree sequence with vanishing seed errors and asymptotically maximal rotation error and the full degree-one energy-zero census with nonexact phase. No inspected source contains or subsumes that pair; the earlier integrator full-text access gap is explicit.

## value

PASS

Energy preservation is a natural diagnostic for oscillator propagation. The theorem rigorously identifies a worst-case failure of that diagnostic despite vanishing local seed error and quantifies exactly how to tune the restoration scale. The degree-one census fully classifies the positive false positives of an exact diagnostic rather than selecting a few numerical counterexamples. The usefulness is as a stress test and a limitation of the diagnostic, not a claim of usual floating-point failure or a critique of the cited adaptive controller.

The dated certificate retains the supplied scientific assessment, sources and limitations.
