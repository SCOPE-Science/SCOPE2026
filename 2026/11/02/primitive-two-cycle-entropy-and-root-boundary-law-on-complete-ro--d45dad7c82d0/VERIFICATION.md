---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-04.md",
      "INDEPENDENT_AUDIT_2026-11-04.json"
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

For connected loopless graph, two-step periodicity makes two-step firing counts a harmonic vertex function; connectedness forces the constant 1 in a primitive 2-cycle (constants 0 or 2 are fixed states). Given phase bipartition, opposite-phase degree c(v)>=1 and admissible nonnegative initial heights form a length-c(v) interval, so each unlabelled temporal orbit corresponds bijectively to a spanning edge-cover H of the tree with weight product_v deg_H(v). The recursive weighted edge-cover DP with A0=0,B0=1 yields A_{j+1}=dB_j(A_j+B_j)^(d-1), B_{j+1}=(A_j+B_j)^(d-1)(A_j+(d+1)B_j); root k histogram is k*C(d,k)*B^(k)*A^(d-k), giving the size-biased binomial exact law. Ratio recursion r_{j+1}=d/(d+1+r_j), contraction q=d/(d+1)^2, and summable logarithmic tail give rho_d and sharp fixed-d asymptotic. Independently counted edge covers on rooted (d,h)=(2,1),(2,2),(2,3),(3,2) reproducing N=2,30,9350,588 and root degrees. The unrestricted theorem follows algebraically, not from finite tests.

## originality

PASS

The Bitar–Goles 1992 bound that tree periods are at most 2 and Jiang 2010 Proposition 2.5 equal firing counts are acknowledged. The weighted spanning edge-cover count, complete d-ary recursion, root binomial law and height entropy are not stated by these period restriction theorems; the newer binary-tree root-chip problem concerns different initial data.

## value

PASS

Exact temporal-orbit counts and the root boundary statistics for a natural family of trees quantify how much period-two behavior is possible in a model where only a qualitative period bound was known. The entropy constant and asymptotic identify scalable structural information, not merely a small finite case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
