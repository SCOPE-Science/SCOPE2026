# Gaussian, atomic, and uniform limits for square-completed divisor ratios

## Finding

For a positive integer \(n\), let \(s(n)\) be the smallest nonnegative integer for which \(n+s(n)\) is a perfect square. Write \(\tau\) for the divisor-counting function, \(\omega\) for the number of distinct prime factors, and
\[
D(v)=\frac{\tau(v)}{2^{\omega(v)}}.
\]
For \(X\ge 100\), choose \(N_X\) uniformly from \(\{1,\ldots,\lfloor X\rfloor\}\), and put
\[
M_X=\lceil\sqrt{N_X}\rceil,\qquad T_X=\lfloor\sqrt X\rfloor,\qquad
c=\log(3/2),\qquad L_X=\log\log T_X.
\]
Define the three real-valued random variables
\[
Z_X=\frac{\log D(N_X+s(N_X))-cL_X}{c\sqrt{L_X}},\qquad
R_X=\log D(N_X+s(N_X))-c\,\omega(M_X),\qquad
U_X=\frac{s(N_X)}{2M_X-1}.
\]
Then, as \(X\to\infty\),
\[
\boxed{(Z_X,R_X,U_X)\ \Longrightarrow\ (Z,R,U),}
\]
where the three coordinates on the right are **mutually independent**, \(Z\) is standard Gaussian, \(U\) is uniform on \([0,1]\), and \(R\) is the explicit, purely atomic random Euler sum below.

For every prime \(p\), take independent integer-valued \(V_p\), with
\[
\Pr(V_p=a)=(1-p^{-1})p^{-a},\qquad a=0,1,2,\ldots .
\]
Then
\[
\boxed{R=\sum_{p\colon V_p\ge2}\log\frac{2V_p+1}{3}}
\]
is almost surely a finite sum, and its characteristic function is
\[
\mathbf E e^{itR}=
\prod_{p}\left(1-p^{-2}+(1-p^{-1})\sum_{a=2}^\infty
p^{-a}\left(\frac{2a+1}{3}\right)^{it}\right).
\]
In particular, two distinguished exact atoms are
\[
\boxed{\Pr(R=0)=\frac6{\pi^2}},\qquad
\boxed{\Pr\left(R=\log\frac53\right)=\frac6{\pi^2}
\sum_{p}\frac1{p(p+1)}}.
\]
The second probability is approximately \(0.200756\); the first is approximately \(0.607927\).

## Assumptions and scope

All limits are unconditional and concern positive integers sampled uniformly up to a real threshold \(X\to\infty\). The normalization is defined for sufficiently large \(X\), and the displayed choice \(X\ge100\) ensures \(L_X>0\). No hypotheses are imposed on the prime factorization of the sampled integer. The first public source defining this square-completion statistic is identified in the references; **none of its claimed summatory asymptotics is assumed** here. The result concerns weak convergence, not local limit probabilities for individual atoms of \(R_X\), and claims no rate for convergence of the triple.

## Proof

**1. Exact arithmetic decomposition.** Let \(m=\lceil\sqrt n\rceil\). Precisely the integers
\[
(m-1)^2<n\le m^2
\]
produce \(n+s(n)=m^2\), and their shifts run once through \(\{0,1,\ldots,2m-2\}\). If \(p^a\parallel m\), then the factor of \(D(m^2)\) contributed by \(p\) is \((2a+1)/2\). Therefore, defining
\[
H(m)=\sum_{p^a\parallel m,\ a\ge2}\log\frac{2a+1}{3},
\]
we have the exact identity
\[
\log D(m^2)=c\,\omega(m)+H(m).
\tag{1}
\]
In particular \(R_X=H(M_X)\).

**2. Weighted sampling and the independent phase.** First restrict to \(X=T^2\), \(T\) a positive integer. There are \(2m-1\) integers in the \(m\)-th square-completion block, so
\[
\Pr(M_{T^2}=m)=\frac{2m-1}{T^2}\qquad(1\le m\le T).
\tag{2}
\]
Conditional on this event, \(s(N_{T^2})\) is uniform on the \(2m-1\) integers from \(0\) to \(2m-2\). For every bounded Lipschitz function \(f\) on \([0,1]\), the conditional expectation of \(f(U_{T^2})\) differs from \(\int_0^1f(u)\,du\) by at most \(\operatorname{Lip}(f)/(2m-1)\). Averaging (2), the error is at most \(\operatorname{Lip}(f)/T\). The same inequality holds when the conditional expectation is multiplied by any bounded function of \(m\). Thus the phase tends to a uniform random variable independently of every tight weak limit of statistics depending only on \(m\), including the two statistics below.

