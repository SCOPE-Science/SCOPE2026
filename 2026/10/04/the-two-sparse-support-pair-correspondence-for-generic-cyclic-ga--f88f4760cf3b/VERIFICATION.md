---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-10-06.md",
      "INDEPENDENT_AUDIT_2026-10-06.json"
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

For \(f=a\delta_0+b\delta_s\), each time slice is a two-term character polynomial. The character \(\xi\mapsto\omega^{-s\xi}\) has image size \(N/d\) and fibers of size \(d\), so a slice has either zero or exactly \(d\) zeros. Excluding the finite collection of algebraic equalities between the root cosets \(-\overline{g(j+s)}/\overline{g(j)}\,\mu_{N/d}\), together with coordinate hyperplanes, gives a nonempty Zariski-open set on which a coefficient ratio can hit at most one time slice. Both zero counts are attainable. The ordinary two-point Fourier polynomial has the identical \(d\)-zero alternative, proving the shifted support spectra. As \(s\) varies, \(d\) runs through the proper divisors of \(N\), and the largest is \(N/p\). The universal upper bound on \(\phi\) follows from a singleton when the window has a zero, or from forcing one \(N/p\)-zero slice when it has full support. I independently checked the distinct-ratio and character-fiber arithmetic for every \(2\le N\le120\) and all nonzero differences.

## originality

PASS

Krahmer--Pfander--Rashkov explicitly pose as Question 4.13 whether, for every cyclic group and almost every window, the Fourier and STFT support-pair sets agree after the \(N^2-N\) shift. Their Table 1 reports only numerical data for \(\mathbb Z_6\), including the value 33 at support at most two. Their general theorem gives lower bounds, not the exact composite-order two-sparse stratum. Malikiosis proves generic full-spark Gabor frames and later discusses Fourier/STFT uncertainty similarities, but the checked accessible statements do not determine the reverse support-pair inclusion for composite cyclic order. Resultary search returned the assigned exact two-sparse theorem and related but different Gabor support results.

## value

PASS

This resolves a complete nontrivial stratum of an explicit cyclic Gabor uncertainty question, for every composite and prime order, and gives the exact generic support-at-most-two optimum. The gcd formula also explains earlier numerical data and is a natural reusable sparse-signal invariant.

The dated certificate retains the supplied scientific assessment, sources and limitations.
