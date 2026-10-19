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

# Verification of forbidden nilpotency indices

Run `python3 verify_nilpotent_gap.py` beside this file. The program independently enumerates all \(2\times2\) matrices with nilpotent reductions and multiplies them to determine their least zero powers, without using the proof's recurrence to assign powers.

The exact checked configurations are \(\mathbb Z/8\mathbb Z\), \(\mathbb F_2[t]/(t^3)\), \(\mathbb Z/16\mathbb Z\), and \(\mathbb Z/27\mathbb Z\). Their nilpotent totals are respectively \(1024,1024,16384,59049\), with maximal-index counts \(384,384,6144,34992\). All forbidden-index counts are zero. The first two rings have matching index histograms despite different characteristics. The program also checks \(\nu(C)=5\) over \(\mathbb F_3[x,y]/(x^2,y^2)\) and \(\mathbb F_5[x,y]/(x^2,y^2)\), and \(\nu(C)=4\) over the corresponding characteristic-two ring.

The proof verifies the general companion recurrence, valuation bounds, exact determinants in the first radical layer, and non-chain witness symbolically. The finite tests are checks and do not certify all rings or constitute independent mathematical validation.
