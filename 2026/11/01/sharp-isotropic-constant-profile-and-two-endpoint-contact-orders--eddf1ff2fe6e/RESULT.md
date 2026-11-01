# Sharp isotropic-constant profile and two endpoint contact orders for apex-truncated simplices

## Finding
For every integer \(n\ge2\) and every \(0\le t<1\), define the full-dimensional convex body
\[
K_{n,t}=\{x\in\mathbb R^n:x_i\ge0\ (1\le i\le n),\quad t\le x_1+\cdots+x_n\le1\}.
\]
It removes a homothetic cap from one vertex of the standard simplex \(\Delta_n=K_{n,0}\). Let \(X\) be uniformly distributed by volume in \(K_{n,t}\), and let its affine-invariant isotropic constant be specified by
\[
L(K_{n,t})^{2n}=\frac{\det\operatorname{Cov}(X)}{\operatorname{Vol}_n(K_{n,t})^2}.
\]
Write
\[
a=1-t^n,\quad b=1-t^{n+1},\quad c=1-t^{n+2},\qquad
E=(n+1)^2ac-n(n+2)b^2.
\]
Then the **exact normalized isotropic profile** is
\[
\boxed{H_n(t):=\left(\frac{L(K_{n,t})}{L(\Delta_n)}\right)^{2n}
=\frac{c^{n-1}E}{a^{n+3}}.}
\]
For every \(n\ge2\), \(H_n(t)\) is **strictly decreasing** on \([0,1)\). Its endpoint behavior is sharp on both sides:
\[
\boxed{H_n(t)=1-(n-1)(n+2)t^n+O_n(t^{n+1})\quad(t\downarrow0),}
\]
\[
\boxed{H_n(1^-)=\frac{(n+1)^2(n+2)^n}{12n^{n+2}},\quad
\frac{H_n(t)}{H_n(1^-)}=1+\frac{(n-1)(n+3)}{30}(1-t)^2+O_n((1-t)^3).}
\]
In particular, the normalized profile has contact order exactly \(n\) at the simplex end but exactly two at the thinning frustum end, and \(\lim_{n\to\infty}H_n(1^-)=e^2/12\). The endpoint \(t=1\) is degenerate; \(H_n(1^-)\) denotes a one-sided limit, not an isotropic constant assigned to a lower-dimensional body.

## Assumptions and scope
The dimension \(n\) is an arbitrary integer at least two, the cap parameter is real with \(0\le t<1\), and the norm, volume, centroid, and covariance are Euclidean/Lebesgue ones in \(\mathbb R^n\). The body has volume \((1-t^n)/n!\); it is a simplex only at \(t=0\). All nondegenerate simplices and their corresponding one-vertex parallel truncations are affinely equivalent to these examples. The isotropic constant is unchanged by invertible affine maps. Its simplex baseline is
\[
\boxed{L(\Delta_n)^{2n}=\frac{(n!)^2}{(n+1)^{n+1}(n+2)^n}.}
\]
The theorem concerns the entire one-parameter family and its two endpoint limits, not arbitrary deformations of convex bodies. A strict global simplex inequality is known separately; it does not by itself imply the strict ordered profile or either coefficient.

## Proof
**1. Exact moments.** Let \(S=X_1+\cdots+X_n\). Slicing the simplex by \(S=s\) gives the density \(ns^{n-1}/a\), for \(t\le s\le1\). Conditional on \(S=s\), the barycentric vector \(Y=X/S\) is uniform on \(\{y_i\ge0:\sum y_i=1\}\), independently of \(S\); equivalently it has the Dirichlet law with all parameters equal to one. Therefore
\[
\mathbb E S=\frac{n}{n+1}\frac ba=:m_1,
\qquad \mathbb E S^2=\frac{n}{n+2}\frac ca=:m_2,
\]
\[
\mathbb E Y_i=\frac1n,\qquad
\mathbb E(Y_iY_j)=\frac{1+\mathbf1_{i=j}}{n(n+1)}.
\]
Thus \(\operatorname{Cov}(X)\) has diagonal entries \(2m_2/[n(n+1)]-m_1^2/n^2\) and off-diagonal entries \(m_2/[n(n+1)]-m_1^2/n^2\). Its \(n-1\) transverse eigenvalues and one axial eigenvalue are respectively
\[
\lambda_\perp=\frac{m_2}{n(n+1)}=\frac{c}{(n+1)(n+2)a},\qquad
\lambda_\parallel=\frac{m_2-m_1^2}{n}=\frac{E}{(n+1)^2(n+2)a^2}.
\]
Both are positive for \(t<1\), since \(S\) is nonconstant and the Dirichlet law is nondegenerate. Multiplying eigenvalues and dividing by the square of \(a/n!\) gives
\[
L(K_{n,t})^{2n}=\frac{(n!)^2 c^{n-1}E}{(n+1)^{n+1}(n+2)^n a^{n+3}},
\]
which proves the exact formula and the simplex normalization. As an algebraic check, \(E=b^2-(n+1)^2t^n(1-t)^2>0\) for \(0<t<1\): indeed \(b=(1-t)\sum_{j=0}^nt^j\), and strict arithmetic-geometric mean gives \(\sum_{j=0}^nt^j>(n+1)t^{n/2}\).

