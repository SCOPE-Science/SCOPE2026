# Same-model review

**Verdict:** PASS.

Same-model review: passed. Independent audit: not yet performed.

## Correctness

The central identity was rederived directly from the map. At a synchronized state \(z\mathbf1\), row-regularity makes every exponential factor equal, and the Jacobian is
\[
e^{r-cz}(I-zA).
\]
Along a periodic scalar orbit, the exponential prefactors telescope and every remaining factor is a polynomial in the single matrix \(A\). This gives the exact monodromy polynomial
\[
P_p(A)=\prod_k\left(I-\frac{w_k}{c}A\right).
\]
Polynomial spectral mapping then gives all Floquet multipliers without any diagonalizability assumption on \(A\).

The closed-left-half-plane obstruction is strict for every nonzero \(\lambda\) with \(\operatorname{Re}\lambda\le0\), since
\[
|1-t\lambda|^2=1-2t\operatorname{Re}\lambda+t^2|\lambda|^2>1
\]
for each \(t>0\).

The all-to-all \(a=1\) boundary was checked separately: identical matrix rows give a common multiplicative update factor, so component ratios are exact invariants and the synchronous orbit cannot attract nearby nonsynchronous rays.

As an algebraic stress test, the formula was also checked on a nonsymmetric nonnegative \(3\times3\) row-regular matrix with a complex-conjugate eigenvalue pair and a scalar Ricker 2-cycle; direct multiplication of the two Jacobians agreed with \(P_2(A)\) to floating-point precision and the computed multiplier sets agreed.

## Originality

The literature search covered exact and synonymous formulations involving Ricker competition, periodic cycles, synchronous solutions, Floquet multipliers, interaction-matrix spectra, row-regular matrices, and master-stability reductions.

Prior art found and incorporated into the statement includes:

- Jiang–Rogers (1987): symmetric planar competition and low-period bifurcations.
- Luís–Elaydi–Oliveira (2011): two-species Ricker stability/bifurcation analysis and Jacobian products for exclusion periodic cycles.
- Ackleh–Salceanu (2015): \(n\)-species exclusion/persistence with potentially complex interior coexistence dynamics.
- Gyllenberg–Jiang–Niu–Yan (2019): three-species classification plus numerical higher-period/chaotic Ricker dynamics.
- Hou (2020): the broader multiplicative population-map class \(x_iG_i((Ax)_i)\), focused on global attraction and fixed points.
- Ryals–Sacker (2022): Lyapunov-exponent stability for coupled almost-periodic Ricker maps with an \(N\)-dimensional extension under coupling restrictions.
- General discrete master-stability theory: decomposition of synchronization stability into coupling eigenmodes.

No inspected source stated the exact row-regular competition-matrix identity
\[
D F_A^p=P_p(A)
\]
for synchronous multispecies Ricker cycles, nor the resulting theorem that any nonzero competition eigenvalue in the closed left half-plane forces every positive synchronous period to be unstable.

The originality claim is therefore limited to this model-specific exact reduction and its consequences. It does not claim novelty for synchronization eigenmode decompositions, planar symmetric periodic-orbit analysis, or Jacobian-product stability in general.

### Residual coverage risk

The full theorem-level text of Jiang–Rogers (1987) was not inspected; its abstract confirms detailed symmetric planar periodic-point analysis. Ryals–Sacker (2022) was inspected through its abstract, figures, references and accessible page text, but its full theorem text was not available in the consulted source. The accepted manuscript of Gyllenberg et al. (2019) was represented by an abstract and indexed excerpts but was not fully inspected. These are the most plausible sources for an equivalent special case or related formulation.

## Value

The result turns an \(n\)-dimensional Floquet product along an arbitrary positive synchronous \(p\)-cycle into one scalar polynomial evaluated on the interaction spectrum. This is reusable across periods and dimensions, permits nonsymmetric competition matrices with complex eigenvalues, and yields a period-independent exclusion region in spectral space. The broader \(x_iG((Ax)_i)\) identity shows that the commuting-polynomial mechanism is structural rather than an isolated algebraic coincidence.

The claim is intentionally narrower than the broad problem of periodic multispecies Ricker dynamics. It does not address nonsynchronous cycles or global attraction, but it gives an exact solution for the row-regular synchronous sector.

## Search/access limitations

Originality is to the best of our knowledge, not an exhaustive guarantee. Search engines and repository indexing can miss equivalent terminology. The partially inspected papers named above remain the main literature uncertainty. No inaccessible source was treated as evidence of non-coverage.
