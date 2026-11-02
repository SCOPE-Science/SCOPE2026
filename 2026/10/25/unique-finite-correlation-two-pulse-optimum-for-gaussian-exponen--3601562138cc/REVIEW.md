# Independent mathematical audit

## correctness

PASS

Gaussianity makes coherence exp[−sigma²tau² Q/2] with Q the nonnegative kernel double integral of the three-sign modulation. Partitioning the integral gives Q=2L−10+4(e^(−a)+e^(−c))+8e^(−b)−4(e^(−a−b)+e^(−b−c))+2e^(−L), corroborated by an independent interval-state integral recursion for 1000 test triples. For fixed middle length b and a+c=L−b, dQ/da=4(1−e^(−b))(e^(−c)−e^(−a)), negative for a<c and positive for a>c; uniquely minimizes at a=c. Along this locus dQ/db=4e^(−a)(1+e^(−b))−8e^(−b); its sign equals sign[2b+2log cosh(b/2)−L]. This continuous strictly increasing scalar from −L to positive at b=L has a unique interior root; both boundary schedules lose. Bounds 0<log cosh(b/2)<b/2 force 1/4<a/L<1/3. Strict convexity of log cosh ensures monotonic ratio as L varies. Small-L root b=L/2−L²/32+O(L³) and gain Q_CPMG−Q_opt=L^4/256+O(L^5) are consistent; independent mpmath high-precision small-L expansion and thousands of unrestricted numerical competitors corroborate. The proof, not the sample search, establishes the universal unique minimum.

## originality

PASS

Qualified best-of-knowledge PASS for this exact fixed-two-pulse unconstrained Gaussian-OU global optimum. The Gaussian filter-function reduction is established and not claimed novel. Ji–Zhao same exponential Gaussian kernel uses numerical multi-pulse designs with a zero-average constraint, not this exact unique unconstrained two-switch root in its inspected full HTML. Earlier Ohmic and Gaussian-frequency spin-bath pulse optimizations have different spectral kernels. Specialized decoupling literature could contain a mathematically equivalent variational result, retained as risk.

## value

PASS

Exactly two-pulse timing is a natural constrained control optimization for Gaussian Ornstein–Uhlenbeck dephasing. The theorem solves a continuous two-variable global problem in closed implicit form, proves uniqueness and sharp geometry, and separates the true finite-correlation coherence optimum from the commonly imposed zero-static-area Carr–Purcell schedule. A model-specific optimal control law is useful without asserting a new general control theorem or experimental superiority.

The dated certificate retains the supplied scientific assessment, sources and limitations.
