# Sharp Hilbert-snowflake exponents and the two-to-three-page transition for pentagonal edge books

## Finding
For every integer \(r\ge2\), form the pentagonal edge book \(G_r\) by taking vertices \(u,v\), joining them by a unit edge, and adding \(r\) internally disjoint four-edge paths \(u-a_j-b_j-c_j-v\), \(1\le j\le r\). All distances are shortest-path distances. Set \(a=2^p\), \(b=3^p\), \(c=4^p\), and define
\[
E_r(p)=\begin{pmatrix}
 -2ar+2br-2b-2r & -3ar+2br-2b+2\\
 -3ar+2br-2b+2 & -2ar+cr-c+r/2
\end{pmatrix},\qquad F_r(p)=\det E_r(p).
\]
The supremal negative-type exponent \(\wp(G_r)\) is the **least positive zero** \(p_r\) of \(F_r\). It lies in \((1,6/5)\) for \(r=2\) and in \((0,1)\) for every \(r\ge3\). For each \(0\le p<p_r\), the metric has strict \(p\)-negative type; at \(p_r\) it has nonstrict \(p_r\)-negative type with a one-dimensional zero-sum equality space; above \(p_r\), negative type fails. In particular, ordinary quadratic embedding holds for the two-page graph and fails for every three-or-more-page graph.

For every \(0<p\le p_r\), the snowflake \(d^{p/2}\) embeds isometrically into a real Hilbert space. The minimal affine embedding dimension is \(3r+1\) for \(0<p<p_r\) and exactly \(3r\) at \(p_r\). As \(r\to\infty\),
\[
p_r=\frac{3}{r\log(32/27)}+O(r^{-2}).
\]
The threshold at \(r=2\) is approximately \(1.108472030974\); the thresholds for \(r=3,4,5\) are approximately \(0.956442043430\), \(0.852646254877\), and \(0.775437849430\).

## Assumptions and scope
Fix an integer \(r\ge2\) and a real exponent \(p\ge0\). For a real coefficient vector \(z\) indexed by the \(3r+2\) vertices, assume \(\sum_x z_x=0\). Define \(Q_p(z)=\sum_{x,y}z_xz_yd(x,y)^p\), taking diagonal terms to be zero, also for \(p=0\). A metric has \(p\)-negative type precisely when \(Q_p(z)\le0\) for every such vector; it has strict type when equality forces \(z=0\). For \(p=0\), off-diagonal powers are one.

## Proof
**1. Exact metric and decomposition.** The nonzero distances are obtained from the common edge and four-edge pages. Within a page, the distance matrix on \((a_j,b_j,c_j)\) is
\[
D_{\rm in}=\begin{pmatrix}0&1&2\\1&0&1\\2&1&0\end{pmatrix},
\]
while across distinct pages the distance matrix is
\[
D_{\rm cross}=\begin{pmatrix}2&3&3\\3&4&3\\3&3&2\end{pmatrix}.
\]
Distances from \((u,v)\) to one page are \(\bigl(\begin{smallmatrix}1&2&2\\2&2&1\end{smallmatrix}\bigr)\). These formulas remain true after applying entrywise \(p\)-th powers to positive entries. The zero-sum coefficient space decomposes into page contrasts (page triples summing to zero across pages), a global reflection-odd two-dimensional sector, and a global reflection-even two-dimensional sector. These sectors are mutually orthogonal for the powered-distance quadratic form, and their dimensions sum to \(3r+1\).

**2. Page contrasts stay strictly negative.** For each page-contrast triple, the quadratic matrix is the powered \(D_{\rm in}-D_{\rm cross}\):
\[
H_p=\begin{pmatrix}-a&1-b&a-b\\1-b&-c&1-b\\a-b&1-b&-a\end{pmatrix}.
\]
Its reflection-odd eigenvalue is \(b-2a\). Its reflection-even block is \(\bigl(\begin{smallmatrix}-b&\sqrt2(1-b)\\\sqrt2(1-b)&-c\end{smallmatrix}\bigr)\), which is negative definite when \(bc>2(b-1)^2\). Both inequalities are strict throughout \(0\le p\le6/5\): for the odd eigenvalue, \((3/2)^{6/5}<2\); for the even block, when \(p\le1\), \(b\le3\) and \(bc\ge b^2>2(b-1)^2\). When \(1\le p\le6/5\), \(c/b\ge4/3\) and \(b<4\), so \(2(1-1/b)^2<9/8<4/3\).

**3. Global reflection-odd sector stays strictly negative.** Give \((u,v)\) coefficients \((t,-t)\), and every page coefficients \((z,0,-z)\). Then
\[
Q_p=-2t^2+4r(1-a)tz+2r\bigl((r-2)a-(r-1)b\bigr)z^2.
\]
Its negativity is equivalent to \(O_r(p)=(r-1)b-(r-2)a-r(a-1)^2>0\). For \(0\le p\le1\), rewrite \(O_r(p)=r(b+a-a^2-1)+(2a-b)\). The first bracket is nonnegative by concavity of \(x^p\) (the pair \((4,1)\) majorizes \((3,2)\)); the second is positive. For \(r=2\), this sector remains strict to \(p=6/5\): \(O_2=b-2(a-1)^2\), and the ratio \(2(a-1)^2/b\) increases with \(p>0\), since its logarithmic derivative is \(2a\log2/(a-1)-\log3>0\). At \(p=6/5\), the rational bounds \(a<2298/1000\), \(b>3737/1000\) give \(2(a-1)^2<b\).

