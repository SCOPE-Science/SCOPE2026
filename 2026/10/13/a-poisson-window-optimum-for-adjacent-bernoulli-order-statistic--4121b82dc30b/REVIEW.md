# Self-review

**Correctness — PASS.** The nested indicator identities give the exact finite-sample Pearson correlation, and positivity of both indicator variances holds for every parameter in the stated open domain. Global optimization is justified: the bounds \(R_n\le 1/(1+nq)\) and \(R_n\le nq/(2-nq)\) for small \(nq\) exclude escaping optimizing sequences. The Poisson-window limit and the unique positive root of \(e^c=1+c+c^2\) then force the unique limiting scale and the sharp constant. The verifier independently compares 28 rational finite instances and confirms four numerical asymptotic instances, not as replacements for the proof.

**Originality — PASS, with residual risk.** The 2021 paper of López-Blázquez and Salamanca-Miño treats the exact family and reports finite numerical maximal squared correlations (including its binary-support Table 3), so neither their computational framework nor finite results are claimed as new. Material inspected from the complete 27-page full text, including the introduction, definitions, tables, discussion and conclusions, did not exhibit the large-sample optimum, the Poisson scaling theorem, or the unique transcendental calibration. The 2022 Papadatos paper and the closest published finite three-atom/two-draw result concern different parameter regimes. Searches across alternate formulations did not locate the limit, but coverage under nested event/Poisson threshold formulations remains possible.

**Value — PASS.** The result closes a natural family-wide asymptotic optimization left beyond finite numerical tables. It identifies a nonzero sharp dependence constant, even though fixed Bernoulli parameters have vanishing correlation, and exactly specifies the rare-event probability at which maximal dependence is retained. This is a structural optimized limit, not a recomputed table entry.

**Limits.** No finite-sample parameter uniqueness, convergence rate, higher-order expansion, arbitrary parent family result, or independent validation is claimed.

Self-review: passed. Independent audit: not yet performed.
