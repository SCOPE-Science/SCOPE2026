# Independent mathematical audit

## correctness

PASS

For the repaired claim in /workspace/repairs/5/RESULT.md. Solving the three linear per-capita equations leaves a single admissible interval for h=m; β(m) has positive derivative there and ranges from −∞ to zero. Differentiating the vector field and expanding its characteristic polynomial reproduces all coefficients and their reductions; positivity follows on the full interval. The Routh first column gives two sign changes for either sign of AB−C when Δ<0; at AB=C the absence of axis roots justifies continuity. For Δ=0 the factorization gives exactly a simple imaginary pair and a Hurwitz quadratic. At m=0 the determinant's quadratic factor has two distinct positive roots and the remaining root is negative; simple-root persistence proves the local parameter interval. Replay: `python /workspace/check_5.py` reproduces the identities and independently tests the frozen overstatement. The frozen Finding and Step 3 asserted nonlinear local asymptotic stability iff the Jacobian is Hurwitz. That is false at β=−9: in the normalization q_z=1 and left-right product 1, the real cubic coefficient Re G21 is between −2.938 and −2.937 at the lower speed and between −72.727 and −72.726 at the upper speed (exact operations in Q(√3679)[iν] and rational bracketing of √3679). With a stable transverse pair, the negative center-manifold radial cubic makes the nonlinear equilibrium locally asymptotically stable at the thresholds too. The repair retains only the proved full spectral classification and the strict-sign nonlinear implications. The cubic calculation diagnoses the original error; the repaired result does not rely on it.

## originality

PASS

The source owns the ODE, nullification state and qualitative intermediate-speed phenomenon. The supported distinct remainder is the parameter-wide local spectral criterion and exact pair of algebraic boundaries, not the prior model, equilibrium, classical Hurwitz test, or observed cycles.

## value

PASS

The special point is selected by the source's interaction-nullification mechanism, not numerical convenience; the source's numerical diagrams motivate locating two reentrant thresholds exactly. The repaired result gives a usable local test at every negative modifier strength, determines the whole linear spectrum's stability type and proves persistence near nullification. These are independent of conjectures about cycles or population survival.

The dated certificate retains the supplied scientific assessment, sources and limitations.
