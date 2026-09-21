# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was checked adversarially at the following points.

1. Writing the middle prime as \(q=h-1\) and the common difference as \(d\), direct reduction modulo \(p+1=h-d\), \(q+1=h\), and \(r+1=h+d\) gives exactly
   \[
   h-d\mid d(2d-3),\quad h\mid d^2,\quad h+d\mid d(2d+3).
   \]
   Sign changes do not affect divisibility.
2. If \(g=(h,d)\), \(h=gu\), \(d=gv\), then \((u,v)=1\). From \(h\mid d^2\), the implication \(u\mid g\) is valid, so \(g=uw\) and \(h=u^2w,d=uvw\).
3. Cancelling \(uw\) in the two outer divisibilities is legitimate. Coprimality with \(v\) reduces them to divisibility of the same odd integer \(2v^2w-3\) by \(u-v\) and \(u+v\).
4. Same parity would force \(u,v\) both odd, making the even number \(u-v\) divide an odd integer, so the parity conclusion is necessary. Under opposite parity, \(\gcd(u-v,u+v)=1\), hence their product is exactly the combined modulus.
5. The converse was checked by reversing each equivalence; no primality or squarefreeness condition is silently inferred from the divisibility algebra. The theorem explicitly assumes the three displayed factors are prime.
6. Uniqueness follows because \((q+1)/d=u/v\) is already in lowest terms, after which \(w\) is determined.
7. The fixed-shape admissibility argument separately handles primes dividing the ray modulus, the parity prime 2, and primes not dividing the modulus. For an odd \(\ell\mid u^2-v^2\), the ray congruence makes none of the three forms zero modulo \(\ell\). For \(\ell\nmid M\), at most three residue classes are excluded; \(\ell=2,3\) are handled explicitly. Thus the Dickson corollary has no hidden local obstruction.

The standalone exact computation enumerates all 186647 three-term arithmetic progressions of odd primes with largest term at most 20000. Direct Lucas–Carmichael testing and the parametrization each select 73 triples, with zero mismatches. A second check compares the original divisibilities with the one-ray condition in 226000 bounded shape/residue cases, again with zero mismatches. These checks support but do not replace the proof.

Correctness verdict: PASS.

## Originality

The closest located prior sources were inspected as follows.

- OEIS A006972 was checked for the definition, data, and construction comments. It records general Lucas–Carmichael numbers and a 2020 sufficient-condition comment for three factors, but not the arithmetic-progression classification proved here.
- OEIS A290810 explicitly gives the family \((6m-1)(12m-1)(18m-1)\). This is prior art and is not claimed as new; the present theorem identifies it as the \(u:v=2:1\) ray inside the full classification.
- OEIS A262723 records products of three distinct primes forming an arithmetic progression, but does not impose or characterize the Lucas–Carmichael divisibility.
- Wright, arXiv:1609.00231 / Bull. London Math. Soc. 50 (2018), was inspected in accessible full text. Its purpose is unconditional infinitude of Lucas–Carmichael and elliptic Carmichael numbers. Full-text searches for `three prime`, `6k`, and `Chernick` returned no matches; `arithmetic progression` occurs in the analytic prime-distribution machinery, not as a classification of equally spaced prime factors.
- Einsele–Paterson (2024), *Average case error estimates of the strong Lucas test*, was inspected in accessible HTML, especially its three-prime Lucas–Carmichael section. It develops a gcd-normalization and upper bounds in a fixed-discriminant setting. No `arithmetic progression` occurrence was found, and no specialization equivalent to the present \(u,v,w\) criterion was located.
- Exact and synonymous searches covered `Lucas-Carmichael arithmetic progression`, `prime factors in arithmetic progression`, `equally spaced`, `p-d,p,p+d`, `q+1 divides d^2`, the formula \(u^2-v^2\mid2v^2w-3\), and the displayed negative-Chernick forms. These searches recovered the known A290810 subfamily but not the complete converse/parametrization.
- The current SCOPE archive was searched for Lucas–Carmichael/arithmetic-progression terminology; no overlapping record was found.

Residual risk is concentrated in older sources that were identified but not inspected in full: Richard Guy, *Unsolved Problems in Number Theory*, 3rd ed. (2004), §A13, and J.-M. De Koninck, *Ces nombres qui nous fascinent* (2008), Entry 399. Both are plausible places for older constructions or parametrizations. Older recreational/sequence material using different notation is another residual risk. This is therefore an originality assessment only to the best of our knowledge.

Originality verdict: PASS, to the best of our knowledge.

## Value

The theorem upgrades a known isolated arithmetic-progression construction into an if-and-only-if classification of all Lucas–Carmichael numbers with exactly three prime factors in arithmetic progression. The normalization separates the problem into a primitive rational shape \(u:v\) and one explicit congruence ray for \(w\). This gives a reusable generation criterion, explains the classical negative-Chernick family structurally, and exposes the remaining difficulty as simultaneous primality of three admissible linear forms. The Dickson-conjecture corollary shows that every primitive opposite-parity shape is expected to contribute infinitely many examples.

Value verdict: PASS.
