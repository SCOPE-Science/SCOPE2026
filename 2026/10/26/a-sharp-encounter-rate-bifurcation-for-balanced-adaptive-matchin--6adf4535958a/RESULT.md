# A sharp encounter-rate bifurcation for balanced adaptive matching

## Finding

Consider the repeated, two-sided matching model described below, with strictly positive desired match rates and balanced totals. There is an exact encounter-rate threshold
\[
K_{\mathrm c}=\frac{c_{\max}d_{\max}}{T},\qquad T=\sum_{i=1}^{M}c_i=\sum_{j=1}^{N}d_j.
\]
For \(0<K<K_{\mathrm c}\) the projected adjustment system has exactly one equilibrium, and its achieved total matching rate \(R(K)\) is strictly less than \(T\). At \(K=K_{\mathrm c}\) the equilibrium is still unique and achieves \(R=T\). For \(K>K_{\mathrm c}\), the equilibrium set is exactly the nondegenerate line-segment parameterization
\[
a_i=\frac{c_i A}{T},\qquad b_j=\frac{d_j}{KA},\qquad
\frac{d_{\max}}K\le A\le\frac{T}{c_{\max}}.
\]
Every equilibrium in this segment achieves the entire target volume \(R=T\). Interior segment points are normally attracting for the linear adjustment law, with precisely one neutral (tangential) mode. The matching shortfall approaches zero *linearly* from below:
\[
\lim_{K\uparrow K_{\mathrm c}}\frac{T-R(K)}{K_{\mathrm c}-K}
=\frac{1}{K_{\mathrm c}\,\eta},\qquad
\eta=\frac1{m_c c_{\max}}+\frac1{m_d d_{\max}}-\frac1T>0,
\]
where \(m_c,m_d\) are the numbers of agents attaining the respective maximum targets. Above the threshold the shortfall is identically zero, so the matched-volume curve has a sharp derivative kink.

There is also an exact outcome-selection law in the homogeneous-within-side version of this balanced model. Suppose all left targets equal \(c\), all right targets equal \(d\), and \(Mc=Nd=T\). Let \(A_0\in[0,M]\), \(B_0\in[0,N]\) be the sums of initially identical acceptance probabilities on the two sides, and write \(h_0=A_0-B_0\). When \(K>K_{\mathrm c}=T/(MN)\), define
\[
h_-=\frac dK-N,\quad h_+=M-\frac cK,\quad
h_*=\min\{h_+,\max\{h_-,h_0\}\}.
\]
Every such symmetric trajectory converges to the equilibrium with aggregate acceptances
\[
A_* = \frac{h_*+\sqrt{h_*^2+4T/K}}2,\qquad B_*=A_*-h_*.
\]
For \(K\le K_{\mathrm c}\), every symmetric trajectory converges to full acceptance \((A,B)=(M,N)\). Thus the encounter threshold separates a uniquely saturated regime from a continuum that retains a quantitatively computable memory of starting selectivity.

## Assumptions and scope

Fix arbitrary integers \(M,N\ge1\), desired left-side rates \(c_i>0\), right-side rates \(d_j>0\), a uniform per-pair encounter rate \(K>0\), and a common adaptation factor \(r>0\). Set \(a_i,b_j\in[0,1]\) for acceptance probabilities and \(A=\sum_i a_i\), \(B=\sum_j b_j\). The projected linear-feedback dynamics are
\[
\dot a_i=r(c_i-Ka_i B),\qquad
\dot b_j=r(d_j-Kb_j A)
\]
whenever a coordinate is below one; at one, replace a positive derivative by zero. At zero the unprojected derivative is positive, so zero cannot be stationary. Matching events count once on each side, giving aggregate successful-match rate \(R=KAB\). All claims assume the balanced condition \(\sum_i c_i=\sum_jd_j=T\), except where explicitly stated otherwise. No randomness of encounters beyond its modeled mean rate is needed for the deterministic results.

The equilibrium classification and threshold also apply to any projected feedback vector fields \(g_i(Ka_iB)\), \(h_j(Kb_jA)\) with a unique sign reversal at \(c_i\), \(d_j\), respectively, as in the motivating model, because stationary coordinates obey the same capped formulas. The neutral spectrum, derivative-time statements, and selection law below concern the common-rate *linear* feedback system displayed above. The homogeneous selection law assumes within-side identical initial acceptance probabilities, not merely identical targets.

## Proof

