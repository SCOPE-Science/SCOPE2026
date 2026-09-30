# Independent audit — 2026-09-29

Record: `2026/09/18/rounded-cluster-allocation-variance-reversal--3aa05569afb8`  
Assigned and audited source tree: `0023a5cf815d3a02d909b4fa249ac476c4d98f20`  
Audited repository state: `SCOPE-Science/SCOPE2026` `eff2c6312cec5b0dee5115e5f42211a853092dfb`  
Current RESULT.md blob: `870aaef72cb4744095ff856e16b7d5efbe85898e`  
Disposition: **passed**

## Correctness

**independently_reproduced**. The arbitrary-count variance identity and counterexample are correct. Independence gives Var(Ghat_cl)=sum p_k^2 sigma_k^2/m_k; subtracting from the uniform-with-replacement variance (sigma_W^2+sigma_B^2)/m yields exactly the displayed criterion with q_k=m_k/m. For the rational example, independent exact arithmetic gives mu_1=2, mu_2=-1, sigma_1^2=1083/50, sigma_W^2=7581/500, sigma_B^2=189/100, and total variance 4263/250. With m=2, nearest proportional counts are unambiguously (1,1), giving clustered variance 53067/5000 versus random variance 4263/500; the excess is 10437/5000 and the ratio is exactly 361/290. All first-cluster gradients are positive and all second-cluster gradients negative, so normalization makes the two groups exactly cosine-separated. With m=10 the exact counts (7,3) restore the source ANOVA reduction, confirming that rounding rather than the decomposition causes the reversal.

## Originality

**supported_targeted_correction**. Niknia-Wang's September 2026 paper publicly claims lower variance for proportional gradient-clustered sampling. Inspection of the source text distinguishes its practical rounded allocation from the theoretical derivation that assumes exact positive-integer counts m n_k/N. Classical stratified-sampling literature already contains Neyman allocation and exact-integer allocation theory, so none of that is new. Searches found no public correction applying the arbitrary-count variance formula to this new sampler or giving the stated cosine-compatible reversal. The originality claim is therefore accepted narrowly as a paper-specific correction and explicit counterexample.

## Scientific value

**high_value_targeted_correction**. The counterexample hits the bridge between the implementable sampler and its advertised variance/convergence guarantee: a clean rounded allocation can increase selection variance by about 24.5 percent even with perfect angular cluster separation. The exact criterion and fallback/Neyman remedies make the result immediately useful without disputing the source theorem under its exact divisibility assumption.

## Literature and evidence checked

- https://github.com/SCOPE-Science/SCOPE2026/tree/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/18/rounded-cluster-allocation-variance-reversal--3aa05569afb8
- https://arxiv.org/abs/2609.16370
- https://www.census.gov/library/working-papers/2016/adrm/rrs2016-03.html
- https://doi.org/10.1080/00031305.2012.733679
## Limitations

- The result does not refute the source theorem when exact proportional integer counts exist.
- It addresses independent sampling with replacement, matching the source analysis, not without-replacement designs.
- The published experiment's realized cluster sizes are not reported, so no claim is made that its empirical runs encountered the reversal.
- Neyman allocation and integer-allocation optimization are classical; novelty is the exact application and source-specific counterexample.
