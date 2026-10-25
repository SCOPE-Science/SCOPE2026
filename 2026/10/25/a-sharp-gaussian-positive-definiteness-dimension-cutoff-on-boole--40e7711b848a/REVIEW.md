# Scientific review: Gaussian positivity cutoff on Boolean Hamming cubes

## Correctness — PASS
The result is an all-dimension theorem in the stated strong-damping range, rather than a finite computational observation. The Walsh eigenvalues follow directly from finite-group character orthogonality and Hamming-shell multiplicity counts. For \(dq\le2\), the nonzero-weight tail is bounded uniformly by \((e^2-3)q^2<q\), forcing the unique lowest eigenvalue to be the parity character. Alternating-tail dominance proves strict positivity for every \(d\le\lfloor q^{-1}\rfloor\); the same uniform bound proves a negative parity eigenvalue two dimensions later. The dimension restriction argument is exact. The parameter derivative bound proves uniqueness of each critical root; the local Taylor estimates prove its asymptotics. The standalone checker independently compared 327 exact/rational character identities and neighborhood-ordering assertions and bracketed four roots at high precision.

## Originality — PASS, bounded literature review
The earliest public historical source is the 2012-09-19 Harrow–Kolla–Schulman preprint (arXiv:1209.4148); its Fourier/Krawtchouk framework analyzes spherical maximal operators, not squared-Hamming Gaussian covariance positivity. Feragen–Lauze–Hauberg (arXiv:1411.0296) and Jayasumana and coauthors (arXiv:1412.0265) study Gaussian positive definiteness for general metrics and manifolds, not the exact Boolean cube parameter–dimension boundary. Searches for squared Hamming Gaussian, parity Walsh obstruction, dimension cutoff and Krawtchouk Fourier transform found no directly dominating indexed statement. Existing general harmonic criteria yield the eigenvalue formula, but do not by themselves settle which eigenvalue is minimal or give the single-integer threshold. The possibility of older unindexed equivalent work remains a real limitation.

## Mathematical value — PASS
The Hamming graph Gaussian is a standard metric-induced covariance candidate, but its squared-Hamming exponent destroys the automatic positive-definiteness property of the chordal Euclidean Gaussian. The exact dimension limit answers when the **complete** Boolean cube is a valid covariance domain for a specified damping, and isolates one rank-one spectral degeneration at the threshold. The one-integer-width cutoff, parity-only obstruction and asymptotic correction are structural, applicable to arbitrarily large dimensions, and not a recomputation of a finite table. The weak-damping phase diagram is unproved and not included.

## Remaining limitations
The parameter range is \(0<q\le1/16\). The classification is not extended to all bandwidths, and no independent audit has checked the mathematics or novelty. Accessible primary sources cover the relevant general Gaussian-kernel and Hamming-harmonic frameworks, but the review cannot exclude a synonymously stated older result.

Self-review: passed. Independent audit: not yet performed.