**3. The correction has a discrete Euler limit.** Fix \(B\), and set \(H_{\le B}\) equal to the sum defining \(H\) restricted to primes not exceeding \(B\). For each fixed finite prime set, the vector of valuations of \(M_{T^2}\) converges to the corresponding independent geometric vector. Indeed, the unweighted count of \(m\le T\) in any fixed residue class modulo \(q\) is \(T/q+O(1)\), and summation by parts upgrades it to the weight (2); prescribing bounded valuations is a finite collection of such congruences, with the unbounded valuation tail made arbitrarily small. Consequently
\[
H_{\le B}(M_{T^2})\Longrightarrow R_{\le B}
=\sum_{p\le B,\ V_p\ge2}\log\frac{2V_p+1}{3}.
\]
For every exponent \(a\ge2\), \(0\le\log((2a+1)/3)\le a-1\), hence
\[
0\le H(m)-H_{\le B}(m)
\le \sum_{p>B}\sum_{a\ge2}\mathbf1_{p^a\mid m}.
\]
The weight (2) is at most \(2/T\); counting multiples proves the uniform bound
\[
\sup_T\mathbf E\left[H(M_{T^2})-H_{\le B}(M_{T^2})\right]
\le2\sum_{p>B}\sum_{a\ge2}p^{-a}
=2\sum_{p>B}\frac1{p(p-1)}\longrightarrow0.
\tag{3}
\]
The same series bounds the limiting tail \(R-R_{\le B}\) in mean. It also ensures \(\sum_p\Pr(V_p\ge2)=\sum_pp^{-2}<\infty\); thus only finitely many terms of \(R\) are nonzero almost surely. The finite-prime limit followed by (3) yields \(H(M_{T^2})\Longrightarrow R\). Independence of the geometric coordinates gives the Euler-product characteristic function.

**4. Gaussian bulk independent of the correction.** For any fixed modulus \(q\) and any nonempty congruence class modulo \(q\), the Erdős–Kac theorem for \(\omega(m)\) remains valid with its usual centering \(\log\log T\) and scale \(\sqrt{\log\log T}\), when \(m\le T\) is restricted to that class. For completeness, here is the standard fixed-progression moment reduction. Put \(y=T^{1/\log\log T}\) and truncate the prime count to \(p\le y\), \(p\nmid q\). For a fixed number of distinct such primes the simultaneous-divisibility count in the progression is \(T/(q\prod p)+O(1)\). As \(y^r=T^{o(1)}\) for every fixed moment order \(r\), the centered moments match those of independent Bernoulli prime indicators and give a standard normal limit after normalization. The excluded primes dividing \(q\) contribute at most \(\omega(q)\), and the primes above \(y\) have conditional mean at most \(O_q(1)+\log\log T-\log\log y=O_q(1+\log\log\log T)\), which is \(o(\sqrt{\log\log T})\); Markov's inequality removes them. The progression result follows. Conditioning on intervals \(\varepsilon T\le m\le T\), or equivalently using partial summation on the progression counting functions, gives the same normal law under the weight (2); the interval below \(\varepsilon T\) has weighted mass at most \(\varepsilon^2\).

Fix \(B\) and bound each valuation at primes \(p\le B\) by a fixed cutoff. Every specified valuation pattern is a union of residue classes for a fixed modulus, so the preceding conditional Gaussian law applies. Letting the valuation cutoffs grow proves the joint limit
\[
\left(
\frac{\omega(M_{T^2})-\log\log T}{\sqrt{\log\log T}},
H_{\le B}(M_{T^2})\right)
\Longrightarrow(Z,R_{\le B})
\]
with **independence** on the right. Uniformly small tails (3) and then \(B\to\infty\) yield independence of \(Z\) and \(R\). Since \(H(M_{T^2})\) is tight, equation (1) and Slutsky's theorem replace the normalized \(\omega\) count by \(Z_{T^2}\) without changing the limit. Step 2 adds the independent uniform phase.

