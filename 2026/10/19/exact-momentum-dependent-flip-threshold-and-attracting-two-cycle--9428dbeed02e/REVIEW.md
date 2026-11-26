# Independent mathematical audit

## correctness

PASS

For the precise smooth scalar recurrence, the companion Jacobian has trace (1+beta)q and determinant beta*q. Its strict Schur region is -1/(1+2*beta)<q<1 for 0<=beta<1. At zero q=1-a; at criticality the roots are -1 and beta/(1+2*beta), and above criticality the characteristic polynomial is negative at -1, so a real root lies below -1. Adding the equations for any two-cycle and using odd injectivity of the smooth sign forces the two entries to be negatives; then solving the single remaining equation gives exactly the claimed amplitude and square-root coefficient. On this cycle q=1-a_c^3/a^2 lies strictly in the Schur interval for every finite a>a_c, and the return derivative is the square of the one-step derivative. For beta=0 the magnitude strictly decreases to zero when a<=2; at a=2 the increment of its inverse square tends to 2 off the finite-hit set. For a>2 magnitudes enter (0,sqrt(a^2-1)) unless they hit zero; the magnitude map g preserves that interval by its explicit maximum. There g+r is strictly increasing and g-r changes sign at h, giving strict contraction of distance to h off h. Above 2h iterates must eventually cross into (0,2h) or converge to a forbidden fixed point there; then strict contraction on a compact set separated from zero yields convergence to h. No global result for positive momentum follows. Read the frozen RESULT.md proof, VERIFICATION.md, and artifacts/verify_scalar_soft_muesterov.py; the recorded finite run is not a fresh execution, and the proof does not depend on it.

## originality

PASS

Credit the same scalar model, the Nesterov linearization mechanism and analogous already-known oscillations. The supported distinction is the complete nonlinear period-two branch for this exact positive-momentum recurrence, including uniqueness and attraction for every finite supercritical step, with a global scalar zero-momentum endpoint classification. The reviewed sources and indexed comparators do not supply that result; this is not an absolute priority claim.

## value

PASS

The exact threshold tells when increasing step size destroys local convergence in a natural scalar specialization of a published optimizer. The isolated cycle exists and stays locally stable arbitrarily far past onset, which does not follow from the threshold or a local flip theorem. The zero-momentum global result and critical rate also locate the scope of the stability analysis. The contribution is model-specific rather than a general optimization theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
