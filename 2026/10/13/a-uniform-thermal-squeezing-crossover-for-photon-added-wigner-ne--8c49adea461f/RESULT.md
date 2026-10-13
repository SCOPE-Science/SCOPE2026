# A uniform thermal–squeezing crossover for photon-added Wigner negativity

## Finding
For a normalized single-photon-added squeezed thermal state, the integrated negative Wigner volume has a **uniform joint high-temperature and large-squeezing crossover**. Let \(t=(1-q)/(1+q)\) be the thermal purity parameter and \(r\geq0\) the real squeezing parameter. Set \(s=t e^{2r}\). In fact, for every \(0<t\le1\) and \(r\ge0\), without restriction on \(s\), the **explicit relative-error bound**
\[
\left|\frac{\mathcal N(t,r)}{t^3\mathcal G(s)}-1\right|\le 12\bigl(e^{-4r}+t e^{-2r}+t^2\bigr)
\tag{A}
\]
holds for the explicit, strictly positive function
\[
\mathcal G(s)=\frac{2}{s(1+s)}\int_0^{1+s/2}(1+s/2-u)
 e^{-su/[2(1+s)^2]}I_0\!\left(\frac{su}{2(1+s)^2}\right)\,du
\quad(s>0).
\]
Here \(I_0\) denotes the modified Bessel function of order zero. Its endpoint values are
\[
\mathcal G(s)\sim s^{-1}\quad(s\downarrow0),\qquad
\mathcal G(s)\longrightarrow \kappa\quad(s\to\infty),
\]
where
\[
\kappa=2\int_0^{1/2}(1/2-u)e^{-u/2}I_0(u/2)\,du
=0.230968177814117\ldots>0.
\]
In particular, for any fixed \(r\ge0\),
\[
\mathcal N(t,r)\sim\frac{t^2}{2\cosh(2r)},\qquad t\downarrow0,
\]
whereas along every high-temperature path \(t\downarrow0\) satisfying \(t e^{2r}\to\infty\), \(\mathcal N(t,r)\sim\kappa t^3\). Along paths with \(t\downarrow0\) and \(s\to\lambda\in(0,\infty)\), one has \(\mathcal N(t,r)/t^3\to\mathcal G(\lambda)\).

There is also an exact sharp large-squeezing envelope. For fixed \(t\in(0,1]\), define \(F(t)=\lim_{r\to\infty}\mathcal N(t,r)\). Then
\[
F(t)=\frac{2t^3}{\pi}\iint_{w^2+v^2<1/2}
 (1/2-w^2-v^2)e^{-w^2-t^2v^2}\,dw\,dv,
\]
and the quotient \(F(t)/t^3\) is strictly decreasing on \((0,1]\). Consequently its exact sharp range is
\[
\left(2e^{-1/2}-1\right)t^3\le F(t)<\kappa t^3.
\]
Equality in the lower bound holds exactly at \(t=1\); the upper constant is approached as \(t\downarrow0\).

## Assumptions and scope
Use one bosonic optical mode with annihilation operator \(a\), creation operator \(a^\dagger\), and \([a,a^\dagger]=1\). Let \(q\in[0,1)\), \(\rho_q=(1-q)\sum_{n\ge0}q^n|n\rangle\langle n|\), and \(S(r)=\exp[\frac r2(a^2-a^{\dagger 2})]\) with \(r\ge0\). The normalized state is
\[
\rho^+_{q,r}=\frac{a^\dagger S(r)\rho_q S(r)^\dagger a}{\operatorname{Tr}[a a^\dagger S(r)\rho_q S(r)^\dagger]}.
\]
Use real phase-space variables \((x,p)\) and the convention \(W_{|0\rangle}(x,p)=\pi^{-1}e^{-(x^2+p^2)}\); all Wigner functions integrate to one. We measure **negative volume**, not doubled negativity:
\[
\mathcal N(t,r)=\iint_{\mathbb R^2}\max\{0,-W_{\rho^+_{q,r}}(x,p)\}\,dx\,dp,
\qquad t=\frac{1-q}{1+q}.
\]
The assertions for \(t\downarrow0\) require \(q\uparrow1\) and apply to exact idealized thermal, squeezing and photon-addition operations. The exact inequality (A) holds for every positive \(t\le1\) and \(r\ge0\), though its right side is asymptotically small specifically when \(t\to0\) and \(r\to\infty\). The sharp fixed-\(t\) envelope also allows \(t=1\).

