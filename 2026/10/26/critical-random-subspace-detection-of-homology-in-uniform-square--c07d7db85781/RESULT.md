# Critical random-subspace detection of homology in uniform square-zero linear maps

## Finding

Fix a prime power \(q\ge2\). Let \(n=2m+\varepsilon\), where \(\varepsilon\in\{0,1\}\) and \(m\to\infty\). Choose \(D\) uniformly from all linear maps on \(V=\mathbb F_q^n\) satisfying \(D^2=0\), and independently choose an \(m\)-dimensional subspace \(W\) uniformly from the Grassmannian. Put
\[
K_m=m-\dim\operatorname{im}D,\qquad
J_m=\dim(W\cap\ker D)-K_m,\qquad
T_m=\dim\frac{(W\cap\ker D)+\operatorname{im}D}{\operatorname{im}D}.
\]
All three are nonnegative integers. There is a complete, explicit limiting joint distribution. Write \(Q=q^{-1}\) and \((Q;Q)_a=\prod_{i=1}^{a}(1-Q^i)\), with \((Q;Q)_0=1\) and \((Q;Q)_\infty=\prod_{i\ge1}(1-Q^i)\). Define
\[
w_\varepsilon(k)=\frac{Q^{2k(k+\varepsilon)}}{(Q;Q)_{2k+\varepsilon}},\qquad
Z_\varepsilon=\sum_{k\ge0}w_\varepsilon(k),\qquad
\beta_k(j)=\frac{(Q;Q)_\infty Q^{j(j+k)}}{(Q;Q)_{j}(Q;Q)_{j+k}}.
\]
For \(k,j\ge0\), \(h=\varepsilon+2k\), and \(0\le t\le\min\{h,k+j\}\),
\[
\lim_{m\to\infty}\Pr(K_m=k,J_m=j,T_m=t)
=\frac{w_\varepsilon(k)}{Z_\varepsilon}\,\beta_k(j)\,
\frac{{h\brack t}_q{k+j\brack t}_q\lvert\mathrm{GL}_t(q)\rvert}{q^{h(k+j)}}.
\]
Here \({a\brack b}_q\) is the Gaussian binomial coefficient. The displayed mass is zero outside the specified ranges, and the sum of all displayed masses is one. Thus, conditioned on a random homology defect \(\varepsilon+2K\), the excess intersection \(J\) has a \(q\)-nullity law, and the detected homology dimension \(T\) has the rank law of an independent uniform \((\varepsilon+2K)\)-by-\((K+J)\) matrix.

In the first-order language of \(\mathbb F_q\)-vector spaces with the linear function \(D\) and unary predicate \(W\), the sentence
\[
\phi:=\exists x\,\bigl(W(x)\land D(x)=0\land\neg\exists y\,(D(y)=x)\bigr)
\]
says that the probe subspace contains a cycle representing a nonzero homology class. Its probability has the two parity-subsequence limits
\[
L_\varepsilon(q)=1-\frac1{Z_\varepsilon}\sum_{k,j\ge0}w_\varepsilon(k)\beta_k(j)q^{-(\varepsilon+2k)(k+j)}.
\]
In particular, direct certified truncation of the rapidly decaying positive series gives
\[
0.3374<L_0(2)<0.3375,\qquad 0.4361<L_1(2)<0.4362.
\]
Consequently, this natural random expansion of finite vector spaces has **no full-sequence first-order convergence law**; the displayed sentence already has distinct even- and odd-dimensional limits.

## Assumptions and scope

The field \(\mathbb F_q\) and the parity \(\varepsilon\) are fixed. The probability distribution on \(D\) is uniform over all square-zero endomorphisms, *not* the distribution obtained by squaring an unrestricted random matrix. The random probe \(W\) has dimension exactly \(m=\lfloor n/2\rfloor\). The first-order vocabulary contains vector addition, zero, scalar multiplication by each field element, the unary linear function \(D\), and the unary predicate for membership in \(W\). The result is a joint limit for the three specified dimension statistics and a particular first-order sentence; it does not claim convergence for every sentence along either parity subsequence.

## Proof

**Exact differential counts.** For any square-zero map of rank \(r\), let \(I=\operatorname{im}D\), \(K=\ker D\). Their dimensions are \(r\) and \(n-r\), and \(I\subseteq K\). Choose \(I\), choose \(K\supseteq I\), and choose an isomorphism \(V/K\to I\). Thus the number of rank-\(r\) maps is exactly
\[
C_{n,r}={n\brack r}_q{n-r\brack r}_q\lvert\mathrm{GL}_r(q)\rvert
=q^{2r(n-r)}\frac{(Q;Q)_n}{(Q;Q)_r(Q;Q)_{n-2r}}.
\]
Let \(n=2m+\varepsilon\), \(r=m-k\). Dividing these counts by \(q^{2m(m+\varepsilon)}\) yields \(w_\varepsilon(k)(Q;Q)_n/(Q;Q)_{m-k}\). The final product ratio is at most one and tends to one for fixed \(k\). Since \(\sum_kw_\varepsilon(k)<\infty\), dominated convergence proves total-variation convergence of \(K_m\) to the mass function \(w_\varepsilon/Z_\varepsilon\).

