# An isolated second-jet zero phase for the classical Dirichlet kernel

## Finding
Let \(\mathbb D\) denote the open unit disk and \(\mathcal D\) the classical analytic Dirichlet Hilbert space with norm
\[
\|f\|_{\mathcal D}^2=|a_0|^2+\sum_{n=1}^{\infty}n|a_n|^2,\qquad f(z)=\sum_{n=0}^{\infty}a_nz^n.
\]
For any integer \(m\ge1\) and finite real \(\tau\ge0\), add the derivative penalty \(\tau|f^{(m)}(0)|^2\). Its reproducing kernel is
\[
K_{m,\tau}(z,w)=F_{m,q}(z\overline w),\qquad
F_{m,q}(t)=1-\log(1-t)-qt^m,\qquad
q=\frac1m-\frac1{m+\tau(m!)^2}.
\]
The logarithm is the analytic principal branch on \(1-\mathbb D\). The kernel has no zero at any pair \(z,w\in\mathbb D\) for every such penalty unless \(m=2\). For \(m=2\), define
\[
q_*=1-\log2,\qquad \tau_*=\frac{1-\log2}{2\log2-1}.
\]
Then zero-freeness holds if and only if \(\tau\le\tau_*\). When \(\tau>\tau_*\), there is exactly one scalar zero \(t\in\mathbb D\), it is simple and lies on the negative real axis: \(t=-r\) is uniquely characterized by
\[
1-\log(1+r)-\frac{\tau}{1+2\tau}r^2=0,\qquad 0<r<1.
\]
The endpoint \(\tau=\tau_*\) is zero-free in the open disk; the limiting zero is at the excluded boundary point \(t=-1\). Numerically \(q_*=0.30685281944005469\ldots\) and \(\tau_*=0.7943497247810449\ldots\).

## Assumptions and scope
The result concerns the canonical Dirichlet coefficient norm specified above, not the alternative \(\sum(n+1)|a_n|^2\) convention and not a Bergman or Hardy norm. The derivative penalty is of exactly one Taylor jet at the disk center; \(m\) ranges over all positive integers, and \(\tau\) over all finite nonnegative reals. A scalar zero \(t\) is realizable as \(z\overline w=t\) with both \(z,w\in\mathbb D\); for example choose \(z=\sqrt{|t|}\) and \(w=\sqrt{|t|}\,\overline t/|t|\) for \(t\ne0\). Statements of zero count refer to distinct scalar zeros, with simplicity asserted where applicable.

## Proof
**Kernel normalization.** The monomials are orthogonal. Their squared norms are \(1\) in degree zero, \(n\) in degree \(n\ge1\), except at \(n=m\), where the squared norm becomes \(m+\tau(m!)^2\). Expanding the orthonormal basis therefore gives the displayed series and coefficient \(q\). In particular \(0\le q<1/m\); throughout the positivity estimates we may replace this by the closed range \(0\le q\le1/m\).

**High jets.** For every \(|t|<1\),
\[
\operatorname{Re}(1-\log(1-t))=1-\log|1-t|>1-\log2.
\]
For \(m\ge4\), \(q|t|^m\le1/m\le1/4<1-\log2\). Hence \(\operatorname{Re}F_{m,q}(t)>0\), establishing zero-freeness in all degrees \(m\ge4\).

**The cubic jet.** On \(t=e^{i\theta}\ne1\), where \(-\pi\le\theta\le\pi\),
\[
\operatorname{Re}F_{3,q}(t)=1-\log(2|\sin(\theta/2)|)-q\cos(3\theta).
\]
If \(\cos(3\theta)\le0\), this is at least \(1-\log2>0\). Otherwise the angle necessarily satisfies \(|\theta|<5\pi/6\), so \(2|\sin(\theta/2)|<\sqrt{2+\sqrt3}\); consequently
\[
\operatorname{Re}F_{3,q}(e^{i\theta})>
\frac23-\frac12\log(2+\sqrt3)>0.
\]
The final strict inequality follows from \(e^{4/3}>2+\sqrt3\); for instance the first five Taylor terms of \(e^{4/3}\) sum to \(911/243>2+\sqrt3\). The boundary real part diverges to \(+\infty\) as \(t\to1\). For any fixed \(q\), the harmonic minimum principle, applied after excluding a small disk around \(1\) and then letting its radius tend to zero, yields \(\operatorname{Re}F_{3,q}>0\) throughout \(\mathbb D\).