**4. Global reflection-even sector and the exact threshold.** Give every page coefficients \((z,w,z)\), and each of \(u,v\) coefficient \(-r(2z+w)/2\). Direct substitution yields \(Q_p=r(z,w)E_r(p)(z,w)^\mathsf T\). Its upper-left entry is strictly negative for \(0\le p\le1\), because \(b-a\le1\), and also for \(r=2\), \(0\le p\le6/5\), because that entry is \(2b-4a-4<0\). The determinants satisfy \(F_r(0)=3r+2>0\) and \(F_r(1)=8-3r\). For \(r\ge3\), a zero exists in \((0,1)\). For \(r=2\), \(F_2(1)=2>0\), whereas \(F_2(6/5)<0\), as the following rational certificate proves: at \(p=6/5\), \(2297/1000<a<2298/1000\), \(3737/1000<b<3738/1000\), and \(5278/1000<c<5279/1000\). Each pair of bounds is validated by raising its endpoints to the fifth power and comparing with \(64\), \(729\), or \(4096\), respectively. They imply
\[
F_2(6/5)<\frac{-2859}{500}\frac{-1457}{500}-\left(\frac{-2153}{500}\right)^2
=\frac{-234923}{125000}<0.
\]
Take \(p_r\) to be the least positive zero in the indicated interval. The determinant and the negative diagonal show that \(E_r(p_r)\) is negative semidefinite with exactly one null direction. All other sectors are strictly negative there, so \(Q_{p_r}\) is negative semidefinite with exactly one zero-sum equality direction. The strict-interior theorem of Li and Weston then implies strict \(p\)-negative type for every \(p<p_r\). It also rules out any negative type at \(p>p_r\), since that would force strict negative type at \(p_r\). Because the two-page graph is strict at \(p=1\), the least positive zero for \(r=2\) must occur after one, as asserted.

**5. Embedding dimension.** The Schoenberg correspondence identifies the Gram matrix of squared distances \(d^p\) with minus one half of the centered powered-distance matrix. Strict type has rank \(3r+1\); the one-dimensional equality sector at the critical exponent lowers the rank to \(3r\). This yields exactly the asserted minimal affine dimensions.

**6. Asymptotics.** Expand \(F_r(p)=r^2 A(p)+rB(p)+C(p)\), where \(A(0)=0\), \(A'(0)=\log(27/32)\), \(B(0)=3\), and \(C(0)=2\). These identities follow by differentiating the displayed determinant. Uniformly for bounded \(x\ge0\),
\[
\frac{F_r(x/r)}{r}=3-x\log(32/27)+O_x(r^{-1}).
\]
A uniform sign bracket around \(3/\log(32/27)\), together with absence of earlier zeros on the smaller scaled interval, gives \(rp_r\to3/\log(32/27)\). A Taylor expansion about this simple limiting zero improves the remainder to \(O(r^{-2})\) in \(p_r\).

## Verification
The included `verify.py` rebuilds graph distances by breadth-first search rather than reading the formulas, compares the entire centered powered-distance spectrum against the predicted threshold and one-dimensional endpoint kernel, tests the even-sector matrix identity, and checks the scaling numerically. Running `python verify.py` with NumPy installed prints `CHECK_OK 59`. These are 59 supplementary assertion groups; they do not constitute a proof for arbitrary \(r\). The determinant interval certificate and the all-parameter sector inequalities above supply the infinite-family proof.

## Relationship to prior work
Młotkowski–Skrzypczyk–Wojtylak study quadratic embedding and three-path theta graphs (arXiv:2409.17662, first posted 2024-09-26). The two-page boundary here is the theta graph \(\Theta(1,4,4)\), but the larger page counts are multi-path rather than three-path theta graphs. Skrzypczyk (arXiv:2603.23681, 2026) proves every \(\Theta(1,\beta,\gamma)\) is quadratically embeddable and therefore already covers the ordinary \(p=1\) assertion for \(r=2\); the present novelty claim is instead the exact variable-exponent threshold and the transition at \(r=3\). Młotkowski–Obata's star-product results concern vertex-gluing, not the shared-edge construction. Li–Weston's strict-interior theorem is used in the proof and is not claimed as new. No directly covering all-page exponent formula was found in the searches described in the review; unindexed or differently phrased prior work remains possible.

## Limitations
All pages have four edges, the common edge has length one, and all jumps are purely metric. No claim is made for pages of other lengths, weighted edge books, asymmetric pages, or more general multitheta graphs. The threshold is specified by the first positive zero, not by a claim that the determinant has only one zero for all positive exponents. Historical originality has not been independently certified.

## References
1. W. Młotkowski, M. Skrzypczyk, and M. Wojtylak, *On quadratic embeddability of bipartite graphs and theta graphs*, arXiv:2409.17662 (first posted 2024-09-26), https://arxiv.org/abs/2409.17662.
2. M. Skrzypczyk, *Quadratic Embedding of Theta Graphs via Reproducing Kernel Hilbert Spaces*, arXiv:2603.23681 (first posted 2026-03-24), https://arxiv.org/abs/2603.23681.
3. W. Młotkowski and N. Obata, *On Quadratic Embedding Constants of Star Product Graphs*, arXiv:1802.01214 (first posted 2018-02-04), https://arxiv.org/abs/1802.01214.
4. H. Li and A. Weston, *Strict p-negative type of a metric space*, arXiv:0901.0695 (first posted 2009-01-06), https://arxiv.org/abs/0901.0695.
