---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-17.md",
      "INDEPENDENT_AUDIT_2026-10-17.json"
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

For unweighted adjacency on the Cartesian power H(d,q)=K_q^{square d}, exp(itA) factorizes into d coordinate unitaries. The one-coordinate probability matrix has constant-eigenspace eigenvalue 1 and perpendicular-eigenspace eigenvalue a(t)=(q-2+2cos(qt))/q. Tensor diagonalization gives a(t)^j with multiplicity binom(d,j)(q-1)^j. Its common-period average equals q^{-j}[z^0](q-2+z+z^{-1})^j, and expansion yields the stated nonnegative sum. q>=3 has positive constant-term contribution (q-2)^j; q=2 has zero exactly at odd j and positive binom(2a,a)/4^a at j=2a. The binomial-multiplicity sum gives rank q^d or 2^(d-1), including d=1. Independently counted equal-weight character pairs for 36 (q,d,j) cases with 2<=q<=5 and 1<=d<=3; this checks normalization but the tensor argument proves all dimensions. The q-alphabet need not be a field.

## originality

PASS

The general average-mixing Schur-projector formula, Coutinho–Guo 2024 association-scheme P/Q instantaneous spectral recipe, and odd-order abelian-Cayley full rank are prior work, as are Hamming graph adjacency eigenvalues. The presented exact *average-mixing eigenspectrum* for arbitrary d,q and the even nonbinary rank result require additional common-clock tensor/character analysis; the inspected primary statements do not supply these as a theorem. The odd-q full-rank corollary is explicitly NOT newly claimed in isolation. Targeted general association-scheme and Hamming-average searches did not identify a dominating formula. An implicit association-scheme corollary or underindexed specialized calculation remains a real originality risk.

## value

PASS

A complete spectrum and sharp singular-to-positive-definite transition for an infinite, natural distance-regular family are meaningful: all eigenvalues and multiplicities quantify rank, nullspaces and spectral conditioning across arbitrary diameter. This resolves the Hamming case of the published primitive-distance-regular full-rank question where H(d,q) is primitive; it is not an isolated low-dimensional table or routine restatement of adjacency eigenvalues.

The dated certificate retains the supplied scientific assessment, sources and limitations.
