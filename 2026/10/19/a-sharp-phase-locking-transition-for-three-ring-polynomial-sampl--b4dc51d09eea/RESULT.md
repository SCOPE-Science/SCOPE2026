# A sharp phase-locking transition for three-ring polynomial sampling determinants

## Finding
For any integer \(n\ge2\), consider exactly \(n\) regular-polygon sampling nodes on each of three concentric circles whose radii form a geometric progression. In any finite-dimensional polynomial Hilbert space with positive orthogonal monomial norms, the determinant of the Gram matrix of the normalized evaluation vectors undergoes a **sharp angular phase-locking transition**, independent of the monomial weights.

Write the circle radii as \(r e^{-h},r,r e^h\) with \(r,h>0\), and put
\[
t=e^{nh},\qquad t_c=2+\sqrt3,\qquad \theta_*(t)=\begin{cases}
\arccos(-(t+t^{-1})/4),&1<t<t_c,\\
\pi,&t\ge t_c.
\end{cases}
\]
All maximum-determinant designs, modulo a common rotation and cyclic relabeling on each ring, have effective inner and outer ring phases \(\mp\theta_*(t)\), respectively, relative to the middle ring. For \(1<t<t_c\), there are exactly two conjugate configurations; for \(t\ge t_c\), they coalesce into a unique configuration in which the inner and outer polygons are aligned and the middle polygon is rotated by half a mesh interval.

The sharp cross-ring distance factor is
\[
L_*(t)=\begin{cases}
\frac{3\sqrt3}{4}(t+t^{-1})^2,&1<t\le2+\sqrt3,\\
\frac{(t+1)^3(t-1)}{t^2},&t\ge2+\sqrt3.
\end{cases}
\]
The formulas agree at the transition. When \(h\to0^+\), the optimal phases approach an equally interlaced three-ring configuration with an effective separation of \(2\pi/3\).

## Assumptions and scope
Let \(\mathcal P_{3n-1}\) be the space of complex polynomials of degree at most \(3n-1\). Fix positive numbers \(\beta_k=\|z^k\|^2>0\), for \(0\le k\le3n-1\), and use the inner product for which the monomials are orthogonal. Its diagonal reproducing kernel is
\[
K(s)=\sum_{k=0}^{3n-1}\frac{s^k}{\beta_k}\quad(s\ge0).
\]
For three arbitrary angles \(\alpha_-,\alpha_0,\alpha_+\), use the \(3n\) nodes
\[
\Lambda=\bigcup_{j\in\{-,0,+\}}
\{r_j\exp(i(\alpha_j+2\pi \ell/n)):\ell=0,\ldots,n-1\},
\]
where \(r_-=re^{-h},r_0=r,r_+=re^h\), and evaluate with vectors individually divided by \(\sqrt{K(|\lambda|^2)}\). The ring radii are distinct because \(h>0\). The square matrix of these evaluations has an invertible Gram matrix \(G\).

Set effective angles \(\phi=n(\alpha_--\alpha_0)\) and \(\psi=n(\alpha_+-\alpha_0)\) modulo \(2\pi\), and define
\[
L(\phi,\psi;t)=\left|t^{-1}e^{i\phi}-1\right|\,
\left|t e^{i\psi}-1\right|\,
\left|t e^{i\psi}-t^{-1}e^{i\phi}\right|.
\]
The **exact finite determinant** for every permissible design is
\[
\det G=
\frac{n^{3n}r^{3n(3n-1)}L(\phi,\psi;t)^{2n}}
{\left(\prod_{k=0}^{3n-1}\beta_k\right)
\left[K(r^2e^{-2h})K(r^2)K(r^2e^{2h})\right]^n}.
\]
All optimization statements refer **only** to rotating three prescribed regular polygons at fixed radii, not optimizing their radii or allowing nonregular nodes.

## Proof
**1. Determinant reduction.** In the orthonormal monomial basis \(z^k/\sqrt{\beta_k}\), the normalized evaluation matrix has entries \(\lambda_j^k/\sqrt{\beta_k K(|\lambda_j|^2)}\). Its squared determinant, equal to \(\det G\), is the Vandermonde product \(\prod_{i<j}|\lambda_i-\lambda_j|^2\) divided by \(\prod_k\beta_k\prod_jK(|\lambda_j|^2)\). The within-ring Vandermonde products are exactly \(n^n r_j^{n(n-1)}\). For distinct rings \(i,j\), the cross product is
\[
\prod_{a,b=0}^{n-1}|r_i e^{i\alpha_i}e^{2\pi ia/n}-r_j e^{i\alpha_j}e^{2\pi ib/n}|^2
=|r_i^n e^{in\alpha_i}-r_j^n e^{in\alpha_j}|^{2n},
\]
by the resultant of the monic binomials with these roots. Since \(r_-r_0r_+=r^3\), collecting the factors gives the displayed determinant. Its denominator is independent of rotation. Hence maximizing \(\det G\) is equivalent to maximizing \(L\).

