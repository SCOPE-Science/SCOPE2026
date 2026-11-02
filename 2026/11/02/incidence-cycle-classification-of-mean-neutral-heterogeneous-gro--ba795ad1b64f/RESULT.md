# Incidence-cycle classification of mean-neutral heterogeneous group influence

## Finding

In the edge-dependent-contribution Friedkin–Johnsen opinion model on an arbitrary finite weighted hypergraph, heterogeneous group influence can preserve the **total equilibrium expressed opinion for every innate-opinion vector** precisely when its deviation from uniform group contributions is a circulation on the vertex–hyperedge incidence graph. The real dimension of all such mean-neutral contribution perturbations equals that graph's cycle rank,
\[
\dim\mathcal C=|\mathcal I|-|V|-|E|+b_0(B),
\]
where \(\mathcal I=\{(e,v):v\in e\}\), \(B\) is the bipartite incidence graph, and \(b_0(B)\) counts connected components, including isolated vertices. In particular, an incidence forest forces uniform contribution shares whenever conservation is required for every innate-opinion vector; conversely, any incidence cycle supports a nonuniform, strictly positive, mean-neutral family. On an individual incidence cycle, its admissible amplitude has an explicit sharp cutoff.

Although every mean-neutral model has equilibrium polarization no greater than initial polarization, its polarization can be either larger or smaller than that of the **uniform-contribution model on the same hyperedges**. This occurs already on four vertices with two overlapping three-person groups; that motif is the smallest possible for distinct three-uniform hyperedges.

## Assumptions and scope

Let \(H=(V,E,h)\) be any finite simple hypergraph. Every edge \(e\) has cardinality \(k_e\ge2\) and a positive weight \(h_e\). Each incident vertex \(v\in e\) has a strictly positive contribution share \(\gamma_e(v)\), with \(\sum_{v\in e}\gamma_e(v)=1\). Isolated vertices are permitted. Vertices and edges are labeled; parallel duplicate hyperedges are not assumed. All claims hold for every such hypergraph, every admissible role vector, and every innate opinion vector \(x\in[0,1]^V\).

Use the directed hypergraph projection of Xu and Zhang: for distinct vertices \(u,v\),
\[
 w_{uv}=\sum_{e\ni u,v}\frac{2h_e}{k_e-1}\gamma_e(v),\qquad
 L_{uv}=-w_{uv},\qquad L_{uu}=\sum_{v\ne u}w_{uv}.
\]
The equilibrium expressed opinions are \(z=(I+L)^{-1}x\). Define \(S(x)=\sum_{v\in V}x_v\), the total-opinion preservation property \(S(z)=S(x)\) **for all** \(x\in[0,1]^V\), and polarization \(P(y)=\sum_{v\in V}(y_v-S(y)/|V|)^2\). The theorem concerns the equilibrium operator, not conservation at every transient synchronous update.

Set \(c_e=2h_e/(k_e-1)\) and \(q_{ev}=c_e(k_e\gamma_e(v)-1)\) for each incidence \((e,v)\in\mathcal I\). Let \(\mathcal C\subset\mathbb R^{\mathcal I}\) be the space defined by
\[
\sum_{v\in e}q_{ev}=0\quad(e\in E),\qquad
\sum_{e\ni v}q_{ev}=0\quad(v\in V).
\]

## Proof

**Existence and positivity of the equilibrium.** Writing \(D=\operatorname{diag}(1+\sum_{v\ne u}w_{uv})\) and \(W=(w_{uv})\), we have \(I+L=D-W\). The matrix \(D^{-1}W\) is nonnegative with every row sum less than one; hence its spectral radius is less than one and
\[
(I+L)^{-1}=\sum_{j=0}^{\infty}(D^{-1}W)^jD^{-1}\ge0.
\]
Moreover \(L\mathbf1=0\), so \(\Omega=(I+L)^{-1}\) satisfies \(\Omega\mathbf1=\mathbf1\).

