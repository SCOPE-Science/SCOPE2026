# Sharp rough-input Lipschitz norms of powered Fejér–Jackson kernels

## Finding

For the normalized positive convolution kernel obtained by taking the \(q\)-th power of the degree-\(n-1\) Fejér kernel, the sharp norm from bounded, possibly discontinuous, data to the Lipschitz seminorm has an exact finite formula. Its frequency-scaled limits involve the local maxima of a squared sinc function, while high powers exhibit a **Gaussian law uniformly in the frequency**.

For integers \(n\geq2\) and \(q\geq1\), put
\[
F_n(t)=\frac1n\left(\frac{\sin(nt/2)}{\sin(t/2)}\right)^2,\qquad
Z_{n,q}=\frac1{2\pi}\int_{-\pi}^{\pi}F_n(t)^q\,dt,\qquad
J_{n,q}=F_n^q/Z_{n,q}.
\]
Let \(T_{n,q}f=J_{n,q}*f\), where convolution uses normalized Haar measure on the circle. Define the best slope-amplification constant
\[
L_{n,q}=\sup_{\|f\|_{\infty}\leq1}\operatorname{Lip}(T_{n,q}f).
\]
The exact norm is
\[
\boxed{L_{n,q}=\frac{\int_{-\pi}^{\pi}|(F_n^q)'(t)|\,dt}
{\int_{-\pi}^{\pi}F_n(t)^q\,dt}.}
\]
To evaluate it finitely, let \(K=\lfloor(n-2)/2\rfloor\). For \(1\leq k\leq K\), let \(u_{n,k}\) be the unique point in \((k\pi/n,(k+1)\pi/n)\) solving
\[
n\cot(nu_{n,k})=\cot u_{n,k},\qquad
M_{n,k}=\frac{n}{1+(n^2-1)\sin^2u_{n,k}}.
\]
Writing \(c_j\) for the coefficients of \((1+z+\cdots+z^{n-1})^q\), one has
\[
\boxed{Z_{n,q}=n^{-q}\sum_{j=0}^{q(n-1)}c_j^2,\qquad
L_{n,q}=\frac{n^q+2\sum_{k=1}^{K}M_{n,k}^q+\mathbf1_{\{n\,\mathrm{odd}\}}n^{-q}}{\pi Z_{n,q}}.}
\]

For each fixed positive integer \(q\), define \(r_j\), for \(j\geq1\), as the unique solution of \(\tan r_j=r_j\) in \((j\pi,(j+1/2)\pi)\), and set
\[
D_q=\int_{-\infty}^{\infty}\left(\frac{\sin u}{u}\right)^{2q}\!du
=\frac{\pi}{(2q-1)!}\sum_{k=0}^{q-1}(-1)^k\binom{2q}{k}(q-k)^{2q-1}.
\]
Then
\[
\boxed{\lim_{n\to\infty}\frac{L_{n,q}}{n}=C_q
:=\frac{1+2\sum_{j=1}^{\infty}(1+r_j^2)^{-q}}{D_q}.}
\]
In particular, \(C_1\approx0.380230087468653\), \(C_2\approx0.479967081437\), and \(C_3\approx0.578872962046\).

The concentration regime is **uniform across all degrees**:
\[
\boxed{\lim_{q\to\infty}\ \sup_{n\geq2}
\left|\frac{L_{n,q}}{\sqrt{q(n^2-1)/(3\pi)}}-1\right|=0.}
\]
Consequently \(C_q\sim\sqrt{q/(3\pi)}\) as \(q\to\infty\). The exact small-degree values include \(L_{2,1}=2/\pi\), \(L_{3,1}=10/(3\pi)\), and \(L_{2,2}=8/(3\pi)\). In fact the entire two-point-frequency boundary is exactly \(L_{2,q}=4^q/[\pi\binom{2q}{q}]\).

## Assumptions and scope

The circle is \(\mathbb T=\mathbb R/(2\pi\mathbb Z)\) with its geodesic metric, and convolution is \((g*f)(x)=\frac1{2\pi}\int_{-\pi}^{\pi}g(x-y)f(y)\,dy\). Input functions are real-valued essentially bounded measurable functions; the same norm is obtained for complex-valued inputs. The seminorm \(\operatorname{Lip}\) is the optimal geodesic Lipschitz constant. Parameters \(n,q\) are arbitrary integers with \(n\geq2\), \(q\geq1\). Fixed-power limits hold with \(q\) fixed; the high-power theorem has no restriction coupling \(n\) and \(q\). The displayed local maxima are those of the complete sidelobes before the right endpoint of a half-circle.

## Proof

**1. Exact operator norm.** The kernel \(J_{n,q}\) is smooth and has normalized mass one. Differentiation under convolution gives \((T_{n,q}f)'(x)=(2\pi)^{-1}\int J_{n,q}'(x-y)f(y)\,dy\); hence the slope seminorm is at most \((2\pi)^{-1}\|J_{n,q}'\|_1\). Equality follows by choosing the measurable sign \(f(y)=\operatorname{sgn}(J_{n,q}'(-y))\) at evaluation point zero, including the sets where the derivative vanishes. On a compact circle the Lipschitz seminorm of a smooth function equals its maximum absolute derivative. Cancelling the normalization proves the first boxed identity.

