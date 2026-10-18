# A log-periodic Gaussian cutoff profile for the delayed-register Markov chain

## Finding

Fix a noise parameter \(0<a<1\), let \(b=-\log a\), and for every integer \(k\ge1\) consider the delayed-register Markov chain on \(\{-1,+1\}^{k}\) with transition
\[
 (x_1,\ldots,x_k)\longmapsto (x_2,\ldots,x_k,x_1E),
 \qquad \Pr(E=\pm1)=\frac{1\pm a}{2},
\]
where successive multipliers are independent. Let \(U_k\) be the uniform stationary measure, \(\beta_k(t)\) the stationary-averaged total-variation distance at time \(t\), and \(d_k(t)\) the maximum over starting states. Write \(t=mk+r\) uniquely with integers \(m\ge0\), \(0\le r<k\), and set \(u=a^m\), \(v=a^{m+1}\). Then at **every** nonnegative integer time,
\[
\boxed{\displaystyle
 \beta_k(t)=d_k(t)=\frac{1}{2^{k+1}}
 \sum_{i=0}^{k-r}\sum_{j=0}^{r}
 {k-r\choose i}{r\choose j}
 \left|(1+u)^i(1-u)^{k-r-i}(1+v)^j(1-v)^{r-j}-1\right|.}
\]
Equality of averaged and worst-case distance is an established feature of this chain [1, Lemma 5.4], not a separate novelty claim. The two-block evaluation above is included to specify the exact law underlying the asymptotic finding.

Define \(c_k=(\log k)/(2b)\) and \(t_k(s)=\lfloor k(c_k+s)\rfloor\) for fixed \(s\in\mathbb R\), with \(k\) sufficiently large to make \(t_k(s)\ge0\). Along any sequence of dimensions for which the fractional parts satisfy
\[
 \theta_k=\{c_k+s\}\longrightarrow\theta\in[0,1],
\]
where the endpoint \(\theta=1\) means approach from below, the following limit holds:
\[
 \boxed{\displaystyle
 \beta_k(t_k(s))\longrightarrow
 2\Phi\!\left(\frac{e^{-bs}H_b(\theta)}{2}\right)-1,
 \qquad H_b(\theta)=e^{b\theta}\sqrt{1-\theta+\theta e^{-2b}}.}
\]
Here \(\Phi\) is the standard normal distribution function. The endpoint values are \(H_b(0)=H_b(1)=1\), while \(H_b(\theta)>1\) for \(0<\theta<1\), and in particular \(H_b(1/2)=\sqrt{\cosh b}>1\). Every interior phase is realized by an integer-dimension subsequence; phase zero is also attainable. Therefore there is **no single pointwise limit** for the real-centered mixing curve \(\beta_k(\lfloor k(c_k+s)\rfloor)\) as \(k\to\infty\) at any fixed real \(s\). Instead there is a nonconstant phase-dependent family of Gaussian cutoff profiles. The cutoff occurs at \(k\log k/(2b)\) with an order-\(k\) transition window.

## Assumptions and scope

The parameter \(a\) is a fixed number strictly between zero and one as the register length \(k\) tends to infinity. Noise multipliers are independent across steps and of the starting state. The finite-time identity also extends to \(a=0\) with the convention \(0^0=1\), but the logarithmic centering concerns only \(0<a<1\). There is no claim about jointly varying \(a\), other register update rules, or uniformity in the centering offset \(s\).

## Proof

**Step 1: exact partial-block law.** After \(mk+r\) steps, each original coordinate has passed the end of the register \(m\) or \(m+1\) times. Exactly \(k-r\) coordinates have received \(m\) independent multiplier factors, and exactly \(r\) have received \(m+1\) factors. The collections of multipliers for distinct coordinates are disjoint, hence all current signs are independent conditional on the initial word. Their means equal the appropriate initial signs multiplied by \(u=a^m\) or \(v=a^{m+1}\). A deterministic permutation and coordinatewise sign change carries this law into the product of \(k-r\) independent signs of mean \(u\) and \(r\) independent signs of mean \(v\). Those transformations preserve \(U_k\); consequently total-variation distance does not depend on the starting word, proving the equality of averaged and worst-case distances (already noted in [1]). Relative to uniform measure, a configuration with \(i\) positive signs in the first block and \(j\) in the second has likelihood ratio
\[
 \mathcal L_{i,j}=(1+u)^i(1-u)^{k-r-i}(1+v)^j(1-v)^{r-j}.
\]
Summing \(|\mathcal L_{i,j}-1|\) over the two binomial multiplicities with the factor \(2^{-k-1}\) proves the displayed finite-time formula; the cases \(m=0\) and \(r=0\) follow with the same interpretation.

