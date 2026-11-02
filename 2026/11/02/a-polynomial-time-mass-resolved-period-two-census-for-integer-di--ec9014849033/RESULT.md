# A polynomial-time mass-resolved period-two census for integer diffusion on arbitrary trees

## Finding

**Theorem.** Let \(T=(V,E)\) be any finite, simple, connected, *labelled* tree on \(n\ge1\) vertices. At each synchronous step, an integer-valued configuration \(x\in\mathbb Z^V\) evolves by
\[
F(x)_v=x_v-\sum_{w\sim v}\operatorname{sgn}(x_v-x_w).
\]
For every integer total \(S\), the number \(N_T(S)\) of *primitive period-two orbits* with \(\sum_v x_v=S\) is exactly
\[
N_T(S)=\frac{a_{S\bmod n}-\mathbf1_{n\mid S}}{2},
\]
where the \(n\) nonnegative integers \(a_0,\ldots,a_{n-1}\) are computed by the explicit rooted-tree recurrence below in the finite group ring \(\mathbb Z[z]/(z^n-1)\). The recurrence uses polynomially many exact integer arithmetic operations: \(O(n^3\Delta^3)\) is a conservative bound for maximum tree degree \(\Delta\), with the simpler total count requiring \(O(n\Delta^3)\). It counts all period-one and period-two states and does not require enumerating the infinitely many integer assignments.

The tree shape matters beyond its degree multiset. The two six-vertex trees with edge lists
\[
\begin{split}
E_A&=\{(0,4),(1,0),(1,2),(1,3),(4,5)\},\\
E_B&=\{(0,3),(0,5),(1,0),(1,2),(3,4)\}
\end{split}
\]
have the same sorted degree sequence \((1,1,1,2,2,3)\) but exactly \(279\) and \(197\) primitive two-cycle orbits, respectively, when counted modulo simultaneous integer translation. Their respective per-total orbit vectors, indexed by \(S\bmod6\), are
\[
(48,47,46,45,46,47),\qquad (32,32,33,35,33,32).
\]
This is the smallest vertex order at which distinct tree shapes can have the same degree multiset.

## Assumptions and scope

The graph is undirected, loopless, connected, and acyclic; vertices remain labelled and no graph-automorphism quotient is taken. Chip values may be arbitrary integers, including negative integers. Time is synchronous, with strict comparisons; equal-valued neighbors exchange no chips. Every primitive two-cycle consists of two different configurations, and an orbit is counted once regardless of starting phase. The fixed-total count \(N_T(S)\) does not identify configurations by translation, because a nonzero simultaneous translation changes \(S\). Without fixing a total, common integer translation identifies recurrent configurations; the number of primitive two-cycle translation classes is \((\sum_{j=0}^{n-1}a_j-1)/2\). No claim is made about transient-entry distributions.

Root \(T\) at any vertex \(r\). For an edge from parent \(v\) to child \(w\), write \(m_w\) for the number of vertices in the descendant subtree rooted at \(w\). Let \(d_v\) be the degree of \(v\). Use two independent formal variables: \(z\) is reduced modulo \(z^n-1\); \(y\) records an ordinary integer exponent and is used only for coefficient extraction.

