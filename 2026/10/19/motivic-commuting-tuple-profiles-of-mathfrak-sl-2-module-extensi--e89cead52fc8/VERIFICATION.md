---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of motivic commuting-tuple identities

Run `python3 verify.py` with Python 3 and the standard library, in the same directory as this file. No external data, downloaded publications, or optional dependencies are needed.

The script constructs the standard \(\mathfrak{sl}_2\) action on each \(\operatorname{Sym}^m\) by its raising, lowering, and weight matrices. It enumerates all projected ordered tuples in selected prime fields; imposes the actual commutator equations on the radical coordinates as a finite linear system; computes ranks by row reduction; and counts each solution fiber by its nullity. This calculation does not assume the final projective-strata formula. It also tests every one-element action kernel and the equality of the two proposed collision profiles for several characteristics and arities.

The direct enumerations cover \(\mathbb F_3\) with module types \(\operatorname{Sym}^1\) and \(\operatorname{Sym}^2\) at tuple lengths two and three; and \(\mathbb F_5\) with \(\operatorname{Sym}^3\), \(\operatorname{Sym}^1\oplus\operatorname{Sym}^4\), \(\operatorname{Sym}^2\oplus\operatorname{Sym}^3\), and \(\operatorname{Sym}^1\oplus\operatorname{Sym}^2\), at tuple length two. The ten-dimensional pair yields \(6,619,140,625\) ordered commuting pairs for each algebra over \(\mathbb F_5\). The run must end with `VERIFY_OK`.

Limits: The calculation is exhaustive only for its stated finite inputs. The arbitrary-field theorem, motive identity, perfection and nonisomorphism are established in the accompanying proof, not inferred from those inputs. No independent audit is claimed.
