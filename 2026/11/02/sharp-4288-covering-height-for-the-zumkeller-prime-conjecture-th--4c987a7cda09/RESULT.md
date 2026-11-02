# Sharp \(4288\) covering height for the Zumkeller--prime conjecture through \(10^9\)

## Finding

Call a positive integer *Zumkeller* if its complete set of distinct positive divisors can be divided into two disjoint sets with equal sums. Let \(Z\) denote these integers, and, for an odd integer \(n\ge9\), let
\[
h(n)=\min\{z\in Z : n-z\text{ is prime}\},
\]
where the minimum is \(+\infty\) if there is no representation. For an upper cutoff \(X\), define the natural extremal invariant on the unresolved progression by
\[
H(X)=\max_{39\le n\le X,\ n\equiv3\pmod{18}}h(n).
\]

**Theorem.** Every odd integer \(n\) with \(9\le n\le10^9\), other than \(21\), is a Zumkeller number plus a prime. More precisely,
\[
H(10^9)=4288,
\]
with the **unique** maximizing argument \(n_*=679570815\). A sharp witness is
\[
679570815=4288+679566527,
\]
where \(679566527\) is prime and \(4288=2^6\cdot67\) is Zumkeller. The exact auxiliary values \(H(10^5)=464\), \(H(10^6)=928\), \(H(10^7)=H(10^8)=2368\) also follow from the same exhaustive computation.

## Assumptions and scope

All numbers, divisors, primality tests and subset sums are ordinary positive integers; repeated use of a divisor is prohibited. The assertion concerns precisely \(39,57,75,\ldots,999999993\) in the hard progression, comprising \(55,555,554\) integers, and uses the previously proved treatment of the remaining odd residues. It is **not** an infinite verification of the conjecture. The algorithm uses exact integer arithmetic, an exhaustive divisor-subset decision procedure and a complete sieve of odd primes through \(10^9\).

## Proof

**Step 1: exact Zumkeller decision.** For each even positive integer \(z\le4288\), list every divisor by testing all positive \(d\le z\). Put \(S=\sigma(z)\). A balanced partition necessarily places \(z\) in one class, so \(z\) is Zumkeller **if and only if** \(S\) is even, \(S\ge2z\), and
\[
S/2-z
\]
is a sum of *distinct proper* divisors of \(z\). Initialize the reachable sums to \(\{0\}\). For each proper divisor \(d\) add the previously reachable values shifted by \(d\), retaining only sums at most \(S/2-z\); equivalently, perform the descending Boolean dynamic program in `verify.cpp`. An induction on the processed divisors proves that the table is exactly the set of sums of their subsets. It follows that the program enumerates **all** even Zumkeller integers at most \(4288\), neither overlooking nor inventing any. The enumeration returns exactly \(972\) such integers.

**Step 2: exact primality.** The odd-only Eratosthenes array starts by marking \(1\) composite and, for each unmarked odd \(p\) with \(p^2\le10^9\), marks \(p^2,p^2+2p,\ldots\) up to \(10^9\). Every odd composite \(m\le10^9\) has a prime divisor at most \(\sqrt m\), so it is marked. Conversely, the marked positive odd integers are composite, by construction. Therefore the remaining odd entries are *exactly* the odd primes. All candidate differences \(n-z\) are between \(1\) and \(10^9\); the sieve correctly excludes \(1\).

**Step 3: finite exhaustive search.** In increasing order take each \(n=18k+3\) for integer \(2\le k\le55,555,555\). In increasing order scan the **complete** finite list from Step 1 until finding \(z<n\) with prime \(n-z\); the list is ordered, so the first match is the smallest possible **even** Zumkeller addend. The loop checks all \(55,555,554\) eligible integers, finds none uncovered, obtains maximum least even addend \(4288\), and finds that maximum at precisely one value, \(n_*=679570815\). These are exhaustive counts, not inferences from sampling.

