# Balanced normal bundles at the first numerical threshold in \(\operatorname{Gr}(2,3k+1)\)

## Finding
For every integer \(k\ge 2\), over \(\mathbf C\), the normal bundle of a general smooth nondegenerate rational curve of Plücker degree \(d=4k-1\) in \(\operatorname{Gr}(2,3k+1)\) is
\[
N_{C/\operatorname{Gr}(2,3k+1)}\simeq
\mathcal O_{\mathbf P^1}(2k+1)^{\oplus(5k-3)}
\oplus \mathcal O_{\mathbf P^1}(2k+2)^{\oplus k}.
\]
In particular, this infinite family is balanced; the first case is degree seven in \(\operatorname{Gr}(2,7)\), with splitting \(\mathcal O(5)^{\oplus7}\oplus\mathcal O(6)^{\oplus2}\). It supplies an infinite series on the sharp boundary of the Coskun–Larson–Vogt numerical obstruction: writing \(d=2q_1+r_1=(3k-1)q_2+r_2\), one has
\[
(q_1,r_1,q_2,r_2)=(2k-1,1,1,k),\qquad
q_1+q_2=(2-r_1)(3k-1-r_2)+1.
\]
The claimed novelty is this precise positive infinite family of the balancedness conjecture, not the general conjecture, the classical normal bundle of a rational normal curve, or the universal two-balanced bound.

## Assumptions and scope
Fix an integer \(k\ge2\), and work over \(\mathbf C\). The notation \(\operatorname{Gr}(2,n)\) refers to the Grassmannian of two-dimensional subspaces of \(\mathbf C^n\). A map from \(\mathbf P^1\) has Plücker degree \(d\) when the restriction of the Plücker polarization has degree \(d\). A curve is nondegenerate here when its constituent two-dimensional subspaces collectively span the full ambient vector space. A vector bundle on \(\mathbf P^1\) is balanced when the largest and smallest degrees of its line-bundle summands differ by at most one.

## Proof
**Construction.** Put \(m=2k-1\) and split the ambient vector space as \(V=V_1\oplus V_2\) with \(\dim V_1=m+1=2k\) and \(\dim V_2=k+1\). Define \(f:\mathbf P^1\to \operatorname{Gr}(2,V)\) by the row span of
\[
\left(\begin{array}{c|c}
 x^m,x^{m-1}y,\ldots,y^m&0,\ldots,0\\
 0,\ldots,0&x^{2k},x^{2k-2}y^2,\ldots,y^{2k}
\end{array}\right).
\]
The two rows never vanish and lie in complementary summands of \(V\). Their degrees are \(m\) and \(2k\), so the pullback of the tautological subbundle is
\[
S\simeq\mathcal O(-m)\oplus\mathcal O(-2k),\qquad
\deg f^*\mathcal O_{\operatorname{Gr}}(1)=m+2k=4k-1.
\]
The first row alone is the complete degree-\(m\) Veronese embedding \(\mathbf P^1\hookrightarrow\mathbf P(V_1)\). Since the two-plane recovers its intersection line with \(V_1\), \(f\) is a closed immersion. The first and second row polynomials each span their full coordinate blocks, so the resulting curve is nondegenerate.

**The tautological quotient.** Restricting the universal exact sequence along \(f\) and using the direct sum \(V_1\oplus V_2\), the quotient is \(Q\simeq Q_1\oplus Q_2\), where
\[
0\to\mathcal O(-m)\to \mathcal O^{m+1}\to Q_1\to0,
\qquad
0\to\mathcal O(-2k)\to\mathcal O^{k+1}\to Q_2\to0.
\]
For the first map, its adjacent polynomial syzygies are \(-y e_j+x e_{j+1}\), and yield \(Q_1^*\simeq\mathcal O(-1)^m\), hence \(Q_1\simeq\mathcal O(1)^m\). For the second map, the corresponding syzygies are \(-y^2e_j+x^2e_{j+1}\); they yield \(Q_2\simeq\mathcal O(2)^k\). Exactness follows directly because the rows have no common zero and these adjacent relations generate the pointwise kernel; equivalently each is a pullback of the evaluation sequence for the complete series on \(\mathbf P^1\).

**Restricted tangent and the differential.** The identity \(T_{\operatorname{Gr}}\simeq S^*\otimes Q\) gives a canonical four-block splitting
\[
 f^*T_{\operatorname{Gr}}=E_{11}\oplus E_{12}\oplus E_{21}\oplus E_{22},
\]
where
\[
 E_{11}=\mathcal O(2k)^{2k-1},\quad
 E_{12}=\mathcal O(2k+1)^k,\quad
 E_{21}=\mathcal O(2k+1)^{2k-1},\quad
 E_{22}=\mathcal O(2k+2)^k.
\]
Projecting the differential \(df:\mathcal O(2)\to f^*T_{\operatorname{Gr}}\) to \(E_{11}\) gives the differential of the degree-\(m\) Veronese map. Under the adjacent syzygy basis for \(Q_1^*\), the projected differential is precisely the nowhere-zero vector of sections
\[
(x^{m-1},x^{m-2}y,\ldots,y^{m-1}),
\]
viewed as a map \(\mathcal O(2)\to\mathcal O(m+1)^m\). To check this identity directly, pair \(\partial_y(x^{m-j}y^j)\) with the adjacent syzygy \(-y e_j+x e_{j+1}\), and divide the resulting homogeneous expression by \(x\); the result is \(x^{m-j-1}y^j\). This formula extends across \(x=0\) since the displayed homogeneous vector is globally defined.

