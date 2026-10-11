# Four-phase Jung constant of weighted Lorentz-predual octagonal planes
## Finding
For every \(0<w<1\), equip the real vector plane with the Lorentz-predual norm
\[
N_w(s,t)=\max\left\{|s|,|t|,\frac{|s|+|t|}{1+w}\right\}.
\]
For every nonempty bounded set \(S\) let \(r_w(S)=\inf_{c\in\mathbb R^2}\sup_{x\in S}N_w(x-c)\) and \(d_w(S)=\sup_{x,y\in S}N_w(x-y)\). Its Jung constant, with radius-to-diameter normalization \(J(X_w)=\sup_{d_w(S)>0}2r_w(S)/d_w(S)\), is exactly
\[
J(X_w)=
\begin{cases}
\dfrac{3(1+w)}{3+w},&0<w\le\dfrac13,\\[2mm]
\dfrac4{3+w},&\dfrac13\le w\le\sqrt2-1,\\[2mm]
\dfrac{2(1+w)}{2+w},&\sqrt2-1\le w\le\dfrac12,\\[2mm]
\dfrac3{2+w},&\dfrac12\le w<1.
\end{cases}
\]
Consequently, the maximum of \(J(X_w)\) throughout this family is \(6/5\), attained at exactly two parameters \(w=1/3\) and \(w=1/2\). At the intermediate regular-octagon parameter \(w=\sqrt2-1\), the profile has a strict local minimum with \(J(X_w)=4-2\sqrt2\). Every branch is witnessed by an explicit three-point set of diameter one, and all upper bounds hold for arbitrary bounded sets, not only triangles.

## Assumptions and scope
All spaces are real and two-dimensional. Write \(k=1+w\), so \(1<k<2\), and set
\[
N_k(s,t)=\max\{|s|,|t|,|s+t|/k,|s-t|/k\}.
\]
This equals the norm in the finding since \(\max\{|s+t|,|s-t|\}=|s|+|t|\). The closed unit ball is a centrally symmetric octagon with coordinate facets and two diagonal facet directions. We use the Jung normalization
\[
J(X_k)=\sup_{S,\ d(S)>0}\frac{2r(S)}{d(S)},
\quad r(S)=\inf_c\sup_{z\in S}N_k(z-c),
\quad d(S)=\sup_{z,z'\in S}N_k(z-z').
\]
Translation and scaling allow us to work with sets of diameter at most one. The supremum over arbitrary bounded sets agrees with that over their compact closures because the norm is continuous in finite dimension.

## Proof
### 1. A finite-support Chebyshev-radius identity
Define four linear forms
\[
f_1(s,t)=s,\quad f_2(s,t)=t,\quad
f_3(s,t)=(s+t)/k,\quad f_4(s,t)=(s-t)/k.
\]
Let \(F=\{\pm f_1,\pm f_2,\pm f_3,\pm f_4\}\). Since \(N_k(z)=\max_{f\in F}f(z)\), the support function \(h_S(f)=\max_{z\in S}f(z)\) satisfies
\[
r(S)=\min_{c\in\mathbb R^2}\max_{f\in F}\bigl(h_S(f)-f(c)\bigr).
\]
Finite linear-programming duality gives
\[
r(S)=\max\left\{\sum_{f\in F}\alpha_fh_S(f):
\alpha_f\ge0,\ \sum_f\alpha_f=1,\ \sum_f\alpha_f f=0\right\}.
\tag{1}
\]
The feasible polytope has three affine equations (mass and the two coefficients). Thus a maximizing extreme point has at most three positive weights. A two-term positive dependence is necessarily an opposite pair \(\{f,-f\}\), contributing half a support width, at most \(d(S)/2\). Any three-term minimal positive dependence uses three distinct unoriented directions. The eight signed forms have just four unoriented directions; choosing three of four gives four possibilities, and coordinate sign changes and interchange identify them in two families. The four underlying direction triples have the explicit relations
\[
f_1+f_2-kf_3=0,\qquad f_1-f_2-kf_4=0,
\]
\[
2f_1-kf_3-kf_4=0,\qquad 2f_2-kf_3+kf_4=0.
\]
Each relation, with its displayed coefficient signs, yields a positive dependence of the appropriately oriented forms. The first two are isometrically equivalent (Type I), as are the latter two (Type II); reversing all signs makes no new type. They yield respective dual weights \((1,1,k)/(k+2)\) and \((2,k,k)/(2+2k)\). We compute the maximal possible obstruction from each type over sets of diameter at most one.

