# Sharp cyclic-variation amplification of Euclidean simplex projection

## Finding

Let \(n\ge2\) be an integer, and let \(P:\mathbb R^n\to\Delta_{n-1}\) be the Euclidean nearest-point projection onto the probability simplex
\[
\Delta_{n-1}=\{z\in\mathbb R^n:z_i\ge0,\ \sum_{i=0}^{n-1}z_i=1\}.
\]
For a real cyclic vector, indices modulo \(n\), put
\[
V_n(z)=\sum_{i=0}^{n-1}|z_{i+1}-z_i|.
\]
The **sharp two-input Lipschitz modulus** in cyclic total variation is
\[
\boxed{\operatorname{Lip}_{V_n}(P):=
\sup_{V_n(x-y)>0}\frac{V_n(Px-Py)}{V_n(x-y)}
=\frac{\left\lfloor (n+2)^2/8\right\rfloor}{\left\lceil (n+2)/2\right\rceil}.}
\]
Equivalently,
\[
\operatorname{Lip}_{V_n}(P)=
\begin{cases}
(n+1)/4,&n\text{ odd},\\
(n+2)/4,&n\equiv2\pmod4,\\
(n+2)/4-1/(n+2),&n\equiv0\pmod4.
\end{cases}
\]
Every constant is attained by a pair of real input vectors. In particular the first strictly expansive dimension is \(n=4\), with modulus \(4/3\), and the modulus grows like \(n/4\). In contrast, each individual vector satisfies \(V_n(Px)\le V_n(x)\).

## Assumptions and scope

All data are real; projection is Euclidean, all cyclic edges have unit weight, and the simplex has unit total mass. The variation is a seminorm, vanishing exactly on constant vectors; the quotient in the finding is taken only when its denominator is positive. The map \(P\) is invariant under adding a constant to all input coordinates, so its two-input variation modulus is well-defined despite the seminorm. The formula extends unchanged to any prescribed strictly positive simplex mass, by the same active-set Jacobians and witnesses.

## Proof

**1. Threshold representation and full-dimensional affine pieces.** The simplex KKT conditions give the unique threshold \(\tau(x)\) such that
\[
(Px)_i=(x_i-\tau(x))_+,
\qquad \sum_i(x_i-\tau(x))_+=1.
\]
If \(A=\{i:(Px)_i>0\}\) is fixed and has size \(m\), then \(\tau(x)=(\sum_{j\in A}x_j-1)/m\). The local affine linear part is
\[
(J_Ah)_i=\begin{cases}
h_i-\frac1m\sum_{j\in A}h_j,&i\in A,\\
0,&i\notin A.
\end{cases}
\]
Every nonempty \(A\) occurs on an open cell: choose \(x_i=1/m\) on \(A\) and \(x_i=-1\) off \(A\). Also \(J_A\mathbf1=0\). Since \(P\) is continuous piecewise affine, integration of affine derivatives on generic line segments, followed by continuity for exceptional segments, yields
\[
\operatorname{Lip}_{V_n}(P)=\max_{\varnothing\ne A\subseteq\{0,\ldots,n-1\}}\|J_A\|_{V_n\to V_n}.
\]
The reverse inequality follows by taking sufficiently small perturbations within the relevant open cell. No differentiability at cell boundaries is assumed.

**2. Cyclic-interval test vectors.** The gradient of any cyclic vector has zero sum. Split its positive and negative gradient masses into a nonnegative transport between ordered pairs of edges. Each elementary edge-pair gradient integrates, modulo a constant, to a signed indicator of a nonempty proper cyclic interval \(I\). The sum of transport coefficients is exactly \(V_n(h)/2\). Because \(J_A\mathbf1=0\), the triangle inequality consequently gives the exact operator-norm reduction
\[
\|J_A\|_{V_n\to V_n}=
\frac12\max_{I\text{ proper cyclic interval}}V_n(J_A\mathbf1_I).
\]
The reverse direction is immediate by testing the interval indicators, each of variation \(2\).

**3. Exact component count.** Fix a nonempty active set \(A\) of size \(m\) and a proper cyclic interval \(I\). Write \(a=|A\cap I|\), \(b=|A\setminus I|\), so \(a+b=m\). When either number is zero, \(J_A\mathbf1_I=0\). Otherwise let \(r\) and \(s\) be the numbers of connected runs of \(A\cap I\) and \(A\setminus I\) within their respective arcs. The vector \(J_A\mathbf1_I\) has value \(b/m\) on \(A\cap I\), value \(-a/m\) on \(A\setminus I\), and zero elsewhere. Variations of the nonnegative and nonpositive pieces add on every edge, including their mutual boundary. Hence
\[
\frac12V_n(J_A\mathbf1_I)=\frac{br+as}{m}.
\]
The run counts satisfy \(1\le r\le a\), \(1\le s\le b\) and
\[
m+r+s\le n+2=:N,
\]
because each of the \(r\) and \(s\) runs, within its own arc, requires a separator between consecutive runs. Conversely any positive integers satisfying these inequalities are realizable by putting the required runs and zeros into the two complementary arcs. In particular the formula is a sharp finite combinatorial reduction.

