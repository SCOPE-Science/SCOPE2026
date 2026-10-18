# Sharp quadratic concentration at a Fourier–Stieltjes zero

## Finding

**Theorem (sharp global rigidity).** Let \(\mu\) be a Borel probability measure on \(\mathbb R\) with finite second moment, let \(m=\int x\,d\mu(x)\), and suppose that its Fourier–Stieltjes transform \(\widehat\mu(t)=\int e^{itx}\,d\mu(x)\) vanishes at a nonzero real frequency \(t\). Put \(b=\pi/2\), \(c_*=4/\pi-1\), and \(\Delta=t^2\operatorname{Var}_\mu(X)-b^2\). Then

\[
\boxed{\Delta\ge c_*\int_{\mathbb R} \bigl(|t(x-m)|-b\bigr)^2\,d\mu(x).}
\]

The coefficient \(c_*\) is the **largest possible** universal coefficient, simultaneously over every probability measure and every nonzero Fourier zero. Furthermore \(\Delta=0\) exactly for the balanced two-atom law
\[
\mu=\tfrac12\delta_{m-b/|t|}+\tfrac12\delta_{m+b/|t|}.
\]
Every other admissible law has strict inequality in the displayed quadratic remainder.

Writing \(Y=t(X-m)\) and \(\nu_b=(\delta_{-b}+\delta_b)/2\), the theorem also implies for any \(r>0\)
\[
\mathbb P\bigl(\operatorname{dist}(Y,\{-b,b\})\ge r\bigr)
\le {\Delta\over c_*r^2},
\qquad
W_1(\mathcal L(Y),\nu_b)\le\sqrt{\Delta/c_*}+{b\Delta\over2c_*}.
\]
Here \(W_1\) is the usual transportation distance with cost \(|x-y|\). The latter estimate gives quantitative convergence to the complete balanced equality law, not merely to its two-point support.

## Assumptions and scope

Only a finite second moment, positivity and unit mass of the measure, and the **exact** Fourier zero \(\widehat\mu(t)=0\) are needed. Neither density nor compact support nor symmetry nor a first-zero assumption is required. The frequency \(t\) may have either sign. The normalization by the mean is essential; both terms in the inequality are dimensionless. The results are nonasymptotic except for the explicit sharpness family below.

## Proof

