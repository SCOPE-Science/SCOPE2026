# Universal rare-completion law for polynomially diffuse clumsy coupon frequencies

## Finding
Fix a loss probability \(p\in(0,1)\) and write \(q=1-p\). For each \(n\ge2\), let \(w_{n,1},\ldots,w_{n,n}>0\) sum to one. Suppose there are fixed constants \(B\ge1\), \(0<\gamma\le1\), and \(c,C>0\) such that, for all sufficiently large \(n\),
\[
 c n^{-B}\le \min_{1\le i\le n}w_{n,i}\le \max_{1\le i\le n}w_{n,i}\le C n^{-\gamma}.
\]
Starting with all \(n\) coupon types absent, repeatedly choose type \(i\) with probability \(w_{n,i}\), and independently overwrite its presence indicator with \(1\) with probability \(q\) and \(0\) with probability \(p\). Write \(T_n\) for the first positive time when every type is present.

The exact stationary rate of **new entrances** into the all-present state is \(\mu_n=pq^n\), independently of the frequency vector. Moreover,
\[
 \mu_nT_n\ \Longrightarrow\ \operatorname{Exp}(1),
 \qquad \lim_{n\to\infty}\mathbb E[(\mu_nT_n)^r]=r!
 \quad\text{for every fixed integer }r\ge1.
\]
The convergence and moment assertions hold uniformly over the above frequency class for fixed admissible constants. In particular, \(\mathbb ET_n\sim (pq^n)^{-1}\) and \(\operatorname{Var}(T_n)\sim(pq^n)^{-2}\). Every fixed Zipf frequency profile \(w_{n,i}\propto i^{-s}\), \(0\le s<1\), belongs to such a class.

The lower-frequency condition cannot be omitted without replacement: if \(w_{n,1}=e^{-\theta n}\) for fixed \(\theta> -\log q\), and the remaining probability is divided equally among the other types, then \(\mu_n T_n\to+\infty\) in probability.

## Assumptions and scope
The probability \(p\), exponent bounds \(B,\gamma\), and constants \(c,C\) do not depend on \(n\). The coupon weights may otherwise depend on \(n\) arbitrarily, and need not be equal, monotone, or regularly varying. The model refreshes **only the selected coordinate** at each discrete step; it does not globally erase coupons. The initial state is the empty collection. The fixed-moment assertion concerns every fixed positive integer exponent and does not claim convergence uniformly in that exponent.

Set \(A_n=\{(1,\ldots,1)\}\) and \(X(t)\in\{0,1\}^n\). A *new entrance* at step \(t\) is the event \(E_t=\{X(t-1)\notin A_n,\ X(t)\in A_n\}\). We abbreviate \(w_- =\min_iw_{n,i}\) and \(w_+=\max_iw_{n,i}\) while keeping the dependence on \(n\) implicit.

## Proof
**1. Product stationary law and exact flux.** The transition consists of choosing one coordinate and resampling it from \(\operatorname{Bernoulli}(q)\); therefore the unique stationary distribution is \(\pi_n=\operatorname{Bernoulli}(q)^{\otimes n}\). In stationarity, a new entrance must choose an absent coordinate, refresh it to present, and find all remaining coordinates present. Summing over the chosen coordinate gives
\[
 \mathbb P_{\pi_n}(E_1)=\sum_{i=1}^n w_{n,i}\,p\,q^{n-1}\,q=pq^n=:\mu_n.
\]
Also \(\pi_n(A_n)=q^n\to0\).

**2. Exact entrance-return identity without a count-chain reduction.** Start instead from the all-present configuration \(\mathbf1\), and observe the selected coordinate indices during the first \(r\) updates. Let \(U_r\) be their set, \(K_r=|U_r|\), and \(W_r=\sum_{i\in U_r}w_{n,i}\). Given those indices, the latest refresh outcomes on the \(K_r\) touched coordinates are independent \(\operatorname{Bernoulli}(q)\), while the other coordinates remain present. A new entrance at time \(r+1\) requires choosing a touched coordinate currently absent, refreshing it to present, and having all other touched coordinates present. Consequently
\[
 a_{r+1}:=\mathbb P_{\mathbf1}(E_{r+1})
 =p\,\mathbb E\bigl[q^{K_r}W_r\bigr]
 \le p w_+\,\mathbb E[K_rq^{K_r}],\qquad r\ge0.
\]
In particular, \(a_1=0\). This identity uses the visited **set**, not just the number currently missing, which is generally not a Markov chain for unequal weights.