**2. Lobe extrema and exact total variation.** Set \(u=t/2\). On any open nodal interval in \(0<u<\pi/2\), \(F_n(2u)>0\), and the logarithmic derivative vanishes exactly when \(n\cot(nu)=\cot u\). The second derivative of \(\log|\sin(nu)/\sin u|\) is \(-n^2\csc^2(nu)+\csc^2u<0\): the inequality follows from \(|\sin(nu)|<n\sin u\) at the relevant interior points (the inequality is strict except at the trivial limit). Thus each complete noncentral lobe has exactly one maximizer. Substituting \(n\cot(nu)=\cot u\) into the kernel yields \(M_{n,k}=n/[1+(n^2-1)\sin^2u_{n,k}]\). On the half-circle, the center peak decreases from \(n\) to zero; each complete sidelobe contributes rise plus fall, namely \(2M_{n,k}^q\), to the total variation of \(F_n^q\). The unfinished terminal lobe for odd \(n\) rises to \(F_n(\pi)^q=n^{-q}\); for even \(n\), \(F_n(\pi)=0\). Doubling by evenness and dividing by the mass produces the finite formula. Finally, the identity \(F_n(t)=n^{-1}|\sum_{j=0}^{n-1}e^{ijt}|^2\) and Parseval's formula give \(Z_{n,q}=n^{-q}\sum c_j^2\).

**3. Fixed-power sinc limit.** Rescaling \(t=2u/n\) gives \(F_n(2u/n)/n\to h(u)=(\sin u/u)^2\) uniformly on compact sets. For the normalized mass, dominated convergence follows from the bound \(F_n(2u/n)/n\leq\min\{1,\pi^2/(4u^2)\}\) throughout the rescaled half-circle. Consequently \(Z_{n,q}/n^{q-1}\to D_q/\pi\). The \(k\)-th complete lobe maximizer, for each fixed \(k\), converges after rescaling to the unique \(r_k\) satisfying \(\tan r_k=r_k\), and \(M_{n,k}/n\to(1+r_k^2)^{-1}\). Moreover, on a lobe numbered \(k\geq1\), \(M_{n,k}/n<1/(4k^2)\). This bound is summable after the \(q\)-th power, including \(q=1\). Dominated convergence applied to the exact total-variation sum proves the formula for \(C_q\). The stated finite-sum expression for \(D_q\) follows from the Fourier transform of the \(2q\)-fold interval convolution (or equivalently integration of the cardinal B-spline density at zero); it is an exact integral identity, not a numerical fit.

