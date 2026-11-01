# Sharp fractional-boundary zero transition for meromorphic weighted Bergman kernels

## Finding

Fix \(-1<\alpha<0\), put \(\theta=\alpha+1\in(0,1)\), and let \(m\in\{0,1,2,\ldots\}\). For each origin-weight exponent \(m-1<\eta<m\) with \(\eta>-1\), write \(b=m-\eta\in(0,1)\). The scalar reproducing kernel of the meromorphic weighted Bergman space defined below has either no zeros or exactly one **scalar zero fibre**, and this alternative is governed by a unique explicit threshold \(b_*(\theta)\in(0,1)\):

\[
 {}_2F_1(-\theta,-b_*(\theta);1-b_*(\theta);-1)=0.
\]

For \(0<b\le b_*(\theta)\), the kernel is zero-free on \((\mathbb D^*)^2\). For \(b_*(\theta)<b<1\), all its zeros satisfy \(z\overline w=-r_{\theta,b}\), where \(0<r_{\theta,b}<1\), and the scalar root \(-r_{\theta,b}\) is unique, real negative, and simple. Moreover \(r_{\theta,b}\) is strictly decreasing in \(b\), with \(r_{\theta,b}\to1\) as \(b\downarrow b_*(\theta)\) and \(r_{\theta,b}\to0\) as \(b\uparrow1\). The root crosses the unit circle transversally at the threshold.

## Assumptions and scope

Let \(\mathbb D^*=\{z\in\mathbb C:0<|z|<1\}\) and let \(dA=\pi^{-1}dx\,dy\) be normalized area. On \(\mathbb D\) use the probability measure
\[
 d\mu_{\alpha,\eta}(z)=\frac{|z|^{2\eta}(1-|z|^2)^\alpha}{B(\alpha+1,\eta+1)}\,dA(z),
\]
where \(B\) is Euler's beta function. The Hilbert space is the holomorphic functions on \(\mathbb D^*\) with finite squared norm in this measure. Its orthogonal monomial basis comprises \(z^k\) for integers \(k\ge-m\); each squared monomial norm is \(B(\theta,k+\eta+1)/B(\theta,\eta+1)\).

For \(\zeta=z\overline w\ne0\), define the analytic numerator
\[
 Q_{\theta,b}(\zeta)={}_2F_1(-\theta,-b;1-b;\zeta),
\]
so that the *actual normalized reproducing kernel* is
\[
 K_{\alpha,\eta}(z,w)=\frac{B(\theta,\eta+1)}{B(\theta,1-b)}\,
 \zeta^{-m}\frac{Q_{\theta,b}(\zeta)}{(1-\zeta)^{1+\theta}}.
\]
Both the positive beta factor and the other displayed factors are nonvanishing for \(0<|\zeta|<1\). The zero classification is therefore precisely the scalar classification of \(Q_{\theta,b}\), with zeros understood as fibres of the product map, not individual pairs \((z,w)\). The theorem concerns the full real strip \(-1<\alpha<0\), not the nonnegative-integer exponents considered in the focal paper's complete polynomial classification.

## Proof

**1. Kernel formula.** The orthogonal monomial expansion gives
\[
 K_{\alpha,\eta}(z,w)=B(\theta,\eta+1)\,\zeta^{-m}
 \sum_{n=0}^\infty\frac{\zeta^n}{B(\theta,n+1-b)}.
\]
The ratio of the \(n\)-th summand to the constant term is \((\theta+1-b)_n/(1-b)_n\). Consequently the inner power series is \({}_2F_1(\theta+1-b,1;1-b;\zeta)/B(\theta,1-b)\). Euler's hypergeometric transformation changes this to \((1-\zeta)^{-1-\theta}{}_2F_1(-\theta,-b;1-b;\zeta)/B(\theta,1-b)\), proving the displayed kernel formula.

**2. Positive Pick representation.** For every integer \(n\ge1\), the coefficient of \(\zeta^n\) in \(Q_{\theta,b}\) equals
\[
 A_n=\frac{b}{n-b}(-1)^{n+1}\binom\theta n>0.
\]
The reflection identity and a beta integral give the *exact* positive representation
\[
 (-1)^{n+1}\binom\theta n=
 \frac{\sin(\pi\theta)}\pi\int_0^1 x^{n-\theta-1}(1-x)^\theta\,dx.
\]
Also \((n-b)^{-1}=\int_0^1u^{n-b-1}du\). Thus the finite positive measure \(\nu_{\theta,b}\) defined by pushing forward
\[
 \frac{b\sin(\pi\theta)}\pi\,x^{-\theta}(1-x)^\theta u^{-b}\,dx\,du
\]
under \((x,u)\mapsto t=xu\) satisfies \(A_n=\int_0^1 t^{n-1}d\nu_{\theta,b}(t)\). Absolute convergence for \(|\zeta|<1\) yields
\[
 Q_{\theta,b}(\zeta)=1+\int_0^1\frac{\zeta}{1-t\zeta}\,d\nu_{\theta,b}(t).
\]
The measure has positive mass \(\nu_{\theta,b}([0,1])=b\theta/(1-b)\), so for \(\operatorname{Im}\zeta\ne0\),
\[
 \operatorname{Im}Q_{\theta,b}(\zeta)=
 \operatorname{Im}\zeta\int_0^1\frac{d\nu_{\theta,b}(t)}{|1-t\zeta|^2}\ne0.
\]
Every zero in \(\mathbb D\) is thus real; \(Q_{\theta,b}(x)>1\) for \(x\in(0,1)\). On \([-1,0]\),
\[
 \frac{d}{dx}Q_{\theta,b}(x)=
 \int_0^1(1-tx)^{-2}\,d\nu_{\theta,b}(t)>0,
\]
so at most one negative zero occurs, and any such zero is simple.

