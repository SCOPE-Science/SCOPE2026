# Frobenius eight-cycles on the lines of a characteristic-three quartic K3 pencil

## Finding

Let \(k=\mathbb F_3\). For each \(a\in k\), consider the quartic surface
\[
X_a:\quad x_1^3x_2-x_1x_2^3+x_0^3x_3-x_0x_3^3
 = a x_0^2x_1x_2\quad\subset\mathbb P^3_k.
\]
It is a smooth K3 surface, and its scheme \(F_1(X_a)\) of projective lines is finite étale over \(k\). The complete Frobenius cycle decomposition is
\[
\begin{array}{c|c|c|c}
a&\text{geometric lines}&\text{fixed geometric lines}&\text{nontrivial Frobenius cycles}\\\hline
0&112&40&36\text{ cycles of length }2\\
1&58&10&6\text{ cycles of length }8\\
-1&58&10&6\text{ cycles of length }8.
\end{array}
\]
Equivalently, the degree distribution of closed points of the finite étale line scheme is
\[
Z(F_1(X_0)/k,T)=\frac{1}{(1-T)^{40}(1-T^2)^{36}},
\qquad
Z(F_1(X_{\pm1})/k,T)=\frac{1}{(1-T)^{10}(1-T^8)^6}.
\]
For every positive integer \(m\), the number of lines defined over \(\mathbb F_{3^m}\) is therefore
\[
\#F_1(X_0)(\mathbb F_{3^m})=
\begin{cases}40&m\text{ odd},\\112&m\text{ even},\end{cases}
\qquad
\#F_1(X_{\pm1})(\mathbb F_{3^m})=
\begin{cases}10&8\nmid m,\\58&8\mid m.\end{cases}
\]
Thus the forty-eight nonrational lines on each nonzero member all first acquire a field of definition of degree eight.

## Assumptions and scope

The coefficient field is exactly \(\mathbb F_3\), the parameter runs through its **three** elements, and a line means a geometric projective line contained in the indicated quartic. The zeta functions are those of the **zero-dimensional line Fano schemes**, not the K3 surfaces. These formulas classify fields of definition of lines; they do not assert isomorphisms of the three quartic surfaces over the base field.

The displayed quartic is smooth for each parameter. In characteristic three, for its defining polynomial \(F_a\),
\[
(F_{x_0},F_{x_1},F_{x_2},F_{x_3})
=(-x_3^3+a x_0x_1x_2,\;-x_2^3-a x_0^2x_2,\;x_1^3-a x_0^2x_1,\;x_0^3).
\]
If all partials vanished at a projective point, the final partial forces \(x_0=0\), the middle two force \(x_1=x_2=0\), and the first forces \(x_3=0\), a contradiction. Hence \(X_a\) is smooth. By adjunction, its canonical bundle is trivial and its \(H^1(\mathcal O)\) vanishes, so it is a K3 surface.

## Proof

**1. Exhaustive line parametrization.** Each projective line corresponds to a unique two-dimensional vector subspace of \(k^4\), after passage to the algebraic closure. A unique reduced-row-echelon basis consists of vectors \(A,B\), with pivot pair \((i,j)\), where \(0\le i<j\le3\). For each chart, the restriction \(F_a(UA+VB)\) must vanish identically in the homogeneous parameters \(U,V\). The resulting five coefficient equations yield the following exhaustive table, where \(u,v,s,t\) are line-chart coordinates:

\[
\begin{array}{c|l|l}
(i,j)&(A;B)&\text{necessary and sufficient equations}\\\hline
(0,1)&(1,0,u,v);(0,1,s,t)&v^3=v,\ s^3=s,\ as=0,\ t=u^3+au,\ u=t^3\\
(0,2)&(1,u,0,v);(0,0,1,t)&v^3=v,\ t=au-u^3,\ t^3=-u\\
(0,3)&(1,u,v,0);(0,0,0,1)&\text{no solution}\\
(1,2)&(0,1,0,u);(0,0,1,v)&\text{no solution}\\
(1,3)&(0,1,u,0);(0,0,0,1)&u^3=u\\
(2,3)&(0,0,1,0);(0,0,0,1)&\text{one line}.
\end{array}
\]
The empty charts have a coefficient equal to \(1\) in their quartic restriction, so their emptiness holds geometrically. Because row-echelon charts cover the Grassmannian of lines and each line has exactly one such chart, the enumeration neither duplicates nor omits lines.

**2. Two additive-polynomial root spaces.** Eliminating \(t\) gives, respectively,
\[
L_+(u)=u^9+a^3u^3-u=0\quad\text{on }(0,1),
\qquad
L_-(u)=u^9-a^3u^3-u=0\quad\text{on }(0,2).
\]
Each is a separable additive polynomial of degree nine, since its formal derivative is \(-1\). Consequently it has exactly nine distinct roots over the algebraic closure, forming a two-dimensional \(\mathbb F_3\)-vector space. In each chart \(v\in\mathbb F_3\); in the first chart also \(s\in\mathbb F_3\), constrained by \(as=0\). The remaining parameters \(t\) are uniquely determined by \(u\). The last two nonempty charts supply three and one \(\mathbb F_3\)-rational lines, respectively.

