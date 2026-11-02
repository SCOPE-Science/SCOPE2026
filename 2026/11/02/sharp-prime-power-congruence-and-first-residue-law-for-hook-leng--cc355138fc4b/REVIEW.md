# Scientific review: sharp prime-power hook/core discrepancy

## Correctness — PASS

The identities hold in the integral formal power-series ring. The proof begins with the exact ratio of the two Euler-product generating functions, telescopes it through the prime-power levels, and controls every omitted binomial term using the inequality \(\nu_p(p^r\binom{p^k}{r})\geq k+r-\nu_p(r)\). It treats \(p=2\) separately because its quadratic binomial term survives at the leading precision. The inverse-divisor expansion follows from the local Euler factor and the dyadic correction from divisor-count parity. The unit constant term and first nonzero correction prove the sharp modulus and first failure. Reproducibility checks independently match 1,392 coefficient predictions across twelve choices of prime and exponent. Finite checks are not the proof.

## Originality — PASS, with residual priority risk

The closest source, Sharma (arXiv:2610.01422; first public 2026-10-01), proves a weaker modulus \(p^a\) for \(t=p^a\) and modulus \(p^2\) for \(a=1\). Its inspected proof and discussion do not give the sharp modulus for arbitrary \(a\), the first failure degree, or the complete leading error profile. Han–Ono (arXiv:0805.2461) treats simultaneous zero sets at \(t=3\). The accessible OEIS A000731/A033687 entries record special coefficient sequences but not the all-prime-power correction laws. Targeted literature, earlier research, and equivalence searches yielded no identified covering result. The elementary p-adic lifting device is standard, so unindexed general theorems could still subsume this specialization; this is a priority risk rather than a claim of demonstrated global uniqueness.

## Mathematical value — PASS

The exact p-adic strength of the coefficient comparison is a natural next question after the published prime-power dichotomy. The theorem answers it for *all* primes and prime-power exponents, determines the earliest obstruction, and gives the entire first residue layer. In odd characteristic the obstruction is governed by inverse-divisor sums; in characteristic two it acquires a distinct square-theta correction. These descriptions make the arithmetic mechanism and the exceptional prime \(2\) explicit, beyond a one-coefficient witness or a routine restatement of the existing congruence.

## Boundaries and follow-up risks

No higher-order normalized correction, non-prime-power classification, or new hook-length identity is claimed. The source inspection is extensive but cannot rule out unindexed general p-adic Euler-product congruences. Independent verification of priority and proof remains outstanding.

Self-review: passed. Independent audit: not yet performed.
