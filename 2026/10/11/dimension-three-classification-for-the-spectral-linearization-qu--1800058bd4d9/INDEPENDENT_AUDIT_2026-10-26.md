# Independent mathematical audit

## correctness

PASS

For every a in R^3 the statement exactly quantifies over real-linear L:S_2(R^3)->S_2(R^6) and all real symmetric A. If a has repeated entries (alpha,beta,beta), beta tr(A)I_3+(alpha-beta)A, doubled by direct sum, realizes every permutation pairing with multiplicity. For distinct a, choose a generic diagonal D_0 yielding six simple eigenvalues of L(D_0). The symmetric-pencil second-derivative identity for the largest eigenvalue forces every off-diagonal coupling of each diagonal-direction pencil to vanish; recursive restriction forces simultaneous diagonalization of the whole diagonal subspace. For a generic diagonal D, first-order perturbations along H_pq give zero diagonal entries for L(H_pq); second derivatives give a rational simple-pole identity. Difference rays from one vertex of the six-vertex permutahedron are pairwise nonproportional; pole comparison forces edges only between permutations differing by the positional transposition (pq), with squared coupling equal to the corresponding squared weight difference. The 3-transposition Cayley graph is parity-bipartite, so tr L(A)^3=0 for any zero-diagonal A. Direct expansion of the six cubed target eigenvalues gives gamma=(a1-2a2+a3)(a1+a2-2a3)(2a1-a2-a3), multiplied by tr A^3, forcing arithmetic progression. After affine normalization a=(1,0,-1), parity makes L(A) a 3+3 offdiagonal symmetric block, so det L(A)=-(det C(A))^2. The prescribed ordered-difference spectrum instead has determinant -Delta(A), with Delta=4(x²+y²+z²)^3-108x²y²z². At z=0 it becomes 4(x²+y²)^3, nonsquare in R[x,y], contradiction. This exhausts distinct weights and covers all normalization, multiplicity and boundary cases. Independently wrote SymPy polynomial identities for the cubic, gamma factor, characteristic/discriminant, tested the explicit block spectrum and checked distinct permutation-vertex rays for several representative weights; finite tests corroborate but do not replace the all-real analytic argument.

## originality

PASS

The exact target question in Sanyal–Saunderson, Spectral Polyhedra (2025), §3 and Question 1 is still open in their published text for d>=3; their Proposition 3.1 gives d=2, while special linearized exterior-power cases and the larger numerical-chain tensor-product pencil do not determine existence of an exact size-6 pencil realizing six permutation-weighted eigenvalues for generic d=3 weights. Originality is of the complete d=3 iff theorem, not the classical spectral perturbation formula, discriminant formula, Schur functors, or repeated-weight exterior-power construction. Resultary returns the audited finding itself as the direct hit, but no independent earlier full d=3 classification. Web searches for question aliases and eigenvalue-difference representation did not locate one. This is a best-of-knowledge verdict, not a universal priority certificate.

## value

PASS

The natural weight-by-weight realizability question is expressly posed in a peer-reviewed primary source and is tied to the size of spectrahedral representations of spectral polyhedra. Resolving the entire first unanswered dimension by a sharp if-and-only-if classification is a substantive structural boundary rather than a tiny numeric improvement. Nonexistence for every distinct-coordinate weight requires several nonroutine arguments: diagonal spectral rigidity, hyperplane pole localization, parity of the S3 transposition graph, and a discriminant square obstruction. A future investigator of exact small spectral pencils can directly use the d3 classification to avoid impossible constructions while retaining the explicit repeated-coordinate cases. This does not settle d>=4 or exclude other spectrahedral formulations.

The dated certificate retains the supplied scientific assessment, sources and limitations.