**3. The special parameter.** For \(a=0\), both root equations are \(u^9=u\), so the root set is exactly \(\mathbb F_9\). The first chart has \(9\cdot3\cdot3=81\) lines; the second has \(9\cdot3=27\) lines; the last two supply \(4\). Thus there are \(112\) geometric lines. Frobenius fixes the root set's three \(\mathbb F_3\)-elements; hence the first chart has \(3\cdot3\cdot3=27\) rational lines, the second has \(3\cdot3=9\), and the last two contribute four, totaling \(40\). Every remaining line is defined over \(\mathbb F_9\), so \((112-40)/2=36\) Frobenius transpositions exhaust the rest.

**4. The two nonzero parameters.** Let \(a\in\mathbb F_3^\times\); then \(a^3=a\). For either sign, on a nine-element root space the map \(\varphi(u)=u^3\) obeys
\[
\varphi^2\pm a\varphi-I=0.
\]
The quadratic \(z^2\pm az-1\) is irreducible over \(\mathbb F_3\), since its discriminant \(a^2+4=2\) is nonsquare. Its two roots in \(\mathbb F_9\) have norm \(-1\); equivalently, in the matrix ring \(\varphi^4=-I\) and \(\varphi^8=I\). As this is an irreducible two-dimensional representation, no nonzero vector is fixed by any proper divisor of the eighth power. Hence the eight nonzero roots constitute one Frobenius cycle of length eight, and zero is the only fixed root. For these parameters \(as=0\) forces \(s=0\). Each of the first two charts therefore consists of three rational lines and three length-eight cycles. Including the last four rational lines yields ten fixed lines and six eight-cycles, a total of \(58\) geometric lines.

**5. Reducedness and zeta.** A line \(L\) on a smooth quartic K3 surface is a smooth rational curve with \(L^2=-2\) by adjunction. Therefore its normal bundle in the surface is \(\mathcal O_{\mathbb P^1}(-2)\), with no sections. Thus the line Hilbert scheme is reduced at every geometric line and is zero-dimensional; it is finite étale over the perfect field \(\mathbb F_3\). Each geometric Frobenius orbit of length \(d\) is a closed point of degree \(d\). The Euler product for the zeta function of a finite étale zero-dimensional scheme is the stated product of \((1-T^d)^{-1}\) factors. Its rational-point counts follow by counting Frobenius fixed points of each power. This finishes the proof.

## Verification

The accompanying standalone Python 3 program `verify.py` uses only the standard library and exact arithmetic. It expands \(F_a(UA+VB)\) symbolically in all six row-echelon charts, then independently enumerates all line subspaces over \(\mathbb F_3\) and \(\mathbb F_9\), obtaining counts \((40,10,10)\) and \((112,10,10)\) for the ordered parameters \((0,1,-1)\), and checks Frobenius has order eight on each nonzero root space. Run `python3 verify.py`; successful execution prints `VERIFY_OK`. The script output is preserved as `verify_output.txt`. The assertion about every field extension follows from the preceding general proof, not from these finite checks.

## Relationship to prior work

Veniani, *Lines on K3 quartic surfaces in characteristic 3* (first publicly posted 2016-08-15, arXiv:1608.04209), provides this characteristic-three quartic family and its **geometric** counts of \(112\) lines for the zero parameter and \(58\) for nonzero parameters. Degtyarev, *Lines in supersingular quartics* (arXiv:1604.05836), treats geometric configurations of lines on characteristic-three supersingular quartics. These geometric counts are used as context, not claimed as discoveries. The result here is the field-of-definition and Frobenius orbit classification for the three \(\mathbb F_3\)-models and the resulting explicit zeta functions of their line schemes. The relevant sections and available primary texts were inspected for these arithmetic statements; no statement of the splitting profile was identified. This is a best-knowledge literature comparison, not a claim of established absolute historical priority.

## Limitations

The theorem pertains only to the three coefficient values in \(\mathbb F_3\), not all parameters in characteristic three; it does not classify line configurations up to incidence, compute the K3 surface zeta functions, or identify the Picard lattices. Although the exact proof and code agree, the scientific review is not independent. An unindexed prior arithmetic computation or an inaccessible source could still affect originality.

## References

1. D. C. Veniani, *Lines on K3 quartic surfaces in characteristic 3*, arXiv:1608.04209 (initial public version 2016-08-15): https://arxiv.org/abs/1608.04209.
2. A. Degtyarev, *Lines in supersingular quartics*, arXiv:1604.05836 (initial public version 2016-04-20): https://arxiv.org/abs/1604.05836.
