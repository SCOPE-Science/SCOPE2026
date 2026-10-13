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

The verifier `artifacts/verify.py` exhausts every \(\mathbb F_2\)-linear endomorphism of the four-dimensional vector space \(M_2(\mathbb F_2)\), so the search contains exactly \(2^{16}=65536\) maps.

For each weight \(\lambda\in\{0,1\}\), the first pass tests the Rota–Baxter identity on all \(16\) ordered pairs of matrix units. The defect is bilinear, hence this is exhaustive. A second routine checks every accepted map on all \(256\) ordered pairs of elements of the algebra. The outputs are exactly \(28\) weight-zero operators and \(110\) weight-one operators.

For every accepted map, powers are computed as exact binary linear maps and all monic polynomial relations of increasing degree are tested. The degree distributions are \((1,21,6)\) for degrees \((1,2,3)\) at weight \(0\), and \((2,84,24)\) at weight \(1\). Hence degree \(3\) is maximal in both cases.

The algebra automorphism group is computed independently in two ways: by exhaustively testing invertible unital multiplicative linear maps, and by inner conjugation from \(\operatorname{GL}_2(\mathbb F_2)\). Both methods give exactly \(6\) automorphisms. Exhaustive orbit closure then gives automorphism-orbit sizes \((3,3)\) at weight \(0\) and \((6,6,6,6)\) at weight \(1\). Adding transpose gives \((6)\) and \((12,12)\); adding \(\phi(R)=R+\operatorname{id}\) at weight \(1\) gives one \(24\)-element class.

The recorded output in `artifacts/verify_output.txt` terminates with `VERIFY_OK`. No timeout, random sampling, floating-point arithmetic, or unproved extrapolation is used.
