# Independent Audit — 2026/09/21/odd-divisor-power-mean-mod8-obstruction--3e49acbf49a0

- Audit date: 2026-09-30 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `6d95308a7632f86b4ad0f229e0f4361dcffa15f5`
- Disposition: **PASSED**

## Correctness

**PASS** — The local 2-adic lemma is valid. Expanding F_N(1+8h) gives the k=1 term 4h(N-1), while for k>=2 the factor 8^k/(k+1) has 2-adic valuation at least 3, so F_N is an odd 2-adic unit with the claimed residue. For r divisible by 4, every odd p satisfies p^r=1 mod 16, forcing all local factors to 1 mod 8. For r=2 mod 4, p^r=p^2 mod 16 and only odd exponents of primes p=±3 mod 8 contribute a factor 5; their parity is exactly the supplementary Jacobi symbol (2/n). Thus the displayed formula and perfect-even-power obstruction follow. An independent bounded computation over every odd n<=5000 and r in {2,4,6,8} found zero residue mismatches.

## Originality

**PASS** — OEIS A140480 records T. D. Noe's 2008 empirical observation that displayed RMS numbers appeared congruent to ±1 mod 8, and separates the known even RMS cases; A003601 records the broader sigma_r-number terminology. Oller-Marcén's paper concerns the arithmetic mean of divisors (r=1), not this even-r 2-adic congruence. Targeted searches for an RMS mod-8 proof, sigma_2/tau congruences, and the general even-r formula did not locate a published theorem. The main residual priority risk is informal sequence discussion, which is explicitly acknowledged.

## Scientific value

**PASS** — The theorem supplies a short proof of a longstanding computational RMS observation and strengthens it to an exact mod-8 formula for every odd integer and every positive even power r. It also applies to any even perfect-power value of the divisor-power mean, making the obstruction broader than the original RMS setting.

## Sources

- **OEIS A140480: RMS numbers** — OEIS Foundation contributors. https://oeis.org/A140480 — Records the empirical ±1 mod 8 observation for RMS numbers and points to the separate even sequence.
- **OEIS A224988: Even RMS numbers** — OEIS Foundation contributors. https://oeis.org/A224988 — Documents that oddness is essential to the congruence theorem.
- **On arithmetic numbers** — A. M. Oller-Marcén. https://arxiv.org/abs/1206.1823 — Adjacent divisor-mean literature for r=1; does not state the audited even-r mod-8 result.

## Limitations

- The congruence theorem is restricted to odd n; even RMS numbers have different 2-adic behavior.
- When r is divisible by 4 the residue is always 1 mod 8, so the argument gives no congruence restriction on n.
- Informal or poorly indexed sequence discussions remain a residual originality risk.

## Independent checks

```json
{
  "local_2adic_expansion_checked": true,
  "jacobi_symbol_reduction_checked": true,
  "perfect_even_power_corollary_checked": true,
  "independent_enumeration_odd_n_max": 5000,
  "independent_enumeration_r_values": [
    2,
    4,
    6,
    8
  ],
  "independent_enumeration_mismatches": 0,
  "source_tree_unchanged": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned record tree was unchanged between the inventory snapshot and the checked commit. GitHub was used only as read-only evidence; no repository mutation or separate dispatcher report was performed. Open-access and preprint sources were checked first, with authorized institutional retrieval used only where a directly relevant full text remained unavailable.
