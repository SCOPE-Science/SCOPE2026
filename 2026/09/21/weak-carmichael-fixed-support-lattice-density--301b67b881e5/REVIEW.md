# Same-model review

## Correctness

**PASS.** The weak-Carmichael criterion gives, for each fixed prime support, exactly the coordinate congruences defining the kernel of the finite-group homomorphism \(\Psi_S\). The kernel is therefore a full-rank finite-index sublattice of \(\mathbb Z^s\). The primitive-power definition is equivalent to divisibility of the exponent vector inside this lattice: \(n(e)=m^f\) with weak Carmichael \(m\) if and only if \(e\in f\Lambda_S\). In a lattice basis this is exactly coprimality of the basis coordinates.

The counting argument was rederived from first principles. Fixed-support height \(n\le X\) becomes a weighted simplex of scale \(L=\log X\). Standard fixed-lattice point counting gives the stated main term and boundary error. Möbius inversion over lattice content gives the factor \(\sum_{d\ge1}\mu(d)d^{-s}=1/\zeta(s)\); the accumulated boundary error is \(O(L\log L)\) for \(s=2\) and \(O(L^{s-1})\) for \(s\ge3\). The two-prime specialization agrees with Meštrović's exact exponent divisibility criterion.

The standalone exact verification checked 2,184 exponent vectors on five admissible supports. It found 508 weak Carmichael vectors and 363 primitive ones; the two-prime normalized-gcd criterion had zero mismatches. Exact logarithmic-height counts also approach the predicted volume constants and primitive proportions. The computation is supporting evidence, not a substitute for proof.

## Originality

**PASS, to the best of our knowledge.** Meštrović's 2013 primary source was inspected around the Borwein--Wong criterion (Theorem 2.4), support construction/obstruction (Proposition 2.6), primitive definition (Definition 2.25), and exact two-prime exponent condition (Proposition 2.36). These prior ingredients are explicitly separated from the present contribution.

Targeted searches for `weak Carmichael exponent lattice`, `primitive weak Carmichael density`, `fixed prime factors/support`, and `zeta` formulations did not locate the arbitrary-support kernel-lattice theorem, the identification of primitive weak Carmichael numbers with primitive lattice vectors, or the fixed-support \(1/\zeta(s)\) density. A 2026 Meštrović preprint was inspected through its accessible full text; searches for `lattice`, `primitive weak`, `zeta`, and fixed-support language did not locate an equivalent result. Current OEIS A225498 and A087442 and the SCOPE archive were also checked.

The strongest unresolved prior-art risk is E. Wong's 1997 MSc thesis *Computations on Normal Families of Primes*. Meštrović explicitly attributes the general support construction to §2.5.3 of that thesis. An archived thesis link is recorded by OEIS A050474, but the thesis itself was not inspected here. It could contain an exponent-structure formulation. No available source gave evidence that it contains the lattice-primitivity or \(1/\zeta(s)\) density theorem. The Borwein--Wong survey and subsequent Meštrović papers were also considered, but no equivalent statement was located.

## Value

**PASS.** The result turns the exponent problem on every fixed admissible prime support into a canonical finite-index lattice, giving a basis-independent primitive criterion and a uniform asymptotic law. The limiting primitive proportion \(1/\zeta(s)\) is independent of the particular primes, while the support only enters through the lattice index and logarithmic weights. The two-prime case gives an explicit gcd classification, and higher-support examples show why ordinary gcd of the standard exponents is insufficient.

## Limitations

The result is fixed-support: it does not estimate weak Carmichael numbers while the primes themselves vary. Error constants depend on the support. Originality remains conditional on the documented search and is not a claim that all historical literature has been exhausted.

**Same-model review: passed. Independent audit: not yet performed.**
