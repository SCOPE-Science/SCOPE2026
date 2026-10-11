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

`base_verify.py` reconstructs the full independence complex of \(G(8,3)\), checks all \(4272\) Hasse covers, verifies a complete acyclic Morse matching, and computes its exact integral Morse boundary. This proves that positive-dimensional integral homology is \(H_3\cong\mathbb Z^4\) and \(H_4\cong\mathbb Z\), with all other positive groups zero.

`verify.py` then checks that the simultaneous cyclic shift has order \(8\) and preserves all \(24\) graph edges. For each power it computes signed traces on every oriented simplicial chain group and hence the exact Lefschetz vector
\[
(-2,0,2,0,-2,0,2,0).
\]

The action on the rank-one degree-\(4\) homology quotient is computed independently modulo \(3\) and modulo \(5\). Both tests distinguish the generator from the identity and give the sign character. The degree-\(3\) character is then recovered from the Lefschetz identity using the independently proved homology support. Finally the script checks the character identity
\[
\chi_{H_3}=\chi_{\mathbf1}+\chi_{\varepsilon}+\chi_{V_4},
\]
where \(V_4\) has minimal polynomial \(x^2+1\) for the cyclic generator.

The computation is exhaustive on the finite complex. No timeout, random sample, or finite experiment is used as a substitute for an infinite theorem.
