# Two-site rigidity and optimal placement for Hilbert stiffness of weighted cyclic sunlets

## Finding

For every integer \(n\ge4\), form a cyclic sunlet by attaching one private pendant leaf \(\ell_j\) to each vertex \(v_j\) of the unit-edge cycle \(C_n\). Initially all pendant edges have length \(t>0\). Include all \(2n\) vertices in the shortest-path metric. Define the centered Euclidean stiffness
\[
\gamma(d)=\min_{\substack{\alpha\in\mathbb R^{2n},\\ \sum_x\alpha_x=0,\\\|\alpha\|_2=1}}-\frac12\sum_{x,y}\alpha_x\alpha_y d(x,y).
\]
This is the least eigenvalue, on the zero-sum subspace, of the centered Schoenberg Gram matrix \(-\tfrac12 JDJ\), where \(D=[d(x,y)]\) and \(J=I-(2n)^{-1}\mathbf1\mathbf1^{\mathsf T}\). In particular it is not an \(\ell_1\)-normalized negative-type gap.

**Parity and exact baseline.** If \(n\) is even, \(\gamma=0\), and increasing any selection of pendant-edge lengths leaves \(\gamma=0\). If \(n\) is odd (thus \(n\ge5\)), put
\[
a=\frac1{4\cos^2(\pi/n)},\qquad
h=\sqrt{a^2+t^2},\qquad
q=\frac{a}{t+h}.
\]
Then
\[
\boxed{\gamma_n(t)=\frac{a+t-h}{2}=\frac{at}{a+t+h}>0.}
\]
The minimum-eigenvalue space has real dimension exactly two, consisting of the cosine and sine Fourier modes at frequency two on the core and proportional pendant coordinates.

**Sharp support threshold.** Increase the lengths of any chosen pendant edges, keeping all other lengths equal to \(t\). For odd \(n\), strengthening one edge by *any* amount leaves the stiffness exactly \(\gamma_n(t)\); strengthening any two distinct pendant edges by any strictly positive amounts makes the stiffness strictly larger than \(\gamma_n(t)\). More generally, for odd \(n\), the stiffness increases strictly if and only if at least two distinct pendant lengths strictly increase. For even \(n\), no collection of such increases can remove the zero stiffness.

**Exact two-site sensitivity and placement.** For odd \(n\), choose two distinct pendant sites \(0\) and \(d\), \(1\le d\le n-1\), and increase their lengths respectively by \(\varepsilon u\) and \(\varepsilon v\), with \(u,v>0\). Put
\[
\rho^2=\frac{2q^2}{n(1+q^2)},\qquad \theta=\frac{4\pi d}{n}.
\]
As \(\varepsilon\downarrow0\),
\[
\boxed{
\gamma(\varepsilon)-\gamma_n(t)
=\varepsilon\frac{\rho^2}{2}
\left(u+v-\sqrt{(u-v)^2+4uv\cos^2\theta}\right)
+O(\varepsilon^2).}
\]
For equal increments \(u=v=1\), this is \(\varepsilon\rho^2(1-|\cos(4\pi d/n)|)+O(\varepsilon^2)\). The optimal separation therefore satisfies
\[
\min_{1\le d<n}|\cos(4\pi d/n)|=\sin\frac{\pi}{2n},
\]
and the *largest* first-order gain per equal unit increment is precisely
\[
\boxed{\rho^2\left(1-\sin\frac\pi{2n}\right).}
\]
For a fixed total infinitesimal increment allocated to two sites, equal allocation and one of these optimal separations maximize the first-order increase.

## Assumptions and scope

The baseline cycle has \(n\ge4\) unit edges; each core vertex has exactly one leaf; all initial pendant lengths equal \(t>0\). Only *lengthening* pendant edges is considered, so paths between different core vertices remain cycle paths. The full graph metric includes the leaves and their attachment vertices. Stiffness always uses the canonical Euclidean \(\ell_2\)-normalization of the coefficients, not an edge-space, graph-Laplacian, or basepoint-dependent Gram normalization. The source metric is evaluated at negative-type exponent \(p=1\). The expansion for the perturbed stiffness is one-sided at zero and for fixed \(n,t,u,v,d\); the exact strict-increase result is global in the increment sizes.

## Proof