**Exact conservation criterion.** Preservation for all \(x\in[0,1]^V\) is equivalent, by testing the standard basis vectors, to \(\mathbf1^\top\Omega=\mathbf1^\top\). Right-multiplication by \(I+L\) shows that this is equivalent to \(\mathbf1^\top L=0\). For every vertex \(v\), the contribution of hyperedge \(e\ni v\) to its outgoing projected weight is \(c_e(1-\gamma_e(v))\), whereas its contribution to incoming weight is \(c_e(k_e-1)\gamma_e(v)\). Thus
\[
\sum_{u\in V}L_{uv}=\sum_{e\ni v}c_e(1-k_e\gamma_e(v))=-\sum_{e\ni v}q_{ev}.
\]
The per-edge normalization independently gives \(\sum_{v\in e}q_{ev}=0\). Therefore total equilibrium opinion is conserved for every \(x\) if and only if \(q\in\mathcal C\). Conversely any \(q\in\mathcal C\) satisfying \(q_{ev}>-c_e\) determines a unique strictly positive normalized contribution assignment
\[
\gamma_e(v)=\frac{1+q_{ev}/c_e}{k_e}.
\]
This is an exact correspondence, not a first-order approximation.

**Cycle rank and sharp existence boundary.** Orient each edge of the bipartite graph \(B\) from its hyperedge-node to its vertex-node. Its signed incidence matrix has one column per \((e,v)\in\mathcal I\); its nullspace is exactly \(\mathcal C\) (reversing the signs of all hyperedge-node equations has no effect). In a finite graph with \(N\) nodes and \(b_0\) components, the oriented incidence matrix has rank \(N-b_0\): a spanning forest supplies \(N-b_0\) independent columns, and the all-ones relation on each component bounds the row rank. Here \(N=|V|+|E|\). The rank–nullity formula yields the stated dimension.

If \(B\) is a forest, its circulation space is zero; hence every conservative role assignment is uniform within every hyperedge. If \(B\) contains a simple cycle, put alternating \(+s\) and \(-s\) on the incidence edges of that cycle and zero elsewhere. Every vertex-node and edge-node receives one positive and one negative value, so the resulting \(q\) is a nonzero circulation. It is strictly feasible exactly when
\[
|s|<\min_{e\text{ on the cycle}}c_e,
\]
because each hyperedge-node on the cycle carries both signs and every role share must remain positive. This interval is sharp along the specified cycle direction: at its endpoints a role share becomes zero. All other independent cycle modes likewise remain feasible at sufficiently small amplitudes. The set of conservative role assignments is consequently a relatively open convex polytope of the stated dimension.

**Polarization.** If \(q\in\mathcal C\), \(\Omega\) is both row and column stochastic. Jensen's inequality, applied to the nonnegative rows of \(\Omega\), gives \(\sum_v(\Omega x)_v^2\le\sum_v x_v^2\). The means coincide, hence \(P(\Omega x)\le P(x)\). If the hypergraph's incidence graph is connected, \(\Omega\) is strictly positive, giving strict inequality whenever \(x\) is nonconstant. More generally equality holds precisely when \(x\) is constant on every connected component of \(B\) containing vertices; isolated vertices count as singleton components.

