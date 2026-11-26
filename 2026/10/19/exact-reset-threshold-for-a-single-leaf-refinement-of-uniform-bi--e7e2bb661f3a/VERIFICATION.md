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

The literal states are all prefixes of lengths 0 through m−1 and the extra prefix 1^m, totaling 2^m. With F=01^m, processing a prefix of length h≤m−2 completes a short word containing the zero and leaves h+1 ones. At h=m−1 or state 1^m the zero finishes a word immediately, leaving m ones; thus F raises/saturates the all-one heights and F^(m−1)0 resets at length m². For the lower bound let f be the length of the common output (not assumed zero), and let E_h count long words parsed from 0^h followed by input w. Then the residues E_h≡L+h−f mod m cover all m residues. The thread of residue m−1 must complete at least m−1 long words. If h>0, the initial codeword necessarily is short and consumes m−h≥1 input letters; this already forces m². If h=0 and L<m², the only candidate has L=m²−1, f=0, and is a concatenation of m−1 blocks 1^m c_j. Starting at state 0 uses m−1 input letters in the first short word, after which the congruence forces zero long completions (m such words would exceed the remainder). The successive length-m blocks occupy jm,…,(j+1)m−1 and contain the unique optional letter c_j at j(m+1), so all c_j must be zero. From state 1, the first block 1^m0 ends at 0; subsequent blocks send 1^r0 to 1^(r+1)0 in the needed range 0≤r≤m−3. This leaves the distinct nonroot output 1^(m−2)0 versus the root, including m=2. In the unrefined decoder the state length changes by +1 modulo m on every letter, preserving distinct phases. Independent exact replay: python3 /workspace/branches/independent_checks.py 3 builds codewords and their strict prefixes explicitly and runs frozenset subset BFS; thresholds at m=2,…,6 are 4,9,16,25,36 and the displayed word resets to the root in each. This replay is finite, not the general proof. The frozen checker and recorded output were inspected, not executed.

## originality

PASS

The exact threshold and shortest word for this one-refined-leaf literal decoder stand apart from inspected general bounds and from exact extremizers with one short leaf. Chadha's two-consecutive-depth theorem includes exactly X_m as an instance, so synchronizability and a quadratic bound are covered; its strict bound for this instance is 2m²−2, not a proof of equality at m². The general exact family claim is supported by the explicit witness and lower bound. The closest older Huffman synchronizing-family constructions remain a real priority risk because their formulas could not be lawfully inspected.

## value

PASS

An equally spaced decoder cannot lose its length phase. The smallest tree refinement of the constant branch changes that obstruction while preserving all but one short codeword. An exact uniform minimum for this canonical perturbation determines synchronization cost in both code depth and literal state count, and why the last one-letter saving from the modular bound is impossible. The answer is useful independently of a general algorithm for exact reset thresholds.

The dated certificate retains the supplied scientific assessment, sources and limitations.
