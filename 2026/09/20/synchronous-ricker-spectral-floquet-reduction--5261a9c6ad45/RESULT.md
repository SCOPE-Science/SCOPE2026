# Spectral Floquet reduction for synchronous cycles in row-regular Ricker competition

## Statement

Consider the \(n\)-species Ricker competition map
\[
F_A(x)_i=x_i\exp\!\bigl(r-(Ax)_i\bigr),\qquad x\in\mathbb R_+^n,
\]
where \(r>0\), \(A\) is a real \(n\times n\) matrix, and
\[
A\mathbf 1=c\mathbf 1,\qquad c>0.
\]
For ecological competition one normally takes \(A\ge 0\); the linear-algebraic reduction below only uses the row-sum hypothesis.

The diagonal ray \(x=z\mathbf1\) is invariant. With \(w=cz\), its scalar dynamics are the standard Ricker map
\[
w^+=w e^{r-w}.
\]

Let \(w_0,\ldots,w_{p-1}>0\) be a \(p\)-periodic orbit of this scalar map, indexed cyclically, and put \(z_k=w_k/c\). Then
\[
z_k\mathbf1,\qquad k=0,\ldots,p-1,
\]
is a synchronous \(p\)-periodic orbit of \(F_A\).

### Theorem 1 — exact Floquet polynomial

The monodromy matrix of the synchronous cycle is
\[
D F_A^p(z_0\mathbf1)
=
P_p(A),
\qquad
P_p(\lambda)=\prod_{k=0}^{p-1}
\left(1-\frac{w_k}{c}\lambda\right).
\]
Consequently its Floquet multipliers, with algebraic multiplicity, are exactly
\[
\left\{
P_p(\lambda):\lambda\in\sigma(A)
\right\}.
\]

In particular, because \(c\in\sigma(A)\) with eigenvector \(\mathbf1\),
\[
P_p(c)=\prod_{k=0}^{p-1}(1-w_k),
\]
which is the ordinary scalar multiplier of the Ricker \(p\)-cycle. All transverse multipliers are obtained by evaluating the same polynomial on the remaining interaction eigenvalues.

Thus the synchronous cycle is locally exponentially stable whenever
\[
|P_p(\lambda)|<1
\quad\text{for every }\lambda\in\sigma(A),
\]
and is unstable whenever \(|P_p(\lambda)|>1\) for some \(\lambda\in\sigma(A)\). Unit-modulus multipliers require separate nonlinear analysis.

Equivalently, the interaction spectrum must lie in the polynomial lemniscate
\[
\mathcal S_p
=
\left\{\lambda\in\mathbb C:
\prod_{k=0}^{p-1}
\left|1-\frac{w_k}{c}\lambda\right|<1
\right\}.
\]

### Corollary 2 — a period-independent spectral obstruction

If \(A\) has a nonzero eigenvalue \(\lambda\) with
\[
\operatorname{Re}\lambda\le 0,
\]
then every positive synchronous periodic orbit is linearly unstable.

Indeed, for every \(t>0\),
\[
|1-t\lambda|^2
=
1-2t\operatorname{Re}\lambda+t^2|\lambda|^2>1
\]
when \(\lambda\ne0\) and \(\operatorname{Re}\lambda\le0\). Taking \(t=w_k/c>0\) shows \(|P_p(\lambda)|>1\).

Hence a necessary condition for a hyperbolically attracting positive synchronous cycle is that every interaction eigenvalue other than the row-sum eigenvalue \(c>0\) lie in the open right half-plane and avoid zero.

### Corollary 3 — uniform all-to-all competition

For
\[
A=(1-a)I+a\mathbf1\mathbf1^{\mathsf T},
\qquad a>0,
\]
the diagonal entries are \(1\), all off-diagonal entries are \(a\), and
\[
c=1+(n-1)a.
\]
The spectrum consists of \(c\) and the transverse eigenvalue \(1-a\) with multiplicity \(n-1\). Therefore
\[
M_{\parallel}
=
\prod_{k=0}^{p-1}(1-w_k),
\qquad
M_{\perp}
=
\prod_{k=0}^{p-1}
\left(
1-\frac{1-a}{1+(n-1)a}w_k
\right),
\]
with \(M_\perp\) repeated \(n-1\) times.

