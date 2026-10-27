# Second Poisson window and three-world common-knowledge geometry after random public announcements

## Finding
Fix a number \(r\geq1\) of epistemic agents. Uniformly sample independent equivalence relations \(E_1,\ldots,E_r\) on the \(n\)-element labelled set, and independently announce a fresh proposition true at exactly \(m=m(n)\) uniformly chosen worlds. Restrict every relation to these surviving worlds. Let \(B_n\) be the \(n\)-th Bell number and \(\rho_n=B_{n-1}/B_n\sim W(n)/n\), where \(W(n)e^{W(n)}=n\). Suppose \(m\to\infty\) and
\[
m^3\rho_n^2\longrightarrow c^3,\qquad 0<c<\infty.
\]
Thus \(m\sim c(n/W(n))^{2/3}\).

Take the connected components of the union of the surviving agents' equivalence relations. With probability tending to one, all components have at most three worlds, and every three-world component belongs to exactly one of the following types:

* A *monochromatic triple* of agent \(a\): three points in one \(E_a\)-class, with no other nontrivial relation inside the component.
* A *mixed wedge* of unordered agent colors \(\{a,b\}\), \(a\ne b\): two two-world classes, one for each agent, sharing exactly their central world.

The joint numbers \(T_a\) of monochromatic triples and \(V_{ab}\) of mixed wedges converge to **mutually independent Poisson variables**, with respective means
\[
\mathbb E T_a\longrightarrow c^3/6,
\qquad \mathbb E V_{ab}\longrightarrow c^3.
\]
For each agent there are, in probability, arbitrarily many components consisting of a single two-world \(E_a\)-class, and there are arbitrarily many isolated worlds. Therefore
\[
\boxed{\Pr(\text{every common-knowledge component has at most two worlds})
\longrightarrow \exp\bigl(-c^3[r/6+\tbinom r2]\bigr).}
\]
For any fixed first-order sentence \(\varphi\) in the relational language \(E_1,\ldots,E_r\), its probability of truth in the announced structure converges. The limit is the expectation of its truth value on the countable structure containing infinitely many isolated worlds, infinitely many isolated two-world components for each agent, and independent Poisson counts of the finitely many three-world types above. The infinite structure is used solely to specify the limit law, not as a sample from the finite ensemble.

More generally, the *three-world threshold* is sharp: if \(m^3\rho_n^2\to0\), all common-knowledge components have at most two worlds with probability tending to one; if \(m^3\rho_n^2\to\infty\) while \(m\rho_n\to0\), the probability of a component with at least three worlds tends to one.

## Assumptions and scope
Every agent's relation is selected uniformly from all \(B_n\) set partitions independently of the others; this is not an Erdős–Rényi edge model. Public announcement restricts each relation to the set satisfying a newly assigned atomic proposition. Conditional on its size, exchangeability allows taking the surviving set to be \([m]\). The asymptotics hold for fixed integer \(r\ge1\), without extra relations or valuations after restriction. Common-knowledge components are connected components of the union of the equivalence classes; they are the equivalence classes of the reflexive transitive closure of that union. The first-order result concerns the language of the agent-equivalence relations; the fresh announced predicate is identically true after updating and adds no information.

For a prescribed partition \(\tau\) of the \(m\) surviving worlds with exactly \(b\) blocks, the exact finite probability for one agent is
\[
\Pr(\Pi_n|_{[m]}=\tau)
=\frac{1}{B_n}\sum_{j=0}^{n-m}\binom{n-m}{j}b^j B_{n-m-j}.
\]
For \(r\) specified induced partitions the probabilities multiply. This classical-type restricted-partition identity is included as the finite normalization and is **not claimed as the principal novelty**.

