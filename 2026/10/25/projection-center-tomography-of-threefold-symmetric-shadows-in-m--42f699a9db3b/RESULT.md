# Projection-center tomography of threefold-symmetric shadows in \(\mathbb R^3\)

## Finding

Let \(K\subset\mathbb R^3\) be a compact, full-dimensional convex body. Suppose that, for every unit vector \(n\in S^2\), the orthogonal projection of \(K\) onto \(n^\perp\) is invariant under an in-plane rotation through \(2\pi/3\) about a point \(c(n)\in n^\perp\). Each rotational center is unique; identify it with its ambient vector in \(\mathbb R^3\).

**Exact range and inversion.** The possible center fields are exactly the ten-dimensional vector space
\[
\mathcal C=\left\{n\longmapsto (I-nn^{\mathsf T})a-\frac14\nabla_{S^2}Y(n):\ a\in\mathbb R^3,\ Y\in\mathcal H_3(S^2)\right\},
\]
where \(\mathcal H_3(S^2)\) is the seven-dimensional space of real degree-three spherical harmonics. Every field in this range is realized by a smooth, strongly convex body satisfying the projection condition. The parameters can be recovered directly from the centers by
\[
a=\frac{3}{8\pi}\int_{S^2}c(n)\,d\sigma(n),\qquad
Y(n)=\frac13\operatorname{div}_{S^2}\left(c(n)-(I-nn^{\mathsf T})a\right).
\]
Every corresponding body has support function \(h_K(u)=R+a\cdot u+Y(u)\), with \(R>0\) equal to half its constant width. Thus the center field determines the body **up to its constant-width radius**: two bodies in this class have the same field exactly when their support functions differ by a constant, equivalently when one is a Euclidean outer parallel body of the other. In particular, all the planar rotational centers are the orthogonal projections of one fixed point if and only if the body is a ball.

The recovery is quantitatively orthogonal:
\[
\int_{S^2}\|c(n)\|^2\,d\sigma(n)
=\frac{8\pi}{3}\|a\|^2+\frac34\int_{S^2}|Y(n)|^2\,d\sigma(n).
\]
All integrals use the ordinary surface-area measure, normalized by \(\sigma(S^2)=4\pi\); the divergence and gradient use the standard round unit-sphere metric.

## Assumptions and scope

No differentiability of \(K\) or its support function is assumed in the forward direction. Rotation by \(2\pi/3\) means **at least** threefold rotational symmetry, so projected disks are included. A compact planar body with nonempty interior has at most one center for a fixed nonidentity rotational symmetry, and every projection here has nonempty interior. The vector \(c(n)\) lies in the linear plane \(n^\perp\); it is unchanged on replacing \(n\) by \(-n\). The class is Euclidean, not affine invariant. The constant \(R\) is not determined by the center field and must be supplied separately to recover a unique body.

## Proof

**1. Reduction to a harmonic cubic.** Let \(h\) be the continuous support function on \(S^2\). Its restriction to the great circle \(S^2\cap n^\perp\) is the support function of the corresponding planar projection. Translating a planar support function changes only Fourier modes \(\pm1\). Hence the assumed \(120^\circ\) rotational symmetry forces all its equatorial Fourier modes outside \(\{0,\pm1,\pm3,\pm6,\pm9,\ldots\}\) to vanish.

For completeness, the needed harmonic-separation argument is as follows. The continuous functions obeying these equatorial conditions form a uniformly closed rotation-invariant linear space; its closure in \(L^2(S^2)\) is a closed \(SO(3)\)-invariant space. Averaging rotations against the degree-\(\ell\) character shows that its spherical-harmonic projector preserves the space. A nonzero spherical harmonic of degree \(\ell\) has a nonzero Fourier coefficient of every frequency \(m\) with \(0\le |m|\le\ell\) and \(m\equiv\ell\pmod2\) on *some* great circle: the coefficient functional is nonzero on the standard degree-\(\ell\) associated Legendre harmonic, and irreducibility of the dual \(SO(3)\)-module makes its rotation orbit separating. These two ingredients are established as Lemmas 4.8 and 4.12 of the cited primary paper; the preceding argument describes their use and the critical nonvanishing input.

For even \(\ell\ge2\), the forbidden second Fourier mode excludes that whole harmonic degree. For odd \(\ell\ge5\), the forbidden fifth mode does likewise. Consequently \(h=R+a\cdot u+Y(u)\), where \(Y\in\mathcal H_3(S^2)\). The equality is pointwise since \(h\) is continuous. Conversely, every degree-three harmonic restricts to any great circle using only first and third Fourier modes, so removing its first mode leaves a threefold-symmetric planar support. Since \(Y\) is odd, \(h(u)+h(-u)=2R\), and the full-dimensionality of \(K\) implies \(R>0\).

**2. The exact center field.** Represent \(Y(u)=T(u,u,u)\) with \(T\) a real symmetric trace-free trilinear form. Fix \(n\) and an orthonormal basis \(e_1,e_2\) of \(P=n^\perp\). Write \(u(\theta)=e_1\cos\theta+e_2\sin\theta\). The center of a threefold-symmetric planar body equals the first Fourier coefficient of its support function, namely \(\pi^{-1}\int_0^{2\pi}h(u(\theta))u(\theta)\,d\theta\): translating by this coefficient removes the first mode, while the rotationally symmetric remainder has zero first mode and its center at the origin.

