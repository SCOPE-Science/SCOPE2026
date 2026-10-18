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

For independent equal-rate Poisson components on jumps 1,...,k, h_{k,n}(t)=[z^n]exp(t sum_j z^j) has the exact Panjer derivative recurrence. Any global mode m satisfies m<=t*k(k+1)/2, so t<=2 reduces to 0<=m<=k(k+1). Reconstructed factorial-normalized integer polynomials and 109,943 triple difference gcds modulo prime 1000003; all had gcd 1 except (1,3,4) for k=4..8 with gcd t+6, and the exact characteristic-zero shared root there is -6. Leading coefficients are units modulo p, hence any positive-characteristic-zero common factor would reduce nontrivially: modular gcd exclusion is rigorous, not floating point. For t>2, Q uniform on jumps 1..k, total Poisson jump rate kt, Q#(j) proportional to j+1 strictly log-concave and (kt)*Q(1)^2>2Q(2); Hansen/JKM gives strict log concavity, preventing three maxima. Endpoints t=2 and mode zero included. The independent checker rebuilt polynomials/gcds from exact coefficient recurrence, with 35+286+1330+4495+12341+29260+62196=109943 triple tests.

## originality

PASS

Scientific best-of-knowledge assessment after independently reading the frozen RESULT.md and recreating relevant proof/calculation, checking Resultary and named primary source statements. The 2023 Mane primary paper explicitly poses three or more joint global modes as open and provides numerical evidence; Kwon--Philippou give limited small-order exact mode information and rate tables. The JKM/Hansen theorem covers the t>2 large-rate portion but cannot settle low t. The exact low-rate algebraic elimination through k=8 is not implied by those published mode statements or generic log concavity.

## value

PASS

The possibility of three tied global maxima is a specific open structural question in higher-order Poisson probability laws. Resolving the first seven nontrivial orders for every continuous rate (rather than sampling a table) is a motivated substantive finite-order boundary; the 109,943 exact algebraic exclusions are logically exhaustive after a proved support cut. The result does not answer k>=9 or classify all two-mode transitions.

The dated certificate retains the supplied scientific assessment, sources and limitations.
