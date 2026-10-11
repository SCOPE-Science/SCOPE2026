# Two-term boundary-period law and velocity skew for a cubic global center

## Finding
For real \(\alpha\) and \(\kappa>0\), set \(\Delta=4\kappa-\alpha^2\) and assume \(\Delta>0\). Consider the **original-time** cubic differential system
\[
\dot x=v,\qquad \dot v=-x\,p(v),\qquad p(v)=1-\alpha v+\kappa v^2.
\]
For every \(A>0\), exactly one periodic orbit \(\Gamma_A\) crosses the positive horizontal axis at \((A,0)\). Let \(T(A)\) denote its minimal period in the time variable displayed above; let \(v_+(A)>0>v_-(A)\) be its positive and negative velocity extrema. Then, as \(A\to\infty\),
\[
T(A)=\frac{4\pi}{A\sqrt\Delta}\left(1+\frac{C_{\alpha,\kappa}}{A^2}+O(A^{-4})\right),\qquad
C_{\alpha,\kappa}=\frac{1}{2\kappa}\log\frac{\Delta}{\kappa}+\frac{\alpha}{\kappa\sqrt\Delta}\arctan\frac{\alpha}{\sqrt\Delta}>0,
\]
and
\[
\lim_{A\to\infty}\frac{v_+(A)}{|v_-(A)|}=\exp\left(-\frac{\pi\alpha}{\sqrt\Delta}\right).
\]
The first two coefficients of the physical-time period and the limiting velocity asymmetry are thus explicit throughout the entire open discriminant region, not just on a selected numerical slice.

In addition, for \(A\downarrow0\),
\[
T(A)=2\pi\left(1+\frac{\alpha^2-3\kappa}{24}A^2+O(A^4)\right).
\]
The local coefficient is **not claimed to be new**: it is the reduced Kukles period coefficient calculated in Rousseau--Toni (1997). Together with the decay \(T(A)\to0\), it implies that whenever \(3\kappa<\alpha^2<4\kappa\), the period function has at least one global maximum attained at a finite, strictly positive amplitude. In contrast, for \(\alpha=0\) the period decreases strictly on \((0,\infty)\). No assertion about the number or nondegeneracy of interior critical periods is made.

## Assumptions and scope
The parameters are constants \(\alpha\in\mathbb R\), \(\kappa>0\) with \(\Delta=4\kappa-\alpha^2>0\). The amplitude \(A\) is the positive \(x\)-axis intercept, not an energy or an asymptotically rescaled amplitude. All times are from the polynomial ODE as written. Endpoints \(\kappa=0\) and \(\Delta=0\) are excluded. The result concerns regular periodic orbits in the entire plane and their large-amplitude geometry.