**5. Arbitrary cutoffs and atom formulas.** With \(T=\lfloor\sqrt X\rfloor\), the integers in the incomplete final square block number at most \(2T+1\), a proportion \(O(T^{-1})\) of \(\{1,\ldots,\lfloor X\rfloor\}\). Their removal changes every bounded test expectation by \(O(T^{-1})\); the normalization based on \(T\) remains the same. This transfers the joint limit from square cutoffs to all real \(X\to\infty\).

For the first atom, \(R=0\) precisely when \(V_p\le1\) for every prime, an event of probability
\[
\prod_p(1-p^{-2})=\zeta(2)^{-1}=6/\pi^2.
\]
The smallest nonzero summand is \(\log(5/3)\), attained exactly at valuation two. Thus \(R=\log(5/3)\) holds exactly when one prime has valuation two and all other primes have valuation at most one. Relative to the event at zero, its probability factor at the distinguished prime is
\[
\frac{\Pr(V_p=2)}{\Pr(V_p\le1)}
=\frac{(1-p^{-1})p^{-2}}{1-p^{-2}}
=\frac1{p(p+1)},
\]
which gives the second claimed atom. This completes the proof.

## Verification

The accompanying `verification/check.py` performs direct integer and rational checks of the block decomposition, the exact divisor-ratio factorization, and the characterization of the first two correction atoms. It checks every shift through \(n=40000\), factorization data for \(m\le30000\), and exact phase grids for \(m\le69\). Its completed execution reports `VERIFY_OK`; the finite check does not prove the central limit theorem, prime-tail estimate, or limiting independence, which are proved above.

## Relationship to prior work

Mihoub (2026, first public version February 24) introduced this particular square-completion divisor statistic and studied its **summatory mean**, not a probability limit in three coordinates. The exact block identity and the local divisor factors are consistent with the definitions there; no summatory asymptotic from that source is used as an ingredient. Levy and Squillace (2024) establish a more general scalar Erdős–Kac theorem for perturbed integer distributions, while the classical Erdős–Wintner theorem and its effective versions address the limiting distribution of additive corrections. These results account for the standard Gaussian and additive-limit ingredients; this theorem identifies the simultaneous, independent Gaussian/atomic/phase law for the shifted-square observable and gives its first two correction atoms. The proof above explicitly treats the congruence conditioning and weighting required for joint independence, so mere marginal convergence is not substituted for a joint theorem. A general unindexed joint additive-function principle might cover portions of the conclusion; no claim of independence from all established probabilistic-number-theory methods is made.

## Limitations

The limit is weak convergence, and neither an effective triple convergence rate nor exact finite-cutoff atom probabilities are claimed. An independent priority assessment remains open. The proof does not establish the summatory mean asymptotic for \(D(n+s(n))\); in particular, it does not use any unpublished or conditional zeta-function estimates. The atoms identified here belong to the centered correction \(R\), not to the normalized Gaussian coordinate \(Z\). Finite calculations provide reproducibility checks, not infinite proofs.

## References

1. Bouderbala Mihoub, *On the Asymptotic Behavior of a Multiplicative Arithmetic Function Related to the Divisor Function Over Perfect Squares Integers Generated by Shifting*, arXiv:2602.20808v1 (public February 24, 2026), https://arxiv.org/abs/2602.20808.
2. Matthew Levy and Joseph Squillace, *A Generalization of the Erdős–Kac Theorem*, arXiv:2405.06860 (2024), https://arxiv.org/abs/2405.06860.
3. Anup B. Dixit and M. Ram Murty, *A localized Erdős–Kac theorem*, Hardy–Ramanujan Journal 43 (2021), 17–23; DOI:10.46298/hrj.2021.7433.
4. Gérald Tenenbaum and Johann Verwee, *Effective Erdős–Wintner Theorems*, Proc. Steklov Inst. Math. 314 (2021), 264–278; DOI:10.1134/S008154382104012X.
5. Paul Erdős and Mark Kac, *The Gaussian law of errors in the theory of additive number theoretic functions*, American Journal of Mathematics 62 (1940), 738–742.
