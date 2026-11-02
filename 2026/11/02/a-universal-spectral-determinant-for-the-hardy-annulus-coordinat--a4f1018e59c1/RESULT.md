# A universal spectral determinant for the Hardy-annulus coordinate commutator

## Finding
For the normalized Hardy space of every annulus \(A_r=\{z\in\mathbb C:r<|z|<1\}\), \(0<r<1\), let \(S_r=M_z\) and \(D_r=S_r^*S_r-S_rS_r^*\). Put \(q=r^2\). The positive trace-class operator \(D_r\) has precisely the eigenvalues
\[
\delta_k(q)=\frac{(1-q)^2q^k}{(1+q^k)(1+q^{k+1})},\qquad k=0,1,2,\ldots,
\]
each with multiplicity two, and no other nonzero spectral values. In particular, \(\operatorname{Tr}D_r=1-q\) and \(\|D_r\|=(1-q)^2/[2(1+q)]\).

As the annulus becomes thin (\(q\uparrow1\)), its complete nonzero spectral shape obeys the following three mutually consistent laws. For every real \(p>0\),
\[
\lim_{q\uparrow1}(1-q)^{1-2p}\operatorname{Tr}(D_r^p)
=B(p,p)=\frac{\Gamma(p)^2}{\Gamma(2p)}.
\]
For every real \(t\geq0\), the Fredholm determinant has the universal limit
\[
\boxed{\lim_{q\uparrow1}(1-q)\log\det\!\left(I+\frac{tD_r}{(1-q)^2}\right)
=\operatorname{arcosh}^{2}\!\left(1+\frac t2\right).}
\]
Finally, for each \(0<a<1/4\), the number \(N_q(a)\) of eigenvalues of \(D_r/(1-q)^2\) strictly exceeding \(a\), counted with multiplicity, satisfies
\[
\lim_{q\uparrow1}(1-q)N_q(a)
=4\operatorname{arcosh}\!\left(\frac1{2\sqrt a}\right).
\]
Equivalently, the rescaled spectral counting measures converge locally away from zero to the measure with density \(2/[y\sqrt{1-4y}]\) on \(0<y<1/4\). This density has infinite mass at zero, so the convergence is *vague*, not weak convergence of finite probability measures.

## Assumptions and scope
Give the annular Hardy Hilbert space the norm
\[
\left\|\sum_{n\in\mathbb Z}a_nz^n\right\|_r^2
=\sum_{n\in\mathbb Z}|a_n|^2(1+r^{2n}),
\]
corresponding to normalized angular measures of mass one on each boundary circle. The orthonormal Laurent basis is \(e_n(z)=z^n/(1+q^n)^{1/2}\). This normalization matters: differently weighted boundary components lead to different formulas. Every assertion concerns fixed \(0<q<1\), or the indicated one-sided limit \(q\uparrow1\); no uniformity is claimed in the exponent \(p\) or determinant parameter \(t\).

## Proof
**Exact spectrum.** On the Laurent basis, \(S_re_n=w_ne_{n+1}\) with
\[
w_n^2=\frac{1+q^{n+1}}{1+q^n}.
\]
Hence \(D_re_n=d_ne_n\), where direct subtraction gives
\[
d_n=w_n^2-w_{n-1}^2
=\frac{(1-q)^2q^{n-1}}{(1+q^{n-1})(1+q^n)}.
\]
The symmetry \(d_{1+k}=d_{-k}=\delta_k(q)\), for integers \(k\geq0\), proves the asserted multiplicity. The ratio
\[
\frac{\delta_{k+1}(q)}{\delta_k(q)}
=\frac{q(1+q^k)}{1+q^{k+2}}<1
\]
proves strict ordering. For each finite interval \([-N,N]\), the sum of the \(d_n\) telescopes to \(w_N^2-w_{-N-1}^2\). Its limit is \(1-q\), establishing positivity, trace class, the trace, and the maximal eigenvalue.

**Continuum limit.** Set \(h=-\log q>0\) and
\[
g_{q,k}=\frac{q^k}{(1+q^k)(1+q^{k+1})}.
\]
For fixed \(x\geq0\) with \(kh\to x\), \(g_{q,k}\to g(x)=e^{-x}/(1+e^{-x})^2=1/[4\cosh^2(x/2)]\). The bounds \(0\leq g_{q,k}\leq e^{-kh}\), \((1-q)/h\to1\), and geometric tail estimates justify Riemann-sum convergence for \(g_{q,k}^p\) whenever \(p>0\), and for \(\log(1+t g_{q,k})\) whenever \(t\geq0\). Exact double multiplicity then yields
\[
\begin{aligned}
\lim_{q\uparrow1}(1-q)^{1-2p}\operatorname{Tr}(D_r^p)
&=2\int_0^\infty g(x)^p\,dx\\
&=\int_{-\infty}^{\infty}g(x)^p\,dx
=\int_0^\infty \frac{u^{p-1}}{(1+u)^{2p}}\,du=B(p,p),
\end{aligned}
\]
where \(u=e^{-x}\) in the full-line integral.

