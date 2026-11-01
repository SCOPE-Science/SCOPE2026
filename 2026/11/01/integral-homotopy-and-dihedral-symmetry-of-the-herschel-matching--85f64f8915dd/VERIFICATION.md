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

# Verification record

The complete, executable certificate is `verify_herschel.py`; the actual recorded output of its successful execution is `verification_output.txt`. The program is self-contained and requires only the Python standard library.

The graph is supplied as an exact eighteen-edge labeled list. Enumerating all matchings yields \(751\) nonempty simplices, with dimension counts \((18,111,280,270,72)\). Greedy edge toggles generate \(367\) matched face pairs and critical-cell counts \((c_0,c_2,c_3)=(1,2,14)\). The full \(2502\)-relation directed Hasse graph is acyclic, checked by topological sorting. Sign-aware gradient-path projection gives the listed integer Morse matrix; a determinant \(-1\) minor, not modular rank alone, establishes integral cancellations. All three auxiliary full-chain modular boundary-rank calculations agree.

The program enumerates exactly \(12\) graph automorphisms by adjacency-preserving backtracking and checks explicit generators of \(D_6\). Signed simplex fixed-point traces for every automorphism give the two stated six-element character lists; exact character inner products yield \((1,0,0,1,3,2)\). Averaging gives one invariant rational homology generator, in degree three.

The proof is specific to this complex; finite examples are not used to extrapolate an infinite-family theorem. A matching complex is distinguished throughout from the independence complex of the original graph. Self-review confirms the documented scientific argument and computations; independent audit and external priority verification have not been performed.
