# A Lucas–six-period census of all-good EFX orientations on unit cycles

## Finding

**Theorem.** For every integer \(n\ge3\), let \(C_n\) be the labeled simple cycle with vertices \(0,\ldots,n-1\) and edges \(e_i=\{i,i+1\}\), indices modulo \(n\). Interpret each edge as an indivisible good allocated to one of its two endpoints. Each vertex values each of its two incident goods at one and every nonincident good at zero, additively. An orientation \(X\) satisfies **all-good EFX** when
\[
 v_i(X_i)\ge v_i(X_j\setminus\{e\})\qquad
 \text{for every }i,j\text{ and every }e\in X_j.
\]
This tests even goods worth zero to the envier. The exact number \(N_n\) of satisfying labeled orientations is
\[
 \boxed{N_n=L_n+2\cos(n\pi/3)},\qquad
 L_0=2,\ L_1=1,\ L_{n+2}=L_{n+1}+L_n.
\]
More precisely, for even \(k\) with \(0\le k\le\lfloor n/2\rfloor\), exactly
\[
 \boxed{\frac{2n}{n-k}\binom{n-k}{k}}
\]
satisfying orientations have exactly \(k\) changes between successive cyclic edge directions; for odd \(k\) the number is zero. Thus a uniformly random independent orientation is all-good EFX with probability \(N_n/2^n\), and
\[
 \frac{N_n}{2^n}\sim \left(\frac{1+\sqrt5}{4}\right)^n
 \quad(n\to\infty).
\]
There are always at least two satisfying orientations (the uniformly clockwise and uniformly counterclockwise orientations), but a random orientation is exponentially unlikely to be fair.

## Assumptions and scope

The graph is a simple cycle of at least three vertices, with no parallel edges, loops, external goods, or unequal edge weights. All \(n\) edges must be allocated to their endpoints, and orientations of labeled edges are distinct. The all-good EFX quantifier ranges over **every** edge of the other bundle, including edges which the envier values at zero. In contrast, the weaker relevant-good-only version is trivial for these simple unit graphical valuations and is not counted by the theorem.

## Proof

**1. Structural characterization on simple graphs.** In any simple graph with the specified unit graphical valuations, an oriented allocation satisfies all-good EFX if and only if no directed edge goes from a vertex of indegree zero to a vertex of indegree at least two. Indeed, a vertex with at least one incoming edge has own value at least one. Its value for any *other* vertex's bundle is at most one, because there is at most one edge joining them; therefore it cannot violate all-good EFX. A vertex \(i\) with indegree zero values vertex \(j\)'s bundle at one only if the edge \(ij\) is directed from \(i\) into \(j\). If \(j\)'s bundle contains no other edge, deletion of its single edge leaves value zero; otherwise deletion of another, zero-valued edge preserves value one and violates the inequality. This proves the characterization including empty bundles.

**2. Cyclic binary encoding.** Write \(b_i=1\) if edge \(e_i\) points from \(i\) to \(i+1\), and \(b_i=0\) otherwise. Then vertex \(i\) has indegree \(b_{i-1}+1-b_i\). A directed edge from a zero-indegree vertex to a two-indegree neighbor occurs precisely at a cyclic consecutive pattern \(010\) or \(101\) of the word \((b_0,\ldots,b_{n-1})\). Thus the all-good EFX condition is equivalent to the absence of two consecutive cyclic bit changes.

Let \(S=\{i:b_i\ne b_{i+1}\}\), subscripts modulo \(n\). The condition says that \(S\) is an independent vertex set in the ordinary cycle \(C_n\). Since the word returns to its initial bit after one turn, \(|S|\) must be even. Conversely, any even independent set \(S\) uniquely determines a cyclic binary word once \(b_0\) is chosen, giving exactly two distinct orientations for each such \(S\). Hence
\[
 N_n=2\sum_{\substack{S\subseteq V(C_n)\text{ independent}\\ |S|\text{ even}}}1.
\]

