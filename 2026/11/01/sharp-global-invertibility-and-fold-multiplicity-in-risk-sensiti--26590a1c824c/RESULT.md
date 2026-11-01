# Sharp global invertibility and fold multiplicity in risk-sensitive learning maps

## Finding

For the coupled risk-sensitive multiplicative-weights and adaptive-belief update of Metaxas and Sapsis [1], there is a sharp, explicit, all-parameter **global invertibility-to-fold boundary**. The boundary distinguishes an orientation-preserving smooth diffeomorphism from a noninvertible map with targets having exactly three preimages. At equality, the map stays injective but its inverse develops a cubic-root singularity. The three-preimage behavior can occur with *all three inputs and their common output inside the invariant probability rectangle*, as an exact example below demonstrates.

Write the population and belief map as
\[
F(x,q)=\left(\frac{x}{x+(1-x)e^{a(x-b+cq)}},\ (1-k)q+k(p_0+p_1x)\right).
\]
For \(0<k<1\), put
\[
k_c=\frac{1}{1+cp_1},\qquad
\beta=\frac{1-k(1+cp_1)}{1-k},\qquad
\Lambda=a\beta.
\]
For \(0<k<1\), the complete global classification on the open strip \(\mathcal S=(0,1)\times\mathbb R\) is:

- If \(k\ge k_c\), or if \(0<k<k_c\) and \(a<4/\beta\), the map is an orientation-preserving \(C^\infty\) diffeomorphism from \(\mathcal S\) onto itself.
- If \(0<k<k_c\) and \(a=4/\beta\), it is a bijective homeomorphism, smooth in the forward direction, but is not a local \(C^1\) diffeomorphism on \(x=1/2\). Its inverse has a cubic-root singularity there.
- If \(0<k<k_c\) and \(a>4/\beta\), it has two disjoint critical lines and a nonempty open set of output points with exactly **three distinct preimages**. The complete inverse-fiber counts are one, two, or three, with explicit boundaries given below.

For \(k=1\), \(F\) is instead a \(C^\infty\) diffeomorphism from \(\mathcal S\) onto \((0,1)\times(p_0,p_0+p_1)\), and has no critical points.

**Exact physical three-preimage witness.** At
\[
(p_0,p_1,c,b,k,a)=\left(0,\frac1{1000},500,\frac12,\frac25,6\log3\right),
\]
three distinct states in the invariant probability rectangle have one image:
\[
F\left(\frac14,\frac1{1500}\right)
=F\left(\frac12,\frac1{2000}\right)
=F\left(\frac34,\frac1{3000}\right)
=\left(\frac1{1+3\sqrt3},\frac1{2000}\right).
\]
The Jacobian determinants at the respective three states have signs \(+,-,+\). Thus the fold is not an artifact of allowing the auxiliary belief coordinate to range over all real values.

## Assumptions and scope

All parameters are fixed with \(a>0\), \(c>0\), \(b\in(0,1)\), \(0<k\le1\), \(p_0\ge0\), \(p_1>0\), and \(p_0+p_1\le1\). The original learning model identifies \(c=M/(1-\alpha)\) for positive intensity \(M\) and confidence level \(0<\alpha<1\), and \(a\) is the positive population-scaled learning rate. The map is extended algebraically to \(\mathcal S\) to state an exact global inverse theorem. Its physical invariant rectangle is
\[
\mathcal R=(0,1)\times[p_0,p_0+p_1],
\]
which maps into itself. The inverse-fiber theorem pertains to \(\mathcal S\); the exact example separately demonstrates three-to-one behavior within \(\mathcal R\). No assertion is made that every parameter point beyond the strip threshold has three physical preimages.

For \(0<k<1\), define the log-odds function \(\ell(x)=\log(x/(1-x))\) for \(0<x<1\), and the scalar reduction
\[
H(x)=\ell(x)-\Lambda x,\qquad
L(s,Q)=\ell(s)-ab+\frac{ac}{1-k}(Q-kp_0).
\]
For \(\Lambda>4\), let
\[
d=\sqrt{1-\frac4\Lambda},\qquad x_-=\frac{1-d}{2},\quad x_+=\frac{1+d}{2}.
\]
Then for *every* target \((s,Q)\in\mathcal S\), the number of distinct preimages equals three if
\[
H(x_+)<L(s,Q)<H(x_-),
\]
two if \(L(s,Q)\) equals either endpoint, and one otherwise. The two fold lines are \(x=x_-\) and \(x=x_+\). Their separation in the sheared logit output coordinate is
\[
W(\Lambda)=H(x_-)-H(x_+)
=\Lambda d-4\operatorname{arctanh}d
=\frac13(\Lambda-4)^{3/2}+O\left((\Lambda-4)^{5/2}\right)
\]
as \(\Lambda\downarrow4\). This gives the precise opening exponent of the three-preimage region.

