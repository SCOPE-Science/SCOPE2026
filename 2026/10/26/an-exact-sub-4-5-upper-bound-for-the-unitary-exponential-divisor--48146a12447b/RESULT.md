# An exact sub-\(4/5\) upper bound for the unitary–exponential divisor comparison density

## Finding
Let \(\sigma^*(n)\) be the sum of unitary divisors and \(\sigma^{(e)}(n)\) the sum of exponential divisors. For the natural density
\[
\delta=\lim_{x\to\infty}\frac{1}{x}\#\{1\le n\le x:\sigma^*(n)>\sigma^{(e)}(n)\},
\]
which is known to exist, the following explicit upper bound holds:
\[
\boxed{\delta\le
\frac{72112510149983208955226454671586496051993960400}{90371142966099382141679202663485100000000000000}
=0.797959478913\ldots<\frac45.}
\]
The displayed decimal is informational; the finite exact-rational inequality is the certificate. This gives an upper bound close to the reported finite-range proportion \(0.778307\) and complements the published explicit lower bound \(0.753659844064288\ldots\).

## Assumptions and scope
For a prime \(p\), let \(v_p(n)\) be its exponent in \(n\), and define \(\rho_p(0)=1\) and, for every positive integer \(a\),
\[
\rho_p(a)=\frac{1+p^a}{\sum_{d\mid a}p^d}.
\]
Both divisor-sum functions are multiplicative, so their ratio is \(\prod_p\rho_p(v_p(n))\). At exponent one, \(\rho_p(1)=1+1/p\); at any exponent at least two, \(0<\rho_p(a)<1\). The head primes are \(P=\{2,3,5,7,11,13,17\}\). For each such prime, the disjoint exponent states are \(a=0,1,\ldots,6\) and \(a\ge7\). There are exactly \(8^7=2,097,152\) states. All large exponents in the last state are replaced by the rigorous local upper bound \(1\); no distributional model is assumed for them.

## Proof
**1. Head–tail domination.** For an integer \(n\), define
\[
H(n)=\prod_{p\in P}h_p(v_p(n)),\qquad
h_p(a)=\begin{cases}\rho_p(a),&0\le a\le6,\\1,&a\ge7,\end{cases}
\]
and
\[
Z(n)=\prod_{\substack{p>17\\p\mid n}}(1+1/p).
\]
Every factor from a prime outside \(P\) is at most \(1+1/p\). Therefore
\[
\frac{\sigma^*(n)}{\sigma^{(e)}(n)}\le H(n)Z(n).
\]
For a fixed head exponent-state vector, the tail valuation indicators have, in natural-density moments, their independent prime-divisibility distribution: the probability that a prime \(p>17\) divides an integer is \(1/p\). This remains valid conditionally on any fixed head state by the Chinese remainder theorem. Absolute convergence of the relevant squarefree divisor expansions permits passage from finite prime sets to the full tail, giving
\[
\mathbb EZ=\prod_{p>17}(1+p^{-2}),\qquad
\mathbb EZ^2=\prod_{p>17}(1+2p^{-2}+p^{-3}).
\]
These conditional moments do not depend on the head state.

**2. Rational moment bounds.** Define the rational upper sums
\[
S_2=\sum_{17<p\le1000\atop p\text{ prime}}p^{-2}+\frac1{1000},\qquad
S_3=\sum_{17<p\le1000\atop p\text{ prime}}p^{-3}+\frac1{2\cdot1000^2}.
\]
The integral test bounds the omitted prime tails by the displayed final terms. Thus \(s_j=\sum_{p>17}p^{-j}\le S_j\) for \(j=2,3\). Since \(e^t\le(1-t)^{-1}\) when \(0\le t<1\),
\[
\mathbb E(Z-1)\le\frac{S_2}{1-S_2}<\frac{71}{5000}=:B_1.
\]
For the second moment, put \(a_p=1+p^{-2}\) and \(b_p=1+2p^{-2}+p^{-3}\). Since
\[
b_p=a_p^2+p^{-3}-p^{-4},
\]
we have \(\prod b_p\le(\prod a_p)^2e^{s_3}\), hence
\[
\begin{aligned}
\mathbb E(Z-1)^2
&=\operatorname{Var}(Z)+(\mathbb EZ-1)^2\\
&\le \frac{1}{(1-S_2)^2}
\left(\frac{S_3}{1-S_3}+S_2^2\right)
<\frac{31}{50000}=:B_2.
\end{aligned}
\]
The two strict rational inequalities involving \(S_2,S_3\) are checked exactly in the accompanying certificate, which sieves primes through \(1000\); neither floating-point estimates nor a numerical prime-tail truncation are used in the proof.