## Proof
**1. Bell identification probabilities.** If a fixed family of equality demands identifies \(v\) named worlds into \(h\) connected groups, the probability that all demands hold in one uniform random partition is exactly \(B_{n-v+h}/B_n\). In particular, a named pair lies in one class with probability \(\rho_n\), and a named triple does so with probability \(\sigma_n=B_{n-2}/B_n\). Standard Bell asymptotics imply, for each fixed \(d\ge0\),
\[
B_{n-d}/B_n=\rho_n^d(1+o(1)),\qquad \rho_n\sim W(n)/n.
\]
At the displayed scaling, \(m\rho_n\to0\), \(m^3\rho_n^2\to c^3\), and \(m^4\rho_n^3\to0\).

**2. Exhaustion of three-world motifs.** A connected three-point common-knowledge substructure contains a two-step path. If both steps have the same agent color, transitivity identifies all three in that agent's class. If the colors differ, the path is a mixed wedge. The expected number of named monochromatic triples of color \(a\) is exactly \(\binom m3\sigma_n\to c^3/6\). The expected number of named mixed paths with distinct fixed colors \(a,b\) and the central vertex specified is exactly \((m)_3\rho_n^2\to c^3\). The requirement that these be *isolated components* changes these counts by \(o_{\Pr}(1)\): every extra incident relation demands one more fixed identification, and the expected number of extensions of the finitely many candidate three-point patterns is \(O_r(m^4\rho_n^3+m^3\rho_n^3)=o(1)\). A connected set of at least four worlds contains a tree on four vertices; for every finite coloring of its three links the joint equality probability is \(O_r(\rho_n^3)\) (redundancy from same-color triangles only decreases this count to a three-world component). Summing over vertex quadruples gives \(O_r(m^4\rho_n^3)=o(1)\). Thus components larger than three vanish.

**3. Joint Poisson limit.** Consider joint falling factorial moments of the counts of the finitely many three-vertex motif types. For disjoint supports, exact Bell identification probabilities and independence across agent colors show that each fixed choice of such supports has probability \((1+o(1))\rho_n^{2s}\), where \(s\) is the total number of prescribed three-world motifs. The resulting combinatorial counts tend to the factorial moments of independent Poisson laws with means \(c^3/6\) and \(c^3\). Intersecting supports contribute \(o(1)\): a connected union of distinct three-point patterns spans \(v\ge4\) vertices and requires at least \(v-1\) independent identifications, giving total order \(O(m^v\rho_n^{v-1})=O(\rho_n^{(v-3)/3})=o(1)\), or lies on the same three vertices with an extra agent constraint, giving \(O(m^3\rho_n^3)=o(1)\). For fixed moment order there are finitely many overlap shapes. Joint factorial moments therefore converge, proving independent Poisson limits by the multivariate method of moments.

**4. Smaller components and first-order logic.** Every two-world equivalence coincidence has probability \(\rho_n\), so for each agent the pair-coincidence count has mean \(\binom m2\rho_n\to\infty\). Its variance is
\[
\binom m2(\rho_n-\rho_n^2)
+\binom m2\bigl(\binom m2-1\bigr)(\sigma_n-\rho_n^2),
\]
which is little-oh of the square of its mean, because \(\sigma_n/\rho_n^2\to1\). Only \(O_{\Pr}(1)\) such pairs lie in three-world components and none lie in larger components with high probability; hence isolated agent-colored pairs diverge in number. The number of nonsingleton vertices is \(O_{\Pr}(m^2\rho_n)=o_{\Pr}(m)\), so isolated worlds also diverge. For a sentence of fixed quantifier rank, all sufficiently large finite disjoint unions having the same numbers of finite three-world components, and at least that rank many components of each abundant one- and two-world type, are Ehrenfeucht–Fraïssé equivalent. Tightness of the Poisson motif counts then yields the asserted mixture limit for every first-order sentence.

