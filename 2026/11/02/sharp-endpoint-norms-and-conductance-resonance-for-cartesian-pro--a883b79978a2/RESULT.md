# Sharp endpoint norms and conductance resonance for Cartesian products of complete graphs

## Finding

Let \(d\ge1\), let \(q_1,\ldots,q_d\ge2\) be integers, and let \(c_1,\ldots,c_d>0\). Form the Cartesian-product graph
\[
G=K_{q_1}\mathbin{\square}\cdots\mathbin{\square}K_{q_d},
\]
assigning conductance \(c_j\) to every edge in coordinate direction \(j\). Choose any orientation of its edge set, let \(B\) be the edge-by-vertex incidence matrix, let \(C\) be the diagonal matrix of conductances, and put \(L=B^{\mathsf T}CB\). The *symmetric electrical-gradient projection* on real edge coordinates is
\[
\Pi=C^{1/2}BL^+B^{\mathsf T}C^{1/2},
\]
where \(L^+\) is the Moore--Penrose inverse. It is the Euclidean orthogonal projection onto \(\operatorname{ran}(C^{1/2}B)\), but its operator norm below uses the coordinate maximum norm.

**Theorem (all alphabet sizes and axis conductances).** Its sharp, attained endpoint norm is
\[
\boxed{\displaystyle
\|\Pi\|_{\ell^\infty(E)\to\ell^\infty(E)}
=\max_{1\le i\le d}\left\{
2\left(1-\frac1{q_i}\right)
+2\sum_{j\ne i}\frac{(q_j-1)\sqrt{c_i c_j}}{q_i c_i+q_j c_j}
\right\}.}
\]
For any prescribed coordinate direction \(i\), every corresponding edge gives exactly the displayed \(i\)-th absolute row sum. A sign vector on the edge set attains the norm.

There is also an **exact conductance-optimization and rigidity theorem**. With
\(q_*:=\min_j q_j\),
\[
\boxed{\displaystyle
\max_{c_1,\ldots,c_d>0}\|\Pi\|_{\infty\to\infty}
=1-\frac1{q_*}+
\frac1{\sqrt{q_*}}\sum_{j=1}^d\frac{q_j-1}{\sqrt{q_j}}.}
\]
Equality holds **exactly** when \(q_1c_1=\cdots=q_dc_d\), equivalently \(c_j=t/q_j\) for some \(t>0\). This includes the one-factor case, where every positive conductance is of that form.

For uniform axis conductances, the maximizing rows are precisely those belonging to a direction of smallest alphabet size. In particular, for the ordinary \(q\)-ary Hamming graph,
\[
\boxed{\displaystyle
\|\Pi\|_{\infty\to\infty}=\frac{(q-1)(d+1)}q,}
\]
and for the binary \(d\)-cube this is \((d+1)/2\). Thus the sharp maximum-norm projection amplification is logarithmic in the number \(q^d\) of vertices at fixed alphabet size, with its exact coefficient.

## Assumptions and scope

All graphs are finite, real, undirected, simple, and connected. The graph's vertices are vectors \((x_1,\ldots,x_d)\) with \(0\le x_j<q_j\); two vertices are adjacent if exactly one coordinate changes. The conductance is constant along each complete-graph coordinate direction, though it may vary between directions. The norm is the unweighted coordinate \(\ell^\infty\) norm of the **symmetrically rescaled edge variables** to which \(\Pi\) acts. It is not the maximum norm of physical edge currents in unscaled variables for unequal conductances. Reorienting any edge conjugates \(\Pi\) by a diagonal sign matrix and leaves the norm unchanged. The nullspace of \(L\) consists of constants.

## Proof

### 1. Reduction to one edge and a strictly monotone resolvent kernel

Write \(L_j\) for the ordinary Laplacian of the factor \(K_{q_j}\). The vertex Laplacian decomposes as the tensor sum \(L=\sum_j c_jL_j\), with identities on all other factors. Fix a coordinate \(i\) and an oriented edge whose endpoints agree in every other coordinate. By vertex-relabeling symmetry assume that its endpoints are \((0,0)\) and \((1,0)\), with the first displayed entry representing coordinate \(i\) and the second the remaining coordinate tuple. Let \(b=\delta_{(0,0)}-\delta_{(1,0)}\).