### 2. Axis--axis--diagonal circuits (Type I)
The Type I functional in (1) is
\[
R_I(S)=\frac{h_S(f_1)+h_S(f_2)+k h_S(-f_3)}{k+2}.
\]
Choose support-attaining points \(p,q,z\) for its three terms and translate so that \(z=0\). The numerator becomes \(p_1+q_2\). Since \(N_k(p),N_k(q),N_k(p-q)\le1\),
\[
p_1+q_2\le2.
\]
Using the three facet inequalities
\[
p_1+p_2\le k,\quad q_1+q_2\le k,\quad
(p_1-q_1)-(p_2-q_2)\le k
\]
we obtain \(2p_1+2q_2\le3k\). Hence
\[
R_I(S)\le\frac{\min\{3k/2,2\}}{k+2}.
\tag{2}
\]
Both bounds are exact. For \(1<k\le4/3\), take the three-point set
\[
S_I(k)=\{0,(3k/2-1,1-k/2),(k-1,1)\}.
\]
Its three pairwise distances are at most one and the chosen support contributions give \(p_1+q_2=3k/2\). For \(4/3\le k<2\), take
\[
S_I(k)=\{0,(1,k-1),(k-1,1)\}.
\]
Again its diameter is one, and \(p_1+q_2=2\). As every support function is at least its value at the indicated point, the dual expression in (1) reaches the displayed bound.

### 3. Axis--diagonal--diagonal circuits (Type II)
The other positive circuit gives
\[
R_{II}(S)=\frac{2h_S(f_1)+k h_S(-f_3)+k h_S(-f_4)}{2+2k}.
\]
Take support points \(p,q,z\) respectively and translate \(z=0\). The numerator is \(2p_1-q_1-q_2\). Since \(N_k(p),N_k(q),N_k(p-q)\le1\), adding
\[
p_1-p_2\le k,\qquad
(p_1-q_1)+(p_2-q_2)\le k
\]
gives \(2p_1-q_1-q_2\le2k\). Also, adding \(p_1\le1\), \(p_1-q_1\le1\), and \(-q_2\le1\) gives the independent bound \(2p_1-q_1-q_2\le3\). Therefore
\[
R_{II}(S)\le\frac{\min\{2k,3\}}{2+2k}.
\tag{3}
\]
Here too both regimes are exact. For \(1<k\le4/3\) take
\[
S_{II}^{(a)}(k)=\{0,(k/2,-k/2),(1-k,-1)\}.
\]
For \(4/3\le k\le3/2\) take
\[
S_{II}^{(b)}(k)=\{0,(1,1-k),(3-2k,-1)\},
\]
and for \(3/2\le k<2\) take
\[
S_{II}^{(c)}(k)=\{0,(1,1-k),(0,-1)\}.
\]
In each parameter interval all three pairwise distances are at most one. The last two support expressions reach \(2k\) in the first two intervals and \(3\) in the last. Thus the upper bound (3) is attained.

### 4. Combining circuits and locating the phase transitions
The opposite-pair circuits contribute at most \(1/2\). For every \(1<k<2\), at least one of (2) and (3) is strictly greater than \(1/2\). Combining all possible dual extreme points and the explicit witness sets gives the exact identity
\[
J(X_k)=2\max\left\{\frac{\min\{3k/2,2\}}{k+2},\frac{\min\{2k,3\}}{2+2k}\right\}
=\max\left\{\frac{\min\{3k,4\}}{k+2},\frac{\min\{2k,3\}}{k+1}\right\}.
\tag{4}
\]
For \(1<k\le4/3\), the first term dominates because \(3(k+1)\ge2(k+2)\). For \(4/3\le k\le3/2\), their equality is \(4/(k+2)=2k/(k+1)\), equivalently \(k=\sqrt2\). For \(3/2\le k<2\), the second dominates because \(3(k+2)\ge4(k+1)\). This yields the four-branch formula in the finding after substitution \(k=1+w\).

