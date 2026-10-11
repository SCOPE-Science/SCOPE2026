---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-05.md",
      "INDEPENDENT_AUDIT_2026-10-05.json"
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

If two ordered hyperbola pairs have the same nonzero vector sum, then their first-coordinate sums agree and equality of inverse-coordinate sums forces the same product, so the unordered pair is determined; every nonzero pair-sum fiber therefore has size at most two. The zero fiber consists of all \(q-1\) ordered antipodal pairs. This gives the same exact weighted-energy identity as in the anisotropic case. Antipodal-pair optimization forces equal moduli within and across pairs and common phase of the products, yielding \(\mathcal Q\le3(q-2)S^2/(q-1)\) and hence the stated normalized constant. Independent brute-force reconstruction for \(q=3,5,7,11,13\) reproduced zero-fiber size \(q-1\), nonzero-fiber maximum two and energy \(3(q-1)(q-2)\); the actual verifier repeats these checks through prime 101 and certifies a nontrivial phase extremizer.

## originality

PASS

The same-dimensional Iosevich--Koh theorem supplies only a uniform \(L^2\to L^4\) estimate for nondegenerate quadratic curves, with a proof that bounds nonzero two-point sums but is deliberately nonsharp at the exceptional zero fiber and in equality. Hyperbola-specific prior work checked studies Fourier decay/additive behavior rather than the exact extension norm. The recent sharp finite-field extension papers located address other surfaces. No prior exact value or all-extremizer classification for this hyperbola was found.

## value

PASS

The multiplicative hyperbola is a canonical finite-field curve. Replacing the known uniform extension estimate by an exact norm and complete extremizer class is a natural sharp endpoint problem, with the split conic's \(q-1\) geometry producing a distinct constant from the anisotropic \(q+1\) case.

The dated certificate retains the supplied scientific assessment, sources and limitations.
