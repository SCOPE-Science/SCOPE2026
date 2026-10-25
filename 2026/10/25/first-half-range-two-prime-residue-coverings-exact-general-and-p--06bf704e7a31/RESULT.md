# First half-range two-prime residue coverings: exact general and prime-power thresholds

## Finding
For every integer \(q\ge2\) and real \(X\ge0\), write \(U(q)=(\mathbb Z/q\mathbb Z)^\times\) and
\[
 E_2(q;X)=\{pr\bmod q:\ p,r\text{ are primes},\ p,r\le X\}\cap U(q).
\]
Repetition of a prime is permitted. Define the least successful cutoff \(B(q)\) as the smallest real \(X\) with \(E_2(q;X)=U(q)\), when such a cutoff exists. Then:

**Theorem (first half-range successes and their sharp cutoffs).** The least integer modulus \(q\ge2\) with \(E_2(q;q/2)=U(q)\) is \(q=96\). The least **prime-power** modulus with that property is \(q=256\). Their least successful prime bounds are
\[
 B(96)=47,\qquad B(256)=127.
\]
Equivalently, the complete binary prime-product residue images first cover all \(32\) units at \(q=96\) using primes no larger than \(47\), and first cover all \(128\) units for a prime-power modulus at \(q=256\), using primes no larger than \(127\). The claim of "first" refers to numerical order of the modulus, not eventual or monotone behavior.

## Assumptions and scope
All moduli and bounds are ordinary positive integers except that the comparison \(q/2\) can be half-integral; for prime products, replacing it by \(\lfloor q/2\rfloor\) makes no difference. \(U(q)\) includes the unit \(1\) even for \(q=2\). Prime factors need not be distinct, but each must separately satisfy the indicated size cutoff. There are no unproved analytic assumptions. The result is an exact finite minimum, not a claim that every larger modulus has the covering property.

## Proof
For \(q\ge2\), put \(P(q,t)=\{p:\ 2\le p\le t,\ p\text{ prime},\ \gcd(p,q)=1\}\). The elementary identity
\[
 E_2(q;t)=\{pr\bmod q:\ p,r\in P(q,t)\}
\]
follows directly from the definitions. This identity reduces the theorem to finite primality, multiplication and coprimality tests.

For the two proposed successful moduli, `coverings.json` gives a witness prime pair for **every** unit class. The verifier `verify.py` checks primality, both size inequalities, and the product congruence for all \(32\) and \(128\) classes respectively; it independently enumerates their pair-product images and checks equality with \(U(96)\) and \(U(256)\).

For minimality, `obstructions.json` gives a specific unit residue absent from all products of primes at most \(\lfloor q/2\rfloor\), separately for each \(2\le q<96\) and each prime-power \(q<256\). There are \(129\) distinct moduli in this union. The verifier independently enumerates candidate prime factors, tests each obstruction using modular inverses, and also tests it against the complete pair-product image. Thus no smaller modulus in either category can have full half-range coverage.

Finally, for \(q=96\), primes up to \(43\) represent only \(30\) of \(32\) units (the missing residues are \(5\) and \(43\)); all \(32\) are reached by prime \(47\). For \(q=256\), primes up to \(113\) represent \(127\) of \(128\) units (the missing residue is \(81\)); all \(128\) are reached by prime \(127\). There are no primes strictly between \(43\) and \(47\) or between \(113\) and \(127\). Since the product image changes only as the factor cutoff passes a prime, these are the sharp least cutoffs. These two further obstructions bring the finite obstruction certificate to \(131\) entries. This completes the proof.

## Verification
Run `python3 verify.py` in the directory containing `verify.py`, `coverings.json`, and `obstructions.json`. It uses only the Python standard library, with integer-exact primality tests (trial division), direct pair enumeration, an independent modular-inverse obstruction method, and explicit coverage witnesses. The expected completion marker is `CERTIFICATE_OK upper_units=160 obstruction_moduli=131 first_general=96 first_prime_power=256 thresholds=47,127`. The finite exhaustive verification is the proof certificate: all permitted smaller moduli, all claimed unit classes and all relevant prime factors are checked, rather than sampled. This result makes no assertion beyond the certified domains.

## Relationship to prior work
Banks and Shparlinski (arXiv:2610.19597v1, October 14, 2026) define the same residue sets \(E_2(q;X)\), using the notation \(\mathsf{EOS}_2(q;X)\). Their Theorems 1.1–1.4 analyze sufficiently large prime powers (especially ternary representations and an almost-all binary conclusion) and related estimates for primes bounded by \(q\), not the present exact finite first-success moduli for \(X=q/2\). Szabó (2024) proves large-modulus estimates for products of primes, likewise not the claimed exact cutoffs. The older work of Erdős, Odlyzko and Sárközy (1987) motivates the binary prime-product conjecture, but a complete copy could not be examined here. The finite computations and witness certificates are new calculations in the present work; the general conjecture and the motivating analytic theorems are not claimed as new.

## Limitations
These results concern the natural half-modulus benchmark, not the full Erdős–Odlyzko–Sárközy conjecture \(E_2(q;q)=U(q)\) for all sufficiently large \(q\). They imply no monotonicity in \(q\), no infinite-family theorem, no asymptotic coverage estimate and no independent external validation. An unindexed previous exact enumeration, especially within older sources, could overlap the cutoffs. The full 1987 source was not accessible for material inspection.

## References
1. William Banks and Igor E. Shparlinski, *On the Erdős–Odlyzko–Sárközy conjecture for prime-power moduli*, arXiv:2610.19597v1 (first public October 14, 2026), https://arxiv.org/html/2610.19597v1.
2. Barnabás Szabó, *On the existence of products of primes in arithmetic progressions*, Bulletin of the London Mathematical Society 56 (2024), 1227–1243, https://doi.org/10.1112/blms.12990.
3. P. Erdős, A. M. Odlyzko and A. Sárközy, *On the residues of products of prime numbers*, Periodica Mathematica Hungarica 18 (1987), 229–239, https://doi.org/10.1007/BF01848086.
4. William D. Banks, *Products of two elements of Granville's random model in residue classes*, arXiv:2609.37434v1 (September 29, 2026), https://arxiv.org/abs/2609.37434.
