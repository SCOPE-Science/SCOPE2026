# A rational generating function for the sphere ranks of ladder cut complexes

## Finding
Let \(L_n=P_n\square K_2\) be the two-row ladder with \(n\ge3\) rungs. For every integer \(3\le k\le2n-3\), let \(\Delta_k(L_n)\) be the ordinary cut complex whose facets are complements of disconnected induced \(k\)-vertex subsets. Put
\[
C(z,t)=\frac{zt(2+t+zt^2)}{(1-z)^2\bigl(1-z(t+t^2)-z^2t^3\bigr)},\qquad c_{n,k}=[z^nt^k]C(z,t),
\]
and
\[
b_{n,k}=\begin{cases}n-(k-1)/2,&k\text{ odd},\\0,&k\text{ even}.\end{cases}
\]
Then the full integral homotopy type is
\[
\boxed{\ \Delta_k(L_n)\simeq\bigvee^{\beta_{n,k}}S^{2n-k-1},\qquad
\beta_{n,k}=\binom{2n-1}{k-1}-c_{n,k}+b_{n,k}.\ }
\]
The coefficient formula is effective simultaneously for all permitted \(n,k\), without enumerating any cut-complex faces. In particular, for all \(n\ge4\),
\[
\beta_{n,5}=\binom{2n-1}{4}-19n+54.
\]

## Assumptions and scope
The graph is finite, simple and undirected, with vertices \((i,0),(i,1)\) for \(1\le i\le n\); edges join the two vertices of a rung and join consecutive vertices in the same row. A disconnected induced \(k\)-set means exactly that its induced graph has at least two connected components. The wedge convention includes the contractible case when \(\beta_{n,k}=0\). The result does not concern the *total* cut complex, where the omitted vertices must be independent, nor the circular ladder \(C_n\square K_2\). The asserted range uses the published shellability theorem for the ordinary \(k\)-cut complex of a two-row rectangular grid.

## Proof
Write \(N=2n\), \(r=N-k\), and \(V=V(L_n)\). A subset \(F\subseteq V\) with at most \(r\) elements is a face of \(\Delta_k(L_n)\) if and only if its complement contains some disconnected induced \(k\)-set. Every subset of at most \(r-2\) vertices is a face: its complement \(T\) has at least \(k+2\) vertices; choose a vertex \(v\) in the leftmost occupied column of \(T\). Its degree in the induced subgraph on \(T\) is at most two. Therefore at least \(k-1\) vertices of \(T\) are distinct from \(v\) and from every neighbor of \(v\). The set consisting of \(v\) and any \(k-1\) such vertices is disconnected.

A set of \(r\) vertices is a nonface exactly when its complementary \(k\)-set is connected. Let \(c_{n,k}\) count connected induced \(k\)-vertex subsets of \(L_n\). A set of \(r-1\) vertices is a nonface exactly when deleting any one vertex from its complementary \((k+1)\)-set \(T\) leaves a connected induced \(k\)-set. Since \(k\ge3\), this is equivalent to the induced graph on \(T\) being connected and having no cut vertex. Such a set has minimum induced degree at least two.

For a connected vertex subset of a ladder, the occupied columns form an interval. Its extreme columns must each contain both row vertices if the induced graph has minimum degree at least two. Every interior column must also contain both vertices: an interior column containing only one vertex produces a cut vertex separating its occupied left and right sides. Conversely, the full set of vertices of any consecutive block of \(m\ge2\) columns induces a two-connected ladder graph (a cycle for \(m=2\), and adjoining adjacent rungs preserves two-connectivity). Thus the only such \(T\) are the \(n-m+1\) fully occupied consecutive blocks of size \(2m=k+1\). Their number is precisely \(b_{n,k}\), including zero when \(k\) is even.

