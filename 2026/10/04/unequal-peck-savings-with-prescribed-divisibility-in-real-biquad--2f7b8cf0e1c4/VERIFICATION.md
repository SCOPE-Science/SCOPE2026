---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---
# Verification

The claim is proved symbolically; no finite search or numerical experiment is used to establish a universal statement.

The following source-level facts were checked directly in the full primary text of arXiv:2609.29469v1:

1. For the unit congruence subgroup \(U_m\), the associated lattice is a sublattice of index at most \(I_m\), and \(u\in U_m\) forces the denominator coordinate \(q=\operatorname{Tr}(\alpha_1^*u)\) to be divisible by \(m\).
2. The shaped Minkowski box lemma depends on the unit lattice through its covolume constant, so replacing the lattice by the congruence sublattice replaces \(J\) by \(J_m\le I_mJ\).
3. In the real biquadratic natural basis, the two nonlinear error coordinates factor as a bounded common exponential factor times \(e^{y_i}-1\), one variable per coordinate.

For \(S=T/C'\), the new parameter choice is
\[
P_m=\frac{J_m\log T}{I_m\log S},\qquad
\mu_{i_1}=8P_m,\qquad \mu_{i_2}=\frac18,\qquad
\eta_i=\frac{\mu_i}{f_i},
\]
where \(f_{i_1}=\max(f_2,f_3)\). The identity
\[
\eta_2\eta_3=\frac{J_m}{\log S}
\]
follows exactly from \(f_2f_3=\log T/I_m\). Since \(J_m/I_m\le J\) and \(\log T/\log S\le2\) for sufficiently large \(T\), the \(\mu_i\) are uniformly bounded. Also \(f_{i_1}\ge\sqrt{\log T/I_m}\), so \(\log T\ge cI_m\) makes every side small enough for the lemma.

The proof does not establish necessity of the \(I_m\) loss, does not cover arbitrary bases, and does not claim anything for smaller heights.
