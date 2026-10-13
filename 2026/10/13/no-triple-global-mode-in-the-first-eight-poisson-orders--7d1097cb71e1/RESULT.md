# No triple global mode in the first eight Poisson orders

## Finding

For each integer \(2\le k\le8\) and all real \(\lambda>0\), the Poisson distribution of order \(k\), defined by
\[
X_{k,\lambda}=\sum_{j=1}^{k} jN_j,\qquad N_j\ \text{independent and distributed as}\ \operatorname{Poisson}(\lambda),
\]
has **at most two distinct global modes**. A mode means an integer attaining the largest mass anywhere on the nonnegative integers. The theorem does not mean the probability mass function is unimodal: local peaks, and two nonconsecutive global modes, are allowed.

In particular, for \(0<\lambda\le2\), no three distinct indices in \(\{0,\ldots,k(k+1)\}\) have the same probability mass. For \(\lambda>2\), the distribution is strictly log-concave, a consequence of a published general theorem [4]. The low-intensity assertion is an exhaustive exact algebraic computation with a self-contained verifier.

## Assumptions and scope

The order is an integer \(2\le k\le8\); all component Poisson rates are the same strictly positive real number \(\lambda\). The variables are independent. No restriction to integer, rational, generic, or sampled intensities is made. The primary classification is 60E05. The originating publicly dated research direction is [1], whose first arXiv version appeared 2023-09-23.

Write
\[
 h_{k,n}(t)=[z^n]\exp\!\left(t\sum_{j=1}^{k}z^j\right),\qquad H_{k,n}(t)=n!h_{k,n}(t).
\]
Then \(\Pr(X_{k,\lambda}=n)=e^{-k\lambda}h_{k,n}(\lambda)\), and \(H_{k,n}\in\mathbb Z[t]\). All infinite-support arguments are analytic; only a finite polynomial identity is computer checked.

## Proof

**1. Coefficient recurrence and mode localization.** Differentiating the generating function gives, for \(n\ge1\),
\[
 n h_{k,n}(t)=t\sum_{j=1}^{\min(k,n)}j h_{k,n-j}(t),\qquad h_{k,0}=1,
\]
with negative-index terms understood as zero. In integer-coefficient normalization this is
\[
 H_{k,0}(t)=1,\quad
 H_{k,n}(t)=t\sum_{j=1}^{\min(k,n)}
 j\frac{(n-1)!}{(n-j)!}H_{k,n-j}(t).
\]
For every positive \(t\), a global modal index \(m\ge1\) satisfies \(h_{k,m-j}(t)\le h_{k,m}(t)\). Applying the recurrence at \(m\) and cancelling its positive mass yields
\[
 m\le t\sum_{j=1}^{k}j=t\,\frac{k(k+1)}2.
\]
The same bound trivially holds for the possible mode \(m=0\). Hence whenever \(0<t\le2\) all modal indices belong to the **finite** integer range \(0\le m\le N_k=k(k+1)\), including the equality endpoint \(t=2\).

