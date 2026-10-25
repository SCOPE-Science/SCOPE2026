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
# Exact verification record

Execute `python3 verify_eos.py` from this package. Expected final line: `VERIFY_OK`. The actual run yielded missing-unit-class counts \(1,2,3,3,5,11,17,30,54,70,121,162,190,240,216,183,92,42,7,3,0\) at exponents \(1\) through \(21\), with a first successful prime cutoff \(50923\) at exponent \(21\). The last obstruction at the preceding prime \(50909\) is \(745135\), and \(50923\cdot7757\equiv745135\pmod{2097152}\). The three excluded classes at exponent \(20\) are exactly \(122299,333455,414971\).

The exact proof is finite. It combines standard sieve correctness, bijective indexing of all odd residues, exhaustive unordered prime-pair enumeration, and separate modular-inverse checks for obstructions. Every checked case is finite; the package does not establish coverage for any exponent above \(21\).
