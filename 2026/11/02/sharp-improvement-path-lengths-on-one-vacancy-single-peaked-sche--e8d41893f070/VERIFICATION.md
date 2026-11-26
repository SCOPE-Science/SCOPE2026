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

For a nonadjacent jumper, the only nonzero fractions to compare are 1/3 and 2/3; on the descending side the reflected arguments give their stated order and tie at half. An adjacent jump keeps the denominator two and can improve only from 1 to 1/2. The occupied path has N-2 edges and contains both colors. Below half each improvement removes one or two same-color edges: into a mixed hole a nonadjacent agent must start at fraction 1, while into a homogeneous hole a nonadjacent improving agent adds zero same-color edges and removes at least one. At or above half a mixed hole always becomes homogeneous after a strict move. With a homogeneous hole any strict move is nonadjacent and takes an agent from fraction 1 to 1/3, removes exactly two same-color edges and leaves the hole homogeneous. Such an occupied path has at least two color changes, so M<=N-4. This yields both bounds and rules out cycles. The low-peak witness consumes one symbol from each initial long run per pair, including the step with a B run of length two (the first jump there is adjacent and goes from 1 to 1/2); the even case has one last adjacent improvement. For the high-peak witness after the adjacent first R jump the usable R and B runs have lengths r-1 and b. Selecting the second vertex of a run reduces its remaining long part by two, while filling the homogeneous hole with the opposite color does not grow other runs. For N congruent to 0, 1, or 3 mod 4 the respective capacities floor((r-2)/2) and floor((b-1)/2) suffice for the alternating schedule. For N congruent to 2 mod 4 with N>=6 the nonadjacent first B jump leaves capacities floor((r-1)/2) and floor((b-2)/2), with the B run wrapping around the fixed origin; choosing its second vertex in cyclic order gives the required losses. N=3 has zero moves, and N=4 has one in both regimes; the split gives different maxima for N>=5. An independent exhaustive search of rotated vacancy-normalized states confirmed both maxima and checked acyclicity for 3<=N<=12 in all three utility orderings, including the tie. Quotienting by rotation and ignoring identities preserves the possible color trajectories because admissibility depends only on the moving color and its origin and target neighborhoods; every color path lifts to labelled agents.

## originality

PASS

Friedrich et al. already prove convergence at peak 1/2 with an explicit bound of N-1 moves, counting vertices here. This half-peak convergence and the general use of an ordinal potential are not new. The exact worst-case formula, its extremal trajectories, and the all-peaks result with its strict cutoff are not supplied by the checked prior statements.

## value

PASS

For this canonical one-vacancy dynamics, exact worst-case convergence separates a regime in which one edge can be lost per step from a regime with an absorbing vacancy configuration and two-edge losses. The constructive maxima quantify the change that a generic finite-improvement result cannot capture, and give a meaningful reference case next to known cycling in the multiple-vacancy setting.

The dated certificate retains the supplied scientific assessment, sources and limitations.
