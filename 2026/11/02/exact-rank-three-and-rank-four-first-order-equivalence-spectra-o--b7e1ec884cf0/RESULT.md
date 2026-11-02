# Exact rank-three and rank-four first-order equivalence spectra of squared paths

## Finding

Let \(P_n\) denote the undirected path with vertex set \(\{1,\ldots,n\}\), for each integer \(n\ge 1\). Its square \(G_n=P_n^2\) has adjacency \(E(i,j)\) precisely when \(1\le |i-j|\le 2\). Treat \(G_n\) as a structure in the first-order language containing only equality and the symmetric binary adjacency predicate \(E\), without endpoints, orientation, an order predicate, or named constants. Write \(G_n\equiv_q G_m\) when the graphs satisfy exactly the same first-order sentences of quantifier rank at most \(q\).

**Theorem.** For all integers \(n,m\ge1\),

\[
G_n\equiv_3G_m\quad\Longleftrightarrow\quad \min\{n,11\}=\min\{m,11\},
\]
\[
G_n\equiv_4G_m\quad\Longleftrightarrow\quad \min\{n,26\}=\min\{m,26\}.
\]

Thus ranks three and four have precisely eleven and twenty-six equivalence classes, respectively: all smaller orders occur singly, and each remaining class is an infinite tail. The sharp stabilization sizes are eleven at rank three and twenty-six at rank four. Graph squaring leaves these precise low-rank logical spectra different from those of ordinary paths; the endpoints of squared paths remain distinguishable at rank four substantially further than a naive locality argument proves.

## Assumptions and scope

Graphs are finite, loopless, undirected, simple graphs. The square operation adds edges between vertices at distance exactly two in the underlying path; in particular \(P_1^2\) is an isolated vertex and \(P_2^2\) is a single edge. Quantifier rank counts nested quantifiers, not the total number of quantifiers. Repeated selections of a previously selected vertex are permitted in Ehrenfeucht--Fraisse games. The result concerns only sentences, not formulas with named vertices.

## Proof

### 1. Exact finite back-and-forth types

For a graph \(G\) and an ordered tuple \(\bar v=(v_1,\ldots,v_k)\), define its atomic signature \(A_G(\bar v)\) to be the string of statuses of all pairs \((v_i,v_j)\), \(i<j\): equal, distinct-and-adjacent, or distinct-and-nonadjacent. Define types recursively:

\[
T_0(G,\bar v)=A_G(\bar v),
\qquad
T_{r+1}(G,\bar v)=\left(A_G(\bar v),
\left\{T_r(G,(\bar v,w)):w\in V(G)\right\}\right).
\]

The braces denote a **set**, not a multiset. By induction on \(r\), two pointed graphs have identical \(T_r\) precisely when Duplicator wins the \(r\)-round Ehrenfeucht--Fraisse game starting from the corresponding previously selected vertices. Indeed the atomic signatures give the partial-isomorphism condition, and equality of extension-type sets permits a response to every Spoiler move on **either** graph. The induction includes repeated vertices and all alternations of existential and universal moves. Therefore \(T_q(G,())\) is a complete rank-\(q\) first-order sentence invariant.

The standalone C++17 source `verify_types.cpp` interns these types exactly as finite integer vectors. It enumerates every \(k\)-tuple, including repetitions, and every one-point extension; no sampling or numeric tolerance is used. Its tables for the **entire** range \(1\le n\le47\) yield

\[
T_3(G_n,())=T_3(G_m,())\iff \min(n,11)=\min(m,11),
\]
\[
T_4(G_n,())=T_4(G_m,())\iff \min(n,26)=\min(m,26)
\]

for all \(n,m\) in that finite range. Type IDs are arbitrary exact interned identifiers; their equality, not their numerical magnitude, expresses logical equivalence. The source also asserts the displayed classification on each pass, and `finite_types.txt` records all results. A separately written Python implementation, `independent_types.py`, uses immutable atomic tuples and sets rather than encoded integer signatures; it independently confirms all ranks for \(1\le n\le12\), and the decisive strict boundary at sizes \(25,26,27\).

### 2. A uniform infinite-family Duplicator strategy

We prove that all sufficiently large squared paths are rank-\(q\) equivalent. At any stage, arrange the distinct selected vertices in their underlying path order. Add artificial sentinels \(0\) and \(n+1\), which are **not** vertices in the graph language. Duplicator maintains an order-preserving correspondence between selected vertices on two paths such that every gap between consecutive selected vertices or sentinels satisfies one of these two alternatives: its two lengths are exactly equal and smaller than \(B_r\), or both lengths are at least \(B_r\). Here \(r\) rounds remain and \(B_r=3\cdot2^r\).

