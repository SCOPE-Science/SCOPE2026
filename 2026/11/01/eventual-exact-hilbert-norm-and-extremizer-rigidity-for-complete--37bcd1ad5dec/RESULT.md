# Eventual exact Hilbert norm and extremizer rigidity for complete-bipartite maximal averages

## Finding
Let \(m\ge2\) be an integer and \(n\ge N_m:=10^6(m+1)^6\) be another integer. On the unit-edge complete bipartite graph \(K_{m,n}\), let \(M\) be the centered Hardy–Littlewood maximal operator defined from counting-measure graph balls. Put
\[
\tau_{m,n}=1+\frac{mn+1}{(m+1)^2},\qquad
\Lambda_{m,n}=\frac{\tau_{m,n}+\sqrt{\tau_{m,n}^2-4/(m+1)^2}}{2}.
\]
The **exact attained strong Hilbert norm** is
\[
\boxed{\|M\|_{\ell^2\to\ell^2}^2=\Lambda_{m,n}.}
\]
Every nonzero extremizer, after taking absolute values, is a scalar multiple of the two-level vector that equals \(1\) at each of the \(m\) vertices in the smaller class and
\[
\boxed{c_{m,n}=\frac{m}{(m+1)^2\Lambda_{m,n}-1}}
\]
at each of the \(n\) vertices in the larger class; in particular \(0<c_{m,n}<1\). All independent coordinate signs are permitted. Moreover, for every fixed \(m\ge2\),
\[
\boxed{\Lambda_{m,n}=\frac{mn}{(m+1)^2}+1+\frac1{(m+1)^2}-\frac1{mn}+O_m(n^{-2})\quad(n\to\infty).}
\]
The explicit stabilization threshold is sufficient, not asserted to be optimal.

## Assumptions and scope
The vertex classes \(A\) and \(B\) have cardinalities \(m\) and \(n\), with \(m,n\ge2\), unit edge lengths and counting measure. For any real signal \(f\), write \(x_i=|f(i)|\) on \(A\), \(y_j=|f(j)|\) on \(B\), and \(X=\sum_i x_i\), \(Y=\sum_j y_j\), \(U=(X+Y)/(m+n)\). Because the graph has diameter two, its three centered ball averages are
\[
(Mf)(i)=\max\left\{x_i,\frac{x_i+Y}{n+1},U\right\}\quad(i\in A),\qquad
(Mf)(j)=\max\left\{y_j,\frac{y_j+X}{m+1},U\right\}\quad(j\in B).
\]
The norm is for real \(\ell^2\) with unweighted counting measure. Values of \(n\) below the stated threshold, and nonuniform vertex masses, are not classified by this theorem.

## Proof
**Step 1: a candidate linear mode and its spectrum.** Select the radius-zero ball at every vertex of \(A\) and the radius-one ball at every vertex of \(B\). The resulting positive linear map is
\[
(Tf)(i)=x_i\ (i\in A),\qquad (Tf)(j)=\frac{X+y_j}{m+1}\ (j\in B)
\]
for nonnegative inputs. In the orthonormal basis of normalized class indicators, the squared singular-value matrix of this map is
\[
Q=\begin{pmatrix}
1+\frac{mn}{(m+1)^2}&\frac{\sqrt{mn}}{(m+1)^2}\\
\frac{\sqrt{mn}}{(m+1)^2}&\frac1{(m+1)^2}
\end{pmatrix}.
\]
The remaining squared singular values are \(1\) on class-\(A\) mean-zero vectors and \((m+1)^{-2}\) on class-\(B\) mean-zero vectors. Since \(\operatorname{tr}Q=\tau_{m,n}\), \(\det Q=(m+1)^{-2}\), and \(\lambda_{\max}(Q)>1\), the squared norm of \(T\) is exactly \(\Lambda_{m,n}\). The positive Perron singular vector has constant class values in ratio \(c_{m,n}\), obtained from the \(B\)-component singular-vector equation. As \(\Lambda_{m,n}>1\), its denominator exceeds \(m(m+2)\); thus \(0<c_{m,n}<1\). For such an input, the selected balls really attain the centered maxima, so \(\|M\|^2\ge\Lambda_{m,n}\). In fact the simpler vector \((m^{-1/2}\mathbf1_A,0_B)\) already gives \(\|M\|^2\ge1+mn/(m+1)^2\).

