# Exact common-knowledge depth distribution for binary S5 information cells

## Finding
Let \(W\) be a finite nonempty labelled set of size \(n\), and let \(R,S\) be two equivalence relations on \(W\), with every equivalence class having at most two points. Write \(K_R\) and \(K_S\) for the usual S5 knowledge operators, and \(E(X)=K_R(X)\cap K_S(X)\) for everybody-knows on an event \(X\subseteq W\). Let \(C(X)\) be common knowledge: all worlds reachable by a finite sequence of \(R\)- or \(S\)-steps belong to \(X\). Define \(d(R,S)\) to be the least nonnegative integer \(d\) such that \(E^d(X)=C(X)\) for **every** event \(X\subseteq W\). Here \(E^0(X)=X\).

**Theorem.** For every such pair \((R,S)\), \(d(R,S)\) equals the largest finite graph distance between two worlds in the same component of the undirected union graph \(G(R,S)\) (the maximum of component diameters). Every component is an isolated point, an edge, an alternating two-coloured path, or an even alternating cycle. In the two-vertex case the edge may belong to both agents; this is counted separately from the two singly coloured edges.

For each integer \(d\ge0\), let \(A_{n,d}\) be the number of **ordered** pairs \((R,S)\) on the labelled set \(W\) such that \(d(R,S)\le d\). Then the exact exponential generating function is
\[
\boxed{\sum_{n\ge0} A_{n,d}\frac{z^n}{n!}=
\exp\!\left(\sum_{j=1}^{d+1}z^j+\sum_{j=1}^{d}\frac{z^{2j}}{2j}\right).}
\]
The \(n=0\) coefficient is only the formal empty combinatorial structure. In particular the unrestricted generating function equals
\[
\sum_{n\ge0} I_n^2\frac{z^n}{n!}=
\frac{\exp(z/(1-z))}{\sqrt{1-z^2}},
\]
where \(I_n\) is the number of involutions on \(n\) letters. For every \(n\ge3\), the maximum possible convergence depth is \(n-1\), attained by **exactly \(n!\)** ordered pairs \((R,S)\); their union graphs are spanning alternating paths. For \(n=1\), the only depth is zero; for \(n=2\), exactly three of the four ordered pairs have depth one.

## Assumptions and scope
All equivalence classes are nonempty and have cardinality one or two. Agents are distinguished, so exchanging \(R\) and \(S\) may change the counted frame. Worlds carry distinct labels, and distinct ordered pairs of relations are counted separately. The two agents' valuations are arbitrary Boolean truth assignments; no restriction on the number of propositional variables is needed because one variable already realizes every event. Every statement concerns classical two-agent S5 frames, equivalently the equality-order subcase of intuitionistic S5 semantics. There is no claim about arbitrary intuitionistic orders or equivalence classes of size three or more.

For a subset \(X\subseteq W\), \(K_R(X)=\{w:[w]_R\subseteq X\}\). Put \(T=R\cup S\) and let \(T^*\) denote reflexive transitive closure. Then \(C(X)=\{w:T^*(w)\subseteq X\}\). The convergence depth is uniform over all \(X\), not the depth for one fixed valuation.

## Proof
**1. Epistemic depth equals component diameter.** Every equivalence class of \(R\) or \(S\) is a singleton or a pair. Accordingly, let \(r,s:W\to W\) be the uniquely determined involutions that swap members of each two-element class and fix singleton classes. The operator \(E\) satisfies
\[
 w\in E(X)\quad\Longleftrightarrow\quad\{w,r(w),s(w)\}\subseteq X.
\]
The union graph has undirected edges \(\{w,r(w)\}\) and \(\{w,s(w)\}\) whenever the two endpoints differ. Write \(B_k(w)\) for the set of worlds at graph distance at most \(k\) from \(w\). Induction on \(k\) gives
\[
 w\in E^k(X)\quad\Longleftrightarrow\quad B_k(w)\subseteq X.
\]
The base case uses \(B_0(w)=\{w\}\); for the successor step, the union of radius-\(k\) balls around \(w,r(w),s(w)\) is exactly \(B_{k+1}(w)\). If \(D\) is the maximum component diameter, then \(B_D(w)\) is the entire connected component of \(w\), so \(E^D(X)=C(X)\) for all \(X\). Conversely, if \(D>0\), choose \(w,u\) in the same component at distance \(D\), and let \(X=W\setminus\{u\}\). Then \(w\in E^{D-1}(X)\) but \(w\notin C(X)\). Thus \(d(R,S)=D\), including \(D=0\).

**2. Component classification.** Regard the transpositions of \(r\) as red edges and of \(s\) as blue edges. Each vertex has at most one incident edge of either colour. An edge appearing in both colours exhausts both incident vertices' matching capacities and therefore forms a component of exactly two vertices. Delete such double edges temporarily. In the remaining graph all degrees are at most two, so each finite connected component is a path or a cycle. At a degree-two vertex the incident edges must have different colours, forcing alternation. All cycles consequently have even length, at least four. The isolated vertices and the double-edge components complete the classification.

