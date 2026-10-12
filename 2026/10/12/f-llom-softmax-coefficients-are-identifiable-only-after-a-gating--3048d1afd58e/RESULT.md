# F-LLoM softmax coefficients are identifiable only after a gating normalization
## Finding
The F-LLoM model uses covariate-dependent softmax tier probabilities
\[
\pi_m(x)
=
\frac{\exp(\alpha_m+x^\top\beta_m)}
{\sum_{j=1}^M\exp(\alpha_j+x^\top\beta_j)},
\qquad m=1,\ldots,M.
\]
Proposition 3 states that, when the component parameters are pairwise distinct and the gating functions vary nondegenerately with covariates, the model parameters are identifiable up to label switching.

For the gating coefficients as written, there is an additional exact nonidentifiability. For every
\[
u=(c,d)\in\mathbb R^{p+1},
\]
apply the same affine shift to every tier,
\[
\alpha_m'=\alpha_m+c,
\qquad
\beta_m'=\beta_m+d.
\]
Then
\[
\pi_m'(x)
=
\frac{e^{c+x^\top d}e^{\alpha_m+x^\top\beta_m}}
{e^{c+x^\top d}\sum_j e^{\alpha_j+x^\top\beta_j}}
=
\pi_m(x)
\]
for every tier and every covariate value. Therefore the full conditional distribution is unchanged although the coefficient vector has moved along a continuous \((p+1)\)-dimensional orbit. This is not label switching.

The ambiguity can be classified exactly. Assume the covariate support affinely spans \(\mathbb R^p\). If two softmax coefficient systems produce the same gate probabilities, then for each \(m<M\),
\[
\log\frac{\pi_m(x)}{\pi_M(x)}
=
(\alpha_m-\alpha_M)+x^\top(\beta_m-\beta_M).
\]
Equality of the gate probabilities on an affinely spanning set therefore forces
\[
\alpha_m'-\alpha_M'=\alpha_m-\alpha_M,
\qquad
\beta_m'-\beta_M'=\beta_m-\beta_M.
\]
Thus there is a single common shift \((c,d)\) such that
\[
\alpha_m'=\alpha_m+c,
\qquad
\beta_m'=\beta_m+d
\]
for every tier. The common affine shift is the entire softmax representation ambiguity under full affine rank.

A reference-tier normalization such as
\[
\boxed{\alpha_M=0,\qquad\beta_M=0}
\]
removes this ambiguity. Equivalent choices include any \(p+1\) independent constraints selecting one representative from each common-shift orbit. Under the reference normalization and full affine covariate rank, the gating coefficients are uniquely identified from the gate probabilities.

Consequently, an unconstrained F-LLoM likelihood has at least \(p+1\) exact flat directions in its gating block. Wherever the log-likelihood is twice differentiable, the observed-information Hessian is singular along those directions. This is exact parameter redundancy, not merely weak finite-sample separation.

The article's numerical implementation appears already to use the normalized convention. In Table 2, the second tier is labeled the baseline and its gating intercept and slope are reported as zero. The BIC table supplies an independent parameter-count check. In the one-covariate simulation, the source uses
\[
\operatorname{BIC}=-2\ell+p_M\log n.
\]
For \(n=500\) and censoring rate \(0.10\), the displayed log-likelihoods and BIC values imply free-parameter counts
\[
\boxed{p_M=3,8,13,18\quad\text{for }M=1,2,3,4.}
\]
These are exactly
\[
3M+2(M-1),
\]
namely three component parameters per tier plus two gating coefficients only for the \(M-1\) nonbaseline tiers. They are not the counts from an unconstrained \(M\)-logit parameterization.

The correction is therefore to state Proposition 3 on a normalized gating parameter space, or equivalently on the quotient by common affine shifts. This repairs the gating obstruction while leaving the source's separate finite-mixture component argument and ordinary label switching to be handled under their stated assumptions.

## Assumptions and scope
There are \(M\ge2\) mixture components. The gate uses an intercept and \(p\) covariates, so each gating coefficient block has dimension \(p+1\).

The exact classification of the common-shift ambiguity assumes that the covariate support has full affine rank. If the design lies in a proper affine subspace, further coefficient directions can be unidentifiable.

The finding corrects the parameter-identifiability statement for the gate. It does not independently re-prove every finite-mixture identifiability step for the Lomax components.

The numerical evidence about Table 1 and Table 2 is used only to show that the article's implementation is consistent with a baseline-normalized gate. The mathematical counterexample does not depend on those tables.

