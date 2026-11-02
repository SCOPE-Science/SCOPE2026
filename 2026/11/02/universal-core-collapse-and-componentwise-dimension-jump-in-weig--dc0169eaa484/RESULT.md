# Universal core collapse and componentwise dimension jump in weighted trust games

## Finding
Let a finite loopless directed network have nonnegative arc weights. A coalition earns a convex mixture of its internal arc weight and the sum, over coalition members, of their minimum incoming weight from outside the coalition. If at least one arc has positive weight, the transferable-utility core is **empty** when the internal coefficient is below \(1/2\), is **a singleton** at \(1/2\), and has affine dimension exactly \(n-c\) above \(1/2\), where \(c\) is the number of weak components of the positive-weight support (including isolated vertices). For coefficients at least \(1/2\), every restricted subgame has a nonempty core. When all arc weights vanish, every coefficient gives the singleton zero core.

In particular, for a connected positive-weight support, the transition at \(1/2\) changes the core from empty to a unique allocation, and immediately thereafter to a polytope of full possible dimension \(n-1\). The result applies to arbitrary finite directed topologies, unequal weights, reciprocated and unreciprocated arcs, and zero-weight arcs.

## Assumptions and scope
Fix a finite vertex set \(N\), \(n=|N|\ge 2\), and a loopless directed graph \(G=(N,E)\). Each arc \((i,j)\in E\) has weight \(a_{ij}\in[0,1]\); unlisted arcs contribute nothing. For \(S\subseteq N\), define
\[
I(S)=\sum_{(i,j)\in E:\ i,j\in S}a_{ij},\qquad
E(S)=\sum_{j\in S} b_j(S),
\]
where \(b_j(S)\) is the minimum of \(\{a_{ij}:(i,j)\in E,\ i\notin S\}\) when this set is nonempty, and is \(0\) otherwise. In particular \(E(N)=0\). For each \(\alpha\in[0,1]\), set
\[
v_\alpha(S)=\alpha I(S)+(1-\alpha)E(S).
\]
The (transferable-utility) core \(\mathcal C_\alpha\) consists of \(x\in\mathbb R^N\) satisfying \(x(N)=v_\alpha(N)\) and \(x(S)\ge v_\alpha(S)\) for every \(S\subseteq N\); here \(x(S)=\sum_{i\in S}x_i\). Monetary transfers can be negative. A restricted subgame on \(S\) retains the original values \(v_\alpha(T)\) for \(T\subseteq S\). The family is *totally balanced* when every nonempty restriction has a nonempty core.

Write \(W=\sum_{(i,j)\in E}a_{ij}\), \(d_j^{\rm in}=\sum_{i:(i,j)\in E}a_{ij}\), and \(d_i^{\rm out}=\sum_{j:(i,j)\in E}a_{ij}\). Let \(H\) be the undirected graph with \(\{i,j\}\) an edge exactly when \(a_{ij}>0\) or \(a_{ji}>0\). Let \(c\) be the number of components of \(H\), including isolated vertices.

## Proof
**1. A deletion identity and impossibility.** Since the only outsider to \(N\setminus\{i\}\) is \(i\), its external term is \(d_i^{\rm out}\), while its internal term is \(W-d_i^{\rm in}-d_i^{\rm out}\). Hence, with \(V=v_\alpha(N)=\alpha W\),
\[
v_\alpha(N\setminus\{i\})
=\alpha W-\alpha d_i^{\rm in}+(1-2\alpha)d_i^{\rm out}.
\]
Any core allocation must satisfy
\[
x_i=V-x(N\setminus\{i\})\le
\alpha d_i^{\rm in}+(2\alpha-1)d_i^{\rm out}.
\]
Summing these bounds, and using that total indegree and total outdegree both equal \(W\), yields
\[
\alpha W=\sum_i x_i\le(3\alpha-1)W.
\]
For \(W>0\) this forces \(\alpha\ge1/2\). This is an obstruction for **each** nonzero weighted network, not merely an example establishing failure of a universal guarantee.

**2. Feasibility and uniqueness at the boundary.** Define the incoming vector \(D=(d_i^{\rm in})_{i\in N}\) and the incoming cut weight \(C(S)=\sum_{(i,j)\in E:\ i\notin S,j\in S}a_{ij}\). Nonnegativity gives \(E(S)\le C(S)\), because the minimum of a nonempty list of nonnegative numbers does not exceed its sum. Since \(D(S)=I(S)+C(S)\), the allocation \(D/2\) is efficient for \(v_{1/2}\) and satisfies
\[
(D/2)(S)\ge\tfrac12(I(S)+E(S))=v_{1/2}(S).
\]
At \(\alpha=1/2\), the upper bounds in Step 1 read \(x_i\le d_i^{\rm in}/2\). They sum to the required grand-coalition worth, so every upper bound must be tight. Therefore \(\mathcal C_{1/2}=\{D/2\}\).

**3. A graph-zonotope of stable allocations above the boundary.** Define the edge-splitting zonotope
\[
Z_G=\left\{\sum_{(i,j)\in E}a_{ij}
\bigl(t_{ij}e_i+(1-t_{ij})e_j\bigr):
0\le t_{ij}\le1\right\},
\]
where \(e_i\) are standard coordinate vectors. Each \(z\in Z_G\) satisfies \(z(N)=W\) and \(z(S)\ge I(S)\), since every internal arc contributes its entire weight to the endpoints in \(S\), and crossing arcs contribute nonnegative amounts. For \(\alpha\ge1/2\), put
\[
x=(1-\alpha)D+(2\alpha-1)z.
\]
Its total equals \(\alpha W\), and for every \(S\subseteq N\),
\[
\begin{aligned}
x(S)&\ge(1-\alpha)(I(S)+C(S))+(2\alpha-1)I(S)\\
&=\alpha I(S)+(1-\alpha)C(S)\\
&\ge\alpha I(S)+(1-\alpha)E(S)=v_\alpha(S).
\end{aligned}
\]
Thus \((1-\alpha)D+(2\alpha-1)Z_G\subseteq\mathcal C_\alpha\). This inclusion is **not** asserted to be an equality.

