# Equal spacing uniquely maximizes extreme-order correlation for every sample size on three equally likely atoms

## Finding
Let \(n\ge2\). Let \(X_1,\ldots,X_n\) be independent, each uniformly distributed on three distinct ordered real values \(x_1<x_2<x_3\). Write \(U_n=\min_i X_i\) and \(V_n=\max_i X_i\). Among all choices of the interior location \(x_2\) with the endpoints \(x_1,x_3\) fixed, the Pearson correlation \(\operatorname{Corr}(U_n,V_n)\) is **uniquely maximized** at the midpoint \(x_2=(x_1+x_3)/2\), for every integer \(n\ge2\).

Its sharp value is
\[
\rho_n^*=\frac{(a+b)^2-a}{b+3a-(a+b)^2},\qquad a=3^{-n},\quad b=(2/3)^n.
\]
In particular, \(\rho_2^*=8/19\), and \(\rho_3^*=1/4\). Strictness holds for every non-midpoint interior position. Affine transformations of all three support points do not affect the assertion.

## Assumptions and scope
The three atoms carry the **same probability** \(1/3\), the sample is drawn **with replacement**, and \(n\) is an arbitrary integer at least two. Endpoints are distinct; the middle point must be strictly between them. No statement is made about optimizing the probability weights, an important and different problem. The random minimum and maximum have strictly positive variances.

## Proof
Positive affine invariance normalizes the three support points to \(0,t,1\), with \(0<t<1\). Put \(a=3^{-n}\), \(b=(2/3)^n\), and \(w=t(1-t)\), so \(0<w\le1/4\), with equality only at \(t=1/2\). Define
\[
A=b(1-b),\quad B=a(1-a),\quad C=a(1-b),\quad D=ab,\quad F=(a-b)^2-a.
\]
Let \(H_1\) indicate that all observations lie in \(\{t,1\}\) and \(H_2\) that all equal \(1\). Let \(J_1\) indicate that some observation lies in \(\{t,1\}\) and \(J_2\) that some observation equals \(1\). Then \(U_n=tH_1+(1-t)H_2\) and \(V_n=tJ_1+(1-t)J_2\). Direct indicator probabilities and the fact that \(n\ge2\) give
\[
\begin{aligned}
\operatorname{Var}(U_n)&=At^2+B(1-t)^2+2Ct(1-t),\\
\operatorname{Var}(V_n)&=Bt^2+A(1-t)^2+2Ct(1-t),\\
\operatorname{Cov}(U_n,V_n)&=D+Fw.
\end{aligned}
\]
The within-minimum indicator covariance is \(\operatorname{Cov}(H_1,H_2)=a(1-b)\), and the within-maximum indicator covariance is \(\operatorname{Cov}(J_1,J_2)=a(1-b)\); the cross-event covariances are \(\operatorname{Cov}(H_1,J_2)=b^2-a\) and \(\operatorname{Cov}(H_2,J_1)=a^2\), giving the displayed covariance. Multiplying the two variances and simplifying yields
\[
\operatorname{Var}(U_n)\operatorname{Var}(V_n)=AB+Lw+Kw^2,
\]
where
\[
L=2a(a-b)(b-1)(a-b-1),\qquad K=(a-b)^2(a-b+1)^2.
\]
Thus the squared correlation \(R(w)\) equals
\[
R(w)=\frac{(D+Fw)^2}{AB+Lw+Kw^2}.
\]
We prove strict monotonicity in \(w\) over the entire admissible interval. First \(F\ge0\): this is the inequality \((2^n-1)^2\ge3^n\), with equality when \(n=2\); the ratio \((2^{n+1}-1)/(2^n-1)>2>\sqrt3\) implies strictness at larger integers. Hence \(D+Fw>0\).

