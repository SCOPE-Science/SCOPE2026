# Sharp finite-horizon quantile-Kaczmarz rates on equiangular planar tight frames

## Finding

For every integer \(m\ge 2\), let \(a_j=(\cos(j\pi/m),\sin(j\pi/m))\), for \(0\le j<m\), and let the equations be consistent: \(b_j=\langle a_j,x_\star\rangle\). Given \(1\le r\le m\), a **tie-inclusive residual-quantile Kaczmarz step** admits every index whose absolute residual does not exceed the \(r\)-th smallest absolute residual and then chooses uniformly from all admitted indices. The chosen equation is enforced by an orthogonal Kaczmarz projection.

Define
\[
Q_{m,r}=\frac12+\frac{\sin(\pi r/m)}{2r\sin(\pi/m)},\qquad
B_{m,r}=\begin{cases}
Q_{m,r+1},&\text{if }r<m\text{ is even},\\
Q_{m,r},&\text{if }r\text{ is odd or }r=m.
\end{cases}
\]
For arbitrary deterministic \(x_0\), write \(e_k=x_k-x_\star\). For **every** integer \(k\ge1\),
\[
\mathbb E\|e_k\|_2^2=B_{m,r}^{\,k-1}\mathbb E\|e_1\|_2^2,
\qquad
\sup_{e_0\ne0}\frac{\mathbb E\|e_k\|_2^2}{\|e_0\|_2^2}
=Q_{m,r}B_{m,r}^{\,k-1}.
\]
The supremum is attained at a nonzero initial error whose **perpendicular** direction bisects an arc containing \(r\) consecutive frame lines; it is attained for all initial directions when \(r=m\).

The conditional post-first-step multiplier is exactly \(B_{m,r}\), even though the first-step conditional multiplier generally depends on the error orientation. The parity effect arises from exact residual ties: after any Kaczmarz projection, the retained set contains \(r+1\) rows when \(r<m\) is even, and precisely \(r\) rows otherwise.

The design is optimally conditioned as a frame, \(A^{\mathsf T}A=(m/2)I_2\), but for any fixed \(r\ge2\) the mean-square convergence loss per step is of order \(m^{-2}\). For \(r=1\), every nonzero initial error becomes permanently stationary after at most one projection. For \(r\ge2\), the iterates converge almost surely to the unique solution.

## Assumptions and scope

All objects are real and two-dimensional. The \(m\) rows are the distinct projective lines sampled at angles \(j\pi/m\), with unit Euclidean lengths, and \(m\ge2\). Data are exactly consistent and arithmetic is exact. At every iteration the residual-quantile selection is recomputed using **all \(m\) rows**; \(r\) denotes an integer rank rather than an interpolated quantile fraction. Every row at the cutoff is admitted, including ties. A fresh independent uniform draw is made from the admitted rows. The error is measured in squared Euclidean norm; no corruption, noise, row subsampling, overrelaxation, or varying stepsizes are included.

The update is \(x_{k+1}=x_k+(b_J-\langle a_J,x_k\rangle)a_J\), with conditional expectation taken over the newly sampled index \(J\). The matrix \(A\) formed from these rows has rank two, and therefore the solution is unique.

## Proof

**1. Geometry of the residual rank.** Fix a nonzero error \(e\). Choose an angle \(\phi\) for the unoriented line \(e^\perp\). Since all rows are unit vectors,
\[
\frac{|\langle a_j,e\rangle|^2}{\|e\|_2^2}
=\sin^2(\phi-j\pi/m),
\]
where angular differences are considered modulo \(\pi\). Thus the admitted directions are the \(r\) nearest points of a uniform projective angular grid, together with any directions tied at the cutoff. In a non-tie configuration those \(r\) points form a consecutive circular block.

**2. Sharp one-step inequality.** For any block \(s,s+1,\ldots,s+r-1\), a finite geometric-series identity gives
\[
\frac1r\sum_{\ell=0}^{r-1}\sin^2\!\left(\phi-\frac{(s+\ell)\pi}{m}\right)
=\frac12-\frac{\sin(\pi r/m)}{2r\sin(\pi/m)}
\cos\!\left(2\phi-\frac{(2s+r-1)\pi}{m}\right).
\]
Because \(0\le\sin(\pi r/m)\) for \(1\le r\le m\), the average selected squared residual is at least \(1-Q_{m,r}\) times squared error. When a cutoff tie admits more than \(r\) points, the additional points all have residual magnitudes no smaller than the first \(r\). Their inclusion cannot **decrease** the average squared residual, so the same lower bound holds with the stipulated tie-inclusive rule. Orthogonal projection satisfies the exact Pythagorean identity
\[
\|e-\langle a_j,e\rangle a_j\|_2^2
=\|e\|_2^2-|\langle a_j,e\rangle|^2.
\]
Therefore \(\mathbb E(\|e_1\|_2^2\mid e_0=e)\le Q_{m,r}\|e\|_2^2\). Equality is obtained by choosing \(\phi=(2s+r-1)\pi/(2m)\): the \(r\) nearest directions are precisely the centered block, and the cosine factor equals one. This equality holds for both parities of \(r\). At \(r=m\), the sine coefficient vanishes and the one-step factor is \(1/2\) for all directions.

