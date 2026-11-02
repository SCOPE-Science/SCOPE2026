# An exceptional-point optimum for cyclic three-edge heat sweeps

## Finding

For the three-vertex triangle, update the three edges successively using exact, reversible continuous-time edge heat steps of a common duration \(t>0\). Although each individual step has **strictly positive real eigenvalues**, the completed edge sweep has complex conjugate nonstationary eigenvalues for short steps and negative real eigenvalues for sufficiently long steps. Its asymptotic convergence rate **per completed three-edge sweep** is uniquely optimal at the finite value

\[
t_*=\log(2+\sqrt3),\qquad r_* =e^{-2t_*}=7-4\sqrt3.
\]

The exact optimum is the exceptional-point rate

\[
\min_{t>0}\rho\bigl(T(t)-\Pi\bigr)
=(2-\sqrt3)^3=26-15\sqrt3=0.0192378864668\ldots,
\]

where \(\Pi=\frac13\boldsymbol1\boldsymbol1^{\mathsf T}\). At the optimum, the repeated nonstationary eigenvalue is negative and has a nontrivial Jordan block. By comparison, the fully equilibrated edge-update limit \(t\to\infty\) has rate \(1/8\), about \(6.50\) times larger. Thus making each reversible substep arbitrarily strong is not rate-optimal for the full ordered sweep.

## Assumptions and scope

Write \(e_1,e_2,e_3\) for the standard basis in \(\mathbb R^3\). For an unordered edge \(ij\), set \(L_{ij}=-(e_i-e_j)(e_i-e_j)^{\mathsf T}\) and

\[
E_{ij}(t)=\exp(tL_{ij})=I-\frac{1-e^{-2t}}2(e_i-e_j)(e_i-e_j)^{\mathsf T}.
\]

Each \(E_{ij}(t)\) is symmetric, doubly stochastic and positive definite for finite \(t>0\), and has spectrum \(\{1,1,e^{-2t}\}\). We define the **fixed ordered sweep**

\[
T(t)=E_{12}(t)E_{23}(t)E_{31}(t),
\qquad \Pi=\frac13\boldsymbol1\boldsymbol1^{\mathsf T}.
\]

The asymptotic rate is \(\rho(T(t)-\Pi)=\lim_{k\to\infty}\|(T(t)-\Pi)^k\|^{1/k}\), independent of matrix norm. This is an optimization **per sweep**; it is not a claim about total physical diffusion time, the best finite-time total-variation distance, or arbitrary edge orders/weights.

## Proof

Put \(r=e^{-2t}\in(0,1)\). Direct multiplication of the three edge matrices (or the exact-rational calculations in `verify.py`) gives \(T\boldsymbol1=\boldsymbol1\), \(\boldsymbol1^{\mathsf T}T=\boldsymbol1^{\mathsf T}\), and \(\det T=r^3\). Since the stationary eigenvalue is \(1\), the other two eigenvalues are exactly the roots of

\[
z^2-\tau(r)z+r^3=0,
\quad\tau(r)=-\frac{(1+r)(r^2-10r+1)}8.
\]

Their discriminant factors as

\[
\tau(r)^2-4r^3
=\frac{(1-r)^4(r^2-14r+1)}{64}.
\]

Within \(0<r<1\), the last factor changes sign only at \(r_*=7-4\sqrt3\). Thus for \(r_*<r<1\), the two nonstationary eigenvalues are conjugate nonreal numbers, whose common modulus is \(\sqrt{r^3}=r^{3/2}\). This quantity increases strictly with \(r\), so it decreases strictly as the heat-step duration \(t\) increases toward \(t_*\).

For \(0<r<r_*\), we have \(r^2-10r+1>0\): indeed it is decreasing on this interval and equals \(4r_*>0\) at its right endpoint. Hence \(\tau(r)<0\) and the two nonstationary eigenvalues are distinct negative reals. Consequently their maximal absolute value is

\[
F(r)=\frac{(1+r)(r^2-10r+1)
 +(1-r)^2\sqrt{r^2-14r+1}}{16}.
\]

