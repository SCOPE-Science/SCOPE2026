# Review — zero-residual false positives in projected certification

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** For the explicit family
\[
H=\operatorname{diag}(0,0,M),\qquad A=[1,0,0],\qquad X=\varnothing,
\]
the constrained feasible space is \(\operatorname{span}\{e_2,e_3\}\) and its maximum Rayleigh quotient is exactly \(M\). The penalized matrix is \(\operatorname{diag}(-\rho,0,M)\), so its dominant eigenvalue is also exactly \(M\) for every positive penalty. At the wrong feasible eigenvector \(e_2\), the penalized eigen-residual, feasibility residual, projected KKT residual, and inter-level projected-value change are all identically zero. The accepted value is nevertheless zero, with error \(M\).

The shifted/scaled inner operator is \(\operatorname{diag}(0,\rho/(M+\rho),1)\) under the paper's conservative bounds. Hence \(e_2\) is a positive-eigenvalue non-dominant eigenvector. The public Split–Merge code stops when its eigenvector residual vanishes and documents nonorthogonality to the dominant eigenvector as an input condition. The Split–Merge convergence theorem also requires nonzero dominant overlap, whereas the displayed PSM Algorithm 1 states only a unit-norm initialization.

The nearby family \(u_\delta=\sqrt{1-\delta^2}e_2+\delta e_3\) independently verifies the semantic obstruction: its residual norm is \(M\delta\sqrt{1-\delta^2}\to0\) while its extremal-value error is \(M(1-\delta^2)\to M\). Thus the four stopping quantities alone cannot control extremal-value error.

The proposed repair is an immediate consequence of Rayleigh–Ritz and the paper's penalty duality: for feasible normalized \(\widehat u\),
\[
\widehat\theta\le\lambda_X^c\le\lambda_{\max}(M_\rho^{(X)})\le U_\rho.
\]
Therefore \(U_\rho-\widehat\theta\) is a genuine global value-error certificate whenever \(U_\rho\) is a validated upper enclosure of the penalized dominant eigenvalue.

The compact verification artifact reproduces the diagonal identities numerically.

## Originality

**PASS, to the best of our knowledge, with a narrow claim.** The general warning that a small eigenpair/Ritz residual does not identify an extreme eigenvalue is classical. Parlett's work on Lanczos misconvergence and the abstract of van Dorsselaer--Hochstenbach--van der Vorst explicitly document this phenomenon. The novelty claim is therefore not the general principle.

The source searched most closely was Wang and Xia's current public arXiv manuscript, which introduces the PSM stopping rule and describes the resulting runs as certified. No erratum, comment, or public source was located that gives the exact three-dimensional zero-residual PSM counterexample, points out the mismatch between PSM's unrestricted displayed initialization and Split–Merge's dominant-overlap hypothesis, proves the robust residual/error separation for the PSM tests, or supplies the penalty-duality extremality bracket stated here.

The full texts of Parlett (1990) and van Dorsselaer et al. (2001) were not inspected; their accessible abstracts are sufficient to establish that the general residual-versus-extremality issue is prior art. They remain a residual risk only for a more specific historical formulation of the repair, not for coverage of the 2026 PSM-specific construction.

The final journal version of Split–Merge cited by Wang and Xia as forthcoming was not separately inspected. The accessible arXiv v2 and public implementation both expose the dominant-overlap requirement relevant here. A later journal version could alter inner-solver details, but it cannot make the four PSM residual quantities themselves index-sensitive; the exact algebraic false-positive statement for those tests remains unchanged.

## Value

**PASS.** The source paper explicitly presents projected certification as the acceptance layer for a matrix-free constrained extremal eigensolver and counts runs satisfying it as certified. The counterexample shows that the stopping rule is only a stationarity/feasibility certificate unless the inner solver's spectral index is independently guaranteed. This distinction matters precisely in large-scale eigensolvers, where residual-based misconvergence is a classical numerical issue.

The result also gives a direct repair compatible with the paper's own penalty duality: supplement local residual checks with an upper enclosure for the penalized dominant eigenvalue. This separates convergence heuristics or random-start guarantees from a genuine a posteriori extremality certificate.

## Limitations

The exact bad initialization is orthogonal to the target and has probability zero under an absolutely continuous random start. No claim is made that random-start PSM fails with positive probability, or that the paper's penalty theorems are incorrect. The result addresses deterministic certification semantics and the stated Algorithm 1 input conditions. The nearby-vector family demonstrates residual insufficiency but does not establish that the implemented inner iteration reaches that family from generic random starts.
