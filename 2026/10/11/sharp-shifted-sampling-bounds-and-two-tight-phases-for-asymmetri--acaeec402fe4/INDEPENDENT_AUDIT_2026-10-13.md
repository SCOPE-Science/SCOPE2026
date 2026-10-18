# Independent mathematical audit

## correctness

PASS

Reintegrated the autocorrelation C_n over the three t-intervals: for a != b it is (a+b)/(2(a-b))(r^n/b-s^n/a), and for a=b=c it is r^n(n+1/c). The exact Fourier Gramian has numerator u+v cos(theta) and two positive geometric denominators. The Fourier transform (a+b)/((a-iξ)(b+iξ)) is nonzero, so u>v>0; the explicit sinh(t)/t monotonicity yields v>0 also at a=b. Independently split the sample Zak transform into two geometric tails with numerator P_y+Q_y exp(i theta). The sharp multiplier (P²+Q²+2PQ cos(theta))/(u+v cos(theta)) is fractional-linear in cos(theta), so both attained essential extrema are its theta=0,pi values E_±. Strict increase of Q/P from zero to infinity gives exactly two positive constant-multiplier roots and one unstable P=Q phase. Strict convexity of P+Q and monotonicity of P-Q give the unique y=0 lower-bound maximizer; first-order zero of P-Q yields the exact quadratic coefficient. Domain 0<=y<1, all a,b>0, complex coefficients, L2 Fourier normalization and failure of a uniform lower bound (not a nonzero sampling-kernel vector) checked. Packaged independent Fourier/Zak finite checks were inspected, not substituted for this universal argument.

## originality

PASS

Inspected the complete openly available de Dios Pont–Gröchenig–Liehr–Shafkulovska–Taylor manuscript via lawful ResearchGate author manuscript, particularly Theorems 1.1/1.2 and Section 5.2: it determines qualitative complete interpolation and the unique bad Zak phase, not the sharp a,b-dependent two-endpoint ratio, exactly two scalar-isometric phase shifts or quadratic coefficient. Read Kloos–Stöckler original full PDF: the exact same symmetric exponential appears, but its near-critical Gabor bounds optimize a different time-frequency lattice. A classical spline quadrature equivalent formula may still be hidden; accepted only best-of-knowledge.

## value

PASS

One sample per period is the canonical critical grid recovery problem for a principal shift-invariant space. Exactly two scalar-isometric phases, the globally optimal grid and precise quadratic loss at the single bad shift characterize the entire conditioning of a natural asymmetric two-parameter kernel family. Unlike qualitative Zak-zero uniqueness, isometry and best constant require substantial sharp frequency analysis. A complete explicit inverse-problem stability profile is a motivated exact result, not an arbitrary computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
