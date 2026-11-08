# Independent mathematical audit

## correctness

PASS

The circular shortest arc X is uniform on [0,C/2] and independent of height-difference Y with triangular density 2(H-y)/H^2; D^2=X^2+Y^2 holds intrinsically, not for 3D chord distance. Expanding exact moments gives s=2U+V, x=U/s in (0,1/2), m2=s/6, m4=s^2(11x^2-7x+3)/45 and m6=s^3(-32x^3+110x^2-62x+15)/420. Quadratic m4 has twin roots summing to 7/11 only for 83/55<rho<9/5; m6 twin difference is -2(x-y)(484(x-7/22)^2+26)/12705 and cannot vanish for distinct roots. At the fold, sixth-moment normalized derivative -52/12705 is nonzero, yielding a smooth inverse there; everywhere else second/fourth derivative suffices. I independently checked exact polynomials/twin factors; finite numerical quadrature is supplementary. Source verify.py actually requires SymPy and SciPy despite RESULT.md inaccurately claiming no external dependencies.

## originality

PASS

Best-of-knowledge originality for the precise final claim after statement-and-implication comparison, preserving explicit priority/access risks; details in four required checks.

## value

PASS

A compact natural metric-measure family has a genuinely sharp finite-statistic inverse identification theorem: the exact minimal three-even-moment threshold, two-moment ambiguity range and fold-local smoothness. This is motivated geometry of random intrinsic distances rather than a routine forward moment computation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
