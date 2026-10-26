# Exact half-unit transport and sharp mode separation for parity-conditioned trinomial sums

## Finding
Let \(X_1,\ldots,X_n\) be independent, each supported on \(\{0,\tfrac12,1\}\), with arbitrary nonnegative state probabilities. Put \(S=\sum_{i=1}^n X_i\). Whenever both parity events have positive probability, let \(\mu_0=\mathcal L(S\mid S\in\mathbb Z)\) and \(\mu_{1/2}=\mathcal L(S\mid S\in\mathbb Z+\tfrac12)\). There is a coupling \((E,O)\) of these conditional laws such that
\[
 |E-O|=\tfrac12\quad\text{almost surely}.
\]
Hence, for **every** \(1\le p\le\infty\), the exact optimal transport cost under the ordinary distance is
\[
 W_p(\mu_0,\mu_{1/2})=\tfrac12,
\]
and \(|\mathbb E E-\mathbb E O|\le\tfrac12\). Any choices of modes \(m_0\) of \(\mu_0\) and \(m_{1/2}\) of \(\mu_{1/2}\), including either member of a two-mode tie, obey the **sharp** bound
\[
 |m_0-m_{1/2}|\le\tfrac32.
\]
The transport assertion is stronger than proximity of conditional means; the mode constant improves the previously published \(\tfrac52\) bound to its exact optimum.

## Assumptions and scope
Fix an arbitrary integer \(n\ge1\). Write \(L_i=\Pr(X_i=0)\), \(T_i=\Pr(X_i=\tfrac12)\), \(W_i=\Pr(X_i=1)\), with \(L_i+T_i+W_i=1\) and each parameter nonnegative. Assume \(\Pr(S\in\mathbb Z)>0\) and \(\Pr(S\in\mathbb Z+\tfrac12)>0\); this is necessary to define both conditional laws. A mode means any maximizer of the probability mass function on the corresponding integer or half-integer lattice. Wasserstein distances use the real-line metric \(|x-y|\); for \(p=\infty\), use the essential supremum of that distance. The coupling is an existence statement, not the coupling induced by conditioning one original sample simultaneously on incompatible events.

## Proof
**1. Polynomial decomposition.** First suppose all \(L_i,T_i,W_i\) are strictly positive. Define
\[
 G(w)=\mathbb E[w^{2S}]=\prod_{i=1}^n(L_i+T_iw+W_iw^2)
 =P(w^2)+wQ(w^2).
\]
The normalized polynomials \(P(z)/P(1)\) and \(Q(z)/Q(1)\) are the probability-generating functions, respectively, of \(E\) and \(O-\tfrac12\) under their separate conditional laws. Each quadratic factor of \(G\) is strictly Hurwitz stable: its roots have strictly negative real part because the sum and product of the roots are \(-T_i/W_i<0\) and \(L_i/W_i>0\). Thus \(G\) is strictly Hurwitz stable.

**2. Strict root interlacing.** The full Hermite–Biehler theorem, including its interlacing conclusion (Holtz, Theorem 1), applied to the stable polynomial \(G(w)=P(w^2)+wQ(w^2)\), gives simple strictly negative roots
\[
 \lambda_1<\eta_1<\lambda_2<\eta_2<\cdots<\eta_{n-1}<\lambda_n<0,
\]
where the \(\lambda_i\) are precisely the roots of \(P\) and the \(\eta_i\) those of \(Q\). The rightmost root belongs to \(P\); this orientation follows from the positive constant and leading coefficients, or explicitly from the last sentence in Holtz's proof of Theorem 2. Normalizing the linear factors produces Bernoulli parameters
\[
 a_i=(1-\lambda_i)^{-1},\qquad b_i=(1-\eta_i)^{-1},
\]
which satisfy \(0<a_1<b_1<a_2<\cdots<b_{n-1}<a_n<1\). Therefore, in distribution,
\[
 E=\sum_{i=1}^n B_i,\quad O=\tfrac12+\sum_{i=1}^{n-1} C_i,
\]
where the \(B_i\) are independent Bernoulli variables with parameters \(a_i\) and the \(C_i\) are independent Bernoulli variables with parameters \(b_i\). These are descriptions of the marginal conditional laws; no independence between \(E\) and \(O\) is claimed.

**3. Stochastic sandwich and coupling.** Put \(K=\sum B_i\) and \(J=\sum C_i\). Coupling each \(B_i\), \(i\le n-1\), below \(C_i\) with a shared uniform random variable, and bounding \(B_n\le1\), shows \(K\le_{\mathrm{st}}J+1\). Coupling each \(C_i\) below \(B_{i+1}\) similarly shows \(J\le_{\mathrm{st}}K\). In terms of cumulative distribution functions, for every integer \(k\),
\[
 \Pr(K\le k)\le\Pr(J\le k)\le\Pr(K\le k+1).
\]
Take the lower (left-continuous) quantiles of \(J\) and \(K\) at the **same uniform parameter** \(U\). Their values \(J^*=F_J^{-1}(U)\) and \(K^*=F_K^{-1}(U)\) satisfy \(J^*\le K^*\le J^*+1\) almost surely. Because they are integer-valued, \(K^*-J^*\in\{0,1\}\). Set \(E^*=K^*\) and \(O^*=J^*+\tfrac12\). Their marginals are \(\mu_0\) and \(\mu_{1/2}\), and \(|E^*-O^*|=\tfrac12\) surely. This construction is also a reproducible quantile-coupling algorithm.

