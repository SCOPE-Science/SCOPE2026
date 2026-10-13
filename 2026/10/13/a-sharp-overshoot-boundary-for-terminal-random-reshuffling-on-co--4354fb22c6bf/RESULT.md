# A sharp overshoot boundary for terminal random reshuffling on common-Hessian quadratics

## Finding

Consider the same constant-stepsize stochastic component-gradient method, with either a fresh independent uniform permutation of every finite data set (random reshuffling, abbreviated RR), or independent uniform component indices at every step (IID). For a common-Hessian convex quadratic finite sum, **the expected objective at the last step of each complete epoch admits an exact sampling comparison** at every finite horizon.

Let \(n\ge2\), \(K\ge1\), \(d\ge1\), and let \(H\in\mathbb R^{d\times d}\) be real symmetric positive definite. Fix arbitrary centers \(b_1,\dots,b_n\in\mathbb R^d\) and write
\[
f_i(x)=\tfrac12(x-b_i)^\mathsf{T}H(x-b_i),\quad f(x)=\tfrac1n\sum_{i=1}^n f_i(x),\quad x_\star=\bar b=\tfrac1n\sum_i b_i.
\]
The update upon visiting index \(i\) is \(x^+=x-\eta H(x-b_i)\), with a common constant \(0<\eta<2/\lambda_{\max}(H)\). Both methods start at the same deterministic \(x_0\). RR draws an independent uniform permutation afresh at each epoch, while IID draws \(n\) independent uniform indices per epoch, independently between epochs. There are exactly \(nK\) component-gradient evaluations in either experiment.

Choose any orthonormal eigensystem \(Hu_r=\lambda_r u_r\), \(1\le r\le d\); define
\[
 v_r=\tfrac1n\sum_{i=1}^n\langle u_r,b_i-\bar b\rangle^2,\quad q_r=1-\eta\lambda_r,\quad
 A_n(q)=\sum_{j=0}^{n-1}q^j,\quad B_n(q)=\sum_{j=0}^{n-1}q^{2j},\quad G_K(q)=\sum_{k=0}^{K-1}q^{2nk}.
\]
Let \(\mathcal R_K=\mathbb E[f(x_{nK}^{\rm RR})-f(x_\star)]\), and let \(\mathcal I_K\) denote the same expected last-iterate excess for IID. Then **the exact terminal comparison** is
\[
\boxed{\displaystyle
 \mathcal R_K-\mathcal I_K
 =\sum_{r=1}^d\frac{\lambda_r(\eta\lambda_r)^2v_rG_K(q_r)}{2(n-1)}\bigl(B_n(q_r)-A_n(q_r)^2\bigr).}
\tag{1}
\]
For every \(-1<q<1\),
\[
\boxed{\displaystyle A_n(q)^2-B_n(q)=\frac{2q(1-q^n)(1-q^{n-1})}{(1-q)^2(1+q)}.}
\tag{2}
\]
All factors apart from \(q\) on the right are positive. Thus each eigenmode with \(v_r>0\) strictly favors RR for \(\eta\lambda_r<1\), is tied for \(\eta\lambda_r=1\), and strictly favors IID for \(\eta\lambda_r>1\). These statements hold for every positive integer \(n,K\).

The resulting **complete uniform-data phase classification** for each fixed positive-definite \(H\) and each stable step \(\eta\) is:

* \(\mathcal R_K\le\mathcal I_K\) for **every** choice of \(b_1,\dots,b_n,x_0\) if and only if \(\eta\le1/\lambda_{\max}(H)\).
* \(\mathcal I_K\le\mathcal R_K\) for **every** such choice if and only if \(\eta\ge1/\lambda_{\min}(H)\). This latter range intersects the stable interval only when the spectral condition number is strictly less than two, except for equality at a degenerate boundary.
* If \(1/\lambda_{\max}(H)<\eta<1/\lambda_{\min}(H)\), there are component-center choices with \(\mathcal R_K<\mathcal I_K\) and others with \(\mathcal I_K<\mathcal R_K\), even for the same \(H,\eta,n,K,x_0\). The orientation is determined by the center-variance spectral allocation in (1), not by a scalar condition number alone.

