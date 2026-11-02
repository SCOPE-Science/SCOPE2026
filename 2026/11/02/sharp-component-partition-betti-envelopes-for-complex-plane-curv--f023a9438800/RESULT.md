# Sharp component-partition Betti envelopes for complex plane curves

## Finding

For a possibly singular reduced complex projective plane curve, the total rational topological Betti number admits a **sharp bound fixed by the degrees of its irreducible components**, with an exact sum of local nonnegative defects and a complete equality classification. These bounds determine both the finite-degree supremum over the entire linear system and the maximum among reducible curves. In contrast to asymptotic leading-coefficient results, this resolves every degree, including the exceptional transitions at degrees \(2\), \(3\), \(4\) and \(5\).

Write \(C=C_1\cup\cdots\cup C_r\subset\mathbb P^2_{\mathbb C}\), with distinct irreducible components of degrees \(d_i\ge1\) and total degree \(d=\sum_i d_i\). Define
\[
 b_*(C)=\sum_{j=0}^2\dim_{\mathbb Q}H_j(C^{\rm an},\mathbb Q),\qquad
 B(d_1,\ldots,d_r)=2+\sum_{i=1}^r(d_i-1)(d_i-2)+\sum_{i<j}d_i d_j.
\]
Then \(b_*(C)\le B(d_1,\ldots,d_r)\), with equality if and only if every component is smooth, every pair of meeting components intersects transversely, and no three distinct components meet at one point. Such curves exist for every degree partition.

More precisely, at every point \(p\) let \(k_p\) count globally distinct components passing through \(p\). Let \(\mu_p(C_i)\) be the Milnor number of the reduced local analytic equation of \(C_i\) at \(p\), defined as zero at its smooth points, and let \(I_p(C_i,C_j)\) be the usual local intersection multiplicity (zero if either component misses \(p\)). Then
\[
 B(d_1,\ldots,d_r)-b_*(C)
 =\sum_i\sum_{p\in\operatorname{Sing}(C_i)}\mu_p(C_i)
 +\sum_{p:k_p\ge2}\left(\sum_{i<j}I_p(C_i,C_j)-(k_p-1)\right).
\]
Each displayed local summand is a nonnegative integer; in particular this identifies **every source of strictness**.

Among reduced curves with fixed total degree \(d\) and exactly \(r\) irreducible components, where \(1\le r\le d\),
\[
 \max b_*=B_{d,r}=d^2-dr-2d+\frac{r(r+3)}2+2.
\]
The maximizing degree partition is uniquely \((d-r+1,1,\ldots,1)\), up to order, and the maximal curves are precisely simple-normal-crossings unions of a smooth degree-\(d-r+1\) curve with \(r-1\) lines. When \(r=1\), this says that the sole extremizers are smooth curves.

Allowing **all** degree-\(d\) effective divisors, including nonreduced ones, does not change the following sharp total maxima:
\[
 M(d)=\begin{cases}2,&d=1,\\3,&d=2,\\5,&d=3,\\d^2-3d+4,&d\ge4.\end{cases}
\]
The degree-\(2\) and degree-\(3\) extremizers are unions of respectively two and three lines without threefold concurrency. For degree \(4\), the extremizers are smooth quartics and four lines with no triple point. For every \(d\ge5\), precisely the smooth irreducible degree-\(d\) curves maximize.

Among reduced **reducible** curves of degree \(d\ge5\),
\[
 \max b_*=d^2-4d+7.
\]
In degree \(5\), equality occurs for a smooth quartic plus a transverse line, or five lines in general position. For every \(d\ge6\), equality holds exactly for a smooth degree-\(d-1\) curve plus a line meeting it transversely. Thus, for \(d\ge6\), the strict inequality \(b_*(C)>d^2-4d+7\) is a sharp topological certificate that a degree-\(d\) divisor is reduced and irreducible.

## Assumptions and scope

All curves are effective Cartier divisors of positive degree in the ordinary complex projective plane. Homology is singular homology of the underlying analytic topology with rational coefficients; nonreduced structures contribute only via their reduced support. The partition-sensitive formula assumes the support is reduced and decomposes into **geometrically irreducible** components (automatic for complex irreducible curves). No assumption of nodes, simple normal crossings, or genericity is made **before** the equality condition.

## Proof

**Step 1: normalization and topological Betti numbers.** Any positive-degree irreducible plane curves meet by Bézout, so \(C\) is connected. Let \(\widetilde C_i\) be the normalization of \(C_i\), with genus \(g_i\). At \(p\) let \(b_{i,p}\) be the number of analytic branches of \(C_i\), interpreted as zero if \(p\notin C_i\), and \(b_p=\sum_i b_{i,p}\). Gluing normalization preimages identifies \(b_p\) points to one, lowering the topological Euler characteristic by \(b_p-1\). Therefore
\[
 \chi(C)=2r-2\sum_i g_i-\sum_{p\in\operatorname{Sing}(C)}(b_p-1).
\]
Here \(b_0(C)=1\), \(b_2(C)=r\), and all higher Betti numbers vanish, giving
\[
 b_*(C)=2+2\sum_i g_i+\sum_{p\in\operatorname{Sing}(C)}(b_p-1).
\]
Only finitely many points contribute to the sums.

