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

The primary family data were checked directly in arXiv:2510.07618v1: the braid word, the range \(n\ge1\), genus \(n+11\), braid index \(4\), hyperbolicity, asymmetry, L-space property, and fixed hyperbolic parent used for the \((-1/n)\)-fillings.

The crossing count is exact arithmetic on the displayed word:
\[
12+13+2n=2n+25.
\]
The lower bound is reconstructed from the canonical Seifert surface and Yamada's theorem:
\[
c(K)\ge2g(K)+b(K)-1.
\]
For this family the right-hand side is \(2n+25\), so the published diagram attains the lower bound for every parameter.

The volume step uses only the theorem that a nontrivial hyperbolic Dehn filling strictly decreases volume. Thus every complement has volume less than the same parent volume. Since the exact crossing number is \(2n+25\), positivity and the uniform upper bound squeeze the volume density to \(0\).

No finite computation is used to infer an infinite statement. No exact hyperbolic volume is asserted. The originality comparison inspected the primary source and searched equivalent exact-crossing and volume-density formulations; the main residual risk is an unindexed short note.