A scalar witness makes the reversal concrete: with \(n=2\), \(H=[1]\), centers \(b_1=1,b_2=-1\), initial \(x_0=0\), \(K=1\), and \(\eta=3/2\), the expected terminal squared errors are \(81/16\) for RR and \(45/16\) for IID. Thus their expected excess objectives are \(81/32\) and \(45/32\), respectively, despite each individual quadratic being smooth and strongly convex and both update schemes being stable. For the same data and \(\eta=1/2\), RR instead yields squared error \(1/16\) versus IID's \(5/16\).

## Assumptions and scope

The result concerns the **terminal iterate after an integral number of complete epochs**, not the average of the inner iterates and not an average of epoch endpoints. Each component has exactly the same strictly positive Hessian. The centers and initialization need not be random, and the centers may be identical, in which case both sampling methods coincide. Sampling is uniform across \(n\) components, IID permits repeats and omissions within an epoch, and RR reshuffles **independently** across epochs. All expectations are only over sample order or indices, not over the input centers.

The strict stability restriction \(0<\eta<2/\lambda_{\max}(H)\) ensures \(-1<q_r<1\), so all modes have finite nonzero positive geometric factors and the sign identity has no singular boundary. The exact expression (1) itself has a polynomial interpretation for arbitrary real \(q\), but no comparison is claimed at or beyond the stated stability boundary. The optimum value \(f(x_\star)\) may be positive because the component minima differ; excesses, rather than raw \(f\)-values, are compared.

No assumption of independent eigenmode noises is needed. Although a single permutation correlates different eigencoordinates, \(f(x)-f(x_\star)=\frac12\sum_r\lambda_r\langle u_r,x-x_\star\rangle^2\) contains no cross terms, so marginal second moments suffice, including when \(H\) has repeated eigenvalues.

## Proof

**Step 1: epoch-end linear recursion.** For any eigenmode \(r\), let \(e=\langle u_r,x-x_\star\rangle\), \(c_{i,r}=\langle u_r,b_i-x_\star\rangle\), and \(t_r=\eta\lambda_r\). Because \(\sum_i c_{i,r}=0\), an update using index \(i\) gives \(e^+=q_r e+t_r c_{i,r}\). After one complete epoch with sampled indices \(I_1,\dots,I_n\), where \(I_j\) are a permutation for RR and iid uniforms for IID, it follows exactly that
\[
 e_{k+1,r}=q_r^n e_{k,r}+t_r Z_{k,r},\qquad Z_{k,r}=\sum_{j=1}^n q_r^{n-j}c_{I_j,r}.
\tag{3}
\]
Both models have \(\mathbb E[Z_{k,r}]=0\). Independent resampling from epoch to epoch makes \(Z_{k,r}\) independent of the incoming epoch state. Hence
\[
 \mathbb E[e_{K,r}^2]=q_r^{2nK}e_{0,r}^2+t_r^2\mathbb E[Z_{0,r}^2]G_K(q_r).
\tag{4}
\]
This equality is exact even for a nonzero deterministic initialization.

**Step 2: second moments without and with replacement.** Fix \(r\), set \(v=v_r=\frac1n\sum_i c_{i,r}^2\), and abbreviate \(q=q_r\). For IID indices, different sampled positions have zero cross covariance and each has variance \(v\), giving
\[
 \mathbb E[Z_{0,r}^2\mid\mathrm{IID}]=v B_n(q).
\tag{5}
\]
For a uniform permutation, every position has the same variance \(v\). At two distinct positions \(j\ne\ell\),
\[
\mathbb E[c_{I_j,r}c_{I_\ell,r}]=\frac{1}{n(n-1)}\sum_{a\ne b}c_{a,r}c_{b,r}=-\frac{v}{n-1},
\]
by the zero-sum identity. Squaring the weighted sum in (3) therefore gives
\[
 \mathbb E[Z_{0,r}^2\mid\mathrm{RR}]
 =v B_n(q)-\frac{v}{n-1}(A_n(q)^2-B_n(q))
 =\frac{v}{n-1}\bigl(nB_n(q)-A_n(q)^2\bigr).
\tag{6}
\]
Subtract (5) from (6), substitute into (4), and sum with weights \(\lambda_r/2\). The initialization contribution cancels exactly, yielding (1). This part is a finite-population covariance identity and does not assume a bound on the sign of \(q\).

