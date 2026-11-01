# Independent mathematical audit

## correctness

PASS

The fused map F(y)=1+(1−1/L)y=y+(L−y)/L, L=2^q, makes the p-bit stochastic-rounding chain nondecreasing on finitely many floats in [1,L]. With upward probability computed from downward p+r-bit truncation, upward motion is possible iff the increment crosses the p+r-grid quantum. Below L, final p-spacing Δ=2^(q−p), higher-grid spacing Δ/2^r. If r<q, the first absorbing state reachable from below is B=L−(2^(q−r)−1)Δ, and no state can jump over B; if r≥q the unique absorber is L. Positive upward probability at all preceding states and independent choices prove finite-time almost sure absorption; the last predecessor is visited and has exact geometric holding mean 2^r or 2^q. Ideal SR always reaches L. Independently enumerated 115 full exact rational reachable finite chains and final holding laws; infinite integer parameter proof is monotonic finite-chain/grid reasoning.

## originality

PASS

El Arar et al (2026) define exactly the truncation-based few-random-bit SR operator and analyze separately rounded Horner, explicitly excluding FMA (Remark 3) and studying finite-degree stagnation. Prior bias and limited-bit SR results do not give the exact almost-sure absorbing threshold for fused all-one geometric polynomial. The contribution is an explicit sharp random-bit barrier and final geometric waiting law, not finite-degree stochastic rounding as such. An equivalent result in hardware/quantized-recursion literature remains a risk.

## value

PASS

Gives a sharp and counterintuitive limitation of finite-random-bit stochastic rounding under a fused operation: correct asymptotic limit iff r≥q and severe deterministic underestimation otherwise; quantifies exact waiting time. The natural geometric polynomial isolates a universal feedback saturation problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
