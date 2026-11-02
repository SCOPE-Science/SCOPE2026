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

# Verification of the tail-mass threshold

The theorem follows from the displayed three-step proof, rather than from numerical sampling. The checks reconstructible from the proof are:

1. At a zero-outgoing leaf, both modalities have the constant values \(1\) and \(0\), respectively; all Gödel propositional connectives select existing inputs or \(1\). This proves the selector lemma by structural induction, including arbitrary nested modal formulas.
2. For each formula with \(m\) variables, the selector lemma gives \(\Pr(0<e(u_n,\psi)<r_n)\le m\mu((0,r_n))\). First Borel–Cantelli applies without independence. A simultaneous claim is justified by countability of the language.
3. Since \(\mu((0,\varepsilon))>0\), convergence of \(\sum_n\mu((0,r_n))\) implies \(r_n\to0\); positive-valued necessity terms are eventually all \(1\), unless some zero-valued term already witnesses the minimum. Possibility terms tend to \(0\), hence have an attained supremum. Values at equality \(e(u_n,\psi)=r_n\) produce Gödel implication value \(1\) and pose no exception.
4. Under divergence, for each \(k\ge2\), \(\sum_n\mu((0,\min(r_n,1/k)))=\infty\). Independence of the chosen atomic truth values across leaves allows second Borel–Cantelli. The root infimum for \(\Box p\) is \(0\) but all contributing terms are strictly positive.
5. In the uniform example, \(\mu((0,t))=t\), giving the classical convergent/divergent \(p\)-series boundary as stated. No finite experiment is used to extrapolate to infinitely many indices.

Checks are mathematical arguments independently reproducible from the definitions. This is not an independent external audit, and no unperformed computational or proof-assistant run is claimed.