The first and third branches are strictly increasing and the second and fourth strictly decreasing. The two peak parameters are \(k=4/3\) and \(k=3/2\), both giving \(J=6/5\). Between them \(k=\sqrt2\) is the unique strict local minimum, with \(J=4/(2+\sqrt2)=4-2\sqrt2\). This proves the complete claim.

## Verification
All five witness triples above admit direct checks using
\[
N_k(a,b)\le1\iff |a|,|b|\le1\ \text{and}\ |a+b|,|a-b|\le k.
\]
For example, in the first Type I triple \(p-q=(k/2,-k/2)\), whereas in the second Type I triple \(p-q=(2-k,k-2)\), whose diagonal constraint is \(2(2-k)\le k\) exactly when \(k\ge4/3\). In the middle Type II triple \(p-q=(2k-2,2-k)\), whose coordinate constraint \(2k-2\le1\) holds exactly when \(k\le3/2\); in the final Type II triple \(p-q=(1,2-k)\), whose diagonal constraint \(3-k\le k\) begins exactly at \(k=3/2\).

The optimization is analytic and includes all bounded sets through finite linear-programming duality. As a separate numerical cross-check only, direct three-point Chebyshev-radius linear programs at rational values \(k=11/10,5/4,4/3,7/5,3/2,8/5,19/10\) reproduce the rational values of (4). These calculations are not needed for the proof.

## Relationship to prior work
Kato, Maligranda, and Takahashi study geometric constants and normal structure of Banach spaces. Mitani and Saito identify the dual norm of two-dimensional Lorentz sequence spaces and compute a James-type constant; the available abstract does not establish any Jung formula. Zuo computes the Ptolemy constant of two-dimensional Lorentz spaces and their duals, including the same \(q=1\) polyhedral dual family. Those formulas concern four-point metric ratios rather than the optimal containing-ball radius, so do not imply (4).

Alonso, Martín, and Papini (2025) give the regular-octagonal inscribed-equilateral perimeter and general inequalities involving the Jung constant. At \(w=\sqrt2-1\), their regular-octagonal side length \(1+1/\sqrt2\) already implies the specialized Jung value \(4-2\sqrt2\); that single special case is *not* claimed to be novel. Their 2026 article develops the general equivalence between Jung's constant and the minimal inscribed-equilateral side length and provides sharp qualitative characterizations. It does not state a Jung profile for weighted Lorentz-predual octagons.

The new contribution is the exact four-regime parameter profile and its two distinct off-regular maxima. Unlike the regular-octagon special case, it requires resolving all positive facet circuits and tracking their crossing as the norm parameter changes.

## Limitations
The theorem is only about the real two-dimensional Lorentz-predual octagonal family with \(0<w<1\). It does not characterize all maximal triangles, give a modulus of stability near maximizing sets, or determine Jung constants for higher-dimensional Lorentz spaces. General Jung results already subsume statements at isolated special shapes but not the explicit profile without the new facet calculation. The complete 2009 original source for the Lorentz dual norm could not be inspected, so a historical same-family coverage risk remains; no claim of exhaustive global novelty is made.

## References
1. M. Kato, L. Maligranda, and Y. Takahashi, “On James and Jordan–von Neumann constants and the normal structure coefficient of Banach spaces,” *Studia Mathematica* 144 (2001), 275–295, DOI 10.4064/sm144-3-5; earliest verified day-level public date 2001-06-17; primary MSC 46B20.
2. K.-I. Mitani and K.-S. Saito, “Dual of two dimensional Lorentz sequence spaces,” *Nonlinear Analysis* 71 (2009), 5238–5247, DOI 10.1016/j.na.2009.04.007.
3. Z.-F. Zuo, “On the Ptolemy constant of Lorentz sequence spaces and their duals,” *ScienceAsia* 44 (2018), 340–345, DOI 10.2306/scienceasia1513-1874.2018.44.340.
4. J. Alonso, P. Martín, and P. L. Papini, “Perimeter of triangles inscribed in the unit ball of normed planes,” *Mediterranean Journal of Mathematics* 22 (2025), Article 46, DOI 10.1007/s00009-025-02805-6; first published 2025-02-23.
5. J. Alonso, P. Martín, and P. L. Papini, “Wheeling around Chebyshev centers and Jung constant in normed planes,” *Rendiconti del Circolo Matematico di Palermo, Series 2* 75 (2026), Article 131, DOI 10.1007/s12215-026-01436-4; first published 2026-07-09.
