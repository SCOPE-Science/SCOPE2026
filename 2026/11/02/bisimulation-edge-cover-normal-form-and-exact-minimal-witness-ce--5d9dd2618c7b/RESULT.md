# Bisimulation edge-cover normal form and exact minimal-witness census for finite \(\mathsf{S5}\) models

## Finding

**Theorem (two-stage edge-cover decomposition).** For any two nonempty finite labelled, one-agent \(\mathsf{S5}\) Kripke models over a fixed finite propositional vocabulary, every nonempty bisimulation is uniquely a choice of compatible pairs of equivalence classes, followed by a collection of nonempty, type-preserving bipartite edge covers inside each chosen pair. Consequently the exact numbers of all nonempty, inclusion-minimal nonempty, global, and inclusion-minimal global bisimulations are the four expressions below. They apply to arbitrary class partitions, atomic valuations, and model sizes; no connectedness, uniform-class-size, or equal-size assumption is imposed.

Let \(C_1,\ldots,C_r\) and \(D_1,\ldots,D_s\) be the equivalence classes of the two accessibility relations. A class has **support** equal to the set of complete propositional truth profiles present in it. Define the bipartite **compatibility graph** \(K\) with an edge \(ij\) precisely when \(C_i\) and \(D_j\) have the same support. For a compatible pair, let \(a_{it}\) and \(b_{jt}\) be the respective positive multiplicities of profile \(t\). Put

\[
U(a,b)=\sum_{p=0}^{a}\sum_{q=0}^{b}(-1)^{p+q}\binom ap\binom bq 2^{(a-p)(b-q)}.
\]

This is the number of spanning edge sets of the complete bipartite graph \(K_{a,b}\), with no isolated vertex. Let \(H(a,b)\) count the inclusion-minimal such edge sets. It is specified by the labelled bivariate exponential generating function

\[
\sum_{a,b\ge0}H(a,b)\frac{x^a y^b}{a!b!}
=\exp\!\left(xy+x(e^y-1-y)+y(e^x-1-x)\right),
\]

with \(H(0,0)=1\) and \(H(a,0)=H(0,b)=0\) for positive arguments. Define edge weights

\[
\beta_{ij}=\prod_{t\in\operatorname{supp}(C_i)}U(a_{it},b_{jt}),\qquad
\eta_{ij}=\prod_{t\in\operatorname{supp}(C_i)}H(a_{it},b_{jt})
\]

for each edge \(ij\) of \(K\). Then, using \(\mathcal E(K)\) for the edge set and \(\operatorname{EC}(K)\) for its family of spanning edge covers,

\[
\begin{aligned}
\#\{\text{nonempty bisimulations}\}
  &=\prod_{ij\in\mathcal E(K)}(1+\beta_{ij})-1,\\
\#\{\text{inclusion-minimal nonempty bisimulations}\}
  &=\sum_{ij\in\mathcal E(K)}\eta_{ij},\\
\#\{\text{global bisimulations}\}
  &=\sum_{F\in\operatorname{EC}(K)}\prod_{ij\in F}\beta_{ij},\\
\#\{\text{inclusion-minimal global bisimulations}\}
  &=\sum_{\substack{F\in\operatorname{EC}(K)\\F\text{ inclusion-minimal}}}
       \prod_{ij\in F}\eta_{ij}.
\end{aligned}
\]

An empty sum is zero. In particular, global bisimulations exist exactly when the compatibility graph has no isolated vertices. A global bisimulation is one whose projections cover **both entire world sets**; inclusion-minimality is among relations satisfying the designated property, not merely minimal cardinality. Each inclusion-minimal compatibility-graph edge cover is a star forest (disjoint union of stars), and each internal minimal typed cover is independently a union of stars.

## Assumptions and scope

Let \(P\) be a finite set of propositional letters, possibly empty. A finite one-agent Kripke model is \(M=(X,E,V)\), where \(X\neq\varnothing\), \(E\subseteq X^2\) is an equivalence relation and \(V\) assigns each letter a subset of \(X\). Let \(N=(Y,F,W)\) be another such model, on a disjoint, separately labelled nonempty world set \(Y\). The complete atomic profile of a world is the subset of \(P\) true there. Each relation \(Z\subseteq X\times Y\) is counted once as a set of ordered pairs, not up to world relabelling.

