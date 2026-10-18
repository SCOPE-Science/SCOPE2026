# Sharp three-regime sparsification of the weighted Schatten-fourth radius on a four-cycle

## Finding
For real \(0\le t\le1\), let \(w=(w_0,w_1,w_2,w_3)\in[0,\infty)^4\) satisfy \(\sum_{j=0}^{3}w_j^2=1\). Define the complex-Hilbert-space cyclic shift \(S_we_j=w_je_{j+1\pmod4}\), the unnormalized Schatten-fourth norm \(\|M\|_4^4=\operatorname{tr}((M^*M)^2)\), and
\[
\mathcal W_{t,4}(S_w)=\sup_{\theta\in\mathbb R}\|t e^{i\theta}S_w+(1-t)e^{-i\theta}S_w^*\|_4.
\]
Put \(A=t^4+(1-t)^4\), \(B=4t^2(1-t)^2\), and \(\beta=B/A\in[0,2]\). The **exact global minimum** over this normalized positive four-cycle family is
\[
\boxed{\min_w\mathcal W_{t,4}(S_w)^4=\begin{cases}
A/4+3B/8,&0\le\beta\le1/2,\\[2pt]
A-(2A-B)^2/(6A-4B),&1/2\le\beta\le1,\\[2pt]
A/2,&1\le\beta\le2.
\end{cases}}
\tag{1}
\]
The transition thresholds, on \(0\le t\le1/2\), are
\[
\boxed{t_1=\frac{\sqrt{4-\sqrt{15}}}{1+\sqrt{4-\sqrt{15}}},\qquad
 t_2=\frac{\sqrt{2-\sqrt3}}{1+\sqrt{2-\sqrt3}}}.\tag{2}
\]
The same transitions occur at \(1-t_2\) and \(1-t_1\). All minimizers, expressed in squared weights \(x_j=w_j^2\), are as follows (always allowing cyclic rotations):

* For \(0\le\beta<1/2\), only \((1/4,1/4,1/4,1/4)\).
* At \(\beta=1/2\), both the uniform vector and the cyclic rotations of \((3/8,1/4,3/8,0)\), and no others.
* For \(1/2<\beta<1\), only the cyclic rotations of \((u/2,1-u,u/2,0)\), where \(u=(2-\beta)/(3-2\beta)\).
* For \(1\le\beta\le2\), only the cyclic rotations of \((1/2,0,1/2,0)\).

In particular, under the strict positivity condition \(w_j>0\), the minimum is attained precisely for \(\beta\le1/2\), and the infimum for all other parameters is the same value but is not attained.

## Assumptions and scope
The Hilbert space is \(\mathbb C^4\), with the standard orthonormal basis indexed cyclically by \(0,1,2,3\). The matrix \(S_w\) has edges along the directed four-cycle, including the closing edge \(3\to0\); this is **not** a nilpotent path shift. Weights are real and nonnegative, zeros are allowed, and the Hilbert--Schmidt normalization \(\|S_w\|_2^2=\sum w_j^2=1\) is fixed. The weighted Schatten numerical radius uses the *unscaled* Schatten-fourth norm. No assertion about the operator-norm numerical radius, arbitrary matrices, or other Schatten exponents is made.

## Proof
**Exact phase-dependent trace.** Put \(s=1-t\), \(x_j=w_j^2\), and \(M_\theta=t e^{i\theta}S_w+s e^{-i\theta}S_w^*\). Its Gram matrix \(G_\theta=M_\theta^*M_\theta\) has diagonal
\[
(G_\theta)_{jj}=t^2x_j+s^2x_{j-1},
\]
indices being modulo \(4\). Its two distinct opposite-corner entries are sums of two length-two paths. Expanding \(\sum_{j,k}|(G_\theta)_{jk}|^2\), their interference term is \(8t^2s^2w_0w_1w_2w_3\cos(4\theta)\), while the remaining terms are \(A\sum_jx_j^2+B\sum_jx_jx_{j+1}\). Therefore
\[
\|M_\theta\|_4^4=A\sum_jx_j^2+B\sum_jx_jx_{j+1}
 +2B\sqrt{x_0x_1x_2x_3}\cos(4\theta).
\]
Since \(B\ge0\), the supremum is attained when \(\cos(4\theta)=1\) (arbitrarily if the product is zero), and
\[
\boxed{\mathcal W_{t,4}(S_w)^4=A\sum_jx_j^2+B\sum_jx_jx_{j+1}
 +2B\sqrt{x_0x_1x_2x_3}.}\tag{3}
\]
The special four-cycle interference term in (3) is absent for nilpotent one-step shifts.

**Two-parameter reduction.** Write \(v=1-u\) and
\[
u=x_0+x_2,\qquad v=x_1+x_3,\qquad p=\sqrt{x_0x_2},\qquad q=\sqrt{x_1x_3}.
\]
Then \(0\le u\le1\), \(0\le p\le u/2\), \(0\le q\le v/2\), and every such quadruple is realized by some nonnegative weights. Formula (3) becomes
\[
F=A(u^2+v^2-2p^2-2q^2)+Buv+2Bpq.\tag{4}
\]
For \(\beta<2\), the Hessian in \((p,q)\) is \(\begin{pmatrix}-4A&2B\\2B&-4A\end{pmatrix}\), strictly negative definite. Thus **every** minimizer lies at a rectangle corner \((p,q)\in\{0,u/2\}\times\{0,v/2\}\) (including degenerate rectangles). By exchanging the two parity classes, the corner types reduce to three competitors:

1. Both parities balanced, \(p=u/2\), \(q=v/2\): \(F=A/2+(3B/2-A)uv\). Its minimum is \(U=A/4+3B/8\) for \(\beta\le2/3\), and \(A/2\) for \(\beta\ge2/3\). In the former case, the unique optimal split is \(u=v=1/2\), except at the irrelevant equality \(\beta=2/3\).
2. Exactly one parity balanced, \(p=u/2\), \(q=0\): \(F=A[u^2/2+(1-u)^2]+Bu(1-u)\). For \(\beta<1\), its unique minimum occurs at \(u=(2-\beta)/(3-2\beta)\), yielding \(R=A-(2A-B)^2/(6A-4B)\). For \(\beta\ge1\), its minimum is \(A/2\), attained at \(u=1\) (this follows directly by comparing the derivative and endpoint values even when the quadratic becomes concave).
3. Neither parity balanced, \(p=q=0\): \(F=A(u^2+v^2)+Buv\). Its minimum for \(0\le\beta\le2\) is at least \(A/2\), with equality only at an endpoint or the \(\beta=2\) degeneracy, and hence cannot improve on case 2.

For \(0\le\beta<1\), direct algebra gives
\[
\frac{R-U}{A}=-\frac{(\beta-2)(2\beta-1)}{8(2\beta-3)},\qquad
\frac{R-A/2}{A}=\frac{(\beta-1)^2}{2(2\beta-3)}<0.\tag{5}
\]
Thus \(U<R\) for \(\beta<1/2\), \(U=R\) at \(\beta=1/2\), and \(R<U\) for \(1/2<\beta<1\). All other branches are strictly larger than the indicated global minimum except where the stated limiting profiles coincide. Strict concavity in (4), plus the strict one-variable minima, yields the **complete** listed optimizer classes, including the coexistence at the first transition and the unique opposite-pair class at the second.

**Degenerate endpoint \(\beta=2\).** This occurs only at \(t=1/2\). Equation (4) reduces exactly to \(F/A=1-2(p-q)^2\). The bounds \(0\le p\le u/2\) and \(0\le q\le(1-u)/2\) imply \(|p-q|\le1/2\), with equality only when one parity has total mass one, equally divided between its opposite edges, and the other parity has mass zero. Hence \(\min F=A/2\), with precisely the stated two opposite-edge classes. This covers all parameters.

Finally, set \(z=t/(1-t)\) for \(0\le t\le1/2\). Then \(\beta=4z^2/(1+z^4)\). Solving \(\beta=1/2\) and \(\beta=1\) gives respectively \(z^2=4-\sqrt{15}\) and \(z^2=2-\sqrt3\); this proves (2). The problem is unchanged by replacing \(t\) by \(1-t\). At \(\beta>1/2\), every global minimizer has a zero component and can be approximated by strictly positive weight vectors, proving the final strict-positivity assertion.

## Verification
The companion standard-library script `verify_cycle.py` recomputes the unphased fourth Schatten trace from exact rational \(4\times4\) matrix multiplication for 648 rational test cases, agrees exactly with the right side of (3) at \(\theta=0\), verifies rational branch comparisons, and tests the claimed lower bound on a finite rational simplex grid. These finite tests are **not** the proof of the phase maximization, continuum optimum, or equality classification; the analytic argument above proves those conclusions. Independently, dense continuous numerical optimization and singular-value calculations were compared with (1) and (3) for twelve parameter choices in \([0,1]\), including both transition regions. The checker is self-contained; run `python verify_cycle.py` alongside this document.

## Relationship to prior work
Pal and Chandok's October 8, 2026 paper defines exactly the weighted Schatten \(p\)-numerical radius used here and derives generalized-Aluthge upper bounds (notably its Theorems 2.1–2.10 and examples). Inspection of its full publicly accessible HTML, including the fourth-power inequalities in Theorem 2.7, found no minimization over positive four-cycle weights at fixed Hilbert–Schmidt mass and no three-regime optimizer classification. The published result *Sharp weighted Schatten-fourth radii of nilpotent shifts* determines a path-shift fourth-moment identity and **maximization** at fixed Schatten-fourth energy; a genuine four-cycle has an additional winding interference term, and the present problem is a **minimum** at fixed Schatten-second energy. Neither assertion implies (1) or the optimizer transitions. Earlier fixed-weight rearrangement papers study the usual operator-norm numerical radius, not the weighted Schatten-fourth minimum. Searches for cycle aliases and exact matrix inequalities identified no published covering result; this is not a proof of absolute novelty.

## Limitations
The theorem treats only positive real weights on a four-cycle, Schatten exponent four, and fixed squared-weight sum one. It does not classify complex edge-phase fluxes (which can affect the winding term), longer cycles, the classical operator-norm radius, or alternative normalization. Finite computational checks provide supporting diagnostics only. Unindexed identical results, broad matrix-optimization statements specialized to this case, and new or inaccessible literature remain genuine priority risks. No independent external audit has been carried out.

## References
1. K. Pal and S. Chandok, *On weighted Schatten p-numerical radii via generalized Aluthge transformation*, arXiv:2610.11336v1 (public October 8, 2026), https://arxiv.org/html/2610.11336v1.
2. *Sharp weighted Schatten-fourth radii of nilpotent shifts*, public research record (October 11, 2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-sharp-weighted-schatten-fourth-radii-of-nilpotent-shifts--17db4dbf42a4.
3. S. Sahoo, *Further bounds on p-numerical radii of operators via generalized Aluthge transform*, arXiv:2504.04693v1 (2025), https://arxiv.org/abs/2504.04693.