**Step 1: a pointwise two-contact certificate.** We prove for every real \(y\)
\[
 y^2+\pi\cos y-b^2\ge c_*(|y|-b)^2,
 \qquad b=\pi/2,\quad c_*=4/\pi-1.
\tag{1}
\]
Equality in (1) is possible only when \(|y|\in\{0,b\}\). By evenness take \(x=|y|\ge0\), and let \(F(x)\) denote left minus right of (1). Direct expansion gives
\[
 F(x)=\alpha x^2+\beta x+\pi(\cos x-1),\qquad
 \alpha=2-4/\pi>0,\quad\beta=4-\pi>0.
\]
We have \(F(0)=F(b)=0\), \(F'(0)=\beta>0\), \(F'(b)=0\), and
\[
 F'(x)=2\alpha x+\beta-\pi\sin x,\quad
 F''(x)=2\alpha-\pi\cos x,\quad F'''(x)=\pi\sin x.
\]
On \((0,b)\), \(F'''(x)>0\), so \(F''\) increases strictly from a negative number to \(2\alpha>0\); hence \(F'\) first decreases and then increases. Since \(F'(0)>0\), \(F'(b)=0\), and \(F''(b)>0\), it follows that \(F'\) has exactly one zero in \((0,b)\), changing from positive to negative there. Thus \(F(x)>0\) for \(0<x<b\). On \([b,\pi]\), \(F''(x)\ge2\alpha>0\), so \(F'\) is positive beyond \(b\). Finally, on \([\pi,\infty)\),
\[
 F'(x)\ge 2\alpha\pi+\beta-\pi=2\pi-4>0.
\]
Hence \(F(x)>0\) for every \(x>b\), completing (1), including its equality set.

**Step 2: integrate at a Fourier zero.** Let \(Y=t(X-m)\). Then \(\mathbb E Y=0\), \(\mathbb E Y^2=t^2\operatorname{Var}(X)\), and
\[
\mathbb E e^{iY}=e^{-itm}\widehat\mu(t)=0,
\qquad\mathbb E\cos Y=\mathbb E\sin Y=0.
\]
Integrating (1) gives exactly the claimed remainder. Pointwise equality requires \(Y\in\{0,-b,b\}\) almost surely. But \(\mathbb E\cos Y=0\) forces zero mass at \(Y=0\), while \(\mathbb E\sin Y=0\) forces equal probabilities at \(\pm b\). Conversely this balanced measure attains equality and has the required Fourier zero. The same argument proves strictness whenever \(\Delta>0\).

**Step 3: optimal coefficient.** For \(0<p<1/2\), set
\[
\theta_p=\arccos\!\left(-\frac{p}{1-p}\right),\qquad
\mu_p=p\delta_0+\frac{1-p}{2}(\delta_{-\theta_p}+\delta_{\theta_p}).
\]
Its mean is zero and \(\widehat\mu_p(1)=p+(1-p)\cos\theta_p=0\). As \(p\downarrow0\), \(\theta_p=b+p+O(p^2)\), so
\[
\Delta_p=(1-p)\theta_p^2-b^2
=p(\pi-\pi^2/4)+O(p^2),
\]
whereas the right-hand distance moment before multiplication by \(c_*\) is
\[
R_p=p b^2+(1-p)(\theta_p-b)^2=p\pi^2/4+O(p^2).
\]
Consequently \(\Delta_p/R_p\to (\pi-\pi^2/4)/(\pi^2/4)=c_*\). Any larger universal coefficient fails on this explicit family. Note that \(p>0\) yields strict inequality: optimality of \(c_*\) is an infimum, not a nontrivial equality case.

**Step 4: concentration and balancing.** The first consequence is Markov's inequality applied to the nonnegative random variable \((|Y|-b)^2\). For the transportation consequence define \(S=1\) when \(Y\ge0\), and \(S=-1\) otherwise. Set \(R=\mathbb E(|Y|-b)^2\). Coupling \(Y\) with \(bS\) costs at most \(\sqrt R\) in mean. Since \(\sin Y=S\cos(|Y|-b)\), including \(Y=0\), and \(\mathbb E\sin Y=0\), we have
\[
|\mathbb E S|=\left|\mathbb E S\bigl(1-\cos(|Y|-b)\bigr)\right|
\le\tfrac12 R.
\]
Moving the resulting excess signed-point mass to balance the atoms costs exactly \(b|\mathbb E S|\). Hence
\(W_1(\mathcal L(Y),\nu_b)\le\sqrt R+bR/2\). The main theorem gives \(R\le\Delta/c_*\), proving the displayed bound.

## Verification

The standalone `verify.py` uses only the Python standard library. It checks the exact contact/derivative identities numerically, samples the global scalar certificate at 100,000 positive points, reproduces the zero constraints of five three-atom laws, and checks convergence of the deficit-to-distance ratios to \(c_*\). Run using `python3 verify.py`. The proof for all real arguments and all probability measures is the analytic argument above; finite sampling is **not** substituted for it.

## Relationship to prior work

The inequality \(t\sqrt{\operatorname{Var}(X)}\ge\pi/2\) for a Fourier zero is the classical Mandelstam–Tamm orthogonality bound, **not** a new result. The new object here is the best-constant uniform *distance remainder*, including exact rigidity and transport consequences. Luo and Zhang's 2004 characteristic-function theorem controls first-zero locations using positive-axis moments but supplies no distance-to-the-two-atom-extremizer remainder. Huang's 2025 central-moment theorem handles general distributions through a different (nonsharp at second moment) scalar inequality and also gives no such remainder. Ismoilov's 2026 measure-dependent sign-uncertainty work analyzes prescribed-degree trigonometric-polynomial sign changes rather than this positive-definite Fourier-zero stability problem. Pati and collaborators' exact quantum speed limits concern modified dynamical generator variances and do not state the present measure-level sharp quadratic remainder. The published statements and available full texts were compared by their quantified objects and implications, not solely their titles.

## Limitations

This theorem assumes an **exact Fourier zero**; it does not bound measures whose Fourier transform is merely small, nor does it locate or guarantee a Fourier zero. It gives no lower bound on the first zero beyond the established sharp Mandelstam–Tamm constant. The sharpness family is discrete, although the theorem applies to arbitrary Borel laws. The identified publications do not establish exhaustive historical priority: older characteristic-function and quantum-speed-limit papers may contain equivalent scalar refinements not indexed under these terms. Independent review has not been carried out.

## References

1. T. Ismoilov, *Sharp sign uncertainty for trigonometric polynomials*, arXiv:2606.02299, first publicly posted June 1, 2026. https://arxiv.org/abs/2606.02299
2. S. Luo and Z. Zhang, *Estimating the first zero of a characteristic function*, C. R. Acad. Sci. Paris, Ser. I 338 (2004), 203–206, doi:10.1016/j.crma.2003.11.028. https://www.numdam.org/item/10.1016/j.crma.2003.11.028.pdf
3. Y. C. Huang, *Estimating the first zero of the characteristic function: a new approach based on the central moments* (2025), doi:10.13140/RG.2.2.18421.08165. https://www.researchgate.net/publication/390470415_Estimating_the_first_zero_of_the_characteristic_function_a_new_approach_based_on_the_central_moments
4. A. K. Pati, B. Mohan, Sahil, and S. L. Braunstein, *Exact quantum speed limits*, Phys. Rev. A 112 (2025), 062209; first preprint arXiv:2305.03839. https://arxiv.org/abs/2305.03839
5. L. Mandelstam and I. Tamm, *The uncertainty relation between energy and time in non-relativistic quantum mechanics*, J. Phys. (Moscow) 9 (1945), 249.
