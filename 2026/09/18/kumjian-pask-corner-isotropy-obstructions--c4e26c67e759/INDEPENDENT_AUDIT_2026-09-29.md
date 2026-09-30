# Independent audit — Corner and isolation obstructions in Kumjian--Pask induction--restriction

**Audit date:** 2026-09-29 (UTC)
**Source path:** `2026/09/18/kumjian-pask-corner-isotropy-obstructions--c4e26c67e759`
**Audited tree:** `b9f983c3fd66a5472a3c89452f3a152a9a08d7d1`

## Disposition

**PASSED.** The record survives independent review on correctness, originality, and scientific value without a substantive research-file change.

## Correctness

All three obstructions and the stated repairs are correct. The one-vertex one-loop graph has KP algebra R[t,t^{-1}] with vertex idempotent 1, so its vertex corner is not scalar. In the disjoint two-loop example, the hereditary corner is the second direct summand and the outside idempotent is annihilated by its identity, so the ambient right corner-module is nonunital and cannot be free. The balanced-tensor identity A tensor_{pAp} V ~= Ap tensor_{pAp} V follows from a tensor v = ap tensor v for unital V. For an ample Hausdorff groupoid, the point mass at the isotropy identity lies in the Steinberg algebra only if {x} is open; conversely, isolation lets a compact-open bisection through each isotropy arrow be cut down to that singleton, so the group algebra embeds exactly in the isolated-unit case.

### Independent checks

- Computed the one-loop KP algebra as R[t,t^{-1}] and checked s_v=1, so s_vAs_v=A and As_v includes negative Laurent powers.
- For A=k[t^{±1}] direct-sum k[u^{±1}] and p=(0,1), checked (1,0)p=0 while (1,0) is nonzero; a free module over unital pAp would be unital, so A_{pAp} is not free.
- Verified the two inverse maps A tensor_{pAp} V -> Ap tensor_{pAp} V, a tensor v |-> ap tensor v, and inclusion, including balancedness.
- Proved necessity of isolation from local constancy of 1_{ {x} } at the identity isotropy arrow.
- Proved sufficiency by intersecting a compact-open bisection U containing g with s^{-1}({x}); the result is the compact-open singleton {g}, and convolution reproduces group multiplication.

## Originality

PASS, with an explicit chronology caveat. The exact 27-page arXiv:2609.20230v1 was independently retrieved and inspected: it states the scalar vertex-corner identification in Section 3.1, the ambient-module freeness theorem in Theorem 3.5, and the singleton point-mass isotropy embedding (4.1)/Proposition 4.1 exactly as targeted. The current v2, dated September 18, 2026, is a substantially different pullback-KP paper that abandons those v1 constructions and explicitly says its isotropy-induction approach avoids identifying an isotropy group algebra with a vertex corner. V2 does not state the three counterexamples or the iff isolated-unit theorem. The SCOPE correction was committed at 2026-09-18T08:01:43Z, but the available arXiv metadata did not expose the exact v2 submission time, so same-day priority between the correction and the author's replacement v2 cannot be resolved more finely. Standard corner and Steinberg facts remain prior art.

### Literature checked

- https://arxiv.org/abs/2609.20230 — Nguyen Bich Van. The exact v1 (27 pages) and current v2 were independently retrieved. V1 contains the three targeted constructions; v2 is a substantially rewritten pullback-KP paper that no longer uses them and explicitly avoids the vertex-corner/isotropy identification.
- https://arxiv.org/abs/2006.09931 — Loc--Van, prior graded isotropy induction for Steinberg algebras; standard isotropy-induction machinery is prior art and offers a repair route.
- https://arxiv.org/abs/2504.11639 — Dokuchaev--Exel--Pinedo, Twisted Steinberg algebras, regular inclusions and induction (2025); further background showing isotropy/regular-inclusion induction does not require singleton-subalgebra embeddings.

## Scientific value

The record gives a precise forensic explanation of why three prominent constructions in v1 fail and supplies exact replacements. Its current value is partly archival because arXiv v2 has already replaced the v1 framework rather than repairing it in place; nevertheless, the explicit counterexamples, isolated-unit criterion, and Ap tensor repair explain the mathematical failure modes and remain useful for evaluating citations or downstream uses of v1.

## Limitations

- The record corrects arXiv:2609.20230v1, not the current v2; v2 has already replaced the flawed framework with a different pullback-KP program.
- The exact ordering within September 18 between the SCOPE correction and arXiv v2 could not be established from the accessible version metadata, so same-day priority is explicitly unresolved even though no matching correction theorem appears in v2.
- The record does not establish that every downstream v1 conclusion is false; some may survive after reformulation through standard corner or Steinberg-isotropy machinery.

## Publication guard

The current source tree on `main` matched the assignment tree exactly during this audit. This guarded change-set adds only the independent-audit evidence pair and updates the independent-audit channel in `VERIFICATION.md`; the Lean and expert-attestation channels are preserved unchanged.
