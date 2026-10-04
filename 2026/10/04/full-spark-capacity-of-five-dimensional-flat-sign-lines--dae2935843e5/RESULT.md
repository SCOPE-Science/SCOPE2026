# Full-spark capacity of five-dimensional flat sign lines
## Finding
Call a nonzero real vector in \(\mathbb R^5\) *flat* when its five coordinate magnitudes are equal. Up to a nonzero scalar, every flat vector has a unique representative of the form
\[
(1,\varepsilon_2,\varepsilon_3,\varepsilon_4,\varepsilon_5),\qquad \varepsilon_j\in\{-1,1\}.
\]
Thus there are sixteen projective flat sign lines. Their largest full-spark subcollections have cardinality exactly \(6\). Exactly \(1088\) six-line subcollections are full spark. Under signed coordinate permutations modulo the global sign, these \(1088\) maximizers form five orbits, with orbit sizes
\[
16,\ 160,\ 192,\ 240,\ 480.
\]
An explicit maximizing subcollection is
\[
\begin{aligned}
&(1,-1,-1,-1,-1),\quad (1,-1,-1,-1,1),\quad (1,-1,-1,1,-1),\\
&(1,-1,1,-1,-1),\quad (1,1,-1,-1,-1),\quad (1,1,1,1,1).
\end{aligned}
\]
The six determinants obtained by deleting one row at a time are
\[
16,\ 16,\ -16,\ 16,\ -16,\ -48,
\]
so this six-line family is full spark.

As a consequence, no eight real flat vectors in \(\mathbb R^5\) can perform weak phase retrieval. A theorem of Botelho-Andrade, Casazza, Ghoreishi, Jose and Tremain states that a weak-phase-retrieval frame of the minimal size \(2n-2\) in \(\mathbb R^n\) must be full spark. For \(n=5\), eight vectors would therefore have to be full spark, but every projectively normalized flat family is contained in the sixteen lines above and no seven of those lines are full spark.

## Assumptions and scope
Full spark means that every five vectors in the family are linearly independent. The flatness condition is coordinate-dependent: it refers to the standard coordinates of \(\mathbb R^5\). Multiplying individual vectors by nonzero scalars does not change either projective full-spark status or weak phase retrieval, so projective normalization loses no information for the stated consequence.

The finite classification concerns only flat real vectors. It does not assert that eight-vector weak phase retrieval is impossible in \(\mathbb R^5\) for arbitrary, non-flat vectors.

## Proof
Normalize the first coordinate of each projective sign line to \(1\). This gives exactly the sixteen representatives
\[
\mathcal H_5=\{(1,\varepsilon_2,\varepsilon_3,\varepsilon_4,\varepsilon_5):\varepsilon_j\in\{-1,1\}\}.
\]
For every five-element subset of \(\mathcal H_5\), compute the corresponding \(5\times5\) determinant exactly over the integers. A subset is full spark precisely when every one of its five-element subsets has nonzero determinant.

There are \(\binom{16}{7}=11440\) seven-line subsets. Exhaustive exact determinant evaluation finds no full-spark seven-line subset. Any full-spark family of cardinality at least seven would contain a full-spark seven-line subfamily, so the capacity is at most six. The displayed six-line family has all six relevant determinants nonzero, proving the matching lower bound.

The same exhaustive test over the \(\binom{16}{6}=8008\) six-line subsets gives exactly \(1088\) full-spark maximizers. Signed coordinate permutations act projectively on \(\mathcal H_5\). Quotienting the global sign gives \(2^4\cdot 5!=1920\) distinct actions. Exact orbit closure of the \(1088\) maximizers yields five orbits of sizes \(16,160,192,240,480\), whose sum is \(1088\).

For the weak-phase-retrieval consequence, suppose eight flat real vectors in \(\mathbb R^5\) performed weak phase retrieval. Rescaling the measurement vectors by nonzero constants preserves the weak-phase-retrieval relation, so projectively normalize them into \(\mathcal H_5\). The minimal-cardinality theorem for weak phase retrieval says that \(2n-2=8\) such vectors in dimension five must be full spark. Repetitions already violate full spark; with distinct projective lines, an eight-element full-spark family would contain a seven-element full-spark subfamily. Both cases contradict the exact capacity-six classification.

## Verification
The accompanying `verify.py` uses the fraction-free Bareiss determinant algorithm, so all rank decisions are exact integers. It evaluates all \(4368\) five-line determinants, all \(11440\) seven-line candidates, all \(8008\) six-line candidates, and all \(1920\) projective signed-coordinate-permutation actions. Its expected terminal output is:

`VERIFY_OK projective_lines=16 max_full_spark=6 full_spark_6sets=1088 symmetry_group=1920 orbits=5 orbit_sizes=16,160,192,240,480`

`WITNESS (0, 1, 2, 4, 8, 15) DETS 16,16,-16,16,-16,-48`

The finite computation proves only the finite flat-sign classification. The implication for weak phase retrieval additionally uses the cited analytic theorem that minimal weak-phase-retrieval frames are full spark.

## Relationship to prior work
The 2016 paper *Weak phase retrieval and phaseless reconstruction* proves the minimal-cardinality full-spark necessity and gives explicit minimal weak-phase-retrieval examples made entirely of sign vectors in \(\mathbb R^3\) and \(\mathbb R^4\). The 2021 paper *A note on (weak) phase and norm retrievable Real Hilbert space frames and projections* explicitly asks for \(2n-2\) weak-phase-retrieval frames in every \(\mathbb R^n\) for \(n\ge5\), identifying dimension five as the first unresolved case beyond those examples. The present result shows that the natural flat-sign pattern of the known examples cannot extend to that first open dimension.

The 2023 paper *Classifying weak phase retrieval* gives a different obstruction: a minimal weak-phase-retrieval frame containing a canonical basis vector cannot work. Flat sign vectors have no zero coordinates, so that theorem does not imply the present hypercube-line capacity bound. General full-spark-frame constructions likewise do not impose the flat-sign constraint.

## Limitations
The result is a sharp classification inside the sixteen projective real flat sign lines. It neither constructs nor rules out a non-flat eight-vector weak-phase-retrieval frame in \(\mathbb R^5\). The orbit statement uses only signed coordinate permutations modulo global sign, not an assertion about equivalence under arbitrary invertible linear transformations.

The literature comparison cannot exclude an obscure or unindexed equivalent classification of projective hypercube vertices under different combinatorial terminology. No covering statement was found in the materially inspected weak-phase-retrieval sources or in targeted searches under full-spark, sign-vector, hypercube, and general-position formulations.

## References
1. R. Botelho-Andrade, P. G. Casazza, D. Ghoreishi, S. Jose, J. C. Tremain, *Weak phase retrieval and phaseless reconstruction*, arXiv:1612.08018, first version 2016-12-23.
2. *A note on (weak) phase and norm retrievable Real Hilbert space frames and projections*, arXiv:2110.06868, first version 2021-10-13.
3. *Classifying weak phase retrieval*, arXiv:2301.03520, first version 2023-01-09.
4. B. Alexeev, J. Cahill, D. G. Mixon, *Full Spark Frames*, arXiv:1110.3548.
