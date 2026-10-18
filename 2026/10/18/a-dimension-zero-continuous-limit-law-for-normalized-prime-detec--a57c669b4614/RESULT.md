# A dimension-zero continuous limit law for normalized prime-detecting Fourier coefficients

## Finding
Fix any odd integers \(3\le k<\ell\). Write
\[
\sigma_s(n)=\sum_{d\mid n}d^s,\qquad
c_{k,\ell}(n)=(1+n^\ell)\sigma_k(n)-(1+n^k)\sigma_\ell(n),\qquad
Z_{k,\ell}(n)=\frac{c_{k,\ell}(n)}{n^{k+\ell}}.
\]
These are the positive-index Fourier coefficients of the classical prime-detecting quasimodular form
\[
 f_{k,\ell}=(D^\ell+1)G_{k+1}-(D^k+1)G_{\ell+1},
\]
where \(D=q\,d/dq\) and the positive-index coefficients of \(G_{s+1}\) are \(\sigma_s(n)\). The coefficient formula and its prime-detection property are previously known; neither is claimed as new here.

For each rational prime \(p\), take mutually independent nonnegative-integer-valued random variables \(V_p\) with
\[
 \Pr(V_p=a)=(1-p^{-1})p^{-a}\quad(a=0,1,2,\ldots).
\]
For \(s>1\) set
\[
 U_s=\prod_p\bigl(1+p^{-s}+\cdots+p^{-sV_p}\bigr),\qquad W_{k,\ell}=U_k-U_\ell.
\]
Each infinite product converges uniformly over all possible exponent configurations and \(0\le W_{k,\ell}\le\zeta(k)-1\). **Theorem.** As \(X\to\infty\), the empirical laws
\[
 \frac1{\lfloor X\rfloor}\sum_{n=1}^{\lfloor X\rfloor}\delta_{Z_{k,\ell}(n)}
 \Longrightarrow \mu_{k,\ell}:=\operatorname{Law}(W_{k,\ell}).
\]
The probability measure \(\mu_{k,\ell}\) is non-atomic and is carried by a Borel subset of \(\mathbb R\) of Hausdorff dimension **zero**. Consequently its distribution function is continuous, while the measure is singular with respect to Lebesgue measure. All conclusions hold simultaneously for every fixed odd pair \(3\le k<\ell\). The two Euler products in the definition are **correlated**, using the same prime exponent variables; they must not be treated as independent.

## Assumptions and scope
The parameter pair is fixed, with \(k,\ell\) odd integers and \(3\le k<\ell\); the limits are for integers \(n\) sampled uniformly from \(1,\ldots,\lfloor X\rfloor\). There is no claim of a uniform rate in \(k,\ell\), of a density function, or of analogous behavior at the endpoint \(k=1\). The zero-dimensional *full-measure set* need not be the topological support of the measure. The statement concerns ordinary rational primes, rather than polynomial primes over a finite field.

## Proof
**1. Exact normalized coefficient.** Directly from the divisor-sum formula,
\[
 Z_{k,\ell}(n)=H_k(n)-H_\ell(n)+R_{k,\ell}(n),\qquad
 H_s(n)=\frac{\sigma_s(n)}{n^s}=\sum_{d\mid n}d^{-s},
\]
with \(R_{k,\ell}(n)=(\sigma_k(n)-\sigma_\ell(n))/n^{k+\ell}\). Since \(H_s(n)\le\zeta(s)\), we have \(|R_{k,\ell}(n)|\le[\zeta(k)+\zeta(\ell)]n^{-k}\). This error tends to zero in probability for a uniformly sampled index. For every prime power \(p^a\), the local factor of \(H_s\) is \(h_s(p,a)=\sum_{j=0}^a p^{-sj}\).

**2. Joint weak convergence.** For any fixed bound \(Y\) on primes and any finite list of prescribed exponents \((a_p)_{p\le Y}\), elementary congruence counting (or the Chinese remainder theorem) gives the limiting frequency
\[
 \prod_{p\le Y}\frac{1-1/p}{p^{a_p}}.
\]
This proves weak convergence of the truncated vector \((H_k^{(Y)}(n),H_\ell^{(Y)}(n))\) to the corresponding product-vector \((U_k^{(Y)},U_\ell^{(Y)})\). The tails can be controlled **uniformly**, without a probabilistic estimate: for every exponent assignment and every \(s\ge k\ge3\),
\[
 1\le\prod_{p>Y} h_s(p,a_p)\le\prod_{m>Y}(1-m^{-s})^{-1}
 =1+O_s(Y^{1-s}).
\]
The full products are bounded by \(\zeta(s)\); hence \(|H_s-H_s^{(Y)}|+|U_s-U_s^{(Y)}|\ll_sY^{1-s}\). First let the index bound tend to infinity for fixed \(Y\), then let \(Y\to\infty\). Adding the vanishing term \(R\) establishes the asserted empirical weak limit.

