# Same-model scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.**

For \(k\ge1\), the proof uses the exact tree excess identity
\[
\sum_v(d(v)-1)=n-2.
\]
At most \(\lfloor(n-2)/(k+1)\rfloor\) vertices can have degree at least \(k+2\); all remaining vertices lie in the single degree window \(1,\ldots,k+1\). This proves the lower bound. The proposed extremal sequence spends the excess \(n-2\) on \(q\) vertices of degree \(k+2\) and, when necessary, one intermediate vertex of degree \(r+1\). Prüfer codes guarantee tree realizability. The only competing window can contain at most \(q+1\) vertices, and \(q+1\le n-q\), so equality follows.

For \(k=0\), the leaf identity
\[
n_1=2+\sum_{i\ge3}(i-2)n_i
\]
implies that if every degree occurs at most \(R\) times, then there are at most \(R-2\) vertices of degree at least \(3\), hence \(n\le3R-2\). The three residue-class degree profiles in RESULT.md satisfy the tree degree-sum condition and attain the resulting lower bound.

Boundary cases \(n=2\), \(n=3\), \(q=0\), and \(r=0\) have been checked explicitly. The construction remains valid when \(k\ge n-2\), where the formula correctly gives \(n\).

The standalone verifier exhausts tree degree multisets through order \(40\) and directly computes the window maximum. All tested cases agree with the theorem.

## Originality

**PASS, to the best of our knowledge.**

The lower-bound ingredients are prior work and are not claimed as new.

Caro--West (2009) was inspected in full. It introduces repetition number, gives the general average/minimum-degree bound, and proves only asymptotic sharpness for trees; its tree construction appears in Theorem 2.5 and does not state the exact fixed-order minimum for every order.

Caro--Lauri--Zarb (2019) was inspected in full. Its Theorem 3.1 gives the tree spread lower bound for \(k\ge1\), but the displayed sharpness construction uses only degrees \(1\) and \(k+2\), whose multiplicities solve
\[
n_1+n_{k+2}=n,\qquad n_1+(k+2)n_{k+2}=2n-2.
\]
Thus that construction applies when \((n-2)/(k+1)\) is integral. For \(k=0\), it states \(\operatorname{rep}(T)\ge\lceil n/3\rceil\) and gives sharpness only on a congruence class.

Caro--Škrekovski--Zarb (2026), arXiv:2609.19762, was also inspected. It develops refined general degree-spread bounds and focuses its class-specific application on maximal outerplanar graphs; no all-order tree extremal formula was found.

Searches using “repetition number of trees”, “degree repetition tree”, “spread of degrees trees”, “sp(T,k)”, exact ceiling/floor forms, tree degree sequences, and fixed-order minimum formulations did not locate an equivalent theorem.

No specific inaccessible paper was identified as especially likely to overturn originality. Residual risk remains from differently phrased older degree-sequence literature and very recent or unindexed parallel work.

## Value

**PASS.**

The result closes a natural fixed-order gap in a classical sparse graph class. It converts previously known lower bounds and congruence-restricted/asymptotic sharpness into exact formulas for every order and every window width. The extremal construction is explicit and structurally simple: all excess degree is packed into degree \(k+2\), with at most one residue-correcting intermediate degree.

For \(k=0\), the formula also gives the exact minimum repetition number of an \(n\)-vertex tree for every \(n\), strengthening the status from an asymptotic or congruence-class statement to a complete fixed-order extremal law.

## Limitations

- The theorem gives extremal values over trees but does not classify every extremal tree.
- The lower bounds themselves are substantially contained in prior work; the new claim is all-order exact attainment and the resulting fixed-order formulas.
- The finite verifier supports but does not replace the symbolic proof.
- Differently phrased older degree-sequence results or very recent unindexed work could weaken the originality assessment.
- Independent audit has not been performed.
