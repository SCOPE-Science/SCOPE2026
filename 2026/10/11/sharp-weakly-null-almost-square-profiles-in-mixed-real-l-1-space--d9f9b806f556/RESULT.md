# Sharp weakly-null almost-square profiles in mixed real \(L^1\) spaces

## Finding
Let \((\Omega,\Sigma,\mu)\) be a finite positive measure space whose nonatomic part has positive measure. For \(x\in S_{L^1(\mu)}\), write \(x=x_{\mathrm{at}}+x_{\mathrm{dif}}\), with disjoint atomic and diffuse supports, and set
\[
a=\|x_{\mathrm{at}}\|_1,\qquad b=\|x_{\mathrm{dif}}\|_1=1-a.
\]
For each real \(t\ge0\), define the two-sided weak-null squareness profile
\[
\Lambda_x(t)=\inf_{\substack{y_n\rightharpoonup0\\\|y_n\|_1\to t}}
\limsup_{n\to\infty}\max\{\|x+y_n\|_1,\|x-y_n\|_1\}.
\]
The infimum is over sequences in \(L^1(\mu)\). The exact profile is
\[
\boxed{\Lambda_x(t)=a+\max\{b,t\}=\max\{1,a+t\}\quad(t\ge0).}
\]
In fact, the infimum is attained by explicit weakly null sequences and both signs have the same limiting norm.

Consequently, the set of attainable asymptotically square perturbation norms is
\[
\mathcal A(x)=\bigl\{t\ge0:\exists y_n\rightharpoonup0,\ \|y_n\|_1\to t,\ \|x+y_n\|_1\to1,\ \|x-y_n\|_1\to1\bigr\}=[0,b].
\]
For every tolerance \(\varepsilon\ge0\), the sharp weak-null perturbation radius
\[
R_x(\varepsilon)=\sup\Bigl\{\limsup_n\|y_n\|_1:\ y_n\rightharpoonup0,\ \limsup_n\max\{\|x+y_n\|_1,\|x-y_n\|_1\}\le1+\varepsilon\Bigr\}
\]
satisfies \(R_x(\varepsilon)=b+\varepsilon\).

A point \(x\in S_{L^1(\mu)}\) is called a weakly almost-square point if \(1\in\mathcal A(x)\), the localized version of the standard WASQ condition. The locus of these points is exactly
\[
\mathcal W=\{x\in S_{L^1(\mu)}:x_{\mathrm{at}}=0\},\qquad
\operatorname{dist}(x,\mathcal W)=2a.
\]

## Assumptions and scope
All spaces and functions are real. A finite positive measure means \(0<\mu(\Omega)<\infty\), with no separability assumption. The union of the positive-measure atoms is understood up to null sets; it consists of at most countably many atoms. Its complement is nonatomic, and is assumed to have positive measure. The atomic and nonatomic coordinate projections are contractive, and the atomic subspace is isometric to a (possibly finite-dimensional) \(\ell_1\) space. The result is valid for arbitrary positive atomic weights and arbitrary nonatomic finite measure spaces. No statement about vector-valued \(L^1\) spaces is asserted.

If the measure is purely atomic, every weakly null sequence in \(L^1(\mu)\) is norm null by the Schur property; in that boundary case \(\mathcal A(x)=\{0\}\), the weakly almost-square locus is empty, and the displayed profile \(\Lambda_x(t)\) is not defined through a nonempty class when \(t>0\). The nonzero nonatomic hypothesis is therefore essential for the full formula.

## Proof
**1. An exact pointwise identity.** For all real scalars \(u,v\),
\[
\tfrac12\bigl(|u+v|+|u-v|\bigr)=\max\{|u|,|v|\}.
\]
Integration yields, for every \(y\in L^1(\mu)\),
\[
\frac{\|x+y\|_1+\|x-y\|_1}{2}
=\int_\Omega\max\{|x|,|y|\}\,d\mu.
\tag{1}
\]

**2. The upper bound on attainable squareness.** Let \((y_n)\) be weakly null with \(\|y_n\|_1\to t\). The projection onto the atomic \(\ell_1\) summand is weak-to-weak continuous, and Schur's theorem therefore gives \(\|(y_n)_{\mathrm{at}}\|_1\to0\). Hence \(\|(y_n)_{\mathrm{dif}}\|_1\to t\). Since the integral of a pointwise maximum dominates either component,
\[
\int\max\{|x|,|y_n|\}\,d\mu
\ge a+\max\bigl\{b,\|(y_n)_{\mathrm{dif}}\|_1\bigr\}.
\]
By (1), the maximum of the two norms is at least their average. Taking the lower limit gives
\[
\liminf_n\max\{\|x+y_n\|_1,\|x-y_n\|_1\}\ge a+\max\{b,t\}.
\tag{2}
\]
This applies to every admissible sequence, including any subsequence selected from a bounded tolerance family.

