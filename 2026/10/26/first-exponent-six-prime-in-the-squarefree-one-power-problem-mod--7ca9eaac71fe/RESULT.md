# First exponent-six prime in the squarefree one-power problem modulo 36

## Finding
For every prime \(p\equiv7\pmod{36}\), define \(e(p)\) as the smallest integer \(a\ge0\) for which \(2^a<p\) and the positive integer \(p-2^a\) is squarefree. Then the smallest prime in this congruence class with \(e(p)\ge6\) is
\[
\boxed{p=189954151},\qquad e(189954151)=6.
\]
In particular, every smaller prime \(p\equiv7\pmod{36}\) has \(e(p)\le5\). Among primes through the displayed threshold, precisely 20 have \(e(p)=5\), and exactly one requires exponent six.

## Assumptions and scope
A positive integer is squarefree when no prime square divides it. Primes and squarefreeness are interpreted over the ordinary positive integers. The claim covers **all** primes in one fixed reduced residue class up to the exact finite boundary; no statement about all larger primes is implied. For this class, \(p-16\equiv0\pmod9\), so exponent four is never a valid witness when the remainder is positive.

## Proof
The decisive candidate is prime, as certified by the complete Eratosthenes sieve below, and it equals \(7\pmod{36}\). Its seven relevant remainders, with exact factorizations, are:

| Exponent \(a\) | \(p-2^a\) | Factorization |
| --- | ---: | --- |
| 0 | 189954150 | \(2\cdot3\cdot5^2\cdot167\cdot7583\) |
| 1 | 189954149 | \(7\cdot11^2\cdot224267\) |
| 2 | 189954147 | \(3\cdot29^2\cdot75289\) |
| 3 | 189954143 | \(31^2\cdot157\cdot1259\) |
| 4 | 189954135 | \(3^2\cdot5\cdot7^2\cdot277\cdot311\) |
| 5 | 189954119 | \(47^2\cdot85991\) |
| 6 | 189954087 | \(3\cdot63318029\), with \(63318029\) prime |

Thus the first six remainders are not squarefree, while the seventh is squarefree; in particular \(e(p)=6\).

To establish **minimality** rather than merely construct a witness, exhaust the complete arithmetic progression of primes from \(7\) through \(189954151\). A standard Eratosthenes sieve marks every composite \(n\) in that interval by crossing multiples of primes \(q\le\sqrt n\), starting at \(q^2\). Separately, mark every integer divisible by some \(q^2\), for primes \(q\le\sqrt{189954151}\). An integer left unmarked in the latter sieve is squarefree: if a square of a composite integer divided it, the square of one of the composite's prime factors would also divide it.

The exact enumerations contain 879429 primes in this progression through the threshold. Only 21 of those fail **all four** squarefree tests at exponents \(0,1,2,3\). Their complete ordered list is recorded in `obstruction_certificate.csv`. Of those 21, the first 20 have \(p-32\) squarefree, and the final one, \(189954151\), does not. Since exponent four is always obstructed, all smaller primes have \(e(p)\le5\). This finishes the minimality proof.

The certificate includes a prime-square divisor for each of the four failed initial tests, and for the exponent-five test at the last candidate. The two independently written complete sieve implementations reproduce both the number of primes and the exact exceptional list. Each uses only integer arithmetic; there is no probabilistic primality test and no extrapolation.

## Verification
Extract the accompanying `verify_sieve.py`, `verify_segmented.cpp` and `obstruction_certificate.csv` into one directory. Run `python3 verify_sieve.py`. Compile the second check with `c++ -std=c++17 -O2 verify_segmented.cpp -o verify_segmented` and run `./verify_segmented`. Both must report `prime_candidates=879429`, `four_failure_count=21`, and first exponent-six prime `189954151`. The Python verifier additionally checks the CSV obstruction witnesses and the squarefree exponent-six remainder; the C++ program independently repeats the complete interval scan in overlapping segments.

The entire finite range is bounded explicitly and is checked exhaustively. An individual divisor list or an isolated test at the final prime would not establish minimality; the full-range prime and squarefree sieves are necessary.

## Relationship to prior work
Harman and Paquin (2026, arXiv:2610.07214v1) study precisely this congruence class, determine the density of primes that can use one of the first four powers, and verify that all primes below \(10^8\) can use some exponent at most five; they list eleven primes below this bound needing exponent five. Their discussion explicitly motivates locating the first example needing a larger exponent. The sharp first exponent-six prime and the exact finite census here extend the computational boundary without claiming a new density theorem.

Hercher (2024, arXiv:2411.01964v1) rigorously verifies existence of representations for all odd integers through a much larger bound and studies early failures for fixed exponents. That global existence theorem does not identify the first prime in the restricted progression that needs exponent six. Earlier related integer-sequence tables and unindexed computations remain possible overlap risks.

## Limitations
This is an exact finite first-occurrence result for \(p\equiv7\pmod{36}\), not an assertion of any positive density for exponent six, nor a solution of the conjecture beyond the finite range. It rests on replayable exhaustive integer sieves; their algorithmic correctness and scope must be reviewed independently before treating the result as independently validated. Published or private computations not indexed by the searched sources could contain the same threshold.

## References
1. S. Harman and D. Paquin, “The One-Power Erdős Conjecture for Primes \(p\equiv7\pmod{36}\),” arXiv:2610.07214v1, publicly released 2026-10-05. https://arxiv.org/abs/2610.07214
2. C. Hercher, “On the Sum of a Squarefree Integer and a Power of Two,” arXiv:2411.01964v1, publicly released 2024-11-04. https://arxiv.org/abs/2411.01964
