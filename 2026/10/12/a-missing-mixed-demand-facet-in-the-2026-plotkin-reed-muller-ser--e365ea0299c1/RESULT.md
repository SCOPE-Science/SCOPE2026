# A missing mixed-demand facet in the 2026 Plotkin Reed–Muller service-rate region
## Finding

For the recursive first-order binary Reed--Muller generator \(G_m\) used by Choudhary and Bhaintwal, the displayed full service-rate region for \(m\ge3\) is missing a mixed-demand facet.

With the source's message ordering, the exact region is
\[
\Lambda(G_m)
=
\left\{
\lambda\in\mathbb R_{\ge0}^{m+1}:
\sum_{i=1}^{m+1}\lambda_i\le2^{m-1},
\quad
3\lambda_1+2\sum_{i=2}^{m+1}\lambda_i\le2^m+2
\right\}.
\]

The October 2026 source instead lists the coordinate maxima
\[
\lambda_1\le\frac{2^m+2}{3},
\qquad
\lambda_i\le2^{m-1}\quad(2\le i\le m+1),
\]
together with subset-sum inequalities bounded by \(2^{m-1}\). Those conditions do not imply the mixed facet above.

Indeed, define
\[
a=\frac{2^m+2}{3},
\qquad
b=2^{m-1}-a=\frac{2^m-4}{6}.
\]
For every \(m\ge3\), \(b>0\), and
\[
\lambda=(a,b,0,\ldots,0)
\]
satisfies every displayed coordinate and subset-sum condition in the 2026 source because
\[
a+b=2^{m-1}.
\]
But
\[
3a+2b
=
2^m+2+2b
>
2^m+2,
\]
so the vector is infeasible. At \(m=3\), this gives the concrete excluded vector
\[
(10/3,2/3,0,0).
\]

The corrected formula is not a new characterization of first-order Reed--Muller service regions: it is exactly the 2020 theorem of Kazemi, Kurz, and Soljanin after the generator coordinates are relabeled. The new point here is the explicit correction of the 2026 Plotkin-recursive application and the uniform counterexample to its displayed region.

## Assumptions and scope

All server capacities are one, as in both cited service-rate formulations. A recovery set for information object \(i\) is a subset of columns whose binary sum equals the unit vector \(e_i\). A feasible request vector is realized by nonnegative flow on recovery sets subject to unit capacity at every server.

The recursive generator in the 2026 source starts from
\[
G_1=
\begin{pmatrix}
1&1\\
0&1
\end{pmatrix}
\]
and applies the first-order Reed--Muller Plotkin recursion. Inductively, the columns of \(G_m\) are precisely
\[
(1,x_1,\ldots,x_m)^T,
\qquad
x\in\mathbb F_2^m.
\]
Thus \(G_m\), after moving the constant row to the final message coordinate and permuting columns, is the non-systematic generator used in Kazemi--Kurz--Soljanin's exact first-order Reed--Muller theorem with their parameter \(k=m+1\).

This finding concerns the full service-rate-region statement for \(m\ge3\). The individual maximum service rates computed in the 2026 source remain consistent with the corrected region: the mixed facet gives \(\lambda_1\le(2^m+2)/3\), and the total-capacity facet gives \(\lambda_i\le2^{m-1}\) for the other objects.

## Proof

First, the generator equivalence transfers the exact 2020 theorem. For \(k\ge4\), Kazemi--Kurz--Soljanin prove that their non-systematic \(\mathrm{RM}_2(1,k-1)\) generator has service-rate region
\[
\sum_{i=1}^{k}\mu_i\le2^{k-2},
\qquad
\sum_{i=1}^{k-1}\mu_i+\frac32\mu_k-1\le2^{k-2}.
\]
The second inequality is equivalently
\[
2\sum_{i=1}^{k-1}\mu_i+3\mu_k\le2^{k-1}+2.
\]
Set \(k=m+1\) and relabel their distinguished constant-coordinate request \(\mu_k\) as \(\lambda_1\). This gives exactly
\[
\sum_{i=1}^{m+1}\lambda_i\le2^{m-1},
\qquad
3\lambda_1+2\sum_{i=2}^{m+1}\lambda_i\le2^m+2.
\]

There is also a direct capacity certificate for the missing facet that does not depend on the 2020 polytope derivation. The server whose column is \(e_1=(1,0,\ldots,0)^T\) receives weight \(3\); every other server receives weight \(1\). The total weighted capacity is
\[
3+(2^m-1)=2^m+2.
\]

Every column of \(G_m\) has first coordinate one. Therefore a recovery set for object \(1\) has odd cardinality. If it is a singleton, its sole column must be \(e_1\), so its weighted cost is \(3\). Otherwise its cardinality is at least \(3\), so its weighted cost is also at least \(3\).

