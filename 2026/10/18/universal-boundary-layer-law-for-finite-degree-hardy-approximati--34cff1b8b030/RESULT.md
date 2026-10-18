# Universal boundary-layer law for finite-degree Hardy approximation to a migrating Blaschke zero

## Finding

Fix a real exponent \(p>2\) and an integer \(n\ge0\). For \(0<a<1\), put \(B_a(z)=(z-a)/(1-az)\) and let \(q_{n,p,a}\) be the unique complex polynomial of degree at most \(n\) minimizing \(E_{n,p}(a)=\|1-B_aq\|_{H^p}^p\), with normalized circle measure. Write \(\varepsilon=1-a\), \(\delta=\varepsilon^{1/(p-1)}\), and
\[
C_0(p)=\frac{2^{p-1}\Gamma((p-1)/2)}{\sqrt\pi\,\Gamma(p/2)},\qquad
C_p=\|1+z\|_{H^p}^p=\frac{2^p\Gamma((p+1)/2)}{\sqrt\pi\,\Gamma((p+2)/2)}.
\]
For each \(n\), let \(P_{n,p}\) be the unique degree-at-most-\(n\) minimizer of
\[
\mathcal F_{n,p}(P)=\|P\|_{H^p}^p-\frac{pC_0(p)}2\operatorname{Re}P(1).
\]
Then coefficientwise and in \(H^p\),
\[
q_{n,p,a}=-1+\delta P_{n,p}+o(\delta),
\quad E_{n,p}(a)=\|1+B_a\|_{H^p}^p+\delta^p\min_P\mathcal F_{n,p}(P)+o(\delta^p),
\]
and \(E_{n,p}(a)/\varepsilon\to C_0(p)\). In contrast, the unrestricted analytic-multiplier optimum has \(H^p\)-error to the power \(p\) exactly \(1-a^2\); therefore
\[
\frac{E_{n,p}(a)}{1-a^2}\longrightarrow \frac{C_0(p)}2>1
\]
for every fixed \(n\), exhibiting a strict finite-degree efficiency gap.

At \(n=1\), the scaled minimizer is explicitly \(P_{1,p}(z)=c_p(1+z)\), where \(c_p=[p/(2(p-1))]^{1/(p-1)}\), and
\[
q_{1,p,a}(z)=-1+c_p\varepsilon^{1/(p-1)}(1+z)+o(\varepsilon^{1/(p-1)}),
\]
\[
E_{1,p}(a)=\|1+B_a\|_{H^p}^p-(p-1)C_pc_p^p\varepsilon^{p/(p-1)}+o(\varepsilon^{p/(p-1)}).
\]
For every even exponent \(p=2m\ge4\), the baseline is \(C_0(p)\varepsilon+O(\varepsilon^2)\), and in particular the full two-term sharp asymptotic at degree one is
\[
E_{1,2m}(a)=2\binom{2m-2}{m-1}\varepsilon-(2m-1)\binom{2m}{m}c_{2m}^{2m}\varepsilon^{2m/(2m-1)}+o(\varepsilon^{2m/(2m-1)}).
\]

## Assumptions and scope

Here \(H^p\) is the analytic Hardy space on the unit disk, equipped with the \(p\)-th power of its normalized boundary \(L^p\) norm. The exponent \(p\) and degree bound \(n\) are fixed before \(a\uparrow1\). All minimizations are over complex polynomials of degree at most \(n\); uniqueness follows from strict convexity of \(L^p\) and injectivity of multiplication by \(B_a\). The assertion does not prescribe simultaneous growth of \(n\) or a limit as \(p\downarrow2\). The remainder in the general \(p>2\) formula is relative to the **exact** baseline \(\|1+B_a\|_{H^p}^p\), not automatically relative to its leading linear approximation.

## Proof

