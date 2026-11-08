# Independent mathematical audit

## correctness

PASS

PASS — Seasonal maps F_i(x)=P_i x/(1+c_iᵀx) compose exactly to G(x)=Mx/(1+Cᵀx), where M=P_{i3}P_{i2}P_{i1} and Cᵀ=c_{i1}ᵀ+c_{i2}ᵀP_{i1}+c_{i3}ᵀP_{i2}P_{i1}. Induction gives G^k(x)=M^k x/[1+Cᵀ Σ_{j<k} M^j x]. M is strictly positive because f_i,s_i,t_i>0. Perron–Frobenius expansion for every x≥0 nonzero proves λ<1 extinction, λ=1 kx_k→v/(Cᵀv), and λ>1 attraction to the unique fixed vector (λ−1)v/(Cᵀv). Exact 2×2 multiplication gives tr(P3P2P1)−tr(P2P3P1)=det[(f_i,s_i,t_i)], common determinant −∏f_i s_i, and λ relative to one determined by T+K relative to one. Independent SymPy algebra confirmed all trace/determinant identities and exact rational season example (T123=98/125, T132=211/250, K=81/500), proving one calendar extinct and the other persistent. The full nonlinear limit and intermediate-phase continuity, not finite trajectories, give the global all-initial-data assertion.

## originality

PASS

PASS, qualified. Mertens et al. 2006 already show noncyclic permutations affect growth in linear periodic matrix populations. Caswell nonlinear periodic sensitivity and Cushing–Ackleh net reproductive thresholds likewise provide antecedents. The combined explicit 3×3 orientation determinant, projectively saturated nonlinear closed iterates, universal critical 1/k rate, and strict global extinction/persistence reversal for exactly three environments were not seen as deductions of those published results. Broader positive matrix-fractional map literature remains a material subsumption risk.

## value

PASS

PASS — This is a sharp, universal-initial-state calendar-order threshold linking an oriented three-trait determinant to real extinction or stable nonzero seasonal cycles. The explicit critical scaling and rational reversal example are meaningful for a natural nonlinear structured-population model; not a purely cosmetic permutation identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