**4. Exact affine dimension.** Suppose \(\alpha>1/2\). The direction space of \(Z_G\) is spanned by \(e_i-e_j\) over positive-weight arcs. For each component of \(H\), the edge differences of a spanning tree span all vectors whose coordinate sum on that component is zero. Consequently
\[
\dim Z_G=n-c.
\]
The positive coefficient \(2\alpha-1\) and Step 3 give \(\dim\mathcal C_\alpha\ge n-c\). Conversely, let \(C\) be any component of \(H\). All arcs crossing from \(C\) to its complement have zero weight (if present), so
\[
v_\alpha(C)=\alpha W_C,\qquad
v_\alpha(N\setminus C)=\alpha(W-W_C),
\]
where \(W_C\) is the total positive arc weight internal to \(C\). Every core point must therefore satisfy \(x(C)=\alpha W_C\). These \(c\) independent component-sum equations bound the affine dimension by \(n-c\). Equality follows.

**5. All restricted subgames.** For any nonempty \(S\subseteq N\), set
\[
q_j^S=\sum_{i\in S:(i,j)\in E}a_{ij}+b_j(S),\quad j\in S.
\]
The vector \(q^S\) is efficient for \(I+E\) on the restriction to \(S\). For any \(T\subseteq S\), its weight assigned to each \(j\in T\) includes the incoming weight from \(T\), the incoming weight from \(S\setminus T\), and \(b_j(S)\). The last two nonnegative terms together dominate \(b_j(T)\): the latter minimum is taken over incoming arcs from \((S\setminus T)\cup(N\setminus S)\), and is at most either available cross-arc sum or the exterior minimum. Summing over \(j\in T\) shows \(q^S(T)\ge I(T)+E(T)\).

Let \(z^S\) split each internal arc of \(S\) nonnegatively between its endpoints. Then \(z^S(S)=I(S)\) and \(z^S(T)\ge I(T)\). Therefore, for every \(\alpha\ge1/2\),
\[
(1-\alpha)q^S+(2\alpha-1)z^S
\]
is efficient and coalitionally rational for the restriction of \(v_\alpha\) to \(S\). Thus the game is totally balanced at and above the threshold. Below it, the nonempty grand-coalition game already has an empty core whenever \(W>0\), so it is not totally balanced.

Finally, if \(W=0\), nonnegativity forces \(I(S)=E(S)=0\) for every \(S\). Every individual coordinate of a core point must be nonnegative and the total must be zero; thus the core is \(\{0\}\) for every coefficient.

## Verification
The accompanying standalone `verify.py` uses exact rational arithmetic (Python standard library) and reproduces `VERIFY_OK rational_graph_parameter_cases=2555 graph_profiles=365 parameters=7`. It covers \(n=2,3,4,5,6\), seven rational coefficients on both sides of the critical value, random nonnegative weighted digraphs, empty and one-edge boundary graphs, and graphs with zero-weight arcs. It enumerates every coalition and every restricted subgame in each sampled graph, checks deletion identities and stability inequalities, and independently computes the rank of the positive-edge incidence differences by rational Gaussian elimination. This finite check supplements; it does not replace or extend the universal proof above.

## Relationship to prior work
Bandhana, Kroupa and García [1] introduced the internal-plus-external trust game and an explicit stable allocation. Ryzák and Kroupa [2, Sections 2 and 5] proved singleton core and total balancedness for the **unscaled sum** \(I+E\), corresponding here to \(\alpha=1/2\) after rescaling. They explicitly identify varying the relative coefficients as a research direction [2, Section 6]. The inclusion of a graphical edge-splitting zonotope uses the classical structure of induced-edge games [3]. Total balancedness at the nonnegative side of the parameter range also follows from a general aggregation-operator insertion criterion and is not presented as novel in isolation. The present contribution is the **every-nonzero-graph obstruction** below the threshold and the **exact core-dimension formula for all positive-weight components** above it, yielding a sharp network-wide geometric phase classification.

## Limitations
The coefficient is restricted to the convex range \(0\le\alpha\le1\), arc weights are nonnegative, and loops are excluded. The result gives affine dimension and an explicit included zonotope, not the full facet structure, vertices, or volume of the core for \(\alpha>1/2\). In fact the included zonotope can be a proper subset: in the complete three-vertex bidirected unit-weight graph at \(\alpha=3/4\), \((1/4,17/8,17/8)\) belongs to the core but not to the displayed zonotope translation because the latter has every coordinate at least \(1/2\). This demonstrates why the inclusion was not upgraded to an unproved equality. No assertion about incentive compatibility or the Shapley value is made.

## References
[1] A. Bandhana, T. Kroupa, S. García, *Trust in Shapley: A Cooperative Quest for Global Trust in P2P Network*, AAMAS 2024, pp. 132–140. https://aamas.csc.liv.ac.uk/Proceedings/aamas2024/pdfs/p132.pdf

[2] D. Ryzák, T. Kroupa, *A Tractable Class of Cooperative Games Defined by Directed Networks: Unanimity Decomposition and Shapley Value*, arXiv:2605.18157v1, first posted 2026-05-18. https://arxiv.org/abs/2605.18157

[3] X. Deng, C. H. Papadimitriou, *On the Complexity of Cooperative Solution Concepts*, Mathematics of Operations Research 19 (1994), 257–266. (Induced-edge coalition games and classical edge allocations.)
