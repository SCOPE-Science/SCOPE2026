# Two Gaussian sketch rows are the sharp expectation threshold for two-column pivoting

## Finding

Consider one first-column pivot chosen by comparing the Euclidean norms of two columns after an independent Gaussian left sketch, followed by the **orthogonal** rank-one projection onto the selected original column. This is the initial column-choice mechanism in Gaussian-sketched QR with column pivoting, including rank-one truncated RQRCP.

For every real two-column matrix \(A=[a\ b]\in\mathbb R^{m\times2}\), \(m\ge2\), of rank two, and every integer \(s\ge2\), the expected **squared** Frobenius error is bounded sharply by twice the best rank-one squared Frobenius error:
\[
\boxed{\mathbb E\|A-P_{A(:,J)}A\|_F^2\le 2\sigma_2(A)^2.}
\]
The factor \(2\) is a supremum approached by rank-two inputs; it cannot be improved at any finite sketch dimension \(s\ge2\). In sharp contrast, for one Gaussian sketch row, the ratio of these two errors is unbounded over rank-two inputs. Thus the smallest sketch dimension that gives a uniform finite relative **expected squared-error** bound is exactly two.

The result includes an exact probability formula for every two-column input and every positive integer \(s\), plus a sharp correlation-dependent mispivot bound.

## Assumptions and scope

Let \(a,b\in\mathbb R^m\) be linearly independent. Relabel columns so that
\[
\alpha=\|a\|_2^2\ge\beta=\|b\|_2^2>0,\qquad \gamma=a^{\mathsf T}b,
\quad h=\alpha\beta-\gamma^2>0.
\]
Let \(\Omega\in\mathbb R^{s\times m}\) have independent \(N(0,1)\) entries. The index \(J\) selects whichever of \(a,b\) has the larger sketched norm \(\|\Omega a\|_2\) or \(\|\Omega b\|_2\). Except for rank-deficient tie cases, the probability of equality is zero. Let \(P_c=cc^{\mathsf T}/\|c\|_2^2\) for a nonzero column \(c\). All operations are in exact real arithmetic.

Define
\[
\delta=\alpha-\beta,\quad
\Delta=\sqrt{(\alpha+\beta)^2-4\gamma^2},\quad
\Lambda=\frac{\alpha+\beta+\sqrt{(\alpha-\beta)^2+4\gamma^2}}2,
\quad x=\frac{\Delta-\delta}{2\Delta}.
\]
Write \(I_x(u,v)=B_x(u,v)/B(u,v)\) for the regularized incomplete beta function. Then the exact probability of choosing the smaller-norm column is
\[
\boxed{p_s=\Pr\{J=b\}=I_x(s/2,s/2).}
\]
When \(\alpha=\beta\), this formula gives \(p_s=1/2\), with either column having the same true squared projection error. The expected error and optimal error are exactly
\[
\boxed{E_s=h\left(\frac{1-p_s}{\alpha}+\frac{p_s}{\beta}\right),
\qquad E_*=\sigma_2(A)^2=\frac h\Lambda.}
\]
For fixed \(\alpha>\beta\), the sharp range of mispivot probabilities over all possible column correlations is \(0<p_s\le I_{\beta/(\alpha+\beta)}(s/2,s/2)\). The upper endpoint is attained when the two columns are orthogonal; the lower endpoint is approached as they become collinear. Consequently, the excess expected error relative to selecting the larger original column is maximized by orthogonal columns and equals
\[
\boxed{\max_{\gamma} \frac{E_s}{h/\alpha}
=1+\left(\frac\alpha\beta-1\right)I_{\beta/(\alpha+\beta)}(s/2,s/2).}
\]

## Proof

