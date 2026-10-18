# A sharp eight-species reversal of clustering and stable coexistence

## Finding
Consider the symmetric competitive Lotka–Volterra system on a finite simple undirected graph \(G\):
\[
\dot x_i=x_i\left(1-x_i-\tau\sum_{j\sim i}x_j\right),\qquad x_i>0,\quad \tau\ge0.
\]
For connected cubic graphs, define \(\tau_c(G)\) as the boundary of the interval starting at \(\tau=0\) on which a linearly asymptotically stable, strictly positive coexistence equilibrium exists. Let \(C(G)\) be the mean local clustering coefficient.

**Sharp nonmonotonicity theorem.** Among all pairs of connected simple cubic graphs with the same number of vertices, the smallest order at which \(C(G_1)>C(G_0)\) and \(\tau_c(G_1)<\tau_c(G_0)\) can simultaneously hold is **eight vertices**. At eight vertices there is exactly one such unordered pair of isomorphism classes. Furthermore, it admits a *single degree-preserving two-edge switch* from the graph of lower clustering to the graph of higher clustering.

An explicit construction starts with the Wagner graph \(W\) on vertices \(0,\ldots,7\). Write \(ij\) for the unordered edge \(\{i,j\}\), and set
\[
E(W)=\{01,02,03,14,15,24,26,35,37,47,56,67\}.
\]
Define \(H\) by removing \(15,24\) and inserting \(12,45\). Both graphs are connected and cubic. They satisfy
\[
C(W)=0,\qquad C(H)=\tfrac18,
\]
yet their exact stable-coexistence thresholds are
\[
\tau_c(W)=\sqrt2-1\quad\text{and}\quad
\tau_c(H)=\frac{2}{1+\sqrt{17}}<\sqrt2-1.
\]
Thus one triangle-forming degree-preserving rewire **reduces** resistance to competitive exclusion, even with all intrinsic growth rates, carrying capacities, and vertex degrees fixed. It also slows the local return to coexistence at **every** positive competition strength common to the stable regimes, although the equilibrium abundance of each species remains identical in the two networks. Indeed, writing \(g_G(\tau)\) for the positive slowest linear decay rate, for every \(0<\tau<\tau_c(H)\),
\[
g_W(\tau)-g_H(\tau)=\frac{\tau(\sqrt{17}-1-2\sqrt2)}{2(1+3\tau)}>0.
\]

## Assumptions and scope
Graphs are finite, undirected, loopless, simple and connected, and all vertices have degree three. The dynamical system has unit intrinsic growth and carrying capacity, equal nonnegative competition \(\tau\) on every edge, and no migration, seasonality or stochasticity. The threshold concerns **linear stability of a positive equilibrium**, not mere positivity of a formal algebraic equilibrium or a claim about all solutions beyond the threshold. For cubic graphs, the two common clustering measures agree: mean local clustering and global transitivity both equal the triangle count divided by the number of vertices.

## Proof
**1. Exact dynamical reduction.** Let \(A\) be the symmetric adjacency matrix and \(B_\tau=I+\tau A\). Since \(A\mathbf1=3\mathbf1\), a positive equilibrium exists for every \(\tau\ge0\), namely \(x_i^*=1/(1+3\tau)\). At this equilibrium,
\[
J=-\frac{I+\tau A}{1+3\tau}.
\]
Hence \(J\) is Hurwitz exactly when \(B_\tau\) is positive definite, or equivalently when \(\tau<-1/\lambda_{\min}(A)\). Every cubic graph with at least one edge has \(\lambda_{\min}(A)<0\). More generally, at any strictly positive equilibrium the Jacobian is \(-\operatorname{diag}(x^*)B_\tau\), similar to a real symmetric matrix congruent to \(-B_\tau\). Consequently **no positive equilibrium is linearly asymptotically stable once** \(\tau\ge-1/\lambda_{\min}(A)\). This proves
\[
\boxed{\tau_c(G)=-1/\lambda_{\min}(A_G).}
\]
In the same linearized dynamics, the slowest relaxation rate for \(\tau<\tau_c(G)\) is \(g_G(\tau)=(1+\tau\lambda_{\min}(A_G))/(1+3\tau)\). Thus the spectral ordering compares relaxation throughout the entire common stable interval, not solely at its endpoint.
For \(\tau<\tau_c\), positive definiteness additionally makes the equilibrium globally attracting among strictly positive states: the Lyapunov function \(V=\sum_i[x_i-x_i^*-x_i^*\log(x_i/x_i^*)]\) satisfies \(\dot V=-(x-x^*)^TB_\tau(x-x^*)<0\) except at equilibrium. Its compact positive sublevel sets ensure convergence.

