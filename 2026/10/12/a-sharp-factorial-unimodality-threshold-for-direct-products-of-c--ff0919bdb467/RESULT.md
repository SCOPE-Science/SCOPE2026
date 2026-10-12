# A sharp factorial unimodality threshold for direct products of complete graphs

## Finding
For integers \(a\ge5\) and \(r\ge2a+4\), let \(T^*(r,a)\) have vertex set \([a]\times[r]\), with distinct vertices adjacent exactly when both coordinates differ. Let \(p_k\) count its \(k\)-vertex general-position sets, where no three selected vertices lie on one shortest path. Then
\[
\boxed{(p_0,p_1,\ldots,p_r)\text{ is unimodal}\quad\Longleftrightarrow\quad r\ge R(a):=2a+2+\frac{(a+1)!}{a}.}
\]
The threshold is an integer. Every admissible \(r<R(a)\) has a specific strict descent followed by ascent:
\[p_a>p_{a+1}<p_{a+2}.\]
For every admissible \(r\), the coefficients strictly increase through degree \(a\). This is a sharp uniform phase classification in the displayed parameter range, not a claimed classification for all pairs.

## Assumptions and scope
All graphs are finite, simple, undirected. We use the coefficientwise definition of unimodality: a sequence is nondecreasing up to some index and nonincreasing thereafter. Set \(\binom nk=0\) when \(k\notin\{0,\ldots,n\}\), and \((r)_k=\prod_{j=0}^{k-1}(r-j)\). The 2024 founding study introduced these polynomials and asked which \(T^*(r,a)\) are unimodal. A 2026 paper corrected the enumerator and established other parameter cases. Its corrected coefficient formula is a *known premise*, not claimed as a new discovery here. The theorem concerns the subsequent sharp factorial decision boundary for \(a\ge5\) and \(r\ge2a+4\).

## Proof
**Coefficient characterization.** For \(a,r\ge3\), this graph has diameter two: nonadjacent distinct vertices share exactly one coordinate, and a third vertex differing in both coordinates supplies a path of length two. Therefore a vertex subset is in general position exactly when its induced graph is a disjoint union of cliques. For size at least three, such subsets are: single-row subsets; single-column subsets; cliques using distinct rows and columns; or three/four vertices of one two-by-two rectangle. To justify exhaustiveness, consider a nonadjacent pair sharing one row, say \((i,j),(i,\ell)\). A selected vertex outside that row must use column \(j\) or \(\ell\), or it would be adjacent to both endpoints and yield an induced three-vertex path. If such an outside vertex exists, assume by symmetry it is \((h,j)\), so \((i,\ell)\) is adjacent to \((h,j)\) whereas \((i,j)\) is adjacent to neither. An additional vertex in row \(i\) but another column would form an induced three-vertex path through \((h,j)\). An additional vertex outside row \(i\) and outside columns \(j,\ell\) would be adjacent to both original endpoints. An additional vertex in column \(j\) but in a third row would form a path through \((i,\ell)\); one in column \(\ell\) and a third row would form a path through \((h,j)\). Therefore every selected vertex lies in the two rows \(i,h\) and the two columns \(j,\ell\). The same argument holds with rows and columns interchanged. A rectangle induces two disjoint edges, so its subsets qualify. Counting the four disjoint types yields the corrected formula of Rather (2026):
\[
p_0=1,\quad p_1=ar,\quad p_2=\binom{ar}{2},\qquad
p_k=a\binom rk+r\binom ak+(r)_k\binom ak+\binom a2\binom r2\binom4k\quad(k\ge3).
\]
Write \(H=\binom a2\binom r2\), \(Q_k=(r)_k\binom ak\), and \(U_k=a\binom rk+r\binom ak+Q_k\). Thus \(p_3=U_3+4H\), \(p_4=U_4+H\), \(p_k=U_k\) for \(5\le k\le a\), and \(p_k=a\binom rk\) for \(k>a\).