**1. Exact stationary equations.** For positive targets, an equilibrium must have \(A,B>0\), and the projected coordinate equations are equivalent to
\[
a_i=\min\{1,c_i/(KB)\},\qquad
b_j=\min\{1,d_j/(KA)\}.
\]
Write \(x=KB\), \(y=KA\), and define increasing capped-demand functions
\[
C(x)=\sum_i\min\{c_i,x\},\qquad
D(y)=\sum_j\min\{d_j,y\}.
\]
Their common value at any equilibrium is the actual match rate:
\[
R=KAB=C(x)=D(y),\qquad xy=KR.
\]
As all \(c_i,d_j\) are positive, \(C\) and \(D\) are continuous and strictly increasing from zero to \(T\) on \([0,c_{\max}]\) and \([0,d_{\max}]\), respectively, and are constant equal to \(T\) above these maxima.

**2. Below-target branch and uniqueness.** For \(0<R<T\), there are unique \(x=C^{-1}(R)\in(0,c_{\max})\) and \(y=D^{-1}(R)\in(0,d_{\max})\). A necessary and sufficient scalar equation is
\[
K=\Psi(R):=\frac{C^{-1}(R)D^{-1}(R)}R.
\]
Indeed, if it holds, set \(a_i=\min\{1,c_i/x\}\), \(b_j=\min\{1,d_j/y\}\). These have sums \(A=R/x=y/K\) and \(B=R/y=x/K\), and satisfy every equilibrium equation. Conversely, every subtarget equilibrium yields this construction. As \(C(x)/x=\sum_i\min\{1,c_i/x\}\) is nonincreasing in \(x>0\), its reciprocal \(C^{-1}(R)/R\) is nondecreasing in \(R\). Since \(D^{-1}(R)\) is strictly increasing and positive, \(\Psi(R)\) is strictly increasing. Moreover,
\[
\lim_{R\downarrow0}\Psi(R)=0,\qquad
\lim_{R\uparrow T}\Psi(R)=\frac{c_{\max}d_{\max}}T=K_{\mathrm c}.
\]
Thus exactly one \(R<T\) equilibrium occurs for each \(0<K<K_{\mathrm c}\), and none occurs at or above the threshold. In the below-threshold regime, each side necessarily has at least one agent accepting with probability one, because \(x<c_{\max}\) and \(y<d_{\max}\).

**3. Full-target branch and the sharp transition.** If \(R=T\), every desired rate must be achieved individually, so \(a_i=c_i/(KB)\) and \(b_j=d_j/(KA)\) even for saturated coordinates (equality is allowed). Summation and \(R=KAB\) give \(a_i=c_i A/T\), \(b_j=d_j/(KA)\), and \(AB=T/K\). The bounds \(a_i,b_j\le1\) are exactly
\[
\frac{d_{\max}}K\le A\le \frac{T}{c_{\max}}.
\]
This interval is nonempty precisely when \(K\ge K_{\mathrm c}\). For equality it is a point; above the threshold it has positive length. Together with step 2, these exhaust all equilibria and give the claimed unique-versus-continuum classification.

**4. Matching-volume cusp.** Let \(m_c\) and \(m_d\) denote the respective multiplicities of \(c_{\max}\) and \(d_{\max}\). For all sufficiently small \(\varepsilon>0\), the exact piecewise-linear identities
\[
C^{-1}(T-\varepsilon)=c_{\max}-\varepsilon/m_c,\qquad
D^{-1}(T-\varepsilon)=d_{\max}-\varepsilon/m_d
\]
hold. Consequently
\[
K=\frac{(c_{\max}-\varepsilon/m_c)(d_{\max}-\varepsilon/m_d)}{T-\varepsilon}
=K_{\mathrm c}\bigl(1-\eta\varepsilon+O(\varepsilon^2)\bigr).
\]
The coefficient \(\eta>0\), since \(m_cc_{\max}\le T\). With \(\varepsilon=T-R(K)\), this proves the one-sided limit. On the full-target branch, \(R(K)=T\) identically, proving the derivative discontinuity.

**5. Normal spectrum of the interior continuum.** At a segment point with strictly subunit coordinates, the unprojected vector field is smooth. Differences of left coordinates with zero aggregate sum decay with exponent \(-rKB\), of multiplicity \(M-1\); analogous right differences decay with exponent \(-rKA\), of multiplicity \(N-1\). The linearization on aggregates is
\[
r\begin{pmatrix}-KB&-KA\\-KB&-KA\end{pmatrix},
\]
whose eigenvalues are \(0\) and \(-rK(A+B)\). Thus the full Jacobian has precisely one zero eigenvalue tangent to the equilibrium segment, with every other eigenvalue negative, proving normal attraction in the usual linearized transverse sense. This does not assert that one particular interior equilibrium attracts the entire surrounding segment.

