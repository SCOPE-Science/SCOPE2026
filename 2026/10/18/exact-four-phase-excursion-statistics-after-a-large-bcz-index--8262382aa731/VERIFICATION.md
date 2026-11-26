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

The chart t=(1+a-kb)/b, s=(1-a)/b sends the k-cylinder to the unit square up to null boundaries, with b=2/(k+t+s), c=kb-a=1-bt and probability density 8/(k+t+s)^3. The first post-k digit is 1 because (1+b)/c is in [1,2) for k>=12. At time 2+j on the proposed run the pair is (c-jb,c-(j+1)b); the floor argument is at least 2 and strictly less than 3 exactly for j<R=(k+s-3t-6)/4. For j<=ceil(R) the smaller coordinate divided by b is at least (k+s+t-2)/4>0. Thus L=ceil(R), with strict inequality at the stopping boundary. Integrating the density over the square yields total mass 8/[k(k+1)(k+2)]. The three exceptional subregions are s<=3t-2 at r=0, s>3t at r=2, and s>3t-1 at r=3; r=1 has no internal cut. Integrating (k+t+s)^(-3) first in s and then by the reciprocal antiderivative in t gives exactly the three ratios k/[2(3k+2)], (k+2)/[2(3k+4)], and (k+2)(9k+5)/[2(3k+1)(3k+5)]. The bounded distance from k/4 and residue-specific limits follow directly. Read the frozen rational itinerary checker; independently checked the masses and tail ratios via exact polygon clipping in the original (a,b) coordinates for k=12..240 (independent_checks.py bcz). The finite replay corroborates the universal calculation, which does not assume independent digits.

## originality

PASS

Pass for the evaluated digit-conditioned finite-k probabilities and four residue-specific laws, not for the existence of a long 2-run, its pointwise exit clock, or the use of itinerary polygons. The same-day roof-conditioned archive result gives the equivalent deterministic clock, and earlier literature covers a uniform forced run and general polygon machinery. The exact masses at the moving exit boundary distinguish the finding and were not established by those comparisons.

## value

PASS

For the natural rare event of a large BCZ digit, the growth-order law L~k/4 cannot distinguish deterministic, rare-extra-step, and nearly equiprobable behavior. The explicit probability at the final step answers this local dynamical question uniformly for all large digits and reveals a four-phase law that the standard forced-prefix and macroscopic excursion estimates miss. The distinct value is the finite conditional law, not the elementary coordinate change or the first-order scale.

The dated certificate retains the supplied scientific assessment, sources and limitations.
