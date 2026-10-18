# Sharp labeled solid-angle tomography of orthogonal simplices in every dimension

## Finding
Fix any integer \(d\ge 2\), and consider the labeled orthogonal simplex
\[
S(a)=\operatorname{conv}\{0,a_1e_1,\ldots,a_de_d\},\qquad a_i>0.
\]
Let \(\Omega_i(a)\) denote the spherical solid angle at \(a_ie_i\), and write \(q_i(a)=\Omega_i(a)/|\mathbb S^{d-1}|\). The angle at the right vertex \(0\) is always \(2^{-d}|\mathbb S^{d-1}|\).

**Sharp finite tomography.** For every fixed omitted label \(k\in\{1,\ldots,d\}\), the \(d-1\) labeled readings \((q_i(a))_{i\ne k}\) determine the complete positive leg-length vector \(a\) up to a common positive factor. Every smaller set of labeled nonright vertex angles has a positive-dimensional local ambiguity, at every shape. In particular \(d-1\) is the exact minimum number of readings needed.

**Order and stability.** For any two labels, \(a_i>a_j\) holds if and only if \(q_i(a)<q_j(a)\). With the normalization \(a_d=1\) and any \(T>0\), if both normalized log-leg vectors lie in \([-T,T]^{d-1}\), then
\[
\big\|(\log a_i-\log b_i)_{i<d}\big\|_\infty
\le c_{d,T}^{-1}\big\|(q_i(a)-q_i(b))_{i<d}\big\|_\infty,
\]
where
\[
M=e^{2T},\quad p=2\big(\Phi(1)-\Phi(1/2)\big),\quad
c_{d,T}=\frac{p^{d-1}}{2^d M}\,\varphi((d-1)M)>0.
\]
Here \(\Phi\) and \(\varphi\) are the standard normal CDF and density. The inverse Lipschitz exponent \(1\) cannot be increased on any neighborhood of a shape. Relabeling gives the same assertion when a different leg is normalized and omitted.

## Assumptions and scope
Angles are \((d-1)\)-dimensional Hausdorff measures of the tangent-cone intersection with the Euclidean unit sphere, divided by the full sphere area. The edge directions \(e_i\) form a labeled orthonormal basis. The simplex is nondegenerate because all \(a_i\) are positive. Only similarity of *labeled orthogonal simplices*, not arbitrary simplex congruence or unlabeled reconstruction, is asserted. No measurements are assumed at the constant-angle orthogonal corner. The stability estimate compares two vectors whose same fixed omitted leg is normalized to one.

## Proof
**1. Exact Gaussian representation.** The tangent cone at \(a_ie_i\) consists, after translation, of directions \(x\in\mathbb R^d\) satisfying
\[
x_j\ge0\quad(j\ne i),\qquad \sum_{j=1}^d x_j/a_j\le0.
\]
A standard Gaussian vector has uniform direction on the sphere. If \(H_j\), for \(j\ne i\), are independent standard half-normal variables, Gaussian conditioning therefore gives the exact formula
\[
q_i(a)=2^{-(d-1)}\mathbb E\!\left[\Phi\!\left(-\sum_{j\ne i}\frac{a_i}{a_j}H_j\right)\right]. \tag{1}
\]
The orthogonal corner is the positive orthant and has probability \(2^{-d}\). Every other vertex has strictly smaller angle, since the argument of \(\Phi\) in (1) is strictly negative almost surely.

**2. Strict ordering.** Suppose \(a_i>a_k\). In (1), couple the half-normal variables for \(q_i\) and \(q_k\), matching the exceptional variables \(H_k\) and \(H_i\), respectively. For every other index \(j\), the coefficient \(a_i/a_j\) strictly exceeds \(a_k/a_j\); for the exceptional term \(a_i/a_k>a_k/a_i\). Thus the sum inside \(\Phi(-\cdot)\) for \(q_i\) is almost surely larger, so \(q_i<q_k\). Equality of leg lengths gives equality of readings by permutation symmetry. This proves the claimed strict order equivalence.

**3. Global uniqueness from any \(d-1\) readings.** Relabel the omitted index as \(d\) and scale to \(a_d=b_d=1\). Suppose \(q_i(a)=q_i(b)\) for all \(i<d\). Let \(\lambda_i=a_i/b_i\), with \(\lambda_d=1\). If \(\max_i\lambda_i>1\), choose a maximizing label \(i<d\). For every \(j\ne i\), \(a_i/a_j\ge b_i/b_j\), and the inequality is strict at \(j=d\). Coupling the same positive half-normal variables in (1) makes \(q_i(a)<q_i(b)\), contradiction. If no ratio exceeds one but some falls below one, choose a minimizing label \(i<d\) and reverse the comparison to derive \(q_i(a)>q_i(b)\), contradiction. Consequently all ratios are one. This establishes global injectivity without an unproved global inverse-function assumption.

