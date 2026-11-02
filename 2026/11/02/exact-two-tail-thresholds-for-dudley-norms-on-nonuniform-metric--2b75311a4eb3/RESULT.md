# Exact two-tail thresholds for Dudley norms on nonuniform metric stars

## Finding
Let \(X=\{o,x_1,\ldots,x_n\}\) be a finite weighted metric star with \(n\ge1\), positive arm lengths \(r_i\), and distances \(d(o,x_i)=r_i\), \(d(x_i,x_j)=r_i+r_j\) when \(i\ne j\). Consider a real zero-total-mass measure
\[
\sigma=-\Bigl(\sum_{i=1}^n c_i\Bigr)\delta_o+\sum_{i=1}^n c_i\delta_{x_i}.
\]
For the **sum-normalized Dudley norm** \(\|f\|_{\mathrm{BL}}=\|f\|_\infty+\operatorname{Lip}(f)\), set
\[
P(b)=\sum_{c_i>0}c_i\min(r_i,b),\qquad
N(a)=\sum_{c_i<0}|c_i|\min(r_i,a).
\]
Then the exact dual norm is
\[
\boxed{\|\sigma\|_{\mathrm{BL}^*}=2\max_{a,b\ge0}\frac{P(b)+N(a)}{2+a+b}.}\tag{1}
\]
Define right-continuous, nonincreasing tail-intensity functions
\[
T_+(t)=\sum_{c_i>0:\ r_i>t}c_i,\qquad
T_-(t)=\sum_{c_i<0:\ r_i>t}|c_i| \quad(t\ge0).
\]
When \(\sigma\ne0\), there is a unique \(\gamma>0\) satisfying
\[
\boxed{\int_0^\infty(T_+(t)-\gamma)_+\,dt+
\int_0^\infty(T_-(t)-\gamma)_+\,dt=2\gamma,\quad
\|\sigma\|_{\mathrm{BL}^*}=2\gamma.}\tag{2}
\]
The integrals are finite sums over at most \(n\) constant-tail intervals. Write these intervals as pairs \((\ell_j,h_j)\) of positive width and tail height, sorted with \(h_1\ge\cdots\ge h_m>0\). Set
\[
A_k=\sum_{j\le k}\ell_j,\quad B_k=\sum_{j\le k}\ell_jh_j,\quad
\gamma_k=\frac{B_k}{2+A_k},\quad h_{m+1}=0.
\]
For at least one \(k\), \(h_{k+1}\le\gamma_k\le h_k\), and for every such \(k\), \(\gamma=\gamma_k\). Therefore the exact norm and a maximizing bounded-Lipschitz function are computable with \(O(n\log n)\) comparisons and arithmetic operations. For rational arm lengths and masses all computations, including the optimum, are rational.

The minimal optimal positive and negative caps are respectively
\[
b=\int_0^\infty\mathbf1_{\{T_+(t)>\gamma\}}\,dt,\qquad
a=\int_0^\infty\mathbf1_{\{T_-(t)>\gamma\}}\,dt.
\]
Consequently both signs have nonzero optimal caps precisely when \(T_+(0)>\gamma\) and \(T_-(0)>\gamma\); otherwise the minimum-cap optimizer is one-sided. Ties in the tail intensities may permit further optimizers but do not change the exact norm.

## Assumptions and scope
All distances \(r_i\) are strictly positive, the coefficients \(c_i\) are arbitrary real numbers, and the hub coefficient is minus their sum. The formulas include repeated radii, tied tail heights, zero coefficients and single-leaf stars. For the zero measure the norm is zero and formula (2) is replaced by \(\gamma=0\). The results concern real test functions and the sum norm, **not** the alternative maximum-type Fortet–Mourier normalization.

## Proof
**1. Reduction to two caps.** Let \(f\) have \(\|f\|_{\mathrm{BL}}\le1\). If its Lipschitz constant \(L\) vanishes, then \(\langle f,\sigma\rangle=0\). Otherwise put \(u=(f-f(o))/L\), so \(u(o)=0\) and \(\operatorname{Lip}(u)=1\). With \(a=-\min_Xu\) and \(b=\max_Xu\), both nonnegative, the arm constraints imply \(|u(x_i)|\le r_i\), whence
\[
\langle f,\sigma\rangle=L\sum_i c_i u(x_i)\le L[P(b)+N(a)].
\]
Moreover the range of \(f\) is \(L(a+b)\), so \(\|f\|_\infty\ge L(a+b)/2\). Therefore \(1\ge\|f\|_{\mathrm{BL}}\ge L(2+a+b)/2\), proving the upper bound (1).

