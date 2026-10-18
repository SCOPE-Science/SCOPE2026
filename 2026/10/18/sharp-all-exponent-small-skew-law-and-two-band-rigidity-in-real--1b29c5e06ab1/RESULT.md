# Sharp all-exponent small-skew law and two-band rigidity in real \(L_p\) spaces

## Finding
For each real \(L_p(\Omega,\mu)\) with \(1<p<\infty\) containing two disjoint norm-one functions and for \(\tau\ge0\), write
\[
\mathcal S_{p,t}(\tau)=\inf_{\|x\|_p=\|y\|_p=1}M_t(\|x+\tau y\|_p,\|\tau x-y\|_p),\qquad 1\le t\le\infty,
\]
where \(M_t(a,b)=((a^t+b^t)/2)^{1/t}\) and \(M_\infty(a,b)=\max\{a,b\}\). For \(p\ne2\), define the unique \(s_p>0\) by
\[
\cosh((p-1)s_p)=(p-1)\cosh s_p,
\qquad
c_p=\frac{|\sinh((p-2)s_p/2)|}{\cosh(p s_p/2)}.
\]
Then, with \(r=\min\{2,p\}\),
\[
\boxed{\mathcal S_{p,t}(\tau)=1-c_p\tau+O_p(\tau^r)}
\]
as \(\tau\downarrow0\), with the remainder **uniform simultaneously over every outer mean \(1\le t\le\infty\)**. For \(p=2\), the same formula holds with \(c_2=0\). The coefficient is attained asymptotically by a single explicit pair, independent of \(t\).

Writing \(J_p(x)=\operatorname{sgn}(x)|x|^{p-1}\), the normalized first-order skew functional
\[
D_p(x,y)=\int_\Omega(J_p(x)y-J_p(y)x)\,d\mu
\]
satisfies the sharp bound \(|D_p(x,y)|\le2c_p\). Its negative extremizers, and only those extremizers, are the two-band pairs specified below. The deficit admits the **exact pointwise-nonnegative decomposition**
\[
E_p(x,y)=2c_p+D_p(x,y)
=\int_\Omega \big[c_p(|x|^p+|y|^p)+J_p(x)y-J_p(y)x\big]d\mu\ge0.
\]
For a pair within \(\varepsilon\tau\) of the infimum at any \(t\), this deficit is at most \(2\varepsilon+O_p(\tau^{r-1})\), uniformly in \(t\).

The near-Hilbert cusp and two exact samples are
\[
\lim_{p\to2}\frac{c_p}{|p-2|}=\frac{z_*}{2\cosh z_*},\quad z_*\tanh z_*=1,\qquad
c_4=\frac1{2\sqrt2},\quad c_6=\frac12.
\]

## Assumptions and scope
The scalar field is real. The measure space admits two disjoint nonzero \(L_p\) functions (in particular, every real \(\ell_p^n\) with \(n\ge2\) qualifies). All norms are genuine \(L_p\) norms. The asymptotic is at \(\tau\downarrow0\), not a finite-\(\tau\) formula, and the coefficient is zero at the Hilbert exponent. The outer parameter ranges over the full closed interval including its maximum endpoint.

## Proof
**1. Scalar sharp coefficient and unique ratio.** Set \(r_p=e^{-s_p}\in(0,1)\). At a nonzero scalar pair \((a,b)\), the absolute value of the skew expression
\[
J_p(a)b-J_p(b)a
\]
is at most \(c_p(|a|^p+|b|^p)\), where the **optimal** scalar constant is
\[
c_p=\max_{0<u<1}\frac{u|1-u^{p-2}|}{1+u^p}.
\]
This follows by dividing by \(|a|^p+|b|^p\) and using symmetry under \(u\mapsto1/u\); if either scalar is zero the left side vanishes. Differentiating the displayed quotient, every interior stationary point obeys
\[
1+u^{2p-2}=(p-1)(u^{p-2}+u^p).
\]
With \(u=e^{-s}\), this is precisely \(\cosh((p-1)s)=(p-1)\cosh s\). The ratio \(\cosh((p-1)s)/\cosh s\) is strictly increasing from one to infinity for \(p>2\), and strictly decreasing from one to zero for \(1<p<2\); hence there is exactly one positive critical point, which is the global maximum, since the quotient vanishes at both endpoints. Rearranging the scalar quotient gives the hyperbolic expression for \(c_p\).

**2. Integral inequality, sharpness, and rigid equality.** Integrate the scalar inequality for unit \(x,y\) to obtain \(|D_p(x,y)|\le2c_p\). Let \(\sigma=\operatorname{sgn}(p-2)\), \(u=r_p\), and choose any disjoint unit functions \(f,g\). Set
\[
a=(1+u^p)^{-1/p},\quad b=ua,\qquad x=af+bg,\quad y=-\sigma bf+\sigma ag.
\]
Both inputs are unit vectors. The pointwise skew contributions on the supports of \(f,g\) have the same negative sign and saturate the scalar bound, so \(D_p(x,y)=-2c_p\). Moreover the two output norms are *identical* for every \(\tau\), since their disjoint coefficient lists agree up to signs and permutation.

