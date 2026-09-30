# Independent Audit — 2026/09/21/affine-agl1q-bi-groups-spectral-residues--aeb40a05a8dc

- Audit date: 2026-09-30 (UTC)
- Repository: `SCOPE-Science/SCOPE2026`
- Branch: `main`
- Inventory commit: `e9ed144c13b7834896a844cc4f9cac3c25a168a6`
- Source-tree checked commit: `253a0fe5d0217455660a277f9adb940030e567ad`
- Audited record tree: `de931d8eeb6f28e4f1290d64a69ffe09a2e85fa9`
- Disposition: **PASSED**

## Correctness

**PASS** — The spectral residue mechanism is valid. For a group with d linear irreducibles and one nonlinear irreducible of degree d, the regular representation puts each linear character sum into the Cayley spectrum once, whereas each eigenvalue from the nonlinear d-dimensional block occurs with multiplicity divisible by d. Thus the multiplicity of each graph eigenvalue modulo d recovers the number of linear character sums equal to it. Connectedness excludes the sole ambiguity l=d because the principal-character eigenvalue |S| is simple in a connected regular graph. The adjacency trace is zero, so the unique nonlinear character sum is then recovered from the sum of the linear contributions. Seitz's one-nonlinear-character classification gives the Frobenius branch with elementary abelian kernel of order q and cyclic complement of order q-1, hence AGL(1,q); here the nonlinear degree and the number of linear characters are both q-1. The Sylow-5 CI obstruction for primes q=1 mod 25 is also correctly applied.

## Originality

**PASS** — Abdollahi-Zallaghi's open 2017/2019 paper explicitly advertises two nonabelian non-CI BI examples of orders 20 and 42 and a census through order 30, rather than a general AGL(1,q) theorem. These examples are AGL(1,5) and AGL(1,7). Searches for AGL(1,q), ratio-one Frobenius groups, and BI-groups did not locate the residue argument or the infinite generalization. The 2026 ratio-one Frobenius spectral paper concerns Ramanujan normal Cayley graphs, not Babai character-sum invariance. The novelty claim is therefore appropriately limited to the general multiplicity-residue criterion and its AGL family.

## Scientific value

**PASS** — The result replaces isolated character-table calculations by a transparent representation-multiplicity mechanism, proves an infinite nonabelian BI family, and yields infinitely many BI-but-not-CI examples. It advances the finite BI-group classification problem while correctly leaving the extraspecial-2 branch open.

## Sources

- **Non-Abelian finite groups whose character sums are invariant but are not Cayley isomorphism** — Alireza Abdollahi; Maysam Zallaghi. https://arxiv.org/abs/1710.04446 — Open source checked; it identifies two nonabelian BI-but-not-CI groups of orders 20 and 42 and lists BI-groups through order 30.
- **Finite groups having only one irreducible representation of degree greater than one** — Gary M. Seitz. https://doi.org/10.1090/S0002-9939-1968-0222160-X — Classical classification supplying the Frobenius and extraspecial branches.
- **Ramanujan Cayley Graphs with Normal Connection Sets in Ratio-One Frobenius Groups** — M.-H. Kang; C.-J. Yang. https://arxiv.org/abs/2608.19905 — Recent related spectral work on the same Frobenius class, but not a BI-group theorem.

## Limitations

- The criterion does not cover the extraspecial 2-group branch of Seitz's classification.
- It concerns simple undirected Cayley graphs under the BI convention, not arbitrary Cayley digraphs.
- The argument relies on connectedness before using the standard connected-complement reduction.
- Concurrent work on this newly highlighted Frobenius class remains a residual priority risk.

## Independent checks

```json
{
  "regular_representation_multiplicity_argument_checked": true,
  "mod_d_linear_sum_recovery_checked": true,
  "connected_top_eigenvalue_ambiguity_checked": true,
  "trace_recovery_of_unique_nonlinear_sum_checked": true,
  "seitz_frobenius_parameter_count_checked": true,
  "open_access_first": true,
  "oxford_used": false
}
```

GitHub was used only as read-only evidence and no repository mutation or separate dispatcher report was performed. The assigned source tree was unchanged between the inventory commit and the source-tree-check commit. Open-access/preprint sources were checked before authorized institutional retrieval. Inaccessible material is explicitly identified and is not claimed read.
