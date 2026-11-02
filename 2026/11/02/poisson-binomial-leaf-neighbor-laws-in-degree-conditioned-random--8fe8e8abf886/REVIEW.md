# Scientific review: Poisson-binomial leaf-neighbor laws in degree-conditioned random labeled trees

## Correctness — PASS

Deleting the marked vertex identifies the prescribed-degree uniform tree with a uniform forest of labeled rooted trees having exactly the prescribed number of components. A singleton component is precisely a leaf adjacent to that vertex. Lagrange coefficient extraction proves the exact degree-conditioned probability-generating polynomial. A direct pole-and-multiplicity argument proves that the degree-preserving differential operator sends polynomials with nonpositive real zeros to polynomials of the same kind; iteration establishes real-rootedness. Exchangeable polarization and the established strongly Rayleigh theorem imply negative association. Independent Prüfer-word enumeration, exact factorial-moment checks, pairwise covariance inequalities and rational Sturm-root tests in `verify.py` produced 27,106 successful assertions. The all-size results rely on proofs, not numerical extrapolation. The n=2 model is deliberately outside the theorem, and the star is treated separately.

## Originality — PASS, qualified

The exact *local* statement combines the marked-root degree condition, the leaf-neighbor count law, its nonpositive zeros, and negative association of the entire exchangeable leaf-neighbor vector. Pitman's rooted-forest enumeration establishes the underlying combinatorial correspondence, not this conditional real-rooted local statistic. The polarization and strongly Rayleigh implications are established by Borcea, Brändén and Liggett, not new here. Bóna–Mező's nonsingleton-partition polynomial counts a different set-partition statistic, so its real-rootedness does not by itself imply the stated fixed-component rooted-forest law. The closest comparison to preexisting degree/leaf results concerns global leaves or degree conditioning in a different random-tree model, not the leaf-neighbor vector. A general older forest-real-rootedness theorem or more specialized enumerative study could entail this law; implicit priority remains a residual risk, not a proof of uniqueness.

## Mathematical value — PASS

Uniform labeled trees are a canonical finite random-tree model. Local pendant-neighbor counts measure the distribution of branching around a distinguished degree class; this is not captured by the marginal degree law or by global leaf counts. An exact Poisson-binomial factorization supplies ultra-log-concavity, concentration tools and finite-sample mean/variance control, while strong Rayleigh extends the conclusion to arbitrary disjoint sets of leaf-neighbor indicators. The result is structurally informative, rather than a small numerical correction or a restatement of Cayley's formula.

## Closest published literature and limits

Jim Pitman, *Coalescent Random Forests*, technical report 457 (1996), §§2–3, https://statistics.berkeley.edu/sites/default/files/tech-reports/457.pdf ; Jim Pitman, *The Multinomial Distribution on Rooted Labeled Forests*, report 499 (1998), §§1–2, https://live-statistics.pantheon.berkeley.edu/sites/default/files/tech-reports/499.pdf ; J. Borcea, P. Brändén, T. M. Liggett, *Negative Dependence and the Geometry of Polynomials* (2007), Cor. 4.7 and Thm. 4.9, https://arxiv.org/pdf/0707.2340 ; M. Bóna, I. Mező, *Real Zeros and Partitions without Singleton Blocks* (2007; 2015 version), https://arxiv.org/pdf/0705.2734 . All broader theorems cited are treated as prior work. No claim is made for arbitrary weighted trees, or that an existing general real-rootedness theorem cannot subsume the new theorem.

Self-review: passed. Independent audit: not yet performed.
