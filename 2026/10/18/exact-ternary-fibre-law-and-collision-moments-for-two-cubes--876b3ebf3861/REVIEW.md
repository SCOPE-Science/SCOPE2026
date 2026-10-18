# Review of the ternary two-cube fibre law

## Correctness — PASS

The statement uses complete ordered residue pairs, the normalization \(F_n=3^{-n}R_n\), and normalized target Haar measure. The essential unit-cube lemma follows from the explicit polynomial \(t+3t^2+3t^3\) and its derivative congruent to one modulo three, so it does not rely on Hensel lifting at a singular point of the two-variable sum. The five residue classes and the exceptional double-nonunit branch partition the input probability space, with total mass one. The resulting density recurrence yields the exact normalized finite-level formula and collision identity; its two numerical base cases are derived separately. The valuation-annulus argument proves both directions of the sharp \(L^s\) threshold and the absence of a singular probability atom. The saved `verify.py` independently recomputes all target counts through modulus \(3^8\), and exact rational moments through exponent eleven. These finite checks support but do not replace the general proof.

## Originality — PASS within inspected evidence

The 2021 work of Brüdern and Vaughan employs the same two-cube congruence count \(\rho(q,a)\) and establishes global variance results, but the inspected article does not give the present all-depth ternary target-fibre formula or its \(L^s\) threshold. Seraj's 2022 formula concerns residues of one power, rather than additive two-cube fibres or moments. Bories' explicit nondegenerate Newton-polyhedron formula does not directly cover the singular residue-characteristic-three case: the gradient of \(x^3+y^3\) vanishes identically modulo three. Targeted published-index and literature searches, together with comparisons against accessible earlier claims on generic odd primes and the dyadic case, did not locate an equivalent full ternary law. No absence-of-results claim is based on an uninspected source; a more general specialized singular-local-zeta computation remains possible.

## Mathematical value — PASS

The exception at the prime dividing the degree is mathematically forced: the usual nonsingular lifting hypotheses fail there. For the natural additive representation invariant \(x^3+y^3\), the result classifies every target at every ternary power, gives an exact rational formula for the collision energies, and identifies a sharp global integrability boundary of the limiting fibre density. The elementary modulo-nine obstruction is acknowledged as known and is not the asserted value. This is a complete local classification at the wild prime, not a finite table or a numerical estimate.

## Closest literature and residual limits

- J. Brüdern and R. C. Vaughan, *A Montgomery–Hooley Theorem for sums of two cubes*, European Journal of Mathematics 7 (2021), doi:10.1007/s40879-021-00495-4; same arithmetic map and congruence counts, different global-asymptotic conclusion.
- S. Seraj, *Counting general power residues*, Notes on Number Theory and Discrete Mathematics 28 (2022), doi:10.7546/nntdm.2022.28.4.730-743; single-power image cardinality, without additive two-variable multiplicities.
- B. Bories, *Igusa's p-adic local zeta function associated to a polynomial mapping and a polynomial integration measure*, arXiv:1012.5087; nondegenerate framework inapplicable directly in residue characteristic three.

The derivation is for local residue pairs, not global integer representations; no independent verification or absolute priority claim is made. A source with an implicit or explicit singular-characteristic-three computation could still subsume part of this result.

Self-review: passed. Independent audit: not yet performed.