**3. Exact transition.** Evaluating at \(-1\), set
\[
 L_\theta(b)=\frac{b\sin(\pi\theta)}\pi
 \int_0^1\!\int_0^1\frac{x^{-\theta}(1-x)^\theta u^{-b}}{1+xu}\,dx\,du.
\]
Then \(Q_{\theta,b}(-1)=1-L_\theta(b)\). For fixed \(0<u\le1\), the factor \(b u^{-b}\) has strictly positive derivative \(u^{-b}(1-b\log u)\); dominated convergence on every compact subinterval of \((0,1)\) proves continuity and strict increase of \(L_\theta\). It tends to \(0\) as \(b\downarrow0\) and to infinity as \(b\uparrow1\): the latter follows by bounding \((1+xu)^{-1}\ge1/2\) and noting \(\int_0^1u^{-b}du=(1-b)^{-1}\). Therefore exactly one \(b_*\in(0,1)\) solves \(L_\theta(b_*)=1\).

Since \(Q_{\theta,b}(0)=1\) and \(Q_{\theta,b}\) is strictly increasing on \([-1,0]\), it has an interior negative root exactly when \(Q_{\theta,b}(-1)<0\), equivalently \(b>b_*\). At equality the unique negative real root is \(-1\), outside the open product disk. When \(b>b_*\), the value at each fixed negative \(x\) strictly decreases with \(b\), because its integral integrand is negative and the measure density increases pointwise. Hence the unique root moves strictly right, so \(r_{\theta,b}\) decreases. Continuity and uniqueness force the endpoints \(r\to1\) as \(b\downarrow b_*\), \(r\to0\) as \(b\uparrow1\) (the latter also follows from the increasing first coefficient \(A_1=b\theta/(1-b)\)). Finally \(\partial_bQ_{\theta,b}(-1)=-L'_\theta(b)<0\), and \(\partial_\zeta Q_{\theta,b}(-1)>0\). The implicit-function theorem gives \(d\zeta/db>0\) at \(b=b_*\), proving transversality.

## Verification

The accompanying self-contained `checker.py` evaluates the hypergeometric kernel against its beta-moment series, tests the integral-sign and transition identities and computes representative critical parameters with high-precision arithmetic. A successful run produced 60 finite numerical checks and, for \(\theta=1/2\), the value \(b_*(1/2)\approx0.67764561954752760836\). These calculations do not replace the above infinite-dimensional and entire-parameter proof.

## Relationship to prior work

Ghiloufi and Snoun [1] give the kernel expansion for general radial power weights and study zero distributions, principally for nonnegative integer boundary exponents. Their general theorem gives near-endpoint root information but not a complete fractional-negative-exponent threshold. The present classification concerns \(-1<\alpha<0\), derives a positive Stieltjes/Pick integral for the hypergeometric numerator, and resolves its entire zero geometry and exact threshold for every allowed origin exponent. Ghiloufi and Zaway [2] establish the underlying meromorphic Bergman-space setting. A general zero-construction theory [3] does not identify these exact roots. No priority claim stronger than the specified comparison is made.

## Limitations

The conclusion is restricted to \(-1<\alpha<0\) and the specified radial power weight; it gives exactly one *scalar product zero* when zeros occur, not one point of the two-variable kernel zero set. The threshold is characterized by a convergent special-function equation rather than an elementary closed form. Existing general complex-analysis or weighted-kernel results may contain an equivalent classification not located here. Numerical checks are finite. No independent mathematical validation has been undertaken.

## References

[1] N. Ghiloufi and S. Snoun, *Zeros of new Bergman kernels*, arXiv:2009.04307 (initial public version September 9, 2020), https://arxiv.org/html/2009.04307v1 .

[2] N. Ghiloufi and M. Zaway, *Meromorphic Bergman spaces*, arXiv:2309.00552 (initial arXiv version September 1, 2023), https://arxiv.org/html/2309.00552v1 .

[3] A. Perälä, *On the zeros of weighted Bergman kernels*, arXiv:1703.05976 (2017), https://arxiv.org/abs/1703.05976 .
