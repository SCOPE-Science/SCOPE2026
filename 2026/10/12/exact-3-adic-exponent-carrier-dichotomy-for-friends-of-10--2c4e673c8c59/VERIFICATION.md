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

The theorem is proved symbolically in `RESULT.md`. The standalone checker performs only finite regression checks:

1. It verifies exactly that \(I(3^4 5^2)>9/5\), \(I(3^2 5^4)>9/5\), and \(I(3^2 5^2 13^2 31^2)>9/5\).
2. For primes below \(500\) and even exponents through \(400\), it checks the local identities used in the proof: zero \(3\)-adic valuation for primes \(2\pmod3\), and \(\nu_3(\sigma(p^a))=\nu_3(a+1)\) for primes \(1\pmod3\).
3. For even exponents through \(5000\), it checks that valuation level \(1\) gives exactly residues \(2,14\pmod{{18}}\), valuation level \(2\) gives exactly residues \(8,44\pmod{{54}}\), and valuation level \(0\) gives residues \(0,4\pmod6\).

The finite checks do not establish the universal theorem; they guard arithmetic and residue bookkeeping in the symbolic proof. No existence of a friend of \(10\) is assumed or computationally claimed.
