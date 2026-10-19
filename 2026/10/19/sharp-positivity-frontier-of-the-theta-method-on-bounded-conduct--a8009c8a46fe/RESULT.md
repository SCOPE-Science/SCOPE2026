# Sharp positivity frontier of the theta method on bounded-conductance graph Laplacians

## Finding
Let \(n\ge3\) and \(w>0\). For any connected undirected weighted graph on \(n\) vertices with symmetric edge conductances \(0\le c_{ij}\le w\), let \(L\) be its combinatorial weighted Laplacian, so \(L_{ij}=-c_{ij}\) for distinct vertices and \(L_{ii}=\sum_{j\ne i}c_{ij}\). For \(0\le\theta\le1\) and time step \(h\ge0\), define the theta-method diffusion update
\[
T_{\theta,h}(L)=(I+\theta hL)^{-1}(I-(1-\theta)hL).
\]
This is a row-stochastic real matrix, although it need not be entrywise nonnegative.

**Theorem.** Put \(\theta_c=(n-1)/n\). If \(0\le\theta<\theta_c\), then, simultaneously for every graph in the stated class,
\[
T_{\theta,h}(L)\ge0\text{ entrywise whenever }
0\le h\le H_{n,w}(\theta):=\frac1{w(n-1-n\theta)}.
\]
The bound is **sharp**, and the graphs attaining this smallest possible positivity horizon are exactly those possessing a *saturated universal vertex*: a vertex joined to all other vertices with conductance exactly \(w\). For each such graph the update ceases to be nonnegative for every \(h>H_{n,w}(\theta)\); for every graph without such a vertex its own maximal positivity horizon is strictly larger. If \(\theta_c\le\theta\le1\), then \(T_{\theta,h}(L)\) is entrywise nonnegative for **every** \(h\ge0\), for every graph in the class.

The extremizing graphs need not be complete graphs: all peripheral edges of a saturated star may be chosen arbitrarily within the cap (including absence), so the complete graph and the star attain exactly the same sharp horizon. This identifies every worst-case topology, rather than just a worst-case bound.