**A strictly increasing initial segment.** Certainly \(p_0<p_1<p_2\). Also
\[
\frac{Q_3}{\binom{ar}{2}}=\frac{(a-1)(a-2)(r-1)(r-2)}{3(ar-1)}>1,
\]
because \((a-1)(a-2)\ge2a\) for \(a\ge5\) and \((r-1)(r-2)\ge2r\) for \(r\ge14\). Hence \(p_3>p_2\). For every integer \(3\le k<a\),
\[
\frac{Q_{k+1}}{Q_k}=\frac{(a-k)(r-k)}{k+1}\ge1+\frac5{k+1}.
\]
Indeed, setting \(t=a-k\ge1\) gives \((a-k)(r-k)-(k+1)\ge t(a+5+t)-a-1\ge5\). The row term \(a\binom rk\) strictly increases over these indices, while the column term can decrease by at most \(r\binom ak\). Consequently
\[
U_{k+1}-U_k>\binom ak\left(\frac{5(r)_k}{k+1}-r\right)>0,
\]
since \(k+1\le a\) and \(5(r-1)(r-2)>a\). We must separately absorb the exceptional rectangle correction at degrees three and four. As
\[
Q_4/Q_3\ge11/2,\quad Q_3/H=2(a-2)(r-2)/3\ge24,
\]
and \(r\binom a3<Q_3\), we get
\[
p_4-p_3\ge(Q_4-Q_3)-r\binom a3-3H>0.
\]
Similarly, \(Q_5/Q_4\ge2\), \(r\binom a4/Q_4\le1/(13\cdot12\cdot11)\), and \(H/Q_4\le1/132\), whence
\[
p_5-p_4\ge(Q_5-Q_4)-r\binom a4-H>0.
\]
Therefore \(p_0<p_1<\cdots<p_a\), including the endpoint case \(a=5\).

**The unique threshold comparison.** Since \(a\ge5\), the coefficients beyond degree \(a\) are simply \(a\binom rk\). They form a unimodal binomial tail, and \(p_{a+2}>p_{a+1}\) because \(r\ge2a+4\). Thus the full sequence is unimodal if and only if \(p_{a+1}\ge p_a\). Their exact difference is
\[
\frac{p_{a+1}-p_a}{(r)_a}
=\frac{a(r-2a-1)}{(a+1)a!}-1-\frac{r}{(r)_a}
=\frac{r-2a-1}{K}-1-\frac{1}{(r-1)(r-2)\cdots(r-a+1)},
\]
where \(K=(a+1)!/a\in\mathbb Z_{>0}\). The right side increases strictly with the integer \(r\). At \(r=2a+1+K\) it is negative. At the next integer \(r=2a+2+K\) it is positive: here \((r-1)\cdots(r-a+1)>K\). It follows that \(p_{a+1}\ge p_a\) exactly when \(r\ge2a+2+K\). Below this threshold, \(p_a>p_{a+1}<p_{a+2}\) precludes unimodality; at and above it, the initial increasing segment joins the unimodal binomial tail. This proves all assertions.

## Verification
An independent direct-geodesic subset enumerator compared the published formula against exhaustive subsets for six small complete-graph products, totaling 139,776 tested configurations. The accompanying stand-alone Python program also compared the exact coefficient polynomial and theorem's unimodality decision on 747 parameter pairs; it checked factorial-threshold transitions for \(5\le a\le11\). In particular the sign switches between \(r=155\) and \(r=156\) for \(a=5\), and between \(r=853\) and \(r=854\) for \(a=6\). Run `python verify.py` from a directory containing the packaged script; it needs only the Python standard library. These finite checks corroborate but do not replace the proof for all integers.

## Relationship to prior work
Iršič, Klavžar, Rus and Tuite (2024, Problem 5.2) explicitly ask for the unimodality parameters of \(T^*(r,a)\). Rather (2026, Theorem 5.3) supplies the **correct** coefficient formula used above and (Theorem 5.6; Corollary 5.7) settles the small-first-parameter cases and the \(a=3\) phase pattern. The present result does not claim the coefficient enumeration, the graph characterization or the already settled cases. Its contribution is the new explicit, sharp factorial threshold for every \(a\ge5\) in the structurally distinguished region \(r\ge2a+4\). A broader classification outside this region is not obtained.

## Limitations
The proof does not classify \(a\in\{1,2,3,4\}\) or the region \(r<2a+4\). It uses known 2026 enumeration as a premise, although the needed small-instance formula was independently stress-tested. Search and comparison with pertinent full-text studies do not establish absolute priority; obscure equivalent threshold statements might exist. There is no claim of independent validation beyond the stated reproducibility checks.

## References
1. V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, arXiv:2401.05696 (first posted 2024-01-11); Results in Mathematics 79, 110 (2024), DOI 10.1007/s00025-024-02133-3. Problem 5.2.
2. B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930 (first posted 2026-03-06), Theorems 5.3 and 5.6 and Corollary 5.7.
3. *The General Position Problem: A Survey*, arXiv:2501.19385, §2.3 (description of the correction and known unimodality results).
