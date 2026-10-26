# Minimal geodetic sets of cycle bouquets: a product formula and real-rooted spectrum

## Finding
Let \(t\ge 2\) and \(n_1,\ldots,n_t\ge3\) be integers. Form a *cycle bouquet* \(B=C_{n_1}\vee\cdots\vee C_{n_t}\) by identifying one designated vertex \(h\) from each cycle and identifying no other vertices. A set \(S\subseteq V(B)\) is *geodetic* if every graph vertex belongs to some shortest path whose endpoints both lie in \(S\). It is *inclusion-minimal geodetic* if it is geodetic but none of its proper subsets is geodetic. Write
\[
\mathcal M_B(z)=\sum_{S\text{ inclusion-minimal geodetic}}z^{|S|},\qquad
b(n)=\binom{\lceil n/2\rceil}{2}.
\]
Then the exact cardinality polynomial is
\[
\boxed{\mathcal M_B(z)=\prod_{i=1}^{t}\left(b(n_i)z^2+\mathbf1_{\{2\mid n_i\}}z\right).}
\]
Every inclusion-minimal geodetic set avoids \(h\). Its intersection with an odd-length petal is exactly one of \(b(n_i)\) admissible pairs of nonhub vertices. Its intersection with an even-length petal is either the unique nonhub vertex antipodal to \(h\), or one of \(b(n_i)\) admissible pairs. Label the vertices of a petal \(0,1,\ldots,n-1\) cyclically with \(h=0\): the pair \(\{a,b\}\), \(1\le a<b\le n-1\), is admissible precisely when
\[
\max\{a,b-a,n-b\}\le\lfloor n/2\rfloor
\]
and neither endpoint is antipodal to \(h\) when \(n\) is even.

If \(o\) of the petal lengths are odd, the geodetic number and the *upper geodetic number* (minimum and maximum cardinalities of inclusion-minimal geodetic sets) are
\[
\boxed{g(B)=t+o,\qquad g^+(B)=2t.}
\]
Every integer between these two bounds is realized as the size of an inclusion-minimal geodetic set. All zeros of \(\mathcal M_B(z)\) are real and nonpositive; in particular its nonzero coefficient sequence is log-concave and has no internal zeros. The difference \(g^+(B)-g(B)=t-o\) is unbounded over bouquets of even cycles. For the petal lengths \((4,5,6)\), one obtains \(\mathcal M_B(z)=3z^4+12z^5+9z^6\), giving exactly \(24\) inclusion-minimal geodetic sets.

## Assumptions and scope
Graphs are finite, simple, connected, and unweighted. A geodesic is an ordinary shortest path and *geodetic* requires existence of at least one such path for each vertex (not every shortest path). Endpoints of a geodesic are included on the path. For every \(i\), the petal \(C_{n_i}\) contains all its cycle edges and shares only \(h\) with other petals. The statement concerns inclusion-minimal sets, not merely minimum-cardinality sets and not strong geodetic sets with one selected path per pair. The case \(t=1\) is excluded because removal of \(h\) from a set need not remain geodetic.

## Proof
**1. Separation at the shared vertex.** Fix a geodetic set \(S\). Each petal must contain a selected nonhub vertex. Indeed a nonhub vertex of petal \(i\) cannot lie on a shortest path joining two vertices outside its petal, because such a path would have to revisit \(h\). If \(h\in S\), remove it. Any geodesic between \(h\) and a selected vertex \(s\) in petal \(i\) can be extended through \(h\) to a selected vertex \(u\) in a *different* petal: the concatenation is a shortest \(s\)-\(u\) path. Geodesics not using \(h\) as an endpoint remain. Hence \(S\setminus\{h\}\) is geodetic, so a minimal geodetic set never includes \(h\).

For \(S\) avoiding \(h\), let \(S_i\) be its intersection with the nonhub vertices of petal \(i\). Then \(S\) is geodetic in the whole bouquet **if and only if** each \(S_i\cup\{h\}\) is geodetic within its own cycle. For necessity, any shortest path covering a nonhub vertex in petal \(i\) either joins two chosen vertices within that petal or is the segment from a chosen petal vertex to \(h\) of a cross-petal shortest path. Sufficiency follows by replacing each local \(h\)-to-\(s\) geodesic by a shortest cross-petal path from \(s\) to a selected vertex of another petal; local paths between two selected vertices require no replacement. Deleting one vertex of \(S_i\) affects exactly the corresponding anchored local covering condition. Thus global inclusion-minimality is equivalent to the independent local inclusion-minimality of the anchored sets \(S_i\cup\{h\}\).

**2. Gap criterion for a marked cycle.** On a cycle \(C_n\) with at least two marked vertices, list the positive edge lengths of the cyclic gaps between consecutive marked vertices. Put \(L=\lfloor n/2\rfloor\). The marked vertices form a geodetic set **if and only if all gaps are at most \(L\)**. If some gap has length greater than \(L\), its complementary arc is strictly shorter than it and contains all other marked vertices, so shortest paths between marked vertices cannot cover the interior of the long gap. Conversely, when a gap has length at most \(L\), that very gap is a shortest path between its marked endpoints and hence covers its own interior. The union of all such gaps is the cycle.

