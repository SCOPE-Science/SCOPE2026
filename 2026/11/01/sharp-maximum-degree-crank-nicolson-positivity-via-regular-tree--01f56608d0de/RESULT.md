# Sharp maximum-degree Crank–Nicolson positivity via regular-tree returns

## Finding

**Theorem (sharp uniform nonnegativity radius).** Fix any integer \(\Delta\ge3\) and let
\[
\sigma_\Delta=\frac{2\Delta-1}{2\Delta(\Delta-1)}.
\]
For every finite connected simple graph \(G\) on at least two vertices, with unit conductances and maximum degree at most \(\Delta\), let \(L_G=D_G-A_G\) be the combinatorial Laplacian and define the Crank–Nicolson update
\[
C_G(s)=(I+sL_G)^{-1}(I-sL_G),\qquad s\ge0.
\]
Then \(C_G(s)\) is entrywise nonnegative whenever \(0\le s\le\sigma_\Delta\). Indeed, every entry is strictly positive if \(0<s\le\sigma_\Delta\). Conversely, for each fixed \(s>\sigma_\Delta\), there is a finite tree of maximum degree \(\Delta\) whose update has a negative diagonal entry. Thus the largest nonnegativity-guaranteeing physical time step \(h=2s\), uniformly over this entire graph class, is
\[
h_\Delta=\frac{2\Delta-1}{\Delta(\Delta-1)}.
\]
In particular, \(\sigma_3=5/12\) and \(\sigma_4=7/24\). These are *uniform* bounds; individual finite graphs can admit larger steps.

## Assumptions and scope

