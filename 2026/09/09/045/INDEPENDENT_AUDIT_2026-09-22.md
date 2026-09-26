# Independent audit — 2026-09-26

Record: `2026/09/09/045`. Verdict: **correctness PASS; originality PASS (witnesses); scientific value PASS (bounded).** Disposition: retain accepted.

## Correctness
I parsed the two 33-triple lists from RESULT.md and used independent bitmask recursion to count disjoint four- and five-block subfamilies. Each covers exactly 99 distinct pairs, each has zero disjoint five-subfamilies, and the disjoint four-subfamily counts are respectively 269 and 266. The sorted point degree multisets agree with the record and differ, proving non-isomorphism. On 16 points a point can lie in at most floor(15/2)=7 triples in a pair packing, so 3B≤112 and B≤37. Thus 33≤beta(4,16)≤37 is valid. The test verifies the explicit constructions and bound, not exact beta or nonexistence at 34–37.

## Prior work and originality
Stinson, arXiv:2007.11033, defines beta(rho,v) and provides general construction/counting bounds. Demirkale–Donovan–Grannell, arXiv:1708.07646, enumerate maximum partial triple systems of order 16 and structural invariants, a different endpoint. These two concrete 33-block PPC-four lists improve the cited construction floor within this record's comparison; I found no matching explicit lists in those open texts. The 37 ceiling is the familiar unconstrained pair count and has no new content.

## Scientific value and limits
The two independently checkable examples narrow the constructive interval and supply different degree types, useful for further extremal search. The four-unit gap is unresolved; random-greedy behavior is no upper-bound evidence, and no classification of 33-block examples follows.

Sources: RESULT.md, output/artifacts/verify.py; https://arxiv.org/abs/2007.11033; https://arxiv.org/abs/1708.07646.