**4. Differential structure and minimality.** Write \(t_i=\log a_i\) and fix \(t_d=0\). Differentiating (1) under the expectation is valid because the Gaussian density is bounded, half-normal moments are finite, and the coefficients vary smoothly on compact parameter sets. For \(i\ne j\), define
\[
w_{ij}(t)=2^{-(d-1)}\mathbb E\!\left[
\varphi(U_i)\,e^{t_i-t_j}H_j\right]>0,
\quad U_i=\sum_{k\ne i}e^{t_i-t_k}H_k.
\]
The Jacobian satisfies
\[
\frac{\partial q_i}{\partial t_i}=-\sum_{j\ne i}w_{ij},\qquad
\frac{\partial q_i}{\partial t_j}=w_{ij}\quad(j\ne i).
\tag{2}
\]
For any set \(I\) of measured nonright labels with \(|I|<d\), normalize an unmeasured label \(k\) to \(t_k=0\). The principal block \((\partial q_i/\partial t_j)_{i,j\in I}\) has strictly negative diagonal and positive off-diagonal entries, with strict row diagonal dominance because \(w_{ik}>0\). It is invertible. There are \(d-1-|I|\) additional independent log-leg parameters. The implicit-function theorem gives a local \((d-1-|I|)\)-dimensional family of distinct normalized leg vectors with all chosen readings identical. The orthogonal-corner angle contributes no parameter information. Hence any fewer than \(d-1\) nonright readings fail locally at *every* point.

**5. Explicit quantitative stability.** Assume \(a_d=b_d=1\) and each normalized log length lies in \([-T,T]\). Along their straight log interpolation every ratio \(e^{t_i-t_j}\) lies in \([M^{-1},M]\), where \(M=e^{2T}\). On the positive-probability event that every half-normal variable in (1) lies in \([1/2,1]\), each summand is bounded above by \(M\), the special \(j=d\) summand is at least \(1/(2M)\), and the event has probability \(p^{d-1}\). Since \(\varphi\) decreases on \([0,\infty)\),
\[
w_{id}(t)\ge\frac{p^{d-1}}{2^d M}\varphi((d-1)M)=c_{d,T}.
\]
Set \(\Delta_i=\log a_i-\log b_i\), \(\Delta_d=0\). Integrate (2) along the interpolation, obtaining
\[
q_i(a)-q_i(b)=-\sum_{j\ne i}\bar w_{ij}(\Delta_i-\Delta_j),\qquad \bar w_{ij}>0,\quad\bar w_{id}\ge c_{d,T}.
\]
Choose a measured index \(i<d\) with \(|\Delta_i|=\max_{j<d}|\Delta_j|\). Every difference \(\Delta_i-\Delta_j\) has the sign of \(\Delta_i\), and \(\Delta_i-\Delta_d=\Delta_i\). Therefore \(|q_i(a)-q_i(b)|\ge c_{d,T}|\Delta_i|\). This proves the inequality. At any fixed interior shape, (2) has a finite nonsingular Jacobian; along a nontrivial smooth parameter path the data change to first order. Hence an inverse bound with exponent strictly greater than one is impossible locally.

## Verification
The standalone `check.py` (NumPy and SciPy) evaluates (1) using deterministic half-normal quadrature. In dimension two it checks the exact arctangent formulas for right triangles. In dimension three it independently constructs tangent cones and evaluates their angles by the determinant/dot-product trihedral formula. It also checks the predicted derivative sign and strict diagonal dominance and reconstructs three sets of log-leg ratios numerically. These finite calculations test normalizations and identities; the all-dimensional injectivity, minimality, and stability statements follow from the analytic argument above, not from numerical enumeration.

## Relationship to prior work
Licht, *On solid angles and simplex shape measures* (arXiv:2610.05883v1, made public October 5, 2026) defines vertex solid angles, provides the Gaussian-cone representation, and proves bounds comparing the **minimum** solid angle to simplex shape quality. The Gaussian-cone representation itself is not claimed as novel. The present finite inverse-tomography theorem uses the entire labeled angle vector of the nonorthogonal vertices and obtains uniqueness from any \(d-1\) components, exact minimality, and a positive stability modulus. These conclusions are not asserted by Licht's inspected results. The older standard trirectangular tetrahedron formulas give leg-based volume/area metrics, not this inverse-angle classification.

A one-scalar optimization of the *minimum* vertex solid angle over orthogonal simplices, even with a known equal-leg maximizer and dimension asymptotics, does not imply injectivity of the \(d-1\)-component labeled angle map, its rank characterization, or the quantitative inverse estimate. The present statement deliberately does not reassert the prior extremal inequality. See also Liu and Joe (1994) for earlier relations between tetrahedral shape measures; historical priority beyond the inspected literature remains uncertain.

## Limitations
The claim applies only to labeled simplices with mutually orthogonal legs at one distinguished vertex. The inverse image of an arbitrary \((d-1)\)-tuple of real readings is not characterized. The explicit Lipschitz coefficient is guaranteed positive but is not claimed sharp. The minimum \(d-1\) measurements are measured exactly, and no finite-sample noise-model optimality is asserted. Older unindexed literature on special tetrahedral angles or orthant probabilities may contain an equivalent reconstruction argument; no claim of absolute historical priority or independent mathematical certification is made.

## References
1. Martin W. Licht, *On solid angles and simplex shape measures*, arXiv:2610.05883v1, 2026-10-05, https://arxiv.org/html/2610.05883v1 .
2. Anwei Liu and Barry Joe, *Relationship between tetrahedron shape measures*, BIT 34 (1994), 268–287; cited in Licht's reference [19].
3. Eric W. Weisstein, *Trirectangular Tetrahedron*, MathWorld, https://mathworld.wolfram.com/TrirectangularTetrahedron.html .
