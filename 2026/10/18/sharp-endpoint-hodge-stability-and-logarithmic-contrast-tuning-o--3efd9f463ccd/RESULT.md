# Sharp endpoint Hodge stability and logarithmic contrast tuning on weighted wheel graphs

## Finding

Let \(m\geq3\), \(t>0\), and consider the wheel with \(m\) rim vertices, one hub, unit-conductance spokes, and conductance \(t\) on every rim edge. In energy-normalized edge coordinates let \(P_{m,t}\) denote the Euclidean orthogonal projection of edge data onto potential-gradient flows. Put
\[
\Delta=\sqrt{1+4t},\qquad q=\frac{\Delta-1}{\Delta+1},\qquad
 g_j=\frac{q^j+q^{m-j}}{\Delta(1-q^m)}\quad(0\leq j<m),\qquad a=\lfloor m/2\rfloor.
\]
Then the two possible absolute row sums of \(P_{m,t}\), at spoke and rim output edges respectively, are precisely
\[
 S_m(t)=1+2\sqrt t\,(g_0-g_a),\qquad
 R_m(t)=2(1-g_0)+2\sqrt t\,(g_0-g_a).
\]
In particular,
\[
 \boxed{\|P_{m,t}\|_{\ell^\infty\to\ell^\infty}=\max\{S_m(t),R_m(t)\}.}
\]
There is exactly one transition \(t_m^*>0\), defined by \(g_0(t_m^*)=1/2\). Spoke rows are strictly maximal below this transition, rim rows above it, and both are maximal at equality. The transition decreases strictly with \(m\) and satisfies
\[
 \boxed{t_m^*=\frac34+4\,3^{-m}+O(m\,9^{-m})\quad(m\to\infty).}
\]
Most importantly, the sharp norm is strictly below \(3\) for every finite \(m,t\), but optimizing conductance gives
\[
 \boxed{\sup_{t>0}\|P_{m,t}\|_{\ell^\infty\to\ell^\infty}
 =3-\frac{2\log m+2+o(1)}m.}
\]
Every maximizing conductance for all sufficiently large \(m\) obeys
\[
 \boxed{t_m\sim\frac{m^2}{4(\log m)^2}.}
\]
Each displayed row sum is sharp: for that output edge, choosing input signs matching its projection row attains it.

## Assumptions and scope

The wheel is a finite simple graph with vertices \(h,v_0,\ldots,v_{m-1}\), spokes \(hv_j\) of weight one, and rim edges \(v_jv_{j+1}\) of weight \(t\), with indices modulo \(m\). Choose any orientations. For an oriented edge \(e=(x,y)\) with conductance \(w_e\), define the weighted incidence map on potentials by \((D\varphi)_e=\sqrt{w_e}(\varphi(y)-\varphi(x))\). Define \(P_{m,t}\) as orthogonal projection onto \(\operatorname{range}D\) in the ordinary Euclidean inner product on \(\mathbb R^{2m}\). The norm uses unweighted coordinatewise maxima on these energy-normalized edge measurements; it is not the operator norm under raw, unscaled potential differences, nor the Euclidean operator norm (which equals one). An orientation change merely conjugates the projector by an edge-sign diagonal matrix and does not affect any stated norm.

## Proof

**1. Reduction to a cyclic Green matrix.** Fix the hub potential to zero and orient spokes from the hub to rim vertices, with cyclic orientations on rim edges. The resulting \(2m\)-by-\(m\) grounded incidence matrix is
\[
 B=\begin{pmatrix}I_m\\ \sqrt t\,C\end{pmatrix},
 \quad (Cz)_j=z_{j+1}-z_j.
\]
Thus \(A=B^\mathsf TB=I_m+tC^\mathsf TC\) is invertible, and \(P=BA^{-1}B^\mathsf T\). The cyclic Green matrix \(G=A^{-1}\) has entries \(G_{ij}=g_{i-j\pmod m}\). Indeed the second-order recurrence
\[
 (1+2t)g_j-tg_{j-1}-tg_{j+1}=\mathbf1_{\{j=0\}}
\]
with periodic indices has the unique solution stated above, because \(q+q^{-1}=2+t^{-1}\). In addition \(g_j>0\), \(\sum_jg_j=1\), and \(g_0>g_1>\cdots>g_a\), with symmetry \(g_j=g_{m-j}\). The strict inequalities follow directly by subtracting consecutive geometric terms; for odd \(m\) the two antipodal positions tie.