Initially, when \(n,m\ge B_q-1\), the unique sentinel-to-sentinel gaps have lengths \(n+1,m+1\ge B_q\). Suppose the invariant holds with \(r+1\) rounds left. Repeatedly selecting a marked point is answered by repeating its correspondent. A fresh choice splits one gap into two positive integer lengths. If the old gap lengths are equal and smaller than \(B_{r+1}\), choose the corresponding offset on the other side; both new gap lengths are equal. Otherwise both old gaps are at least \(B_{r+1}=2B_r\). If one new subgap is smaller than \(B_r\), copy its exact length; the complementary gap on the other side remains at least \(B_r\). If neither new subgap is smaller than \(B_r\), split the other old gap with a subgap of length \(B_r\), leaving its complement at least \(B_r\). Both new gaps then satisfy the invariant for \(r\) remaining rounds. Thus the strategy works regardless of which graph Spoiler plays in.

At the end, \(B_0=3\). Every distance between two selected vertices is a sum of consecutive positive gaps. Such a distance is one or two precisely when all contributing gaps are exact small gaps with total one or two; the same condition holds on the other side. Equality is also preserved. Hence adjacency and nonadjacency are respected, and Duplicator wins. This proves

\[
n,m\ge23\Longrightarrow G_n\equiv_3G_m,
\qquad
n,m\ge47\Longrightarrow G_n\equiv_4G_m.
\]

### 3. Sharp thresholds for all sizes

The exact finite types show that \(G_{11},\ldots,G_{47}\) share a single rank-three type, and \(G_{26},\ldots,G_{47}\) share a single rank-four type, with every preceding size having a different type. The infinite strategy identifies every larger graph with \(G_{47}\) at rank four, and every graph of size at least twenty-three with \(G_{23}\) at rank three. Transitivity supplies the two asserted equivalences for **all** positive sizes. Neither the finite classification alone nor the strategy alone would give the sharp result; both are required.

## Verification

The package contains `verify_types.cpp`, `independent_types.py`, `finite_types.txt`, and `independent_check.txt`. To replay from the directory containing the files, run:

```sh
g++ -O3 -std=c++17 verify_types.cpp -o verify_types
./verify_types 47 > replay_finite.txt
python3 independent_types.py > replay_independent.txt
```

The expected terminal lines are `COMPLETE_RANK_THREE_AND_FOUR_FINITE_TYPE_CHECK_PASS through_n=47` and `INDEPENDENT_PYTHON_TYPE_CLASSIFICATION_PASS`. On every size from one to forty-seven, the compiled checker verifies type IDs \(\min(n,11)\) and \(\min(n,26)\). The independent implementation corroborates selected cases, including the decisive rank-four change from size twenty-five to twenty-six and equality at sizes twenty-six and twenty-seven. The infinite part is the preceding proved gap-invariant strategy; these programs do not extrapolate from finite results.

## Relationship to prior work

Brown and Hoshino studied first-order Ehrenfeucht--Fraisse games on **ordinary** undirected paths and cycles, not their graph squares. Ganian and collaborators established general first-order model-checking results for interval graphs; the squared paths are unit-interval graphs, but their qualitative reduction theorem does not provide the sharp equivalence classes computed here. Fagin, Lenchner, Regan, and Vyas treated multi-structural games measuring the **number** of quantifiers, which is distinct from the usual quantifier-rank invariant used here. Allen, Mergoni Cecchelli, Roberts, and Skokan investigated **Ramsey numbers** of squared paths and cycles, providing a natural middle-period source for the graph family rather than a logical classification. No directly covering rank-three/rank-four squared-path theorem was identified in the accessible comparisons; this is a bounded historical-priority assessment, not a proof of novelty.

## Limitations

The theorem makes no claim for quantifier ranks five or higher, for graph powers other than the square, or for formulas in languages with named endpoints, successor, linear order, or counting quantifiers. The comparison to existing literature is not an exhaustive priority certificate. Only the finite type enumeration uses computation; the all-size extension is a separate elementary mathematical proof. This analysis has not been independently audited.

## References

1. J. Brown and R. Hoshino, *The Ehrenfeucht--Fraisse Game for Paths and Cycles*, Ars Combinatoria 83 (2007), 193--212, https://combinatorialpress.com/article/ars/Volume%20083/volume-83-paper-13.pdf.
2. R. Ganian, P. Hlinený, D. Král', J. Obdržálek, J. Schwartz, and J. Teska, *FO Model Checking of Interval Graphs*, Logical Methods in Computer Science 11(4:11) (2015), https://arxiv.org/abs/1302.6043.
3. R. Fagin, J. Lenchner, K. W. Regan, and N. Vyas, *Multi-Structural Games and Number of Quantifiers*, first arXiv version 2021-04-30, https://arxiv.org/abs/2104.14709.
4. P. Allen, D. Mergoni Cecchelli, B. Roberts, and J. Skokan, *The Ramsey Numbers of Squares of Paths and Cycles*, first public arXiv version 2022-12-30, https://arxiv.org/abs/2212.14860.