For \(t\in\{-1,0,1\}\), integers \(q,q'\), and a positive integer \(m\), define the following group-ring element:
\[
H_t(q,q';m)=
\begin{cases}
\mathbf1_{q=q'},&t=0,\\[2pt]
\displaystyle\sum_{k=1}^{\max\{0,\,t(q-q')-1\}}z^{-mtk},&t\in\{-1,1\}.
\end{cases}
\]
The empty sum is zero. All exponents of \(z\) are reduced modulo \(n\).

For a nonroot vertex \(v\), let \(s\in\{-1,0,1\}\) denote \(\operatorname{sgn}(x_v-x_{\operatorname{parent}(v)})\); at the root set \(s=0\) by convention. Let \(q\) denote the signed net outgoing flux \(\sum_{w\sim v}\operatorname{sgn}(x_v-x_w)\). Define the group-ring polynomials \(F_v(s,q)\), for \(-d_v\le q\le d_v\), by bottom-up recursion. At a leaf:
\[
F_v(s,q)=\mathbf1_{q=s}.
\]
At any other vertex \(v\), with children \(\mathrm{Ch}(v)\), set
\[
F_v(s,q)=[y^{q-s}]\prod_{w\in\mathrm{Ch}(v)}\left(
\sum_{t=-1}^{1}y^t\sum_{q'=-d_w}^{d_w}
F_w(-t,q')H_t(q,q';m_w)\right).
\]
The empty product is one. For the root use the same formula with \(s=0\). Finally let
\[
A_T(z)=\sum_{q=-d_r}^{d_r}F_r(0,q)
=\sum_{j=0}^{n-1}a_jz^j\quad\bmod(z^n-1).
\]
The values \(a_j\) are independent of the choice of root.

## Proof

**1. Exact edge-flux reversal for period-two states.** Orient the tree edges arbitrarily, and let \(B\) be the associated vertex-edge incidence matrix. Define \(\sigma_e=\operatorname{sgn}(x_u-x_v)\) when edge \(e\) is oriented from \(u\) to \(v\). Then \(F(x)=x-B\sigma\). If \(x\mapsto x'\mapsto x\) is periodic within two steps, \(B(\sigma+\sigma')=0\), where \(\sigma'\) is the analogous sign vector at \(x'\). The integer kernel of the incidence matrix of a tree is zero, so \(\sigma'=-\sigma\) edge by edge. Conversely, this edgewise reversal makes the two-step net flux vanish, yielding \(F^2(x)=x\). A flat edge must remain flat in both phases.

**2. Exact available gap lengths.** Fix a rooted-tree assignment of signed edge signs, and set \(q_v=\sum_{w\sim v}\operatorname{sgn}(x_v-x_w)\). On a parent-child edge \(v\to w\), put \(t=\operatorname{sgn}(x_v-x_w)\) and \(g=x_v-x_w\). Since \(F(x)_v=x_v-q_v\), its next-phase gap is \(g'=g-(q_v-q_w)\). For \(t=0\), the only admissible gap is \(g=0\), and it remains flat if and only if \(q_v=q_w\). For \(t\ne0\), write \(g=tk\) with integer \(k\ge1\). Reversal to sign \(-t\) holds exactly when
\[
1\le k\le t(q_v-q_w)-1.
\]
Thus the permissible gaps contribute precisely \(H_t(q_v,q_w;m_w)\). These choices are independent across the edges: a tree has no cycle-integrability constraints, and prescribing its signed edge gaps determines all vertex values up to one simultaneous translation. The local signed fluxes are enforced by \(q_v=s+\sum_{w\in\mathrm{Ch}(v)}t_{vw}\). Therefore the displayed coefficient-extraction recursion enumerates every two-periodic configuration modulo translation exactly once, including the constant configuration.

**3. Conservation and mass residues.** With root value \(x_r=c\), any descendant vertex \(u\) has \(x_u=c-\sum_{e\in P(r,u)}g_e\). Summing over all vertices gives
\[
\sum_{v\in V}x_v=nc-\sum_{v\to w}m_wg_{vw}.
\]
Consequently a particular signed-gap assignment admits exactly one integer root value \(c\) with total \(S\) if and only if \(-\sum m_wg_{vw}\equiv S\pmod n\). The monomial \(z^{-m_wg_{vw}}\) in \(H_t\) records precisely that residue. The coefficient \(a_{S\bmod n}\) therefore counts all configurations at total \(S\) with period dividing two.

**4. Remove fixed points and divide by the primitive orbit size.** If \(F(x)=x\), then \(B\sigma=0\), so all edge signs vanish and connectedness forces a constant configuration. At total \(S\), this fixed configuration exists if and only if \(n\mid S\), and it is unique. All other counted states belong to disjoint primitive two-cycles, each containing two states with the same conserved total. Subtract the fixed-state indicator and divide by two. This proves the formula, its integrality, and root independence.

**5. Complexity.** For each vertex and boundary sign, only \(2d_v+1\) possible fluxes occur. The product over its children is an integer-exponent convolution over a range of width \(O(d_v)\); every edge contributes at most \(2d_w+1\) child fluxes and \(3\) edge signs. This gives \(O(n\Delta^3)\) arithmetic operations for the unweighted count. Representing the group ring by an array of \(n\) integer coefficients and using naive cyclic convolution introduces at most an additional \(O(n^2)\) factor, giving \(O(n^3\Delta^3)\) operations for the mass-resolved vector. Coefficient bit lengths are polynomially bounded in \(n\) and \(\log(\Delta+1)\), since every nonzero edge gap is at most \(2\Delta-1\). Thus both calculations are polynomial-time in the ordinary bit model as well.

## Verification

Run `python3 tree_diffusion_verify.py` in the directory containing the provided script, using only the Python standard library. The checker independently computes an explicit edge-sign/gap sum and the rooted dynamic program for every labelled tree of orders \(1\) through \(6\), generated by Prüfer sequences; these are \(1+1+3+16+125+1296=1442\) trees, counting labelled instances. It compares full chip-sum residue vectors for all those trees and separately compares the simpler unweighted recurrence. It also directly simulates both phases for all normalized integer configurations within a stated finite grid on seven representative six-vertex trees and checks a range of larger path/star examples. The degree-twin vectors above appear explicitly in the checker output `tree_diffusion_verify.log`.

These experiments are finite cross-checks only. The proof of the infinite-family result is Steps 1–5 above, not the computation.

## Relationship to prior work

Duffy, Lidbetter, Messinger, and Nowakowski introduced integer diffusion and analyzed periodicity on several graph families; their earliest arXiv preprint is dated 2016-09-19 [1]. Long and Narayanan subsequently proved eventual period at most two on any finite graph and described reversal of edge transfer directions in recurrent phases [2]. The edge-reversal property is treated here as known background; the additional content is the exact all-tree, conserved-total orbit census via a polynomial-time rooted group-ring transfer.

Mullen, Nowakowski, and Cox later determined a recurrence for periodic configurations on paths [3]. The new recurrence specializes consistently to the labelled path counts, but path-only transfer arguments do not themselves classify arbitrary branched trees or their individual chip-sum residue classes. Their complete-graph work [4] concerns a different graph family and quotient convention. No equivalent all-tree, mass-resolved dynamic program was identified in the inspected literature; historical equivalence remains possible.

## Limitations

The theorem counts the period-one and primitive period-two portions of the integer state space, not the number or distribution of starting configurations attracted to them, and does not bound convergence time. It applies to simple trees, not graphs containing cycles or directed/multiple edges. Polynomial complexity refers to exact arithmetic on finite integer coefficient arrays; no asymptotic formula in the number of vertices for arbitrary changing tree shapes is claimed. No independent external validation is asserted.

## References

[1] C. Duffy, T. F. Lidbetter, M. E. Messinger, R. J. Nowakowski, *A Variation on Chip-Firing: the diffusion game*, arXiv:1609.05792, v1 submitted 2016-09-19, https://arxiv.org/abs/1609.05792.

[2] J. Long and B. Narayanan, *Diffusion on graphs is eventually periodic*, arXiv:1704.04295, first posted 2017-04-13, https://arxiv.org/abs/1704.04295.

[3] T. Mullen, R. Nowakowski, and D. Cox, *Counting Path Configurations in Parallel Diffusion*, arXiv:2010.04750, first posted 2020-10-09, https://arxiv.org/abs/2010.04750.

[4] T. Mullen, R. Nowakowski, and D. Cox, *Complete Graphs and Polyominoes*, arXiv:2010.07745, first posted 2020-10-14, https://arxiv.org/abs/2010.07745.
