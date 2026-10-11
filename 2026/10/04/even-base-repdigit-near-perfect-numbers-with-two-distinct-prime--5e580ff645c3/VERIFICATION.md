---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-04.md",
      "INDEPENDENT_AUDIT_2026-10-04.json"
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

The proof correctly starts from the published exhaustive A/B/C-plus-40 classification of near-perfect numbers with two prime factors. Because an even base makes the repunit factor odd, Type A forces that factor to be either the Mersenne prime or its square; the single-prime option violates the digit bound, while the square option and Ljunggren's repunit-square theorem exclude every length above two. Type B makes the digit too large. Type C forces the odd repunit factor to equal its odd prime; if length were at least three, \(U_n>g^2>a^2=2^{2t-2}\ge2^t>q\), contradiction. The isolated 40 is excluded directly. Substitution proves both converse families, and the package verifier correctly supplies only finite regression checks.

## originality

PASS

Hasanalizade's primary full text studies the same repdigit question but Theorem 1.3 is explicitly restricted to bases \(2\le g\le10\). It also records Ren--Chen's exhaustive two-prime near-perfect classification. The audited parity argument removes the base bound for the infinite natural subclass of all even bases and gives exact symbolic families; fresh Resultary searches found no prior all-even-base theorem.

## value

PASS

Repdigit near-perfect numbers are an established research object, and extending a finite-base theorem to every even base while obtaining an exhaustive parametric classification is a natural structural advance. The result explains exactly why two of the four general two-prime types cannot occur and why all surviving repdigits have two digits.

The dated certificate retains the supplied scientific assessment, sources and limitations.
