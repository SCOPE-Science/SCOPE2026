# Exact Gaussian XNysTrace correlation and a vanishing-diagnostic variance cliff

## Finding

The original, **unnormalized Gaussian** XNysTrace leave-one-out estimates have a closed-form, positive pairwise correlation on the identity matrix. If \(n\ge2\), \(2\le m\le n\), and \(\nu=n-m+1\), their common correlation is
\[
\operatorname{Corr}(B_i,B_j)=\frac{1}{\nu+3}\quad(i\ne j).
\]
The averaged absolute-error mean square and expected reported squared-error diagnostic are **not** asymptotically interchangeable near full sketch rank:
\[
\operatorname{Var}(T_m)=\frac{2\nu(n+3)}{m(\nu+3)},\qquad
\mathbb E J_m=\frac{2\nu(\nu+2)}{m(\nu+3)},\qquad
\frac{\operatorname{Var}(T_m)}{\mathbb E J_m}=\frac{n+3}{\nu+2}.
\]
At \(m=n\), the expected diagnostic vanishes like \(3/(2n)\), whereas the actual squared **absolute** error tends to \(1/2\). One extra probe, \(m=n+1\), makes the pseudoinverse-based method exact. This is an exact calibration and sample-budget boundary for the specific unnormalized algorithm, not a criticism of its normalized version.

## Assumptions and scope

Fix an integer \(n\ge2\), an integer \(2\le m\le n\), and \(A=I_n\). Draw independent standard real Gaussian columns \(g_1,\ldots,g_m\in\mathbb R^n\). For every \(j\), let \(P_{-j}\) be the orthogonal projector onto the span of all columns except \(g_j\). Define the individual unnormalized Nyström leave-one-out estimators, their average, and the **squared** posterior error proxy by
\[
B_j=\operatorname{tr}(P_{-j})+g_j^{\mathsf T}(I_n-P_{-j})g_j,\quad
T_m=\frac1m\sum_{j=1}^m B_j,\quad
J_m=\frac1{m(m-1)}\sum_{j=1}^m(B_j-T_m)^2.
\]
These are Eq. (8), Eq. (9), and Algorithm 3 of Epperly–Tropp–Webber, interpreted with the squared-error convention of their Eq. (16). We use Moore–Penrose inverses for all Nyström approximations. The probability space is the product of the real Gaussian laws. No floating-point, normalized-residual, or adaptive-stopping assertion is made.

Put \(\nu=n-m+1\). Since \(m-1\le n-1\), every \(P_{-j}\) has rank \(m-1\) almost surely. For comparison the definitions also extend to \(m\ge n+1\), when \(P_{-j}=I_n\) almost surely.

## Proof

**Step 1: individual moments.** Each \(g_j\) is independent of \(P_{-j}\), whose orthogonal complement has rank \(\nu\). Therefore
\[
Y_j:=g_j^{\mathsf T}(I_n-P_{-j})g_j\sim\chi^2_\nu,\quad
B_j=(m-1)+Y_j,\quad
\mathbb E B_j=n,\quad\operatorname{Var}(B_j)=2\nu.
\]

**Step 2: exact dependence through one shared angle.** Fix different indices \(i,j\). Condition on the other \(m-2\) Gaussian columns and project onto their common orthogonal complement. Its dimension is \(d=n-(m-2)=\nu+1\), and the two projected columns \(a,b\) are independent standard Gaussian vectors in this \(d\)-dimensional space. The leave-one-out residual squares become
\[
Y_i=\|a\|_2^2\left(1-\frac{\langle a,b\rangle^2}{\|a\|_2^2\|b\|_2^2}\right),\qquad
Y_j=\|b\|_2^2\left(1-\frac{\langle a,b\rangle^2}{\|a\|_2^2\|b\|_2^2}\right).
\]
Write the shared angular factor as \(W\). The independent squared radii each have the \(\chi^2_d\) law and are independent of \(W\). The independent uniform sphere directions imply
\[
W\sim\operatorname{Beta}((d-1)/2,1/2),\qquad
\mathbb E W=\frac{d-1}{d},\qquad
\mathbb E W^2=\frac{d^2-1}{d(d+2)}.
\]
Conditioning on the other columns does not change these distributions or values. As a result,
\[
\mathbb E(Y_iY_j)=d^2\mathbb E(W^2)
=\frac{d(d^2-1)}{d+2},
\]
and subtraction of \((d-1)^2=\nu^2\) yields
\[
\operatorname{Cov}(B_i,B_j)=\operatorname{Cov}(Y_i,Y_j)
=\frac{2(d-1)}{d+2}=\frac{2\nu}{\nu+3}.
\]
Divide by the individual variance \(2\nu\) to get correlation \(1/(\nu+3)\). This is an exact moment calculation, not an independence assumption.