## Proof
Write the augmented covariate vector as
\[
\widetilde x=(1,x^\top)^\top
\]
and the tier coefficient vector as
\[
g_m=(\alpha_m,\beta_m^\top)^\top.
\]
Then
\[
\pi_m(x)=\frac{e^{\widetilde x^\top g_m}}{\sum_j e^{\widetilde x^\top g_j}}.
\]
For any common vector \(u\in\mathbb R^{p+1}\), replacing every \(g_m\) by \(g_m+u\) multiplies numerator and denominator by the same factor \(e^{\widetilde x^\top u}\). All gates are therefore unchanged.

This proves nonidentifiability of the unconstrained coefficient representation. The source's condition that the coefficient vectors are not all identical does not remove it: adding a common vector preserves every pairwise difference \(g_m-g_j\).

For the converse, suppose \(\pi_m'(x)=\pi_m(x)\) for every tier and every \(x\) in an affinely spanning set. Taking log-odds relative to tier \(M\) gives
\[
\widetilde x^\top(g_m'-g_M')
=
\widetilde x^\top(g_m-g_M)
\]
for each \(m<M\). Full affine rank implies
\[
g_m'-g_M'=g_m-g_M.
\]
Setting \(u=g_M'-g_M\) yields
\[
g_m'=g_m+u
\]
for all \(m\). Hence common translation is exactly the ambiguity.

If the reference constraint \(g_M=0\) is imposed in both representations, then \(u=0\), so all gate coefficients are equal. Thus the gate is identified after normalization, subject to full affine rank.

Finally, let \(\ell(g_1,\ldots,g_M,\ldots)\) denote any observed log-likelihood depending on the gating coefficients only through the softmax probabilities. For every \(u\),
\[
\ell(g_1+u,\ldots,g_M+u,\ldots)
=
\ell(g_1,\ldots,g_M,\ldots).
\]
Differentiating along any common-shift direction shows zero score and, where a Hessian exists, a zero Hessian action. There are at least \(p+1\) linearly independent such directions.

## Verification
The included checker evaluates a three-tier softmax at several covariate points, applies a nonzero common affine shift, and verifies equality of every gate probability and of a representative mixture density.

It then verifies the converse numerically through log-odds: after reference normalization, the original coefficients are recovered from the gate log-ratios on a full-rank covariate design.

The checker also reconstructs the parameter counts implicit in the source's Table 1 BIC values. For the \(n=500\), censoring-rate \(0.10\) block it obtains values within rounding error of \(3,8,13,18\), matching \(3M+2(M-1)\).

The computations illustrate the exact algebra. The common-shift invariance and its converse are proved analytically above.

## Relationship to prior work
The F-LLoM article explicitly defines all \(M\) softmax logits in Proposition 3 and calls the full model identifiable up to label switching when the gating coefficients are not all identical. That condition does not eliminate the common affine shift.

Standard mixture-of-experts implementations impose a baseline category precisely to remove this softmax redundancy. For example, a 2026 softmax-gated mixture-of-experts treatment sets the final gate coefficient vector identically to zero for identifiability and estimates only the \(K-1\) nonbaseline blocks.

The F-LLoM article's own simulation output follows that normalized practice: Table 2 reports the second tier as a zero gate baseline, and the BIC values imply the baseline-normalized number of free parameters. Thus the theoretical statement and the numerical implementation can be reconciled by adding the missing normalization to Proposition 3.

A previous result concerning the same F-LLoM source studies its tail asymptotics and extreme-survivor tier localization. Those statements concern the already-defined gate probabilities and do not imply, or repair, the coefficient-level softmax nonidentifiability addressed here.

Focused searches using the exact DOI, F-LLoM name, Proposition 3, softmax identifiability, common-shift, baseline-category, and mixture-of-experts aliases did not locate a published source-specific correction.

## Limitations
The correction establishes the gating-parameter obstruction and its exact quotient under full affine covariate rank. It does not independently certify every component-mixture identifiability assertion in the source.

A rank-deficient covariate design can create additional coefficient nonidentifiability beyond the common shift.

The article's tables strongly indicate that its computations used a baseline normalization, but the source does not state that normalization in Proposition 3 itself.

A recent unindexed correction could exist outside the sources examined.

## References
1. M. Rahmouni, “Frailty-Augmented Logistic-Weighted Lomax Mixture regression for survival analysis,” AIMS Mathematics 11 (2026), 6329–6349. DOI: 10.3934/math.2026261.
2. J.-Y. Chen, M.-C. Chang, M. Yang, and J. Stufken, “Efficient and Interpretable Mixtures of Experts: Statistical Inference, Initialization, and Applications,” Journal of Statistical Theory and Practice 20 (2026), article 127. DOI: 10.1007/s42519-026-00646-4.
