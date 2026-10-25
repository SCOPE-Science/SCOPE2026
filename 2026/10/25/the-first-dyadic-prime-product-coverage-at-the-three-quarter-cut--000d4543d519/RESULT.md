# The first dyadic prime-product coverage at the three-quarter cutoff

## Finding
Let \(E_2(q;X)\) denote the residue classes coprime to \(q\) of products \(p_1p_2\), where \(p_1,p_2\) are primes at most \(X\), with repeated primes allowed. Put \(q_m=2^m\) and \(B_m=\lfloor q_m^{3/4}\rfloor\).

**Finite sharp threshold.** Among positive integers \(m\), the first for which \(E_2(q_m;B_m)\) contains every unit class is \(m=21\). At that exponent the least prime cutoff making the coverage complete is \(50923\), strictly below \(B_{21}=55108\). At \(m=20\), exactly the three unit classes \(122299,333455,414971\) modulo \(1048576\) remain uncovered by primes at most \(B_{20}=32768\). Immediately before the cutoff \(50923\), the lone missing unit class modulo \(2097152\) is \(745135\), and
\[
50923\cdot7757\equiv745135\pmod{2097152}.
\]

## Assumptions and scope
All primes are ordinary positive rational primes, repetition is permitted, and only unit residue classes are counted. The result is an exact finite theorem for \(1\le m\le21\); it makes no assertion that the property persists for \(m>21\). The bound \(B_m\) is the exact integer fourth root \(\lfloor\sqrt[4]{2^{3m}}\rfloor\), not a rounded floating-point approximation. In particular, \(B_1=1\) and \(B_2=2\), so no odd-prime product occurs in the unit group at those exponents.

## Proof
A standard Eratosthenes sieve with cutoff \(B_m\) lists every odd prime \(p\le B_m\). Since all units modulo \(2^m\) are odd, prime \(2\) cannot occur in a represented unit class. For a prime list \(p_0<\dots<p_{t-1}\), the nested loops in `verify_eos.py` visit exactly once every unordered pair \(\{p_i,p_j\}\) with \(0\le i\le j<t\), allowing equality. Because multiplication is commutative, these pairs give **every** residue of a product of two permitted primes. Each is marked at array index \(((p_ip_j)\bmod2^m-1)/2\); equivalently the bit-index implementation uses \(((p_ip_j)\mathbin{\&}(2^m-1))\gg1\). This is an exact identity for odd products and powers of two. Therefore the number of zero bits after all pairs is precisely the number of uncovered unit classes.

The standalone verifier enumerates **all** exponents \(m=1,\ldots,21\) and checks the following exact missing-class counts:

| \(m\) | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Missing | 1 | 2 | 3 | 3 | 5 | 11 | 17 | 30 | 54 | 70 | 121 |

| \(m\) | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| Missing | 162 | 190 | 240 | 216 | 183 | 92 | 42 | 7 | 3 | 0 |

Thus every \(m\le20\) fails and \(m=21\) succeeds. For sharpness of the last cutoff, the program records the first prime at which the missing count becomes zero: \(50923\), whose preceding prime is \(50909\). It independently checks the unit \(745135\) cannot equal a product of two primes at most \(50909\) by testing every possible first prime using a modular inverse, and that \(50923\cdot7757\) represents it. Therefore no smaller real cutoff succeeds, completing the finite proof.

## Verification
Run `python3 verify_eos.py` with the Python 3 standard library. It prints one line per exponent and ends `VERIFY_OK`. Exact fourth roots are obtained by `isqrt(isqrt(1 << (3*m)))`. The sieve marks every composite via primes at most the integer square root. Arrays have exactly \(2^{m-1}\) cells, one for each odd residue. Inverse-based obstruction checks provide a second route for the listed missing witnesses. No random testing or unverified heuristic is used.

## Relationship to prior work
Banks and Shparlinski, arXiv:2610.19597v1, prove that for large powers of a fixed prime, *almost all* classes contain products of two primes at most the modulus; they do not give full coverage of specific moduli at the smaller \(3/4\)-power cutoff. Banks, arXiv:2609.37434v1, establishes almost-sure full coverage for a model of primes at every fixed exponent **strictly greater than** \(3/4\); its method identifies \(3/4\) as a critical methodological boundary, but it does not assert finite coverage for actual primes at that endpoint. The present result gives a sharp finite dyadic benchmark at exactly that motivated exponent. Earlier finite computations for the different cutoff \(q/2\) do not imply these values because for \(q=2^{21}\), \(q^{3/4}<55109\ll q/2=1048576\).

## Limitations
This is a certified finite computation and not an infinite theorem for later exponents. It does not establish the Erdős--Odlyzko--Sárközy conjecture in general, nor full coverage for \(m>21\). A residual literature risk remains that an obscure computational table may contain the same exact cutoff; novelty comparisons found no such table, not a proof of uniqueness.

## References
- W. D. Banks and I. E. Shparlinski, *On the Erdős--Odlyzko--Sárközy conjecture for prime-power moduli*, arXiv:2610.19597v1 (first public 2026-10-14).
- W. D. Banks, *Products of two elements of Granville’s random model in residue classes*, arXiv:2609.37434v1 (first public 2026-09-29).
- K. Matomäki and J. Teräväinen, *Products of primes in arithmetic progressions*, arXiv:2301.07679 (2023).
