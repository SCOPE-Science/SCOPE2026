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

# Verification notes

The argument derives \(u=0\) directly from the original identity by testing a central generator against an arbitrary vector. The remaining equivalence follows from bilinearity of the alternating form and holds in characteristic two. The two varieties and their dimensions are established algebraically using the symplectic group, Lagrangian Grassmannian, and the dual polynomial obstruction.

Execute `python3 verify.py`. The script enumerates all \(3\times3\) endomorphism matrices over \(\mathbb F_2\) and \(\mathbb F_3\) and compares the original weight-zero identity with the reduced matrix criterion; it independently enumerates all \(4\times4\) matrices over \(\mathbb F_2\) and tests each of the \(c=0\) and \(c=1\) fibers. The exact checked results are \(64\), \(729\), and \(3376+720=4096\) matrix/scalar choices (each with \(16\) free functionals). It checks the nonclosure witness's column and row pairings explicitly.

The script does not enumerate larger finite fields or algebraic closures and does not prove irreducibility; the geometric proof and group/Grassmannian counts establish those statements. The comparison with publications does not certify absolute publication priority. No independent audit has been performed.
