---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

Multiplication by 3I+2sT_n recovers 4R_n(s)-I from the claimed transfer. The stated Green function solves the second-order resolvent recurrence, with zero values at 0 and n+1 and the unit jump at the source; both resolvents are strictly positive. For t=2s/3 the ratio for i<=j is (2/3)h_i h_{n+1-j}/(h_1 h_{n+1}). The function log(h_x) is strictly decreasing and concave: y*coth(xy) increases in y and y/sinh(xy) decreases. Replacing i by j reduces the product, and the concave sum at complementary indices j,n+1-j is minimized at j=1 or n. The endpoint ratio must be >=3/4, yielding the stated 9/8 inequality, including the singleton n=1 case. For fixed i,j the finite Green functions converge to the decaying half-line resolvent satisfying the same recurrence and left boundary; the endpoint dominance therefore passes to every half-line entry. Writing a=1-q_s and b=1-q_t gives endpoint values a^2 and b^2; zero transfer there forces b=2a/sqrt(3), and t=2s/3 then gives the unique admissible a=1/(6sqrt(3)-8). The sign starts positive and becomes negative since a^2/b^2 tends to 2/3, giving s<=180-102sqrt(3). For the two-point witness direct 2-by-2 inversion gives R_11(s)=24/119, R_12(s)=10/119, R_11(t)=13/48 and R_12(t)=5/48, reproducing (-11,45)/1904 in the first row. The endpoint numerator is a positive multiple of -4s^3+5s^2+8s+3, equal to -33/4 at the witness. The frozen script and log were read; the witness was recomputed without running that script. No claim about later BDF2 iterates is inferred.

## originality

PASS

Credit the established BDF2 recurrence and BE startup and their elementary resolvent rearrangement. The supported distinct claim is sharp endpoint dominance for the first BE-started BDF2 value on the centered Dirichlet path, and the resulting exact half-line frontier. The strongest inspected general result is sufficient and addresses a different iterate quantifier; the nearest lattice and indexed BDF2 findings use different kernels, starters, or observables.

## value

PASS

For a standard spatial heat model and multistep starter, this replaces a matrix-wide entrywise sign test by a sharp scalar boundary test valid for every grid length. It resolves a boundary-limited positivity effect not captured by stability or by the positive starter alone, gives a usable half-line step cutoff, and supplies a small exact sign-loss witness. The value is the sharp first-value theorem, not a claim of all-iterate monotonicity.

The dated certificate retains the supplied scientific assessment, sources and limitations.
