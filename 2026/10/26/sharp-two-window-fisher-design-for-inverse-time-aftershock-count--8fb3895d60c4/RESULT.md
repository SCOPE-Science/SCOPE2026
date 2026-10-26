# Sharp two-window Fisher design for inverse-time aftershock counts

## Finding

Consider a nonhomogeneous Poisson aftershock process on \([0,T]\) with intensity
\[
\lambda(t)=\frac{K}{t+c},\qquad K>0,\quad c>0,\quad T>0.
\]
Only two counts are retained: the number of events in \([0,\tau]\) and in \((\tau,T]\), with \(0<\tau<T\). Both amplitude \(K\) and time-offset \(c\) are unknown; the inverse-time exponent is *fixed at one*. The observation horizon and the count boundary are deterministic, and information is evaluated locally at a nominal \(c\).

Write
\[
L=\log(1+T/c),\qquad u=\log(1+\tau/c),\qquad v=L-u.
\]
There is exactly one breakpoint maximizing the determinant of the \((K,c)\) Fisher information matrix, equivalently maximizing Fisher information for \(c\) after eliminating nuisance parameter \(K\). It is \(\tau_*(T,c)=c(e^{u_L}-1)\), where \(u_L\) is the unique solution in \((0,L)\) of
\[
\boxed{\frac{e^{u_L}-1-u_L}{u_L}
=1-\frac{1-e^{-(L-u_L)}}{L-u_L}.}
\]
The optimizer obeys \(0<u_L<L/2\), increases strictly with \(L\), and tends to the unique positive \(u_\infty\) satisfying \(e^{u_\infty}=1+2u_\infty\). Consequently,
\[
\boxed{\lim_{T/c\to\infty}\frac{\tau_*(T,c)}c
=2u_\infty=2.512862417252338\ldots.}
\]
At this optimum, the asymptotic ratio of nuisance-adjusted Fisher information from the two counts to that from every exact arrival time is
\[
\boxed{\eta_\infty=\frac{8u_\infty}{(1+2u_\infty)^2}
=0.8145287551781475\ldots.}
\]
The corresponding ratio tends to \(3/4\) as \(T/c\downarrow0\). All conclusions concern this specified two-parameter, two-count, ideal-observation model.

## Assumptions and scope

The intensity is exactly \(K/(t+c)\). Disjoint counts are independent Poisson variables. There is no background seismicity, offspring triggering beyond the modeled intensity, missing detections, or uncertainty in the inverse-time exponent. The start time is exactly zero; all detected events are counted. The local design evaluates Fisher information at a posited value of \(c\); estimating \(c\) without a nominal value requires a separate pilot or adaptive design. The maximizing criterion is local D-optimality for \((K,c)\), equivalently the Schur-complement information for \(c\) with \(K\) nuisance, not global risk optimality for an estimator.

## Proof

**1. Count information and nuisance elimination.** The two independent expected counts are \(\mu_1=Ku\) and \(\mu_2=Kv\). With \(h=1-e^{-u}\) and \(H=1-e^{-L}\), differentiating at fixed \(\tau,T\) gives
\[
\frac{\partial u}{\partial c}=-\frac{h}{c},\qquad
\frac{\partial L}{\partial c}=-\frac{H}{c}.
\]
The Poisson Fisher information entries for parameters \((K,c)\) therefore are
\[
I_{KK}=\frac{L}{K},\qquad I_{Kc}=-\frac{H}{c},\qquad
I_{cc}=\frac{K}{c^2}\left(\frac{h^2}{u}+\frac{(H-h)^2}{v}\right).
\]
The information for \(c\) with the nuisance amplitude removed is the Schur complement
\[
I_{c\mid K}(u)=I_{cc}-\frac{I_{Kc}^2}{I_{KK}}
=\frac{K}{c^2}J_L(u),\quad
J_L(u)=\frac{L}{uv}\left(h-\frac{uH}{L}\right)^2.
\]
Because \(I_{KK}=L/K\) does not depend on the cutoff, maximizing this Schur complement is equivalent to maximizing the full Fisher determinant. For every interior \(u\), \(J_L(u)>0\) by strict concavity of \(1-e^{-u}\) and its chord, while \(J_L(u)\) tends to zero at both endpoints.

**2. Reduction to an exact two-centroid problem.** Under the monotone transformation \(y=\log(1+t/c)\), expected event measure is \(K\,dy\) on \([0,L]\), and the \(c\)-score, apart from a constant factor, is \(z(y)=e^{-y}\). The conditional means of this score over the two bins are
\[
a(u)=\frac{1-e^{-u}}u,\qquad
b(u)=\frac{e^{-u}-e^{-L}}{L-u}.
\]
The between-bin variance identity gives \(J_L(u)=uv(a-b)^2/L\). Hence maximizing \(J_L\) is equivalent to minimizing the within-bin squared error
\[
W(u)=\int_0^u(z(y)-a)^2\,dy+\int_u^L(z(y)-b)^2\,dy.
\]
Since \(a\) and \(b\) are the conditional centroids, differentiating under the integral sign cancels the derivatives of the centroids and gives
\[
W'(u)=(a-b)\bigl(a+b-2e^{-u}\bigr).
\]
Here \(a>e^{-u}>b\). Write
\[
\frac{a-e^{-u}}{e^{-u}}=A(u):=\frac{e^u-1-u}{u},\quad
\frac{e^{-u}-b}{e^{-u}}=B(v):=1-\frac{1-e^{-v}}v.
\]
The derivative has the sign of \(A(u)-B(L-u)\). Both \(A\) and \(B\) are strictly increasing for positive arguments: their derivative numerators are, respectively, \((u-1)e^u+1>0\) and \(1-(1+v)e^{-v}>0\). At the left endpoint \(A(0+)=0<B(L)\); at the right endpoint \(A(L)>0=B(0+)\). Therefore \(A(u)-B(L-u)\) increases strictly from negative to positive, has exactly one zero, and that zero is the unique global minimizer of \(W\) and maximizer of \(J_L\). The displayed equation in the finding is exactly this zero condition.

