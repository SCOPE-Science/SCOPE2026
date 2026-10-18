# Dyadic rigidity of one-gap two-binomial complexity for the Thue–Morse word

## Finding
Let \(\mathbf t=0110100110010110\cdots\) be the fixed point beginning with zero of \(\varphi(0)=01\), \(\varphi(1)=10\). For each length \(n\), let \(b_{\mathbf t}^{(1,2)}(n)\) denote the number of equivalence classes of its length-\(n\) factors under equality of all one-symbol counts and all two-symbol scattered-subword counts with **at least one unselected position between the selected positions**. Then
\[
\boxed{b_{\mathbf t}^{(1,2)}(2^m)=12\quad\text{for every integer }m\ge3.}
\]
This proves the dyadic-specialization assertion explicitly predicted by Rigo, Stipulanti and Whiteland in their 2023 conjecture, without claiming their full proposed two-regularity statement.

## Assumptions and scope
All words are binary and indexed from zero. For \(a,b\in\{0,1\}\), let \(G_{ab}(w)\) count pairs \(0\le i<j<|w|\) with \(j-i\ge2\), \(w_i=a\), \(w_j=b\). A factor's complete observation is its vector \(P(w)=(|w|_1,G_{00},G_{01},G_{10},G_{11})\); the omitted zero count is its length minus the first coordinate. Fix \(m\ge3\), put \(n=2^m\), \(h=n/2\), \(e=m\bmod2\), and \(T=\varphi^m(0)\). A bar denotes bitwise complementation. Write \(\mathbf u_{ab}\) for the unit vector at coordinate \(ab\), ordered \((00,01,10,11)\).

## Proof
**1. Reduction to four families of block cuts.** The infinite fixed point is partitioned into consecutive length-\(n\) blocks, each equal to \(T\) or \(\overline T\), with block labels again forming \(\mathbf t\). Every binary adjacent pair occurs in \(\mathbf t\), as is already visible in \(\varphi^3(0)=01101001\). Consequently **all** length-\(n\) factors are exactly the words
\[
W_{a,b,r}=A[r:n]B[0:r],\qquad A\in\{T,\overline T\},\ B\in\{T,\overline T\},\quad0\le r<n,
\]
with all four ordered choices of \(A,B\) allowed. (At \(r=0\) only \(A\) matters.) Complements exchange the two one-symbol counts and exchange the \(00,11\) and \(01,10\) gap counts.