**3. Weakly-null oscillations on the diffuse part.** Every finite nonatomic measure space admits sign functions \(r_n\), supported on its diffuse part, with \(|r_n|=1\) almost everywhere there, and \(f r_n\rightharpoonup0\) in \(L^1\) for every \(f\in L^1\) on that part. For completeness, bisect measurable sets recursively to obtain independent fair signs \(r_n\). They are orthonormal in \(L^2\); for \(h\in L^1\), approximation by \(L^2\) functions and Bessel's inequality imply \(\int h r_n\,d\mu\to0\). For any bounded test function \(g\), use \(h=fg\) to obtain the asserted weak convergence. The construction also works for nonseparable measure algebras.

Suppose \(b>0\) and fix \(t\ge0\). Set \(c=t/b\) and \(y_n=c x_{\mathrm{dif}}r_n\), extended by zero to the atoms. Then \(y_n\rightharpoonup0\) and \(\|y_n\|_1=t\). The scalar sign identity
\[
|1\pm cr_n|=\max\{1,c\}\pm\min\{1,c\}r_n
\]
gives
\[
\|x\pm y_n\|_1=a+b\max\{1,c\}\pm b\min\{1,c\}\int r_n\,\frac{|x_{\mathrm{dif}}|}{b}\,d\mu.
\]
The final integral tends to zero. Thus both norms tend to \(a+\max\{b,t\}\), proving equality in (2).

If \(b=0\), the diffuse component still has positive measure by hypothesis. Choose \(h\in L^1\) on that component with \(\|h\|_1=1\), and put \(y_n=t h r_n\). This is weakly null, has norm \(t\), and has support disjoint from \(x\), so \(\|x\pm y_n\|_1=1+t\) for every \(n\). This again meets (2). These constructions include \(t=0\).

**4. Exact spectrum, tolerance, and distance.** The lower bound (2) forces \(t\le b\) whenever both signed norms tend to one. Conversely, the constructions in Step 3 give both limits equal to one for every \(0\le t\le b\). Thus \(\mathcal A(x)=[0,b]\).

If a weakly null sequence satisfies the tolerance defining \(R_x(\varepsilon)\), the argument in Step 2, without assuming convergence of \(\|y_n\|_1\), forces \(\limsup_n\|y_n\|_1\le b+\varepsilon\). The witness from Step 3 with \(t=b+\varepsilon\) attains equality. Thus \(R_x(\varepsilon)=b+\varepsilon\).

The condition \(1\in\mathcal A(x)\) is equivalent to \(b=1\), or \(x_{\mathrm{at}}=0\). For any \(z\in\mathcal W\), the disjoint decomposition and reverse triangle inequality give \(\|x-z\|_1=a+\|x_{\mathrm{dif}}-z\|_1\ge a+|1-b|=2a\). If \(b>0\), equality holds at \(z=x_{\mathrm{dif}}/b\); if \(b=0\), it holds at every diffuse unit vector \(z\). This completes the distance formula.

## Verification
The argument is analytic and applies to every finite measure space with a nonzero nonatomic part. Its nonstandard existence ingredient is the sign-sequence lemma, independently reconstructed from dyadic bisections and Bessel's inequality and appearing as Lemma 2.1 of Rodríguez--Rueda Zoca (arXiv:2301.07943). The atomic obstruction uses the standard Schur property of \(\ell_1\). An accompanying exact-rational algebraic checker tests the pointwise maximum identity, the two-sign equality construction, and the distance formula on rational samples; those finite checks are illustrations, not a substitute for the measure-theoretic argument.

## Relationship to prior work
Abrahamsen--Langemets--Lima introduce WASQ for whole spaces and establish examples including nonatomic \(L^1\); Rodríguez--Rueda Zoca extend nonatomic examples and explicitly prove weak nullity of Rademacher-type products. Hardtke and the earlier work treat inheritance of whole-space WASQ under direct sums, while Ciaci studies positive LASQ and a WASQ criterion for lattices. The present formula identifies the exact *pointwise* weak-null norm profile for mixed atomic/non-atomic \(L^1\), including its sharp tolerance and metric stability. The pure nonatomic endpoint \(a=0\) is consistent with the existing WASQ theorem. The novelty claim concerns the full mixed-space quantitative profile, not the established nonatomic WASQ fact or whole-space inheritance.

## Limitations
The result is restricted to real scalar \(L^1\) of finite measure with nonzero diffuse part. The Schur argument does not automatically extend to vector-valued atomic fibers, and the sign identity is special to real scalars. The asymptotic weak-null condition cannot be replaced by arbitrary norm-one perturbations without changing the statement. No independent external audit is asserted. Equivalent results under terminology not captured by the searched literature remain possible.

## References
1. J. Rodríguez and A. Rueda Zoca, *On weakly almost square Banach spaces*, arXiv:2301.07943v1 (public 19 January 2023), especially Lemma 2.1, Theorem 1.1 and Corollary 2.5.
2. T. A. Abrahamsen, J. Langemets and V. Lima, *Almost square Banach spaces*, arXiv:1402.0818 (public 4 February 2014), especially Sections 3 and 5.
3. J.-D. Hardtke, *Summands in locally almost square and locally octahedral spaces*, arXiv:1705.06610 (public 18 May 2017), especially Proposition 2.3.
4. S. Ciaci, *Locally almost square Banach lattices*, arXiv:2210.13306 (public 24 October 2022), especially Section 2.
