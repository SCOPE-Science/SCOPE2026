# A sharp Euclidean solution-error barrier for symmetric GMRES(1)

## Result

Let \(A\in\mathbb R^{n\times n}\) be real, symmetric and nonsingular, and consider
one step of minimal residual iteration (MRI), equivalently GMRES restarted after
one Krylov vector (GMRES(1)), for \(Ax=b\):
\[
r_k=Ax_k-b,\qquad
\alpha_k=\frac{r_k^TAr_k}{r_k^TA^2r_k},\qquad
x_{k+1}=x_k-\alpha_k r_k.
\]
Write \(x_* = A^{-1}b\) and \(e_k=x_k-x_*\), so \(r_k=Ae_k\). Then every
nonzero-error step satisfies the dimension-free sharp bound
\[
\boxed{\frac{\|e_{k+1}\|_2}{\|e_k\|_2}\le \frac{2}{\sqrt3}.}
\]
Thus residual minimization on a symmetric indefinite system can increase the
Euclidean solution error, but a single GMRES(1) cycle can never increase it by more
than \(15.4700538\ldots\%\). The constant is independent of dimension, spectral
scale and the distance of the spectrum from zero.

The constant is attained by a two-dimensional symmetric indefinite system. Put
\[
\lambda_+=\frac{3+\sqrt{33}}{12},\qquad
\lambda_- =\frac{3-\sqrt{33}}{12},\qquad
w_+=\frac12-\frac{13\sqrt{33}}{198},
\]
let \(A_*=\operatorname{diag}(\lambda_+,\lambda_-)\), and choose an error whose
squared eigencoordinates are \(w_+\) and \(1-w_+\). Then the first MRI step has
\(\alpha_0=1\) and
\[
\frac{\|e_1\|_2}{\|e_0\|_2}=\frac2{\sqrt3}.
\]
Moreover this witness is periodic in direction: the next step has
\(\alpha_1=-2\),
\[
\frac{\|e_2\|_2}{\|e_1\|_2}=\frac1{\sqrt3},\qquad
e_2=\frac23e_0,
\]
and the two-step pattern repeats. The residual norm decreases by
\(\sqrt{2/3}\) on each of these steps, so every other step gives the largest
possible solution-error spike while the residual decreases strictly and steadily.

## Proof of the universal bound

Diagonalize \(A\) orthogonally. Normalize \(\|e_k\|_2=1\), let \(\lambda_i\)
be the active eigenvalues, and let \(w_i\ge0\), \(\sum_iw_i=1\), be the squared
coordinates of \(e_k\) in the eigenbasis. Define
\[
m_j=\sum_i w_i\lambda_i^j.
\]
Since \(r_k=Ae_k\),
\[
\alpha_k=\frac{e_k^TA^3e_k}{e_k^TA^4e_k}=\frac{m_3}{m_4}.
\]
If \(\alpha_k=0\), then \(e_{k+1}=e_k\) and the claimed bound is immediate.
Otherwise put \(z_i=\alpha_k\lambda_i\). The minimizing step length gives the
moment identity
\[
\sum_i w_i z_i^3(1-z_i)
=\alpha_k^3(m_3-\alpha_km_4)=0.
\]
For every real \(z\), the following scalar identity is exact:
\[
\frac43-(1-z)^2-12z^3(1-z)
=\frac{(6z^2-3z-1)^2}{3}\ge0.
\]
Average it with weights \(w_i\) and use the moment identity. Since
\[
\frac{\|e_{k+1}\|_2^2}{\|e_k\|_2^2}
=\sum_iw_i(1-z_i)^2,
\]
we obtain
\[
\frac{\|e_{k+1}\|_2^2}{\|e_k\|_2^2}\le\frac43,
\]
which proves the theorem.

Equality in the scalar inequality requires each active \(z_i\) to satisfy
\(6z^2-3z-1=0\), whose two roots are \(\lambda_+\) and \(\lambda_-\) above.
The stated weight is the unique nontrivial two-root weight satisfying
\(\sum_iw_i z_i^3(1-z_i)=0\), proving sharpness.

For the two-cycle, direct substitution gives \(\alpha_0=1\) and \(\alpha_1=-2\).
On either eigenvalue, the root relation \(6\lambda^2-3\lambda-1=0\) gives
\[
(1+2\lambda)(1-\lambda)=1+\lambda-2\lambda^2=\frac23.
\]
Hence \(e_2=(2/3)e_0\), so the normalized direction returns and the same two-step
pattern repeats. Direct substitution also gives
\(\|r_{k+1}\|_2/\|r_k\|_2=\sqrt{2/3}\) on both alternating steps.

## Definite systems cannot exhibit this error amplification

If \(A\succ0\), all moments \(m_j\) above are positive. The elementary moment
inequality
\[
m_1m_4-m_2m_3
=\frac12\sum_{i,j}w_iw_j\lambda_i\lambda_j
(\lambda_i+\lambda_j)(\lambda_i-\lambda_j)^2\ge0
\]
implies \(\alpha_km_2=m_2m_3/m_4\le m_1\). Therefore
\[
\frac{\|e_{k+1}\|_2^2}{\|e_k\|_2^2}-1
=\alpha_k(\alpha_km_2-2m_1)
\le -\alpha_km_1<0.
\]
The same follows for \(A\prec0\) after replacing \(A\) by \(-A\). Thus a
nontrivial Euclidean error increase requires an indefinite active spectrum.

## No nontrivial absolute-condition-number safety threshold