**1. Exact Gaussian norm-comparison law.** For a single row \(z\sim N(0,I_m)\),
\[
(z^{\mathsf T}a)^2-(z^{\mathsf T}b)^2=z^{\mathsf T}(aa^{\mathsf T}-bb^{\mathsf T})z.
\]
On \(\operatorname{span}\{a,b\}\), the symmetric matrix \(aa^{\mathsf T}-bb^{\mathsf T}\) has trace \(\delta\), determinant \(-h\), and eigenvalues \(\lambda_+=(\Delta+\delta)/2>0\) and \(\lambda_-=(\delta-\Delta)/2<0\). The remaining eigenvalues vanish. Orthogonal invariance of a Gaussian gives, for independent \(U,V\sim\chi_s^2\),
\[
\|\Omega a\|_2^2-\|\Omega b\|_2^2
\stackrel d=\lambda_+U-|\lambda_-|V.
\]
Since \(U/(U+V)\sim\operatorname{Beta}(s/2,s/2)\), the probability of negative difference is
\[
\Pr\left\{\frac{U}{U+V}<\frac{|\lambda_-|}{\lambda_++|\lambda_-|}\right\}
=I_{(\Delta-\delta)/(2\Delta)}(s/2,s/2).
\]
For \(\alpha>\beta\), decreasing \(|\gamma|\) increases \(\Delta\) and therefore increases the beta argument \(x\); the orthogonal maximum is \(x=\beta/(\alpha+\beta)\). Collinearity makes \(x\downarrow0\). This proves the exact law and sharp correlation ordering.

**2. Exact projection loss.** If the selected column is \(a\), the squared residual of the other column is \(\|b-P_a b\|_2^2=h/\alpha\). If the selected column is \(b\), the loss is \(h/\beta\). Taking the expectation proves the formula for \(E_s\). The nonzero eigenvalues of \(A^{\mathsf T}A\) have sum \(\alpha+\beta\), product \(h\), and larger eigenvalue \(\Lambda\). The best rank-one squared Frobenius error is the smaller eigenvalue \(h/\Lambda\), by the singular-value characterization of best rank-one approximation.

**3. A sharp two-row expectation bound.** If \(0\le x\le1/2\), the lower tail \(I_x(t,t)\) is nonincreasing in \(t>0\). To verify the direction without appealing to a heuristic about concentration, set \(W=|2Z-1|\), where \(Z\sim\operatorname{Beta}(t,t)\). Its density on \((0,1)\) is proportional to \((1-w^2)^{t-1}\). For \(t_2>t_1\) the density ratio is strictly decreasing in \(w\), so \(W\) is stochastically smaller at \(t_2\). Since \(I_x(t,t)=\frac12\Pr(W\ge1-2x)\) for \(x<1/2\), the claim follows, including endpoints by continuity.

For every integer \(s\ge2\), therefore,
\[
 p_s\le p_2=x=\frac12\left(1-\frac\delta\Delta\right)
 \le\frac\beta{\alpha+\beta},
\]
where the last inequality uses \(\Delta\le\alpha+\beta\) and \(\delta\ge0\). Hence
\[
\frac{1-p_s}{\alpha}+\frac{p_s}{\beta}
\le\frac1\alpha+
\frac\beta{\alpha+\beta}\left(\frac1\beta-\frac1\alpha\right)
=\frac2{\alpha+\beta}.
\]
As \(\Lambda\le\alpha+\beta\),
\[
 E_s\le\frac{2h}{\alpha+\beta}\le\frac{2h}{\Lambda}=2E_*.
\]
This proves the uniform estimate, with no restriction on \(m\), condition number, or angle between the columns. For full-rank \(A\), both \(h>0\) and \(\Lambda<\alpha+\beta\), so equality in the global factor \(2\) is not attained.

**4. Sharpness at every \(s\ge2\).** For \(a=e_1\) and \(b=\cos\theta\,e_1+\sin\theta\,e_2\), \(0<\theta<\pi/2\), the true column norms coincide and both possible squared projection errors equal \(\sin^2\theta\). The optimal rank-one squared error equals \(1-\cos\theta\). Consequently, regardless of sketch dimension or pivot outcome,
\[
 \frac{E_s}{E_*}=1+\cos\theta\longrightarrow2
 \qquad(\theta\downarrow0).
\]

**5. One row has no uniform expected-error factor.** With orthogonal \(a=e_1\) and \(b=\sqrt\varepsilon\,e_2\), \(0<\varepsilon<1\), a one-row sketch chooses \(b\) when \(|Z_1|<\sqrt\varepsilon|Z_2|\), for independent standard normals. Their ratio is Cauchy, giving
\[
 p_1=\frac2\pi\arctan\sqrt\varepsilon,
\qquad\frac{E_1}{E_*}=1+(\varepsilon^{-1}-1)p_1
\sim\frac2{\pi\sqrt\varepsilon}\longrightarrow\infty.
\]
This establishes the necessity of at least two Gaussian rows for any finite worst-case expected squared-error factor.

