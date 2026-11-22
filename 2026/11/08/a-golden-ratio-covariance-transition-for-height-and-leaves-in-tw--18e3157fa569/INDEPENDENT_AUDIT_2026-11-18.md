# Independent mathematical audit

## correctness

PASS

The finite tree identities were independently reconstructed: D_0=0,D_1=1 and X_i=D_i-D_(i-1) obey X_1=1, X_i=1 for B_i=1 and X_i=1-X_(i-1) for B_i=0; hence X_i in {0,1}, nondecreasing depths and H_n=D_n. The exact rooted leaf increment is A_i=1{B_(i-1)=1,B_i=0}, with forced B_1=1. Success-delimited iid geometric K with P(K=k)=p q^k yields T=K+1, R=floor(K/2)+1, S=1{K>=1}, finite moments and renewal rates v=1/(1+q), ell=pq. The classical vector renewal-reward CLT applies to centered iid block rewards, with bounded L² incomplete-block remainder. Symbolic direct evaluation of p E[(R-vT,S-ell T)^{⊗2}] produced the three claimed Σ entries exactly and det=p²q⁴(1+q-q²)/(1+q)^4>0. An independent stationary covariance proof uses A_i and X_j: Cov(X_(i-1),A_i)=pq(1-μ), Cov(X_(i+k),A_i)=-pq μ(-q)^k for k>=0, and earlier j covariance zero. Summing gives Σ_12=pq(q²+q−1)/(1+q)². Leaf indicators A_i are stationary 1-dependent with lag-one covariance -(pq)², giving Σ_22=pq(1-3pq), and X has nontrivial eigenvalue -q, giving Σ_11. The common p-reset implies geometric mixing; summable lag and nonstationary boundary corrections prove Cov(H_n,L_n) and both diagonal entries nΣ+O(1). The O(1) mean bias is negligible under sqrt(n). Exact independent enumeration of all 1,022 labelled parent-word trees through n=10 matched recursions; independent rational six-moment DP through n=500 at p=1/3,1/2,2/3 matches the asymptotic signs and bounded n-error. These finite checks corroborate algebra only; infinite CLT follows analytically. Scope: fixed 0<p<1, n+1 vertices n edges, rooted leaves; no claims at p=0/1 or for varying p_n.

## originality

PASS

Best-of-knowledge PASS for the explicit joint (height,leaf) covariance, its nondegenerate Gaussian limit and golden-ratio zero; partial coverage is substantive and explicitly credited. Same-model published November 2 height/diameter theorem and November 8 Brownian distance-field theorem already supply the first marginal limit and variance pq/(1+q)^3. Tang–Wang–Wu 2026 full paper supplies the random-tree model and trunk/branch structure. Neither establishes a leaf-dependent cross covariance or its sign transition. General finite-state/renewal-reward CLTs are standard methodology rather than a new result. Searches of published findings, same-model trees and primary tree-parameter literature did not identify an earlier full joint covariance theorem. This is qualified by unindexed equivalents or implicit abstract Markov reward calculations; a failed search is not priority certification.

## value

PASS

Height and rooted leaf count are canonical, independently motivated global geometric and branching observables in this concrete two-lag attachment law. The exact joint covariance changes sign at q=(sqrt(5)-1)/2, separating negative and positive mesoscopic dependence; at the critical parameter the limiting Gaussian coordinates are independent, despite using the same Bernoulli input. The explicit analytic threshold, not an arbitrary sampled finite case or mere generic CLT existence, is a meaningful new structural quantitative fact, and the O(1) covariance remainders sharpen its finite-n interpretation. Because prior work already covers the height marginal, value is specifically in the joint leaf comparison and transition.

The dated certificate retains the supplied scientific assessment, sources and limitations.
