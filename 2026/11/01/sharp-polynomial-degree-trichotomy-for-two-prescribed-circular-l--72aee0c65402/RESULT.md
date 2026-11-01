# Sharp polynomial-degree trichotomy for two prescribed circular limit cycles

## Finding

Fix two distinct positive radii \(0<r_1<r_2\), two positive minimal periods \(T_1,T_2\), and two prescribed positive transverse Floquet multipliers \(\mu_1,\mu_2\neq1\). Consider the class of rotation-equivariant real planar polynomial vector fields
\[
\dot x=xP(s)-yQ(s),\qquad\dot y=yP(s)+xQ(s),\qquad s=x^2+y^2.
\]
where \(P,Q\) are real polynomials and \(Q(s)>0\) for every \(s\ge0\). Require that the **only nonconstant periodic trajectories anywhere in the plane** be the two circles of radii \(r_1,r_2\), each with precisely its specified physical-time minimal period and multiplier. Let \(d_{\min}\) denote the smallest total Cartesian polynomial degree of such a field.

Put \(s_i=r_i^2\) and
\[
 c_i=\frac{|\log\mu_i|}{2s_iT_i(s_2-s_1)}>0\quad (i=1,2).
\]
If \(\log\mu_1\) and \(\log\mu_2\) have the same sign, there is **no realization at any finite degree**. If they have opposite signs, the full sharp classification is
\[
\boxed{
 d_{\min}=\begin{cases}
 5,&c_2=c_1,\\
 7,&c_1<c_2\le(s_2/s_1)c_1,\\
 9,&c_2<c_1\text{ or }c_2>(s_2/s_1)c_1.
 \end{cases}}
\]
In particular, exactly alternating stability types are possible without additional cycles, but **alternating stability does not determine the least polynomial degree**. The numerical sizes of the prescribed Floquet multipliers select among three sharp degrees.

## Assumptions and scope

All vector fields are autonomous polynomial vector fields on \(\mathbb R^2\), of the displayed rotation-equivariant form. The angular coefficient is strictly positive at every nonnegative squared radius, including the origin; thus angular motion is never arrested on a nonzero circle. The two target radii are distinct and strictly positive. Each desired physical-time period is finite and strictly positive. The desired multipliers lie in \((0,\infty)\setminus\{1\}\), so the target cycles must be hyperbolic. Total polynomial degree is the maximum of the degrees in \(x,y\) of the two vector-field components. No assertion is made about optimization among polynomial fields **without** rotational equivariance or global positive angular speed.

The hypothesis of **exactly** two nonconstant periodic orbits is essential. Additional equilibria (including at the origin) are not prohibited. The claimed Floquet multiplier is the nontrivial transverse multiplier; the tangential multiplier is always \(1\). Local dynamics near both circles exist and are smooth. Forward completeness of every unbounded trajectory is not required.

## Proof

**1. Exact radial and angular reduction.** For \(s=x^2+y^2\) and the polar angle \(\theta\), direct differentiation gives
\[
\dot s=2sP(s),\qquad \dot\theta=Q(s).
\]
A nonconstant periodic trajectory of a one-dimensional autonomous equation for \(s\) cannot exist, by uniqueness: every periodic solution \(s(t)\) is constant. Therefore every nonconstant periodic trajectory of the planar system must be a circle at a positive zero of \(P\); conversely, each such zero gives a circle traversed with positive angular speed. The origin is a fixed point. Thus precisely two periodic circles occur if and only if \(P\) has exactly the two simple positive roots \(s_1,s_2\), with no other positive roots. Simplicity follows from the requirement of nonunit transverse multipliers.