**2. A positive coefficient certificate.** Define the integer polynomials
\[
B_n(t)=(n-1)-(n+3)t+t^n(1+t)\big((n+1)^2(1-t)^2+4t\big)
-t^{2n+2}\big((n+3)-(n-1)t\big)
\]
and
\[
P_n(t)=\sum_{j=0}^{n-2}\alpha_{n,j}(t^j+t^{2n-3-j}),\qquad
\alpha_{n,j}=(n-1)\binom{j+5}{5}-(n+3)\binom{j+4}{5}
=\frac{5(n-1)-4j}{5}\binom{j+4}{4}.
\]
A coefficient identity, valid for **every** integer \(n\ge2\), is
\[
\boxed{B_n(t)=(1-t)^6P_n(t).}
\]
Here is a coefficient proof, avoiding any finite-dimensional experimental assumption. For \(j\ge0\), the generating series of the displayed \(\alpha_{n,j}\) is
\[
\sum_{j\ge0}\alpha_{n,j}t^j
=\frac{(n-1)-(n+3)t}{(1-t)^6}.
\]
Define the coefficients of \(P_n\) on \(0\le j\le2n-3\) by reflection about \((2n-3)/2\), as in the finite sum. Upon multiplication by \((1-t)^6\), their sixth differences vanish except at the initial and final positions and the four reflected central positions. The initial coefficients are \(n-1,-(n+3)\). Direct use of Pascal's identity gives
\[
\alpha_{n-1}=\alpha_{n-2},\quad
\alpha_{n-3}-\alpha_n=(n+1)^2,\quad
\alpha_{n-4}-\alpha_{n+1}-6(\alpha_{n-3}-\alpha_n)=4-(n+1)^2,
\]
where the binomial expressions are interpreted as zero for negative indices occurring when \(n=2,3\). Thus the four central coefficients, in positions \(n,n+1,n+2,n+3\), are \((n+1)^2,4-(n+1)^2,4-(n+1)^2,(n+1)^2\), and the final two coefficients, by palindromic reflection, are \(-(n+3),n-1\). These are precisely the coefficients of the stated sparse polynomial \(B_n\), establishing the identity. Since \(0\le j\le n-2\), one has \(5(n-1)-4j\ge n+3>0\), so every \(\alpha_{n,j}>0\), hence \(P_n(t)>0\) for \(0\le t\le1\).

**3. Strict monotonicity.** Differentiate \(H_n=c^{n-1}E/a^{n+3}\) and use \(a'=-nt^{n-1}\), \(c'=-(n+2)t^{n+1}\), along with the definition of \(E\). Elementary multiplication of the derivative numerator gives the exact identity
\[
\begin{aligned}
&(n-1)c'Ea+cE'a-(n+3)cEa'\\
&\hspace{12mm}=-n(n+2)t^{n-1}(1-t)B_n(t).
\end{aligned}
\]
Substituting the coefficient identity yields the explicit positive-factor derivative
\[
\boxed{H_n'(t)=-\frac{n(n+2)t^{n-1}(1-t)^7
(1-t^{n+2})^{n-2}}{(1-t^n)^{n+4}}\,P_n(t)<0}\qquad (0<t<1).
\]
Thus monotonicity is strict for every dimension and parameter and does not rely on the global simplex bound.

**4. Sharp asymptotics at the simplex.** Since \(a=1-t^n\), \(c=1+O_n(t^{n+2})\), and \(E=1-(n+1)^2t^n+O_n(t^{n+1})\), multiplication yields
\[
H_n(t)=1-\big((n+1)^2-(n+3)\big)t^n+O_n(t^{n+1})
=1-(n-1)(n+2)t^n+O_n(t^{n+1}).
\]
The leading coefficient is nonzero and positive in the deficit, so the contact order is exactly \(n\).