**2. From ordinary subsequences and adjacent pairs to gap counts.** Let \(c=|w|_1\), \(I(w)=\#\{i<j:w_iw_j=01\}\), and \(E(w)=(|w|_{00},|w|_{01},|w|_{10},|w|_{11})\), where these last four counts refer to **adjacent** factors. Then
\[
P(w)=\left(c,\binom{n-c}{2}-E_{00},\ I(w)-E_{01},\ c(n-c)-I(w)-E_{10},\ \binom c2-E_{11}\right).\tag{1}
\]
For \(T=\varphi^m(0)\), \(c=h\), \(I(T)=h^2/2\), and the adjacency vector is
\[
E(T)=\begin{cases}
((h-2)/3,(2h-1)/3,(2h-1)/3,(h+1)/3),&e=0,\\
((h-1)/3,(2h+1)/3,(2h-2)/3,(h-1)/3),&e=1.
\end{cases}\tag{2}
\]
Indeed, every \(\varphi\)-image has one zero and one one, so its contribution to \(I\) is \(\binom h2+|\varphi^{m-1}(0)|_0=h^2/2\). For adjacency counts, each image contributes one internal \(01\) or \(10\), while the boundary between \(\varphi(x)\) and \(\varphi(y)\) equals \((1-x)y\); induction from \(T_2=0110\) proves (2). The endpoints of \(T\) are \(0,e\).

**3. Exact cut enumeration.** Write \(U=\varphi^{m-1}(0)\), so \(T=\varphi(U)\). In the following formulas \(\Delta I=I(W)-h^2/2\), \(\Delta E=E(W)-E(T)\), and a proposed triple \((c,\Delta I,\Delta E)\) is converted to \(P(W)\) by (1), (2). Each row also contributes its bit complement. This is a complete list of **possible** profiles:

| Blocks and cut | Parameters | \(c\) | \(\Delta I\) | \(\Delta E\) |
| --- | --- | --- | --- | --- |
| \(T,T\), \(r=0\) | none | \(h\) | \(0\) | \(\mathbf0\) |
| \(T,T\), \(r=2s>0\) | \(u=U_{s-1},v=U_s\) | \(h\) | \(0\) | \(\mathbf u_{e0}-\mathbf u_{(1-u)v}\) |
| \(T,T\), \(r=2s+1\) | \(u=U_s\) | \(h\) | \(-h(1-2u)\) | \(\mathbf u_{e0}-\mathbf u_{u(1-u)}\) |
| \(T,\overline T\), \(r=2s>0\), even \(s\) | \(u=U_{s-1},v=U_s\) | \(h\) | \(0\) | \(\mathbf u_{e1}-\mathbf u_{(1-u)v}+(u,u-1,1-u,-u)\) |
| \(T,\overline T\), \(r=2s>0\), odd \(s\) | \(u=U_{s-1},v=1-u\) | \(h\) | \(2u-1\) | \(\mathbf u_{e1}-\mathbf u_{(1-u)v}+(u,u-1,1-u,-u)\) |
| \(T,\overline T\), \(r=2s+1\), even \(s\) | \(u=U_s\) | \(h+1-2u\) | \(u-1\) | \(\mathbf u_{e1}-\mathbf u_{u(1-u)}+(u,-u,u,-u)\) |
| \(T,\overline T\), \(r=2s+1\), odd \(s\) | \(u=U_s\) | \(h+1-2u\) | \(-u\) | \(\mathbf u_{e1}-\mathbf u_{u(1-u)}+(u,-u,u,-u)\) |

For the even-cut rows with even \(s\), \((u,v)\) is initially allowed to range over all four pairs, while every single-bit parameter ranges over \(\{0,1\}\). There is no independent odd-\(s\) parameter \(v\): the two entries of a substituted pair are complementary. These rows follow by deleting the adjacency edge crossing the cut, inserting its new join edge, and complementing the moved prefix in the mixed-block case. More explicitly, for \(r=2s\), complementing the prefix changes the internal adjacency counts by \((u,u-1,1-u,-u)\); for \(r=2s+1\) this change is \((u,-u,u,-u)\). The corresponding inversion-count changes are shown in the table, obtained by separating ordered pairs within the two pieces and those crossing the cut. These formulas do not assume that all parameter choices occur at small \(m\), so they also give a uniform upper bound.

**4. Exactly twelve distinct vectors.** Substitution of the seven rows into (1)--(2), adjoining complements and simplifying quadratic expressions in \(h\), produces exactly twelve **different polynomial vectors** for each \(e\): eight have first coordinate \(h\), two have \(h-1\), and two have \(h+1\). In particular, there are never more than twelve profiles. The companion `verify.py` performs this finite algebra in exact rational polynomial arithmetic: it computes all polynomial tuples and, for each distinct pair, identifies a coordinate difference whose coefficients after replacing \(h\) by \(4+t\) have one strict sign for every \(t\ge0\). Thus no accidental collision occurs at any permitted \(h=2^{m-1}\ge4\).

For \(m\ge5\), all the parameter choices that yield these twelve tuples actually occur: \(U=\varphi(V)\) with \(V=\varphi^{m-2}(0)\), and \(V\) contains all four ordered digrams. These realize all four pairs \((U_{s-1},U_s)\) at even positive \(s\), while the internal complementary pairs at odd \(s\) realize both single-bit values. Both letters also appear at both parities required for odd cuts. Each displayed class therefore has a realizing factor. The two remaining cases \(m=3,4\) have respectively twelve distinct profiles by direct listing of the \(4\cdot2^m\) block cuts; the exhaustive two-loop comparison is explicitly reproducible by `verify.py`, and only these two finite base cases are delegated to enumeration. Hence the count equals twelve for every \(m\ge3\). \(\square\)

## Verification
Run `python3 verify.py` from this directory; no dependencies other than the Python standard library are needed. It verifies the symbolic twelve-class calculation for both parities, and proves a noncollision sign certificate for **all real \(h\ge4\)**. It independently enumerates all admissible gap pairs for every cut at lengths \(8,16,32,64,128\), and separately scans contiguous factors from long substitution prefixes at lengths \(8,16,32,64\). These finite checks corroborate, but do not replace, the all-length argument.

## Relationship to prior work
Rigo, Stipulanti and Whiteland (2023), Section IV, Conjecture 4.3 (notation in their published manuscript), conjecture a full two-regular representation for this complexity and explicitly note as its consequence the unproved identity \(b_{\mathbf t}^{(1,2)}(2^m)=12\) for \(m\ge3\). The result here proves that **one stated consequence**, without asserting their full conjecture. Lejeune, Leroy and Rigo (2020) determine the *ordinary* binomial complexity (including adjacent subsequence choices); Greinecker (2015) studies two-abelian complexity. Neither invariant identifies the present one-gap classes. published-finding corpus comparisons found adjacent-pair spectra of arbitrary finite binary words, local composition reconstruction, and subsequence-universality counts, but not the statement or an implication covering it.

## Limitations
No assertion is made for non-dyadic lengths, higher gap widths, higher deck orders, the full two-regular conjecture, or independent audit. The research comparison is bounded by inspected accessible literature; a previously unnoticed proof of the same dyadic consequence remains possible. The polynomial certificate checks algebraic simplification while the text establishes why the finite parameter table exhausts all factors.

## References
1. M. Rigo, M. Stipulanti and M. A. Whiteland, *Gapped Binomial Complexities in Sequences*, IEEE ISIT (2023), pp. 1294–1299; official publicly accessible full text: https://orbi.uliege.be/bitstream/2268/302524/1/isit2023.pdf ; repository record: https://orbi.uliege.be/handle/2268/302524 (first public availability 2023-05-11).
2. M. Lejeune, J. Leroy and M. Rigo, *Computing the k-binomial complexity of the Thue-Morse word*, Journal of Combinatorial Theory A **176** (2020), 105284; preprint: https://arxiv.org/abs/1812.07330 .
3. F. Greinecker, *On the 2-abelian complexity of the Thue-Morse word*, Theoretical Computer Science **593** (2015), 88–105.
4. R. Golm, M. Nahvi, R. Gabrys and O. Milenkovic, *The gapped k-deck problem*, IEEE ISIT (2022), 49–54.
