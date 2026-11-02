# Independent mathematical audit

## correctness

PASS

With a odd and k of popcount 7, k≥127 and n≥7. Since gcd(a,2a−1)=1 the semigroup is numerical. For higher-index summands, setting T=Σ2^i and C=#summands yields value aT−(T−C), and T is even. The binary splitting lemma is valid: T/2 is sum of exactly C binary powers iff popcount(T/2)≤C≤T/2, by repeated splitting of powers into pairs. For each residue −u, 1≤u≤a−1, the proposed piecewise even T (2u, a+1, a+3, a+5, a+7) has C=T−u meeting those bounds using the five weight counts 7,8,8,9,8; direct inequalities bound every representative by M=a(a+6)+3 and ensure strict inequality unless u=a−3. For a hypothetical smaller residue-3 representative, discard copies of a; u=a−3+ta (t≥0). If t≥1, aT−u≥2a²−4a+3>M for a>10. If t=0, even T≥a−1 and value<M forces T∈{a−1,a+1,a+3,a+5}; C∈{2,4,6,8} is less than the respective popcount 7,8,8,9. Thus M is the uniquely largest Apéry element and Frobenius is M−a. The proof covers arbitrary admissible coefficients and exponents, not just sampled k,n. Independently recomputed the exact record Git tree from eight fetched blob identities; exact Dijkstra on three admissible k,n plus exhaustive witness inequalities and one lower-weight boundary case corroborates but does not prove the family.

## originality

PASS

Best-of-knowledge PASS for the new evaluated infinite-family closed Frobenius formula and unique maximizing Apéry residue, not for the computability of individual instances. The highly relevant Liu–Xin–Ye–Yin Theorem 5.2 provides every Apéry value via greedy representation, a substantial general algorithm; its evaluated Frobenius Theorems 5.4–5.5 explicitly require one of the first two greedy digits nonzero. The article singles out q=63, where both are zero, as outside those formulas. Srivastava–Thakkar treat coefficient 2^r+1, with much smaller binary weight. The separate general-repunit note assumes d>0, while these semigroup generators use d=−1. No searched published finding or exact table states a uniform seven-one maximum/residue. The new residue-complete witness construction and popcount obstruction are a nontrivial evaluation of an already computable generic finite maximum; a generic algorithm is acknowledged but not equivalent to a proved uniform closed form. Residual risk of hidden or later derivations remains.

## value

PASS

The Frobenius number and top Apéry residue are natural numerical-semigroup invariants; a closed formula for an infinite full binary-Hamming-weight class is meaningful. Weight seven includes k=127=2^6+63, the first explicit q=63 family singled out as beyond the two standard greedy-prefix closed-form theorems. The proof determines a sharp global maximum among a−1 residues using a structural binary-splitting obstruction rather than merely recomputing finitely many table entries. The exact maximal residue may inform investigations of the Apéry-poset geometry and complements of nearby Proth semigroups. No genus, type or other-weight classification is asserted.

The dated certificate retains the supplied scientific assessment, sources and limitations.