**5. Thin-frustum endpoint and its quadratic contact.** Put \(h=1-t\). The slice variable \(S\) is supported on \([1-h,1]\), and its normalized density tends uniformly after rescaling to the uniform law; hence \(\operatorname{Var}(S)=h^2/12+O_n(h^3)\), \(m_2\to1\), and \(\operatorname{Vol}_n(K_{n,t})=nh/n!+O_n(h^2)\). Using the covariance eigenvalues in step 1 gives
\[
H_n(1^-)=\frac{(n+1)^2(n+2)^n}{12n^{n+2}}.
\]
The hockey-stick binomial sum applied to \(\alpha_{n,j}\) gives
\[
P_n(1)=2\sum_{j=0}^{n-2}\alpha_{n,j}
=\frac{n(n-1)(n+1)^2(n+2)(n+3)}{180}.
\]
The derivative formula in step 3 consequently has the one-sided expansion
\[
\frac{H_n'(t)}{H_n(1^-)}
=-\frac{(n-1)(n+3)}{15}(1-t)+O_n((1-t)^2).
\]
Integrating from \(t\) to one proves the stated exact quadratic contact coefficient. The elementary limit \((1+2/n)^n\to e^2\) proves \(H_n(1^-)\to e^2/12\).

## Verification
The included standalone standard-library program `verify.py` reconstructs moments and covariance matrices with exact rational arithmetic and directly computes their determinants for dimensions two through eight. It independently evaluates the all-dimensional derivative-numerator and positive-polynomial identities as integer coefficient arrays for dimensions two through fifty, and tests strict decrease at ordered rational depths for dimensions two through twenty. It completes **558 exact checks** and prints `VERIFY_OK 558 exact checks`. In particular, the program uses no floating-point approximation to accept the polynomial certificates. These are reproducibility checks over bounded instances; the infinite-dimensional-parameter statements rest on the general algebraic and probabilistic derivations in the preceding proof.

## Relationship to prior work
*A sharp entropy bound and the simplex inequality for isotropic constants* (2026), Theorem 1.1, supplies the sharp universal upper bound, with equality only for simplices. That theorem implies \(H_n(t)<1\) for \(t>0\) but does **not** compare two positive truncation depths or determine the exact formula or sharp endpoint coefficients. The available complete manuscript was inspected for a truncation or frustum-specific result; none was found.

*Exact Godbersen mixed-volume profile for one-vertex simplex truncations* (2026) treats the **same family** and gives exact mixed volumes of \(K_{n,t}\) and \(-K_{n,t}\). Its fully inspected result does not involve the covariance determinant or the affine isotropic constant and cannot imply the present profile without a new moment calculation and the coefficient-positivity argument. *Universal Santaló and volume-product laws for homothetic frusta* (2026), likewise inspected, proves a different polar-volume-product monotonicity for frusta, not the isotropic-constant monotonicity here. Rademacher's earlier theorem concerns possible global maximizers, not values along this truncation path. Classical simplex-frustum volume integrations are compatible with the elementary volume formula used here but do not themselves supply the claimed isotropic profile.

## Limitations
The theorem does not assert monotonicity for arbitrary truncations, multiple vertex cuts, or other convex-body deformation paths. The \(n\)-th order small-cap deficit is sharp **within this explicitly parameterized family**, not a proposed universal stability exponent. The limiting value at \(t=1\) is a one-sided normalized full-dimensional limit, not a lower-dimensional isotropic constant. The historical-priority comparison remains provisional: a relevant but currently unindexed frustum-moment formula could conceivably imply part of the result.

## References
1. *A sharp entropy bound and the simplex inequality for isotropic constants*, preprint released 5 October 2026, Theorem 1.1 and Section 7.
2. *Exact Godbersen mixed-volume profile for one-vertex simplex truncations* (2026), the complete public result on the same vertex-truncation family.
3. *Universal Santaló and volume-product laws for homothetic frusta* (2026), Sections on polar-volume factorization and monotonicity.
4. L. Rademacher, *A simplicial polytope that maximizes the isotropic constant must be a simplex*, arXiv:1404.5662 (2014).
5. G. Varsi, *The multidimensional content of the frustum of the simplex*, Pacific Journal of Mathematics 46 (1973), 303–314; referenced only for background on frustum volumes.
