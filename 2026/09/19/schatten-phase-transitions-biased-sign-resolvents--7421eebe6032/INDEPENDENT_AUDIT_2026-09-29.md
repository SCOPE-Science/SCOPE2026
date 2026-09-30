# Independent audit — 2026-09-30

Record: `2026/09/19/schatten-phase-transitions-biased-sign-resolvents--7421eebe6032`  
Assigned and audited source tree: `208922f92696009dfd0d79022240cd94a74bb278`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `bed40f62151cfb27ecf4854e2d6c329d68b4ffe0`  
Disposition: **passed**

## Correctness

**independently_supported**. The Schatten formulas and phase diagram are correct. Walsh diagonalization immediately gives the exact Schatten p-sum, and the Mellin identity plus Tonelli gives the product integral. Finite Schatten membership forces summability of the singleton eigenvalues; exponential domination then yields sum_j exp(-2u lambda_j)<infinity for every u>0, so Kakutani's criterion makes each positive-time biased product measure absolutely continuous with respect to Haar and hence the resolvent mixture absolutely continuous. For lambda_j=sqrt(log(j+1)), the level with max F=N already contributes at least 2^{N-1}(1+tN sqrt(log(N+1)))^{-p}, excluding every finite p. For lambda_j=exp(c j^gamma), the max-index level bounds compare entropy N log 2 with energy pcN^gamma and give the claimed gamma<1/all-fail and gamma>1/all-pass regimes. In the geometric case a^j, multiplicity 2^{N-1} at scale a^{-N} gives the critical exponent d=log_a 2, weak-S_d endpoint and s_k asymptotic order k^{-1/d}. The zeta-residue grouping and the dyadic Hurwitz-zeta specialization also check.

## Originality

**qualified_supported**. Acuaviva's 2026 paper supplies the biased-sign semigroup/resolvent setting and the compact singular Schur example; its public description does not discuss Schatten membership. Schachermayer's classical singular convolution example is important prior art, but it has multiplicative product eigenvalues and can be singular while belonging to S_p for p>2. The audited reciprocal-additive resolvent spectrum behaves differently: finite Schatten membership forces absolute continuity. Targeted searches did not locate the exp(c j^gamma) phase transition, exact weak-Schatten endpoint, or geometric zeta residue. Originality is therefore supported for these spectral consequences, not for Walsh diagonalization, Kakutani, representability criteria or general Schatten facts.

## Scientific value

**meaningful_operator_ideal_classification**. The record precisely locates Acuaviva's compact Schur block beyond every finite Schatten class and supplies an explicit one-parameter family realizing arbitrary critical Schatten exponents, including a spectral-zeta residue. This sharpens the operator-ideal picture of a current Banach-space construction while clearly separating it from classical singular convolution phenomena.

## Literature and evidence checked

- https://arxiv.org/abs/2609.17283
- https://doi.org/10.1007/BFb0076303
- https://doi.org/10.2307/1969123
- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/19/schatten-phase-transitions-biased-sign-resolvents--7421eebe6032

## Limitations

- Absolute continuity is proved as a necessary consequence of finite Schatten membership; no converse is claimed.
- The exponential-weight examples classify the resolvent spectrum but are not claimed to retain all singular-measure or Schur-space properties of Acuaviva's specific sequence.
- The theorem does not classify arbitrary weight sequences.
- Schachermayer's singular S_p convolution construction is prior art and relies on a different multiplicative spectrum.
