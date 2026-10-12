# The full coefficient spectrum of generalized alternating divisor sums

## Finding

Let \(\mathcal P\) denote the primes. For **every** subset \(Q\subseteq\mathcal P\), including infinite sets and the empty set, put
\[
 t_Q(n)=\begin{cases}1,&p\nmid n\text{ for every }p\in Q,\\-1,&\text{otherwise},\end{cases}
 \qquad S_Q(X)=\sum_{1\le n\le X}t_Q(n)\sigma(n),
\]
where \(\sigma(n)=\sum_{d\mid n}d\) and \(X\) tends to infinity through real values. Define the convergent, possibly zero, product
\[
 P_Q=\prod_{p\in Q}\left(1-\frac1p\right)\left(1-\frac1{p^2}\right),
\]
where any infinite product is the decreasing limit over the primes in \(Q\). Then the unrestricted limit exists and is
\[
 \boxed{\lim_{X\to\infty}\frac{S_Q(X)}{X^2}=\frac{\pi^2}{12}(2P_Q-1).}
\]
The full spectrum of these limits, as \(Q\) ranges over **all** subsets of primes, is exactly the interval
\[
 \boxed{\left[-\frac{\pi^2}{12},\frac{\pi^2}{12}\right].}
\]
In fact every value is realized by a set \(Q\) containing **only odd primes**, and coefficients arising from finite \(Q\) are dense in the interval. Nonetheless **no finite** \(Q\) produces zero coefficient, whereas the explicitly specified greedy infinite set of odd primes below does:
\[
 \boxed{P_Q=\frac12,\qquad S_Q(X)=o(X^2).}
\]
Thus cancellation of the complete quadratic main term is an attainable but necessarily infinite-prime phenomenon.

## Assumptions and scope

The theorem has no regularity, density, or reciprocal-summability hypothesis on \(Q\). All products and sums are over positive integers and rational primes. A finite set may be empty. The normalizing exponent is exactly \(2\), and the conclusion asserts an ordinary limit, not merely a limit superior or logarithmic average. The set \(Q\) is fixed while \(X\to\infty\); choosing \(Q\) as a function of \(X\) is not covered.

## Proof

**1. Finite prime sets.** Write \(c_Q(n)=(1+t_Q(n))/2\), the indicator that \(n\) is divisible by none of the primes in \(Q\). Suppose first that \(Q\) is finite, of size \(k\), and write \(\alpha_Q=\prod_{p\in Q}(1-p^{-1})\). Inclusion–exclusion gives
\[
 C_Q(T):=\sum_{n\le T}c_Q(n)=\alpha_QT+O(2^k),
\]
for every real \(T\ge1\), with an absolute implied constant. Partial summation therefore yields
\[
 A_Q(T):=\sum_{n\le T}n c_Q(n)=\frac{\alpha_Q}{2}T^2+O(2^kT).
\]
Because \(c_Q(ab)=c_Q(a)c_Q(b)\) and \(\sigma(n)=\sum_{d\mid n}d\),
\[
 F_Q(X):=\sum_{n\le X}c_Q(n)\sigma(n)
 =\sum_{r\le X}c_Q(r) A_Q(X/r).
\]
Hence
\[
 F_Q(X)=\frac{\alpha_Q X^2}{2}\sum_{r\le X}\frac{c_Q(r)}{r^2}
 +O\left(2^k X\sum_{r\le X}\frac1r\right).
\]
The convergent Dirichlet series satisfies
\[
 \sum_{r\ge1}\frac{c_Q(r)}{r^2}
 =\zeta(2)\prod_{p\in Q}(1-p^{-2}).
\]
Replacing its truncation by the full series costs \(O(X)\), because \(\sum_{r>X}r^{-2}=O(1/X)\). Thus
\[
 F_Q(X)=\frac{\zeta(2)}2 P_QX^2+O(2^kX\log(2X)).
\]
In particular, taking \(Q=\varnothing\) gives
\[
 \sum_{n\le X}\sigma(n)=\frac{\zeta(2)}2 X^2+O(X\log(2X)).
\]
The identity \(S_Q(X)=2F_Q(X)-\sum_{n\le X}\sigma(n)\) proves the stated formula for every finite \(Q\).

**2. Uniform control of primes omitted from a finite truncation.** For every prime \(p\) and positive integer \(m\), multiplicativity and the prime-power geometric series give
\[
 \sigma(pm)\le(p+1)\sigma(m).
\]
Indeed, when \(p^a\) exactly divides \(m\), the ratio \(\sigma(p^{a+1})/\sigma(p^a)\) equals \(p+(p-1)/(p^{a+1}-1)\), which is at most \(p+1\). Also, directly from the divisor-pair count,
\[
 \sum_{m\le T}\sigma(m)=\sum_{d\le T}d\lfloor T/d\rfloor\le T^2
\]
for all real \(T\ge1\). For any \(Q\), let \(Q_{\le Y}=\{p\in Q:p\le Y\}\). Positivity and the union bound give
\[
 \begin{aligned}
 0\le F_{Q_{\le Y}}(X)-F_Q(X)
 &\le\sum_{\substack{p\in Q\\p>Y}}\sum_{m\le X/p}\sigma(pm)\\
 &\le X^2\sum_{\substack{p\in Q\\p>Y}}\frac{p+1}{p^2}
 \le 2X^2\sum_{\substack{p\in Q\\p>Y}}\frac1p.
 \end{aligned}
\]
The bound remains valid if its right side is infinite, although it is useful quantitatively when that prime-reciprocal tail is finite.

