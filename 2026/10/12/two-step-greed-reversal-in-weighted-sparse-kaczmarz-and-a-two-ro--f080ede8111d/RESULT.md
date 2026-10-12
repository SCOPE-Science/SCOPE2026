# Two-step greed reversal in weighted sparse Kaczmarz and a two-row projection barrier

## Finding

The inexact weighted randomized sparse Kaczmarz (WRaSK) iteration of Zhang–Yuan–Wang–Zhang admits a consistent, nonsingular three-equation instance on which residual-power row sampling is **better after one update but worse after two updates** than uniform sampling, even though every residual-power exponent \(p\ge24\) retains the published convergence guarantee. With regularization \(\lambda=1/2\), the example below has

\[
\mathbb E_p\|x_1-\widehat x\|_2^2<\mathbb E_0\|x_1-\widehat x\|_2^2=\frac{179}{30},
\qquad
\mathbb E_p\|x_2-\widehat x\|_2^2>
\mathbb E_0\|x_2-\widehat x\|_2^2=\frac{4193}{900}
\quad(p\ge24).
\]

For ordinary unregularized orthogonal-projection Kaczmarz, this phenomenon has a sharp row-count obstruction: **on every system consisting of at most two row labels, the two-step maximal-residual greedy method has no greater squared solution error than independent uniform sampling**, for any initial error. The displayed three-row geometry also produces a strict two-step reversal in that unregularized case, so three rows are the minimum for this particular projection comparison. The two-row assertion is made only for orthogonal projections, not for \(\lambda>0\).

## Assumptions and scope

Fix \(\widehat x=(2,0,2)^\mathsf T\) and integer row vectors

\[
 v_1=(0,1,1),\qquad v_2=(2,1,0),\qquad v_3=(1,-1,0),
 \qquad s_i=\|v_i\|_2^2=(2,5,2)_i.
\]

Let the three rows of \(A\) be \(a_i=v_i/\sqrt{s_i}\), and let \(b=A\widehat x\). Since \(\det[v_1;v_2;v_3]=-3\), the system is full rank and the unique feasible point—and hence the unique minimizer of the augmented-basis-pursuit objective \(\lambda\|x\|_1+\|x\|_2^2/2\) subject to \(Ax=b\)—is \(\widehat x\).

For \(\lambda=1/2\), initialize both the dual and primal variables at \(y_0=x_0=0\). At time \(k\), select row \(i\) with probability proportional to \(\lvert\langle a_i,x_k\rangle-b_i\rvert^p\), and make the published **inexact**, rather than exact-line-search, WRaSK update

\[
 y_{k+1}=y_k-\frac{\langle v_i,x_k-\widehat x\rangle}{s_i}v_i,
 \qquad x_{k+1}=S_{\lambda}(y_{k+1}),\qquad
 S_{\lambda}(t)=\operatorname{sign}(t)\max\{|t|-\lambda,0\}
\]

componentwise. Here \(p>0\) is arbitrary real; \(p=0\) means the explicitly defined uniform-row baseline. All expectations concern independent random choices conditional on the current iterate, with row labels allowed to repeat. The error observable is **squared Euclidean solution error**, not Bregman distance, a theorem's worst-case rate upper bound, residual norm, or the exact-step variant. In the unregularized comparison, set \(\lambda=0\) and use the same row geometry.

## Proof

**First update.** At \(x_0=0\), normalized squared residuals are \((2,16/5,2)\). Consequently the probability that the first row is row \(2\) equals

\[
 P_0(2)=\frac{1}{1+2(5/8)^{p/2}}>\frac13\qquad(p>0).
\]

The squared solution errors after selecting rows \(1,2,3\), respectively, are \(13/2,49/10,13/2\). Thus putting more than one third of the first-step mass on row \(2\) strictly reduces the first-step expectation below \(179/30\).

**The uniform two-step benchmark.** For \(p=0\), all nine row-label pairs have probability \(1/9\). Direct application of the stated update gives the following squared errors, with first row indexing the table rows and second row indexing the columns:

\[
 \begin{pmatrix}
 6&49/10&61/16\\
 971/200&89/20&409/100\\
 61/16&401/100&6
 \end{pmatrix}.
\]

Their arithmetic average is exactly \(4193/900\).

**A high-probability bad path for every real exponent \(p\ge24\).** On the first event \(i_0=2\), exact dual and primal states are

\[
 y_1=(8/5,4/5,0),\qquad x_1=(11/10,3/10,0).
\]

The three normalized squared residuals are then \((289,90,144)/200\); hence, conditionally on the first choice, row \(1\) is sampled second with probability

\[
 P_1(1\mid i_0=2)=
 \frac{1}{1+(90/289)^{p/2}+(144/289)^{p/2}}.
\]

For every \(p\ge24\), the strict inequalities \((5/8)^{12}<1/200\) and \(90/289<1/2\), \(144/289<1/2\) yield

\[
 P_0(2)>\frac{100}{101},\qquad
 P_1(1\mid i_0=2)>\frac{2048}{2049}.
\]

On the specific path \((i_0,i_1)=(2,1)\), the two-step primal iterate is \(x_2=(11/10,23/20,7/20)\), with squared error \(971/200\). All other path errors are nonnegative, so

\[
 \mathbb E_p\|x_2-\widehat x\|_2^2>
 \frac{971}{200}\frac{100}{101}\frac{2048}{2049}
 =\frac{994304}{206949}>
 \frac{4193}{900}
 \qquad\text{for every real }p\ge24.
\]

The greedy limit selects \((2,1)\) and has exactly \(971/200\) error at two steps. These are exact finite-horizon statements, with no asymptotic iteration limit.

**The unsparsified three-row witness.** When \(\lambda=0\), the same geometry is ordinary Kaczmarz on the same consistent equations, initialized at \(x_0=0\). Its uniform two-step expected squared error is exactly \(101/25\). Maximum-residual selection chooses row \(2\) first and one of the tied rows \(1\) and \(3\) second; either gives error \(102/25\). The second residual on row \(2\) is zero, so the conditional error after first choosing row \(2\) is \(102/25\) for any positive finite power. Since \((5/8)^{12}<1/204\) implies \(P_0(2)>102/103\), every real \(p\ge24\) satisfies

\[
 \mathbb E_p\|x_2-\widehat x\|_2^2>
 \frac{102}{25}\frac{102}{103}=
 \frac{10404}{2575}>\frac{101}{25}.
\]

**Two rows cannot reverse this comparison in ordinary Kaczmarz.** Consider arbitrary unit row normals \(a,b\) in a real inner-product space, any initial error \(e\), and set \(c=\langle a,b\rangle\), \(u=\langle a,e\rangle\), \(v=\langle b,e\rangle\). Without loss, the maximal-residual greedy rule selects \(a\) first, so \(u^2\ge v^2\). Orthogonal projection reduces squared error by the square of the corresponding row residual. The total two-step decrease under greedy selection is \(R_g=u^2+(v-cu)^2\); the expected decrease for two iid uniform choices is

\[
 R_u=\frac{u^2+v^2}{2}+
 \frac{(v-cu)^2+(u-cv)^2}{4}.
\]

Direct expansion gives the **nonnegative exact defect identity**

\[
 4(R_g-R_u)=(1+c^2)(u^2-v^2)+2(cu-v)^2\ge0.
\]

The initial squared error is common, so larger decrease is precisely smaller final error. This proof includes zero residuals, coincident/opposite normals, ties, and ambient dimension greater than two. A one-row system trivially has no reversal. With the above three-row witness, three labels are therefore necessary and sufficient for a two-step greedy-versus-uniform reversal **within this unregularized projection comparison**.

## Verification

Run `python3 verify.py` from this folder (standard library only). Its exact-fraction checks reconstruct the normalized residuals, source update, both first-step expectations, all nine second-step errors, the \(p=24\) weighted expectation, the rational lower bounds and the unregularized companion. The verifier separately checks the two-row polynomial defect identity on 343 exact-rational parameter triples. The displayed algebraic identity is the proof for arbitrary real parameters; the 343 samples are only a consistency check. No sampling experiment, floating-point fit, or external output is used as a universal proof.

