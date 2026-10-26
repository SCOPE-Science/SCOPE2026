# Oscillatory critical logarithmic Bergman weights have an exact Hilbert-matrix essential norm

## Finding
Let \(a:[0,\infty)\to(0,\infty)\) be \(C^1\), satisfy \(0<c\le a(u)\le C<\infty\), and obey \(a'(u)\to0\). Set
\[
L(t)=1+\log\frac1{1-t},\qquad w(t)=L(t)^2a(\log L(t))^2,\quad 0\le t<1.
\]
For the Hilbert matrix \(H\), with \((Hf)_m=\sum_{n\ge0}f_n/(m+n+1)\), acting from the analytic weighted Bergman Hilbert space \(A^2_w\) into ordinary \(A^2\),
\[
\boxed{\|H:A^2_w\to A^2\|_{\mathrm{ess}}=2\limsup_{u\to\infty}\frac1{a(u)}=\frac2{\liminf_{u\to\infty}a(u)}.}
\]
In particular, the genuine nonconvergent multiplier \(a(u)=1+\frac14\sin\sqrt{u+1}\) gives the exact value \(8/3\). The operator is bounded and never compact under these hypotheses.

## Assumptions and scope
Area measure is normalized by \(dA(re^{i\theta})=r\,dr\,d\theta/\pi\). The input norm is \(\|f\|_{A^2_w}^2=\int_{\mathbb D}|f(z)|^2w(|z|^2)\,dA(z)\); the target is \(A^2=A^2_1\). The essential norm is the distance to compact linear operators between these two Hilbert spaces. The assumption \(a'(u)\to0\) is additive slow oscillation in the double-logarithmic variable, not convergence of \(a\). No assertion is made about the exact (unreduced) operator norm.

## Proof
**1. Normalize monomials and extract moments.** Write \(v_n=\int_0^1t^nw(t)\,dt\). Angular orthogonality gives the input orthonormal basis \(z^n/\sqrt{v_n}\) and the output orthonormal basis \(\sqrt{m+1}\,z^m\). Consequently the Hilbert-matrix operator has matrix
\[
K_{mn}=\frac1{(m+n+1)\sqrt{(m+1)v_n}},\qquad m,n\ge0.
\]
For \(n\to\infty\), a Laplace substitution \(y=n(1-t)\) gives, uniformly under the stated bounds on \(a\),
\[
v_n=\frac{(\log n)^2 a(\log\log n)^2}{n}\bigl(1+O(1/\log n)\bigr).
\]
To justify the error, on \(y\le n/2\) use \(L(1-y/n)=1+\log n-\log y\). The relative change of the squared-logarithm factor is \(O((1+|\log y|)/\log n)\), and boundedness of \(a'\), together with \(a\ge c\), yields the same bound for the multiplier, using \(|\log L-\log\log n|\le O((1+|\log y|)/\log n)\) on the central region. Integrate against the exponentially decaying Laplace kernel; \(\int_0^\infty e^{-y}(1+|\log y|+|\log y|^2)\,dy<\infty\). The complement of \(n^{-1/4}\le y\le n^{1/4}\) has power- or exponentially small contributions compared with \((\log n)^2/n\); changing the central cutoff slowly if necessary ensures all displayed estimates. Hence \(v_n^{-1/2}=\sqrt n/[\log n\,a(\log\log n)](1+O(1/\log n))\).

**2. A compact-error triangular model.** Delete the first three input and output coordinates, a finite-rank change. Put \(d_n=1/a(\log\log n)\). Define
\[
P_{mn}={\bf1}_{n\ge m}\frac1{\sqrt{mn}\log n},\qquad (P_d)_{mn}=P_{mn}d_n,\qquad m,n\ge3.
\]
Then \(K-P_d\) is Hilbert--Schmidt. For \(n<m\), the squared matrix entries of \(K\) are bounded by \(C n/(m^3\log^2n)\), giving the convergent sum \(\sum_n 1/(n\log^2n)\). For \(n\ge m\), the leading ratio of \(K_{mn}\) to \((P_d)_{mn}\) is \(n/(n+m)\) with an error bounded by \(C(1/m+1/\log n)\). Its squared difference is dominated by
\[
\frac{C}{mn\log^2n}\left((m/n)^2+m^{-2}+(\log n)^{-2}\right).
\]
Summing first in \(m\le n\) gives, respectively, \(O(1/(n\log^2n))\), \(O(1/(n\log^2n))\) and \(O(1/(n\log^3n))\), all summable. Therefore the normalized Hilbert matrix and \(P_d\) have identical essential norms, since Hilbert--Schmidt operators are compact.

**3. Sharp essential norm of the unweighted triangular tail.** Put \(h_j=(j\log j)^{-1/2}\), \(j\ge3\). On any common tail \(m,n\ge N\), the Schur ratios obey
\[
\frac{\sum_{n\ge m}P_{mn}h_n}{h_m}=\sqrt{\log m}\sum_{n\ge m}\frac1{n(\log n)^{3/2}}\longrightarrow2,
\]
\[
\frac{\sum_{m=N}^{n}P_{mn}h_m}{h_n}=\frac1{\sqrt{\log n}}\sum_{m=N}^{n}\frac1{m\sqrt{\log m}}\le2+o_N(1).
\]
Thus Schur's test gives \(\|Q_NPQ_N\|\le2+o_N(1)\), with \(Q_N\) the projection to coordinates \(j\ge N\). The discarded rows and columns are finite rank, so \(\|P\|_{\mathrm{ess}}\le2\).

For the lower bound let \(U,L>0\) and choose a finitely supported vector \(x_n=(n\log n)^{-1/2}\) when \(\log\log n\in[U,U+L]\), zero otherwise. Its squared norm is \(L+o_U(1)\) for fixed \(L\). On the same coordinate window, direct integral comparison gives
\[
(Px)_m=\frac{2+o_U(1)}{\sqrt{m\log m}}\bigl(1-e^{-(U+L-\log\log m)/2}\bigr)
\]
with an additive error negligible in the window's squared norm. Hence
\[
\liminf_{U\to\infty}\frac{\|Px\|_2^2}{\|x\|_2^2}\ge\frac4L\int_0^L(1-e^{-s/2})^2\,ds.
\]
Letting \(L\to\infty\) makes the right side tend to \(4\). The unit vectors drift to infinity and converge weakly to zero, so their images obstruct every compact approximation. Thus \(\|P\|_{\mathrm{ess}}=2\).

**4. Slowly oscillating multiplier.** Set \(D=\limsup_{u\to\infty}1/a(u)>0\). The upper estimate follows by deleting finitely many input coordinates and using \(\|P\|_{\mathrm{ess}}=2\): \(\|P_d\|_{\mathrm{ess}}\le2D\). For the reverse estimate choose any fixed window length \(L\) and a sequence \(U_k\to\infty\) at which \(1/a(U_k)\to D\). Since \(a'(u)\to0\) and \(a\) stays above \(c\), \(d_n\ge D-o_k(1)\) uniformly whenever \(\log\log n\in[U_k,U_k+L]\). Apply the nonnegative matrix \(P\) to the preceding nonnegative test vector. Positivity gives a lower bound \((D-o_k(1))\) times the unweighted output norm. After \(k\to\infty\) and \(L\to\infty\), \(\|P_d\|_{\mathrm{ess}}\ge2D\). Combining both bounds with the compact-error reduction proves the assertion.

## Verification
The proof includes explicit normalizations, moment error estimates, a summable square-entry bound for the compact perturbation, a two-sided Schur calculation and weakly null logarithmic-window test vectors. No finite computation or truncation is presented as a substitute for the operator-theoretic argument. For the oscillating example, \(\liminf a=3/4\), \(a'(u)=\cos\sqrt{u+1}/(8\sqrt{u+1})\to0\), and the formula yields exactly \(8/3\).

## Relationship to prior work
Norrbo (2026) proves boundedness at the pure logarithmic critical power and failure below that power. A previously published logarithmic-endpoint result computes essential norm \(2\) for the constant multiplier. The present two-weight result identifies the exact answer under an arbitrary nonconvergent positive slow modulation at the second logarithmic scale, showing that the essential norm measures a limiting lower envelope rather than an average. Lindström, Miihkinen and Norrbo (2022) treat generalized Hilbert matrix essential norms on the same weighted analytic space; their setting does not directly give this two-space logarithmic boundary formula. Existing oscillatory generalized Hilbert-matrix results on \(\ell^p\) concern coefficients in a distinct one-space kernel model, and do not explicitly imply the present two-weight critical Bergman formula.

## Limitations
The multiplier is assumed positive, bounded above and below, and differentiable with derivative tending to zero in the double-logarithmic scale. Rapid oscillations and multipliers approaching zero are not covered. The essential norm, not the exact operator norm, is determined. The proof is self-reviewed only, not independently audited; historical priority may require broader manual checking of two-weight Hardy--Copson results.

## References
- David Norrbo, *The Hilbert matrix operator into the Bergman space*, arXiv:2610.00252v1 (publicly posted 23 September 2026), https://arxiv.org/abs/2610.00252 .
- Mikael Lindström, Santeri Miihkinen and David Norrbo, *Exact essential norm of generalized Hilbert matrix operators on classical analytic function spaces*, arXiv:2201.09591v1 (2022), https://arxiv.org/abs/2201.09591 .
- *Exact essential norm at the logarithmic Bergman endpoint*, publicly indexed result, October 2026 (scientific comparison: pure critical logarithmic case).
- *Exact essential norm for slowly oscillating generalized Hilbert matrices on \(\ell^p\)*, publicly indexed result, October 2026 (scientific comparison: different kernel/space setting).