## Proof

**1. Exact inverse-fiber equation.** Since \(0<x<1\), the first image coordinate \(s=F_1(x,q)\) is in \((0,1)\) and obeys
\[
\ell(s)=\ell(x)-a(x-b+cq).
\]
For \(0<k<1\), prescribing the second image coordinate \(Q\) forces
\[
q=\frac{Q-kp_0-kp_1x}{1-k}.
\]
Substitution gives the exact equivalence \(F(x,q)=(s,Q)\iff H(x)=L(s,Q)\), where \(q\) is uniquely recovered by the preceding formula. Thus the inverse-fiber problem in two dimensions is *equivalent*, not merely approximated, by counting the roots of one scalar equation on \((0,1)\). At either endpoint \(H(x)\) tends to the corresponding infinite limit because the logarithmic divergence dominates the finite linear term. Hence \(F\) is surjective onto \(\mathcal S\) for each \(0<k<1\).

**2. Exact Jacobian and injective regimes.** The derivatives of \(s=F_1(x,q)\) are
\[
\partial_xs=s(1-s)\left(\frac1{x(1-x)}-a\right),\qquad
\partial_qs=-ac\,s(1-s).
\]
Consequently
\[
\det DF(x,q)
=s(1-s)\left[\frac{1-k}{x(1-x)}-a\bigl(1-k(1+cp_1)\bigr)\right]
=(1-k)s(1-s)H'(x).
\]
Because \(x(1-x)\le1/4\), if \(\beta\le0\), or if \(\beta>0\) and \(a\beta<4\), then \(H'(x)>0\) everywhere. Strict monotonicity and the infinite endpoint limits make \(H\) a bijection \((0,1)\to\mathbb R\). The inverse-function theorem and the explicit inverse formulas make \(F\) a global smooth diffeomorphism with positive Jacobian. Since \(\beta\le0\iff k\ge k_c\) for \(k<1\), this proves the first regime.

**3. Critical equality.** At \(a\beta=4\), one has \(H'(x)\ge0\), with equality only at \(x=1/2\), so \(H\) is still strictly increasing. Writing \(x=1/2+u\) gives the convergent local expansion
\[
H(1/2+u)-H(1/2)=\frac{16}{3}u^3+\frac{64}{5}u^5+O(u^7).
\]
Thus \(F\) remains a homeomorphism on \(\mathcal S\), but \(\det DF=0\) on the entire line \(x=1/2\), and inversion transverse to its image has a cubic-root singularity. In particular, a \(C^1\) local inverse is impossible on that line.

**4. Two folds, exact multiplicities, and opening law.** If \(\Lambda>4\), solving \(H'(x)=0\) gives exactly \(x_\pm\) above. As \(x\) increases, \(H'\) has signs \(+,-,+\) on the three complementary intervals. Therefore \(x_-\) is a strict local maximum and \(x_+\) a strict local minimum. Together with the infinite endpoint limits, this proves all three inverse-fiber counts, including the double-fiber values on the fold images. Direct substitution gives
\[
W(\Lambda)=\Lambda d-4\operatorname{arctanh}d
=4\left(\frac{d}{1-d^2}-\operatorname{arctanh}d\right).
\]
Using \(d^2=(\Lambda-4)/\Lambda\) and the Taylor series \(\operatorname{arctanh}d=d+d^3/3+O(d^5)\) yields
\[
W(\Lambda)=\frac83d^3+O(d^5)
=\frac13(\Lambda-4)^{3/2}+O\left((\Lambda-4)^{5/2}\right).
\]
The fold criticality is nondegenerate since \(H''(x_\pm)\ne0\), while the single critical line at equality is cubically degenerate in the transverse coordinate.

**5. Unit belief-adjustment rate.** At \(k=1\), the second image coordinate is \(Q=p_0+p_1x\), so \(x=(Q-p_0)/p_1\). The first-coordinate logit then determines
\[
q=\frac{\ell(x)-a(x-b)-\ell(s)}{ac}.
\]
Because \(p_1,c,a>0\), this is a smooth global inverse to the stated image strip. The Jacobian is \(acp_1s(1-s)>0\).

**6. Physical realization.** For the displayed three input states, \(x-b+cq\) is exactly, respectively, \(1/12\), \(1/4\), \(5/12\). Their input logits are \(-\log3\), \(0\), \(+\log3\); subtracting \(6\log3\) times the respective cost gives the common output logit \(-\frac32\log3\). Direct rational substitution into the belief update gives \(Q=1/2000\) in all three cases. Since \(1/(x(1-x))\) equals \(16/3,4,16/3\) at these points, respectively, the Jacobian formula and \(1<\log3<4/3\) give its signs \(+,-,+\). All states satisfy \(0<x<1\) and \(0\le q\le1/1000\), as required.

## Verification

The standalone file `check_fold.py` evaluates the exact model at 70-digit precision, confirms the three images and determinant signs, the critical-point formulas, the positive fold width, and the \(1/3\) width coefficient. A separate exact-symbolic calculation confirms the Jacobian identity, the cubic Taylor coefficient, and the three logarithmic-cost equalities. The finite computational checks are diagnostics; every quantified assertion follows from the elementary logit reduction, monotonicity, and Taylor-expansion proof above. To reproduce the diagnostic run: `python check_fold.py` with Python 3 and `mpmath` installed.

## Relationship to prior work

Metaxas and Sapsis [1], Section 2, introduce the same two-dimensional learning map and derive its equilibria and Cesàro-average properties. Their Section 3 analyzes numerical bifurcation diagrams, periodic/chaotic attractors, and basins; the material inspected does not present an exact global invertibility or inverse-fiber classification. The all-parameter classification above is an additional structural result for that same map, not a new definition of the learning rule.

Chotibut, Falniowski, Misiurewicz, and Piliouras [2] study multiplicative-weights dynamics in a different two-agent congestion-game map and its one-dimensional invariant diagonal. Bielawski and coauthors [3] develop chaos for regularized learning in routing games. Neither result supplies this adaptive-belief map's explicit inverse, critical learning-rate curve, or three-preimage physical example. General fold and cusp phenomena in noninvertible planar maps are established background; the claimed contribution is the *model-specific sharp global classification and exact physical witness*, not fold theory itself.

For example, the numerical parameter choice of [1] with \(c=500\) and \(p_1=10^{-3}\) has \(k_c=2/3\); its illustrated case \(k=0.865\) therefore belongs to the proven globally injective regime for every \(a>0\). Thus complex dynamics and folding of the one-step map need not coincide. This observation does not imply an analytical proof of chaos in that parameter regime.

## Limitations

The complete one/two/three inverse-fiber census is on the algebraic extension \(\mathcal S\). Boundary-clipped physical fibers may contain fewer points; the explicit physical witness shows that three can occur without claiming they occur in the rectangle for every supercritical parameter tuple. The theorem does not classify attractors, invariant measures, rates of mixing, periodic points, or the analogous CVaR-clipped variant discussed in [1]. Novelty is assessed against inspected literature and searched records; an equivalent historical formula in unexamined sources cannot be excluded, and there has been no independent scientific audit.

## References

[1] Konstantinos Metaxas and Themistoklis P. Sapsis, *Risk-Sensitive Learning in Population Games under Extreme Events: Bifurcations and Chaotic Dynamics*, arXiv:2606.29967, initially public 2026-06-29. https://arxiv.org/abs/2606.29967 . Equations (4)–(10), Section 3, Appendix A.

[2] Thiparat Chotibut, Fryderyk Falniowski, Michał Misiurewicz, and Georgios Piliouras, *Family of chaotic maps from game theory*, arXiv:1807.06831 (2018); *Dynamical Systems* 36 (2021), 48–63. https://arxiv.org/abs/1807.06831 .

[3] Jakub Bielawski, Thiparat Chotibut, Fryderyk Falniowski, Grzegorz Kosiorowski, Michał Misiurewicz, and Georgios Piliouras, *Follow-the-Regularized-Leader Routes to Chaos in Routing Games*, ICML/PMLR 139 (2021), 925–935. https://proceedings.mlr.press/v139/bielawski21a.html .
