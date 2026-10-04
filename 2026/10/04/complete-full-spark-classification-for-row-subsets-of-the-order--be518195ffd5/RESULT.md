# Complete full-spark classification for row subsets of the order-\(14\) Fourier matrix
## Finding
Let \(\mathcal F_{14}=(\omega^{mn})_{m,n\in\mathbb Z_{14}}\), where \(\omega=e^{-2\pi i/14}\), and let \(\mathcal F_{14}[\mathcal M,:]\) be the rows indexed by a nonempty proper subset \(\mathcal M\subset\mathbb Z_{14}\). This row-selected harmonic frame is full spark if and only if \(\mathcal M\) is uniformly distributed over the divisors of \(14\) and, up to an affine map \(x\mapsto ax+b\) with \(a\in\mathbb Z_{14}^{\times}\), neither \(\mathcal M\) nor its complement is one of \(\{0,1,3,4\}\), \(\{0,1,2,3,6\}\), \(\{0,1,2,3,6,11\}\), or \(\{0,1,2,3,5,6,11\}\). The seven exceptional affine orbits occur in cardinalities \(4,5,6,7,8,9,10\), with the cardinality-seven orbit self-complementary. Equivalently, exactly \(1834\) nonempty proper row sets are full spark; among the \(2142\) uniformly distributed row sets, exactly \(308\) fail full spark.

The exceptional affine-orbit representatives of cardinality at most \(7\), together with one exact zero maximal minor for each, are:

| row representative | zero-minor column set | affine-orbit size |
| --- | --- | ---: |
| \(\{0,1,3,4\}\) | \(\{0,1,2,8\}\) | \(42\) |
| \(\{0,1,2,3,6\}\) | \(\{0,1,4,6,8\}\) | \(84\) |
| \(\{0,1,2,3,6,11\}\) | \(\{0,1,2,4,6,7\}\) | \(14\) |
| \(\{0,1,2,3,5,6,11\}\) | \(\{0,1,2,3,4,8,10\}\) | \(28\) |

The first three yield complementary exceptional orbits in cardinalities \(10,9,8\); the cardinality-seven orbit is self-complementary. The numbers of full-spark row sets by cardinality \(1,\ldots,13\) are
\[
14,42,210,168,336,126,42,126,336,168,210,42,14.
\]

## Assumptions and scope
The Fourier matrix is indexed by \(\mathbb Z_{14}\), and a row-selected frame with \(|\mathcal M|=m\) is called full spark when every \(m\times m\) maximal minor is nonzero. Uniform distribution means that for every divisor \(d\mid 14\), the counts of \(\mathcal M\) in residue classes modulo \(d\) differ by at most one; it suffices here to check \(d=2\) and \(d=7\).

The statement is a finite classification at Fourier order \(14\). It does not assert a characterization for arbitrary composite orders.

## Proof
Alexeev--Cahill--Mixon prove that uniform distribution is necessary for a row-selected discrete Fourier frame to be full spark at arbitrary order. Thus it remains to classify the \(2142\) nonempty proper uniformly distributed subsets of \(\mathbb Z_{14}\).

Full spark is invariant under affine maps \(x\mapsto ax+b\) with \(a\in\mathbb Z_{14}^{\times}\): multiplication by \(a\) permutes Fourier columns and translation by \(b\) applies nonzero column scalings. Complementary-minor symmetry for the invertible Fourier matrix identifies the full-spark status of \(\mathcal M\) with that of its complement. Exact enumeration gives \(38\) affine orbits of uniformly distributed sets, and complement symmetry reduces the verification to \(20\) orbits of cardinality at most \(7\).

For each of those \(20\) representatives and each choice of \(|\mathcal M|\) columns, the determinant is an algebraic integer in \(\mathbb Z[\zeta_{14}]\). The verifier reduces it through two homomorphisms
\[
\zeta_{14}\mapsto4\in\mathbb F_{29},\qquad
\zeta_{14}\mapsto2\in\mathbb F_{43},
\]
where the target elements have exact order \(14\). If a complex determinant vanished, its integer determinant polynomial would be divisible by
\[
\Phi_{14}(X)=X^6-X^5+X^4-X^3+X^2-X+1,
\]
so it would vanish under both reductions. Therefore a nonzero value in either finite field certifies a nonzero complex minor.

Across \(33086\) maximal-minor tests, exactly the four representatives displayed above have minors vanishing in both reductions. For each of these four, the displayed witness determinant is then expanded as an integer polynomial and reduced exactly modulo \(\Phi_{14}\); the remainder is identically zero, proving genuine complex singularity rather than merely modular singularity. Every other low-cardinality affine orbit has every maximal minor certified nonzero. Affine invariance and complement symmetry then complete the classification.

The four low-cardinality bad orbits and the complements of the first three comprise exactly \(308\) uniformly distributed sets. Subtracting them from the \(2142\) uniformly distributed sets gives \(1834\) full-spark nonempty proper row sets.

## Verification
The standalone script `verify_z14_fullspark.py` uses only exact integer and finite-field arithmetic. It independently enumerates all uniformly distributed subsets, affine orbits, complementary classes, all maximal minors of all low-cardinality representatives, and exact cyclotomic zero witnesses. A successful replay ends with `VERIFY_OK` and reports \(2142\) uniformly distributed sets, \(38\) affine orbits, \(20\) low-cardinality orbits, \(308\) exceptional sets, and \(1834\) full-spark sets.

## Relationship to prior work
Alexeev, Cahill, and Mixon, *Full Spark Frames* (arXiv:1110.3548), prove the prime-power sufficiency theorem, general necessity of uniform distribution, and give the order-\(10\) uniformly distributed counterexample. Osgood, Siripuram, and Wu, *Discrete Sampling and Interpolation: Universal Sampling Sets for Discrete Bandlimited Spaces* (arXiv:1204.0992), develop the equivalent universal-sampling formulation with a complete prime-power characterization. Achanta et al., *Coprime Conditions for Fourier Sampling for Sparse Recovery* (DOI:10.1109/SAM.2014.6882460), study composite orders and partially treat the product-of-two-primes setting through restricted families.

Targeted searches using full-spark, universal-sampling, partial-DFT, affine-orbit, explicit-row-set, and order-\(14\) formulations did not locate a prior complete order-\(14\) classification. The theorem here therefore supplies an exact finite boundary case beyond the prime-power result while retaining an explicit residual literature risk.

## Limitations
The classification is specific to order \(14\). The nonvanishing proof is a complete finite certificate rather than a general symbolic characterization of composite Fourier orders. Literature searches cannot rule out an unindexed or differently phrased prior statement. Independent audit has not been performed.

## References
1. B. Alexeev, J. Cahill, and D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548, first public version 2011-10-17.
2. B. Osgood, R. Siripuram, and W. Wu, *Discrete Sampling and Interpolation: Universal Sampling Sets for Discrete Bandlimited Spaces*, arXiv:1204.0992.
3. A. Achanta, S. Biswas, B. Dasgupta, A. Jacob, B. N. Dasgupta, and R. Mudumbai, *Coprime Conditions for Fourier Sampling for Sparse Recovery*, IEEE SAM 2014, DOI:10.1109/SAM.2014.6882460.
