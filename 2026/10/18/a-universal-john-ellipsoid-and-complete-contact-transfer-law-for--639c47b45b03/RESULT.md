# A universal John ellipsoid and complete contact transfer law for affine free joins

## Finding

Let \(k\ge 2\), and let \(B_i\) be a compact, full-dimensional convex body of dimension \(d_i\ge1\). Embed the bodies in mutually skew affine subspaces and take their **affine free join** (not the origin-intersecting free sum). After an affine change of coordinates its points are exactly
\[
\mathcal J=\{(x_1,\ldots,x_k,t):\ t_i\ge0,\ \sum_{i=1}^k t_i=1,\ x_i\in t_i B_i\}.
\]
Write \(d=\sum_i d_i+k-1\) and \(N=d+1\). Affinely normalize the unique John ellipsoid of each \(B_i\) to the origin-centered unit Euclidean ball. Set
\[
\tau_i=\frac{d_i+1}{N},\qquad q_i=\frac{d_i(d_i+1)}{dN},\qquad
C=\frac{\operatorname{diag}(\tau)-\tau\tau^{\mathsf T}}{d}.
\]
Here \(C\) is positive definite on the \((k-1)\)-dimensional hyperplane \(H=\{u:\sum_i u_i=0\}\) and has kernel spanned by the all-ones vector. **The unique maximum-volume ellipsoid inside \(\mathcal J\)** is centered at \((0,\tau)\) and has covariance (shape) operator
\[
Q=\operatorname{diag}(q_1 I_{d_1},\ldots,q_k I_{d_k},C|_H).
\]
Thus the ellipsoid is \((0,\tau)+Q^{1/2}B_2^d\), where the indicated square root is on the intrinsic affine space. No central symmetry of the factors is assumed. Applying the inverse factor-affine normalizations gives the answer for the original bodies.

**Complete contact classification.** Let \(\mathcal T_i=\partial B_i\cap S^{d_i-1}\) be the contact set of the normalized factor's John ball. Every point of \(\partial\mathcal J\cap\partial E\), and no other point, is specified by one index \(i\) and one \(v\in\mathcal T_i\) as follows:
\[
 x_i=\frac{d_i}{d}v,\quad x_j=0\ (j\ne i),\qquad
 t_i=\frac{d_i}{d},\quad t_j=\frac{d_j+1}{d}\ (j\ne i).
\]
The factor index is unique, and a factor with finitely many contacts contributes exactly that many contacts to the join. If the factor unit ball contacts are a continuum, the same formula parametrizes the corresponding continuum of join contacts.

## Assumptions and scope

All factors have positive finite dimensions; \(k\ge2\). The join is in dimension \(d\), not in the lower dimension of a convex hull of origin-intersecting subspaces. The Euclidean metric used to display \(Q\) is the intrinsic direct-product metric **after** each factor is put in John position. Because maximum-volume inscribed ellipsoids are affine-covariant, the conclusion is independent of this choice. In the original factor coordinates, if \(J(B_i)=a_i+L_i B_2^{d_i}\), use the invertible affine mapping \(x_i=t_i a_i+L_i y_i\) and the unchanged barycentric coordinates \(t\) to recover the result.

## Proof

**1. Universal containment.** In John position \(B_2^{d_i}\subseteq B_i\), so every \(v\in B_i^\circ\) satisfies \(\|v\|_2\le1\). The factor constraint \(x_i\in t_i B_i\) is equivalent, for \(t_i\ge0\), to \(\langle v,x_i\rangle-t_i\le0\) for all \(v\in B_i^\circ\). On the asserted ellipsoid \(E\), the support maximum of this affine functional is
\[
-\tau_i+\sqrt{q_i\|v\|_2^2+C_{ii}}
\le -\tau_i+\sqrt{q_i+C_{ii}}=0,
\]
because the defining formulas imply \(q_i+C_{ii}=\tau_i^2\). Also \(t_i\ge\tau_i-\sqrt{C_{ii}}>0\) everywhere on \(E\), since \(q_i>0\). Thus \(E\subseteq\mathcal J\). Notice that this argument works for every supporting direction of **any** normalized convex factor, without a polyhedral assumption.

