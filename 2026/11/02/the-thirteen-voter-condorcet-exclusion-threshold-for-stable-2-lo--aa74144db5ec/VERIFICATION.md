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

For each voter, the attacker copy's conditional rank is uniform on the candidate's probability interval, or equals its collapsed rank if the mass is zero. The probability of beating both independent defender ranks averages to ell²+ell z+z²/3. Averaging against the candidate weights integrates rank² on [0,1], giving sum D(x)H_x(D)=1/3. Existence at this value can also be seen directly: the continuous simplex map D↦(D+g)/(1+sum g) with g_x=max(H_x−1/3,0) has a Brouwer fixed point. If sum g>0 there, every supported candidate has payoff above 1/3, contradicting the identity. Thus stability is exactly H_x≤1/3 for all x, with equality on support. If a strict winner A is omitted, singleton support makes H_A>1/2, and for interior B,C support equality gives x=D(B)=(3u−n)/n, u the integer B-over-C count. With k=floor(n/2)+1, the counts t of A-first ballots and b,c of A-middle ballots satisfy t+b,t+c≥k and t≥2k−n. If t≥k then H_A≥k/n>1/3. Otherwise H_A≥[(2k−n)+(n−k)(x²+(1−x)²)]/n. For even n≤12 this is at least 3/8; for odd n≥3 the integer grid gives |x−1/2|≥3/(2n), and the resulting bound decreases to 446/1331>1/3 at n=11. At n=1 the strict winner tops the ballot and omission gives H_A=1. For the given 13 ballots the payoff triple is (703/2197,1/3,1/3), with both pairwise margins 7–6. For any stable lottery on this profile the B inequality yields b≥5/13, where b denotes its mass. At each such b the C payoff decreases strictly with its mass c over c≤1−b, since its derivative is at most (8−23b)/39<0. The minimum at c=1−b exceeds 1/3 by b(13b−5)/39 unless b=5/13. So the displayed lottery is unique. Fresh exact anonymous-profile enumeration found no omissions through 12, and 2 at 13 among 2688 strict-A-winner profiles and 1288 interior stationary pairs. It corroborates the bound, and does not assert uniqueness of the profile.

## originality

PASS

Credit is confined to the sharp electorate threshold over all strict three-alternative profiles, specifically the obstruction through twelve even with all six rankings allowed. The thirteen-voter example and its unique outcome already follow from the stronger criterion on the single-peaked subdomain in Resultary 10a294dece8f; they are not separately novel. Shah's prior uniqueness theorem and symmetric exclusion construction also cover those kinds of conclusions. The bounded comparisons do not supply the unrestricted lower bound. The frozen statement names the sharp threshold as its contribution; the Appendix A comparison for eighteen voters is an adaptation of the proof, not a literal case of Cai et al.'s stated distortion theorem.

## value

PASS

The previous qualitative possibility does not identify the smallest strict electorate where this minimax rule can exclude the pairwise winner. The universal small-electorate guarantee and exact boundary are meaningful for judging how early the support anomaly can occur, and avoid interpreting it as an artifact of a choice among multiple stable outcomes in the example.

The dated certificate retains the supplied scientific assessment, sources and limitations.
