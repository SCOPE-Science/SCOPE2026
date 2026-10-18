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

The mathematical proof in `RESULT.md` establishes exact results for all integer moduli \(r\ge2\). Its critical invariants are (i) the binary-MSD counts of completed \(11\) pairs in both phase alignments, (ii) reachable and distinguishable states obtained using the words \(1100\), \(0110\), and phase-testing suffixes, and (iii) binary-LSD residue and pending-low-bit states separated by explicit suffix families. The edge case \(r=2\) is covered because \(1\not\equiv0\pmod r\).

The independent finite consistency check is reproducible with `python3 verification/checker.py`; it uses only the Python standard library. The verifier independently minimizes all three explicit automata by partition refinement, checks that every proposed state is reachable, and verifies outputs against direct base-four digit counts for all \(0\le n<512\), four padding choices, and eight moduli \(2\le r\le9\). The expected exact log is in `verification/checker_output.txt`. Finite automaton experiments cannot replace the parameter-uniform reachability and distinguishability arguments.

No external or independent scientific review is claimed.