**2. Reflection rigidity.** Put \(a=t^{-1}\in(0,1)\), \(U=1+a^2\), \(u=(\phi+\psi)/2\), and \(v=(\psi-\phi)/2\). The square of the product of the first two distances in \(L\), divided by \(t^2\), is
\[
\bigl(U-2a\cos(u-v)\bigr)\bigl(U-2a\cos(u+v)\bigr)
=U^2-4aU\cos u\cos v+4a^2(\cos^2u+\cos^2v-1).
\]
The third distance depends on \(\psi-\phi=2v\) only. For each fixed \(v\), the displayed expression is a **strictly convex quadratic in \(\cos u\)** because its quadratic coefficient is \(4a^2>0\). It is therefore maximized at \(\cos u=\pm1\), with no interior maximizers. Since every pairwise distance is positive for \(t>1\), the same conclusion holds for \(L\). Thus every global maximizer satisfies \(\phi+\psi\equiv0\pmod{2\pi}\).

**3. One-variable global maximum.** Write \(\phi=-\theta\), \(\psi=\theta\), and \(x=\cos\theta\in[-1,1]\). Direct multiplication gives
\[
L^2=t^4(U-2ax)^3(U+2ax).
\]
All factors are strictly positive. The logarithm of the angle-dependent factor is strictly concave, since
\[
\frac{d^2}{dx^2}\bigl[3\log(U-2ax)+\log(U+2ax)\bigr]
=-\frac{12a^2}{(U-2ax)^2}-\frac{4a^2}{(U+2ax)^2}<0.
\]
Its derivative vanishes precisely when \(x=-U/(4a)=-(t+t^{-1})/4\). For \(1<t<t_c\), this is in \((-1,1)\). At \(t=t_c\), it reaches \(-1\), because \(t+t^{-1}=4\); for larger \(t\), the maximum is attained at the endpoint \(x=-1\). Strict concavity yields uniqueness of the maximizing cosine, and the only remaining two choices of angle are the conjugate phases \(\pm\theta\) (which coincide at \(\theta=\pi\)).

**4. Exact value and transition.** At the interior maximum \(U-2ax=3U/2\) and \(U+2ax=U/2\), yielding \(L_*=(3\sqrt3/4)t^2U^2=(3\sqrt3/4)(t+t^{-1})^2\). At the endpoint \(x=-1\), one obtains \(L_*=t^2(1+a)^3(1-a)=(t+1)^3(t-1)/t^2\). This proves the complete optimal-angle classification, both determinant formulas, and the transition at \(nh=\log(2+\sqrt3)\).

## Verification
Run the independent numerical checker `check_three_ring.py` with Python, NumPy, and SciPy; `check_three_ring.out` records one actual execution. It checks the sharp three-point product against a two-angle numerical optimizer for ten values of \(t\), and separately constructs full normalized Fock evaluation Gram matrices of dimensions \(3n\), for \(n=1,2,3,4\), comparing their numerically computed log-determinants with the exact Vandermonde formula. A further collection of comparisons checks that a fixed equi-staggered phase is suboptimal when \(t>1\). These finite computations corroborate but do not establish the theorem for unbounded \(n\), arbitrary monomial norms, or every radius. Those conclusions follow from the algebraic proof above.

## Relationship to prior work
The polynomial reproducing-kernel sampling framework is developed in Gröchenig and Ortega-Cerdà's papers on Hardy/Bergman polynomial sampling (2020) and Fock polynomial sampling (2021). Their main results concern sampling families and uniform frame bounds, not the determinant optimum over the three prescribed regular polygons or its critical angular transition. A two-ring angular optimum follows from a single cross-ring resultant and has no competing pairwise interaction; it does not determine the three-ring optimum. The three-ring optimization reduces to the nontrivial competing product of three distances in the plane. Existing work on angular stability of single-orbit Szegő-kernel frames concerns one angular orbit rather than three concentric orbits. A hidden equivalent presentation in classical logarithmic-energy, Fekete-point, or resultant-maximization literature remains possible.

## Limitations
The optimality and uniqueness are restricted to three **regular** within-ring \(n\)-gons, whose three radii are fixed in a geometric progression; there is no assertion of optimality among arbitrary point placements or variable radii. Only the Gram determinant is optimized: the result does not assert simultaneous optimization of spectral condition number or lower frame bound. The phase transition is in the effective variable \(t=e^{nh}\); the critical physical logarithmic radial spacing is \(h_c=\log(2+\sqrt3)/n\). Independence from monomial norms requires that those norms be strictly positive, orthogonal, and rotationally invariant. The numerical checker is finite-dimensional evidence, not a universal proof. Literature comparison is best-knowledge, not a definitive novelty certificate.

## References
1. K. Gröchenig and J. Ortega-Cerdà, *Marcinkiewicz–Zygmund Inequalities for Polynomials in Bergmann and Hardy Spaces*, arXiv:2005.14176v1, initially posted 2020-05-28, https://arxiv.org/html/2005.14176v1.
2. K. Gröchenig and J. Ortega-Cerdà, *Marcinkiewicz–Zygmund Inequalities for Polynomials in Fock Space*, arXiv:2109.11825v1, initially posted 2021-09-24, https://arxiv.org/html/2109.11825v1.
