# Sharp normality-defect bound for Gibbs-averaged finite Markov chains

## Finding

**Theorem.** Let \(N\ge2\), let \(P\) be an arbitrary stochastic matrix on an \(N\)-point set with a strictly positive stationary law \(\pi\), and let \(G\) resample within every cell of an arbitrary partition from the conditional stationary distribution. Put \(\Pi(x,y)=\pi(y)\), \(Q=GPG\), and \(A=P-\Pi\). All operator norms and adjoints below refer to \(\ell^2(\pi)\). Write \(s_1(A)\ge\cdots\ge s_{N-1}(A)\ge0\) for the nonzero-or-zero singular values on the stationary-mean-zero space, and define

\[
D=\|P-Q\|_{F,\pi}^{2},\qquad
\delta_t(P)=\sum_{j=1}^{N-1}s_j(A)^{2t}-\|P^t-\Pi\|_{F,\pi}^{2}\ge0.
\]

For **every** integer \(t\ge1\), without reversibility or normality assumptions,

\[
\boxed{\quad
\|(GPG)^t-\Pi\|_{F,\pi}^{2}
+\frac{D^{t}}{(N-1)^{t-1}}
\le\|P^{t}-\Pi\|_{F,\pi}^{2}+\delta_t(P).
\quad}
\]

If the partition has \(k\) cells, one also has the spectral-rank bound

\[
\|(GPG)^t-\Pi\|_{F,\pi}^{2}
\le\sum_{j=1}^{k-1}s_j(P-\Pi)^{2t}.
\]

The nonnormality defect is exact at time two:

\[
\boxed{\quad\delta_2(P)=\frac12\|P^*P-PP^*\|_{F,\pi}^{2}.\quad}
\]

In particular, if \(P\) is **normal** on \(\ell^2(\pi)\), then \(\delta_t(P)=0\) at every time, and therefore

\[
\boxed{\quad
\|(GPG)^t-\Pi\|_{F,\pi}^{2}
\le\|P^{t}-\Pi\|_{F,\pi}^{2}
-\frac{\|P-GPG\|_{F,\pi}^{2t}}{(N-1)^{t-1}}.
\quad}
\]

For normal \(P\), equality between the **unadjusted** squared distances at even one positive time occurs precisely when \(P=GPG\); otherwise the comparison is strict at *all* positive times. If, additionally, \(P\) is irreducible and aperiodic, then \(GPG\) is irreducible and aperiodic and its squared-Frobenius mixing time is no greater at every positive threshold. This includes normal but nonreversible directed chains. A normal baseline need not produce a normal averaged chain.

The universal coefficient \((N-1)^{-(t-1)}\) of the normal-case gap is **sharp** for every \(N\) and every positive integer \(t\): take \(P=rI+(1-r)\Pi\), \(0<r<1\), and the one-cell averaging projection \(G=\Pi\). Then both sides of the displayed normal-case inequality vanish and the coefficient cannot be increased universally.

For a general (possibly nonnormal) baseline the time-two inequality gives a direct criterion: averaging strictly improves the time-two squared-Frobenius distance whenever

\[
\|P-GPG\|_{F,\pi}^{4}>
\frac{N-1}{2}\|P^*P-PP^*\|_{F,\pi}^{2}.
\]

## Assumptions and scope

A stochastic matrix is row-stochastic. Stationarity is \(\pi P=\pi\) with \(\pi(x)>0\). For a partition \(\mathcal B\), the Gibbs projection is

\[
G(x,y)=\mathbf1_{\{x,y\text{ belong to the same cell }C\}}\,
\frac{\pi(y)}{\pi(C)},
\]

where \(\pi(C)=\sum_{z\in C}\pi(z)\). It is the orthogonal conditional-expectation projection on \(\ell^2(\pi)\) and satisfies \(G^2=G=G^*\) and \(G\Pi=\Pi G=\Pi\). The weighted Frobenius norm is \(\|M\|_{F,\pi}^2=\sum_{x,y}\pi(x)M(x,y)^2/\pi(y)\). Schatten norms use the same weighted Hilbert-space representation. Normal means \(PP^*=P^*P\), which is weaker than reversibility \(P=P^*\).