If \(a>1\), then every factor in \(M_\perp\) exceeds \(1\), so every positive synchronous periodic orbit is unstable.

If \(a=1\), all rows of \(A\) are identical and every component receives the same multiplicative factor. Hence every ratio \(x_i/x_j\) is invariant wherever it is defined. Nearby nonsynchronous rays cannot converge to the synchronous ray, so no positive synchronous periodic orbit is locally asymptotically stable.

Thus a locally asymptotically stable positive synchronous periodic orbit in this uniform competition family can occur only when
\[
0<a<1.
\]

### Corollary 4 — directed cyclic competition

Let
\[
A=I+aP_n,\qquad a>0,
\]
where \(P_n\) is the cyclic permutation matrix. Then \(c=1+a\) and
\[
\sigma(A)=
\{1+a e^{2\pi i k/n}:k=0,\ldots,n-1\}.
\]
Corollary 2 gives a topology-dependent obstruction:

- if \(n\) is even, \(a>1\) forces instability of every positive synchronous periodic orbit;
- if \(n\) is odd, \(a\ge \sec(\pi/n)\) forces instability of every positive synchronous periodic orbit.

At the odd-\(n\) threshold the critical interaction eigenvalues have zero real part but are nonzero, so the instability is strict.

## Proof of Theorem 1

At a synchronized point \(x=z_k\mathbf1\), row-regularity gives
\[
(Ax)_i=cz_k=w_k
\]
for every component. Differentiating
\[
F_A(x)_i=x_i e^{r-(Ax)_i}
\]
therefore yields
\[
J_k
=
D F_A(z_k\mathbf1)
=
e^{r-w_k}(I-z_kA).
\]
Along the scalar orbit,
\[
z_{k+1}=z_k e^{r-w_k},
\]
so
\[
J_k
=
\frac{z_{k+1}}{z_k}
\left(I-\frac{w_k}{c}A\right).
\]
The matrices \(I-(w_k/c)A\) are all polynomials in the same matrix \(A\), hence they commute. Multiplication around the \(p\)-cycle gives
\[
J_{p-1}\cdots J_0
=
\left(\prod_{k=0}^{p-1}\frac{z_{k+1}}{z_k}\right)
\prod_{k=0}^{p-1}
\left(I-\frac{w_k}{c}A\right).
\]
The scalar prefactor telescopes to \(z_p/z_0=1\), proving
\[
D F_A^p(z_0\mathbf1)=P_p(A).
\]
The spectral statement follows from the polynomial spectral-mapping theorem. For the row-sum eigenvalue,
\[
P_p(c)=\prod_k(1-w_k),
\]
and \(1-w_k\) is the derivative of \(w\mapsto we^{r-w}\) at \(w_k\), proving the longitudinal identity.

## A broader multiplicative identity

The commutation mechanism is not peculiar to the exponential response. For
\[
F_i(x)=x_iG((Ax)_i)
\]
with a differentiable common response \(G\) and \(A\mathbf1=c\mathbf1\), the synchronized scalar map is
\[
z^+=zG(cz).
\]
At a synchronous \(p\)-cycle \(z_k\mathbf1\),
\[
D F^p(z_0\mathbf1)
=
\prod_{k=0}^{p-1}
\left[
G(cz_k)I+z_kG'(cz_k)A
\right].
\]
Thus the full Floquet spectrum is again obtained by evaluating one explicit scalar polynomial in the interaction eigenvalues. The Ricker formula above is unusually simple because the factors \(G(cz_k)=e^{r-cz_k}=z_{k+1}/z_k\) telescope.

## Relation to prior literature

The result concerns a special invariant sector of a standard line of Ricker competition models rather than a new population model.

Jiang and Rogers (1987) studied the symmetric planar competition map and low-period bifurcations, so planar symmetric-cycle analysis is prior art. Luís, Elaydi and Oliveira (2011) gave a detailed two-species Ricker stability and bifurcation analysis and explicitly evaluated Jacobian products on exclusion cycles. Ackleh and Salceanu (2015) studied \(n\)-species Ricker exclusion and persistence and emphasized that coexistence need not converge to an interior equilibrium. Gyllenberg, Jiang, Niu and Yan (2019) classified substantial parts of three-species Ricker dynamics and exhibited higher-period and chaotic behavior numerically. Hou (2020) treated the broader class \(T_i(x)=x_iG_i((Ax)_i)\), with emphasis on global attraction and stability of fixed points.

