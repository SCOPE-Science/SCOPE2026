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

The exact checker `verify.py` performs the following finite checks with integer projective arithmetic:

- the four quotient lines meet at \([1:1:2]\);
- the coordinate entries of their intersections with \(aX+bY+cZ=0\) yield exactly the six branch forms \(a+b\), \(a-b\), \(a+c\), \(b+c\), \(a+2c\), \(b+2c\);
- the six branch lines in parameter space have exactly one admissible triple point, \([2:2:-1]\), and exactly six admissible double points, matching the Finding;
- intersections of the free line \(a+b+2c=0\) with the branch divisor are only singular diagonal conics or the already-present conic, so the valid free-line case has no hidden branch collision;
- the intersection cardinalities are \(4,10,12,14,16\) in the five strata and map to the source theorem’s free/free/plus-one/neither/neither cases;
- the two diagonal conics explicitly printed in Example 4.1 fall into the predicted free and plus-one generated strata.

The local analytic statements are checked by proof rather than finite enumeration. For \(a+b+2c=0\), the relevant conics form one pencil and two generators have independent gradients at each of its four base points, so they are analytic local coordinates and the local equation is a product of distinct linear forms. For \(a+b+2c\neq0\), each branch condition restricts the added conic to a nonzero square on the affected smooth base branch, giving contact exactly two and hence an \(A_3\) singularity.

The checker does not independently reprove Măcinic’s general addition theorem or resolution corollary. Those are external mathematical inputs and are explicitly cited in the result.
