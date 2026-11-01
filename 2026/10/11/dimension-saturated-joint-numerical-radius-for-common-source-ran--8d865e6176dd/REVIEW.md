# Mathematical assessment of the common-source joint numerical-radius theorem

## Correctness

The exact joint operator norm is the Frobenius norm of the common-source output family. For the source-parallel coefficient vector `a` and perpendicular synthesis map `S`, symmetric unit test vectors give `4W^2 >= ||a||^2 + ||S||^2`. The rank restriction `rank(S) <= min(k,m-1)` yields the sharp dimension-dependent ratio, and explicit coordinate partial isometries attain it. Equality when the rank threshold exceeds one is equivalent to zero source-parallel part and all nonzero singular values equal; when the threshold is one, a separate one-variable perturbation rules out a nonzero source-parallel part. The exact perpendicular-source spectral deficit and stated near-minimal estimates follow.

Numerical examples and random matrix tests illustrate the result but do not replace this analytic proof.

## Relationship to prior literature

Mal's 2023 Hilbert joint-index theorem obtains the unrestricted complex sharp value for tuple length `k<m`, with a common-source construction. The new fixed-dimensional restricted-family assertion concerns the parameter range beyond that construction and describes all equality families. The 2017 Euclidean-radius inequalities by Moslehian, Sattari and Shebrawi give different general bounds, while Grover and Singla study subdifferentials and operator-tuple orthogonality. A 2014 antecedent by Drnovšek and Müller is cited by Mal for its construction idea; its complete text has not been examined, so prior equivalence remains a genuine risk. Failure to find a matching source does not prove global novelty.

## Mathematical significance and scope

The restricted class is the natural rank-one construction from the motivating joint-index theorem. Saturation at the dimension of the source's orthogonal complement and the transition from orthogonal families to redundant tight frames are precise and useful structural invariants. No statement is made about unrestricted operator tuples above the threshold or formal proof-assistant verification.
