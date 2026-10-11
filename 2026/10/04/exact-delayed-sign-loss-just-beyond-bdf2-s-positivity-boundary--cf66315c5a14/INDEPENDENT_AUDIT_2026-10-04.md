# Independent mathematical audit

## correctness

PASS

The recurrence has characteristic polynomial \((3+2r)\xi^2-4\xi+1\). For \(r>1/2\) its roots are \(\rho e^{\pm i\theta}\) with \(\rho=(3+2r)^{-1/2}\) and \(\cos\theta=2/\sqrt{3+2r}\). Matching the backward-Euler starter gives \(z_n=\rho^n[\cos(n\theta)+\beta\sin(n\theta)]\), \(\beta=((1+r)\sqrt{2r-1})^{-1}\), hence a phase \(\cos(n\theta-\phi)\). Because \(0<\theta<\pi/2\), the first strictly negative term is exactly the first integer with \(n\theta>\pi/2+\phi\), including the zero-at-equality boundary. The repeated-root formula at \(r=1/2\) is positive. Expanding \(\theta\) and \(\phi\) at \(r=1/2+\varepsilon\) yields the stated \(\pi\sqrt2\) delay constant. Fresh exact-rational replay reproduced first-negative indices 42, 12, 5 and 3 at \(r=0.51,0.6,1,2\).

## originality

PASS

The closest primary source establishes positivity/monotonicity threshold behavior for implicit two-step methods with starting procedures and its numerical section explicitly treats BDF2 with a backward-Euler start and the change at the one-half parameter. It does not state the exact first-negative index above the threshold or the square-root divergence of that index. Current Resultary searches under BDF2 positivity, sign loss, oscillation and backward-Euler starter terminology found no equivalent phase law. The known threshold alone does not determine the delayed failure index.

## value

PASS

The first wrong-signed iterate is a natural diagnostic immediately beyond a sharp positivity boundary. Its exact phase formula and critical \(1/\sqrt{r-1/2}\) delay explain why a slightly supercritical step can appear positive for a long transient. This is a motivated boundary refinement rather than an arbitrary recurrence exercise.

The dated certificate retains the supplied scientific assessment, sources and limitations.
