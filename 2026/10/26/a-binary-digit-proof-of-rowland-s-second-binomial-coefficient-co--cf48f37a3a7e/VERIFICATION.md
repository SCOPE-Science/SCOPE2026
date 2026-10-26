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
# Verification and limitations

The bundled standalone Python 3 program `verify.py` independently generates the original floor-sum exceptional residue classes exactly as written by Rowland (2011) and compares them with the binary-mask criterion. Every odd prime \(p\le3000\) is tested; the 429 tests cover all residues modulo \(2^{1+\lfloor\log_2(2p)\rfloor}\) for each such prime. For every odd prime \(p\le197\), the verifier additionally checks all positive \(n\) in one full binary period by forming \(\binom{n-1}{2p-1}\) as an exact integer, checking integrality of the corrected quotient and its parity. That second test encompasses 44 primes and 11,816 exact binomial calculations.

Actual output from the prepackaging execution:

`VERIFY_OK: 429 odd primes <=3000, all residues of Rowland parametrizations; 44 odd primes <=197 and 11816 exact integer-binomial checks`

To reproduce: execute `python verify.py` from the extracted files using the Python standard library. The verifier does not call external services and makes no probabilistic assumptions. All tested finite cases corroborate the equations; the universal theorem depends on the algebraic proof in `RESULT.md`, especially the digitwise coefficient identity. No independent mathematical audit has been performed, and prior-literature searches cannot certify global novelty.