It follows that all faces of cardinality at most \(r-2\) occur; exactly \(b_{n,k}\) faces of cardinality \(r-1\) are absent; and exactly \(c_{n,k}\) faces of cardinality \(r\) are absent. The alternating binomial identity yields
\[
(-1)^{r-1}\widetilde\chi(\Delta_k(L_n))
=\binom{N-1}{k-1}-c_{n,k}+b_{n,k}.
\]
Theorem 5.6 of Chandrakar--Hazra--Rout--Singh proves that \(\Delta_k(L_n)\) is shellable for \(3\le k\le2n-3\). A nonvoid pure shellable simplicial complex is homotopy equivalent to a wedge of spheres in its top dimension, here \(r-1\). Hence its top sphere rank is the displayed Euler-characteristic value, with free integral homology and no other reduced homology.

It remains to count \(c_{n,k}\) uniformly. Each connected vertex subset occupies some consecutive interval of \(w\) columns, and its occupied columns have one of three states: top only, bottom only, or both. A transition between opposite singleton states is forbidden, because it disconnects the induced graph. All other transitions are allowed. Let \(A_w(t)\) count state words ending in one *specified* singleton state, weighted by a factor \(t\) for each selected vertex; let \(D_w(t)\) count words ending with both vertices. Reflection interchanges the two singleton states, so
\[
A_1=t,\quad D_1=t^2,\qquad
A_{w+1}=t(A_w+D_w),\quad D_{w+1}=t^2(2A_w+D_w).
\]
Solving these two linear generating-series equations gives
\[
\sum_{w\ge1}(2A_w(t)+D_w(t))z^w
=\frac{zt(2+t+zt^2)}{1-z(t+t^2)-z^2t^3}.
\]
An occupied block of width \(w\) admits exactly \(n-w+1\) placements in \(L_n\). Multiplication by \(1/(1-z)^2\) implements this translation count, giving the claimed \(C(z,t)\). For size five the only widths are three, four and five; the corresponding numbers of state words are \(6,12,2\), respectively. Thus \(c_{n,5}=6(n-2)+12(n-3)+2(n-4)=20n-56\) for \(n\ge4\). Together with \(b_{n,5}=n-2\), the stated specialized formula follows. \(\square\)

## Verification
The attached standalone Python 3 program `VERIFY.py` generates the weighted state-word counts by independent coefficient recurrence and enumerates induced connected subsets and deletion-robust subsets directly for \(3\le n\le7\). It compares these independent counts and the closed rank formula. It also constructs facets and alternating face counts on small ladders to check the Euler-characteristic prediction. The finite replay is a consistency test, **not** a replacement for the infinite proof given above. In particular, the checks reproduce the five-cut rank sequence \(13,85,270,636\) for \(n=4,5,6,7\), as tabulated in [1].

## Relationship to prior work
Bayer--Denker--Jelić Milutinović--Sundaram--Xue [1] introduce the ordinary cut-complex convention, develop general face-poset and Euler methods (Section 2), and give the ladder-grid five-cut values for only a finite tabulated range (Section 5, Table 3). They also determine the three- and four-cut ranks for general rectangular grids. Chandrakar--Hazra--Rout--Singh [2], Theorem 5.6 in version 3, prove the necessary two-row-grid shellability for every \(3\le k\le2n-3\), but do not provide an all-parameter rank generating function. The contribution here is the exact bivariate rational coefficient formula for all ladder sizes and cut parameters, based on the explicit classification of exceptional complementary sets. Ordinary cut complexes should not be conflated with total cut complexes or with squared-path or circular-ladder constructions.

## Limitations
The shellability input is from [2] rather than reproved here, and the formula is restricted to \(3\le k\le2n-3\). The result is not an independent proof of a new shellability theorem. It does not determine equivariant homology, cellular attaching maps, or an analogous formula for wider grids. The novelty assessment is based on accessible full-text comparisons and searches, not an exhaustive proof that the formula has never appeared elsewhere.

## References
[1] M. Bayer, M. Denker, M. Jelić Milutinović, S. Sundaram, L. Xue, *Topology of Cut Complexes II*, arXiv:2407.08158v1, first publicly available 2024-07-11. https://arxiv.org/abs/2407.08158

[2] H. Chandrakar, N. R. Hazra, D. Rout, A. Singh, *Topology of total cut complexes and cut complexes of grid graphs*, arXiv:2408.07646; originally submitted 2024-08-14, Theorem 5.6 read in version 3 (2026-01-12). https://arxiv.org/abs/2408.07646
