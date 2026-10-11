# Independent mathematical audit

## correctness

PASS

The finite claim was reconstructed from the exact Example 6.1 generators over \(\mathbb F_5[x]/(x^8-1)\). Row-reducing all cyclic shifts gives dimensions eight for \(C\) and \(D\), rank sixteen for the stacked generators, and an eight-dimensional exact nullspace for \(D^\perp\). I independently enumerated all \(5^8=390625\) words of \(C\) and all \(5^8\) words of \(D^\perp\). Both ordinary Hamming histograms are exactly \(1,704,1992,8000,21280,45696,79856,96768,80160,45504,10664\) at weights \(0,7,\ldots,16\), respectively. The composition \((9,0,0,1,6)\) occurs eight times in \(C\) and zero times in \(D^\perp\), while their minimum-weight layers occupy 48 and 20 ordered composition types. This reproduces the package certificate and verifier independently, so equality of Hamming spectra and permutation inequivalence are both certified exactly.

## originality

PASS

The primary LCP paper prints the exact Example 6.1 polynomial generators and proves only that the pair has length sixteen, dimension split eight plus eight, and optimal security parameter seven. A full-text search of that paper found no weight-enumerator statement. The paper separately notes that general quasi-cyclic LCPs need not have \(C\) permutation equivalent to \(D^\perp\), but that general existence fact does not imply inequivalence for this Example 6.1 pair, much less the stronger fact that its two security sides have identical complete ordinary Hamming spectra. The separating composition census is additional same-example information requiring exact code enumeration. Current Resultary searches for the exact parameters, source example, Hamming-isospectral property, and complete composition returned no prior statement of these invariants.

## value

PASS

Example 6.1 is a published optimal-security quasi-cyclic LCP, so distinguishing the two security-side codes is mathematically motivated. The exact fact is stronger than merely finding another inequivalent LCP: the sides agree at every ordinary Hamming weight, showing that the standard spectrum misses their inequivalence, while a concrete complete-composition coefficient separates them. That gives a precise reusable benchmark for equivalence tests on a natural published code and satisfies the narrow-exact-invariant value standard.

The dated certificate retains the supplied scientific assessment, sources and limitations.