**1. Pendant cut identity.** Let \(c_j=\alpha_{v_j}\), \(z_j=\alpha_{\ell_j}\), and \(\beta_j=c_j+z_j\), so that \(\sum_j\beta_j=0\). For arbitrary positive pendant lengths \(t_j\), writing \(C\) for the \(n\)-by-\(n\) matrix of intrinsic cycle distances, direct expansion of shortest-path distances gives the *exact* quadratic identity
\[
\alpha^{\mathsf T}D\alpha=\beta^{\mathsf T}C\beta-2\sum_jt_jz_j^2.
\tag{1}
\]
Indeed, the extra \(t_j\) occurs in every distance from leaf \(\ell_j\) to another vertex and the coefficient sum vanishes; the diagonal leaf-to-itself term must be excluded, leaving \(-2t_jz_j^2\). Consequently, on the zero-sum subspace, increasing \(t_j\) by \(\delta_j\ge0\) adds exactly \(\sum_j\delta_jz_j^2\) to the Schoenberg quadratic form. This is a positive-semidefinite rank-one update for each strengthened leaf.

**2. Uniform Fourier decomposition.** At \(t_j=t\), for each nonconstant cycle character with cycle-distance eigenvalue \(\lambda_j\), equation (1) gives the distance quadratic-form matrix
\[
M(\lambda_j)=
\begin{pmatrix}\lambda_j&\lambda_j\\\lambda_j&\lambda_j-2t\end{pmatrix}
\]
on the normalized core and leaf character coordinates. The remaining constant-character zero-sum direction has distance Rayleigh eigenvalue \(-t\). For odd \(n\), the cycle-distance spectrum is strictly negative off the constant character, and its *largest* nonconstant eigenvalue is \(-a\), of real multiplicity two, at frequencies \(j=2,n-2\), where \(a=1/(4\cos^2(\pi/n))\); see the cycle-distance Fourier formula in Graovac–Jashari–Strunje. For even \(n\), all nonconstant cycle-distance eigenvalues are nonpositive and some vanish; every corresponding core-only Fourier vector is a zero-sum equality vector in (1).

The largest eigenvalue of \(M(\lambda)\) increases strictly with \(\lambda\le0\) whenever \(t>0\), because the dependence is the rank-one form \(\lambda(1,1)^{\mathsf T}(1,1)\), and its maximizing eigenvector has nonzero coordinate sum. For odd \(n\), the largest nonconstant distance Rayleigh eigenvalue therefore comes from \(\lambda=-a\) and equals
\[
\mu_+=-a-t+\sqrt{a^2+t^2}=-2\gamma_n(t).
\]
It exceeds \(-t\), the radial value. This proves the exact gap and the two-dimensional bottom eigenspace. A normalized real basis for this eigenspace has pendant coordinates at site \(j\) equal, up to common sign, to
\[
\sqrt{\rho^2}\cos(4\pi j/n),\qquad
\sqrt{\rho^2}\sin(4\pi j/n),
\]
where \(\rho^2=2q^2/[n(1+q^2)]\), \(q=a/(t+\sqrt{a^2+t^2})\). The factor follows by normalizing the core/leaf ratio \((1,-q)\) and using \(\sum_j\cos^2(4\pi j/n)=\sum_j\sin^2(4\pi j/n)=n/2\).

**3. Global one-site rigidity and two-site strictness.** The positive-semidefinite update from one strengthened leaf vanishes on the one-dimensional subspace of the bottom eigenspace whose pendant coordinate at that leaf is zero. Thus its minimum eigenvalue remains exactly \(\gamma_n(t)\), for arbitrarily large strengthening. With two distinct strengthened leaves at sites \(0,d\), a bottom eigenvector could have both pendant coordinates zero only if the real two-dimensional Fourier coefficients solve two linearly independent equations. Their determinant is \(\sin(4\pi d/n)\), nonzero for odd \(n\) and \(1\le d<n\). Therefore no bottom eigenvector annihilates both increments; positive-semidefinite monotonicity and the finite-dimensional Rayleigh minimum imply the new stiffness is strictly larger. Additional strengthenings preserve strictness. For even \(n\), a core-only zero mode persists and is annihilated by every pendant update, proving the parity statement.