**3. Exact enumeration.** Write \(I(C_n,z)=\sum_{S\text{ independent}}z^{|S|}\). The standard two-state transfer matrix \(T(z)=\left(\begin{smallmatrix}1&z\\1&0\end{smallmatrix}\right)\) has trace \(\operatorname{tr}(T(z)^n)=I(C_n,z)\), because its cyclic closed walks encode independent zero-one words with weight \(z\) for each chosen vertex. The two eigenvalues solve \(t^2-t-z=0\), giving
\[
 I(C_n,z)=\left(\frac{1+\sqrt{1+4z}}2\right)^n+
 \left(\frac{1-\sqrt{1+4z}}2\right)^n.
\]
By the even-parity filter, \(N_n=I(C_n,1)+I(C_n,-1)\). At \(z=1\) this is the Lucas term \(L_n\); at \(z=-1\) the eigenvalues are \(e^{\pm i\pi/3}\), so the second term is \(2\cos(n\pi/3)\). This proves the closed formula.

For exactly \(k\ge1\) independent change positions, select a distinguished chosen position and then positive circular gaps, yielding \(\frac{n}{k}\binom{n-k-1}{k-1}=\frac{n}{n-k}\binom{n-k}{k}\) possible sets. The same formula gives one set when \(k=0\). Doubling for the initial bit proves the refinement. Since \(L_n=\varphi^n+(1-\varphi)^n\) for \(\varphi=(1+\sqrt5)/2\), and the cosine correction is bounded, the asymptotic statement follows.

## Verification

The standalone standard-library script `verify.py` enumerates all \(2^n\) labeled orientations for each \(3\le n\le14\). It checks the original all-good EFX inequalities directly, compares them with the forbidden-pattern test, and checks the Lucas formula and each even change-count layer independently. Executed with `python3 verify.py`, it prints `VERIFY_OK n=3..14`. The total EFX counts for \(n=3,\ldots,14\) are \(2,6,12,20,30,46,74,122,200,324,522,842\). Exhaustive finite testing is corroboration only; the proof above establishes every \(n\ge3\).

## Relationship to prior work

Zeng's 2026 work characterizes simple graphs for which an EFX orientation exists under every valuation assignment; Zeng and Mehta's earlier work establishes structural existence guarantees, including those for cycles. These are existential, not enumerative, statements. Kanellopoulos and collaborators study the computational complexity of EF and EFX orientation existence, including binary valuations, rather than this exact labeled-orientation count. Deligkas and collaborators explicitly distinguish the all-good and relevant-good interpretations of EFX. The present theorem counts all-good EFX orientations and refines the count by direction changes. The independent-set transfer-matrix enumeration is classical; the substantive connection is the exact fairness-to-cyclic-independence reduction and its robustness consequences.

## Limitations

The closed form applies only to simple uniform-unit cycles. It does not imply an analogous formula for arbitrary graphical valuations, multigraphs, or other fairness definitions. The weak relevant-good EFX condition is different. The numerical checks only cover sizes at most fourteen. Although targeted comparisons found no published equivalent count, differently phrased or unindexed prior enumerations may exist; independent validation has not been performed.

## References

- J. A. Zeng, *A Polynomial Time Characterization For Strongly EFX Orientable Graphs*, arXiv:2609.36498v1 (public September 29, 2026), https://arxiv.org/abs/2609.36498.
- J. A. Zeng and R. Mehta, *On the Structure of EFX Orientations on Graphs*, arXiv:2404.13527v2, https://arxiv.org/html/2404.13527v2.
- S. Kanellopoulos, E. Nemery, C. Pergaminelis, M. M. Sotiriou, and M. Vasilakis, *EF(X) Orientations: A Parameterized Complexity Perspective*, arXiv:2512.25033v1, https://arxiv.org/html/2512.25033v1.
- A. Deligkas, E. Eiben, T.-L. Goldsmith, and V. Korchemna, *EF1 and EFX Orientations*, arXiv:2409.13616v1, https://arxiv.org/html/2409.13616v1.