**3. A self-contained non-atomicity lemma.** First note that for any fixed exponent assignment at the primes other than \(p\), the products \(A=\prod_{q\ne p}h_k(q,V_q)\) and \(B=\prod_{q\ne p}h_\ell(q,V_q)\) obey \(A\ge B\ge1\). If precisely one prime \(p\) has exponent \(1\) in a selected finite prime block and all other primes of that block have exponent \(0\), then with the remaining exponents frozen the value is
\[
 T(p)=A(1+p^{-k})-B(1+p^{-\ell}).
\]
For real \(x\ge2\),
\[
 T'(x)=-kAx^{-k-1}+\ell Bx^{-\ell-1}
 \le Ax^{-k-1}(-k+\ell\,2^{-(\ell-k)})<0.
\]
Indeed \(\ell<k2^{\ell-k}\) for all integers \(\ell>k\ge3\). Thus \(T(p)\) takes distinct values at distinct primes.

Partition all sufficiently large primes into successive disjoint finite blocks \(B_j\) satisfying \(1\le S_j=\sum_{p\in B_j}p^{-1}\le2\). The existence of infinitely many blocks is exactly the classical divergence of the prime harmonic series. Let \(E_j\) be the event that exactly one variable in \(B_j\) equals \(1\) and all others equal \(0\). Independence gives
\[
 \Pr(E_j)=\left(\prod_{p\in B_j}(1-p^{-1})\right)S_j\ge e^{-4}>0.
\]
Here \(\log(1-1/p)\ge-2/p\). Conditional on \(E_j\), the unique active prime has probability \(p^{-1}/S_j\) of being \(p\). Consequently, with all variables outside \(B_j\) fixed, no fixed value of \(W_{k,\ell}\) can have conditional probability more than \(1/\min B_j\). In a long collection of blocks beginning at index \(J\), the probability that no \(E_j\) occurs is at most \((1-e^{-4})^{N}\). On the complementary event choose the first successful block. Conditioning on the success indicators and on all variables outside that chosen block preserves its stated conditional distribution, so for any \(t\in\mathbb R\)
\[
 \Pr(W_{k,\ell}=t)\le(1-e^{-4})^{N}+(\min B_J)^{-1}.
\]
Let \(N\to\infty\), then \(J\to\infty\). The right side goes to zero, proving atomlessness.

**4. A zero-dimensional full-measure set.** For \(X>2\), write \(\mathcal V_X=(V_p)_{p\le X}\) and define its information content
\[
 L_X=-\log\Pr(\mathcal V_X)
 =\sum_{p\le X}\left(-\log(1-p^{-1})+V_p\log p\right).
\]
Since \(\mathbb EV_p=1/(p-1)\), the elementary prime-sum estimate \(\sum_{p\le X}(\log p)/p=O(\log X)\) implies \(\mathbb EL_X\le C\log X\) for an absolute constant \(C\), once \(X\ge3\). Fix \(K>4C\). Markov's inequality then gives \(\Pr(L_X\le K\log X)\ge3/4\) for all large \(X\).

Fix a real \(0<\varepsilon<1\), put \(Y=X^{1/\varepsilon}\), and let \(G_X\) be the event that \(V_p=0\) for every prime \(X<p\le Y\). Mertens' product formula gives
\[
 \Pr(G_X)=\prod_{X<p\le X^{1/\varepsilon}}(1-p^{-1})\longrightarrow\varepsilon.
\]
The events \(G_X\) and \(\{L_X\le K\log X\}\) depend on disjoint prime sets and are independent. Thus their conjunction has probability bounded away from zero for large \(X\). Take a deterministic increasing sequence \(X_j=\exp(j^2)\). The probability that infinitely many of these conjunctions hold is at least their limiting lower probability (apply \(\Pr(\limsup E_j)\ge\limsup\Pr(E_j)\)).

To turn this positive probability into probability one, consider the event
\[
 \mathcal F_\varepsilon=
 \left\{\liminf_{\substack{j\to\infty\\G_{X_j}\ \mathrm{holds}}}
 \frac{L_{X_j}}{\log X_j}\le K\right\},
\]
with an empty liminf interpreted as infinity. This event has positive probability by the preceding argument. Changing finitely many prime-exponent variables alters \(L_{X_j}\) by a fixed finite constant for all large \(j\), hence changes its quotient by \(\log X_j\) by \(o(1)\), and cannot affect \(G_{X_j}\) for all sufficiently large \(j\). Therefore \(\mathcal F_\varepsilon\) is a tail event of the independent family \((V_p)\). Kolmogorov's zero-one law implies \(\Pr(\mathcal F_\varepsilon)=1\). In particular, for almost every configuration there are infinitely many \(j\) for which both \(G_{X_j}\) and \(L_{X_j}\le(K+1)\log X_j\) hold.

