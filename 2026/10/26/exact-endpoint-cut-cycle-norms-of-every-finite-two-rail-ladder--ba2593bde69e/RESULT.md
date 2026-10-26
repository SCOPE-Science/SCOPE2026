# Exact endpoint cut–cycle norms of every finite two-rail ladder

## Finding

For every integer \(n\ge2\), let \(L_n=P_2\square P_n\) be the unweighted two-rail ladder with \(n\) rungs. Give its real edge-coordinate space the standard \(\ell_1\) norm. Let \(D\) be an arbitrarily oriented vertex–edge incidence matrix and define the canonical Euclidean-orthogonal cut and cycle projections
\[
Q_n=D^{\mathsf T}(DD^{\mathsf T})^+D,\qquad P_n=I-Q_n.
\]
Put \(r=2-\sqrt3\), \(c=\lfloor(n+1)/2\rfloor\), and
\[
A_{n,j}=\frac{(1+r^{2j-1})(1+r^{2n-2j+1})}{2\sqrt3(1-r^{2n})},\qquad
B_{n,j}=\frac{(1+r)(r^{j-1}+r^{n-j})}{2\sqrt3(1-r^n)}.
\]
Then the **exact induced real endpoint norms** are
\[
\boxed{\|Q_n\|_{1\to1}=1+4A_{n,c}-2B_{n,c}},\qquad
\boxed{\|P_n\|_{1\to1}=2-2B_{n,c}}.
\]
The same formulas hold for \(\ell_\infty\to\ell_\infty\), since both matrices are symmetric. For \(n\ge3\), the only maximizing columns of **either** projection are central rungs: rung \(c\), and also rung \(c+1\) when \(n\) is even. For \(n=2\), all four edges maximize both norms.

The cut projection strictly dominates its cycle complement for every finite \(n\ge2\):
\[
\boxed{\|Q_n\|-\|P_n\|=4A_{n,c}-1>0.}
\]
Both family-wide sharp suprema are unattained at finite length:
\[
\boxed{\sup_{n\ge2}\|Q_n\|=1+\frac2{\sqrt3},\qquad
\sup_{n\ge2}\|P_n\|=2.}
\]
The corresponding norms converge to those suprema as \(n\to\infty\), so their limiting gap is \(2/\sqrt3-1>0\). For example, the cut and cycle norms at \(n=3\) are \(9/5\) and \(8/5\); at \(n=4\) they are \(27/14\) and \(7/4\); and at \(n=5\) they are \(39/19\) and \(36/19\).

## Assumptions and scope

The graph is connected, simple, and has all edge conductances equal to one. Its vertices are \((\varepsilon,j)\) with \(\varepsilon\in\{0,1\}\) and \(1\le j\le n\). The rung at column \(j\) joins \((0,j)\) to \((1,j)\); the two rails join consecutive columns in each layer. The induced matrix \(\ell_1\) norm is the maximum absolute column sum, not the smallest possible norm among arbitrary projections onto the cycle or cut space. Reference edge orientations change matrix signs by diagonal conjugation, preserving those norms. The superscript \(+\) denotes the Moore–Penrose inverse. The \(n=2\) graph is a four-cycle; \(n=1\) is excluded because its cycle projection is zero and it has no rail edges.

## Proof

**1. Positive Green kernel.** Let \(L\) be the Laplacian of the \(n\)-vertex path and put \(R=(L+2I)^{-1}\). The entry \(R_{ij}\) is strictly positive. Write \(C=[2\sqrt3(1-r^{2n})]^{-1}\). Solving the interior recurrence \(4u_i-u_{i-1}-u_{i+1}=0\) with endpoint diagonal \(3\) gives the exact inverse
\[
R_{ij}=C\bigl(r^{|i-j|}+r^{i+j-1}
+r^{2n-i-j+1}+r^{2n-|i-j|}\bigr).
\tag{1}
\]
The identity can be checked directly by multiplying by the tridiagonal matrix, using \(r+r^{-1}=4\). In particular,
\[
R_{jj}=A_{n,j},\qquad R_{1j}+R_{nj}=B_{n,j},\qquad
\sum_{i=1}^nR_{ij}=\frac12.
\tag{2}
\]
One useful equivalent expression, with \(\theta=\operatorname{arcosh}(2)\) and \(f_k=\cosh((k-\tfrac12)\theta)\), is
\[
R_{ij}=\frac{f_{\min(i,j)}f_{n+1-\max(i,j)}}{\sinh\theta\,\sinh(n\theta)}.
\tag{3}
\]
This factorization proves that each column increases strictly up to its diagonal and decreases strictly thereafter. It also proves that the dipole \(g=R(e_j-e_{j+1})\) is strictly positive and increasing on \(1,\ldots,j\), and strictly negative and increasing on \(j+1,\ldots,n\): on each side its values are a nonzero constant times \(f_i\) or \(f_{n+1-i}\), with the indicated signs.

