# Exact physical-time correlations in a quadratic-reset hybrid oscillator

## Finding

The planar hybrid oscillator of Llibre and Santana with two opposite linear centers and quadratic reset has a natural ergodic stationary probability measure in its open unit disk. Its *Cartesian* horizontal coordinate has a non-decaying, exactly computable physical-time autocorrelation, whereas its centered radius has compactly supported autocorrelation. More generally, every pair of Chebyshev radial observables has an exact finite-time correlation law.

Write \(r=\sqrt{x^2+y^2}\), and let \(\nu\) be the stationary measure constructed below. Its density relative to Euclidean area is
\[
\frac{d\nu}{dx\,dy}=\frac{1}{2\pi^2 r\sqrt{r(1-r)}},\qquad 0<r<1.
\]
For a stationary trajectory, let \(R(t)=\sqrt{x(t)^2+y(t)^2}\), let \(X(t)=x(t)\), and let \(T_m\) be the Chebyshev polynomial of the first kind. For integers \(m,n\ge1\), set \(H_m(r)=T_m(1-2r)\). If \(t\ge0\), \(q=\lfloor t/\pi\rfloor\), and \(\alpha=t/\pi-q\), then
\[
\mathbb E_\nu[H_m(R(0))H_n(R(t))]
=\frac12\Big((1-\alpha)\mathbf1_{\{m=2^q n\}}+\alpha\mathbf1_{\{m=2^{q+1}n\}}\Big).
\]
In particular,
\[
\operatorname{Cov}_\nu(R(0),R(t))=\frac18\max\{1-t/\pi,0\}.
\]
By contrast, \(\mathbb E_\nu[X(t)]=0\), and
\[
\operatorname{Cov}_\nu(X(0),X(t))=
\begin{cases}
\displaystyle \frac18\cos t+\frac{(\pi-t)\cos t+\sin t}{16\pi},&0\le t\le\pi,\\[4pt]
\displaystyle \frac18\cos t,&t\ge\pi.
\end{cases}
\]
Thus the stationary physical-time dynamics is not mixing, although its radial linear observable loses all correlation after one half-turn.

## Assumptions and scope

On the left half-plane \(x<0\), the continuous vector field is \((\dot x,\dot y)=(-y,x)\); on the right half-plane \(x>0\), it is \((\dot x,\dot y)=(y,-x)\). When a trajectory reaches the switching line \(x=0\) from either half-plane, it is reset according to \((0,y)\mapsto(0,-4y(1+y))\), and then follows the vector field that enters the opposite half-plane. The assertion concerns the invariant regular-motion family with post-reset heights in \((0,1)\). The countable set of heights whose iterates eventually hit \(0\) or \(1\) has measure zero under \(\nu\). Resets take zero physical time, and each nontrivial semicircular flight takes exactly \(\pi\) units of original physical time.

For a statistically stationary trajectory, expectations and covariance are taken with respect to \(\nu\). No assertion is made that every initial condition, every invariant measure, or every branch convention on the switching line yields these statistics.

## Proof

**Half-flight reduction.** A left flight beginning at \((0,r)\), \(0<r<1\), follows \((-r\sin s,r\cos s)\) for \(0<s<\pi\), reaches \((0,-r)\), and resets to \((0,F(r))\), with \(F(r)=4r(1-r)\). The right flight from \((0,F(r))\) is \((F(r)\sin s,F(r)\cos s)\), again for a physical duration \(\pi\), and resets to \((0,F^2(r))\). The full-section return \(F^2\) is the map computed by the motivating paper; for physical-time statistics the intervening half-return \(F\) matters.

**Invariant measure.** The substitution \(r=\sin^2(\pi u)\), with \(u\) uniform on \([0,1]\), gives the arcsine probability law
\[
\mu(dr)=\frac{dr}{\pi\sqrt{r(1-r)}}.
\]
Since \(F(\sin^2(\pi u))=\sin^2(2\pi u)\), this law is \(F\)-invariant. Introduce the half-plane parity \(e\in\{0,1\}\) and flight age \(a\in[0,\pi)\). Use product probability \(\mu(dr)\) times the uniform parity law times \(da/\pi\). The physical-time semiflow increments \(a\) at unit speed and, at \(a=\pi\), applies \((e,r)\mapsto(1-e,F(r))\) and resets \(a\) to zero. This product measure is invariant. Because \(F^2\) is ergodic for \(\mu\), its parity-flip extension is ergodic, and so is the constant-roof suspension.