Differentiation gives
\[
R'(w)=\frac{(D+Fw)(H_0+H_1w)}{(AB+Lw+Kw^2)^2},\quad H_0=2FAB-DL,\quad H_1=FL-2DK.
\]
The numerator sign is determined by the affine function \(H_0+H_1w\). We verify it is positive at both endpoints of \([0,1/4]\). Factoring,
\[
H_0=2ab(1-b)(a^2-ab-a+b^2).
\]
Since \(b\le4/9\), \(a/b^2=(3/4)^n\le9/16\), and \(a^2-ab-a+b^2\ge b^2-a(1+b)\), we obtain
\[
a^2-ab-a+b^2\ge b^2\bigl(1-\tfrac9{16}(1+\tfrac49)\bigr)=\frac{3b^2}{16}>0.
\]
For the other endpoint, elementary polynomial expansion gives
\[
H_0+\frac{H_1}{4}=\frac a2\left[2b^3(1-b)-ab(1-b)(3-2b)-a^2b(1-b)-a^2(1-a)^2\right].
\]
Using \(a\le(9/16)b^2\), \((1-a)^2\le1\), and \(b\le4/9\), the bracket is at least \(b^3(1-b)\) times
\[
2-\frac9{16}(3-2b)-\frac{81}{256}\left(b^2+\frac{b}{1-b}\right)
=\frac{81b^3-369b^2+127b+80}{256(1-b)}.
\]
The numerator is strictly positive, since \(81b^3\ge0\) and \(-369b^2\ge-164b\) imply it is at least \(80-37b>0\). Both endpoint values are positive; therefore the affine derivative factor is positive for every \(w\in[0,1/4]\). Thus \(R(w)\) is strictly increasing, as is the positive correlation.

The unique maximum of \(w=t(1-t)\) is \(1/4\), attained only at \(t=1/2\), proving unique equal-spacing optimality. At this point each variance equals \([b+3a-(a+b)^2]/4\), and covariance equals \([(a+b)^2-a]/4\); their quotient gives the claimed \(\rho_n^*\). Every inequality above holds for all integers \(n\ge2\), without truncation.

## Verification
The included `checker.py` independently computes the moment formulas from the four indicator-event probabilities using exact rational arithmetic; compares those formulas with explicit enumeration for sample sizes \(2\le n\le7\); checks the endpoint derivative identities over \(2\le n\le70\); and compares the closed-form optimizers with exact finite-grid support positions. These finite checks are reproducibility aids only. The preceding algebra and endpoint inequalities prove the infinite family.

Run `python checker.py` with the Python standard library. No additional files or dependencies are required.

## Relationship to prior work
Papadatos, *A discrete analogue of Terrell's characterization of rectangular distributions*, arXiv:2205.14360v1 (2022), proves equal-spacing extremality for two draws on any finite equally weighted support and poses related discrete correlation questions. The present theorem treats **every number of draws** on **exactly three equally weighted atoms**, a different parameter regime that does not follow from the two-draw result alone. Classical upper bounds for extreme-order correlation over arbitrary distributions likewise need not identify the optimizer within the constrained three-atom family.

Earlier published findings optimized the **probability masses with equally spaced support fixed**: one establishes uniform masses for two draws, and another shows uniform masses fail to be locally extremal from three draws onward. These do not determine the optimal interior **support location with masses fixed equal**. The present statement should not be interpreted as optimality when both masses and positions vary.

## Limitations
This is a constrained, exact three-atom classification. It does not optimize unequal weights or four or more support points, or establish historical priority beyond the sources checked. No independent scientific audit has been conducted.

## References
1. N. Papadatos, *A discrete analogue of Terrell's characterization of rectangular distributions*, arXiv:2205.14360v1 (public May 28, 2022), https://arxiv.org/abs/2205.14360.
2. published-finding corpus, *Sharp min-max correlation over three-point probability weights*, ID `2026/9/20/SCOPE-uniform-maximizes-three-point-minmax-correlation--92f0f4188ee4`.
3. published-finding corpus, *Sample size two is the exact boundary for three-point uniform-probability extremality*, ID `2026/10/4/SCOPE-sample-size-two-is-the-exact-boundary-for-three-point-uniform-pr--200fa86d60cb`.
4. published-finding corpus, *A three-draw counterexample to uniform-probability extremality for discrete order-statistic correlation*, ID `2026/10/4/SCOPE-a-three-draw-counterexample-to-uniform-probability-extremality-f--72e2dab2ac87`.
