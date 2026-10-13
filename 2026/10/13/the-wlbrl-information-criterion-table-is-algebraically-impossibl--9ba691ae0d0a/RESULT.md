# The WLBRL information-criterion table is algebraically impossible
## Finding
The 2026 weighted length-biased Ramos–Louzada model is defined by a density depending on
\[
(\beta,\lambda,k).
\]
The source's simulation Table 1 estimates all three quantities, and its conclusion explicitly describes the extension as having two parameters from the base distribution plus one weighted parameter.

Hence the WLBRL distribution has three fitted distributional parameters in the likelihood comparison:
\[
p=3.
\]

Let
\[
Q=-2\log\widehat L
\]
denote the reported maximized deviance. The ordinary information criteria must then be
\[
\operatorname{AIC}=Q+2p
\]
and
\[
\operatorname{BIC}=Q+p\log n.
\]

For dataset 1, the source states that there are \(n=33\) leukemia survival observations and Table 5 reports
\[
Q=549.37,\qquad
\operatorname{AIC}=537.65,\qquad
\operatorname{BIC}=528.92.
\]
But with any positive parameter count, AIC must exceed \(Q\), and for \(n>1\) BIC must also exceed \(Q\). Both printed values are instead smaller.

Using the source's actual three-parameter WLBRL model gives
\[
\boxed{\operatorname{AIC}=555.37}
\]
and
\[
\boxed{\operatorname{BIC}=559.8595226844\ldots}.
\]

For dataset 2, the source states that there are \(n=60\) observations and Table 5 reports
\[
Q=410.34,\qquad
\operatorname{AIC}=411.28,\qquad
\operatorname{BIC}=399.20.
\]
The AIC difference is only
\[
411.28-410.34=0.94,
\]
which would require the impossible parameter count
\[
p=0.47.
\]
The printed BIC is again below \(Q\).

For \(p=3\), the values implied by the reported likelihood are
\[
\boxed{\operatorname{AIC}=416.34}
\]
and
\[
\boxed{\operatorname{BIC}=422.6230336867\ldots}.
\]

The inconsistency cannot be resolved by using the paper's later Table 6 statement that WLBRL has two distributional parameters. If \(p=2\), dataset 1 would instead give
\[
\operatorname{AIC}=553.37,\qquad
\operatorname{BIC}=556.3630151229\ldots,
\]
and dataset 2 would give
\[
\operatorname{AIC}=414.34,\qquad
\operatorname{BIC}=418.5286891244\ldots.
\]
None equals the Table 5 values.

Thus the Table 5 AIC and BIC columns are algebraically incompatible with the table's own \(-2\log L\) values under either parameter count stated elsewhere in the article.

If the conventional finite-sample correction
\[
\operatorname{AICc}
=
\operatorname{AIC}
+
\frac{2p(p+1)}{n-p-1}
\]
is used with \(p=3\), the values implied by the reported likelihoods are
\[
556.1975862069\ldots
\]
for dataset 1 and
\[
416.7685714286\ldots
\]
for dataset 2, rather than the printed \(537.80\) and \(410.33\).

The AICc convention is not needed for the main conclusion: the AIC and BIC contradictions follow directly from their defining penalties.

## Assumptions and scope
The calculation treats the column labeled \(-2\log L\) in Table 5 as the quantity stated by that label and treats the three WLBRL quantities fitted throughout the distributional analysis, \(\beta\), \(\lambda\), and \(k\), as free distributional parameters.

The result does not reconstruct the underlying raw maximum likelihood fit, so it does not assert that the printed \(-2\log L\) values are themselves correct.

The result also does not recompute information criteria for the PINN, whose effective complexity may require a different accounting than an ordinary three-parameter likelihood model.

The standard AIC and BIC inconsistency is independent of the AICc convention.

## Proof
The source's WLBRL density contains \(\beta\), \(\lambda\), and the weight exponent \(k\). Its simulation Table 1 reports estimates of all three, and its conclusion describes exactly two base-distribution parameters plus a single weighted parameter. Therefore
\[
p=3.
\]