**3. Uniform sum bound for entrance returns.** Put \(d=\lfloor(64w_+)^{-1}\rfloor\), which tends to infinity at least as a positive multiple of \(n^\gamma\) and satisfies \(d\le n\) for large \(n\). For every \(1\le r\le d\), the conditional chance that the next selected index repeats an earlier index is at most \(r w_+\le1/64\). Counting possible collections of at least half the steps that repeat earlier indices gives
\[
 \mathbb P(K_r<r/2)
 \le 2^r(rw_+)^{r/2}\le4^{-r}.
\]
Indeed, for any fixed collection of \(k\) designated repeat steps, iterated conditioning bounds its probability by \((rw_+)^k\), and there are at most \(2^r\) possible collections. It follows that
\[
 \mathbb E[K_rq^{K_r}]\le r(q^{r/2}+4^{-r})\quad(1\le r\le d).
\]
For \(r>d\), monotonicity of the visited sets implies \(K_r\ge K_d\), so
\[
 \mathbb E[K_rq^{K_r}]\le n(q^{d/2}+4^{-d}).
\]
Choose a polynomial block length \(b_n=\lceil n^{B+4}\rceil\). The previous displays imply
\[
 \sum_{t=1}^{b_n}a_t\le
 p w_+\left[\sum_{r=1}^d r(q^{r/2}+4^{-r})
       +b_n n(q^{d/2}+4^{-d})\right]=o(1).
\]
Here the infinite series converges, \(w_+=O(n^{-\gamma})\), and the second term is a polynomial times \(\exp[-\Omega(n^\gamma)]\).

**4. Rare entrances in a stationary block.** Under stationarity define \(N_b=\sum_{t=1}^{b_n}\mathbf1_{E_t}\). The first moment is \(\mathbb E_{\pi_n}N_b=b_n\mu_n\). For \(1\le s<t\le b_n\), conditioning on \(E_s\) leaves the chain at \(\mathbf1\); the Markov property therefore gives \(\mathbb P_{\pi_n}(E_s\cap E_t)=\mu_n a_{t-s}\). Thus
\[
 \mathbb E_{\pi_n}[N_b(N_b-1)]
   =2\mu_n\sum_{j=1}^{b_n-1}(b_n-j)a_j
   \le 2b_n\mu_n\sum_{j=1}^{b_n}a_j=o(b_n\mu_n).
\]
Bonferroni and Markov's inequality now yield
\[
 \mathbb P_{\pi_n}(N_b\ge1)=b_n\mu_n(1+o(1)).
\]
As \(b_n\) is polynomial, \(b_n\mu_n\to0\).

**5. Mixing and initial burn-in.** Couple two copies by using the same coordinate indices and overwrite bits. They coincide after every coordinate has been selected at least once. Therefore the maximal total-variation distance to stationarity after \(h\) steps satisfies
\[
 \alpha_n(h)\le\sum_{i=1}^n(1-w_{n,i})^h\le n e^{-w_-h}.
\]
Let \(\lambda=-\log q\). Choose a constant \(H>(\lambda+2)/c\) and \(h_n=\lceil Hn^{B+1}\rceil\). Then \(h_n=o(b_n)\), \(h_n\mu_n\to0\), and \(\alpha_n(h_n)=o(b_n\mu_n)\). From the empty collection, conditional on any sequence of indices, either some coupon is untouched (completion impossible at that time) or all have been touched and their last refresh bits are independent with presence probability \(q\). Hence \(\mathbb P_{\mathbf0}(X(t)\in A_n)\le q^n\) for each \(t\), giving \(\mathbb P_{\mathbf0}(T_n\le h_n)\le h_nq^n=o(1)\).

**6. Exponential law and moments.** Divide a stationary trajectory into active blocks of length \(b_n\), separated by gaps of length \(h_n\). Each active block has a new entrance with probability \(b_n\mu_n(1+o(1))\). Mixing after a gap bounds the difference between this probability and the corresponding conditional probability given all preceding active blocks contained no entrance by \(\alpha_n(h_n)=o(b_n\mu_n)\). At a horizon \(t/\mu_n\), the number of active blocks is asymptotic to \(t/(b_n\mu_n)\); the probability of no entrance in those blocks therefore tends to \(e^{-t}\). The probability of any entrance in the intervening gaps is at most their stationary expected number, \(O(t h_n/b_n)=o(1)\). The chance of starting in \(A_n\) is \(q^n=o(1)\). This proves the stationary exponential law. By Step 5, the empty-start burn-in hits with probability \(o(1)\), mixes to stationarity, and is negligible in units of \(\mu_n^{-1}\), so the same law holds from \(\mathbf0\). This is also an application of the published stationary-entry block criterion [2, Theorem 2.3].

