# Sharp endpoint Hodge projection on prism graphs: an edge transition and a log-periodic defect

## Finding

Let \(G_n=C_n\square K_2\), \(n\ge3\), with unit conductances and one real coordinate per undirected edge. Let \(P_n\) be the Euclidean orthogonal projection onto vertex gradients, acting on the edge coordinate maximum norm. The largest absolute row sum is a rung row at \(n=3\), both edge orbits tie at \(n=4\), and it is a rail row for all \(n\ge5\). The corresponding small norms are \(9/5\) and \(2\). The norm is strictly less than 3 for every finite \(n\), but tends to 3.

Put \(q=2+\sqrt3\), \(r=1/q\), \(L=\log q\), and \(\beta_n=\log_q(n/\sqrt3)\). The sharp phase correction is
\[
n(3-\|P_n\|_{\infty\to\infty})-2\log(n)/L=F(\{\beta_n\})+o(1),
\qquad F(u)=2+(\sqrt3-1)q^u-2u-\frac{\log3}{L}\quad(0\le u\le1).
\]
Here \(F(1)=F(0)\), so this defines a continuous period-one function, and the error tends to zero without excluding any phase or any near-integer cutoff. The centered defect has limsup \(F(0)\approx1.8978462432\) and liminf \(F(u_*)\approx1.5762442666\), where \(u_*=L^{-1}\log(2/((\sqrt3-1)L))\).

## Exact row sums

Use the forward difference \(D\) on each consistently oriented rail and orient the rungs from the first rail to the second. If \(B\) is the incidence operator from vertex to edge coordinates, then \(P_n=B(B^{\mathsf T}B)^+B^{\mathsf T}\). Reversing an edge only changes signs of its row and column. Let \(S\) be the cyclic shift and \(L_C=2I-S-S^{-1}\). On symmetric and antisymmetric rail-potential modes the Laplacians are \(L_C\) and \(L_C+2I\). The latter has circulant inverse \(G\) with entries from
\[
g_j=\frac{r^j+r^{n-j}}{2\sqrt3(1-r^n)},\quad 0\le j<n.
\]
Indeed \((4I-S-S^{-1})g=\delta_0\), by \(r+r^{-1}=4\) and the normalization at zero. Hence \(\sum_j g_j=1/2\); the kernel decreases strictly with cyclic distance \(j\le m=\lfloor n/2\rfloor\). The kernel is already encoded in Cinkir's exact effective-resistance formulas (see below).

On cycle-edge coordinates the symmetric mode yields \(DL_C^+D^{\mathsf T}=I-J/n\), with \(J\) the all-ones matrix, since the orthogonal complement of cycle gradients consists of constants. The antisymmetric mode yields \(DGD^{\mathsf T}=I-2G\) by commutation of the circulants. The same- and opposite-rail blocks of the projector are therefore \(I-J/(2n)-G\) and \(G-J/(2n)\), respectively. The two rail-to-rung blocks have opposite signs and kernel \(DG\); the rung-to-rung block is \(2G\). For offset zero in a rail row, the two rail coefficients add in absolute value to \(1-1/n\): both are nonnegative since \(1/(2\sqrt3)<g_0\le3/10\) and \(1/(2n)\le1/6\). At nonzero offsets their sum is \(\max\{1/n,2g_j\}\). The total variation of \(g\) around the cycle is \(2\Delta_n\), where \(\Delta_n=g_0-g_m\). It follows that
\[
H_n=1-\frac1n+\sum_{j=1}^{n-1}\max\{1/n,2g_j\}+2\Delta_n,
\qquad V_n=1+4\Delta_n
\]
are the rail and rung row sums. Their maximum is the norm, and sign inputs matching a maximizing row attain it.

Substitution yields \((H_3,V_3)=(26/15,9/5)\) and \((H_4,V_4)=(2,2)\). For \(n\ge5\), \(H_n-V_n\ge1-2/n-2\Delta_n>0\) because \(\Delta_n<1/(2\sqrt3)\). This last inequality follows by factoring its numerator as \((1-r^m)(1-r^{n-m})\), strictly less than \(1-r^n\) for \(0<r<1\). Write \(a_j=2g_j\). From \(\sum_j a_j=1\), the exact positive defect for every \(n\) is
\[
3-H_n=\frac2n+a_m+\sum_{j=1}^{n-1}\min\{1/n,a_j\}.
\]
Also \(V_n<1+2/\sqrt3<3\), proving the finite bound independently of the asymptotics.

## Phase evaluation

