# Independent Audit — 2026-09-28

**Record:** `2026/09/11/023`  
**Title:** No single Hall isoclinism family contains SmallGroup(64,199) and the nine B0-positive order-64 groups  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `01fc5cda68b34b7a5c638d54927b069a55f60c6d`  
**Disposition:** **PASSED**

## Independent checks

- Read the live HAP census and invariance theorem rather than relying on the repository copy.
- Checked the live Jena catalogue entry for 64gp199.
- Separated the valid impossibility conclusion from the unperformed capability/epicenter computation.

## Three-axis assessment

- **Correctness — PASS**: The contradiction is immediate and valid from independently checked public data. HAP’s exhaustive loop over AllSmallGroups(64) lists exactly IDs 149,150,151,170,171,172,177,178,182 as having nontrivial Bogomolov multiplier, so ID 199 has trivial B0. The same HAP documentation states Moravec’s theorem that isoclinic groups have isomorphic Bogomolov multipliers. Therefore 199 cannot belong to one Hall isoclinism family with any of those B0-positive groups, much less all nine. The Jena catalogue independently identifies 64gp199 as Hall–Senior 106.
- **Originality — LIMITED**: The record combines two already-published facts—an exhaustive HAP census and isoclinism invariance of B0—to refute an inconsistent family description. The logical consequence is correct and useful, but it is not a new group-theoretic theorem or a new B0 computation.
- **Scientific Value — PASS**: As a scope diagnostic, the result prevents a capability/epicenter project from being built on a nonexistent single family and forces the input groups to be re-partitioned correctly before any Z*(G) table is attempted. Its value is corrective rather than classificatory.

## Findings

- Current main tree exactly equals the assigned source-tree SHA.
- HAP’s all-groups order-64 output contains the nine stated positive IDs and not 199.
- HAP explicitly states B0 is an isoclinism invariant.
- Jena lists SmallGroup(64,199) as Hall–Senior 106; the core contradiction does not depend on the auxiliary Hall–Senior fingerprint mapping for the nine positive groups.

## Sources compared

- Repository record 023 RESULT.md: https://github.com/SCOPE-Science/SCOPE2026/blob/e9ed144c13b7834896a844cc4f9cac3c25a168a6/2026/09/11/023/RESULT.md — States the one-family impossibility claim audited here.
- HAP: The Bogomolov Multiplier: https://gap-packages.github.io/hap/www/SideLinks/About/aboutBogomolov.html — Publishes the exhaustive order-64 nontrivial-B0 list and states Moravec’s isoclinism-invariance theorem.
- Jena cohomology catalogue: Small group number 199 of order 64: https://users.fmi.uni-jena.de/~green/Coho_v3/64gps/64gp199.html — Identifies 64gp199 and gives Hall–Senior number 106.

## Limitations

- No epicenter Z*(G), capability status, or complete isoclinism partition is computed.
- The novelty is intentionally limited: the result is a corrective corollary of public census/invariance data.

This audit is independent of the repository’s pre-existing audit material. GitHub was read only as evidence; no repository changes were made by this audit run.
