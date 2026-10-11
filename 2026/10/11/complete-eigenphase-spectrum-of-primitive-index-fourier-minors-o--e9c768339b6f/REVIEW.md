# Scientific review: primitive-index Fourier eigenphases

## Correctness — PASS

The statement covers every odd \(N\ge3\), with the positive-sign, \(N^{-1/2}\)-normalized Fourier compression on unit residues. Its proof derives both the exact Ramanujan Gram kernel and the stronger **complex** identity \(A^2=KR\). For an odd repeated prime factor, \(K\) is a residue-fiber projection, the unit quadratic trace cancels exactly, and the reflection trace vanishes; these facts force equal fourth-root eigenspace multiplicities. For an odd first-power prime, the constant eigenline splits off and the classical quadratic Gauss sum determines the remaining fourth-root imbalance. Chinese remaindering includes the necessary local additive twists and gives a genuine similarity, not merely equality of singular values. Eigenspace projectors and the rank and nonzero-conditioning consequences follow from the proven normal decomposition.

A standalone standard-library checker completed local Fourier identities, trace-power tests and Chinese remainder congruences. A separate numerical eigensolver comparison across nineteen moduli agreed with the exact proposed multiset. Finite computations do not establish the infinite theorem; the full proof does.

## Originality — PASS, qualified

The closest prior material is the classical discrete Fourier fourth-root eigenspace decomposition (Horn, 2010), Ramanujan arithmetic transforms (Planat–Minarovjech–Saniga, 2008), and the rank/principal-minor literature (Delvaux–Van Barel, 2006/2008; Caragea–Lee, 2024). Those inspected results do not give this **unit-indexed principal compression's** all-modulus complex eigenvalue multiplicities and projectors. Earlier exact valuation-shell concentration spectra yield the Gram singular values at prime-power parameters, but not the signs, fourth-root eigenphases, isolated first-power eigenline, or phase-dependent multiplicities. Earlier primitive-row frame-potential results control pair correlations, not the compressed Fourier operator's complex eigenspaces. An inspected published-finding index returned nearby principal-minor and rank results but no explicit covering eigenphase theorem.

The 2006/2008 rank-deficiency paper was available through an abstract and bibliography, but its complete text could not be inspected; an equivalent eigenphase description there or elsewhere remains a genuine historical-priority risk. The absence of a search hit alone is not considered evidence of novelty. No independent historical priority certification is claimed.

## Mathematical value — PASS

Unit residues form the canonical primitive set for cyclic Fourier sampling. Its principal Fourier matrix is a natural structured operator, and the complete complex eigenspectrum is stronger than a rank or singular-value calculation: it gives exact eigenspace projectors and all arithmetic phase multiplicities, including the local \(1,-1,i,-i\) equal-split phenomenon and the Legendre-symbol-dependent splitting at first-power primes. The global tensor law covers every odd modulus and yields an explicit arithmetic conditioning corollary. This answers a natural spectral classification question rather than an arbitrary finite table entry. The work makes no claim about general principal Fourier minors or even moduli.

## Limits and closest references

The sign convention must be preserved. The rank/singular spectrum at repeated prime powers is related to known shell-localization formulas; only the complex eigenphase decomposition is assessed as the contribution. The quadratic Gauss-sum sign is classical. The comparison to the older rank-deficiency paper remains incomplete because its full text was unavailable. Sources: arXiv:0812.2170v1; Horn, DOI:10.1080/0035919X.2010.510665; arXiv:2409.09793; Delvaux–Van Barel, DOI:10.1016/j.laa.2008.04.043.

Same-model review: passed. Independent audit: not yet performed.
