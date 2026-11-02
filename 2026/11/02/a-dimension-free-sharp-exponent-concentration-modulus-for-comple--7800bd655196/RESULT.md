# A dimension-free sharp-exponent concentration modulus for complex quadratic polynomials on \(c_0\)

## Finding

Write \(\pi_F\) for coordinate restriction to a finite nonempty set \(F\subset\mathbb N\), with zero extension, and \(P_F=P\circ\pi_F\). For every continuous complex two-homogeneous polynomial \(P:c_0(\mathbb N;\mathbb C)\to\mathbb C\) of norm one, put

\[
\delta=1-\|P_F\|,\qquad K=e^4+2e^2+\frac12.
\]

Then the following estimate is valid *independently of the cardinality of* \(F\):

\[
\boxed{\|P-P_F\|\le 8\sqrt K\,\sqrt\delta+\delta.}
\]

If \(x_0\in S_{c_0}\) is supported in \(F\), then \(\|P_F\|\ge |P(x_0)|\) and the same bound holds when \(\delta\) is replaced by \(1-|P(x_0)|\). The power \(1/2\) is universally optimal: a three-coordinate family below has error asymptotic to \(\sqrt2\sqrt\delta\).

## Assumptions and scope

All vector spaces, polynomial coefficients, and norms are complex. The Banach space \(c_0\) carries its usual supremum norm. The norm of a polynomial is the supremum of its absolute value over the closed unit ball. \(P\) is continuous and exactly two-homogeneous (not a general analytic map), \(F\) is an arbitrary finite nonempty coordinate set, and \(\pi_F:c_0\to c_0\) is the contractive canonical projection. No restriction is placed on the number of coordinates of \(P\) outside \(F\).

The conclusion includes \(\delta=0\) by a limiting argument and is useful for small positive deficits. The displayed prefactor \(8\sqrt K=66.873617987\ldots\) is explicit but **not claimed to be optimal**.

## Proof

**1. Disjoint-support decomposition and two scalar disk bounds.** Let \(B\) be the continuous symmetric bilinear form associated to \(P\). For \(u\in c_0(F)\), \(v\in c_0(F^c)\), write

\[
P(u+v)=A(u)+L_v(u)+C(v),\quad
A(u)=P(u),\quad L_v(u)=2B(u,v),\quad C(v)=P(v).
\]

For \(\|u\|_\infty,\|v\|_\infty\le1\), disjointness gives \(\|u+t v\|_\infty\le1\) whenever \(|t|\le1\). Thus \(f(t)=A(u)+tL_v(u)+t^2C(v)\) maps the unit disk into the closed unit disk. Schwarz--Pick at the origin (or the constant-modulus boundary case) yields

\[
|L_v(u)|\le1-|A(u)|^2.
\tag{1}
\]

Taking the even part \((f(t)+f(-t))/2=A(u)+t^2C(v)\), bounded by one on the unit circle, and optimizing the phase of \(t^2\), gives

\[
|A(u)|+|C(v)|\le1.
\tag{2}
\]

Let \(a=\|A\|=\|P_F\|=1-\delta\), \(D=1-a^2\). Since \(F\) is finite, \(A\) attains its norm on the finite polytorus, and (2) implies \(\|C\|\le\delta\). Equation (1) also gives \(\|L_v\|\le1\) for every \(\|v\|_\infty\le1\).

**2. Uniform second-derivative control along the coordinate torus.** Choose \(z^0\in\mathbb T^F\) with \(|A(z^0)|=a\). Fix \(v\) of norm at most one supported in \(F^c\), and write

\[
L_v(u)=\sum_{j\in F}l_j u_j,\qquad\sum_{j\in F}|l_j|=\|L_v\|\le1.
\]

