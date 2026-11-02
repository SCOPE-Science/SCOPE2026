# Poisson dust and finite exceptional loss modes in clumsy coupon collection

## Finding

**Theorem (heterogeneous clumsy collection: exact factorization and finite-defect critical law).** Fix an integer \(r\ge0\). For each integer \(m>r\), draw one of \(m\) coupon types uniformly and independently each day. When type \(i\) is drawn, its occupied flag is replaced by absent with probability \(p_{m,i}\in[0,1)\) and by present with probability \(1-p_{m,i}\), independently of all past draws and marks. Other flags are unchanged. Initially every flag is absent. Write \(C_m\) for the ordinary first-appearance time of all types, \(T_m\) for the first all-present time, and \(W_m=T_m-C_m\).

For each finite \(m\), **\(C_m\) and \(W_m\) are independent**. Set
\[
 H_m(u)=\prod_{i=1}^{m}(1-p_{m,i}+p_{m,i}u)
 =\sum_{k=0}^{m}a_{m,k}u^k,
 \qquad a_{m,0}=\prod_{i=1}^{m}(1-p_{m,i}).
\]
For every \(0<z<1\), put \(v=m(z^{-1}-1)\). The waiting-time probability-generating function is exactly
\[
 \boxed{\mathbb E[z^{W_m}]
 =\frac{a_{m,0}}{v\int_0^1u^{v-1}H_m(u)\,du}
 =\frac{a_{m,0}}{\sum_{k=0}^{m}a_{m,k}v/(v+k)}.}
\]

Assume that the first \(r\) types have persistent loss probabilities and all remaining types have diffuse losses:
\[
 p_{m,j}\longrightarrow q_j\in[0,1)\ (1\le j\le r),\qquad
 \max_{r<i\le m}p_{m,i}\longrightarrow0,\qquad
 \sum_{i=r+1}^{m}p_{m,i}\longrightarrow c\in[0,\infty).
\]
Then
\[
 \boxed{\frac{T_m-m\log m}{m}\ \Longrightarrow\ G+\tau_{c,\mathbf q},}
\]
where \(G\) is standard Gumbel, independent of the nonnegative variable \(\tau_{c,\mathbf q}\), and, for every \(s>0\),
\[
 \boxed{\mathbb E[e^{-s\tau_{c,\mathbf q}}]
 =\frac{\prod_{j=1}^{r}(1-q_j)}
 {s\int_0^1u^{s-1}e^{cu}\prod_{j=1}^{r}(1-q_j+q_ju)\,du}.}
\]
The law is the stationary-start first hitting time of the all-zero state of a product of an immigration–death process (arrival rate \(c\), per-particle death rate one) and \(r\) independent two-state absent/present refresh chains, with absent stationary probability \(q_j\). It has an atom
\[
 \boxed{\Pr(\tau_{c,\mathbf q}=0)=e^{-c}\prod_{j=1}^{r}(1-q_j).}
\]
In particular, **all diffuse microscopic loss heterogeneity washes out**, depending only on its total mass \(c\), but an order-one exceptional loss type survives as a separate two-state component. For \(r=1\), \(c=0\), and \(0<q_1=q<1\),
\[
 \tau_{0,(q)}\sim(1-q)\delta_0+q\,\operatorname{Exp}(1-q),
\]
where \(\operatorname{Exp}(1-q)\) denotes the exponential law of rate \(1-q\). This law is not the pure diffuse-loss law with \(c=q\): their masses at zero differ, \(1-q\ne e^{-q}\).

## Assumptions and scope

Each loss mark refers to the *selected type only*, and observation occurs immediately after the daily refresh. Type choices are uniform; loss probabilities may depend on the type and on \(m\), but not on time or history. Every finite-system loss probability is strictly below one. The number \(r\) of exceptional types is fixed, while \(m\to\infty\). The theorem concerns weak distributional limits, not convergence of unbounded moments. The limiting queue process is well defined also for \(c=0\) (identically zero queue) and any \(q_j=0\) (permanently present exceptional flag). An empty product is one.

The standard Gumbel variable has cumulative distribution function \(\Pr(G\le x)=\exp(-e^{-x})\). The two-state component is described using its *absent* flag: absent becomes present at rate \(1-q_j\), present becomes absent at rate \(q_j\), and its stationary absent probability is \(q_j\). The queue counts absent diffuse types; immigration adds one absent type at rate \(c\) and each absent type recovers at rate one.

## Proof

**1. Exact post-appearance stationarity and independence.** Reveal the entire sequence of coupon *labels* through their first full coverage \(C_m\), but do not reveal any independent success/loss marks. Every type has a unique last occurrence by \(C_m\). The marks at these last occurrences are independent, with loss probability \(p_{m,i}\) for type \(i\), irrespective of the realized label sequence and of \(C_m\). Thus the absent indicators at time \(C_m\) have the product Bernoulli law \(\pi_m\) with those parameters, independent of the entire revealed label history. Future labels and marks are independent. The refresh chain preserves \(\pi_m\), since each selected coordinate is redrawn from its own stationary Bernoulli law. Consequently \(W_m\) is exactly the all-present hitting time of this stationary-start chain and is independent of \(C_m\), proving the stated finite factorization.