The graph is finite, simple, undirected, connected and has at least two vertices. All present edges carry conductance exactly one; absent edges have conductance zero. There is no normalization of the combinatorial Laplacian. The degree cap \(\Delta\) is an integer at least three, not necessarily the actual largest degree of a particular graph. The update is the unmodified trapezoidal/Crank–Nicolson step for \(u'=-L_Gu\), where \(s\) is half the physical step. Entrywise nonnegativity means preservation of every nonnegative initial vector, and the update always has row sum one. The sharpness family consists of finite radius balls about the root of an infinite regular tree, with their ordinary (unweighted, reflecting-degree) combinatorial Laplacians.

## Proof

**1. Resolvent criterion.** Set \(R_G(s)=(I+sL_G)^{-1}\). Since \(I-sL_G=2I-(I+sL_G)\),
\[
 C_G(s)=2R_G(s)-I.
\]
At each \(s>0\), \(R_G(s)\) has strictly positive entries: for instance, the Neumann expansion below has a positive contribution from some path between every pair of vertices. Hence only diagonal entries can obstruct positivity, and the condition is \(R_G(s)_{vv}\ge1/2\) at every vertex.

**2. Closed-walk lower bound.** Define the auxiliary nonnegative matrix
\[
 H_G=A_G+\operatorname{diag}(\Delta-\deg_G(v)),\qquad
 \alpha=\frac{s}{1+s\Delta}.
\]
Every row of \(H_G\) sums to \(\Delta\) and \(L_G=\Delta I-H_G\). Therefore \(0<\alpha\Delta<1\), and the absolutely convergent series is
\[
 R_G(s)_{vv}=\frac{1}{1+s\Delta}
  \sum_{k=0}^{\infty}\alpha^k(H_G^k)_{vv}.
\]
Interpret each of the \(\Delta-\deg_G(v)\) diagonal units of \(H_G\) as a separately labelled *stationary port* at \(v\). Ordinary edge ports come in reverse pairs, while a stationary port is its own reverse. Thus every vertex has exactly \(\Delta\) ports, with each directed port having a designated reverse at its endpoint. A walk in this port system records its exact port sequence; matrix powers count such walks including stationary-port multiplicities.

Construct the covering tree whose vertices are non-backtracking reduced port words beginning at a chosen root \(v\); traversing a port either appends that port or cancels the last port when it is the reverse. This is the infinite \(\Delta\)-regular tree \(\mathcal T_\Delta\). Its local projection to the port system has a unique lifting property. In particular, each length-\(k\) closed walk from the tree root projects injectively (as a port sequence) to a length-\(k\) closed walk from \(v\) in the auxiliary graph. Consequently,
\[
 (H_G^k)_{vv}\ge (A_{\mathcal T_\Delta}^k)_{oo}\quad\text{for every integer }k\ge0.
\]
Writing \(L_{\mathcal T_\Delta}=\Delta I-A_{\mathcal T_\Delta}\), this gives the resolvent comparison
\[
 R_G(s)_{vv}\ge g_\Delta(s):=
 \langle\delta_o,(I+sL_{\mathcal T_\Delta})^{-1}\delta_o\rangle.
\]
For a finite connected graph, the inequality is strict at every \(s>0\). Indeed, if some vertex has a missing-degree stationary port, a path to it, followed by the stationary port and the reverse path, produces a closed port sequence that does not reduce to the empty tree word. Otherwise the finite graph is \(\Delta\)-regular and therefore contains a cycle; travelling to a cycle, once around it and back gives such a word. At some length the finite graph has strictly more rooted closed port walks, and the positive series makes the comparison strict.

**3. Regular-tree Green function and exact threshold.** Put \(z=1+s\Delta\). Remove the parent edge of a nonroot tree vertex and let \(q=q_\Delta(s)>0\) denote the diagonal cavity resolvent. Schur complementation across the \(\Delta-1\) forward branches gives
\[
 q=\frac{1}{z-(\Delta-1)s^2q},\qquad
 q=\frac{z-\sqrt{z^2-4(\Delta-1)s^2}}{2(\Delta-1)s^2}.
\]
The smaller quadratic root is chosen because it is the positive branch continuous at \(s=0\), with \(q(0)=1\). At the root, another Schur complement yields
\[
 g_\Delta(s)=\frac{1}{z-\Delta s^2q}
 =\frac{2(\Delta-1)}{(\Delta-2)z+\Delta\sqrt{z^2-4(\Delta-1)s^2}}.
\]
The discriminant is positive for \(\Delta\ge3\), \(s>0\). The function \(g_\Delta(s)\) decreases strictly from one: indeed
\[
 g_\Delta'(s)=-\big\langle
 (I+sL_{\mathcal T_\Delta})^{-1}\delta_o,
 L_{\mathcal T_\Delta}(I+sL_{\mathcal T_\Delta})^{-1}\delta_o
 \big\rangle<0,
\]
since a vertex delta is not in the nullspace of the tree Laplacian. To identify the half-return crossing, imposing \(g_\Delta(s)=1/2\) gives
\[
 q=\frac{\Delta s-1}{\Delta s^2}.
\]
Substitute into the cavity quadratic; after multiplying by the positive denominator this simplifies to
\[
 2\Delta(\Delta-1)s=2\Delta-1.
\]
At \(s=\sigma_\Delta\) the displayed \(q\) is positive and is the smaller physical root (direct substitution or the quadratic formula). Thus \(g_\Delta(\sigma_\Delta)=1/2\), and strict monotonicity gives \(g_\Delta(s)\ge1/2\) exactly when \(0\le s\le\sigma_\Delta\). Step 2 and the strict positivity of the offdiagonal resolvent complete the universal assertion, including strict positivity at the endpoint on every *finite* connected graph.

**4. Sharpness among finite trees.** Let \(T_r\) be the induced radius-\(r\) ball about \(o\) in \(\mathcal T_\Delta\), considered as a finite simple graph with its ordinary combinatorial Laplacian. Define its auxiliary matrix \(H_r=A_{T_r}+\operatorname{diag}(\Delta-\deg_{T_r})\). For each fixed \(k\), once \(r>k\) no rooted length-\(k\) walk can encounter a boundary stationary port; therefore
\[
 (H_r^k)_{oo}=(A_{\mathcal T_\Delta}^k)_{oo}.
\]
Both sides are bounded by \(\Delta^k\). Since \(\alpha\Delta<1\), dominated convergence of the Neumann series implies
\[
 \lim_{r\to\infty}(I+sL_{T_r})^{-1}_{oo}=g_\Delta(s).
\]
For any fixed \(s>\sigma_\Delta\), the limiting Crank–Nicolson center diagonal is \(2g_\Delta(s)-1<0\), so a sufficiently large *finite* ball has a negative center diagonal. Each \(T_r\) has maximum degree \(\Delta\). This proves uniform sharpness.

## Verification

An accompanying standard-library Python verifier checks the cavity identity and the half-return root exactly with rational arithmetic for degrees two through ten, exhaustively verifies nonnegativity at the claimed degree bound for all \(771\) connected labelled simple graphs on two through five vertices, and verifies exact-rational negative center diagonals on radius-two tree balls for degrees two, three and four at \(s=11\sigma_\Delta/10\). The nontrivial degree-three and degree-four center entries are \(-64/1817\) and \(-12855/324713\), respectively. A separate numerical check of the connected graph atlas on at most seven vertices found no counterexample in \(994\) connected nontrivial graphs of actual maximum degree at least two. Finite tests are supplementary and do not establish the universal quantifiers or asymptotic sharpness; those follow from the covering-tree comparison and dominated-convergence proof.

Reproduce the exact finite tests using `python3 verify.py` from the extracted package. No third-party Python packages are needed for that script.

## Relationship to prior work

The general matrix-positivity framework for parabolic schemes is established by Faragó and Horváth (2006, Theorem 4.2 and Section 6). That work's necessary-and-sufficient positivity matrix condition and mesh-dependent sufficient bounds do not contain the present all-graph maximum-degree threshold or its sharp regular-tree-ball extremizers. Bressloff, Dwyer and Kearney (1996) develop diffusion Green functions on trees by a path-summation approach; their object is diffusion propagation, not a sharp uniform trapezoidal-method positivity step for arbitrary finite bounded-degree graphs. Angel, Friedman and Hoory (2007) study universal-cover Green functions and non-backtracking spectra; the covering principle is classical, and its combination here with an exact Crank–Nicolson threshold is the distinct claim. General resolvent-return positivity criteria and exact one-dimensional path cases are already known, and neither is claimed as new here. The contribution is the sharp \(\Delta\)-only bound, a strict guarantee on every finite graph, and finite-tree sharpness in all degrees \(\Delta\ge3\).

## Limitations

Only the unweighted combinatorial Laplacian is covered; the formula is not asserted for arbitrary nonuniform conductances or normalized Laplacians. The result gives a uniform worst-case threshold and does **not** compute the exact individual threshold of every finite graph. Arbitrary data-dependent positivity beyond the uniform threshold is not addressed. The method guarantees nonnegativity of one Crank–Nicolson step, not an error or convergence estimate for changing step sizes or nonlinear dynamics. Priority relative to additional specialist graph-diffusion and maximum-principle literature not available in full text remains open to independent verification.

## References

1. I. Faragó and R. Horváth, *Discrete Maximum Principle and Adequate Discretizations of Linear Parabolic Problems*, SIAM Journal on Scientific Computing **28** (2006), 2313–2336. DOI: `10.1137/050627241`. Published online 21 December 2006. <https://epubs.siam.org/doi/10.1137/050627241>.
2. P. C. Bressloff, V. M. Dwyer, and M. J. Kearney, *A ‘sum-over-paths’ approach to diffusion on trees*, Journal of Physics A **29** (1996), 1881–1896. DOI: `10.1088/0305-4470/29/9/005`. <https://www.researchgate.net/publication/231030732_A_sum-over-paths_approach_to_diffusion_on_trees>.
3. O. Angel, J. Friedman, and S. Hoory, *The Non-Backtracking Spectrum of the Universal Cover of a Graph*, first public arXiv version 2 December 2007, `arXiv:0712.0192`. <https://arxiv.org/abs/0712.0192>.
4. Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods*, Applied Numerical Mathematics **53** (2005), 341–356. DOI: `10.1016/j.apnum.2004.08.026`. The abstract was consulted; complete text not available during comparison.
