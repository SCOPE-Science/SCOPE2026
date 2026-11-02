# Gaussian spectral plunge and sharp projection defect in exponential Bergman balls

## Finding

Fix an integer \(d\ge 1\) and real numbers \(c>0\) and \(\gamma>0\). Let \(\mathbb B_d\subset\mathbb C^d\) be the unit ball, and equip its analytic Bergman space \(H_{d,c,\gamma}\) with the squared norm
\[
\|f\|^2=\int_{\mathbb B_d}|f(z)|^2\exp\!\left[-\frac{c}{(1-|z|^2)^\gamma}\right]\,dV(z).
\]
For \(0<\varepsilon<1\), let \(T_\varepsilon\) be the compression to \(H_{d,c,\gamma}\) of multiplication by the characteristic function of \(\{|z|^2\le 1-\varepsilon\}\). Denote by \(\Phi\) the standard normal distribution function.

Set
\[
L_\varepsilon=c\gamma(1-\varepsilon)\varepsilon^{-\gamma-1}-d,
\qquad
Q_\varepsilon^2=c\gamma\left[(1-\varepsilon)\varepsilon^{-\gamma-1}+(\gamma+1)(1-\varepsilon)^2\varepsilon^{-\gamma-2}\right].
\]
The following statements hold as \(\varepsilon\downarrow0\).

**Exact spectrum.** On every homogeneous holomorphic degree \(k\ge0\), \(T_\varepsilon\) has one eigenvalue, of multiplicity \(\binom{k+d-1}{d-1}\), given by
\[
\lambda_{k,\varepsilon}=\frac{\int_0^{1-\varepsilon}t^{k+d-1}\exp[-c/(1-t)^\gamma]dt}
{\int_0^1t^{k+d-1}\exp[-c/(1-t)^\gamma]dt}.
\]
The eigenvalues are strictly decreasing in \(k\), and \(T_\varepsilon\) is positive, trace class and contractive.

**Gaussian spectral plunge.** Uniformly for \(u\) in every fixed compact real interval,
\[
\lambda_{\lfloor L_\varepsilon+uQ_\varepsilon\rfloor,\varepsilon}\longrightarrow\Phi(-u).
\]
For each fixed threshold \(0<\tau<1\), the eigenvalue counting function, including degree multiplicities, satisfies
\[
N_\varepsilon(\tau):=\operatorname{Tr}\mathbf 1_{(\tau,1]}(T_\varepsilon)
=\frac{L_\varepsilon^d}{d!}
-\frac{L_\varepsilon^{d-1}Q_\varepsilon}{(d-1)!}\Phi^{-1}(\tau)
+o(L_\varepsilon^{d-1}Q_\varepsilon).
\]
In particular, for fixed \(0<\tau<1/2\), the number of eigenvalues in \((\tau,1-\tau)\), counted with multiplicity, is asymptotic to
\[
\frac{2|\Phi^{-1}(\tau)|}{(d-1)!}L_\varepsilon^{d-1}Q_\varepsilon.
\]

**Sharp projection defect.** The full trace has leading order
\[
\operatorname{Tr}T_\varepsilon\sim \frac{(c\gamma)^d}{d!}\,\varepsilon^{-d(\gamma+1)},
\]
while the projection defect has the strictly smaller, exact leading term
\[
\boxed{\ \operatorname{Tr}[T_\varepsilon(I-T_\varepsilon)]
\sim\frac{(c\gamma)^{d-1}\sqrt{c\gamma(\gamma+1)}}{(d-1)!\sqrt\pi}
\,\varepsilon^{-(\gamma+1)(d-1)-(\gamma+2)/2}.\ }
\]
For the exponential weight \(c=\gamma=1\) on the disk \(d=1\), the defect coefficient is exactly \(\sqrt{2/\pi}\), with exponent \(3/2\).

## Assumptions and scope

