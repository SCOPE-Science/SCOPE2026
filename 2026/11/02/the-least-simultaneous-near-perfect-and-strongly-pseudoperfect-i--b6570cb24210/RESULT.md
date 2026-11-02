# The least simultaneous near-perfect and strongly pseudoperfect integer

## Finding

The least positive integer that is both near-perfect and strongly pseudoperfect is
\[
\boxed{174592=2^{9}\cdot 11\cdot 31}.
\]
In particular, a simultaneous example exists, affirmatively answering Question 42 of McCormack and Zelinsky [1]. The assertion of leastness is over **every positive integer**, not only those with a specified factorization or parity.

## Assumptions and scope

For a positive integer \(n\), let \(\sigma(n)=\sum_{d\mid n}d\). Following [1,3], call \(n\) **near-perfect** if there exists a proper positive divisor \(e\mid n\), \(1\le e<n\), with \(\sigma(n)=2n+e\). This is equivalent to expressing \(n\) as the sum of all its proper positive divisors except \(e\).

Call \(n\) **strongly pseudoperfect** [1,2] if some subset \(S\) of its positive divisors satisfies both
\[
\sum_{d\in S}d=2n,\qquad
\bigl(d\in S\iff n/d\in S\bigr)
\quad\text{for every }d\mid n.
\]
Unlike ordinary pseudoperfectness, the latter requires closure under complementary divisors. The statement concerns the intersection of these two precise classes; it does not assert either class is finite.

## Proof

**Direct existence.** Put \(N=174592=2^{9}\cdot11\cdot31\). Multiplicativity of \(\sigma\) yields
\[
\sigma(N)=(2^{10}-1)(11+1)(31+1)
=1023\cdot12\cdot32=392832
=2N+43648.
\]
Since \(43648=N/4\) is a proper divisor, \(N\) is near-perfect.

For strong pseudoperfectness, take \(S\) to be the union of the following nine *complete complementary divisor pairs* (the entries in each pair multiply to \(N\)):
\[
\begin{aligned}
&(1,174592),\ (2,87296),\ (4,43648),\\
&(8,21824),\ (22,7936),\ (31,5632),\\
&(32,5456),\ (124,1408),\ (176,992).
\end{aligned}
\]
All eighteen entries are distinct divisors, and their exact sum is \(349184=2N\). Including both members of every pair makes \(S\) complementary-divisor-closed. Thus \(N\) is strongly pseudoperfect.

**Exhaustive minimality.** For any \(2\le n\le N\), near-perfectness is equivalent to the three exact integer tests
\[
0<e_n:=\sigma(n)-2n<n,\qquad e_n\mid n.
\]
The attached `verify_near_strong_overlap.py` enumerates every such \(n\) with a complete divisor-sum sieve: it initializes \(\sigma(n)=0\) and adds each divisor \(d\) to every multiple of \(d\) through \(N\). Exactly 37 integers pass the near-perfect test:

\(12,18,20,24,40,56,88,104,196,224,234,368,464,650,992,1504,1888,1952,3724,5624,9112,11096,13736,15376,15872,16256,17816,24448,28544,30592,32128,77744,98048,122624,128768,130304,174592\).

For each candidate, let \(w_1,\ldots,w_r\) be the weights of the complementary-divisor orbits: \(d+n/d\) for the smaller divisor \(d<\sqrt n\), and the singleton weight \(\sqrt n\) if \(n\) is square. A subset of divisors is complementary-divisor-closed **if and only if** it is the union of some of these disjoint orbits. Consequently, strong pseudoperfectness is equivalent to a subset of \(w_1,\ldots,w_r\) summing to \(2n\).

The verifier computes the entire attainable-sum set exactly by the recursion \(B_0=\{0\}\), \(B_{j+1}=B_j\cup\{s+w_{j+1}:s\in B_j\}\), retaining only sums at most \(2n\); binary-integer bitsets implement that recursion without approximation. Among all 37 candidates it finds the single successful value \(N\). These operations exhaust every positive integer below \(N\); neither a probabilistic primality test nor an unproved search heuristic is used. Hence \(N\) is the least simultaneous example.

## Verification

Run, with Python 3 and no dependencies outside the standard library:

```sh
python3 verify_near_strong_overlap.py
```

Expected exact output:

```text
VERIFY_OK limit=174592 near_candidates=37 intersection=[174592] factorization=2^9*11*31 sigma=392832 redundant_divisor=43648 included_orbits=9 included_divisors=18
```

The script independently reconstructs the divisor list of each near-perfect candidate, cross-checks it against the divisor-sum sieve, verifies all nine explicit complementary pairs and their sum, and performs exhaustive subset-sum tests for every near-perfect candidate in the full interval. The finiteness of this bounded classification is part of the theorem; no finite test is extrapolated to an unbounded assertion.

## Relationship to prior work

McCormack and Zelinsky [1], Section 4, explicitly posed as Question 42 whether a number can be both near-perfect and strongly pseudoperfect; they distinguished this from the possibility of a perfect-square near-perfect number whose omitted divisor equals its square root (Question 40). The example here is **not** square and answers Question 42 directly, without answering Question 40.

Wang and Zelinsky [2] subsequently studied strong pseudoperfectness, giving constructions and restrictions, but the inspected text does not exhibit the present simultaneous example or establish its leastness. The integer \(174592\) already appears in the **near-perfect** table OEIS A181595 [3]; its occurrence in that table alone does not establish strong pseudoperfectness. The strong-pseudoperfect sequence A334405 [4] supplies the definition and a table ending at \(30324\), below the present witness. The result claimed here is therefore **the intersection and its least element**, not the original discovery of \(174592\) as a near-perfect number.

## Limitations

The result gives one simultaneous example and its leastness. It does not determine whether infinitely many such integers exist, nor classify all joint examples, nor answer the distinct square-root-omission question. Priority is assessed against explicitly inspected primary literature and mathematical records; an unindexed equivalent result remains a bibliographic possibility.

## References

1. T. McCormack and J. Zelinsky, *Weighted Versions of the Arithmetic-Mean-Geometric Mean Inequality and Zaremba's Function*, arXiv:2312.11661, first public version 2023-12-18, Section 4, Questions 40–42. https://arxiv.org/abs/2312.11661
2. A. Wang and J. Zelinsky, *Strongly Pseudoperfect Numbers*, arXiv:2609.36068, first posted 2026-09-28, Sections 1–5. https://arxiv.org/abs/2609.36068
3. OEIS A181595, *Abundant numbers with proper-divisor abundance* (near-perfect numbers). https://oeis.org/A181595
4. OEIS A334405, *Strongly pseudoperfect numbers*; see also its first 1650 terms. https://oeis.org/A334405 and https://oeis.org/A334405/b334405.txt
