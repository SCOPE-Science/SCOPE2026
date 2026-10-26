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

# Reproducibility of the six-period covering theorem

Run `python3 verify.py` with Python 3.8 or newer; only the standard library is used. The verifier checks exact factorization of \(111111\), the six-period identities modulo every relevant prime, and two independent full enumerations: integer gcds of the padded expressions and a separately constructed CRT root test. Every one of the \(6\times111111=666666\) finite states is compared, without sampling or heuristic factorization.

The program additionally exhausts \(37037\) residues for each digit-length class for padding digits \(3\) and \(9\) excluding the prime \(3\), reproduces the compressed residue table, and directly checks each of the sixteen digit-\(1\) obstruction witnesses. The expected result is `VERIFY_OK: all 666666 residue states, two independent criteria` together with the six count rows \((60,10121,111,10121,60,10101)\).

The computation establishes the universal conditional theorem because the proof in `RESULT.md` first reduces every possible center and arbitrary positive padding length to this complete finite state space. Neither the computation nor the theorem tests the primality of padded numbers whose gcd with \(111111\) is one. Other prime factors, longer-period covers, and unresolved global prime questions are outside scope.
