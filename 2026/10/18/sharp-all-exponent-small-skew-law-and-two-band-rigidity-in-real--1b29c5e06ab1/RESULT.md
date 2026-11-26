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
satisfies the sharp bound \(|D_p(x,y)|\le2c_p\). For \(p\ne2\), equality at \(D_p=-2c_p\) holds exactly for the two-band pairs specified below. For \(p=2\), \(D_2=0\) for every pair and there is no such rigidity. The deficit admits the **exact pointwise-nonnegative decomposition**
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

The distinct claim is the general non-Hilbert equality and deficit profile beyond the already indexed quartic case, with a unique scalar optimizer at every non-Hilbert exponent. The coefficient as a scalar supremum and the transfer of the first-order law from the matched to other outer means are included as consequences of known numerical-radius and matched-mean formulas, not as independent discoveries.

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
This is the standard scalar constant \(M_p\) of the numerical-radius literature (see References 4–5). The inequality follows by dividing by \(|a|^p+|b|^p\) and using symmetry under \(u\mapsto1/u\); if either scalar is zero the left side vanishes. Differentiating the displayed quotient, every interior stationary point obeys
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
For \(p\ne2\) the two-band pair above has equal output norms with common value \(1-c_p\tau+O_p(\tau^r)\), proving the matching upper bound **for every \(t\) at once**. For \(p=2\), the lower bound uses \(D_2=0\) and two disjoint unit functions are an orthogonal input pair with outputs \(\sqrt{1+\tau^2}\), proving the corresponding upper bound. If a competing pair is within \(\varepsilon\tau\) of the infimum, comparison of these bounds gives \(E_p=2c_p+D_p\le2\varepsilon+O_p(\tau^{r-1})\). For \(p\ne2\) the deficit is exactly an integral of pointwise scalar slack for the unique two-ratio minimizing geometry.

**4. The Hilbert cusp.** Let \(p=2+\delta\). Divide the unique-critical-point equation by \(\delta\) and pass to \(\delta=0\). The limiting equation is \(s\tanh s=1\), with unique positive root \(z_*\) and strictly positive derivative of \(s\sinh s-\cosh s\) there. The implicit function theorem after removal of the factor \(\delta\) yields \(s_p\to z_*\), and expanding the hyperbolic expression gives \(c_p/|p-2|\to z_*/(2\cosh z_*)\). Elementary triple- and quintuple-angle identities give \(c_4=1/(2\sqrt2)\) and \(c_6=1/2\).

## Verification
The source paper's definitions and its matched-mean exact identity were checked against the October 2, 2026 first version. The mathematical proof does not require empirical extrapolation. The standalone `verify.py` evaluates the scalar stationary equation, two-band equality, and a finite collection of scalar inequalities at eleven exponents; all 2,222 diagnostics passed. Its finite checks are not offered as proofs of universal quantifiers. The integrability and uniform remainder estimates are established analytically above.

## Relationship to prior work
Martín, Merí and Popov use the same scalar supremum \(M_p\) and identify it as a real \(\ell_p^2\) operator numerical radius, citing Martín and Merí [4–5]. For the quarter-turn \((a,b)\mapsto(b,-a)\) the norming duality pairing is exactly the scalar skew numerator divided by \(|a|^p+|b|^p\). In particular, the variational value of the coefficient and its pointwise bound are already implicit in that formula.

Xu and Liu [1, Theorem 3.2 and Remark 3.3] establish the exact matched-exponent relation \(\mathcal S_{L_p,p}(\tau)=(1+\tau^2)/\|A_\tau\|_{\ell_p^2\to\ell_p^2}\) and attain it with equal outputs. The balanced pair and monotonicity in \(t\) imply equality of the infima for \(t\ge p\). For \(1\le t\le p\), the two input norms to the power mean are in \([1-\tau,1+\tau]\); expansion at their arithmetic mean bounds the difference between the two power means of orders \(t\) and \(p\) by \(O_p(\tau^2)\) uniformly. Thus the common first-order law transfers from the matched exponent. The proof here derives it directly from pointwise slack to make the relationship with the equality classification explicit.

The quartic specialization of the two-band class and deficit overlaps the exact square identities in [6–7]; [6] also gives a stronger, second-order expansion uniform over all outer means. No exclusive priority is claimed for the quartic case. The distinct scope here is the unique-ratio, signed-band classification and deficit estimate for general real \(L_p\), beyond that quartic special case. An orthogonality-constrained Birkhoff residual [3], or a supremal rather than infimal skew geometric-mean constant [2], does not optimize the same unconstrained two-function functional.

## Limitations
The result is an exact first-order and stability theorem; it does not determine the full finite-\(\tau\) profile of every mean. The scalar equality classification is for real \(L_p\); complex phases are not included. Near-minimizers have small *integrated scalar slack*, not an asserted strong norm distance to any particular fixed pair. A comprehensive priority guarantee is impossible; equivalent first-variation results under semi-inner-product asymmetry terminology could exist.

## References
1. Ying Xu and Qi Liu, *Skew Schäffer Type Constants*, arXiv:2610.03050v1, first posted October 2, 2026, especially Theorem 3.2 and Remark 3.3.
2. Q. Ni, Q. Liu and Y. Zhou, *Some aspects of new skew geometric constants in Banach spaces*, Mathematical Inequalities & Applications 28 (2025), 327–342, DOI 10.7153/mia-2025-28-22.
3. *Dimension-free C-approximate Birkhoff symmetry of real \(L_p\) spaces*, published October 11, 2026 (related constrained optimization, not an equality of invariants).
4. M. Martín, J. Merí and M. Popov, *On the numerical index of real \(L_p(\mu)\)-spaces*, arXiv:0903.2704, Theorem 1 and the paragraph after Corollary 4.
5. M. Martín and J. Merí, *A note on the numerical index of the \(L_p\) space of dimension two*, Linear and Multilinear Algebra 57 (2009), 201–204, Lemma 2 (as cited in [4]).
6. *Uniform quadratic small-skew law and extremizer rigidity in real \(L_4\) spaces*, https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-uniform-quadratic-small-skew-law-and-extremizer-rigidity-in-real--2846c5f281be/RESULT.md.
7. *Perfect-square first-variation rigidity for skew Schäffer means*, https://github.com/Resultary/2026/blob/main/2026/10/18/SCOPE-perfect-square-first-variation-rigidity-for-skew-sch-ffer-means--0608f06c0ab6/RESULT.md.
