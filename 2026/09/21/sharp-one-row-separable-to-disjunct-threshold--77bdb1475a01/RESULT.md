# Exact one-row frontier from separability to disjunctness

## Statement

For an integer \(s\ge2\), let \(G(s)\) be the largest integer \(k\) with the following property: every binary matrix with more than \(s\) columns that is exactly \(s\)-separable can be made \(k\)-disjunct by appending at most one binary row.

Then
\[
\boxed{G(s)=\left\lfloor\frac{s}{2}\right\rfloor\qquad(s\ge2).}
\]

Thus the Chen--Hwang conversion theorem is quantitatively sharp in the worst case: exact \(2d\)-separability guarantees a \(d\)-disjunct matrix after at most one added row, and no larger disjunctness parameter can be guaranteed from exact separability of a given order.

The sharpness is witnessed by an explicit family. For every integer \(d\ge2\), there is a binary matrix \(M_d\) with \(2d+1\) columns and \(4d-2\) rows such that
\[
M_d\text{ is exactly }(2d-1)\text{-separable},
\qquad
\boxed{a_d(M_d)=2},
\]
where \(a_d(M)\) is the minimum number of additional binary rows needed to make \(M\) \(d\)-disjunct.

Because every \(\overline{d+1}\)-separable matrix is \(d\)-disjunct, the same family also obstructs any universal one-row upgrade from exact \((2d-1)\)-separability to \(\overline{d+1}\)-separability.

## Definitions

For a set \(S\) of columns, write \(B(S)\) for their Boolean sum (coordinatewise OR).

- \(M\) is exactly \(k\)-separable if \(B(S)\ne B(T)\) for every two distinct \(k\)-sets \(S,T\) of columns.
- \(M\) is \(d\)-disjunct if no column is contained coordinatewise in the Boolean sum of any \(d\) other columns.
- \(M\) is \(\overline{k}\)-separable if all Boolean sums of at most \(k\) columns are distinct.

These are the conventions used in the Chen--Hwang result.

## A monotonicity lemma

If a binary matrix with \(n>s\) columns is exactly \(s\)-separable, then it is exactly \(t\)-separable for every \(1\le t<s\). This standard monotonicity can be seen directly. Suppose distinct \(t\)-sets \(A,B\) have the same Boolean sum, and put \(u=|A\setminus B|=|B\setminus A|\ge1\).

If \(u>s-t\), enlarge \(A\) by \(s-t\) columns from \(B\setminus A\), and enlarge \(B\) symmetrically by \(s-t\) columns from \(A\setminus B\). The two resulting \(s\)-sets are distinct and have the same Boolean sum.

If \(u\le s-t\), add \(u-1\) columns from \(B\setminus A\) to \(A\), add \(u-1\) columns from \(A\setminus B\) to \(B\), and then add the same \(s-t-u+1\) columns from outside \(A\cup B\) to both. Such outside columns exist because \(n>s\). Again the resulting distinct \(s\)-sets have the same Boolean sum, a contradiction.

## Construction of the sharpness family

Fix \(d\ge2\). The columns are
\[
C,\ C',\ A_1,\ldots,A_d,\ D_1,\ldots,D_{d-1}.
\]
Call the \(A_i\) and \(D_j\) columns *ordinary*.

The rows are the following \(4d-2\) incidence rows:

1. for each ordinary column \(Z\), one private row \(p_Z\) supported exactly on \(\{Z\}\);
2. for each \(1\le i\le d\), one row \(q_i\) supported exactly on \(\{C,A_i\}\);
3. for each \(1\le j\le d-1\), one row \(r_j\) supported exactly on \(\{C',D_j\}\).

There are \((2d-1)+d+(d-1)=4d-2\) rows.

## Exact \((2d-1)\)-separability

There are \(2d+1\) columns, so every \((2d-1)\)-set is the complement of a unique omitted pair \(P=\{X,Y\}\). It suffices to recover \(P\) from the Boolean sum of all non-omitted columns.

For every ordinary column \(Z\), its private row \(p_Z\) is absent from this Boolean sum exactly when \(Z\in P\). Hence the Boolean sum determines the ordinary part of \(P\).

- If two ordinary columns are omitted, the pair is already determined.
- If no ordinary column is omitted, then necessarily \(P=\{C,C'\}\).
- If exactly one ordinary column is omitted and it is \(A_i\), then row \(q_i\) is absent for \(\{C,A_i\}\) and present for \(\{C',A_i\}\), because \(C\) remains in the latter case.
- If exactly one ordinary column is omitted and it is \(D_j\), then row \(r_j\) is absent for \(\{C',D_j\}\) and present for \(\{C,D_j\}\), because \(C'\) remains in the latter case.

Thus distinct omitted pairs give distinct Boolean sums, so \(M_d\) is exactly \((2d-1)\)-separable.

## Why one additional row cannot suffice

In \(M_d\), every 1-entry of \(C\) lies in one of the rows \(q_i\), and row \(q_i\) also contains \(A_i\). Hence
\[
C\subseteq B(\{A_1,\ldots,A_d\}).
\]
If an appended row has entries \(x_Z\) in column \(Z\), breaking this particular \(d\)-cover requires
\[
x_C=1,
\qquad
x_{A_1}=\cdots=x_{A_d}=0.
\tag{1}
\]

Likewise every 1-entry of \(C'\) lies in one of the rows \(r_j\), and row \(r_j\) also contains \(D_j\). Therefore
\[
C'\subseteq B(\{C,D_1,\ldots,D_{d-1}\}),
\]
where the set on the right has exactly \(d\) columns. Breaking this cover with the same appended row requires
\[
x_{C'}=1,
\qquad
x_C=x_{D_1}=\cdots=x_{D_{d-1}}=0.
\tag{2}
\]

Conditions (1) and (2) force both \(x_C=1\) and \(x_C=0\), a contradiction. Thus
\[
a_d(M_d)\ge2.
\]

## Two rows do suffice

Append one row supported only on \(C\), and a second row supported only on \(C'\). Every ordinary column already has its private row \(p_Z\). After the two additions every column has a private row, so no column can be covered by the Boolean sum of any collection of other columns. In particular the enlarged matrix is \(d\)-disjunct. Hence
\[
a_d(M_d)\le2.
\]
Therefore \(a_d(M_d)=2\).

## Exact one-row frontier

Let \(s\ge2\), and put \(k=\lfloor s/2\rfloor\). By the monotonicity lemma, every exactly \(s\)-separable matrix is exactly \(2k\)-separable. The Chen--Hwang theorem therefore makes it \(k\)-disjunct after at most one appended row. Hence
\[
G(s)\ge\left\lfloor\frac{s}{2}\right\rfloor.
\]

For the reverse inequality, first let \(s=2d-1\) be odd. The matrix \(M_d\) is exactly \(s\)-separable but cannot be made \(d=(s+1)/2\)-disjunct with one row. Thus \(G(s)\le d-1=\lfloor s/2\rfloor\).

Now let \(s=2d\) be even. Apply the construction with parameter \(d+1\). The matrix \(M_{d+1}\) is exactly \((2d+1)\)-separable, hence by monotonicity is exactly \(2d=s\)-separable, but it cannot be made \((d+1)\)-disjunct with one row. Thus \(G(s)\le d=\lfloor s/2\rfloor\).

Combining both directions proves
\[
\boxed{G(s)=\left\lfloor\frac{s}{2}\right\rfloor.}
\]

## Relation to prior work

Chen and Hwang proved that exact \(2d\)-separability always permits a \(d\)-disjunct matrix after adding at most one row. Their paper explicitly described the separable-to-disjunct link as quantitatively weaker than desired and invited stronger connections. The result above determines the exact worst-case one-row frontier: without additional hypotheses, the guaranteed disjunctness parameter from exact \(s\)-separability is precisely \(\lfloor s/2\rfloor\).

The 2009 error-tolerant extension by Chen, Cheng, He and Zhong develops a noisy analogue of the separable-to-disjunct transformation. Aldridge, Baldassini and Gunderson later restated the Chen--Hwang \(2k\)-separable-to-\(k\)-disjunct one-row theorem when discussing the asymptotic relation between separability and disjunctness. Recent cover-free-family and group-testing literature continues to use exact separability and disjunctness as distinct recovery notions.

Searches covered the matrix, set-system and coding terminology: exact separable matrices, union-free families, disjunct matrices, cover-free families, superimposed codes, one-row/one-test augmentation, the parameter phrases \(2d-1\) and \(2d\), and the Chen--Hwang title and DOI. No source located states this sharpness family or the exact one-row frontier above. Originality is therefore asserted only to the best of our knowledge.

## Reproducibility

`artifacts/verify.py` constructs \(M_d\), checks exact \((2d-1)\)-separability, exhaustively tests all possible single appended rows for \(d=2,\ldots,6\), and verifies an explicit two-row \(d\)-disjunct completion. `artifacts/verification.txt` records the verified output. These finite checks supplement, but do not replace, the general proof.

## Limitations

The result concerns noiseless binary matrices and one-row augmentation. It does not optimize the row count of the witness matrices, classify all extremal examples, or address error-tolerant variants. The frontier is a worst-case statement over exact separability; additional structural hypotheses may permit stronger conversions.

## References

1. H.-B. Chen and F. K. Hwang, “Exploring the missing link among d-separable, d-bar-separable and d-disjunct matrices,” *Discrete Applied Mathematics* 155 (2007), 662–664. DOI: https://doi.org/10.1016/j.dam.2006.10.009.
2. H.-B. Chen, Y. Cheng, Q. He, and C. Zhong, “Transforming an error-tolerant separable matrix to an error-tolerant disjunct matrix,” *Discrete Applied Mathematics* 157 (2009), 387–390. DOI: https://doi.org/10.1016/j.dam.2008.06.004.
3. M. Aldridge, L. Baldassini, and K. Gunderson, “Almost separable matrices,” *Journal of Combinatorial Optimization* 33 (2017), 215–236. DOI: https://doi.org/10.1007/s10878-015-9951-1.
4. T. B. Idalino and L. Moura, “A Survey of Cover-Free Families: Constructions, Applications, and Generalizations,” in *New Advances in Designs, Codes and Cryptography* (2023/2024), 195–239. DOI: https://doi.org/10.1007/978-3-031-48679-1_11.
5. T. B. Idalino and L. Moura, “Cover-free families on hypergraphs and combinatorial group testing,” *Journal of Combinatorial Optimization* 51 (2026), article 55. DOI: https://doi.org/10.1007/s10878-026-01429-0.
