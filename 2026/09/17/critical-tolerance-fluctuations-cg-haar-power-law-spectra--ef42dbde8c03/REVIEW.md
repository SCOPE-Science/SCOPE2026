# Same-model review

## Verdict

**PASS (same-model review only).** Correctness, originality to the best of our
knowledge, and value were assessed separately. This is not independent
validation or peer review.

## Correctness audit

The argument was checked at the points where normalization, moment tails, and
the stopping-time conclusion could fail.

1. **CG normalization.** In the Haar source model the squared spectral weights
   are normalized independent exponentials. The normalization cancels from the
   quotient defining the relative squared \(A\)-norm error. Rescaling
   \(\lambda_j=j^{-p}\) by \(Y_{j,n}=(n/j)^p\) preserves the class of
   degree-\(d\) residual polynomials with value one at zero.
2. **Jacobi reduction.** The substitution \(x=1/y\) converts the constrained
   residual-polynomial minimum into the monic orthogonal-polynomial problem for
   the weight \(x^{p^{-1}-2d-2}\) on \([0,1]\). The leading coefficient and
   Jacobi norm give
   \(F_d(p)=\binom{p^{-1}-2}{d}^{-2}\). Direct symbolic inversion of the
   limiting Hankel moment matrix agrees with this formula for degrees
   \(d=1,2,3,4\).
3. **Moment CLT and deterministic bias.** The largest raw moment needed by the
   degree-\(d\) quadratic form is \(A_{2d+1,n}\). The covariance CLT therefore
   needs moments through exponent \(2(2d+1)p\), giving exactly the stated
   strict condition \((4d+2)p<1\). The same condition makes every deterministic
   Riemann-sum bias \(o(n^{-1/2})\). Lindeberg follows because the maximal
   triangular-array coefficient is \(o(1)\) at the square-root-\(n\) scale
   and the exponential square is uniformly integrable.
4. **Delta-method derivative.** The limiting moment Gram matrix is positive
   definite, so the constrained minimizer is unique and depends smoothly on
   the finite moment vector. The envelope derivative is
   \[
   D\Phi[\delta A]
   =(1-p)\left(
   \sum_{a,b=0}^d c_ac_b\,\delta A_{a+b+1}
   -F_d\,\delta A_1\right),
   \]
   at the limiting minimizing coefficients \(c_a\). This produces the stated
   influence function and variance. The variance is finite under the same
   exponent condition and positive because the influence polynomial is not
   identically zero.
5. **Half-step conclusion.** Under \((4d+2)p<1\), degree \(d+1\) is also in the
   finite-moment regime. The closed form gives strict gaps
   \(F_{d-1}>F_d>F_{d+1}\). Thus, with probability tending to one, the stopping
   time at tolerance \(F_d\) is confined to \(\{d,d+1\}\); the centered
   nondegenerate Gaussian limit gives probability \(1/2\) for each value.
6. **Real-Haar variant.** Replacing exponential weights by mean-one
   \(\chi_1^2\) weights changes only their variance, from one to two, so the
   Gaussian variance doubles and the sign probability remains one half.

### Correctness limitations

The proof does not cover the boundary \((4d+2)p=1\), where logarithmic or
non-Gaussian normalization may appear, or the heavier-tail regime above it. It
is a fixed-degree exact-arithmetic result and does not address preconditioning,
finite precision, or growing degree.

## Originality audit

### Internal SCOPE overlap

Repository searches using `conjugate gradient`, `power-law spectrum`,
`critical tolerance`, `Haar`, `Jacobi`, and the source identifier
`2606.02484` found no SCOPE record covering this claim. Repository text search
is not a proof of semantic non-overlap, so this remains a best-effort collision
check.

### External literature checked

- **Amsel et al., arXiv:2602.05394v2.** The current arXiv record was inspected.
  Problem 2.4 supplies the Haar power-law CG/RCD source model.
- **Chen et al., arXiv:2606.02484v1.** The current full 43-page PDF and arXiv
  version history were inspected. Appendix A defines all finite-degree floors
  \(F_D(p)\) and proves fixed-degree convergence. Its critical analysis is
  centered on the terminal active floor \(F_{K(p)}(p)\) and first-inactive
  Schur-complement corrections. Searches of the full text found no central
  limit theorem, Bernoulli stopping law, or square-root-\(n\) interior-floor
  fluctuation statement.
- **Velikanov--Yarotsky, JMLR 2024 / arXiv:2202.00992.** The paper develops
  sharp power-law spectral convergence analysis and uses Jacobi-polynomial
  structure. This is why the Jacobi identity in the present proof is treated
  as a calculation supporting the new statement, not as a standalone novelty
  claim.
- **Paquette--Trogdon, arXiv:2007.00640.** The full paper was inspected around
  its main results. It proves CLTs for CG/MINRES residual and error norms and
  almost-deterministic iteration counts for sample-covariance ensembles.
  This is the closest located precedent for fluctuation-level average-case CG,
  but its random-matrix model and limiting spectral regime differ from the
  deterministic power-law spectrum with Haar source weights considered here.
- **Deift--Trogdon, arXiv:1901.09007, and related random-matrix CG work.**
  Searches confirmed prior almost-deterministic iteration-count results for
  well-conditioned Wishart systems, again in a different ensemble.

Targeted searches were also made for combinations of `critical tolerance`,
`fixed-degree conjugate gradient`, `power law`, `Haar`, `Gaussian
fluctuations`, `Bernoulli iteration count`, and the explicit binomial/Jacobi
form. No source stating the theorem in this record was located.

### Equivalence and stronger-result check

A generic delta-method observation that smooth functions of empirical moments
have Gaussian fluctuations is not, by itself, the stated result: the moment
range, deterministic power-law bias, exact influence function, finite variance
condition, and conversion to the discrete CG stopping law all have to align.
The closest general CG fluctuation literature establishes the mechanism in
other random-matrix ensembles, while the 2026 source paper for this exact
model stops at convergence in probability for fixed degree and uses different
heavy-tail asymptotics at its terminal floor.

The resulting theorem is therefore assessed **PASS to the best of our
knowledge** as a sharp refinement of the fixed-degree behavior in the specific
Haar power-law source model.

### Uninspected sources and residual risk

No specific inaccessible paper was identified as especially likely to contain
the same theorem. Residual risk comes from ordinary citation-index
incompleteness and from the possibility that an equivalent finite-moment delta
method appears under different Krylov/random-spectral-measure terminology.
This uncertainty is reflected in the qualified originality claim.

## Value audit

The result identifies the previously unresolved behavior at exact interior
fixed-degree tolerance curves: rather than an almost-deterministic single
iteration count, CG has a sharp two-point limit with equal mass on adjacent
iterations. It also supplies an explicit variance and the precise finite
second-moment boundary \((4d+2)p<1\). This complements the terminal-floor
heavy-tail/Schur analysis of the recent phase-diagram result and links that
model to fluctuation-level average-case Krylov theory.

The contribution is narrower than a new global complexity theorem and does
not treat the heavy-tail critical boundary. Its value is a sharp local
asymptotic law and an explicit structural explanation, not a new worst-case
CG rate.
