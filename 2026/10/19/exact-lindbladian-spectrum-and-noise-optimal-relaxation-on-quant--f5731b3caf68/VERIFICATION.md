---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The full complex matrix-unit equations have the stated permutation-trivial and standard blocks. To see that they exhaust the non-scalar action, the off-diagonal leaf row/column-sum map has image the pairs of vectors with equal total sum. On mean-zero coefficient vectors its 2×2 map is [[n−1,−1],[−1,n−1]], invertible for n≥3; the constant off-diagonal block supplies the common scalar sum. Its kernel is precisely the zero-diagonal leaf-only remainder of dimension n²−3n+1. In a standard block the sum of the two hub–leaf coordinates and difference of the off-diagonal coordinates form the quadratic sector; the complementary three variables give S_n. In the trivial block the trace is conserved and the symmetric hub–leaf variable decays at −γ, leaving the T_n sector. The factors, multiplicities, and simple zero follow. In the positive-u parametrization y=2u/(u²+1−2/n), γ is strictly increasing onto (0,∞) since y′≥−1/[4(1−2/n)]. This gives the unique root in the stated interval and the unique optimizer. After shifting by −s, S_n reduces to w times a strictly stable quadratic. For shifted T_n, a=2γ−3s>0, c_T=a ng², and b_T>ng², so Routh–Hurwitz gives strict separation; the other factors lie at real part −γ. The contrast is the diagonal coefficient in the standard three-variable block with initial value 1, giving the stated numerator, positive residue, and observed rate. The sentence at line 120 calling s itself an eigenvalue is a sign slip: it is −s, as the shifted proof and finding require. Independent direct matrix-unit generation gave exact polynomial agreement at (n,g,γ)=(3,−2,7),(4,1,2),(5,2,9) and exact rational leaf-resolvent agreement at z=1,3 in each case; these finite checks support, not replace, the proof.

## originality

PASS

The supported distinct contribution is the exhaustive all-n adjacency-star Liouvillian factorization and the strict comparison showing that its standard sector dominates all additional star sectors. An earlier-dated universal-hub indexed result, specialized to a complete graph and rescaled, already gives the same rational scalar transfer function, including its numerator and S_n denominator. This is stronger overlap than identifying the cubic alone. The scalar contrast law and optimum of its dominant rate are not independent novelty claims; the new content is that this mode is realized by a leaf contrast in the adjacency star and governs the entire star relaxation despite additional sectors. None of the inspected sources gives or forces this complete star-specific result.

## value

PASS

The all-order reduction resolves a growing nonnormal generator into fixed low-degree spectral factors and quantifies multiplicities and separation. For a canonical hub–leaf system it identifies a measurable contrast that sees the actual global relaxation exponent, rather than just a fitted decay or absorption rate. The full spectral comparison carries this value even though a rescaled scalar transfer was already known.

The dated certificate retains the supplied scientific assessment, sources and limitations.
