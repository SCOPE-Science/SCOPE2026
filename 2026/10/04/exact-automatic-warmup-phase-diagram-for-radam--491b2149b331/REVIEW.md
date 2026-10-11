# Independent mathematical audit

## correctness

PASS

For fixed b, \(tb^t/(1-b^t)\) strictly decreases in t, so \(\rho_t\) strictly increases and tends to \((1+b)/(1-b)\), proving the exact no-activation boundary b<=3/5. Since \(\rho_t<t\), activation cannot precede step five. Algebra gives \(\rho_t>4\) iff \(F_t(b)>0\), with \(F_t=(b-1)^2P_t\). The coefficients of \(P_t\) have exactly one sign change; \(P_t(3/5)<0<P_t(1)\), so Descartes plus continuity gives one positive root in the required interval. Monotonicity of \(\rho_t\) orders the roots. The exact root identity for \(\delta_t=b_t-3/5\) implies exponential smallness and then \(\delta_t\sim(4/25)t(3/5)^t\). A fresh independent numerical replay reproduced b_5 through b_11 and the stated activation indices for 0.8, 0.9, 0.99, 0.999, 0.7, 0.65, and 0.61.

## originality

PASS

The defining RAdam paper gives the effective-SMA statistic, the \(\rho_t>4\) gate, and the degeneracy statement for \(\beta_2\le0.6\), but its inspected full text does not partition \(\beta_2\) into exact first-activation intervals, give the root polynomials, or derive the threshold accumulation law. Resultary searches for exact activation indices and warmup phase diagrams found no covering published result.

## value

PASS

The activation time is an intrinsic, gradient-independent part of a widely used optimizer and the exact parameter dependence is not captured by the source's binary degeneration statement. The theorem explains why common \(\beta_2\) values all rectify at step five while the unadapted phase becomes arbitrarily long near 0.6, giving a natural exact phase diagram rather than an arbitrary numerical slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.
