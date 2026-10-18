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

# Reproduction and proof boundary

With Python 3 standard library, from the directory containing these attachments run:

```sh
python3 verify_square_bouquet.py
python3 check_collapse.py
```

The outputs are stored verbatim in `verify_square_bouquet.out` and `check_collapse.out`. The first program independently constructs the strong matchings from all vertex orderings, without assuming the join-and-cone decomposition. It separately builds the proposed local factors and checks equality of every generated face for one, two, and three petals; it also computes all mod-two boundary ranks.

For the one-petal complex it reconstructs 8 vertices, 12 edges, and first Betti number 5. For two petals it reconstructs 296 nonempty faces and reduced mod-two Betti number 1 in degree 3. For three petals it reconstructs 3,732 nonempty faces and reduced mod-two Betti number 1 in degree 5. The second program checks the entire 64-pair elementary simplicial collapse for two petals and the entire 768-pair collapse for three petals, ending **exactly** at their respective six-cycle joins. Every removed codimension-one face is verified to have a unique remaining coface.

These calculations are exhaustive within the three enumerated finite cases but are **not** an exhaustive proof for unbounded numbers of petals or an integral classification on their own. The general proof is the explicit local order classification and relative-cone collapse in `RESULT.md`, which holds uniformly for every integer \(p\ge2\). The six-cycle join is a PL sphere; thus its homotopy and integral homology follow without inferring integral torsion-freeness from mod-two computations. Independent audit is not performed.
