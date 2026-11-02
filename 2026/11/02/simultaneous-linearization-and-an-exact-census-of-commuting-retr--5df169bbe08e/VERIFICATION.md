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

# Verification record

The proof independently classifies the solutions for all fields by an induction on the tensor-word degree; the computations below only test finite instances. Run the standalone `verify.py` in a Python 3 environment with its standard library. It constructs the nonunital algebra on words of lengths one and two in two generators and enumerates homomorphisms by arbitrary generator images. Idempotence and pairwise commutation are checked by direct substitution and multiplication, not by assuming the classification.

The checker inspects all \(4096\) and \(531441\) algebra endomorphisms over \(\mathbb F_2\) and \(\mathbb F_3\). It finds \(98\) and \(974\) idempotents, respectively. It checks all \(9604\) and \(948676\) ordered pairs of those idempotents and all \(941192\) ordered triples over \(\mathbb F_2\), comparing the complete simultaneous weight-space-dimension histograms to the closed formula. The commuting totals are \(868\), \(13612\), and \(5288\). The attached `verification_output.txt` is the output of an actual completed run.

The checker uses prime fields only. The general theorem permits all finite fields and all higher word lengths, but those cases were proved algebraically rather than exhaustively enumerated. No independent expert or external certification has been performed.
