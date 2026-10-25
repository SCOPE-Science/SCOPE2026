# Gorenstein rigidity of alternating adjacent-sum lattice polytopes

## Finding
For every integer \(d\ge2\) and \(s\ge1\), define the full-dimensional lattice polytope
\[
P_d^{(s)}=\bigl\{x\in\mathbb R^d:x_i\ge0\ (1\le i\le d),\quad x_i+x_{i+1}\le s+\mathbf1_{2\mid i}\ (1\le i<d)\bigr\}.
\]
Here \(\mathbf1_{2\mid i}\) is one for even \(i\) and zero otherwise. **The Ehrhart ring of \(P_d^{(s)}\) is Gorenstein exactly when \(s=1\) and \(d\) is even, or when \((d,s)=(2,3)\).** Its index is three in the former cases and one in the latter. In particular, for every \(s\ge2\) and \(d\ge3\), the polytope is not Gorenstein. Equivalently, its reduced Ehrhart \(h^*\)-polynomial is not palindromic.

This settles the Gorenstein-parameter classification requested in Question Q1 of Jiang--Wen--Zhong (2026) for all even dimensions, and additionally classifies the odd-dimensional members.

## Assumptions and scope
Parameters \(s,d\) are positive integers with \(d\ge2\) and \(s\ge1\), exactly as in the source's path model. The halfspaces are the nonnegative coordinate inequalities and alternating adjacent-sum upper bounds, with the first edge having bound \(s\). Total unimodularity of the path's edge--vertex incidence system and the integer right-hand sides give integrality; the positive small-coordinate points show full dimension. Every coordinate is bounded because it belongs to a positive-capacity path edge. No cyclic closure, higher-period model, or real-valued parameter is asserted.

A lattice polytope \(P\) is Gorenstein of index \(q\) if a positive integer \(q\) and a lattice point \(c\in\operatorname{int}(qP)\) exist such that \(qP-c\) is reflexive, i.e. every primitive integral facet normal has lattice distance one from the origin. Equivalently its Ehrhart ring is Gorenstein. These two conditions require checking **all actual facets**, not every inequality of a potentially redundant description.

## Proof
**Facet-distance principle.** Each coordinate lower bound \(x_j\ge0\) is a facet of \(P_d^{(s)}\). Indeed, setting \(x_j=0\) and all other coordinates to a sufficiently small positive \(\varepsilon\) makes every other defining inequality strict; this also proves full dimension. Suppose \(P_d^{(s)}\) is Gorenstein, with \(qP_d^{(s)}-c\) reflexive. Its coordinate facets have primitive normals \(-e_j\). Their lattice distances from \(c\) inside \(qP_d^{(s)}\) are \(c_j\), so reflexivity forces
\[
c_1=c_2=\cdots=c_d=1. \tag{1}
\]
If an upper inequality \(x_i+x_{i+1}\le b_i\) is a genuine facet, then the corresponding scaled facet in \(qP_d^{(s)}\) has primitive normal \(e_i+e_{i+1}\). Its lattice distance from \(c\) is \(qb_i-c_i-c_{i+1}=qb_i-2\); hence
\[
qb_i=3. \tag{2}
\]

**Two types of active upper facets.** The first edge \(x_1+x_2\le s\) is always a facet: set \(x_1=x_2=s/2\), and choose every other coordinate sufficiently small and positive. This saturates exactly that upper bound. If \(s\ge2\) and \(d\ge3\), the second edge \(x_2+x_3\le s+1\) is also a facet: set \(x_2=x_3=(s+1)/2\), and all other coordinates to a sufficiently small positive \(\varepsilon<(s-1)/2\). The immediately neighboring odd bounds remain strict since \((s+1)/2+\varepsilon<s\), as do all remaining bounds. Thus (2) requires simultaneously \(qs=3=q(s+1)\), an impossibility. This excludes every \(s\ge2\) in every dimension \(d\ge3\).

If \(s=1\) and \(d\ge3\) is odd, the final upper edge has even index \(d-1\), hence capacity two. It is a facet: take \(x_{d-1}=\varepsilon\), \(x_d=2-\varepsilon\), and every earlier coordinate \(\varepsilon\), for sufficiently small positive \(\varepsilon\) (e.g. \(0<\varepsilon<1/3\)). All other edge bounds remain strict. Together with the first edge of capacity one, equation (2) would require \(q=3\) and \(2q=3\), another impossibility. This excludes odd \(d\) when \(s=1\).