**2. Exact transform from a stationary hitting-time resolvent.** Embed the discrete chain in independent rate-one Poisson clocks, one per type. Their union has rate \(m\) and its successive selected type labels are independent and uniform; at each jump apply the same refresh mark. Starting in \(\pi_m\), write \(\sigma_m\) for the first time all coordinates are present. Conditional on \(W_m\), it is the sum of \(W_m\) independent rate-\(m\) exponentials, hence
\[
 \mathbb E[e^{-s\sigma_m}]
 =\mathbb E\left[\left(\frac{m}{m+s}\right)^{W_m}\right],\qquad s>0.
\]
Call the all-present state \(\mathbf0\). Its stationary mass is \(\pi_m(\mathbf0)=a_{m,0}\). If the process starts from \(\mathbf0\), the probability that type \(i\) is present at time \(t\) is \(1-p_{m,i}+p_{m,i}e^{-t}\), by the rate-one refresh clock. Independence across clocks gives its return probability
\[
 K_m(t)=\Pr_{\mathbf0}(X_t=\mathbf0)
 =\prod_i(1-p_{m,i}+p_{m,i}e^{-t})=H_m(e^{-t}).
\]
The strong Markov property at \(\sigma_m\) and stationarity imply the renewal convolution
\[
 a_{m,0}=\Pr_{\pi_m}(X_t=\mathbf0)
 =\int_{[0,t]}K_m(t-u)\,\Pr_{\pi_m}(\sigma_m\in du).
\]
Tonelli's theorem and a Laplace transform in \(t\) yield
\[
 \frac{a_{m,0}}s
 =\mathbb E[e^{-s\sigma_m}]\int_0^\infty e^{-st}H_m(e^{-t})\,dt
 =\mathbb E[e^{-s\sigma_m}]\int_0^1u^{s-1}H_m(u)\,du.
\]
Here \(a_{m,0}>0\) and the denominator is positive, so solving for the transform is legitimate. Take \(s=v=m(z^{-1}-1)\) and expand \(H_m\) into its nonnegative coefficients. This proves the *exact* finite-system generating function, including the case \(W_m=0\).

**3. Critical loss-profile convergence.** For \(i>r\) and \(0\le u\le1\), write \(h_{m,i}(u)=1-p_{m,i}(1-u)\). Since \(\max_{i>r}p_{m,i}\to0\) and \(\sum_{i>r}p_{m,i}\to c\), uniformly for \(u\in[0,1]\),
\[
 \sum_{i>r}\log h_{m,i}(u)
 =-(1-u)\sum_{i>r}p_{m,i}
 +O\!\left(\sum_{i>r}p_{m,i}^2\right)
 \longrightarrow-c(1-u),
\]
because \(\sum_{i>r}p_{m,i}^2\le(\max_{i>r}p_{m,i})\sum_{i>r}p_{m,i}\to0\). Taking the finite exceptional product gives the uniform limit
\[
 H_m(u)\longrightarrow H_\infty(u)=e^{c(u-1)}\prod_{j=1}^{r}(1-q_j+q_ju),
\qquad a_{m,0}\longrightarrow H_\infty(0)=e^{-c}\prod_j(1-q_j)>0.
\]
For fixed \(s>0\), set \(z_m=e^{-s/m}\) and \(v_m=m(e^{s/m}-1)\to s\). In the generating-function formula, \(0\le H_m(u)\le1\); for large \(m\), \(v_m\ge s/2\), so the integral is dominated by a constant times \(u^{s/2-1}\), integrable on \((0,1)\). Dominated convergence produces
\[
 \mathbb E[e^{-sW_m/m}]
 \longrightarrow
 \frac{e^{-c}\prod_j(1-q_j)}{s\int_0^1u^{s-1}e^{c(u-1)}\prod_j(1-q_j+q_ju)\,du},
\]
which simplifies to the asserted formula. The limiting expression is a Laplace transform, as proved in Step 4, so the continuity theorem gives \(W_m/m\Rightarrow\tau_{c,\mathbf q}\).

**4. Identification of the limiting hitting time.** Construct the independent stationary-start immigration–death and two-state chains specified above. The immigration–death count is Poisson with mean \(c\) at stationarity; starting from zero, the count at time \(t\) is Poisson with mean \(c(1-e^{-t})\), so its zero-state return probability is \(e^{-c(1-e^{-t})}\). For an exceptional two-state chain initially present, the chance of being present at \(t\) is \(1-q_j+q_je^{-t}\). Therefore the all-zero return probability is precisely \(H_\infty(e^{-t})\), and its stationary all-zero mass is \(H_\infty(0)>0\). The convolution argument from Step 2 applies verbatim, giving the limiting transform. This product continuous-time chain is positive recurrent and hits the all-zero state almost surely: the immigration–death count is recurrent to zero from every finite state, the finite independent flag chain is irreducible after removing deterministic components, and the joint stationary mass of the target is strictly positive. Consequently its first-hitting-time distribution is proper.

