# Independent mathematical audit

## correctness

PASS

PASS: The restricted worth v(T)=Σ_{j∈T}[Σ_{i∈T}a_ij+F(B_j(N\T))] is carefully distinguished from recomputation of an induced graph. Assume the insertion-budget inequality F(U⊎{b})≤F(U)+b. For S⊆N define x_j^S=Σ_{i∈S}a_ij+F(B_j(N\S)), giving exact efficiency Σx^S=v(S). For every T⊆S, split external incoming multiset B_j(N\T)=B_j(N\S)⊎B_j(S\T); iterating the budget controls every coalition constraint termwise. Conversely any violating U,b builds an in-star target j with distinguished p and outside sources whose restriction to {p,j} has v({j})>v({p,j})-v({p}) and empty core. Singleton normalization F({b})=b implies v(N\{j})=v(N)-Σ_i a_ij, and every core coordinate ≤ incoming sum, hence uniqueness by efficiency. For min, max, mean and rank statistics the budget follows from order-statistic coordinate Lipschitz bound; the ranks k(m+1)≤k(m)+1 cover medians and quantiles. Independently checked exact rational core inequalities in three-node graphs and four aggregators (C5_OK), not a substitute for universal symbolic proof.

## originality

PASS

PASS, qualified: Ryzák–Kroupa arXiv:2605.18157v1 proves total balancedness and core uniqueness for minimum aggregation, and explicitly calls alternative external aggregation stability an open research direction in Section 6. Bandhana–Kroupa–García 2024 introduced the minimum model and incoming-weight core. The new universal iff insertion criterion includes necessity via a strict two-player obstruction and nonminimum stable classes; neither inspected primary result states this. A generic cooperative-game marginal-subadditivity theorem could imply the characterization at a higher level, which remains a priority risk.

## value

PASS

PASS: Classifies the entire natural operator class permitting stable inherited-worth subgames, rather than a handful of examples. Its exact converse and unique-core refinement provide decision and construction tools for graph games; the prior 2026 authors specifically identify this family as open.

The dated certificate retains the supplied scientific assessment, sources and limitations.
