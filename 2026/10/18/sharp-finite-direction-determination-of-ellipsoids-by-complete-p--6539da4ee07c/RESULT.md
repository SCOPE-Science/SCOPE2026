# Sharp finite-direction determination of ellipsoids by complete parallel-section profiles

## Finding
For \(d\ge2\), consider the full class of translated nondegenerate ellipsoids in \(\mathbb R^d\), and assume that every measurement direction and every hyperplane offset is calibrated in one common coordinate system. For a unit vector \(u\), let
\[
A_{E,u}(t)=\mathcal H^{d-1}\bigl(E\cap\{x:\langle x,u\rangle=t\}\bigr),\qquad t\in\mathbb R.
\]
For a prescribed collection \(U=(u_1,\ldots,u_N)\) of unit directions, the data consist of the **entire functions** \(A_{E,u_i}\), not just central section areas. Let \(\operatorname{Sym}_d\) be the real vector space of symmetric \(d\)-by-\(d\) matrices.

**Sharp characterization.** The data uniquely determine **every** translated ellipsoid if and only if
\[
\boxed{\operatorname{span}\{u_i u_i^{\mathsf T}:1\le i\le N\}=\operatorname{Sym}_d.}
\]
Consequently, the exact minimum number of directional profiles for universal reconstruction is
\[
\boxed{N_{\min}=\frac{d(d+1)}2.}
\]
Almost every configuration of \(N_{\min}\) unit directions suffices. There is an explicit optimal configuration: all coordinate directions \(e_i\) and all bisectors \((e_i+e_j)/\sqrt2\) for \(1\le i<j\le d\).

The lower bound holds **even if the ellipsoid's total volume and center are known in advance**. More precisely, for **every** prescribed collection of fewer than \(d(d+1)/2\) directions, there exist two distinct origin-centered ellipsoids of exactly the same volume whose complete parallel-section profiles agree at all those directions.