**Step 2: Gaussian total-variation limit.** At \(t_k(s)\), write \(m_k=\lfloor c_k+s\rfloor\) and \(r_k=\lfloor k\theta_k\rfloor\). Thus
\[
 \sqrt{k}\,a^{m_k}=e^{-bs+b\theta_k},\quad
 k a^{2m_k}\to e^{-2bs+2b\theta},\quad r_k/k\to\theta.
\]
Under the uniform product measure, introduce independent unbiased signs \(\sigma_i\) and the likelihood ratio
\[
 \mathcal L_k=\prod_{i=1}^{k-r_k}(1+a^{m_k}\sigma_i)
 \prod_{i=k-r_k+1}^{k}(1+a^{m_k+1}\sigma_i).
\]
If \(\mu_{k,i}\) denotes the respective coordinate bias, then
\[
 \max_i|\mu_{k,i}|=O(k^{-1/2}),\qquad
 \sum_i\mu_{k,i}^2\to z^2
 =e^{-2bs+2b\theta}(1-\theta+\theta e^{-2b}),\qquad
 \sum_i\mu_{k,i}^4=O(k^{-1}).
\]
Uniform Taylor expansion of \(\log(1+\mu_{k,i}\sigma_i)\), followed by the Lindeberg central limit theorem for the bounded independent triangular array, gives
\[
 \log\mathcal L_k\Rightarrow N(-z^2/2,z^2)
 \quad\text{under }U_k.
\]
The total-variation distance is \(\mathbb E_{U_k}[(1-\mathcal L_k)_+]\). Since \(y\mapsto(1-e^y)_+\) is continuous and bounded by one, convergence in distribution implies convergence of expectations without any uniform-integrability assumption. Direct Gaussian integration yields
\[
 \mathbb E[(1-e^Y)_+]=2\Phi(z/2)-1,
 \qquad Y\sim N(-z^2/2,z^2),
\]
which proves the claimed phase-dependent limit.

**Step 3: all phases and nonconvergence.** For any fixed \(\theta\in(0,1)\), choose positive integers \(k_j\) nearest to \(\exp(2b(j+\theta-s))\); rounding has vanishing effect on \(\{c_{k_j}+s\}\), so its limit is \(\theta\). To realize phase zero, take \(k_j\) nearest \(\exp(2b(j-s+j^{-1/2}))\), giving fractional part tending to zero from above. Strict weighted arithmetic-geometric mean gives
\[
 1-\theta+\theta e^{-2b}>e^{-2b\theta}
 \quad(0<\theta<1),
\]
so \(H_b(\theta)>1\) in the interior, whereas \(H_b(0)=1\). As \(2\Phi(z/2)-1\) is strictly increasing for positive \(z\), the phase-zero and phase-one-half subsequences have different limits at every fixed \(s\). This proves nonconvergence for the specified centering.

**Step 4: cutoff scale.** For times with \(t/k-c_k\to+\infty\), the squared coordinate biases sum to at most \(k a^{2\lfloor t/k\rfloor}\to0\). The exact identity \(\chi^2=\prod_i(1+\mu_i^2)-1\), together with \(\|P-U_k\|_{\mathrm{TV}}\le\tfrac12\sqrt{\chi^2}\), gives convergence to zero. For times with \(t/k-c_k\to-\infty\), the squared biases sum to at least \(k a^{2(\lfloor t/k\rfloor+1)}\to\infty\). The product Hellinger affinity between the chain law and \(U_k\) is at most \(\exp(-\tfrac18\sum_i\mu_i^2)\), using concavity of square root (or a one-coordinate Taylor/elementary bound). Since total variation is at least one minus affinity, it converges to one. The two sides establish cutoff at the stated center with an order-\(k\) window. In the lower bound, this applies only to nonnegative times; for any fixed negative offset the time is eventually positive because the center diverges.

## Verification

The standalone file `verify.py` reproduces the all-time formula by independently evolving the finite-state transition kernel over exact rational numbers. It checks three initial states, four noise parameters and register lengths up to six, verifies monotonicity and complete-block reduction, and checks analytic phase-factor constraints. Execute `python3 verify.py` using the standard library. The recorded verification run returned `PASS: 1366 finite exact-rational or deterministic assertions`. Finite checks do not establish the normal limit, the infinite cutoff, or originality; those follow from the proof and documented source comparisons.

## Relationship to prior work

Judd and Esposito [1, Section 4.1 and Lemmas 5.2, 5.4, including their proofs] introduce precisely this delayed-register kernel, establish its uniform stationarity and state-independent total-variation distance, prove a support-based bound before the first complete block, and determine the distance at integer multiples of \(k\) as a one-parameter binomial product functional. Those prior conclusions are not claimed as new. Their results do not state the two-block finite-time formula, the subsequential Gaussian profile, or the phase-dependent failure of a single centered limiting profile. The present asymptotic conclusion uses classical local-asymptotic-normality reasoning for weak product biases, not an independently novel normal approximation principle. Levin and Tankala [2] study a different, XOR-based randomized shift-register chain, so their cutoff does not imply this chain's phase-sensitive profile. Other published work on weak-signal Bernoulli-product total variation can supply the normal approximation step, but does not by itself identify the time-dependent two-block bias allocation of this chain.

## Limitations

This is a self-review, not an independent proof or priority audit. The phase limit is subsequential, not uniform jointly over a varying noise parameter; no assertion is made about cutoff universality for other cyclic-register chains. The absence of a previously located explicit profile does not establish historical uniqueness. An earlier unpublished or unlocated application of classical product-measure cutoff methods to this exact chain could overlap with the result. The equality of averaged and worst-case distances and the complete-block formula are prior findings, not new contributions.

## References

[1] N. A. Judd and A. R. Esposito, *On the Impossibility of Estimating the Average Mixing Time*, arXiv:2610.10860v1, first public 2026-10-07; Section 4.1, Lemmas 5.1–5.4, Appendix A. https://arxiv.org/html/2610.10860v1

[2] D. A. Levin and C. Tankala, *Fast mixing of a randomized shift-register Markov chain*, Journal of Applied Probability 60 (2023), 253–266; preprint arXiv:2109.05387. https://arxiv.org/abs/2109.05387

[3] D. A. Levin and Y. Peres, *Markov Chains and Mixing Times*, second edition, American Mathematical Society (2017), standard total-variation and cutoff background.