To classify equality, the pointwise integrand in \(E_p\) is nonnegative, so vanishing of its integral forces equality almost everywhere. At every nonzero point, scalar equality requires \(y/x=-\sigma u\) or \(y/x=\sigma/u\); on the complement both functions vanish. Since both inputs have norm one, if \(w\) is the \(|x|^p\)-mass of the first band, then \(w+(1-w)=1\) and \(u^p w+u^{-p}(1-w)=1\). Thus
\[
w=\frac1{1+u^p},\qquad 1-w=\frac{u^p}{1+u^p},
\]
which proves the exhaustive two-band classification, including on nonatomic spaces. Conversely every such pair has zero deficit.

**3. Uniform small-skew expansion.** Real \(L_p\) satisfies the uniform norm expansion
\[
\|x+\tau y\|_p=1+\tau\int J_p(x)y\,d\mu+O_p(\tau^r),
\quad r=\min\{2,p\},
\]
for all unit \(x,y\), with the analogous expansion around \(-y\). For \(p\le2\), the scalar map \(u\mapsto|u|^p\) has a globally Hölder \((p-1)\) derivative, giving integrated remainder \(O_p(\tau^p)\). For \(p\ge2\), its derivative is locally Lipschitz with remainder bounded by \(C_p\tau^2(|x|^{p-2}|y|^2+\tau^{p-2}|y|^p)\), integrable by Hölder. Passing to the \(p\)-th root is uniformly smooth near one.

Every power mean for \(t\ge1\) dominates the arithmetic mean, so uniformly in \(t\),
\[
M_t(\|x+\tau y\|_p,\|\tau x-y\|_p)
\ge1+\frac\tau2 D_p(x,y)-C_p\tau^r
\ge1-c_p\tau-C_p\tau^r.
\]
For the two-band pair above the output norms coincide and their common value equals \(1-c_p\tau+O_p(\tau^r)\), proving the matching upper bound **for every \(t\) at once**. If a competing pair is within \(\varepsilon\tau\) of the infimum, comparison of these bounds gives \(E_p=2c_p+D_p\le2\varepsilon+O_p(\tau^{r-1})\). The deficit is exactly an integral of pointwise scalar slack, so this gives a stability assertion for the unique two-ratio minimizing geometry.

**4. The Hilbert cusp.** Let \(p=2+\delta\). Divide the unique-critical-point equation by \(\delta\) and pass to \(\delta=0\). The limiting equation is \(s\tanh s=1\), with unique positive root \(z_*\) and strictly positive derivative of \(s\sinh s-\cosh s\) there. The implicit function theorem after removal of the factor \(\delta\) yields \(s_p\to z_*\), and expanding the hyperbolic expression gives \(c_p/|p-2|\to z_*/(2\cosh z_*)\). Elementary triple- and quintuple-angle identities give \(c_4=1/(2\sqrt2)\) and \(c_6=1/2\).

## Verification
The source paper's definitions and its matched-mean exact identity were checked against the October 2, 2026 first version. The mathematical proof does not require empirical extrapolation. The standalone `verify.py` evaluates the scalar stationary equation, two-band equality, and a finite collection of scalar inequalities at eleven exponents; all 2,222 diagnostics passed. Its finite checks are not offered as proofs of universal quantifiers. The integrability and uniform remainder estimates are established analytically above.

## Relationship to prior work
Xu and Liu establish the skew Schäffer definition, general bounds, the exact matched-exponent relation \(\mathcal S_{L_p,p}(\tau)=(1+\tau^2)/\|A_\tau\|_{\ell_p^2\to\ell_p^2}\), and the two-coordinate attainment construction. Those results are assumed and are **not** presented here as new. They allow recovery of the derivative at the matched exponent, but do not state the full exponent-uniform first-order formula, the unique hyperbolic ratio across all \(p\), the all-mean two-band equality structure, or its quantitative pointwise deficit. An earlier independent exact small-skew formula at \(p=4\) for finite outer means is also treated as known; the distinct contribution here is the all-\(p\), all-outer-mean structure. Results on \(C\)-approximate Birkhoff symmetry impose an orthogonality constraint and optimize a different normalized residual, so do not imply this unconstrained skew difference. A result on the supremal skew geometric-mean constant optimizes the opposite direction and likewise does not determine the present all-mean infimal rigidity statement.

## Limitations
The result is an exact first-order and stability theorem; it does not determine the full finite-\(\tau\) profile of every mean. The scalar equality classification is for real \(L_p\); complex phases are not included. Near-minimizers have small *integrated scalar slack*, not an asserted strong norm distance to any particular fixed pair. A comprehensive priority guarantee is impossible; equivalent first-variation results under semi-inner-product asymmetry terminology could exist.

## References
1. Ying Xu and Qi Liu, *Skew Schäffer Type Constants*, arXiv:2610.03050v1, first posted October 2, 2026, especially Theorem 3.2 and Remark 3.3.
2. Q. Ni, Q. Liu and Y. Zhou, *Some aspects of new skew geometric constants in Banach spaces*, Mathematical Inequalities & Applications 28 (2025), 327–342, DOI 10.7153/mia-2025-28-22.
3. *Dimension-free C-approximate Birkhoff symmetry of real \(L_p\) spaces*, published October 11, 2026 (related constrained optimization, not an equality of invariants).
