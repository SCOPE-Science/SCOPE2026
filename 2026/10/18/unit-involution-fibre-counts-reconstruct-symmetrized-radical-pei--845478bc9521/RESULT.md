# Unit–involution fibre counts reconstruct symmetrized radical Peirce graphs

## Finding
Let \(A\) be a finite-dimensional unital associative algebra over \(\mathbb F_q\), \(q\) odd, whose Jacobson quotient is a nonempty product of finite fields, \(A/J\cong\prod_{i=1}^{t}F_i\). Choose mutually orthogonal idempotent lifts \(e_1,\ldots,e_t\) with sum \(1\). Put
\[
w_{ij}=\dim_{\mathbb F_q}(e_iJe_j)+\dim_{\mathbb F_q}(e_jJe_i)\quad(i<j).
\]
For \(a\in A\), let \(\overline a=(a_1,\ldots,a_t)\) be its image in the quotient, and let \(N(a)\) count ordered decompositions \(a=u+v\) with \(u\in A^\times\) and \(v^2=1\). Then the **exact fibre law** is
\[
N(a)=\sum_{\substack{\epsilon\in\{\pm1\}^t\\a_i\ne\epsilon_i\text{ in }F_i\ \forall i}}q^{\sum_{i<j}w_{ij}\mathbf 1_{\epsilon_i\ne\epsilon_j}}.\tag{1}
\]
In particular every element has at least one decomposition. Conversely, in characteristic two, no nonzero finite-dimensional algebra with such a field-product quotient has this universal property.

The family of integers \(N(a)\), restricted to elements with all quotient coordinates in \(\{\pm1\}\), reconstructs each labelled weight \(w_{ij}\) exactly. Thus it determines the symmetrized radical Peirce graph; it does **not** determine arrow orientations or the full multiplication of \(A\).

## Assumptions and scope
All fields \(F_i\) are finite extensions of \(\mathbb F_q\); no splitness, commutativity, or radical-square-zero assumption on \(A\) is needed. The Jacobson radical \(J\) is nilpotent. Lifting the primitive central idempotents of \(A/J\) gives pairwise orthogonal \(e_i\) summing to one. The weights are unchanged by simultaneous conjugation of the lifts by a unit congruent to one modulo \(J\). The quotient factor labels are fixed for the reconstruction statement; without labels the graph is recovered up to permutation compatible with the factors.

An involution here means an element \(v\) satisfying \(v^2=1\), including \(v=1\). This is the convention in the unit-plus-involution decomposition problem. The decomposition count is finite and counts choices of \(v\), since \(u=a-v\) is then forced.

## Proof
**1. Lifting and unit detection.** Because \(J\) is nilpotent, orthogonal idempotents of \(A/J\) lift to orthogonal idempotents of \(A\); the usual induction through square-zero quotients establishes this (the correction to an approximate idempotent \(f\) is \(-(2f-1)(f^2-f)\) modulo a square-zero ideal). An element is invertible in \(A\) exactly when its image is invertible in \(A/J\): the inverse modulo \(J\) can be corrected by finite geometric series in the nilpotent ideal. Therefore \(a-v\) is a unit precisely when \(a_i-\epsilon_i\ne0\) for every simple factor, where \(\epsilon_i\) is the image of \(v\) in \(F_i\).

**2. Classifying involution lifts.** For odd characteristic, every \(\epsilon_i\) is \(+1\) or \(-1\). Fix a sign vector \(\epsilon\) and let \(D_\epsilon=\sum_i\epsilon_i e_i\). Every involution \(v\) with residue \(\epsilon\) is conjugate to \(D_\epsilon\) by an element of \(1+J\). Indeed, set \(p=(1+v)/2\), \(p_0=(1+D_\epsilon)/2\); these are idempotents congruent modulo \(J\). The element \(g=pp_0+(1-p)(1-p_0)\) is congruent to \(1\) modulo \(J\), hence invertible, and satisfies \(gp_0=pg\). Consequently \(v=gD_\epsilon g^{-1}\).

**3. Orbit cardinality.** The group \(1+J\) has \(q^{\dim J}\) elements. Its stabilizer at \(D_\epsilon\) consists of \(1+j\) with \(jD_\epsilon=D_\epsilon j\). Using the direct Peirce decomposition \(J=\bigoplus_{i,j}e_iJe_j\), commutation reads \((\epsilon_i-\epsilon_j)e_i j e_j=0\). Because \(2\) is invertible, exactly the same-sign components survive. Orbit–stabilizer therefore yields
\[
\#\{v:v^2=1,\ \overline v=\epsilon\}=q^{\sum_{i<j}w_{ij}\mathbf1_{\epsilon_i\ne\epsilon_j}}.\tag{2}
\]
Combining (2) with unit detection in Step 1 gives (1). At every coordinate at least one of the distinct signs \(+1,-1\) differs from \(a_i\), so the sum is nonempty and \(N(a)>0\).

