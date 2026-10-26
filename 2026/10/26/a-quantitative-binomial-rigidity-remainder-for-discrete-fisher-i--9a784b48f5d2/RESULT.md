# A quantitative binomial rigidity remainder for discrete Fisher-information convolution

## Finding
For every pair of strictly positive finitely supported probability masses satisfying the alternating-balance condition of Ball and Gárgyán, their discrete Fisher-information convolution deficit admits an explicit **three-term nonnegative remainder**. Besides quantifying weighted score-increment mismatch, it controls the squared distances of both score-increment sequences from constant increments. It consequently yields explicit total-variation stability toward the balanced binomial distributions, with an optimal square-root dependence on the information deficit in fixed support dimensions.

For integers \(m,n\ge1\), let \(f=(f_0,\ldots,f_m)\), \(g=(g_0,\ldots,g_n)\) have positive entries summing to one and satisfy
\[
\sum_{i=0}^{m}(-1)^i f_i=0,\qquad \sum_{j=0}^{n}(-1)^j g_j=0.
\]
Their discrete score sequences and Fisher information are defined below. For positive real \(a,b\), set
\[
\mathcal G_{a,b}=a^2J(f)+b^2J(g)-(a+b)^2J(f*g),\qquad c=(\min_i f_i)^2(\min_jg_j)^2.
\]
Let \(\Delta s_i=s_i-s_{i-1}\) and \(\Delta t_j=t_j-t_{j-1}\); define
\[
E_f=\sum_{i=1}^{m}(\Delta s_i-4/m)^2,\quad E_g=\sum_{j=1}^{n}(\Delta t_j-4/n)^2.
\]
Then the main result is
\[
\boxed{\mathcal G_{a,b}\ge c\left[n a^2E_f+m b^2E_g+16mn\left(\frac a m-\frac b n\right)^2\right].}
\]
For positive \(a,b\), equality \(\mathcal G_{a,b}=0\) holds **if and only if** \(f=\mathrm{Bin}(m,1/2)\), \(g=\mathrm{Bin}(n,1/2)\), and \(a/m=b/n\). In particular, equality in the reciprocal discrete Blachman–Stam inequality holds precisely for the two balanced binomial distributions.

An explicit probability-distance consequence is as follows. Define
\[
\tau_f=\sqrt{\frac{m\mathcal G_{a,b}}{cna^2}},\qquad
\tau_g=\sqrt{\frac{n\mathcal G_{a,b}}{cmb^2}}.
\]
If \(\tau_f\le2/m\), then
\[
\boxed{d_{\mathrm{TV}}\!\left(f,\mathrm{Bin}(m,1/2)\right)\le\min\left\{1,\frac{e^{m^2\tau_f}-1}{2}\right\}.}
\]
The analogous conclusion holds for \(g\) when \(\tau_g\le2/n\), with \(m\) replaced by \(n\). Both bounds are local statements with explicit, possibly small, mass-dependent constants; no dimension-free stability is asserted.

## Assumptions and scope
Let \(m,n\) be arbitrary positive integers. The support is exactly \(\{0,\ldots,m\}\) for \(f\) and \(\{0,\ldots,n\}\) for \(g\), all masses strictly positive, and both laws alternate-balance as above. No log-concavity assumption is imposed. For a law \(p=(p_0,\ldots,p_d)\) in this class, define its score explicitly by
\[
\sigma_i(p)=2-\frac4{p_i}\sum_{u=0}^{i}(-1)^{i-u}p_u,\quad 0\le i\le d,\qquad
J(p)=\sum_{i=0}^{d}p_i\sigma_i(p)^2.
\]
These are the finite-path Laplacian score and associated information introduced in the source. Write \(s_i=\sigma_i(f)\), \(t_j=\sigma_j(g)\), and \(h=f*g\). Its mass at \(k\) is \(h_k=\sum_{i+j=k}f_ig_j\). The endpoint identities \(s_0=t_0=-2\), \(s_m=t_n=2\) follow directly from positive normalization and alternating balance.

