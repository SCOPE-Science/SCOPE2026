# Scientific review: exact same-species adsorption cluster intensities

## Correctness (C): PASS

For each \(0<p<1\), \(q=1-p\), \(0<t\le1\), and integer \(k\ge2\), the decreasing-priority dependency construction defines the infinite-volume one-attempt process. The half-line endpoint ODE yields \(a(t)=H_p(t)\) and \(1-b(t)=\cosh(\sqrt{pq}t)-\sqrt{q/p}\sinh(\sqrt{pq}t)\). The all-\(A\) interval event forces exactly \(k\) attempted \(A\)-labels, with independent left and right exterior boundary survival probabilities, proving \(Q_k(t)=H_p(t)^2(pt)^{k-2}\). Two-site inclusion-exclusion and the one-site boundary integral then give all \(\lambda_k(t)\), including \(\lambda_1(t)\). The conditional cluster-count distribution is an exact geometric law when \(pt<1\), which holds under the theorem hypotheses.

The independent exhaustive finite-path checker tests all relative arrival orders, active site subsets and color assignments for paths up to seven sites, and compares 270 distinct finite joint-event probabilities in exact rational arithmetic. Its total of 360 assertions includes half-line approximation and cluster-intensity identities. These checks do not replace the analytic infinite-volume argument. Critical boundaries \(k=2\), \(p\in(0,1)\), \(t\in(0,1]\), and the singleton exception are all explicitly treated.

## Originality (O): PASS, with residual historical-priority risk

The strongest source is do Amaral and dos Santos, [arXiv:2306.09786](https://arxiv.org/abs/2306.09786) (first posted 2023-06-16), which defines the identical one-attempt model and solves its one-site densities. Its full preprint was examined for all-contiguous occupancy and maximal run-length results; it supplies neither. The new statement is the entire \(Q_k\), \(\lambda_k\) and shifted-geometric law, not the already-known one-site density or half-line method.

A similar-looking one-species nearest-neighbor model in [arXiv:2210.05627](https://arxiv.org/abs/2210.05627) forbids any two adjacent occupied sites, and the two-color model in [arXiv:2211.04622](https://arxiv.org/abs/2211.04622) allows repeated trials. Their statements and implications cannot cover the present all-\(A\) cylinder probability for exactly one attempt per site. General graph adsorption methods in [arXiv:math/0503519](https://arxiv.org/abs/math/0503519) use a different blocking interaction. Published record queries for alternative cluster/run terminology and comparison with accessible prior claims uncovered no equivalent theorem. Unindexed exact-cylinder work could still precede this analysis; search noncoverage is not a proof of novelty.

## Value (V): PASS

Cluster lengths are a natural structural observable for irreversible two-species deposition. The full intensity sequence and its exact geometric tail give information that cannot be inferred from the one-site density alone, and the singleton formula completes the length-profile classification. The theorem applies to all positive times and all biases and supplies finite-order analytic benchmarks for investigating spatial fragmentation; no general downstream theorem is needed to make this exact classification meaningful.

## Limitations and evidence

The result applies only to single-try independent marks, the one-dimensional nearest-neighbor lattice and opposite-species inhibition. It does not assert inter-cluster independence, Gaussian process limits or generalization to repeated attempts. Finite enumeration is a verification check, not an infinite proof. An independent mathematical audit and exhaustive historical-priority review remain outstanding.

Self-review: passed. Independent audit: not yet performed.
