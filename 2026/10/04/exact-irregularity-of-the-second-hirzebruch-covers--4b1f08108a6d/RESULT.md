# Exact irregularity of the second Hirzebruch covers
## Finding
Let
\[
f'_n:Y'_n\longrightarrow Z'=\operatorname{Bl}_{p_1,\ldots,p_4}\mathbf P^2
\]
be the second classical Hirzebruch family used by Anghel: the branch arrangement is the six lines joining four general points, and \(Y'_n\) is the smooth \((\mathbf Z/n)^5\)-cover obtained after blowing up the four triple points. Then, for every integer \(n\ge2\),
\[
q(Y'_n)=h^1(Y'_n,\mathcal O_{Y'_n})
=5\binom{n-1}{2}
=\frac52(n-1)(n-2).
\]
Using Anghel's formula
\[
\chi(\mathcal O_{Y'_n})=\frac{(7n^2-30n+35)n^3}{12},
\]
one obtains
\[
p_g(Y'_n)=\frac{7n^5-30n^4+35n^3+30n^2-90n+48}{12}.
\]

For the quasi-Gorenstein section rings
\[
R_n=R(Y'_n,H'),\qquad n\ge6,
\]
from Anghel's Corollary 4.3, the standard section-ring/local-cohomology correspondence gives
\[
\dim_{\mathbf C}[H^2_{(R_n)_+}(R_n)]_0
=h^1(Y'_n,\mathcal O_{Y'_n})
=5\binom{n-1}{2}.
\]
Thus the smallest member \(n=6\) has
\[
q(Y'_6)=50,\qquad p_g(Y'_6)=1975,
\qquad \dim_{\mathbf C}[H^2_{(R_6)_+}(R_6)]_0=50.
\]

## Assumptions and scope
The base field is \(\mathbf C\). The four points \(p_1,\ldots,p_4\subset\mathbf P^2\) are in general position, so no three are collinear. Write \(L\) for the pullback of a line and \(E_v\) for the four exceptional curves. The six branch lines are indexed by the edges of the complete graph \(K_4\); a vertex \(v\) corresponds to one of the four triple points.

The family and its smoothness, the \((\mathbf Z/n)^5\)-cover structure, and the Euler-characteristic formula are inputs from the cited literature. The new calculation is the exact irregularity and its consequences for \(p_g\) and the degree-zero local-cohomology defect. No claim is made about the full graded local-cohomology module, the Albanese map, or the cohomology ring.

## Proof
Characters of the deck group can be represented by weights
\[
a=(a_e)_{e\in E(K_4)},\qquad 0\le a_e\le n-1,
\qquad \sum_e a_e\equiv0\pmod n.
\]
Put
\[
d=\frac1n\sum_e a_e,
\qquad
s_v=\sum_{e\ni v}a_e,
\qquad
b_v=\left\lfloor\frac{s_v}{n}\right\rfloor.
\]
Because three edges meet each vertex, \(b_v\in\{0,1,2\}\). The usual abelian-cover eigensheaf formula, in the same notation used by Anghel for the Hesse family and in his explicit irregularity argument for the second family, gives
\[
f'_{n*}\mathcal O_{Y'_n}
=\bigoplus_a L_a^{-1},
\qquad
L_a=dL-\sum_v b_vE_v.
\]
Hence
\[
q(Y'_n)=\sum_a h^1\bigl(Z',L_a^{-1}\bigr).
\]
The trivial character contributes zero because \(Z'\) is rational.

Fix a nontrivial character and set
\[
D=-L_a=-dL+\sum_v b_vE_v.
\]
Since \(D\cdot L=-d<0\), one has \(h^0(Z',D)=0\). Let
\[
k=\#\{v:b_v=2\}.
\]
Riemann--Roch on \(Z'=\operatorname{Bl}_4\mathbf P^2\) gives
\[
\chi(\mathcal O_{Z'}(D))
=1+\frac{d(d-3)}2-k.
\]
By Serre duality,
\[
h^2(Z',D)=h^0\left(Z',(d-3)L+\sum_v(1-b_v)E_v\right).
\]
The terms with \(b_v=0\) are fixed exceptional components; after removing them, each vertex with \(b_v=2\) imposes one simple point condition on a plane curve of degree \(d-3\). Since the four points are general and \(0\le d\le5\), these conditions are independent. Therefore
\[
h^2(Z',D)=
\begin{cases}
0,&d\le2,\\
1,&d=3,\ k=0,\\
0,&d=3,\ k\ge1,\\
\max(3-k,0),&d=4,\\
6-k,&d=5.
\end{cases}
\]
It follows that \(h^1(Z',D)\) can be nonzero only in the following two situations:
\[
(d,k)=(2,1)\quad\text{or}\quad(d,k)=(4,4),
\]
and in either case \(h^1(Z',D)=1\). Here are the required exclusions.

For \(d=1\), the total weight is \(n\), so no vertex sum can reach \(2n\). For \(d=2\), two vertices cannot both have \(b_v=2\): if \(u,v\) were such vertices and \(uv\) and \(wx\) were opposite edges, then
\[
s_u+s_v=2n+a_{uv}-a_{wx}\le3n-1<4n,
\]
contradicting \(s_u+s_v\ge4n\). For \(d=3\), the same identity gives
\[
s_u+s_v=3n+a_{uv}-a_{wx}\le4n-1,
\]
so again at most one vertex has \(b_v=2\); Riemann--Roch then gives \(h^1=0\). For \(d=5\), the computed \(h^2\) equals \(\chi\), so \(h^1=0\). Thus only the two displayed cases remain.

It remains to count them. First take \(d=2\) and fix a vertex \(v\) with \(b_v=2\). Since the total edge weight is exactly \(2n\), the three edges not incident with \(v\) all have weight zero, while the three incident weights \(x,y,z\) satisfy
\[
x+y+z=2n,
\qquad 0\le x,y,z\le n-1.
\]
Writing \(u=n-x\), \(v'=n-y\), \(w=n-z\), this is a positive composition
\[
u+v'+w=n.
\]
There are \(\binom{n-1}{2}\) such triples. The exceptional vertex is unique, so the four choices of vertex give
\[
4\binom{n-1}{2}
\]
characters.

Now take \(d=4\) and \(k=4\). Since
\[
\sum_v s_v=2\sum_e a_e=8n
\]
and every \(s_v\ge2n\), one has \(s_v=2n\) for all four vertices. Solving these four equations shows that opposite edges have equal weights:
\[
a_{12}=a_{34}=x,
\qquad a_{13}=a_{24}=y,
\qquad a_{14}=a_{23}=z,
\]
with
\[
x+y+z=2n,
\qquad 0\le x,y,z\le n-1.
\]
The same positive-composition count gives \(\binom{n-1}{2}\) characters. Summing the two contributions proves
\[
q(Y'_n)=5\binom{n-1}{2}.
\]

Finally,
\[
p_g=\chi+q-1
\]
gives the displayed polynomial. For a section ring \(R(Y'_n,H')\), the standard graded local-cohomology correspondence gives
\[
[H^2_{R_+}(R)]_0\cong H^1(Y'_n,\mathcal O_{Y'_n}),
\]
which proves the degree-zero deficiency statement.

## Verification
The accompanying `verify.py` performs an exact finite replay for \(2\le n\le8\). It enumerates all \(n^5\) characters, computes \(d\), the four integers \(b_v\), Riemann--Roch and Serre-duality dimensions, and verifies that the only nonzero contributions are precisely the \((d,k)=(2,1)\) and \((4,4)\) families. It checks
\[
q(Y'_n)=0,5,15,30,50,75,105
\]
for \(n=2,3,4,5,6,7,8\), matching \(5\binom{n-1}{2}\), and also checks the closed formula for \(p_g\), including \(p_g(Y'_6)=1975\). The general proof is the character classification above; the finite replay is not used as an induction argument.

## Relationship to prior work
Anghel's 2026 paper uses this classical second Hirzebruch family to produce quasi-Gorenstein section rings without graded maximal Cohen--Macaulay modules. It records the cover, the formulas for \(K^2\), \(c_2\), \(\chi(\mathcal O)\), and the polarization \(H'\), and proves only the lower bound
\[
q(Y'_n)\ge1
\]
by exhibiting one character with nonzero \(H^1\). The exact irregularity, the resulting geometric genus, and the degree-zero deficiency dimension are not stated in the inspected text.

Bauer--Catanese study the same complete-quadrangle Hirzebruch--Kummer covers, identify them as \((\mathbf Z/n)^5\)-covers of the degree-five del Pezzo surface, prove rigidity results, and give explicit equations in products of Fermat curves. Their inspected paper is therefore the closest older same-object source. Targeted searches in that text and exact-formula searches did not locate the irregularity formula above.

## Limitations
The calculation is additive and character-theoretic. It does not determine the Albanese variety or Albanese map, the full Hodge diamond beyond what follows from the displayed invariants, or the full graded structure of \(H^2_{R_+}(R)\).

The complete-quadrangle covers are classical and have substantial older literature. Although the closest same-object paper and targeted exact-formula searches were inspected, an unindexed or differently phrased older computation of the same irregularity remains a residual originality risk.

## References
1. C. Anghel, *Polarized varieties without arithmetically Cohen--Macaulay bundles and section rings without graded maximal Cohen--Macaulay modules in characteristic zero*, arXiv:2609.15589v1, submitted 14 September 2026.
2. I. Bauer and F. Catanese, *Del Pezzo surfaces, rigid line configurations and Hirzebruch--Kummer coverings*, Bollettino dell'Unione Matematica Italiana 12 (2019), 43--62, DOI 10.1007/s40574-018-0169-x.
3. R. Pardini, *Abelian covers of algebraic varieties*, Journal für die reine und angewandte Mathematik 417 (1991), 191--214.
