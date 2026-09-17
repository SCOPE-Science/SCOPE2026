# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

**PASS.**

Aoki's Theorem 6.5 expresses the global dimension as the maximum saturated-pair weight
\[
\bar\omega(S,C)=|\operatorname{Max}(C\setminus S)|+|\operatorname{Min}(S\setminus C)|.
\]
For a saturated pair of weight \(n-1\), partitioning \(P\) into
\(A=C\setminus S\), \(B=S\setminus C\), \(D=S\cap C\), and
\(E=P\setminus(S\cup C)\), and measuring the failures of \(A\) to be all maximal and \(B\) to be all minimal, gives the exact nonnegative identity
\[
|D|+|E|+\bigl(|A|-|\operatorname{Max}A|\bigr)
+\bigl(|B|-|\operatorname{Min}B|\bigr)=1.
\]
The four possible locations of the unit defect are exhaustive. They give, respectively, a double star; a connected three-element poset (again a double star); \(K_{2,n-2}\); and its dual \(K_{n-2,2}\). The interval, relative-downset, relative-upset, and extremal-boundary conditions rule out all additional comparabilities in these cases.

For each listed family, an explicit saturated pair of weight \(n-1\) is exhibited. Hence Aoki's formula proves the converse. Corollary 6.7 then gives the equivalent interval-resolution statement. The counting corollary follows by distinguishing the numbers of minimal and maximal elements and accounting for the low-order overlaps among the families.

No empirical calculation is used in place of the proof.

## Originality

**PASS, to the best of our knowledge.**

Aoki's arXiv:2609.15927v1 proves the bound \(\operatorname{gldim}\Lambda_P\le |P|-1\) and demonstrates sharpness using a one-sided star. The inspected text does not classify equality cases. It also gives the saturated-pair formula and the relative Auslander relation needed for the present classification.

Targeted searches for equality/extremal classifications for interval endomorphism global dimension and interval-resolution global dimension found Aoki's 2026 preprint and the earlier interval-resolution literature, but no matching maximum-case classification. The 2025 paper of Aoki--Escolar--Tada gives a complete classification at the opposite endpoint, interval-resolution global dimension zero, rather than at the new maximum \(|P|-3\).

### Residual literature risk

The main source is a very recent v1 preprint, so a concurrent revision or independent consequence of its saturated-pair formula is a realistic residual risk. No specific inaccessible paper was identified as especially likely to contain this exact equality characterization. The search is not claimed to exhaust unpublished notes or all equivalent formulations.

## Value

**PASS.**

The result upgrades a sharpness example for a new homological bound to a complete structural classification of every equality case. It also transfers immediately to the maximum interval-resolution global dimension and gives a closed count of extremal isomorphism types: 3 for \(n=3\), 5 for \(n=4\), and \(n+2\) for \(n\ge5\). The classification isolates two mechanisms for extremality: a single overlap point between the two extremal intervals, or a single failure of maximality/minimality producing a complete height-two bipartite poset.

## Scope of the claim

No novelty is claimed for Aoki's saturated-pair formula, the upper bounds, the relative Auslander formula, or the earlier theory of interval resolutions. The claimed contribution is the complete equality classification and its enumeration.
