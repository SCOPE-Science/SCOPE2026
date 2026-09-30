# Independent Audit — 2026/09/19/odd-quotient-characteristic-two-grl-hulls--089106bda32c

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `7b48cb0793b60579da091a5e1b54615128a7b15b`
- Disposition: **PASSED**

## Correctness

**PASS** — The finite-field and polynomial arguments are correct. Writing e=db and ell=da with gcd(a,b)=1 and b odd, a common divisor of 2^ell+1 and 2^e-1 would force the same power of 2^d to be both 1 and -1 modulo that odd divisor; hence gcd(2^ell+1,2^e-1)=1 and x↦x^(2^ell+1) is bijective on F_q^*. This permits roots w_i with w_i^(r+1)=u_i for every evaluation skeleton. Scaling exactly z=k-s-h multipliers by beta makes the dual equations unscaled at n-z points. The dimension bound implies r(k-1)≤n-k-1, so g-f^r has more distinct zeros than its possible degree and therefore g=f^r. The GRL extension equation then forces the top s coefficients of f to vanish, while the z scaled positions force z prescribed roots. The resulting polynomial space has dimension exactly h, and the converse construction satisfies every dual equation. Diagonal rescaling of the first n coordinates is a monomial Hamming isometry, so the classical weight distribution and distances are indeed unaffected by hull tuning.

## Originality

**PASS** — Wu-Liu-Chen-Zhou's 2026 GRL paper develops prescribed Galois hulls using normalized Lagrange coefficients and six structured evaluation families; its constructions retain additional arithmetic/evaluation restrictions. Wan-Zhu already treat the odd-quotient characteristic-two field regime for GRS/EGRS codes and obtain arbitrary hull dimensions there, so neither the power-map lemma nor arbitrary-hull MDS coding is new. The audited contribution is the specific GRL consequence: in the low-degree range, every distinct evaluation set and every nonsingular extension matrix A_s admit every hull dimension. Targeted searches did not locate this arbitrary-skeleton statement.

## Scientific value

**PASS** — The theorem removes the main normalized-Lagrange/subfield/evaluation-family constraints from a newly introduced GRL hull construction in a clean characteristic-two regime. Because the tuning is by coordinate multipliers, it preserves the entire classical Hamming profile of any fixed GRL skeleton, making the result directly reusable for MDS/AMDS/NMDS instances and entanglement-assisted constructions. The retained low-degree bound is a real limitation but does not erase the structural simplification.

## Sources

- Galois Hulls of Generalized Roth-Lempel Codes and Their Applications to EAQECCs (Xuefei Wu; Qi Liu; Yingchun Chen; Haiyan Zhou): https://arxiv.org/abs/2609.20453 — Primary GRL source, including the dual polynomial characterization and structured prescribed-hull constructions.
- Galois self-orthogonal MDS codes with large dimensions (Ruhao Wan; Shixin Zhu): https://arxiv.org/abs/2412.05011 — Prior GRS/EGRS treatment of all Galois exponents, including odd-quotient characteristic two and propagation to arbitrary hull dimensions.
- Generalized Roth-Lempel Codes: NMDS Characterization, Hermitian Self-Orthogonality, and Quantum Constructions (Qi Liu; Xuefei Wu; Haiyan Zhou): https://arxiv.org/abs/2604.11350 — Earlier GRL Hermitian/self-orthogonality background.

## Limitations

- The result retains k≤floor((n+2^ell-1)/(2^ell+1)) and does not classify larger dimensions.
- It does not claim novelty for the power-map bijection or for arbitrary Galois hull dimensions of GRS/EGRS codes.
- It does not classify which arbitrary GRL skeletons are MDS, AMDS, or NMDS, and it does not address odd characteristic.

## Independent checks

```json
{
  "proof_reconstructed": true,
  "power_map_gcd_checked": true,
  "degree_and_root_counts_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was used only as read-only evidence and no repository mutation was performed. Preprints and lawful open-access sources were checked first; no decisive comparison remained unavailable, so Oxford Download was not required.
