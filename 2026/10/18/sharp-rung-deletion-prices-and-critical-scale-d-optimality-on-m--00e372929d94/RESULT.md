# Sharp rung-deletion prices and critical-scale D-optimality on Möbius ladders

## Finding

For each integer \(n\ge 2\), take the cycle on \(2n\) vertices numbered \(0,1,\ldots,2n-1\) and add the \(n\) antipodal rungs \(\{j,j+n\}\), \(0\le j<n\). Assign independently chosen nonnegative conductances to all \(3n\) edges, with a price of \(1\) per unit conductance on each cycle edge and a price of \(t>0\) per unit on each rung. For any fixed budget \(B>0\), maximize the weighted spanning-tree sum
\[
\tau(w)=\sum_{T\text{ spanning tree}}\prod_{e\in T}w_e
\]
subject to exact expenditure \(\sum_{e\text{ cycle}}w_e+t\sum_{e\text{ rung}}w_e=B\).

**Global finite-size classification.** The optimizer is unique among all independent edge assignments. It assigns one common conductance \(b>0\) to all cycle edges and one common conductance \(a\ge0\) to all rungs. Put
\[
 t_c(n)=\frac{n^2}{2n-1}.
\]
For \(t\ge t_c(n)\), the unique optimum deletes every rung: \(a=0\) and \(b=B/(2n)\). For \(0<t<t_c(n)\), both classes are strictly positive. Writing \(r=a/b\), the unique positive solution of
\[
\frac{T_n'(1+r)}{T_n(1+r)+1}=\frac{(2n-1)t}{2+tr}
\tag{1}
\]
determines the exact optimal allocation
\[
 b=\frac{B}{n(2+tr)},\qquad a=rb.
\tag{2}
\]
Here \(T_n\) is the usual degree-\(n\) Chebyshev polynomial of the first kind, characterized by \(T_n(\cos\theta)=\cos(n\theta)\). The entire objective along the symmetric allocations is
\[
\tau(a,b)=n b^{2n-1}\bigl(T_n(1+a/b)+1\bigr),\qquad b>0.
\tag{3}
\]
In particular, \(t_c(n)\sim n/2\), so the price at which the optimal support loses all rungs diverges linearly with network size.

**Fixed-price limit.** For every fixed \(t>0\), let \(r_n(t)\) be the optimal ratio. Then
\[
 r_n(t)\longrightarrow r_\infty(t)
 =\frac{2\bigl(1-2t+\sqrt{(2t-1)^2+3}\bigr)}{3t}>0.
\tag{4}
\]
The fraction of budget optimally spent on rungs converges to \(t r_\infty(t)/(2+t r_\infty(t))\). At equal unit prices \(t=1\), that fraction tends to exactly \(1/4\), rather than the \(1/3\) that equal edge conductances would spend on rungs.

**Critical-price scaling and quantitative gain.** More generally, suppose \(t=t_n>0\) depends on size and \(t_n/n\to c\in(0,\infty)\). For \(0<c<1/2\), let \(z_c>0\) be the unique solution of
\[
 \tanh z_c=2c z_c.
\tag{5}
\]
Then the optimum retains all rungs and
\[
 n^2 r_n(t_n)\longrightarrow 2z_c^2.
\tag{6}
\]
Let \(\tau_n^\star\) be the optimal weighted spanning-tree sum and \(\tau_n^{\mathrm{cycle}}=2n[B/(2n)]^{2n-1}\) the value of the feasible all-cycle allocation. Then
\[
\frac{\tau_n^\star}{\tau_n^{\mathrm{cycle}}}
\longrightarrow \exp(-2c z_c^2)\cosh^2 z_c>1,
\qquad 0<c<1/2.
\tag{7}
\]
If \(c\ge1/2\), instead \(n^2 r_n(t_n)\to0\) and the optimal-to-cycle ratio tends to \(1\). For \(c>1/2\), every rung is exactly absent for all sufficiently large \(n\). At the borderline \(c=1/2\), finite-size solutions may or may not use rungs depending on the approach of \(t_n\) to \(t_c(n)\).

These statements form one design classification for the same weighted-spanning-tree objective; no separate optimization objective is claimed.

## Assumptions and scope

The graph is the finite undirected simple Möbius ladder with labeled vertices \(\mathbb Z/(2n\mathbb Z)\); no parallel edges occur for \(n\ge2\). Edge conductances are real and nonnegative, the budget is spent exactly, and prices are strictly positive. The objective is the *weighted sum of spanning-tree conductance products*, equivalently any cofactor of the weighted Laplacian by the matrix-tree theorem. It is not the all-terminal reliability probability for a prescribed probability model. There are no additional edge-capacity or integrality constraints. The assertions of uniqueness concern the full \(3n\)-variable allocation problem, not only a pre-symmetrized two-parameter model.

## Proof

**Step 1: global uniqueness before imposing symmetry.** Delete any one row and column from the weighted graph Laplacian to obtain \(L_{\mathrm{red}}(w)\). The matrix-tree theorem gives \(\tau(w)=\det L_{\mathrm{red}}(w)\). Feasible weight vectors form a compact simplex, and a strictly positive feasible vector makes the determinant positive. Thus a maximizing vector exists and its reduced Laplacian is positive definite.

On the set of positive-definite reduced Laplacians, \(\log\det\) is strictly concave. Moreover, the linear map from individual edge weights of a *simple* graph to \(L_{\mathrm{red}}\) is injective: off-diagonal entries recover every edge not incident to the deleted vertex, and diagonal entries then recover the remaining incident edges. Equivalently, for any nonzero weight perturbation \(v\) with associated nonzero symmetric matrix \(H\), the second directional derivative is
\[
 -\operatorname{tr}\bigl((L_{\mathrm{red}}^{-1/2}HL_{\mathrm{red}}^{-1/2})^2\bigr)<0.
\]
Consequently the maximizer is unique. Rotations of the cyclic vertex labeling preserve each edge-price class, so invariance and uniqueness force all rim weights to equal \(b\) and all rung weights to equal \(a\). A positive determinant requires \(b>0\): rungs alone form \(n\) disconnected pairs. Both all-rim and positive-rung solutions are allowed.

**Step 2: exact spectral tree enumerator.** With common rim weight \(b\) and rung weight \(a\), the Fourier mode indexed by \(k=0,\ldots,2n-1\) has Laplacian eigenvalue
\[
 \lambda_k=2b\bigl(1-\cos(\pi k/n)\bigr)
 +a\bigl(1-(-1)^k\bigr).
\]
The \(n-1\) nonzero even-index eigenvalues have product \(n^2b^{n-1}\), using \(\prod_{j=1}^{n-1}4\sin^2(\pi j/n)=n^2\). The \(n\) odd-index eigenvalues have product
\[
 2b^n\bigl(T_n(1+a/b)+1\bigr),
\]
because the multiset \(\{\cos((2j+1)\pi/n):0\le j<n\}\) is the root multiset of \(T_n(x)+1\), whose leading coefficient is \(2^{n-1}\). The matrix-tree eigenvalue formula divides the product of the nonzero eigenvalues by \(2n\), yielding equation (3). The same identity holds by continuity at \(a=0\), with \(\tau(0,b)=2n b^{2n-1}\).

**Step 3: finite optimality and exact support transition.** Let \(r=a/b\). Budget equality gives equation (2), and substitution into equation (3) gives
\[
 \tau(r)=n\left(\frac{B}{n(2+tr)}\right)^{2n-1}
\bigl(T_n(1+r)+1\bigr).
\tag{8}
\]
As \(r\to\infty\), the rungs retain finite weight but rim conductances vanish, so \(\tau(r)\to0\). Differentiating \(\log\tau(r)\) yields exactly the difference between the two sides of equation (1). The one-sided derivative at zero is
\[
 \frac{T_n'(1)}{T_n(1)+1}-\frac{(2n-1)t}{2}
 =\frac{n^2-(2n-1)t}{2},
\tag{9}
\]
using \(T_n(1)=1\) and \(T_n'(1)=n^2\). The family of feasible symmetric weights parametrized by \(r\) is the interior of a straight budget segment after reparametrizing by \(a\). Strict concavity along that segment proves that (9) being nonpositive makes \(a=0\) the unique optimum, while positivity forces a unique interior optimum satisfying (1). This also proves all endpoint equalities and uniqueness without assuming that (1) has only one algebraic root on unrelated branches.

**Step 4: hyperbolic stationary equation.** For \(r>0\), put \(u=\operatorname{arcosh}(1+r)\). The identities \(T_n(1+r)=\cosh(nu)\), \(T_n'(1+r)=n\sinh(nu)/\sinh u\), and \(\sinh u=\sqrt{r(r+2)}\) convert equation (1) into
\[
 \frac{n\tanh(nu/2)}{\sqrt{r(r+2)}}
 =\frac{(2n-1)t}{2+tr}.
\tag{10}
\]
For fixed \(t\) and any fixed positive \(r\), dividing (10)'s two sides by \(n\) and sending \(n\to\infty\) gives the limiting comparison
\[
 \frac{1}{\sqrt{r(r+2)}}\ \mathop{\gtrless}\ 
 \frac{2t}{2+tr}.
\]
For sufficiently small fixed \(r\) the left side is larger; for sufficiently large fixed \(r\) it is smaller. The uniqueness of the finite optimizer therefore traps it between two positive constants. Every subsequential limit solves the equality, equivalent after squaring positive quantities to
\[
 3t^2r^2+(8t^2-4t)r-4=0.
\]
This quadratic has one positive root, namely equation (4); thus the entire sequence converges. The budget fraction follows from equation (2).

**Step 5: size-dependent prices and gain.** Suppose \(t_n/n\to c>0\). At the test ratio \(r=x/n^2\), for any fixed \(x>0\) one has \(n\operatorname{arcosh}(1+x/n^2)/2\to\sqrt{x/2}\). Divide the difference of the two sides of equation (10) by \(n^2\): its sign converges to the sign of
\[
 \frac{\tanh\sqrt{x/2}}{\sqrt{2x}}-c.
\tag{11}
\]
For \(0<c<1/2\), this strictly decreasing function of \(x>0\) starts above zero and ends below zero. Finite uniqueness and sign bracketing give \(n^2r_n\to2z_c^2\) for the unique \(z_c>0\) with equation (5). For \(c\ge1/2\), expression (11) is negative at every fixed \(x>0\). Consequently either \(r_n=0\) or \(r_n<x/n^2\) for all sufficiently large \(n\), and hence \(n^2r_n\to0\). If \(c>1/2\), eventually \(t_n\ge n^2/(2n-1)\), so deletion is exact.

Lastly, the exact optimal-to-cycle ratio is
\[
 \frac{\tau_n^\star}{\tau_n^{\mathrm{cycle}}}
 =\left(\frac{2}{2+t_n r_n}\right)^{2n-1}
 \frac{T_n(1+r_n)+1}{2}.
\tag{12}
\]
For \(0<c<1/2\), insert \(r_n\sim2z_c^2/n^2\): the first factor tends to \(\exp(-2c z_c^2)\), and the second tends to \(\cosh^2z_c\). The strict inequality in equation (7) follows because the continuous function \(2\log\cosh z-2cz^2\) is zero at \(z=0\), positive near zero when \(c<1/2\), and uniquely maximized at the positive solution of \(\tanh z=2cz\). For \(c\ge1/2\), \(n^2r_n\to0\) makes both factors tend to one. This completes the proof.

## Verification

Run `python3 verify.py` from the directory containing this document. The standalone checker uses only the Python standard library. It constructs reduced Laplacians and verifies equation (3) by exact rational determinants for \(n=2,\ldots,7\), including the zero-rung boundary; checks the first four classical unweighted tree counts; exercises the exact transition derivative for \(n=2,\ldots,49\); and provides floating-point convergence checks for the two asymptotic laws. These finite computations are reproducibility checks, not proofs for all sizes or all real prices. The universal assertions follow from Steps 1–5.

## Relationship to prior work

Bailey and Cameron's 2011 treatment of A-, D-, and E-optimal block designs uses the Möbius ladder as a high-performing fixed, unweighted concurrence graph at eight vertices and motivates the determinant criterion, but does not optimize continuously chosen prices across all its edges. Khosoussi, Sukhatme, Huang, and Dissanayake's 2016 weighted spanning-tree design work supplies the graph-reliability and determinant-optimization context, particularly discrete edge-selection formulations and effective-resistance increments, without an all-size priced Möbius-ladder allocation or the present support and asymptotic laws. Classical enumerative results on unweighted Möbius ladders and Chebyshev tree formulas are background, not claimed as newly discovered here. The contribution assessed here is the **full independent-edge continuous-budget optimizer**, its exact rung-deletion boundary, and the fixed-price and critical-price scaling regimes; it does not claim novelty for the matrix-tree theorem, Laplacian Fourier diagonalization, Chebyshev identities, or log-determinant concavity.

## Limitations

The result is for the specified undirected Möbius-ladder family with homogeneous prices within each of the two edge orbits, not arbitrary graphs or heterogeneous per-edge prices. All conclusions are for the weighted spanning-tree sum; reliability probabilities generally require a separate probabilistic model. Equation (1) is an implicit exact characterization, not a radicals formula for every degree. The asymptotic limits do not give a uniform finite-size error bound as \(t\) varies. Numerical verification samples do not establish the infinite-family result. The authorship, independent validation, and historical priority of this mathematical analysis have not been externally certified; equivalent earlier treatments may exist.

## References

1. R. A. Bailey and P. J. Cameron, *Using graphs to find the best block designs*, arXiv:1111.3768, version initially public November 16, 2011, particularly Section 3.3.
2. K. Khosoussi, G. S. Sukhatme, S. Huang, and G. Dissanayake, *Maximizing the Weighted Number of Spanning Trees: Near-t-Optimal Graphs*, arXiv:1604.01116, initially public April 5, 2016, especially Sections 2–4.
3. S. N. Daoud and K. A. Mohamed, *Complexity of some special named graphs with double edges*, Journal of Taibah University for Science 8 (2014), 162–174, DOI:10.1016/j.jtusci.2013.08.002 (classical graph-enumeration comparison, not continuous cost optimization).
