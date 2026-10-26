# A reciprocal balance law for the generalized roundness of one-spoke weighted stars

## Finding

For an integer \(m\ge 2\) and a parameter \(t>0\), let \(T_{m,t}\) be the metric space comprising the center and all \(m+1\) leaves of a star: \(m\) arms have length \(1\), and the remaining arm has length \(t\). Distances are shortest-path lengths. For \(p\ge0\), say that \(T_{m,t}\) has \(p\)-negative type when
\[
\sum_{u,v\in T_{m,t}}a_ua_v d(u,v)^p\le0
\qquad\text{whenever }\sum_u a_u=0,
\]
where at \(p=0\) the diagonal is interpreted as zero. Define \(\wp_m(t)\) to be the supremum of admissible exponents.

Put
\[
p_0=\log_2\!\left(\frac{2m}{m-1}\right),\qquad
p_\mathrm{bal}=\log_2\!\left(\frac{2(m+1)}m\right),\qquad
H_p(t)=\frac{(1+t)^p-t^p-1}{t^{p/2}}.
\]
Then \(\wp_m(t)\) is the **unique** solution \(p\in(1,p_0)\) of
\[
H_p(t)^2=2\left(2-\frac{m-1}{m}2^p\right).
\tag{1}
\]
The space has \(p\)-negative type precisely for \(0\le p\le\wp_m(t)\), and strict \(p\)-negative type precisely for \(0\le p<\wp_m(t)\). The threshold satisfies
\[
\wp_m(t)=\wp_m(1/t),\qquad
p_\mathrm{bal}\le\wp_m(t)<p_0,
\]
with equality in the first lower bound **only at** \(t=1\). Moreover,
\[
\lim_{t\downarrow0}\wp_m(t)=\lim_{t\to\infty}\wp_m(t)=p_0.
\]
Thus among stars with one exceptional arm the equilateral star uniquely has the **smallest** allowable exponent, while reciprocal arm ratios have the same exponent despite generally being nonisometric.

Two sharp boundary rates refine this statement. If \(m\ge3\), then, as \(t\downarrow0\),
\[
p_0-\wp_m(t)\sim\frac{p_0^2}{4\log 2}\,t^{2-p_0}.
\tag{2}
\]
For \(m=2\), let \(L=\log(1/t)\) and let \(W\) be the positive Lambert function, \(W(z)e^{W(z)}=z\). Then
\[
2-\wp_2(t)\sim\frac{W(L/\log 2)}{L}.
\tag{3}
\]
The corresponding large-\(t\) rates follow by \(t\mapsto1/t\). At the critical exponent \(p=\wp_m(t)\), the squared-distance matrix of the Hilbert snowflake \(d^{p/2}\) has exactly one nontrivial affine dependence; below it the \(m+2\) embedded points are affinely independent.

## Assumptions and scope

The objects are the \(m+2\) **vertices** of a positive-length metric star, including its center; the continuous interior of an arm is not part of the metric space. All distances use the shortest-path metric. The criterion is the standard real conditionally negative semidefinite quadratic form, not a positivity claim for arbitrary coefficient vectors. The exponent is real and nonnegative, and \(m\ge2\) is an integer. Natural logarithms are used unless the base is displayed.

## Proof

**1. Exact reduction of conditional negative type.** Denote the ordinary leaves by \(u_1,\ldots,u_m\), the exceptional leaf by \(v\), and the center by \(o\). Let the coefficients on \(u_i\) be \(a_i\), let that on \(v\) be \(b\), and put \(s=\sum_i a_i\). The zero-sum condition forces the coefficient at \(o\) to equal \(-s-b\). Set \(h=(1+t)^p-t^p-1\). Direct expansion using ordinary-leaf pair distances \(2\), exceptional-to-ordinary distances \(1+t\), and center-to-leaf distances \(1,t\), gives
\[
Q_p=\bigl(2^p-2\bigr)s^2-2^p\sum_i a_i^2+2hbs-2t^pb^2.
\]
Write \(a_i=s/m+\xi_i\) with \(\sum_i\xi_i=0\). This becomes
\[
Q_p=-2^p\sum_i\xi_i^2-
\left(2-\frac{m-1}{m}2^p\right)s^2+2hbs-2t^pb^2.
\tag{4}
\]
Completing the square in \(b\), the \((s,b)\) block is nonpositive if and only if
\[
2\left(2-\frac{m-1}{m}2^p\right)\ge\frac{h^2}{t^p}=H_p(t)^2.
\tag{5}
\]
The right side is nonnegative, so this condition also enforces nonpositivity of the \(s^2\) coefficient. Formula (4) is an exact decomposition of the full \(m+1\)-dimensional zero-sum coefficient space. No unexamined coefficient directions remain.

