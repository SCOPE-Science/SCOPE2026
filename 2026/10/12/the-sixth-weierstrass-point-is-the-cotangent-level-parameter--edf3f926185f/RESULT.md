# The sixth Weierstrass point is the cotangent-level parameter
## Finding
Let \(X\subset \mathbf P^4_{\mathbb C}\) be a smooth degree-four del Pezzo surface. Its pencil of containing quadrics has five singular parameters \(b_1,\ldots,b_5\in\mathbf P^1\). For a nonzero cotangent level with projective direction \(e\notin\{b_1,\ldots,b_5\}\), let \(S_{\tilde e}\) be the Kim--Lee level surface and let \(C_e\to\mathbf P^1\) be the genus-two double cover branched at \(b_1,\ldots,b_5,e\).

Then the degree-eight K3 surface \(K_e\) associated to the level is the desingularized Kummer surface of \(\operatorname{Jac}(C_e)\), compatibly with the double-cover map to \(X\). In the notation of Kim--Lee Remark 3.12, the sixth Weierstrass parameter can therefore be chosen to be the level parameter itself:
\[
\bar e=e.
\]
Moreover the abelian compactification may be taken to be \(\operatorname{Jac}(C_e)\), and the sixteen missing points are precisely its two-torsion points:
\[
S_{\tilde e}\cong \operatorname{Jac}(C_e)\setminus \operatorname{Jac}(C_e)[2].
\]
This holds for every nondiscriminant direction, not only for a general one.

## Assumptions and scope
Everything is over \(\mathbb C\). The surface \(X\) is smooth, so the five discriminant points of the quadric pencil are distinct. The direction \(e\) is required to avoid those five points. A projective change of coordinate on the pencil allows all six points \(b_1,\ldots,b_5,e\) to lie in one affine chart; write them as \(\theta_1,\ldots,\theta_5,r\), with \(r\ne\theta_i\).

The statement concerns the Kim--Lee degree-eight K3 surface and the corresponding nonzero level surface. It does not make a claim about the five discriminant directions, where the level surfaces are reducible.

## Proof
Set
\[
P(t)=\prod_{i=1}^5(t-\theta_i),\qquad A_i=P'(\theta_i)^{-1}.
\]
In the normalized coordinates recalled by Kim--Lee, \(X\) is cut out by
\[
q_0=\sum_{i=1}^5 A_i y_i^2=0,\qquad q_1=\sum_{i=1}^5 \theta_iA_i y_i^2=0.
\]
The pencil member in direction \(r\) is
\[
q_r=rq_0-q_1=\sum_{i=1}^5 A_i(r-\theta_i)y_i^2.
\]
For \(x\in X\), the affine tangent space to the cone over \(X\) is defined by
\[
\sum_{i=1}^5A_i x_i z_i=0,\qquad 
\sum_{i=1}^5\theta_iA_i x_i z_i=0.
\]
The vector \(x\) is always in the radical of the restriction of \(q_r\) to this tangent space. A second radical vector must have the form
\[
z_i=x_i\frac{\alpha+\beta\theta_i}{r-\theta_i}.
\]
Define
\[
S_k=\sum_{i=1}^5\frac{\theta_i^kA_i x_i^2}{r-\theta_i}\qquad (k=0,1,2).
\]
The two tangent equations for \(z\) are
\[
\begin{pmatrix}S_0&S_1\\S_1&S_2\end{pmatrix}
\binom{\alpha}{\beta}=0.
\]
On \(X\), the elementary identities
\[
S_1=rS_0-q_0(x)=rS_0,
\qquad
S_2=rS_1-q_1(x)=r^2S_0
\]
show that this matrix equals
\[
S_0\begin{pmatrix}1&r\\r&r^2\end{pmatrix}.
\]
Thus \(q_r\) cuts the projective tangent plane in a double line exactly when
\[
B_r:\quad \sum_{i=1}^5\frac{A_i x_i^2}{r-\theta_i}=0.
\]
By the geometric description of Kim--Lee, this is exactly the branch divisor of \(K_e\to X\).

