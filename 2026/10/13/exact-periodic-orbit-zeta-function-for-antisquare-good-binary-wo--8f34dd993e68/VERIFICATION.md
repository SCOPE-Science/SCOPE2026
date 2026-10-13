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
# Verification

Run `python3 verify.py` in this package; only the Python 3 standard library is needed.

The program constructs the length-four admissible state graph for \(G=\{010,101,11111,01110\}\) and checks every labeled edge against the explicit table in `RESULT.md`. Integer trace-based Newton identities compute
\[
\det(I-zA)=1-z-z^4-z^6.
\]
Independently it builds the length-five de Bruijn graph forbidding \(F\); this has twenty states and determinant
\[
\det(I-zB)=(1-z-z^4-z^6)^2.
\]
The exact traces satisfy \(\operatorname{tr}(B^n)=2\operatorname{tr}(A^n)\) through \(n=40\).

Independent exhaustive circular-word enumeration confirms the exact traces for all lengths \(1\) through \(16\). A direct check against actual antisquare factors for orders \(2\) through \(2n+6\) is performed for each period \(n\le10\). The explicit all-period witness is independently checked for \(4\le n\le300\).

These bounds describe regression and independent finite calculations; the infinite result is proved by the symbolic parity argument, published forbidden-language equivalence, exact finite-matrix identities, and formal determinant identity in `RESULT.md`. Independent external audit has not been performed.
