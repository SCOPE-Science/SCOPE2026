# Sharp first-jet Berezin envelopes and rigidity of the Hardy composition radius

## Finding
For the classical Hardy space \(H^2(\mathbb D)\), let \(C_\varphi f=f\circ\varphi\) be the composition operator of any analytic selfmap \(\varphi:\mathbb D\to\mathbb D\). Its Berezin transform and radius are
\[
\widetilde C_\varphi(z)=\frac{1-|z|^2}{1-\overline z\varphi(z)},\qquad
\operatorname{ber}(C_\varphi)=\sup_{z\in\mathbb D}|\widetilde C_\varphi(z)|.
\]
Define \(t=|\varphi(0)|\) and \(c=|\varphi'(0)|/(1-t^2)\), so \(0\le t<1\) and \(0\le c\le1\). For \(0\le r<1\), put
\[
u_c(r)=\frac{r(r+c)}{1+cr},\qquad
E_{t,c}(r)=\frac{(1-r^2)(1+t u_c(r))}{1+t u_c(r)-rt-r u_c(r)}.
\]
Then, for every \(r\in[0,1)\),
\[
\boxed{\sup_{|z|=r}|\widetilde C_\varphi(z)|\le E_{t,c}(r).}
\]
The envelope is jointly sharp: for every \(t,c\) an explicit single symbol attains equality for **all** \(r\), not merely for one selected radius. Equivalently, the exact largest Berezin radius subject to the value and first-derivative constraints \(|\varphi(0)|=t\) and \(|\varphi'(0)|\le c(1-t^2)\) is \(\sup_{0\le r<1}E_{t,c}(r)\).

For \(0<t<1\), the universal radius bound \(\operatorname{ber}(C_\varphi)\le1+t\) is an equality **if and only if**
\[
\boxed{\varphi(z)=\frac{z+b}{1+\overline b z},\quad b=\varphi(0)\ne0.}
\]
When \(b=0\), every disk selfmap fixing the origin instead has Berezin radius \(1\); hence that endpoint is not rigid.

## Assumptions and scope
The domain is the open unit disk, \(\mathbb D=\{z\in\mathbb C:|z|<1\}\), and \(\varphi\) is any analytic disk selfmap. There is no boundary regularity, finite degree, univalence, or compactness hypothesis. The Hilbert space is the standard analytic Hardy space with norm \(\|\sum a_nz^n\|^2=\sum|a_n|^2\), and all suprema over radius circles use \(r<1\). For \(t=0\), any phase can be chosen in the extremizer definition.

## Proof
**Reduction to a real center.** For \(b=\varphi(0)\ne0\), write \(\omega=b/|b|\) and replace \(\varphi\) by \(\phi(z)=\overline\omega\varphi(\omega z)\). This rotates the parameter in the Berezin formula, so it preserves each radial maximum, the Berezin radius, and \(|\varphi'(0)|\). Then \(\phi(0)=t\ge0\). For \(b=0\), use \(\omega=1\).

**Two Schwarz–Pick steps.** Define
\[
\psi(z)=\frac{\phi(z)-t}{1-t\phi(z)}=z h(z).
\]
Schwarz's lemma gives an analytic selfmap \(h\) of the closed-unit ball, with \(|h(0)|=c\). The Schwarz–Pick estimate applied to \(h\) is
\[
|h(z)|\le\frac{|z|+c}{1+c|z|},\qquad
|\psi(z)|\le u_c(r),\quad r=|z|.
\]
For \(0\le t<1\) and any \(w\) with \(|w|=s<1\), direct expansion of squared moduli gives
\[
\left|\frac{t+w}{1+tw}\right|\le\frac{t+s}{1+ts}.
\]
This is equivalent to the Schwarz–Pick pseudohyperbolic magnitude envelope; it becomes an equality for nonnegative real \(w\). Hence \(|\phi(z)|\le(t+u_c(r))/(1+t u_c(r))\). Applying \(|1-\overline z\phi(z)|\ge1-r|\phi(z)|\) gives the displayed \(E_{t,c}(r)\), whose denominator is strictly positive for every \(r<1\).

**Simultaneous sharpness.** Define \(h_c(w)=(c+w)/(1+cw)\) for \(0\le c\le1\), interpreting \(h_1\equiv1\). Put \(\eta_c(w)=w h_c(w)\), and for any desired center \(b=t\omega\), set
\[
\varphi_{b,c}(z)=\omega\frac{t+\eta_c(\overline\omega z)}{1+t\eta_c(\overline\omega z)}.
\]
It is an analytic disk selfmap with \(|\varphi_{b,c}(0)|=t\) and \(|\varphi'_{b,c}(0)|=(1-t^2)c\). At \(z=r\omega\), the three magnitude inequalities above are exact, giving \(|\widetilde C_{\varphi_{b,c}}(r\omega)|=E_{t,c}(r)\) for every \(r\). For \(c<1\) the normalized map is a finite Blaschke product of degree two (also when \(c=0\)); for \(c=1\) it is a disk automorphism. Maximizing over \(r\) proves the sharp constrained global-radius formula.

**Rigidity at the universal bound.** Since \(u_c(r)\le r\), \(E_{t,c}(r)\le1+tr\). Also
\[
\lim_{r\uparrow1} E_{t,c}(r)
=\frac{2(1+t)(1+c)}{(1+t)(1+c)+2(1-t)}.
\]
If \(0<t<1\) and \(c<1\), this limit is strictly below \(1+t\). Were \(\operatorname{ber}(C_\phi)=1+t\), an extremizing sequence would have \(r\to1\), since \(E_{t,c}(r)\le1+tr\); the strict limit excludes this. Thus \(c=1\). Equality in Schwarz's lemma then forces \(h(z)\equiv\tau\), \(|\tau|=1\), and \(\phi(z)=(t+\tau z)/(1+t\tau z)\).

Choose \(z_n\) with \(|\widetilde C_\phi(z_n)|\to1+t\). Passing to a subsequence gives \(z_n\to\zeta\in\partial\mathbb D\). Since the numerator \(1-|z_n|^2\to0\), the nonzero limiting modulus implies \(\phi(\zeta)=\zeta\). The inequality \(|\widetilde C_\phi(z_n)|\le(1-|z_n|^2)/(1-|z_n|\,|\phi(z_n)|)\) implies
\[
\limsup_n\frac{1-|\phi(z_n)|}{1-|z_n|}\le\frac{1-t}{1+t}.
\]
For the Möbius map \(\phi\), the exact automorphism identity
\[
1-|\phi(z)|^2=\frac{(1-t^2)(1-|z|^2)}{|1+t\tau z|^2}
\]
shows that this ratio has limit \((1-t^2)/|1+t\tau\zeta|^2\). Hence \(|1+t\tau\zeta|\ge1+t\). As \(t>0\), equality in the triangle inequality forces \(\tau\zeta=1\). Therefore \(\phi(\zeta)=1\), and the fixed-point relation forces \(\zeta=1\) and \(\tau=1\). Undoing the initial rotation gives exactly \(\varphi(z)=(z+b)/(1+\overline b z)\). Conversely, for this symbol, evaluation along \(z=r\omega\) yields \(1+tr\to1+t\), proving sufficiency.

If \(t=0\), the known general bound gives radius at most one, and evaluation at the origin equals one, completing the exception.

## Verification
A standalone Python checker uses exact fractions on grids \(t\in\{0,0.1,\ldots,0.9\}\), \(c\in\{0,0.1,\ldots,1\}\), and \(r\in\{0,0.01,\ldots,0.99\}\) to confirm algebraic equality at the extremizer, envelope monotonic comparison, and the boundary strictness. It also checks complex angular samples. The executed result was `PASS: 34360 exact-rational and complex sample assertions`. These finite verifications are auxiliary; the proof covers all parameters and all analytic selfmaps.

## Relationship to prior work
Bourdon, Le, and Thompson [1, Proposition 2.1] established the general bound \(\operatorname{ber}(C_\varphi)\le1+|\varphi(0)|\) and examined Berezin ranges and convexity for affine symbols. The present theorem determines the *sharp entire radius profile* conditional on the first derivative, produces simultaneous degree-two Blaschke extremizers, and characterizes equality in their universal upper bound for all disk selfmaps with nonzero center. Augustine, Garayev, and Shankar [2] investigated Berezin-range convexity in Hardy and Bergman settings, including automorphic examples. Their studied convexity statements do not supply this constrained radial envelope or universal-bound rigidity.

## Limitations
The exact constrained global Berezin radius is represented as the maximum of a completely explicit one-variable rational profile; its critical points are not classified here. The result concerns \(H^2(\mathbb D)\) with the standard Szegő kernel, not weighted Bergman kernels, and makes no claim of priority beyond the inspected sources. The extremal rigidity fails when \(\varphi(0)=0\), where every origin-fixing symbol has radius one. A previously unnoticed equivalent expression in broader Schwarz–Pick extremal literature remains a historical-priority risk.

## References
[1] P. Bourdon, T. Le, D. Thompson, *Berezin ranges of composition operators on* \(H^2\), arXiv:2610.17634v1 (first posted 2026-10-13), especially Proposition 2.1 and Sections 3–4.

[2] A. Augustine, M. Garayev, P. Shankar, *Composition operators, convexity of their Berezin range and related questions*, arXiv:2302.12547v2 (2023), Section 4.