**2. All rung columns.** Inject one unit at the upper endpoint of rung \(j\) and remove one unit at its lower endpoint. Reflection through the midline makes the vertex potentials \((R_{ij},-R_{ij})\) on the two rails. Therefore the cut projection column has rung entries of absolute size \(2R_{ij}\), while its two horizontal rail responses at interval \(i\) have absolute sizes \(|R_{i+1,j}-R_{ij}|\). Positivity, the column-sum identity, and monotonicity in (2)–(3) give the cut absolute column sum
\[
H_j=2\sum_iR_{ij}+2\sum_{i=1}^{n-1}|R_{i+1,j}-R_{ij}|
=1+4R_{jj}-2(R_{1j}+R_{nj}).
\tag{4}
\]
Since the diagonal cut entry equals \(2R_{jj}\), the complementary cycle column has sum
\[
H'_j=1+H_j-4R_{jj}=2-2(R_{1j}+R_{nj}).
\tag{5}
\]
These identities include endpoint rungs.

**3. All rail columns.** Take the upper horizontal edge between columns \(j\) and \(j+1\), and let \(g=R(e_j-e_{j+1})\). Decompose the source into the symmetric and antisymmetric two-rail modes. For the symmetric mode, the path current is supported exclusively on that interval. Away from it, the two rail currents have absolute sum \(|g_{i+1}-g_i|\); on it their absolute sum is \(1\). Rung-current magnitudes sum to \(\sum_i|g_i|\). Set
\[
u=g_j>0,\quad v=-g_{j+1}>0,\quad \ell=g_1>0,\quad t=-g_n>0.
\]
The sign and monotonicity from (3) give \(\sum_{i\ne j}|g_{i+1}-g_i|=u+v-\ell-t\). Summing the equation \((L+2I)g=e_j-e_{j+1}\) over columns \(1,\ldots,j\), and using \(\sum_i g_i=0\), yields \(\sum_i|g_i|=1-u-v\). Thus the cut and cycle rail-column sums are exactly
\[
V_j=2-\ell-t,
\qquad V'_j=2-u-v-\ell-t.
\tag{6}
\]
The source diagonal is \((1+u+v)/2\), which lies strictly between zero and one. Indeed \(u+v=(e_j-e_{j+1})^{\mathsf T}R(e_j-e_{j+1})<1\), by comparing \((L+2I)^{-1}\) with the path pseudoinverse on the mean-zero subspace. This verifies the absolute-value step in (6).

**4. Both rung norms peak at the center.** For \(j<n\) set \(a=r^{j-1}\), \(b=r^{n-j-1}\), and retain \(C\) from (1). Elementary differences of the explicit Green entries give
\[
R_{j+1,j+1}-R_{jj}=Cr(1-r^2)(b-a)(a+b),
\]
\[
B_{n,j+1}-B_{n,j}=C(1-r^2)(1+r^n)(b-a).
\]
Consequently
\[
H_{j+1}-H_j=2C(1-r^2)(b-a)
\bigl[2r(a+b)-(1+r^n)\bigr].
\tag{7}
\]
For \(n\ge3\), \(a+b\le1+r\) and \(2r(1+r)<1\), so the bracket is strictly negative. If \(j<n/2\), then \(b<a\), proving \(H_{j+1}>H_j\). Equation (5) and the second displayed difference similarly show \(H'_{j+1}>H'_j\). Reflection gives the remaining strict decrease, with the expected central tie when \(n\) is even. At \(n=2\), both rung columns tie.

**5. Rung maxima strictly beat rail columns for \(n\ge3\).** Equation (6) implies \(V_j<2\). For \(n\ge5\), choose a central rung \(c\). Its distances to both path boundaries are at least two; (2) and \(r<3/10\), \(5/3<\sqrt3<7/4\) imply
\[
B_{n,c}\le\frac{(1+r)r^2}{\sqrt3(1-r^5)}
<\frac1{14}.
\tag{8}
\]
Also \(R_{cc}\ge1/(2\sqrt3)\). Therefore \(H_c>1+8/7-1/7=2\), so no rail column maximizes the cut norm. For \(n=3,4\), direct exact substitution into (4) and (6) gives \(\max H=9/5>5/3=\max V\) and \(\max H=27/14>13/7=\max V\), respectively.

