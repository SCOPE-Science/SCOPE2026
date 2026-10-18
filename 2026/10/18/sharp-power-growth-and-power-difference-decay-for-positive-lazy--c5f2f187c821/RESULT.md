# Sharp power growth and power-difference decay for positive lazy backward shifts on reflexive sequence spaces

## Finding

Fix real parameters \(1<p<\infty\), \(0<\alpha<1/p\), and \(0<\delta<1\). On complex \(\ell^p(\mathbb N)\), let \(W_\alpha e_1=0\) and
\[
W_\alpha e_j=\left(\frac{j}{j-1}\right)^\alpha e_{j-1}\quad(j\ge2),\qquad T=(1-\delta)I+\delta W_\alpha.
\]
There are constants \(c,C>0\) and an integer \(n_0\), depending only on these fixed parameters, such that for every integer \(n\ge n_0\),
\[
c\,n^{\alpha/2}\le \|T^n\|\le C\,n^{\alpha/2},
\qquad
c\,n^{(\alpha-1)/2}\le \|T^{n+1}-T^n\|\le C\,n^{(\alpha-1)/2}.
\]
In particular, \(T\) is positive, is \(p\)-absolutely Cesàro bounded, is not power bounded, and satisfies
\[
\sigma(T)=(1-\delta)+\delta\overline{\mathbb D},\qquad
\sigma(T)\cap\mathbb T=\{1\},\qquad
\|T^{n+1}-T^n\|\longrightarrow0.
\]
The displayed polynomial exponents are exact: neither can be replaced by a strictly smaller power in its two-sided estimate. The theorem is a quantitative positive example within the scope of the Katznelson–Tzafriri question, not a resolution of that question for arbitrary positive operators.

## Assumptions and scope

The underlying norm exponent and Cesàro exponent coincide and satisfy \(1<p<\infty\). The weight exponent obeys \(\alpha p<1\) strictly; no uniform constants as the parameters approach their endpoints are claimed. The operator is the specified noninvertible backward shift followed by a fixed lazy convex average. The asserted norm inequalities are for the infinite-dimensional \(\ell^p\) operator norms, not for finite truncations.

An operator \(S\) is \(p\)-absolutely Cesàro bounded if a constant \(K<\infty\) satisfies
\[
\frac1N\sum_{k=0}^{N-1}\|S^k x\|^p\le K\|x\|^p
\quad(x\in\ell^p,\;N\ge1).
\]

## Proof

**Step 1 (boundedness, Cesàro estimates, and spectrum).** Telescoping gives
\[
W_\alpha^k e_j=
\begin{cases}(j/(j-k))^\alpha e_{j-k},&0\le k<j,\\0,&k\ge j.\end{cases}
\]
Consequently \(\|W_\alpha^k\|=(k+1)^\alpha\) for \(k\ge0\). For any \(x\in\ell^p\), Tonelli's theorem applied to the nonnegative coordinates and the elementary power-sum comparison show
\[
\frac1N\sum_{k=0}^{N-1}\|W_\alpha^k x\|_p^p
\le \frac1{1-\alpha p}\|x\|_p^p.
\]
The constant is exact for \(W_\alpha\), by applying the inequality to \(e_j\), taking \(N=j\), and letting \(j\to\infty\). By the binomial/Jensen/Abel lemma (Arnold, Lemma 7.3 in arXiv:2610.00271v1), the convex combination \(T=(1-\delta)I+\delta W_\alpha\) is likewise \(p\)-absolutely Cesàro bounded with constant at most \((1-\alpha p)^{-1}\). The weights are nonnegative, so \(T\) is positive.

The spectral radius of \(W_\alpha\) equals one because \(\|(W_\alpha)^k\|^{1/k}\to1\). For every \(|\lambda|<1\), the nonzero sequence \((\lambda^{j-1}j^{-\alpha})_{j\ge1}\in\ell^p\) is an eigenvector for \(W_\alpha\) with eigenvalue \(\lambda\). Hence \(\sigma(W_\alpha)=\overline{\mathbb D}\), and polynomial spectral mapping gives the stated disk for \(T\), touching the unit circle only at \(1\).

