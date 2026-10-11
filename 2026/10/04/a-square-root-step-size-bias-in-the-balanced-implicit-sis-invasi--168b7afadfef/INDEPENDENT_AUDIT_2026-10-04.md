# Independent mathematical audit

## correctness

PASS

The disease-free transverse SDE is exactly dJ=aJ dt-\sigma J dW, hence its almost-sure exponent is a-\sigma^2/2. Differentiating the frozen BIM update at (K,0) with F_1=0 and F_2=\sigma S/K gives the positive iid multiplier M_h(Z)=[1+(c+a)h+\sigma\sqrt h(|Z|-Z)]/[1+ch+\sigma\sqrt h|Z|]. With \varepsilon=\sqrt h, n=\sigma(|Z|-Z), d=\sigma|Z|, the exact Gaussian moments E n=E d=\sigma\sqrt{2/\pi}, E n^2=2\sigma^2, E d^2=\sigma^2, E n^3=8\sigma^3\sqrt{2/\pi}, and E d^3=2\sigma^3\sqrt{2/\pi} yield E log M_h=(a-\sigma^2/2)\varepsilon^2+\sqrt{2/\pi}\sigma(2\sigma^2-a)\varepsilon^3+O(\varepsilon^4). Uniform fourth-derivative domination near the threshold justifies expectation of the remainder. Strict monotonicity in a then gives the unique local zero a_h=\sigma^2/2-(3/2)\sqrt{2/\pi}\sigma^3\sqrt h+O(h). The finite checker was used only as algebraic corroboration.

## originality

PASS

Best-of-knowledge originality survives statement-level comparison. The open-access Schurz–Tosun paper supplies the exact BIM and proves invariance plus fixed-finite-horizon mean-square convergence of order 1/2, but it does not compute the fixed-step almost-sure transverse Lyapunov exponent or the square-root step-size displacement of the invasion threshold. A different dynamics-preserving SIS discretization in Liu–Wang–Dai is designed to reproduce extinction/persistence for every step and therefore does not imply the bias of this BIM. Fresh Resultary search found no source-specific equivalent.

## value

PASS

The calculation isolates a mathematically meaningful discrepancy between fixed-finite-time convergence and an infinite-time invasion threshold in the exact BIM used by the source. The \sqrt h law gives a quantitative boundary and a nonempty stability-mismatch interval, rather than a cosmetic local truncation error.

The dated certificate retains the supplied scientific assessment, sources and limitations.
