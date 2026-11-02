# Five is the unique update-optimal reuse count in rolling cyclic Ritz descent

## Finding
For the rolling cyclic Ritz (RCR) implementation studied by Gu [1], the constant number of successive uses of each historical Ritz step can be selected by maximizing its proved doubly-exponential decay **per actual gradient update**. In the exactly solvable active-spectrum regime \(q=m+1\), and for every integer memory \(m\ge 1\), the unique optimal integer reuse count is
\[
\boxed{\ell_\star=5.}
\]
The resulting exact generic asymptotic double-log slope is
\[
\max_{\ell\in\mathbb N_{\ge1}}\lim_{t\to\infty}\frac{\log(-\log\|g_t^{(\ell)}\|)}{t}
=\frac{1}{5m}\log\!\left(\frac{7+\sqrt{41}}2\right).
\]
Equivalently the maximal per-update doubly-exponential base is \(\big((7+\sqrt{41})/2\big)^{1/(5m)}\). The runner-up \(\ell=4\) is close but **strictly inferior**; infinitely repeated Ritz steps ultimately lose per-update efficiency.

## Assumptions and scope
Let \(f(x)=\tfrac12 x^{\mathsf T}Ax+b^{\mathsf T}x\), with a finite real symmetric positive definite \(A\). Fix \(m\ge1\). Exactly \(q=m+1\) distinct eigenvalues have nonzero projection in the starting gradient; eigenvalue multiplicities are permitted. Use the fully specified RCR cycle and matched full-rank history initialization of [1, Section 2], without restarts, safeguards, premature stopping, or floating-point rounding. A cycle contains precisely \(m\ell\) actual gradient updates and repeats each of the \(m\) historical reciprocal Ritz values exactly \(\ell\) times. For each integer \(\ell\ge1\), denote the resulting actual gradients by \(g_t^{(\ell)}\).

Gu's [1, Theorem 5] exceptional set for each fixed \(\ell\) has Lebesgue measure zero among admissible full-support initial points. Their countable union together with the rank-deficient/non-full-support initial points is also null. Consequently one **common full-measure set** supports the displayed rate comparisons simultaneously for all integer \(\ell\). The comparison is pointwise among these runs, all using the source's matched initialization convention. The stated rate is the limit of a double logarithm and does not compare transient constants or floating-point wall time.

## Proof
**Step 1 — transfer of the source's exact rates.** Theorem 5 of [1], including the transfer to every actual gradient update in its equation (23), gives
\[
L_m(\ell):=\lim_{t\to\infty}\frac{\log(-\log\|g_t^{(\ell)}\|)}t=\frac{\log\sigma_\ell}{m\ell},
\]
where
\[
\sigma_\ell=\begin{cases}
\sqrt2,&\ell=1,2,\\
2,&\ell=3,\\
\frac{2\ell-3+\sqrt{(2\ell-3)^2-8}}2,&\ell\ge4.
\end{cases}
\]
The source derives these quantities from the characteristic equation of its exact delayed weight recurrence, rather than a simplified spectral model. Since \(m\) is a fixed positive factor, it is enough to maximize \(\log\sigma_\ell/\ell\) over the positive integers.

