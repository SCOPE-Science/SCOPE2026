# Review

## Correctness
PASS. The construction prescribes pairwise distinct basis images and extends them to permutation unitaries because input and output dimensions both equal \(Md\). With \(r=\min\{M,d\}\), the two displayed unit range vectors have exactly \(r\) coincident key-index components. When \(d<M\), every remaining component of the first vector has an \(X\)-basis coordinate orthogonal to the distinguished \(|0\rangle_X\), so no additional inner product survives. Therefore their overlap is exactly \(r/M\). The published upper bound gives equality. The finite verifier independently reconstructs the projection ranges for representative dimensions and agrees with the analytic formula.

## Originality
PASS, scoped to the sharpness statement. The closest primary source, arXiv:2609.32515v1, proves the decoded privacy-test upper bound \(\|PQ\|\le\min\{1,d_C/M\}\) and identifies the shared-system dimension factor in its proof, but the inspected lemma and proof do not supply an equality construction. arXiv:2608.01308v1 has the analogous Bell-target upper bound, again without the inspected sharpness family. arXiv:1602.08898v1 supplies the older privacy-test converse framework rather than this decoder-placement geometry. Semantic searches for shared-receiver overlap sharpness, Bell-projector overlap, and the exact \(d_C/M\) dependence did not reveal a dominating statement. Residual risk remains that the elementary construction appears in older operator-algebra language under different terminology.

## Value
PASS. The factor \(d_C/M\) is the main local incompatibility estimate used by the recent private-capacity strong-converse proof. Exact attainment for every pair \((M,d_C)\) establishes a sharp structural boundary: neither the coefficient nor the dependence on the shared receiver dimension can be improved at this lemma without additional hypotheses. This directly identifies where future improvements to the complete exponent must obtain extra information, while avoiding any claim that the downstream exponent itself is optimal.

Same-model review: passed. Independent audit: not yet performed.
