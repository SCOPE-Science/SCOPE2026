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

# Reproducibility and scope

Run `python3 verify_spider.py` using Python 3 and the standard library, from the directory containing this file. It reconstructs each finite spider as a graph, tests all induced connected components to enumerate allowable faces, computes complete mod-two reduced homology by independent exact elimination, constructs the claimed discrete-Morse matching on the hub link and checks that **every** cover relation orients an acyclic Hasse graph, then compares integral signed-Lefschetz alternating simplex counts with the character of \(\det(\mathbb Z^J)\otimes\bigwedge^t U_Z\).

Observed output:

`PASS 158 mod-two Betti plus acyclic-Morse checks and 576 signed-Lefschetz checks, arms 3 to 5, 3-4 arms, at most 12 nonhub vertices`

The check covers every ordered tuple of three or four arm lengths in \(\{3,4,5\}\) whose sum is at most \(12\), and every integer parameter \(r\) from the maximum arm length through one more than the sum of arm lengths. The verifier's finite checks are not an infinite-parameter proof and its mod-two computations do not alone establish integral torsion-freeness; that comes from the integral chain argument in RESULT.md. Exact signed Lefschetz traces determine the claimed representation characters on tested permutations, not an external certification.

**Scientific boundaries:** The theorem requires all arms to have at least three edges and \(r\ge\max_i\ell_i\). It does not claim an equivariant homotopy wedge decomposition, a lower-parameter classification or independent validation.