**3. Exact post-first-step law and parity.** After a projection onto row \(a_j\), the new error is perpendicular to \(a_j\). If nonzero, its perpendicular direction \(\phi\) is therefore exactly one grid line. The residual rank order among grid lines is then symmetric: one residual is zero, the next two have equal magnitudes, then the next two, and so on. For odd \(r\), or for \(r=m\), precisely \(r\) rows lie under the cutoff; their angular offsets form the \(r\)-term symmetric consecutive block, and the block identity gives mean residual removal \(1-Q_{m,r}\). For even \(r<m\), the cutoff crosses a symmetric pair and precisely \(r+1\) rows are admitted, giving removal \(1-Q_{m,r+1}\). Hence for every grid-perpendicular nonzero error, independently of the row index and magnitude,
\[
\mathbb E(\|e_{k+1}\|_2^2\mid e_k)=B_{m,r}\|e_k\|_2^2.
\]
The same equality holds for \(e_k=0\) because zero remains zero. Once the first projection occurs, this conditional identity applies indefinitely. Taking successive expectations establishes the exact \(k\)-step expression. Combining it with the one-step sharpness above proves the displayed finite-horizon supremum and its attained maximizers.

**4. Convergence threshold.** When \(r=1\), the first projection leaves the error perpendicular to the chosen row, and that row thereafter has zero residual. Because the projective row directions are all distinct, it is the unique minimum-residual row for any nonzero error, so all subsequent updates are zero. A nonzero error cannot be annihilated by the chosen least-residual row on this frame: if a projection annihilated it, the chosen row would be parallel to the error and have strictly larger residual than at least one different row. Thus nonzero errors never converge to zero at rank one. When \(r\ge2\), the trigonometric expression satisfies \(B_{m,r}<1\), including \(r=m\). Expected squared error consequently tends to zero. Since \(\|e_k\|_2^2\) is nonincreasing on every sample path, its almost-sure limit is zero by bounded monotone convergence of the expectations.

**5. Scaling laws.** For fixed \(r\ge2\) and \(m\to\infty\), Taylor expansion of the sine quotient yields
\[
1-Q_{m,r}=\frac{\pi^2(r^2-1)}{12m^2}+O(m^{-4}),
\]
while, for fixed even \(r\),
\[
1-B_{m,r}=\frac{\pi^2 r(r+2)}{12m^2}+O(m^{-4});
\]
for fixed odd \(r\) it equals the first expression. If \(r/m\to q\in(0,1]\), then both factors converge to
\[
\frac12+\frac{\sin(\pi q)}{2\pi q}.
\]
Finally, summing the equispaced projective rank-one matrices by the same root-of-unity identity yields \(\sum_j a_ja_j^{\mathsf T}=(m/2)I_2\), proving the claimed perfect conditioning. Uniform selection over all rows has contraction \(1/2\), while fixed-rank quantile selection has the displayed quadratic slowdown.

## Verification

The companion standalone Python checker `verify.py` uses only the standard library. Run `python3 verify.py` in the directory containing the code. It independently constructs all planar unit rows, computes the retained set using an explicit numerical tie tolerance, applies projections, enumerates weighted transition energies through four updates, and compares the predicted one-step, post-step and full-horizon laws, as well as the asymptotic scaling limits. The recorded run performed 39,420 checks successfully. Numeric tests supplement, but are not the proof of, the infinite-dimensional-parameter and all-iteration claims: those are supplied by the preceding exact trigonometric and conditional-expectation derivation. Floating-point comparisons should not be interpreted as exact tie certificates.

## Relationship to prior work

Steinerberger's quantile-Kaczmarz formulation selects uniformly among all rows with residual magnitude below an empirical quantile, including threshold ties, and supplies general convergence conditions relevant to corrupted systems. Lok and Rebrova introduce a subspace-constrained quantile extension and study acceleration and robustness with a constrained iterate geometry. Coria, Haddock and Pacheco analyze quantile randomized Kaczmarz under time-dependent errors. These works motivate the precise selection rule and the need for rates that do not obscure structured frame geometry. The present statement is a **sharp exact consistent-data specialization** on an equiangular two-dimensional unit-norm tight frame, including a parity-sensitive cutoff law and a worst-initialization equality for every horizon. It does not claim to replace robustness or high-dimensional results in these papers.

The trigonometric sum and orthogonal-projection identity are classical; novelty, if maintained after further literature scrutiny, is the combination of the tie-inclusive quantile algorithm, its after-one-step state reduction, sharp all-horizon risk, and the even/odd slowdown distinction. General small-residual selection can be slow is already part of the prior motivation and is not claimed as new.

## Limitations

The analysis concerns two real coordinates, regularly spaced projective row normals, exact consistency, and an exact order-statistic cutoff. It does not cover irregular frames, positive measurement corruption, noise, rank-deficient systems, coordinate rounding, or random mini-batch quantiles. The independence of selected-row draws is assumed. All claims of rate and optimality are within the specified selection rule and frame class, not over all possible algorithms. A result in older geometric projection literature could potentially imply the sharp trigonometric formula by a non-obvious translation; this remains a literature priority risk. No independent validation has been performed.

## References

1. Jackie Lok and Elizaveta Rebrova, *A subspace constrained randomized Kaczmarz method for structure or external knowledge exploitation*, arXiv:2309.04889 (initial public submission 2023-09-09), https://arxiv.org/abs/2309.04889.
2. Stefan Steinerberger, *Quantile-based Random Kaczmarz for corrupted linear systems of equations*, *Information and Inference*, doi:10.1093/imaiai/iaab029, https://doi.org/10.1093/imaiai/iaab029.
3. Nestor Coria, Jamie Haddock, and Jaime Pacheco, *On Quantile Randomized Kaczmarz for Linear Systems with Time-Varying Noise and Corruption*, arXiv:2403.19874 (2024), https://arxiv.org/abs/2403.19874.