**Step 4: remove the parity restriction and prove sharpness.** For odd \(n\), a representation with an *odd* Zumkeller addend has even prime difference, hence the difference must be \(2\), forcing the addend \(n-2\). In particular, at \(n_*\), this odd addend exceeds \(4288\). The complete even list and prime sieve certify that no smaller even Zumkeller addend works at \(n_*\). Hence \(h(n_*)=4288\). For every other eligible \(n\), Step 3 gives an even addend strictly less than \(4288\), so the global maximum is exactly and uniquely as stated. Directly,
\[
\sigma(4288)=(1+2+\cdots+2^6)(1+67)=127\cdot68=8636,
\]
and \(4288+2+4+8+16=4318=\sigma(4288)/2\), an explicit balanced half-divisor sum; the other half consists of the remaining positive divisors. The exact sieve certifies \(679566527\) prime.

**Step 5: all remaining odd residues.** Somu--Kukla--Tran, Proposition 4.12 and Conjecture 4.20, establish the representation for every odd \(n\ge9\) not congruent to \(3\pmod{18}\); the only exceptional smaller positive value within this congruence class is \(21\). Combining this published theorem with Steps 1--4 proves the claimed full odd range through \(10^9\).

## Verification

Compile and run the complete finite certificate from the same directory as this document:

`c++ -O3 -std=c++17 verify.cpp -o verify && ./verify`

It returns:

`VERIFY_OK checked=55555554 uncovered=0 maximum_least_summand=4288 unique_max_n=679570815 extremal_prime=679566527 admissible_even_summands=972`

A separately coded formulation of the finite subset-sum recurrence using Python integer bitsets returned the same \(972\) even Zumkeller integers. Separate exact integer/primality checks corroborated every hard-progression case through \(10^5\), the sharp witness prime and the absence of a smaller feasible even Zumkeller summand at the extremum. Only the C++ verifier performs the complete \(10^9\) search; these supplementary checks do not independently audit that whole loop.

## Relationship to prior work

Somu, Kukla and Tran first published arXiv:2310.14149 on **22 October 2023**. Their Proposition 4.12 handles all other odd residue classes, and their Conjecture 4.20 leaves \(18k+3\) for \(k\ge2\); the paper reports computational verification only through \(k=1000\). The present bound reaches \(k=55,555,555\) and, rather than merely extending the cutoff, establishes the exact sharp minimal-addend covering height and its unique extremizer. OEIS A368082 records small prime--Zumkeller sums, not this maximum. A later 2026 work by Li derives a density-zero statement for the exceptional set; it does not imply the finite sharp covering-height value or the no-exception census here. None of these sources supplies the specific extremal certificate. These comparisons do not guarantee absolute bibliographic priority.

## Limitations

This is a rigorously bounded computation, not a proof for arbitrary \(n\). The value \(10^9\) is a natural finite milestone, not a theoretical transition. The least admissible Zumkeller summand can grow beyond the observed height on larger inputs: for any finite bound, choose distinct odd primes \(q_z\) not dividing \(18\) for the finitely many even Zumkeller offsets \(z\) below the bound. Chinese-remainder solutions of \(n\equiv3\pmod{18}\) and \(n\equiv z\pmod{q_z}\) give infinitely many sufficiently large \(n\) with all \(n-z\) composite; odd offsets are excluded by parity for large \(n\). No universal constant bound is claimed. No statement about the full conjecture beyond the computed range, the existence of every \(h(n)\) beyond it, or independent scientific validation is made.

## References

1. S. T. Somu, A. Kukla and D. V. K. Tran, *Some Results on Zumkeller Numbers*, arXiv:2310.14149v1 (22 October 2023), Proposition 4.12 and Conjecture 4.20; relevant full text: https://arxiv.org/html/2310.14149v2.
2. OEIS Foundation, A368082, *Positive integers which can be written as a sum of a Zumkeller number and a prime number*, https://oeis.org/A368082.
3. T. H. S. Li, *The Density and Quantitative Upper Bound of Integers Not Expressible as the Sum of a Prime and a Zumkeller Number*, arXiv:2610.19574v1 (14 October 2026), https://arxiv.org/abs/2610.19574.