A **bisimulation** means a nonempty relation \(Z\) satisfying atomic agreement and both standard forth/back conditions: for every \((x,y)\in Z\), every \(x'\in[x]_E\) has some \(y'\in[y]_F\) with \((x',y')\in Z\), and every \(y'\in[y]_F\) has some \(x'\in[x]_E\) with \((x',y')\in Z\). The word *global* means that the two projections of \(Z\) equal \(X\) and \(Y\). The formulas also apply to the case of zero propositional letters (one atomic type).

The theorem is deliberately one-agent: adding several independent knowledge equivalences changes the forth/back coupling and is not covered. It concerns ordinary bisimulation relations, not bounded-depth bisimulation sequences, functional bounded morphisms, or model isomorphisms.

## Proof

**1. Pairwise class reduction.** Suppose \((x,y)\in Z\), with \(x\in C_i\) and \(y\in D_j\). Because \(E\) and \(F\) are equivalence relations, the successors of \(x\) and \(y\) are exactly \(C_i\) and \(D_j\). Forth implies every world of \(C_i\) has an incident pair belonging to \(C_i\times D_j\); back implies the same for every world of \(D_j\). By atomic agreement, these pairs connect only worlds of the same complete profile, so the supports of \(C_i\) and \(D_j\) agree. Moreover for each profile \(t\), the restriction of \(Z\) to \(C_{i,t}\times D_{j,t}\) is a bipartite edge cover. Thus an active class pair necessarily is a compatibility edge, and its profile blocks are independently spanning nonempty edge sets.

Conversely, choose any collection of compatibility edges, and on each chosen edge independently choose an edge cover in each corresponding profile block. The union obeys atomic agreement. A pair lies in a selected class pair, whose cover contains a witness for every successor on either side, so forth and back hold. Distinct choices produce distinct relations, proving the bijection. Notice that an endpoint may be incident to several different active class pairs; each must separately obey the edge-cover constraint. This prevents an erroneous reduction to a *single* cover across all pairs.

**2. All nonempty relations.** In the independent choices above, an inactive compatibility edge contributes one possibility and an active edge contributes \(\beta_{ij}\) possibilities. Their product counts all choices, including the empty relation. Subtract the one empty choice. A nonempty bisimulation is inclusion-minimal precisely if it activates a single compatibility edge and every profile block is an inclusion-minimal edge cover: with two active class pairs one can delete a whole class-pair block, while a nonminimal cover has a removable relation pair. This proves the first two formulas, conditional only on the independent edge-cover decomposition.

**3. Bipartite counts and minimality.** For positive \(a,b\), inclusion-exclusion over the \(a+b\) vertices that might be isolated gives \(U(a,b)\) as stated. An edge set \(A\) without isolated vertices is inclusion-minimal if and only if every chosen edge has at least one endpoint of degree one: otherwise an edge whose two ends both have degree at least two could be removed, and conversely removal of an edge with a degree-one endpoint creates an isolated vertex.

This criterion forces each connected component of an inclusion-minimal edge cover to be a star. If a connected component contained two different vertices of degree at least two, the path between them would have an edge both of whose ends have degree at least two. Hence the possibilities are a single edge, a star with one left center and at least two right leaves, or a star with one right center and at least two left leaves. The exponential formula for labelled disjoint unions of these three component types yields the displayed bivariate generating function for \(H\). An alternative computation is \(H(0,0)=1\) and, for positive arguments,

\[
H(a,b)=\sum_{t=1}^{b}\binom bt H(a-1,b-t)
 +b\sum_{s=2}^{a}\binom{a-1}{s-1}H(a-s,b-1).
\]

Here the distinguished left vertex is either the center of a star with \(t\) right leaves (including a single edge), or a leaf of a right-centered star with \(s\ge2\) left leaves. The two cases are disjoint and exhaustive. This recursion independently establishes the coefficients of the generating function.

**4. Globality and its minimality.** A nonempty bisimulation is global if and only if its active compatibility edges cover every class vertex. Indeed, an active pair covers all constituent worlds on both sides, while an inactive class vertex is absent from the corresponding projection. Therefore active edges must form an edge cover \(F\) of \(K\), and the independent internal choices give weight \(\prod_{ij\in F}\beta_{ij}\), proving the third formula.

If a global relation is inclusion-minimal, its active compatibility edge cover must be inclusion-minimal: otherwise deleting an entire redundant class-pair block preserves globality and bisimulation. Each profile block in each active class pair must also be inclusion-minimal, since otherwise an individual world-pair can be deleted while still preserving the bisimulation and global projections. Conversely, for a minimally covered compatibility graph and internally minimal profile blocks, deleting any individual pair either breaks a profile-block cover while that class pair remains active, or removes its entire class-pair block; in the latter case minimality of \(F\) destroys globality. Thus the union is inclusion-minimal global. This yields the fourth formula and the two-stage star-forest description.