**Exact flag counts.** For fixed \(D\), write \(h=n-2r\), \(s=n-r\), \(b=\dim(W\cap K)\), and \(t=\dim((W\cap K+I)/I)\), so \(a=b-t=\dim(W\cap I)\). The number of \(b\)-subspaces \(U\subseteq K\) with \(\dim(U\cap I)=a\) is
\[
{r\brack a}_q{h\brack t}_q q^{t(r-a)}.
\]
For a fixed such \(U=W\cap K\), the number of \(m\)-subspaces \(W\) with that exact intersection is
\[
{n-s\brack m-b}_q q^{(s-b)(m-b)}.
\]
Multiplication and division by \({n\brack m}_q\) give the *exact finite-dimensional joint law*, with the convention that Gaussian coefficients outside their natural ranges vanish and the expression is zero unless all exponents are nonnegative.

**Limit of the intersection dimension.** Given \(K_m=k\), put \(b=k+j\). Summing the finite flag count over \(t\) gives
\[
\Pr(\dim(W\cap K)=b\mid K_m=k)
=\frac{{s\brack b}_q{n-s\brack m-b}_q q^{(s-b)(m-b)}}{{n\brack m}_q}.
\]
Inserting the standard product expression for the three Gaussian coefficients and cancelling all powers of \(q\) yields the fixed-\(j\) limit \(\beta_k(j)\); the net power is \(q^{-j(j+k)}\). The probabilities are tight: their exact product formula admits a summable \(O_q(q^{-j(j+k)})\) bound uniformly for sufficiently large \(m\). Equivalently, normalization follows from the Gaussian-binomial intersection identity and dominated convergence.

**Limit of homology detection.** Conditional on \(W\cap K=U\) and its dimension \(b\), the subspace \(U\) is uniform among \(b\)-subspaces of \(K\). Generate \(U\) by \(b\) independent uniform vectors of \(K\), conditioned on their independence. For each fixed \(b\), the conditioning event has probability tending to one as \(\dim K\to\infty\). Their images in the fixed-dimensional quotient \(K/I\cong\mathbb F_q^h\) are exactly independent uniform vectors before conditioning. Hence \(t\) converges to the rank of a uniform \(h\)-by-\(b\) matrix, with mass \({h\brack t}_q{b\brack t}_q\lvert\mathrm{GL}_t(q)\rvert q^{-hb}\). Truncation in \(k,j\) and the previously proved tightness yield the full joint law.

**First-order witness and parity.** The formula \(\phi\) holds exactly when \(T_m\ge1\). The limiting conditional probability of \(T=0\) is \(q^{-hb}\), the probability that the induced matrix is identically zero. Averaging yields \(L_\varepsilon(q)\). At \(q=2\), truncating \(k,j<8\) and the product \((Q;Q)_\infty\) after 128 factors gives the displayed separated intervals: the missing tails are bounded by \(4\sum_{k\ge8}2^{-2k^2}\) and \(4\sum_{j\ge8}2^{-j^2}\), and the product error is below \(2^{-127}\). Their total is smaller than \(10^{-14}\). The intervals are disjoint, proving nonconvergence.

## Verification

The included Python checker reconstructs square-zero maps directly for \(n\le4\) over \(\mathbb F_2\), enumerates every half-dimensional probe subspace, and compares the \((r,b,t)\) census with the two independent Gaussian-binomial formulas. It also verifies exact normalization for \(q=2,3,4\), \(2\le n\le12\), and every permitted rank. Its successful output is:

`SQUARE_ZERO_RANDOM_SUBSPACE_OK 343 11227 141 even 0.337415921240 odd 0.436153157721`

The 343 endomorphisms and 11,227 endomorphism/probe pairs exhaust only the stated small finite cases. The proof of the limiting distribution uses exact enumeration and limit arguments, not finite-case extrapolation. Reproduce with `python3 checker.py`.

## Relationship to prior work

The ungraded finite-field square-zero differential model and its homology-rank limit law are due to Ginzburg and Pasechnik (2017), building on earlier square-zero enumeration by Kovács. Those known formulas supply the marginal \(K\)-law, but neither an independent critical-dimensional random probe, a joint three-statistic intersection law, nor the parity-separated first-order detection formula. Catanzaro and Zabka (2021) study a distinct sequential differential model and Betti distributions. Ababneh and Kahle (2026) analyze real-vector-space random complexes rather than the finite-field probe law. Koponen (2026) motivates attention to first-order probabilities of expansions of finite structures but does not analyze square-zero operators with random Grassmannian predicates. Elementary Gaussian-binomial intersection and rectangular-matrix rank identities are standard ingredients; the contribution here is their coupling to the random homology defect and the resulting parity-sensitive first-order law.

## Limitations

The only asserted first-order nonconvergence is witnessed by \(\phi\); no universal first-order classification is claimed. The probe dimension is half the ambient dimension, and the field size is fixed. Generalizations to other probe dimensions, graded chain complexes, nonuniform random differentials, or other logical formulas are not established here. Historical priority beyond the inspected literature is not certified, and no independent scientific audit has been performed.

## References

1. V. L. Ginzburg and D. V. Pasechnik, *Random Chain Complexes*, Arnold Mathematical Journal (2017), arXiv:1602.08538, https://amj.math.stonybrook.edu/html-articles/Files-2015-2024/16-62/ .
2. M. J. Catanzaro and M. J. Zabka, *A Model for Random Chain Complexes*, arXiv:1901.00964 (first submitted 2019-01-04), https://arxiv.org/abs/1901.00964 .
3. A. Ababneh and M. Kahle, *Random chain complexes of real vector spaces*, arXiv:2602.10783 (first submitted 2026-02-11), https://arxiv.org/abs/2602.10783 .
4. V. Koponen, *A characterization of the finite model property for \(\omega\)-categorical theories*, arXiv:2610.16163v1 (first submitted 2026-10-12; primary MSC 03C13), https://arxiv.org/html/2610.16163v1 .