**Step 3: factorization and sign.** For \(-1<q<1\), the geometric-sum formulas are \(A_n(q)=(1-q^n)/(1-q)\) and \(B_n(q)=(1-q^{2n})/(1-q^2)\). Direct subtraction simplifies to (2). Indeed,
\[
 \frac{(1-q^n)^2}{(1-q)^2}-\frac{(1-q^n)(1+q^n)}{(1-q)(1+q)}
 =\frac{2q(1-q^n)(1-q^{n-1})}{(1-q)^2(1+q)}.
\]
Because \(|q|<1\), each of \(1-q^n\), \(1-q^{n-1}\), \(1+q\), and \((1-q)^2\) is strictly positive. Moreover \(\lambda_r>0\), \(t_r^2>0\), and \(G_K(q_r)>0\), proving the asserted sign of every nonzero-variance contribution and tying it to the threshold \(t_r=1\).

**Step 4: necessity and mixed regimes.** If \(\eta\le1/\lambda_{\max}(H)\), every \(q_r\ge0\), so (1) is nonpositive for arbitrary centers. Conversely, if \(\eta>1/\lambda_{\max}(H)\), choose an eigenvector \(u\) of \(\lambda_{\max}(H)\), let \(b_1=u\), \(b_2=-u\), and \(b_i=0\) for \(i\ge3\). Then exactly one eigendirection has positive centered variance, and its \(q<0\), so (1) is strictly positive. This proves the first if-and-only-if. Similarly, \(\eta\ge1/\lambda_{\min}(H)\) makes all \(q_r\le0\), forcing (1) nonnegative; for \(\eta<1/\lambda_{\min}(H)\), the same centered construction along a minimum-eigenvalue eigenvector forces (1) strictly negative. This proves the second. In the strict intermediate regime, both witness choices are valid simultaneously, and they yield the two possible strict orderings for every \(K\). If \(\lambda_{\max}=\lambda_{\min}\), that intermediate interval is empty, as required.

**Step 5: explicit numbers.** For \(n=2\) and centers \(\pm1\), one epoch begins at the minimizer and has \(v=1\). With \(q=-1/2\) and \(t=3/2\), (5) gives \(\mathbb E[e^2_{1}\mid\mathrm{IID}]=\frac94(1+\frac14)=\frac{45}{16}\), whereas (6) gives \(\mathbb E[e^2_{1}\mid\mathrm{RR}]=\frac94(2(1+\frac14)-(1-\frac12)^2)=\frac{81}{16}\). With \(q=1/2\) and \(t=1/2\), the corresponding exact values are \(5/16\) and \(1/16\). This completes all quantifiers, including strict witnesses and boundary ties.

## Verification

The included standalone `verify.py` is a standard-library Python 3 checker using `fractions.Fraction`. Running `python verify.py` returns `VERIFY_OK 123 exact-rational cases`. It independently enumerates complete random-permutation and with-replacement histories (including repeated epochs), compares exact second moments to (4)--(6), tests \(n=2,3,4\), both positive and negative \(q\), \(q=0\), and horizons through three epochs, and verifies a two-eigenvalue instance with either strict sign. An additional symbolic identity check using polynomial cancellation was performed for \(2\le n\le12\). These are finite consistency tests; the preceding finite-population identity, factorization, and eigenmode argument prove the unlimited \(n,K,d\) statements.

## Relationship to prior work

