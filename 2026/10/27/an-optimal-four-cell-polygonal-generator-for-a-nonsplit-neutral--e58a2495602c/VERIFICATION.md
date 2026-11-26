---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

The merged labels are precisely the greedy ternary digits of y. For a.e. y the points v_n=3^n y mod 2 are equidistributed on [0,2); this follows from ergodicity of tripling on the doubled circle and remains true for a.e. y in its subinterval [0,1). The recurrence gives x_n=z+v_n/2 mod 1 and y_n={v_n}, where z={x-y/2}. Sheet j=0,1 therefore supplies a dense set of comparisons {s+t/2}<3t with s={z+j/2}. Before wrap the comparison opens at 2s/5; on wrap it is true, giving threshold min(2s/5,2(1-s)). Taking the first label-0 infimum on each dense return set, or 1/3 if that label is absent, handles the maximum threshold and all equality conventions. Two distinct equal first thresholds force z'=1-z/5 with z<5/6<z'. Comparing the translated thresholds on z<1/3, 1/3<=z<1/2, and z>=1/2 gives only the nontrivial pair 5/12,11/12. The excluded fibers and atypical base orbits are Haar-null. Independently the Haar-preserving, piecewise-affine measurable conjugacy a={2x-y}, b={x-a/2} with inverse x={b+a/2}, y={2b}, gives (a,b)->(a,{3b}), entropy log 3 and nonergodicity. A generating three-letter name at that entropy must have entropy n log 3 for every length-n block and hence be uniform i.i.d., an ergodic process; fewer letters violate the entropy bound. Replay: RESULT.md lines 22–60. The frozen rational checker and recorded outputs were inspected, not executed; their samples do not establish equidistribution or the entropy obstruction.

## originality

PASS

The distinct contribution is the displayed generator with exactly four single polygonal cells in the original square, refining the original y digit partition by splitting only its bottom strip with the line x=3y. The optimal cardinality alone (even for piecewise-affine boundaries allowing disconnected atoms) is a corollary of the preceding split-product result via an explicit piecewise-affine measurable conjugacy and is not credited as new.

## value

PASS

An optimal alphabet with a single straight cut of one of the original digit strips preserves direct access to the natural expanding coordinate. The doubled-circle decoder shows how this coarser geometric constraint can still retain the neutral sheet information, which a partition pulled back through the natural two-to-one factor cannot retain. The value is in this concrete simple coding and its decoder, not in a new entropy theorem, a general classification or a claim about Markov coding.

The dated certificate retains the supplied scientific assessment, sources and limitations.
