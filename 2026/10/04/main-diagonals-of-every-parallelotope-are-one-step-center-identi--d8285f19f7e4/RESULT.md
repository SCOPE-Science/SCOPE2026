# Main diagonals of every parallelotope are one-step center-identifying for the polarity process
## Finding
For the exact polarity process for the maximum-volume inscribed ellipsoid, let
\[
P=b+A[-1,1]^n,
\]
where \(n\ge 2\) and \(A\) is invertible. For every sign vector \(\sigma\in\{\pm1\}^n\) and every \(|t|<1\), start at
\[
x_0=b+tA\sigma.
\]
Then the next polarity center is exactly
\[
x_1=b.
\]
A second exact polarity iteration therefore returns the exact maximum-volume inscribed ellipsoid
\[
b+A B_2^n.
\]
Thus every main-diagonal start of every parallelotope reaches the exact MaxIE in at most two outer iterations, uniformly even when \(|t|\) is arbitrarily close to \(1\).

## Assumptions and scope
The claim concerns the exact process: each shifted-polar minimum-volume covering ellipsoid is solved exactly. The parallelotope is full dimensional, \(n\ge2\), and the start is an interior point on a main diagonal. No claim is made for general off-diagonal starts, inexact MinCE oracles, or finite-precision implementations.

By affine covariance it suffices to analyze the cube \(C=[-1,1]^n\), a start \(x=t\mathbf 1\), and \(|t|<1\). Signed-coordinate symmetries reduce every \(\sigma\) to \(\mathbf1\).

## Proof
For the shifted cube \(C-t\mathbf1\), the polar has vertices
\[
v_i^+=\frac{e_i}{1-t},\qquad v_i^-=-\frac{e_i}{1+t},\qquad i=1,\ldots,n.
\]
The dual MinCE objective used by the polarity process is invariant under coordinate permutations. Concavity permits averaging any optimizer over this symmetry group, so an optimizer may be taken with equal weights inside the positive and negative vertex orbits. Write their total masses as \(\alpha\) and \(1-\alpha\), and set \(y=2\alpha-1\in(-1,1)\).

For this symmetric weight vector, the determinant of the dual covariance, up to a positive factor independent of \(y\), is
\[
(1+t^2+2ty)^{n-1}(1-y^2).
\]
Its logarithm is strictly concave on \((-1,1)\). Its first-order equation reduces to
\[
(n+1)t y^2+(1+t^2)y-(n-1)t=0. \tag{1}
\]
Hence the relevant root is unique. For \(t\ne0\), it is
\[
y(t)=\frac{\sqrt{(1+t^2)^2+4(n^2-1)t^2}-(1+t^2)}{2(n+1)t},
\]
and \(y(0)=0\).

Using the dual notation of Sun, the MinCE center and covariance satisfy
\[
c=\frac{t+y}{n(1-t^2)}\mathbf1,
\]
while the covariance matrix \(S\) has eigenvalues
\[
s_\perp=\frac{1+t^2+2ty}{n(1-t^2)^2}
\]
on \(\mathbf1^\perp\), and
\[
s_\parallel=\frac{1-y^2}{n(1-t^2)^2}
\]
in the \(\mathbf1\) direction. Sun's dual relation gives \(Q=n^{-1}S^{-1}\). Therefore
\[
\tau=c^TQc=\frac{(t+y)^2}{n(1-y^2)},
\qquad
Qc=\frac{(1-t^2)(t+y)}{n(1-y^2)}\mathbf1.
\]
The published exact center map is \(K(x)=x-Qc/(1-\tau)\). Its scalar coordinate is consequently
\[
t_+=t-\frac{(1-t^2)(t+y)}{n(1-y^2)-(t+y)^2}.
\]
After multiplication by the positive denominator, its numerator is
\[
-\big((n+1)t y^2+(1+t^2)y-(n-1)t\big),
\]
which is zero by (1). Thus \(K(t\mathbf1)=0\).

At the cube center, the shifted polar is the cross-polytope \(\operatorname{conv}\{\pm e_i\}\). Signed-permutation symmetry and uniqueness force its MinCE to be \(B_2^n\); polarizing back again gives \(B_2^n\), the cube's MaxIE. Hence the second exact iteration returns the exact MaxIE.

Finally, for \(P=b+AC\) and \(x=b+Au\), shifted polarity obeys
\[
(P-x)^\circ=A^{-T}(C-u)^\circ.
\]
Minimum-volume covering ellipsoids commute with invertible linear maps, and polarity maps back covariantly. Therefore \(K_P(b+Au)=b+A K_C(u)\), which proves the stated result for every parallelotope and every main diagonal.

## Verification
The algebraic cancellation in the center update was expanded independently: the common numerator equals the negative of the first-order polynomial in (1). The bundled standard-library checker evaluates the unique root and the returned center for dimensions \(2,3,5,10\) and starts \(t=\pm0.1,\pm0.5,\pm0.9\), requiring both the stationarity residual and \(t_+\) to be below \(10^{-11}\). It also checks the closed-form root against the defining quadratic. These finite checks support the algebra but are not used as a proof of the all-dimensional statement.

## Relationship to prior work
Sun's 2026 paper defines the exact polarity process, derives the dual MinCE covariance representation and the center map \(K(x)=x-Q(x)c(x)/(1-\tau(x))\), and proves an instance-dependent global linear contraction of a potential gap. Its numerical experiments explicitly include boxes and skewed boxes, but the inspected full text does not state the main-diagonal finite-identification law above. The result here is a special exact trajectory classification inside that process, not a strengthening of Sun's global theorem.

Khachiyan and Todd introduced the corresponding polarity iteration in 1993 as Algorithm IC and asked whether its iterates converge to the maximal inscribed ellipsoid. Their full article gives the iteration but not the parallelotope main-diagonal finite-termination calculation. General MaxIE/MinCE polarity duality, including Gürtuna's semi-infinite-programming treatment, supplies background equivalences but does not by itself imply this two-step trajectory law.

## Limitations
Only starts on the \(2^{n-1}\) main diagonal lines are classified. The proof assumes exact MinCE solutions; an approximate inner solve destroys the exact cancellation and requires a separate stability analysis. No worst-case iteration bound for arbitrary starts is claimed. A residual originality risk remains that an older or less searchable special-case calculation may exist outside the inspected literature.

## References
1. K. Sun, *The Polarity Process for the Maximum-Volume Inscribed Ellipsoid Problem*, arXiv:2609.10888v1, 2026.
2. L. G. Khachiyan and M. J. Todd, *On the complexity of approximating the maximal inscribed ellipsoid for a polytope*, Mathematical Programming 61 (1993), 137-159. DOI:10.1007/BF01582144.
3. F. Gürtuna, *Duality of Ellipsoidal Approximations via Semi-Infinite Programming*, SIAM Journal on Optimization 20 (2009), 1421-1437. DOI:10.1137/080717973.