**2. Exact absolute row sums.** In spoke–rim blocks,
\[
 P=\begin{pmatrix}G&\sqrt t\,GC^\mathsf T\\ \sqrt t\,CG&tCGC^\mathsf T\end{pmatrix}.
\]
Every spoke–spoke row sums in absolute value to one because the Green entries are positive and sum to one. Every spoke–rim row is a cyclic first difference of \(g\); since \(g\) decreases to the antipode and increases thereafter, its absolute row sum is \(2\sqrt t(g_0-g_a)\). The rim–spoke block has the same absolute row sum by transposition and cyclic symmetry. Finally,
\[
 tCGC^\mathsf T=I_m-G
\]
(as \(C\) is the cyclic difference and commutes with the cyclic \(G\)). Its diagonal entries \(1-g_0\) are nonnegative and off-diagonal entries \(-g_j\) are negative. The absolute row sum is therefore \(2(1-g_0)\). Combining the blocks proves \(S_m,R_m\) and the sharp induced norm. Each row's signs provide an exact finite-dimensional maximizing input.

**3. Unique row-type transition.** The row-sum difference is \(R_m-S_m=1-2g_0\). By Fourier diagonalization of the cycle,
\[
 g_0(t)=\frac1m\sum_{k=0}^{m-1}
 \frac1{1+t(2-2\cos(2\pi k/m))}.
\]
This is strictly decreasing on \(t>0\), from \(1\) to \(1/m<1/2\), proving existence and uniqueness. At fixed \(t\), the explicit geometric form shows \(g_0(m,t)=\Delta^{-1}(1+q^m)/(1-q^m)\) strictly decreases as \(m\) grows. Hence \(t_m^*\) strictly decreases. Its limit solves \((1+4t)^{-1/2}=1/2\), namely \(3/4\). Expanding the exact transition equation near this limit, using \(q(3/4)=1/3\) and \(\frac{d}{dt}(1+4t)^{-1/2}|_{t=3/4}=-1/4\), gives \(t_m^*=3/4+4\,3^{-m}+O(m\,9^{-m})\).

**4. Exact transformed formula and the strict ceiling.** Set
\[
 u=\operatorname{arsinh}\bigl((2\sqrt t)^{-1}\bigr),\quad x=mu,\quad
 c_m(u)=\begin{cases}1,&m\text{ even},\\\cosh u,&m\text{ odd}.\end{cases}
\]
Since \(q=e^{-2u}\) and \(\Delta=\coth u\), direct substitution yields
\[
 g_0=\tanh u\,\coth x,\quad
 2\sqrt t(g_0-g_a)=\operatorname{sech}u\,
 \frac{\cosh x-c_m(u)}{\sinh x}.
\]
The fraction is positive and at most \(\tanh(x/2)<1\), while \(\operatorname{sech}u<1\). Therefore \(S_m<2\), \(R_m<3\), and \(\|P\|<3\) for every finite pair.