## Proof
**1. Normalized Wigner function.** Write \(\gamma=\cosh(2r)\) and \(\alpha=(x+ip)/\sqrt2\). The squeezed thermal Gaussian has
\[
W_G(x,p)=\frac t\pi\exp[-t(e^{2r}x^2+e^{-2r}p^2)].
\]
With the standard Weyl correspondences, left multiplication by \(a^\dagger\) acts as \(\alpha^*-\tfrac12\partial_\alpha\), and right multiplication by \(a\) as \(\alpha-\tfrac12\partial_{\alpha^*}\). Applying both gives
\[
W_{a^\dagger\rho_G a}=\frac12\left[(1+t e^{2r})^2x^2+(1+t e^{-2r})^2p^2-(1+t\gamma)\right]W_G.
\]
The positive trace of \(a^\dagger\rho_Ga\) is \((\gamma+t)/(2t)\). Hence
\[
W_{t,r}(x,p)=\frac{t^2}{\pi(\gamma+t)}e^{-t(e^{2r}x^2+e^{-2r}p^2)}
\left[(1+t e^{2r})^2x^2+(1+t e^{-2r})^2p^2-1-t\gamma\right].\tag{1}
\]
Direct Gaussian integration verifies \(\iint W_{t,r}=1\): the Gaussian expectation of the square-bracket factor is \(\gamma/t+1\). Its negative region is precisely the ellipse where that bracket is negative.

**2. Exact positive integral.** Put \(s=t e^{2r}\), \(z=t e^{-2r}\), so \(sz=t^2\), and define
\[
A_s=\frac{(1+s)^2}{s},\quad B_z=\frac{(1+z)^2}{z},\quad
C_{s,z}=1+\frac{s+z}{2},\quad C_s=1+\frac s2.
\]
In the phase-space coordinates \(y=\sqrt{s}\,x\), \(v=\sqrt{z}\,p\), the negative ellipse becomes \(A_sy^2+B_zv^2<C_{s,z}\). Change again to \(Y=\sqrt{A_s}y\), \(V=\sqrt{B_z}v\), and then set \(Y=\sqrt u\cos\theta\), \(V=\sqrt u\sin\theta\). The polar Jacobian is \(du\,d\theta/2\). Angular integration using
\[
\frac1{2\pi}\int_0^{2\pi}e^{-u(\cos^2\theta/A+\sin^2\theta/B)}d\theta
=e^{-u(A^{-1}+B^{-1})/2}I_0\bigl(u(A^{-1}-B^{-1})/2\bigr)
\]
produces the exact identity
\[
\mathcal N(t,r)=\frac{2t^3}{(s+z+2t^2)(1+s)(1+z)}J(s,z),\tag{2}
\]
where \(J(s,z)\) is the integral from \(0\) to \(C_{s,z}\) of \(C_{s,z}-u\) times the above angular average with \(A=A_s\), \(B=B_z\). Let \(J(s,0)\) use \(C_s\) and \(B^{-1}=0\). Then \(\mathcal G(s)=2J(s,0)/[s(1+s)]\), giving the displayed Bessel formula for \(\mathcal G\).

**3. Uniform comparison.** Because \(C_s/A_s=s(1+s/2)/(1+s)^2\le1/2\), the angular weight defining \(J(s,0)\) lies between \(e^{-1/2}\) and \(1\). Thus \(J(s,0)\ge e^{-1/2}C_s^2/2\), uniformly in \(s>0\). For \(u\le C_s\), adding the second Gaussian damping factor changes the weight by relative amount at most \(C_s/B_z\le z+t^2/2\). Enlarging the integration endpoint from \(C_s\) to \(C_s+z/2\) changes the nonnegative integral by at most \(z C_s/2+z^2/8\). It follows, uniformly for \(0<t\le1\), \(r\ge0\), that
\[
\frac{J(s,z)}{J(s,0)}=1+O(z+t^2).
\]
From (2), the remaining prefactor ratio is exactly
\[
\frac{\mathcal N(t,r)}{t^3\mathcal G(s)}
=\frac{J(s,z)}{J(s,0)}\,
\frac1{(1+z/s+2z)(1+z)},
\]
with \(z/s=e^{-4r}\). For completeness, the absolute constant can be chosen as \(12\). Writing \(\delta=z/2\) and using \(z\le1\), the endpoint-shift estimate divided by \(J(s,0)\ge e^{-1/2}C_s^2/2\) is at most \(e^{1/2}(z+z^2/4)\le2.061z\). The added Gaussian damping reduces the integrand by a relative amount no greater than \(C_{s,z}/B_z\le z+t^2/2+z^2/2\le1.5z+t^2/2\). Hence \(1-1.5z-t^2/2\le J(s,z)/J(s,0)\le1+2.061z\), and \(1-p\le e^{-4r}+3z\) for the positive prefactor ratio \(p=1/[(1+e^{-4r}+2z)(1+z)]\). Thus \(|pJ(s,z)/J(s,0)-1|\le3.061e^{-4r}+11.244z+t^2/2\le12(e^{-4r}+z+t^2)\). This proves the asserted **path-uniform relative bound (A)**. In particular, every path with \(t\to0\), \(r\to\infty\) lies in this common scaling law.

