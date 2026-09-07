# Maximum endpoint hitting time in the 8-state quarter-grid birth–death stratum

## Context
Small-chain extremals bridge textbook birth–death hitting formulas and asymptotic mixing bounds. No finite denominator-restricted extremal table was available for direct MCMC worst-case benchmark citation. This record compiles the exhaustive census for one stratum: 8-state quarter-probability birth–death chains.

## Definitions
State space $\{0,\dots,7\}$. Write $p_i=P_{i,i+1}$, $q_i=P_{i,i-1}$, $r_i=P_{i,i}$ ($q_0=p_7=0$). Birth–death means $P_{i,j}=0$ unless $|i-j|\le 1$ and each row sums to $1$. Quarter-grid means every entry is a multiple of $1/4$. Irreducible means $p_i>0$ ($i<7$), $q_i>0$ ($i>0$). Aperiodic means some $r_i>0$.

Let $S_{8,4}$ be the irreducible quarter-grid set: $p_0\in\{1/4,1/2,3/4,1\}$, $q_7\in\{1/4,1/2,3/4,1\}$, each interior $i=1..6$ in 6 options $(p_i,q_i,r_i)$: $(1/4,1/4,1/2)$, $(1/4,1/2,1/4)$, $(1/4,3/4,0)$, $(1/2,1/4,1/4)$, $(1/2,1/2,0)$, $(3/4,1/4,0)$. Hence $4\cdot 6^6\cdot 4=746{,}496$ chains; $1\cdot 3^6\cdot 1=729$ have all $r_i=0$ (periodic); aperiodic stratum has $745{,}767$.

For $P\in S_{8,4}$ let $H(P)=\mathbb{E}_0[T_7]$, mean hitting time of $7$ from $0$. With $h_i=\mathbb{E}_i[T_7]$, $h_7=0$, $h_i=1+p_i h_{i+1}+q_i h_{i-1}+r_i h_i$. With $d_i=h_i-h_{i+1}$: $d_0=1/p_0$, $p_i d_i-q_i d_{i-1}=1$ ($i\ge 1$), i.e. $d_i=(1+q_i d_{i-1})/p_i$, and $H(P)=\sum_{i=0}^{6}d_i$. $H$ uses only rows $0$–$6$; row $7$ never enters. Equivalent form: $(I-Q)h=\mathbf{1}$ with $Q=P_{0..6,0..6}$.

## Result
Canonical extremizer $P^\star$ (fixes free $q_7=1/4$):
- Row 0: $r_0=3/4$, $p_0=1/4$;
- Rows 1–6: $q_i=3/4$, $p_i=1/4$, $r_i=0$;
- Row 7: $q_7=1/4$, $r_7=3/4$.

Matrix rows 0–7: `[3/4,1/4,0,0,0,0,0,0]`, `[3/4,0,1/4,0,0,0,0,0]`, `[0,3/4,0,1/4,0,0,0,0]`, `[0,0,3/4,0,1/4,0,0,0]`, `[0,0,0,3/4,0,1/4,0,0]`, `[0,0,0,0,3/4,0,1/4,0]`, `[0,0,0,0,0,3/4,0,1/4]`, `[0,0,0,0,0,0,1/4,3/4]`. Irreducible and aperiodic.

Theorem (exact census):
(a) $H(P^\star)=6544/1$ exactly.
(b) No $P\in S_{8,4}$ exceeds 6544. Maximum attained by exactly 4 full chains: unique rows-0–6 pattern above times 4 choices of $q_7$ (all aperiodic since $r_0>0$). Modulo row 7 the maximizer is unique.
(c) Top-five distinct values with lexicographically-first rows-0–6 representatives (append any $q_7$): 1: 6544, $p_0=1/4$, all $(1/4,3/4,0)$; 2: 5088, $p_0=1/4$, $(1/4,1/2,1/4)$ at $i=1$, rest $(1/4,3/4,0)$; 3: 4608, deviation at $i=2$; 4: 4464, deviation at $i=3$; 5: 4358, $p_0=1/2$, all $(1/4,3/4,0)$. Ranks 2–4 each have a second pattern with identical $H$ (deviation at $i=6,5,4$ respectively), i.e. 8 full chains each; rank 5 unique mod row 7 (4 chains). Maximum over the 729 excluded periodic chains is $3265<6544$.