No commutation between \(P\) and \(G\) is assumed, and the averaged chain \(Q\) is not required to be reversible or normal. The first two inequalities do not require irreducibility or aperiodicity of \(P\). Mixing-time assertions require ergodicity of the normal baseline. For \(k=1\) and \(k=N\), the statements use the usual empty-sum conventions and allow the trivial/full partitions.

## Proof

**Step 1: projection identities.** Since \(P\), \(Q\), and \(G\) preserve \(\pi\), and \(G\Pi=\Pi G=\Pi\), put \(B=Q-\Pi=GAG\). The stationarity relations \(P\Pi=\Pi P=\Pi\) and \(Q\Pi=\Pi Q=\Pi\) imply \(P^t-\Pi=A^t\) and \(Q^t-\Pi=B^t\) for every integer \(t\ge1\). The map \(M\mapsto GMG\) is an orthogonal projection for the Hilbert–Schmidt inner product, so

\[
\|A\|_{F,\pi}^2=\|B\|_{F,\pi}^2+\|A-B\|_{F,\pi}^2,
\qquad A-B=P-Q.
\]

Both \(A\) and \(B\) annihilate constants and have constant vectors in the adjoint kernel; thus each has at most \(N-1\) potentially nonzero singular values. If there are \(k\) partition cells, \(B\) has rank at most \(k-1\).

**Step 2: a power bound without normality of the compression.** By the Eckart–Young variational characterization and \(\|G\|_{2\to2,\pi}=1\), every singular value satisfies \(s_j(B)\le s_j(A)\), including zero padding. Noncommutative Schatten Hölder gives, for each integer \(t\ge1\),

\[
\|B^t\|_{F,\pi}\le\|B\|_{S_{2t},\pi}^{t},\qquad
\text{hence}\quad\|B^t\|_{F,\pi}^{2}\le\sum_j s_j(B)^{2t}.
\]

Notice that this step **does not** assume \(B\) is normal. It also immediately proves the spectral-rank bound in the finding.

**Step 3: quantitative lost singular-value mass.** For \(j=1,\dots,N-1\), put \(x_j=s_j(A)^2\) and \(y_j=s_j(B)^2\). Then \(x_j\ge y_j\ge0\), and Step 1 gives \(\sum_j(x_j-y_j)=D\). For every integer \(t\ge1\), the elementary inequalities

\[
x_j^t-y_j^t\ge(x_j-y_j)^t,
\qquad\sum_{j=1}^{N-1}(x_j-y_j)^t
\ge\frac{D^t}{(N-1)^{t-1}}
\]

follow respectively from the binomial expansion and convexity. Consequently

\[
\|B^t\|_{F,\pi}^{2}
\le\sum_j y_j^t
\le\sum_j x_j^t-\frac{D^t}{(N-1)^{t-1}}
=\|A^t\|_{F,\pi}^{2}+\delta_t(P)
-\frac{D^t}{(N-1)^{t-1}}.
\]

This proves the universal all-time inequality. The defect is nonnegative by the same Hölder estimate applied to \(A\).

**Step 4: normality and the second-time commutator.** If \(P\) is normal, so is \(A=P-\Pi\) because \(P\), \(P^*\), and \(\Pi\) commute; the spectral theorem gives \(\|A^t\|_F^2=\sum_j s_j(A)^{2t}\), hence \(\delta_t(P)=0\). If \(P\ne Q\), then \(D>0\), so the explicit gap in the theorem is positive for every finite \(t\). If \(P\) is ergodic and normal, every eigenvalue of \(A\) has modulus strictly below one, implying \(\|B\|_{2\to2,\pi}\le\|A\|_{2\to2,\pi}<1\). Thus \(Q^t\to\Pi\), which has every entry positive, so \(Q\) is primitive. At time zero both chains have the same squared distance \(N-1\); therefore their squared-Frobenius mixing times have the asserted ordering.

For arbitrary \(P\), cyclicity of trace gives

\[
\begin{aligned}
\delta_2(P)
&=\operatorname{tr}[(A^*A)^2]
-\operatorname{tr}[(A^*A)(AA^*)]\\
&=\tfrac12\operatorname{tr}[(A^*A-AA^*)^2]
=\tfrac12\|P^*P-PP^*\|_{F,\pi}^{2}.
\end{aligned}
\]

All traces and adjoints are in an orthonormal representation of \(\ell^2(\pi)\). Substituting this into Step 3 for \(t=2\) proves the sufficient near-normality criterion.

