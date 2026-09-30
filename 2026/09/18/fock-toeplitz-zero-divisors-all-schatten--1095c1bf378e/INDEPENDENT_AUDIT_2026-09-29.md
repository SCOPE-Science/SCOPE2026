# Independent audit — 2026-09-29

Record: `2026/09/18/fock-toeplitz-zero-divisors-all-schatten--1095c1bf378e`  
Assigned and audited source tree: `ab9161eccd0ebb9879336f4940a9db48aad60f0b`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Disposition: **passed**

## Correctness

**supported_against_primary_full_text**. Qin's primary full text was retrieved after open-access fetch attempts failed and directly confirms Lemma 2.1: T_{sigma_U}K_a=2^(-n-2)K_{D_U^*a} with D_U=diag(U/4,I_{n-2}/2), as well as the four-term unimodular Gaussian decompositions of f and g. Using C_A h(z)=h(Az), the kernel identity gives T_{sigma_U}=2^(-n-2) C_{D_U^*}^*. Because D_U^* is a unitary factor times diag(1/4,1/4,1/2,...,1/2), the normalized monomial basis yields the exact geometric-product Schatten formula. At p=1 it simplifies to 1/9 per block, so four-term trace-norm subadditivity gives 4/9 for each factor. The same diagonal contraction preserves homogeneous degree; truncation above degree m has norm at most 2^(-n-m-1) after summing four blocks, and the degree<=m space has rank binom(n+m,n). The stated singular-value and stretched-exponential bounds follow by approximation numbers. Finite sums remain in every Schatten quasi-class for 0<p<1. The zero product and nonvanishing are Qin's theorem.

## Originality

**qualified_quantitative_refinement**. Qin proves the bounded Schwartz zero-divisor pair but does not formulate the all-Schatten, trace-class or singular-value consequences in the inspected primary text. General Schatten regularity for Fock Toeplitz/localization operators is substantial prior art, so the qualitative fact that rapidly decaying symbols can yield very regular compact operators is not new. Targeted searches did not locate this explicit refinement of Qin's pair, the exact Gaussian-block Schatten formula, the uniform 4/9 nuclear bound, or the displayed tail estimate. Originality is therefore supported only for that narrow quantitative synthesis.

## Scientific value

**useful_operator_ideal_sharpening**. The result places the newly constructed two-factor zero divisors deep inside the compact-operator scale: both factors are trace class and in every Schatten quasi-ideal with explicit stretched-exponential singular-value decay. This sharply shows that standard compactness and even very strong ideal regularity do not restore the two-factor zero-product implication in complex dimension at least two.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/fock-toeplitz-zero-divisors-all-schatten--1095c1bf378e
- https://arxiv.org/abs/2609.20555
- https://doi.org/10.1016/S0022-1236(03)00166-6
- https://doi.org/10.1007/s00020-010-1768-9
- https://arxiv.org/abs/2609.16970

## Limitations

- The result is restricted to Qin's n>=2 explicit pair and does not address the still-open two-bounded-symbol question in one complex dimension.
- The 4/9 trace-norm and singular-value bounds are upper bounds and are not claimed optimal.
- General Schatten regularity of rapidly decaying Fock Toeplitz/localization operators is prior art; novelty is limited to the explicit zero-divisor refinement and quantitative estimates.
- The primary full text was accessed through the authorized Oxford retrieval only after direct arXiv/open-access full-text fetches failed in this run.
