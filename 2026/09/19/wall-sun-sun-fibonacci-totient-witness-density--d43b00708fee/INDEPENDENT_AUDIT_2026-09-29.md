# Independent Audit — 2026/09/19/wall-sun-sun-fibonacci-totient-witness-density--d43b00708fee

- Audit date: 2026-09-29 (UTC) (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `13413b0e28b4fec51e34242e7f1ae25ab3a33cb7`
- Disposition: **PASSED**

## Correctness

**PASS** — The density formula follows rigorously from the standard Fibonacci lifting law. For odd q!=5, z(q)|pi(q) and pi(q)|q^2-1, hence q does not divide A=pi(q)/z(q). If z(q) does not divide the fixed residue r, no index in the progression is divisible by z(q). If z(q)|r, writing m_t/z=u+tA gives v_q(F_m_t)=e_q+v_q(u+tA); for s>=0 the congruence q^s|(u+tA) selects exactly one class of t mod q^s. Thus the natural density is q^{-max(a-e_q,0)}. The square-divisibility and Wall-Sun-Sun dichotomy are immediate. The totient consequence is also correct: whenever q|phi(F_m) but q^2 does not divide F_m, some other prime divisor p of F_m must satisfy p=1 mod q. Hence the external-witness density lower bounds are the complements of the exact q^2-witness densities. The omitted t=0 term when r=0 has zero density.

## Originality

**PASS** — Goel's 2026 paper defines S(q) and its Lemma 4.3 explicitly argues that an arbitrary q under consideration is not Wall-Sun-Sun because no such primes are known, then invokes z(q^2)=q z(q). That inference is not unconditional. The audited record isolates the missing branch and gives an exact q^a index-density formula inside every Pisano-period class. The lifting law itself is classical, and Bragman-Rowland study a different density problem (values attained modulo growing prime powers), so novelty is appropriately limited to this source-specific density theorem and correction. Targeted searches found no prior statement of this exact S(q) result.

## Scientific value

**PASS** — The result repairs a genuine logical gap in a current Fibonacci-totient argument without pretending that a Wall-Sun-Sun prime exists, and strengthens the valid non-Wall-Sun-Sun branch from infinitude to an explicit positive-density witness statement. It also cleanly identifies what any proof of Goel's conjectural converse would still need to establish in the hypothetical Wall-Sun-Sun case.

## Sources

- **Sophie Germain Primes and the Totient of Fibonacci Numbers** — Aradhya Goel. https://arxiv.org/abs/2604.17847 — Lemma 4.3 lines 190-199 were checked in the open arXiv full text; its proof assumes the arbitrary q is not Wall-Sun-Sun because no examples are known.
- **The p-Adic Valuation of Lucas Sequences** — Carlo Sanna. https://doi.org/10.1080/00150517.2016.12427821 — Classical p-adic lifting background for Lucas/Fibonacci sequences.
- **Limiting density of the Fibonacci sequence modulo powers of a prime** — Nathan Bragman; Eric Rowland. https://doi.org/10.1007/s40993-025-00667-1 — Related but different density problem: density of residue values attained as the modulus power grows, not index density within a fixed Pisano class.

## Limitations

- The prime-power lifting ingredient is classical; originality is only the exact fixed-class density application and correction.
- No existence of a Wall-Sun-Sun prime is asserted and the record does not disprove Goel's Conjecture 4.4.
- The statement excludes q=5 to align with the source lemma; analogous special-prime formulations are not audited here.
- Very recent unindexed commentary on the April 2026 preprint remains a residual priority risk.

## Independent checks

```json
{
  "goel_open_full_text_checked": true,
  "lemma_4_3_flawed_wall_sun_sun_inference_verified": true,
  "lifting_density_proof_reconstructed": true,
  "boundary_cases_r_zero_and_e_q_ge_2_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Open-access/preprint sources were checked before institutional retrieval. Any inaccessible comparison is explicitly identified above rather than claimed read.
