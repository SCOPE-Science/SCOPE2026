# Sharp Tjurina bound for conics adjoining the non-Fano seven-line arrangement

## Finding
Let \(\mathcal L\) be any complex projective arrangement of seven distinct lines with exactly six ordinary triple points and three ordinary nodes, and no higher multiplicity points. For every smooth conic \(Q\) such that \(\mathcal C=\mathcal L\cup Q\) has only ordinary nodes, ordinary tacnodes, and ordinary triple points, its total Tjurina number satisfies
\[
\boxed{\tau(\mathcal C)\le 46.}
\]
The bound is sharp. In coordinates over \(\mathbb C\), one extremal example is
\[
\mathcal L:\; xyz(x+y)(x+z)(y+z)(x+y+z)=0,\qquad
Q:\; (x-y)^2-4i(x+y)z-4z^2=0.
\]
Its complete singularity basket is \((n_2,t,n_3)=(5,3,8)\), so \(\tau=5+3\cdot3+4\cdot8=46\). Consequently no conic extension of this seven-line combinatorial type that has the stipulated singularities is nearly free; **no assertion is made for arbitrary degree-nine conic-line arrangements**.

## Assumptions and scope
All curves and projective equivalences are over \(\mathbb C\). An ordinary triple point is a transverse intersection of three smooth local branches; an ordinary tacnode is a contact-two intersection of two smooth branches. A node, tacnode, and ordinary triple point contribute local Tjurina numbers \(1,3,4\), respectively. The set of allowed conics is nonempty by the displayed witness. The parameter \(i\) denotes a root of \(i^2=-1\). The result is an exact statement for the entire non-Fano line-arrangement combinatorial stratum, not for general arrangements with seven lines.

## Proof
**1. The underlying line arrangement is rigid.** Seven lines with exactly six triple points have three double points, by \(\binom72=3\cdot6+3\). Let \(r(L)\) count triple points on a line. Because a triple uses two of its six intersections with other lines, a line with \(r\) triples has \(6-2r\) doubles. Since there are only three double points in the whole arrangement, \(r\ge2\), while \(r\le3\). Summing triple incidences gives \(\sum r(L)=18\), so four lines have \(r=3\), and three have \(r=2\). Call these four *high* and three *low*.

A high line has no double point, so every pair of high lines meets at an original triple. If \(a_j\) denotes the number of original triples containing exactly \(j\) high lines, then
\[
\sum_{j=0}^3a_j=6,\quad \sum_{j=0}^3ja_j=12,\quad a_2+3a_3=6.
\]
These equalities give \(a_0=-a_3\), hence \(a_3=a_0=0\), \(a_2=6\), and \(a_1=0\). In particular the four high lines are in general position; their six intersection points are distinct. Each low line contains two of those six intersections, so it joins two disjoint pairs of the high lines. The three low lines realize the three perfect matchings of four objects. Projective normalization of the four high lines gives the explicit seven-line equation in the finding, up to permutation and scalar. The three original doubles are
\[
P_1=[1:-1:-1],\quad P_2=[1:-1:1],\quad P_3=[1:1:-1].
\]

**2. Reduction to the incidence sum.** Let \(h\in\{0,1,2,3\}\) be the number of the three original double points lying on \(Q\), and let \(t\) count conic-line tacnodes. The conic avoids the six original triple points, since a fourth branch would violate the singularity hypothesis. At each selected old double \(Q\) meets both lines transversely, creating exactly one new ordinary triple point. Thus \(n_3=6+h\). Counting pairwise intersections with multiplicity yields
\[
35=\binom72+7\cdot2=n_2+2t+3n_3,
\qquad \tau=n_2+3t+4n_3=41+h+t.
\]
Each five-element set of lines contains three concurrent lines, since among four high lines and three low lines it necessarily contains a full high-pair matching at one of the original triples (alternatively check the perfect-matchings description). A smooth conic cannot be tangent to three distinct concurrent lines: their three dual points would be collinear on the smooth dual conic. Consequently \(t\le4\). If \(h\le1\), immediately \(h+t\le5\). It remains to exclude \((h,t)=(2,4)\) and \(h=3,t\ge3\).

**3. Two old doubles and four tangencies are impossible.** Every low line passes through at least one of any two of \(P_1,P_2,P_3\). Since it already meets \(Q\) transversely there, no low line is tangent to \(Q\) anywhere. Thus four tangencies require tangency to all four high lines, normalized as \(x=0,y=0,z=0,x+y+z=0\). Express a smooth conic by its invertible symmetric coefficient matrix \(A\), and put \(B=A^{-1}\) up to nonzero scale. Tangency of a line with coefficient vector \(\ell\) is equivalent to \(\ell^TB\ell=0\). The first three high-line tangencies force
\[
B=\begin{pmatrix}0&u&v\\u&0&w\\v&w&0\end{pmatrix};
\quad \det B=2uvw\ne0.
\]
Tangency to the fourth gives \(u+v+w=0\). Because the primal conic is represented up to scale by \(\operatorname{adj}(B)\), evaluating its equation at \(P_1,P_2,P_3\) gives, respectively,
\[
4uv,\qquad4uw,\qquad4vw.
\]
All are nonzero because \(uvw\ne0\); not even one old double can be on this four-tangent conic. This excludes \((h,t)=(2,4)\).