**2. Unique threshold.** On \(1\le p\le p_0\), the left side of (5) decreases strictly from \(4/m\) to zero. For fixed \(t>0\), the quantity \(H_p(t)\) increases strictly with \(p\ge1\). Indeed, with \(a=\sqrt t\), \(b=1/\sqrt t\) and \(c=a+b\), we have
\[
H_p(t)=c^p-a^p-b^p.
\]
After interchanging \(a,b\), assume \(a\ge1\ge b\). Then \(c>a\), so \(c^p\log c>a^p\log a\), while \(-b^p\log b\ge0\). Thus \(\partial_pH_p(t)>0\). At \(p=1\), \(H_1(t)=0\). At \(p=p_0>1\), \(H_{p_0}(t)>0\) by strict convexity of the power function. The intermediate value theorem and strict monotonicity give exactly one root in \((1,p_0)\). Formula (5) gives strict negative type below the root on \([1,p_0)\) and failure above it. At \(p>p_0\), the \(s^2\) coefficient in (4) is positive, so negative type fails by choosing \(b=0\), \(\xi_i=0\). At lower exponents, the known negative-type interval property gives admissibility. Strictness for \(0\le p<1\) follows from the strict lower-exponent theorem of Li and Weston [2], applied to the already established admissible exponent \(p=1\). The direct strictness conclusion for \(1\le p<\wp_m(t)\) follows from the strict negativity of both blocks in (4). The equality case of (5) is the claimed singular critical exponent.

**3. Reciprocal symmetry and the unique balance minimum.** Algebraically,
\[
H_p(1/t)=H_p(t).
\]
For \(1<p<2\), differentiate in \(t\):
\[
\operatorname{sgn}(\partial_tH_p(t))
=\operatorname{sgn}\bigl(1-t^p+(t-1)(1+t)^{p-1}\bigr).
\]
When \(0<t<1\), consider \(f(q)=t^q+(1-t)(1+t)^{q-1}\). It is strictly convex as a function of \(q\) and satisfies \(f(1)=f(2)=1\). Therefore \(f(p)<1\), and \(H_p(t)\) is strictly increasing on \((0,1)\). Reciprocal symmetry makes it strictly decreasing on \((1,\infty)\). Hence
\[
H_p(t)\le H_p(1)=2^p-2,
\]
with equality only when \(t=1\). Substituting \(t=1\) into (1) gives \(2^p=2(m+1)/m\). Thus the balanced threshold is \(p_\mathrm{bal}\), and the strict inequality in \(H_p\) yields \(\wp_m(t)>p_\mathrm{bal}\) for \(t\ne1\). All relevant roots are below \(2\), including when \(m=2\).

**4. End behavior.** For any fixed \(p\in(1,p_0)\), the expansion \((1+t)^p-1-t^p=pt+o(t)\) yields \(H_p(t)\sim p\,t^{1-p/2}\to0\), since \(p<p_0\le2\). It follows from (5) that \(\wp_m(t)\to p_0\) as \(t\downarrow0\), and reciprocal symmetry handles \(t\to\infty\).

For \(m\ge3\), write \(\varepsilon=p_0-\wp_m(t)\), so \(p_0<2\). Equation (1) becomes \(4(1-2^{-\varepsilon})=H_{p_0-\varepsilon}(t)^2\). Uniform expansion near \(p_0\) gives
\[
4\log2\,\varepsilon(1+o(1))
=(p_0-\varepsilon)^2t^{2-p_0+\varepsilon}(1+o(1)).
\]
The equation first implies \(\varepsilon=O(t^{2-p_0})\), hence \(\varepsilon\log t\to0\). Replacing \(t^\varepsilon\) by \(1+o(1)\) proves (2).