**Determinant.** Trace class makes \(\det(I+tD_r/(1-q)^2)\) well defined and strictly positive for \(t\geq0\). Its eigenvalue-product logarithm converges to
\[
I(t)=\int_{-\infty}^{\infty}
\log\!\left(1+\frac{t}{4\cosh^2(x/2)}\right)\,dx.
\]
Differentiation under the integral (domination by \(g(x)\)) and the substitution \(v=\tanh(x/2)\) give, for \(t>0\),
\[
I'(t)=\int_{-1}^1\frac{2\,dv}{4+t(1-v^2)}
=\frac{4\operatorname{arsinh}(\sqrt{t}/2)}{\sqrt{t(t+4)}}.
\]
Integrating with \(I(0)=0\), we obtain \(I(t)=4\operatorname{arsinh}^2(\sqrt t/2)=\operatorname{arcosh}^2(1+t/2)\), including \(t=0\) by continuity.

**Counting.** For \(0<a<1/4\), the continuous profile \(g(x)\) is strictly decreasing on \(x>0\) and exceeds \(a\) exactly when \(|x|<2\operatorname{arcosh}(1/(2\sqrt a))\). The double lattice samples \(kh\), \(k\geq0\); counting points in this interval and using \((1-q)/h\to1\) gives the announced coefficient \(4\operatorname{arcosh}(1/(2\sqrt a))\). Differentiating this upper-tail function produces the claimed density.

## Verification
The standalone standard-library checker `check.py` verifies the exact rational weight-difference identity and spectral reflection, strict monotonicity, exact finite telescoping, and numerical approaches of the Schatten moments and determinant to their proven limits. It reports 137 passed checks. These tests cannot prove the infinite-dimensional conclusions; the proof above supplies the required tail bounds, quantifiers, and analytic integrations.

## Relationship to prior work
Das and Narayanan (2025) specify this annular Hardy norm and its Laurent basis, and investigate Toeplitz zero products and Hankel compactness rather than the spectrum of the coordinate self-commutator. Douglas and Kim (2009) study reducing subspaces for the corresponding annular multiplication shifts. Parker (2025) obtains commutator trace formulas for a class of unilateral disk shifts, a distinct geometry. The new quantitative contribution is the full thin-annulus spectral law: all positive real Schatten moments, an explicit limiting logarithmic Fredholm determinant, and exact level-set counting coefficients. Knowing the scalar trace or the weights alone does not state these global limiting laws.

## Limitations
The claim is for one canonical choice of boundary normalization and the coordinate symbol only; it does not cover arbitrary annular Toeplitz symbols. The convergence is pointwise in fixed \(p>0\), \(t\geq0\), and \(0<a<1/4\), not uniform over these parameters. No statement is made at spectral threshold zero, where the limiting density has infinite total mass, nor is an individual-eigenvalue asymptotic at a variable index proved beyond the explicit exact formula. Historical-priority assessment is based on inspected accessible literature and indexed comparisons; an older implicit equivalent formulation cannot be excluded.

## References
1. Susmita Das and E. K. Narayanan, *Zero Products of Toeplitz operators on the Hardy and Bergman spaces over an annulus*, arXiv:2504.04270v1 (first public April 5, 2025); New York Journal of Mathematics 31 (2025), 984–1001. https://arxiv.org/abs/2504.04270
2. Ronald G. Douglas and Yun-Su Kim, *Reducing Subspaces on the Annulus*, arXiv:0902.1794 (2009). https://arxiv.org/abs/0902.1794
3. Nathan Parker, *Commutators of the Unilateral Shift and Adjoint for Reproducing Kernel Hilbert Spaces on the Disk*, arXiv:2508.02896v1 (2025). https://arxiv.org/abs/2508.02896
4. Joshua M. Tattersall, *Toeplitz and Hankel operators on Hardy spaces of complex domains*, University of Leeds PhD thesis (2015). https://etheses.whiterose.ac.uk/id/eprint/11498/
