# Independent mathematical audit

## correctness

PASS

With two unnormalized Rademacher vectors the leave-one-out projectors have rank one; the two squared sketch norms both equal S₂>0. Writing P_j=∑a_i^j g_i h_i, applying either residual projector in the basic estimate gives S₁+S₃/S₂−2P₁P₂/S₂+S₃P₁²/S₂². This proves equality before averaging and makes the sample-variance diagnostic (3.1) zero on every sample. The diagonal terms in the products cancel the constant beyond S₁, and the independent fair probe-product signs give the orthogonal pair characters with the stated coefficients, hence the stated MSE and unbiasedness. For two nonzero entries a,b the decisive factor is −ab(a+b); for at least three, equality of all pair sums would force all nonzero entries equal, in which case their pair sum is twice S₃/S₂. This exhausts zero risk in scope. For A=I_n the coefficients are all −2/n, giving MSE 2(1−1/n); the two-point n=2 law and the direct Hutchinson comparison follow exactly.

## originality

PASS

Credit only the two-probe samplewise theorem across arbitrary real nonzero diagonals, the exact Walsh risk and its zero set. Both the general diagnostic mechanism and a close scalar-identity example of false stopping with more sign probes were already known. Neither inspected result gives the full finding at two probes.

## value

PASS

The minimal two-probe budget is a natural boundary of this empirical diagnostic, not an arbitrary finite slice. The theorem supplies a full class on which exchangeable estimates coincide and hide nonzero MSE, even for positive-definite inputs in dimensions above the matvec budget. The zero-risk classification and exact true-versus-reported risk are directly useful for testing diagnostics and interpreting small-budget behavior.

The dated certificate retains the supplied scientific assessment, sources and limitations.
