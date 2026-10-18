# A sharp null-basin barrier for diagonal invariant sets in the three-dimensional Lozi map

## Finding

Consider the three-dimensional piecewise-affine map introduced in [1], restricted to its symmetric parameter family:
\[
T_{a,b}(x,y,z)=\bigl(a|x|+y\operatorname{sgn}(z)+1,\ b(x+z),\ a|z|+y\operatorname{sgn}(x)+1\bigr),
\]
where \(a,b\in\mathbb R\setminus\{0\}\) and \(\operatorname{sgn}(0)=1\). Write \(D=\{(x,y,z):x=z\}\). The central theorem is a global obstruction to ambient attraction on this natural invariant plane, including the neutral parameter boundary. The exact transverse derivative supplies the mechanism and a constructive sink example shows that the parameter restriction cannot be relaxed uniformly.

**Supporting exact transverse law.** With \(u=(x+z)/2\) and \(w=(x-z)/2\), whenever \(x,z\) have the same assigned sign \(s\in\{-1,1\}\),
\[
u'=as u+s y+1,\qquad y'=2bu,\qquad w'=as w.\tag{1}\]
In particular, \(D\) is invariant. For every invariant ergodic probability \(\mu\) supported on \(D\) with \(\mu(\{x=0\})=0\), the three Lyapunov exponents, counted with multiplicity, consist of the two tangent Lyapunov exponents of \(T_{a,b}|_D\) and the **exact transverse exponent**
\[
\lambda_\perp=\log|a|.\tag{2}
\]
Moreover, the sum of the two tangent exponents is \(\log|2b|\). The transverse sign changes precisely at \(|a|=1\), independent of the invariant probability and of \(b\). If the restricted measure has a positive tangent exponent, then for \(|a|>1\) its ambient three-dimensional derivative cocycle has at least two positive exponents; this does not imply that its support is an ambient attractor.

**Global null-basin theorem.** If \(|a|\ge1\) and \(K\subset D\) is any nonempty compact forward-invariant set with \((0,0,0)\notin K\), then
\[
\operatorname{Leb}_3\{p\in\mathbb R^3:\operatorname{dist}(T_{a,b}^{n}p,K)\longrightarrow0\}=0.\tag{3}
\]
The conclusion allows \(K\) to intersect the switching line \(x=z=0\) at points with nonzero \(y\). In particular, every such set is excluded from being a positive-volume-basin attractor in the ambient space, even if it attracts points within \(D\). The theorem does **not** assert (3) for compact sets containing the origin.

**Sharpness of the parameter range.** For every \(a\) with \(0<|a|<1\), choose
\[
0<b<\frac{1-|a|}{2}.\tag{4}
\]
Then the diagonal fixed point
\[
P_{a,b}=\left(\frac1{1-a-2b},\frac{2b}{1-a-2b},\frac1{1-a-2b}\right)\tag{5}
\]
is a hyperbolic attracting fixed point in the full three-dimensional phase space and therefore has an open positive-volume basin. Thus no analogous uniform null-basin conclusion can hold for all \(|a|<1\). The exact transverse exponent (2) and this positive-basin example are supporting consequences; novelty is asserted for the all-parameter global null-basin barrier (3), especially its neutral and switching-line boundary cases.

**Exact finite-time separation away from the switching line.** Suppose a reference orbit in \(D\) has diagonal coordinate \(u_j\) with \(|u_j|\ge\delta>0\) throughout a finite interval, and perturb it by \(w_0\) without changing \(u_0,y_0\). Until \(|w_j|\) first reaches \(\delta\), the center follows the reference orbit exactly and \(|w_j|=|a|^j|w_0|\). If \(|a|>1\) and \(0<|w_0|<\delta\), the first exit time from the \(\delta\)-tube is
\[
N=\left\lceil\frac{\log(\delta/|w_0|)}{\log|a|}\right\rceil,\tag{6}
\]
provided the reference orbit stays at least \(\delta\) away from \(u=0\) through step \(N-1\). At \(|a|=1\), exact transverse distance is constant as long as signs match.

## Assumptions and scope

The map is defined on all of \(\mathbb R^3\), with the convention \(\operatorname{sgn}(0)=1\) from [1]. The hypotheses \(a\ne0\), \(b\ne0\) make every open-quadrant affine branch locally invertible. The term *basin* in (3) is the set of initial points whose Euclidean distance to \(K\) tends to zero, not a claim of convergence to any selected orbit. The ergodic-spectrum assertion applies to invariant probabilities avoiding the switching line in measure, because classical derivatives may fail on that line. No attracting or chaotic measure is assumed to exist; each conclusion is conditional on the explicitly stated invariant object.

The sign of an argument is defined to be \(-1\) strictly below zero and \(+1\) at and above zero; this convention also fixes the boundary dynamics. The claims are formulated for the exact real map without numerical rounding.

## Proof

**1. Coordinate splitting.** Put \(x=u+w\), \(z=u-w\). If the assigned signs of \(x,z\) agree at \(s\), then either both are nonnegative or both strictly negative, and
\(|x|+|z|=2s u\), \(|x|-|z|=2s w\). Substitution gives (1). On \(D\), the equality \(x=z\) also forces equal assigned signs, including at zero, proving forward invariance.

At a diagonal point with \(u\ne0\), the derivative in coordinates \((u,y,w)\) is
\[
J_s=\begin{pmatrix}as&s&0\\2b&0&0\\0&0&as\end{pmatrix},\quad
\det J_s=-2ab.\tag{7}
\]
The tangent and normal subspaces are invariant under every smooth-branch derivative. The normal \(n\)-step derivative is \(a^n\prod_{j=0}^{n-1}\operatorname{sgn}(u_j)\), whose absolute value is \(|a|^n\). The tangent derivative has determinant of absolute value \(|2b|\) at every step. Both the derivative and its inverse have bounded norms on the finitely many smooth branches because \(a,b\ne0\). Thus the standard multiplicative ergodic theorem applies along almost every orbit of any invariant ergodic probability assigning zero mass to \(u=0\), yielding (2), the tangent exponent-sum identity, and the multiset decomposition. These are identities for the linear cocycle, not assertions of nonlinear stability at a discontinuity.

**2. Opposite-sign visits cannot persist near a compact diagonal set avoiding the origin.** Let \(p_n=T^n(p)=(u_n+w_n,y_n,u_n-w_n)\), and assume \(\operatorname{dist}(p_n,K)\to0\). Since \(K\subset D\), we have \(w_n\to0\). Suppose there were infinitely many indices \(n_j\) where the assigned signs of \(x_{n_j}\) and \(z_{n_j}\) differ. Then, including the prescribed convention at zero, the two coordinates necessarily lie on opposite sides of zero, so \(|u_{n_j}|\le|w_{n_j}|\to0\). Their transverse update is exactly
\[
w_{n_j+1}=\begin{cases}a u_{n_j}-y_{n_j},&\operatorname{sgn}(x_{n_j})=1,\ \operatorname{sgn}(z_{n_j})=-1,\\-a u_{n_j}+y_{n_j},&\operatorname{sgn}(x_{n_j})=-1,\ \operatorname{sgn}(z_{n_j})=1.
\end{cases}\tag{8}
\]
Because \(w_{n_j+1}\to0\), equation (8) forces \(y_{n_j}\to0\). Hence \(p_{n_j}\to(0,0,0)\). Compactness of \(K\) and \(\operatorname{dist}(p_{n_j},K)\to0\) imply \((0,0,0)\in K\), a contradiction. Therefore there is an \(N_0\) after which assigned signs always agree.

By (1), for all \(n\ge N_0\) one has \(|w_{n+1}|=|a||w_n|\). If \(|a|\ge1\) and \(w_n\to0\), this forces \(w_{N_0}=0\). Consequently every point in the basin of \(K\) belongs to \(\bigcup_{n\ge0}T^{-n}(D)\).

**3. The exceptional preimage set is null.** In every open sign quadrant, the derivative of the original map is
\[
\begin{pmatrix}a s_x&s_z&0\\b&0&b\\0&s_x&a s_z\end{pmatrix}
\]
with determinant \(-2ab\), independent of \(s_x,s_z\in\{-1,1\}\). Each restriction is therefore an invertible affine transformation. The two switching planes already have three-dimensional Lebesgue measure zero. The preimage of any three-dimensional null set is contained in the switching planes together with the finitely many affine inverse images of that null set, hence is null. Since \(D\) is a plane and is null, induction shows that every \(T^{-n}(D)\) is null. The countable union is null, proving (3).

**4. Sharpness by an actual ambient sink.** For \(0<|a|<1\) and \(b\) satisfying (4), the denominator in (5) is strictly positive. Direct substitution shows that \(P_{a,b}\) is fixed. Since its diagonal coordinate is positive, the derivative is (7) with \(s=1\). The transverse multiplier is \(a\), while the tangent multipliers solve \(\lambda^2-a\lambda-2b=0\) and have maximum modulus
\[
\frac{|a|+\sqrt{a^2+8b}}2<1,
\]
where the last inequality is exactly \(b<(1-|a|)/2\). All multipliers have modulus below one; local smoothness near this positive fixed point gives a genuine ambient attracting neighborhood.

**5. Quantitative tube exit.** Along the reference orbit, until the first \(|w_j|\ge\delta\), the inequalities \(|w_j|<\delta\le|u_j|\) force the signs of \(u_j+w_j\) and \(u_j-w_j\) to agree with the reference sign. Equation (1) keeps \((u,y)\) on the reference orbit and multiplies \(|w|\) by \(|a|\) exactly. Iterating to the first threshold yields (6). No asymptotic approximation is used.

## Verification

The standalone script `check_transverse.py` verifies the affine branch determinants, the block factorization of characteristic polynomials on both same-sign quadrants, the exact center/normal formulas in all four sign quadrants, and rational finite-iterate identities for six nondegenerate parameter pairs. It passes 4,050 exact symbolic or rational checks. These calculations are **not** used as an exhaustive proof of the basin claim; that claim follows from the compactness contradiction and null-preimage induction above. Reproduce with Python 3 and SymPy using `python check_transverse.py`.

## Relationship to prior work

Lozi's 2023 paper [1,2] defines the three-dimensional map, identifies the symmetric invariant plane, writes its smooth-branch Jacobian, and reports full-dimensional multipliers at several diagonal **fixed points**. In particular, the extra multiplier \(-1.25\) at an exhibited fixed point is already in [1]; this specific fixed-point observation is **not** claimed as new. The contribution asserted here is the global ambient null-basin criterion (including the neutral case and switching-line intersections away from the origin), its sharpness in the transverse parameter, and the exact pre-switching separation clock. The normal-exponent identity is included as the explicit mechanism and is not claimed independently of the already published Jacobian. The source's numerical use of the term *thread attractor* motivates distinguishing attraction within \(D\) from attraction by a positive-volume set in \(\mathbb R^3\).

Earlier transverse-instability/riddled-basin studies [3] give the general conceptual context, but concern coupled logistic maps rather than this discontinuous three-dimensional Lozi family. Prior rigorous work on two-dimensional Lozi attractors [4] does not classify ambient transverse basin nullity for the symmetric three-dimensional model. No general claim that a positive normal Lyapunov exponent alone proves a null basin is made: assertion (3) uses an additional exact nonlinear sign law, compactness, and piecewise branch invertibility.

## Limitations

The null-basin conclusion does not address compact invariant sets that contain the origin, or arbitrary measurable invariant sets that are not compact. The sharpness construction establishes existence of a full-dimensional sink for suitable \(b\) below the barrier, not a complete classification of all \(b\). Positive transverse Lyapunov exponent by itself does not exclude intermittent behavior near the switching set. The ergodic exponent identity omits measures charging the switching line where the derivative may be undefined. No proof of existence of a particular chaotic invariant probability, no complete global attraction-basin classification, and no claim about small asymmetric parameter perturbations are supplied. The sign-changing boundary \(|a|=1\) is a normal-cocycle transition; its nonlinear global consequences outside the proven compact-set domain are left open. Historical priority beyond the inspected sources remains subject to independent assessment.

## References

[1] R. Lozi, *Coexistence of Thread and Sheet Chaotic Attractors for Three Dimensional Lozi Map*, publicly posted 11 May 2023, preprint v1, DOI `10.20944/preprints202305.0775.v1`; full author-posted text: https://www.preprints.org/manuscript/202305.0775.

[2] R. Lozi, *Coexistence of Thread and Sheet Chaotic Attractors for Three-Dimensional Lozi Map*, Dynamics 3 (2023), 315–344, DOI `10.3390/dynamics3020019`.

[3] Y. L. Maistrenko, V. L. Maistrenko, A. Popovich, and E. Mosekilde, *Transverse instability and riddled basins in a system of two coupled logistic maps*, Physical Review E 57 (1998), 2713, DOI `10.1103/PhysRevE.57.2713`.

[4] P. Kucharski, *Strange attractors for the family of orientation preserving Lozi maps*, Chaos 33 (2023), 113121, DOI `10.1063/5.0139893`.
