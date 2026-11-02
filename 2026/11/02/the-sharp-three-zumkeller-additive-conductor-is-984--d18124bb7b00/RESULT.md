# The sharp three-Zumkeller additive conductor is \(984\)

## Finding
A positive integer is **Zumkeller** if its distinct positive divisors can be partitioned into two sets of equal sum. Let \(Z\) denote the set of all such integers and \(3Z=\{x+y+z:x,y,z\in Z\}\), with summands allowed to repeat.

**Theorem.** Every integer \(n\ge984\) belongs to \(3Z\), whereas \(983\notin3Z\). Hence the least integer \(C\) for which every integer \(n\ge C\) is a sum of three positive Zumkeller numbers is exactly \(C=984\).

More constructively, every even \(n\ge98\) is a three-Zumkeller sum. For odd \(n\ge984\), all classes modulo \(18\) have an explicit linear representation involving the odd Zumkeller number \(945\), except for two additional representations at \(1001\) and \(1019\).

## Assumptions and scope
All numbers and summands are **positive integers**. In a sum of three Zumkeller numbers, repetitions are permitted. Write \(\sigma(n)=\sum_{d\mid n}d\). The condition that a subset of distinct divisors sums to \(\sigma(n)/2\) is equivalent to being Zumkeller. We use no assertion about primes or unproved asymptotic density. The published source establishes that \(945\) is the least odd Zumkeller number; we also check the short interval \(947,949,\ldots,983\) directly below.

## Proof
**1. An infinite progression of Zumkeller numbers.** For each integer \(k\ge1\), the divisors of \(3\cdot2^k\) have total sum \(4(2^{k+1}-1)\). The subset consisting of \(3\cdot2^k\) and all \(2,4,\ldots,2^{k-1}\) sums to exactly half that total (with the second part empty when \(k=1\)). Thus \(3\cdot2^k\) is Zumkeller.

If \(u\) is Zumkeller and \(\gcd(u,v)=1\), then \(uv\) is Zumkeller: every divisor of \(uv\) is uniquely a product of a divisor of \(u\) and a divisor of \(v\), so multiply both halves of a balanced divisor partition of \(u\) by the entire divisor set of \(v\). Consequently, every positive integer divisible by \(6\) but not by \(9\) is Zumkeller. In particular,
\[
18t+6\in Z,\qquad18t+12\in Z\quad(t\ge0).\tag{1}
\]
This progression is also explicitly observed in the motivating paper.

**2. Eight fixed witnesses.** The following are Zumkeller, as is checked by exhibiting a subset of their divisors whose sum is half their total divisor sum:

| \(n\) | \(\sigma(n)/2\) | selected distinct divisors |
|---:|---:|---|
| \(6\) | \(6\) | \(6\) |
| \(12\) | \(14\) | \(12,2\) |
| \(20\) | \(21\) | \(20,1\) |
| \(28\) | \(28\) | \(28\) |
| \(40\) | \(45\) | \(40,5\) |
| \(54\) | \(60\) | \(54,6\) |
| \(80\) | \(93\) | \(80,10,2,1\) |
| \(945\) | \(960\) | \(945,15\) |

**3. Explicit residue-class covering.** In each row of the following tables, choose the displayed fixed \(e\) and \(v\in\{6,12\}\). Every integer \(n\) of the indicated residue \(r\pmod{18}\) with \(n\ge B\) then has the exact three-term representation
\[
n=K+e+(18t+v),\qquad t=(n-B)/18\ge0,
\]
where \(K=6\) for the even rows and \(K=945\) for the odd rows. Every summand is Zumkeller by (1) and step 2.

| even \(r\) | \(e\) | \(v\) | \(B=6+e+v\) |
|---:|---:|---:|---:|
| \(0\) | \(6\) | \(6\) | \(18\) |
| \(2\) | \(20\) | \(12\) | \(38\) |
| \(4\) | \(28\) | \(6\) | \(40\) |
| \(6\) | \(6\) | \(12\) | \(24\) |
| \(8\) | \(80\) | \(12\) | \(98\) |
| \(10\) | \(28\) | \(12\) | \(46\) |
| \(12\) | \(12\) | \(12\) | \(30\) |
| \(14\) | \(20\) | \(6\) | \(32\) |
| \(16\) | \(40\) | \(6\) | \(52\) |