## Proof
**Exact center foliation.** The completed square
\[
p(v)=\kappa\left(v-\frac{\alpha}{2\kappa}\right)^2+\frac{\Delta}{4\kappa}>0
\]
shows that
\[
K(v)=\int_0^v\frac{u}{p(u)}\,du,\qquad H(x,v)=\frac{x^2}{2}+K(v)
\]
is a first integral, because \(\dot H=xv+(v/p(v))(-xp(v))=0\). Here \(K'(v)=v/p(v)\), so \(K\) strictly increases away from zero in the outgoing directions and has unique minimum \(K(0)=0\). More precisely, as \(v\to\pm\infty\), \(K(v)=\kappa^{-1}\log|v|+O(1)\). Thus \(H\) is proper, has only one critical point, and its positive levels are smooth simple closed curves. A nonvanishing tangent vector field on each such compact curve produces a periodic orbit. Its turning points are exactly \((\pm A,0)\) at energy \(E=A^2/2\).

**Exact passage-time representation.** Let \(v_-(E)<0<v_+(E)\) be the unique solutions of \(K(v)=E\). The two passages from one velocity extremum to the other have \(|x|=\sqrt{A^2-2K(v)}\) and \(|\dot v|=|x|p(v)\). Therefore
\[
T(A)=2\int_{v_-(E)}^{v_+(E)}\frac{dv}{p(v)\sqrt{A^2-2K(v)}}.
\]
Define \(F(t)=1/v_+(t)-1/v_-(t)>0\), for \(t>0\). Splitting the integral into the positive and negative velocity branches gives the exact identity
\[
A T(A)=2\int_0^E\frac{F(t)}{\sqrt{1-t/E}}\,dt,\qquad E=A^2/2.
\]
As \(t\downarrow0\), \(F(t)=O(t^{-1/2})\). Since \(K(v)=\kappa^{-1}\log|v|+O(1)\) at both ends, \(F(t)=O(e^{-\kappa t})\) at infinity. Consequently all nonnegative integral moments \(\int_0^\infty t^jF(t)\,dt\) exist. On \(t\le E/2\), Taylor's theorem uniformly gives
\[
(1-t/E)^{-1/2}=1+\frac{t}{A^2}+O\left(\frac{t^2}{A^4}\right).
\]
On \(E/2<t<E\), exponential decay of \(F\) and integrability of the square-root singularity make the entire contribution exponentially small (in \(A^2\)). Extending truncated moments to infinity has the same property. Hence
\[
A T(A)=2I_0+\frac{2I_1}{A^2}+O(A^{-4}),\qquad
I_0=\int_{-\infty}^{\infty}\frac{dv}{p(v)},\quad
I_1=\int_{-\infty}^{\infty}\frac{K(v)}{p(v)}\,dv.
\]
The equality for the moments follows from \(dt=\frac{v}{p(v)}dv\) on each velocity branch, with the correct reversal of integration orientation on the negative branch.

**Evaluation of both coefficients.** Put \(\theta=\arctan((2\kappa v-\alpha)/\sqrt\Delta)\) and \(\theta_0=\arctan(\alpha/\sqrt\Delta)\). Then
\[
\frac{dv}{p(v)}=\frac{2}{\sqrt\Delta}\,d\theta,\qquad
K(v)=\frac{\log p(v)}{2\kappa}+\frac{\alpha}{\kappa\sqrt\Delta}(\theta+\theta_0),\qquad
p(v)=\frac{\Delta}{4\kappa}\sec^2\theta.
\]
The integration range is \(\theta\in(-\pi/2,\pi/2)\). Using \(\int_{-\pi/2}^{\pi/2}\log(\cos\theta)\,d\theta=-\pi\log2\), we find
\[
I_0=\frac{2\pi}{\sqrt\Delta},\qquad
\frac{I_1}{I_0}=\frac{\log(\Delta/\kappa)}{2\kappa}+\frac{\alpha\theta_0}{\kappa\sqrt\Delta}=C_{\alpha,\kappa}.
\]
For positivity, let \(z=\alpha/\sqrt\Delta\). Since \(\Delta/\kappa=4/(1+z^2)\),
\[
\kappa C_{\alpha,\kappa}=\log2-\frac12\log(1+z^2)+z\arctan z.
\]
This is even and its derivative is \(\arctan z\), so its strict global minimum is \(\log2>0\). Substitution into the preceding period identity proves the stated two-term law.

**Velocity-extrema asymmetry.** The same explicit primitive gives
\[
K(v)=\frac{\log|v|}{\kappa}+C_\pm+o(1)\quad(v\to\pm\infty),\qquad
C_+-C_-=\frac{\pi\alpha}{\kappa\sqrt\Delta}.
\]
Because \(K(v_+(E))=K(v_-(E))=E\), subtracting the two equations yields
\[
\log\frac{v_+(E)}{|v_-(E)|}\longrightarrow-\kappa(C_+-C_-)
=-\frac{\pi\alpha}{\sqrt\Delta}.
\]
The extrema occur on the vertical axis because \(\dot v=-xp(v)\) and \(p>0\).

**Local behavior and the maximum.** Introduce \(w=\operatorname{sgn}(v)\sqrt{2K(v)}\), an increasing analytic global coordinate with \(w(0)=0\), \(w'(0)=1\). Then \(x^2+w^2=A^2\), and original-time period is
\[
T(A)=\int_0^{2\pi}\frac{A\sin\theta}{v(A\sin\theta)}\,d\theta,
\]
interpreting the quotient continuously at zero. Taylor inversion gives
\[
v(w)=w-\frac\alpha3 w^2+\left(\frac{\alpha^2}{36}+\frac\kappa4\right)w^3+O(w^4),\qquad
\frac{w}{v(w)}=1+\frac\alpha3w+\frac{\alpha^2-3\kappa}{12}w^2+O(w^3).
\]
A full angular integration kills odd powers, giving the local expansion above, consistent with Rousseau--Toni. If \(\alpha^2>3\kappa\), the period is strictly larger than \(2\pi\) for sufficiently small positive \(A\), whereas it tends to zero as \(A\to\infty\). Continuity, combined with its finite limit \(2\pi\) at zero, implies a global maximum at some interior amplitude \(A_*>0\). For \(\alpha=0\), \(K(v)=\frac{1}{2\kappa}\log(1+\kappa v^2)\), whence \(w/v(w)=\sqrt\kappa\,|w|/\sqrt{e^{\kappa w^2}-1}\), which is strictly decreasing in \(|w|>0\) because \(1-e^{-u}<u\) for \(u>0\). Thus \(T(A)\) strictly decreases when \(\alpha=0\).

## Verification
The standalone file `tools/check_period.py` verifies the first-integral differentiation identity, the analytic small-amplitude coefficient, the explicit discriminant substitutions, the closed-form two-term coefficient and its positive-minimum identity. Run `python tools/check_period.py` with Python 3 and SymPy. As an independent numerical sanity check (not a proof), for \(\alpha=0\), \(\kappa=1\), direct quadrature at amplitudes \(A=10\) and \(A=20\) gave \(A T(A)/(2\pi)=1.0071372635\) and \(1.0017452358\), compared with two-term predictions \(1.0069314718\) and \(1.0017328680\), respectively. The proof is analytic; these finite computations do not establish the asymptotic limits by themselves.

## Relationship to prior work
Appis and Llibre (2024), Theorem 4(c), already identify precisely this open discriminant region as a global-center locus (in their notation \(a_2=\alpha\), \(a_6=-\kappa\), \(a_4=0\)). Their paper establishes the phase portrait, not the two-term physical-time period law or velocity-extrema asymmetry. Rousseau and Toni (1997) calculate the local reduced Kukles period coefficient; the above local calculation is cited only to connect known local behavior to the new large-amplitude law, not to claim new local coefficients. Christopher, Jun Zhang and Weinian Zhang (2026) prove broad Cherkas-system global-center and non-isochronicity results using compactification and analyze qualitative period behavior near infinity; the inspected non-isochronicity proof does not state the present exact coefficients, limiting skew ratio, or this mixed local-to-global maximum implication. These are statement-to-statement comparisons rather than title comparisons.

## Limitations
No uniqueness, hyperbolicity, or multiplicity of interior critical periods is asserted; no conclusions apply at \(\Delta=0\) or \(\kappa=0\). The large-amplitude expansion is for fixed parameters, and no uniformity is claimed as \(\Delta\downarrow0\). The expansion is in the original time and positive turning amplitude \(A\); rescaling either changes coefficients. The literature comparison is finite, and unindexed or unpublished equivalent results remain possible. Independent validation has not been performed.

## References
Appis, R. F., and Llibre, J. *Global centers of a family of cubic systems*, Aequationes Mathematicae **98** (2024), 1373–1389, DOI 10.1007/s00010-024-01051-7; first public 2024-04-05; openly accessible full text at `https://pmc.ncbi.nlm.nih.gov/articles/PMC11374847/`.

Rousseau, C., and Toni, B. *Local Bifurcations of Critical Periods in the Reduced Kukles System*, Canadian Journal of Mathematics **49** (1997), 338–358, DOI 10.4153/CJM-1997-017-4; full Cambridge PDF examined.

Christopher, C., Zhang, J., and Zhang, W. *Global center of polynomial Newton system and its non-isochronicity*, arXiv:2602.07315v1 (2026-02-07), openly accessible full text `https://arxiv.org/html/2602.07315v1`.
