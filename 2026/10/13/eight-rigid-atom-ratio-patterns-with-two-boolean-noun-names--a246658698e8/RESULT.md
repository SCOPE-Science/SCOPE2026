# Eight rigid atom-ratio patterns with two Boolean noun names

## Finding
Consider finite nonempty structures with two unary predicate names \(P,Q\), and the four Boolean atoms
\[
A_1=P\cap Q,\quad A_2=P\cap\neg Q,\quad
A_3=\neg P\cap Q,\quad A_4=\neg P\cap\neg Q.
\]
A **fully supported rank-three balance theory** requires each \(A_i\) to be nonempty and specifies three linearly independent cardinality equalities \(|U_j|=|V_j|\), where \(U_j,V_j\) are Boolean combinations of \(P,Q\). Independence means that the three induced rational-linear equations in the four atom cardinalities have rank three.

**Classification theorem.** A positive primitive atom-cardinality ratio arises from such a theory if and only if, up to permutation of the four atoms, it is one of
\[
\begin{gathered}
(1,1,1,1),\ (1,1,1,2),\ (1,1,1,3),\ (1,1,2,2),\\
(1,1,2,3),\ (1,1,2,4),\ (1,2,2,3),\ (1,2,3,4).
\end{gathered}
\]
There are exactly **75** ordered primitive ratios, in eight permutation classes. The finite-model spectrum of each theory is exactly \(s\mathbb N_{>0}\), where \(s\) is the sum of the four entries of its primitive ratio. The attainable values of \(s\), with counts of ordered ratios, are

| \(s\) | 4 | 5 | 6 | 7 | 8 | 10 |
|:---|---:|---:|---:|---:|---:|---:|
| Number of ordered ratios | 1 | 4 | 10 | 12 | 24 | 24 |

Thus every fully supported rank-three balance theory using two Boolean noun names has a model of cardinality at most **10**, the bound is sharp, and the primitive model size **9 does not occur** in this class.

## Assumptions and scope
All structures have a finite nonempty universe. The noun-term language allows arbitrary Boolean combinations of the two predicate names. Each equality \(|U|=|V|\) can be encoded by the two cardinality-comparison sentences \(|U|\ge|V|\) and \(|V|\ge|U|\); atom nonemptiness is expressible by existential sentences. There are exactly three independent balance equalities; extra logically redundant equalities do not change the theory. The theorem is **not** about arbitrary combinations of strict cardinal inequalities or the original restricted noun-term language.

For every model put \(x_i=|A_i|\). The four positive integers \(x_i\) completely determine all Boolean noun cardinalities. A primitive ratio is the unique integer vector \(v\in\mathbb N_{>0}^4\) spanning the nonzero rational kernel of the balance equations and satisfying \(\gcd(v_1,v_2,v_3,v_4)=1\). Here \(\mathbb N_{>0}\) denotes positive integers.

## Proof
**1. Exact translation to a finite matrix problem.** For an equality \(|U|=|V|\), cancel the atoms that occur on both sides. The resulting coefficient row lies in \(\{-1,0,1\}^4\). Conversely, every such row is representable: put the union of atoms with coefficient \(+1\) on the left and the union of atoms with coefficient \(-1\) on the right. Whenever the row annihilates a strictly positive vector and is nonzero, both sides have at least one atom. Negating an equation is immaterial. Fix the sign so the first nonzero coefficient is \(+1\); there are exactly \((3^4-1)/2=40\) possible row directions.

**2. Rigidity and primitive models.** Three independent rows form a rank-three integer matrix \(M\) of shape \(3\times4\). Its rational nullspace has dimension one. A strictly positive solution exists exactly when the nonzero cofactor kernel vector has four coordinates of the same strict sign. Divide its absolute coordinates by their greatest common divisor to obtain the unique primitive \(v\). Because \(v\) is primitive, every integer solution in the positive ray is \(tv\) for an integer \(t\ge1\). All such solutions are realized as finite structures by choosing each atom to have the prescribed number of elements. Thus the spectrum is exactly \(s\mathbb N_{>0}\), with \(s=\sum_i v_i\).

