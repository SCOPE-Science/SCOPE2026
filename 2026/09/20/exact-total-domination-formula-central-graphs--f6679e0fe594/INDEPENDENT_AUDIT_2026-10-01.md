---
audit_date: 2026-10-01
status: passed
---

# Independent scientific audit

## Final claim

For every finite simple graph \(G\) without isolated vertices, \(\gamma_t(C(G))\) equals the minimum over vertex covers \(A\) of \(|A|+\rho_G(R_G(A))\), equivalently \(|A|+|R_G(A)|-\nu(G[R_G(A)])\); equality with \(\tau(G)\) has the stated complement-total-domination criterion.

## Correctness — PASS

A total dominating set of the central graph decomposes exactly into an original-vertex cover and subdivision vertices whose corresponding edges cover the residual original vertices lacking a selected complement neighbor. Conversely any such pair is a total dominating set. The partial edge-cover number equals \(|R|-
u(G[R])\) by a maximum-matching construction and matching lower bound.

**Checked sources.** assigned RESULT.md; artifacts/verify_formula.py; Kazemnejad--Moradi 2019 full text; Chen--Sohn--Wang 2020 abstract

**Residual risks.** 

## Originality — PASS

The 2019 primary source gives only the general bounds and family formulas; it does not state the all-graph residual vertex-cover/partial-edge-cover optimization identity. The 2020 source is tree-specific by its public description.

### Equivalent formulations

Equivalent matching and complement formulations were compared.

### Broader coverage

No broader theorem was located that implies the arbitrary-graph identity.

### Exact database or table

Finite graph tables are not an antecedent for the symbolic theorem.

### Claim versus prior implication

The exact decomposition is additional structural content, not a mechanical corollary of the bounds.

**Checked sources.** https://doi.org/10.4134/BKMS.b180891; https://doi.org/10.4134/BKMS.b190162; Resultary assigned-record hit

**Residual risks.** A tree-specialized overlap may exist but cannot cover the general theorem.

## Value — PASS

The result upgrades foundational all-graph bounds to an exact reusable structural identity and characterizes the residual cost by an induced matching number.

**Checked sources.** Kazemnejad--Moradi 2019; Chen--Sohn--Wang 2020

**Residual risks.** 

## Limitations

- Structural identity, not a polynomial-time algorithm.
- The 2020 tree paper was only available at abstract/bibliographic level.

## Disposition

PASSED. Acceptance requires PASS on correctness, originality, and value.