**1. Concentrating residual.** Since \(B_a\) is inner, write \(R_a=1+B_a=\varepsilon(1+z)/(1-az)\), and \(q=-1+P\). Thus \(1-B_aq=R_a-B_aP\). With \(z=e^{i\theta}\) and \(\theta=\varepsilon t\), \(R_a(e^{i\varepsilon t})\to2/(1-it)\). The bound \( |R_a(e^{i\theta})|\le C\varepsilon/(\varepsilon+|\theta|)\) (for \( |\theta|\le\pi\)) and dominated convergence for \(p>1\) show
\[
\|R_a\|_{H^p}^p=C_0(p)\varepsilon+o(\varepsilon).
\]
More generally, \(\int|R_a|^s=O(\varepsilon)\) for \(s>1\), \(O(\varepsilon\log(1/\varepsilon))\) for \(s=1\), and \(O(\varepsilon^s)\) for \(0<s<1\). Because \( |B_a|=1\) on the circle, \(R_a\overline{B_a}=\overline{R_a}\). Also \(\operatorname{Re}R_a=|R_a|^2/2\), and the imaginary part of \(\int|R_a|^{p-2}R_a\) vanishes by conjugation symmetry. Hence **exactly**
\[
\int|R_a|^{p-2}\overline{R_a}\,dm=\tfrac12\|R_a\|_{H^p}^p.
\]
The measures with densities \( |R_a|^{p-1}\) have mass \(O(\varepsilon)\) and concentrate at \(z=1\). Consequently, uniformly on bounded subsets of any fixed polynomial space,
\[
J_a(P):=\int |R_a|^{p-2}R_a\overline{B_aP}\,dm
=\frac{C_0(p)}2\varepsilon\overline{P(1)}+o(\varepsilon).
\]
(The real part is all that is used in subsequent estimates.)

**2. Scaling and finite-degree variational convergence.** The standard uniform convexity inequality for \(p>2\) gives a constant \(b_p>0\) such that for complex numbers \(x,y\), \( |x-y|^p\ge |x|^p-p\operatorname{Re}(|x|^{p-2}x\overline y)+b_p|y|^p\). Thus, denoting by \(P_a=q_{n,p,a}+1\) the unique minimizer and comparing with \(P=0\), we obtain
\[
b_p\|P_a\|_{H^p}^p\le p|J_a(P_a)|\le C_{p,n}\varepsilon\|P_a\|_{H^p}.
\]
Therefore \(P_a=O(\delta)\) in any coefficient norm. For \(P=\delta T\), uniformly over bounded \(T\), the scalar Taylor inequality
\[
\left||x-y|^p-|x|^p+p\operatorname{Re}(|x|^{p-2}x\overline y)-|y|^p\right|
\le C_p\bigl(|x|^{p-2}|y|^2+|x||y|^{p-1}\bigr)
\]
with \(x=R_a\), \(y=\delta B_aT\), shows
\[
\|R_a-\delta B_aT\|_{H^p}^p
=\|R_a\|_{H^p}^p+\delta^p\|T\|_{H^p}^p-p\delta\operatorname{Re}J_a(T)+o(\delta^p).
\]
Indeed \(\delta^2\int|R_a|^{p-2}=o(\delta^p)\) in each of the ranges \(2<p<3\), \(p=3\), \(p>3\); also \(\delta^{p-1}\int|R_a|=o(\delta^p)\). As \(\delta\varepsilon=\delta^p\), the normalized objective converges uniformly on coefficient-bounded sets to \(\mathcal F_{n,p}\). Boundedness of minimizing coefficients and uniqueness of the strictly convex limit show \(P_a/\delta\to P_{n,p}\), and convergence of minimum values proves the two displayed asymptotics.

**3. Explicit linear polynomial.** In degree one, complex conjugation and coefficient reversal leave both \(\|u+vz\|_{H^p}\) and \(\operatorname{Re}(u+v)\) invariant. Strict uniqueness therefore forces the minimizer to have \(u=v\in\mathbb R\); nonzero optimality forces positivity. Write \(P=c(1+z)\). The objective becomes \(C_pc^p-pC_0(p)c\) and has unique positive critical point \(c^{p-1}=C_0(p)/C_p=p/[2(p-1)]\). Its minimum is \(-(p-1)C_pc_p^p\), proving the explicit degree-one formula.

