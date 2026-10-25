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
# Verification of the octagonal pushability calculation

Run `python3 verify_octagon.py` from the directory containing this file. No external dependencies or private data are required.

The script enumerates 10 dihedral classes of first supports and 92 possible second supports, a total of 920. Each support contains at most three vertices because of the LP support-reduction lemma in `RESULT.md`. The linear constraints are solved exactly in \(\mathbb Q(\sqrt2)\). The Hessian is tested for strict negative definiteness on each support's affine tangent space, and only feasible strictly positive stationary points are retained. There are 126. The largest exact value is \((26-7\sqrt2)/32\), and the explicit attaining pair is checked against all equalities.

For separately zero-mean laws, the program checks all nonempty supports of size at most three; it recovers 12 extreme distributions, evaluates 144 pairs, and verifies a maximum of \(1/2\). These checks are finite but exhaustive after the analytic reductions; they are not Monte Carlo tests or a substitute for the reductions.

The result does not certify general octagons, more than two laws, all equality cases, or priority against unavailable mathematics. Independent audit has not been performed.