**3. Connected counts.** For \(j\ge2\), an unoriented labelled path on \(j\) vertices has \(j!/2\) orderings; exactly two alternating red-blue colourings are possible. Hence there are \(j!\) connected path objects; this also holds for \(j=1\), where there is one isolated vertex. A length-\(j\) path has diameter \(j-1\). On two labelled vertices, besides the two singly coloured paths, there is exactly one double-edge object of diameter one. For each \(j\ge2\), there are \((2j-1)!/2\) undirected labelled cycles on \(2j\) vertices; each has two alternating colourings, giving \((2j-1)!\) coloured cycles of diameter \(j\). The double-edge object extends the same cyclic count to \(j=1\), since \((2j-1)!=1\) there. Therefore the labelled connected exponential generating function, restricted to diameter at most \(d\), is
\[
 P_d(z)=\sum_{j=1}^{d+1} \frac{j!}{j!}z^j+
 \sum_{j=1}^{d}\frac{(2j-1)!}{(2j)!}z^{2j}
 =\sum_{j=1}^{d+1}z^j+\sum_{j=1}^{d}\frac{z^{2j}}{2j}.
\]
Every pair \((R,S)\) decomposes uniquely into an **unordered set of disjoint labelled connected components**, so the labelled exponential formula gives \(\exp(P_d(z))\). Passing to the limit of coefficientwise formal series as \(d\to\infty\) yields \(\exp(z/(1-z))(1-z^2)^{-1/2}\). Independently, each equivalence relation of cell size at most two is uniquely an involution, so its unrestricted pair count is \(I_n^2\), giving the displayed identity.

**4. Extremal count.** Each component of size \(j\) has diameter at most \(j-1\), with equality only for a path when \(j\ge3\). Thus for \(n\ge3\), diameter \(n-1\) requires a single component on all \(n\) vertices, and it must be an alternating path. There are \(n!\) such labelled pairs. The cases \(n=1,2\) follow directly from the three two-world nontrivial pairs.

## Verification
The accompanying standalone `check.py` enumerates every involution pair through seven labelled worlds, constructs its union graph, computes component diameters by breadth-first search, and compares the cumulative number of pairs at each depth with exact coefficients of \(\exp(P_d(z))\) computed over rational numbers. It also exhaustively checks the Boolean event semantics and depth equality through four worlds. It produces these counts by exact depth:

| \(n\) | total ordered pairs | exact-depth counts \(d=0,1,\ldots,n-1\) |
|---:|---:|---|
| 1 | 1 | 1 |
| 2 | 4 | 1, 3 |
| 3 | 16 | 1, 9, 6 |
| 4 | 100 | 1, 45, 30, 24 |
| 5 | 676 | 1, 165, 270, 120, 120 |
| 6 | 5,776 | 1, 855, 1,920, 1,560, 720, 720 |
| 7 | 53,824 | 1, 3,843, 15,540, 14,280, 10,080, 5,040, 5,040 |

Run `python3 check.py` with Python 3.8 or later. No third-party modules are required. The computations are finite consistency checks; the proof above establishes the theorem for all positive integers \(n\).

## Relationship to prior work
Zenger's 2026 *Intuitionistic Common Knowledge* defines common knowledge over the reflexive-transitive closure of the union of epistemic relations and explicitly relates classical S5 common knowledge to an intuitionistic extension (Definition 4.2 and Theorem 4.12). Its paper concerns axiomatization, translation and proof complexity, not the labelled depth distribution under size-two information cells. Classical work of Halpern and Moses introduced common knowledge in distributed settings. The alternating-path-and-even-cycle decomposition is standard for unions of two matchings, and the exponential formula for labelled components is also standard; neither constituent tool is asserted to be new. The contribution claimed here is the **exact depth-refined labelled census**, including its uniform formula and extremal multiplicity in the restricted epistemic frame class. A prior enumeration in a different combinatorial vocabulary could imply this formula; no global novelty certification is asserted.

## Limitations
The counts are for **ordered** relations on **labelled** worlds, not frames up to isomorphism. The formula does not quantify over intuitionistic valuations constrained by a nontrivial information-growth order, and it does not address three or more epistemic agents or larger equivalence classes. Independently proving the graph and exponential-formula steps is necessary for the infinite statement: the executable checks by themselves certify only the stated small values. Related permutation-pair enumerations might entail the same exact coefficients; this is a residual literature risk.

## References
1. Lukas Zenger, *Intuitionistic Common Knowledge*, arXiv:2605.00523v1, first publicly submitted 2026-05-01, especially Sections 2 and 4. [Primary preprint](https://arxiv.org/html/2605.00523).
2. Joseph Y. Halpern and Yoram Moses, *Knowledge and Common Knowledge in a Distributed Environment*, Journal of the ACM 37 (1990), 549–587. DOI: 10.1145/79147.79161.
3. Standard alternating matching decomposition: see the matching discussion in *The Best of Both Worlds: Asymptotically Efficient Mechanisms with a Guarantee on the Expected Gains-From-Trade*, Observation E.8 (preprint available online).
4. Standard labelled-set exponential formula: lecture notes *Species and exponential generating functions*, Section 4, Queen Mary University of London.
