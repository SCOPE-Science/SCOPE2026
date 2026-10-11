# Exact local quartic stability constants at the constant extremizer on cycles
## Finding
Let \(n\in\{5,6,\ldots\}\cup\{\infty\}\), where \(n=\infty\) denotes the circle with the heat energy. Use the admissible classes, normalized energies, logarithmic deficits and distances of Chen--Lam--Lu:
\[
\Delta_n(u)=2\mathcal E_n(u)-\operatorname{Ent}(u^2),\qquad d_n(u)=\|u-1\|_2,
\]
with \(u\in\mathcal A_n\). Define
\[
\mathcal C_{n,\mathrm{loc}}=\lim_{\rho\downarrow0}\inf\left\{\frac{\Delta_n(u)}{d_n(u)^4}:u\in\mathcal A_n,\ 0<d_n(u)<\rho\right\}.
\]
For finite \(n\), put
\[
q_n=4\cos^2\!\left(\frac{\pi}{n}\right)-1,
\]
and put \(q_\infty=3\). Then
\[
\mathcal C_{n,\mathrm{loc}}=\frac34-\frac{1}{4q_n}.
\]
For the finite-cycle word-length energy \(\mathcal E_{\mathrm w,n}\), define \(\Delta_{\mathrm w,n}\) and \(\mathcal C^{\mathrm w}_{n,\mathrm{loc}}\) analogously. For every finite \(n\ge5\),
\[
\mathcal C^{\mathrm w}_{n,\mathrm{loc}}=\frac12.
\]
These values are the exact local quartic constants at the constant extremizer. They coincide with the upper-bound coefficients produced by the first-plus-second-harmonic family in Chen--Lam--Lu, but they do not assert that those coefficients are the global sharp constants.

## Assumptions and scope
For finite \(n\), \(C_n=\mathbb Z/n\mathbb Z\) has the uniform probability measure and \(\mathcal A_n\) consists of nonnegative functions with \(L^2\)-norm one. For \(n=\infty\), the space is \(\mathbb T=\mathbb R/\mathbb Z\), \(\mathcal A_\infty\) is the nonnegative unit sphere in \(H^1(\mathbb T)\), and
\[
\mathcal E_\infty(u)=\frac{1}{4\pi^2}\int_0^1|u'(x)|^2\,dx.
\]
The finite nearest-neighbor energy is normalized to have spectral gap one. The word-length energy is
\[
\mathcal E_{\mathrm w,n}(u)=\sum_{k=0}^{n-1}\min(k,n-k)|\widehat u(k)|^2.
\]
The statement is local in \(d_n(u)\). No claim is made about the still-unknown global constants \(\mathcal C_n\), \(\mathcal C^{\mathrm w}_n\) for \(n\ge5\), or \(\mathcal C_\infty\).

## Proof
Write the orthogonal Fourier decomposition used by Chen--Lam--Lu as
\[
u=a+v+z,
\]
where \(a=\langle u\rangle\), \(v\) lies in the first-harmonic eigenspace, and \(z\) is orthogonal to constants and first harmonics. Put
\[
r=\|v\|_2,\qquad t=\|z\|_2,\qquad s=r^2+t^2.
\]
Since \(\|u\|_2=1\), their exact identities give
\[
s=1-a^2,\qquad d^2:=d_n(u)^2=2(1-a),
\]
so
\[
a=1-\frac{d^2}{2},\qquad s=d^2-\frac{d^4}{4}.
\]
For the nearest-neighbor or heat energy define the high-frequency excess
\[
Q(z)=\mathcal E_n(z)-\|z\|_2^2.
\]
For the word-length energy use the same definition with \(\mathcal E_{\mathrm w,n}\). On the orthogonal complement of constants and first harmonics,
\[
Q(z)\ge p\|z\|_2^2,
\]
where \(p=q_n\) for the nearest-neighbor or heat model and \(p=1\) for the finite word-length model. The second harmonic has excess eigenvalue exactly \(p\).

Let
\[
\mathcal F(u)=\mathcal E(u)-\frac13\left\langle (u-1)^2(u+2)\right\rangle
\]
be the cubic deficit for the chosen energy. The exact decomposition underlying the source proof is
\[
\mathcal F(u)=Q(z)+\frac{s^2}{4}+\mathcal R(a)-\frac13\langle(v+z)^3\rangle,
\]
where
\[
\mathcal R(a)=\frac{(1-a)^3(1+3a)}{12}.
\]
The first harmonic satisfies \(\langle v^3\rangle=0\). If \(v=re\) with \(\|e\|_2=1\), then for \(n\ge5\) and for the circle
\[
g:=e^2-1
\]
is a pure second harmonic with
\[
\|g\|_2^2=\frac12.
\]
Expanding the cubic gives
\[
\frac13\langle(v+z)^3\rangle=r^2\langle g,z\rangle+\langle vz^2\rangle+\frac13\langle z^3\rangle.
\]