**Step 2: exact local defect.** The arithmetic genus of an irreducible plane degree-\(d_i\) curve is \(p_a(C_i)=(d_i-1)(d_i-2)/2\). The normalization formula gives \(g_i=p_a(C_i)-\sum_p\delta_p(C_i)\), where \(\delta_p\) is the local delta invariant. The Milnor formula for a reduced plane curve germ is
\[
 \mu_p(C_i)=2\delta_p(C_i)-b_{i,p}+1
\]
when \(p\in C_i\). For \(p\) lying on \(k_p\) distinct global components,
\[
 b_p-1=\sum_{i:p\in C_i}(b_{i,p}-1)+(k_p-1).
\]
Using Bézout's identity \(\sum_pI_p(C_i,C_j)=d_id_j\) for each pair of distinct irreducible components, substitution yields **exactly**
\[
 B(d_1,\ldots,d_r)-b_*(C)=\sum_i\sum_{p\in\operatorname{Sing}(C_i)}\mu_p(C_i)
 +\sum_{p:k_p\ge2}\bigl(\sum_{i<j}I_p(C_i,C_j)-(k_p-1)\bigr).
\]
For each \(p\), if \(k_p\ge2\), every pair of distinct components contributes at least one to its local intersection number, whence
\[
 \sum_{i<j}I_p(C_i,C_j)\ge\binom{k_p}{2}\ge k_p-1.
\]
Equality in the second inequality holds exactly when \(k_p=2\) (or \(k_p\le1\)), and equality in the first then requires transverse local intersection multiplicity one. Every non-smooth reduced plane germ has positive Milnor number. Therefore the defect vanishes globally precisely for smooth components meeting pairwise transversely with no triple points. General components of the prescribed degrees can be chosen to satisfy this by Bertini and avoidance of finitely many intersection points. This proves sharpness for **every** partition, including \(r=1\).

**Step 3: fixed component count.** Expand the partition bound using \(\sum_i d_i=d\):
\[
 B(d_1,\ldots,d_r)=2+\tfrac12(d^2+\sum_i d_i^2)-3d+2r.
\]
For fixed \(d,r\), the sum of squares of positive integral component degrees is uniquely maximal for \((d-r+1,1,\ldots,1)\): whenever two degrees exceed one, transferring one degree unit from the smaller to the larger strictly increases the sum. Substitution gives \(B_{d,r}\) as stated, and the equality characterization follows from Step 2.

**Step 4: global and reducible extrema.** As a function of \(r\),
\[
 B_{d,r}=d^2-dr-2d+\frac{r^2+3r}{2}+2
\]
is strictly convex. For \(2\le r\le d\), its maximum therefore occurs at \(r=2\) or \(r=d\). Their values are \(d^2-4d+7\) and \(2+\binom d2\), respectively, and their difference is \((d-5)(d-2)/2\). Including the \(r=1\) value \(d^2-3d+4\) proves the piecewise maxima and all equality cases, using strict convexity to rule out other component counts. In particular, the exceptional reducible tie at \(d=5\) is exact.

A nonreduced degree-\(d\) divisor has support of degree \(t<d\) and the same topological Betti numbers as that support. The already-established sequence \(M(1)=2,M(2)=3,M(3)=5,M(4)=8\) and \(M(t)=t^2-3t+4\) for \(t\ge4\) is strictly increasing in \(t\). Therefore no nonreduced divisor maximizes at its nominal degree, and the irreducibility certificate follows.

## Verification

The accompanying standalone Python program independently enumerates all unordered degree partitions through degree \(12\), checking the two algebraically independent expressions for their sharp partition bounds, their unique fixed-component-count maximizers, and the exceptional global and reducible cases. It is a finite consistency check; the proofs above establish the result for arbitrary degree. Additional manual checks: a nodal irreducible cubic has total Betti number \(3\) and one Milnor defect, versus \(4\) for a smooth cubic; three nonconcurrent lines have total Betti number \(5\); four nonconcurrent lines have \(8\); a smooth quartic and transverse line have \(12\), tying five general lines in degree \(5\).

## Relationship to prior work

Ancona–Cao (2026, arXiv:2610.24134v1, first posted 2026-10-16) introduce the asymptotic total-Betti invariant \(\beta(L)\) and prove its equality with volume for ample line bundles and projective surfaces. Their Sections 1–3 treat the limiting normalized supremum and related birational/volume properties, not the partition-stratified exact **finite-degree** maximum or its equality geometry in \(\mathbb P^2\). Pan–Zhang–Zhang (2026, arXiv:2601.20179v1, first posted 2026-01-28), especially Sections 1 and 6, obtain general asymptotic Betti upper bounds \(d^n+O(d^{n-1})\) on locally complete intersections and do not state the present exact polynomial, local defect decomposition, or degree-\(4\)/\(5\) equality transitions. The arithmetic-genus, Milnor/delta and Bézout ingredients are classical; only their combined sharp finite-degree envelope/equality classification is advanced here as a candidate new statement, not the ingredients themselves.

## Limitations

This is a complex dimension-one statement in the ordinary projective plane, not a universal topological Betti extremality result for divisors on arbitrary surfaces, finite fields, or higher-dimensional hypersurfaces. The computation uses rational Betti numbers, not free-resolution Betti tables. The claimed originality is a best-knowledge comparison, not a historical-priority certificate: an equivalent elementary formulation may exist in classical curve literature. Independent mathematical review has not been performed.

## References

1. M. Ancona and J. Cao, *Invariants of big classes from asymptotic total Betti numbers*, arXiv:2610.24134v1 (2026-10-16), https://arxiv.org/html/2610.24134v1 .
2. X. Pan, D. Zhang, and X. Zhang, *Asymptotic Betti bounds for hypersurfaces in a singular variety*, arXiv:2601.20179v1 (2026-01-28), https://arxiv.org/html/2601.20179v1 .
3. Classical genus-degree formula, normalization-delta formula, local Milnor number identity, and Bézout's theorem; standard facts used explicitly in the proof.