For \(m=2\), \(p_0=2\) and \(\varepsilon=2-\wp_2(t)\to0\). The same equation is now \(4\log2\,\varepsilon(1+o(1))=(2-\varepsilon)^2t^\varepsilon(1+o(1))\). With \(L=\log(1/t)\), this gives \((\varepsilon L)e^{\varepsilon L}=(L/\log2)(1+o(1))\). Since \(W\) is increasing and slowly varying at infinity, inversion proves (3).

**5. Attaining coefficient vector and Hilbert rank.** At \(p=\wp_m(t)\), choose ordinary coefficients \(a_i=1/m\), exceptional coefficient \(b=h/(2t^p)\), and center coefficient \(-1-b\). Formula (4) gives exactly \(Q_p=0\). All zero-sum null vectors are scalar multiples of this vector: the \(\xi\)-block is strictly negative and the two-dimensional block in (4) has precisely one zero eigenvalue. The standard Schoenberg correspondence between negative-type kernels and squared Hilbert distances therefore yields exactly one affine dependence at the critical exponent and no such dependence for smaller exponents.

## Verification

The accompanying `verify.py` computes the unique root of (1), independently forms the full powered distance matrix on the \(m+2\) vertices and tests its restriction to the zero-sum subspace. It also tests the reciprocal symmetry, the balanced minimum, the scalar inequality \(H_p(t)\le H_p(1)\), and the distinct small-arm asymptotic regimes with arbitrary-precision arithmetic. The executed checker passed 7,547 finite checks. These are diagnostics, not a proof for all real parameters; Steps 1–5 above provide the general proof.

Run with `python verify.py` in an environment containing NumPy, SciPy and mpmath.

## Relationship to prior work

Doust and Weston, *Enhanced negative type for finite metric trees* (2007 public preprint), establish quantitative negative-type gaps and the exact exponent for ordinary equal-arm stars (their Example 1 and Theorem 38). The balanced value above agrees with that result, which is prior work, not new. Li and Weston (2009 public preprint) establish the strict-negative-type interval property, used here as contextual background. Sánchez (2011 public preprint) supplies a general distance-matrix criterion for computing the negative-type threshold of arbitrary finite metrics; it applies to these stars, but does not itself give their one-exceptional-arm reciprocal balance law, strict minimum, critical null vector, or two distinct asymptotic rates. Levy-Moore, Nichols and Weston (2016) treat generalized-roundness comparisons for weighted infinite trees, not the finite one-defect exact threshold. The contribution claimed here is the joint **weighted one-arm law, extremal balance rigidity, and critical boundary-rate classification**, not the general distance-matrix method or the classical equal-arm formula.

## Limitations

The classification concerns finite vertex metrics of stars with exactly one exceptional arm and \(m\) equal arms. It does not classify arbitrary independently weighted arms, metric-graph interiors, infinite trees, or different non-tree metrics. Its exact exponent is defined as the unique root of a scalar nonlinear equation, not asserted to have an elementary closed form for general \(t\). The comparison against historical literature cannot rule out an unindexed equivalent weighted-star calculation; independently checking the older metric-embedding literature remains appropriate.

## References

1. I. Doust and A. Weston, *Enhanced negative type for finite metric trees*, first posted 2007-05-03, arXiv:0705.0411, https://arxiv.org/abs/0705.0411.
2. H. Li and A. Weston, *Strict p-negative type of a metric space*, first posted 2009-01-06, arXiv:0901.0695, https://arxiv.org/abs/0901.0695.
3. S. Sánchez, *On the supremal p-negative type of a finite metric space*, first posted 2011-08-02, arXiv:1108.0451, https://arxiv.org/abs/1108.0451.
4. L. Levy-Moore, M. Nichols and A. Weston, *Comparing the generalized roundness of metric spaces*, first posted 2016-08-12, arXiv:1608.03699, https://arxiv.org/abs/1608.03699.
