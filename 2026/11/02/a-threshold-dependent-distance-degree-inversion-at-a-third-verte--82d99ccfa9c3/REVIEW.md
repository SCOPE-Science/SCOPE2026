# Scientific review of third-vertex distance–degree inversion

## Correctness — PASS

The statement carefully separates three fixed distinct labels, all conditional boundary lengths, and fixed integer high-degree thresholds. Conditioning on a specified path produces a rooted forest whose Laplacian determinant is \(m n^{r-1}\). A marked-root determinant gives the binomial-plus-Bernoulli offspring law; a marked-nonroot determinant gives the shifted binomial law. The path-membership mixture proves the exact degree law. The leaf monotonicity and opposite tail inequalities at the terminal two path lengths are algebraic. At the fluctuation scale \(L/\sqrt n\), the independent order-\(n^{-1/2}\) contributions cancel; second-order expansion and a Rayleigh exponential tail bound yield the stated limiting covariance constants. The standalone program passed 11,422 exact-or-numerical checks, including exhaustive trees through eight vertices. Its finite experiments are corroboration, not the basis for the infinite proof.

## Originality — PASS (best-knowledge, with residual historical risk)

The closest published mathematical record treats degree at an **endpoint**, where the conditional law is binomial plus Bernoulli and stochastically *decreasing* in distance. It also implies the third-vertex conditional **mean** through the deterministic sum of all vertex degrees. Accordingly the mean formula is expressly not a separately novel result. Pitman's coalescent-forest work establishes the extension formulas, and Aldous–Pitman's spanning-subtree formula covers path inclusion; neither inspected full text states the **third-vertex conditional degree distribution** or the **high-threshold negative covariance with exact \(n^{-1/2}\) coefficient**. The new conclusion genuinely distinguishes mean regression from threshold regression. Broader forest enumerations could potentially conceal an implicit equivalent; absence from checked sources is not an absolute priority certificate.

## Mathematical value — PASS

The distinction between measuring degree *at* a path endpoint and at a *third* labeled vertex matters in random network sampling. The exact joint law identifies the mechanism by which a longer path makes the third vertex more likely to lie on it while reducing external offspring. At first order those effects cancel, leading to positive association with nonleaf status but negative covariance with fixed degree thresholds of at least four. That simultaneous contrast and its sharp asymptotic coefficients are a structural, motivated dependence boundary, rather than a routine calculation of a single covariance.

## Closest literature and limitations

Primary background is Pitman, *Coalescent Random Forests*, Berkeley Report 457 (first catalog date 1996-09-01), whose full-text enumeration establishes rooted and unrooted forest counts; Aldous–Pitman, *A Family of Random Trees with Random Edge Lengths*, Berkeley Report 526 (1998), with a general spanning-subtree formula; and the published endpoint-degree/distance result linked in `RESULT.md`. The complete open text of Berzunza Ojeda–Janson on simply generated tree distance profiles was inspected for neighboring conditioning results. The theorem is specific to uniform labeled trees, yields eventual rather than explicit finite cutoffs at high thresholds, and makes no \(q=3\) sign claim.

Self-review: passed. Independent audit: not yet performed.
