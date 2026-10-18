---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-15.md",
      "INDEPENDENT_AUDIT_2026-10-15.json"
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

PASS: Every base vertex v must be selected: if unselected, any of its private leaves not chosen is undominated, while selecting a leaf without v makes that selected leaf isolated in the induced selected graph. Because v can partner with only one selected private leaf in any perfect matching, at most one leaf at v can be chosen. Thus selected supports have all roots, one pendant at each root outside U and none at U; the remaining selected induced roots U require a perfect matching. Conversely every such U and one leaf choice at each excluded root gives domination and a perfect matching. The bijection yields coefficients without overcounting the several perfect matchings an induced U may possess. If G has no even cycle, two distinct matchings cannot have equal vertex endpoint support: their symmetric difference would include an even alternating cycle. Consequently sum over U is a positive weighted matching generating function, and Heilmann--Lieb real-rootedness after z=-1/x^2 places all nonzero x zeros on the imaginary axis. Boundary: isolated base vertices work by a leaf partner; the C4 matching count differs from support count and invalidates a naive unconditional matching replacement. Independently enumerated paired dominating subsets of K2 with (r1,r2)=(2,3): coefficients D=x^2+6x^4, agreeing with the theorem.

## originality

PASS

PASS (qualified): The 1998 Haynes--Slater paper introduces paired domination and establishes elementary scalar minima. Ohsugi--Tsuchiya and Davis--Kohl give the perfectly-matchable-set polynomial, and Davis--Kohl Lemma 3.2 already proves that it agrees with the matching polynomial if and only if G has no even cycle; those inputs are explicitly prior. No inspected source states the heterogeneous private-leaf paired-domination support bijection, its full coefficient transform or corresponding zero result; early paired-domination-polynomial conference publication accessible only as its single-page abstract leaves a real coverage risk. The new statement is not reducible to renaming the perfectly-matchable polynomial because it interprets actual selected sets in a decorated graph and tracks independently variable pendant multiplicities.

## value

PASS

PASS: The natural paired-domination enumerator is computed for arbitrarily large, irregular heterogeneous pendant-corona graphs without solving the perfect-matching constraint anew in each decorated graph. The structural bijection and sharp root geometry for all base graphs without even cycles are motivated, nontrivial exact graph invariants; the familiar matched-support and Heilmann--Lieb results are credited as inputs rather than sold as new.

The dated certificate retains the supplied scientific assessment, sources and limitations.
