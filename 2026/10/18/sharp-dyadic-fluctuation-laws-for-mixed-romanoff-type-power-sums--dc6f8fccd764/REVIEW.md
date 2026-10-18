# Scientific review: sharp dyadic fluctuation laws for mixed Romanoff-type power sums

## Correctness — PASS
The precise domain is every fixed integer \(r\ge2\), dyadic cutoff \(2^N\) with integer \(N\ge2\), and positive integer indices \(a,b\). The proof identifies exactly \((N-1)\lfloor(N-1)^{1/r}\rfloor\) labeled pairs and exactly \(\binom{\lfloor(N-1)^{1/r}\rfloor}{2}\) two-representation collisions, with no other binary collision. The fractional-root block count is uniform in interval endpoints and has error \(O_r(K^{1-1/r})\); the dyadic-block perturbation argument preserves this error in the empirical secondary distribution. The exact enumerator passed 294 instances, without being used as an infinite proof. The proof does not rely on unpublished computational results.

## Originality — PASS, subject to recorded risk
Yan (arXiv:2610.13691v1), inspected through its accessible full HTML text, cites only Chen's leading asymptotic for the set cardinality and proves statements on prime-plus-set representations. The exact dyadic formula, multiplicity classification, and effective nondegenerate secondary limit law do not follow as logical conclusions from this first-order result. The Ding–Li and Chen articles address related Romanoff sets and representation functions; their available abstracts and summaries do not assert the present law, but their full texts were not accessible for complete exclusion. Targeted published-result searches including the formula, aliases, two-bit collision multiplicity, and uniform second-order oscillation found no matching statement; nearest records concern unrelated binary block counts, summatory floor functions, and digital fluctuations. An earlier implicit derivation via elementary root equidistribution is a genuine residual originality risk. Search failure alone is not treated as proof of novelty.

## Mathematical value — PASS
The source's counting lemma is an essential quantitative input to current Romanoff-type density arguments. The theorem fixes the sharp second-order scale in the simplest asymmetric restricted-power family, derives a complete effective distribution of fluctuations, and proves that no constant second asymptotic coefficient exists. The boundary between \(r=2\) and \(r\ge3\) reflects a genuine competition between representation collisions and lattice cutoff error; the full range and uniform law are natural precise invariants, not arbitrary finite slices. It does not settle prime-representation density or optimality of the Kolmogorov convergence exponent.

## Closest literature and limitations
1. Xiao-Hui Yan, *On a conjecture on Romanoff type representations*, arXiv:2610.13691v1 (2026-10-09); full HTML studied.
2. Y.-G. Chen, *On Integers of the Form \(p+2^{k_1^{r_1}}+\cdots+2^{k_t^{r_t}}\), II*, DOI:10.1007/s11464-026-0057-0 (2026); leading counting asymptotic quoted by Yan, full text unavailable.
3. Yuchen Ding and Liangxun Li, *On a conjecture on Romanoff type sumsets*, arXiv:2606.06118v2 (2026); abstract and accessible synopsis studied, full text unavailable.
4. Relevant OEIS floor-root sequences (including A022554) found in a direct formula search are different summatory invariants; this finding does not rely on table omission.

The result is limited to exact dyadic cutoffs, fixed integer \(r\), and internal sumset counting, and independent external scientific validation has not been performed.

Self-review: passed. Independent audit: not yet performed.
