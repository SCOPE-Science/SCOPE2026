# A dimension-source critical window for catalytic lattice branching

## Finding
Consider continuous-time independent-coordinate simple symmetric walks on \(\mathbb Z^d\), each coordinate jumping to each nearest neighbor at rate one. A catalytic source at the origin has net mean reproduction intensity \(\beta>0\). Define \(G_d(\lambda)=\int_0^\infty e^{-\lambda t}p_t(0,0)\,dt\), and the critical intensity \(\beta_c(d)=1/G_d(0)\) for \(d\ge3\). For each fixed real \(s\), put \(\beta_d=2d-1+s/d\). Then
\[
\beta_c(d)=2d-1-\frac1d+O(d^{-2}).
\]
When \(s<-1\), the mean growth operator \(A_d+\beta_d\delta_0\langle\delta_0,\cdot\rangle\) has no positive eigenvalue for all sufficiently large \(d\). When \(s>-1\), it has exactly one positive eigenvalue \(\lambda_d\), satisfying
\[
\lim_{d\to\infty}d\lambda_d=s+1.
\]
The boundary \(s=-1\) is not classified here. A uniform resolvent expansion underlying these statements is, for \(u\ge0\) in any fixed compact set,
\[
2dG_d(u/d)=1+\frac1{2d}+\frac{3/4-u/2}{d^2}+O(d^{-3}).
\]

## Assumptions and scope
All dimensions \(d\) are integers at least three. The walk generator is \((A_df)(x)=\sum_{j=1}^d[f(x+e_j)+f(x-e_j)-2f(x)]\). The source is a rank-one positive perturbation, equivalent to the first-moment generator of branching with net source intensity \(\beta_d\); this is a first-moment spectral statement and not a law of large numbers for the random population. The asymptotic constants refer to the chosen per-oriented-edge jump rate one. The parameter \(s\) is fixed as \(d\to\infty\).

## Proof
**Rank-one criterion.** Let \(\lambda>0\). Since \(\lambda-A_d\) is invertible, the eigenvalue equation implies \(f=\beta f(0)(\lambda-A_d)^{-1}\delta_0\). Evaluating at zero gives the necessary and sufficient scalar equation \(\beta G_d(\lambda)=1\), with eigenvector the Green kernel. Since \(G_d(\lambda)\) is strictly decreasing from \(G_d(0)<\infty\) to zero in dimensions \(d\ge3\), there is a unique positive eigenvalue exactly when \(\beta>\beta_c(d)\); otherwise there is none.

**Uniform resolvent expansion.** Coordinate independence gives \(p_t(0,0)=[e^{-2t}I_0(2t)]^d\), where \(I_0(z)=\sum_{m\ge0}(z^2/4)^m/(m!)^2\). Substitution \(y=2dt\) yields
\[
2dG_d(u/d)=\int_0^\infty e^{-y-u y/(2d^2)}I_0(y/d)^d\,dy.
\]
For bounded nonnegative \(u\), Taylor expansion at zero gives \(\log I_0(z)=z^2/4+O(z^4)\), so for \(0\le y\le d^{1/8}\), with an integrable polynomial-weight remainder,
\[
e^{-u y/(2d^2)}I_0(y/d)^d
=1+\frac{y^2}{4d}+\frac{y^4/32-u y/2}{d^2}
+O\!\left(d^{-3}(y^4+y^6+y^8+u^2y^2)\right).
\]
For the complementary range \(d^{1/8}<y\le d\), \(I_0(z)\le e^{z^2/4}\) implies \(e^{-y}I_0(y/d)^d\le e^{-3y/4}\), giving a super-polynomial small tail. On \(y\ge d\), write \(y=dz\). The function \(k(z)=e^{-z}I_0(z)\) is strictly decreasing for positive \(z\), \(k(1)<1\), and \(\int_1^\infty k(z)^3\,dz<\infty\) because \(k(z)=O(z^{-1/2})\). Hence the tail is bounded by \(d k(1)^{d-3}\int_1^\infty k(z)^3\,dz\), exponentially small. The expansions and their uniform remainder may therefore be integrated. Exponential moments \(\int_0^\infty y^j e^{-y}\,dy=j!\) produce \(1+1/(2d)+(3/4-u/2)/d^2+O(d^{-3})\).

**Threshold and window.** Setting \(u=0\) and inverting \(G_d(0)\) gives \(\beta_c(d)=2d-1-d^{-1}+O(d^{-2})\). For \(\beta_d=2d-1+s/d\), uniformly on compact \(u\)-sets,
\[
\beta_d G_d(u/d)=1+\frac{s+1-u}{2d^2}+O(d^{-3}).
\]
For \(s<-1\), the value at \(u=0\) is less than one for large \(d\), so no positive eigenvalue exists. For \(s>-1\), the value at zero exceeds one. For every fixed \(0<\varepsilon<s+1\), the values at \(u=s+1-\varepsilon\) and \(u=s+1+\varepsilon\) lie strictly above and below one, respectively, for sufficiently large \(d\). Strict monotonicity brackets \(d\lambda_d\) between these values. Taking \(\varepsilon\downarrow0\) proves convergence. No inference is made about the unresolved equality window \(s=-1\).

## Verification
The standalone `verify.py` checks the Bessel coefficient integrations as exact fractions, verifies the resolvent-window multiplication symbolically, and independently evaluates finite-dimensional Green integrals numerically to test the asymptotic signs and convergence. These finite tests support, but do not replace, the analytic infinite-dimensional and large-d arguments. See `VERIFICATION.md` and `verification_output.txt`.

## Relationship to prior work
Yarovaya (2026, arXiv:2610.27129, Theorems 4 and 5) treats nested lattices and the high-source-intensity expansion with fixed dimension, and explicitly describes the fixed-dimension setting as conventional. The present assertion instead locates a double-scaling spectral birth threshold when both dimension and source strength grow, and identifies the critical \(d^{-1}\)-window in the source intensity. The fixed-dimension \(\beta\to\infty\) expansion is not uniform in this window. Earlier single-source branching literature establishes the resolvent eigenvalue criterion, which is used rather than claimed new. High-dimensional simple-walk return-probability asymptotics supply related background; the precise joint eigenvalue transition requires the shifted resolvent expansion.

## Limitations
The exact equality boundary \(s=-1\) requires an additional expansion term and is not settled. The result is for a unit-rate nearest-neighbor generator, a single catalytic source and the first-moment operator, not general branching laws or multiple sources. Existing high-dimensional Green-function literature may contain equivalent asymptotic ingredients; definitive historical priority requires additional external review. Numerical finite-dimensional tests cannot prove the asymptotic theorem.

## References
1. E. Yarovaya, *Supercritical Branching Random Walks on Nested Lattices*, arXiv:2610.27129 (first public October 19, 2026), https://arxiv.org/abs/2610.27129.
2. A. Rytova and E. Yarovaya, *Heavy-Tailed Branching Random Walks on Multidimensional Lattices. A Moment Approach*, arXiv:2001.08032 (2020), https://arxiv.org/abs/2001.08032.
3. S. A. Molchanov and E. B. Yarovaya, *Limit theorems for the Green function of the lattice Laplacian under large deviations of the random walk*, Izvestiya: Mathematics 76 (2012), 1190–1217, https://doi.org/10.1070/IM2012v076n06ABEH002621.
4. Standard modified Bessel integral identity \(p_t(0,0)=e^{-2t}I_0(2t)\) for the continuous-time one-dimensional simple walk.
