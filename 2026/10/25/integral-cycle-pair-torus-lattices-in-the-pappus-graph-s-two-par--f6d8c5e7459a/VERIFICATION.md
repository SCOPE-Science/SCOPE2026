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

# Exact reproduction

With Python 3.11 or later and the dependencies in `requirements.txt`, run `python verify_pappus.py`. All calculations use integers, modular arithmetic over the explicitly named primes, and exact integer Smith normal form; the program performs no downloads.

The verifier checks the graph's independent standard representation, 153/432/297 cell counts, exact boundary composition, connectivity, 783 unique graph cycles, 234 disjoint pairs of cycles, all torus-cycle boundary equations, and a rank-270 second boundary modulo 101. The 45 hexagon tori provide 27 mod-two independent classes with a 27-by-27 **integer** minor of determinant +1, which, together with the boundary-rank upper/lower argument, gives a complete integral basis of second homology.

It enumerates 216 graph automorphisms, determines the 18- and 27-member hexagon-pair orbits, reconstructs every torus as an integer combination of the selected 27 basis vectors, and computes exact Smith factors. The 18-member orbit has rank 17 and only unit nonzero Smith factors; the 27-member orbit has rank 27 and factors 2,2,2,2,2. Length types (6,6), (6,8), (6,10), and (8,8) have ranks 27 and nonunit factors respectively none, none, (2,2,2,2,4), and (2,2,2,2,2).

The model equivalence is a mathematical input from Barnett–Farber (2009), not an assertion derived solely from the finite script. The theorem does not assert any result about higher-particle spaces, any general graph family, or the exact torsion in first homology. Bibliographic priority and independent validation remain unperformed.
