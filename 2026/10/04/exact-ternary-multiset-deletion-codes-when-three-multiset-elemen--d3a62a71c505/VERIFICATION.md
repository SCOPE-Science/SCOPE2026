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

`verify.py` uses only the Python standard library. It performs the following checks:

- enumerates every ternary composition at \(n=5\) and \(n=6\);
- verifies the stated four-word witnesses;
- exhaustively checks every five-subset at those two lengths and confirms that none satisfies pairwise multiset intersection at most two;
- confirms that the heavy-free words at \(n=5\) are exactly the permutations of \((2,2,1)\), and that any two of them are incompatible;
- confirms that \((2,2,2)\) is the unique heavy-free word at \(n=6\);
- checks on \(7\le n\le30\) that every composition has a heavy coordinate, as a finite consistency check of the pigeonhole premise.

Replay from the packaged verifier returns `VERIFY_OK`. The finite range check for \(n\ge7\) is not used as an infinite certificate: the proof in `RESULT.md` establishes that premise for all \(n\ge7\) because three coordinates each at most two would sum to at most six.

The originality comparison used the current full text of arXiv:2601.05636v2 and the foundational arXiv:1612.08837v5, plus searches under deletion, intersection, and discrete-simplex aliases. No independent audit has been performed.