Both nonnegative summands in the numerator are strictly decreasing in \(r\in[0,r_*)\). For the first one, differentiate to obtain \(3r^2-18r-9<0\). The second is a product of two positive strictly decreasing functions, since \(r^2-14r+1>0\) and its derivative \(2r-14<0\). Therefore \(F(r)\) decreases strictly with \(r\) and **increases** strictly with duration \(t\) beyond \(t_*\). Continuity at the double root proves that \(t_*\) uniquely minimizes the nonstationary spectral radius on all \(t>0\).

At \(r=r_*\), the repeated nonstationary root is \(\tau(r_*)/2=-26+15\sqrt3\), of modulus \((2-\sqrt3)^3\). It is *defective*: direct multiplication gives

\[
T_{12}(t)-T_{21}(t)=-\frac{(1-r)^2(1+r)}8\ne0.
\]

If the doubly stochastic matrix \(T(t_*)\) were diagonalizable with its two nonstationary eigenvalues equal to \(\lambda_*\), then it would equal \(\Pi+\lambda_*(I-\Pi)\) and thus be symmetric, a contradiction. A Jordan polynomial factor in finite powers does not alter their limiting spectral radius.

Finally, as \(r\downarrow0\) (equivalently, \(t\to\infty\)), the quadratic becomes \(z(z+1/8)\), yielding limiting rate \(1/8\). Every finite-duration edge step is reversible and has only positive eigenvalues; a product of two positive-definite symmetric factors likewise has positive real eigenvalues by similarity to a positive-definite symmetric matrix. Three factors are therefore necessary for the nonreal/negative spectrum in this positive-definite setting.

## Verification

Run `python3 verify.py` with the standard library. It reconstructs each edge step and the ordered product using exact rational arithmetic at 24 parameter values and checks stochastic row/column sums, determinant, the nonstationary trace polynomial, the factored discriminant, the nonsymmetry identity, and strict entrywise positivity in the interior. It also checks numerical parameter boundaries and 11 off-optimum rate comparisons. Expected output: `VERIFY_OK rational_sweeps=24 phase_boundaries=3 rate_tests=11`. The proof above, not the finite tests, establishes all-parameter signs, optimality and defectiveness.

## Relationship to prior work

Ordered reversible updates and systematic-versus-random scan methods are established topics; see Backlund et al. (2018 first public version) and Shimizu--Shiraga (2021 first public version). Dyer--Greenhill--Ullrich prove nonnegative spectra for **convex combinations** of idempotent heat-bath steps, which does not cover ordered products. These works do not, in the portions inspected, establish the full one-parameter spectral discriminant or the globally sharp edge-sweep optimum stated here. This is a qualified literature comparison, not a claim that nonreversibility of systematic scans, products of projections, or polynomial spectral calculations were first discovered here.

## Limitations

Only the uniform-rate three-state triangle, three edges in a fixed cyclic order, exact continuous-time edge heat factors, identical positive durations, and the **asymptotic spectral radius per full sweep** are covered. Defectiveness at the optimum means that finite-sweep transient decay need not be bounded by a pure geometric term with the optimal spectral factor and a uniform constant. The theorem does not assert fastest convergence under a fixed physical-time budget or among arbitrary positive Markov kernels, and publication priority remains subject to specialist comparison with older cyclic-projection and relaxation literature.

## References

1. G. Backlund, J. P. Hobert, Y. J. Jung, and K. Khare, *A Hybrid Scan Gibbs Sampler for Bayesian Models with Latent Variables*, arXiv:1808.09047 (first public preprint 2018-08-27). https://arxiv.org/abs/1808.09047
2. N. Shimizu and T. Shiraga, *Reversible Random Walks on Dynamic Graphs*, arXiv:2102.08002 (first public preprint 2021-02-16). https://arxiv.org/abs/2102.08002
3. M. Dyer, C. Greenhill, and M. Ullrich, *Structure and eigenvalues of heat-bath Markov chains*, arXiv:1301.4055 (supporting, older literature). https://arxiv.org/abs/1301.4055
4. Y. Censor, T. Elfving, G. T. Herman, and T. Nikazad, *On Diagonally Relaxed Orthogonal Projection Methods*, SIAM J. Sci. Comput. 30 (2008), 473--504, doi:10.1137/050639399 (abstract inspected; specialist coverage risk). https://doi.org/10.1137/050639399