| odd \(r\) | \(e\) | \(v\) | \(B=945+e+v\) |
|---:|---:|---:|---:|
| \(1\) | \(40\) | \(6\) | \(991\) |
| \(3\) | \(6\) | \(6\) | \(957\) |
| \(5\) | \(20\) | \(12\) | \(977\) |
| \(7\) | \(28\) | \(6\) | \(979\) |
| \(9\) | \(6\) | \(12\) | \(963\) |
| \(11\) | \(80\) | \(12\) | \(1037\) |
| \(13\) | \(28\) | \(12\) | \(985\) |
| \(15\) | \(12\) | \(12\) | \(969\) |
| \(17\) | \(20\) | \(6\) | \(971\) |

The even rows cover every even \(n\ge98\). Among odd \(n\ge984\), each row starts no later than the first integer of its residue class above \(983\), **except** \(r=11\). That exceptional residue has the two additional values below its table start, namely
\[
1001=945+28+28,\qquad1019=945+20+54.
\]
Thus every integer \(n\ge984\) is in \(3Z\).

**4. Sharpness at \(983\).** The motivating paper identifies \(945\) as the least odd Zumkeller number. Every odd integer strictly between \(945\) and \(983\) is deficient: for each \(n\in\{947,949,\ldots,983\}\), direct divisor summation gives \(\sigma(n)<2n\), an exact nineteen-integer check reproduced by the accompanying standalone verifier. A deficient number cannot be Zumkeller because no subset of its proper divisors can balance the divisor \(n\). Hence the only odd Zumkeller number not exceeding \(983\) is \(945\).

If \(983\) were the sum of three Zumkeller numbers, the parity of the sum would require either one or three odd summands. Three odd summands are impossible since \(3\cdot945>983\). Thus the unique odd summand would be \(945\), leaving \(38\) as a sum of two even Zumkeller numbers. The only Zumkeller numbers below \(38\) are \(6,12,20,24,28,30\): this follows by enumerating their divisor sums and subset sums (or by the standalone exact verifier). No two members of this six-element set sum to \(38\). Therefore \(983\notin3Z\), completing the proof.

## Verification
Run `python3 verify_three_zumkeller.py` using the Python standard library. It checks the eight balanced divisor partitions, all eighteen residue-class witnesses, the nineteen odd deficiencies, and over \(49,000\) exact constructive representations. Independently, it computes the Zumkeller predicate by full divisor-subset sums for every integer through \(1200\), forms the exact threefold sumset by integer bitsets, checks that \(983\) is absent and that all \(984\le n\le1200\) are present. Expected output begins `VERIFY_OK`. The infinite result follows from the modular covering argument, not from finite testing.

## Relationship to prior work
Somu, Kukla and Tran [1] prove that all integers above \(94185\) are sums of two Zumkeller numbers and explicitly suggest investigating **three or four Zumkeller summands** in Section 5. They record the \(18t+6\) and \(18t+12\) progressions and the least odd Zumkeller number \(945\). The new ingredient here is a complete eighteen-residue covering with a sharp boundary obstruction, yielding the exact conductor \(984\) for three terms. The OEIS two-summand exception sequence [2] is a different invariant and does not give this sharp three-summand bound without an additional argument.

## Limitations
This determines the eventual threshold, not the complete list of all representations or all exceptional integers below \(984\). The proof concerns sums of exactly three **positive** Zumkeller numbers with repetition, not three distinct summands or two-summand representations. No independent scholarly audit has been performed, and an unindexed earlier equivalent result remains possible.

## References
1. S. T. Somu, A. Kukla and D. V. K. Tran, *Some Results on Zumkeller Numbers*, arXiv:2310.14149v1 (22 October 2023), especially Remarks 2.3 and Section 5; full revised text arXiv:2310.14149v2 (27 November 2023), https://arxiv.org/html/2310.14149v2.
2. OEIS A368007, *Positive integers which cannot be written as a sum of two Zumkeller numbers*, https://oeis.org/A368007.
