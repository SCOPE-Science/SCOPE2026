# Mathematical review

## Correctness — PASS

The proof separates the complete \(n=5\) boundary from \(n\ge6\). For every larger dimension it reduces the unrestricted stochastic problem by convex dihedral averaging, derives the exact Fourier quadratic, proves the middle-grid frequency index for every residue class modulo four, and obtains the minimax value by three alternating multipliers. It checks the nontrivial coefficient-positivity conditions with explicit factorizations and proves uniqueness only within the invariant family. The same result is supported by a replayable standard-library verifier with 1,006,259 assertions; finite checks are not substituted for proof.

## Originality — PASS, with residual risk

The closest direct source is Boyd–Ghosh–Prabhakar–Shah (2005), Section 3.1, whose two-neighbor ring is the same graph but for which it states an asymptotic near-optimal walk and lower bound, not this exact finite-size equality. Boyd–Diaconis–Xiao (2004) establish a generic SDP framework, and Boyd–Diaconis–Parrilo–Xiao (2009) solve the ordinary one-hop cycle with symmetry. Searches for exact cyclic second-neighbor optimum formulas found no dominating statement in the inspected sources. An inaccessible or unindexed prior exact classification remains possible; unsuccessful searches are not novelty proofs.

## Mathematical value — PASS

The full classification provides explicit optimal holding and two jump-distance probabilities for every ring size, with the precise active negative Fourier mode. It explains why almost all optimal mass moves two sites in the large-ring limit while a strictly positive but vanishing one-site probability maintains mixing, and establishes the fourfold asymptotic spectral-gap gain. This addresses an independently motivated network-averaging design problem rather than a numerical example.

## Verification and limitations

The file `verify.py` checks the exact \(n=5,6\) cases and all Fourier modes for \(6\le n\le1000\), and compares against a separately formulated linear program for \(5\le n\le80\). Its floating-point checks are corroboration; no machine-checked infinite proof or independent audit is claimed. The result does not assert uniqueness of every spatially inhomogeneous global optimizer, nor finite-time total-variation optimality.

Self-review: passed. Independent audit: not yet performed.
