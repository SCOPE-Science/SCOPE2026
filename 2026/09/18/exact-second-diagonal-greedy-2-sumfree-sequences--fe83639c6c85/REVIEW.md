# Review: exact second-diagonal greedy 2-sumfree sequences

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.** The claimed set has two exceptional elements and four periodic residue blocks modulo \(M=9f-1\). A complete block-sum calculation shows that the periodic residue set is disjoint from its pairwise sumset modulo \(M\). Separate residue calculations cover sums involving the two exceptional elements, and the two exceptional target values are ruled out directly.

Greedy saturation is also complete. Every omitted integer between \(3f\) and \(M\) lies in one of four elementary strict sumsets. For every omitted residue modulo \(M\), an explicit two-term witness represents either \(r\) or \(M+r\); translating a periodic summand by a multiple of \(M\) produces a representation of every higher omitted integer by two distinct earlier members. The two rows that use the absent initial value \(f+1\) use it only after a positive translation, where that residue-class element is present. Hence no excluded case is left untreated.

The exact difference word follows from the residue description. Its period block has length \(2f+2\), sum \(9f-1\), and contains the value \(2f\) exactly once for \(f\ge4\), so it is primitive. The preceding difference is \(1\), while a backward extension of the period would require \(f+3\), proving minimality of the preperiod as well.

The standalone verification artifact separately checks the greedy formula for \(f=4,\ldots,80\), 700 terms per case, and checks the modular sum-free and saturation certificates for \(f=4,\ldots,200\).

## Originality

**PASS, to the best of our knowledge.** Van Berkel--Bosma, arXiv:2609.18522v1 (16 September 2026), was inspected through its full HTML rendering. It formulates explicit conjectures for all period and preperiod lengths. The ray \(d=2f\), equivalently \(g=3f\), is predicted there but is not among the proved infinite families; the paper instead supplies finite computational certification outside its proved region. The preceding arXiv:2609.16843v1 proves a broad region closer to the diagonal.

Searches covered the exact family notation `S_{f,3f}`, the formulas `9f-1` and `2f+2`, strict greedy 2-sumfree terminology, and the older synonyms `0-additive` and `non-additive`. No matching theorem or equivalent residue classification was found. Current reference sources continue to describe ultimate regularity of general \(0\)-additive sequences as conjectural.

Two older sources remain the principal access limitation. Raymond Queneau, *Sur les suites s-additives*, J. Combin. Theory Ser. A 12 (1972), 31--71, DOI 10.1016/0097-3165(72)90083-0, contains a substantial section on \(0\)-additive sequences and extensive explicit computations. Steven R. Finch, *Are 0-Additive Sequences Always Regular?*, Amer. Math. Monthly 99 (1992), 671--673, DOI 10.1080/00029890.1992.11995911, is another direct predecessor. Their full texts were not independently inspected. This leaves a real residual possibility that a special family equivalent to \(S_{f,3f}\) was recorded there under older notation. Against that risk, the 2026 van Berkel--Bosma work surveys this literature yet still treats the relevant period/preperiod values beyond its proved range as conjectural and computational. No concrete evidence of prior coverage was located.

## Value

**PASS.** The result proves an infinite one-parameter family beyond the currently proved diagonal region, confirms both the minimal period and preperiod predictions on the entire second diagonal \(d=2f\), and gives a stronger exact residue-class description rather than only eventual periodicity. The proof is elementary and uniform, replacing finite certification by a closed structural argument.