The circle fourth-moment identity is
\[
\frac1\pi\int_0^{2\pi}u_i u_j u_k u_l\,d\theta
=\frac14\left(\Pi_{ij}\Pi_{kl}+\Pi_{ik}\Pi_{jl}+\Pi_{il}\Pi_{jk}\right),\qquad \Pi=I-nn^{\mathsf T}.
\]
Contracting it with \(T\) gives the cubic contribution \(\tfrac34\Pi\sum_{j=1}^2 T(e_j,e_j,\cdot)\). Since \(T\) is trace-free, the sum equals \(-T(n,n,\cdot)\). Moreover \(\nabla_{S^2}Y(n)=3\Pi T(n,n,\cdot)\). The linear contribution is \(\Pi a\), so
\[
 c(n)=\Pi a-\frac34\Pi T(n,n,\cdot)
      =\Pi a-\frac14\nabla_{S^2}Y(n).
\]
In particular the center field is automatically smooth, even if the initial body was not assumed smooth.

**3. Inversion and orthogonal identity.** For every fixed vector \(a\), \(\int_{S^2}\Pi a\,d\sigma=(8\pi/3)a\). Also \(\int_{S^2}\nabla_{S^2}Y\,d\sigma=0\): componentwise spherical integration by parts reduces this to the orthogonality of degree-three and degree-one harmonics. Integrating the field formula therefore recovers \(a\). Set \(d=c-\Pi a\). Then \(d=-\tfrac14\nabla_{S^2}Y\) and the degree-three Laplace eigenvalue gives
\[
\operatorname{div}_{S^2}d=-\frac14\Delta_{S^2}Y=3Y.
\]
This recovers \(Y\) uniquely. Orthogonality of distinct spherical harmonic degrees and \(\int|\nabla Y|^2=12\int Y^2\) give the displayed exact norm identity; the linear-field norm is \(\int\|\Pi a\|^2=(8\pi/3)\|a\|^2\).

**4. Surjectivity, uniqueness and rigidity.** Given arbitrary \(a\in\mathbb R^3\) and \(Y\in\mathcal H_3(S^2)\), choose
\[
R>\max_{u\in S^2}\left\|\nabla_{S^2}^2Y(u)+Y(u)I_{T_uS^2}\right\|_{\mathrm{op}}.
\]
Then \(h(u)=R+a\cdot u+Y(u)\) has positive definite spherical curvature-radius tensor \(\nabla_{S^2}^2h+hI\). The standard support-function convexity criterion realizes it as a smooth strongly convex body; its projections have the stated threefold symmetry and center field. The inversion formulas prove that identical center fields imply identical \(a,Y\), with only \(R\) free. If a field is \(\Pi a\) for a fixed point \(a\), then its recovered cubic \(Y\) vanishes, so the body is a ball; the converse is immediate.

## Verification

The general result is analytic and does not rely on finite enumeration. The standalone algebraic script `checks.py` verifies the center coefficient for five trace-free cubic polynomials on three rationally framed planes (15 exact tests), checks five corresponding spherical-divergence identities, and tests the nontrivial example \(Y(u)=u_1u_2u_3\) on the plane with unit normal \(n=(0,1,1)/\sqrt2\), where the center displacement is \((-1/8,0,0)\). Run `python checks.py` with Python 3 and SymPy installed. The source's harmonic-separation lemma, the general fourth-moment identity and the support-function criterion are proved or explicitly reconstructed above; finite checks alone cannot certify their universal scope.

## Relationship to prior work

Myroshnychenko, Ryabogin and Saroglou (2026) prove spherical rigidity when all planar projections have at least fourfold rotational symmetry and exhibit nonball threefold-symmetric examples. Their harmonic-projection and nonvanishing lemmas supply the established classification machinery used in Step 1. Existing equatorial Fourier-energy criteria likewise imply that the relevant support functions have only degrees zero, one and three. **Neither harmonic classification nor the existence of cubic examples is asserted here as new.** The new subject is the precise range, invertibility, dimension and quadratic norm of the field of **rotational centers of projections**, including the characterization of its radius ambiguity and the coherent-center rigidity criterion. Searches located related exact curvature and brightness calculations for special cubic examples, but not a statement determining this entire center field or reconstructing the body from it.

## Limitations

The theorem assumes the threefold symmetry property for **every** two-plane; finitely many shadows do not satisfy its premise. The rotational-center field alone cannot recover the radius \(R\), and no optimal reconstruction estimate under measurement noise is claimed. The shape is reconstructed in the fixed Euclidean coordinate system. Possible equivalent results in less-indexed literature are a residual novelty risk.

## References

1. S. Myroshnychenko, D. Ryabogin and C. Saroglou, *On convex bodies with rotationally symmetric planar projections*, arXiv:2609.27192v1, first submitted 23 September 2026, https://arxiv.org/html/2609.27192v1 (particularly §§3–5, Lemmas 4.8 and 4.12, Proposition 5.1, Theorem 5.4).
2. R. Schneider, *Convex Bodies: The Brunn–Minkowski Theory*, 2nd ed., Cambridge University Press, 2014; standard support functions and the spherical curvature-radius criterion. The book is background, not evidence of a full-text inspection in this work.