**Step 5: sharpness and nonnormal compression.** For \(P=rI+(1-r)\Pi\) and \(G=\Pi\), \(B=0\) and \(D=(N-1)r^2\), while \(\|P^t-\Pi\|_{F,\pi}^2=(N-1)r^{2t}\). Thus the universal coefficient is attained with equality.

For a genuinely directed example, on four states take the lazy clockwise cycle \(P=\tfrac12(I+S)\), where \(S(i,j)=\mathbf1_{\{j=i+1\pmod4\}}\), the uniform stationary law, and the partition \(\{\{0,1\},\{2\},\{3\}\}\). The baseline \(P\) is nonreversible and normal. Its averaged \(Q=GPG\) has \((QQ^{\mathsf T}-Q^{\mathsf T}Q)_{0,2}=-1/16\), so is **not normal**. Nevertheless its exact squared errors at times one and two are \(9/16\) and \(41/256\), respectively, versus \(1\) and \(1/2\) for \(P\). This checks a nontrivial use of Step 2 rather than inheriting normality after averaging.

## Verification

The standalone standard-library script `verify.py` constructs all partitions of small state spaces and independently checks stochasticity, stationarity, weighted normality, the one-step orthogonal identity, all-time quantitative gaps and their strictness using exact rational arithmetic. It also tests nonnormal baselines against the exact time-two commutator bound, a nonuniform stationary law, the directed four-cycle whose averaging is nonnormal, and coefficient-sharp full averaging. Running `python3 verify.py` passed **5,602 exact-rational assertions**. These finite checks are supplementary; arbitrary finite sizes, all integer times, and the sharp coefficient are proved analytically in the preceding steps.

## Relationship to prior work

Choi and Wang, *Bregman projections and partition design for accelerating finite Markov chains* (arXiv:2610.39239v1, first public October 29, 2026), Theorem 4.1 and Corollaries 4.2–4.4, establish an all-time squared-Frobenius comparison for **reversible** ergodic baselines. Their proof uses self-adjointness of both the baseline and averaged kernel to identify powered Frobenius norms with powered singular values. The present theorem replaces that use of self-adjointness with Schatten Hölder, allowing a **normal nonreversible** baseline even though its averaged chain may be nonnormal, and adds a dimension-sharp quantitative gap and a commutator-controlled nonnormality correction. Their one-step Bregman Pythagorean identity is a recognized antecedent of Step 1.

The earlier Choi–Wang group-averaging paper (arXiv:2509.02996) treats averaged samplers, spectral gaps and comparisons among averaging variants, not the stated all-time baseline-versus-Gibbs-compression quantitative defect. Choi, Hird and Wang (2025) study permutation and projection samplers under different averaging constructions. Generic Schatten Hölder, singular-value compression and the normal spectral theorem are classical ingredients, not claimed new here. The novelty assessment concerns their sharp combined Markov-chain comparison, subject to historical-priority uncertainty.

## Limitations

The conclusion concerns the squared \(\pi\)-weighted Frobenius distance, not pointwise total variation for every initial state. For nonnormal baselines the defect can outweigh the positive projection gap, so an unconditional all-time improvement is **not** claimed. The universal near-normality condition is sufficient rather than necessary. Improved transitions-to-tolerance do not automatically mean reduced computational cost once conditional sampling costs are included. The finite-state assumption, full support of \(\pi\), exact conditional Gibbs projection and normality requirement for the unconditional theorem are essential as stated. Independent mathematical audit and definitive priority determination are not asserted.

## References

1. M. C. H. Choi and Y. Wang, *Bregman projections and partition design for accelerating finite Markov chains*, arXiv:2610.39239v1 (October 29, 2026), especially §4, Theorem 4.1 and Corollaries 4.2–4.4. https://arxiv.org/html/2610.39239v1
2. M. C. H. Choi and Y. Wang, *Group-averaged Markov chains: mixing improvement*, arXiv:2509.02996, especially §§3–5. https://arxiv.org/html/2509.02996
3. M. C. H. Choi, M. Hird and Y. Wang, *Improving the Convergence of Markov Chains via Permutations and Projections*, Random Structures & Algorithms 66 (2025), e70016. https://doi.org/10.1002/rsa.70016
4. Standard finite-dimensional Eckart–Young singular-value approximation, Schatten Hölder inequality and the spectral theorem for normal matrices (classical matrix-analysis tools).
