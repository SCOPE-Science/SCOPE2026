# Independent mathematical audit

## correctness

PASS

For a guaranteed p-cycle with p prime and fully known p×p binary signature b_i(t)=1_{f^t(x_i)<=x_i}, label the phase a_j by f^{a_j}(x_1)=x_j. The time-zero-cleared row of x_{i+1} equals A_i(t+a_{i+1}), where A_i is the length-p indicator of the already known phase set S_i. A nonempty proper subset of additive Z/p has no nonzero translational stabilizer. Thus one cyclic rotation is unique and linear-time KMP matching in the doubled word recovers each of p-1 phases in O(p) steps and O(p) auxiliary storage. The reconstructed permutation maps phase a_i to a_i+1. Independently exhaustive enumeration checks all 1, 2, 24, 720 p-cycles for p=2,3,5,7, with an independent rotation matcher; tests corroborate and group-action proof covers all primes. Complexity applies to explicit full signatures, not unknown-signature or bit-precise input lower bounds.

## originality

PASS

Fuhrmann–Gröger–Passeggi arXiv:2610.07435v1 proves uniqueness (Lemma 2.1), and the cited Remark 2.4 states O(p^3) reconstruction. A cyclically translated known-prefix phase-set indicator combined with KMP gives a distinct O(p^2) algorithm; the generic 1977 KMP theorem alone does not give this representation. Resultary finds the assigned result, not a separate identical quadratic algorithm. Primary full preprint was not freshly accessible; claim of noncoverage remains bounded to the identified Lemma/Remark rather than its unread entirety.

## value

PASS

An explicit O(p^2) reconstruction algorithm is linear in the p²-bit signature-table input size and improves the cubic inverse procedure underlying periodic-orbit-order rigidity. The gain is algorithmically motivated, exact, and works for all prime lengths rather than a small finite enumeration. It does not claim a new theorem about obtaining the signatures from unordered interval orbits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