Liu, *Random Reshuffling Dominates Stochastic Gradient Descent* (arXiv:2606.32005, June 2026; extended Optimization Online version, September 2026), establishes a stronger rate guarantee than conventional SGD **for a carefully weighted average of all within-epoch iterates**. Its Theorem 1 does not compare expected objectives of the two methods' individual terminal iterates on the same data. The present exact calculation demonstrates a sharp reversal of that **different output metric**, and does not contradict the averaged-output theorem. Neither rate bound asserts pointwise last-iterate stochastic dominance.

Ying, *Learning Under Random Reshuffling and Distributed Features* (2018 dissertation, Chapter 3, Lemma 3.1 and Theorem 3.2), derives the underlying weighted finite-population covariance formula for nonnegative scalar weights and positive-semidefinite matrix weights, and proves small-step stationary behavior. Formula (6) is **not claimed as an original covariance lemma**. The new claim is the exact comparison with iid terminal objectives across the **signed** contraction regime \(-1<q<0\), together with its sharp reciprocal-curvature transition and complete spectral classification. In particular the existing covariance lemma explicitly assumes a nonnegative scalar weight and therefore does not by itself assert the reverse-order regime.

De Sa, *Random Reshuffling Is Not Always Better* (NeurIPS 2020), shows that a broad matrix-product conjecture fails using noncommuting multiplicative examples in noiseless quadratic problems. That result already warns against unconditional superiority; it neither supplies the same common-Hessian noisy finite-sum model nor proves (1) and the exact data-uniform threshold. Dewasurendra, *The Missing Horizon in Random Reshuffling* (full PDF), analyzes the minimax risk of the **all-inner average** and includes a common-Hessian bridge construction, but its stated step regime is \(\eta\le1/(6L)\), excluding the present negative-contraction boundary. Shaw and Whalley (2025) treat stochastic-gradient Langevin dynamics and mention SGD-RR bounds for steps below \(1/L\); those upper bounds do not imply the sharp reverse comparison for \(1/L<\eta<2/L\).

## Limitations

The theorem is an exact expectation comparison on quadratic finite sums with a **shared fixed positive Hessian** and iid reshuffling between epochs. It does not imply analogous comparisons for heterogeneous or noncommuting Hessians, nonquadratic functions, mini-batches, fixed shuffles, last iterates within incomplete epochs, pathwise ordering, or weighted averages. It measures objective excess; a statement about generalization, distributional dominance, or computational speed is not made. The algebraic covariance precursor is known for nonnegative scalar weighting. A preexisting analysis of signed geometric weights or another equivalent last-iterate phase classification could make the claimed comparison nonoriginal; the checked sources did not establish one.

## References

1. Zijian Liu, *Random Reshuffling Dominates Stochastic Gradient Descent*, arXiv:2606.32005v1, first public 2026-06-30. https://arxiv.org/abs/2606.32005
2. Zijian Liu, *Random Reshuffling for Smooth Convex Optimization: Dominates Stochastic Gradient Descent*, extended manuscript, September 2026, Theorem 1 and Algorithm 1. https://optimization-online.org/wp-content/uploads/2026/09/Random-Reshuffling-for-Smooth-Convex-Optimization.pdf
3. Bicheng Ying, *Learning Under Random Reshuffling and Distributed Features*, dissertation (2018), Chapter 3, Lemma 3.1, equations (3.46)--(3.57). https://escholarship.org/content/qt76r7c14r/qt76r7c14r.pdf
4. Christopher De Sa, *Random Reshuffling Is Not Always Better*, NeurIPS 2020, Sections 1--2. https://proceedings.neurips.cc/paper_files/paper/2020/file/42299f06ee419aa5d9d07798b56779e2-Paper.pdf
5. Pahan Dewasurendra, *The Missing Horizon in Random Reshuffling*, Sections 1, 5 and Appendix C, full manuscript. https://andotheror.github.io/pdf/the-missing-horizon-in-random-reshuffling.pdf
6. Luke Shaw and Peter A. Whalley, *Random Reshuffling for Stochastic Gradient Langevin Dynamics*, arXiv:2501.16055, Theorems 3.5--3.6. https://arxiv.org/abs/2501.16055