**3. Upper bound for each state.** If a head state has \(H\ge1\), assign conditional probability upper bound \(1\). If \(H=N/D<1\), with positive integers \(N,D\) not necessarily reduced, then the event \(\sigma^*(n)>\sigma^{(e)}(n)\) entails \(Z-1>D/N-1\). Applying Markov's inequality to the nonnegative variables \(Z-1\) and \((Z-1)^2\) yields
\[
\Pr(\sigma^*(n)>\sigma^{(e)}(n)\mid\text{head state})
\le \min\!\left\{1,\frac{B_1N}{D-N},\frac{B_2N^2}{(D-N)^2}\right\}.
\]
This inequality applies to limiting upper densities even without invoking the known existence of \(\delta\), by approximating the tail with finitely many primes and using the absolutely convergent first and second divisor-moment series.

**4. Exact finite sum.** Set \(M=10^7\) and \(Q=\prod_{p\in P}p^7\). For a prime \(p\in P\), a state \(a\le6\) has probability \((p-1)/p^{a+1}\) and integer weight \((p-1)p^{6-a}\) over denominator \(p^7\); the state \(a\ge7\) has probability \(p^{-7}\) and weight \(1\). The product of the seven weights is denoted \(w\). For every state with \(H=N/D<1\), set
\[
 b(H)=\min\!\left\{M,
\left\lceil\frac{71MN}{5000(D-N)}\right\rceil,
\left\lceil\frac{31MN^2}{50000(D-N)^2}\right\rceil\right\};
\]
for \(H\ge1\), set \(b(H)=M\). These are integer *upper* roundings. Exhaustive exact-integer enumeration of all \(8^7\) states gives
\[
\begin{aligned}
Q&=9037114296609938214167920266348510000000,\\
\sum w\,b(H)&=72112510149983208955226454671586496051993960400.
\end{aligned}
\]
Consequently \(\delta\le\sum w\,b(H)/(QM)\). The certificate explicitly checks the strict integer inequality \(5\sum w\,b(H)<4QM\), completing the proof.

## Verification
Run `python3 verify_density_bound.py` in a Python 3 environment. It uses only the standard library, recomputes the prime list and rational moment inequalities, constructs all local exponent states and their exact integer weights, enumerates \(2,097,152\) cases with integer products and ceiling divisions, and checks \(5\sum w\,b(H)<4QM\). A fresh execution returned `CERTIFICATE_OK`, `leaf_count 2097152`, and `certified_upper_decimal 0.797959478913`. Numerical decimals are not needed for the certificate. The proof of the infinite density inequality uses the analytic head–tail comparison and moment bounds, not an extrapolation from finite integers.

## Relationship to prior work
Tim Trudgian's *The sum of the unitary divisor function* (first public 2013-12-17) formulates the density problem, supplies the squarefree lower bound \(6/\pi^2\), observes a proportion about \(0.778307\) through \(10^9\), and notes existence of the density. A published later explicit prime-exponent cylinder construction strengthens the **lower** bound to \(0.753659844064288\ldots\). Neither lower bound nor a finite-range proportion implies any rigorous upper bound below \(4/5\). The present independent upper-bound argument uses a different, two-moment control of unrestricted large-prime tails and a complete finite head-state certificate. Related inequalities for each divisor-sum function separately do not compare the event's natural density.

## Limitations
This is an upper bound, not an exact evaluation of \(\delta\), and the selected head cutoff, moment inequalities, and integer ceiling grid are not optimized. The conditional moment argument does not prove any independence among the full arithmetic functions; only finite-prime CRT independence and absolutely convergent tail moments are used. Previously unindexed or inaccessible earlier upper estimates remain a publication-priority risk. No independent external audit has been performed.

## References
1. T. Trudgian, *The sum of the unitary divisor function*, arXiv:1312.4615v1, initially submitted 2013-12-17; later Publ. Inst. Math. (Beograd) 97 (111), 175–180; DOI 10.2298/PIM140617001T. Full text: https://arxiv.org/html/1312.4615v3 .
2. *An explicit \(0.753659844\ldots\) lower bound for the unitary–exponential divisor-sum comparison density*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-an-explicit-0-753659844-ldots-lower-bound-for-the-unitary-expone--831dd476bf82 . The complete `RESULT.md` was inspected for scope and implication comparison.