For any maximized likelihood \(\widehat L\), Akaike's criterion is
\[
\operatorname{AIC}
=
-2\log\widehat L+2p.
\]
Writing
\[
Q=-2\log\widehat L
\]
gives
\[
\operatorname{AIC}-Q=2p.
\]
For every model with \(p>0\), this difference is strictly positive.

Schwarz's criterion is
\[
\operatorname{BIC}
=
-2\log\widehat L+p\log n,
\]
so
\[
\operatorname{BIC}-Q=p\log n>0
\]
whenever \(p>0\) and \(n>1\).

Dataset 1 violates both necessary inequalities:
\[
537.65<549.37
\]
and
\[
528.92<549.37.
\]

Dataset 2 violates the BIC inequality:
\[
399.20<410.34.
\]
Its AIC difference,
\[
0.94,
\]
is positive but cannot equal \(2p\) for any positive integer parameter count. In particular, it is neither the \(4\) penalty implied by the source's Table 6 count nor the \(6\) penalty implied by the actual three-parameter density.

Substitution of \(p=3\) and \(n=33,60\) yields the corrected AIC/BIC numbers displayed above.

## Verification
The bundled checker reads the two Table 5 WLBRL rows as constants, evaluates AIC and BIC for both \(p=2\) and \(p=3\), and verifies that none of those values equals the printed criteria.

It also verifies the necessary inequalities
\[
\operatorname{AIC}>-2\log\widehat L
\]
and
\[
\operatorname{BIC}>-2\log\widehat L
\]
for positive parameter count and \(n>1\), showing that three of the four printed AIC/BIC entries fail even this minimal check.

Finally, it evaluates the conventional AICc expression for \(p=3\). These arithmetic checks supplement the defining identities and do not depend on numerical optimization.

## Relationship to prior work
The primary article itself supplies every ingredient needed for the contradiction: a three-parameter WLBRL density, three estimated WLBRL parameters in Table 1 and Table 5, the sample sizes, the \(-2\log L\) column, and the AIC/BIC columns. It then uses those criteria as evidence that WLBRL gives a superior real-data fit.

The same article later labels WLBRL as a two-parameter model in Table 6, but substituting \(p=2\) still does not reproduce Table 5. The parameter-count inconsistency therefore cannot explain away the information-criterion arithmetic.

Akaike's and Schwarz's criteria supply the defining likelihood penalties. Hurvich and Tsai provide the standard small-sample corrected-AIC framework. Focused searches using the article DOI, model acronym, Table 5 values, information-criterion terminology, and parameter-count aliases did not locate a published correction of the source table.

## Limitations
The corrected AIC and BIC values are conditional on the source's printed \(-2\log L\) values being the intended maximized deviances.

The conventional AICc numbers are included as an additional consistency check; the main result does not require a particular AICc formula.

The result does not determine whether recomputation would preserve or reverse every model ranking because the competing-model likelihoods and complexity accounting would also need to be validated consistently.

A recent or unindexed correction could exist outside the material examined.

## References
1. M. M. AL Sobhi, “Physics-informed weighted Ramos–Louzada model: integrating statistical and physical constraints for survival analysis,” AIMS Mathematics 11 (2026), 6777–6803. DOI: 10.3934/math.2026280.
2. H. Akaike, “Information theory and an extension of the maximum likelihood principle,” in Breakthroughs in Statistics, Springer reprint. DOI: 10.1007/978-1-4612-0919-5_38.
3. G. Schwarz, “Estimating the Dimension of a Model,” The Annals of Statistics 6 (1978), 461–464. DOI: 10.1214/aos/1176344136.
4. C. M. Hurvich and C.-L. Tsai, “Regression and time series model selection in small samples,” Biometrika 76 (1989), 297–307. DOI: 10.1093/biomet/76.2.297.
