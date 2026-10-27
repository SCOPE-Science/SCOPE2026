# Exact orthogonal-pair advantage for planar random-subspace Gauss–Newton

## Finding

Let \(H\in\mathbb R^{2\times2}\) be symmetric positive definite and \(f(x)=\tfrac12x^{\mathsf T}Hx\). Start from a deterministic \(x_0\in\mathbb R^2\) and perform two **sequential exact one-dimensional minimizations**
\[
T_u(x)=x-u\frac{u^{\mathsf T}Hx}{u^{\mathsf T}Hu}.
\]
Compare the following distributions of search directions, with \(u_1\) uniform on the Euclidean unit circle in both protocols: (i) independent directions, where \(u_2\) is independently uniform; and (ii) orthogonal pairing, where \(u_2=Ru_1\) and \(R\) is a fixed counterclockwise quarter-turn. Put \(\kappa=\lambda_{\max}(H)/\lambda_{\min}(H)\). For **every** such \(H\) and \(x_0\), their outputs satisfy the exact matrix-free expectation identity
\[
\boxed{\mathbb E[f(x_{2,\mathrm{pair}})]
=\left(\frac{\kappa-1}{\kappa+1}\right)^2
\mathbb E[f(x_{2,\mathrm{iid}})].}
\]
For every nonzero \(x_0\), the independent expectation is strictly positive and pairing strictly improves it. When \(\kappa=1\), pairing gives the exact minimizer after the second step almost surely. At large finite \(\kappa\), the guaranteed relative advantage approaches zero. A uniform direction can equivalently be obtained by normalizing a two-dimensional isotropic Gaussian, so these are one-column Gaussian sketches with a dependent, orthogonalized second sketch. On a linear-residual least-squares objective, each one-dimensional minimization is the exact unregularized rank-one subspace Gauss–Newton step.

## Assumptions and scope

Only \(d=2\), \(H\succ0\), an exact quadratic model, exact one-dimensional minimization, and Euclidean (not Hessian-metric) orthogonality of the two paired directions are asserted. Expectations refer to the angular randomness, not data noise. The same fixed \(H\) is used at both steps. The result is **not** asserted for sequential projections in dimension \(d>2\), trust-region truncations, noisy function measurements, nonquadratic residuals, or approximate line searches.

## Proof

Orthogonal conjugation and positive scalar scaling do not change the relative expectation. In an eigenbasis write \(H=\lambda_{\min}\operatorname{diag}(r^2,1)\), where \(r=\sqrt\kappa\ge1\), and introduce \(y=\operatorname{diag}(r,1)x\). The harmless factor \(\lambda_{\min}\) can be restored in the objective. The scaled objective is \(\tfrac12\|y\|_2^2\). Write \(c=\cos\theta\), \(s=\sin\theta\) and \(u_1=(c,s)\). Define \(D=r^2c^2+s^2\) and \(E=r^2s^2+c^2\). In the \(y\) coordinates the first line minimization removes the unit direction \(v=(rc,s)/\sqrt D\), leaving
\[
y_1=(w^{\mathsf T}y_0)w,\qquad w=(-s,rc)/\sqrt D.
\]

For a fresh independent uniform second line, the normalized \(y\)-direction \(v_2\) has covariance
\[
M=\mathbb E[v_2v_2^{\mathsf T}]
=\operatorname{diag}\!\left(\frac r{r+1},\frac1{r+1}\right).
\]
This follows by substituting \(t=\tan\theta\) into the elementary angular integrals. Thus, conditioned on \(\theta\),
\[
\mathbb E[\|y_{2,\mathrm{iid}}\|_2^2\mid\theta]
=(w^{\mathsf T}y_0)^2 w^{\mathsf T}(I-M)w.
\]
For the perpendicular second line \(u_2=(-s,c)\), its normalized \(y\)-direction is \(v_\perp=(-rs,c)/\sqrt E\). Hence \(w^{\mathsf T}v_\perp=r/\sqrt{DE}\) and
\[
\|y_{2,\mathrm{pair}}\|_2^2
=(w^{\mathsf T}y_0)^2\left(1-\frac{r^2}{DE}\right),\qquad
DE-r^2=(r^2-1)^2s^2c^2.
\]