For a fixed \(j\), the number \(N_j\) of possible exponent prefixes \((a_p)_{p\le X_j}\) having information content at most \((K+1)\log X_j\) is at most \(X_j^{K+1}\): every such prefix has probability at least \(X_j^{-(K+1)}\) and these probabilities sum to at most one. For each such prefix form its finite Euler-product difference \(w(a)\). On \(G_{X_j}\), the entire unrecorded contribution comes from primes exceeding \(Y_j=X_j^{1/\varepsilon}\). The uniform tail bound in Step 2 yields
\[
 |W_{k,\ell}-w(a)|\le C_{k,\ell}Y_j^{1-k}
 =C_{k,\ell}X_j^{-(k-1)/\varepsilon}.
\]
Consequently the measure is carried by a limsup of covers consisting, at stage \(j\), of no more than \(X_j^{K+1}\) intervals of diameter \(2C_{k,\ell}X_j^{-(k-1)/\varepsilon}\). For every \(d>\varepsilon(K+1)/(k-1)\), the total \(d\)-cost of these covers over all \(j\) is bounded by
\[
 C_d\sum_{j\ge1}\exp\left(j^2\left[K+1-\frac{d(k-1)}{\varepsilon}\right]\right)<\infty.
\]
Their limsup therefore has Hausdorff dimension no greater than \(\varepsilon(K+1)/(k-1)\). Apply this conclusion to the countable sequence \(\varepsilon=1/m\) for integers \(m\ge2\), and intersect the corresponding full-measure Borel limsup sets. The intersection still has full measure and has Hausdorff dimension zero. This completes the proof.

## Verification
The accompanying standalone `verify.py` uses exact rational arithmetic to compare the Fourier-coefficient formula with the normalized divisor-power representation, check known prime zeros and composite positivity, and test selected local strict-monotonicity instances. Running `python3 verify.py` gives `VERIFY_OK exact_coefficients=3000 monotonic_pairs=30`. No finite enumeration or numerical measurement is used as a proof of weak convergence, non-atomicity, or Hausdorff dimension; those conclusions follow from Steps 2–4.

## Relationship to prior work
Samuel Lelièvre (2004, Lemma 2 and Corollary 1) wrote down precisely the prime-detecting divisor-sum coefficients and the quasimodular family. Craig, van Ittersum, and Ono (2024, Lemma 9) established the same coefficient property in their partition-theoretic setting. Allen and Craig (arXiv:2609.32053v1, first posted 2026-09-25) recently studied these forms in prime intervals and arithmetic progressions; this is the immediate literature motivation for asking what their globally normalized coefficient distribution looks like. These works are not claimed as discoveries of the current theorem's coefficient formula. Erdős (1974) explicitly discusses the classical singular continuous distribution of \(\sigma(n)/n\), a one-component analogue, not the correlated difference of two divisor-power products or its dimension-zero description. Classical Erdős–Wintner theory establishes existence and continuity for many *additive* functions; the present difference of correlated multiplicative Euler products is not itself an additive function. The proof above separately establishes the specific joint random model, atomlessness, and dimension-zero carrier rather than treating earlier singularity as equivalent to the latter assertion.

## Limitations
The limit is qualitative: no explicit convergence rate or closed distribution function is claimed. Hausdorff dimension zero pertains to one Borel carrier of full measure, not necessarily the entire topological support. The normalization changes the values at primes, and prime indices themselves have zero density; this does not conflict with the prime-detecting zero coefficients. The proof assumes \(k\ge3\) so that the uniform Euler-product tail decays as a power; the \(k=1\) case is outside scope. The originality assessment is based on inspected primary literature and targeted searches, and cannot exclude a previously unpublished or implicitly stronger general measure-theoretic theorem.

## References
1. Samuel Lelièvre, *Quasimodular Forms with Fourier Coefficients Zero at Primes*, 8 June 2004, Lemma 2 and Corollary 1. https://www.imo.universite-paris-saclay.fr/~lelievre/papers/qmp/qmp.pdf
2. William Craig, Jan-Willem van Ittersum, and Ken Ono, *Integer Partitions Detect the Primes*, Proceedings of the National Academy of Sciences, 2024, Lemma 9. https://doi.org/10.1073/pnas.2409417121
3. Kevin Allen and William Craig, *Quasimodular Forms, Partitions, and Primes in Intervals*, arXiv:2609.32053v1, first submitted 2026-09-25. https://arxiv.org/abs/2609.32053
4. Paul Erdős, *On the Distribution of Numbers of the Form* \(\sigma(n)/n\) *and on Some Related Questions*, Pacific Journal of Mathematics 52 (1974), 59–65. https://scispace.com/pdf/on-the-distribution-of-numbers-of-the-form-sigma-n-n-and-on-p8qg1xu54x.pdf
