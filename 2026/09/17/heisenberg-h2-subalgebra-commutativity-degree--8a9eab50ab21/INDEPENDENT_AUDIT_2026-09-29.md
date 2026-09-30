# Independent Audit — 2026/09/17/heisenberg-h2-subalgebra-commutativity-degree--8a9eab50ab21

- Audit date: 2026-09-29 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Audited commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `d24bb51dcd2f713eefae436e8b3e15e390cf553f`
- Disposition: **PASSED**

## Correctness

**PASS** — The symplectic classification and incidence count are correct. Subalgebras containing the one-dimensional center are inverse images of arbitrary subspaces of the four-dimensional quotient; subalgebras disjoint from the center are graphs of linear functionals over totally isotropic subspaces. For graph subalgebras, z belongs to A+B exactly when the functionals differ on U∩W, giving the stated nonpermutability criterion and q^(r+s-t) functional weight. The line/Lagrangian counts then expand to E=q^10+3q^9+7q^8+8q^7+7q^6+5q^5+q^4, and N^2-E gives the displayed numerator. As an independent exact check, I freshly enumerated all 374 subspaces of F_2^5 in RREF form, found exactly 158 Lie subalgebras, and counted 18,964 permutable ordered pairs, matching the theorem.

## Originality

**PASS** — The full v1 of Muhie-Otera-Russo was independently retrieved from arXiv in this run. Its introduction explicitly asks for sd(h(m)) and Theorem 1.2 gives only the rank-one h(1) formula; no h(2) theorem appears among its main results. Targeted searches for the exact rank-two/five-dimensional formula and for a matching extraspecial-p-group subgroup commutativity formula did not locate a prior result. The symplectic-subspace ingredients are classical, but the exact rank-two invariant and the graph-pair enumeration appear new.

## Scientific value

**PASS** — This resolves the first Heisenberg rank beyond the source paper's rank-one computation, gives a closed formula over every finite field including characteristic two, and isolates a general symplectic incidence criterion that can be reused for higher ranks. The asymptotic sd(h(2,F_q))~3/q is also a concrete first data point for the open h(m) program.

## Sources

- On the number of modular pairs in finite dimensional Lie algebras on finite fields (Seid Kassaw Muhie; Daniele Ettore Otera; Francesco G. Russo): https://arxiv.org/abs/2609.19086 — Full v1 independently inspected: lines around Theorem 1.2 compute h(1) and explicitly pose values of sd(h(m)).
- The subgroup commutativity degree of finite P-groups (Marius Tărnăuceanu): https://doi.org/10.1017/S0004972715000702 — Nearest group-theoretic background; no matching extraspecial order-p^5 formula was surfaced in targeted searches.

## Limitations

- The theorem is rank two; it does not provide a closed formula for arbitrary h(m).
- The independent brute-force check covers q=2; the all-prime-power statement rests on the symplectic proof.
- A specialized older group-theoretic formula under Lazard correspondence remains a residual originality risk, but no concrete covering source was located.

## Independent exact check

```json
{
  "implementation": "fresh F2 RREF-subspace enumeration and direct Lie-bracket/permutability test",
  "ambient_subspaces": 374,
  "lie_subalgebras": 158,
  "permutable_ordered_pairs": 18964,
  "all_ok": true
}
```

The assigned source tree was unchanged between the inventory commit and the audited source-tree-check commit. GitHub was read only as evidence and no repository mutation was performed. Open-access/preprint sources were checked first. Oxford Download was not needed for this record.