**4. Uniform high-power limit.** Write \(H_n=F_n/n\) and \(a_n=(n^2-1)/12\). The uniform Taylor expansion near zero is
\[
\log H_n(t)=-a_nt^2+O(n^4t^4),\qquad |t|\leq c/n,
\]
where \(c>0\) is fixed and sufficiently small. On the central scale \(t=s/\sqrt{q(n^2-1)}\), this implies \(H_n(t)^q\to e^{-s^2/12}\), uniformly in \(n\geq2\) for \(s\) on compact sets. For \(|t|\leq c/n\), a uniform quadratic exponential upper bound follows from the same expansion. On the rest of the first lobe, the ratio of sines has a uniform strict gap from one after excluding a fixed central-scale neighborhood; outside \(|t|\geq2\pi/n\), the elementary estimate \(H_n(t)\leq\pi^2/(n^2t^2)\) gives a summable power tail. Splitting these regions proves the uniform Laplace asymptotic
\[
\int_{-\pi}^{\pi}H_n(t)^q\,dt
=\sqrt{\frac{12\pi}{q(n^2-1)}}\,(1+o(1)),
\]
where the \(o(1)\) is uniform over \(n\geq2\). Independently, the half-circle lobe decomposition gives
\[
\int_{-\pi}^{\pi}|(H_n^q)'(t)|\,dt
=2\left[1+2\sum_{k=1}^{\lfloor(n-2)/2\rfloor}(M_{n,k}/n)^q+\mathbf1_{\{n\,\mathrm{odd}\}}n^{-2q}\right]
=2[1+O(4^{-q})]
\]
uniformly in \(n\), because \(M_{n,k}/n<1/(4k^2)\) and odd \(n\geq3\). Dividing the two integrals yields \(L_{n,q}\sim\sqrt{q(n^2-1)/(3\pi)}\), uniformly in \(n\). Taking \(n\to\infty\) at fixed \(q\) and then the uniform \(q\to\infty\) limit gives \(C_q\sim\sqrt{q/(3\pi)}\).

## Verification

The standalone program `verify_jackson.py` independently evaluates the exact Fourier-coefficient normalization, complete-lobe stationary values, and integral total variation. It checks \(706\) finite assertions across multiple degrees and powers, including three exact small-degree identities, positive mass, sidelobe envelope inequalities, fixed-power trends, and high-power uniform Gaussian comparisons. The program uses numerical quadrature only for finite cross-checks. It does **not** prove either quantified asymptotic theorem. Every claimed universal limit rests on the preceding analytical argument. Run `python verify_jackson.py` with NumPy and SciPy available.

## Relationship to prior work

Classical Fejér kernels, their approximate-identity and real-line sinc connections, and kernel periodization are standard; see Laugesen's *Harmonic Analysis Lecture Notes*, first available as arXiv:0903.3845v1 on 2009-03-23. The powered positive kernels are natural Jackson-type smoothing kernels. De Klerk–Hess–Laurent, arXiv:1603.03329v1, analyze polynomial Jackson kernels for approximation rates and optimization; those stated estimates are not formulas for the present sharp bounded-input derivative norm. Greiner's 1999 paper on generalized Jackson kernels is a relevant earlier reference, but its complete text was not accessible for full comparison. The distinguishing questions here are the exact nonlinear lobe-total-variation sum and a concentration law **uniform in two independent parameters**. No independent historical-priority audit has been performed.

## Limitations

Originality is judged only against the accessible material and documented searches, not established conclusively. The complete text of Greiner's earlier generalized-kernel work could not be inspected; it could conceivably imply a special case or stronger assertion. The theorem applies to powers of the standard Fejér kernel, not all positive trigonometric approximate identities or all Jackson kernels. The exact finite formula involves transcendental stationary roots except at special small degrees, although it is directly evaluable. The computational checks are finite supporting evidence, not infinite proofs.

## References

1. R. S. Laugesen, *Harmonic Analysis Lecture Notes*, arXiv:0903.3845v1 (2009-03-23), https://arxiv.org/abs/0903.3845 . Sections on Fejér kernels and periodization.
2. E. de Klerk, R. Hess, M. Laurent, *Improved convergence rates for Lasserre-type hierarchies of upper bounds for box-constrained polynomial optimization*, arXiv:1603.03329v1 (2016-03-10), https://arxiv.org/abs/1603.03329 .
3. R. Greiner, *Generalized Jackson kernels in approximation theory* (1999), earlier related work; complete text unavailable for detailed implication comparison.