**3. Finite exhaustive upper classification.** Each cofactor of \(M\) is a determinant of a \(3\times3\) matrix with entries in \(\{-1,0,1\}\). Hadamard's inequality gives \(|\det|\le3\sqrt3<6\), so every coordinate of the primitive positive kernel vector is in \(\{1,2,3,4,5\}\). Consequently it suffices to check the **63** nondecreasing primitive positive quadruples in that interval. For a candidate \(v\), form the set of all 40 signed ternary rows orthogonal to \(v\), and calculate its exact rational rank. A rank of three is necessary and sufficient for three independent balance equations with ratio \(v\). The full finite census yields rank distribution \(8\) at rank one, \(47\) at rank two, and \(8\) at rank three; the eight rank-three candidates are precisely the eight listed in the theorem. This is an exhaustive finite mathematical certificate, not an extrapolation.

**4. Explicit realization and multiplicities.** The table gives three independent coefficient rows for each nondecreasing representative. In each row \(1\) denotes inclusion of the corresponding atom on the left, \(-1\) its inclusion on the right, and \(0\) omission. Every row evaluates to zero on its listed vector; the three rows have rank three.

| Primitive ratio \(v\) | Three balance rows |
|:---|:---|
| \((1,1,1,1)\) | \((0,0,1,-1)\), \((0,1,-1,0)\), \((1,-1,-1,1)\) |
| \((1,1,1,2)\) | \((0,1,-1,0)\), \((0,1,1,-1)\), \((1,-1,0,0)\) |
| \((1,1,1,3)\) | \((0,1,-1,0)\), \((1,-1,0,0)\), \((1,1,1,-1)\) |
| \((1,1,2,2)\) | \((0,0,1,-1)\), \((1,-1,-1,1)\), \((1,1,-1,0)\) |
| \((1,1,2,3)\) | \((0,1,1,-1)\), \((1,-1,0,0)\), \((1,1,-1,0)\) |
| \((1,1,2,4)\) | \((1,-1,0,0)\), \((1,1,-1,0)\), \((1,1,1,-1)\) |
| \((1,2,2,3)\) | \((0,1,-1,0)\), \((1,-1,-1,1)\), \((1,0,1,-1)\) |
| \((1,2,3,4)\) | \((1,-1,-1,1)\), \((1,0,1,-1)\), \((1,1,-1,0)\) |

A primitive ratio with entry multiplicities \(m_1,m_2,\ldots\) gives \(4!/\prod m_i!\) distinct ordered ratios. The eight multiplicities are \(1,4,4,6,12,12,12,24\), summing to \(75\). Their coordinate sums give the stated model-size distribution and the sharp bound.

## Verification
Run `python3 verify.py` using Python 3 and its standard library. The program implements two independent exhaustive routes: all \(\binom{40}{3}=9880\) unordered triples of row directions with exact integral cofactor arithmetic, and all 63 sorted primitive positive candidates bounded by Hadamard, tested using exact fraction-free rational-rank elimination. It checks equality of the outputs and all eight explicit classes, the 75 ordered ratios, their exact size distribution, and the rank of witnesses. In the replay performed for this result, all assertions passed. No randomness, floating-point comparison, external package, or unresolved computational dependency is involved.

## Relationship to prior work
Jiang's 2026 study classifies finite spectra for a syllogistic cardinal-comparison language and its sentence-level Boolean extension. Moss and Topal studied syllogistic cardinal comparisons on infinite domains. The present question is different: Boolean combinations are allowed **inside noun terms**, the number of predicate names is fixed to two, and the invariant is the complete list of primitive fully supported ratios determined by rank-three equalities. The unrestricted finite-spectrum classification does not itself provide the eight ratio classes, 75 labelled ratios, or sharp ten-element bound. The finite linear-algebra reduction uses standard determinants and Hadamard's inequality; those ingredients are not claimed as new.

## Limitations
The 75-ratio classification is restricted to fully supported, rank-three **equalities** among Boolean noun cardinalities. In particular, the exclusion of \(9\) is **not** a claim that other two-noun theories cannot have a nine-element minimum model or spectrum \(9\mathbb N_{>0}\). This work does not classify higher-rank or mixed-inequality theories, arbitrary numbers of predicate names, infinite-model spectra, or sentence-level Boolean logic. The literature search did not establish universal novelty; an older equivalent finite-matrix or alphabet-bounded spectrum computation could exist.

## References
1. R. Jiang, *Finite Spectra of Syllogistic Logic with Cardinality Comparisons*, arXiv:2609.24902, first version 2026-09-21.
2. L. S. Moss and S. Topal, *Syllogistic Logic with Cardinality Comparisons, On Infinite Sets*, arXiv:1705.03037, first version 2017-05-08.
3. Hadamard's determinant inequality (classical); used solely for the explicit finite search bound.