**4. Three old doubles and at least three tangencies are impossible.** Each low line meets \(Q\) at two different original doubles, so none is tangent. If a conic goes through all three doubles, its homogeneous quadratic equation is necessarily
\[
Q_{a,b,c}=ax^2+by^2+cz^2+s(xy+xz+yz),\qquad s=a+b+c.
\]
The tangency discriminants for the four high lines \(x=0,y=0,z=0,x+y+z=0\) are
\[
s^2-4bc,\quad s^2-4ac,\quad s^2-4ab,\quad(c-a-b)^2-4ab.
\]
The last expression has the same symmetric interpretation upon permuting \(a,b,c\). If the first three vanish, the equations force either the zero coefficient triple or \(a=b=c\ne0\), when \(9a^2=4a^2\), absurd. If two coordinate-axis discriminants and the diagonal discriminant vanish, relabel so the first two vanish. They give \(c(a-b)=0\). If \(c=0\), then \(a+b=0\) and the diagonal discriminant forces \(ab=0\), so all coefficients vanish. Otherwise \(a=b=r\), and the remaining two equations become \(c^2+4r^2=0\) and \(c(c-4r)=0\); these have only the zero solution over \(\mathbb C\), since substituting \(c=4r\) gives \(20r^2=0\). Thus no three high lines are tangent, proving \(t\le2\) when \(h=3\).

Combining all cases gives \(h+t\le5\), hence \(\tau\le46\).

**5. Sharpness.** For the conic \(Q=(x-y)^2-4i(x+y)z-4z^2\), the symmetric matrix
\[
A=\begin{pmatrix}1&-1&-2i\\-1&1&-2i\\-2i&-2i&-4\end{pmatrix}
\]
has \(\det A=16\ne0\), proving smoothness. The conic passes through \(P_1,P_2\), but through neither \(P_3\) nor any of the six old triples. The line-tangency test \(\ell^T\operatorname{adj}(A)\ell=0\) holds exactly for \(x=0,y=0,z=0\) among the seven lines. The three tangent contacts are respectively \([0:2i:1]\), \([2i:0:1]\), \([1:1:0]\), all away from the other lines. At \(P_1,P_2\), the conic is transverse to both intersecting lines. Consequently there are \(h=2\) new triple incidences and \(t=3\) tacnodes; the remaining five singularities are nodes, as the pairwise Bézout sum forces. Therefore \(\tau=46\), attaining the bound.

**6. Near-freeness corollary.** A nearly free reduced plane curve of degree \(m=9\) has \(\tau=r^2-r(m-1)+(m-1)^2-1=(r-4)^2+47\ge47\), where \(r\) is its minimal Jacobian syzygy degree (the standard nearly free Tjurina formula). Our \(\tau\le46\) precludes near-freeness for this class, without any computation of \(r\).

## Verification
The accompanying `verify.py` uses exact SymPy arithmetic. It independently enumerates the nine line-line singularities, tests every five-line subset for a triple concurrency, checks the dual conic identities and the three old doubles, and verifies smoothness, tangencies, contact separation, transversality, singularity basket, and \(\tau=46\) of the explicit witness. The universal inequality follows from the complete algebraic case split above, not finite parameter sampling. Execute `python verify.py` with a current SymPy installation.

## Relationship to prior work
Dimca–Pokora (2022, Proposition 5.6) prove that no free conic-line arrangement of seven lines and a smooth conic with the prescribed singularities exists. Their argument identifies the non-Fano seven-line arrangement as the extreme candidate and rules out a conic simultaneously tangent to four high lines and passing through all three old doubles. That free-case obstruction neither asserts this **sharp global Tjurina maximum** nor excludes the distinct prospective nearly-free boundary \(\tau=47\). The present proof excludes all cases with \(h+t\ge6\), supplies a conic with \(\tau=46\), and resolves near-freeness only for the six-triple-point line stratum. Gałecka (2022) leaves degree-nine nearly free arrangements unresolved in general. Bannai–Guerville-Ballé–Shirane (2024) construct degree-nine seven-line/one-conic Zariski pairs with different line incidence configurations; their two families do not attain six original line triples and do not imply the sharp extremal statement. Lampa-Baczyńska–Wojcik (2024) study a six-line, one-conic near-free stratum; it does not cover the present seven-line stratum.

## Limitations
This result does **not** classify all degree-nine conic-line arrangements or settle the general degree-nine nearly-free existence question. The characteristic-zero hypothesis is used in discriminant and coefficient contradictions (in particular the factor \(20\)); positive-characteristic analogues are not asserted. The witness lies over \(\mathbb Q(i)\), not necessarily over \(\mathbb Q\). The search for covering literature included direct primary-text comparisons and database queries but cannot guarantee exhaustive bibliographic coverage.

## References
1. A. Gałecka, *On the nearly freeness of conic-line arrangements with nodes, tacnodes, and ordinary triple points*, arXiv:2204.13969v1 (29 April 2022), DOI 10.1007/s40590-022-00461-4. https://arxiv.org/html/2204.13969v2
2. A. Dimca and P. Pokora, *On conic-line arrangements with nodes, tacnodes, and ordinary triple points*, J. Algebraic Combin. 56 (2022), 403–424, Proposition 5.6. DOI 10.1007/s10801-022-01116-3. https://link.springer.com/article/10.1007/s10801-022-01116-3
3. S. Bannai, B. Guerville-Ballé, and T. Shirane, *Zariski pairs of conic-line arrangements with a unique conic*, arXiv:2410.04969v1 (2024), Sections 2.2–2.3. https://arxiv.org/html/2410.04969v1
4. M. Lampa-Baczyńska and D. Wojcik, *Weak Ziegler pairs of conic-line arrangements with ordinary singularities*, arXiv:2403.16870v1 (2024). https://arxiv.org/html/2403.16870v1