Define the physical phase \(\phi=a+e\pi\) modulo \(2\pi\). It is uniform, independent of \(r\), and evolves as \(\phi(t)=\phi(0)+t\) modulo \(2\pi\). The embedding in the physical plane is
\[
(x,y)=\begin{cases}
(-r\sin\phi,r\cos\phi),&0<\phi<\pi,\\
(-r\sin\phi,-r\cos\phi),&\pi<\phi<2\pi.
\end{cases}
\]
The physical polar angle is uniform on a full circle and independent of \(r\). Dividing the product polar density by the Jacobian \(r\) proves the stated Euclidean density.

**All polynomial radial correlations.** With \(r=\sin^2(\pi u)\), the Chebyshev identity gives
\[
H_m(F^k(r))=\cos(2\pi m 2^k u).
\]
Consequently, Fourier orthogonality on \([0,1]\) yields, for every \(k\ge0\),
\[
\int_0^1 H_m(r)H_n(F^k(r))\,d\mu(r)
=\frac12\mathbf1_{\{m=2^k n\}}.
\]
At time \(t\), the number \(N\) of resets equals \(\lfloor(a+t)/\pi\rfloor\). With \(q=\lfloor t/\pi\rfloor\) and \(\alpha=t/\pi-q\), uniform \(a\) makes \(N=q\) with probability \(1-\alpha\) and \(N=q+1\) with probability \(\alpha\). Averaging the preceding Fourier identity proves the claimed Chebyshev law. Since \(r-1/2=-H_1(r)/2\), its special case gives the compact-support radial covariance.

**Cartesian correlation.** The plane embedding gives \(X(t)=-R(t)\sin(\phi(0)+t)\). Orthogonality gives \(\mathbb E[R(0)R(t)\mid\phi(0)]=3/8\) if no reset occurs and \(1/4\) after at least one reset. Therefore
\[
\mathbb E[X(0)X(t)]
=\frac14\mathbb E_\phi[\sin\phi\sin(\phi+t)]
+\frac18\mathbb E_\phi[\mathbf1_{\{N=0\}}\sin\phi\sin(\phi+t)].
\]
The first expectation is \(\cos t/2\). For \(0\le t\le\pi\), the second is
\[
\frac1\pi\int_0^{\pi-t}\sin u\sin(u+t)\,du
=\frac{(\pi-t)\cos t+\sin t}{2\pi};
\]
it is zero for \(t\ge\pi\). This proves the exact Cartesian formula. Because this covariance equals \(\cos t/8\) for arbitrarily large \(t\), it cannot tend to the product of coordinate means; hence the stationary physical-time semiflow is not mixing.

## Verification

The proof above uses exact trigonometric integration and frequency orthogonality. The self-contained program `checks/verify.py` independently reconstructs the half-flight reset from its explicit coordinates, checks the Chebyshev integral for many pairs of integer frequencies using deterministic Fourier-grid quadrature, and checks the exact Cartesian and radial formulas against independent two-dimensional angular/quasiperiodic quadrature. Run it with `python3 checks/verify.py` using only the Python standard library. Its finite tests support the algebra but are not a proof of the infinite-index statement.

## Relationship to prior work

Llibre and Santana exhibit this same hybrid vector field and reset map and prove that the full return on the positive section is \(F^2\), with \(F(r)=4r(1-r)\); they establish Devaney-type chaos, not a physical-time invariant density or an all-time Cartesian correlation law. The arcsine invariant law and trigonometric conjugacy of \(F\) are classical. Kohda, Tsuneda and Lawrance study correlations of discrete Chebyshev chaotic sequences; such discrete correlations are credited here. The result above concerns their new geometric combination with the original half-turn clock and an explicitly specified Cartesian observable. The non-mixing property of constant-roof suspensions is also standard; the exact coexistence of a finite-range radial covariance and a persistent Cartesian \(\cos t/8\) tail for this planar hybrid model is the quantitative statement established here.

## Limitations

These statistics refer to one natural ergodic stationary measure, not to all invariant measures. The system is hybrid rather than a continuous classical planar flow; physical-time dynamics includes instantaneous state resets. Singular landing and switching points require branch conventions but form a stationary-measure-null set. The discrete Chebyshev correlation mechanism is pre-existing, and the relationship to general suspension theory is acknowledged. No independent verification or absolute publication priority is asserted.

## References

1. J. Llibre and P. Santana, *Limit cycles and chaos in planar hybrid systems*, arXiv:2407.05151v2 (first submitted 2024-07-06), particularly Sections 2, 3 and 6; https://arxiv.org/html/2407.05151v2 .
2. T. Kohda, A. Tsuneda and A. J. Lawrance, *Correlational Properties of Chebyshev Chaotic Sequences*, Journal of Time Series Analysis **21** (2000), 181–191, doi:10.1111/1467-9892.00180.
3. E. W. Weisstein, *Logistic Map--r=4*, MathWorld, https://mathworld.wolfram.com/LogisticMapR=4.html .
