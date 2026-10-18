# Strict migration enhancement and exact weak-dispersal sensitivity in a cyclic three-patch model

## Finding
For the equal-three-season population system of Benaïm–Lobry–Sari–Strickler (arXiv:2407.07553, model (38)), the principal population growth exponent \(\Lambda(m,T)\) is **strictly increasing in dispersal intensity** \(m\geq0\), for every fixed period \(T>0\) and every \(a>b\). It has the exact one-sided weak-dispersal sensitivity
\[
\left.\frac{\partial\Lambda(m,T)}{\partial m}\right|_{m=0^+}
=\frac{(e^{(a-b)T/9}-1)^2}{3e^{(a-b)T/9}}>0.
\]
At the degenerate boundary \(a=b\), \(\Lambda(m,T)=a\) for all \(m\ge0\), so strictness is sharp in the growth-rate contrast. The result proves, rather than infers from plots, that increasing migration between the currently unfavorable pair of patches strictly improves the overall growth exponent.

## Assumptions and scope
Let \(a,b\in\mathbb R\), \(a>b\), \(T>0\), and \(m\ge0\). There are three patches and three seasons of duration \(h=T/3\). During season one, patch one has per-capita growth \(a\), patches two and three have growth \(b\), and only the last two exchange migrants symmetrically at per-capita rate \(m\):
\[
A_1=\begin{pmatrix}a&0&0\\0&b-m&m\\0&m&b-m\end{pmatrix}.
\]
The favorable patch shifts cyclically from patch one to two to three in the subsequent seasons. Explicitly, for
\(P=\begin{pmatrix}0&0&1\\1&0&0\\0&1&0\end{pmatrix}\), let \(A_2=P A_1P^{-1}\), \(A_3=P^2A_1P^{-2}\). The system is \(\dot X=A_jX\) during season \(j\), extended periodically, and
\[
\Lambda(m,T)=T^{-1}\log\rho(e^{hA_3}e^{hA_2}e^{hA_1}).
\]
At \(m=0\), this common growth exponent equals \((a+2b)/3\); for \(m>0\), the monodromy is irreducible and all nonzero nonnegative initial states share this exponent. Throughout, derivatives in \(m\) are taken at finite \(m\); at zero they are one-sided.

## Proof
Set \(r=e^{bh}\), \(s=e^{(a-b)h}>1\) and \(p=(1+e^{-2mh})/2\in[1/2,1]\). Writing \(E=e^{hA_1}\), direct two-patch exponentiation gives
\[
E=r\begin{pmatrix}s&0&0\\0&p&1-p\\0&1-p&p\end{pmatrix}.
\]
Since the season matrices are successive cyclic conjugates, their product satisfies the **exact** identity
\[
e^{hA_3}e^{hA_2}e^{hA_1}=(P^{-1}E)^3.
\]
Define the nonnegative matrix
\[
B=r^{-1}P^{-1}E=
\begin{pmatrix}0&p&1-p\\0&1-p&p\\s&0&0\end{pmatrix},
\qquad R=\rho(B)>0.
\]
Consequently \(\Lambda=b+h^{-1}\log R\). The characteristic polynomial is
\[
f(\lambda,p)=\lambda^3+(p-1)\lambda^2+(p-1)s\lambda+(1-2p)s.
\]
By Perron–Frobenius, its largest positive root \(R\) is simple, including when \(p=1\) (the directed three-cycle). Hence \(f_\lambda(R,p)>0\). Put \(x=s^{1/3}>1\). A direct substitution yields
\[
f(x,p)=x^2(p-1)(x-1)^2\le0.
\]
For \(p<1\), this is strictly negative; since \(f(\lambda,p)\to+\infty\) at positive infinity and \(R\) is the Perron root, \(R>x\). At \(p=1\), \(f(\lambda,1)=\lambda^3-s\), giving \(R=x\). Thus in every case \(R\ge x\), and
\[
f_p(R,p)=R^2+sR-2s\ge x^2+sx-2s=x^2(x-1)^2>0.
\]
Implicit differentiation therefore gives \(dR/dp=-f_p/f_\lambda<0\). As \(dp/dm=-h e^{-2mh}<0\), the **exact response law** is
\[
\boxed{\quad
\frac{\partial\Lambda}{\partial m}
=e^{-2mh}\frac{R^2+sR-2s}{R[3R^2+2(p-1)R+(p-1)s]}>0.
\quad}
\]
This proves strict increase for every finite \(m\ge0\) and \(T>0\). At \(m=0\), \(p=1\), \(R=x\) and \(f_\lambda=3x^2\), so the derivative reduces to \((x-1)^2/(3x)\), giving the stated weak-dispersal formula. If \(a=b\), each season's growth is \(a\) plus conservative migration, whence \(\Lambda=a\) for all \(m\), completing the boundary classification.

## Verification
The standalone script `verify.py` executes exact rational determinant comparisons for the displayed characteristic polynomial and independent finite numerical checks of its Perron-root equation, monotonicity, response derivative, and weak-dispersal endpoint. Run `python3 verify.py` from the extracted package directory. The analytic proof above, rather than finite numerical sampling, establishes all quantifiers. Checks do not establish new claims about monotonicity in \(T\).

## Relationship to prior work
Benaïm, Lobry, Sari and Strickler, arXiv:2407.07553v2, Section 3.2.1, model (38), Proposition 25 and Figure 8, provide the seasonal system and limiting growth exponents. Their text observes *numerically* that \(m\mapsto\Lambda(m,T)\) appears strictly increasing, without proving that parameterwise assertion. In the earlier arXiv:2407.07553v1, Proposition 18 states the **distinct** upper bound \(\Lambda(m,T)\le(a+b)/2\); that upper bound is expressly **not** claimed as a new result here. The related study “Population growth on a time varying network,” arXiv:2411.07821, Section 4.5, supplies a growth sufficient condition and references the same previously published upper bound, but does not establish the displayed strict derivative law. Standard characteristic-polynomial and Perron–Frobenius tools are not new; the new content is their exact application to this migration-response question.

## Limitations
The theorem assumes three equal-duration seasons, a cyclically moving favorable patch, two identical unfavorable growth rates, and symmetric exchange restricted to the unfavorable pair at one common rate. It does not prove monotonicity for asymmetric, static, or generally time-varying dispersal graphs. The explicit susceptibility concerns the deterministic principal Lyapunov exponent, not nonlinear carrying-capacity equilibria or stochastic extinction probabilities. It does not assert novelty for the previously published bound on \(\Lambda\), or for the previously published large-period and large-migration limits.

## References
1. M. Benaïm, C. Lobry, T. Sari, and E. Strickler, *Dispersal-induced growth or decay in a time-periodic environment. The case of reducible migration matrices*, arXiv:2407.07553v2 (2025), Section 3.2.1, model (38), Proposition 25, Figure 8 and Appendix A.6. First public arXiv version: 2024-07-10. https://arxiv.org/pdf/2407.07553
2. Same authors, arXiv:2407.07553v1 (2024), Proposition 18 and Appendix A.5, previously stated upper bound. https://arxiv.org/abs/2407.07553
3. Same authors, *Population growth on a time varying network*, arXiv:2411.07821 (2024), Sections 4.4–4.5 and references. https://arxiv.org/abs/2411.07821
