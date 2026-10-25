# Unequal-arm theta graphs give a 34-dimensional failure of Ehrhart gamma-positivity

## Finding
Let \(G(6,8,8,8,8)\) be the two-terminal graph consisting of five internally vertex-disjoint paths of respective lengths \(6,8,8,8,8\). Its symmetric edge polytope \(Q_G\) has dimension \(34\) and Ehrhart \(h^*\)-polynomial with gamma coefficient
\[
\boxed{\gamma_{15}(Q_G)=-236544.}
\]
Thus \(Q_G\) is not gamma-positive. This example has dimension two lower than the 36-dimensional equal-arm example explicitly exhibited by Ferroni (2026). No claim is made that dimension 34 is minimal among all symmetric edge polytopes.

A structural formula underlying the example computes the entire Ehrhart \(h^*\)-polynomial of every theta graph \(G(a_1,\ldots,a_m)\) with \(m\ge2\) and path lengths \(a_r\ge2\) all having the same parity. It specializes to Ferroni's equal-arm formula but allows independently varying path lengths.

## Assumptions and scope
For integers \(m\ge2\) and \(a_1,\ldots,a_m\ge2\) of common parity, let \(G(a_1,\ldots,a_m)\) have distinct terminals \(s,t\), with \(m\) otherwise vertex-disjoint undirected \(s\)-\(t\) paths. Let
\[
Q_G=\operatorname{conv}\{e_u-e_v,e_v-e_u:\{u,v\}\in E(G)\}
\]
in the rank-\((|V(G)|-1)\) root lattice. Its dimension is
\[
d=\sum_{r=1}^{m}a_r-m+1.\]
Define \(h_G^*(z)\) by \(\sum_{q\ge0}|qQ_G\cap\mathbb Z^{|V(G)|-1}|z^q=h_G^*(z)/(1-z)^{d+1}\) in a primitive root-lattice coordinate system. Define its gamma coefficients through
\[
h_G^*(z)=\sum_{j=0}^{\lfloor d/2\rfloor}\gamma_j z^j(1+z)^{d-2j}.\]
These coefficients exist uniquely because \(Q_G\) is reflexive and its Ehrhart numerator is palindromic. The formula below concerns this precise normalization, not the ordinary edge-polytope Ehrhart polynomial.

## Proof
**Step 1: exact unequal-arm formula.** Set
\[
\mathcal H=\{h\in\mathbb Z:|h|\le\min_r a_r,\ h\equiv a_1\pmod2\},\qquad i_r(h)=(a_r+h)/2.
\]
For each \(h\in\mathcal H\) and path \(r\), set
\[
A_r(h,z)=\binom{a_r}{i_r(h)}z^{i_r(h)}.
\]
With \(i=i_r(h)\) and \(a=a_r\), also set
\[
B_r^+(h,z)=\sum_{u=0}^{i-1}\sum_{v=0}^{a-i}
\binom{u+v}{u}\binom{a-1-u-v}{i-1-u}
 z^{a-i+u-v},
\]
\[
B_r^-(h,z)=\sum_{u=0}^{i}\sum_{v=0}^{a-i-1}
\binom{u+v}{u}\binom{a-1-u-v}{i-u}
 z^{a-i-1+u-v},
\]
where an empty sum is zero. Then the claimed general formula is
\[
\boxed{
h_G^*(z)=\sum_{h\in\mathcal H}\sum_{k=1}^m
 A_k(h,z)\prod_{r<k}B_r^+(h,z)\prod_{r>k}B_r^-(h,z).
}
\]
To prove it, first observe that the graph is bipartite because all terminal-to-terminal paths have the same parity. As in Ferroni's facet analysis, a facet functional has integer consecutive differences of absolute value at most one, its tight-edge subgraph is spanning and connected, and parity along tight edges forces *every* graph edge tight. A facet is therefore specified by a sign word on each path, with a common total signed height \(h\) from \(s\) to \(t\). The number of plus signs on path \(r\) is \(i_r(h)\).

Embed the paths in cyclic order. The planar-dual arborescence dissection used in Ferroni's proof and the spanning-tree activity theorem of Kálmán--Tóthmérész work without equal path lengths. A dual spanning tree omits one bundle (leaving primal path \(k\) intact) and selects one dual edge from each other bundle (deleting one primal edge). The deleted edge has sign plus on paths before \(k\) and minus on paths after \(k\), after fixing one of the equivalent planar conventions. This yields one dissecting spanning tree for every such sign-word and deletion choice. The activity theorem counts the edges directed away from \(s\).