**Step 2 — a strict tail monotonicity theorem.** Extend \(\sigma_\ell\) for real \(x\ge4\) by \(s(x)=(2x-3+\sqrt{(2x-3)^2-8})/2\). Write \(d(x)=\sqrt{(2x-3)^2-8}\), \(F(x)=\log s(x)/x\), and \(H(x)=\log s(x)-2x/d(x)\). Direct differentiation gives
\[
F'(x)=-\frac{H(x)}{x^2},\quad
\frac{d}{dx}\log s(x)=\frac2{d(x)},\quad
H'(x)=\frac{4x(2x-3)}{d(x)^3}>0\quad(x\ge4).
\]
We prove \(H(5)>0\) with entirely rational bounds. Since \(\sqrt{41}>32/5\), we have \(s(5)=(7+\sqrt{41})/2>67/10\) and \(10/\sqrt{41}<25/16\). For \(u=(67/10-1)/(67/10+1)=57/77\), the convergent positive series for \(\log[(1+u)/(1-u)]\) yields
\[
\log s(5)>\log(67/10)>2\left(\frac{57}{77}+\frac{(57/77)^3}{3}\right)=\frac{799368}{456533}>\frac{25}{16}>\frac{10}{\sqrt{41}}.
\]
Thus \(H(5)>0\), and strict increase of \(H\) proves \(F'(x)<0\) for every real \(x\ge5\). No integer \(\ell\ge6\) can maximize.

**Step 3 — strict dominance over all short cycles.** The exact radical expressions give
\[
\sigma_5=\frac{7+\sqrt{41}}2>\frac{67}{10},\qquad
\sigma_4=\frac{5+\sqrt{17}}2<\frac{457}{100},
\]
where the second inequality follows from \(17<(207/50)^2\). The integer calculation
\[
\left(\frac{67}{10}\right)^4-\left(\frac{457}{100}\right)^5
=\frac{217738505943}{10000000000}>0
\]
therefore implies \(\sigma_5^4>\sigma_4^5\), or \(F(5)>F(4)\). Moreover \(\sigma_5^2>(67/10)^2>32\), so \(\sigma_5^{1/5}>\sqrt2\). This beats \(\sigma_1^{1/1}=\sqrt2\), \(\sigma_2^{1/2}=2^{1/4}\), and \(\sigma_3^{1/3}=2^{1/3}\). Together with Step 2, it proves that the unique maximizing integer is \(\ell=5\). Multiplication by \(1/m\) preserves uniqueness. \(\square\)

## Verification
The standalone standard-library program `verify_ritz_reuse.py` checks the exact rational lower and upper radical enclosures, exact integer inequality, and strict rational logarithm-series bound. It also independently samples the quoted characteristic roots and rates for finite reuse counts and memory values as a numerical cross-check; the infinite tail is certified by the analytic derivative, **not** by those samples. Run `python verify_ritz_reuse.py`.

## Relationship to prior work
Gu [1, Lemma 4, Theorem 5] supplies the algorithm definition, the exact delayed weight recurrence, the complete-update convergence limit, and the piecewise formula for \(\sigma_\ell\). Those are not claimed as new. This result resolves the **separate integer design problem of choosing \(\ell\) to maximize the proven per-update asymptotic slope** and makes the same-initialization generic quantifier simultaneous for all reuse counts. Gu [2] treats cyclic steepest descent, whose current-gradient line-search step is distinct from delayed historical Ritz recycling. Zhou, Gu and Yuan [3] treat rebound-aware step selection and global linear convergence under safeguards, not an exact RCR repetition optimum. See also the original cyclic BB paper [4].

## Limitations
The maximum is only for constant integer reuse counts in the exact \(q=m+1\) RCR regime of [1]; it is not a finite-tolerance complexity, operation-weighted runtime, or practical benchmark for dense/high-dimensional arbitrary-spectrum problems. It says nothing about SCR, memory tuning, adaptive varying reuse, safeguards, or finite-precision behavior. The scientific novelty is the global integer scheduling classification, not the original spectral recurrence or rate formula. Earlier equivalent analyses of this particular cost-normalized expression cannot be categorically excluded.

## References
[1] Ran Gu, *Superlinear Convergence of Cyclic Gradient Methods with Historical Ritz Step Sizes*, arXiv:2610.32705v1 (first public October 23, 2026), https://arxiv.org/html/2610.32705v1 . Relevant material: Sections 2–3, Lemma 4, Theorem 5 and equation (23).

[2] Ran Gu, *Doubly exponential convergence of the cyclic steepest descent method for strictly convex quadratics in arbitrary dimensions*, arXiv:2609.25800v1 (September 22, 2026), https://arxiv.org/html/2609.25800v1 .

[3] Yijia Zhou, Ran Gu and Ya-xiang Yuan, *Structured Spectral Step-Sizes and Rebound-Aware Ordering for Gradient Methods*, arXiv:2606.25311v3 (first public June 24, 2026), https://arxiv.org/html/2606.25311v3 .

[4] Dai, Hager, Schittkowski and Zhang, *The cyclic Barzilai–Borwein method for unconstrained optimization*, IMA Journal of Numerical Analysis 26 (2006), 604–627; cited in [1].