## Proof
**1. Exact conditional-variance identity.** Let independent \(X\sim f\) and \(Y\sim g\); put \(S=X+Y\), \(W=as_X+bt_Y\). The score-convolution identity (also derivable by reordering the alternating sums) gives
\[
\mathbb E[s_X\mid S=k]=\mathbb E[t_Y\mid S=k]=\sigma_k(h),\quad
\mathbb E[W\mid S]=(a+b)\sigma_S(h).
\]
The individual scores have mean zero. Hence independence yields \(\mathbb E[W^2]=a^2J(f)+b^2J(g)\). Therefore
\[
\mathcal G_{a,b}=\mathbb E[\operatorname{Var}(W\mid S)].
\]
Using the weighted variance identity on each fiber \(i+j=k\) gives the exact finite equality
\[
\mathcal G_{a,b}=\sum_{k=0}^{m+n}\frac{1}{h_k}
\sum_{\substack{(i,j)<(i',j')\\i+j=i'+j'=k}}
f_ig_jf_{i'}g_{j'}\left[a(s_i-s_{i'})+b(t_j-t_{j'})\right]^2.
\]
Here \(<\) is any fixed total order on index pairs; each distinct unordered pair is counted exactly once. The displayed sum is an algebraic identity, not an asymptotic argument.

**2. Keep adjacent fiber edges.** For each \(1\le i\le m\), \(1\le j\le n\), the pairs \((i,j-1)\) and \((i-1,j)\) lie in the same fiber. Keeping only their nonnegative contributions yields
\[
\mathcal G_{a,b}\ge\sum_{i=1}^{m}\sum_{j=1}^{n}
\frac{f_i f_{i-1}g_jg_{j-1}}{h_{i+j-1}}
(a\Delta s_i-b\Delta t_j)^2.
\]
Every positive mass is at least its minimum, and \(0<h_k\le1\). Thus each coefficient in this sum is at least \(c\). By the endpoint score identities, \(\sum_i\Delta s_i=4\) and \(\sum_j\Delta t_j=4\). Expanding around these means gives the exact orthogonal decomposition
\[
\sum_{i,j}(a\Delta s_i-b\Delta t_j)^2
=na^2E_f+mb^2E_g+mn(4a/m-4b/n)^2.
\]
The claimed three-term remainder follows for all allowed support sizes.

**3. Exact equality classification.** If \(\mathcal G_{a,b}=0\), positivity of \(c,a,b\) forces \(E_f=E_g=0\) and \(a/m=b/n\). Thus \(s_i=-2+4i/m\) and \(t_j=-2+4j/n\). Let \(A_i=\sum_{u=0}^i(-1)^{i-u}f_u\). Since \(A_i=f_i-A_{i-1}\), the defining score formula yields the adjacent ratio recurrence
\[
(2+s_i)f_i=(2-s_{i-1})f_{i-1},\qquad
\frac{f_i}{f_{i-1}}=\frac{m-i+1}{i},\quad1\le i\le m.
\]
Normalization uniquely yields \(f_i=2^{-m}\binom mi\); similarly \(g_j=2^{-n}\binom nj\). Conversely their affine scores satisfy \(as_i+bt_j=-2(a+b)+(4a/m)(i+j)\) when \(a/m=b/n\), a deterministic function of \(S\). The conditional variance vanishes.

Because \(J(\mathrm{Bin}(m,1/2))=4/m\), taking \(a=J(f)^{-1}\), \(b=J(g)^{-1}\) translates the result into equality rigidity for the reciprocal Blachman–Stam inequality. Positivity of \(J\) follows from \(s_0=-2\) and \(f_0>0\).

**4. Quantitative total-variation estimate.** Cauchy–Schwarz gives, for each \(i\),
\[
\left|s_i-(-2+4i/m)\right|
=\left|\sum_{r=1}^{i}(\Delta s_r-4/m)\right|
\le\sqrt{mE_f}\le\tau_f.
\]
Let \(B_i=2^{-m}\binom mi\). The ratio recurrence, now without assuming score linearity, gives
\[
\frac{f_i}{f_{i-1}}=\frac{2-s_{i-1}}{2+s_i},\qquad
\frac{B_i}{B_{i-1}}=\frac{4(m-i+1)/m}{4i/m}.
\]
When \(\tau_f\le2/m\), the four positive factors compared in these fractions are all at least \(2/m\). Using \(|\log u-\log v|\le |u-v|/\min(u,v)\) gives
\[
\left|\log\frac{f_i/B_i}{f_{i-1}/B_{i-1}}\right|\le m\tau_f.
\]
The range of \(\log(f_i/B_i)\) is therefore at most \(m^2\tau_f\). Since \(\sum_iB_i(f_i/B_i)=1\), that range straddles zero, proving \(e^{-m^2\tau_f}\le f_i/B_i\le e^{m^2\tau_f}\). Summation of absolute mass differences then gives the stated total-variation bound. The proof for \(g\) is identical.

