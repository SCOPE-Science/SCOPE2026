# Sharp realizing-length spectrum for homopolymer-free ternary digram rankings

## Finding
Let \(\Sigma=\{0,1,2\}\). A circular word \(w=w_0\cdots w_{n-1}\), indexed modulo \(n\), is *homopolymer-free* when \(w_i\ne w_{i+1}\) for every index. For each ordered pair \(uv\) with \(u\ne v\), write \(c_{uv}(w)\) for the number of occurrences of \(uv\) at successive cyclic positions. A *strict six-transition ranking* is the increasing ordering of these six counts, provided all six are positive and distinct.

The feasible labeled rankings number **60** (a count already implied by the earlier unrestricted nine-coordinate rank census). **The finding here is their sharp shortest-realization spectrum and structural classification:** the minimum realizing circular lengths are distributed as follows:

| Minimum length | Number of labeled rankings |
| ---: | ---: |
| \(21\) | \(24\) |
| \(22\) | \(12\) |
| \(26\) | \(12\) |
| \(27\) | \(12\) |

In particular, the **sharp worst-case shortest realizing length is \(27\)**, and exactly \(12\) of the \(60\) realizable rankings require that length. The five interval-interleaving types form five alphabet-permutation/reversal orbits of size \(12\) each.

## Assumptions and scope
The word is circular, so its last-to-first ordered pair is counted. Only the six transitions between different symbols are ranked: the three identical-symbol transitions are excluded, not ranked jointly with the other six. All six allowed frequencies must be positive and pairwise unequal. Alphabet labels are fixed in the count \(60\); reversal and simultaneous alphabet relabeling are used only for the orbit classification. The minimum length is the number of cyclic positions, equivalently the sum of the six transition counts. No fixed-length exact-spectrum formula beyond minimum realizations is claimed.

For explicit notation, the clockwise directed triangle is \(E_+=(01,12,20)\), and the reverse triangle is \(E_-=(10,21,02)\), each paired positionwise with the opposite edge. A ranking is a permutation of \(\{01,10,12,21,20,02\}\) from lowest to highest frequency.

## Proof
**1. Flow characterization.** For any circular word, the number of transitions entering a symbol equals the number leaving it. Setting \(X=(c_{01},c_{12},c_{20})\) and \(Y=(c_{10},c_{21},c_{02})\), the three balance equations are equivalent to
\[
X_1-Y_1=X_2-Y_2=X_3-Y_3=\delta.
\]
If \(\delta=0\), three pairs of counts are equal, contradicting strictness. Hence \(\delta\ne0\). Changing the cyclic orientation if necessary, let \(d=|\delta|\ge1\), and let the three smaller counts, sorted increasingly, be
\[
y_1=a,\qquad y_2=a+p,\qquad y_3=a+p+q
\]
with positive integers \(a,p,q\). Their three opposite larger counts, in the same paired order, are \(x_i=y_i+d\). Distinctness of all six values requires \(d\notin\{p,q,p+q\}\). Conversely, any such positive parameters determine a positive balanced profile once the three smaller counts are assigned bijectively to one orientation of the directed triangle; there are \(3!\) assignments for each choice of orientation.

**2. Sufficiency via a cyclic Euler walk.** A positive profile on all six off-diagonal directed edges induces a connected and strongly connected directed multigraph on three vertices, with indegree equal to outdegree at every vertex by Step 1. An Eulerian circuit traverses each edge with its prescribed multiplicity. Reading successive vertices of that circuit produces a cyclic homopolymer-free word with exactly those six counts. Thus the positive integral balance condition is both necessary and sufficient, with no additional word-realization obstruction.

**3. Classification of rank orders.** Sorting the three lower values yields the same order for their three upper partners because all three upper partners have common offset \(d\). Denote a lower endpoint by \(O\), its larger partner by \(C\), and forget labels temporarily. Every feasible interleaving is a length-six Dyck word with three \(O\)'s and three \(C\)'s: every initial segment has at least as many \(O\)'s as \(C\)'s. Conversely, all five Dyck words arise with the indicated strict parameter inequalities:

| Interleaving | Necessary and sufficient strict inequalities | Least \((a,p,q,d)\) | Least length |
| --- | --- | --- | ---: |
| `OCOCOC` | \(d<\min(p,q)\) | \((1,2,2,1)\) | \(21\) |
| `OCOOCC` | \(q<d<p\) | \((1,3,1,2)\) | \(26\) |
| `OOCCOC` | \(p<d<q\) | \((1,1,3,2)\) | \(22\) |
| `OOCOCC` | \(\max(p,q)<d<p+q\) | \((1,2,2,3)\) | \(27\) |
| `OOOCCC` | \(d>p+q\) | \((1,1,1,3)\) | \(21\) |

Indeed, exactly \(5\) Dyck words have semilength three, and checking the relative positions of \(y_1,y_2,y_3\) and \(y_1+d,y_2+d,y_3+d\) gives the displayed inequalities. The total cyclic length is
\[
n=\sum_{i=1}^3(x_i+y_i)=6a+4p+2q+3d.
\]
Its positive coefficients show that minimizing each type reduces to the smallest integral parameters satisfying that type's strict inequalities. The five minimizers in the table follow directly. For the `OOCOCC` case, \(d\) must lie strictly between both gaps and their sum, forcing \(p,q\ge2\); the minimum is attained by \(p=q=2,d=3\). Consequently this type truly needs length \(27\), not merely a construction of that length.

