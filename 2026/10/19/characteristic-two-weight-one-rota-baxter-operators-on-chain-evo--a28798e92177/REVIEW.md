# Independent mathematical audit

## correctness

PASS

The bilinear weight-one identity on diagonal basis pairs forces successive columns by iterated squaring, and the terminal equation is automatic from Q^n=0. For an off-diagonal pair with column separation d, coefficient comparison and injectivity of Frobenius give a_(t+d) a_t^(2^d) = a_(d+1) a_t^(2^(d+1)) for t+d<=n-1. Every such equation is realized already by a pair starting at e_1. The first nonzero interior coefficient at j forces a_1 in {0,1}; the equations at t=j then propagate period j-1 with the stated Frobenius exponents. Concatenation of the exponent sums proves sufficiency for every t,d, without requiring perfectness. The terminal first-column coefficient is free. The least nonzero row and its shifts give the stated ranks, including the empty interior at n=2. With standard column conventions the triangular matrix is lower rather than upper triangular; that wording in the rank proof does not affect any calculation. A fresh bounded checker (branches/7131221e-51e8-4a7b-a76a-ce3dd300187b/reproduce_independent.py) matched accepted columns and the increasing-rank counts (1,3,12,12,36) for (q,n)=(4,4) and (1,1,2,2,2,8) for (2,5). The frozen checker was inspected, not executed; finite checks are not an arbitrary-field proof. Frozen independent audit, Lean and expert statuses were not performed.

## originality

PASS

The supported contribution is the characteristic-two weight-one Frobenius-support classification and census for the unperturbed chain. The inspected earlier weight-one theorem assumes characteristic zero. A distinct later-dated catalog record is a full statement-level match, including ranks, and is credited as such; there is no evidence here that it preceded the frozen finding. This is a bounded assessment, not a claim to historical priority or uniqueness in the current catalog.

## value

PASS

Weight one on the standard nilpotent chain is a natural boundary of the established characteristic-zero classification. The Frobenius recurrence explains the exact admissible supports even over imperfect fields and yields the complete finite-field ranks, rather than extrapolating from a handful of dimensions. It does not purport to classify perturbed chains or automorphism orbits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
