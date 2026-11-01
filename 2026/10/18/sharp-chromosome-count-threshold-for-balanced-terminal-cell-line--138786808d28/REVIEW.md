# Independent mathematical audit

## correctness

PASS

Reconstructed the model with n=2m complete binary divisions, independent node/chromosome fair coins, complementary daughter end-shortening, zero allowed. Viability at n requires exactly m first-end losses per chromosome; monotonic budgets make it equivalent to survival at all preceding nodes. For a fixed leaf p=2^{-n} C(n,m), so E Z=2^n p^K. For ordered distinct leaves with j shared edges, t=n-j-1 independent suffix edges, the joint single-coordinate balanced probability is q_j=2^{-j-2t} sum_{r=0}^j C(j,r) C(t,m-r-1) C(t,m-r); exact pair multiplicity 2^{2n-j-1} gives E Z^2/(E Z)^2=(E Z)^{-1}+sum_{j=0}^{n-1}2^{-j-1}(q_j/p^2)^K. q_{n-1}=0. Conditioning on one balanced leaf yields q_j<=p M_t, and the exact binomial central-mass ratio M_t/p<=sqrt(n/t) (checked via adjacent even terms) establishes R_j<=sqrt(n/(n-j-1)). Fixed j gives R_j=1+O_j(1/n). For K<=(2 log2-delta)n/log n, j<n/2 is uniformly geometrically dominated, n/2<=j<=(1-eta)n is O(n exp(-c n+O(n/log n))), and late prefixes are exp(-c n) by eta log2<delta/2. Hence second-moment ratio→1 and L2 concentration; Chebyshev gives P(Z>0)→1. For upper K>(2 log2+delta)n/log n Stirling makes E Z→0 and Markov gives P→0. n=2m yields coefficient 4 log2. Verified the source tree SHA exactly from seven pinned Git blobs. Independent exact rational tester examined 4,290 (m,j) central-mass/joint bounds for m<=65 and exhaustively enumerated four tiny complete genealogy cases (8+64+512+32,768 fair coin assignments), matching E Z and E Z². No code log is treated as proof of the asymptotic argument.

## originality

PASS

Best-of-knowledge new sharp terminal-viability probability transition for the K-coordinate complementary-daughter binary genealogy. The same-rule 2026 Baland–Toupance–Villemonais source proves a large-initial-population deterministic limit/CLT, not a single-root first-order K_m~4 log2 m/log m success threshold. Wattis–Qi–Byrne concerns continuum telomere-length distributions, Benetos et al. 2024 studies continuous-time mean semigroups, Malthusian behavior, telomerase and simulations, while Benetos et al. 2023 treats intergenerational age-structured inheritance. None of the materially inspected results implies the all-m fixed terminal generation survival claim and L2 concentration, and targeted Resultary and web searches found no such theorem. This is a bounded priority assessment, not proof of absolute novelty.

## value

PASS

The event of a viable cell at the maximal generation of a telomerase-free complementary-daughter genealogy is a natural first-passage/terminal-survival observable, and the chromosome count K is the biologically motivated constraint dimension. The upper transition is a simple first-moment calculation, but lower survival with high probability is not: genealogical sharing could create severe clustering. The proven L2 concentration and sharp first-order constant identify when correlations do not move the threshold, yielding a nontrivial high-dimensional branching survival result. It is a mathematical asymptotic under a stylized model; no claim of clinical parameter prediction or exact critical window.

The dated certificate retains the supplied scientific assessment, sources and limitations.
