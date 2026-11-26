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

The repaired distinct claim is the large-step P₄ witness; the multipartite parity and scalar results are retained as proved comparisons. For each even s the two top coefficients of the exact Padé polynomial satisfy a_(s,s−1)/a_(s,s)=s(s+1). Dividing at infinity gives R_s(−x)=1−2s(s+1)/x+O_s(x^−2). The constant eigenspace has multiplier exactly 1, so on the fixed path the expansion at each positive eigenvalue yields I−2s(s+1)L†/h+O_s(h^−2). Independently, path effective resistances are d_ij=|i−j| and L† is minus half the doubly centered resistance matrix. Row sums of the resistance matrix for vertices 1 and 2 are 6 and 4 and its total sum is 20, giving (L†)_12=−(1−6/4−4/4+20/16)/2=1/8. The coefficient is therefore −s(s+1)/4, strictly negative at every even s. All connected bipartite graphs on at most three vertices other than the singleton are complete bipartite; the singleton step is the identity. For the comparison, the coefficient ratios a_(s,2i)/a_(s,2i+1) increase, with a terminal unpaired even coefficient harmless in the cross-products. Thus E/O is nondecreasing and 2/(x+E(x²)/O(x²)) strictly decreases. The exact factorial-integral representation makes the numerator strictly positive for even s, and positivity of the even and odd parts gives |R_s(−x)|<1 for finite x>0. The multipartite contrast projectors yield positive off-diagonals by strict deficit monotonicity, and positive eigenvalues give positive diagonals. Odd s has graph limit 2J/n−I, while K₂ has positive entries from the strict scalar bound. No internal-stage claim is made. Frozen verify.py and its recorded exact finite checks were inspected without running it.

## originality

PASS

For the narrowed Finding only: the exact same-entry P₄ large-step coefficient across all even stage counts is distinct from the known multipartite criterion and the classical scalar mechanism. The replacements do not claim priority for deficit monotonicity, the projector implication, the two-stage benchmark, or the elementary odd limiting mechanism.

## value

PASS

The obstruction answers a motivated sharp-boundary question: whether unconditional positivity for arbitrarily high even orders extends to all connected bipartite meshes. P₄ is smallest possible, and a signed coefficient for the identical entry at every even order resolves the obstruction quantitatively rather than by a single low-order example or a generic existence argument. The classical scalar and multipartite results explain why this boundary is meaningful without being counted as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
