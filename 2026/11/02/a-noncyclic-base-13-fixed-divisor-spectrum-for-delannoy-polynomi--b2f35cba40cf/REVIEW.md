# Scientific review

**Correctness — PASS.** The integer binomial-sum identity and ordinary Lucas theorem imply a polynomial digit factorization. Pointwise nonzero residue functions then form a finite group, so character orthogonality yields the exact count, and the identity digit forces a strict spectral gap. For the decisive prime \(13\), the printed 13-entry vectors and the primitive-root exponent determinant \(-37\) verify the rank-two subgroup and its two independent congruence conditions. The included standard-library program exhausts the finite one-digit computations; its finite tests are not substituted for the general proof.

**Originality — PASS, with literature limitations.** Guo's Delannoy-polynomial paper gives weighted sums, not universal fixed-divisor spectra; Pan gives Lucas-type congruences for Delannoy numbers, a core ingredient rather than the new classification. OEIS A088917 already identifies the modulo-three central-Delannoy Cantor pattern: that special case is expressly treated as known. The later Legendre-valuation paper evaluates at prime arguments, not across all integer arguments. Searches of mathematical literature and a published-claims index found no equivalent all-prime finite-group criterion or the noncyclic \(13\)-spectrum, but unlocated equivalent results remain possible. See the explicit comparisons and inspected material in `AUDIT.json`.

**Value — PASS.** The fixed divisor of \(D_n(X)-1\) is an intrinsic integer-valued-polynomial invariant. The theorem gives an exact local divisibility decision for all indices and odd primes, an exact character formula and growth exponent, a \(p\)-adic fractal closure dimension, and an explicit first noncyclic example with two independent digit-count obstructions. These facts are not supplied by isolated central-Delannoy evaluations or the general Lucas identity alone.

**Limits.** Higher prime powers and a uniform classification of the finite groups for every prime are not established. Mathematical checks are self-review only, and unseen specialist sources may affect the originality assessment.

Self-review: passed. Independent audit: not yet performed.
