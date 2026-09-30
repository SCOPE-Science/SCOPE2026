# A disconnected reconfiguration graph of minimum-genus orientable embeddings of K(4,7)

This record uses the following explicit move. A vertex is one isomorphism class of orientable genus-3 rotation systems of K(4,7). Two classes are adjacent when one can be obtained from the other by replacing the cyclic order at exactly one graph vertex by a genuinely different cyclic order, with the resulting rotation system still of genus 3. Cyclic shifts of a row represent the same rotation and are not edges. This is a custom rotation-reordering graph, not the standard diagonal-flip graph of a surface triangulation.

For K(4,7), V=11 and E=28. Ringel's formula gives minimum orientable genus 3, equivalently F=13. The two witnesses are:

E1 A-rows:
(6,5,4,2,1,0,3)
(6,3,0,5,1,2,4)
(6,0,3,4,2,1,5)
(3,6,4,5,0,1,2)

E1 B-rows:
(1,2,0,3), (0,1,2,3), (3,2,1,0), (3,2,1,0), (3,1,2,0), (1,3,0,2), (1,3,2,0)

E2 A-rows:
(2,6,0,4,5,3,1)
(5,0,6,1,3,2,4)
(4,1,3,5,6,2,0)
(4,0,2,3,1,6,5)

E2 B-rows:
(2,3,0,1), (0,1,3,2), (2,0,1,3), (1,0,2,3), (1,2,0,3), (2,0,1,3), (1,0,2,3)

Independent face tracing gives F=13 and face lengths {4^11,6^2} for both systems, so both have genus 3.

A brute-force check of all 4!·7!=120960 bipartition-preserving relabellings finds no orientation-preserving rotation-system isomorphism E1 -> E2.

For each witness, exhaustively replace one A-row by every other permutation of the seven B-neighbours and one B-row by every other permutation of the four A-neighbours. After excluding the identical row, there are 4(7!-1)+7(4!-1)=20317 candidates. Exactly 45 candidates preserve F=13: six nontrivial cyclic shifts at each of the four A-vertices and three nontrivial cyclic shifts at each of the seven B-vertices, for 4·6+7·3=45. There are zero genus-3 replacements that are not cyclic shifts.

Thus E1 and E2 are distinct isolated vertices of the stated reconfiguration graph. The graph is therefore disconnected.

## Reproducibility and limitations

The 2026-09-29 audit independently implemented face tracing, the full 120960 relabelling test, and the 20317 single-row replacement test for each witness. The previously referenced `output/artifacts/witnesses.json` and `verify_final.py` are not present in the audited repository tree and are not claimed as evidence. The former approximate wider census is not needed for the theorem and is omitted here.

No complete census, component count, or statement about other notions of flip is claimed.

## References

- Grannell and Knor, *An enumeration of minimum genus orientable embeddings of some complete bipartite graphs* (2010), which already enumerates minimum-genus K(4,7) embeddings.
- Burton, Datta, Spreer, *Flip Graphs of Stacked and Flag Triangulations of the 2-Sphere*, Electron. J. Combin. 29 (2022), for comparison with the standard triangulation-flip setting.
