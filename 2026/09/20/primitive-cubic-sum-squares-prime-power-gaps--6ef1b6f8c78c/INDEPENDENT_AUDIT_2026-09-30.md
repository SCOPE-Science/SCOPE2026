# Independent Audit — 2026/09/20/primitive-cubic-sum-squares-prime-power-gaps--6ef1b6f8c78c

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `fed0e369df42f40e6ef0832ed0207988261d519d`
- Disposition: **PASSED**

## Correctness

**PASS** — The Gaussian-integer parametrization and both sign cases lead to the claimed classification. In the A<0 regime, Delta=(a-b)(a^2+4ab+b^2) and the two factors have gcd gcd(a-b,3). For a prime power with prime ell!=3, coprimality forces a-b=1; for ell=3, the second factor is either 1 mod 3 or has exactly one factor of 3 but is >3, excluding this regime. In the A>0 regime, Delta=(a+b)|a^2-4ab+b^2| and the factor gcd is again at most 3. For ell!=3, the second factor must have absolute value one; its congruence 1 mod 4 forces +1, equivalent to s^2-3d^2=-2. The Pell converse gives coprime opposite-parity a,b. For ell=3, the factor has 3-adic valuation one and congruence 1 mod 4, so it equals -3, reducing to d^2+2=3^{2r-1}; the classical Nagell-Sury theorem leaves exactly r=1,d=1 and r=2,d=5, giving gaps 9 and 27. Independent enumeration of all normalized coprime opposite-parity pairs with a<=250 found 111 prime-power gaps and zero classification mismatches.

## Originality

**PASS** — The Gaussian-cube parametrization is classical generalized-Fermat material, and the x^2+2=y^n theorem used for the exceptional 3-powers is classical. The located literature and targeted searches did not contain the exact prime-power classification for the coordinate gap |x-y|, its star-number/Pell dichotomy, or the assertion that 9 and 27 are the only powers of 3. The result is an elementary refinement of a classical parametrization, so older problem-book, thesis, or differently indexed coverage remains the main residual originality risk.

## Scientific value

**PASS** — The theorem gives a complete and explicit classification of a natural arithmetic invariant across all primitive positive solutions of x^2+y^2=z^3, separating two infinite mechanisms and a finite exceptional branch. It also reduces future prime-power questions to star-number and negative-Pell sequences. The scope is specialized but mathematically clean and complete.

## Sources

- **The Diophantine equation Ax^p+By^q=Cz^r** — Frits Beukers. https://doi.org/10.1215/S0012-7094-98-09105-0 — Classical generalized-Fermat/Gaussian parametrization background; the parametrization itself is not claimed new.
- **On the Diophantine equation x^2+2=y^n** — B. Sury. https://doi.org/10.1007/s000130050454 — Classical theorem yielding the unique n>1 solution (up to sign) needed in the exceptional 3-power branch.
- **A003154: Centered 12-gonal numbers** — OEIS Foundation. https://oeis.org/A003154 — Identifies the star/centered-dodecagonal sequence arising in the first branch.

## Limitations

- The theorem does not classify which star-number or Pell-sequence terms are prime powers.
- Only primitive positive solutions and the exponent 3 are covered.
- Because the proof is an elementary refinement of a classical parametrization, unindexed older coverage is a residual priority risk.

## Independent checks

```json
{
  "gaussian_parametrization_logic_checked": true,
  "factor_gcd_arguments_checked": true,
  "pell_converse_checked": true,
  "three_power_reduction_checked": true,
  "independent_parameter_enumeration_max_a": 250,
  "prime_power_hits": 111,
  "classification_mismatches": 0,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned record tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Open-access and preprint sources were checked first; no decisive comparison required institutional retrieval in this audit.
