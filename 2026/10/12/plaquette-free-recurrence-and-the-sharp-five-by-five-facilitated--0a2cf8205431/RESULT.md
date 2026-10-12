# Plaquette-free recurrence and the sharp five-by-five facilitated-exclusion threshold

## Finding

Consider the directional facilitated exclusion process on the periodic five-by-five square lattice, with a conserved particle number \(K\) satisfying \(1\le K\le24\). For every \(17\le K\le24\), there is **exactly one recurrent communicating class**. It consists **exactly** of the configurations in which every periodic \(2\times2\) plaquette contains at least one particle. In particular, the smallest particle number supporting uniqueness of the recurrent class is \(K=17\): for \(1\le K\le16\), at least two distinct recurrent classes exist by Theorem 2.1 of Kim–Lee–Seo [1].

Let \(h=25-K\) count the vacancies. The exact counts of recurrent configurations and the decomposition of the complete transition digraph are:

| Vacancies \(h\) | Particles \(K\) | Configurations | Strongly connected components | Terminal components | Recurrent configurations |
|---:|---:|---:|---:|---:|---:|
| 8 | 17 | 1,081,575 | 426 | 1 | 941,450 |
| 7 | 18 | 480,700 | 126 | 1 | 448,450 |
| 6 | 19 | 177,100 | 76 | 1 | 171,900 |
| 5 | 20 | 53,130 | 26 | 1 | 52,605 |
| 4 | 21 | 12,650 | 26 | 1 | 12,625 |
| 3 | 22 | 2,300 | 1 | 1 | 2,300 |
| 2 | 23 | 300 | 1 | 1 | 300 |
| 1 | 24 | 25 | 1 | 1 | 25 |

The unique recurrent class is active in each sector, since its cardinality exceeds one. Transient states in sectors with \(K=17,\ldots,21\) are exactly the configurations containing a fully vacant periodic \(2\times2\) plaquette.

## Assumptions and scope

Write \(\mathbb T=(\mathbb Z/5\mathbb Z)^2\), and let \(\eta:\mathbb T\to\{0,1\}\), with \(\eta(x)=1\) indicating occupancy. The process preserves \(\sum_{x\in\mathbb T}\eta(x)=K\). For every site \(x\) and each of the four coordinate directions \(v\in\{\pm e_1,\pm e_2\}\), a directed transition moves a particle from \(x\) to \(x+v\) at positive rate if and only if

\[
\eta(x-v)=1,\qquad \eta(x)=1,\qquad \eta(x+v)=0.
\]

All coordinates and plaquettes are periodic modulo five. A recurrent communicating class is a strongly connected component with no outgoing directed transition; this equivalence is exact for any finite continuous-time Markov chain with positive rates on precisely these directed edges. The result does not depend on the positive magnitudes of the legal transition rates.

For \(x=(r,c)\), the associated elementary plaquette is \(B_x=\{(r+i,c+j):i,j\in\{0,1\}\}\), modulo five. Define the plaquette-free set by

\[
\mathcal R_K=\{\eta:\sum_x\eta(x)=K,\ \sum_{y\in B_x}\eta(y)\ge1\ \text{for every }x\in\mathbb T\}.
\]

The theorem asserts that \(\mathcal R_K\) is the unique recurrent class for every \(17\le K\le24\).

## Proof

**1. An analytic closed-set lemma.** The property that every elementary \(2\times2\) plaquette contains a particle is preserved under every legal jump on the five-by-five torus. Let a legal jump remove occupancy from \(x\) and add it at \(x+v\); the facilitator at \(x-v\) remains occupied. If a plaquette becomes empty for the first time, it must contain \(x\) and exclude \(x+v\). Along the coordinate direction \(v\), a two-site interval containing \(x\) but not \(x+v\) necessarily contains \(x-v\). This puts the occupied facilitator inside the alleged empty plaquette, a contradiction. Thus \(\mathcal R_K\) is closed.

**2. Exact finite transition-graph certificate.** Encode the vacancy set as a 25-bit integer \(b\), where bit \(5r+c\) is one exactly when \((r,c)\) is vacant. For each \(h\in\{1,\ldots,8\}\), enumerate **all** \(\binom{25}{h}\) such bitmasks in increasing order, with an injective index array. Construct every directed legal edge by visiting all 25 sites and all four directions: its pre-jump vacancy bits at (facilitator, source, target) are (0,0,1), and the successor mask is \(b\) XOR the source and target bits. The reverse-neighbor iterator uses the inverse post-jump pattern (0,1,0), so it exactly enumerates predecessors without storing a second graph.

