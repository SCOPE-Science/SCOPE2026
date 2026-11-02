# Exact second-flip boundary and local attracting four-cycle in a rational unimodal map

## Finding
Consider the rational interval family
\[
K_\mu(x)=\frac{\mu x(1-x)}{1+x},\qquad x\in[0,1],\qquad 0<\mu\le 3+2\sqrt2.
\]
Its unique primitive two-cycle exists exactly when \(\mu>\mu_b=2+\sqrt5\). Its two points are
\[
p_\pm(\mu)=\frac{\mu+1}{2\mu}\pm\frac1{2\mu}\sqrt{\frac{(\mu+1)(\mu^2-4\mu-1)}{\mu-1}},
\]
and its multiplier is
\[
\Lambda_2(\mu)=1-\frac{(\mu^2-1)(\mu^2-4\mu-1)}{2\mu^2}.
\]
The two-cycle is attracting exactly on \(\mu_b<\mu<\mu_f\), has multiplier \(-1\) at
\[
\boxed{\mu_f=1+\sqrt2+\sqrt{4+2\sqrt2}=5.027339492125848\ldots},
\]
and is repelling on \(\mu_f<\mu\le3+2\sqrt2\). Thus the second period doubling occurs at a closed radical parameter, rather than the previously tabulated numerical values near \(5.03\).

Moreover, the flip at \(\mu_f\) is nondegenerate and supercritical. There is an \(\varepsilon>0\) such that for every \(\mu_f<\mu<\mu_f+\varepsilon\) exactly one primitive attracting four-cycle lies in sufficiently small fixed neighborhoods of the former two-cycle, and no primitive four-cycle lies in those neighborhoods for \(\mu_f-\varepsilon<\mu<\mu_f\). With \(\delta=\mu-\mu_f\), for each \(\sigma\in\{-,+\}\) the two points near \(p_\sigma(\mu_f)\) have asymptotics
\[
x_{\sigma,\pm}(\mu)=p_\sigma(\mu_f)\pm C_\sigma\sqrt\delta+O(\delta),
\qquad C_->0,\quad C_+>0.
\]
The two amplitudes are \(C_-=0.211072666779666\ldots\) and \(C_+=0.101360669114122\ldots\). The four-cycle return multiplier is
\[
\boxed{\Lambda_4(\mu)=1-4a\delta+O(\delta^{3/2})},\qquad
 a=\frac{(\mu_f^2+1)(\mu_f^2-2\mu_f-1)}{\mu_f^3}>0.
\]
No assertion is made about other four-cycles away from these neighborhoods or the global basin.

## Assumptions and scope
The state space is the closed interval \([0,1]\). The restriction \(0<\mu\le3+2\sqrt2\) ensures that it is forward invariant: the unique critical point \(c=\sqrt2-1\) has image \(K_\mu(c)=\mu(3-2\sqrt2)\le1\), and both endpoints map to zero. A primitive \(r\)-cycle means \(r\) distinct points of least period \(r\). An attracting cycle has return multiplier of absolute value strictly less than one; a repelling cycle has multiplier absolute value greater than one. The constants in the local error terms are uniform for sufficiently small positive \(\delta\).