**Step 2: a uniform bound on maximizing inputs.** Since the nonnegative unit sphere is compact, choose \(f\ge0\) with \(\|f\|_2=1\) maximizing \(\|Mf\|_2\). Write \(a=\|x\|_2\), \(b=\|y\|_2\). The elementary inequality \(\max\{u,v,w\}^2\le u^2+v^2+w^2\) for nonnegative entries, Cauchy–Schwarz \(X\le\sqrt m\,a\), \(Y\le\sqrt n\,b\), and \(n\ge m\) give
\[
\|Mf\|_{\ell^2(A)}^2\le a^2+\frac{(a+\sqrt m\,Y)^2}{(n+1)^2}+\frac{m(X+Y)^2}{(m+n)^2}\le a^2+\frac{8m}{n}.
\]
Likewise,
\[
\|Mf\|_{\ell^2(B)}^2\le b^2+\frac{b^2+2XY+nX^2}{(m+1)^2}+\frac{(X+Y)^2}{n}.
\]
Therefore, with \(F=\|Mf\|_2^2\),
\[
\tag{1}F\le1+\frac{nX^2}{(m+1)^2}+\frac{9m}{n}
+\frac{2\sqrt{mn}}{(m+1)^2}b+\frac{2\sqrt m}{\sqrt n}b+2b^2.
\]
Let \(\alpha=m/(m+1)^2\). Since \(F\ge1+\alpha n\) and \(X^2\le m(1-b^2)\), (1) yields
\[
(\alpha n-2)b^2\le\frac{9m}{n}+
\left(\frac{2\sqrt{mn}}{(m+1)^2}+\frac{2\sqrt m}{\sqrt n}\right)b.
\]
The given threshold ensures \(\alpha n\ge4\). Setting \(t=\sqrt n\,b\), and using \(n\ge m\ge2\), gives
\[
\frac\alpha2 t^2\le9+3t.
\]
The positive solution of this quadratic inequality is strictly less than \(10/\alpha\), hence
\[
\tag{2} b\le\frac{10}{\alpha\sqrt n}\le\frac{20(m+1)}{\sqrt n},\qquad Y\le20(m+1).
\]
Comparing (1) again with \(F\ge1+\alpha n\), then using \(t\le20(m+1)\), gives
\[
\frac{n(m-X^2)}{(m+1)^2}\le\frac{9m}{n}+
\frac{2\sqrt m}{(m+1)^2}t+\frac{2\sqrt m}{n}t+\frac{2t^2}{n}
\le900(m+1)^2,
\]
and therefore
\[
\tag{3}m-X^2\le\frac{900(m+1)^4}{n}.
\]
In particular,
\[
\sum_{i\in A}\left(x_i-\frac Xm\right)^2=a^2-\frac{X^2}{m}
\le\frac{900(m+1)^4}{mn}.
\]
For \(n\ge10^6(m+1)^6\), the last bound and (3) imply \(x_i>1/(2\sqrt m)\) for all \(i\in A\), and \(X>\sqrt m/2\).

**Step 3: strict selector stabilization.** At a maximizing input, (2), \(x_i\le1\), and \(X\le\sqrt m\) bound both nontrivial ball averages at every vertex of \(A\) by \(21(m+1)/n\), strictly below \(x_i\). At each vertex of \(B\), the radius-one average is at least \(X/(m+1)>\sqrt m/[2(m+1)]\), whereas both the radius-zero value and the global average are at most
\[
\max\left\{\frac{20(m+1)}{\sqrt n},\frac{21(m+1)}{n}\right\}.
\]
The stated threshold makes these smaller than the radius-one average. Thus **every maximizing modulus** activates exactly the linear selector \(T\). It follows that
\[
\|M\|_2^2=\|Tf\|_2^2\le\|T\|_2^2=\Lambda_{m,n}.
\]
Combining with Step 1 proves equality. The largest eigenvalue of \(T^*T\) is simple and its eigenvector is strictly positive, so the maximizing modulus is unique up to scaling and has the claimed two levels. Since \(M\) depends only on moduli, arbitrary independent signs preserve equality.

**Step 4: asymptotics.** Writing \(\delta=(m+1)^{-2}\) gives \(\tau=\alpha n+1+\delta\) and
\[
\Lambda_{m,n}=\frac{\tau+\sqrt{\tau^2-4\delta}}2
=\tau-\frac\delta\tau+O_m(n^{-3}).
\]
Since \(\delta/(\alpha n)=1/(mn)\), the claimed expansion follows.

## Verification
Running `python verify_biclique_stabilization.py` with NumPy verifies the mode spectrum and extremizing vectors, exhaustively checks 3,969 complete ball-selector matrices on small graphs, checks 5,832 selector-class patterns on larger examples, and probes the asymptotic expansion. None of the finite tests establishes the universally quantified stabilization threshold; Steps 2–3 do so analytically. The package includes the complete standalone checker.

## Relationship to prior work
Soria and Tradacete (2014) introduced the finite-graph centered maximal-operator framework and obtained sharp norm bounds for \(0<p\le1\) and estimates for stars. González-Riquelme and Madrid (2020) derived strong \(\ell^2\) norms for complete graphs and stars. Earlier finite complete-bipartite calculations give exact results for \(K_{2,3}\) and \(K_{3,3}\), and an explicit lower bound for balanced \(K_{r,r}\). Those statements do not imply the present fixed-class, highly unbalanced **eventual exact norm and all-extremizer rigidity**. This claim does not assert exactness for the unclassified intermediate range or for arbitrary weighted graphs.

## Limitations
The threshold \(10^6(m+1)^6\) is deliberately conservative and not claimed minimal. The theorem applies to the centered (not uncentered) maximal operator on simple unweighted \(K_{m,n}\), counting measure, and real \(\ell^2\). It does not establish a global formula for all \(m,n\), nonuniform masses, or other exponents. The literature comparison is subject to unindexed equivalent formulations; independent validation has not been conducted.

## References
- J. Soria and P. Tradacete, *Best constants for the Hardy–Littlewood maximal operator on finite graphs*, arXiv:1410.6204 (first submitted 22 October 2014), https://arxiv.org/abs/1410.6204.
- C. González-Riquelme and J. Madrid, *Sharp Inequalities for maximal operators on finite graphs*, arXiv:2005.03146 (first submitted 6 May 2020), https://arxiv.org/html/2005.03146v3.
- C. González-Riquelme and J. Madrid, *Sharp inequalities for maximal operators on finite graphs, II*, arXiv:2011.02630 (first submitted 5 November 2020), https://arxiv.org/abs/2011.02630.
