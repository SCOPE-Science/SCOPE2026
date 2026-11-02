# Five vertices are the sharp binary-opinion edge-insertion polarization threshold

## Finding
For a finite **connected simple undirected graph** \(G\) with unit-weight edges and a binary innate opinion vector \(s\in\{-1,+1\}^{V(G)}\), consider the symmetric Friedkin–Johnsen expressed equilibrium \(z_G=(I+L_G)^{-1}s\) and **centered** polarization
\[
P_G(s)=\sum_{v\in V(G)}\left(z_G(v)-\frac{1}{|V(G)|}\sum_{w\in V(G)}z_G(w)\right)^2.
\]
For an absent edge \(e\), let \(G+e\) add that edge at unit weight. Every connected graph with at most four vertices satisfies \(P_{G+e}(s)\le P_G(s)\) for **every** binary vector and every absent edge. Five vertices are sharp: among all \(728\) connected labeled five-vertex graphs, exactly \(480\) of the \(100480\) labeled triples \((G,e,s)\) strictly reverse this inequality. Up to vertex relabeling and the global opinion flip \(s\mapsto-s\), these \(480\) triples consist of **exactly two orbits**, each containing \(240\) triples.

With vertices numbered \(0,1,2,3,4\), the two representatives are:

1. The five-path with edges \(\{02,04,12,13\}\), newly added edge \(01\), and \(s=(1,-1,-1,1,-1)\). Its exact increase is \(8/405\). More strongly, an added edge of arbitrary weight \(t>0\) has increase \(8t^2/[5(4t+5)^2]>0\).
2. The triangle-with-two-edge-tail with edges \(\{01,04,12,13,23\}\), newly added edge \(02\), and \(s=(1,1,-1,1,-1)\). Its unit-edge increase is \(18123/1250600>0\).

Here a string such as \(02\) is an edge connecting vertex \(0\) to vertex \(2\); all unspecified edges are absent. The counts refer to labeled *triples*, so each fixed graph can participate with multiple nonedges and innate vectors.

## Assumptions and scope
The initial network is connected, simple, undirected, unweighted and has \(2\le n\le5\). The FJ stubbornness coefficient is one at every vertex. The innate opinions are exactly the two values \(-1,+1\), though their mean need not vanish. Each intervention inserts exactly one initially missing edge with unit weight. Polarization is centered squared Euclidean norm, not the polarization-plus-disagreement index. Multiplying polarization by \(1/n\) does not alter any comparison. The separate all-positive-weight statement is asserted only for the displayed five-path configuration.

## Proof
**Mean-centering identity.** Every graph Laplacian satisfies \(L\mathbf1=0\), so \((I+L)^{-1}\mathbf1=\mathbf1\) and both old and new expressed vectors have the same mean as \(s\). Consequently, when comparing the same innate vector, the difference of centered polarization equals the difference of the raw squared norms \(\|(I+L)^{-1}s\|_2^2\). This permits exact rational arithmetic without subtracting means at every test.

**Exhaustive finite cutoff, with complete state space.** For each \(n=2,3,4,5\), order all \(\binom n2\) vertex pairs lexicographically. Iterate all integers from \(0\) through \(2^{\binom n2}-1\) as edge-incidence masks. Retain a mask precisely when breadth-first reachability from vertex \(0\) reaches all \(n\) vertices. Iterate every zero bit in that mask as the candidate missing edge, and every integer from \(0\) through \(2^n-1\) as a binary innate-opinion mask. Construct \(I+L_G\) and \(I+L_{G+e}\), invert both by rational Gauss–Jordan elimination with exact pivoting, multiply the inverses by the same binary vector, and compare the exact sums of squared coordinates. The accompanying complete program `verify_binary.py` implements all these operations, checks each inverse by exact multiplication, and asserts the following exhaustive results:

| \(n\) | connected labeled graphs | tested \((G,e,s)\) | strictly increasing triples |
|---:|---:|---:|---:|
| 2 | 1 | 0 | 0 |
| 3 | 4 | 24 | 0 |
| 4 | 38 | 1344 | 0 |
| 5 | 728 | 100480 | 480 |

The loops are finite and explicitly cover every graph, every eligible inserted edge, and all two-valued opinion profiles at these orders. No Monte Carlo estimate, timeout, or partial search is used. For each of the \(480\) increasing triples at order five, separately enumerate all \(5!=120\) vertex permutations and both global sign choices and take the lexicographically smallest edge-mask / candidate-edge-index / sign-mask triple. The resulting complete orbit count is \(240\) for canonical code \((58,0,9)\) and \(240\) for code \((185,1,11)\), with no other code. The code uses the same lexicographic vertex-pair ordering defined above.