**5. Sharpness.** If \(m^3\rho_n^2\to0\), the expectation of all monochromatic triple and mixed wedge witnesses tends to zero; Markov's inequality gives no component of size three or larger. For the opposite regime with \(m\rho_n\to0\), the monochromatic triple count in one agent has mean asymptotic to \(m^3\rho_n^2/6\to\infty\). The pair-intersection contributions to its variance are negligible relative to its squared mean: for two distinct triples sharing one or two vertices they cost respectively \(O(m^5\rho_n^4)\) and \(O(m^4\rho_n^3)\), and disjoint triples have asymptotically factorized probabilities. Since \(m^3\rho_n^2\to\infty\), \(m\rho_n\to0\), and \(m\to\infty\), the relative variance tends to zero. A triple exists with probability tending to one.

**6. Exact finite counting.** To realize a fixed restricted partition \(\tau\) with \(b\) distinguished blocks, select \(j\) of the \(n-m\) omitted worlds that join one of those \(b\) blocks (\(\binom{n-m}j b^j\) choices); partition the remaining omitted worlds independently (\(B_{n-m-j}\) choices). Summation yields the finite formula.

## Verification
The accompanying executable `verify.py` constructs all set partitions through eight worlds and directly checks, for every restriction size and every possible target partition, the exact finite restriction formula and pair factorial moments. It also checks all exact finite \(k\)-class first moments through eight worlds and enumerates every ordered pair of partitions through six worlds for the independent-agent mixed-wedge and triple moment identities. All integer equalities passed. Those finite checks do not establish the infinite Poisson or logical limit law, which follow from the proof above.

## Relationship to prior work
Lerouvillois and Poggiolesi (arXiv:2609.37440; public 2026-09-29) develop dynamic proof theory for S5 epistemic updates, not a stochastic model of the surviving common-knowledge component geometry; the publicly accessible abstract, but not full text, was inspected. Koponen (arXiv:2610.16163; public 2026-10-12), specifically Example 2.12 and Remark 2.15 of the inspected full HTML paper, discusses random expansions and logical convergence but does not provide this S5 restriction/mixed-wedge theorem. DLMF 26.7 and older random-set-partition literature provide the Bell-number asymptotics and partition tools underlying the proof. Classical birthday/occupancy results may imply portions of the individual-agent Poisson behavior; the result assessed here is the **joint two-agent-type three-world geometry, the exact mixed-wedge intensity, and the resulting full first-order limit law** under multi-agent S5 announcements. No claim of mathematical priority is made for the elementary Bell identities.

## Limitations
The distribution assumes independent uniform labelled set partitions and size-conditioned independent announcements, not adversarial announcements, correlated agents, or arbitrary epistemic update products. The claims concern finite-\(n\) exact counting and the stated \(n\to\infty\) scales, not an explicit total-variation error bound. Priority risk remains from the extensive classical literature on occupancy and sparse colored component limits; the 2026 motivating DEL paper's full text and some older primary full texts were inaccessible during comparison. This is self-review only, not independent certification.

## References
1. Clara Lerouvillois and Francesca Poggiolesi, *Dynamic Proof Theory for Dynamic Epistemic Logic* (2026), arXiv:2609.37440, https://arxiv.org/abs/2609.37440 .
2. Vera Koponen, *A characterization of the finite model property for ω-categorical theories* (2026), arXiv:2610.16163, https://arxiv.org/html/2610.16163v1 .
3. NIST Digital Library of Mathematical Functions, §26.7 *Set Partitions: Bell Numbers*, https://dlmf.nist.gov/26.7 .
4. John Haigh, *Random equivalence relations*, J. Combinatorial Theory A 13 (1972), 287–295, doi:10.1016/0097-3165(72)90032-5 .
5. William M. Y. Goh and Eric Schmutz, *Random Set Partitions*, SIAM J. Discrete Math., doi:10.1137/S0895480190186974 .
6. Richard Arratia, Skip Garibaldi, James Kilian, *Asymptotic distribution for the birthday problem with multiple coincidences*, Random Structures & Algorithms (2016), doi:10.1002/rsa.20591 .