**5. Boundaries and witnesses.** If the compatibility graph has no edges, the product expression is \(1-1=0\), and every other count is zero. If \(K\) has isolated vertices it has no global edge cover, although nonempty partial bisimulations can still exist. For two worlds on each side, if each equivalence relation consists of two singleton classes and every world has the same profile, \(K=K_{2,2}\), every edge has unit weight, and the four counts in theorem order are \(15,4,7,2\). If instead the two worlds on each side form a single equivalence class, the four counts are \(7,2,7,2\). These examples show that counting minimal and global witnesses is not determined merely by world cardinalities or propositional colors: the accessibility partitions matter.

## Verification

Run `python checker.py` with Python 3 and the standard library. The checker constructs all set partitions and binary valuations for each side with one to three labelled worlds, and directly enumerates all nonempty binary relations between every resulting ordered pair of models. It tests atomic harmony and the quantified forth/back clauses without using the theorem's normal form. Minimality is detected by independent subset inclusion and globality by both projections. All four exact formula counts are then compared. The checker also tests four larger four-world versus three-world model pairs and separately verifies inclusion-exclusion and the minimal-cover recursion for five bipartite sizes.

Output of the completed checker: `ALL_CHECKS_OK model_pairs=2504 profile_cases=5`. The comparisons cover 2,500 complete small-model pairs and four additional larger pairs. This is a finite reproducibility check; the argument in the proof establishes the universal claim for all finite cardinalities.

Useful component coefficients are \(U(1,1)=1\), \(U(2,2)=7\), \(U(2,3)=25\), \(U(3,3)=265\), \(U(4,4)=41503\), while the corresponding minimal-cover counts are \(1,2,6,15,184\).

## Relationship to prior work

Burrieza, Soler-Toscano and Yuste-Ginel formulate the exact atomic/forth/back conditions for bisimulation between arbitrary Kripke models, study modal expressibility and logical complexity, and identify surjective p-morphisms as a related extension. Their results supply definitions and motivation but do not state the present all-size, weighted enumeration of witness relations, or the two-level minimality decomposition.

Van Ditmarsch, Fernández-Duque and van der Hoek explicitly define *total* (global) bisimulation and establish its modal definability for finite epistemic models. Their work is about definability, not the number of such relations. Ordinary bipartite edge covers, their inclusion-exclusion counts, and the star-forest criterion for minimal covers are standard combinatorial components; the claim of interest is their exact nested appearance and weighted assembly for **arbitrary pairs of finite one-agent epistemic models**. Related work on bounded-morphism covers and finite S5 model quotients addresses different functions or model invariants, not these four counts for binary bisimulation witnesses.

## Limitations

The formulas count relations between two **fixed labelled models**, not the total number of models, equivalence classes of models, or bisimulation relations modulo automorphisms. They apply to one-agent equivalence-accessibility structures and complete valuations over the selected finite vocabulary. They do not extend without modification to multiagent S5, partial bisimulation conditions, or generic Kripke frames. The bivariate star-forest generating function is an elementary known edge-cover identity rather than a novel combinatorial primitive; possible older equivalent classifications of minimal bisimulations under another name remain a historical-priority risk. The proof is mathematical, and the small-instance checker does not independently certify infinite generality. No independent scientific audit has been performed.

## References

1. Alfredo Burrieza, Fernando Soler-Toscano, and Antonio Yuste-Ginel. *A meta-modal logic for bisimulations*. arXiv:2507.15117, first version published 20 July 2025; version 4 published 26 October 2026. https://arxiv.org/abs/2507.15117 ; complete version examined at https://arxiv.org/html/2507.15117v4 .
2. Hans van Ditmarsch, David Fernández-Duque, and Wiebe van der Hoek. *On the definability of simulation and bisimulation in epistemic logic*. *Journal of Logic and Computation* 24 (2014), 1209–1227. Author-posted full text: https://cgi.csc.liv.ac.uk/~wiebe/pubs/Documents/logcom.exs058.full.pdf .
3. Standard bipartite edge-cover combinatorics; see Eric W. Weisstein, *Edge Cover*, MathWorld, https://mathworld.wolfram.com/EdgeCover.html .