**4. Analytic benchmark and gap.** If \(F=1-B_a h\) for analytic \(h\in H^p\), then \(F(a)=1\), so the Hardy point-evaluation inequality gives \(\|F\|_{H^p}^p\ge1-a^2\). Equality is attained by \(F_a(z)=((1-a^2)/(1-az))^{2/p}\); the quotient \(h=(1-F_a)/B_a\) is analytic because the numerator vanishes at \(z=a\), and lies in \(H^p\). The strict gap follows from \(C_0(2)=2\) and strict increase of \(C_0(p)\) for \(p>2\): differentiating its gamma quotient gives \( (\log C_0)'(p)=\log2-[\psi(p/2)-\psi((p-1)/2)]/2\), zero at \(p=2\) and positive thereafter because the positive digamma increment decreases with \(p\) (trigamma is strictly decreasing).

**5. Even-power refinement.** At \(p=2m\), using \(\overline{B_a}=B_a^{-1}\) on the circle and the mean-value property for powers of \(B_a\),
\[
\|1+B_a\|_{H^{2m}}^{2m}=
\sum_{j,k=0}^{m}\binom mj\binom mk(-a)^{|j-k|}.
\]
This polynomial vanishes at \(a=1\), has derivative \(-C_0(2m)\) there, and hence equals \(C_0(2m)\varepsilon+O(\varepsilon^2)\). The gamma factors simplify to \(C_0(2m)=2\binom{2m-2}{m-1}\), while \(C_{2m}=\binom{2m}{m}\). Since \(2m/(2m-1)<2\), the preceding degree-one correction dominates the quadratic remainder.

## Verification

The included `verify.py` evaluates the full **exact quartic** formula for the \(H^4\) degree-one objective, solves its stationary system at seven values of \(\varepsilon\) down to \(10^{-12}\) with 65-digit arithmetic, and checks both the predicted phase coefficient \(c_4=(2/3)^{1/3}\) and the improvement constant \(18c_4^4\). It separately checks the \(H^6\) polynomial baseline at three scales. All numerical comparisons pass; these finite checks are not used as infinite proofs. The analytic scaling and uniqueness arguments above prove the theorem for all real \(p>2\) and fixed degrees.

## Relationship to prior work

Centner, Cheng and Felder (2023, arXiv:2305.16068) study low-degree Hardy \(H^p\) optimal polynomial approximants and uniform root bounds for inner functions. Cheng and Felder (2023, arXiv:2310.16010) analyze existence, continuity, fixed-point equations, and approximation errors. Neither inspected text identifies the all-\(p>2\), fixed-degree singular moving-zero law or the degree-one Puiseux coefficient. Bénéteau and collaborators (arXiv:2511.08000, initially public 2025) determine the unrestricted invariant-subspace distance but do not give its comparison with finite-degree moving-zero errors. The present claim is the **boundary asymptotic and finite-versus-unrestricted gap**, not previously known existence, strict convexity, or root-location bounds.

## Limitations

The theorem assumes fixed degree and real \(p>2\), not joint degree/exponent limits, nor \(1<p<2\). The two-term expansion at general non-even \(p\) retains the exact baseline because intermediate powers of \(\varepsilon\) can occur. The literature comparison is best knowledge, not a proof of absolute novelty; older work using equivalent singular-perturbation language could contain a related result. Numerical evidence does not replace analytic verification. No quantitative remainder uniform in unbounded degree is claimed.

## References

1. R. Centner, R. Cheng, C. Felder, *Optimal Polynomial Approximants in \(H^p\)*, first public 2023-05-25, https://arxiv.org/abs/2305.16068.
2. R. Cheng, C. Felder, *More Properties of Optimal Polynomial Approximants in Hardy Spaces*, first public 2023-10-24, https://arxiv.org/abs/2310.16010.
3. C. Bénéteau et al., *Metric projections, zeros of optimal polynomial approximants, and some extremal problems in Hardy spaces*, first public 2025-11-11, https://arxiv.org/abs/2511.08000.
