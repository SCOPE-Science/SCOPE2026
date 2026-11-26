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

In characteristic three the original branch polynomial is Xh³, and h² accounts for the square ratio to Xh wherever h≠0. At zeros the two equations both give exactly one affine point, and both monic even-degree models contribute two smooth rational points at infinity. This proves the zeta equality over all extensions, including reducible parameters. The derivative h′=c−X isolates the only possible repeated root, c; h(c)=c³−c²+d, so the repeated-root and zero-root loci are b=D and b=0. In the complement the root multiplicities are 1,3,3,3; on the separate b=0 and b=D branches they are respectively 4,3,3 and 1,6,3. At (0,0) they are 7,3, and at (1,0) the whole polynomial is X⁴(X−1)⁶. Units in the geometric completed local rings have square roots, yielding the asserted local equations; the nonsquare cases are geometrically integral. When smooth, the quartic transforms to W²=1+t+ct²+dt³, whose Cartier coefficient in characteristic three is c, giving the supersingularity criterion. Dividing the quartic by the square factors at the two-branch boundary gives smooth genus-zero conics with rational points; at the affected point the preimages satisfy W²=c in both cases. Thus normalization correction is −χ_q(c)^m=−χ_q(a)^m in degree m. At (0,0) there is no split-branch correction and the normalization is rational; at (1,0) there are two rational components meeting at two rational points, giving 2q^m. The two exceptional parameter loci have precisely two intersections, giving all five frequencies. The phrase ‘rational cuspidal normalization’ in the frequency summary refers to the cuspidal fiber with smooth rational normalization, as stated in case 3 and the proof; the normalization itself has no cusp. A separate direct square-root count from the expanded equations checked every pair over fields of sizes 3 and 9, including the trace criterion modulo 3 and every boundary count.

## originality

PASS

The degree-ten pencil and the Hasse–Witt technique are known. The supported distinction is the full characteristic-three classification of this singular specialization and its normalization/zeta strata, including the exceptional pairwise intersections. The closest inspected same-equation results address smooth curves in different characteristics, and the closest characteristic-three result uses a different smooth equation.

## value

PASS

Characteristic three is a natural bad prime for the cyclic-six pencil. Determining only that the branch polynomial is inseparable would miss the elliptic locus and its ordinary/supersingular split, the two exceptional parameter curves, and the dependence of the boundary zeta factor on branch splitting. The complete classification gives concrete arithmetic information on every specialization, rather than a selected finite-field sample.

The dated certificate retains the supplied scientific assessment, sources and limitations.