For explicit exact amplitudes, put \(p=p_\pm(\mu_f)\), \(q=K_{\mu_f}(p)\) (the other point of the two-cycle), and
\[
D_\pm=\frac{1}{(p^2+2p-1)^2}
       +\frac{K_{\mu_f}'(p)^2}{(q^2+2q-1)^2},
\qquad
\boxed{C_\pm=\sqrt{\frac{a}{2D_\pm}}}.
\]
All denominators in these formulas are nonzero, and \(D_\pm>0\).

## Proof
**1. Forward invariance and the complete two-cycle census.** Differentiation gives
\[
K_\mu'(x)=\frac{\mu(1-2x-x^2)}{(1+x)^2};
\]
hence the maximum of \(K_\mu\) on \([0,1]\) occurs at \(c=\sqrt2-1\) and equals \(\mu(3-2\sqrt2)\). Direct composition, with a denominator nonzero for \(x\in[0,1]\) and the stated parameters, yields the exact rational identity
\[
K_\mu^2(x)-x=
\frac{x\bigl((\mu+1)x-(\mu-1)\bigr)Q_\mu(x)}
{(x+1)(\mu x^2-\mu x-x-1)},
\quad Q_\mu(x)=\mu(\mu-1)x^2-(\mu^2-1)x+\mu+1.
\]
The two linear factors give fixed points \(0\) and, when \(\mu>1\), \((\mu-1)/(\mu+1)\). The discriminant of the quadratic is
\[
\operatorname{disc}(Q_\mu)=(\mu^2-1)(\mu^2-4\mu-1).
\]
For \(0<\mu<1\), \(Q_\mu\) is concave on \([0,1]\), with strictly positive endpoint values \(Q_\mu(0)=\mu+1\) and \(Q_\mu(1)=2\), hence has no interval root; for \(\mu=1\) it is the constant \(2\). For \(1<\mu<\mu_b\), its discriminant is negative. At \(\mu_b\) its double root coincides with the nonzero fixed point, so no primitive two-cycle exists. For \(\mu>\mu_b\), the quadratic has the two distinct stated roots. They lie in \((0,1)\): positivity follows from \((\mu+1)(\mu-1)>(\mu^2-4\mu-1)\), and the upper root is less than one since
\[
(\mu-1)^3-(\mu+1)(\mu^2-4\mu-1)=8\mu>0.
\]
Neither root is a fixed point (the only coincidence is the double root at \(\mu_b\)); therefore they form the unique primitive two-cycle.

**2. Exact multiplier and strict stability phases.** The two roots have elementary symmetric functions
\[
p_-+p_+=\frac{\mu+1}{\mu},\qquad p_-p_+=\frac{\mu+1}{\mu(\mu-1)}.
\]
Substituting these into \(K_\mu'(p_-)K_\mu'(p_+)\) gives \(\Lambda_2(\mu)\) as stated. Moreover
\[
-\Lambda_2'(\mu)=\frac{(\mu^2+1)(\mu^2-2\mu-1)}{\mu^3}>0
\qquad(\mu\ge\mu_b).
\]
The multiplier decreases strictly from \(+1\) at \(\mu_b\). The equation \(\Lambda_2=-1\) is equivalent to
\[
\mu^4-4\mu^3-6\mu^2+4\mu+1=0.
\]
Factoring over \(\mathbb Q(\sqrt2)\) gives the sole solution in \((\mu_b,3+2\sqrt2]\) as \(\mu_f=1+\sqrt2+\sqrt{4+2\sqrt2}\). In particular \(\mu_b<\mu_f<3+2\sqrt2\); monotonicity yields all asserted stability inequalities.

**3. Strict Schwarzian sign and nondegenerate flip.** The Schwarzian derivative, defined wherever \(K_\mu'\ne0\) by \(Sf=f'''/f'-(3/2)(f''/f')^2\), is
\[
S K_\mu(x)=-\frac{12}{(x^2+2x-1)^2}<0.
\]
Set \(G_\mu=K_\mu^2\). Its two fixed points \(p_-(\mu),p_+(\mu)\) persist analytically near \(\mu_f\). On each of them, \(G_{\mu_f}'=-1\) and both derivatives along the orbit are nonzero. By the Schwarzian chain rule,
\[
S G_{\mu_f}(p)=S K_{\mu_f}(p)
 +S K_{\mu_f}(q)K_{\mu_f}'(p)^2=-12D_\pm<0.
\]
The transversal parameter derivative is \(\Lambda_2'(\mu_f)=-a<0\), with \(a>0\) as above. The flip is therefore transverse and its cubic normal-form coefficient is strictly positive, as verified directly in the following calculation.

**4. Local creation, amplitudes, and attracting multiplier.** Fix either persistent branch \(p=p_\pm(\mu)\) and let \(u=x-p\), \(\delta=\mu-\mu_f\). Taylor expansion of \(G_\mu\) gives
\[
G_\mu(p+u)-p=-(1+a\delta)u+A u^2+B u^3
       +O(\delta^2|u|+|\delta|u^2+|u|^4),
\]
with \(A=G_{\mu_f}''(p_\pm(\mu_f))/2\), \(B=G_{\mu_f}'''(p_\pm(\mu_f))/6\). At derivative \(-1\), the Schwarzian identity simplifies to
\[
q:=A^2+B=-\frac16S G_{\mu_f}(p_\pm(\mu_f))=2D_\pm>0.
\]
Composing the Taylor series once more gives
\[
G_\mu^2(p+u)-(p+u)
 =2a\delta u-2q u^3
   +O(\delta^2|u|+|\delta|u^2+|u|^4).
\]
The factor \(u\) accounts for the persisting old cycle. For \(u\ne0\), divide by \(u\). For \(\delta>0\), putting \(u=\sqrt\delta\,v\) gives the reduced equation
\[
2a-2qv^2+O(\sqrt\delta)=0,
\]
whose two simple roots converge to \(v=\pm\sqrt{a/q}=\pm C_\pm\). The implicit-function theorem in the variable \(\sqrt\delta\) yields exactly two local nonzero roots, at
\[
u=\pm C_\pm\sqrt\delta+O(\delta).
\]
For \(\delta<0\) the divided equation is strictly negative for all sufficiently small \(u\), because its leading terms are \(2a\delta-2qu^2\); thus no nonzero local roots occur. This proves the one-sided local birth and exclusion. There are two new points of period two for \(G_\mu\) near each original point; the map \(K_\mu\) exchanges the neighborhoods and carries them into the same primitive four-cycle. No other new four-cycle occurs in those neighborhoods, by the local root count.

Finally, differentiate the composed expansion at a new fixed point of \(G_\mu^2\):
\[
(G_\mu^2)'=1+2a\delta-6q u^2+O(\delta^{3/2})
=1-4a\delta+O(\delta^{3/2}).
\]
It lies strictly between \(-1\) and \(+1\) for all sufficiently small positive \(\delta\). The new four-cycle is attracting. This completes the proof.

## Verification
The standalone file `checks/verify.py` uses SymPy to check the rational factorization of \(K_\mu^2-x\), the quadratic discriminant, the two-cycle multiplier modulo \(Q_\mu\), the quartic radical root, the Schwarzian identity, and the parameter derivative. It also uses high-precision arithmetic to locate the four near-critical points for a small positive perturbation and to check their distinctness, return multiplier, and leading square-root scales. Run from the package root with `python checks/verify.py` (dependencies: `sympy`, `mpmath`). These finite diagnostics supplement but do not prove the existence, uniqueness, or all-parameter statements; those follow from the preceding algebra and local implicit-function argument.

## Relationship to prior work
Kumar, Alzabut, Kumari, Rani and Chugh (2022) introduced this precise map, determined its fixed points, and gave numerical plots of a period-two window ending around \(\mu=5.033\), followed by a period-four example at \(\mu=5.1\). Their paper does not give the closed form of the second flip, the exact two-cycle multiplier, or the local four-cycle square-root coefficients. Conejero, Lizama and Quijada (2025) subsequently studied a two-parameter family containing this map as the \(\lambda=1\) slice; the publicly indexed bifurcation section still lists a numerical threshold near \(5.03\). Its complete text could not be inspected in this comparison, leaving a priority risk. The generic flip mechanism and Schwarzian chain rule are classical; the family-specific exact threshold, complete two-cycle stability phase, and both explicit four-cycle amplitudes are the asserted contribution.

## Limitations
The theorem does not classify the global attractor, the number of four-cycles elsewhere in the interval, higher period-doubling thresholds, or chaotic parameter sets. The nondegenerate four-cycle conclusion is local in \(\mu\) near \(\mu_f\). The numerical checker is not a proof of infinite statements. Originality is relative to the sources inspected; inaccessible or unindexed equivalent results may exist. Independent mathematical validation has not been performed.

## References
1. A. Kumar, J. Alzabut, S. Kumari, M. Rani, R. Chugh, “Dynamical properties of a novel one dimensional chaotic map,” *Mathematical Biosciences and Engineering* **19** (2022), 2489–2505. DOI: `10.3934/mbe.2022115`. First published 2022-01-07. Full text: https://www.aimspress.com/aimspress-data/mbe/2022/3/PDF/mbe-19-03-115.pdf.
2. J. A. Conejero, C. Lizama, D. Quijada, “Dynamical Properties for a Unified Class of One-Dimensional Discrete Maps,” *Mathematics* **13** (2025), 518. DOI: `10.3390/math13030518`. https://www.mdpi.com/2227-7390/13/3/518.
