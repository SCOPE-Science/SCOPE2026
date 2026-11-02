---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-29.md",
      "INDEPENDENT_AUDIT_2026-10-29.json"
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

For r=2k source relations, the finite tag set has M=1+r(t+1)+sum binary one bits, t=ceil(log2 r). Only root and marker vertices loop; the root detector R(v,v)&exists nonself successor identifies precisely (a,rho). Each path length t+2 with loop-free internal positions is forced along one tagged layer chain; bit-marker tests at positions 1..t recover unique relation i, and only the layer-t to t+1 edge carries S_i(a,b). FO3 path formulas of O(t) syntax-tree size use a held endpoint and alternating rebindings of two scratch variable names; inner-scope marker tests use a spare name and close before further path traversal. For an arbitrary one-relation CoR circuit, the M² tagged blocks of every gate can be simulated with free Boolean and converse operations; each composition (G;H)_{uv}=union_w G_{uw};H_{wv} introduces at most M³ composition gates across all blocks, including shared subcircuits. The root-root block computes Uezato Phi_k on every finite base structure, so his actual Theorem 1.3, independently checked against primary full arXiv HTML, forces 2^(k-1)<=M³*g_(;). Thus a family of size O(klog k) needs 2^Omega(s/log s) composition gates. Inspected actual fixed_signature_gap_checker.py implementation and its finite sample scope; unlike source output, no unperformed run is claimed. Imported Theorem 1.3 is a published premise, not independently reproved.

## originality

PASS

Best-of-knowledge original fixed one-relation near-exponential composition-gate lower bound, conditional on published growing-vocabulary theorem. Full Uezato Theorem 1.3 and Remark 4.1 inspected and correctly match the precise hard formula and explicitly leave fixed signature open; source has not proven the fully exponential fixed-signature gap.

## value

PASS

The result establishes a quantitative near-exponential lower bound in the previously explicitly open fixed-vocabulary setting, preserving the meaningful composition-gate metric even for circuits with unrestricted sharing. The construction is nontrivial because both FO3 definability at O(log k) per label and M³ block-simulation cost are essential; it does not claim the fully exponential or positive-fragment open problem solved.

The dated certificate retains the supplied scientific assessment, sources and limitations.
