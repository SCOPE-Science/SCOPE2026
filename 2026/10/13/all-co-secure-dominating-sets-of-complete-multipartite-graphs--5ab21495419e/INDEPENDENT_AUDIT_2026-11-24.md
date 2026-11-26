# Independent mathematical audit

## correctness

PASS

PASS applies to the repaired text, not to the frozen scalar claim. The frozen formula says γ_cs(K_{5,5})=5, but a set with two vertices on each shore is co-secure: every selected vertex can be swapped with an omitted vertex across the bipartition, leaving both shores occupied. In any two-shore co-secure set, a shore with one selected vertex forces exactly one omission on the opposite shore and hence total size equal to that opposite shore size. If both selected counts are at least two, the total is at least four. This proves min{a,b,4}, attained by a whole smaller part when its size is at most four and otherwise by a 2+2 selection. The star and K_{1,1} values follow from the one-part test. The independent repair script artifacts/check_biclique_minimum.py confirmed the corrected minimum on all 28 profiles 1≤a≤b≤7, including K_{5,5} with minimum 4. For the remaining classification: a set dominates iff it meets two parts or fills one part. A full part of size at least two can swap into another part; a singleton full part can swap only into another singleton. For r≥3 and two occupied parts an unoccupied third part supplies every swap; with at least three occupied parts, the only obstruction is an empty complement or one confined to a single occupied part. With r=2 and both parts occupied, a swap after deleting the last selection from one shore must complete the opposite shore, yielding exactly the frozen mixed-set test. Counting the disjoint exclusions and adding the admissible one-part sets gives the stated polynomials. The frozen verifier checks the criterion and coefficients, not the asserted scalar minimum; its reported replay does not contradict the counterexample. The corrected proof and reproducibility notes are in /workspace/repairs/2/; frozen evidence is unchanged.

## originality

PASS

PASS is for the repaired complete classification and enumerators. The corrected scalar biclique result is prior work and is explicitly credited in the repair. The closest exact-family catalogue result uses secure, not co-secure, domination, and does not cover the repaired feasible-set system. The inspected evidence did not establish prior coverage of the all-set co-secure statement or its polynomials.

## value

PASS

The repaired result specifies the actual family of co-secure sets in a natural dense graph class, showing why the two-part case differs and giving exact counts by size for arbitrary part sizes. This is more than the known minimum, and the proof gives the replacement obstruction directly from the part occupancies.

The dated certificate retains the supplied scientific assessment, sources and limitations.
