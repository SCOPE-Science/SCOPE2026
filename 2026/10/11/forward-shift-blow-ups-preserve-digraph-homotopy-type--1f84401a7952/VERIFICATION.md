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

The proof is symbolic and all-parameter. A finite replay is included to check the implementation-level statements used by the proof and to stress-test the directed-cycle corollary.

Running `python verify_forward_shift_blowup.py` produces `VERIFY_OK`. The script exhaustively enumerates every loopless digraph on two and three vertices and every endomorphism \(\tau\) satisfying \(v\to\tau(v)\) at every vertex. For each of 53 resulting endomorphism instances it constructs a nontrivial complete blow-up, checks that the projection and section are digraph maps, checks that \(q=s\tau\pi\) is a digraph map, and checks both one-step homotopies pointwise.

The script also constructs nonuniform complete blow-ups of \(\overrightarrow C_n\) for \(3\le n\le7\). It forms the degree-one boundary matrix, constructs an explicit basis of \(\Omega_2\) from differences of two-step paths sharing endpoints, and performs exact rational elimination. Every sample has \(b_0=b_1=1\). Finally, it checks the unique-skip argument on the base directed cycles for \(3\le n\le12\).

The computations are corroborative only. The infinite statement rests on the explicit homotopy and the direct base-cycle chain argument, not on extrapolation from finite cases.