The intact path contributes one away-pointing edge for each plus sign, giving \(A_k\). If a deleted edge lies after \(u\) plus and \(v\) minus signs, then the surviving path has \(u\) away-pointing plus edges on its \(s\)-side, and all minus edges after deletion point away from \(s\) through the intact path. For a deleted plus edge, this gives exponent \(a-i+u-v\), with word count \(\binom{u+v}{u}\binom{a-1-u-v}{i-1-u}\). For a deleted minus edge, the exponent is \(a-i-1+u-v\), with count \(\binom{u+v}{u}\binom{a-1-u-v}{i-u}\). Summing these independent path contributions proves the formula.

**Step 2: exact arithmetic specialization.** Set \((a_1,\ldots,a_5)=(6,8,8,8,8)\), so \(d=6+4\cdot8-5+1=34\) and \(\mathcal H=\{-6,-4,-2,0,2,4,6\}\). Evaluating the finite polynomial sum gives the palindromic Ehrhart numerator with coefficients, in ascending degree,
\[
\begin{aligned}
(&1,42,865,11648,115384,897008,5702136,30482912,139665036,\\
&554547384,1915733708,5748320992,14901043080,33127191568,\\
&62631833544,99751615936,132545819462,145853691452,\\
&132545819462,99751615936,62631833544,33127191568,\\
&14901043080,5748320992,1915733708,554547384,139665036,\\
&30482912,5702136,897008,115384,11648,865,42,1).
\end{aligned}
\]
The triangular basis conversion
\[
\gamma_j=h_j^*-\sum_{i=0}^{j-1}\gamma_i\binom{34-2i}{j-i}
\quad(0\le j\le17)
\]
then gives, in ascending index,
\[
(\gamma_0,\ldots,\gamma_{17})=
(1,8,48,256,1280,6144,28672,117344,379536,1019456,
2433408,5081472,10692480,19652864,23686656,-236544,0,0).
\]
In particular the displayed negative coefficient is exact, proving the failure of gamma-positivity. The graph has \(35\) vertices, hence the polytope has dimension \(34\).

## Verification
Run \(\texttt{python verify.py}\) with Python 3 and no nonstandard dependencies. The program independently computes the polynomial (a) by closed binomial sums and (b) by enumerating binary orientation words and deleted-edge positions, and checks equality on the claimed graph, the published equal-arm benchmark, and several smaller unequal-arm graphs. It also checks palindromicity, the coefficient \(h_1^*=2|E(G)|-d=42\), the complete gamma-basis reconstruction, the exact coefficient \(\gamma_{15}=-236544\), and invariance under all five placements of the shorter arm. Successful output begins \(\texttt{EXACT_OK}\). All calculations use exact integers. The general formula follows from the dissection proof; finite checks alone are not a proof for arbitrary lengths.

## Relationship to prior work
Ferroni's arXiv:2607.02424 (first public July 2, 2026) proves non-gamma-positivity for symmetric edge polytopes and computes an equal-arm theta example \(G(8,8,8,8,8)\) in dimension \(36\), with \(\gamma_{16}=-9799680\). Its Proposition 2.1 treats equal arm lengths, explicitly suggesting formulas for arbitrary arm vectors but not giving them. The present result uses that same dissection principle to obtain an all-common-parity, unequal-arm formula and an explicit dimension-34 witness. The Kálmán--Tóthmérész spanning-tree activity theorem is the essential pre-existing enumerative input, not claimed here as new. Earlier gamma-positivity and gamma-coefficient results of Ohsugi--Tsuchiya and D'Alì et al. concern background positivity constraints and do not state this exact example.

## Limitations
The result does **not** establish a minimum counterexample dimension, a classification of all non-gamma-positive symmetric edge polytopes, or a global statement for theta graphs whose arm lengths have mixed parity. Priority is subject to further historical review, particularly for independently tabulated irregular theta graphs. The proof assumes the established planar-dual dissection and spanning-tree activity theorems; the exact integer specialization has two reproducible implementations. Independent validation has not been performed.

## References
1. L. Ferroni, *Symmetric edge polytopes are not gamma-positive*, arXiv:2607.02424 (first posted July 2, 2026), https://arxiv.org/abs/2607.02424.
2. T. Kálmán and L. Tóthmérész, *\(h^*\)-vectors of graph polytopes using activities of dissecting spanning trees*, Algebraic Combinatorics 6 (2023), 1637–1651, DOI:10.5802/alco.318, https://alco.centre-mersenne.org/articles/10.5802/alco.318/.
3. H. Ohsugi and A. Tsuchiya, *The \(h^*\)-polynomials of locally anti-blocking lattice polytopes and their gamma-positivity*, Discrete Comput. Geom. 66 (2021), 701–722.
4. A. D'Alì, M. Juhnke-Kubitzke, D. Köhne, and L. Venturello, *On the gamma-vector of symmetric edge polytopes*, SIAM J. Discrete Math. 37 (2023), 487–515.