For each starting state \(x\), mixing during the first \(h_n\) steps makes the chance of a new entrance in the next \(b_n\) steps at least \(b_n\mu_n(1+o(1))-\alpha_n(h_n)\ge b_n\mu_n/2\). The Markov property at multiples of \(b_n+h_n\) therefore bounds the completion-time tail by a geometric tail whose decay rate, after multiplication by \(\mu_n\), is bounded away from zero independently of \(n\) and the allowed frequency vector. This yields a uniform exponential tail for \(\mu_n T_n\) (with fixed constants) and uniform integrability of every fixed power; hence its moments converge to the corresponding factorial moments. Taking the first and second moments gives the stated mean and variance.

**7. Exponentially rare coordinate obstruction.** Give type \(1\) weight \(e^{-\theta n}\) and distribute the remaining mass equally among the other types, with \(\theta>\lambda\). Since the initial state lacks type \(1\), collection cannot complete before this type is selected. For every \(t\ge0\),
\[
 \mathbb P(T_n\le t)\le t e^{-\theta n}.
\]
At \(t=\lfloor x/\mu_n\rfloor\), the right side is at most \((x/p)e^{-(\theta-\lambda)n}\to0\) for each fixed \(x>0\). Thus \(\mu_nT_n\to+\infty\) in probability. This does not characterize the full range of possible superpolynomial frequencies.

## Verification
The standalone Python 3 program `CHECKER.py` evaluates stationary entrance fluxes independently from the product law and computes future-entrance probabilities in two separate ways: direct exact-rational Markov propagation on presence states and exact-rational propagation on sets of previously selected coordinates. It passes 540 exact-rational assertions for unequal and uniform weights, six dimensions, three loss probabilities, and eight time horizons. These finite assertions verify identities used in the proof, not the infinite-\(n\) limit. Steps 3–6 establish the required asymptotic bounds analytically, uniformly over the declared class.

## Relationship to prior work
Attrill and Garoni [1] give the clumsy collector's uniform-frequency model and limit theorems. Long [2, Section 4] gives the fixed-loss uniform-frequency exponential law, its stationary entrance rate, and a proof relying on a birth–death chain for the number of absent types. Long [2, Theorem 2.3] also provides the general stationary-entry criterion used here. The new model-specific content is the visited-set identity and clump estimate for **unequal frequencies**, yielding the same exact exponential scale uniformly over an extensive class (including fixed Zipf profiles), plus the explicit exponentially rare-coordinate obstruction. The nonuniform reset-button process studied in [2, Section 3.6] erases the entire collection at reset and does not cover selected-coordinate clumsy refresh. The global post-draw thinning mechanism of Cruciani and Dudeja [3] is different again. No assertion is made that the general block criterion or the uniform-frequency case is new.

## Limitations
The loss probability is fixed strictly between zero and one; the theorem does not handle \(p=p_n\), arbitrary weight sequences with \(w_+\not\to0\), or all superpolynomially small \(w_-\). It proves no optimal general threshold for individual rare weights. The statement and proof treat full-collection first hitting, rather than the complete path law or partial-coverage times. An earlier equivalent conclusion expressed as a random-scan product-chain rare-hitting theorem remains a priority risk; absence from searches is not a proof of novelty. Independent scientific audit has not been performed.

## References
[1] L. J. Attrill and T. M. Garoni, *The clumsy coupon collector's problem*, arXiv:2605.14206v1 (first publicly posted 2026-05-14), https://arxiv.org/abs/2605.14206.

[2] C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors*, arXiv:2605.14511v1 (first publicly posted 2026-05-14), https://arxiv.org/abs/2605.14511, especially Theorem 2.3 and Section 4.

[3] E. Cruciani and A. Dudeja, *The Careless Coupon Collector's Problem*, arXiv:2602.20705v1 (2026), https://arxiv.org/abs/2602.20705.
