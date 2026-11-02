# Scientific review

## Correctness — PASS

For five positive squared-column masses summing to one, the volume distribution is exactly \((p_i+p_j)/4\) on unordered pairs and the amplification exactly \(1/(p_i+p_j)\). A five-cycle excludes eight or more light edges below \(\theta=2/5\). With seven light edges, a heavy-star case contradicts normalization; the remaining heavy triangle gives the exact bound \(12\theta-2\). At most six light edges gives \(6\theta\). All regimes have explicit strictly positive attaining masses. These arguments verify all inequalities, equality cases, strict domain boundaries and the jump at \(t=5/2\), not just discrete tests. `verify.py` passed the documented 127,600 exhaustive rational checks, eleven attaining profiles, and 100 expectation identities.

## Originality — PASS with residual historical risk

Kozyrev--Osinsky (arXiv:2610.08576v1) provides an expectation formula and volume-sampling algorithms, not the five-column worst-case *distributional* envelope or competing sharp tails. Dereziński--Warmuth (arXiv:1705.06908) studies unbiased pseudoinverse estimation; Dereziński--Warmuth--Hsu (NeurIPS 2018) studies regression error and tail lower bounds, not this precise matrix amplification-tail maximization. Searches for aliases involving size-biased pair sums, low-sum threshold graphs, volume-sampling upper tails and rank-one pseudoinverses produced no identified equivalent or stronger implication. No exhaustive historical-priority proof is claimed; an equivalent small weighted-graph inequality could exist elsewhere.

## Value — PASS

The source establishes optimality of a universal mean bound, while this theorem supplies an exact input-uniform upper-tail safety calibration for the smallest fixed testbed here with competing six-light-edge and seven-light-edge extremizers. The switch at \(t=3\) distinguishes adversarial column-energy patterns; the one-sided jump at the known mean \(5/2\) shows what expectation-only analysis misses. The result has a natural numerical linear algebra object, exact attained finite-sample risk and a structural obstruction proof. It does not assert high-dimensional concentration or arbitrary-rank applicability.

## Closest literature and limitations

- Kozyrev and Osinsky, *Subset selection for matrices by volume sampling*, arXiv:2610.08576v1, Sections 1--5 and Appendix, https://arxiv.org/html/2610.08576v1.
- Dereziński and Warmuth, *Unbiased estimates for linear regression via volume sampling*, arXiv:1705.06908, introductory and moment statements in the accessible nine-page PDF, https://arxiv.org/pdf/1705.06908; not every remaining section inspected.
- Dereziński, Warmuth and Hsu, *Leveraged volume sampling for linear regression*, NeurIPS 2018, introduction and theorem material, https://proceedings.neurips.cc/paper_files/paper/2018/file/2ba8698b79439589fdd2b0f7218d8b07-Paper.pdf; no claim of complete full-document exclusion.

Self-review: passed. Independent audit: not yet performed.
