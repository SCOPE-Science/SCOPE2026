# Self-review: exact inverse-bias law for ordered sparse Schur-clique trees

## Correctness — PASS

The exact star Schur complement is \(P=I-\mathbf1\mathbf1^{\mathsf T}/n\). The RCHOL single-clique algorithm on equal incident weights samples \(n-1\) independent increasing-parent links with conductances \((n-i)/n\), exactly as normalized in [1, Algorithm 3] and [2, Algorithm 3]. Each link has mean conductance \(1/n\) against each potential later endpoint, proving primal unbiasedness. In the backwards-built tree, each newly introduced pendant edge has series resistance \(n/(n-i)\). Uniform independent parent choice and the induction hypothesis give \(\mathbb ER(k,j)=n/(n-k)+(n-k-1)n/(n-k)=n\) for every pair. Double-centering the all-pairs effective resistance matrix proves \(\mathbb ET^\dagger=(n/2)P\). The deterministic final edge has resistance \(n\), giving a Rayleigh quotient \(n/2\) in the inverse and the stated upper bound on the smallest nonzero eigenvalue.

The actual packaged standard-library `verify.py` was executed successfully. It enumerated every parent map for sizes 2 through 8 (5,913 trees) and checked all pair-resistance and edge-conductance expectations using exact rational arithmetic. Finite enumeration corroborates but does not substitute for the infinite-family proof. Nullspaces, ranges, reciprocal conductance/resistance conventions and normalization were checked.

## Originality — PASS, with residual risk

**Exact claim under comparison:** equality of the entire mean pseudoinverse to \((n/2)P\) and deterministic resistance \(n\) for one fixed pair, for the actual ordered `SampleClique` on an equally weighted star center eliminated first. This is narrower than global solver guarantees and stronger than the source's expected-matrix identity.

The complete relevant method section and appendices of Chen–Liang–Biros [1] describe the ordered sampling, its unbiasedness and connectedness, but do not give the exact inverse-moment law. Gao–Kyng–Spielman [2] prove the essentially identical tree and expected update and discuss its practical limitations, but not the scalar expectation for pseudoinverses. Kyng–Sachdeva [3] establish an approximation theorem under other sampling/splitting conditions, not an unsplit one-tree inverse law. The later CAST analysis [4] introduces a different order-independent spanning-tree distribution and edge rescaling; its local minimax leverage criterion is not the inverse-moment statement for `SampleClique`. Known matrix Jensen inequalities give only qualitative inverse bias. The named prior-equivalence, broader-coverage, exact-table and claim-implication checks are detailed in `AUDIT.json`, including actual search strings, sources and applicability.

Residual priority risk: an exact ordered recursive-tree resistance law may exist in unindexed specialized electrical-network/probabilistic literature; mathematical independence from all external published results is not certified. The source algorithm implicitly makes the induction possible, but its earlier published theorem is not the same statement, nor an explicit stronger inverse claim.

## Value — PASS

The exact \(n/2\) **isotropic** inverse inflation is a structural risk law for a genuine numerical-linear-algebra primitive, not an arbitrary finite lookup. It isolates a mathematically important distinction: unbiased estimated Schur complement and connected sampled graph do not control expected effective resistances, nor the smallest centered eigenvalue of each sample. Its growth rate is exact in neighborhood degree, and the same claim supplies a fixed-pair deterministic spectral obstruction. That makes it a useful calibration example for designing sparse approximate-Cholesky local updates and interpreting inverse-sensitive objectives. The result does not pretend to establish how a full multistep solver behaves; the motivating inverse observable is resistance, a standard invariant of graph Laplacians.

## Closest literature and limitations

Closest: [1] `SampleClique` and [2] `CliqueTreeSample` (identical unsplit equal-weight tree law); [3] spectral factorization under distinct sampling conditions; [4] different spanning-tree distribution. The equal-weight, center-first, one-tree restriction is essential. The deterministic eigenvalue bound is not asserted optimal, and no claim of universal failure of random Cholesky preconditioning is made.

Self-review: passed. Independent audit: not yet performed.