**4. Endpoint behavior and fixed squeezing.** As \(s\downarrow0\), \(C_s\to1\), \(A_s^{-1}\to0\), so \(J(s,0)\to\int_0^1(1-u)du=1/2\) by dominated convergence. This yields \(\mathcal G(s)\sim s^{-1}\). As \(s\to\infty\), substitute \(u=s\xi\) in \(J(s,0)\); since \(C_s/s\to1/2\) and \(s/A_s\to1\), dominated convergence gives \(\mathcal G(s)\to2\int_0^{1/2}(1/2-\xi)e^{-\xi/2}I_0(\xi/2)d\xi=\kappa\).

For fixed \(r\), equation (1) or the ellipse integral has \(A_s\sim1/(t e^{2r})\), \(B_z\sim1/(t e^{-2r})\), and \(C_{s,z}\to1\). The normalized ellipse integral consequently yields \(\mathcal N(t,r)/t^2\to1/[2\cosh(2r)]\); convergence is uniform when \(r\) stays in a compact interval. Combining this with the preceding limits gives all stated square-law, crossover, and cubic-law regimes. The special \(r=0\) case follows directly from (1).

**5. Sharp strongly squeezed envelope.** For fixed \(t>0\), substitute \(X=e^r x\) and \(P=e^{-r}p\) into (1), then let \(r\to\infty\). The resulting Gaussian-polynomial integrand converges on its negative set, which remains bounded after the further linear transformation \(w=\sqrt t X\), \(v=P/\sqrt t\). Gaussian domination proves the displayed disk-integral formula for \(F(t)\). For every \((w,v)\) in that disk, the integrand of \(F(t)/t^3\) is nonincreasing in \(t\), and it decreases strictly on a set of positive measure; hence the quotient is strictly decreasing. Its value at \(t=1\) is calculated in polar coordinates as \(2e^{-1/2}-1\), and its limit at \(t\downarrow0\) is \(\kappa\) by dominated convergence. This proves both sharp constants and the equality conditions.

## Verification
An included standalone Python checker uses independent polar-angle and Bessel-integral quadratures, checks Gaussian normalization and the one-photon benchmark, compares multiple finite squeezed-thermal parameter pairs, and tests the two asymptotic regimes and crossover profile. The verifier prints a success marker only if all assertions pass. Numerical checks support but do not replace steps 1–5, whose infinite-parameter assertions use exact identities and dominated-convergence bounds.

Run `python verify.py` with the accompanying `requirements.txt` dependencies installed. The script does not access networks, invoke symbolic theorem provers, or require other unpublished files.

## Relationship to prior work
Kenfack and Życzkowski (arXiv:quant-ph/0406015, first public 2004-06-02) introduced the negative-volume measure, with a convention twice the one used here. Xu, Hu and Fan (arXiv:0907.4817) and Hu and Zhang (arXiv:1110.6587) established Wigner negativity for single-photon-added squeezed thermal states and studied noise/decoherence. Hertz and De Bièvre (arXiv:2204.06358, especially Section VI A and Appendix E) obtained the Wigner formula and an **exact integral for the fixed-temperature large-squeezing limit**, together with numerical finite-parameter behavior and a small-thermal-noise approximation. Those identities and observations are antecedents, not contributions claimed here.

The distinction assessed here is the *simultaneous* high-temperature/large-squeezing asymptotic **uniform for every joint scaling path**, its explicit transition profile and error, and the resulting exact high-temperature coefficient and sharp strongly squeezed normalized range. The prior fixed-temperature integral is acknowledged and is compatible with the disk-integral specialization. These conclusions are analytic consequences of the established model, not claims that the underlying state or its Wigner formula is new.

## Limitations
The analysis concerns one ideal bosonic mode, thermal states with geometric Fock weights, exact single-photon addition **after** squeezing, real squeezing, and the integrated negative volume in the specified normalization. The result does not extend automatically to higher photon addition, displacement, mixed arbitrary Gaussian inputs, thermal-loss time evolution, multimode settings, or imperfect photon addition. The positive Wigner negativity persists for each finite temperature; statements about its asymptotic size do not imply a finite-temperature positivity threshold. The closest antecedent provides an exact fixed-temperature integral, so unlocated evaluations or alternate asymptotic presentations remain an originality risk.

## References
1. A. Kenfack and K. Życzkowski, *Negativity of the Wigner function as an indicator of nonclassicality*, arXiv:quant-ph/0406015 (first public 2004-06-02), https://arxiv.org/abs/quant-ph/0406015.
2. X.-x. Xu, L.-y. Hu and H.-y. Fan, *Photon-added squeezed thermal states: statistical properties and its decoherence in a photon-loss channel*, arXiv:0907.4817 (first public 2009-07-28), https://arxiv.org/abs/0907.4817.
3. L.-Y. Hu and Z.-M. Zhang, *Nonclassicality and decoherence of photon-added squeezed thermal state in thermal environment*, arXiv:1110.6587 (first public 2011-10-30), https://arxiv.org/abs/1110.6587.
4. A. Hertz and S. De Bièvre, *Decoherence and nonclassicality of photon-added/subtracted multi-mode Gaussian states*, arXiv:2204.06358 (first public 2022-04-13), https://arxiv.org/abs/2204.06358, Section VI A and Appendix E.