**5. Square-root scale cannot be improved in general.** Fix \(m=n=2\), \(g=\mathrm{Bin}(2,1/2)\), and \(f=(1/4+\varepsilon,1/2,1/4-\varepsilon)\) for \(0<|\varepsilon|<1/4\). Both balance conditions hold. For the reciprocal-information choices \(a=1/J(f)\), \(b=1/J(g)\), direct rational expansion gives
\[
\mathcal G_{a,b}=\frac{10}{3}\varepsilon^2+O(\varepsilon^4),\qquad
 d_{\mathrm{TV}}(f,\mathrm{Bin}(2,1/2))=|\varepsilon|.
\]
More exactly, for this family direct substitution gives the positive rational identity
\[
\mathcal G_{a,b}=\frac{2\varepsilon^2(1-16\varepsilon^2)(5-8\varepsilon^2)(1+8\varepsilon^2)}{3(1-4\varepsilon^2)(1+16\varepsilon^2)^2}.
\]
The exponent \(1/2\) in any local estimate using only \(\mathcal G_{a,b}\) cannot in general be increased. No optimal multiplicative constant is asserted.

## Verification
The accompanying standalone script `verify_stam_stability.py` uses exact rational arithmetic. It checks the score conditional-expectation identities and the full pairwise conditional-variance equality, tests the adjacent-pair remainder for 400 independently constructed alternating-balanced positive pairs with varying rational weights, checks 100 binomial equality cases, and tests six rational perturbations. All 506 tested configurations passed. The mathematical argument above covers all positive real masses and weights; the finite checks are independent consistency tests, not an exhaustive proof.

Run with `python verify_stam_stability.py` from the directory containing the extracted files; it requires only Python's standard library.

## Relationship to prior work
Ball and Gárgyán (2026), Definition 1 and Theorem 4, introduced the score used here and proved the unquantified discrete Blachman–Stam inequality through conditional Cauchy–Schwarz. Their Proposition 3 established that a linear score characterizes the balanced binomial law in the discrete Cramér–Rao equality case. Those are antecedents, not the claimed result. The new claim is the explicit convolution **deficit decomposition and total-variation near-equality bound**, including optimal local square-root exponent. The earlier work on finite-group discrete Fisher information by Gibilisco and Isola and the earlier discrete Stam study by Nishiyama use other information frameworks; their named inequalities cannot directly imply a quantitative remainder for this particular score without further new reduction. Literature checks do not establish absolute priority.

## Limitations
The coefficient \(c\) depends on the smallest individual masses and may be extremely small; no uniform dimension-free estimate or sharp coefficient is claimed. Total-variation conclusions require the stated quantitative small-deficit hypothesis. Supports are contiguous finite integer intervals, and all masses must be strictly positive and alternating-balanced. No infinite-support limiting theorem is established. The checked finite examples do not substitute for proof. Independent external validation has not been performed.

## References
1. Keith M. Ball and Barnabás Gárgyán, *On the discrete Fisher information*, arXiv:2610.19076v1 (first public submission 2026-10-13), Definition 1, Proposition 3, Theorem 4. https://arxiv.org/html/2610.19076v1
2. Tomohiro Nishiyama, *Cramér–Rao-type Bound and Stam's Inequality for Discrete Random Variables*, arXiv:1904.12704v2 (2019). https://arxiv.org/abs/1904.12704
3. Paolo Gibilisco and Tommaso Isola, *Fisher information and Stam inequality on a finite group*, Bulletin of the London Mathematical Society 40 (2008), 855–862. Distinct finite-group score framework.