The parameters \(d,c,\gamma\) are fixed before the limit. The cutoff is the concentric ball in squared radial coordinates, and the weight is the displayed rapidly vanishing radial exponential weight. The threshold \(\tau\) is fixed strictly between zero and one. Volume normalization cancels in every eigenvalue. Here \(\Phi^{-1}\) is the ordinary real quantile of the standard normal distribution, and \(o(\cdot)\) is for \(\varepsilon\downarrow0\). All trace assertions include the full homogeneous-degree multiplicity. The result is not a claim about arbitrary nonradial cutoffs or about the rate of convergence.

## Proof

**1. Diagonalization and trace class.** The radial weight makes distinct monomials orthogonal. Polar integration on \(\mathbb C^d\), with \(t=|z|^2\), gives the exact ratio in the finding, independent of the specific monomial of total degree \(k\). There are \(m_k=\binom{k+d-1}{d-1}\) such monomials. For each fixed \(\varepsilon\), choose \(1-\varepsilon<b<1\). The numerator of the eigenvalue is at most a constant times \((1-\varepsilon)^k\), whereas its denominator is at least a positive constant times \(b^k\), by restricting the integral to a compact subinterval above \(b\). Hence \(\lambda_{k,\varepsilon}\le C_\varepsilon((1-\varepsilon)/b)^k\), and polynomial multiplicities imply trace class. The density with respect to \(t\) at degree \(k+1\) is obtained from that at degree \(k\) by a strictly increasing likelihood ratio \(t\); therefore \(\lambda_{k+1,\varepsilon}<\lambda_{k,\varepsilon}\).

**2. Gaussian limit at the correct spectral center.** Put \(y=-\log t\), \(y_\varepsilon=-\log(1-\varepsilon)\), and \(U(y)=c(1-e^{-y})^{-\gamma}\). Up to normalization, the eigenvalue integral is the probability law
\[
 p_k(y)\,dy\ \propto\ \exp[-(k+d)y-U(y)]\,dy,\qquad y>0,
\]
and \(\lambda_{k,\varepsilon}=\Pr_k(Y\ge y_\varepsilon)\). Direct differentiation gives
\[
-U'(y_\varepsilon)=c\gamma(1-\varepsilon)\varepsilon^{-\gamma-1}=L_\varepsilon+d,
\qquad U''(y_\varepsilon)=Q_\varepsilon^2>0.
\]
Also \(U''(y)>0\) for every \(y>0\), and
\[
L_\varepsilon\sim c\gamma\varepsilon^{-\gamma-1},\qquad
Q_\varepsilon\sim\sqrt{c\gamma(\gamma+1)}\,\varepsilon^{-(\gamma+2)/2},
\qquad \frac{Q_\varepsilon}{L_\varepsilon}\longrightarrow0.
\]
For \(k=\lfloor L_\varepsilon+uQ_\varepsilon\rfloor\) and \(z=Q_\varepsilon(y-y_\varepsilon)\), Taylor's theorem gives, locally uniformly for bounded \(u,z\),
\[
(k+d)(y-y_\varepsilon)+U(y)-U(y_\varepsilon)
=uz+\tfrac12z^2+o(1).
\]
Indeed \(U^{(3)}(y_\varepsilon)=O(\varepsilon^{-\gamma-3})\), hence \(U^{(3)}(y_\varepsilon)/Q_\varepsilon^3=O(\varepsilon^{\gamma/2})\to0\). On \(|y-y_\varepsilon|\le\theta\varepsilon\) with fixed sufficiently small \(\theta>0\), the curvature is uniformly comparable to \(Q_\varepsilon^2\). As \(Q_\varepsilon\varepsilon\to\infty\), the exponential density in \(z\) has Gaussian-dominated tails there; outside that interval, convexity of \(U\) bounds it by continuing the two tangent slopes at its endpoints, yielding negligible exponentially decaying mass. Thus dominated Laplace convergence gives \(z\Rightarrow N(-u,1)\) under \(p_k\), uniformly for \(u\) on compact sets, and proves the claimed \(\Phi(-u)\) limit.