**6. Additional sharp anisotropy law.** For orthogonal columns, put \(K=\alpha/\beta\ge1\). Then
\[
 \frac{E_s}{h/\alpha}=1+(K-1)I_{1/(K+1)}(s/2,s/2).
\]
The beta density integral at its left endpoint yields, for each fixed integer \(s\),
\[
 I_{1/(K+1)}(s/2,s/2)
\sim\frac{K^{-s/2}}{(s/2)B(s/2,s/2)}.
\]
Thus for \(s=1\) the excess penalty diverges at square-root rate, for \(s=2\) it tends to \(1\) (the full ratio tends to \(2\)), and for every \(s>2\) the excess penalty vanishes in this orthogonal high-anisotropy family. This does not contradict global sharpness of factor \(2\) for larger \(s\): the near-collinear, equal-norm family in step 4 is a different extremal mechanism.

## Verification

The standalone file `artifacts/verify.py` checks the exact two-row orthogonal formula using rational arithmetic, tests the uniform inequality on random full-rank Gram matrices, directly simulates two million independent Gaussian probe pairs across eight representative configurations, and checks the beta-tail dimension law numerically. The file `artifacts/verification_output.txt` records the actual output. These tests support, but do not replace, the proof above. In particular the claim about all dimensions and all inputs follows from steps 1–6, not finite enumeration.

## Relationship to prior work

Gaussian norm sketches for pivot selection and rank-one truncated QR approximations are established algorithmic ingredients in RQRCP (Xiao, Gu, and Langou, 2018); the initial sketched QRCP mechanism is also used by CQRRPT (Melnichenko and collaborators, 2023). Duersch and Gu (2015) analyzed Gaussian norm statistics and pivot selection, while the 2018 RQRCP article proves a high-probability pseudo-diagonal-dominance guarantee requiring an oversampling budget. Those statements do not provide the present exact two-column correlated norm-ordering law, sharp **expected rank-one spectral-tail ratio** at two sketch rows, or the one-row unboundedness threshold. The projection-DPP and adaptive randomized pivoting bounds in later column-subset literature concern a different sampling law and do not imply the Gaussian norm-maximizing pivot claim here.

## Limitations

The theorem concerns exactly two real columns, an initial Gaussian norm-maximizing pivot, a single orthogonal column-space projection, and exact arithmetic. The result is in **expectation of squared Frobenius error**, not a high-probability pointwise guarantee, and does not extend automatically to three or more competing columns or multiple pivot stages. The one-row counterexample is a valid rank-one RQRCP sketch configuration, but the 2023 full CQRRPT routine typically requires at least as many sketch rows as input columns. The exact beta identity for correlated quadratic Gaussian forms is classical machinery; novelty, if any, concerns the combined sharp pivot approximation and sketch-dimension classification, not the beta distribution in isolation.

## References

1. J. Xiao, M. Gu, and J. Langou, *Fast Parallel Randomized QR with Column Pivoting Algorithms for Reliable Low-rank Matrix Approximations*, arXiv:1804.05138, first version April 13, 2018. https://arxiv.org/abs/1804.05138
2. M. Melnichenko, O. Balabanov, R. Murray, J. Demmel, M. W. Mahoney, and P. Luszczek, *CholeskyQR with Randomization and Pivoting for Tall Matrices (CQRRPT)*, arXiv:2311.08316, first version November 14, 2023. https://arxiv.org/abs/2311.08316
3. J. A. Duersch and M. Gu, *Randomized QR with Column Pivoting*, arXiv:1509.06820, first version September 23, 2015. https://arxiv.org/abs/1509.06820
4. A. Cortinovis and D. Kressner, *Adaptive Randomized Pivoting for Column Subset Selection, DEIM, and Low-Rank Approximation*, SIAM Journal on Matrix Analysis and Applications 47 (2026), 25–47. https://doi.org/10.1137/24M1719189
