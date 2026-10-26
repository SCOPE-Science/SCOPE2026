# Exact maximal-transient census for disjunctive dynamics on halved Boolean cubes

## Finding
Let \(n\ge6\). Place one Boolean state at each vertex of \(\{0,1\}^n\), and update synchronously by OR over vertices at Hamming distance exactly two. Every trajectory reaches one of four fixed configurations. Its sharp largest first-entry time is
\[
T_n=\lfloor n/2\rfloor.
\]
Write \(N=2^{n-1}\) and
\[
A_n=\begin{cases}
N,&n\text{ even},\\
N\bigl(2^n-n-\tfrac12\binom n2\bigr),&n\text{ odd}.
\end{cases}
\]
The exact number of *labelled initial configurations* whose first periodic-entry time is \(T_n\) is
\[
\boxed{E_n=2A_n2^N-A_n^2.}
\]
These configurations are characterized geometrically: on at least one of the two Hamming-parity components, the nonempty initial set is either a singleton (even \(n\)) or a nonempty subset of the Hamming neighbors of a single vertex in the opposite parity class (odd \(n\), after antipodal complementation). States on the other component are unrestricted. In particular, \(A_6=32\), \(A_7=7072\), \(A_8=128\), and \(A_9=124160\).

## Assumptions and scope
Vertices are \(v\in\mathbb F_2^n\). Write \(d(v,w)=|v\oplus w|\) for Hamming distance, and set
\[
(Fx)_v=\bigvee_{w:d(v,w)=2}x_w.
\]
The graph is *loopless*: there is no self-input. All vertices update simultaneously. The two components are the even- and odd-weight vertices \(P_0,P_1\), each of cardinality \(N\). A configuration is periodic only if \(F^k(x)=x\) for some \(k\ge1\); its first-entry time \(\tau(x)\) is the least nonnegative \(t\) for which \(F^t(x)\) is periodic. All counts distinguish every cube vertex and every binary labeling. The assertion is for every integer \(n\ge6\), without a finite-size cutoff.

## Proof
**Exact-length reachability.** Regard a vector of weight two as an edge generator in the additive group \(\mathbb F_2^n\). By repeated distributivity of OR, \(F^t(\mathbf1_S)\) is the indicator of the union of endpoints of walks of *exactly* length \(t\) from seeds \(S\). For every \(t\ge2\), such a walk from \(0\) reaches exactly the vectors of even weight at most \(2t\). Necessity follows because each edge changes two bits. For sufficiency, a target of weight \(2r\ge2\) is a sum of \(r\) disjoint weight-two generators. It also has a representation with \(r+1\) generators: for \(r=1\), use a third coordinate and two generators sharing that coordinate; for \(r\ge2\), replace two disjoint pairs on four target coordinates by three pairs sharing one target coordinate. Appending a generator twice increases any representation length by two. For weight zero, a repeated generator gives length two and the three edges of a coordinate triangle give length three; adding repeated generators supplies every length at least two. These constructions establish the exact reachability statement for all relevant \(n\ge6\).

**Fixed points and the cutoff.** Each parity component is connected (every even difference is a sum of weight-two vectors). If a nonempty set \(S\) has \(F(\mathbf1_S)=\mathbf1_S\), then its neighbors are contained in \(S\); connectedness forces \(S\) to be the whole component. The empty set is also fixed, giving exactly four fixed configurations. At \(t=T_n\), every parity-compatible difference has weight at most \(2T_n\), so every occupied parity component has become completely filled, and every trajectory is fixed. A single seed fails to fill its component at \(t=T_n-1\), since an even-parity vertex at maximum compatible Hamming distance \(2T_n\) remains unreachable. Thus the cutoff is sharp.

**Last missing vertex criterion.** Since \(T_n-1\ge2\), the reachability statement shows that a nonempty seed set \(S\subseteq P_\eta\) has not filled its component at time \(T_n-1\) if and only if there is \(v\in P_\eta\) with \(d(v,w)=2T_n\) for every \(w\in S\). For even \(n\), the farthest compatible vertex from \(v\) is its unique bitwise complement; consequently \(S\) must be a singleton. There are \(A_n=N\) such nonempty support sets on each parity component.

