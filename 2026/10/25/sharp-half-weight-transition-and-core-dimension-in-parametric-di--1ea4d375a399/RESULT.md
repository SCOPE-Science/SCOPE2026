# Sharp half-weight transition and core dimension in parametric directed trust games

## Finding

Consider any finite loopless weighted directed graph, with nonnegative arc weights, and the parametric cooperative trust game obtained by assigning weight \(\lambda\) to internal interactions and \(1-\lambda\) to minimum incoming exposure. For every \(0\le\lambda\le1\), its core exhibits an exact three-phase transition. If at least one arc has positive weight, the core is **empty** for \(\lambda<\tfrac12\), is the **single half-indegree allocation** for \(\lambda=\tfrac12\), and has **affine dimension \(n-c\)** for \(\lambda>\tfrac12\), where \(c\) is the number of weakly connected components of the positive-weight support graph. Moreover, the game is totally balanced if and only if \(\lambda\ge\tfrac12\). When every arc has zero weight, the core is the singleton zero allocation for all parameters.

More precisely, for \(\lambda>\tfrac12\) a canonical core allocation has exactly those coalitions that are unions of positive-support components tight. This determines the complete affine dimension of the core for arbitrary graph topology and arbitrary admissible arc weights, including zeros and disconnected graphs.

## Assumptions and scope

Let \(N=\{1,\ldots,n\}\), \(n\ge1\). Let \(E\subseteq N\times N\) be a simple directed edge set with no loops and nonnegative weights \(a_{ij}\in[0,1]\). Missing edges have weight zero. For \(U\subseteq N\), define the minimum incoming weight at vertex \(j\) from \(U\) by

\[
m_j(U)=\begin{cases}\min\{a_{ij}:i\in U,\ (i,j)\in E\},&\text{if the set is nonempty},\\0,&\text{otherwise}.\end{cases}
\]

Thus an empty incoming set contributes zero, not infinity. For each \(0\le\lambda\le1\) and coalition \(S\subseteq N\), define

\[
v_\lambda(S)=\lambda\sum_{i,j\in S}a_{ij}+(1-\lambda)\sum_{j\in S}m_j(N\setminus S).
\]

The first sum counts directed internal edges, and the second counts the minimum outside incoming weight separately for each member. Define \(I_j=\sum_i a_{ij}\), \(O_j=\sum_k a_{jk}\), \(W=\sum_jI_j=\sum_jO_j\). Let \(H\) be the undirected positive-support graph: \(\{i,j\}\) is an edge of \(H\) exactly when \(a_{ij}>0\) or \(a_{ji}>0\). Let \(c\) be its number of connected components, counting isolated vertices.

The transferable-utility core is

\[
\operatorname{Core}(v_\lambda)=\{x\in\mathbb R^n:\sum_{j\in N}x_j=v_\lambda(N),\ \sum_{j\in S}x_j\ge v_\lambda(S)\ \text{for all }S\subseteq N\}.
\]

A game is totally balanced if every restriction to a nonempty player subset has a nonempty core.

## Proof

**Step 1: exact co-singleton obstruction and the empty phase.** Because no loops are present, for each \(j\in N\), the internal sum on \(N\setminus\{j\}\) is \(W-I_j-O_j\); its sole outside vertex \(j\) contributes precisely \(O_j\) to the external sum. Hence

\[
v_\lambda(N\setminus\{j\})=\lambda W-\lambda I_j+(1-2\lambda)O_j.
\]

Any core allocation is efficient and respects the coalition \(N\setminus\{j\}\); therefore

\[
x_j\le v_\lambda(N)-v_\lambda(N\setminus\{j\})=\lambda I_j+(2\lambda-1)O_j.
\]

Summing these upper bounds yields

\[
\lambda W=\sum_jx_j\le (3\lambda-1)W.
\]

If \(W>0\), this is impossible for \(\lambda<\tfrac12\). If \(W=0\), nonnegativity makes every weight zero and the game identically zero; its core is \(\{0\}\).

**Step 2: construction and exact slack.** For \(\lambda\ge\tfrac12\), define

\[
x^*_j=\frac{I_j}{2}+\left(\lambda-\frac12\right)O_j.
\]

This allocation is efficient because \(\sum_jx^*_j=\lambda W=v_\lambda(N)\). For each coalition \(S\), write

\[
A(S)=\sum_{i\in S,\ j\notin S}a_{ij},\quad B(S)=\sum_{i\notin S,\ j\in S}a_{ij},\quad E(S)=\sum_{j\in S}m_j(N\setminus S).
\]

Every minimum outside incoming weight is bounded above by the sum of those outside weights, so \(0\le E(S)\le B(S)\). An internal edge contributes exactly \(\lambda\) to \(x^*(S)\); an edge entering \(S\) contributes \(\tfrac12\), and an edge leaving \(S\) contributes \(\lambda-\tfrac12\). Consequently the **exact coalition slack identity** is

\[
x^*(S)-v_\lambda(S)=\left(\lambda-\frac12\right)(A(S)+B(S))+(1-\lambda)(B(S)-E(S)).
\]

Both terms are nonnegative for \(\tfrac12\le\lambda\le1\); therefore \(x^*\) belongs to the core. At \(\lambda=\tfrac12\), the Step 1 bounds become \(x_j\le I_j/2\); their sum equals the required efficiency sum \(W/2\). Thus every bound is an equality and \(\operatorname{Core}(v_{1/2})=\{(I_j/2)_j\}\).

