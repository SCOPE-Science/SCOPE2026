# Incidence conservation and half-factor classification of two-cycles in line-graph majority dynamics

## Finding

Let \(G=(V,E)\) be any finite undirected simple graph such that the degrees at the two ends of every edge have the **same parity**. Give each edge of \(G\) a binary state and update all states synchronously by strict majority among the other edges sharing an endpoint, retaining the old state on a tie. Equivalently, perform binary majority dynamics on the line graph \(L(G)\).

For every state \(x\) satisfying \(F^2(x)=x\), the number of state-one edges incident to **each** vertex of \(G\) is the same in \(x\) and \(F(x)\). Every edge that oscillates belongs to an Eulerian subgraph of \(G\), and **no bridge of \(G\) oscillates**.

More precisely, write \(d_v=\deg_G(v)\), \(h_v=\sum_{e\ni v}x_e\), and, for \(e=uv\), \(r_{uv}=(d_u+d_v)/2\). For each integer vector \(h=(h_v)\) with \(0\le h_v\le d_v\), define the disjoint edge sets
\[
P_h=\{uv\in E:h_u+h_v>r_{uv}\},\quad
Z_h=\{uv\in E:h_u+h_v=r_{uv}\},\quad
N_h=\{uv\in E:h_u+h_v<r_{uv}\}.
\]
The complete recurrent-state classification is as follows: a configuration is recurrent precisely when its incident-count vector is some \(h\), all edges of \(P_h\) have state one, all edges of \(N_h\) have state zero, and its state-one edges inside \(Z_h\) form a **half-factor** of \(Z_h\), meaning that exactly \(\deg_{Z_h}(v)/2\) of these edges meet each vertex \(v\). The vector must consequently satisfy
\[
h_v=\deg_{P_h}(v)+\frac12\deg_{Z_h}(v)\qquad(v\in V).
\]
For such a state, \(F\) fixes all edges outside \(Z_h\) and complements every edge inside \(Z_h\). It is a fixed point if \(Z_h=\varnothing\), and otherwise belongs to a primitive two-cycle.

There is therefore an exact finite combinatorial orbit-count formula for every graph in this class. Define
\[
H(Z)=[\prod_{v\in V}z_v^{\deg_Z(v)/2}]\prod_{uv\in Z}(1+z_u z_v),
\]
with \(H(Z)=0\) when some \(\deg_Z(v)\) is odd. If \(\mathcal A\) denotes the set of integer vectors \(h\) satisfying the displayed incident-count equation, the numbers of fixed states and primitive two-cycle orbits are exactly
\[
Q_1=\#\{h\in\mathcal A:Z_h=\varnothing\},\qquad
Q_2=\frac12\sum_{\substack{h\in\mathcal A\\Z_h\ne\varnothing}}H(Z_h).
\]
These statements apply, in particular, to the line graph of **every finite regular graph**, without a bound on graph order, and to nonregular graphs of locally equal degree parity. The parity hypothesis is sharp for the asserted incidence conservation: on \(G=P_3\), the two states of the primitive two-cycle on \(L(G)=K_2\) exchange unequal original-vertex incidence counts.

## Assumptions and scope

* Graphs are finite, undirected and simple; isolated vertices of \(G\) are allowed, contribute no line-graph sites, and have \(h_v=0\).
* \(L(G)\) has one site per edge of \(G\), with sites adjacent exactly when their original edges share one vertex.
* A site becomes one when strictly more than half its neighbors are one, becomes zero when strictly fewer than half are one, and keeps its state on equality. All sites update simultaneously.
* For every \(uv\in E\), \(d_u\equiv d_v\pmod 2\), so the degree \(d_u+d_v-2\) of the line-graph site \(uv\) is even and \(r_{uv}\) is integral.
* A recurrent state is a state lying on a temporal orbit; the classical finite symmetric-majority period-two theorem implies such an orbit has least period one or two. The proof below independently characterizes all solutions of \(F^2(x)=x\) without using that theorem.

## Proof

**Single-step formula.** For \(e=uv\), the number of state-one line-graph neighbors is exactly \(h_u+h_v-2x_e\), and its total number of line-graph neighbors is \(d_u+d_v-2=2(r_{uv}-1)\). Strict majority with retention gives, for an **arbitrary** state \(x\),
\[
F(x)_{uv}=\begin{cases}
1,&h_u+h_v>r_{uv},\\
0,&h_u+h_v<r_{uv},\\
1-x_{uv},&h_u+h_v=r_{uv}.
\end{cases}
\tag{1}
\]
At the boundary value an edge flips in either direction; above and below it is forced to one or zero, respectively.

**Conservation on two-cycles.** Suppose \(y=F(x)\) and \(x=F(y)\), and let \(\delta_e=y_e-x_e\in\{-1,0,1\}\) and \(\Delta_v=\sum_{e\ni v}\delta_e=h_v(y)-h_v(x)\). If \(\delta_{uv}=1\), then the zero-to-one update from \(x\) requires \(h_u(x)+h_v(x)\ge r_{uv}\), while the one-to-zero update from \(y\) requires \(h_u(y)+h_v(y)\le r_{uv}\). Hence \(\Delta_u+\Delta_v\le0\). If \(\delta_{uv}=-1\), the reverse inequalities give \(\Delta_u+\Delta_v\ge0\). Therefore every edge satisfies \(\delta_{uv}(\Delta_u+\Delta_v)\le0\). But
\[
0\ge\sum_{uv\in E}\delta_{uv}(\Delta_u+\Delta_v)
=\sum_{v\in V}\Delta_v\sum_{e\ni v}\delta_e
=\sum_{v\in V}\Delta_v^2\ge0.
\]
Every \(\Delta_v\) is therefore zero. This establishes incidence conservation without invoking experiments or a large-state-space argument.