Ryals and Sacker (2022) developed Lyapunov-exponent stability criteria for coupled almost-periodic Ricker maps and reported an \(N\)-dimensional extension under coupling constraints. Generic master-stability theory for discrete networks also gives the general principle that synchronization stability can be decomposed by network eigenmodes.

Against that background, the contribution claimed here is narrow: for row-regular multiplicative competition maps, the Jacobians along a synchronous orbit are commuting affine polynomials in the *competition matrix itself*. For autonomous Ricker competition this collapses the entire \(p\)-cycle monodromy to the explicit polynomial \(P_p(A)\), which in turn yields the closed-left-half-plane obstruction above for every positive period. In the sources inspected, this exact row-regular competition-matrix formula and its period-independent spectral obstruction were not located.

A 2024 survey of periodic evolutionary Ricker competition describes periodic higher-dimensional analysis as sparse and computationally difficult. The reduction here does not solve that broad problem: it applies only to the row-regular synchronous sector, but in that sector it removes the dimension-dependent Floquet product completely.

## Limitations

- The row-sum condition \(A\mathbf1=c\mathbf1\) and a common intrinsic growth parameter are essential for the stated synchronous reduction.
- The theorem is local. It does not prove existence of a scalar \(p\)-cycle, global attraction, persistence of species, or absence of nonsynchronous attractors.
- A multiplier on the unit circle is not classified by the linear criterion. The \(a=1\) uniform-competition case is handled separately by exact ratio invariance.
- The planar symmetric literature already contains detailed low-period analysis; the claimed contribution is the arbitrary-dimension row-regular spectral reduction and the resulting general obstruction, not the existence of synchronous cycles or the general idea of eigenmode stability.
- Originality is to the best of our knowledge. The closest unresolved overlap risks are older planar symmetric-cycle work and the \(N\)-dimensional almost-periodic coupling result of Ryals and Sacker (2022); the latter's complete theorem text was not available for inspection in the source consulted.
- The 2019 accepted manuscript on multi-species carrying-simplex dynamics was checked through its abstract and indexed excerpts but not in complete theorem-level text.

## References

1. H. Jiang and T. D. Rogers, “The discrete dynamics of symmetric competition in the plane,” *Journal of Mathematical Biology* 25 (1987), 573–596. https://doi.org/10.1007/BF00275495
2. R. Luís, S. Elaydi and H. Oliveira, “Stability of a Ricker-type competition model and the competitive exclusion principle,” *Journal of Biological Dynamics* 5 (2011), 636–660. https://doi.org/10.1080/17513758.2011.581764
3. A. S. Ackleh and P. L. Salceanu, “Competitive exclusion and coexistence in an n-species Ricker model,” *Journal of Biological Dynamics* 9 (2015), 321–331. https://doi.org/10.1080/17513758.2015.1020576
4. M. Gyllenberg, J. Jiang, L. Niu and P. Yan, “On the dynamics of multi-species Ricker models admitting a carrying simplex,” *Journal of Difference Equations and Applications* 25 (2019), 1489–1530. https://doi.org/10.1080/10236198.2019.1663182
5. Z. Hou, “Geometric method for global stability of discrete population models,” *Discrete and Continuous Dynamical Systems - B* 25 (2020), 3305–3334. https://doi.org/10.3934/dcdsb.2020063
6. B. Ryals and R. J. Sacker, “Bifurcation in the almost periodic 2D Ricker map,” *Discrete and Continuous Dynamical Systems - B* 27 (2022), 1263–1284. https://doi.org/10.3934/dcdsb.2021089
7. R. Ramasamy and coauthors, “Synchronizability of Discrete Nonlinear Systems: A Master Stability Function Approach,” *Complexity* (2023), Article 6616560. https://doi.org/10.1155/2023/6616560
8. R. Luís, “Open Problems and Conjectures in the Evolutionary Periodic Ricker Competition Model,” *Axioms* 13 (2024), 246. https://doi.org/10.3390/axioms13040246
