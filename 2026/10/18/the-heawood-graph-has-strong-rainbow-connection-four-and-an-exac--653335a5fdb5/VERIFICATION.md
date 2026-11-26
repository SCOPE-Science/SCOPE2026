---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

Any two distinct points are on a unique line and any two lines meet at one point. Thus a pair of adjacent edges is the unique two-step geodesic between its other endpoints; strong rainbow colouring forces propriety, including with the fourth colour. A nonincident point–line pair has precisely three geodesics of length three, one per point on the target line. Consequently only the 28 nonincidences need testing once propriety holds. I independently enumerated colour permutations at each point, discarding line conflicts and normalizing at point 0. There are eight classes, the eight frozen obstruction strings all match, each failed set is a bijection of points to nonincident lines, and every nonincidence occurs twice. A second recursion generated matchings as partial injections of points into incident lines. For each geodesic and input colouring I tested admissible intersections with the matching: zero recoloured edges if the original path is rainbow, one if the two retained colours differ, never two or more. This reproduced the all-matching vector (1,21,168,644,1218,1050,336,24) and the success vector (0,0,0,0,126,84,0,0) for each of the eight classes. The specific frozen four-colour witness passed. Palette renaming multiplies the class count by 6 and preserves successes. Nonmatching recolourings cannot avoid adjacent new-colour conflicts, so the four-edge minimum is exact within the specified model and src(H)=4.

## originality

PASS

The factorization counts and Fano incidence facts are known inputs. The supported distinct finding is the rainbow-geodesic obstruction design and its quantitative fresh-colour matching repair census, including an exact witness and minimum. The available comparisons establish the invariant and computational methods but did not yield those counts or an equivalent result. Priority of the bare src value is less well resolved than that of the joint census.

## value

PASS

The canonical cubic Fano incidence graph is a natural distance-three test case. Beyond the optimal value, the obstruction incidence pattern and full repair polynomial measure how a standard proper colouring can be changed to make all distances work. The loss of all successes again at six or seven recolourings is a meaningful nonmonotone effect, not implied by the existence of one successful repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.
