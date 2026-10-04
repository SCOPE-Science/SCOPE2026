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

The primary source was inspected at the exact statements used:
\[
\deg\Delta_{S(p,q,\varepsilon)}=(p-1)(q-1)
\]
and
\[
|a_1|=q\gamma_{p-1}+1.
\]
Thus for \(D=\deg\Delta\) and \(m=|a_1|-1\), every spiral representation satisfies
\[
q-1\mid D,
\qquad
q\mid m,
\qquad
p=1+\frac{D}{q-1}.
\]
The knot parameter convention additionally requires \(\gcd(p,q)=1\).

If \(m\) is prime, \(q\ge2\) and \(q\mid m\) force \(q=m\), after which the degree formula forces \(p\). This proves the uniqueness statement without finite enumeration.

The bundled checker enumerates synthetic admissible triples over a finite range and confirms that every one survives the sieve, and that prime gaps yield singleton candidate sets. It also checks the source \(6_2\) example and the \(8_{21}\) obstruction. It reports:

`VERIFY_OK synthetic_cases=58999 source_6_2=[(5,2,1)] source_8_21=[] prime_gap_unique=true`

The finite check is only regression evidence. The universal theorem is the divisibility proof above.

No independent audit has been performed.