**6. Exact selection in homogeneous populations.** Assume \(c_i=c\), \(d_j=d\), \(Mc=Nd=T\), and within-side uniform initial values. That symmetry is preserved. The projected aggregate flow is
\[
\dot A=\dot B=r(T-KAB)
\]
whenever neither upper bound is actively clipping a positive velocity; positive velocities are set to zero on \(A=M\) or \(B=N\), respectively. For \(K\le T/(MN)\), the product \(AB\le MN\) forces both aggregates to increase toward \((M,N)\), the sole equilibrium. For \(K>T/(MN)\), the equilibrium hyperbola \(AB=T/K\) meets the rectangle \([0,M]\times[0,N]\) on a connected arc with endpoint differences \(h_-=d/K-N\) and \(h_+=M-c/K\). Prior to any active upper-face clipping, \(h=A-B\) is constant; the scalar velocity changes sign only on the hyperbola. If \(h_0\in[h_-,h_+]\), the trajectory reaches the hyperbola asymptotically before an outward upper-face contact, retaining \(h_0\). If \(h_0>h_+\), its initial product is below \(T/K\), its left aggregate reaches \(M\), and its right aggregate then increases to \(c/K\), selecting \(h_+\). The reflected case \(h_0<h_-\) selects \(h_-\). Intersecting the hyperbola with \(A-B=h_*\) gives the stated square-root formula, including all boundary initial states.

## Verification

The accompanying standalone `verify.py` uses only Python's standard library. It exhaustively pairs all positive-integer target vectors of lengths one to three with totals at most nine, resulting in 2,405 balanced target instances. It constructs 88,985 exact-rational equilibria on the below-threshold and at/above-threshold branches, independently checking coordinatewise capped stationarity and both aggregate matching identities. In addition, 384 projected-flow numerical trials check the homogeneous outcome-selection formula across sizes, encounter rates, and initial values. All checks pass. These finite tests corroborate the algebra; they do not establish the universal claims, which follow from the proof above.

For a concrete heterogeneous balanced example, take left and right target vectors both equal to \((1,2)\). Here \(T=3\), \(K_{\mathrm c}=4/3\). At \(K=2\), the interior equilibrium with \(A=5/4\) has \(a=(5/12,5/6)\) and \(b=(2/5,4/5)\). All four target rates are achieved. At \(K=1\), the unique equilibrium is symmetric across sides with \(a=b=(1/\varphi,1)\), where \(\varphi=(1+\sqrt5)/2\), and it delivers only \(R=\varphi^2<3\).

## Relationship to prior work

Gelastopoulos (2026) specifies the two-sided adaptive-selectivity system, proves unique globally attractive equilibrium when the two sides' sums of desired rates are *unequal*, and supplies implicit capped equilibrium equations for arbitrary rates. Its Section 2.2 explicitly sets aside the equal-sums case, and its Section 3.3 does not provide the sharp encounter-rate classification on that excluded balance hyperplane. The present result uses the same model but proves the balanced-case rate threshold, complete heterogeneity-sensitive equilibrium shape, sharp matching-volume cusp, normal spectral structure, and homogeneous initial-condition selection. The published capped equations are important starting points; this is not a new mechanism or a claim to a new model.

Related economic search-and-matching balance work (Lauermann, Nöldeke, and Tröger, 2020; Lauermann and Nöldeke, 2025) addresses market entry/exit balance and search frictions rather than this fixed-population, continuously adjusted acceptance system. Exact priority for an equivalent theorem under other matching terminology is not independently certified.

## Limitations

The classification is for a deterministic mean-rate model with independent bilateral acceptance in encounters, positive target rates, fixed group populations, and symmetric pair-encounter intensity. The normal-spectrum calculation requires linear adaptation with a common coefficient and excludes segment endpoints, where the projected vector field is nonsmooth. The exact global selection result is only for *homogeneous targets and within-side homogeneous initial conditions*. No universal selection formula is claimed for arbitrary heterogeneous initial configurations. The projected dynamics do not model exclusive long-term matches or strategic forward-looking search, and no stochastic fluctuation or finite-sample concentration theorem is asserted. Historical priority remains subject to independent literature evaluation.

## References

1. A. Gelastopoulos, *Feedback dynamics in matching networks drive behavioral differentiation despite overlapping objectives*, arXiv:2606.31802v1, first posted 30 June 2026. https://arxiv.org/html/2606.31802
2. S. Lauermann, G. Nöldeke, and T. Tröger, *The Balance Condition in Search-and-Matching Models*, Econometrica 88 (2020), 595–618, DOI:10.3982/ECTA8356.
3. S. Lauermann and G. Nöldeke, *Matching with Frictions*, in *Handbook of the Economics of Matching*, Vol. 2 (2025), pp. 579–642.
