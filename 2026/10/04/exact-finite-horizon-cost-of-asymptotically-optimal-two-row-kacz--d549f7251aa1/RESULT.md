# Exact finite-horizon cost of asymptotically optimal two-row Kaczmarz overrelaxation

## Finding
For a nonsingular two-equation real system, normalize the two row normals to unit vectors \(a,b\) and orient them so that their angle \(\theta\) is acute. Set \(s=\sin\theta\in(0,1)\) and \(c=\cos\theta\in(0,1)\). A cyclic Kaczmarz sweep using the same relaxation \(0<\omega<2\) on both rows has error operator
\[
T_\omega=(I-\omega bb^\top)(I-\omega aa^\top).
\]
The unrelaxed choice \(\omega=1\) is the unique minimizer of the worst-case Euclidean error after one full sweep:
\[
\min_{0<\omega<2}\|T_\omega\|_2=\|T_1\|_2=c.
\]
In contrast, the relaxation minimizing the asymptotic spectral radius is
\[
\omega_\star=\frac{2}{1+s},\qquad q:=\rho(T_{\omega_\star})=\frac{1-s}{1+s}.
\]
At this parameter the two eigenvalues coalesce and the sweep is defective. For every integer \(k\ge1\),
\[
\|T_{\omega_\star}^k\|_2
=q^k\left(\sqrt{1+\frac{4k^2s^2}{c^2}}+\frac{2ks}{c}\right),
\qquad
\|T_1^k\|_2=c^{2k-1}.
\]
Therefore the exact ratio between the spectral-radius-optimal and unrelaxed worst-case Euclidean errors after \(k\) sweeps is
\[
R_k(s)=\frac{\sqrt{1-s^2+4k^2s^2}+2ks}{(1+s)^{2k}}.
\]
For every nonorthogonal pair, \(R_1(s)>1\), although \(R_k(s)\to0\) as \(k\to\infty\). If \(s\downarrow0\) and \(k(s)\sqrt{s}\to\alpha\in(0,\infty)\), then
\[
\log R_{k(s)}(s)=\alpha\left(1-\frac{4\alpha^2}{3}\right)s^{3/2}+o(s^{3/2}).
\]
Thus the transient-to-asymptotic crossover for nearly parallel rows occurs on the \(s^{-1/2}\) sweep scale, with critical scaled horizon \(\alpha=\sqrt{3}/2\): below that value the overrelaxed choice is eventually worse, and above it it is eventually better.

## Assumptions and scope
The system has exactly two linearly independent real rows. Both rows are normalized to unit Euclidean norm, the same constant relaxation is used for both row updates, and performance is measured by the Euclidean norm of the solution error after complete two-row sweeps. The result concerns deterministic cyclic Kaczmarz. It does not claim optimality for randomized row selection, inconsistent systems, different row-dependent relaxations, residual norms, or more than two rows.

The orthogonal endpoint \(s=1\) is degenerate in the displayed formulas containing \(c^{-1}\): there \(\omega_\star=1\), and one unrelaxed sweep solves the two-equation system exactly. The nearly parallel limit \(s\downarrow0\) is singular because the two rows approach linear dependence.

## Proof
Choose coordinates \(a=(1,0)^\top\) and \(b=(c,s)^\top\). Direct multiplication gives
\[
T_\omega=
\begin{pmatrix}
(1-\omega)(1-\omega c^2) & -\omega cs\
-(1-\omega)\omega cs & 1-\omega s^2
\end{pmatrix}.
\]
Apply this matrix to \(a^\perp=(0,1)^\top\). Since \(c^2+s^2=1\),
\[
\|T_\omega a^\perp\|_2^2=c^2+s^2(\omega-1)^2.
\]
Hence \(\|T_\omega\|_2\ge\sqrt{c^2+s^2(\omega-1)^2}\ge c\), with equality in the second inequality only at \(\omega=1\). At \(\omega=1\), the first column of \(T_1\) is zero and the second has norm \(c\), so \(\|T_1\|_2=c\). This proves unique one-sweep optimality.

For the asymptotic rate, the two-row Kaczmarz sweep is the corresponding two-cyclic relaxation iteration. Specializing the classical two-block SOR/Young formula to the unrelaxed spectral factor \(c^2\) gives
\[
\omega_\star=\frac{2}{1+s},\qquad
q=\rho(T_{\omega_\star})=\omega_\star-1=\frac{1-s}{1+s}.
\]
Equivalently, direct calculation gives
\[
\operatorname{tr}(T_\omega)=c^2\omega^2-2\omega+2,
\qquad
\det(T_\omega)=(1-\omega)^2,
\]
and characteristic discriminant
\[
\Delta_\omega=\omega^2c^2\,[2-\omega(1-s)]\,[2-\omega(1+s)].
\]
Thus \(\Delta_{\omega_\star}=0\). For \(0<s<1\), \(T_{\omega_\star}\neq qI\), so it has a nontrivial size-two Jordan block. Write
\[
T_{\omega_\star}=qI+N.
\]
Then \(N^2=0\), \(\operatorname{tr}N=0\), and direct simplification yields
\[
\|N\|_F^2=\frac{16s^2(1-s)}{(1+s)^3},
\qquad
\frac{\|N\|_F^2}{q^2}=\frac{16s^2}{c^2}.
\]
Therefore
\[
T_{\omega_\star}^k=q^kI+kq^{k-1}N.
\]
After factoring out \(q^k\), the remaining two-by-two matrix has determinant one and squared Frobenius norm \(2+16k^2s^2/c^2\). Its larger singular value is therefore
\[
\sqrt{1+\frac{4k^2s^2}{c^2}}+\frac{2ks}{c},
\]
which proves the first power-norm formula.