**2. One explicit edge switch.** The edge lists above have twelve edges, all degrees three, and are connected. Direct counting gives no triangles in \(W\) and exactly one triangle \(012\) in \(H\). In a cubic graph on \(n\) vertices, each triangle contributes three units to \(\sum_i T_i\); hence \(C(G)=T(G)/n\). The exact characteristic polynomials are
\[
\begin{aligned}
\chi_W(z)&=(z-3)(z-1)^2(z+1)(z^2+2z-1)^2,\\
\chi_H(z)&=z(z-3)(z^2+z-4)(z^2+z-1)^2.
\end{aligned}
\]
Their least roots are respectively \(-1-\sqrt2\) and \(-(1+\sqrt{17})/2\). In particular \(\sqrt{17}>1+2\sqrt2\), because after squaring positive quantities this reduces to \(2>\sqrt2\). Substitution into the dynamical reduction proves the asserted strict reversal.

**3. Sharpness and uniqueness at the first order.** A simple cubic graph has even order at least four. Exhaustive degree-constrained enumeration gives exactly one connected isomorphism class at order four, two at order six, and five at order eight. The six-vertex classes are the triangular prism (two triangles, threshold \(1/2\)) and \(K_{3,3}\) (no triangles, threshold \(1/3\)); there is no inversion. At eight vertices the complete, exact class table is:

| Triangles \(T\) | Number of labeled graphs in class | Stable-coexistence threshold |
| ---: | ---: | ---: |
| \(4\) | \(2520\) | \(1/\sqrt5\) |
| \(2\) | \(10080\) | \(\sqrt2-1\) |
| \(1\) | \(3360\) | \(2/(1+\sqrt{17})\) |
| \(0\), Wagner | \(2520\) | \(\sqrt2-1\) |
| \(0\), cube | \(840\) | \(1/3\) |

These are all classes because the labeled orbit sizes sum to \(19320\), the number of connected cubic graphs on eight labeled vertices; the generating recursion enumerates all \(19355\) labeled cubic graphs, of which \(35\) are disconnected. The exact characteristic polynomial of each class (including the lower orders) is in `classification.json`; `verify.py` regenerates **all** labeled graphs, checks that the five relabeling orbits are disjoint and exhaustive, verifies the characteristic polynomials by integer Newton identities, verifies the one-edge-switch construction, and compares certified rational intervals for the algebraic thresholds. Inspection of the complete table shows precisely one strict inversion across distinct triangle counts: the one-triangle class against the Wagner class. The smaller orders have none. Thus eight is sharp, and the claimed class pair is unique.

## Verification
Run `python3 verify.py` from the directory containing `verify.py` and `classification.json`. It uses only the Python standard library. It checks totals \(1,70,19355\) for all labeled cubic graphs on \(4,6,8\) vertices; connected totals \(1,70,19320\); disjoint class orbit cover with counts \(1\), \(60,10\), and \(2520,10080,3360,2520,840\); exact integer characteristic coefficients for all eight representatives; and the explicit swap, spectra, rational root bounds and uniqueness of inversion. The integer characteristic polynomials are computed independently from the expected coefficients; no floating-point eigenvalue experiment is used in the certification.

## Relationship to prior work
Mooij et al., arXiv:2603.17584, analyze exactly this equal-competition network model and prove universal bounds on coexistence thresholds, while finding a **positive statistical association** of clustering with robustness in degree-preserving rewiring experiments. Their reported association is not a universal monotonicity theorem; the present theorem identifies the first finite connected cubic case where a strict inverse change is possible, including a single explicit rewire. The classification of five connected eight-vertex cubic graph types and the spectrum of the Wagner graph are prior graph-theoretic facts. The result claimed here is the **combined sharp ecological threshold comparison and explicit one-swap inversion**, not discovery of the graph types or a new general spectral identity. Almaraz et al. treat general Lotka–Volterra global-attractor stability and invasion graphs but do not provide this clustering/threshold ordering.

## Limitations
This is a complete result for connected simple **cubic** networks only; it does not assert minimality among graphs with varying degrees, directed or weighted networks, or other Lotka–Volterra interactions. It does not contradict a positive **average** correlation between clustering and coexistence robustness in larger random networks. The threshold concerns the existence of a linearly asymptotically stable strictly positive equilibrium; at and above it, boundary equilibria and nonlinear behavior are not classified. Known small-graph spectra are used as independently recomputed mathematical data. No independent external scientific audit is claimed.

## References
1. M. N. Mooij, M. Baudena, A. S. von der Heydt, L. Miele, I. Kryven, *A dynamic mechanism for prevalence of triangles in competitive networks*, arXiv:2603.17584 (initial public version 18 March 2026), especially equation (1), Section 2, Methods; https://arxiv.org/html/2603.17584v2 .
2. P. Almaraz, P. Kalita, J. A. Langa, F. Soler–Toscano, *Structural stability of invasion graphs for Lotka–Volterra systems*, Journal of Mathematical Biology **88** (2024), article 64, https://doi.org/10.1007/s00285-024-02087-8 .
3. *Table of simple cubic graphs*, https://en.wikipedia.org/wiki/Table_of_simple_cubic_graphs (known small-graph enumeration; independently reconstructed in the accompanying certificate).
4. *Wagner graph*, https://en.wikipedia.org/wiki/Wagner_graph (known graph and spectral nomenclature; the characteristic polynomial is also independently reconstructed).
