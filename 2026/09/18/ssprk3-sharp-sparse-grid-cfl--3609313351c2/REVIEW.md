# Same-model review

Same-model review: passed. Independent audit: not yet performed.

## Correctness

**PASS.** The proof was checked at the operator and scalar-polynomial levels separately.

The nonnormality issue is essential: an eigenvalue-only argument would not be sufficient for an induced L2 norm. The proof instead uses Huang's contraction H with ||H||_2 <= 1 and von Neumann's inequality for polynomial functions of a Hilbert-space contraction. This gives a genuine operator-norm upper bound over the full disk |z+mu| <= mu. Huang's constant and alternating modes provide eigenvalues +1 and -1 of H, hence exact lower witnesses at the scalar arguments 0 and -2mu.

For SSPRK(3,3), the boundary calculation was rederived symbolically. Writing z=mu(w-1), |w|=1, and x=1-Re(w), the identity

1-|R_3(z)|^2 = (mu*x/9) F_mu(x)

was verified. Expressing F_mu(2y) in the Bernstein basis yields three coefficients whose signs are controlled by the unique positive root of 2mu^3-3mu^2+3mu-3. This proves disk inclusion without a numerical maximization assumption. The alternating mode gives strict instability immediately above the root because R_3(-2mu)+1 is exactly two-thirds of 3-3mu+3mu^2-2mu^3.

The standalone verification artifact checks the symbolic identities and also constructs a finite two-dimensional Haar sparse-grid matrix for an anisotropic velocity example. It verifies the contraction at the predicted endpoint and amplification immediately above it.

## Originality

**PASS, to the best of our knowledge.** The source paper arXiv:2609.17312v1 was read in the portions containing Theorem 3.8, Lemma 3.9, Corollary 3.10, Remark 3.11, and Corollary 4.4. Remark 3.11 states the SSP-coefficient sufficient condition and explicitly says its sharpness is not guaranteed. The exact SSPRK(3,3) threshold is not stated there.

The scalar Runge--Kutta stability-disk constant is prior art and is not claimed as new. Jeltsch--Nevanlinna (1978) studied largest disks in explicit RK stability regions, while Dahlquist--Jeltsch (1979/2008) distinguished stability disks from stronger nonlinear circle contractivity and report stability-disk radii about 1.25 for third-order formulas. Gottlieb--Shu--Tadmor (2001) provides the SSP framework and the coefficient-one SSPRK(3,3) baseline.

Searches covered the source arXiv identifier and title together with SSPRK, Runge--Kutta, CFL, sparse-grid DG, stability disks, and equivalent origin-tangent-disk language. They also covered sparse-grid DG predecessor papers and classical RK stability-disk literature. No located source states the exact 1.256372663309164... L2 CFL threshold for Huang's standard sparse-grid DG operator, the contraction-to-stability-disk reduction, or the matching alternating-mode sharpness for SSPRK(3,3).

The principal residual originality risk is simultaneous follow-up to the very recent source preprint or a result buried in older RKDG literature that applies the same contraction/disk mechanism without using the same sparse-grid terminology. No inaccessible paper produced concrete evidence of coverage. The older stability-disk papers were sufficiently inspectable to delimit the novelty: their disk theory is prior, while the sparse-grid application is not found there.

## Value

**PASS.** The result closes an explicit sharpness gap in a current numerical-analysis preprint, enlarges the certified SSPRK(3,3) time step by about 25.64% over the stated SSP bound, and does so uniformly in the ambient spatial dimension for the standard sparse-grid construction. The general two-sided RK reduction also gives a reusable route for analyzing other stability polynomials on the same spatial operator.

## Limitations

The theorem is restricted to linear constant-coefficient periodic transport, the piecewise-constant standard total-level sparse-grid upwind DG discretization, exact arithmetic, and L2 one-step stability. It does not establish a corresponding threshold for nonlinear or variable-coefficient problems, higher spatial degree, limiters, arbitrary adaptive/downward-closed index sets, internal-stage stability, or finite precision.