For all sufficiently large \(n\) let \(k_n<m\) be the largest cyclic distance for which \(a_{k_n}\ge1/n\). The first \(k_n\) nonzero distances on each side contribute \(1/n\) to the minimum sum above, and the remaining interval sums geometrically. Thus
\[
3-H_n=\frac{2k_n+2}{n}+a_m+
\frac{2r^{k_n+1}(1-r^{n-2k_n-1})}{\sqrt3(1-r)(1-r^n)}.
\]
Write \(b_n=\lfloor\beta_n\rfloor\). Directly from the kernel, \(na_{b_n}\ge1\) because of the leading geometric term, whereas \(na_{b_n+2}\le q^{-1}(1+o(1))<1\) since \(b_n=O(\log n)\). Therefore \(k_n=b_n\) or \(b_n+1\). The latter requires \(q^{\beta_n-b_n-1}\ge1-o(1)\), hence \(\{\beta_n\}\to1\) along any sequence of exceptional sizes. This derivation is valid even for exponentially close approaches to the threshold.

We have \(na_m=o(1)\). Multiplying the geometric tail by \(n\) gives \((\sqrt3-1)q^{\beta_n-k_n}+o(1)\) by \(2r/(1-r)=\sqrt3-1\), with uniform control since \(k_n\in\{b_n,b_n+1\}\). Subtract \(2\log(n)/L=2\beta_n+\log3/L\). For \(k_n=b_n\) the resulting expression is \(F(\{\beta_n\})+o(1)\); for \(k_n=b_n+1\) the argument is shifted down by one, from near 1 to near 0. The same analytic expression is continuous there and \(F(0)=F(1)\), so this makes an \(o(1)\) difference. In particular \(H_n\to3\). The function is strictly convex on \([0,1]\), with its unique minimum at the indicated \(u_*\) and its maximum at the endpoints. For each phase \(u\), nearest integers to \(\sqrt3q^{j+u}\) have phases tending to \(u\) on the circle. This proves the extrema as subsequential limits, including when phases approach zero from either side.

## Prior work and scope

The Hodge decomposition and transfer-current interpretation are standard [1,2]. Cinkir [3, §2, Eqs. (10)–(11)] gives all-pair prism resistances. These determine every projector entry: for oriented edges \(e=(a,b)\), \(f=(c,d)\), polarization gives \(P_{ef}=(R(a,d)+R(b,c)-R(a,c)-R(b,d))/2\). Thus the entries and finite norm are recoverable from existing exact data; the row formulas above are used as a basis for the explicit edge comparison and phase analysis rather than claimed as new transfer-current data.

An earlier Möbius-ladder result [4] finds the same leading logarithmic deficit with an \(O(n^{-1})\) remainder and has an exact row-sum formula using an antiperiodic Green kernel. In fact the finite rim row sum there and the prism rail row sum above are exponentially close for large \(n\). In their common positive-part form the sums range over distances \(1\le j\le\lfloor(n-1)/2\rfloor\), with the prism midpoint inactive for large \(n\). The difference of the periodic and antiperiodic kernels is bounded by a constant times \(r^{n-j}+r^{n+j}\), the positive-part function is 1-Lipschitz, and the additional prism midpoint term is exponentially small. Therefore the leading logarithmic law is not the new part of the comparison; it is the explicit order-\(1/n\) phase, including its nondegenerate oscillation, that is not evaluated in [4]. Its orbit conclusion also differs: strict rim dominance on the stated Möbius-ladder range rather than the small-order prism transition.

Only the canonical projection on real, unweighted finite prisms is asserted here, not a minimum over all projections. The supplied finite checker is a consistency check; the orbit and oscillation claims follow from the analytic inequalities.

## References

1. X. Jiang, L.-H. Lim, Y. Yao, Y. Ye, *Statistical ranking and combinatorial Hodge theory*, [arXiv:0811.1067](https://arxiv.org/abs/0811.1067).
2. A. Kassel, W. Wu, *Transfer current and pattern fields in spanning trees*, [arXiv:1312.2946](https://arxiv.org/abs/1312.2946).
3. Z. Cinkir, *Effective Resistances and Kirchhoff Index of Prism Graphs*, [arXiv:1704.03429](https://arxiv.org/abs/1704.03429).
4. *Sharp logarithmic endpoint-projection deficit on Möbius ladders*, [Resultary, 2026-10-26](https://github.com/Resultary/2026/blob/main/2026/10/26/SCOPE-sharp-logarithmic-endpoint-projection-deficit-on-m-bius-ladders--833010be3478/RESULT.md).