**5. The optimal logarithmic boundary layer.** Put \(F_m(x)=R_m(t)\) with \(t=(4\sinh^2(x/m))^{-1}\). From the previous formula,
\[
 3-F_m(x)\ge 2\tanh(x/m)+\frac2{e^x+1},\qquad x>0.
\]
At \(x=\log m\), the exact expression gives
\[
 3-F_m(\log m)=\frac{2\log m+2+o(1)}m.
\]
The value here tends to zero; spoke rows remain below two, so for all large \(m\) a maximizing output row must be a rim row. The limiting values as \(t\downarrow0\) and \(t\to\infty\) are below three, hence a finite optimizing \(t\) exists when \(m\) is sufficiently large. Any minimizing \(x_m\) of \(3-F_m\) lies below \(\sqrt m\) for all sufficiently large \(m\): otherwise the displayed lower bound has first term at least \(2\tanh(m^{-1/2})\), which dominates \((\log m)/m\). Uniformly for \(0<x\le\sqrt m\),
\[
 3-F_m(x)\ge\frac{2x}m+\frac2{e^x+1}-O(m^{-3/2}).
\]
For \(m>4\), the scalar function on the right without its error has a unique minimum on \(x\ge0\), at
\[
 e^{x}=\frac{m-2+\sqrt{m(m-4)}}2,
\]
with minimum \((2\log m+2+o(1))/m\). This proves the matching sharp lower bound on the defect and hence the norm asymptotic. To localize every optimizer, write \(z_m=x_m-\log m\). The preceding matching bounds imply \(z_m\) is bounded, and for each bounded \(z\)
\[
 m\bigl(3-F_m(\log m+z)\bigr)-2\log m
 \longrightarrow 2(z+e^{-z}).
\]
The limit has a unique minimum at \(z=0\), so \(x_m=\log m+o(1)\). Therefore
\[
 t_m=(4\sinh^2(x_m/m))^{-1}\sim m^2/[4(\log m)^2].
\]
This proves the final conclusions.

## Verification

The companion `verify.py` reconstructs the grounded weighted incidence matrix and its projector independently with exact rational Gaussian elimination for \(m=3,\ldots,11\) and six rational square roots of rim conductance. It checks every row sum, Green-row normalization, projector symmetry, and selected exact idempotence identities. It also tests the transformed large-size defect at four mesh sizes. A complete local execution passed 16,896 assertions. Finite tests are not a proof of the all-parameter or asymptotic statements; steps 1–5 establish these analytically.

## Relationship to prior work

Jiang, Lim, Yao and Ye formulate least-squares graph-edge ranking via an orthogonal discrete Hodge decomposition [1]. Kassel and Wu describe the transfer-current projection kernel using the graph Green operator [2], and Lyons develops its relation to cut and star spaces [3]. These general identities motivate, but do not state, the present weighted-wheel sharp \(\ell^\infty\) norm, exact spoke/rim switch, or logarithmically tuned optimization. Related published calculations of generalized-theta Hodge-projection norms concern a different, non-wheel graph family without the wheel's weighted rim–hub cyclic Green profile. The published weighted-wheel Löwner-ellipsoid result concerns an enclosing ellipsoid rather than this edge-space projection norm. Equivalence under transfer-current, electrical-flow, or least-squares terminology remains a bibliographic possibility.

## Limitations

The weights and graph family are specified exactly: only equal spoke weights and equal rim weights are covered. The coordinate norm is applied after multiplication by the square roots of conductances; conclusions need not hold for unscaled edge observations. The finite-size optimizer is not claimed unique. The asymptotic localization describes every global maximizer for sufficiently large rim size; finite-size exact optimizing conductances are not classified. Historical priority has not been independently established.

## References

[1] X. Jiang, L.-H. Lim, Y. Yao, Y. Ye, *Statistical ranking and combinatorial Hodge theory*, preprint first submitted November 7, 2008, arXiv:0811.1067; *Mathematical Programming* **127** (2011), 203–244. https://arxiv.org/abs/0811.1067

[2] A. Kassel, W. Wu, *Transfer current and pattern fields in spanning trees*, arXiv:1312.2946 (2013). https://arxiv.org/abs/1312.2946

[3] R. Lyons, *Determinantal probability measures*, *Publ. Math. Inst. Hautes Études Sci.* **98** (2003), 167–212. https://www.numdam.org/article/PMIHES_2003__98__167_0.pdf