**The surviving cases.** In dimension \(d=2\), the only upper facet has capacity \(s\); equation (2) requires the positive integer solution \(qs=3\), giving precisely \((s,q)=(1,3)\) or \((3,1)\). Both suffice: the scaled triangle \(qP_2^{(s)}\), shifted by \((1,1)\), has the three primitive facet equations \(y_1\ge-1\), \(y_2\ge-1\), \(y_1+y_2\le1\), so is reflexive.

For \(s=1\) and even \(d=2r\), every odd adjacent-sum constraint bounds one disjoint pair \((x_{2j-1},x_{2j})\) by one. Consequently \(0\le x_i\le1\) and every intervening even-indexed constraint \(x_{2j}+x_{2j+1}\le2\) is redundant. Thus
\[
P_{2r}^{(1)}=T^r,\qquad T=\{(u,v):u,v\ge0,\ u+v\le1\}.
\]
The translated dilation \(3P_{2r}^{(1)}-\mathbf1\) has exactly the facet inequalities \(y_i\ge-1\) and \(y_{2j-1}+y_{2j}\le1\); their normals are primitive, all facet offsets are one, and the origin is interior. It is reflexive. Thus the index is three, completing the necessary-and-sufficient classification. In both surviving families the stated index is minimal, since equation (2) forces it.

## Verification
The proof holds for every admissible integer pair; finite calculations are auxiliary. The accompanying dependency-free Python program `check.py` computes Ehrhart lattice-point counts by exact integer transfer summation, extracts \(h^*\)-vectors by the exact binomial inversion, and compares palindromicity with the theorem for all \(2\le d\le10\), \(1\le s\le8\). Its output is `ALTERNATING_GORENSTEIN_CHECK_OK cases=72`. Representative computations include \(h^*(P_3^{(1)},z)=1+4z\), \(h^*(P_4^{(1)},z)=1+4z+z^2\), and \(h^*(P_4^{(3)},z)=1+90z+284z^2+94z^3+z^4\). The finite checks alone do not prove the classification.

Run with `python3 check.py` (Python standard library only). Source, hypotheses, and output are self-contained in the embedded file.

## Relationship to prior work
Jiang, Wen and Zhong (arXiv:2607.14887v1, July 16, 2026) establish \(s=1\) in every even dimension and \((d,s)=(2,3)\), prove some higher-dimensional non-Gorenstein cases, and pose an all-even-dimensional characterization as Question Q1. They do not state the exclusion for every \(s\ge2\) and \(d\ge3\). The present facet-distance argument yields that exclusion uniformly and also settles the odd-dimensional cases.

Ohsugi--Hibi and Miyazaki study Gorenstein properties of ordinary stable-set polytopes with **uniform unit** clique bounds. Hamano--Hibi--Ohsugi study fractional stable-set polytopes with **uniform unit** edge bounds. These do not directly impose the conflicting facet distances for alternating capacities \(s,s+1\). The reflexivity criterion itself is classical and is used here openly; the classification is a new specialization in the recent explicit problem family, not a claim that the general criterion is new.

## Limitations
The theorem concerns only the stated path family and does not characterize Gorenstein members of cyclic or arbitrary higher-period variants. Historical priority is provisional, and an equivalent formulation under weighted stable-set terminology could pre-exist. The criterion is elementary once genuine facets are identified; its value is the complete resolution of the explicit parameter classification, not a new general method. No independent scientific audit is asserted.

## References
1. Xinru Jiang, Suzhen Wen, Yueming Zhong, *Alternating adjacent-sum polytopes: transfer matrices and Ehrhart series*, arXiv:2607.14887v1 (first public July 16, 2026), particularly Theorem 1.9, Proposition 3.21, Corollary 3.24, and Question Q1. https://arxiv.org/html/2607.14887v1
2. Mitsuhiro Miyazaki, *On the Gorenstein property of the Ehrhart ring of the stable set polytope of an h-perfect graph*, arXiv:2005.03259 (2020), Sections 1 and 3. https://arxiv.org/abs/2005.03259
3. Ginji Hamano, Takayuki Hibi, Hidefumi Ohsugi, *Ehrhart series of fractional stable set polytopes of finite graphs*, arXiv:1603.09613 (2016), Introduction. https://arxiv.org/abs/1603.09613
