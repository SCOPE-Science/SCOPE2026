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

The unrestricted argument is in `RESULT.md`.

The checker verifies the three symbolic branches used in the proof:

1. prime followed by semiprime reduces to
\[
(a-1)(b-1)=2;
\]
2. semiprime followed by prime reduces to
\[
(a-1)(b-1)=0;
\]
3. semiprime followed by semiprime, after setting \(t=c-a\), reduces to
\[
t(b-a-t)=1.
\]

The checker also computes the prime-factor sum \(S\) and total multiplicity \(\Omega\) for every integer through \(2{,}000{,}001\). It confirms that, among all Ruth–Aaron pairs beginning at \(n\le2{,}000{,}000\), the only pair with both multiplicities at most \(2\) is \((5,6)\). It also checks the sharp witness \((8,9)\).

The finite sweep is corroborative only. The theorem is unrestricted because the proof exhausts every prime and semiprime factorization pattern algebraically.
