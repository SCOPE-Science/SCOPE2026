# Independent Audit — 2026-09-29

**Record:** `2026/09/12/013`  
**Title:** Fukuda First-Layer Stabilization over Q(sqrt29) at p=5  
**Repository:** `SCOPE-Science/SCOPE2026`  
**Audited tree:** `e74d344d014de540c09c49f76481bb5bcaf4568c`  
**Disposition:** **REPAIRED**

## Independent checks

- Rechecked the base class-number argument and split/Hensel congruences.
- Verified the group-theoretic mod-25 fifth-power subgroup {1,7,18,24} and the epsilon obstruction.
- Checked the Chevalley ambiguous-class formula specialization and the fixed-point implication for a nontrivial finite 5-group.
- Compared the stabilization step with Fukuda's theorem and narrowed the local norm argument using local reciprocity for Q5.

## Three-axis assessment

- **Correctness — PASS_AFTER_REPAIR**: The headline conclusion |A0|=|A1|=1 and lambda_5=mu_5=0 survives, but the filed proof overstates a local norm lemma: N(U_L)=U_K^5 is not valid for an arbitrary unramified extension K/Q5 of higher residue degree. In this application each completion k_p is exactly Q5 because 5 splits, and for the specific degree-5 cyclotomic subextension of Q5(zeta_25), local reciprocity gives norm units equal to Q5-unit fifth powers, equivalently residues mod 25 in {1,7,18,24}. The epsilon images 14 and 16 fail that test, so j=5; Chevalley and Fukuda then give the claimed stabilization.
- **Originality — LIMITED**: The proof is an explicit instance of standard Chevalley/local-reciprocity/Fukuda machinery. Searches found broad real-abelian criteria (including Tsuji 2003) and older Fukuda–Taya computations, so the audit does not claim first priority for the vanishing statement; the explicit first-layer certificate remains useful.
- **Scientific value — PASS**: After narrowing the local norm claim to the actual Q5 cyclotomic completion, the record gives a compact reproducible first-layer proof of Greenberg stabilization for this specific (d,p) pair. Its value is as a concrete certificate and reusable worked example, not as a new general theorem.

## Findings

- The current record tree exactly matches the assigned tree SHA.
- Minkowski plus inertness of 2 proves h(Q(sqrt29))=1, hence |A0|=1.
- The Hensel lifts omega≡12,14 (mod25) give epsilon≡14,16 and fourth powers 16,11, so epsilon is not in the cyclotomic local norm subgroup at either split 5-adic place.
- The filed general local-norm sentence for arbitrary unramified K_v/Q5 is too broad; the corrected proof restricts it to k_p=Q5 and the degree-5 subfield of Q5(zeta25), where the criterion is valid.
- Fukuda's stabilization theorem applies once total ramification and |A0|=|A1| are established.
- The corrected RESULT and METADATA also use actual repository-relative `artifacts/...` paths.

## Sources compared

- Fukuda, Remarks on Z_p-extensions of number fields (1994): https://projecteuclid.org/journals/proceedings-of-the-japan-academy-series-a-mathematical-sciences/volume-70/issue-8/Remarks-on-Z_p-extensions-of-number-fields/10.3792/pjaa.70.264.full — Stabilization theorem: after total ramification begins, equality of two consecutive p-class-group orders forces subsequent stabilization and lambda=mu=0.
- Local Fields notes: local reciprocity and cyclotomic norm groups: https://androma.org/page/Cambridge%20III%20Local%20Fields — Explains the Artin map on Q_p units and cyclotomic norm groups; this supports the corrected Q5-specific mod-25 norm criterion.
- Tsuji, On the Iwasawa lambda-invariants of real abelian fields: https://doi.org/10.1090/S0002-9947-03-03357-9 — Provides broad odd-p real-abelian Greenberg criteria, so priority for this isolated numerical instance should not be overstated.
- Fukuda–Taya, The Iwasawa lambda-invariants of Z_p-extensions of real quadratic fields: https://eudml.org/doc/206688 — Earlier real-quadratic Iwasawa computations and criteria; method context for the submitted instance.

## Limitations

- The audit does not claim that the (29,5) vanishing instance is absent from every prior computational table or criterion.
- The repaired argument establishes only the 5-primary stabilization in the cyclotomic Z5 tower, not full class groups at higher layers.
- The current exact scripts support arithmetic identities but do not themselves formalize local class field theory or Fukuda's theorem.
- The full text of Tsuji (2003) was not obtained in this run: open-access searching returned metadata/abstract only, and the Oxford institutional retrieval attempt was blocked by the tool. The audit therefore does not claim to have read that paper.

This audit is independent of the repository's pre-existing audit material. GitHub was read only as evidence; no repository changes were made by this audit run.