**First three-uniform overlap and a genuine sign reversal.** Let \(V=\{1,2,3,4\}\), \(e=\{1,2,3\}\), \(f=\{2,3,4\}\), and \(h_e=h_f=1\). For \(-1/3<d<1/3\), assign the shares, in their vertex orders,
\[
\gamma_e=(1/3,1/3+d,1/3-d),\qquad
\gamma_f=(1/3-d,1/3+d,1/3).
\]
These give \(q_{e,2}=3d=-q_{f,2}\), \(q_{e,3}=-3d=-q_{f,3}\), and all other deviations zero, so they are mean-neutral despite the projected influence being asymmetric when \(d\ne0\). Direct inversion gives
\[
\Omega_d=\begin{pmatrix}
23/35&1/7+d/5&1/7-d/5&2/35\\
1/7&11/21&4/21&1/7\\
1/7&4/21&11/21&1/7\\
2/35&1/7-d/5&1/7+d/5&23/35
\end{pmatrix}.
\]
For the two admissible innate profiles \(x^+=(1,1,0,0)^\top\) and \(x^-=(1,0,1,0)^\top\), exact simplification gives
\[
P(\Omega_d x^+)=\frac{18d^2+54d+53}{225},\qquad
P(\Omega_d x^-)=\frac{18d^2-54d+53}{225}.
\]
At \(d=0\) both polarizations equal \(53/225\). At \(d=1/6\) they are respectively \(5/18\) (larger) and \(89/450\) (smaller). Their total equilibrium opinion is still exactly two. Distinct three-person edges on at most three vertices allow at most one edge, so their incidence graph has no cycle; this four-vertex motif is the smallest possible with nonuniform mean-neutral roles among distinct three-uniform hyperedges.

## Verification

Run `python verify.py` with SymPy 1.12 or later. The script computes the four-vertex resolvent and both polarization formulas symbolically. It also verifies rank–nullity, the exact vertex-balance identities, and equivalence of column stochasticity and incidence circulation in 175 pseudorandom rational hypergraphs with three through seven vertices. The exact fractions and symbolic identities are checked by assertions. The all-size theorem follows from the proof above; the finite tests are not substitutes for it.

## Relationship to prior work

Xu and Zhang, *Linear Opinion Dynamics Model with Higher-Order Interactions* (arXiv:2310.05689, initial public version October 9, 2023), define exactly the directed projection used here in Eq. (4) and the equilibrium resolvent in Eq. (2). Their Section V observes that symmetric projections preserve the sum of innate opinions while asymmetric ones can change it, and reports an increase in polarization in a particular multilayer example. They do not state the converse conservation classification for heterogeneous shares, the incidence-cycle parameter-space dimension, the sharp cycle amplitudes, or the two-sided polarization response under mean neutrality.

Chitra and Raphael, *Random Walks on Hypergraphs with Edge-Dependent Vertex Weights* (ICML 2019; arXiv:1905.08287), study random-walk transition matrices, reversibility and stationary distributions. Their results concern a different normalization and do not state the classification for the Friedkin–Johnsen equilibrium resolvent. The oriented-incidence rank formula and doubly stochastic contraction are classical ingredients; neither is claimed as new in isolation. The contribution is the exact model-specific correspondence and its smallest-motif polarization consequences.

## Limitations

Total-opinion preservation is asserted for every innate vector at **equilibrium**, not at intermediate updates and not for a particular vector alone. The strict-contraction claim is relative to innate polarization, not to the polarization under the uniform-role comparison model; the example shows either relative direction is possible. Contributions are positive, edges are nonempty with size at least two, and the projection and unit innate-opinion weight are fixed as stated. No claim is made for nonlinear group updates, time-varying weights, other projection normalizations, empirical behavior, or independent validation. An equivalent specialized characterization may exist in literature outside the inspected primary sources.

## References

1. W. Xu and Z. Zhang, *Linear Opinion Dynamics Model with Higher-Order Interactions*, arXiv:2310.05689 (first posted October 9, 2023). https://arxiv.org/html/2310.05689
2. U. Chitra and B. J. Raphael, *Random Walks on Hypergraphs with Edge-Dependent Vertex Weights*, Proceedings of Machine Learning Research 97, 1172–1181 (2019), arXiv:1905.08287. https://proceedings.mlr.press/v97/chitra19a.html
3. L. Neuhäuser, A. Mellor and R. Lambiotte, *Multibody interactions and nonlinear consensus dynamics on networked systems*, Physical Review E 101, 032310 (2020). https://doi.org/10.1103/PhysRevE.101.032310
