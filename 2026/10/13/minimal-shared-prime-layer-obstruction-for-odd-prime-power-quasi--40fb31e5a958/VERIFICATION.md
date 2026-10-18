---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-16.md",
      "INDEPENDENT_AUDIT_2026-10-16.json"
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

For b>=3 odd and q odd, if sigma(N)/N=(sigma(q^b)+1)/q^b with q^b|N, an even host is excluded by the 3/2 (q>=5) or 2 (q=3 with 6|N) abundancy bound. Then sigma(N) is odd, since sigma(q^b) is even; an odd host with odd divisor sum has only even prime exponents, so N is a square. If N=q^(b+1)p^(2a), let S=sigma(q^b), H=sigma(q^(b+1))=S+q^(b+1). Divisibility monotonicity gives p>=S. The exact ratio implies H*sigma(p^(2a-1))=(q-1)p^(2a). As p>=S>q and sigma(p^(2a-1))==1 mod p, p^(2a)|H. But S^2>H, a contradiction. The next possible square-host shared exponent is >=b+3. Independently checked rational identities and size inequalities on many q,b, but this is a symbolic all-prime proof.

## originality

PASS

Holdener and Holdener’s primary article establishes host oddness, the lower bound for other prime divisors and the square-host observation for odd b, but does not rule out the first q-adic shared-prime layer with two-prime host. A published Resultary theorem eliminates two-prime hosts for q as divisor (b=1), whose stronger prime-case result does not imply b odd >=3. The new divisibility-and-size contradiction uses H=sigma(q^(b+1)) at exactly the minimal layer. Best of knowledge; historical abundancy literature is not exhaustively indexed.

## value

PASS

The first shared-prime valuation layer is the natural smallest branch left by parity in a published open quasi-friendly-divisor existence problem. Uniformly ruling it out for two-prime hosts provides a meaningful structural obstruction with exact sharp scope, not merely failure to find a small example. It guides later attempts by requiring either >=3 prime supports or q-adic depth at least b+3.

The dated certificate retains the supplied scientific assessment, sources and limitations.