**Independent exact witnesses.** For the five-path representative, write \(b=e_0-e_1\), \(H=(I+L_G)^{-1}\), \(w=Hb\). Direct exact inversion gives
\[
b^{\mathsf T}Hb=\frac45,\qquad w^{\mathsf T}s=\frac25,\qquad w^{\mathsf T}Hs=0,\qquad \|w\|^2=\frac25.
\]
The rank-one inverse formula \((I+L_G+tbb^{\mathsf T})^{-1}=H-\gamma ww^{\mathsf T}\) with \(\gamma=t/(1+4t/5)\) therefore yields
\[
P_{G+t e}(s)-P_G(s)=\gamma^2\|w\|^2(w^{\mathsf T}s)^2=\frac{8t^2}{5(4t+5)^2}>0.
\]
At unit weight this is \(8/405\). Direct exact rational inversion of the second representative gives \(18123/1250600\). Both representatives and the orbit counts are rechecked from the packaged program itself.

## Verification
Run `python3 verify_binary.py` with Python 3's standard library. The script checks all stated finite ranges with `fractions.Fraction`, verifies every matrix inverse by exact multiplication, rechecks the four row counts, canonicalizes all \(480\) increasing instances, and replays the two exact rational representatives. Its successful output begins `EXHAUSTIVE_RATIONAL_CENSUS_OK`. Only the finite-order classification through five vertices is claimed; no extension to all graph orders is inferred from this enumeration.

## Relationship to prior work
Rácz and Rigobon, *Towards Consensus: Reducing Polarization by Perturbing Social Networks* (public arXiv version June 17, 2022), Section 4.2 and Appendix A.2, derive the general single-edge polarization-update formula, show that pure polarization need not be monotone, exhibit a three-person example with **nonbinary** innate opinions, and prove a sufficient safe-update condition when two vertices share their neighborhoods. **Those facts and formulas are prior art.** They do not assert a minimal order or a complete isomorphism census specifically for two-valued innate profiles on connected unweighted graphs. The present finite binary classification does not contradict their three-person nonbinary example.

Bhalla, Lechowicz, and Musco study local edge evolution and distinguish pure polarization from the monotone combined index. Musco, Musco, and Tsourakakis introduce the centered polarization/disagreement optimization formalism. Zhu, Bao, and Zhang establish monotonicity of the **combined** polarization-plus-disagreement index under link addition, not of pure polarization. The binary first-order census is a different question; no claim is made to the earlier general update identities, graph-design algorithms, or general nonmonotonicity.

## Limitations
The graph classification is exact only for \(n\le5\), binary innate opinions, a single new unit-weight edge, and the homogeneous symmetric FJ model. The two-class statement is up to simultaneous vertex permutation and a global opinion-sign reversal; it is not a census of larger graphs, weighted base networks, directed influence, heterogeneous stubbornness, or edge swaps. The five-path's arbitrary-added-weight formula does not upgrade the five-vertex census to arbitrary weights. The calculations do not establish an empirical causal effect of recommended edges on human beliefs. A bibliographic risk remains that an unindexed appendix or older enumeration covers the binary census; no independent audit has been performed.

## References
- M. Z. Rácz and D. E. Rigobon, *Towards Consensus: Reducing Polarization by Perturbing Social Networks*, arXiv:2206.08996, first posted June 17, 2022. https://arxiv.org/abs/2206.08996
- N. Bhalla, A. Lechowicz, and C. Musco, *Local Edge Dynamics and Opinion Polarization*, arXiv:2111.14020, first posted November 28, 2021. https://arxiv.org/abs/2111.14020
- C. Musco, C. Musco, and C. E. Tsourakakis, *Minimizing Polarization and Disagreement in Social Networks*, arXiv:1712.09948, first posted December 28, 2017. https://arxiv.org/abs/1712.09948
- L. Zhu, Q. Bao, and Z. Zhang, *Minimizing Polarization and Disagreement in Social Networks via Link Recommendation*, NeurIPS 2021. https://proceedings.neurips.cc/paper_files/paper/2021/hash/101951fe7ebe7bd8c77d14f75746b4bc-Abstract.html