**Step 3: average and diagnostic.** The basic estimators are exchangeable. Hence
\[
\operatorname{Var}(T_m)
=\frac{\operatorname{Var}(B_1)+(m-1)\operatorname{Cov}(B_1,B_2)}{m}
=\frac{2\nu(n+3)}{m(\nu+3)}.
\]
Expanding the centered empirical squares gives
\[
\mathbb E J_m
=\frac{\operatorname{Var}(B_1)-\operatorname{Cov}(B_1,B_2)}{m}
=\frac{2\nu(\nu+2)}{m(\nu+3)}.
\]
Division gives \((n+3)/(\nu+2)=1+m/(\nu+2)\), agreeing with the *general* correlation identity of Proposition 2 of the source, now with the exact identity-matrix correlation evaluated.

**Step 4: high-dimensional failure of absolute-error calibration.** Set \(m=n\), so \(\nu=1\). The identities yield
\[
\operatorname{Var}(T_n)=\frac{n+3}{2n}\longrightarrow\frac12,
\qquad\mathbb E J_n=\frac{3}{2n}\longrightarrow0.
\]
Since \(J_n\ge0\), Markov's inequality proves \(J_n\to0\) in probability. To show that the true absolute error does *not* vanish in probability, write \(T_n-n=n^{-1}\sum_{j=1}^n(Y_j-1)\) and apply Jensen's inequality:
\[
\mathbb E\left|\frac1n\sum_jY_j\right|^4
\le\mathbb E Y_1^4=105,
\quad
\mathbb E|T_n-n|^4\le8(105+1)=848.
\]
For any real random variable \(Z\), Cauchy–Schwarz applied to the event \(\{|Z|>1/2\}\) gives
\[
\Pr(|Z|>1/2)\ge\frac{(\mathbb E Z^2-1/4)^2}{\mathbb E Z^4}
\quad\text{if }\mathbb E Z^2>1/4.
\]
Here \(\mathbb E|T_n-n|^2\ge1/2\). Therefore for every \(n\ge2\),
\[
\Pr(|T_n-n|>1/2)\ge\frac1{13568}.
\]
For each fixed \(\varepsilon>0\), \(\Pr(J_n>\varepsilon^2)\le3/(2n\varepsilon^2)\). Subtracting this vanishing term proves
\[
\liminf_{n\to\infty}\Pr(|T_n-n|>1/2,\ J_n\le\varepsilon^2)
\ge\frac1{13568}.
\]
Finally, fixing \(\nu\ge1\) and taking \(m=n-\nu+1\) in the exact identities gives the fixed-codimension limits. For \(m\ge n+1\), the remaining \(m-1\) Gaussian columns span \(\mathbb R^n\) almost surely, and every Nyström projection is \(I_n\), making each basic estimator exactly \(n\).

## Verification

Run `python verify.py` after installing dependencies from `requirements.txt`. The standalone verifier checks the moment, beta-angular, covariance, average, and diagnostic formulas by exact rational arithmetic for a grid of integer dimensions, then compares selected cases with independently generated seeded Gaussian sketches. The infinite-dimensional asymptotic conclusions, covariance formula, and strict probability bound are analytical: finite arithmetic checks and Monte Carlo are not substitutes for the proof.

## Relationship to prior work

Epperly, Tropp, and Webber [1] define the XNysTrace leave-one-out algorithm in Eq. (8), Eq. (9), and Algorithm 3 and establish in Proposition 2 the **general identity relating posterior expected squared error to pairwise basic-estimator correlation**. The present theorem does not claim to discover that identity. Rather, it computes its exact correlation for the standard-Gaussian identity-matrix case, establishes the ensuing dimension-dependent calibration ratio, and proves an explicit probability-level variance cliff. Their general XNysTrace variance bounds (including Proposition 5) do not give these exact special-case expressions. Earlier related leave-one-out randomized linear algebra is discussed in [2]. Classical chi-square and beta angular moments are established tools.

## Limitations

This finding is restricted to **unnormalized** real standard-Gaussian probes and the idealized exact-arithmetic Eq. (8) construction. The source explicitly recommends normalizing distinguished residual probes (Section 2.3); on \(A=I_n\), such normalization can remove this random residual-norm effect entirely. No instability or calibration failure is claimed for that separately recommended implementation, nor for Rademacher probes. The nonconcentration concerns **absolute** trace error; because \(\operatorname{tr}(I_n)=n\), it does not establish failure of fixed-tolerance *relative* trace accuracy or of practical adaptive stopping. The one-extra-probe exactness conclusion uses the mathematical Moore–Penrose definition, not a claim about a particular fast implementation. No originality claim is made for beta or chi-square identities by themselves. Unindexed specialized literature might establish equivalent conclusions.

## References

[1] E. N. Epperly, J. A. Tropp, and R. J. Webber, *XTrace: Making the most of every sample in stochastic trace estimation*, first publicly submitted 2023-01-19, arXiv:2301.07825, https://arxiv.org/abs/2301.07825 ; accessible full text https://ar5iv.labs.arxiv.org/html/2301.07825 .

[2] E. N. Epperly and J. A. Tropp, *Efficient error and variance estimation for randomized matrix computations*, arXiv:2207.06342, https://arxiv.org/abs/2207.06342 .