The probability of a *zero* hitting time is precisely the stationary mass of the all-zero state, \(e^{-c}\prod_j(1-q_j)\), since positive waiting times cannot contribute to the atom at time zero. For one exceptional type and \(c=0\), a present initial state (probability \(1-q\)) yields zero waiting, whereas an absent initial state (probability \(q\)) waits for a rate-\(1-q\) recovery; the explicit mixture follows.

**5. Completion-time limit.** For uniformly sampled coupon labels, the classical Erdős–Rényi coupon-collector limit yields \((C_m-m\log m)/m\Rightarrow G\). The Step 1 independence is *exact for each* \(m\), so the joint limit has independent coordinates and the continuous-mapping theorem yields \((T_m-m\log m)/m\Rightarrow G+\tau_{c,\mathbf q}\). This concludes the proof.

## Verification

The standalone `check.py` verifies the finite generating function by exact rational Gaussian elimination of first-hitting probabilities in all nontrivial subset states for several heterogeneous \(m\le4\) examples; it verifies the one-exception explicit mixture and obstruction by rational identities, and it compares the finite-\(m\) transforms numerically with the displayed integral for several multi-exception profiles at three increasing sizes. The recorded output is in `CHECK_OUTPUT.txt`. Every computation is supplementary and finite; the infinite weak-convergence theorem is justified by the uniform logarithmic estimate, dominated convergence, stationary-hitting resolvent, and classical coupon-collector limit in the proof.

Run `python3 check.py` with Python 3's standard library. No external data, random seeds, packages, or network services are required. The checker evaluates the completed claims rather than certifying mathematical priority or replacing the analytic proof.

## Relationship to prior work

Attrill and Garoni, *The clumsy coupon collector's problem* (2026), Theorem 4.10, prove \(G+\tau_c\) for one **common** loss probability satisfying \(mp_m\to c\). The present \(r=0\) case contains that known law and is **not** asserted new by itself. The new structural statement is the joint universality of all diffusely heterogeneous loss profiles together with independent finite exceptional loss modes, their explicit transform and their sharp one-exception obstruction. Their sections 3–4 derive generating functions and the critical immigration–death limit for identical loss parameters; no type-dependent profile or macroscopic exceptional modes appear in the inspected results.

Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors* (2026), studies the fixed homogeneous loss probability regime using stationary entry flux, and studies a separate global reset-button model. Those results do not imply the present critical mixed diffuse/fixed-defect law. Gast (2011) studies random scanning of **identical absorbing** chains, yielding growth-order bounds; the present state is not absorbing and has nontrivial stationary target mass. General Markov-chain resolvent identities themselves are standard: novelty is not claimed for the convolution identity alone, but for its exact type-dependent coupon application and the limiting universality-with-exceptions classification.

A related published mathematical record on balanced nonuniform global-reset coupon collectors varies *coupon sampling weights* while imposing a common **global reset event**. It does not address distinct loss probabilities applied independently to the selected coupon, and its rate-functional exponential delays are not the present critical waiting law. Related terminal-cloud results for sliding-window coupon expiration are also different: loss there follows a window cutoff, not an independent refresh mark for the selected type.

## Limitations

The theorem requires uniform coupon selection, independent time-homogeneous loss marks, and a *fixed finite* number of exceptional types with loss probabilities bounded away from one in the limit. It does not cover many exceptional modes of nonvanishing size, moving \(q_j\to1\), loss marks dependent on time or other coupon types, or nonuniform coupon selection. No convergence of the means or higher moments of the scaled waiting time is asserted. The possibility that a more general, unindexed heterogeneous product-chain first-hitting theorem already subsumes the stated probability law remains a historical-priority risk; independent review has not been performed.

## References

1. L. J. Attrill and T. M. Garoni, *The clumsy coupon collector's problem*, arXiv:2605.14206 (first public May 14, 2026), especially Sections 3–4 and Theorem 4.10. https://arxiv.org/abs/2605.14206
2. C. D. Long, *Clumsy and Careless: Stationary-Entry Flux in Non-monotone Coupon Collectors*, arXiv:2605.14511 (first public May 14, 2026), especially Sections 1, 2 and 4. https://arxiv.org/abs/2605.14511
3. N. Gast, *Computing hitting times via fluid approximation: application to the coupon collector problem*, arXiv:1107.3385 (first public July 18, 2011), especially Sections 2–4. https://arxiv.org/abs/1107.3385
