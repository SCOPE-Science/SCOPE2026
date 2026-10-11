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
The checked claim is:

Let \(L_3=P_3\mathbin{\square}K_2\) be the three-rung ladder graph. For its ordinary Morse complex \(\mathcal M(L_3)\) of acyclic discrete vector fields, \[\mathcal M(L_3)\simeq \bigvee^{2}S^{3}\vee\bigvee^{2}S^{4}.\]

`verify.py` reconstructs the seven-edge ladder and all fourteen primitive vector fields. It enumerates the Morse-complex faces in two independent finite representations and verifies exact agreement on \(575\) nonempty faces with face vector \((14,74,184,213,90)\).

It then applies the fixed primitive-toggle order \(12,10,3,5,13,4,1,11,6,0,2,9,7,8\), checks all \(285\) matched cover pairs and all \(2002\) Hasse covers, and topologically sorts the fully oriented Hasse graph after matching reversals. The critical profile is exactly one cell in dimension \(0\), two in dimension \(3\), and two in dimension \(4\).

Exact signed gradient-path elimination computes the integral Morse boundary from degree \(4\) to degree \(3\) as the zero \(2\times2\) matrix. Direct simplicial homology over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\) independently gives Betti vector \((1,0,0,2,2)\).

The verifier also checks that the double-oriented ladder has no dominant pair, documenting why the dominant-pair shellability theorem does not specialize to this graph. The successful terminal marker is `LADDER_MORSE_VERIFY_OK`.

The computation is exhaustive for \(L_3\) only. It does not prove any assertion for larger ladders and does not itself establish literature originality.