For any object \(i\ge2\), a recovery set sums to \(e_i\), whose first coordinate is zero. Hence its cardinality is a positive even integer and is at least \(2\). Its weighted cost is therefore at least \(2\).

Multiply every server-capacity inequality by the corresponding server weight and sum. Each unit of object-\(1\) demand consumes weighted capacity at least \(3\), while each unit of every other demand consumes weighted capacity at least \(2\). Thus every feasible request vector satisfies
\[
3\lambda_1+2\sum_{i=2}^{m+1}\lambda_i\le2^m+2.
\]

Finally, take
\[
a=(2^m+2)/3,
\qquad
b=2^{m-1}-a.
\]
For \(m\ge3\), \(b=(2^m-4)/6>0\). The vector \((a,b,0,\ldots,0)\) obeys the 2026 coordinate caps and every subset-sum cap because its total demand is exactly \(2^{m-1}\), but it violates the proved weighted inequality by \(2b\). Hence the 2026 displayed full region is strictly too large for every \(m\ge3\).

## Verification

`artifacts/verify.py` uses only the Python standard library and performs three independent checks.

First, for \(m=3\) it reconstructs
\[
G_3=
\begin{pmatrix}
1&1&1&1&1&1&1&1\\
0&1&0&1&0&1&0&1\\
0&0&1&1&0&0&1&1\\
0&0&0&0&1&1&1&1
\end{pmatrix}
\]
and exhausts all nonempty subsets of the eight columns. It extracts every inclusion-minimal recovery set for each information object and verifies the weighted-cost certificate recovery set by recovery set.

Second, it certifies the exact \(m=3\) polytope from the two corrected facets. It verifies feasible recovery-set allocations for every nonzero vertex:
\[
(10/3,0,0,0),
\]
the three axis vertices with value \(4\), and the three mixed vertices with coordinates \((2,2)\) on object \(1\) and one other object. Convexity then gives the whole corrected region, while the two inequalities give the converse.

Third, for \(3\le m\le8\) it checks the recursive-column description and the uniform counterexample algebra exactly with rational arithmetic.

Successful replay prints `VERIFY_OK`.

## Relationship to prior work

Choudhary--Bhaintwal's October 2026 preprint develops recovery-set recursion for Plotkin-type codes and then states a full service-rate-region description for first-order Reed--Muller codes. Its individual service-rate maxima agree with established results, but the displayed simultaneous-demand region omits the mixed facet above.

Kazemi--Kurz--Soljanin already gave the exact service-rate region of the same non-systematic first-order Reed--Muller generator in 2020. Their theorem contains precisely the missing facet after a permutation of message coordinates. Thus the exact formula itself is prior work; the contribution here is identifying that the new recursive application conflicts with that theorem and giving a uniform family of request vectors that witnesses the conflict.

Ly--Soljanin--Lalitha's later Reed--Muller service-rate work also treats the same distributed-storage model and explicitly recognizes the earlier exact first-order characterization while developing bounds for broader Reed--Muller families. It does not rescue the enlarged 2026 region.

Focused searches by the October 2026 article identifier and title, together with correction, erratum, mixed-demand, and weighted-facet terminology, did not locate a public correction as of 5 October 2026.

## Limitations

The finding targets version 1 of the October 2026 preprint and its displayed full-region characterization. A later revision may repair that statement.

The exact corrected region is inherited from the 2020 theorem after an explicit generator equivalence; it is not claimed here as a newly discovered service-rate theorem. The independent weighted-capacity argument proves the missing inequality and the counterexample family, while exact achievability of the whole region uses the established 2020 theorem.

The finite exhaustive replay is only for \(m=3\). The all-\(m\) correction is proved symbolically from the generator structure and the cited theorem, not inferred from finite experiments.

## References

1. Priyanka Choudhary and Maheshanand Bhaintwal, *Recovery Set Structures and Service Rates of Codes Obtained by the Plotkin-type Construction*, arXiv:2610.01900v1, first public 1 October 2026.
2. Fatemeh Kazemi, Sascha Kurz, and Emina Soljanin, *A Geometric View of the Service Rates of Codes Problem and its Application to the Service Rate of the First Order Reed-Muller Codes*, arXiv:2001.09121v1, 24 January 2020; IEEE ISIT 2020, DOI 10.1109/ISIT44484.2020.9174345.
3. Hoang Ly, Emina Soljanin, and V. Lalitha, *On the Service Rate Region of Reed--Muller Codes*, arXiv:2501.13105; IEEE Transactions on Information Theory 72 (2026), 5525--5542, DOI 10.1109/TIT.2026.3681406.
