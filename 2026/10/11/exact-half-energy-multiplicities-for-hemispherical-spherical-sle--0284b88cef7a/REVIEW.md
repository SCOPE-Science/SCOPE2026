# Same-model review

## Correctness
PASS. In a fixed order, associated-Legendre parity makes the same-parity hemisphere Gram blocks exactly \(\tfrac12 I\). A Sturm--Liouville Lagrange identity factors every opposite-parity entry into nonzero row and column factors times \(1/(k(k+1)-\ell(\ell+1))\). The resulting rectangular Cauchy matrix has full rank, so the block spectrum is exactly \(1/2\) plus and minus its nonzero singular values, with nullity equal to the parity-count imbalance. The global count follows from the \(m=0\) singleton and the duplicated \(\pm m\) blocks. The packaged numerical checker agrees on 1298 independently assembled blocks, but the proof does not rely on those finite tests.

## Originality
PASS. The closest primary source, arXiv:math/0408424v1, supplies the spherical Slepian framework, low-pass localization matrices, complementarity, and polar-cap machinery, but the inspected text does not state an exact hemispherical \(1/2\)-eigenspace law. DOI:10.1093/gji/ggs122 explicitly introduces bandpass Slepian functions by omitting low degrees and treats the needed changes as straightforward dimensional adaptations; it does not give the hemisphere parity decomposition, Cauchy factorization, or exact threshold multiplicity. Ramamoorthi's 2002 hemisphere orthogonality calculation is a low-order Lambertian PCA application with additional spectral weights, not the arbitrary-mask concentration theorem. Semantic-index and web searches under equivalent hemisphere, bandpass, parity, Cauchy, and associated-Legendre formulations found no statement implying the claim. The remaining risk is terminology drift into special-function or approximation literature.

## Value
PASS. The value is structural: \(1/2\) is the exact transition between predominantly inside- and outside-hemisphere Slepian modes, and the theorem determines its multiplicity for every low-pass, bandpass, or gapped degree mask without diagonalizing the concentration matrix. The low-pass corollary gives an exact \(L+1\)-dimensional transition space and exact counts on both sides, while the arbitrary-mask law shows that threshold degeneracy is controlled by a discrete parity invariant rather than solely by the Shannon trace.

## Closest literature and limitations
The known spherical Slepian theory supplies the concentration problem and its numerical machinery. The later bandpass literature supplies a natural motivation for deleting degree ranges. The new statement does not provide closed forms for the off-centre eigenvalues; it gives their reflection pairing and the exact central multiplicity. A hidden equivalent formulation in older hemisphere-restriction literature remains the principal originality risk.

Same-model review: passed. Independent audit: not yet performed.
