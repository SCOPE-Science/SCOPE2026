---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

Under the source's own skew multiplication, \(g_2=x+1\) has prime-field coefficients and therefore \((1+x^2)g_2=x^3+x^2+x+1=g_3\). Hence the product-ring code contains \(c=(0,g_3,g_3)\). At every one of its four ring coordinates the row is \((0,1,1)\), and right multiplication by the printed Gray matrix gives \((0,1,0)\). Thus the Gray image contains an explicit word of Hamming weight \(4\), disproving the published distance \(6\). Fresh exhaustive reconstruction of the \(5\)-dimensional quaternary image gives rank \(5\), all \(4^5=1024\) words, weight enumerator \(1+9z^4+72z^6+243z^8+384z^9+216z^{10}+99z^{12}\), and minimum distance \(4\). Independent column-subspace enumeration gives maxima \((0,1,2,4,8)\) and generalized Hamming weights \((4,8,10,11,12)\).

## originality

PASS

The current journal Table 2 and arXiv-source data print the same \(q=4,l=3,n=4\) matrix and component generators and label the Gray image as an optimal \([12,5,6]_4\) code. The explicit weight-four word follows from those exact published conventions. Targeted Resultary and web searches using the paper identifier, both parameter sets, the matrix/generators, and Gray-image terminology found no corrigendum or prior report of this discrepancy. The complete corrected enumerator and generalized-weight hierarchy are likewise absent from the inspected source.

## value

PASS

Correcting an advertised optimal code row is directly relevant to reproducibility and downstream quantum-code constructions. The result supplies both a four-coordinate countercertificate and the exact replacement parameters, weight enumerator, and generalized Hamming-weight hierarchy, so it is a substantive finite correction rather than a bare negative check.

The dated certificate retains the supplied scientific assessment, sources and limitations.