**The linear jet.** The boundary minimum for \(q=0\) is \(1-\log2>0\). For \(q=1\), set \(s=1-\cos\theta\in(0,2]\). The boundary real part becomes
\[
\operatorname{Re}F_{1,1}(e^{i\theta})=s-\tfrac12\log(2s)\ge\tfrac12,
\]
with equality only for \(s=1/2\), by elementary differentiation. For \(q\in[0,1]\), \(\operatorname{Re}F_{1,q}\) is the convex combination of these two harmonic real parts; its boundary values are uniformly positive away from the point \(t=1\), where they diverge to \(+\infty\). The harmonic minimum principle proves \(\operatorname{Re}F_{1,q}>0\) in \(\mathbb D\).

**The quadratic jet: exclusion of nonreal zeros.** Write \(t=x+iy\in\mathbb D\). For \(y\ne0\), integration of \(-\log(1-t)\) gives
\[
\frac{\operatorname{Im}F_{2,q}(t)}{y}=
\int_0^1\frac{du}{|1-ut|^2}-2qx.
\]
When \(x\le0\), this is strictly positive. When \(0<x<1\), Jensen's inequality for the strictly convex reciprocal function gives
\[
\int_0^1\frac{du}{|1-ut|^2}
\ge\frac1{1-x+|t|^2/3}
>\frac1{4/3-x}>x\ge2qx.
\]
Here the penultimate comparison follows from \(x(4/3-x)\le4/9<1\), and the last from \(q\le1/2\). Thus the imaginary part has the sign of \(y\); every zero in \(\mathbb D\) must be real.

On \(0\le t<1\) one has \(F_{2,q}(t)\ge1-qt^2>0\). On the negative real axis, write \(t=-r\) and define \(G_q(r)=1-\log(1+r)-qr^2\) for \(0\le r\le1\). Then \(G_q(0)=1\), \(G'_q(r)=-1/(1+r)-2qr<0\), and \(G_q(1)=1-\log2-q\). Exactly one simple zero lies at \(0<r<1\) if and only if \(q>1-\log2\). Equality gives a zero only at the excluded endpoint \(r=1\).

Finally \(q=\tau/(1+2\tau)\) in degree two, which increases strictly from zero to \(1/2\). Solving \(q=q_*\) gives precisely \(\tau_*=(1-\log2)/(2\log2-1)\). This completes the classification.

## Verification
The proof is analytic and covers every positive integer \(m\), every finite \(\tau\ge0\), and the excluded unit-circle boundary. A companion standalone checker recomputes the critical constants, verifies the exact Taylor rational inequality, samples the boundary real parts of the extremal forms, and solves representative negative-axis roots. Its finite numerical experiments are illustrative only and are not used as a substitute for the harmonic-minimum or nonreal-zero arguments. The checker requires Python 3 with only its standard library.

## Relationship to prior work
Kellay and Mashreghi [1] develop zero-set theory for arbitrary functions in the unperturbed Dirichlet space. Fricain, Mashreghi and Seco [2] study cyclicity and optimal approximants in weighted analytic Hilbert spaces including the Dirichlet space. Bénéteau, Khavinson, Liaw, Seco and Sola [3] relate optimal approximants to kernels of polynomial-generated subspaces and establish zero restrictions for those approximants. Their nonvanishing theorems do not automatically classify zeros of the entire rank-one, coefficient-penalized Dirichlet reproducing kernel. The exact all-jet isolated-second-derivative threshold stated here was not located in the sources examined; that limited literature comparison does not prove global priority.

## Limitations
The theorem is specific to the stated center-jet Dirichlet norm and does not assert analogous classifications for arbitrary basepoint penalties, simultaneous jet penalties, other coefficient weights, or multispace kernels. The zero count concerns the scalar product \(t=z\overline w\), not the number of pairs \((z,w)\) realizing a zero. Relevant unindexed or inaccessible work could predate the stated classification. No independent audit has been performed.

## References
[1] K. Kellay and J. Mashreghi, *On zero sets in the Dirichlet space* (2011), arXiv:1102.5596, https://arxiv.org/abs/1102.5596 (publicly posted 2011-02-28).

[2] E. Fricain, J. Mashreghi and D. Seco, *Cyclicity in reproducing kernel Hilbert spaces of analytic functions* (2013), arXiv:1312.7739, https://arxiv.org/abs/1312.7739.

[3] C. Bénéteau, D. Khavinson, C. Liaw, D. Seco and A. A. Sola, *Orthogonal polynomials, reproducing kernels, and zeros of optimal approximants* (2015), arXiv:1509.04807, https://arxiv.org/abs/1509.04807.
