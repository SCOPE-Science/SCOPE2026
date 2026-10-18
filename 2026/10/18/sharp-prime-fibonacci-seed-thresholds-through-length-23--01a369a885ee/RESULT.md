# Sharp prime-Fibonacci seed thresholds through length 23

## Finding

A *prime-Fibonacci trajectory* begins at an ordered pair of distinct odd primes \((p,q)\). If the sum of the last two terms is a power of two, the trajectory terminates; otherwise its next term is the smallest odd prime divisor of that sum. Its length \(L(p,q)\) is the number of prime terms, including the initial two.

For every integer \(2\leq\ell\leq23\), define the *optimal seed ceiling*
\[
M(\ell)=\min\{\max(p,q): p,q\text{ are distinct odd primes and }L(p,q)\geq\ell\}.
\]
The complete initial values are:

| \(\ell\) | \(M(\ell)\) | \(\ell\) | \(M(\ell)\) | \(\ell\) | \(M(\ell)\) |
|---:|---:|---:|---:|---:|---:|
| 2 | 5 | 10 | 47 | 18 | 761 |
| 3 | 7 | 11 | 53 | 19 | 1487 |
| 4 | 7 | 12 | 53 | 20 | 2381 |
| 5 | 11 | 13 | 131 | 21 | 3863 |
| 6 | 11 | 14 | 443 | 22 | 3863 |
| 7 | 19 | 15 | 461 | 23 | 4919 |
| 8 | 29 | 16 | 521 | | |
| 9 | 41 | 17 | 521 | | |

In particular, among all ordered distinct odd-prime seeds with both entries at most \(4919\), the **only** trajectory containing at least \(23\) terms starts with \((4007,4919)\). Every seed with both entries at most \(4909\), the preceding prime, terminates within \(22\) terms. This is an exact finite extremal theorem, not an asymptotic assertion about greater seed primes.

## Assumptions and scope

The words *prime*, *odd prime*, *least odd prime factor*, and *power of two* have their standard integer meanings. Both orders of each pair of distinct initial odd primes are permitted. Terms are counted up to the last prime before the two-term sum becomes a power of two; the power-of-two sum is not a term. The threshold minimum ranges over all positive odd prime pairs, not just pairs within the computational bound. Its values through length \(23\) are nevertheless determined by certificates contained in that finite bound.

## Proof

If \(p\ne q\) are odd primes, any next odd prime divisor \(r\) of \(p+q\) satisfies \(r\leq(p+q)/2<\max(p,q)\), since \(p+q\) is even. Further, \(r\ne p,q\), because divisibility of \(p+q\) by either one would force divisibility of the other distinct prime. Thus adjacent pairs retain distinct prime entries. If the larger initial term is the first entry, the next pair immediately has smaller maximum; if it is the second entry, the following pair has smaller maximum because the newly generated term is strictly below that larger entry. Hence the maximum decreases after at most two successor transitions, which proves termination and excludes repeated ordered prime pairs.

For a finite ceiling \(B\), every trajectory seeded below \(B\) stays within the same prime ceiling, so exact exhaustive enumeration requires only the odd primes at most \(B\). The included `verify.py` enumerates these primes independently by trial division and by an Eratosthenes sieve, agreeing on exactly \(656\) odd primes up to \(B=4919\). It visits every \(656\cdot655=429680\) ordered pair with distinct entries exactly once.

Two independently coded transition algorithms calculate \(L(p,q)\): one divides the odd part of each sum by trial divisors, and another uses a complete sieve of least prime factors and memoized pair depths. They agree for all ordered pairs in the finite domain. Scanning seed ceilings through odd primes in increasing order, the program records the first ceiling for which a trajectory of length at least \(\ell\) exists. The output exactly matches the stated \(22\)-value threshold table for \(2\leq\ell\leq23\). For each \(\ell\), the first identified ceiling supplies an actual witness; all smaller ceilings are exhaustively ruled out. Therefore the finite computations prove the global minimum \(M(\ell)\) for each listed length, without making a claim about untested greater lengths.

For the final threshold, the unique qualifying seed \((4007,4919)\) has the trajectory
\[
4007,4919,4463,4691,23,2357,5,1181,593,887,5,223,3,113,29,71,5,19,3,11,7,3,5.
\]
Its final two terms sum to \(8\), and all earlier successor rules are checked exactly by `verify.py`. The complete enumeration finds no second ordered seed with the same ceiling attaining length \(23\), nor any seed below that ceiling doing so.

## Verification

Run `python3 verify.py` using Python \(3.10\) or later; no third-party dependencies are required. The program reconstructs primes, verifies the entire threshold table, checks both algorithms for all \(429680\) ordered seeds, verifies the unique longest witness, and prints `PASS`. This exhaustive finite proof does not rely on probabilistic primality tests, sampling, or extrapolation.

## Relationship to prior work

Alm and Herald introduced this prime-Fibonacci recurrence and proved termination for distinct odd-prime seeds, with arbitrarily long trajectories obtainable through backward extension. Their qualitative theorems do not give the first attainable seed ceilings as a function of trajectory length. The present theorem determines those concrete sharp values through length \(23\). The different *subprime Fibonacci* recurrence of Guy, Khovanova, and Salazar divides a composite sum by its least prime factor; its cycle data are not extremal data for the smallest-odd-divisor recurrence analyzed here.

## Limitations

There is no formula here for \(M(\ell)\) at \(\ell\geq24\), nor a general asymptotic growth estimate. The novelty comparison establishes no absolute uniqueness in all unpublished or unindexed enumerations, and an independently executed audit has not been performed. The mathematical result is the exact initial threshold classification and its unique depth-\(23\) witness, not the already known fact that all such trajectories terminate.

## References

1. Jeremy Alm and Taylor Herald, *A Note on Prime Fibonacci Sequences* (first posted July 17, 2015), arXiv:1507.04807, https://arxiv.org/abs/1507.04807.
2. Richard K. Guy, Tanya Khovanova, and Julian Salazar, *Conway's Subprime Fibonacci Sequences* (first posted July 21, 2012), arXiv:1207.5099, https://arxiv.org/abs/1207.5099.
