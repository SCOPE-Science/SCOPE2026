# Sharp void exponent for asymmetric Weibull-tail perturbed lattices

## Finding

Let an independently perturbed one-dimensional integer lattice have opposite displacement-tail logarithmic rates \(c_-\) and \(c_+\), with a common stretched-exponential exponent \(\alpha>0\). The probability that its stationary version has no point in an interval of length \(L\) has the exact rate
\[
\lim_{L\to\infty}\frac{-\log\Pr\{\Xi([0,L])=0\}}{L^{\alpha+1}}
=\frac{c_-c_+}{(\alpha+1)(c_-^{1/\alpha}+c_+^{1/\alpha})^{\alpha}}.
\]
The same limit holds with the stationarizing shift fixed at any \(u\in[0,1)\), uniformly in \(u\). This determines both the large-void exponent and its coefficient from only the two one-sided displacement tails. The dimensionless crossover point between escaping left and escaping right is
\[
\vartheta=\frac{c_+^{1/\alpha}}{c_-^{1/\alpha}+c_+^{1/\alpha}}.
\]
In particular, for centered Gaussian displacements with variance \(\sigma^2>0\),
\[
\lim_{L\to\infty}\frac{-\log\Pr\{\Xi([0,L])=0\}}{L^3}=\frac1{24\sigma^2}.
\]

## Assumptions and scope

Let \((Y_j)_{j\in\mathbb Z}\) be iid real-valued, atomless random variables, each having positive probability of either sign. Assume there exist common \(\alpha>0\) and constants \(c_-,c_+\in(0,\infty)\) such that
\[
\lim_{t\to\infty}\frac{-\log\Pr(Y_0<-t)}{t^\alpha}=c_-\qquad\text{and}\qquad
\lim_{t\to\infty}\frac{-\log\Pr(Y_0>t)}{t^\alpha}=c_+.
\]
Let \(U\) be independent and uniform on \([0,1)\), and put
\(\Xi=\sum_{j\in\mathbb Z}\delta_{j+U+Y_j}\). Here \(\Xi([0,L])\) counts points with multiplicity; endpoints have probability zero by atomlessness. All limits are over real \(L\to\infty\). There is no moment assumption on \(Y_0\) beyond the displayed tail conditions, and no assumption of symmetry.

## Proof

**Step 1: Exact independent product.** Fix a shift \(u\in[0,1)\), write \(a_j=j+u\), and define
\[
 p_j=\Pr(a_j+Y_j\notin[0,L])=\Pr(Y_0<-a_j)+\Pr(Y_0>L-a_j).
\]
The two events on the right are disjoint. Conditional independence gives
\[
 H_L(u):=\Pr(\Xi([0,L])=0\mid U=u)=\prod_{j\in\mathbb Z}p_j.
\]
This infinite product is positive. To see this and control its logarithm, split lattice sites into those inside and outside the interval; the interior set is finite and every \(p_j>0\), by the two positive tails.