For arbitrary real \(\eta_j\in[-1,1]\), define \(z_j(t)=z_j^0 e^{it\eta_j}\), \(g(t)=A(z(t))\) and \(h(t)=|g(t)|^2\) for real \(t\). The function \(h\) has a global maximum \(a^2\) at zero, so \(h'(0)=0\). For every real center \(t\), the analytic extension of \(g\) to the complex unit disk about that center satisfies \(|g(w)|\le e^2\): each argument has modulus at most \(e\), and \(\|A\|\le1\) with quadratic homogeneity. Cauchy's estimate therefore supplies \(|g'(t)|\le e^2\) and \(|g''(t)|\le2e^2\). Consequently,

\[
|h''(t)|\le2|g'(t)|^2+2|g(t)||g''(t)|\le H:=2e^4+4e^2.
\]

Taylor's theorem, \(h'(0)=0\), and (1) give, for every real \(t\),

\[
|L_v(z(t))|\le1-h(t)\le D+\frac H2t^2,
\quad |L_v(z(0))|\le D.
\tag{3}
\]

**3. Recover the full mixed norm without a dimension factor.** The scalar function \(t\mapsto L_v(z(t))\) has real second derivative of modulus at most \(\sum_{j\in F}|l_j|\le1\). Its first derivative at zero is \(i\sum_jl_jz_j^0\eta_j\). Using (3) and Taylor's theorem once more, for \(t>0\),

\[
\left|\sum_{j\in F}l_jz_j^0\eta_j\right|
\le\frac{2D}{t}+Kt,\qquad
K=\frac{H+1}{2}=e^4+2e^2+\frac12.
\tag{4}
\]

When \(D>0\), choose \(t=\sqrt{2D/K}\); the right side becomes \(2\sqrt{2KD}\). When \(D=0\), let \(t\downarrow0\) in (4). Finally, for arbitrary complex numbers \(c_j\), independently selecting the signs of their real and imaginary parts shows

\[
\sum_j|c_j|\le2\sup_{\eta_j\in[-1,1]}\left|\sum_jc_j\eta_j\right|.
\]

Apply this with \(c_j=l_jz_j^0\) in (4). For all \(\|v\|_\infty\le1\),

\[
\|L_v\|=\sum_j|l_j|\le4\sqrt{2KD}.
\]

Together with the decomposition, \(\|C\|\le\delta\), and \(D=\delta(1+a)\le2\delta\), this proves

\[
\|P-P_F\|\le4\sqrt{2KD}+\delta\le8\sqrt K\sqrt\delta+\delta.
\]

**4. Optimality of the exponent.** For each real \(b>0\), let

\[
R_b(z)=\frac12z_1(z_1+z_2)+b(z_1-z_2)z_3,
\qquad Q_b=\frac{R_b}{\sqrt{1+4b^2}},\quad F=\{1,2\}.
\]

On the distinguished boundary of the tridisk, first optimize the phase of \(z_3\) and then set the angular half-difference between \(z_1,z_2\) equal to \(\theta\). The maximum is exactly

\[
\|R_b\|=\max_{0\le\theta\le\pi/2}(\cos\theta+2b\sin\theta)=\sqrt{1+4b^2}.
\]

The maximum-modulus principle ensures that boundary optimization gives the full polynomial norm. Thus \(\|Q_b\|=1\), while

\[
\|(Q_b)_F\|=\frac{1}{\sqrt{1+4b^2}},\qquad
\|Q_b-(Q_b)_F\|=\frac{2b}{\sqrt{1+4b^2}}.
\]

For \(\delta_b=1-\|(Q_b)_F\|\), direct cancellation yields

\[
\frac{\|Q_b-(Q_b)_F\|^2}{\delta_b}
=1+\frac1{\sqrt{1+4b^2}}\longrightarrow2
\quad(b\downarrow0).
\]

Hence no universal estimate with exponent strictly larger than \(1/2\) can hold.

## Verification

The proof is analytic and applies to every finite \(F\) and every continuous two-homogeneous complex polynomial on \(c_0\). The accompanying standalone Python checker uses only the standard library; it tests the exact three-coordinate optimizer, the exact deficit identity, the elementary real-sign domination inequality, and the numerical constant bounds. These finite checks are **not** a proof of the dimension-independent theorem: that is supplied by the preceding Schwarz--Pick, Cauchy, Taylor, and sign-selection argument.

Run `python3 checker.py` from the directory containing this document and the checker.

## Relationship to prior work

Dantas and Rodríguez, *Concentration theorems for 2-homogeneous polynomials and bilinear forms with applications to the Kadec-Klee properties* (arXiv:2608.00780, first public August 1, 2026), Theorem 3.4, prove a **qualitative uniform concentration statement** on complex \(p\)-convex sequence lattices with \(p>2\); their proof is by contradiction and provides no explicit modulus. The new result supplies an effective **dimension-free square-root modulus specifically on complex \(c_0\)** and a three-variable example proving the exponent sharp. The broader qualitative theorem does not imply the asserted numerical rate.

Dantas, Jung, Mazzitelli, and Rodríguez, *On the strong subdifferentiability of the homogeneous polynomials and (symmetric) tensor products* (arXiv:2209.01767, first public September 5, 2022), Proposition 4.6, give a related point-dependent qualitative localization of complex \(c_0\) polynomials, with auxiliary moduli depending on the norming vector. Their result does not state a dimension-free bound in terms of \(1-\|P_F\|\) or establish the optimal square-root exponent.

## Limitations

The constant \(8\sqrt{e^4+2e^2+1/2}\) may be improved; only the exponent, not this prefactor, is proved optimal. The statement is for complex scalar-valued quadratic polynomials on \(c_0\), not real polynomials, higher degrees, vector-valued maps, or all complex Banach lattices. No claim of independent review or exhaustive publication-priority certification is made. Even though targeted literature and claim searches did not uncover the quantitative bound, an older equivalent lemma under different terminology remains possible.

## References

1. S. Dantas and J. T. Rodríguez, *Concentration theorems for 2-homogeneous polynomials and bilinear forms with applications to the Kadec-Klee properties*, arXiv:2608.00780 (v1, August 1, 2026), Section 3.1, Theorem 3.4; Section 6. https://arxiv.org/abs/2608.00780
2. S. Dantas, M. Jung, M. Mazzitelli, and J. T. Rodríguez, *On the strong subdifferentiability of the homogeneous polynomials and (symmetric) tensor products*, arXiv:2209.01767 (v1, September 5, 2022), Section 4.2.2, Proposition 4.6. https://arxiv.org/abs/2209.01767