Since \(L_i(\delta_0-\delta_1)=q_i(\delta_0-\delta_1)\), the zero-mean solution \(u=L^+b\) has the exact form
\[
u(x_i,z)=(\mathbf1_{x_i=0}-\mathbf1_{x_i=1})v(z),\qquad
v=(q_ic_i I+L_{-i})^{-1}\delta_0,
\]
where \(L_{-i}=\sum_{j\ne i}c_jL_j\). The inverse exists because \(q_ic_i>0\). For \(j\ne i\), the heat kernel of \(c_jL_j\), started at the distinguished symbol \(0\), is
\[
h_j(t;0,0)=\frac{1+(q_j-1)e^{-q_jc_jt}}{q_j},\qquad
h_j(t;0,a)=\frac{1-e^{-q_jc_jt}}{q_j}\quad(a\ne0).
\]
The resolvent representation therefore gives
\[
v(z)=\int_0^\infty e^{-q_ic_it}
\prod_{j\ne i}h_j(t;0,z_j)\,dt.
\]
Every integrand is nonnegative, so \(v(z)>0\). For any \(j\ne i\), replacing \(z_j=0\) by any nonzero symbol strictly decreases \(v\), because
\[
h_j(t;0,0)-h_j(t;0,a)=e^{-q_jc_jt}>0\quad(t>0).
\]
Replacing one nonzero symbol with another leaves \(v\) unchanged. These sign facts justify all absolute-value evaluations below; no cancellation or heuristic current direction is assumed.

### 2. Absolute transfer-current row sums

For any target oriented edge \(f\) of direction \(j\), the absolute entry in the row of \(\Pi\) corresponding to the fixed edge is
\[
|\Pi_{e f}|=\sqrt{c_i c_j}\,|u(f_+)-u(f_-)|.
\]
The orientation changes only the sign. First sum over edges in direction \(i\), on each fixed other-coordinate fiber \(z\). The potentials in that fiber are \(v(z),-v(z),0,\ldots,0\), and the complete-graph sum of absolute potential differences is exactly \(2(q_i-1)v(z)\). Hence this direction contributes
\[
2(q_i-1)c_i\sum_z v(z)
=2(q_i-1)c_i\int_0^\infty e^{-q_ic_it}\,dt
=2\left(1-\frac1{q_i}\right).
\]
Here \(\sum_z\prod_{j\ne i}h_j(t;0,z_j)=1\) at every time.

Fix \(j\ne i\). Only the two slices \(x_i\in\{0,1\}\) have nonzero potential. Within either slice, an edge of direction \(j\) has nonzero potential difference exactly when one symbol is \(0\) and the other is nonzero. There are \(q_j-1\) such edges per coordinate line, all with the same positive absolute difference. Summing across the other coordinates and both slices gives
\[
\begin{aligned}
\sum_{f:\,\operatorname{dir}(f)=j}|\Pi_{ef}|
&=2(q_j-1)\sqrt{c_i c_j}
\int_0^\infty e^{-q_ic_it}e^{-q_jc_jt}\,dt\\
&=\frac{2(q_j-1)\sqrt{c_ic_j}}{q_ic_i+q_jc_j}.
\end{aligned}
\]
Adding all directions proves the asserted \(i\)-th row formula. Coordinate permutations within each factor act transitively on its edges; thus every row of direction \(i\) has the same absolute sum. The maximum absolute row sum is precisely the induced \(\ell^\infty\) norm of a finite matrix. For an edge realizing this maximum, taking each input edge coordinate equal to the sign of its row entry (arbitrary sign for a zero entry) attains equality.

### 3. Globally optimal conductances and equality cases

Set \(x_i=q_ic_i>0\). By the arithmetic--geometric mean inequality,
\[
\frac{2\sqrt{c_ic_j}}{q_ic_i+q_jc_j}
=\frac1{\sqrt{q_iq_j}}\frac{2\sqrt{x_ix_j}}{x_i+x_j}
\le\frac1{\sqrt{q_iq_j}},
\]
with equality precisely when \(x_i=x_j\). Consequently the \(i\)-th row sum is bounded above by
\[
R_i^*=2\left(1-\frac1{q_i}\right)
+\sum_{j\ne i}\frac{q_j-1}{\sqrt{q_iq_j}}.
\]
All these bounds hold with equality simultaneously when the rates \(q_jc_j\) are equal, so optimizing the maximum row sum amounts to computing \(\max_iR_i^*\).

Let \(S=\sum_j(q_j-1)/\sqrt{q_j}\). An exact rearrangement yields \(R_i^*=1-1/q_i+S/\sqrt{q_i}\). If \(a=q_i<b=q_k\), then
\[
R_i^*-R_k^*
=\left(\frac1{\sqrt a}-\frac1{\sqrt b}\right)
\left(S-\frac1{\sqrt a}-\frac1{\sqrt b}\right)>0,
\]
because the latter parenthesis is at least \((a-2)/\sqrt a+(b-2)/\sqrt b>0\). Hence \(\max_iR_i^*\) occurs exactly at any smallest \(q_i=q_*\), giving the optimization formula. When \(d\ge2\), equality in that formula for any conductance vector forces equality in every positive off-direction AM--GM term of a maximizing row, hence \(q_ic_i=q_jc_j\) for every \(j\). Conversely these equations attain equality. The \(d=1\) case is immediate.