For an anchored marked set containing \(h\), deleting a nonhub mark merges its two neighboring gaps. Provided at least one other mark remains, the mark is essential precisely when the sum of those neighboring gaps is greater than \(L\). If there were three or more nonhub marks and each were essential, take the first and third nonhub marks in cyclic order after \(h\); their adjacent gap pairs are disjoint. Each pair would have sum greater than \(L\), forcing their combined length to exceed \(2L+2>n\), impossible. Thus any anchored inclusion-minimal set contains at most two nonhub marks.

**3. Local one- and two-vertex sets.** An anchored singleton \(S_i=\{s\}\) is geodetic exactly if both gaps between \(h\) and \(s\) have length at most \(L\), which occurs precisely for an even cycle with \(s\) antipodal to \(h\). For a pair \(S_i=\{a,b\}\) in increasing cyclic order after \(h=0\), the three gaps are \(a,b-a,n-b\). The gap criterion gives their maximum at most \(L\). The pair is anchored inclusion-minimal unless one of its elements is already the antipode, since that singleton is then an anchored geodetic set. This proves the stated structural characterization.

Count the admissible pairs. For \(n=2m+1\), the positive gap triples bounded by \(m\) and summing to \(2m+1\) correspond, by taking deficits from \(m\), to nonnegative triples summing to \(m-1\); they number \(\binom{m+1}{2}=b(n)\). For \(n=2m\), the bounded positive gap triples summing to \(2m\) number \(\binom{m+2}{2}-3\) by inclusion-exclusion (only one gap can exceed \(m\)). Exactly \(2(m-1)\) of these place one nonhub marked vertex at the antipode of \(h\). Their difference is \(\binom m2=b(n)\). These calculations hold also for \(m=1\) and \(m=2\) as applicable.

**4. Factorization and consequences.** Each petal contributes independently either \(b(n_i)\) choices of size two, or, for an even petal, one choice of size one. Multiplication yields \(\mathcal M_B(z)\). Odd petals force two selections; each even petal permits one or two, establishing the full interval of sizes \([t+o,2t]\). Factoring gives
\[
\mathcal M_B(z)=z^{t+o}\left(\prod_{n_i\text{ odd}}b(n_i)\right)
\prod_{n_i\text{ even}}\bigl(1+b(n_i)z\bigr).
\]
All factors have nonpositive real roots, proving real-rootedness. Newton's inequalities (or the standard elementary-symmetric-coefficient inequality) yield log-concavity for the nonzero coefficient sequence. Taking arbitrarily many even petals makes the extremal cardinality gap arbitrarily large. This completes the proof.

## Verification
The independent Python verifier `verify.py` builds each bouquet from the original graph definition, computes all-pairs shortest-path distances using breadth-first search, and determines geodesic membership from the distance identity \(d(a,v)+d(v,b)=d(a,b)\). It then exhaustively enumerates nonempty selected-vertex sets, retains precisely the geodetic sets for which every one-vertex deletion fails, and compares **the actual family of sets** with the formula-based local-product construction. It checks the complete cardinality distribution as a separate assertion. The recorded command `python3 verify.py` checked \(104644\) nonempty subsets across \(28\) distinct two- and three-petal bouquets, and all assertions passed. These are finite corroborations; the preceding proof establishes the universal quantifiers.

## Relationship to prior work
Bergougnoux, Defrain, and Mc Inerney (2023) study enumeration of inclusion-minimal solution sets for metric-graph problems, including geodetic sets, and analyze general complexity and split-graph reductions. The inspected primary article does not give the stated cycle-bouquet family enumeration. Ekim and Erey (2014) give a block-decomposition method for computing a *minimum* geodetic set on block-cactus graphs, and discuss its relation to hull sets; such an optimum-size algorithm does not determine all inclusion-minimal sets or their cardinalities. Evangelista and collaborators (2023) enumerate **all** geodetic subsets of sunlet and triangular-snake graphs, different objects and without the inclusion-minimal condition. Cactus strong-metric-dimension results concern a different invariant. The present result is the complete inclusion-minimal-set enumerator, structural description, and root/spectrum consequences for cycle bouquets; it does not claim that the basic cycle gap criterion or the minimum geodetic number in this family are independently new.

## Limitations
The bouquet must contain at least two cycles and have exactly one common articulation vertex; the theorem is not a formula for arbitrary cactus or block-cactus graphs. The real-rootedness conclusion applies to the inclusion-minimal geodetic polynomial, not the full polynomial of all geodetic sets. No claim is made that a computational sample proves the infinite theorem. Bibliographic priority may be affected by equivalent results under graph-hull or other terminology that are absent from the inspected primary works and records. Independent mathematical review has not been performed.

## References
1. B. Bergougnoux, O. Defrain, F. Mc Inerney, *Enumerating minimal solution sets for metric graph problems*, arXiv:2309.17419 (first posted 2023-09-29), https://arxiv.org/abs/2309.17419 and https://arxiv.org/pdf/2309.17419.
2. T. Ekim and A. Erey, *Block decomposition approach to compute a minimum geodetic set*, RAIRO Operations Research (2014), DOI:10.1051/ro/2014019, https://doi.org/10.1051/ro/2014019.
3. *Geodetic polynomials of n-sunlet and triangular snake graphs*, 2023, DOI:10.17654/0974165823064, https://pphmjopenaccess.com/aadm/article/download/1093.
4. *The Strong Resolving Graph and Strong Metric Dimension of Cactus Graphs*, Mathematics 8 (2020), article 1266, DOI:10.3390/math8081266, https://doi.org/10.3390/math8081266.
