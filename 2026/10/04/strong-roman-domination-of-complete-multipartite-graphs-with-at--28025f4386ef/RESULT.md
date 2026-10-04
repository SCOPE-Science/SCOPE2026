# Strong Roman domination of complete multipartite graphs with at least three parts
## Finding
Let \(G=K_{n_1,\ldots,n_r}\) be a finite connected complete multipartite graph with \(r\ge3\). Write \(N=\sum_{i=1}^r n_i\) and \(m=\min_i n_i\). Then
\[
\gamma_{\mathrm{StR}}(G)=\left\lceil\frac{N+m}{2}\right\rceil.
\]
Since \(\Delta(G)=N-m\), this says that every complete multipartite graph with at least three nonempty parts attains the general bound
\[
\gamma_{\mathrm{StR}}(G)\le N-\left\lfloor\frac{\Delta(G)}2\right\rfloor.
\]
A minimum function is explicit: choose a smallest part \(V_1\), give one vertex of \(V_1\) label \(1+\lceil(N-m)/2\rceil\), give the other \(m-1\) vertices of \(V_1\) label \(1\), and give every vertex outside \(V_1\) label \(0\).

## Assumptions and scope
A strong Roman dominating function on a graph of maximum degree \(\Delta\) is a map
\[
f:V(G)\to\{0,1,\ldots,1+\lceil\Delta/2\rceil\}
\]
such that every vertex labeled \(0\) has a neighbor \(w\) satisfying
\[
f(w)\ge 1+\left\lceil\frac{|N(w)\cap B_0|}{2}\right\rceil,
\qquad B_0=\{v:f(v)=0\}.
\]
The theorem assumes \(r\ge3\) and all part sizes are positive. The bipartite case is deliberately excluded because the lower-bound argument has a genuine two-part boundary: two zero-containing defender parts can exhaust the graph.

## Proof
Let \(z_i=|B_0\cap V_i|\) and \(z=|B_0|\). Every positively labeled vertex contributes a baseline of at least \(1\). If a positive vertex \(u\in V_j\) serves as a defender, then its zero neighbors are exactly the zeros outside \(V_j\), so its excess above the baseline satisfies
\[
f(u)-1\ge\left\lceil\frac{z-z_j}{2}\right\rceil.
\]

For the upper bound, choose a smallest part \(V_1\) of size \(m\). Label one vertex by \(1+\lceil(N-m)/2\rceil\), the other vertices of \(V_1\) by \(1\), and every vertex outside \(V_1\) by \(0\). The distinguished vertex is adjacent to all \(N-m\) zeros, so this is a strong Roman dominating function of weight
\[
m+\left\lceil\frac{N-m}{2}\right\rceil
=\left\lceil\frac{N+m}{2}\right\rceil.
\]

For the lower bound, consider any strong Roman dominating function. If \(z=0\), its weight is at least \(N\), so the desired inequality is immediate. Assume \(z>0\).

First suppose some defender lies in a zero-free part \(V_j\), so \(z_j=0\). There are \(N-z\) positive vertices and hence \(N-z\ge n_j\ge m\), while that defender needs excess at least \(\lceil z/2\rceil\). Therefore
\[
w(f)\ge N-z+\left\lceil\frac z2\right\rceil
=N-\left\lfloor\frac z2\right\rfloor
\ge N-\left\lfloor\frac{N-m}{2}\right\rfloor
=\left\lceil\frac{N+m}{2}\right\rceil.
\]

It remains to suppose that every defender lies in a part containing at least one zero. Choose a zero-containing part. A zero there needs a defender in a different part, say \(V_a\). Since \(V_a\) also contains a zero, that zero needs a defender in a second part \(V_b\ne V_a\). Thus two distinct defender parts exist, and each contains both a defender and at least one zero. Their two defenders contribute excess at least
\[
\left\lceil\frac{z-z_a}{2}\right\rceil+
\left\lceil\frac{z-z_b}{2}\right\rceil.
\]
Consequently
\[
w(f)\ge N-z+\frac{2z-z_a-z_b}{2}
=N-\frac{z_a+z_b}{2}.
\]
Because each of \(V_a,V_b\) contains a positive defender, \(z_a\le n_a-1\) and \(z_b\le n_b-1\). Since \(r\ge3\), at least one further part has size at least \(m\), so \(n_a+n_b\le N-m\). Hence
\[
z_a+z_b\le N-m-2,
\]
and therefore
\[
w(f)\ge\frac{N+m+2}{2}.
\]
As \(w(f)\) is an integer, this is strictly stronger than the required lower bound. Combining the two cases with the explicit construction proves the formula.

## Verification
The accompanying verifier enumerates every nondecreasing complete-multipartite part profile with at least three parts and total order at most \(10\). For each profile it enumerates every allowed labeling whose weight is at most the claimed optimum, checks the defining strong Roman condition directly, confirms that no smaller feasible weight exists, and checks the explicit smallest-part construction. The replay result is recorded in `VERIFICATION.md`.

The finite computation is a regression check, not the proof of the infinite theorem. The proof above supplies the universal lower and upper bounds.

## Relationship to prior work
The foundational strong Roman domination paper introduced the invariant and proved the general upper bound
\[
\gamma_{\mathrm{StR}}(G)\le N-\left\lfloor\frac{\Delta(G)}2\right\rfloor.
\]
Its searchable full text does not state a complete-multipartite theorem. The result here identifies an infinite natural class, with at least three parts of arbitrary sizes, on which that bound is always exact.

Total strong Roman domination is a distinct refinement: it additionally requires the positive-labeled vertices to induce a graph without isolated vertices. Results for total strong Roman domination on complete multipartite graphs therefore do not imply the ordinary strong Roman formula proved here. Later \(k\)-strong Roman work gives exact values for complete bipartite graphs for its own parameter and is relevant to the two-part boundary, but it does not cover the stated \(r\ge3\) theorem for the original invariant.

## Limitations
The theorem does not assert the corresponding formula for \(r=2\). That case has a different optimization because two zero-containing defender parts can cover all parts, invalidating the strict third-part estimate used above. The computational check only covers order at most \(10\), and no claim of exhaustive literature uniqueness is made beyond the inspected sources and searches.

## References
1. M. P. Alvarez-Ruiz, I. Gonzalez Yero, T. Mediavilla-Gradolph, S. M. Sheikholeslami, and J. C. Valenzuela, “On the Strong Roman Domination Number of Graphs,” arXiv:1502.03933; later Discrete Applied Mathematics 231 (2017), 44–59, DOI:10.1016/j.dam.2016.12.013.
2. S. Nazari-Moghaddam, M. Soroudi, S. M. Sheikholeslami, and I. G. Yero, “On the total and strong version for Roman dominating functions in graphs,” arXiv:1912.01093.
3. “Theoretical studies of the \(k\)-strong Roman domination problem,” Kuwait Journal of Science 51 (2024), article 100283, DOI:10.1016/j.kjs.2024.100283.