**4. Sharp first-order design.** The bottom eigenvalue of the unperturbed odd-sunlet Gram matrix is isolated from the rest of its spectrum but has multiplicity two. Finite-dimensional symmetric perturbation theory, or the min–max principle with the orthogonal complementary spectral gap, shows that the first-order shifts are the eigenvalues of the perturbation restricted to that two-dimensional eigenspace (the remainder is \(O(\varepsilon^2)\)). The restricted matrix is
\[
\rho^2\left[u\binom10(1,0)+v\binom{\cos\theta}{\sin\theta}(\cos\theta,\sin\theta)\right].
\]
Its smaller eigenvalue is exactly the coefficient displayed above. For fixed \(u+v\), this coefficient is maximized by maximizing \(uv\) (equal allocation) and minimizing \(|\cos\theta|\). For odd \(n\), the residues \(2d\pmod n\) run through all nonzero residues; the closest available angles to an odd multiple of \(\pi/2\) are at angular deviation \(\pi/(2n)\). Hence \(\min_d|\cos(4\pi d/n)|=\sin(\pi/(2n))\), proving the sharp placement law.

## Verification

Run `python3 verify_two_site_sunlet.py` with the NumPy dependency specified in `requirements.txt`. The standalone checker uses exact rational arithmetic for 32 nonuniform pendant-cut identities; direct centered-matrix eigenspectra for 1,350 one- versus two-site configurations; and 168 finite-difference checks of the first-order formula, including the optimal angular separation. It prints `ALL_CYCLIC_TWO_SITE_STIFFNESS_CHECKS_OK`. These finite computations corroborate, but do not replace, the all-parameter proof.

## Relationship to prior work

The 1985 cycle-distance spectrum of Graovac, Jashari and Strunje supplies the Fourier input. Indulal and Stevanović (2015) obtained an exact *unweighted, symmetric* corona distance spectrum, including cycles with uniform unit pendant edges. Wolf's finite-metric negative-type gap work treats an \(\ell_1\)-normalized gap and examples including cycles; it does not give the present centered \(\ell_2\) sensitivity or a two-site reinforcement law. Irawan and Sugeng (2021) evaluate quadratic embedding constants for *other* bearded-cycle and broken-sun families, with all graph edge lengths equal to one. The uniform-wheel QE calculations of Obata and of Lou–Obata–Huang concern a different graph operation and do not cover asymmetrically lengthened sunlet pendants. The uniform baseline is an input rather than a separate originality claim. The asserted new content is the global one-/two-site strengthening threshold and exact optimal first-order design for the nonuniform metrics; it is not a restatement of a distance spectrum for a uniform corona. Unindexed or differently formulated spectral-perturbation literature may contain related or equivalent results.

## Limitations

The proof assumes equal initial pendant lengths and only nonnegative pendant-length changes. The global strictness theorem does not give a closed formula for the finite-increment stiffness with two or more unequal lengths. The spacing optimum is specifically *first-order* as the total increment tends to zero; finite-budget global optimality is not asserted. The centered \(\ell_2\) stiffness differs from the customary \(\ell_1\) negative-type gap. The result does not classify powered metrics with \(p\ne1\), arbitrary weighted cycle cores, or other corona attachments.

## References

1. A. Graovac, G. Jashari and M. Strunje, *On the distance spectrum of a cycle*, Aplikace matematiky 30 (1985), 286–290, DOI: 10.21136/AM.1985.104151.
2. I. Doust and A. Weston, *Enhanced negative type for finite metric trees*, arXiv:0705.0411v1 (public 2007-05-03), §1 and finite-gap discussion.
3. R. Wolf, *On the gap of finite metric spaces of p-negative type*, arXiv:1008.0964v1 (2010), §1 and finite-cycle discussion.
4. G. Indulal and D. Stevanović, *The distance spectrum of corona and cluster of two graphs*, AKCE Int. J. Graphs Combin. 12 (2015), 186–192, DOI: 10.1016/j.akcej.2015.11.014, especially Theorem 1.
5. W. Irawan and K. A. Sugeng, *Quadratic embedding constants of hairy cycle graphs*, J. Phys.: Conf. Ser. 1722 (2021), 012046, DOI: 10.1088/1742-6596/1722/1/012046, especially §3.
6. Z. Lou, N. Obata and Q. Huang, *Quadratic Embedding Constants of Graph Joins*, arXiv:2001.06752 (2020), §3, including its account of wheel metrics.
