# Independent Audit — 2026/09/20/prime-power-pseudoperfect-local-rigidity--e2b81fad1a6a

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `f2614139fa8e44cea912a55f73f530e27340a09f`
- Disposition: **PASSED**

## Correctness

**PASS** — Both the local criterion and the three-support classification are correct. Multiplying H(n) by n and reducing modulo P_i=p_i^{a_i} leaves exactly 1+m_i(1+p_i+...+p_i^{a_i-1}); multiplication by p_i-1 gives the equivalent congruence m_i≡p_i-1 mod P_i, and CRT makes these local congruences equivalent to integrality of H(n). For at most four prime supports, the displayed geometric-series bounds are all strictly below 2, so a positive integral H(n) must equal 1. In the three-support slice, the parity/size bound forces p=2. Rewriting the reciprocal identity with A=2^a, R=r^c and d=q-A gives d-1=(Aq-d(r-1))V. The d=1 branch forces q=A+1 and r=A^2+A+1, and reduction modulo 3 leaves only A=2, hence (2,3,7). If d>1, positivity yields V<=d-1, forcing c=1; then d(r-A)=A^2+1 and a modulo-3 argument makes one of q,r a composite multiple of 3. The converse family 6*7^c satisfies H=1 directly. Independent exact-rational enumeration through 20,000 found no mismatch between the local criterion and H(n)=1 for omega(n)<=4.

## Originality

**PASS** — Machacek introduced prime-power pseudoperfect numbers and established sufficient prime-factorization constructions, including the closure mechanism generating 6*7^c. The squarefree specialization of the local congruence is classical weak-primary-pseudoperfect/Sondow territory. The located literature does not state the prime-power modulus criterion for arbitrary exponents or the converse uniqueness of 6*7^c in the three-support slice with simple middle prime. The algebra is elementary, so equivalent formulations under generalized Sondow terminology remain a real but bounded originality risk.

## Scientific value

**PASS** — The local criterion converts a global Egyptian-fraction condition into independent prime-power congruences, and the three-support theorem turns a known infinite construction into an exact rigidity statement on a natural slice. The result is useful structural classification despite not covering five or more supports or the case of a higher middle-prime exponent.

## Sources

- **Egyptian Fractions and Prime Power Divisors** — John Machacek. https://cs.uwaterloo.ca/journals/JIS/VOL21/Machacek/mach4.html — Introduces prime power pseudoperfect numbers and gives sufficient factorization constructions.
- **On μ-Sondow Numbers** — José M. Grau; Antonio M. Oller-Marcén; Daniel Sadornil. https://arxiv.org/abs/2111.14211 — Related generalized Sondow congruence literature; the squarefree specialization is acknowledged prior context.
- **Port Fillings for Primary Pseudoperfect Numbers** — H. Wang. https://arxiv.org/abs/2605.21518 — Recent squarefree primary-pseudoperfect structural work, distinct from the prime-power local criterion.

## Limitations

- For more than four prime supports, the congruences characterize integrality of H(n), not by themselves H(n)=1.
- The three-support classification assumes the middle prime has exponent one.
- Equivalent formulations in older generalized Sondow or Egyptian-fraction literature remain a residual originality risk.

## Independent checks

```json
{
  "local_crt_proof_reconstructed": true,
  "omega_le_4_bound_checked": true,
  "three_support_diophantine_reduction_checked": true,
  "independent_exact_enumeration_limit": 20000,
  "criterion_mismatches": 0,
  "family_6_times_7_power_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned record tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Open-access and preprint sources were checked first; no decisive comparison required institutional retrieval in this audit.