For the explicit optimal configuration, write \(b_i\) for the midpoint of the support interval of \(A_{E,e_i}\) and \(s_i\) for its squared half-width. Write \(s_{ij}\) for the squared half-width of the profile in direction \((e_i+e_j)/\sqrt2\). If
\[
E=c+Q^{1/2}B_2^d,\quad Q\in\operatorname{Sym}_d\text{ positive definite},
\]
then reconstruction is exact and linear in these extracted measurements:
\[
\boxed{c_i=b_i,\quad Q_{ii}=s_i,\quad Q_{ij}=s_{ij}-\tfrac12(s_i+s_j)\ (i<j).}
\]
In particular, if the squared half-width measurements of two ellipsoids differ by at most \(\varepsilon\), entry by entry, and their coordinate midpoint measurements differ by at most \(\delta\), then
\[
\boxed{\|Q-Q'\|_{\max\mathrm{entry}}\le2\varepsilon,
\qquad \|c-c'\|_\infty\le\delta.}
\]
The stability estimate is for the explicit measured squared half-widths and midpoints, not for arbitrary noisy samples of the section-volume functions.

## Assumptions and scope
An ellipsoid is full-dimensional and represented by a center \(c\in\mathbb R^d\) and a symmetric positive definite shape matrix \(Q\). The unit normals and signed offsets are known; uncalibrated rotations, relabelings, and independently translated offset axes are **not** allowed. Data include zero values outside each section's support interval, so its endpoints are observable. The characterization is universal over all ellipsoids and all prescribed direction sets; it does not say that fewer directions fail at every particular ellipsoid, nor does it concern reconstruction of arbitrary convex bodies.

## Proof
**1. Exact section-function reduction.** Let \(\kappa_{d-1}\) denote the Euclidean volume of the unit ball in dimension \(d-1\). Every ellipsoid has the form \(E=c+Q^{1/2}B_2^d\), with \(Q\) symmetric positive definite. Put \(h_u^2=u^{\mathsf T}Qu\) and \(b_u=\langle u,c\rangle\). A linear change of variables applied to the ball's sections, or equivalently the one-dimensional marginal of uniform volume on the ellipsoid, gives
\[
\boxed{
A_{E,u}(t)=\frac{\kappa_{d-1}\sqrt{\det Q}}{h_u}
\left(1-\frac{(t-b_u)^2}{h_u^2}\right)_+^{(d-1)/2}.
}
\]
Here \(z_+=\max(z,0)\). The nonzero support interval is \([b_u-h_u,b_u+h_u]\). Thus its midpoint directly yields \(b_u\), its squared half-width yields the quadratic measurement \(u^{\mathsf T}Qu\), and its amplitude yields \(\det Q\). Conversely, these three quantities determine the entire directional section profile. In particular, two ellipsoids have identical prescribed complete profiles if and only if their measured center projections, their measured quadratic forms, and their determinants agree.

**2. Sufficiency and explicit reconstruction.** Define the linear measurement map
\[
\mathcal L_U:\operatorname{Sym}_d\longrightarrow\mathbb R^N,
\quad \mathcal L_U(Q)_i=u_i^{\mathsf T}Qu_i
=\operatorname{tr}(Q u_i u_i^{\mathsf T}).
\]
This map is injective exactly when the matrices \(u_i u_i^{\mathsf T}\) span \(\operatorname{Sym}_d\). In that case the direction vectors themselves necessarily span \(\mathbb R^d\): otherwise a rank-one matrix \(ww^{\mathsf T}\) for a common orthogonal vector \(w\ne0\) would lie in the kernel. Therefore the measured midpoints determine \(c\), while the squared half-widths determine \(Q\), establishing sufficiency. For \(e_i\) and \((e_i+e_j)/\sqrt2\), the quadratic measurements are respectively \(Q_{ii}\) and \((Q_{ii}+2Q_{ij}+Q_{jj})/2\), giving the explicit inverse and the displayed coefficientwise stability bounds. There are \(d+d(d-1)/2=d(d+1)/2\) views. Since the associated measurement determinant is nonzero, the failure set for arbitrary configurations with this many directions is a proper real-algebraic subset; its complement has full spherical-product measure and is open and dense.

**3. Why even knowing the volume cannot save a direction.** Assume \(N<d(d+1)/2\). The linear map \(\mathcal L_U\) has a nonzero symmetric kernel element. We show that some kernel element \(H\) is **indefinite**, regardless of the directions. If \(u_1,\ldots,u_N\) span \(\mathbb R^d\), any nonzero kernel element must be indefinite: a positive-semidefinite or negative-semidefinite matrix whose quadratic form vanishes on a spanning set is zero. If the directions do not span, select a nonzero vector \(w\) orthogonal to every direction and a vector \(v\) not parallel to \(w\). Then \(H=wv^{\mathsf T}+vw^{\mathsf T}\) belongs to the measurement kernel because \(u_i\cdot w=0\); its quadratic form takes both positive and negative values, so it is indefinite.

Fix such an indefinite \(H\). The matrix pencil \(Q(s)=I+sH\) is positive definite precisely for \(s\) in a bounded open interval \((a,b)\) containing zero. The determinant \(f(s)=\det(I+sH)\) is strictly positive inside the interval, extends continuously to the endpoints, and satisfies \(f(a)=f(b)=0\). Therefore for every level strictly between zero and the maximum of \(f\), the intermediate value theorem gives **two distinct** points \(s_1,s_2\in(a,b)\) with \(f(s_1)=f(s_2)\). Set \(Q_1=I+s_1H\), \(Q_2=I+s_2H\). These are distinct positive-definite matrices, have equal determinant, and satisfy
\[
 u_i^{\mathsf T}Q_1u_i=u_i^{\mathsf T}Q_2u_i=1
 \qquad(1\le i\le N),
\]
where the last equality uses unit directions. The two origin-centered ellipsoids determined by \(Q_1,Q_2\) therefore have equal volume, equal directional support intervals and equal full section functions at **every measured direction** by Step 1. This proves necessity and the stated strongest form of nonidentifiability.

## Verification
The standalone exact-arithmetic file `ellipsoid_check.py` reconstructs positive-definite integer-Gram perturbations in every dimension \(2\) through \(7\) using the explicit \(d(d+1)/2\) directions. It verifies 83 squared half-width measurements and recovers every shape coefficient and center coordinate exactly. It also constructs, in each dimension, a pair of distinct positive-definite matrices with identical determinants and identical quadratic data for the \(d(d+1)/2-1\) prescribed directions obtained by omitting one bisector. The test prints `VERIFY_OK`. These finite examples corroborate the construction; the arbitrary-direction minimality theorem follows from the indefinite-kernel proof above.

## Relationship to prior work
The 2026 study of Fish, Ryabogin, Sun, and Yaskin investigates identification and rigidity of convex bodies from parallel section functions with full angular information, and in particular characterizes ellipsoids by structural properties of those functions. The present theorem addresses a different finite-acquisition question restricted to the full ellipsoid family: exactly which *finite* directional configurations determine the body, and whether the extra determinant information contained in each complete profile permits fewer views than generic quadratic interpolation. The answer is negative even with volume known, and the full direction-set criterion, paired equal-volume counterexamples, and explicit stable reconstruction address that finite-acquisition gap. The equation of an ellipsoid as a quadratic form and its ordinary linear parameter count are classical, as is the fact that certain finite sets of quadratic samples recover symmetric matrices. Those standard ingredients are not claimed as new by themselves. Accessible published work concerning unlabeled random section moments and all-angle fixed-offset ellipsoid rigidity asks different measurement questions and does not imply this universal minimal labeled-direction classification.

## Limitations
A complete section profile along each direction is assumed to be available, with its support endpoints and absolute offset calibration. Conversion of noisy sampled functions to support endpoints is not addressed. The minimal-view result concerns ellipsoids and does not characterize arbitrary convex bodies. It gives a linear conditioning bound for one explicit view configuration but not the optimal condition number over all possible configurations. A closely equivalent formulation may exist in older quadratic-form measurement or geometric tomography literature not identified here; historical priority and independent validation remain unverified.

## References
1. A. Fish, D. Ryabogin, W. R. Sun, V. Yaskin, *On determination of convex bodies by their section functions*, arXiv:2610.10229 (first public version 2026-10-07), https://arxiv.org/abs/2610.10229.
2. R. J. Gardner, *Geometric Tomography*, 2nd edition, Cambridge University Press, 2006 (classical background on section functions and reconstruction).
3. R. Anwar et al., *Direct ellipsoidal fitting of discrete multi-dimensional data*, arXiv:1901.05511, https://arxiv.org/abs/1901.05511 (related algebraic reconstruction methods; the present sharp finite-section criterion is not inferred from this reference).
