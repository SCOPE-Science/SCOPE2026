---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-20.md",
      "INDEPENDENT_AUDIT_2026-10-20.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Reconstructed Fourier kernel k_n,t(j)=(1/n) sum_m cos(2pi*m*j/n)/(1+16t sin^4(pi m/n)), with row sum 1. For n>=5 L_n^2 has distance-two positive coefficient so kernel initially negative, while t->infty kernel is positive mean projector. Scale t=c*n^4; continuum periodic Green G_c has critical c*=1/(64rho^4), rho in (pi/2,pi) solving tan rho+tanh rho=0; at c* unique quadratic zero at antipode, G_c>0 for c>c*. Expand discrete fourth symbol to order n^-2 uniformly by summable O(m^-2) difference and show F_n(c,j)=G_c(j/n)+n^-2 H_c(j/n)+o(n^-2). At c=c*+tau/n² antipodal local minimum is Gamma*tau+H+K*(j-n/2)^2/2+o(1); allowed nearest offsets are 0 for even n and 1/2 for odd n. Thus beta_even=tanh(rho)*(3-rho*tanh(rho))/(48rho³)>0 and beta_odd=-tanh(rho)^2/(48rho²)<0. Away from the antipode strict continuum positivity and for sufficiently large c Fourier tail bound control the entire EVENTUAL threshold. Independently numerically inverted Fourier circulants at n=40,41,80,81,150,151,300,301 and estimated (threshold-c*n^4)/n², converging to the two opposite-sign coefficients; finite support only. Did not assume finite window proves global monotonicity.

## originality

PASS

Best-of-knowledge, statement-and-implication comparison: inspected same-object primary results and relevant published records; literature access limits documented. Source covering the leading continuum threshold is only partial; complete asserted theorem requires uniform n^-2 symbol analysis and global eventual positivity tail control. No inspected prior result implies the correction.

## value

PASS

Periodic biharmonic smoothing loses positivity at moderate regularization but eventually regains the convex-hull/range-preserving property; the exact n^4 scaling and oppositely signed n² lattice-parity correction are important for finite-cycle kernel design. Separates periodic from open-end Whittaker–Henderson boundary conditions and is a sharp natural asymptotic rather than a routine constant replacement.

The dated certificate retains the supplied scientific assessment, sources and limitations.
