# Thirty-six distinct loops for Das's map at \(k=20735\)

## Finding
For \(k\in\mathbb N\), let \(\varphi_k\) be Angsuman Das's map on integers greater than \(1\):
\[
\varphi_k(x)=
\begin{cases}
x+k,&x\text{ prime},\\
P(x),&x\text{ composite},
\end{cases}
\]
where \(P(x)\) is the largest prime divisor of \(x\). Let \(L(k)\) denote the number of distinct eventual loops as the starting value varies.

Among odd integers
\[
3\le k\le20735,
\]
the first parameter with
\[
L(k)=36
\]
is
\[
k=20735.
\]
No smaller odd \(k\) in this range has \(36\) loops.

At \(k=20735\), the 36 loops have period distribution
\[
6\text{ loops of period }4,\quad
14\text{ of period }6,\quad
10\text{ of period }8,\quad
5\text{ of period }10,\quad
1\text{ of period }12.
\]

The record sequence over odd \(k\) through \(20735\) is
\[
\begin{aligned}
&(3,2),(15,4),(51,5),(105,6),(159,7),(715,8),(1365,13),\\
&(4479,14),(6335,15),(12095,17),(14399,20),(17919,23),(20735,36).
\end{aligned}
\]

## Assumptions and scope
The source paper proves eventual periodicity for every \(k\), proves that \(L(k)\) is finite, and reports a computation for \(1\le k\le5000\) in which the maximum observed value is \(14\), attained only at \(k=4479\). It then asks whether \(L(k)\) is unbounded as \(k\) varies.

The present result is a finite exact computation for odd parameters only. It does not assert that \(k=20735\) is the first parameter among all positive integers to have 36 loops, and it does not prove that \(L(k)\) is unbounded.

## Proof
Fix an odd integer \(k\ge3\).

Every loop contains a prime. Das's Lemma 2.2 states that if \(p>k\) is prime, then
\[
\varphi_k^2(p)<p.
\]
Consequently every loop contains a prime \(p\le k\): otherwise choose the least prime occurring in the loop; Lemma 2.2 would produce a smaller prime in the same loop, a contradiction.

It is therefore enough to start trajectories from the finitely many primes
\[
p\le k.
\]

These trajectories can be followed inside the finite interval
\[
2\le x\le2k+2.
\]
Indeed, if \(p\le k\) is an odd prime, then \(p+k\le2k\) is an even composite integer, and its largest prime divisor is at most
\[
\frac{p+k}{2}\le k.
\]
For the exceptional start \(p=2\), the value \(k+2\) is at most \(2k+2\). If \(k+2\) is composite, its largest prime divisor is below \(k\); if \(k+2\) is prime, the next value is \(2k+2\), whose largest prime divisor is at most \(k\) for \(k\ge3\). Thus after at most two prime steps the trajectory is again at a prime not exceeding \(k\).

The accompanying exact enumerator applies this finite reduction independently for each odd
\[
3\le k\le20735.
\]
It records each directed cycle in canonical rotation, so two starting primes leading to the same loop are counted once. Its strict record sequence is
\[
(3,2),(15,4),(51,5),(105,6),(159,7),(715,8),(1365,13),
(4479,14),(6335,15),(12095,17),(14399,20),(17919,23),(20735,36).
\]
Hence \(L(20735)=36\), and no smaller odd parameter in the scanned interval has 36 loops.

## Verification
The file `verify.cpp` performs the complete odd-\(k\) enumeration. It first constructs an exact largest-prime-factor table through
\[
2\cdot20735+2=41472.
\]
For each odd \(k\), it starts from every prime \(p\le k\), follows the exact map, identifies directed cycles, and merges duplicate basins by cycle identity.

The replay requires the terminal line `VERIFY_OK`, the complete odd-record sequence above, exactly 36 cycles at \(k=20735\), and the period histogram
\[
4:6,\quad6:14,\quad8:10,\quad10:5,\quad12:1.
\]
The file `cycles.txt` contains the exact replay output, including all 36 canonical cycles.

An independent implementation was also used to recompute the \(k=20735\) cycle set and obtained the same count and period histogram. That independent check is supporting evidence; the packaged finite proof is the exhaustive `verify.cpp` replay together with the reduction above.

## Relationship to prior work
Das introduced this family, proved eventual periodicity and finiteness of the number of loops for fixed \(k\), and reported that among
\[
1\le k\le5000
\]
the maximum loop count is \(14\), attained only at \(k=4479\). The paper's first open issue asks whether the number of loops is unbounded as \(k\) varies.

Dubickas later studied a broader class of bounded iterative integer sequences that includes the largest-prime-divisor rule, establishing periodicity and explicit bounds in that setting. The inspected material does not state an updated loop-count record for Das's specific map.

Targeted searches by the map definition, the source title, the parameter \(20735\), the value \(36\), and the phrase “number of distinct loops” did not locate a prior indexed statement of this record.

## Limitations
This is a finite record computation and does not prove the source paper's unboundedness question. The “first” assertion is only over odd
\[
k\le20735.
\]
Even parameters between \(5001\) and \(20735\) were not enumerated here.

Literature non-detection is not a proof of novelty; an unindexed or private computation may already contain the same or a stronger loop record.

## References
1. Angsuman Das, “A Family of Iterated Maps on Natural Numbers,” arXiv:2312.06629v1, first posted 11 December 2023, MSC 11B83, 11B37, 11A25.
2. Artūras Dubickas, “A Class of Bounded Iterative Sequences of Integers,” *Axioms* 13 (2024), 107, DOI 10.3390/axioms13020107.
