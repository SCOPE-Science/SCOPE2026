# The \(k=13\) case of Chu's divisor-function conjecture for even perfect numbers

## Finding
For a positive integer \(m\), write
\[
\sigma_{13}(m)=\sum_{d\mid m}d^{13}.
\]
Let
\[
n=2^{\alpha-1}p^{\beta-1},
\qquad \alpha,\beta>1,
\]
where \(p\) is an odd prime satisfying
\[
p<3\cdot2^{\alpha-1}-1.
\]
Then
\[
n\mid\sigma_{13}(n)
\]
if and only if \(n\) is an even perfect number different from
\[
2^{12}(2^{13}-1)=2^{12}\cdot8191.
\]

Thus the \(k=13\) instance of Chu's Conjecture 1.5 holds.

## Assumptions and scope
Chu's 2020 preprint, later published in the *Journal of Integer Sequences*, proves the corresponding statement for \(\beta=2\) for every prime \(k>2\) such that \(2^k-1\) is a Mersenne prime, and proves the full \(\beta>1\) statement for \(k=5\). It states the full assertion for general such \(k\) as Conjecture 1.5. The proof below specializes Chu's general preliminary lemmas to \(k=13\), for which
\[
2^{13}-1=8191
\]
is prime.

No assertion is made here about arbitrary integers outside the form \(2^{\alpha-1}p^{\beta-1}\), nor about exponents \(k\) for which \(2^k-1\) is composite.

## Proof
Put
\[
M=2^{13}-1=8191,
\qquad
S_\alpha=\sigma_{13}(2^{\alpha-1})
=\frac{2^{13\alpha}-1}{8191}.
\]
Assume first that
\[
n\mid\sigma_{13}(n).
\]
Since
\[
\sigma_{13}(p^{\beta-1})\equiv1\pmod p,
\]
multiplicativity gives
\[
p^{\beta-1}\mid S_\alpha.
\tag{1}
\]
Also \(\sigma_{13}(p^{\beta-1})\) is a sum of \(\beta\) odd terms and is divisible by \(2^{\alpha-1}\), with \(\alpha>1\). Hence \(\beta\) is even. Write
\[
\beta=2^v b,
\qquad b\ \text{odd},\quad v\ge1.
\]

### Case 1: \(p\equiv1\pmod4\)

Chu's Lemma 4.2, valid for the general exponent \(k\), gives after setting \(k=13\)
\[
\alpha\le v+1
\tag{2}
\]
and
\[
p^{2^v-1}
\le
\frac{2^{13(v+1)}-1}{8191}.
\tag{3}
\]
Since \(p\ge5\), inequality (3) fails at \(v=5\):
\[
5^{31}>
\frac{2^{78}-1}{8191}.
\]
It then fails for every larger \(v\). Indeed, increasing \(v\) by one multiplies the left lower bound by \(5^{2^v}\), while the right side is multiplied by less than \(8193\). Therefore
\[
1\le v\le4.
\]

The remaining range is finite by (2) and the hypothesis on \(p\). Exact enumeration, deliberately allowing composite values as well as primes so that no primality test is needed, finds no divisor of \(S_\alpha\) in the required residue class for \(v=1,2\). For \(v=3,4\), the only pair \((\alpha,p)\) with \(p\equiv1\pmod4\), \(p<3\cdot2^{\alpha-1}-1\), and \(p\mid S_\alpha\) is
\[
(\alpha,p)=(4,5),
\]
and
\[
\nu_5(S_4)=1.
\]
But (1) requires
\[
\nu_p(S_\alpha)\ge\beta-1\ge2^v-1,
\]
which is at least \(7\) for \(v=3\). This is impossible.

### Case 2: \(p\equiv3\pmod4\)

Chu's Lemma 4.3 gives
\[
p^{2^v-27}
<
\frac{2^{13(v-1)}}{8191}.
\tag{4}
\]
If \(v=6\), the lower bound \(p\ge3\) already yields
\[
3^{37}>
\frac{2^{65}}{8191}.
\]
For larger \(v\), the left lower bound gains a factor \(3^{2^v}\) at each step, whereas the right side gains only \(2^{13}\). Hence
\[
1\le v\le5.
\tag{5}
\]

Write
\[
p+1=2^\lambda q,
\qquad q\ \text{odd}.
\]
The valuation step in Chu's Lemma 4.4 gives
\[
\alpha\le\lambda+v.
\tag{6}
\]

First consider the denominator prime \(p=8191\). Here \(\lambda=13\), so (5)--(6) give \(\alpha\le18\). By LTE,
\[
\nu_{8191}(S_\alpha)=\nu_{8191}(\alpha)=0
\]
in this range, contradicting (1). Thus \(p\ne8191\).