**4. Boundary parameters.** For each \(\varepsilon\in(0,1)\), replace every probability triple by \((1-\varepsilon)(L_i,T_i,W_i)+\varepsilon(\tfrac13,\tfrac13,\tfrac13)\). All entries then are strictly positive. As \(\varepsilon\downarrow0\), the two nondegenerate conditional probability vectors converge coefficientwise on their fixed finite supports. Every corresponding quantile coupling is supported on the closed finite relation \(\{|e-o|=\tfrac12\}\), so a subsequence of the couplings converges to a coupling with the same support and the required limiting marginals. This establishes the theorem with zeros and deterministic factors permitted whenever both conditioning events have positive probability.

**5. Exact transport and modes.** Any integer and half-integer are at least \(\tfrac12\) apart. Thus every coupling has \(W_p\ge\tfrac12\), for finite \(p\ge1\) and for \(p=\infty\). Step 4 supplies a coupling attaining the lower bound at every exponent. The conditional means consequently differ by at most \(\tfrac12\). Each conditional law is a shifted Poisson-binomial distribution: this follows from the factorizations in Step 2 in the positive case and from coefficientwise limits of its real-rooted generating polynomials in the boundary case. Darroch's strict mode–mean bound gives
\[
 |m_0-\mathbb E E|<1,\qquad |m_{1/2}-\mathbb E O|<1.
\]
Therefore \(|m_0-m_{1/2}|<\tfrac52\). As one mode is integral and the other half-integral, the distance is a nonnegative half-integer of the form \(\tfrac12,\tfrac32,\tfrac52,\ldots\), hence it is at most \(\tfrac32\).

**6. Sharpness.** Take \(n=2\). Let \(X_1\) equal \(\tfrac12\) with probability \(\tfrac14\) and \(1\) with probability \(\tfrac34\); independently, let \(X_2\) equal \(0\) or \(1\), each with probability \(\tfrac12\). Then \(\mu_0\) assigns probability \(\tfrac12\) to each of \(1,2\), while \(\mu_{1/2}\) assigns probability \(\tfrac12\) to each of \(\tfrac12,\tfrac32\). The modes \(2\) and \(\tfrac12\) have distance \(\tfrac32\), so no smaller universal mode constant is possible. The exact \(\tfrac12\) transport cost is automatically optimal for any admissible model because of the lattice separation.

## Verification
The self-contained exact-arithmetic program `verify.py` enumerates all probability triples on rational grids with denominators two and three and all product laws of up to five independent variables; it checks the full CDF sandwich (not only a mean inequality), Darroch-derived mode bound, and an exact sharpness witness. Run `python3 verify.py`. It passed 7,966 nondegenerate instances on the denominator-two grid and 107,205 instances on the denominator-three grid; the two-variable sharpness witness also passed. These finite tests independently stress-test the algebraic inequalities but **do not** establish them for arbitrary \(n\) or arbitrary real parameters; the proof above does.

## Relationship to prior work
Broadie and Petkova, *On the structure of the Poisson trinomial distribution* (arXiv:2603.09019v1, first public 2026-03-09), prove parity-conditioned Poisson-binomial structure, a conditional-mean comparison with the unconditioned mean, and the \(\tfrac52\) bound on any cross-parity pair of modes. They invoke Hermite–Biehler to conclude that the even/odd polynomials are separately real-rooted. The argument here additionally exploits **the alternating order of their roots**, translates that order into a stochastic-order sandwich, and thereby obtains exact optimal transport and the sharp \(\tfrac32\) modal constant. These transport and sharpened mode statements are not asserted in the cited motivating paper. Holtz's theorem supplies the standard strict root interlacing, but not the probabilistic transport conclusion. Tang and Tang's Poisson-binomial survey gives general context for Bernoulli sums and approximations, rather than this parity-conditioned trinomial coupling. These are comparisons of mathematical implications, not evidence of exhaustive uniqueness.

## Limitations
Both parity events must have positive probability. The variables must be independent and supported on \(\{0,\tfrac12,1\}\). The coupling relates the two **conditional distributions**, not two outcomes observed jointly from a single physical experiment. The sharp modal example uses zero probability for some states; the universal inequality holds throughout the closed probability simplex. No assertion is made for arbitrary larger single-step supports, dependent trials, or conditional total-variation distances. Related treatments of stable-polynomial interlacing might imply the transport result without explicitly naming it; publication originality is therefore subject to external literature assessment. The result has undergone a self-review only, not an independent audit.

## References
1. M. Broadie and I. Petkova, *On the structure of the Poisson trinomial distribution*, arXiv:2603.09019v1 (posted 2026-03-09), https://arxiv.org/html/2603.09019v1.
2. O. Holtz, *Hermite–Biehler, Routh–Hurwitz, and total positivity*, Linear Algebra and its Applications **372** (2003), 105–110; open preprint arXiv:math/0512591, https://arxiv.org/abs/math/0512591.
3. J. N. Darroch, *On the distribution of the number of successes in independent trials*, Annals of Mathematical Statistics **35** (1964), 1317–1321.
4. W. Tang and F. Tang, *The Poisson binomial distribution — Old & New*, arXiv:1908.10024, https://arxiv.org/abs/1908.10024.