Reported mixing bracket for $P^\star$ (numerical/empirical, not interval-certified): eigenvalues $1,0.8678396994,0.71583796,0.445564186,0.0997552436,-0.2618445803,-0.5767208769,-0.7904316318$ (trace 1.5 checks); $|\lambda^\star|\approx0.86784$, gap $\approx0.13216$, $t_{\mathrm{rel}}\approx7.567$; stationary $\pi\propto(1,1/3,\dots,1/3^6,1/3^6)\approx(0.66636,0.22212,0.07404,0.02468,0.00823,0.00274,0.000914,0.000914)$; $t_{\mathrm{mix}}(1/4)\ge\lceil\ln(1/2)/\ln|\lambda^\star|\rceil=5$; Levin–Peres–Wilmer numeric bound $\le64$; seeded monotone coupling from $(0,7)$ (seed 20260907, $N=20000$, mean $\approx16.9$, $P(\tau>20)\approx0.253$) gives empirical $t_{\mathrm{mix}}(1/4)\lesssim21$. Reported as $5\le t_{\mathrm{mix}}(1/4)\lesssim21$ (empirical upper) and $\le64$ (analytic-numeric upper).

## Proof / Evidence
Hand check: $d_0=4$, $d_i=4+3d_{i-1}$ gives $d_i=2\cdot3^{i+1}-2$: $4,16,52,160,484,1456,4372$ summing to $6544$.

Exhaustive certificate: exact recursion with Python Fractions over all $186{,}624$ rows-0–6 patterns (2.6 s); sorted distinct list has $10{,}046$ values topped as above; maximum pattern unique; $\times4$ for free $q_7$ gives full census with per-chain aperiodicity check. Cross-check: Fraction Gauss–Jordan on $(I-Q)h=\mathbf{1}$ reproduces all top-five values. Float pre-screen ($186{,}624$ numpy solves, 1.4 s) independently peaks at same pattern ($6544.0000000007$). Analytic dominance: for any $d_{\mathrm{prev}}>0$, $(1+q d_{\mathrm{prev}})/p$ is maximized by $(1/4,3/4)$ among the 6 options and $d_0$ by $p_0=1/4$, so left-drift is the unique maximizer mod row 7 independent of enumeration. Rank-5 hand sum $2+10+34+106+322+970+2914=4358$; rank-2 $4+12+40+124+376+1132+3400=5088$ (symmetric late variant $4+16+52+160+484+1456+2916=5088$).

Mixing methods: lower bound via $|\lambda^\star|^t\le2d(t)$ instantiated numerically; upper via monotone coupling preserving order from worst pair $(0,7)$ plus reversible-chain $t_{\mathrm{rel}}\log(1/(\varepsilon\pi_{\min}))$ evaluated numerically. See Limitations.

## Limitations
Mixing bracket is not theorem-grade: spectral lower uses numpy eig (~1e-12 error, trace/det checked, $|\lambda^\star|$ well separated from 0.7904) not interval arithmetic; coupling upper is Monte Carlo quantile ($N=20000$, seed recorded) not a theorem; $\le64$ bound is analytic form evaluated numerically. Exact hitting-time census itself is exact rational and deterministic. Uniqueness only modulo free row 7; ranks 2–4 have extra paired ties. Extremizer left-drift unsurprising; value is compiled benchmark table, not surprise. First-compiled-census claim limited to standard texts (Levin–Peres–Wilmer; Norris; Aldous–Fill); broader literature priority not claimed (live web verification unavailable).

## Reproducibility
Scripts in `output/artifacts/`: `exact_census.py`, `verify_exact.py`, `enumerate.py`, `spectral.py`, `coupling.py`, `selfcheck.py`, `tie_detail.py`. Run `python3 output/artifacts/exact_census.py`, `verify_exact.py`, `spectral.py`, `coupling.py`. Total <1 min on laptop CPU. Fixed loop order; only randomness is seeded coupling.

## References
- D. Levin, Y. Peres, E. Wilmer, Markov Chains and Mixing Times (2nd ed., AMS).
- J. Norris, Markov Chains (Cambridge Statistical Laboratory notes).
- D. Aldous, J. Fill, Reversible Markov Chains and Random Walks on Graphs (draft).