### 4. Uniform conductances and exact direction classification

When all conductances are equal, each direction has row norm
\[
R_i=2\left(1-\frac1{q_i}\right)
+2\sum_{j\ne i}\frac{q_j-1}{q_i+q_j}.
\]
For \(a=q_i<b=q_k\), subtraction gives
\[
R_i-R_k=2(b-a)\left[
\frac1{a+b}-\frac1{ab}
+\sum_{j\notin\{i,k\}}\frac{q_j-1}{(a+q_j)(b+q_j)}\right]>0,
\]
since \(ab-a-b=(a-1)(b-1)-1>0\) when \(2\le a<b\). Thus precisely the smallest-alphabet directions maximize the norm. Taking every \(q_j=q\) yields \((q-1)(d+1)/q\), proving the remaining assertions.

## Verification

The standalone verifier `verification/check_exact.py` constructs a graph from its vertex coordinates, forms the **weighted grounded graph Laplacian**, inverts it by exact rational Gauss--Jordan elimination, reconstructs the edge-transfer matrix, and compares every edge-row absolute sum with the theorem. It does not implement the heat-kernel proof or rely on floating-point tolerances. For the weighted test profiles the axis conductances are integer squares, so the square-root rescaling remains rational. The verifier additionally constructs maximizing edge-sign inputs and checks equality exactly. Executing the bundled verifier passed **24 graph/conductance profiles and 478 exact edge-row comparisons**, including nonuniform alphabets and nonuniform axis conductances.

As illustrative independent values, uniform conductances on \(K_2\square K_3\) give row norms \(9/5\) and \(26/15\) in the two coordinate directions; on \(K_2\square K_3\square K_4\), the three row norms are \(14/5\), \(272/105\), and \(101/42\). These values are direct grounded-Laplacian outputs as well as evaluations of the formula. Exact finite checks corroborate the analytical proof and do not independently certify an infinite family.

## Relationship to prior work

Kelner and Maymounkov's 2009 work develops electrical routing and Laplacian-based operator norm methods on general graphs, but its principal results are routing bounds and an inverse-Laplacian norm estimate, not a sharp Cartesian-product electrical-projection formula. Schild, Rao, and Srivastava (2017) derive general localization bounds and analyze parallel-path, expander, and grid examples; their bounds and examples do not directly determine mixed-alphabet anisotropic products. Gurel-Gurevich, Nachmias, and Sachdeva (2026) prove sharp-order logarithmic general bounds for absolute transfer-current matrices, but do not give the present exact product formula or conductance-optimization equality characterization. The paper texts were searched for the specific Hamming/cube/product instances, and their most relevant definitions, theorems, examples, and proof mechanisms were inspected.

Related exact formulas for a single complete graph, a square, certain parallel-path networks, or certain complete multipartite graphs cover special low-dimensional instances, not arbitrary Cartesian powers of complete graphs with independently variable axis conductances. In particular, the classical \(d=1\) or \(d=2,\,q_1=q_2=2\) cases alone are **not** asserted to be novel. The additional fixed-conductance and optimal-conductance formulas for the entire product family, together with rigidity, are the substantive claim. A mathematically equivalent calculation could still occur in unlocated older circuit-theoretic or product-graph literature; nonappearance in searches is not proof of unique priority.

## Limitations

The theorem concerns real finite-dimensional edge coordinates and conductances constant on each complete-graph coordinate direction. It does not cover arbitrary conductance values on individual edges, Cartesian products of noncomplete factors, or physical-current \(\ell^\infty\) norms without the specified symmetric square-root scaling. The explicit sign extremizer depends on the selected projection row. General routing competitive ratios and asymptotic constants for unrelated graphs are not determined. Independent validation and an exhaustive literature-priority audit have not been performed.

## References

1. J. Kelner and P. Maymounkov, *Electric routing and concurrent flow cutting*, arXiv:0909.2859v1, first posted 2009-09-15; especially the electrical routing operator definition and the general norm bounds. https://arxiv.org/abs/0909.2859
2. A. Schild, S. Rao, and N. Srivastava, *Localization of Electrical Flows*, arXiv:1708.01632v1, first posted 2017-08-04; especially Section 1, Examples 1.1--1.3, and the main localization theorem. https://arxiv.org/abs/1708.01632
3. O. Gurel-Gurevich, A. Nachmias, and S. Sachdeva, *A Tight Bound on Localization of Electrical Flows*, arXiv:2605.24130v1, first posted 2026-05-22; especially Theorems 1.1--1.4 and the general transfer-current analysis. https://arxiv.org/abs/2605.24130
