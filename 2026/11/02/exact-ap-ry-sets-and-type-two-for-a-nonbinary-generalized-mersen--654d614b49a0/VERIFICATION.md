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

Let t=(h−1)^2, so c=hb+t and b−t=h. Each of the three legal coin exchanges preserves the offset and either decreases cost or preserves cost and increases the number of c-coins. On a fixed offset there are finitely many representations, so reduction terminates; the no-exchange conditions give x<b, y≤h, and x<t if y=h, hence by+x<c. This independently establishes the greedy optimum. For residues dr, coprimality gives precisely offsets r+ell a, and translating by a=mc raises cost by mh^3, so no larger offset or positive a-generator contribution can improve the Apéry minimum. Within each of the first h full b-blocks the discrete weight increases with u, and the last full block and the partial block have equally high endpoints; elsewhere the weight is smaller. The top c-block adds (m−1)h^3, and d>0 makes the later of its two endpoints the unique largest Apéry element. Summing the weights in full and partial blocks gives the stated genus by the Apéry sum identity. For maximality in semigroup order only individual generator steps need be tested, since any increment once outside the Apéry set remains outside. The c-offset eliminates all earlier c-blocks. In the top block any v<c−b can advance by b. Within the remaining portion, the unit step eliminates all but the last full b-block endpoint and v=c−1. The b-offset at these two points wraps, and its residue u lies below b: w(r)≥h²(h−1)=h(b−1)≥w(u). The c-offset wraps with positive excess a(mh^3+d). The unit step fails at the first candidate by the strict cost drop relative to naive carrying, and wraps at the second with positive excess. Thus exactly two maxima remain and their weight difference is zero; their offsets differ by t, so their associated PF numbers differ by dt. This covers m=1, including a redundant fourth generator. A separate residue shortest-path check verified every residue and F, genus and PF in six cases (h,m,d)=(3,1,1),(3,2,51),(4,1,123),(4,3,2),(5,2,3),(6,1,5), including d>a. To replay, use the residues modulo a as vertices, with one edge adding each of the other three generators, weighted by that generator. Find shortest distances from residue 0, then compute gaps by the distance threshold and test each Apéry element minus a for the PF condition by the same modular-distance tests after adding each generator. The first example gives F=899, g=504, PF={895,899}. The frozen checker.py additionally describes larger finite diagnostics; neither experiment substitutes for the unrestricted proof.

## originality

PASS

The underlying higher-base family and its orderly coin minimization are already known; the Apéry formula uses that known machinery and the divisible-offset hypothesis. The supported distinct content is the evaluation of the tied extremal weights and the exact two-element pseudo-Frobenius spectrum in the nonbinary cubic subfamily, not the binary case or greedy change-making. An exactly equivalent distinct indexed record dated later was inspected and is disclosed; it does not establish earlier priority or unique provenance for either proof. No inspected earlier result mechanically gives the nonbinary maximal Apéry classification.

## value

PASS

The shifted-power family is explicitly motivated in the earlier literature. Taking the initial generator to be a multiple of the terminal offset isolates the failure of naive weight monotonicity in a meaningful cubic subfamily, rather than imposing an arbitrary finite cutoff. The exact PF classification explains why precisely two top-block residues survive and why the separation is independent of m. This is a natural type and spectrum computation for all h, m and admissible d in the stated regime; it does not claim to solve the unrestricted higher-base problem.

The dated certificate retains the supplied scientific assessment, sources and limitations.
