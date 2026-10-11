# Phase-velocity thresholds for Cesàro commutators with oscillatory multipliers

## Finding
On the complex Hilbert space \(L^2(0,1)\), consider the real-variable Cesàro operator
\[
(Cf)(x)=\frac1x\int_0^x\frac{f(t)}{1-t}\,dt.
\]
Write \(\ell(x)=\log(x/(1-x))\). Let \(\Phi:\mathbb R\to\mathbb R\) be constant on \(( -\infty,0]\), locally absolutely continuous on \(\mathbb R\), and twice continuously differentiable on \((0,\infty)\). Suppose \(v(s)=\Phi'(s)>0\) for all sufficiently large \(s\), and \(v\) is eventually monotone. Let \(L=\lim_{s\to\infty}v(s)\in[0,\infty]\). If \(L=0\), also suppose that \(v(s+t)/v(s)\to1\) for each fixed \(t\ge0\). Define the unimodular multiplier \(b_\Phi(x)=\exp(i\Phi(\ell(x)))\) and its commutator
\[
K_\Phi=M_{b_\Phi}C-CM_{b_\Phi}.
\]
Then the following are exact:
\[
K_\Phi\text{ is compact}\quad\Longleftrightarrow\quad L=0,
\]
\[
K_\Phi\in\mathcal S_2\quad\Longleftrightarrow\quad L=0\ \text{and}\ \int_1^\infty v(s)^2\,ds<\infty.
\]
When \(L=0\), the localized squared-kernel density satisfies
\[
J_\Phi(s):=\int_0^\infty e^{-t}|e^{i\Phi(s+t)}-e^{i\Phi(s)}|^2\,dt
\sim 2v(s)^2\qquad(s\to\infty).
\]
In particular, for every \(\theta>0\) put \(\Phi_\theta(s)=(1+\max\{s,0\})^\theta\). The commutator is Hilbert--Schmidt exactly when \(0<\theta<1/2\), compact but not Hilbert--Schmidt exactly when \(1/2\le\theta<1\), and noncompact exactly when \(\theta\ge1\). Define the truncated Hilbert--Schmidt energy (which does not assert ideal membership)
\[
E_\theta(R)=\int_0^R\!\int_0^\infty e^{-t}\left|e^{i\Phi_\theta(s+t)}-e^{i\Phi_\theta(s)}\right|^2\,dt\,ds.
\]
Then \(E_{1/2}(R)\sim\tfrac12\log R\), and for \(1/2<\theta<1\),
\[
E_\theta(R)\sim\frac{2\theta^2}{2\theta-1}R^{2\theta-1}.
\]
Thus two distinct sharp thresholds occur within a natural family of bounded unimodular multipliers, each of which oscillates infinitely often toward the endpoint \(x=1\).

## Assumptions and scope
All operators act on the complex Hilbert space \(L^2(0,1)\). The operator \(C\) is bounded, and every multiplier \(M_{b_\Phi}\) is unitary. The function \(\Phi\) may have a corner at zero; its local absolute continuity ensures an integrable derivative on every compact interval, even if its derivative is not locally square-integrable at zero. The Hilbert--Schmidt criterion concerns only the tail \(s\ge1\). Eventual monotonicity and positivity refer to the phase velocity \(v=\Phi'\), not to the phase multiplier. The additional ratio hypothesis in the zero-speed case is essential to the stated pointwise density asymptotic; no conclusion is claimed for arbitrary irregular velocities.

## Proof
**1. Exact kernel.** Set \(x(s)=e^s/(1+e^s)\). The map
\[
(Uf)(s)=\sqrt{x(s)(1-x(s))}\,f(x(s))
\]
is unitary from \(L^2(0,1)\) onto \(L^2(\mathbb R)\), since \(x'(s)=x(s)(1-x(s))\). Changing variables in the defining integral yields the exact identity
\[
(UCU^{-1}g)(s)=\int_{-\infty}^s e^{-(s-r)/2}g(r)\,dr=:Rg(s).
\]
Writing \(F(s)=e^{i\Phi(s)}\), the transported commutator \(UK_\Phi U^{-1}=[M_F,R]\) has measurable kernel
\[
\mathbf1_{r<s}e^{-(s-r)/2}(F(s)-F(r)).
\]
Consequently the Hilbert--Schmidt criterion and norm, when finite, are exactly
\[
\|K_\Phi\|_{\mathcal S_2}^2=\int_{-\infty}^{\infty}\int_0^\infty e^{-t}|F(s+t)-F(s)|^2\,dt\,ds.
\]
The portion with \(s<0\) is finite: its integrand vanishes for \(t\le-s\), and its contribution is at most \(4\int_0^\infty te^{-t}dt=4\). Finite portions with \(s\ge0\) are similarly harmless. Thus Hilbert--Schmidt membership is controlled by the tail density \(J_\Phi(s)\).

**2. Zero-speed density asymptotic.** If \(L=0\), eventual monotonicity forces \(v\) to decrease. Put \(d_s(t)=\int_0^t v(s+u)\,du\). The ratio assumption and monotonicity give \(d_s(t)/v(s)\to t\) for every fixed \(t\ge0\), with \(0\le d_s(t)/v(s)\le t\). Since \(|e^{iy}-1|\le|y|\), dominated convergence with majorant \(e^{-t}t^2\) gives
\[
\lim_{s\to\infty}\frac{J_\Phi(s)}{v(s)^2}
=\int_0^\infty e^{-t}t^2dt=2.
\]
The nonnegative kernel norm formula now proves the Hilbert--Schmidt equivalence when \(L=0\).

**3. Compactness at zero speed.** For \(R>0\), freeze \(F\) to its constant value \(F(R)\) to the right of \(R\), leaving it unchanged on the left, and call the result \(F_R\). The derivative \(F_R'\) has compact support. For each \(u\), the rank-one operator with kernel
\[
e^{-s/2}\mathbf1_{s>u}\,e^{r/2}\mathbf1_{r<u}
\]
has trace norm exactly one, because the two factor norms are \(e^{-u/2}\) and \(e^{u/2}\). Integrating these rank-one kernels against \(F_R'(u)\,du\) proves
\[
\|[M_{F_R},R]\|_{\mathcal S_1}\le\int_{\mathbb R}|F_R'(u)|\,du<\infty.
\]
On the other hand, \(D_R=F-F_R\) is globally Lipschitz with constant at most \(\sup_{s\ge R}v(s)\to0\). Young's inequality applied to the kernel estimate
\[
|D_R(s)-D_R(r)|e^{-(s-r)/2}\mathbf1_{r<s}\le \sup_{u\ge R}v(u)\,(s-r)e^{-(s-r)/2}\mathbf1_{r<s}
\]
gives \(\|[M_{D_R},R]\|\le4\sup_{s\ge R}v(s)\), because \(\int_0^\infty te^{-t/2}dt=4\). Hence the commutator is a norm limit of trace-class operators and is compact.

**4. Noncompactness at nonzero speed.** If \(L=a\in(0,\infty)\), use the unit vectors \(g_n(r)=e^{-i\Phi(r)}\mathbf1_{[n,n+1]}(r)\), which converge weakly to zero. For \(s=n+t\), \(0<t<1\), the commutator outputs converge in \(L^2(0,1)\) after translation to
\[
H_a(t)=\int_0^t e^{-(t-u)/2}\left(e^{ia(t-u)}-1\right)\,du.
\]
This is not zero: its small-\(t\) expansion is \(H_a(t)=iat^2/2+O(t^3)\). Therefore the images cannot tend to zero in norm, contradicting compactness.

If \(L=\infty\), \(v\) eventually increases and \(v(n)\to\infty\). On \([n,n+1]\), integration by parts against the phase \(e^{-i\Phi(r)}\) and the monotone derivative \(v\) gives uniformly
\[
\left|R(e^{-i\Phi}\mathbf1_{[n,n+1]})(s)\right|\le\frac{4}{v(n)},\quad n\le s\le n+1.
\]
The bound follows by differentiating \(e^{-(s-r)/2}/v(r)\): its boundary terms cost at most \(2/v(n)\), its exponential-amplitude derivative costs at most \(1/v(n)\), and the derivative of \(1/v\) costs at most \(1/v(n)\). Yet \(R(Fg_n)=R\mathbf1_{[n,n+1]}\) equals \(2(1-e^{-(s-n)/2})\) on this interval, with a fixed positive \(L^2\)-norm. Thus again the commutator maps weakly null unit vectors to vectors bounded away from zero in norm and is noncompact.

**5. Power-chirp thresholds and coefficients.** On \(s>0\), \(v_\theta(s)=\theta(1+s)^{\theta-1}\). If \(0<\theta<1\), its ratio at any fixed displacement tends to one. It is square-integrable precisely for \(\theta<1/2\). At \(\theta=1\) it tends to one, and for \(\theta>1\) it tends to infinity; these cases are noncompact by Step 4. For \(0<\theta<1\), Step 2 yields \(J_{\Phi_\theta}(s)\sim2\theta^2(1+s)^{2\theta-2}\). Integrating this asymptotic over \([0,R]\) gives the stated logarithmic and power-law growth, including the coefficient \(1/2\) at \(\theta=1/2\).

## Verification
The derivation is analytic and does not rely on finite sampling. A standalone `verify_chirp.py` performs reproducible quadrature diagnostics of the asymptotic density at three exponents below one and the exact \(\theta=1\) kernel integral. Its finite numerical checks are illustrative only, not an infinite-dimensional proof. The sharp boundaries \(\theta=1/2\) and \(\theta=1\) follow from Steps 2--5.

## Relationship to prior work
Belli, Gül, Ross and Siskakis identified the real-variable Cesàro operator and its unitary exponential-convolution representation, and established its spectral structure; that representation and its normalization are used, not claimed as new. The contribution here is the phase-velocity compactness/Hilbert--Schmidt classification, the three-region power-chirp example, and the exact critical divergence law. Classical convolution-commutator compactness theory, including the work of Karlovich, is relevant to the compactness direction; it does not, from the accessible examined statements, supply the explicit Hilbert--Schmidt threshold and logarithmic coefficient. More general ideal criteria could potentially encompass parts of the argument.

## Limitations
No classification in the trace class or in \(\mathcal S_r\) for \(r\ne2\) is asserted. No result is claimed for highly irregular or sign-changing phase speeds outside the stated hypotheses. The truncation energy is not the full Hilbert--Schmidt norm when the latter diverges; it is an exact restricted nonnegative integral measuring the source of divergence. General background commutator results may imply portions of the compactness statement; an older relevant article could not be inspected in full and remains a literature risk. Independent evaluation has not been carried out.

## References
1. A. Belli, U. Gül, W. T. Ross and A. G. Siskakis, *Crescents and the real variable Cesàro operator*, arXiv:2606.08600v1 (first public 2026-06-07); open-access article, DOI:10.1007/s00020-026-02865-7.
2. A. Belli, U. Gül, W. T. Ross and A. G. Siskakis, *The Cesaro operator on \(L^2(0,1)\)*, arXiv:2604.19691v2 (2026); especially its convolution representation.
3. A. Yu. Karlovich, *Commutators of convolution type operators on some Banach function spaces*, Ann. Funct. Anal. 6 (2015), 191--205, DOI:10.15352/afa/06-4-191.
4. C. A. Fernandes, A. Yu. Karlovich and Yu. I. Karlovich, *Algebra of convolution type operators with continuous data on Banach function spaces*, arXiv:1908.07754v1 (2019).