If \(\alpha\le v\), then (5) and the size hypothesis leave a finite range, which is included in the exact enumeration below. Suppose now that
\[
\alpha>v.
\]
Set
\[
m=\alpha-v\ge1.
\]
By (6), \(m\le\lambda\), so
\[
t=\frac{p+1}{2^m}
\]
is a positive integer. Thus
\[
p=t2^m-1.
\tag{7}
\]
The size hypothesis gives
\[
t<3\cdot2^{v-1},
\tag{8}
\]
and, because \(p\mid S_\alpha\) and \(p\ne8191\),
\[
2^{13\alpha}\equiv1\pmod p.
\]
Multiplying the identity \(2^\alpha=2^{v+m}\) by \(t\) and using (7) gives
\[
t2^\alpha=2^v(p+1)\equiv2^v\pmod p.
\]
Raising to the thirteenth power yields
\[
p\mid 2^{13v}-t^{13}.
\tag{9}
\]

If \(t=2^v\), then (7) becomes
\[
p=2^\alpha-1.
\]
For \(p\ne8191\), LTE gives
\[
\nu_p(S_\alpha)=1.
\]
Therefore (1) forces \(\beta-1\le1\), so \(\beta=2\) and \(v=1\). In this case \(n=2^{\alpha-1}(2^\alpha-1)\) is an even perfect number.

It remains to exclude \(t\ne2^v\). Then
\[
D_{v,t}=2^{13v}-t^{13}
\]
is nonzero. Equations (7) and (9) imply
\[
t2^m-1=p\le |D_{v,t}|,
\]
hence
\[
2^m\le\frac{|D_{v,t}|+1}{t}.
\tag{10}
\]
Together, (5), (8), and (10) give a completely explicit finite enumeration.

The exact checker over-enumerates by allowing composite \(p\), so every prime candidate is certainly included. Among candidates satisfying \(p\equiv3\pmod4\), the size hypothesis, and \(p\mid S_\alpha\), the maximum exponent
\[
u=\max\{e:p^e\mid S_\alpha\}
\]
is as follows:
\[
\begin{array}{c|ccccc}
v&1&2&3&4&5\\ \hline
\max u&0&1&1&2&2.
\end{array}
\]
For \(v\ge2\),
\[
\beta-1\ge2^v-1\ge3>\max u,
\]
contradicting (1). For \(v=1\), the non-special enumeration is empty, so only the already treated \(t=2^v\) branch survives. Thus the forward implication forces \(\beta=2\) and \(n\) to be even perfect.

For the reverse implication, Chu's Theorem 1.3 applies directly at \(k=13\): every even perfect number in the stated size setting satisfies the divisibility except
\[
2^{12}(2^{13}-1).
\]
This completes the proof.

## Verification
The accompanying `verify.py` uses only exact integer arithmetic. It checks the two growth cutoffs, exhaustively verifies the finite \(p\equiv1\pmod4\) range, and executes the finite reduction (5), (8), (10) in the \(p\equiv3\pmod4\) branch. The enumeration intentionally admits composite \(p\); this enlarges the candidate set and therefore cannot discard a prime solution.

The script also checks the listed maximal divisibility exponents and prints `VERIFY_OK`. The infinite Mersenne branch is handled symbolically in the proof by LTE, not by a finite experiment.

## Relationship to prior work
Chu's paper proves Conjecture 1.5 for \(k=5\) and the \(\beta=2\) slice for every relevant prime \(k\), while explicitly presenting the full \(\beta>1\) statement as a conjecture. A later published result proves the \(k=7\) case by specializing Chu's general lemmas and a finite exact reduction. That result explicitly notes that it does not settle \(k=13,17,19,\ldots\).

Searches using the exact conjecture, the paper title and author, `sigma_13`, “thirteenth powers of divisors,” the form \(2^{\alpha-1}p^{\beta-1}\), and the divisibility \(n\mid\sigma_{13}(n)\) did not locate a published proof of the \(k=13\) case. The closest sources were Chu's original conjecture, the \(k=7\) result, and sequence/database pages listing values of \(\sigma_{13}\)-divisibility without this structural theorem.

## Limitations
This proves only the \(k=13\) instance of Chu's broader conjecture. It does not settle the cases \(k=17,19,\ldots\).

The finite step is computer-assisted, although it is an exact exhaustive check over ranges proved finite before computation. The originality assessment is based on targeted searches and source inspection; an unindexed result could still exist.

## References
1. H. V. Chu, “On Even Perfect Numbers II,” arXiv:2001.08633v1, 17 January 2020; published as “Divisibility of Divisor Functions of Even Perfect Numbers,” *Journal of Integer Sequences* 24 (2021), Article 21.3.4.
2. “The \(k=7\) case of Chu's divisor-sum conjecture for even perfect numbers,” published mathematical record, 20 September 2026.
