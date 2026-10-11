# Joint chi-square face-vector fluctuations of random central regular-simplex sections

## Finding

For each integer \(N\ge4\), take a regular Euclidean simplex \(S_N\) with \(N\) vertices, of dimension \(N-1\). Let \(H_N\) be a Haar-uniform hyperplane through its centroid within its affine span, and put \(Q_N=S_N\cap H_N\). For \(0\le j\le N-3\), write \(f_j(Q_N)\) for its number of \(j\)-faces. Put \(r=j+2\) and define the deterministic maximal possible count
\[
B_{N,j}=\binom N r-\binom{\lfloor N/2\rfloor}r-\binom{\lceil N/2\rceil}r,
\qquad \Delta_{N,j}=B_{N,j}-f_j(Q_N).
\]
All binomial coefficients with an upper integer smaller than the lower one are zero. Then each \(\Delta_{N,j}\) is nonnegative. More strongly, if \(X_1,\ldots,X_N\) are independent standard Gaussian variables, \(\bar X=N^{-1}\sum_iX_i\), and \(K_N=\#\{i:X_i>\bar X\}\), the **entire joint face vector** satisfies the exact distributional identity
\[
\bigl(f_j(Q_N)\bigr)_{j=0}^{N-3}
\overset{d}{=}\left(\binom N{j+2}-\binom{K_N}{j+2}-\binom{N-K_N}{j+2}\right)_{j=0}^{N-3}.
\tag{1}
\]
Define \(s^2=1/4-1/(2\pi)>0\). For every fixed integer \(J\ge0\), as \\(N\\to\\infty\\),
\[
\boxed{\left(\frac{\Delta_{N,j}}{N^{j+1}}\right)_{j=0}^{J}
\ \Longrightarrow\ \left(\frac{s^2}{2^j j!}Z^2\right)_{j=0}^{J},\quad Z\sim\mathcal N(0,1).}
\tag{2}
\]
In (2), restrict to \(N\ge J+3\). All joint moments of fixed nonnegative integer orders converge; in particular, for any fixed \(j,k\ge0\),
\[
\boxed{\operatorname{Cov}\bigl(f_j(Q_N),f_k(Q_N)\bigr)
\sim \frac{2s^4}{2^{j+k}j!k!}\,N^{j+k+2}.}
\tag{3}
\]
Consequently the Pearson correlations between face counts of any two fixed ranks tend to \(1\). These are **non-Gaussian, rank-one joint fluctuations** even though the underlying signed-normal imbalance obeys a Gaussian central limit theorem. For vertices, one also has the exact finite-dimensional mean
\[
\mathbb Ef_0(Q_N)=\frac{N(N-1)}4+
\frac{N(N-1)}{2\pi}\arcsin\!\left(\frac1{N-1}\right)
=\frac{N^2}4-Ns^2+O(N^{-1}).
\tag{4}
\]
For every \(t>0\), a nonasymptotic concentration inequality is
\[
\boxed{\mathbb P\{\Delta_{N,0}\ge Nt^2\}
\le 2e^{-t^2/2}+2e^{-\pi t^2/4}.}
\tag{5}
\]
The new mathematical assertion evaluated here is the **joint face-vector distributional reduction and rank-one chi-square fluctuation law** (1)–(3), with (4)–(5) as verification and concentration consequences; no priority is claimed merely for basic Gaussian sign probabilities or an isolated expected-face formula.

## Assumptions and scope

The simplex is regular; the hyperplane is chosen with rotationally invariant normal within the \((N-1)\)-dimensional linear space parallel to the simplex, and is constrained to pass through the centroid. Genericity holds with probability one: no simplex vertex lies in the hyperplane. The face-vector statement covers all \(0\le j\le N-3\), while limits (2)–(3) concern **fixed** face dimensions as \\(N\\to\\infty\\), not face ranks growing with dimension. All sections are nonempty and \((N-2)\)-dimensional. The model is a section, not a projection or a randomly translated hyperplane.

## Proof

**1. An exact combinatorial face-vector formula.** Represent the regular simplex affinely as
\[
S_N=\{x\in\mathbb R^N:x_i\ge0,\ \sum_{i=1}^N x_i=1\}.
\]
Its centroid is \((1/N,\ldots,1/N)\). A generic central hyperplane has equation \(\sum_i a_i x_i=0\) with \(\sum_i a_i=0\). Let \(K\) entries of \(a\) be positive and \(N-K\) negative; both signs occur. A \((j+1)\)-face of \(S_N\) is indexed by a subset \(I\) of \(j+2\) vertices. Its relative interior meets the hyperplane in a \(j\)-dimensional section precisely when \(I\) has both signs. Faces of the sliced polytope correspond bijectively to these crossed simplex faces: any supporting face of the section is the intersection with an ambient simplex face, with the ambient dimension one greater in general position. Thus
\[
f_j=\binom N{j+2}-\binom K{j+2}-\binom{N-K}{j+2}.
\]
For fixed \(j\), the function \(k\mapsto\binom{k}{j+2}+\binom{N-k}{j+2}\) is convex as a discrete integer sequence, since its second differences are nonnegative binomial coefficients. Its minimum is at the balanced values \(\lfloor N/2\rfloor,\lceil N/2\rceil\), giving \(B_{N,j}\) and nonnegativity of the deficit. This shows that every face-rank deficit depends on only one integer \(K\).

**2. Uniform orientations are centered Gaussian signs.** The normal space is the linear subspace \(L=\{a:\sum_i a_i=0\}\). If \(X_i\) are independent standard Gaussians and \(a_i=X_i-\bar X\), the vector \(a\) is an isotropic Gaussian on \(L\). Dividing it by its length produces a uniformly distributed direction on the sphere of \(L\). This positive scaling preserves signs, so \(K\) has precisely the law of \(K_N\), establishing (1).

**3. Fluctuation of the sign imbalance.** Write \(\phi(0)=1/\sqrt{2\pi}\) and \(F_N\) for the empirical distribution function of the Gaussian sample. The identity \(K_N/N=1-F_N(\bar X)\) and stochastic equicontinuity of the centered empirical cdf at the random threshold \(\bar X=O_p(N^{-1/2})\) give
\[
\frac{K_N-N/2}{\sqrt N}=
\frac1{\sqrt N}\sum_{i=1}^N
\left({\bf1}_{\{X_i>0\}}-\frac12-\phi(0)X_i\right)+o_p(1).
\tag{6}
\]
For completeness, the equicontinuity needed here can be verified without assuming the result: restrict \(|t|\le N^{-2/5}\) (which contains \(\bar X\) with probability tending to one), take a grid of mesh \(N^{-3/4}\), and use Bernstein's binomial tail bound on the centered counts over intervals between zero and grid points. Each such count has variance \(O(N^{3/5})\), there are \(O(N^{7/20})\) grid points, and the maximum centered fluctuation is \(o_p(\sqrt N)\). Counts in grid cells have uniformly \(o_p(\sqrt N)\) size by the same bound. The smooth expansion \(\Phi(t)=1/2+\phi(0)t+O(t^3)\) completes (6).

The iid summands in (6) have mean zero and variance
\[
\operatorname{Var}\left({\bf1}_{\{X>0\}}-\frac12-\phi(0)X\right)
=\frac14-\frac1{2\pi}=s^2,
\]
because \(\mathbb E[X{\bf1}_{\{X>0\}}]=\phi(0)\). Therefore the ordinary central limit theorem gives
\[
T_N:=(K_N-N/2)/\sqrt N\Longrightarrow sZ.
\tag{7}
\]

**4. A uniform local expansion for all fixed face dimensions.** For fixed \(j\), put \(r=j+2\) and expand the polynomial \(g_r(k)=\binom{k}{r}+\binom{N-k}{r}\) around the real center \(N/2\). It is even in the deviation \(k-N/2\), and the leading quadratic term has coefficient \(N^j/(2^j j!) +O(N^{j-1})\). The use of the nearest integer center in \(B_{N,j}\) changes only \(O(N^j)\) terms. For deviations \(|k-N/2|=O(\sqrt N)\), the higher even polynomial terms, after division by \(N^{j+1}\), tend to zero. Hence, jointly over any fixed finite collection of ranks,
\[
\frac{\Delta_{N,j}}{N^{j+1}}=\frac{T_N^2}{2^j j!}+o_p(1).
\]
Combining with (7) proves (2).

**5. Uniform integrability and covariance.** The Dvoretzky–Kiefer–Wolfowitz inequality and the Gaussian tail bound for \(\bar X\) yield, for every \(t>0\),
\[
\mathbb P\{|T_N|\ge t\}
\le 2e^{-t^2/2}+2e^{-\pi t^2/4}.
\tag{8}
\]
Indeed, \(|K_N/N-1/2|\le\sup_x|F_N(x)-\Phi(x)|+\phi(0)|\bar X|\), and allocate half the threshold to each term. For fixed \(j\), the polynomial formula and bounded discrete second difference give the uniform deterministic estimate
\[
0\le \Delta_{N,j}/N^{j+1}\le C_j(1+T_N^2)
\]
with constant \(C_j\) independent of \(N\) when \(N\ge j+3\). The Gaussian-type tail (8) consequently gives uniform integrability for every fixed polynomial product of normalized deficits. Therefore the joint convergence in (2) extends to all fixed polynomial moments. Since \(\operatorname{Var}(Z^2)=2\), covariance asymptotics (3) follow, as do the correlations \(\to1\).

**6. Exact vertex mean and concentration.** A central normal vector has pairwise coordinate correlation \(-1/(N-1)\). For each pair of vertices, the probability that its edge crosses the section is \(1/2+\arcsin(1/(N-1))/\pi\), by the standard bivariate Gaussian quadrant identity. Summing over the \(\binom N2\) edges gives (4). Finally \(\Delta_{N,0}=\lfloor N^2/4\rfloor-K_N(N-K_N)\le (K_N-N/2)^2\); (8) immediately gives (5).

## Verification

The included self-contained script `verify.py` reproduces the mathematical diagnostics using Python with NumPy and SciPy. It directly constructs a section's intersection points on crossed simplex edges, computes their convex hull in the section's affine coordinates, and compares the resulting vertex count with the exact signed-count formula for 125 sample sections across \(N=4,5,6,7,8\). Euler face-number identities provide additional finite checks. For \(N=16,64,256\), 65,000 Gaussian samples at each size verify the finite vertex expectation and examine the non-Gaussian chi-square scaling and the fixed-rank joint profile. The script prints `VERIFY_OK` when all stated tests pass. No Monte Carlo test or finite enumeration is used in place of the proof for infinitely many dimensions.

## Relationship to prior work

Dirksen [1] investigates volume formulas and extremizers for central regular-simplex sections, not random combinatorial face-count fluctuations. Affentranger–Schneider [2] concerns **random projections** of simplices and expected face counts; its abstract was accessible but its complete text was not, leaving a historical uncertainty rather than proof of noncoverage. Baryshnikov–Vitale [3] establishes a projection/Gaussian-polytope relationship. Kabluchko–Thäle [4], whose full text was examined, proves monotonicity of **expected face counts of projections**, not the present law for centroidal **sections** or the joint chi-square fluctuation. Böröczky–Lugosi–Reitzner [5] gives high-dimensional asymptotic **expected facets** of Gaussian polytopes, again for projections/Gaussian convex hulls. Brown et al. [6] investigate counts above a sample mean in a different heavy-tailed probability model; that related one-dimensional statistical concept is not asserted to be new here.

No claim of priority is made for general Gaussian sign/quadrant formulas, empirical-distribution central limit theory, or preexisting expected-face identities. The original contribution assessed here is the exact full centroidal simplex-section face-vector reduction together with the common-factor, chi-square, all-fixed-ranks fluctuation and covariance laws.

## Limitations

The limit is for face ranks fixed as dimension grows. It does not give asymptotics for ranks growing proportionally to dimension, a local limit theorem or an exact elementary distribution for \(K_N\), and it does not transfer unchanged to arbitrary nonregular simplices or noncentral hyperplanes. The completeness of the historical literature comparison is limited by unavailable full text of some relevant early projection papers; an equivalent older section result cannot be excluded by keyword searching. The present work has not undergone independent audit.

## References

[1] H. Dirksen, *Sections of the regular simplex—Volume formulas and estimates*, arXiv:1509.06408, original submission September 21, 2015; https://arxiv.org/abs/1509.06408 .

[2] F. Affentranger and R. Schneider, *Random projections of regular simplices*, Discrete Comput. Geom. 7 (1992), 219–226; https://doi.org/10.1007/BF02187839 .

[3] Y. M. Baryshnikov and R. A. Vitale, *Regular simplices and Gaussian samples*, Discrete Comput. Geom. 11 (1994), 141–147; https://doi.org/10.1007/BF02574000 .

[4] Z. Kabluchko and C. Thäle, *Monotonicity of expected f-vectors for projections of regular polytopes*, arXiv:1704.02496 (2017); https://arxiv.org/abs/1704.02496 .

[5] K. J. Böröczky, G. Lugosi and M. Reitzner, *Facets of High-Dimensional Gaussian Polytopes*, J. Geom. Anal. 34, 69 (2024); https://doi.org/10.1007/s12220-023-01440-5 .

[6] M. Brown, J. E. Cohen, C. Tang and S. C. P. Yam, *Taylor's law of fluctuation scaling for semivariances and higher moments of heavy-tailed data*, PNAS 118 (2021), e2108031118; https://doi.org/10.1073/pnas.2108031118 .