**Step 3: affine dimension for \(\lambda>\tfrac12\).** In the displayed exact slack identity the first coefficient is now positive, so equality holds exactly when \(A(S)+B(S)=0\). These are precisely the coalitions that are unions of connected components of \(H\). For each component \(C\), the coalitions \(C\) and \(N\setminus C\) have no crossing positive edges, so every core allocation must satisfy \(x(C)=v_\lambda(C)=\lambda\sum_{i,j\in C}a_{ij}\), by efficiency and the two core inequalities. The resulting \(c\) independent component-sum equations bound the affine dimension by \(n-c\).

Conversely, \(x^*\) satisfies every coalition inequality that splits a positive-support component *strictly*. It satisfies the component-union equalities, and only those equalities. Since there are finitely many coalitions, a sufficiently small open neighborhood of \(x^*\) within the affine space defined by the \(c\) component-sum equations remains feasible. The core therefore has affine dimension **exactly** \(n-c\).

**Step 4: total balancedness, without an external existence theorem.** Fix any nonempty \(R\subseteq N\) and restrict the same characteristic function to subsets of \(R\). Define for \(j\in R\)

\[
y^R_j=\lambda\sum_{i\in R}a_{ij}+(1-\lambda)m_j(N\setminus R).
\]

It is efficient: \(\sum_{j\in R}y^R_j=v_\lambda(R)\). For any \(T\subseteq R\), subtracting \(v_\lambda(T)\) from \(y^R(T)\) reduces the inequality vertex by vertex to comparing \(\lambda\sum_{i\in R\setminus T}a_{ij}+(1-\lambda)m_j(N\setminus R)\) with \((1-\lambda)m_j(N\setminus T)\), for \(j\in T\). If at least one incoming edge to \(j\) starts outside \(R\), enlarging the set over which the minimum is taken cannot increase that minimum; the external term alone therefore suffices. Otherwise the outside minimum for \(R\) is zero and the outside minimum for \(T\) is bounded by \(\sum_{i\in R\setminus T}a_{ij}\); its coefficient \(1-\lambda\) is at most \(\lambda\). Thus every coalition inequality holds. This proves total balancedness for \(\lambda\ge\tfrac12\). For \(W>0\) and \(\lambda<\tfrac12\), the grand coalition already has an empty core, so total balancedness fails.

**Sharpness at two vertices.** Take only the positive arc \(1\to2\) of weight one. Its coalition values are \(v_\lambda(\{1\})=0\), \(v_\lambda(\{2\})=1-\lambda\), \(v_\lambda(N)=\lambda\). For \(\lambda\ge\tfrac12\) its core is the interval

\[
\{(t,\lambda-t):0\le t\le2\lambda-1\}.
\]

Thus the transition cannot be improved, and the non-singleton phase already appears on the smallest graph with a positive edge.

## Verification

Run `python verify_parametric_trust.py` from the same directory as this document. The script uses only Python's standard library and exact rational arithmetic, and prints a concise PASS summary on success. It checks all \(4{,}165\) loopless zero-or-unit-weight digraphs on \(1\le n\le4\) vertices at five parameter values, plus \(180\) seeded nonnegative weighted digraphs on \(2\le n\le5\) at seven values: \(22{,}085\) parameterized graph cases in all. For these cases it checks the co-singleton identities, the phase obstruction, the proposed core allocation, tight-coalition and weak-component equivalences, and the restricted-game core certificates, together with the two-vertex witness. These finite computations corroborate but do not establish the unbounded-\(n\) theorem; Steps 1–4 do.

## Relationship to prior work

Bandhana, Kroupa, and García (2024) introduced the unweighted-sum trust game and exhibited an indegree-based core allocation. Ryzák and Kroupa (2026) proved that the core of that **fixed sum** is a singleton and that its restrictions are balanced; they also established power-index formulas. Their Section 6 explicitly identifies the effect of convexly weighting internal versus external contributions on the core as a future research direction. The present result treats precisely that coefficient family. The 2026 fixed-sum game corresponds, up to positive scalar multiplication, to \(\lambda=\tfrac12\); that isolated case neither implies the empty-core side nor gives the positive-dimensional core formula on the other side. The well-known internal edge-sum game is the endpoint \(\lambda=1\), but its behavior alone does not establish the universal transition or the dimensions at intermediate weights.

## Limitations

The theorem assumes finite loopless directed graphs, nonnegative arc weights, an external *minimum* with the explicit empty-set convention, and convex coefficients \(0\le\lambda\le1\). It does not analyze signed weights, unbounded graphs, median or mean external aggregators, arbitrary allocations outside the core, or the full vertex/facet structure of the core. The algebraic proof is exact and does not depend on sampling; the finite checks are independent corroboration only. Historical priority under terminology not captured by the targeted literature comparison remains a risk; no independent audit or external validation is claimed.

## References

1. D. Ryzák and T. Kroupa, *A Tractable Class of Cooperative Games Defined by Directed Networks: Unanimity Decomposition and Shapley Value*, arXiv:2605.18157v1 (first submitted 18 May 2026), https://arxiv.org/html/2605.18157v1. In particular Definition 2.1, Section 5, and the parametric direction in Section 6.
2. A. Bandhana, T. Kroupa, and S. García, *Trust in Shapley: A Cooperative Quest for Global Trust in P2P Network*, AAMAS 2024, pp. 132–140, https://aamas.csc.liv.ac.uk/Proceedings/aamas2024/pdfs/p132.pdf. In particular Section 3 (trust-game definition and core construction).