## Relationship to prior work

Zhang–Yuan–Wang–Zhang [1] define Algorithm 1, the inexact and exact alternatives, the residual-power row sampling rule, and a linear Bregman-distance convergence theorem. They prove a monotone **rate-bound coefficient**, not an exact ordering of finite-horizon squared Euclidean risks. In particular, the present counterexample does not refute their upper bound or convergence result. The earliest independently verified public source for [1] is the publisher's publication dated **2022-11-08**; its lawful arXiv full-text version [2] was publicly uploaded on 2023-06-12.

Tondji–Winkler–Lorenz [7] previously describe the same weighted sparse Kaczmarz sampling rule in a 2021 conference paper and prove a global expected squared-error convergence-rate upper bound; that paper does not supply the present exact two-step risk comparison. The available 2021 conference attribution does not verify the day the conference manuscript first became publicly accessible. Steinerberger [3] treats residual-power sampling in unregularized Kaczmarz and proves a convergence-rate upper bound, not a universal pathwise or finite-step ranking of the actual expected errors. Nutini et al. [4] establish greedy row-selection rates, including orthogonality-based multistep bounds; Haddock–Ma [5] sharpen sampling Kaczmarz–Motzkin convergence estimates. None of those inspected statements gives the present specific two-step strict reversal with a sharp two-row impossibility proof. Tsipory et al. [6] study greedy versus random **task orderings** in continual linear regression, with distinct sampling and error criteria; their results do not furnish this same two-step with-replacement solution-error comparison. A related published residual-spike analysis concerns **one-step total residual norm** under coherence restrictions, whereas the present observable is **two-step expected squared solution error**; that assertion does not imply either sign of this comparison.

## Limitations

The counterexample concerns a particular full-rank three-equation system, the source-initialized inexact WRaSK recurrence, a fixed positive regularizer \(\lambda=1/2\), and exactly two updates. It shows a strict ordering for all \(p\ge24\) against \(p=0\), **not** the exact reversal threshold in \(p\), monotonicity for smaller exponents, an adverse asymptotic convergence rate, or failure of the cited Bregman guarantee. The sharp minimum of three row labels is established **only for the zero-regularization orthogonal-projection comparison**. Full novelty relative to unindexed or inaccessible specialized work is not established by negative searches; an independent literature and proof audit has not been performed.

## References

[1] L. Zhang, Z. Yuan, H. Wang, H. Zhang, *A weighted randomized sparse Kaczmarz method for solving linear systems*, Computational and Applied Mathematics **41**, 383 (2022), DOI `10.1007/s40314-022-02105-9`, publicly published 2022-11-08.

[2] Same authors and title, lawful full-text preprint, arXiv `2306.06813v1` (2023-06-12), Sections 3.1–3.3, 4.2 and Algorithm 1.

[3] S. Steinerberger, *A Weighted Randomized Kaczmarz Method for Solving Linear Systems*, arXiv `2007.02910v3`, particularly Sections 2.1–2.3 and the main rate theorem.

[4] J. Nutini et al., *Convergence Rates for Greedy Kaczmarz Algorithms, and Faster Randomized Kaczmarz Rules Using the Orthogonality Graph*, arXiv `1612.07838`, especially Section 9.

[5] J. Haddock and A. Ma, *Greed Works: An Improved Analysis of Sampling Kaczmarz-Motzkin*, arXiv `1912.03544`.

[6] M. Tsipory et al., *Are Greedy Task Orderings Better Than Random in Continual Linear Regression?*, arXiv `2510.19941`, especially the task-ordering formalism and later comparison sections.

[7] L. N. Tondji, M. Winkler, D. A. Lorenz, *Linear convergence of a weighted randomized sparse Kaczmarz method*, 2021 Online International Conference on Computational Harmonic Analysis; publicly accessible author-uploaded complete conference text.
