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

# Exact reproducibility and boundaries

Execute `python3 check_octahedral_equivariant_morse.py` using Python 3 standard library only. The checker enumerates all \(5^6=15625\) root-directed assignment possibilities and constructs the complete simplicial face set. It verifies the counts \((1,24,228,1072,2496,2304)\), checks all \(25176\) nonempty Hasse incidences, and topologically sorts the reversed-matching Hasse diagram to certify acyclicity, with \(2724\) paired edges and one critical vertex plus \(675\) top-dimensional cells.

The same verifier checks the induced action of each of \(48\) graph automorphisms on every face; computes the exact signed traces on every augmented chain group; groups the \(48\) Lefschetz values into their ten signed cycle types; evaluates all ten irreducible signed-permutation characters; verifies exact orthogonality, integral nonnegative multiplicities, character reconstruction, total dimension \(675\), and invariant dimension \(11\). Its terminal success marker is `ALL EXACT CHECKS PASS`. All arithmetic is integer arithmetic apart from exact divisions that assert zero remainder.

The inference from the acyclic matching to the homotopy wedge and the inference from alternating chain traces to homology traces invoke standard discrete-Morse and Hopf–Lefschetz theorems, respectively. The matching is not asserted to be group-invariant. No integral representation decomposition, external human audit, or all-literature uniqueness proof has been conducted.