**4. Sharp integer optimization.** Interchanging the two arcs if necessary, suppose \(a\ge b\). From \(r\le a\), \(s\le b\),
\[
\frac{br+as}{m}\le\frac{2ab}{m}\le\frac{2\lfloor m^2/4\rfloor}{m}.
\]
Using \(r+s\le N-m\) instead gives
\[
br+as=b(r+s)+(a-b)s\le b(N-m)+(a-b)b=b(N-2b).
\]
The maximum over integral \(b\) of \(b(N-2b)\) is \(\lfloor N^2/8\rfloor\). Thus, if \(m\ge\lceil N/2\rceil\),
\[
\frac{br+as}{m}\le\frac{\lfloor N^2/8\rfloor}{\lceil N/2\rceil}.
\]
If \(m\le N/2\), write \(N=2h\) or \(N=2h+1\). In the even case, \(m\le h\) and the integer function \(2\lfloor m^2/4\rfloor/m\) increases with \(m\), so the bound is at most \(2\lfloor h^2/4\rfloor/h=\lfloor N^2/8\rfloor/\lceil N/2\rceil\). In the odd case, \(m\le h\), so the bound is at most \(m/2\le h/2=\lfloor N^2/8\rfloor/(h+1)\). This proves the universal inequality.

**5. Equality and actual pairs.** For even \(N\), take \(m=N/2\), \(a=\lceil m/2\rceil\), \(b=\lfloor m/2\rfloor\), and \(r=a\), \(s=b\). For odd \(N\), take \(m=(N+1)/2\), the same balanced \(a,b\), and \(r=a-1\), \(s=b\). In both cases \(m+r+s=N\), and the component expression equals the displayed sharp constant. Construct \(I\) by placing \(a\) selected vertices in \(r\) runs separated by single zeros and its complement by placing \(b\) selected vertices in \(s\) such runs; together they occupy exactly \(n=N-2\) vertices.

Let \(A\) be the selected positions and set \(x_i=1/m\) for \(i\in A\) and \(x_i=-1\) otherwise. For sufficiently small \(\varepsilon>0\), both \(x\) and \(y=x+\varepsilon\mathbf1_I\) remain in the same active-set cell, and
\[
Py-Px=\varepsilon J_A\mathbf1_I,
\qquad V_n(y-x)=2\varepsilon.
\]
Their quotient is the desired sharp constant. Finally, for fixed \(x\), the scalar clipping map \(t\mapsto(t-\tau(x))_+\) is 1-Lipschitz, proving \(V_n(Px)\le V_n(x)\).

## Verification

The standalone `checker.py` uses exact rational arithmetic to enumerate all active-set selectors and all proper cyclic intervals through dimension \(10\), checks every proposed equality witness as an actual pair of simplex projections, and independently tests additional rational input pairs. Run `python3 checker.py`. It reports 115226 exhaustive selector/interval comparisons, nine exact attaining witnesses, and 2280 rational two-data tests, together with 2280 one-input tests. The enumeration is only a finite diagnostic; the all-dimensional proof is the five-step argument above.

## Relationship to prior work

Classical simplex projection and its soft-threshold KKT formula are established results, not contributions claimed here. Duchi et al. [1] developed efficient projection methods; Wang and Carreira-Perpiñán [2] supplied an elementary proof; Condat [3] examined algorithms and their complexity. These sources establish the active-set formula, but do not compute a cyclic-gradient two-input operator norm.

Lellmann et al. [4] combine spatial total-variation regularization with simplex constraints on label vectors, but the variation there is spatial across image sites, not the cyclic total variation across the coordinates of one simplex-projection input or output. A published analysis [5] of the **same simplex projection map** calculates its sharp \(\ell_4\) stability using active-set centering operators. Its \(\ell_4\) norm does not dominate, or determine exactly, the cycle-gradient seminorm quotient examined here. The new content is the interval-cut reduction, the exact all-dimensional integer optimum, the residue-class defect, and attained amplification growing linearly with dimension. An unindexed equivalent formula remains a bibliographic possibility.

## Limitations

The result concerns Euclidean projection onto a real standard simplex with cyclic unit-weight variation. It does not assert a sharp constant for arbitrary graphs, weighted cyclic variation, coordinatewise \(\ell_p\) measurement, or non-Euclidean projection objectives. The source comparisons do not constitute a proof of worldwide novelty. No independent mathematical audit has been performed.

## References

[1] J. Duchi, S. Shalev-Shwartz, Y. Singer, and T. Chandra, *Efficient Projections onto the \(\ell_1\)-Ball for Learning in High Dimensions*, ICML 2008, 272–279, first verified public publication 2008-07-05, DOI https://doi.org/10.1145/1390156.1390191.

[2] W. Wang and M. A. Carreira-Perpiñán, *Projection onto the Probability Simplex: An Efficient Algorithm with a Simple Proof, and an Application*, arXiv:1309.1541v1, publicly posted 2013-09-06, https://arxiv.org/html/1309.1541v1.

[3] L. Condat, *Fast Projection onto the Simplex and the \(\ell_1\) Ball*, HAL-01056171v1, publicly posted 2014-08-17, https://optimization-online.org/wp-content/uploads/2014/08/4498.pdf.

[4] J. Lellmann, J. Kappes, J. Yuan, F. Becker, and C. Schnörr, *Convex Multi-Class Image Labeling by Simplex-Constrained Total Variation*, SSVM 2009, https://www.lellmann.net/work/_media/files/lellmann_ssvm09.pdf.

[5] *Sharp \(\ell_4\) Stability of Metric Projection onto a Probability Simplex*, published mathematical record, https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-sharp-ell-4-stability-of-metric-projection-onto-a-probability-si--ade1ccb04ed3.
