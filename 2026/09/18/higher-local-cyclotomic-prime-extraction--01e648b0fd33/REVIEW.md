# Review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

The proof was checked from the Möbius product rather than inferred from numerical data. The key split is exact: for a squarefree index n=m r, the divisor factors supported on m equal Phi_m(x)^{mu(r)}. After removing them, the remaining Möbius exponents have total sum zero and the unique smallest remaining divisor is the next prime q. The resulting l-adic power series has first nonconstant term +/-x^q, with unit coefficient, forcing valuation q nu_l(x).

For odd l, the competing branch differs by Phi_m(x)^2; its valuation is exactly nu_l(x) because Phi_m(x)-1 has that valuation while Phi_m(x)+1 is an l-adic unit. For x=2, the competing branch has valuation p_1+1, using the squarefree least-prime congruence. In the odd-squarefree case q>=p_1+2, so there is no tie and taking the larger of the two integer valuations recovers q at every stage.

Adversarial checks included the parity of the remaining Möbius factor, negative exponents in the product, the need for m to contain the smallest already recovered primes, and the exceptional even-squarefree scale collision at (2,3). The public verification script separately checks thousands of exact finite instances at multiple bases and local primes; it is supporting evidence rather than a substitute for the general proof.

## Originality

The motivating source, Shunia's arXiv:2609.18480 (submitted 16 September 2026), was inspected in full in the relevant sections. Its local result recovers the least prime from Phi_n(2)+1 and then obtains further primes locally by applying that least-prime identity to quotient indices. Its fixed-target successive peeling theorem is Archimedean, using logarithmic fingerprints and rounding. It does not state the corrected higher local residual identity, the sign-free odd-prime valuation pair, or the fixed-target binary recursion proved here.

Pomerance--Rubinstein-Salzedo's *Cyclotomic Coincidences* was also inspected in the relevant sections. It supplies the classical Möbius product and real dominance estimates used in the surrounding literature, but no matching p-adic prefix-residual extraction theorem was found.

External searches used exact and synonymous forms involving Phi_n(2), Phi_m(2), successive prime divisors, p-adic/2-adic valuation, squarefree indices, cyclotomic factor peeling, and corrected residuals. No prior statement matching the theorem was found. The originality assessment is therefore to the best of our knowledge, not an exhaustive literature guarantee.

No inaccessible paper was identified whose title, abstract, citation context, or available metadata specifically suggests the same result. The main residual risk is unindexed contemporaneous work because the motivating preprint is extremely recent.

## Value

The result supplies an exact local counterpart to the recent paper's Archimedean successive peeling. It upgrades least-prime local extraction to a recursive higher-prime mechanism, gives a base-independent l-adic theorem after a known prefix, removes the unknown Möbius sign at every odd local prime, and yields a particularly simple all-stage binary recursion for odd squarefree indices. The formulas are structural identities rather than isolated parameter computations.

## Scope

The result is not presented as an efficient factorization algorithm. Its inputs can be enormous, and computing cyclotomic values at large indices may dominate any practical use. The theorem concerns exact arithmetic information encoded in those values.