**2. The large-rate region is already covered by a known strict log-concavity theorem.** Regard the law as a compound Poisson distribution with total jump intensity \(\Lambda=kt\) and a uniform jump law \(Q(j)=1/k\) for \(1\le j\le k\). The size-biased jump law \(Q^{\#}\) is supported on \(\{0,\ldots,k-1\}\) with masses proportional to \(j+1\), and is log-concave; the jump law \(Q\) itself is log-concave. Furthermore
\[
 \Lambda Q(1)^2>2Q(2)\quad\Longleftrightarrow\quad t>2.
\]
The strict version of the compound-Poisson log-concavity criterion in Johnson, Kontoyiannis and Madiman [4, Section 7, building on Theorem 5.5 and Hansen's identity] implies \(p_n^2>p_{n-1}p_{n+1}\) for every integer \(n\ge1\) whenever \(t>2\), where \(p_n=\Pr(X_{k,t}=n)>0\). Strictly decreasing adjacent mass ratios preclude three distinct global maxima. This step is **not** a new log-concavity result.

**3. Complete algebraic exclusion in the low-rate region.** Fix an order \(k\) and \(N=N_k\). For each \(0\le i<j\le N\), set
\[
 F_{k;i,j}(t)=j!H_{k,i}(t)-i!H_{k,j}(t)
 =i!j!\bigl(h_{k,i}(t)-h_{k,j}(t)\bigr)\in\mathbb Z[t].
\]
Its degree is \(j\) and its leading coefficient is \(-i!\). Remove all *exact integer-polynomial* factors of \(t\), obtaining \(\widetilde F_{k;i,j}\); this does not change its nonzero complex roots. Reduce the remaining coefficients modulo the prime \(p=1000003\), which exceeds \(N\) for all seven orders, so \(-i!\not\equiv0\pmod p\) and the degree is preserved.

For every triple \(0\le i<j<\ell\le N\), compute the monic Euclidean gcd over \(\mathbb F_p[t]\) of the reductions of \(\widetilde F_{k;i,j}\) and \(\widetilde F_{k;i,\ell}\). The enclosed `verify.py` recomputes every coefficient *over the integers before reduction*, every reduced polynomial, and every Euclidean gcd, using only the Python standard library. There are exactly
\[
 \binom{7}{3}+\binom{13}{3}+\binom{21}{3}+\binom{31}{3}+\binom{43}{3}+\binom{57}{3}+\binom{73}{3}
 =109943
\]
triple comparisons. Every gcd equals \(1\), **except** for the triple \((i,j,\ell)=(1,3,4)\) for each \(k\in\{4,5,6,7,8\}\), where the monic gcd is \(t+6\).

**4. Why the modular calculation is an exact characteristic-zero proof.** For integer polynomials whose leading coefficients remain nonzero modulo a prime, any nonconstant common factor over \(\mathbb Q[t]\) remains nonconstant and common after reduction: clear denominators, use primitive integer factorizations and Gauss's lemma, and observe that the leading coefficients of each integer factor cannot vanish modulo \(p\) when the product's leading coefficient is a unit. Consequently, a constant finite-field gcd forbids *every* nonzero complex common root in characteristic zero. A linear finite-field gcd restricts the rational gcd to degree at most one.

For the five exceptional cases, the exact coefficient identities valid whenever \(k\ge4\) are
\[
 h_{k,3}(t)-h_{k,1}(t)=\frac{t^2(t+6)}6,\qquad
 h_{k,4}(t)-h_{k,1}(t)=\frac{t^2(t+6)^2}{24}.
\]
Their only common nonzero root is \(t=-6\), which is not a positive intensity. Therefore no three distinct masses among \(0,\ldots,N\) are equal for \(t>0\), and in particular there cannot be three global modes when \(0<t\le2\). Together with Step 2 this proves the theorem for **every** \(t>0\) and all eight stated orders.

## Verification

Run `python3 verify.py` in this directory (Python standard library only). The script checks that each polynomial has the prescribed degree and leading coefficient, strips only *exact* powers of the parameter before modular reduction, and exhausts all \(109943\) index triples. The seven reported orderwise comparison counts are \(35,286,1330,4495,12341,29260,62196\), respectively. The script also verifies both exact identities isolating the exceptional negative root. Its successful output is `PASS: 109943 exact modular triple-gcd tests across orders 2..8`. The mathematical deduction from modular gcds and the strict large-rate theorem are proved/explained above; no numerical scan of real parameters is used as proof.

## Relationship to prior work

Mane [1] identifies the exclusion of three or more joint global modes as an **open question** and gives numerical evidence, not a proof; local peaks are distinguished from joint global modes. Kwon and Philippou [2] rigorously treat selected modes of orders \(3,4\) in \(0<\lambda<1\), and list computational mode intervals for orders \(2,3,4\) up to intensity \(2\), not an exact all-intensity triple-mode theorem. Georghiou, Philippou and Saghafi [3] proved an all-order mode upper bound and specified unique modes at **integer** intensities for orders \(2\) through \(5\). Theorem 5.5 and Section 7 of Johnson, Kontoyiannis and Madiman [4] already cover the strictly log-concave large-intensity regime for these uniform-jump compound Poisson distributions. The new content is the finite, exact low-rate triple-coincidence exclusion for the first eight orders, coupled with these existing theorems to obtain the global statement.

## Limitations

This does not settle the three-joint-mode problem for orders \(k\ge9\), classify the actual two-mode transition parameters, remove the equal-intensity hypothesis, give a simple symbolic argument uniform in \(k\), or prove global unimodality. The new finite-range statement is computationally certified by an explicitly reproducible exact modular calculation rather than by a short paper-and-pencil enumeration. Prioritization is based on inspected literature and targeted searches; a previously published equivalent statement under another name remains possible. Independent audit has not been performed.

## References

[1] S. R. Mane, *Structure of the probability mass function of the Poisson distribution of order k*, arXiv:2309.13493v1 (first public version 2023-09-23), https://arxiv.org/html/2309.13493v1.

[2] Y. Kwon and A. N. Philippou, *The Modes of the Poisson Distribution of Order 3 and 4*, Entropy 25 (2023), article 699, doi:10.3390/e25040699, https://doi.org/10.3390/e25040699.

[3] C. Georghiou, A. N. Philippou and A. Saghafi, *On the Modes of the Poisson Distribution of Order k*, Fibonacci Quarterly 51 (2013), 44–48, https://www.mathstat.dal.ca/FQ/Papers1/51-1/GeorghiouPhilippouSaghafi.pdf.

[4] O. Johnson, I. Kontoyiannis and M. Madiman, *Log-concavity, ultra-log-concavity, and a maximum entropy property of discrete compound Poisson measures*, Discrete Applied Mathematics 161 (2013), 1232–1250, arXiv:0912.0581v2, https://arxiv.org/pdf/0912.0581.
