# Spectral twins separate under majority dynamics: exact Shrikhande–rook attraction censuses

## Finding
Let \(R=K_4\square K_4\) be the \(4\times4\) rook graph, and let \(S\) be the Shrikhande graph. They are nonisomorphic, strongly regular, cospectral graphs with parameters \((16,6,2,2)\) and adjacency spectrum \(6^1,2^6,(-2)^9\). For synchronous binary strict-neighbor majority with the previous bit retained at a tie, their **complete** finite-state dynamics differs as follows:

| Invariant | Rook \(R\) | Shrikhande \(S\) |
|---|---:|---:|
| Fixed configurations | 302 | 142 |
| Primitive two-cycle orbits | 1,197 | 685 |
| Periodic configurations | 2,696 | 1,512 |
| Sharp maximum first-periodic-entry time | 3 | 5 |
| Initial configurations reaching all-zero consensus | 20,789 | 28,221 |
| Initial configurations reaching all-one consensus | 20,789 | 28,221 |

In particular, \(F_R^5=F_R^3\), but the sharp global iterate identity for \(S\) is \(F_S^7=F_S^5\). Every recurrent orbit has primitive period one or two. Under independent fair binary initial opinions, the exact eventual unanimity probabilities are \(20789/32768\) and \(28221/32768\), respectively; the gap is \(929/4096\), approximately 22.68 percentage points. Thus neither strong-regularity intersection parameters nor the full adjacency spectrum determines the nonlinear majority attractor census, sharp transient length, or eventual unanimity probability.

## Assumptions and scope
The vertex set of both labelled graphs is \(V=\mathbb Z_4\times\mathbb Z_4\), indexed by \(v=4i+j\) for \(0\le i,j<4\). In \(R\), distinct vertices are adjacent when their first or their second coordinates agree. In \(S\), distinct vertices are adjacent when their difference belongs to \(\{\pm(1,0),\pm(0,1),\pm(1,1)\}\) modulo four, with the two signs of \((1,1)\) coupled. Every state \(x\) is a map \(V\to\{0,1\}\); its integer encoding is \(\sum_{v=0}^{15}2^v x_v\). For \(G\in\{R,S\}\), let \(F_G\) update all sixteen sites simultaneously. A vertex whose six neighbors contain at least four ones becomes one, a vertex with at most two such neighbors becomes zero, and a vertex with exactly three such neighbors keeps its present bit.

The first-periodic-entry time of a state is the smallest \(t\ge0\) for which \(F_G^{t+2}(x)=F_G^t(x)\). The basin of a recurrent orbit consists of every initial state ultimately entering that orbit. All state and orbit counts are for labelled configurations, without quotienting by graph automorphisms or by global bit complementation.

## Proof
**1. Equal linear parameters but distinct graphs.** Directly from either adjacency rule, every vertex has six neighbors and every two distinct vertices have two common neighbors, whether adjacent or not. Consequently the real adjacency matrices satisfy \(A_G^2=4I+2J\). The all-ones eigenvector has eigenvalue six, and the other fifteen eigenvalues are six copies of two and nine copies of minus two (using the zero trace). Nevertheless \(R\) has exactly eight four-cliques (four rows and four columns), whereas \(S\) has none (the induced neighborhood of a vertex is a six-cycle). Hence the two graphs are not isomorphic and have identical adjacency spectra.

**2. Exact exhaustive recurrence certificate.** Write \(N_G(v)\) for the bit mask of the six neighbors of vertex \(v\), and let \(c_v(x)=\operatorname{popcount}(x\mathbin{\&}N_G(v))\). The complete transition function is precisely
\[
 F_G(x)=\sum_{v=0}^{15}2^v\,\mathbf 1\!\left[c_v(x)>3\ \text{or}\ (c_v(x)=3\ \text{and}\ x_v=1)\right].
\]
The standalone program `verify_functional.py` constructs all \(2^{16}=65,536\) states and their successors. It verifies \(F_R^5(x)=F_R^3(x)\) and \(F_S^7(x)=F_S^5(x)\) for **every** state \(x\), then enumerates the entire directed functional graph. Each recurrent orbit is represented by its smallest integer state; every other state is assigned to its unique recurrent orbit by reverse traversal of its forward path. The counts in the table follow by summing orbit representatives, their basin sizes, and the minimal distances to the periodic components.

