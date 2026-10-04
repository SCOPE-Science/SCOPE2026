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
The embedded `verify_rsd_cre_three_agents.py` provides an exact finite replay using only the Python standard library.

Every one of the \(216\) strict three-agent preference profiles is evaluated under all six priority orders and all six initial endowments.

Serial dictatorship is coded in two independent forms. Core from random endowments is also checked in two independent forms: top trading cycles and direct core enumeration. The direct core routine examines every deterministic matching, every nonempty coalition, and every reassignment of that coalition's endowed houses, rejecting a matching exactly when a coalition weakly improves all its members and strictly improves at least one.

The replay verifies:
- equality of the two serial-dictatorship implementations;
- equality of TTC with the directly enumerated unique core for every initial endowment;
- exact equality of RSD and CRE matching multiplicities at every profile;
- structural-cell counts \(48,6,18,72,36,36\);
- multiplicity-spectrum counts \((6):48\), \((3,3):36\), \((3,2,1):72\), \((2,2,1,1):54\), and \((1,1,1,1,1,1):6\);
- support-size counts \(1:48,2:36,3:72,4:54,6:6\);
- no support of size \(5\);
- mean support size \(49/18\).

Run:

`python3 verify_rsd_cre_three_agents.py`

The first output line must be:

`VERIFY_OK`

No statement about markets with four or more agents is inferred from the finite replay.
