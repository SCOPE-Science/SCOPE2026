# Complete base classification for periodic last nonzero digits of self-powers

## Finding

For each integer base \(b\ge 2\), write \(\nu_b(x)=\max\{a\ge0:b^a\mid x\}\) for positive integers \(x\), and let
\[
F_b(n)=\left(\frac{n^n}{b^{\nu_b(n^n)}}\right)\bmod b\qquad(n\ge1).
\]
Here residues are the least nonnegative representatives modulo \(b\); by the choice of \(\nu_b\), the representative is always between \(1\) and \(b-1\). Thus \(F_b(n)\) is the last nonzero base-\(b\) digit of \(n^n\), where a nonzero digit means a digit other than \(0\), not necessarily a unit modulo \(b\).

**Theorem (complete periodicity classification).** For every integer \(b\ge2\), the sequence \((F_b(n))_{n\ge1}\) is eventually periodic if and only if
\[
b=2^{2^s}\quad\text{for some integer }s\ge0.
\]
For these bases it is periodic from the first term, with \(b\) as a period. For every other base it is not eventually periodic. The new ingredient is a uniform nonperiodicity proof for **all bases with at least two distinct prime divisors**, including nonsquarefree bases not handled by the motivating work. The prime-power cases are supplied by the published theorem of Grau and Oller-Marcén [1], not claimed here as new.

**Constructive stronger statement.** If \(b\) has at least two distinct prime factors, then for *every* pair of positive integers \(T,N\) there are integers \(m>n\ge N\) satisfying
\[
m\equiv n\pmod T,\qquad F_b(n)=1,\qquad F_b(m)\equiv0\pmod p
\]
for any fixed choice of a prime \(p\mid b\) accompanied by a different prime \(q\mid b\). In particular \(F_b(m)\ne F_b(n)\), disproving any proposed eventual period \(T\).

## Assumptions and scope

All bases \(b\), indices \(n\), thresholds \(N\) and proposed periods \(T\) are positive integers with \(b\ge2\). The completely general classification combines the constructive mixed-prime statement proved below with the prior prime-power classification [1, Theorem 7]. No assumption of squarefreeness, parity, primality of the index, or size of the proposed period is made. Neither the least period for positive cases nor statistical digit frequencies are claimed.

## Proof

**1. Decompose an arbitrary proposed period.** Suppose \(b\) has at least two distinct prime divisors \(p\) and \(q\), and fix any \(T,N\ge1\). Write
\[
T=T_{\parallel}T_{\perp},
\]
where \(T_{\parallel}\) is the largest divisor of \(T\) supported on primes dividing \(b\), and \(\gcd(T_{\perp},b)=1\). These two factors are coprime. Choose \(k\ge1\) so large that
\[
T_{\parallel}\mid b^k,\qquad b^k\ge N.
\]
This is possible because \(T_{\parallel}\) has no prime factors outside the support of \(b\).

**2. Construct a contrasting multiple.** By the Chinese remainder theorem, there is a positive integer \(u>1\) such that
\[
u\equiv0\pmod p,\qquad
u\equiv1\pmod q,\qquad
u\equiv1\pmod{T_{\perp}}.
\]
The moduli \(p\), \(q\) and \(T_{\perp}\) are pairwise coprime; the congruence modulo \(1\), if present, is vacuous. Define
\[
n=b^k,\qquad m=b^k u.
\]
Then \(m>n\ge N\). Furthermore \(m-n=b^k(u-1)\) is divisible by \(T_{\parallel}\), and \(u-1\) is divisible by \(T_{\perp}\), so \(m\equiv n\pmod T\).