**3. Passage to arbitrary sets.** If \(\sum_{p\in Q}p^{-1}<\infty\), the inequality in Step 2 makes the normalized difference between \(F_Q(X)\) and \(F_{Q_{\le Y}}(X)\) uniformly small as \(Y\to\infty\). Step 1 supplies the limit for each finite truncation. The finite Euler factors converge to \(P_Q\), so
\[
 \lim_{X\to\infty}\frac{F_Q(X)}{X^2}=\frac{\zeta(2)}2P_Q.
\]
If instead \(\sum_{p\in Q}p^{-1}=\infty\), then the factors obey \((1-p^{-1})(1-p^{-2})\le1-p^{-1}\), whence \(P_{Q_{\le Y}}\to0\). By positivity,
\[
 0\le F_Q(X)\le F_{Q_{\le Y}}(X).
\]
Taking first the upper limit as \(X\to\infty\) and then \(Y\to\infty\) proves \(F_Q(X)=o(X^2)\). The same limit formula therefore holds with \(P_Q=0\). In both cases, combine it with \(S_Q=2F_Q-\sum\sigma\) and \(\zeta(2)=\pi^2/6\).

**4. Attainable spectrum and the critical construction.** For each odd prime \(p\), put
\[
 f_p=(1-p^{-1})(1-p^{-2})\in(0,1).
\]
The factors satisfy \(f_p\to1\) and \(\prod_{p\ge3}f_p=0\), the latter by Euler's divergence of the sum of prime reciprocals (the omission of \(2\) does not matter). Fix any \(t\in(0,1)\). Scan the odd primes in increasing order, beginning with a running product \(u=1\). Include \(p\) in \(Q_t\) exactly when replacing \(u\) by \(uf_p\) leaves \(uf_p\ge t\); otherwise skip \(p\). Every partial product stays at least \(t\), so it tends to a limit \(L\ge t\). If \(L>t\), then for all sufficiently large odd primes \(p\), the closeness \(f_p\to1\) implies \(uf_p\ge t\). The algorithm would include every sufficiently large prime, forcing its product to zero, a contradiction. Hence \(L=t\). For \(t=1\), take \(Q=\varnothing\); for \(t=0\), take all odd primes. Thus every \(P_Q\in[0,1]\) occurs, and the normalized signed coefficient fills the asserted interval. Finite partial sets of the greedy choices show that finite-set coefficients are dense there.

Finally, take \(t=1/2\). If a finite \(Q\) includes \(2\), then \(P_Q\le f_2=3/8<1/2\). If a finite \(Q\) consists only of odd primes, then
\[
 P_Q=\prod_{p\in Q}\frac{(p-1)^2(p+1)}{p^3}
\]
is a rational number admitting an **odd** denominator, so it cannot equal \(1/2\). Therefore the greedy set \(Q_{1/2}\) necessarily has infinitely many elements, and no finite set attains its zero signed coefficient. This establishes all assertions.

## Verification

The standalone `verify.py` performs exact rational checks of the local factors and of finite greedy products at targets \(1/4\), \(1/2\), and \(3/4\); it checks \(\sigma(pm)\le(p+1)\sigma(m)\) on finite inputs and compares complete signed sums through \(X=30000\) with the analytic leading constants for five finite prime sets. The recorded command is `python3 verify.py`, with its actual output in `verification_output.txt`. These tests are not an infinite proof: Steps 1–4 supply that proof independently.

## Relationship to prior work

Tóth [1, Theorem 57 and Open Problem 58] proved the corresponding asymptotic for finite \(Q\) and explicitly asked for arbitrary fixed prime subsets. His Proposition 56 gives a Dirichlet-series identity for arbitrary \(Q\), but not the unrestricted ordinary summatory asymptotic. Zurita [2, Theorem 4] reproved and developed the finite-prime-set framework for the sum-of-divisors function; the paper's scope and theorem continue to require \(Q\) finite. The advance here is the ordinary \(X^2\)-scale limit for **all** infinite prime sets, including divergent reciprocal sums, plus the complete coefficient range and the finite-versus-infinite zero-cancellation distinction. The finite-set formula itself is not claimed as new.

## Limitations

The \(o(X^2)\) statement at the critical infinite set does not provide a universal rate. For sets with \(\sum_{p\in Q}1/p<\infty\), Step 2 gives a quantitative prime-tail approximation; in the divergent case the proof uses a two-stage limit instead. The theorem concerns \(\sigma\), not every other multiplicative function mentioned in Tóth's wider problem. Computational tests cover finite samples only. No independent verification or publication-priority adjudication is asserted here.

## References

[1] László Tóth, *Alternating Sums Concerning Multiplicative Arithmetic Functions*, Journal of Integer Sequences **20** (2017), Article 17.2.1, §5, Proposition 56, Theorem 57, Open Problem 58. https://cs.uwaterloo.ca/journals/JIS/VOL20/Toth/toth25.pdf

[2] Rimer Zurita, *Generalized Alternating Sums of Multiplicative Arithmetic Functions*, Journal of Integer Sequences **23** (2020), Article 20.10.4, Theorem 4, published October 17, 2020. https://cs.uwaterloo.ca/journals/JIS/VOL23/Zurita/zur3.pdf
