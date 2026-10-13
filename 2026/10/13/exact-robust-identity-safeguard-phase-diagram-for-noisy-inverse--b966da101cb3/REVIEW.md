# Scientific review — robust identity safeguarding of an uncertain inverse

## Correctness — PASS

The mathematical claim has four independently checkable steps. First, simultaneous diagonalization of real symmetric commuting \(A\) and \(E\) gives \(B=I+A(E+\omega I)\succ0\), with each eigenvalue at least \(1-L\delta>0\). Second, exact one-dimensional residual minimization and the sharp positive-definite Kantorovich inequality produce \((K-1)/(K+1)\) for an attained extremal spectral ratio \(K\), with an explicit endpoint-residual equality witness. Third, independent sign-extreme perturbations on the \(\mu\) and \(L\) modes determine the exact two-mode ratio; duplicating the \(L\) mode in dimension three changes which lower eigenvalue is attainable and hence changes the exact dimension-independent high-dimensional ratio. Fourth, differentiation and the unique crossing of two rational branches give all three regimes with the stated equality cases, plateaux, and limiting infimum. Each premise, threshold boundary and strict inequality was checked analytically, and the standalone verifier corroborates several thousand algebraic instances. No finite test is used as proof of infinite quantifiers.

## Originality — PASS, with documented residual risk

The June 2026 paper by Shah, Li, Gokmen, Kalantzis, Horesh, and Xi motivates the problem by introducing reliable identity safeguarding for analog approximate-inverse preconditioning in its §3.4, equation (3.20). That full-text passage explains damping qualitatively and provides numerical comparisons, not the present exact robust first-step minimax ratio, duplicated-eigenmode effect, and critical error frontier. The 2021 analog inversion paper by Feinberg and collaborators examines hardware compensation and accelerated solves. Kalantzis et al. (2021) give a noise-bound convergence analysis for preconditioned Richardson iteration, with additive write errors but no reliable-identity minimax optimization for one GMRES step. The 2020 general preconditioner survey by Pearson and Wathen and the classical one-step Kantorovich bound give necessary background but not, in the inspected material, the joint minimax classification. Searches for inverse-preconditioner identity shifts, diagonal write noise, and worst-case GMRES damping did not reveal an equivalent statement. These searches cannot prove global novelty; an equivalent classical robust-condition-number reduction is a genuine remaining literature risk. No novelty is attributed to simultaneous diagonalization or the Kantorovich inequality.

## Mathematical value — PASS

The exact \(\omega\) choice in an analog/digital safeguard, the sharp noise level beyond which the safeguard cannot outperform a bare identity map, and the discontinuous two-versus-three-dimensional design law are motivated quantities for the inverse-error model itself. The change from \(\omega\sim (\mu+L)\delta^2/2\) in dimension two to \(\omega=\delta\) in every higher dimension is structural rather than a numerical tuning accident: a duplicate large-eigenvalue mode permits independent positive and negative errors on the same spectral level. The global classification is natural and complete, not a single arbitrary parameter slice, and it exposes the precise limitation of small spectral errors when deciding whether a reliable identity branch should dominate. This does not imply a universal device rule or multi-step solver rate.

## Closest prior literature and scope risk

- Shah et al., *Hybrid Digital-Analog Approximate Inverse Preconditioning for Krylov Methods*, arXiv:2606.17227v1, §3.4 (full paper inspected).
- Feinberg et al., *An Analog Preconditioner for Solving Linear Systems*, HPCA 2021, DOI:10.1109/HPCA51647.2021.00069 (complete publicly available paper inspected).
- Kalantzis et al., *Solving Sparse Linear Systems with Approximate Inverse Preconditioners on Analog Devices*, arXiv:2107.06973 (accessible complete manuscript inspected, including Appendix A error analysis).
- Pearson and Wathen, *Preconditioners for Krylov subspace methods: An overview*, GAMM-Mitteilungen (2020), DOI:10.1002/gamm.202000015 (relevant preconditioning sections inspected).
- Classical sharp Kantorovich inequality; deliberately treated as known.

The statement assumes a perfect baseline inverse, deterministic commuting perturbations bounded in the spectral norm, noiseless identity action and one exact-arithmetic right-preconditioned GMRES step. It is not a claim about general changing analog preconditioners or quantized/noncommuting perturbations. The originality determination is literature-based and not an independent audit.

Self-review: passed. Independent audit: not yet performed.