**4. Labeled counts and symmetries.** For each interleaving, there are exactly two choices for which oriented directed triangle supplies the lower counts, and exactly \(3!\) assignments of its lower positions to the three labeled arcs. Thus each type yields \(2\cdot3!=12\) distinct strict rankings, for \(5\cdot12=60\) in total. The action of the six alphabet permutations and reversal acts freely on the six distinct labeled ranks and transitively on the twelve rankings of each type. Hence precisely five orbits, each of size twelve, occur. Two types attain minimum \(21\), and the remaining three respectively attain \(26,22,27\), giving the claimed distribution and sharp maximum.

## Verification
The standalone `verify_ternary_ranks.py` reproduces the classification by two separate routes. First it examines every ordered sextuple of distinct positive integer counts with total length at most \(27\), tests the three in/out-balance equations, and records the shortest realization for each increasing ranking; exactly \(21,600\) sextuples are visited. Second it enumerates the independent \((a,p,q,d)\) parameterization and arc assignments, comparing all shortest lengths and rank identities. The included `shortest_rank_witnesses.json` lists all \(60\) increasing rankings, their minimal integer profiles, and one explicit circular Eulerian word each. The checker recomputes all six cyclic transition frequencies from each witness and verifies that no adjacent symbols are equal.

Command from a directory containing both artifacts: `python3 verify_ternary_ranks.py --witnesses shortest_rank_witnesses.json`. Expected summary: `TERNARY_SIX_RANKS_PASS ranks=60 min_lengths=21:24,22:12,26:12,27:12 maximally_required=27 direct_vectors_checked=21600`.

The code is a finite cross-check: the unrestricted-length classification is proved by the balance, interleaving and Euler-circuit arguments above; finite enumeration alone is not used as proof of necessity for arbitrary lengths.

## Relationship to prior work
Raviv, Schwartz and Yaakobi (arXiv:1708.02146, version 1, 2017) introduced rank-modulation feasibility on cyclic DNA profile counts, described the exact flow/Eulerian criterion, developed Catalan-order machinery, and derived general realization-length bounds. They and the later Beeri–Schwartz treatment give the exact count \(30{,}240\) of feasible strict rankings on all nine ternary digrams. **That existing result already implies the present coarse count \(60\):** any strict order of six positive nonloop counts can be extended to a strict order on all nine entries by placing three independently adjustable loop counts in \(\binom{9}{3}3!=504\) ways. To realize any placement, first multiply a positive balanced six-vector by a sufficiently large integer, then insert three distinct positive loop weights between the chosen six levels (or above them); adding loops preserves flow. Conversely, restricting a positive balanced nine-vector to the six nonloop entries and discarding loop counts leaves a positive balanced strongly connected digraph. Hence \(30{,}240/504=60\). **Neither the count \(60\) nor generic Eulerian feasibility is claimed new.** What the inspected source does not imply is the exact *minimum loop-free realizing length for each of the 60 ranks*, the sharp bound \(27\), its frequency distribution, or the corresponding optimized integer interval constraints.

Beeri and Schwartz (arXiv:2101.06033, version 1, 2021) constructed larger rank-modulation code families and discussed forbidden-gram constraints. The full-nine feasibility count entails the 60-value six-coordinate count by the extension identity just proved, but the **optimized no-loop representative lengths** are a different invariant from the unconstrained length of a shortest representative with all nine frequencies distinct. General polynomial realization bounds and cyclic profile-enumeration tables likewise do not provide the four sharp length values or the classification of which strict ranks require each length.

## Limitations
This result is restricted to the three-symbol alphabet, adjacent ordered pairs, circular words, positive support on all six distinct-symbol transitions and strict ranking of those six frequencies. Removing any of those hypotheses changes the classification problem. The optimum length \(27\) is the maximum over *shortest realizations of rankings*, not the maximum possible word length; any realized ranking can be represented by longer words as well. The code and witness census do not establish novelty by themselves. Closely related unindexed literature may contain equivalent statements, although no such coverage was found in the inspected sources. Independent validation has not been performed.

## References
1. N. Raviv, M. Schwartz and E. Yaakobi, *Rank-Modulation Codes for DNA Storage*, arXiv:1708.02146v1 (7 August 2017), https://arxiv.org/pdf/1708.02146 . The longer version appeared as *Rank-Modulation Codes for DNA Storage With Shotgun Sequencing*, IEEE Transactions on Information Theory 65 (2019), 50–64.
2. N. Beeri and M. Schwartz, *Improved Rank-Modulation Codes for DNA Storage with Shotgun Sequencing*, arXiv:2101.06033v1 (15 January 2021), https://arxiv.org/pdf/2101.06033 .
3. K. G. Banerjee and A. Banerjee, *Bounds on Size of Homopolymer Free Codes*, arXiv:2305.10741v1 (2023), https://arxiv.org/abs/2305.10741 . Background on the adjacent-repeat constraint, not an exact rank enumeration.
