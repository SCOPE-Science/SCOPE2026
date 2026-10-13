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

The exact Smith implication used in the proof is
\[
s_B(t)\equiv t\pmod{B-1}.
\]
For \(n=pq\) with prime factors counted with multiplicity, this gives
\[
(p-1)(q-1)\equiv1\pmod{B-1}.
\]
The odd-base classification then follows entirely from reduction modulo \(2\) and the direct digit-sum check for \(4\).

For even bases, the checker independently verifies the residue involution
\[
T(r)=1+(r-1)^{-1}
\]
and the product formula
\[
|A_m|=\prod_{\ell^a\parallel m}\ell^{a-1}(\ell-2)
\]
for a range of moduli, and checks every finite Smith semiprime against the predicted residue condition.

The asymptotic is not inferred from the finite scan. Its proof uses fixed-modulus prime-number theory in arithmetic progressions, Mertens estimates for reciprocal primes in progressions, Brun--Titchmarsh tail control, and Landau's semiprime asymptotic. The computation only checks finite shadows of the exact algebraic reductions.