**2. Global optimality, not merely the largest centered inball.** By the classical John criterion for each \(B_i\), its contact set contains finitely many vectors \(v_{ij}\in\mathcal T_i\) with positive \(c_{ij}\) satisfying
\[
\sum_j c_{ij}v_{ij}=0,\quad
\sum_j c_{ij}v_{ij}v_{ij}^{\mathsf T}=I_{d_i},\quad
\sum_j c_{ij}=d_i.
\]
Let \(a_{ij}\) be the intrinsic linear functional with block \(i\) equal to \(v_{ij}\), all other fiber blocks zero, and barycentric component \(-e_i\) (restricted to \(H\)). Each inequality \(a_{ij}\cdot(x,t)\le0\) supports \(\mathcal J\). Its ellipsoid support equals zero, so the vector
\[
 u_{ij}=\frac{Q^{1/2}a_{ij}}{\tau_i}
\]
is a unit contact direction after mapping \(E\) to the Euclidean unit ball. Assign positive weights
\[
\lambda_{ij}=\frac{\tau_i^2}{q_i}c_{ij}.
\]
Then the factor first-moment identities imply \(\sum_{ij}\lambda_{ij}u_{ij}=0\); factor second moments and the barycentric identity
\[
 C\,\operatorname{diag}(\tau)^{-1}C=\frac{C}{d},
 \qquad dC^{1/2}\operatorname{diag}(\tau)^{-1}C^{1/2}=P_H
\]
(where \(P_H\) is orthogonal projection onto \(H\)) imply
\[
\sum_{ij}\lambda_{ij}u_{ij}u_{ij}^{\mathsf T}=I_d.
\]
All cross moments vanish because \(\sum_jc_{ij}v_{ij}=0\); on each fiber block the second-moment sum is \(I_{d_i}\). The asserted barycentric matrix identity follows directly by multiplying \(\operatorname{diag}(\tau)-\tau\tau^{\mathsf T}\) and using \(\sum_i\tau_i=1\); its restriction has positive rank \(k-1\). John's necessary-and-sufficient contact criterion therefore proves that \(E\) is the **unique unrestricted maximum-volume inscribed ellipsoid**.

**3. All boundary contacts.** Every \(t_i\) is strictly positive throughout \(E\). Hence a point of \(E\) on \(\partial\mathcal J\) lies on some factor support \(\langle v,x_i\rangle=t_i\), with \(v\in B_i^\circ\). Equality in Step 1 requires \(\|v\|_2=1\), and equality in Cauchy--Schwarz on the ellipsoid forces the unique point
\[
 (x,t)=(0,\tau)+\frac{Qa_i}{\tau_i}.
\]
Since \(v\in B_i^\circ\cap S^{d_i-1}\), the unit-ball contact point \(v\) belongs to \(\partial B_i\), so \(v\in\mathcal T_i\). Evaluating the displayed formula gives \(x_i=q_i v/\tau_i=(d_i/d)v\), \(x_j=0\) for \(j\ne i\), and
\[
t_i=\tau_i-C_{ii}/\tau_i=d_i/d,\qquad
t_j=\tau_j-C_{ji}/\tau_i=(d_j+1)/d\quad (j\ne i).
\]
Conversely every such factor contact makes its supporting inequality tight. The displayed barycentric coordinates determine \(i\) uniquely because the corresponding fiber coordinate \(x_i\) is nonzero, so the list has no hidden overlaps.

## Verification

The standalone `verify_free_join.py` reconstructs the proposed rational covariance matrix and a positive complete contact decomposition using cube factors (whose John contacts are signed coordinate vectors). It checks 360 dimension profiles with \(2\le k\le5\) and \(1\le d_i\le3\). For each profile it checks \(C\operatorname{diag}(\tau)^{-1}C=C/d\), \(q_i+C_{ii}=\tau_i^2\), positive coordinate margins, zero first moment, and the exact second-moment identity in the unnormalized affine coordinates; every test passes. These finite computations verify the formulas and provide reproducibility, while Step 2 proves the theorem for **all** admissible factors and dimensions.

## Relationship to prior work

John's classical contact-decomposition criterion provides the optimality certificate, but not the free-join ellipsoid's particular covariance, center, contact positions, or weights. Ivanov and Naszódi, *Functional John and Löwner conditions for pairs of log-concave functions* (first preprint 2022), give general functional John conditions; their Sections 1, 4 and 12 discuss optimality and the convex-body case, rather than the dimension-weighted free-join formula. Chen and Davis, *A Product Formula for the Normalized Volume of Free Sums of Lattice Polytopes* (first preprint 2017), treat the origin-intersecting free sum \(\operatorname{conv}((P,0)\cup(0,Q))\) and normalized lattice volume, neither the higher-dimensional skew affine free join nor its John ellipsoid. Other particular John ellipsoid formulas and affine free-join asymmetry results concern different families or invariants; these do not imply the universal contact-transfer law. This comparison is evidence of distinction, not a claim of an exhaustive proof of priority.

## Limitations

The claimed metric block formula is in factor John-normalized coordinates and must be transported affinely for arbitrary original embeddings. Only the **inscribed** maximum-volume ellipsoid is determined; no formula for the minimum-volume enclosing Löwner ellipsoid is claimed. General John existence and uniqueness are used as classical input. The complete contact classification does not assert that all factors have finitely many contacts. A previously unknown equivalent join theorem in older or differently named literature cannot be ruled out. Independent validation has not occurred.

## References

- Tianran Chen and Robert Davis, *A Product Formula for the Normalized Volume of Free Sums of Lattice Polytopes*, arXiv:1711.11130v1 (first public 2017-11-29), https://arxiv.org/html/1711.11130v2 .
- Grigory Ivanov and Márton Naszódi, *Functional John and Löwner conditions for pairs of log-concave functions*, arXiv:2212.11781v1 (first public 2022-12-22), https://arxiv.org/html/2212.11781v2 .
- F. John, *Extremum problems with inequalities as subsidiary conditions*, Studies and Essays Presented to R. Courant on His 60th Birthday (1948), classical contact characterization as recalled in the Ivanov–Naszódi introduction.
