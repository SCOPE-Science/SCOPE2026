# Review of exceptional-prime and Frobenius classification

## Correctness: PASS
The explicit twelve hyperflex and sixteen ordinary line equations restrict the Fermat quartic to perfect squares (or fourth powers) in every odd characteristic, and the classical 28-bitangent theorem establishes completeness. Exhausting the triple-line determinants in the integer cyclotomic ring produces 60 zero determinants and a complete 3216-entry nonzero norm spectrum, whose odd prime support is precisely 3, 5, 17. These norms rule out additional concurrent triples for all other odd primes. Exact finite-field incidence enumeration at these three primes and the pair count 378 cover all geometric crossings. Permuting coefficient exponents by q-power Frobenius then gives the full stated orbit table. The standalone verifier actually reproduced all of these finite exact checks and ended in `VERIFY_OK`.

## Originality: PASS (best-knowledge; qualified)
The twelve-plus-sixteen line construction and the complex \(288,0,15\) count **are known** and expressly excluded from the novelty claim. Edge and Janasz--Pokora--Zieliński cover these ingredients; the latter primary paper explicitly works over the complex numbers. The evaluated claim is the exhaustive odd-prime degeneration law (exactly 3, 5, 17), each special-stratum count, and the corresponding q-Frobenius orbit and zeta data. Direct inspection of the nearest primary material and semantic comparisons found no such combined result. Full historical priority is uncertain: existing explicit bitangent coordinates may permit a derivation, and obscure older arithmetic literature could contain related tables.

## Mathematical value: PASS
The reduced intersection locus of all 28 classical bitangents is a natural finite invariant of a distinguished plane quartic. Its exact arithmetic bad-reduction spectrum and uniform finite-field zeta data extend a classical incidence description to arithmetic geometry, including qualitative concurrency jumps and unexpected triple strata. The all-prime norm certificate and full geometric-and-arithmetic case distinctions provide substantially more than a small numerical example.

## Closest prior work and scientific limits
Edge treats the classical configuration; Plaumann--Sturmfels--Vinzant and Dalla Piazza--Fiorentino--Salvati Manni provide general bitangent theory. Janasz--Pokora--Zieliński establish the complex \(288,0,15\) incidence census, and Bethea--Brazelton analyze geometric symmetry actions. The result is for reduced crossing supports of the literal diagonal quartic in odd characteristic; neither nonreduced Jacobian singular structure nor twists nor characteristic two are addressed. No independent scientific audit has been conducted.

Self-review: passed. Independent audit: not yet performed.
