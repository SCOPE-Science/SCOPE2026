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

Checked the all-length proof directly. The identities p[2i]=0 and p[2i+1]=1−p[i] forbid 11 and then 0000. Every even-length window of 2n letters is either an aligned image of a length-n factor or its one-step rotation (the next block's leading zero wraps to the end). For n≥2 images contain a 1, so the two relative parities are disjoint, injective phases, and even rotations desubstitute to ordinary rotations. Thus every represented class lifts with twice its cardinality. For odd m, the only odd circular distance between successive 1s is the closing distance g; in any factor rotation it straddles the boundary, so the initial and final zero lengths s,t satisfy s+t=g−1 with 0≤s,t≤3. The possibilities g=1,3,5,7 permit at most 1,3,3,1 cuts respectively, and the all-zero factor contributes size at most one. For the sharp lower bound, any even distance 2e is realized between ones: choose even j with j+e even if e is even, or j+e≡3 mod 8 if e is odd, to get p[j]=p[j+e]=0 and ones at the corresponding odd positions. Choose even d amongst (m−1)/2,(m+1)/2; the two ones at distance d create two 000 runs under substitution, whose 00 starts can be picked at distance 2d±1=m. In 00u00 the three shifted m-windows are distinct, since period one or rotation by two at odd length would force a constant word, contradicting no 0000. The bases M(1)=1 and M(2)=2 and iteration give the formula; a class of size n entails primitivity. Inspected the finite checker and its two-block completeness argument, without executing it; the proof does not use that checker or extrapolate from length 192.

## originality

PASS

Credit the exact maximum, especially the sharp three rotations at every odd length m≥5 and the resulting 2-adic law at all their multiples. The earlier Lie-complexity result already covers the full primitive-orbit existence corollary via its explicit fully represented classes and uses the same phase lifting for complete classes. The extension of that phase argument yields classwise doubling; it is not a distinct novelty pillar. The inspected earlier sources do not imply the matching upper and lower multiplicities for partially represented classes at every odd length.

## value

PASS

Partial conjugacy multiplicity measures an aspect of the factor language not given by aggregate cyclic complexity or the census of complete classes. The gap and triple-witness arguments resolve its extremal law uniformly, including all odd lengths where no complete orbit exists. This is a structural refinement of a natural invariant rather than a finite table or a restatement of Lie complexity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