Now form the genus-two curve \(C_e\) branched at \(\theta_1,\ldots,\theta_5,r\), and put
\[
Q(t)=P(t)(t-r).
\]
Skorobogatov's intersection-of-three-quadrics model for the desingularized Kummer surface of \(\operatorname{Jac}(C_e)\) uses the six weights \(Q'(\theta_i)^{-1}\). For \(i\le5\),
\[
Q'(\theta_i)^{-1}=\frac{A_i}{\theta_i-r}.
\]
If its three equations are denoted by \(E_0,E_1,E_2\), then eliminating the sixth coordinate gives
\[
E_1-rE_0=q_0,
\qquad
E_2-rE_1=q_1.
\]
Hence projection away from the sixth coordinate maps this Kummer K3 surface two-to-one onto the same \(X\). Its branch divisor is obtained by setting the sixth coordinate to zero, and is
\[
\sum_{i=1}^5\frac{A_i x_i^2}{\theta_i-r}=0,
\]
which is exactly \(B_r\).

Therefore the Kim--Lee surface \(K_e\to X\) and the desingularized Kummer surface of \(\operatorname{Jac}(C_e)\to X\) are double covers with the same branch divisor. The Picard group of a smooth degree-four del Pezzo surface is torsion-free, so the square root of the branch line bundle is unique; over \(\mathbb C\), a scalar discrepancy in the branch section is absorbed by a square root. The two double covers are consequently isomorphic over \(X\).

Kim--Lee prove that every nondiscriminant \(K_e\) is smooth and of Kummer type and that contracting its sixteen distinguished \((-2)\)-curves gives the sixteen-node Kummer quotient. Under the identification above this quotient is \(\operatorname{Jac}(C_e)/\{\pm1\}\). The natural abelian double cover is therefore \(\operatorname{Jac}(C_e)\), with the sixteen preimages of the nodes equal to \(\operatorname{Jac}(C_e)[2]\). Removing them gives the claimed level surface.

## Verification
The standalone checker `verify.py` symbolically verifies the tangent identities, the two elimination identities in the six-branch-point Kummer model, equality of the two branch equations up to sign, and the count of sixteen two-torsion points. Its recorded output is `verification_output.txt`.

The remaining geometric inputs are published theorems: Kim--Lee identify the branch of \(K_e\to X\) through the double-line condition and prove smooth Kummer type for every nondiscriminant direction; Skorobogatov gives the three-quadric Kummer model. The proof above supplies the missing comparison of their parameters.

## Relationship to prior work
Kim--Lee, arXiv:2210.01317, Theorem 1.2 and Corollary 3.15, show that every nondiscriminant level is an abelian surface minus sixteen points and that every corresponding \(K_e\) is a degree-eight K3 surface of Kummer type. Their Remark 3.12 constructs a genus-two curve using the same five fixed branch points and an additional point \(\bar e\), but explicitly leaves open whether \(\bar e=e\). The calculation above resolves that parameter identification.

Skorobogatov, DOI:10.4171/LEM/56-1-3, Theorem 3.1, provides the classical three-quadric model of a desingularized genus-two Kummer surface used in the comparison.

Beauville--Etesse--Höring--Liu--Voisin, arXiv:2304.10919 and DOI:10.1112/mod.2024.3, later describe a general fiber using a hyperelliptic curve whose moving branch parameter is the fiber parameter. In dimension two this already covers the generic parameter identification. The finding here is the uniform statement for every nondiscriminant direction on every smooth degree-four del Pezzo surface, together with the direct branch-divisor proof and the exact identification of the omitted sixteen points.

## Limitations
No assertion is made for the five discriminant directions. The argument is over \(\mathbb C\) and uses the torsion-freeness of \(\operatorname{Pic}(X)\) and the standard Kummer quotient of a principally polarized genus-two Jacobian. It does not classify degenerations of \(C_e\) as \(e\) approaches a discriminant point.

A residual literature risk remains that the same all-directions comparison may appear in a later revision or under a different Kummer-coordinate formulation; the inspected arXiv version of Kim--Lee still states the parameter equality as unclear, and the closest later general treatment states its explicit Jacobian-fiber description generically.

## References
1. H. Kim and Y. Lee, *Lagrangian fibration structure on the cotangent bundle of a del Pezzo surface of degree 4*, arXiv:2210.01317.
2. A. Skorobogatov, *Del Pezzo surfaces of degree 4 and their relation to Kummer surfaces*, Enseign. Math. 56 (2010), 73--85, DOI:10.4171/LEM/56-1-3.
3. A. Beauville, F. Etesse, A. Höring, J. Liu, and C. Voisin, *Symmetric tensors on the intersection of two quadrics and Lagrangian fibration*, arXiv:2304.10919; DOI:10.1112/mod.2024.3.