**3. Compute the last nonzero digits exactly.** The first index satisfies
\[
n^n=(b^k)^n=b^{kn},\quad\text{hence}\quad F_b(n)=1.
\]
The second satisfies
\[
m^m=b^{km}u^m.
\]
Because \(u\equiv1\pmod q\) and \(q\mid b\), no positive power of \(u\) is divisible by \(b\). Consequently \(\nu_b(m^m)=km\) *exactly*, without any unremoved factors of \(b\), and
\[
F_b(m)\equiv u^m\pmod b.
\]
Since \(p\mid u\), this yields \(F_b(m)\equiv0\pmod p\). As \(F_b(n)=1\not\equiv0\pmod p\), the two digits differ. The statement holds for arbitrary \(T\) and arbitrarily large \(N\), proving mixed-prime nonperiodicity. (The last nonzero digit of a number may indeed be divisible by one prime factor of a composite base.)

**4. Complete the classification using known prime-power results.** Every integer \(b\ge2\) is either a prime power or has at least two distinct prime factors. The latter case has just been proved. In the former case, [1, Theorem 7] proves that eventual periodicity occurs precisely for \(b=2^{2^s}\) with integer \(s\ge0\); [1, Proposition 10] gives period \(b\) from the first term. Together these exhaust all integer bases and prove the theorem. \(\square\)

## Verification

The accompanying standalone `verify.py` uses only Python's standard library. Running `python3 verify.py` constructs exactly congruent counterexample indices across \(22\) mixed-prime bases and \(16\) proposed periods, and checks the predicted digit discrepancy by modular arithmetic. It additionally evaluates individual (large but finite) powers directly when practical, and checks the published positive-period formula on four prime-power bases. Expected output:

```text
VERIFY_OK mixed_prime_period_witnesses 352 direct_witness_evaluations 75 prime_power_positive_period_cases 512
```

These experiments only test the construction. The proof above establishes the statement for **all** bases with at least two prime factors, all periods and all thresholds; the prime-power conclusion depends on the published theorem [1].

## Relationship to prior work

Grau and Oller-Marcén [1] introduced the general last-nonzero-digit periodicity question and stated **Conjecture 11**, predicting precisely the classification above. Their Theorem 7 proves the complete prime-power case; their other negative results include even squarefree bases. Their conjecture remains unproved by the arguments presented in [1] for arbitrary nonsquarefree bases with several prime factors. The constructive Chinese-remainder witness of Steps 1–3 fills that remaining case. Thus the conclusion for all bases follows from a genuinely new mixed-prime lemma plus the *credited*, pre-existing prime-power theorem; neither the conjecture nor the positive periodic cases are new objects.

Sobolewski [2] treats last-nonzero-digit and automaticity properties for values of tuples of prime-adic analytic functions; this does not supply a global classification for the variable-exponent self-power \(n^n\). OEIS A260031 [3] records values for base \(12\) without the all-period nonperiodicity argument. Comparisons of statements, not just titles, leave no inspected source implying the mixed-prime lemma. Earlier specialized base results, or more general unindexed results, could affect publication priority; this is not a proof of global uniqueness of the result.

## Limitations

The new assertion is elementary and relies on a standard Chinese remainder theorem construction. It does not reprove [1, Theorem 7], determine minimal periods for the periodic bases, study multi-digit tails, or establish a general theory for exponent sequences other than \(n^n\). The originality assessment is based on the inspected primary works, sequence record and published-research search, with the possibility of unindexed equivalent statements. No independent mathematical audit has been performed.

## References

[1] José María Grau and Antonio M. Oller-Marcén, *On the last digit and the last non-zero digit of \(n^n\) in base \(b\)*, arXiv:1203.4066v1 (first public posting 2012-03-19), Bull. Korean Math. Soc. **51** (2014), 1325–1337, DOI:10.4134/BKMS.2014.51.5.1325. https://arxiv.org/abs/1203.4066

[2] Bartosz Sobolewski, *On k-regularity of sequences of valuations and last non-zero digits*, Ramanujan J. **61** (2023), 1151–1195, DOI:10.1007/s11139-023-00710-8. https://link.springer.com/article/10.1007/s11139-023-00710-8

[3] OEIS A260031, *Final nonzero digit of \(n^n\) in base \(12\)*. https://oeis.org/A260031
