# Refutation of the sharp truncation threshold β_c = 2/3 for the Pareto α=3 Wigner family

## Context
Truncation at $B_N=N^\\beta$ is the canonical one-parameter deformation bridging heavy-tailed and classical random-matrix theory. The admitted target claimed that for the normalized symmetric-Pareto $\\alpha=3$ Wigner ensemble E3, $\\beta_c=2/3$ sharply separates rescaled Tracy–Widom (TW1) edge statistics ($\\beta<2/3$) from heavy-tail Poisson edge statistics ($\\beta>2/3$). This record certifies the rigorous refutation: the TW-half is false as stated.

## Definitions
- **E3:** real Wigner ensemble with unscaled i.i.d. off-diagonal entries $x_{ij}$ standardized symmetric Pareto($\\alpha=3$): mean 0, variance 1, tail $P(|x|>t)=(t_0/t)^3$, $t\\ge t_0$, $t_0=1/\\sqrt{3}$, tail constant $c_*=t_0^3=3^{-3/2}$.
- **Truncated family E3$^{(\\beta)}$:** truncate unscaled entries at $B_N=N^\\beta$ with variance renormalization: $y_{ij}=T_{B_N}(x_{ij})/\\sigma_N$, $\\sigma_N^2=\\mathrm{Var}(T_{B_N}(x))$, $H^{(\\beta)}_{ij}=N^{-1/2}y_{ij}$ ($i<j$; diagonal analogous). Covers zero-fill $T_B(x)=x\\mathbf{1}_{|x|\\le B}$, clip/Winsorize $T_B(x)=\\mathrm{sgn}(x)\\min(|x|,B)$, and conditional law given $|x|\\le B$.
- **TW1:** GOE Tracy–Widom distribution with d.f. $F_1$, of full support on $\\mathbb{R}$ ($0<F_1(s)<1$ for all $s$).

## Result
At the fixed exponent $\\beta_0=3/5<2/3$, under any of the three truncation conventions,
$$\\max_{i<j}|H^{(\\beta_0)}_{ij}|\\xrightarrow{P}+\\infty,\\qquad \\max_i|H^{(\\beta_0)}_{ii}|\\xrightarrow{P}0,$$
hence for every fixed $K$, $P(\\lambda_{\\max}(H^{(\\beta_0)})\\ge K)\\to 1$.
In particular $P(N^{2/3}(\\lambda_{\\max}-2)\\le s)\\to 0$ for every fixed $s$, while $F_1(s)>0$, so $N^{2/3}(\\lambda_{\\max}-2)$ cannot converge to TW1 (nor to any tight law at any fixed centering). The claimed sharp two-sided diagram with meeting point $\\beta_c=2/3$ is therefore false as stated.

## Proof / evidence
- **Lemma 1 (renormalization):** $\\sigma_N^2=1-3^{-1/2}/B_N\\to 1$ (zero-fill); clip adds $B^2P(|x|>B)=c_*/B$ terms, conditioning divides by $1-O(B^{-3})$; all $O(1/B_N)\\to 1$. Proof by $E[x^2\\mathbf{1}_{|x|>B}]=3t_0^3/B$.
- **Lemma 2 (off-diagonal divergence):** for fixed $K'$, $B_N/(\\sigma_N\\sqrt N)\\sim N^{0.1}\\to\\infty$, so $\\{|H_{ij}|>K'\\}=\\{K'\\sigma_N\\sqrt N<|x_{ij}|\\le B_N\\}$ with $p_N=c_*(K'\\sigma_N\\sqrt N)^{-3}-c_*B_N^{-3}$ (clip: superset lower bound; conditioning: divided by $\\to 1$). With $M=N(N-1)/2$, $Mp_N\\ge \\mathrm{const}\\cdot N^{1/2}(1-r_N)\\to\\infty$ where $r_N=(K'\\sigma_N\\sqrt N/B_N)^3\\to 0$; $(1-p_N)^M\\le e^{-Mp_N}\\to 0$.
- **Lemma 3 (diagonal bounded):** $P(\\max_i|H_{ii}|>1)\\le N c_*(\\sigma_N\\sqrt N)^{-3}=O(N^{-1/2})\\to 0$ (fixed-law case via uniform integrability).
- **Spectral step:** for $v=(e_i+s e_j)/\\sqrt 2$, $s=\\mathrm{sgn}(H_{ij})$, $v^THv=(H_{ii}+H_{jj})/2+|H_{ij}|\\ge |H_{ij}|-\\max_k|H_{kk}|$, so $\\lambda_{\\max}\\ge\\max_{i<j}|H_{ij}|-\\max_i|H_{ii}|$ and $P(\\lambda_{\\max}\\ge K)\\ge P(\\max|H_{ij}|\\ge K+1)-P(\\max|H_{ii}|>1)\\to 1$.
- Mechanism: truncation with $\\beta>1/2$ leaves scaled entries of size $N^{\\beta-1/2}\\to\\infty$; fixed-law Lee–Yin tail criterion fails for the $N$-dependent law ($s^4P(|y|>s)$ diverges like $\\sqrt N$ at $s\\asymp\\sqrt N$). True single-entry TW threshold is at most $1/2$.
- Numerical illustration (not the proof): `output/artifacts/verify_counterexample.py` gives $\\sigma_N^2\\to 1$, $Mp_N$: 0.6 ($N=10^4$) → 374 ($N=10^9$), sampled maxima $>1$, and one $N=800$ Wigner sample with $\\max|H_{ij}|=1.96$, $\\lambda_{\\max}=2.50>2$. Replay: `python3 output/artifacts/verify_counterexample.py`. Log: `output/artifacts/verify_counterexample.log`.

## Limitations
Refutes only the TW-half and hence sharpness as stated; the $\\beta>2/3$ Poisson-persistence half is untouched and may be true. Does not identify the true TW-restoration threshold (only $\\le 1/2$) nor characterize the intermediate $(1/2,2/3)$ phase; a corrected diagram is a different claim and left open.

## Reproducibility
Analytic proof is self-contained hand computation (tail integral, union bound, $2\\times 2$ variational bound). Numerical file vendored with fixed seed; independently replayed VERIFY_OK during audit.

## References
- Soshnikov (2004), Poisson Statistics for the Largest Eigenvalues of Wigner Random Matrices with Heavy Tails, https://doi.org/10.1214/ecp.v9-1112
- Auffinger, Ben Arous, Péché (2009), Poisson convergence for the largest eigenvalues of heavy tailed random matrices, https://doi.org/10.1214/08-aihp188
- Lee, Yin (2014), A Necessary and Sufficient Condition for Edge Universality of Wigner matrices, https://arxiv.org/abs/1206.2251