**3. Bounds and asymptotic cutoff.** At \(u=L/2\), \(A(u)-B(u)=2(\sinh u-u)/u>0\), so \(u_L<L/2\). As \(L\) increases, \(B(L-u)\) increases pointwise, so its unique crossing with the strictly increasing \(A\) moves strictly right. Since \(B(v)<1\) for every finite positive \(v\), \(A(u_L)<1\) and therefore \(u_L<u_\infty\), where \(A(u_\infty)=1\). Monotone convergence and \(L-u_L\to\infty\) force \(A(\lim u_L)=1\), proving \(u_L\uparrow u_\infty\). The equation \(A(u_\infty)=1\) is \(e^{u_\infty}=1+2u_\infty\), with a unique positive solution since \(A\) is strictly increasing. Thus \(e^{u_\infty}-1=2u_\infty\), proving the cutoff limit.

**4. Information retained relative to arrival-time observations.** The full-event-time Fisher matrix has the same \(I_{KK}=L/K\) and \(I_{Kc}=-H/c\) but \(I_{cc}=(K/(2c^2))(1-e^{-2L})\). Its nuisance-adjusted information is
\[
I_{c\mid K}^{\rm full}=\frac{K}{c^2}
\left(\frac{1-e^{-2L}}2-\frac{H^2}{L}\right).
\]
At \(u_L\to u_\infty\), \(J_L(u_L)\to(1-e^{-u_\infty})^2/u_\infty\), while the full information factor tends to \(1/2\). Their ratio is \(2(1-e^{-u_\infty})^2/u_\infty=8u_\infty/(1+2u_\infty)^2\). For \(L\downarrow0\), the centroid equation gives \(u_L/L\to1/2\). Taylor expansion gives \(J_L(u_L)=L^3/16+O(L^4)\), while full information is \(L^3/12+O(L^4)\); their ratio tends to \(3/4\).

## Verification

Run `python3 verify_cutoff.py` from the directory containing this document, using Python's standard library. The program evaluates \(2{,}200\) seeded parameter settings, independently reconstructs the count Fisher matrix by derivatives of the original means, verifies the analytic Schur complement, compares cutoff candidates, checks the unbinned information upper bound, and evaluates both limiting constants. It is supporting numerical verification, not a substitute for the preceding all-parameter proof. For \(L=2\), the unique root is \(u_L\approx0.692389314015153\), corresponding to \(\tau_*/c\approx0.998484841127046\).

## Relationship to prior work

The inverse-time aftershock intensity is classical; the likelihood and unbinned Fisher-matrix method are established in Ogata's 1983 study. Ogata's 2004 regional study uses modified Omori-type kernels in a richer seismicity model. Lolli and Gasperini analyze the empirical importance and possible catalog-incompleteness confounding of the offset parameter. General Lloyd–Max quantization theory gives the midpoint-of-centroids *stationary condition*, not automatically uniqueness, the specialized optimal cutoff for the log-uniform score distribution, or the information-efficiency limits. The present result concerns the exact solution to that specific two-count design problem, rather than claiming any of those underlying methods as new.

## Limitations

No statistical claim is made for a misspecified aftershock intensity, a jointly unknown exponent, time-varying detection probability, clustered ETAS processes, or adaptive binning based on the same observed events. The analysis is local at the unknown nominal scale \(c\). The mathematical limit \(T/c\to\infty\) idealizes arbitrarily long observation of a critical inverse-time Poisson rate, whose expected total count diverges logarithmically. The result gives Fisher-information design, not a finite-sample estimator or physical identification of \(c\). Broader published quantization results could subsume the specialized global optimizer; an exhaustive historical priority claim is not made.

## References

1. Y. Ogata, “Estimation of the parameters in the modified Omori formula for aftershock frequencies by the maximum likelihood procedure,” *Journal of Physics of the Earth* 31 (1983), 115–124. DOI: 10.4294/jpe1952.31.115.
2. Y. Ogata, “Space-time model for regional seismicity and detection of crustal stress changes,” *Journal of Geophysical Research: Solid Earth* 109 (2004), B03308. DOI: 10.1029/2003JB002621 (first published online 2004-03-23).
3. B. Lolli and P. Gasperini, “Comparing different models of aftershock rate decay: the role of catalog incompleteness in the first times after main shock,” preprint (2005), arXiv:physics/0510081; subsequently *Tectonophysics* 423 (2006), 43–59.
4. B. Girod, *Quantization*, Stanford EE398A lecture notes, section on Lloyd–Max scalar quantizers, https://web.stanford.edu/class/ee398a/handouts/lectures/05-Quantization.pdf.