Consider any sequence \(u_j\to1\) for which \(\Delta(u_j)/d_j^4\) stays bounded; sequences for which this quotient diverges cannot lower the local infimum. The scalar remainder in the source splitting
\[
\Delta(u)=2\mathcal F(u)+\langle H(u)\rangle
\]
is nonnegative. Hence \(\mathcal F(u_j)=O(d_j^4)\). The cubic expansion, \(r,t=O(d)\), the spectral inequality \(Q\ge p t^2\), and the high-frequency sup-norm estimate in the nearest-neighbor and circle models give, for small \(d\),
\[
\mathcal F(u)\ge (1-Cd)Q(z)-C d^2\sqrt{Q(z)}-C d^4.
\]
For a fixed finite word-length model the same estimate follows from finite-dimensional norm equivalence together with \(Q\ge t^2\). Completing the square in \(\sqrt{Q(z)}\) therefore shows
\[
Q(z)=O(d^4),\qquad t=O(d^2).
\]
Consequently, after writing \(z=d^2w\), the family \(w\) is bounded in the quadratic form \(Q\), while
\[
\frac{r^2}{d^2}\longrightarrow1.
\]
The terms \(\langle vz^2\rangle\), \(\langle z^3\rangle\), and \(\mathcal R(a)\) are then \(o(d^4)\). Dividing the exact cubic identity by \(d^4\) yields
\[
\frac{\mathcal F(u)}{d^4}=\frac14+Q(w)-\langle g,w\rangle+o(1).
\]

Because \(g\) is a second harmonic, the self-adjoint quadratic form \(Q\) satisfies \(Qg=pg\) in spectral notation. Completing the square gives
\[
Q(w)-\langle g,w\rangle
=Q\!\left(w-\frac{g}{2p}\right)-\frac{\|g\|_2^2}{4p}
\ge -\frac{1}{8p}.
\]
Hence every sequence approaching the constant extremizer satisfies
\[
\liminf\frac{\mathcal F(u)}{d^4}\ge \frac14-\frac{1}{8p}.
\]
The explicit source family with a first harmonic of size \(\varepsilon\) and a second harmonic of size \(\varepsilon^2/(2\sqrt2 p)\) attains this limit, so the cubic local coefficient is exactly \(1/4-1/(8p)\).

It remains to restore the logarithmic deficit. Since \(Q(z)=O(d^4)\), we have uniformly
\[
u-1=re+O(d^2).
\]
The source scalar remainder has the Taylor expansion
\[
H(1+\eta)=\frac{\eta^4}{6}+O(|\eta|^5).
\]
Every normalized first harmonic in these models satisfies
\[
\langle e^4\rangle=\frac32.
\]
Therefore
\[
\frac{\langle H(u)\rangle}{d^4}\longrightarrow\frac14.
\]
Combining this with \(\Delta=2\mathcal F+\langle H\rangle\) gives
\[
\liminf_{u\to1}\frac{\Delta(u)}{d(u)^4}
\ge 2\left(\frac14-\frac{1}{8p}\right)+\frac14
=\frac34-\frac{1}{4p}.
\]
The source perturbation family gives equality in the limiting infimum. Substituting \(p=q_n\) yields the nearest-neighbor and circle formula; substituting \(p=1\) yields \(\mathcal C^{\mathrm w}_{n,\mathrm{loc}}=1/2\).

## Verification
The argument was checked against the exact source formulas for the Fourier decomposition, the relation \(d^2=2(1-a)\), the high-frequency excess energy, the cubic-deficit identity, the second-harmonic identities, the Taylor expansion of the scalar remainder, and the explicit perturbation family. The only computation used as a sanity check was finite-cycle evaluation of the source family for several \(n\); the proof itself is symbolic and covers all stated parameters.

The local lower-bound argument explicitly treats arbitrary sequences approaching the constant. Its key compactness substitute is the estimate \(Q(z)=O(d^4)\) for every sequence with bounded normalized deficit; this prevents high-frequency leakage from evading the quadratic completion. For the circle, the source high-frequency sup-norm estimate supplies the required control. For each fixed finite word-length cycle, finite dimensionality supplies it.

## Relationship to prior work
Chen--Lam--Lu prove global lower bounds and construct a first-plus-second-harmonic family giving the global upper bounds
\[
\mathcal C_n\le\frac34-\frac{1}{4q_n},\qquad \mathcal C^{\mathrm w}_n\le\frac12.
\]
They explicitly state that the global exact constants for \(n\ge5\) and for the circle are not determined. Their construction computes the limiting ratios along one family. The present result adds the converse local statement: no other perturbation converging to the constant can have a smaller limiting quartic ratio.

Xie--Zhang prove a global word-length quartic remainder with coefficient \(1/12\) and identify the quartic exponent as sharp locally, while explicitly not claiming that the coefficient \(1/12\) is optimal. Frank--Ivanisvili establish the underlying sharp logarithmic Sobolev and cubic Sobolev inequalities. Neither inspected source gives the exact local numerical constants above.

## Limitations
The theorem is local at the constant extremizer. It does not determine the global sharp constants in the models with \(n\ge5\), and it does not exclude a nonlocal competitor with a smaller ratio than the local value. Constants hidden in the localization estimate may depend on a fixed finite \(n\) in the word-length case; the final local coefficient itself does not. No assertion is made for the exceptional four-cycle, whose fourth-order cubic cancellation has different geometry and is treated separately in the focal source.

## References
1. Lu Chen, Nguyen Lam, Guozhen Lu, *Sharp uniform stability of the logarithmic Sobolev inequality on finite cycles and stability of the cubic Sobolev inequality*, arXiv:2610.05347v1, 2026.
2. Xinyuan Xie, Haonan Zhang, *Sharp log-Sobolev inequalities and quartic stability on finite cyclic groups*, arXiv:2606.02847v4, 2026.
3. Rupert L. Frank, Paata Ivanisvili, *The sharp log Sobolev inequality on finite cycles*, arXiv:2605.29035, 2026.