To compare cycle columns, let \(d=e_j-e_{j+1}\). The largest eigenvalue of \(L+2I\) is strictly less than six, hence
\[
u+v=d^{\mathsf T}(L+2I)^{-1}d>\frac{\|d\|_2^2}{6}=\frac13.
\]
Equation (6) thus gives \(V'_j<5/3\). At \(n=4\) the central rung has \(H'_c=7/4\); for \(n\ge5\), (8) gives \(H'_c>13/7>5/3\). At \(n=3\), direct substitution gives \(H'_c=8/5\), while \(\max V'=6/5\). Thus the central rung columns are the unique norm maximizers for both projections whenever \(n\ge3\). The \(n=2\) formulas give \(H_j=V_j=3/2\) and \(H'_j=V'_j=1\); all four edges maximize.

**6. Dominance and sharp suprema.** Since the two norms occur at the same central rung,
\[
\|Q_n\|-\|P_n\|=4R_{cc}-1.
\]
Formula (1) yields \(R_{cc}\ge1/(2\sqrt3)>1/4\), proving strict dominance. Equation (2) gives \(\|P_n\|=2-2B_{n,c}<2\). For the cut bound, put \(x=r^{c-1}\), \(y=r^{n-c}\), so \(rxy=r^n\). The quantity \((\|Q_n\|-1)\sqrt3/2\) is
\[
\frac{(1+rx^2)(1+ry^2)}{1-r^2x^2y^2}
-\frac{(1+r)(x+y)}{1-rxy}.
\]
Subtracting one and putting over the positive common denominator gives the numerator
\[
r(x^2+y^2)+2r^2x^2y^2-(1+r)(x+y)(1+rxy),
\]
which is strictly negative because \(0<x,y\le1\), \(x^2+y^2\le x+y\), and \(2x^2y^2\le x+y\). Therefore \(\|Q_n\|<1+2/\sqrt3\) for every finite \(n\). Finally, as \(n\to\infty\) with \(c\) central, \(x,y\to0\), so \(R_{cc}\to1/(2\sqrt3)\) and \(B_{n,c}\to0\). This proves both sharp unattained suprema and the limiting gap.

## Verification

The standalone `check_ladder_endpoint.py` constructs grounded graph Laplacians and canonical projection matrices with exact rational arithmetic independently of the path Green reduction. For every ladder length \(2\le n\le12\), it checks every edge column of both projections against the formulas (4)–(6), and it verifies the global maximizing rung identities, their exact equality sets, and strict dominance. The successful replay reports `LADDER_ENDPOINT_EXACT_OK graphs=11 checked_projection_columns=209`. This is finite corroboration only; the unrestricted proof consists of steps 1–6. The checker requires Python 3 and SymPy and does not access external data.

## Relationship to prior work

Dilworth, Kutzarova, and Ostrovskii (arXiv:2305.12582, first public 2023-05-21; MSC 46B04) study graph cycle spaces, canonical/invariant projections, discrete tori, and Hamming graphs. Their relevant full-text sections do not state an endpoint classification for the open two-rail ladder, including the extremizing edge orbits or its strict cut-versus-cycle ordering. Klenke (arXiv:1704.00182) develops weighted spanning-tree processes on infinite ladder-like graphs and their transfer currents, not these finite projection endpoint maxima.

A later published calculation, *Exact finite-volume rung kernel and boundary-bulk split for weighted ladder spanning trees* (2026), provides the full finite **rung-to-rung** transfer-current kernel, including its boundary corrections. Its rung block supplies part of the Green input to (4)–(5); those formulas are therefore not presented as newly discovered Green functions. The present claim additionally solves all **rail-source** columns, compares them rigorously against rungs, gives the unique norm-maximizer classes for every length, and establishes simultaneous sharp endpoint limits and strict norm ordering. The earlier rung-kernel statement does not state these operator-norm conclusions. An equivalent derivation in another electrical-network source may exist, so originality is a best-knowledge assessment rather than a completeness certificate.

## Limitations

These are norms of the specified canonical Euclidean-orthogonal projections on real, unweighted, finite ladders, not optimal norms over all possible nonorthogonal projections. No weighted-rung, wider-strip, infinite-operator, or intermediate \(\ell_p\) assertion is made. The closed Green kernel is standard tridiagonal analysis and is used, not claimed as novel. Independent mathematical audit has not been performed.

## References

1. S. J. Dilworth, D. Kutzarova, M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582 (2023-05-21), https://arxiv.org/abs/2305.12582.
2. A. Klenke, *The Random Spanning Tree on Ladder-like Graphs*, arXiv:1704.00182 (2017-04-01), https://arxiv.org/abs/1704.00182.
3. *Exact finite-volume rung kernel and boundary-bulk split for weighted ladder spanning trees*, 2026, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-finite-volume-rung-kernel-and-boundary-bulk-split-for-weig--647fc3f7ee8c.