Average over \(\theta\in[0,\pi)\). The mixed coefficients in the quadratic forms vanish by reflecting \(\theta\mapsto\pi-\theta\). Let \(\langle g\rangle=\pi^{-1}\int_0^\pi g(\theta)\,d\theta\). To make the remaining integrations reproducible, their four requisite values, obtained using \(t=\tan\theta\) and partial fractions, are
\[
\begin{aligned}
\left\langle\frac{s^4+r^3s^2c^2}{D^2}\right\rangle
 &=\frac{r^2+r+2}{2(r+1)^2},\\
\left\langle\frac{r^2s^2c^2+r^5c^4}{D^2}\right\rangle
 &=\frac{r(2r^2+r+1)}{2(r+1)^2},\\
\left\langle\frac{s^4c^2}{D^2E}\right\rangle
 &=\frac{r^2+r+2}{2(r+1)^3(r^2+1)^2},\\
\left\langle\frac{r^2s^2c^4}{D^2E}\right\rangle
 &=\frac{r(2r^2+r+1)}{2(r+1)^3(r^2+1)^2}.
\end{aligned}
\]
More explicitly, the four integrals on the left, in the displayed order, are all \(2/\pi\) times integrals over \(t\in(0,\infty)\) with respective rational integrands
\[
\frac{t^4+r^3t^2}{(1+t^2)(r^2+t^2)^2},\qquad
\frac{r^2t^2+r^5}{(1+t^2)(r^2+t^2)^2},
\]
\[
\frac{t^4}{(1+t^2)(r^2+t^2)^2(1+r^2t^2)},\qquad
\frac{r^2t^2}{(1+t^2)(r^2+t^2)^2(1+r^2t^2)}.
\]
These are proper even rational functions, so elementary partial fractions prove the evaluations using the identities \(\int_0^\infty dt/(t^2+a^2)=\pi/(2a)\) and \(\int_0^\infty dt/(t^2+a^2)^2=\pi/(4a^3)\) for \(a>0\). The other three are evaluated identically. The separate \(r=1\) values also follow directly from the trigonometric integrals.

Write the angular-averaged squared norms as \(\mathbb E\|y_{2,\bullet}\|^2=C_{\bullet,1}y_{0,1}^2+C_{\bullet,2}y_{0,2}^2\). Substitution gives
\[
\begin{aligned}
C_{\mathrm{iid},1}&=\frac{r^2+r+2}{2(r+1)^3},&
C_{\mathrm{iid},2}&=\frac{r(2r^2+r+1)}{2(r+1)^3},\\
C_{\mathrm{pair},1}&=\frac{(r^2-1)^2(r^2+r+2)}{2(r+1)^3(r^2+1)^2},&
C_{\mathrm{pair},2}&=\frac{r(r^2-1)^2(2r^2+r+1)}{2(r+1)^3(r^2+1)^2}.
\end{aligned}
\]
Both paired coefficients are their corresponding independent coefficients times \(((r^2-1)/(r^2+1))^2\), independently of \(y_0\). Restoring the common objective factor \(\lambda_{\min}/2\) proves the formula. Both independent coefficients are positive for \(r\ge1\), so the claimed strictness holds for every \(x_0\ne0\). All boundary assertions follow immediately.

## Verification

`verify.py` is a standalone Python standard-library checker for the displayed coefficient formulas. It directly samples the angle-integral expressions for the sequential projections with the midpoint rule at 65,536 angles and checks all four coefficients for seven anisotropies, including the isotropic boundary. Execute `python verify.py`, which prints `VERIFY_OK`. These finite quadrature checks are supplementary; the general identity is proved by the preceding exact integrals.

## Relationship to prior work

Cartis–Fowkes–Shao (arXiv:2211.09873v1, Section 5) analyze a broader random-subspace Gauss–Newton framework and Gaussian sketches for nonlinear least squares; their guarantees concern safeguarded algorithms and global complexity, not this unconditional two-step exact objective comparison. Stich–Müller–Gärtner (arXiv:1111.0194v2, Sections 2–5) analyze random pursuit with independently drawn one-dimensional line-search directions and bounds on convergence; their reported guarantees do not state this comparison with a dependent perpendicular second line. Kozak and coauthors (arXiv:2107.03941) explicitly analyze orthogonal directions but chiefly finite-difference stochastic gradient steps, rather than two successive exact line minimizers. Gürbüzbalaban and coauthors (arXiv:1803.08200) compare fixed-coordinate random-permutation and with-replacement descent on special Hessians; fixed axes with random ordering do not supply the Haar-rotated all-SPD two-step identity by direct implication. These are comparisons of mathematical statements, not claims that the full literature has been exhausted.

## Limitations

The result is a finite two-step, planar exact-arithmetic fact, not a global complexity bound in arbitrary dimension. Sampling independently versus pairing can change algorithm implementation and parallelization requirements; no universal computational-runtime comparison is proved. It is possible that a general unpublished or unindexed formula for randomly rotated Gauss–Seidel already implies this identity. A closely related publicly indexed 2026 result on two-coordinate Gauss–Seidel Euclidean transients was available in summary form, but its full text could not be retrieved, leaving a specific residual comparison risk. The proof does not require or assert statistical independence of the two paired search vectors.

## References

1. Cartis, Fowkes, and Shao, *Randomised subspace methods for non-convex optimization, with applications to nonlinear least-squares*, arXiv:2211.09873v1, 17 November 2022, https://arxiv.org/html/2211.09873v1.
2. Stich, Müller, and Gärtner, *Optimization of Convex Functions with Random Pursuit*, arXiv:1111.0194v2, https://arxiv.org/html/1111.0194v2.
3. Kozak, Molinari, Rosasco, Tenorio, and Villa, *Zeroth order optimization with orthogonal random directions*, arXiv:2107.03941, https://arxiv.org/abs/2107.03941.
4. Gürbüzbalaban, Özdaglar, Vanli, and Wright, *Randomness and Permutations in Coordinate Descent Methods*, arXiv:1803.08200, https://arxiv.org/abs/1803.08200.
5. Chen, Hu, and Wu, *Randomized Fast Subspace Descent Methods*, arXiv:2006.06589, https://arxiv.org/abs/2006.06589.
