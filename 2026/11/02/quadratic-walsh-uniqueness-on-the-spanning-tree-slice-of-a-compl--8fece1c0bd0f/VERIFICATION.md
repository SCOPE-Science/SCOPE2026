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

The claim concerns every integer \(n\ge3\). The proof is self-contained in `RESULT.md`; its critical steps are the edge-exchange linear lemma, induction on the complete-graph order, and three explicit star-tree evaluations. Those steps, not a finite computation, justify universal quantifiers.

Running `python3 VERIFY.py` from the extracted files uses only the Python standard library and yields the exact prime-field row ranks of the pair-inclusion matrix: \(3\) for \(n=3\) (three trees), \(15\) for \(n=4\) (sixteen trees), \(45\) for \(n=5\) (125 trees), and \(105\) for \(n=6\) (1296 trees). Each equals \(\binom{\binom n2}{2}\). These are independent finite consistency checks: they do not prove the infinitely many larger cases. Modular rank can prove nonzero rational minors in the tested cases but cannot replace the general argument.

The normalized Gram rank is measure-independent only when all trees have **strictly positive** probabilities; measures that exclude trees can reduce rank. No nonzero eigenvalue bounds or numerical conditioning claims are made. No independent mathematical audit or validation has occurred.
