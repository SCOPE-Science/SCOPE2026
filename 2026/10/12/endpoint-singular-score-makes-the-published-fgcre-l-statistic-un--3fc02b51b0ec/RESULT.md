# Endpoint-singular score makes the published FGCRE L-statistic undefined
## Finding
Alqefari (2026) defines the score
\[
J_\beta(u)=\frac{[-\log(1-u)]^{\beta-1}}{\Gamma(\beta+1)}\,[\beta+1+\log(1-u)],\qquad 0<u<1,
\]
and then prints the empirical statistic
\[
\widehat{\mathbb T}_\beta=\frac1n\sum_{i=1}^n J_\beta\!\left(\frac{i}{n}\right)X_{(i)}.
\]
For every \(\beta>0\), the last weight is outside the stated domain and has divergent left limit:
\[
\lim_{u\uparrow1}J_\beta(u)=-\infty.
\]
Consequently, the empirical statistic in equation (7) is not a finite statistic as written. Under the exponential null, \(X_{(n)}>0\) almost surely, so the natural extended-real interpretation gives \(\widehat{\mathbb T}_\beta=-\infty\).

The exact-null representation in equations (9)–(10) is affected at the same point. Each coefficient
\[
b_{r,n}=\frac1{n-r+1}\sum_{i=r}^nJ_\beta\!\left(\frac{i}{n}\right)
\]
contains \(J_\beta(1)\), hence is undefined. Therefore the finite-sample distribution in Theorem 3.1 cannot be the distribution of the statistic defined by the displayed formulas without an unstated endpoint regularization.

A second obstruction shows that replacing \(i/n\) by interior plotting positions does not automatically validate the theorem for the full advertised range \(\beta>0\). The paper's Remark 3.1 says that \(J_\beta\) is strictly monotone. For \(\beta>1\) this is false: after writing \(v=-\log(1-u)>0\),
\[
J_\beta(u)=\frac{v^{\beta-1}(\beta+1-v)}{\Gamma(\beta+1)},
\]
and
\[
\frac{d}{dv}\left[v^{\beta-1}(\beta+1-v)\right]
=v^{\beta-2}(\beta^2-1-\beta v).
\]
Thus the score increases for small \(v\) and decreases for large \(v\) whenever \(\beta>1\).

## Assumptions and scope
The claim concerns the formulas printed in equations (6)–(10) and Remark 3.1 of the cited 2026 article. No assertion is made about unpublished code or about a different statistic obtained by replacing \(i/n\) with an interior plotting position such as \(i/(n+1)\).

The endpoint conclusion holds for every integer \(n\ge1\), every \(\beta>0\), and every sample with \(X_{(n)}>0\). In particular, it holds almost surely under every exponential law on \((0,\infty)\).

## Proof
Put
\[
v=-\log(1-u).
\]
Then \(v\to\infty\) as \(u\uparrow1\), and equation (6) becomes
\[
J_\beta(u)=\frac{v^{\beta-1}(\beta+1-v)}{\Gamma(\beta+1)}.
\]
Since \(\Gamma(\beta+1)>0\) and
\[
v^{\beta-1}(\beta+1-v)=-v^\beta\left(1-\frac{\beta+1}{v}\right),
\]
the score tends to \(-\infty\) for every \(\beta>0\).

Equation (7) evaluates the score at \(u=i/n\). The term with \(i=n\) is therefore \(J_\beta(1)X_{(n)}\), although equation (6) defines \(J_\beta\) only for \(0<u<1\). Under the exponential null, \(X_{(n)}>0\) almost surely. Hence the displayed statistic is undefined; if one extends the score by its left limit, the statistic equals \(-\infty\).

The spacing coefficients in equation (9) satisfy
\[
b_{r,n}=\frac1{n-r+1}\sum_{i=r}^nJ_\beta\!\left(\frac{i}{n}\right),
\]
so every one of them contains the same endpoint term \(J_\beta(1)\). The coefficients required by Theorem 3.1 are therefore not finite, and the product formula in equation (10) is not a distribution formula for the printed statistic.

Finally, differentiating the interior score with respect to \(v\) gives
\[
\frac{dJ_\beta}{dv}
=\frac{v^{\beta-2}}{\Gamma(\beta+1)}(\beta^2-1-\beta v).
\]
Because \(dv/du=(1-u)^{-1}>0\), the same sign controls monotonicity in \(u\). For \(0<\beta\le1\), the score is strictly decreasing. For \(\beta>1\), it rises until
\[
v=\beta-\frac1\beta
\]
and falls thereafter. This directly contradicts the all-\(\beta\) strict-monotonicity statement in Remark 3.1.

## Verification
The source PDF was inspected at the score definition, empirical statistic, spacing representation, exact-null theorem, and monotonicity remark. Equation (6) states the domain \(0<u<1\); equation (7) nevertheless uses \(J_\beta(i/n)\) through \(i=n\); equation (9) repeats the same endpoint evaluation inside every \(b_{r,n}\). Theorem 3.1 then assumes finite pairwise-distinct coefficients, and Remark 3.1 attempts to justify distinctness by a strict-monotonicity claim.

The endpoint limit and derivative calculation above are exact symbolic identities. No numerical experiment is used as proof. The paper also reports finite simulated and applied values of the proposed statistic, so those computations necessarily use some convention other than the displayed equation (7), but the present claim does not infer which convention was used.

## Relationship to prior work
The target article cites classical L-statistic and normalized-spacing theory, including Stigler (1974) and Box (1954). Those results can support a finite weighted order-statistic or spacing statistic once its deterministic coefficients are well defined; they do not define the singular endpoint weight in equation (7).

A later 2026 entropy-based exponentiality paper uses a related scale-free L-statistic framework and also discusses interior weighting choices, but it does not constitute a correction to DOI 10.3934/math.2026519. Focused database and web searches for the exact DOI, the score formula, endpoint singularity, undefined \(J_\beta(1)\), and corrigenda did not locate a published correction or an equivalent diagnosis.

## Limitations
This finding does not show that no finite statistic inspired by the population functional can be constructed. Replacing the empirical endpoint by interior plotting positions, truncating the score, or otherwise regularizing the endpoint could produce a valid finite statistic, but each such choice defines a different procedure whose null distribution must be derived and whose coefficient distinctness must be checked separately.

No claim is made about the correctness of numerical tables produced from undocumented code, except that finite reported values cannot arise from equation (7) literally evaluated with \(i=n\).

## References
1. A. A. Alqefari, “Exact and entropy-based nonparametric tests for exponentiality against increasing failure rate alternatives,” AIMS Mathematics 11 (2026), 12621–12649. DOI: 10.3934/math.2026519.
2. S. M. Stigler, “Linear functions of order statistics with smooth weight functions,” The Annals of Statistics 2 (1974), 676–693. DOI: 10.1214/aos/1176342756.
3. G. E. P. Box, “Some theorems on quadratic forms applied in the study of analysis of variance problems, I,” The Annals of Mathematical Statistics 25 (1954), 290–302. DOI: 10.1214/aoms/1177728786.