**Step 2 (binomial kernel estimates).** Set
\[
b_n(k)=\binom nk\delta^k(1-\delta)^{n-k}\quad(0\le k\le n),
\qquad h_n(k)=b_n(k)-b_n(k-1),
\]
with \(b_n(k)=0\) outside \([0,n]\). Elementary binomial unimodality, Stirling's bounds and the adjacent-mass ratio yield, for each fixed \(\delta\in(0,1)\), constants depending only on \(\delta\) such that
\[
\|b_n\|_{\ell^1}=1,\quad
\|b_n\|_{\ell^\infty}\le Cn^{-1/2},\quad
\|h_n\|_{\ell^1}=2\max_k b_n(k)\le Cn^{-1/2},\quad
\|h_n\|_{\ell^\infty}\le Cn^{-1}.
\]
For the last estimate, on the central strip \(|k-n\delta|\le \eta n\), use
\[
h_n(k)=b_n(k-1)\frac{\delta(n+1)-k}{k(1-\delta)}.
\]
The central Gaussian point bound \(b_n(k)\le Cn^{-1/2}\exp[-c(k-n\delta)^2/n]\) and the displayed ratio imply \(|h_n(k)|\le Cn^{-1}\) (the Gaussian absorbs \(|k-n\delta|/\sqrt n\)). Outside the strip, standard fixed-parameter binomial exponential tails give the same bound after enlarging \(C\). Interpolation between \(\ell^1\) and \(\ell^\infty\) now gives, for \(p'=p/(p-1)\),
\[
\|b_n\|_{\ell^{p'}}\le Cn^{-1/(2p)},\qquad
\|h_n\|_{\ell^{p'}}\le Cn^{-1+1/(2p')}.
\]

**Step 3 (upper bounds).** In the canonical basis, binomial expansion and telescoping give the exact matrices, for \(j\ge i\ge1\),
\[
(T^n)_{ij}=\left(\frac ji\right)^\alpha b_n(j-i),\qquad
(T^{n+1}-T^n)_{ij}=-\delta\left(\frac ji\right)^\alpha h_n(j-i),
\]
with all other entries zero. More generally, let \(K_n\) denote either matrix with \(b_n\) or \(h_n\), temporarily omitting the fixed factor \(\delta\). Split its output into \(i\ge\sqrt n\) and \(1\le i<\sqrt n\).

When \(i\ge\sqrt n\), nonzero kernel terms satisfy \(0\le j-i\le n+1\), hence \((j/i)^\alpha\le Cn^{\alpha/2}\). Young's convolution inequality yields
\[
\|1_{\{i\ge\sqrt n\}}K_n x\|_p\le Cn^{\alpha/2}\|k_n\|_{\ell^1}\|x\|_p,
\]
where \(k_n=b_n\) or \(h_n\). On \(i<\sqrt n\), \((j/i)^\alpha\le Cn^\alpha i^{-\alpha}\), and Hölder gives
\[
|(K_nx)_i|\le Cn^\alpha i^{-\alpha}\|k_n\|_{\ell^{p'}}\|x\|_p.
\]
Because \(\alpha p<1\),
\[
\left(\sum_{1\le i<\sqrt n}i^{-\alpha p}\right)^{1/p}
\le Cn^{(1-\alpha p)/(2p)}.
\]
Combining these estimates with Step 2 gives the upper power bound \(Cn^{\alpha/2}\), and the upper consecutive-power-difference bound \(Cn^{(\alpha-1)/2}\). The constants absorb the fixed factor \(\delta\).

**Step 4 (matching lower bounds).** Put \(\mu=n\delta\). For sufficiently large \(n\), consider the two windows of integer indices
\[
I_n=\{i:\sqrt n\le i\le(3/2)\sqrt n\},\qquad
J_n=\{j:\mu+2\sqrt n\le j\le\mu+3\sqrt n\}.
\]
They both contain \(\asymp\sqrt n\) integers. Every \(i\in I_n\), \(j\in J_n\) satisfies \(j-i=\mu+u\sqrt n\) with \(1/2\le u\le2\), up to endpoint-rounding errors. The fixed-parameter binomial local central limit theorem, uniformly on this closed window, implies
\[
b_n(j-i)\ge c n^{-1/2},\qquad
h_n(j-i)\le -c n^{-1}.
\]
For the second bound, substitute the local limit into the exact adjacent-mass ratio in Step 2: its numerator is a negative multiple of \(\sqrt n\) and its denominator is a positive multiple of \(n\). Also \((j/i)^\alpha\ge c n^{\alpha/2}\). Choose the unit vector \(x_j=|J_n|^{-1/p}\) on \(J_n\), and zero elsewhere. For every \(i\in I_n\), positivity of all the \(b_n\) terms and common negativity of all the \(h_n\) terms give
\[
|(T^nx)_i|\ge c n^{\alpha/2-1/(2p)},\qquad
|((T^{n+1}-T^n)x)_i|\ge c n^{(\alpha-1)/2-1/(2p)}.
\]
The \(\ell^p\) norm over \(|I_n|\asymp\sqrt n\) outputs adds the factor \(n^{1/(2p)}\), yielding the two required lower operator-norm inequalities. Both constants are strictly positive. Since \(\alpha>0\), the power norms diverge, whereas \(\alpha<1/p<1\) makes the difference norms converge to zero. This concludes the proof.

## Verification

The analytic proof uses the exact matrix identities, binomial mass and first-difference estimates, and a uniform local central limit bound, not finite computation. Reproduce finite binomial mass, total-variation, sign, and matching boundary-window scaling diagnostics by running `python checks/finite_diagnostics.py` in an ordinary Python 3 interpreter. Its three reflexive parameter triples and three sample sizes each test nonzero normalized lower witnesses; these finite checks are supplementary and do not certify the infinite-dimensional limits.

## Relationship to prior work

Arnold, *Self-improvement for absolutely Cesàro bounded operators* (arXiv:2610.00271v1; first submitted 2026-09-24), gives the positive weighted backward-shift model (Example 3.2), preservation of \(p\)-absolute Cesàro boundedness under convex averaging (Lemma 7.3), non-power-bounded lower examples, and Question 8.2 about the positive Katznelson–Tzafriri conclusion. The present contribution concerns the **sharp two-sided operator-norm exponents for every fixed reflexive \(\ell^p\) exponent \(p>1\)** of these positive lazy shifts, not their already established Cesàro boundedness, nor any universal affirmative answer to Question 8.2. Abbar–Arnold–Coine (arXiv:2609.24601v1) develop broader Cesàro bounds and weighted-shift growth criteria; Cohen–Cuny–Eisner–Lin (2020) establish general growth and resolvent bounds, but no matching two-sided lazy-shift consecutive-power exponent was identified in the accessible material. The corresponding \(\ell^1\) model admits sharper asymptotic constants and is deliberately excluded from the new domain. Broader weighted Hardy-operator and discrete analytic-semigroup estimates should be independently checked for alternate derivations.

## Limitations

The constants in the two-sided inequalities are not evaluated exactly, and no parameter-uniform bounds are claimed. The exponent \(p=1\), the endpoint \(\alpha p=1\), and general positive operators beyond this particular weighted-shift family are excluded. No claim is made about an optimal rate over all positive absolutely Cesàro bounded operators. General priority remains subject to independent comparison with broader binomial-kernel and weighted-shift literature. No independent mathematical audit has been performed.

## References

1. L. Arnold, *Self-improvement for absolutely Cesàro bounded operators*, arXiv:2610.00271v1 (2026), especially Example 3.2, Lemma 7.3, Question 8.2. https://arxiv.org/abs/2610.00271
2. A. Abbar, L. Arnold and C. Coine, *On absolutely Cesàro bounded operators*, arXiv:2609.24601v1 (2026). https://arxiv.org/abs/2609.24601
3. G. Cohen, C. Cuny, T. Eisner and M. Lin, *Resolvent conditions and growth of powers of operators*, Journal of Mathematical Analysis and Applications 487 (2020), article 124035. doi:10.1016/j.jmaa.2020.124035.
4. Y. Katznelson and L. Tzafriri, *On power bounded operators*, Journal of Functional Analysis 68 (1986), 313–328.
