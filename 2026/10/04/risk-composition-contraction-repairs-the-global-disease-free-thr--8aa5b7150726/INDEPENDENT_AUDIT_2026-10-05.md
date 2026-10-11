# Independent mathematical audit

## correctness

PASS

Direct substitution of the source parameter set confirms that the printed global comparison can reverse sign at an admissible simplex state even though the source R0 is below one. For q=S/rho-L/(1-rho), subtracting the two susceptible equations gives the exact scalar identity q' = -(mu+beta H)q -(alpha-beta)H S/rho, so the positive part contracts at least as e^{-mu t}. The exact decomposition alpha S+beta L = a0(S+L)+(alpha-beta)rho(1-rho)q then bounds the time-dependent effective susceptibility by a0 plus an exponentially decaying excess. When R0<1, after finite time the infected two-by-two Metzler block is entrywise dominated by a fixed Hurwitz Metzler matrix, which yields exponential decay of E and I; scalar variation of constants then gives R to zero and S,L to their disease-free shares. The disease-free Jacobian is locally stable at the same threshold, so global attraction plus local stability gives global asymptotic stability. A fresh independent symbolic reconstruction verified the q equation and the susceptibility decomposition; the exact package checker separately verifies those identities, the infected-block determinant, and the numerical sign-reversal counterexample.

## originality

PASS

The complete Pan--Tang primary PDF was inspected through the normalized model, R0 calculation, Theorem 1 and its global-stability proof. The source explicitly uses the invalid pointwise replacement of alpha S+beta L by the disease-free weighted value. No correction or erratum giving the submitted composition variable was found in targeted searches. Related heterogeneous-susceptibility epidemic models use different flows or Lyapunov structures and do not imply this exact contraction identity. The submitted result therefore supplies a source-specific repair that preserves the published threshold rather than merely pointing out an error.

## value

PASS

The result repairs a published global threshold theorem whose printed comparison fails even for the paper's own subcritical parameter set. The contraction identity explains why the original threshold nevertheless remains correct and isolates a reusable risk-composition mechanism rather than merely producing a counterexample to one line of proof.

The dated certificate retains the supplied scientific assessment, sources and limitations.