For odd \(n\), the farthest shell from \(v\) consists of the \(n\) ordinary Hamming neighbors of its bitwise complement. There are \(N\) possible centers of opposite parity. Exactly \(N\) singleton support sets qualify. Qualifying pairs are precisely pairs of vertices at Hamming distance two; each such pair has two common Hamming neighbors, so there are \(N\binom n2/2\) qualifying pairs. Every subset of size at least three of an ordinary Hamming-neighborhood has a *unique* center: three distinct neighbors of a center have no other common Hamming neighbor. The count of these larger subsets is \(N(2^n-1-n-\binom n2)\). Addition gives \(A_n=N(2^n-n-\tfrac12\binom n2)\).

**Both components.** The two parity supports evolve independently. Exactly \(A_n\) nonempty supports on either component have first-entry time \(T_n\). The other component can have any of \(2^N\) supports. Inclusion-exclusion for the union of these two events gives \(E_n=2A_n2^N-A_n^2\). No distinct attractors or nontrivial cycles have been omitted, by the fixed-point and cutoff argument.

## Verification
The accompanying standalone Python program `verify.py` constructs the exact OR update by bit masks; checks the all-length walk-shell identity at computational test dimensions; enumerates the qualifying farthest-shell subsets at odd dimensions seven and nine; tests all sparse one- and two-seed configurations, sampled three-seed configurations, and random configurations; and compares simulated first-entry times with the geometric criterion. The inspected execution reported `VERIFY_OK`, 36 walk-shell checks and 246494 initial-state checks, and reproduced \(A_6=32\), \(A_7=7072\), \(A_8=128\), and \(A_9=124160\). Those finite tests corroborate, but do not replace, the preceding unrestricted proof.

## Relationship to prior work
General conjunctive/disjunctive Boolean-network theory already supplies structural links between graph walks, transient height, and limit cycles. Goles and Hernández (2000) characterize the qualitative basins of OR networks on connected undirected graphs, and Jarrah, Laubenbacher, and Veliz-Cuba (2008) relate network height to the exponent of its dependency graph. Aledo and collaborators (2015) survey this general framework. The known halved-cube graph geometry and these general methods explain why a sharp height computation is accessible. The more specific contribution assessed here is an exact labelled-state **maximal-transient extremizer census** for the distance-two Boolean cube, with an even/odd geometric distinction and closed count \(E_n\); the general sources inspected do not provide that specialized count. A published result on XOR/parity dynamics on the same graph is a different update rule and does not imply this OR census.

## Limitations
No claim is made about every intermediate transient-depth stratum, asynchronous updates, Hamming distance other than two, or noisy networks. The theorem starts at \(n=6\) because the penultimate exact-walk shell needs at least two updates; low dimensions require separate formulas. General walk-connectivity and qualitative attractor facts are not claimed as new. Historical priority of the specialized count requires independent expert review.

## References
1. E. Goles and G. Hernández, *Dynamical behavior of Kauffman networks with AND-OR gates*, Journal of Biological Systems 8 (2000), 151–175. DOI: 10.1142/S0218339000000109.
2. A. S. Jarrah, R. Laubenbacher, and A. Veliz-Cuba, *The Dynamics of Conjunctive and Disjunctive Boolean Networks*, first posted 2008-05-02, arXiv:0805.0275, https://arxiv.org/abs/0805.0275.
3. J. A. Aledo et al., *Parallel Dynamical Systems over Graphs and Related Topics: A Survey*, Journal of Applied Mathematics (2015), article 594294, DOI: 10.1155/2015/594294.
4. *Halved Cube Graph*, MathWorld, https://mathworld.wolfram.com/HalvedCubeGraph.html (graph terminology; not used for novelty claims).