## Assumptions and scope
All graphs have fixed labeled vertex set of cardinality \(n\ge3\), positive conductances along their actual edges bounded above by \(w\); absent edges have conductance zero. Graphs are connected and undirected. The diagonal of the graph Laplacian is the **weighted degree**, and the theta method is applied to the ODE \(u'(t)=-Lu(t)\), with \(\theta\in[0,1]\) and arbitrary nonnegative \(h\). A positivity horizon means the supremum of steps for which the entire update is entrywise nonnegative; the proof shows positivity holds for all smaller steps and fails for all larger steps when the horizon is finite. The theorem concerns entrywise preservation of nonnegative vectors at the full time step, not positivity of intermediate stages or high-order temporal accuracy.

## Proof
**Step 1 (exact entrywise criterion for positive theta).** For \(\theta>0\), set \(t=\theta h\) and \(R_t=(I+tL)^{-1}\). Since \(L\) is a symmetric graph Laplacian, \(I+tL\) is a nonsingular Stieltjes matrix; its inverse is entrywise nonnegative and preserves \(\mathbf1\). Elementary multiplication gives
\[
T_{\theta,h}(L)=\frac1\theta R_t-\frac{1-\theta}{\theta}I.
\]
Therefore off-diagonal entries are always nonnegative and
\[
T_{\theta,h}(L)\ge0\ \Longleftrightarrow\ 
(R_t)_{ii}\ge1-\theta\quad\text{for every vertex }i.
\]
For connected graphs, the spectral theorem shows
\[
(R_t)_{ii}=\frac1n+\sum_{k=2}^n\frac{u_k(i)^2}{1+t\lambda_k},
\]
where \(0<\lambda_2\le\cdots\le\lambda_n\) are nonzero Laplacian eigenvalues and \(u_k\) complete an orthonormal eigenbasis with \(u_1=\mathbf1/\sqrt n\). The positive summands have total numerator weight \(1-1/n>0\); hence every diagonal is continuous and strictly decreasing from \(1\) to \(1/n\) as \(t\) increases. In particular, if \(\theta\ge1-1/n\), every diagonal stays at least \(1-\theta\) for all steps, establishing unconditional positivity.

**Step 2 (uniform sharp comparison).** The graph-edge cap gives the Loewner inequality
\[
L\preceq wL_{K_n}=w(nI-\mathbf1\mathbf1^{\mathsf T}).
\]
Inverting positive-definite matrices reverses that order:
\[
R_t\succeq R_t^{K}:=(I+twL_{K_n})^{-1}.
\]
The explicit complete-graph resolvent has
\[
R_t^{K}=\frac1n\mathbf1\mathbf1^{\mathsf T}+
\frac1{1+ntw}\left(I-\frac1n\mathbf1\mathbf1^{\mathsf T}\right),\qquad
(R_t^K)_{ii}=\frac{1+tw}{1+ntw}.
\]
Thus every graph has \((R_t)_{ii}\ge(1+tw)/(1+ntw)\). For \(0<\theta<(n-1)/n\), the latter expression is at least \(1-\theta\) exactly when \(h\le1/[w(n-1-n\theta)]\), proving the universal bound.

**Step 3 (complete equality characterization).** Fix any \(t>0\) and vertex \(i\), and abbreviate \(A=I+tL\), \(B=I+twL_{K_n}\). The matrix \(A^{-1}-B^{-1}\) is positive semidefinite. Its \(i\)-th diagonal entry vanishes exactly when \((A^{-1}-B^{-1})e_i=0\), equivalently
\[
(B-A)B^{-1}e_i=0.
\]
Indeed a positive-semidefinite matrix has zero diagonal quadratic form exactly when it annihilates that vector; multiplying the resulting inverse-vector identity by \(A\) gives the stated equivalence, and the converse follows by reversing the algebra. The vector \(B^{-1}e_i\) has a common value on all vertices other than \(i\), and differs strictly at \(i\). Meanwhile \(B-A=t(wL_{K_n}-L)\) is the Laplacian with nonnegative edge weights \(w-c_{jk}\), so
\[
(B^{-1}e_i)^{\mathsf T}(B-A)(B^{-1}e_i)
= t\left(\frac1{1+ntw}\right)^2\sum_{j\ne i}(w-c_{ij}).
\]
It follows that \((R_t)_{ii}=(R_t^K)_{ii}\) **if and only if** \(c_{ij}=w\) for all \(j\ne i\), namely \(i\) is saturated and universal. Notice that no restriction at all is imposed on edges between peripheral vertices.

For \(0<\theta<(n-1)/n\), at the universal threshold the comparison resolvent diagonal equals \(1-\theta\). By the equality characterization, any graph with a saturated universal vertex has a diagonal exactly at that threshold, and a graph without one has *all* diagonals strictly above the threshold. Strict monotonicity and the large-step limit \(1/n<1-\theta\) now establish the asserted equality/strict inequality of maximal horizons, respectively. Moreover, for an extremizer the relevant diagonal falls below \(1-\theta\) at every larger step.

**Step 4 (explicit Euler endpoint).** If \(\theta=0\), then \(T_{0,h}=I-hL\). Its off-diagonal entries are nonnegative; its diagonal entries are \(1-hd_i\), where \(d_i=\sum_{j\ne i}c_{ij}\). Hence the exact horizon is \(1/\max_i d_i\), and the largest possible weighted degree is \((n-1)w\). Equality holds precisely if at least one vertex is joined to all other vertices at conductance \(w\). The resulting universal threshold is the displayed formula at \(\theta=0\). This completes all cases.

## Verification
The companion `verify.py` uses exact rational arithmetic, forms full graph Laplacians, and checks the proposed theorem on all connected unweighted graphs of orders three and four at representative rational theta parameters. It additionally verifies complete-graph and saturated-star equality for orders three through five, and confirms the nonnegativity loss just beyond the claimed finite thresholds. These finite tests are diagnostic; the proof of the unrestricted weighted, all-order statement is entirely the four-step argument above. Execute `python verify.py` with SymPy installed.

## Relationship to prior work
Schatz, Thomée, and Wahlbin (2010) analyze theta-scheme positivity and maximum-norm contractivity for parabolic discretizations; their displayed local CFL-type criterion is a sufficient condition and does not characterize all finite graphs that maximize their sharp positivity obstruction under an edge-conductance cap. Kovács, Li, and Lubich (2015 preprint) study maximal regularity of A-stable time discretizations, a different stability property which does not entail coordinatewise positivity.

The earlier public result *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains* proves the diagonal-resolvent criterion for the Crank–Nicolson case, its fixed-chain threshold, and the complete-graph example. **That general criterion and the complete-graph threshold are prior work and are not claimed here**. Our Step 1 extends the elementary algebra from Crank–Nicolson to general theta. The distinct theorem is the **sharp uniform conductance-capped inequality with an if-and-only-if classification of every worst-case graph, including saturated noncomplete stars, across all theta parameters and graph orders**. Neither the inspected fixed-chain threshold nor the complete-graph example implies the saturated-universal-vertex equality characterization without the Loewner inverse comparison and its equality analysis.

## Limitations
This is a worst-case graph-family theorem and does not supply a simple closed form for the positivity horizon of every individual graph without a saturated universal vertex. The graph order, positive conductance cap, undirectedness, and connectedness are essential to the stated classification. The theta parameter is restricted to the usual interval \([0,1]\). The comparison is at the full-step update; positivity of an internal solver stage or approximation of nonlinear dynamics is not established. The proof does not imply that the complete graph uniquely minimizes the positivity horizon—indeed that uniqueness statement is false by the stated characterization. Although targeted literature and database comparisons found no implication-equivalent general classification, equivalent work could remain in unindexed literature.

## References
1. A. H. Schatz, V. Thomée, and L. B. Wahlbin, *On Positivity and Maximum-Norm Contractivity in Time Stepping Methods for Parabolic Equations*, Computational Methods in Applied Mathematics 10 (2010), DOI: 10.2478/cmam-2010-0025.
2. B. Kovács, B. Li, and C. Lubich, *A-stable time discretizations preserve maximal parabolic regularity*, first publicly posted 24 November 2015, arXiv:1511.07823.
3. Z. Horváth, *Positivity of Runge–Kutta and Diagonally Split Runge–Kutta Methods*, Applied Numerical Mathematics 28 (1998), DOI: 10.1016/S0168-9274(98)00050-6.
4. *A resolvent-return law for Crank–Nicolson positivity on reversible Markov chains*, public mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-a-resolvent-return-law-for-crank-nicolson-positivity-on-reversib--d475df91cd2a.