Conversely fix arbitrary \(a,b\ge0\). Define \(u(o)=0\); set \(u(x_i)=\min(r_i,b)\) when \(c_i>0\), \(u(x_i)=-\min(r_i,a)\) when \(c_i<0\), and \(u(x_i)=0\) when \(c_i=0\). This is 1-Lipschitz on the star because its leaf-to-hub differences do not exceed \(r_i\), and any leaf-to-leaf difference is bounded by the sum of arm lengths. Its oscillation is at most \(a+b\). Subtract the midpoint of its actual range and multiply by \(2/(2+a+b)\). The resulting \(f\) satisfies \(\|f\|_\infty+\operatorname{Lip}(f)\le1\) and has pairing \(2[P(b)+N(a)]/(2+a+b)\). This proves (1) and exhibits an optimizer.

**2. Tail-root identity.** For any \(\gamma\ge0\), the numerator of (1) exceeds \(\gamma(2+a+b)\) at some caps exactly when
\[
\sup_{b\ge0}[P(b)-\gamma b]+\sup_{a\ge0}[N(a)-\gamma a]>2\gamma.
\]
Because \(P(b)=\int_0^bT_+(t)\,dt\) and \(N(a)=\int_0^aT_-(t)\,dt\), and both tails decrease, each supremum equals the integral of the positive part of its tail minus \(\gamma\). This establishes (2) at the optimal ratio. The left side of (2) minus \(2\gamma\) is continuous and strictly decreasing; when the measure is nonzero, its value at zero is positive and its value above both tail maxima is negative. Thus its root is unique. The displayed caps maximize the two independent concave expressions, proving the one-sided/two-sided criterion.

**3. Finite sort certificate.** Group the positive and negative leaf charges by increasing radius separately. On each consecutive radius interval the corresponding tail is constant, giving at most \(n\) positive-width positive-height pairs \((\ell_j,h_j)\). Sort all pairs by tail height. On \(h_{k+1}\le\gamma\le h_k\), equation (2) becomes \(B_k-\gamma A_k=2\gamma\). Its solution is \(\gamma=B_k/(2+A_k)\). The unique root belongs to at least one of these closed intervals, including all tie boundaries, proving the finite test and the operation count. Constructing the two caps and the normalized function from step 1 requires only another scan.

## Verification
A standalone exact-rational implementation in `verify_star.py` reconstructs (2) by sorting intervals, explicitly constructs norm-attaining functions, and checks their exact feasibility and value in 1,370 rational instances. A distinct linear-program formulation in the original vertex-function variables checks the norm against SciPy HiGHS in 916 additional cases (including repeated radii, vanishing charges and both sign patterns). These finite checks supplement rather than replace the proof above.

For instance, arm lengths \((1,2,4,7)\) with leaf coefficients \((2,-3,1,-1)\) give \(\gamma=11/5\), the minimal caps \(b=1\), \(a=2\), and \(\|\sigma\|_{\mathrm{BL}^*}=22/5\). Lengths \((3,1)\) with coefficients \((3,-1)\) give \(\gamma=9/5\) and a one-sided optimum \(\|\sigma\|_{\mathrm{BL}^*}=18/5\).

## Relationship to prior work
Hille and Theewis (arXiv:2206.12234, Sections 1 and 6) develop general finite-support Fortet–Mourier computations and an adapted linear-programming treatment of the Dudley norm. Their general method neither states the weighted-star two-tail formula nor the sorting certificate above. Their later work (arXiv:2305.08500) describes general norming and extremal bounded-Lipschitz functions, not the special geometry of heterogeneous arms. Sato, Yamada and Kashima (arXiv:2006.02703) give a quasi-linear tree algorithm for a different fixed-penalty unbalanced transport objective; this does not immediately yield the sum-normalized Dudley threshold, where the sup-bound and Lipschitz bound share a budget. A published calculation for equal-arm stars covers that specialization; no novelty is asserted for the equal-arm case. The new statement explicitly treats unequal arms and simultaneously supplies the threshold and an attaining test function.

## Limitations
No claim is made for arbitrary trees, nonzero-total-mass measures, a maximum-type test-function norm, or a faster-than-sorting algorithm. The published literature comparison does not establish historical priority with certainty: an equivalent formula under tree transport or flat-norm terminology could exist, and the full text of the equal-arm published note was not available for inspection. Real arithmetic complexity does not imply fixed-bit complexity for arbitrary real-valued input. No independent mathematical audit has been performed.

## References
1. R. Sato, M. Yamada and H. Kashima, *Fast Unbalanced Optimal Transport on a Tree*, arXiv:2006.02703, first publicly posted 4 June 2020. https://arxiv.org/abs/2006.02703
2. S. C. Hille and E. S. Theewis, *Explicit expressions and computational methods for the Fortet–Mourier distance to finite weighted sums of Dirac measures*, arXiv:2206.12234, first publicly posted 24 June 2022. https://arxiv.org/abs/2206.12234
3. S. C. Hille and E. S. Theewis, *Norming and dense sets of extreme points of the unit ball in spaces of bounded Lipschitz functions*, arXiv:2305.08500, first publicly posted 15 May 2023. https://arxiv.org/abs/2305.08500
4. *Exact Dudley norms and mass-imbalance thresholds on equiradial stars*, published online research note (2026); abstract inspected, full text not inspected.