For a symmetric nonsingular matrix define
\[
\kappa_{|\lambda|}(A)=\frac{\max_i|\lambda_i|}{\min_i|\lambda_i|}.
\]
There is no safety interval \(1<\kappa_{|\lambda|}\le K\) on which GMRES(1)
solution errors are guaranteed to be monotone for all symmetric matrices.
Indeed, for any \(t>1\), take \(A=\operatorname{diag}(1,-t)\) and let
\(r=e_2^2/e_1^2>0\) denote the squared-error weight ratio. The squared one-step
error ratio is
\[
Q(r,t)=\frac{r(t+1)^2(rt^6+1)}{(r+1)(rt^4+1)^2}.
\]
At \(r=t^{-3}\), the minimizing step is \(\alpha=0\) and \(Q=1\), while
\[
\left.\frac{\partial Q}{\partial r}\right|_{r=t^{-3}}
=\frac{2t^4(t-1)}{(t+1)(t^2-t+1)}>0.
\]
Hence every \(t>1\), however close to one, admits nearby initial errors with
\(Q>1\). At \(t=1\), by contrast, \(A^2=c^2I\) after scaling and the one-step
error is nonincreasing. The sharp equality witness for the universal \(2/\sqrt3\)
bound has
\[
\kappa_{|\lambda|}(A_*)
=\frac{7+\sqrt{33}}4=3.1861406616\ldots.
\]

## Symmetry is essential

No dimension-free analogue holds for arbitrary nonsymmetric matrices. For
\[
A_M=\begin{pmatrix}1&M\\0&1\end{pmatrix},\qquad e=(0,1)^T,
\]
one GMRES(1) step uses
\[
\alpha=\frac{2M^2+1}{4M^2+1}.
\]
Its Euclidean solution-error ratio grows as \(M/2\), whereas its residual ratio
is asymptotic to \(1/(2M)\). Thus the bounded transient is a consequence of
self-adjoint spectral structure, not residual minimization alone.

## Computational model and limitations

The statements concern exact arithmetic, real symmetric nonsingular matrices, the
ordinary Euclidean norm, and unpreconditioned MRI/GMRES(1), meaning that the method
is restarted after every single Krylov direction. They do not assert the same
per-step bound for full GMRES, full MINRES after its first Krylov step, nonsymmetric
systems, flexible or variable preconditioning, or finite-precision recurrences.
The result bounds solution error, not residual convergence speed or runtime. For
symmetric indefinite matrices GMRES(1) can stagnate for residuals with
\(r^TAr=0\); the theorem does not imply global convergence.

The deterministic artifact checks the exact equality two-cycle, random symmetric
spectra, and a nonsymmetric unbounded-amplification family. These computations are
supporting evidence; the proof is the scalar identity and moment relation above.

## Literature context

Minimal-residual Krylov methods classically minimize residual rather than solution
error. Saad--Schultz introduced GMRES, while Saad's later analysis and modern
GMRES(1)/MRI work study residual convergence. He (2025) gives a theorem-level
analysis of one-step and asymptotic GMRES(1) residual factors for symmetric systems;
for indefinite symmetric matrices the worst-case residual q-linear/root factor is
one. The error quantity treated here is instead \(\|x_k-x_*\|_2\).

The separation between residual decrease and solution-error behavior is also known
qualitatively. Weiss (1994) emphasizes that residuals may decrease while solution
errors increase, and Meurant (2011) develops solution-error norm formulas and
estimators for FOM/GMRES. Searches under GMRES(1), MRI, Orthomin(1), minimal
residual Richardson, symmetric indefinite systems, Euclidean solution error,
error amplification/monotonicity, the constants \(2/\sqrt3\), \(4/3\), and the
sharpness values involving \(\sqrt{33}\) did not locate the universal one-step
bound, its equality classification, or the exact alternating equality cycle.

The most important residual historical-coverage risk is older literature on
minimum-residual and minimum-error iterations, including Fridman's 1963 note and
Saad's 2000 paper; their complete theorem-level contents were not all available for
full inspection. Weiss (1994) and Meurant (2011) are also broad enough that an
equivalent inequality under different terminology cannot be completely excluded.
Accordingly originality is claimed only to the best of our knowledge.

## References

1. Y. Saad and M. H. Schultz, “GMRES: A Generalized Minimal Residual Algorithm for Solving Nonsymmetric Linear Systems,” *SIAM Journal on Scientific and Statistical Computing* 7(3), 1986, 856–869. https://doi.org/10.1137/0907058
2. R. Weiss, “Error-Minimizing Krylov Subspace Methods,” *SIAM Journal on Scientific Computing* 15(3), 1994, 511–527. https://doi.org/10.1137/0915034
3. Y. Saad, “Further Analysis of Minimum Residual Iterations,” *Numerical Linear Algebra with Applications* 7(2), 2000, 67–93. https://doi.org/10.1002/(SICI)1099-1506(200003)7:2%3C67::AID-NLA186%3E3.0.CO;2-8
4. G. Meurant, “Estimates of the Norm of the Error in Solving Linear Systems with FOM and GMRES,” *SIAM Journal on Scientific Computing* 33(5), 2011, 2686–2705. https://doi.org/10.1137/100795565
5. Y. He, “The worst-case root-convergence factor of GMRES(1),” arXiv:2501.10248, 2025. https://arxiv.org/abs/2501.10248
6. V. M. Fridman, “The method of minimum iterations with minimum errors for a system of linear algebraic equations with a symmetrical matrix,” *U.S.S.R. Computational Mathematics and Mathematical Physics*, 1963, 362–363. https://doi.org/10.1016/0041-5553(63)90412-9
