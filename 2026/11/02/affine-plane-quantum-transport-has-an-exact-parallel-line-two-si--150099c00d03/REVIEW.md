# Scientific review

## Correctness — PASS

The theorem is specified for every finite affine plane of order \(q\ge3\), uniform adjacency hopping and precisely two positive-rate absorbing sites. Its proof is reconstructed from the incidence identities, all five exact spectral projectors, positivity of the two-sink Gram determinants, zero-eigenvalue parallel-line rank, and strict decay of the bright subspace. The incident point–line four-valued local law follows from explicit two-by-two inversion and seven site types. `symbolic_check.py` reproduces the determinants and local identities exactly, while `affine_check.py` independently diagonalizes the full matrix for 475 absorber placements of prime orders 3, 5 and 7, checking all their site probabilities. The finite checks are evidence, not a substitute for the all-plane analytic proof.

## Originality — PASS on examined evidence, with historical risk

Varbanov, Krovi and Brun (2008) provide quantum hitting-time foundations. Novo et al. (2014/2015) establish the general Krylov-subspace method. Le et al. (2017) analyze dark states. Razzoli, Paris and Bordone (2020/2021) give single-trap transport for selected families. Their inspected texts do not give the two-absorber incidence-plane dimension table, the rank loss for parallel line traps, or the incident mixed-trap site distribution. Previous strongly regular and Hamming-network analyses do not imply this biregular five-eigenvalue case. Searches of affine/Levi incidence, two-sink, parallel-class, and spectral-design aliases found geometric-topology entries but no matching statement. This is evidence-based best-knowledge originality, not an assertion that no inaccessible source exists.

## Mathematical value — PASS

An affine-plane Levi graph has a natural, highly structured arrangement of possible absorber sites. The explicit 6/7/8 bright-mode trichotomy determines exactly which two-site placements maximize average capture, and identifies a parallel-class penalty that survives every positive sink-rate choice. The four-valued incident mixed-pair site law supplies a nontrivial local transport benchmark beyond a trace count. These are meaningful natural exact invariants rather than a finite unmotivated computation.

## Limitations and closest literature

The conclusions do not apply without modification to the Laplacian model, disorder, additional sinks, finite-time efficiencies, or quantum many-particle evolution. Numerical confirmation covers prime Desarguesian planes only; the proof uses axioms valid for any affine plane. The closest prior tools are arXiv:0803.3446, arXiv:1412.7209, arXiv:1707.07482 and arXiv:2011.13794. A specialized unlocated two-trap finite-design theorem remains a historical-priority risk.

Self-review: passed. Independent audit: not yet performed.