**3. Independent direct-iteration certificate.** The standalone C++17 program `verify_direct.cpp` constructs adjacency by separately evaluating coordinate differences, computes majority by summing sixteen signed neighbor opinions, and for every initial integer \(0\le x<65536\) directly calculates nine successive states. It finds the first \(t\) with equality \(F_G^{t+2}(x)=F_G^t(x)\), the primitive period, and the minimum member of the eventual orbit. This produces independently the same complete orbit counts, first-entry distributions, individual-basin histograms, and consensus basins. Neither program reads the other's output. Both independently check the common-neighbor identities and four-clique distinction. Complete source and recorded outputs are included, so these finite claims are decidable by replay rather than inferred from sample experiments.

**4. Sharpness.** For the rook graph, state encoding 359 evolves through \(359\to23\to1\to0\), first periodic at time three. For the Shrikhande graph, state 1901 evolves as \(1901\to18162\to1652\to1632\to1056\to0\), first periodic at time five. The exhaustive iterate identities in step 2 supply matching universal upper bounds, proving sharpness. Since the all-zero and all-one states are fixed, their basin cardinalities give the stated exact eventual unanimity probabilities.

## Verification
Both exact full-state verifiers were run with the provided sources. The first-entry-time population is \((2696,14136,29984,18720)\) for \(R\), at times \(0,1,2,3\), and \((1512,9304,26240,18496,9024,960)\) for \(S\), at times \(0,1,2,3,4,5\). Each vector sums to 65,536. All configurations entering a two-cycle do so within one update, whereas later entrants reach fixed points. Individual-basin histograms are preserved in `functional_output.json` and `direct_output.txt`; they independently sum to 65,536 for each graph. The graph certificates establish the common parameter set and four-clique separation.

Replay with Python 3 using `python3 verify_functional.py` and with a C++17 compiler using `g++ -std=c++17 -O2 verify_direct.cpp -o verify_direct && ./verify_direct`. The programs are self-contained and have no third-party dependencies. The recorded output files give the exact expected results.

## Relationship to prior work
The finite-graph eventual period-one-or-two theorem is classical (Goles and Olivos); Benjamini, Chan, O'Donnell, Tamuz and Tan (2014, arXiv:1405.2486) describe its role and study almost-sure and random-graph behavior. Their paper does not provide the present two-graph exact comparison. Agur, Fraenkel and Klein (1988) enumerate fixed configurations for a cyclic three-neighbor majority rule, not for these six-regular graphs. The rook graph is a line graph of \(K_{4,4}\), so general half-factor descriptions of majority two-cycles on line graphs are relevant and can cover part of its periodic structure; they do not imply the Shrikhande census, either complete basin distribution, or the sharp cross-graph unanimity contrast. The two graphs' shared parameters and distinct local geometry are classical. No claim is made to discovering that cospectral graphs may have different **graph-theoretic** invariants; the specific contribution is the exact majority-dynamical separation.

## Limitations
This is a finite, reproducible classification of **these two 16-vertex graphs only**, not a theorem for all cospectral or strongly regular graphs. Numerical outputs are exact integer counts from exhaustive finite enumeration, not independently certified by an external auditor. The computations and displayed proofs establish the claims conditional on correct implementation of the elementary graph and update definitions; they are independently implemented but not formally verified. Previous or unindexed published tabulations of the same majority-dynamics statistics remain a historical-overlap risk. The result does not imply anything about majority evolution under alternative tie conventions, asynchronous updates, or nonuniform initial distributions.

## References
1. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz, and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, arXiv:1405.2486v1 (first publicly posted 2014-05-11), https://arxiv.org/abs/1405.2486.
2. Z. Agur, A. S. Fraenkel, and S. T. Klein, *The number of fixed points of the majority rule*, Discrete Mathematics **70** (1988), 295–302, https://doi.org/10.1016/0012-365X(88)90005-2.
3. S. S. Shrikhande, *The uniqueness of the \(L_2\) association scheme*, Annals of Mathematical Statistics **30** (1959), 781–798. Graph facts and bibliographic note: https://jaanos.github.io/tables/graphs/Shrikhande.html.