The included `verify_fep5.cpp` implements iterative Kosaraju strongly connected decomposition: a forward depth-first finishing order, a second depth-first search on exactly the reversed edges, and a full final scan of outgoing edges from every component. It marks a component terminal precisely when no legal edge leaves it. Separately, at **every enumerated state**, it tests all 25 periodic plaquette masks and checks the exact Boolean equivalence between terminal-component membership and absence of a completely vacant plaquette. The eight sectors, all component counts, terminal-component counts, cardinalities, and directed-edge totals are checked against the displayed integer results. Hence for every sector \(17\le K\le24\), the unique terminal component is exactly \(\mathcal R_K\). This is an exhaustive **finite proof**, rather than a sampling argument.

**3. Independent count of the geometrically defined set.** For two vacancy-row bitmasks \(a,b\in\{0,1\}^5\), declare a vertical pair admissible if the common vacancy mask \(a\mathbin{\&}b\) has no adjacent bits on the cyclic row of length five. Let \(T_{ab}(z)=z^{|b|}\) for admissible pairs and zero otherwise, where \(|b|\) is the number of vacant bits. Since the five rows form a cyclic sequence, the coefficient of \(z^h\) in \(\operatorname{tr}(T(z)^5)\) counts exactly the vacancy patterns with no empty \(2\times2\) plaquette. Exact integer polynomial arithmetic in `count_plaquette_free.py` independently gives the coefficients through degree eight as

\[
1,\ 25,\ 300,\ 2300,\ 12625,\ 52605,\ 171900,\ 448450,\ 941450.
\]

These independently reproduce the recurrent-class sizes from the transition graph.

**4. Sharpness below 17.** Kim–Lee–Seo [1, Theorem 2.1(2)] prove multiple recurrent classes whenever the number of particles is at most \(N^d-((N+1)/2)^d\) for odd side \(N\) in dimension \(d\ge2\). At \(N=5\) and \(d=2\), this becomes \(K\le16\). Joining that published lower-side result to the complete enumeration for \(K\ge17\) yields the asserted sharp finite-size threshold.

## Verification

Reproduce with C++17 and Python 3, in a directory containing the two supplied source files:

```sh
g++ -O3 -std=c++17 -Wall -Wextra -Werror verify_fep5.cpp -o verify_fep5
./verify_fep5
python3 count_plaquette_free.py
```

The graph verifier prints eight sector records and finishes with `VERIFY_OK eight high-density sectors and plaquette-free characterization`. Its largest sector contains 1,081,575 states and 17,054,400 directed transitions. The polynomial verifier finishes with `COUNT_OK`. Both were executed successfully. A separate implementation using a sparse directed adjacency matrix and an independent strongly-connected-components routine agreed on the eight sector counts. The reported results rely on a complete finite enumeration of every state and every possible legal edge, not on a probabilistic simulation or asymptotic extrapolation.

## Relationship to prior work

Kim–Lee–Seo [1] introduced the higher-dimensional directional model and established uniqueness for \(K\ge22\) and nonuniqueness for \(K\le16\) on the five-by-five torus, by specialization of their general odd-side theorem. Their proof uses fully occupied elementary boxes and does not give a recurrent-set census in the unresolved five intermediate sectors \(17\le K\le21\). The present result closes that specific gap, supplies the plaquette-free characterization, and gives exact recurrent-state counts.

Goldstein–Lebowitz–Speer [2] study long-scale density fluctuations of a one-dimensional facilitated exclusion process. Their rigorous classification is for dimension one; the higher-dimensional dynamics mentioned in their introduction permits facilitation by any occupied neighbor rather than exclusively the collinear neighbor behind the jump. Neither its object nor its conclusions give the present five-by-five directed transition graph or its recurrent-class threshold.

## Limitations

The exact connectivity step is finite and specific to the 25-site torus. It does not prove the same threshold or the same recurrent-set description for larger odd tori or higher dimensions. No claim is made about spectral gaps, mixing times, hitting times, or the probability distribution on transient paths. The finite-state proof presumes precisely the stated directional facilitation rule and positive rates for every allowed edge. The source paper's low-particle nonuniqueness theorem is used, rather than independently reproduced, for \(K\le16\).

## References

[1] S. Kim, S. Lee, I. Seo, *Facilitated Exclusion Process in Higher Dimensions: Recurrent Structure and Transient Dynamics*, arXiv:2609.18885v1 (first public September 16, 2026), especially Theorem 2.1 and Sections 2.1, 3.1–3.2. https://arxiv.org/html/2609.18885v1

[2] S. Goldstein, J. L. Lebowitz, E. R. Speer, *Approach to Hyperuniformity in the One-Dimensional Facilitated Exclusion Process*, arXiv:2407.02652 (first public July 2, 2024), especially Sections 1–2. https://arxiv.org/html/2407.02652v2