**3. Uniform control of all degrees.** The preceding compact-window convergence alone would not justify a trace limit. Fix \(M>1\), and take integer indices \(K_+=\lceil L_\varepsilon+MQ_\varepsilon\rceil\) and \(K_-=\lfloor L_\varepsilon-MQ_\varepsilon\rfloor\), positive for small \(\varepsilon\). Increasing the degree from \(K_+\) to \(K_++j\) multiplies its unnormalized density in \(y\) by \(e^{-jy}\). Comparing the part \(y\ge y_\varepsilon\) to the part \(y\le y_\varepsilon-Q_\varepsilon^{-1}\) gives, for every integer \(j\ge0\),
\[
\lambda_{K_++j,\varepsilon}\le e^{-j/Q_\varepsilon}
\frac{\Pr_{K_+}(Y\ge y_\varepsilon)}
{\Pr_{K_+}(Y\le y_\varepsilon-Q_\varepsilon^{-1})}.
\]
Similarly, decreasing the degree from \(K_-\) to \(K_--j\) multiplies the density by \(e^{jy}\), and gives, for \(0\le j\le K_-\),
\[
1-\lambda_{K_--j,\varepsilon}\le e^{-j/Q_\varepsilon}
\frac{\Pr_{K_-}(Y\le y_\varepsilon)}
{\Pr_{K_-}(Y\ge y_\varepsilon+Q_\varepsilon^{-1})}.
\]
By Step 2 both probability ratios tend to
\[
C_M=\frac{\Phi(-M)}{\Phi(M-1)},\qquad C_M\longrightarrow0\quad(M\to\infty).
\]
Because \(Q_\varepsilon/L_\varepsilon\to0\), a geometric-series estimate, even after multiplication by the degree multiplicity \(m_k\), shows that the contributions to \(\sum m_k\lambda_{k,\varepsilon}(1-\lambda_{k,\varepsilon})\) from both outer regions, divided by \(L_\varepsilon^{d-1}Q_\varepsilon\), have limsup at most a constant depending only on \(d\) times \(C_M\). This uses \(\lambda(1-\lambda)\le\min(\lambda,1-\lambda)\), \(m_k\sim k^{d-1}/(d-1)!\), and \(\sum_{j\ge0}(K_++j+1)^{d-1}e^{-j/Q_\varepsilon}=O(L_\varepsilon^{d-1}Q_\varepsilon)\).

**4. Exact defect constant.** On the remaining \(O(MQ_\varepsilon)\) degrees, Step 2 and the multiplicity formula give a Riemann sum:
\[
\lim_{\varepsilon\downarrow0}\frac{\sum_{|k-L_\varepsilon|\le MQ_\varepsilon}m_k\lambda_{k,\varepsilon}(1-\lambda_{k,\varepsilon})}
{L_\varepsilon^{d-1}Q_\varepsilon}
=\frac{1}{(d-1)!}\int_{-M}^{M}\Phi(u)\Phi(-u)\,du.
\]
Let \(M\to\infty\), using the tail bounds from Step 3. For independent standard normals \(X_1,X_2\), Fubini gives
\[
\int_{\mathbb R}\Phi(u)\Phi(-u)\,du
=\mathbb E[(X_2-X_1)_+]
=\frac{1}{\sqrt\pi}.
\]
This proves the normalized trace limit and, on inserting the explicit asymptotics of \(L_\varepsilon\) and \(Q_\varepsilon\), its sharp coefficient and exponent. The same tail estimates show that replacing every \(\lambda_{k,\varepsilon}\) by the step \(\mathbf 1_{k<L_\varepsilon}\) changes the full trace by \(O(L_\varepsilon^{d-1}Q_\varepsilon)=o(L_\varepsilon^d)\); summing multiplicities gives \(\sum_{k\le L_\varepsilon}m_k\sim L_\varepsilon^d/d!\).