**Step 2: Outside sites cost at most linearly.** For \(a_j\notin[0,L]\) let \(q_j=1-p_j\), the probability that site \(j\) enters the interval. Since the distribution is atomless, with
\[
 \eta=\max\{\Pr(Y_0>0),\Pr(Y_0<0)\}<1,
\]
we have \(0\le q_j\le\eta\) for every outside site. The elementary inequality \(-\log(1-q)\le q/(1-\eta)\) for \(0\le q\le\eta\) therefore yields
\[
 0\le\sum_{a_j\notin[0,L]}-\log p_j
 \le\frac1{1-\eta}\sum_{j\in\mathbb Z}q_j.
\]
If \(Y\) is a single random variable distributed as \(Y_0\), Tonelli's theorem gives
\[
 \sum_{j\in\mathbb Z}q_j
 =\mathbb E\bigl[\#\{j\in\mathbb Z:j+u+Y\in[0,L]\}\bigr]\le L+1.
\]
The last inequality holds because an interval of length \(L\) contains at most \(L+1\) integer lattice sites (counting inclusively). Thus the outside contribution is \(O(L+1)\), uniformly in \(u\), and is negligible on the scale \(L^{\alpha+1}\). This also justifies convergence of the outside logarithmic product.

**Step 3: Interior large-deviation cost.** For \(a_j\in[0,L]\), let
\[
 B_-(a_j)=-\log\Pr(Y_0<-a_j),\qquad
 B_+(L-a_j)=-\log\Pr(Y_0>L-a_j).
\]
The log-sum identity gives the deterministic bounds
\[
 \min(B_-(a_j),B_+(L-a_j))-\log2
 \le -\log p_j\le
 \min(B_-(a_j),B_+(L-a_j)).
\]
Fix \(\varepsilon>0\). By the tail hypotheses choose \(M<\infty\) so that for every \(t\ge M\), the respective tail costs differ from \(c_-t^\alpha\) and \(c_+t^\alpha\) by at most \(\varepsilon t^\alpha\). At interior sites with both \(a_j\) and \(L-a_j\) at least \(M\), the difference between \(-\log p_j\) and
\[
 f_L(a_j)=\min\{c_-a_j^\alpha,c_+(L-a_j)^\alpha\}
\]
is bounded by \(\varepsilon L^\alpha+\log2\). The number of such sites is at most \(L+1\). Within distance \(M\) of an endpoint there are at most \(2(M+2)\) sites: \(-\log p_j\) is bounded independently of \(L\) by the positive relevant one-sided tail at \(M\), and \(f_L(a_j)\) is likewise bounded by \(\max(c_-,c_+)M^\alpha\). Their contribution is \(O_M(1)\). Thus, uniformly in \(u\),
\[
 \lim_{L\to\infty}\frac1{L^{\alpha+1}}
 \left[\sum_{a_j\in[0,L]}-\log p_j-\sum_{a_j\in[0,L]}f_L(a_j)\right]=0,
\]
by first taking \(L\to\infty\) and then \(\varepsilon\downarrow0\).

**Step 4: Riemann limit and explicit coefficient.** The continuous function \(g(x)=\min(c_-x^\alpha,c_+(1-x)^\alpha)\) on \([0,1]\) satisfies the shifted-grid Riemann-sum limit, uniformly in \(u\in[0,1)\),
\[
 \lim_{L\to\infty}L^{-\alpha-1}\sum_{a_j\in[0,L]}f_L(a_j)
 =\int_0^1g(x)\,dx.
\]
Its two branches agree only at \(\vartheta=c_+^{1/\alpha}/(c_-^{1/\alpha}+c_+^{1/\alpha})\). Integrating on the two sides gives
\[
 \int_0^1g(x)\,dx
 =\frac{c_-\vartheta^{\alpha+1}+c_+(1-\vartheta)^{\alpha+1}}{\alpha+1}
 =\frac{c_-c_+}{(\alpha+1)(c_-^{1/\alpha}+c_+^{1/\alpha})^\alpha}.
\]
Steps 2–4 yield \(-\log H_L(u)/L^{\alpha+1}\to I\) uniformly in \(u\). Hence for every \(\varepsilon>0\) and all large \(L\),
\[
 e^{-(I+\varepsilon)L^{\alpha+1}}\le H_L(u)
 \le e^{-(I-\varepsilon)L^{\alpha+1}}
\]
for all \(u\). Integration over \(u\) proves the stationary void limit.

**Step 5: Gaussian specialization.** For \(Y_0\sim N(0,\sigma^2)\), the Gaussian Mills asymptotic gives \(\alpha=2\), \(c_-=c_+=1/(2\sigma^2)\). Substitution into the exact rate yields \(I=(1/(2\sigma^2))/(2^2\cdot3)=1/(24\sigma^2)\). This completes the proof.

## Verification

The standalone `verify.py` computes the conditional infinite-product logarithm by truncation, with logarithmically stable tail functions, for symmetric and asymmetric two-sided stretched-exponential laws and for Gaussian displacements. It compares the finite ratios with the proved constants and checks the elementary crossover integral numerically. Its actual output is in `verify_output.txt`; 107 finite assertions passed. These tests do not prove the infinite-length statement and do not replace Steps 1–5. To reproduce, run `python3 verify.py` with NumPy and SciPy available. All necessary analytical arguments are contained above.

## Relationship to prior work

Flimmel (2026), Section 3.1 and Proposition 2, gives the conditional independent-product identity for perturbed-lattice void probabilities, while focusing principally on bounds valid under dependence. It does not state an exact one-dimensional tail-dependent leading constant. Elboim, Spinka, and Yakir (2025), Lemma 2.5, bound the corresponding hole probability between powers of the perturbation tail, implying the correct stretched-exponential *order* but not its coefficient or the two-sided asymmetric formula. The present result sharpens that order for the stated one-dimensional independent tail class; it does not improve their matching construction or extend Flimmel's dependent-field theorem.

## Limitations

The result assumes iid displacement variables, a one-dimensional unit-spacing lattice, atomless law, strictly positive probabilities of both signs, a common exponent \(\alpha\) for both logarithmic one-sided tails, and a fixed nonrandom displacement distribution. It does not cover dependent perturbations, distinct left/right exponents, or higher-dimensional observation shapes. The exact finite-length void probability is not claimed to equal its leading exponential approximation. The result has only self-review; independent validation and historical-priority assessment have not been performed. Literature coverage is not exhaustive, so a broader existing large-deviation theorem might imply this formula.

## References

1. Daniela Flimmel, *Void probabilities for perturbed lattices under mixing*, arXiv:2610.24650v1, first posted 17 October 2026. https://arxiv.org/html/2610.24650v1 (Section 3.1, Proposition 2).
2. Dor Elboim, Yinon Spinka, and Oren Yakir, *Optimal matchings of randomly perturbed lattices*, arXiv:2506.16873v1, first posted 20 June 2025. https://arxiv.org/html/2506.16873v1 (Section 2.3, Lemma 2.5).
