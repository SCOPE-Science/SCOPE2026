# Independent mathematical audit

## correctness

PASS

For n>=3 equally spaced sites, distinct traps a<b, 0<q<1 and independent detections q^distance, exact per-site union probability is q^{|i-a|}+q^{|i-b|}−q^{|i-a|+|i-b|}; summing gives exact deficit D=2(1+q)/(1−q)−F = q(1+q^s)(q^a+q^r)/(1−q)+q^s[s+1+q²(2−q^{2a}−q^{2r})/(1−q²)], s=b−a,r=n−1−b. For fixed s, dependence on a,r is H_s(a)+H_s(r), H_s(x)=alpha q^x−beta q^{2x}, and alpha>4 beta gives strict convexity, yielding exactly centered gap placements. For fixed q and n→∞, a balanced triple of gaps makes D<=C_q(n+1)q^{floor((n−1)/3)}; the nonnegative terms lower bound D>=q^{min(a+1,r+1,s)}, implying each gap n/3+O_q(log n) and limits (1/3,2/3). For q↑1 first, missed probability equals (1−q)²Σ_i |i−a||i−b|+O_n((1−q)^3), and normalized Riemann sums uniformly converge to I(c,d)=c²−c+1/3+(8/3)d³−d² with unique minimizer c=1/2,d=1/4, hence quarter sites. Enumerated n=3..12 using independent exact rational score, checked closed form, fixed-gap centering, and the symbolic factor F7(1,5)-F7(1,4)=q²(1−q)²(q³+2q−1), giving first q-dependent n=7 change (root 0.4533976515...). Finite checks corroborate general algebra only; no simulation of the infinite limits used as proof.

## originality

PASS

Best-of-knowledge PASS for the optimal **two-fixed-trap average detection** placement theorem, all-separation centering, two noncommuting limiting site fractions and minimal seven-site crossover. Earlier sensor-placement research uses the identical exponential detection probability but optimizes sitewise coverage constraints / number of sensors rather than an exactly-two-trap mean union probability. Another prior randomized-sensor model uses independent outright failures and expected worst distance, not the present sitewise probability. Ecological capture-recapture trap configuration studies focus on parameter-estimation precision with half-normal kernels rather than this exact combinatorial objective. Thus prior model similarity is credited without treating unrelated objectives as dominating claims.

## value

PASS

The decision to place traps depends qualitatively on the order of the landscape-size and detection-range limits: thirds versus quarters. The theorem makes this effect exact and supplies universal centering at fixed separation plus first seven-site parameter transition, useful to prevent conflating short- and long-range sensor designs. The object and probability objective are natural enough that the exact closed-form frontier is a meaningful structural fact, not an arbitrary small-instance calculation.

The dated certificate retains the supplied scientific assessment, sources and limitations.