**5. Threshold counting.** Strict decrease in Step 1 and the locally uniform Gaussian profile in Step 2 imply that the crossing of a fixed \(\tau\in(0,1)\) occurs at degree
\[
 k_\tau=L_\varepsilon-Q_\varepsilon\Phi^{-1}(\tau)+o(Q_\varepsilon).
\]
Counting all monomials up to that degree and using \(\sum_{k=0}^{K}\binom{k+d-1}{d-1}=\binom{K+d}{d}\) proves the displayed two-term counting law. Subtracting the laws at \(\tau\) and \(1-\tau\) proves the plunge-window count.

## Verification

The standalone script `verify.py` computes radial eigenvalues using an independent numerical quadrature in the logarithmic coordinate. It tests six dimension/cutoff combinations, 18 points of the Gaussian profile, six defect constants, six full traces, nine quantile crossings, six curvature identities, and the Gaussian integral coefficient. Run `python verify.py` with the Python packages in `requirements.txt`. These tests are consistency checks, not a substitute for the all-degree tail argument or the asymptotic proof in Steps 2–5.

## Relationship to prior work

Cho, Lee and Park introduced and analyzed the exponential weight with \(c=\gamma=1\) on the unit ball; their 2022 work concerns Carleson embeddings and bounded/compact Toeplitz operators, not the present shrinking-cutoff eigenvalue law or sharp projection-defect trace. The Gaussian error-function transition is a recognized phenomenon in Bergman theory: Zelditch and Zhou prove an interface central limit theorem for spectral partial Bergman kernels on polarized compact Kähler manifolds with a tensor-power parameter; Hedenmalm and Wennman obtain related interfaces for planar entire-function spaces with varying potentials. Neither cited theorem states the fixed-singular-weight, shrinking-radius eigenvalue counting or the dimension-dependent exact defect constant here. Marceca, Romero, Speckbacher and Valentini study broad nonasymptotic spectral-deviation bounds for reproducing-kernel concentration operators, not this particular sharp asymptotic. Rozenblum's radial Toeplitz eigenvalue work concerns different fixed-symbol decay bounds. These are comparisons of mathematical regimes, not a guarantee of historical priority.

## Limitations

The result is restricted to radial balls and the displayed exponential-power weight. The parameters and counting threshold are fixed; the result gives no uniformity when these parameters vary with \(\varepsilon\), no explicit remainder estimate, and no nonradial boundary law. Gaussian edge behavior has substantial prior literature, so the novelty claim is confined to the exact weight/geometry/multiplicity/counting/trace combination. It has not undergone independent mathematical validation.

## References

1. Hong Rae Cho, Han-Wool Lee and Soohyun Park, *Carleson embedding theorem for an exponential Bergman space on the unit ball*, first posted July 28, 2022, arXiv:2207.13937, Sections 1 and 4.2.
2. Steve Zelditch and Peng Zhou, *Central Limit theorem for spectral Partial Bergman kernels*, first posted August 30, 2017, arXiv:1708.09267, introduction and main theorem.
3. Haakan Hedenmalm and Aron Wennman, *Off-Spectral Analysis of Bergman Kernels*, first posted May 2018, arXiv:1805.00854; Communications in Mathematical Physics 373 (2020), 1049–1083, introductory setting.
4. Felipe Marceca, José Luis Romero, Michael Speckbacher and Lisa Valentini, *Spectral Deviation of Concentration Operators on Reproducing Kernel Hilbert Spaces*, Constructive Approximation (2026), DOI:10.1007/s00365-026-09768-1.
5. Grigori Rozenblum, *On lower eigenvalue bounds for Toeplitz operators with radial symbols in Bergman spaces*, Journal of Spectral Theory 1 (2011), 299–325, DOI:10.4171/JST/13.