**Necessity of the half-factor.** The vectors \(h(x)\) and \(h(y)\) now coincide. Applying (1) at both times shows that an edge of \(P_h\) is one in both states, an edge of \(N_h\) is zero in both, and an edge of \(Z_h\) flips. At each \(v\), the incident one-count within \(Z_h\) is the same at the two times, while every boundary bit complements. It must therefore equal exactly half the degree in \(Z_h\). The displayed equation for \(h_v\) follows. In particular, every degree of \(Z_h\) is even.

**Sufficiency.** Conversely, take any integer vector \(h\) satisfying the incident-count equation and any half-factor \(S\subseteq Z_h\). Define \(x_e=1\) exactly on \(P_h\cup S\). Its incident-one counts are \(h\). Equation (1) takes it to \(y\), where the one edges are precisely \(P_h\cup(Z_h\setminus S)\). Because \(S\) and its complement have equal degree at every original vertex, \(h(y)=h(x)=h\). Applying (1) again returns \(x\). If \(Z_h\) is nonempty, all its edges flip and \(x\ne y\); otherwise \(x=y\).

**Counting and bridges.** Each subset \(S\subseteq Z_h\) contributing the prescribed degrees appears once in the coefficient \(H(Z_h)\). Since \(h\) is uniquely recovered from each state, there is no duplication between vectors. For nonempty \(Z_h\), each primitive orbit contains exactly two such states, yielding the factor \(1/2\) in \(Q_2\). Every component of the even-degree graph \(Z_h\) is Eulerian; every edge of an Eulerian graph lies on a cycle. Consequently no bridge of \(G\) can oscillate. In particular, every trajectory on \(L(G)\) converges to a fixed point whenever \(G\) is a forest satisfying the degree-parity hypothesis, by the classical period-two property.

**Sharpness and a boundary example.** On the three-vertex path \(G=P_3\), adjacent original degrees have different parity; the line graph is \(K_2\) and configurations \((0,1)\) and \((1,0)\) exchange every update, changing leaf-incidence counts. As a distinct illustration, let \(G\) consist of two triangles sharing only a vertex \(c\), with outer vertices \(a,b\) and \(d,e\). The state-one edges \(\{ca,cb,de\}\) have incident counts two at \(c\) and one at every outer vertex. Every edge lies in \(Z_h\), and the update complements all six edges, giving a primitive two-cycle even though \(G\) has no even simple cycle. This shows why the oscillating subgraph must be allowed to be Eulerian rather than merely a union of even cycles.

## Verification

The proof is an all-finite-graph argument. Reproducible standalone finite checks serve only as checks of the definitions, boundary cases, and implementation. From a directory containing the attached files, run:

```sh
python3 verify.py
c++ -O2 -std=c++17 -Wall -Wextra -pedantic check.cpp -o check
./check
```

The Python checker exhausts all \(1{,}099\) simple labelled base graphs on at most five vertices, among them \(154\) satisfying the degree-parity hypothesis. It independently compares the combinatorial criterion to two direct updates on all \(4{,}909\) eligible binary edge configurations. The C++ checker exhausts line-graph configurations on \(K_3,\ldots,K_7\), the three-cube, the Petersen graph and the two-triangle graph, including all \(2{,}097{,}152\) states on \(L(K_7)\). Both separately verify the parity counterexample on \(P_3\). Reproduced standard outputs are in `verify_output.txt` and `check_output.txt`. No finite enumeration is used to infer the theorem for untested graph sizes.

## Relationship to prior work

Goles and Olivos (1980) established the eventual period-one-or-two property for finite symmetric threshold dynamics. Benjamini, Chan, O'Donnell, Tamuz and Tan (first public preprint May 11, 2014) state the finite-graph theorem explicitly and analyze period-two behavior, unanimity and disagreement in broad random and unimodular graph settings. Their manuscript's introduction and relevant main statements do not give incidence conservation or a half-factor recurrent-state classification specifically for line graphs. This finding strengthens the period-two statement **only for the specified line-graph and parity-homogeneous family**: it identifies the edge-flip support and gives an exact orbit-count reduction to half-factors.

Other studied finite graph dynamics such as binary neighbor-XOR on line graphs use a different linear rule and do not imply the nonlinear majority classification. The half-factor coefficient is a standard enumerative construction applied to the newly identified recurrent-state decomposition, not a claim to have invented factor enumeration. Literature and research-record searches found no equivalent statement; this is an evidence-limited originality assessment rather than a proof of global novelty.

## Limitations

The theorem does not give a polynomial-time algorithm for evaluating the half-factor coefficients, a sharp transient bound, or attraction-basin counts for arbitrary graphs. It does not assert incidence conservation when opposite ends of an original edge have different degree parities. The original 1980 article could not be inspected in full through the available authorized access; an equivalent older specialization under different terminology remains a residual risk.

## References

1. E. Goles and J. Olivos, *Periodic behaviour of generalized threshold functions*, Discrete Mathematics **30** (1980), 187–189. DOI: `10.1016/0012-365X(80)90121-1`.
2. I. Benjamini, S.-O. Chan, R. O'Donnell, O. Tamuz and L.-Y. Tan, *Convergence, unanimity and disagreement in majority dynamics on unimodular graphs and random graphs*, first public arXiv posting May 11, 2014, `arXiv:1405.2486`, version 1; later published in Stochastic Processes and their Applications **126** (2016), 2719–2733.
3. G. Moran, *On the period-two-property of the majority operator in infinite graphs*, Transactions of the AMS **347** (1995), 1649–1667. DOI: `10.1090/S0002-9947-1995-1297535-1`.