The dual of this map, twisted by \(\mathcal O(m+1)\), is the evaluation surjection of the complete series \(H^0(\mathbf P^1,\mathcal O(m-1))\). Its kernel is \(\mathcal O(-1)^{m-1}\). Dualizing and twisting back gives the exact sequence
\[
0\longrightarrow\mathcal O(2)\longrightarrow E_{11}
\longrightarrow\mathcal O(m+2)^{m-1}\longrightarrow0.
\]
Since the projection of \(df\) onto \(E_{11}\) is a subbundle injection, quotienting the full four-block tangent bundle gives a second short exact sequence
\[
0\longrightarrow E_{12}\oplus E_{21}\oplus E_{22}
\longrightarrow N_f\longrightarrow \mathcal O(m+2)^{m-1}\longrightarrow0.
\]
Here \(m+2=2k+1\). Every summand of the left term has degree \(2k+1\) or \(2k+2\). Because \(H^1(\mathbf P^1,\mathcal O)=H^1(\mathbf P^1,\mathcal O(1))=0\), the extension splits. Counting summands gives
\[
N_f=\mathcal O(2k+1)^{\oplus(k+2k-1+2k-2)}
\oplus\mathcal O(2k+2)^{\oplus k},
\]
which is the asserted splitting. Its rank is \(6k-3\), and its degree is \((3k+1)(4k-1)-2\), as required by the tangent exact sequence.

**Passage to a general curve.** The degree-fixed scheme of maps \(\mathbf P^1\to\operatorname{Gr}(2,3k+1)\) is irreducible (Kim–Pandharipande, as invoked in Coskun–Larson–Vogt). Immersivity, embedding, and spanning the full ambient space are open conditions on the relevant parameter family. Balancedness of a normal bundle on \(\mathbf P^1\) is also open: it is equivalent to \(H^1(\mathbf P^1,\operatorname{End}(N_f))=0\), and the latter holds for and only for splitting gaps at most one. Since the displayed point satisfies each condition, a general smooth nondegenerate curve has the same balanced splitting. The total rank and degree fix the two multiplicities uniquely.

## Verification
A standalone exact-integer checker in `CHECK.py` verifies the displayed monomial syzygies, differential identities, nonvanishing at representative projective points, the numerical obstruction equality, the rank, and the degree for \(2\le k\le10\). It uses only the Python standard library and runs as `python3 CHECK.py`. Those checks corroborate the local calculations; the infinite statement follows from the exact bundle sequences and cohomological splitting argument above, not from finite sampling.

## Relationship to prior work
Coskun–Larson–Vogt (arXiv:2404.08102) prove universal two-balancedness and state the numerical conjecture. Cao (arXiv:2609.19381, first released 2026-09-16) proves it for \(\operatorname{Gr}(2,4)\), \(\operatorname{Gr}(2,5)\), and \(\operatorname{Gr}(2,6)\), but not for the present dimensions \(3k+1\ge7\). Ran (arXiv:2111.02466) gives other infinite families of degrees through degeneration and interpolation; his Theorems 13, 20, 23 and Corollary 24 do not explicitly assert the displayed sharp-boundary family or its normal splitting. In particular, Theorem 13(i)'s degree construction when \(3k\) is odd requires \(e\ge 2\lfloor3k/2\rfloor+(3k-2)\), excluding the displayed \(e=4k-1\) for odd \(k\ge3\). More generally, absence of a verbatim statement alone is not a proof of novelty; the normal-bundle and parameter implications were compared, with residual risk of unindexed equivalent constructions.

## Limitations
This proves only the specific one-parameter degree/dimension series, not the whole numerical conjecture or the balance of arbitrary non-general maps. The proof uses characteristic zero; no assertion is made for positive characteristic, especially characteristic two. It does not classify all rational curves with this splitting. The named existence results and irreducibility/open-locus facts are cited as standard inputs, not reproved here. Independent validation and exhaustive literature coverage have not been performed.

## References
1. A. Cao, *Balancedness of Normal Bundles of Rational Curves in Grassmannians*, arXiv:2609.19381v1 (first posted 2026-09-16), https://arxiv.org/html/2609.19381v1.
2. I. Coskun, E. Larson, I. Vogt, *Normal bundles of rational curves in Grassmannians*, arXiv:2404.08102v1 (first posted 2024-04-11), https://arxiv.org/html/2404.08102v1.
3. Z. Ran, *Interpolation of rational scrolls*, arXiv:2111.02466v1 (2021), https://arxiv.org/html/2111.02466v1.
