# Independent mathematical audit

## correctness

PASS

For iid categorical draws Y_1,...,Y_n with all p_i>0 and sum p_i=1, let N_i be counts, K=sum_i 1[N_i>0], F_r=sum_j 1[N_j=r] for 1<=r<=n. The diagonal term Cov(1[N_j>0],1[N_j=r])=P(N_j=0)P(N_j=r); for i!=j, Cov(1[N_i>0],1[N_j=r])=P(N_i=0)P(N_j=r)-P(N_i=0,N_j=r). Multinomial probabilities yield the stated binomial-coefficient sum exactly, including r=n via the conventional zeroth power/event probability. I independently enumerated all 153 integer triples (a,b,c)>=0 with a+b+c=16, weighted by exact 16!/(a!b!c!) (7/10)^a(1/5)^b(1/10)^c, checked total probability 1 and computed E[K], E[F_r], E[K F_r] directly for r=1,...,16. The 16 signs are +++++-++++++---- with exactly three changes (5/6, 6/7, 12/13); fractions at 5,6,7,12,13 reproduce all five displayed exact rational values. Reconstructed the universal covariance formula independently, then checked additional exact rational profiles (1/3,1/3,1/3;n=6), (1/2,3/10,1/5;n=8), (1/2,1/4,1/8,1/8;n=5), (2/3,1/3;n=9) against multinomial enumeration. For two categories, when 1<=r<n, K F_r=2F_r pointwise since F_r vanishes when K=1, so Cov(K,F_r)=P(K=1)E[F_r]>0. For r=n, F_n=1[K=1], yielding Cov=-P(K=1)P(K=2)<0. A single category has constant K and no switches. Thus three categories are the least support for three sign reversals. These exact finite checks establish the particular witness, not a general maximum number of reversals or minimum sample size among three-category laws.

## originality

PASS

Best-of-knowledge distinct mathematical counterexample to extending the published homogeneous one-switch law to unequal sampling weights. A source-complete review of the published equal-box result shows its q=(m-1)/m, s=(m-2)/m derivation requires every p_i=1/m; its unique switch does not constrain a profile (0.7,0.2,0.1). Sagitov 2026 Lemma 1 gives a genuinely broader exact joint-occupancy-count moment/covariance identity for arbitrary q_i, and since K=m-F_0 this mechanically determines Cov(K,F_r) after substitution, so neither a general covariance identity nor numerical evaluation alone is claimed as new. The particular constructive three-reversal pattern and sharp minimal positive support under a natural challenged one-switch generalization are not stated or proved in the inspected prior work. Barbour-Gnedin 2008 proves asymptotic joint approximations for infinitely many positive frequencies with diverging variances, not a fixed three-box finite sign spectrum. The sharp rarefaction richness-trait variation-diminishing theorem involves without-replacement sampling and an individual trait mean, not F_r under iid with-replacement multinomial draws. Resultary searches returned the target itself (excluded as independent prior), the uniform one-switch result, and these neighboring but mathematically distinct results. Search nonappearance is not proof of novelty; historical exact finite covariance tables and older urn-theory texts may have equivalent examples.

## value

PASS

The same natural statistics K (observed richness) and F_r (exact-frequency spectrum) have a rigorously established single sign switch under homogeneous occupancy; the exhibited rational heterogeneous law forces three reversals at fixed sample size, showing genuine qualitative fragility, not merely rounding noise or a parameter renaming. Two positive species provably cannot have more than one switch for any sampling weights or sample size; hence m=3 is the sharp natural alphabet boundary. The finite exact witness is a motivated obstruction for attempts to extend uniform covariance phase laws to biodiversity and inhomogeneous balls-in-boxes settings. It is not a new covariance identity, not a classification of three-species models, and makes no arbitrary claim of minimal sample size n=16.

The dated certificate retains the supplied scientific assessment, sources and limitations.