**4. Exact reconstruction.** For a subset \(S\subseteq\{1,\ldots,t\}\), take \(\epsilon^S_i=+1\) on \(S\) and \(-1\) outside. Put \(a^S=-D_{\epsilon^S}\) and \(N_S=N(a^S)\). Every coordinate of \(\overline{a^S}\) forbids precisely the sign opposite to \(\epsilon^S_i\), leaving a single admissible sign vector. Thus
\[
N_S=q^{c(S)},\qquad c(S)=\sum_{\substack{i\in S\\j\notin S}}w_{ij}.
\]
Writing \(N_i=N_{\{i\}}\) and \(N_{ij}=N_{\{i,j\}}\), the cut identities give
\[
\boxed{\ \frac{N_iN_j}{N_{ij}}=q^{2w_{ij}}\ },\quad i\ne j.\tag{3}
\]
Each weight is therefore the uniquely determined nonnegative integer exponent obtained from (3), divided by two. This recovers every labelled edge multiplicity using only singleton and doubleton forced-sign fibres.

**5. Sharp limits and a nonreconstruction pair.** Every term in (1) is positive. Hence \(N(a)\) is maximized exactly when no quotient coordinate equals \(+1\) or \(-1\), in which case \(N(a)=\sum_S q^{c(S)}\), an antiferromagnetic cut partition function. Its minimum is \(1\), attained exactly when every quotient coordinate is \(\pm1\) and the resulting forced signs are constant on each connected component of the positive-weight graph.

Let \(B\) and \(C\) be radical-square-zero path algebras of the oriented quivers \(1\to2\to3\) and \(1\leftarrow2\to3\), respectively (all paths of length at least two killed), over the same odd finite field. Both have \(A/J\cong\mathbb F_q^3\) and edge weights \(w_{12}=w_{23}=1\), \(w_{13}=0\). Formula (1) gives identical labelled quotient-fibre counts and the same full multiplicity histogram, because each quotient fibre has \(q^2\) elements in either algebra. Yet the ordinary quivers have different source/sink-degree types, even after reversal, so these algebras are neither isomorphic nor anti-isomorphic. The graph reconstruction is therefore strictly weaker than reconstructing the algebra.

In characteristic two, every involution maps to \((1,\ldots,1)\) in the quotient, since \(x^2=1\) has the unique solution \(1\) in every characteristic-two field. For \(a=1\), the difference \(a-v\) then has zero quotient coordinates and cannot be a unit, proving the stated boundary.

## Verification
The accompanying `verify.py` uses only Python's standard library. It constructs exact finite-field matrix-unit multiplication tables, enumerates all elements and all involutions, counts each unit-plus-involution fibre directly, and compares with (1). Five exhaustive cases were checked: \(T_3(\mathbb F_3)\) (729 elements, 56 involutions), \(T_2(\mathbb F_5)\) (125 elements, 12 involutions), and three five-dimensional radical-square-zero quiver algebras over \(\mathbb F_3\) (243 elements and 32 involutions each). The verifier returned `VERIFY_OK`. These finite checks test the algebraic formula; the proof above is uniform for every admissible finite-dimensional algebra.

For \(T_n(\mathbb F_q)\), \(w_{ij}=1\) for all distinct vertices, so (1) specializes to
\[
N(a)=\sum_{r=0}^{c}\binom cr q^{(b+r)(n-b-r)},
\]
where \(b\) is the number of diagonal entries of \(a\) equal to \(-1\), \(c\) is the number different from both \(\pm1\), and the remaining \(n-b-c\) entries equal \(+1\). For any finite poset, the incidence-algebra specialization replaces the exponent by the size of the sign cut in its comparability graph.

## Relationship to prior work
Ansari and Hakami (2026) analyze coefficient data, diagonal idempotents, and inner conjugation in incidence algebras through local higher derivations, providing a recent structural setting for reconstruction questions. Kirova's 2026 expanded note studies existence of unit-plus-involution decompositions in formal matrix rings (and explicitly acknowledges a related Russian conference publication from 2019), but does not give decomposition-fibre multiplicities or a radical-graph reconstruction theorem. Gargate and Gargate (2019) study and enumerate involutions in incidence algebras, including fixed-diagonal families; that component of the counting mechanism is established background and is not claimed as novel here. The new claim combines the *unit-constrained* exact fibres across all algebras with field-product semisimple quotient with the inverse recovery (3) and its sharp orientation limitation.

## Limitations
The semisimple quotient must be a product of finite fields; matrix simple factors are not covered. The characteristic must be odd for (1). The graph detected is the **symmetrized total radical Peirce-dimension graph**, not the oriented Gabriel quiver or the algebra multiplication. The proof and tests do not claim independent formal certification. While targeted comparisons did not identify the full fibre-and-reconstruction theorem, an unindexed equivalent use of idempotent lifting and cut functions remains a bibliographic risk.

## References
1. M. A. Ansari and K. H. Hakami, *Anchored weak 2-local Hasse–Schmidt derivations on incidence algebras*, Journal of Taibah University for Science, published online July 22, 2026. DOI: 10.1080/16583655.2026.2705030.
2. V. Kirova, *Formal Matrix Rings with the Involution Property*, arXiv:2610.04709v1, October 3, 2026. Expanded translation acknowledging 2019 Russian predecessor.
3. I. Gargate and M. Gargate, *Involutions on Incidence Algebras of Finite Posets*, arXiv:1907.06805v1, July 16, 2019.
4. Standard nilpotent-ideal idempotent lifting and unit lifting are proved in the relevant special form in the proof above.
