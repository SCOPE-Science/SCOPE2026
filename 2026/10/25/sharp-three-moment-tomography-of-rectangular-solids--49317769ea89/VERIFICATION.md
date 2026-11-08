---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-02.md",
      "INDEPENDENT_AUDIT_2026-11-02.json"
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

For squared sides s_i>0, Z=D²=Σ_i s_iW_i with W=(U-V)² and E(W^k)=2/((2k+1)(2k+2)). Direct integration gives κ1(W)=1/6, κ2(W)=7/180, κ3(W)=11/945; hence the displayed S1=6M2,S2=(180/7)(M4−M2²),S3=(945/11)(M6−3M4M2+2M2³) equal Σs_i^j. Newton yields the cubic with all roots positive, even at multiplicities. With r_i=s_i/S1, u=Σr_i²,v=Σr_i³, a real-rooted normalized cubic q(z)=z³−z²+(1−u)z/2−(1−3u+2v)/6 has discriminant nonnegative iff |v−(u−2/9)|≤[2(3u−1)]^{3/2}/36. Positive product v>(3u−1)/2 and positive pair sum with total 1 force all roots positive; for 1/3<u<1/2 the discriminant interval is entirely positive; at u=1/2 zero-edge lower equality is excluded; cube is u=1/3,v=1/9. Volume²=s1s2s3=36M2³(1−3u+2v). Distinct triples (1±2t,1∓t,1∓t) share M2,M4 but differ in M6 by 44t³/315. For δ in (0,1/2), R=(2δ)^{1/3} and Rouché on union of old-root radius-R disks proves equal root counts by components because |q|≥2δ>|q−qtilde| there; each component has length ≤6R and sorted real roots match. Larger δ bound trivial. Near the cube, the ±t triples have normalized sorted-root gap 2t/3 and δ=4t³/9, ruling out any exponent >1/3. All boundaries, quantifiers and degeneracy restrictions checked.

## originality

PASS

A full 2007 primary forward density for varying box sides is important prior coverage and is explicitly credited. Its law gives ALL distance moments and the complete distance distribution; the new finite-observation claim is specifically that three even moments suffice, two do not, with the exact attainable normalized (u,v) domain and optimal global inverse exponent 1/3. Those assertions are not stated in the inspected Philip primary report. Abas 2026 proves three-cumulant inversion for spherical directional widths, not two-point interior distances. Classical cumulants, Newton inversion, cubic discriminant and general root continuity are not claimed as novel by themselves. No direct prior theorem covering the combined finite-statistic distance-moment statement was found in actual primary/source/corpus searches. Because full-law data is stronger, originality is restricted to minimal-data recovery and sharp feasible/stability specification, with a real risk that these are elementary corollaries of established forward formulas.

## value

PASS

Given an unlabeled one-dimensional point-pair distance statistic from a nondegenerate orthogonal box, the natural inverse task is to recover the three side lengths. Determining the exact minimal initial even-moment cutoff is a motivated finite-statistic identifiability question; two moments have a continuum of incompatible boxes, three recover the exact geometry. The complete physically realizable normalized-moment region identifies consistent data and the exact boundary where a dimension collapses; the sharp 1/3 Hölder exponent gives intrinsic ill-conditioning at cubes. These are coherent natural geometric-statistical invariants beyond quoting a cube table, even though elementary cumulants/Newton/root stability are the proof tools and the full forward density is long known. No general downstream paper-size result is required.

The dated certificate retains the supplied scientific assessment, sources and limitations.
