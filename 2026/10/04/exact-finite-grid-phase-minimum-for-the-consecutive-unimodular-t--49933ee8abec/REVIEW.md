# Independent mathematical audit

## correctness

PASS

Writing \(u=e^{i\alpha}\), \(v=e^{i\beta}\), \(c=\cos(\alpha-\beta/2)\), and \(y_k=\beta/2+2\pi k/N\) gives the exact quadratic sample formula \(1+4c\cos y_k+4\cos^2y_k\). For fixed grid rotation, convexity reduces the worst sample to the two extreme cosines \(p\) and \(-r\); balancing them at \(c=r-p\) gives the exact value \(1+4pr\). Regular-polygon geometry then yields \(\min pr=\cos^2(\pi/N)\) for even \(N\) and \(\cos(\pi/N)\) for odd \(N\), with the displayed phases realizing the balance. The verifier checks the extremizers through \(N=1200\) and the endpoint reduction on multiple rotations. An independent dense rotation scan for \(3\le N\le30\) matched the analytic formulas to numerical tolerance.

## originality

PASS

Neuwirth solves the continuous maximum-modulus phase problem for trigonometric trinomials with prescribed coefficient moduli and gives the continuous consecutive equal-modulus benchmark. The audited problem is a different optimization: the norm is sampled only on the complete \(N\)-th-root grid. The exact parity law and explicit finite-grid extremizers are not implied by the continuous theorem. Resultary search returned the assigned result as the direct finite-grid match and no earlier covering theorem.

## value

PASS

Finite root-of-unity sampling is the natural discrete counterpart of the classical continuous phase-minimax problem and is directly relevant to finite Fourier systems. The exact all-\(N\) parity law, explicit extremizers, and sharp second-order discretization deficit provide structural information beyond a finite numerical benchmark.

The dated certificate retains the supplied scientific assessment, sources and limitations.
