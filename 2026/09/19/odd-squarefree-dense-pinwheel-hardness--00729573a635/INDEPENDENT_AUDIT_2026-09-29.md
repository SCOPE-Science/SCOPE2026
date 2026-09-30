# Independent Audit — 2026/09/19/odd-squarefree-dense-pinwheel-hardness--00729573a635

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `42ac50c082e78ed98a8fe6034fa9c5a2330557e2`
- Disposition: **PASSED**

## Correctness

**PASS** — The restriction-preserving reduction is sound. Prime-padding a sparse tripartite triangle-partition instance to a common odd prime part size p>3 by isolated forced triangles preserves feasibility in both directions and preserves the source degree/triangle-incidence promises. Applying the published marker-prime reduction then gives witness periods p m_v and cell periods 3p m_v, where m_v is a product of one to three distinct marker primes r_T>p. Thus every period is odd and squarefree with at most four or five prime factors. Cell multiplicities are positive because m_v>p>3. The LCM contains exactly 3, p, and every marker; the GCD is exactly p because 3 is absent from witnesses and no triangle marker occurs at all vertices. Each vertex block has density 1/(3p), and there are 3p vertices. Under the source's bounded-incidence promise the number and size of marker primes, each m_v, the task multiplicities and the largest period remain polynomial, so the explicit unary reduction is polynomial. NP membership is inherited from the source residue-class certificate.

## Originality

**PASS** — Kobayashi-Lin-Swernofsky's September 2026 theorem proves unary/strong NP-completeness for dense pinwheel packing and exposes the sparse-triangle marker-prime construction, but its public statement does not impose oddness, squarefreeness, bounded prime support, squarefree global LCM, or prime global GCD. The audited prime-padding observation simultaneously enforces all of those arithmetic restrictions without altering the scheduling reduction. Classical squarefree covering-system results concern structural existence, especially with distinct moduli, and do not supply this computational hardness statement; repeated equal periods are explicitly allowed here. Targeted searches found no earlier matching restricted-hardness theorem.

## Scientific value

**PASS** — This refinement locates the hardness inside a highly rigid Chinese-remainder regime and demonstrates that evenness, repeated prime powers, and large prime support are not responsible for the source construction's complexity. It is a concise arithmetic strengthening rather than a new NP-hardness mechanism, but the simultaneous restrictions are meaningful for exact-covering and pinwheel structure.

## Sources

- Dense Pinwheel Packing Is Strongly NP-Complete (Yusuke Kobayashi; Bingkai Lin; Joseph Swernofsky): https://arxiv.org/abs/2609.20075 — Primary 2026 strong-hardness source; gives the sparse tripartite triangle-partition reduction with polynomial unary periods.
- NP-Hardness and a PTAS for the Pinwheel Problem (Robert Kleinberg; Abhishek Mishra): https://arxiv.org/abs/2604.13974 — Earlier pinwheel NP-hardness with exponentially large numerical periods.
- The Erdős-Selfridge problem with square-free moduli (Paul Balister; Béla Bollobás; Robert Morris; Julian Sahasrabudhe; Marius Tiba): https://arxiv.org/abs/1901.11465 — Classical structural squarefree covering-system result; distinct-modulus setting differs from explicit-list pinwheel instances.

## Limitations

- Equal periods may occur as distinct tasks; the theorem does not imply a hardness result for distinct-modulus covering systems.
- The bound of five prime factors per period is not proved optimal.
- The novelty is an arithmetic restriction of a very recent reduction, so near-simultaneous observation remains a material priority risk.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "prime_padding_equivalence_checked": true,
  "lcm_gcd_density_and_prime_support_checked": true,
  "unary_polynomial_size_argument_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Preprints and lawful open-access sources were checked first; no decisive comparison remained unavailable, so Oxford Download was not required.
