# Independent mathematical audit

## correctness

PASS

Factor X^n−1 into distinct integral cyclotomic factors Phi_d of degree φ(d). Degree completeness is exactly the subset-sum fullness of the coin multiset {φ(d):d|n}. An odd φ-practical n must be divisible by 3 to obtain degree 2 and by 5 to obtain degree 4; write n=3^a5^bq^c. The largest coin φ(n)=8(q−1)T, with T=3^{a−1}5^{b−1}q^{c−1}, and the sum of the other coins n−φ(n) implies (q−16)T≤1; hence q in {7,11,13,17}, with q=17 forcing T=1 and n=255. For q≤13, the base 15q interval is complete, and exact two-prime cofactor max-gap identities Δ(3^a5^b)=3^{a−1}5^{b−1}, Δ(3^aq^c)=(q−4)3^{a−1}q^{c−1}, Δ(5^bq^c)=(3q−8)5^{b−1}q^{c−1} give sufficient overlap for adding arbitrary further powers of any of three primes. The proof uses a precise subset-sum union gap lemma and induction on exponents, not exhaustive finite exponent testing. Independent exact bitsets checked 64 representative q,exponent cases and 96 two-prime gap formulas; all matched.

## originality

PASS

Thompson (2011) defined and studied φ-practical numbers, the squarefree criterion and Lemma 4.1 for adjoining a new prime (including prime powers); Pomerance–Thompson–Weingartner (2016) refined general asymptotics and primer-extension rules. Those are decisive precedents for the definition and some sufficiency directions, e.g. 15q and powers of a newly added q. Neither materially inspected full source states the exact odd support size-three classification with the {7,11,13} infinite exponent families and solitary 255, nor an all-three-exponents cofactor-gap proof. General prime-extension rules do not literally give arbitrary exponents of 3 and 5 when those primes already divide the number. A stronger known support theorem or table remains a residual risk; the novelty assertion is only the sharp bounded-support classification.

## value

PASS

Prime-factor support is the natural finite-complexity parameter in φ-practical-number theory, where no simple universal Stewart-like classification exists. The complete three-distinct-prime classification determines an infinite set of integer families and a sharp isolated exception, with an exact gap mechanism that distinguishes prime-power extensions. It is a motivated natural cutoff, not an arbitrary small-integer check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