For \(\omega=1\), the rank-one matrix \(T_1\) has nonzero eigenvalue \(c^2\), so \(T_1^k=c^{2k-2}T_1\) and \(\|T_1^k\|_2=c^{2k-1}\). Dividing the two exact formulas and using \(q/c^2=1/(1+s)^2\) gives \(R_k(s)\).

At \(k=1\),
\[
R_1(s)=\frac{\sqrt{1+3s^2}+2s}{(1+s)^2}>1,
\]
because \(\sqrt{1+3s^2}>1+s^2\) is equivalent to \(s^2(1-s^2)>0\). For fixed \(s>0\), the numerator of \(R_k(s)\) grows only linearly in \(k\) while the denominator grows geometrically, so \(R_k(s)\to0\).

Finally, the exact identity
\[
\log R_k(s)=\frac12\log(1-s^2)
+\operatorname{arsinh}\!\left(\frac{2ks}{\sqrt{1-s^2}}\right)
-2k\log(1+s)
\]
permits a uniform Taylor expansion when \(k\sqrt{s}\) stays bounded. If \(k(s)\sqrt{s}\to\alpha\), cancellation of the order-\(s^{1/2}\) terms leaves
\[
\log R_{k(s)}(s)=\alpha\left(1-\frac{4\alpha^2}{3}\right)s^{3/2}+o(s^{3/2}),
\]
which gives the stated crossover scale and threshold.

## Verification
The accompanying checker constructs the sweep symbolically, verifies the one-sweep lower-bound identity, trace and determinant, the factorized characteristic discriminant, the nilpotent Jordan remainder at \(\omega_\star\), and the Frobenius-norm identity. It also replays the all-\(k\) norm formula on exact rational angle data for several horizons and checks the small-angle series. Its recorded output is included.

No finite experiment is used as a substitute for the algebraic proof. The numerical replay is only a consistency check of identities already derived symbolically.

## Relationship to prior work
Relaxed Kaczmarz is classical, and Szwarc and Świderski study convergence of relaxed Kaczmarz iterations in Hilbert space. Czaja and Tanis give a frame-theoretic treatment of the Kaczmarz algorithm. The asymptotically optimal relaxation formula used here is a specialization of the classical two-cyclic SOR/Young relation; Oseledets, Rakhuba, and Uschmajew state this relation explicitly for two-block SOR, and Dax discusses spectral-radius-optimal relaxation for Kaczmarz-type iterations.

The additional statement here is finite-horizon and uses the Euclidean solution-error operator norm in the original two-row Kaczmarz variables. The spectral-radius optimum lands exactly at a defective double root, which creates the explicit polynomial transient factor in \(\|T_{\omega_\star}^k\|_2\). The literature and published-result searches recorded in the audit found nearby results on residual spikes, unrelaxed alternating projections, Kaczmarz bias, and two-coordinate Gauss-Seidel transients, but not this exact relaxed two-row power norm, its one-sweep incompatibility, or its \(s^{-1/2}\) crossover law.

## Limitations
The proof is exact only for two independent rows and a common relaxation. It does not establish a corresponding closed form for larger cyclic systems, where optimal relaxation and nonnormal transients can depend on more than one principal angle or spectral parameter. The originality check cannot prove absence from all historical SOR/Kaczmarz literature; the strongest residual risk is that an older source may have derived the same two-by-two finite-power singular-value formula without using the same finite-horizon interpretation.

## References
1. W. Czaja and J. Tanis, “Kaczmarz Algorithm and Frames,” arXiv:1409.8310, first submitted 29 September 2014.
2. R. Szwarc and G. Świderski, “Kaczmarz algorithm with relaxation in Hilbert space,” *Studia Mathematica* 216(3), 237–243 (2013), DOI 10.4064/sm216-3-3.
3. I. V. Oseledets, M. V. Rakhuba, and A. Uschmajew, “Local convergence of alternating low-rank optimization methods with overrelaxation,” *Numerical Linear Algebra with Applications*, DOI 10.1002/nla.2459; first published 1 July 2022.
4. A. Dax, “The Rate of Convergence of the SOR Method in the Positive Semidefinite Case,” *Computational and Mathematical Methods* (2022), Article 6143444, DOI 10.1155/2022/6143444.
