# Ordinary class sizes and the number of involutions do not determine involution class sizes

## Finding

On the vertex set \(\{0,1,2,3,4,5,6\}\), take the two graphs with edges
\[
 E_A=\{01,03,04,13,14,16,24,25\},\qquad E_B=\{01,02,04,05,12,23,45,56\}.
\]
Their graphical groups \(G_A(q),G_B(q)\) have the same number of conjugacy classes of each size at every prime power \(q\). For \(q=2^f\) with \(f\ge 1\), they also have the same number of elements of order dividing two, but their class-size enumerators restricted to these elements differ:
\[
 H_A(q,T)-H_B(q,T)=q^3(q-1)^2T^2(T-q)^3,
\]
where the coefficient of \(T^r\) counts classes of size \(q^r\). In particular the groups are nonisomorphic at every even \(q\). The identity is included in \(H\); subtracting one from the constant coefficient of each enumerator gives the same difference for exact order two.

At \(q=2\) both groups have order \(32768\), with \(7424\) elements of order dividing two. The coefficient vectors in increasing exponent order are \((256,256,256,416,112,16)\) and \((256,256,320,320,160,8)\), respectively.

## Definitions and proof

For a finite simple graph \(\Gamma=(V,E)\) with ordered vertices, use the algebra \(J\) over \(\mathbb F_q\) with basis \(x_v\) and \(z_{uv}\) for vertices and edges, respectively. Its only nonzero basis products are \(x_u x_v=z_{uv}\) for edges with \(u<v\). Since \(J^3=0\), \(1+J\) is a group. Let \(e=|E|\), \(S\) be the support of the vertex coordinates of an element, and \(N(S)\) be the vertices outside \(S\) adjacent to \(S\).

Two elements \(1+a,1+b\) commute just when their vertex coordinates satisfy \(a_u b_v-a_v b_u=0\) on every edge. For \(a\) with support \(S\), the constraints set \(b_w=0\) for every \(w\in N(S)\) and make \(b_v/a_v\) constant on each connected component of \(\Gamma[S]\). Thus the class size is \(q^{\rho(S)}\), where \(\rho(S)=|S|+|N(S)|-c(\Gamma[S])\) and \(c\) counts connected components, with \(c(\Gamma[\varnothing])=0\). Conjugation preserves the vertex coordinates since the quotient by the central edge subspace is abelian. There are \((q-1)^{|S|}q^e\) elements with support \(S\). Dividing by the class size gives the term \((q-1)^{|S|}q^{e-\rho(S)}T^{\rho(S)}\) in the ordinary class enumerator.

In characteristic two, the square of \(1+a\) is \(1+\sum_{uv\in E,u<v}a_ua_v z_{uv}\). The element therefore has order dividing two exactly when \(S\) is independent. On these supports, \(\rho(S)=|N(S)|\), giving the auxiliary restricted enumerator
\[
 H_\Gamma(q,T)=\sum_{S\text{ independent}}(q-1)^{|S|}q^{e-|N(S)|}T^{|N(S)|}.
\]

Enumerate the \(128\) masks of the seven vertices in each graph. For each, form \(S\), collect the outside endpoints of edges meeting \(S\) to obtain \(N(S)\), count components of the induced graph on \(S\) (including isolates), and tally \((|S|,\rho(S))\). In a separate tally keep only masks that contain no edge. The ordinary tallies agree, and the independent-set size counts for sizes zero through four are \((1,7,13,7,1)\) in both graphs, with no larger independent sets. Hence the square-one totals agree and equal \(q^8(1+7(q-1)+13(q-1)^2+7(q-1)^3+(q-1)^4)\). In the independent-support tallies, the only nonzero differences \(A-B\) are at \(|S|=2\), with differences \((-1,3,-3,1)\) in columns \(\rho=2,3,4,5\). Their weighted sum is
\[
(q-1)^2(-q^6T^2+3q^5T^3-3q^4T^4+q^3T^5)=q^3(q-1)^2T^2(T-q)^3.
\]
The polynomial is nonzero for every stated even field size. Neither the ordinary class-size spectra nor the square-one totals distinguish this pair, while the restricted class distribution does.

## Reproduction and scope

The unchanged `CERTIFICATE.json` contains both exhaustive support tallies; use `python3 verify.py` in the source package to recompute them and the formal polynomial comparison. The 128 masks for each graph are the entire support domain. Field-uniformity follows from the commutation and square calculations, not from testing field sizes. Neither minimality nor classification of such pairs is asserted.

## Relationship to other results

Rossmann, *Enumerating conjugacy classes of graphical groups over finite fields*, [arXiv:2107.05564v3](https://arxiv.org/abs/2107.05564v3), Theorem A and equation (1.3), gives the unrestricted graph-to-class enumeration. The auxiliary square-one enumerator is also stated coefficient by coefficient in [*Characteristic-two graphical groups: involution classes and maximal elementary abelian subgroups*](https://github.com/Resultary/2026/tree/main/2026/11/2/SCOPE-characteristic-two-graphical-groups-involution-classes-and-maxim--3e561a32bdb5), Finding part 1. Neither general formula is claimed as a contribution here. The contribution is the specific obstruction: knowing both marginal statistics does not determine the class-size spectrum on elements of order two. No claim of priority against unexamined work is made.