On \(s=s_i\), the minimal period is \(T_i=2\pi/Q(s_i)\). Linearizing the radial equation at its nonzero root yields the transverse characteristic exponent \(2s_iP'(s_i)\) per unit physical time, and hence
\[
\log\mu_i=2s_iT_iP'(s_i).
\]
This formula is exact (not a small-amplitude approximation) and has the same value in any smooth nonzero transverse radial coordinate.

**2. Factorization and the forced interpolation data.** Set
\[
R(s)=(s-s_1)(s-s_2),\qquad d=s_2-s_1>0.
\]
Any realizing polynomial factors as \(P(s)=R(s)B(s)\), and the two derivative conditions force
\[
B(s_1)=b_1:=-\frac{\log\mu_1}{2s_1T_1d},\qquad
B(s_2)=b_2:=\frac{\log\mu_2}{2s_2T_2d}.
\]
Therefore \(|b_i|=c_i\). If the logarithmic multipliers have the same sign, \(b_1,b_2\) have opposite signs. By continuity, every such \(B\) has a zero strictly between the two specified positive nodes. This would produce an additional nonconstant periodic circle because \(Q>0\), contradicting the requirement. This proves impossibility in that case.

For the remaining cases the numbers \(b_1,b_2\) have the same nonzero sign \(\sigma\). Define the linear cardinal polynomials
\[
\ell_1(s)=\frac{s_2-s}{d},\qquad
\ell_2(s)=\frac{s-s_1}{d},\qquad
\ell_1(s)+\ell_2(s)=1.
\]
The unique interpolating affine polynomial is
\[
 B_*(s)=b_1\ell_1(s)+b_2\ell_2(s),\qquad
 \sigma B_*(s)=c_1+\frac{c_2-c_1}{d}(s-s_1).
\]
If \(c_1=c_2\), it is a nonzero constant. If \(c_2>c_1\), it increases with \(s\) after multiplication by \(\sigma\); it has no positive zero precisely when \(c_2\le(s_2/s_1)c_1\). At equality its only zero occurs at \(s=0\), which is harmless because that point is not a nonconstant periodic orbit. If \(c_2>(s_2/s_1)c_1\), it has an unwanted root in \((0,s_1)\). If \(c_2<c_1\), the affine interpolant decreases and has an unwanted root in \((s_2,\infty)\). This is the exhaustive affine sign classification.

**3. Exact realizations at the asserted degrees.** Put \(\omega_i=2\pi/T_i>0\) and choose the globally positive angular polynomial
\[
 Q_*(s)=\omega_1\ell_1(s)^2+\omega_2\ell_2(s)^2.
\]
Both coefficients are positive and \(\ell_1,\ell_2\) never vanish simultaneously, so \(Q_*(s)>0\) for every real \(s\). Moreover \(Q_*(s_i)=\omega_i\), giving the required periods.

When \(c_1=c_2\), take \(B(s)=b_1\) and \(P(s)=R(s)b_1\). Its positive zeros are precisely \(s_1,s_2\). Here \(\deg_s P=2\) and \(\deg_s Q_*=2\), so the Cartesian degree equals \(5\).

When \(c_1<c_2\le(s_2/s_1)c_1\), take \(B=B_*\) and \(P=RB_*\). The sign calculation proves that \(B_*\) has no strictly positive zero. It is genuinely affine, so \(\deg_sP=3\) and the Cartesian degree equals \(7\).

In all remaining opposite-stability cases take the positive-squares interpolant
\[
 B_\square(s)=b_1\ell_1(s)^2+b_2\ell_2(s)^2,\qquad
 P(s)=R(s)B_\square(s),\quad Q(s)=Q_*(s).
\]
Because \(b_1,b_2\) share a nonzero sign and \(\ell_1,\ell_2\) have no common zero, \(B_\square\) never vanishes on \(\mathbb R\) and has the prescribed node values. Its quadratic coefficient is \((b_1+b_2)/d^2\neq0\), so \(\deg_s P=4\), giving Cartesian degree \(9\). The derivative and period identities from Step 1 give precisely the two requested multipliers and periods in every construction, not merely their signs.

**4. Lower bounds and sharpness.** Any realizing \(P\) has two distinct simple roots and hence \(\deg_sP\ge2\); its planar Cartesian degree is therefore at least \(5\). A degree-at-most-\(5\) field forces \(\deg_sP\le2\), so \(B\) is constant, implying \(b_1=b_2\), equivalent to \(c_1=c_2\) in the feasible opposite-stability regime. A degree-at-most-\(7\) field forces \(\deg_sP\le3\), so \(B\) is affine and must equal \(B_*\). The unwanted positive root found in Step 2 makes all such realizations impossible in the remaining cases. Thus the degree-\(9\) construction is optimal there. All possible input parameters are exhausted, proving the classification.

**Concrete sharpness witness.** Choose \(s_1=1\), \(s_2=2\), \(T_1=T_2=1\), \(\log\mu_1=-1\), and \(\log\mu_2=6\). Then \(b_1=1/2\), \(b_2=3/2\), and the unique affine interpolant is \(B_*(s)=s-1/2\); any degree-at-most-\(7\) realization therefore creates an extra circle at \(s=1/2\). The sharp degree-\(9\) realization is
\[
\begin{aligned}
 P(s)&=(s-1)(s-2)\bigl(\tfrac12(2-s)^2+\tfrac32(s-1)^2\bigr),\\
 Q(s)&=2\pi\bigl((2-s)^2+(s-1)^2\bigr).
\end{aligned}
\]
It has exactly the two target circles, minimal period \(1\) at each, and transverse multipliers \(e^{-1}\) and \(e^6\), respectively. A degree-\(5\) example follows by choosing \(b_1=b_2\), and a degree-\(7\) example follows from \(s_1=1,s_2=2,b_1=1,b_2=3/2\), taking \(B=B_*\) in both cases.

## Verification

A standalone dependency-free checker `verify.py` performs exact rational polynomial interpolation and derivative tests for the explicit witness and representative feasible degree-\(5\), degree-\(7\), boundary, and degree-\(9\) cases. It checks the prescribed logarithmic Floquet multipliers, degrees, positivity at a finite rational grid, and the extra positive affine root in the degree-\(9\) witness. Run `python3 verify.py` from the same directory. The verifier's finite grid checks are illustrative; the sign proofs above establish positivity on the entire continuum and the degree bounds for all admissible real input parameters.

## Relationship to prior work

Jana and Sarkar, *Some remarks on polynomial vector fields in \(\mathbb R^2\)* (2026), Theorem 2.5, characterize polynomial fields with multiple concentric invariant circles and discuss their number for low degrees. They do not formulate the inverse requirement to prescribe **both** the physical periods and numerical transverse multipliers or determine the smallest degree satisfying those data with exactly two cycles and positive angular speed. Their structural circle factorization motivates the inverse question.

Margalef-Bentabol and Peralta-Salas, *Realization problems for limit cycles of planar polynomial vector fields* (2015), Theorems 1.2, 2.1 and 4.2, establish prescribed periods, multiplicities and stable/unstable classifications for far more general configurations. Their period-and-stability realization does not itself furnish arbitrary **numerical** Floquet multipliers, nor does it give this rotation-equivariant sharp \(5/7/9\) classification. The present result concerns a more restrictive family and stronger numerical data; it does not challenge their broader existence theorem. Giné, Llibre and Valls (2018), Theorem 1, show in a complete cubic classification that two concentric invariant circles of a cubic field cannot be limit cycles; this supports the degree-separation context but does not fix exact periods or transverse multipliers. Christopher (2001) provides explicit fields with prescribed algebraic cycle curves and degree-optimality for generic curves, but available bibliographic material does not establish this Floquet-and-period trichotomy.

## Limitations

Sharp minimality is proved **only inside** the rotation-equivariant polynomial subclass with globally positive angular speed and with exactly two periodic circles. Allowing angle dependence, additional periodic orbits, a vanishing angular speed, or other nonpolynomial terms could change the minimum degree or feasibility. The theorem is not an unrestricted Hilbert's sixteenth-problem degree lower bound. Strict hyperbolicity is essential: unit transverse multipliers are not classified. The two physical-time periods may differ arbitrarily. No global forward completeness is asserted outside the compact periodic orbits. The closest published work supports the motivation but does not establish an absolute historical priority claim; unindexed specialized inverse-design results remain a residual literature risk.

## References

1. S. Jana and S. Sarkar, *Some remarks on polynomial vector fields in \(\mathbb R^2\)*, arXiv:2610.33226v1 (first publicly posted 2026-10-23), especially Theorem 2.5 and Section 3. https://arxiv.org/abs/2610.33226.
2. J. Margalef-Bentabol and D. Peralta-Salas, *Realization problems for limit cycles of planar polynomial vector fields*, arXiv:1507.00698 (first publicly posted 2015-07-02), *Journal of Differential Equations* 260 (2016), 3844–3859; DOI:10.1016/j.jde.2015.10.044. https://arxiv.org/pdf/1507.00698.
3. J. Giné, J. Llibre, C. Valls, *The Cubic Polynomial Differential Systems with two Circles as Algebraic Limit Cycles*, *Advanced Nonlinear Studies* 18 (2018), 183–193, DOI:10.1515/ans-2017-6033, especially Theorem 1. https://ddd.uab.cat/pub/artpub/2018/199332/advnonstu_a2018v18n1p183preprint.pdf.
4. C. Christopher, *Polynomial Vector Fields with Prescribed Algebraic Limit Cycles*, *Geometriae Dedicata* 88 (2001), 255–258; DOI:10.1023/A:1013171019668. https://doi.org/10.1023/A:1013171019668.
