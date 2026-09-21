# Exact stick-number propagation under trefoil summation

## Result

Let \(\operatorname{stick}(K)\) denote the stick number of a nontrivial knot \(K\), and let \(b(K)\) denote its bridge index. Suppose
\[
\operatorname{stick}(K)=2b(K)+2.
\tag{1}
\]
Let \(T_1,\ldots,T_m\) be arbitrary right- or left-handed trefoil knots. Then
\[
\boxed{
\operatorname{stick}(K\#T_1\#\cdots\#T_m)
=
\operatorname{stick}(K)+2m
}
\tag{2}
\]
for every \(m\ge 0\). Equivalently,
\[
\operatorname{stick}(K\#T_1\#\cdots\#T_m)
=
2\bigl(b(K)+m\bigr)+2.
\tag{3}
\]

More generally, let \(K,L\) be nontrivial knots satisfying
\[
\operatorname{stick}(K)=2b(K)+2,\qquad
\operatorname{stick}(L)=2b(L)+2,
\tag{4}
\]
and suppose \(L\) has a minimum-stick polygonal representative with an external edge, meaning an edge contained in the boundary of the convex hull. Then
\[
\boxed{
\operatorname{stick}(K\#L)
=
\operatorname{stick}(K)+\operatorname{stick}(L)-4.
}
\tag{5}
\]
In particular, \(K\#L\) again satisfies the bridge-stick equality
\[
\operatorname{stick}(K\#L)=2b(K\#L)+2.
\tag{6}
\]

## Proof

Two classical ingredients match exactly.

First, Kuiper's bridge/superbridge inequality together with Jin's polygonal bound gives, for every nontrivial knot \(J\),
\[
b(J)<\operatorname{sb}(J)\le \frac{\operatorname{stick}(J)}{2}.
\]
Since bridge and superbridge indices are integers,
\[
\operatorname{stick}(J)\ge 2b(J)+2.
\tag{7}
\]

Second, Schubert's connected-sum formula gives
\[
b(K\#L)=b(K)+b(L)-1.
\tag{8}
\]
Therefore (7), (8), and (4) imply
\[
\begin{aligned}
\operatorname{stick}(K\#L)
&\ge 2(b(K)+b(L)-1)+2\\
&=2b(K)+2b(L)\\
&=\operatorname{stick}(K)+\operatorname{stick}(L)-4.
\end{aligned}
\tag{9}
\]

For the upper bound, Sato's proof of the polygon-index connected-sum inequality records the sharper construction available when one minimum polygon has an external edge. If \(L\) has such a minimum representative, the two polygons can be matched along one edge and those two matched edges removed, producing
\[
\operatorname{stick}(K\#L)
\le
\operatorname{stick}(K)+\operatorname{stick}(L)-4.
\tag{10}
\]
Combining (9) and (10) proves (5). Equation (6) follows at the same time from (8).

Both chiral trefoils have six-stick representatives with external edges, as explicitly noted by Sato, and
\[
b(T)=2,\qquad \operatorname{stick}(T)=6=2b(T)+2.
\]
Thus (5) with \(L=T\) gives
\[
\operatorname{stick}(K\#T)=\operatorname{stick}(K)+2.
\]
The resulting connected sum still satisfies (1), so iteration proves (2) and (3), independently of the chirality chosen at each step. \(\square\)

## Application: nineteen infinite exact families

Cantarella, Rechnitzer, Schumacher, and Shonkwiler proved in 2025/2026 that the following nineteen prime knots have stick number exactly \(10\):
\[
\begin{gathered}
11n71,\ 11n75,\ 11n76,\ 11n78,\\
13n225,\ 13n230,\ 13n285,\ 13n288,\ 13n307,\ 13n584,\ 13n586,\ 13n593,\\
13n602,\ 13n603,\ 13n604,\ 13n607,\ 13n608,\ 13n1192,\ 13n5018.
\end{gathered}
\]
Their proof also records that each of these knots has bridge index \(4\). Hence every one satisfies
\[
10=2\cdot4+2.
\]
Consequently, if \(K\) is any knot in the displayed list and \(T_1,\ldots,T_m\) are trefoils of arbitrary chiralities, then
\[
\boxed{
\operatorname{stick}(K\#T_1\#\cdots\#T_m)=10+2m.
}
\tag{11}
\]
Thus each of the nineteen newly determined prime stick numbers generates an infinite family of exact stick numbers for composite knots.

## Context and originality boundary

The ingredients are classical. Adams--Brennan--Greilsheimer--Woo (1997) studied stick numbers under composition and determined exact stick numbers for compositions of their \((n,n-1)\)-torus-knot family. Sato (2001) gave an explicit geometric proof of the general connected-sum upper bound and, within that proof, the four-stick saving when one minimum polygon has an external edge; he used the external-edge six-stick trefoil to recover the eight-stick square and granny knots. Schubert's bridge-number connected-sum formula is classical, and the bridge/superbridge lower bound used above is standard.

The claim here is therefore not any of those ingredients. The contribution is the matching criterion (4)--(5): the external-edge four-stick saving is exactly certified as optimal whenever both summands saturate the universal bridge-stick lower bound. The trefoil case then gives the propagation law (2). Applying it to the nineteen exact \(10\)-stick, \(4\)-bridge knots found by Cantarella et al. yields (11).

The checked composition literature, current stick-number tables, and the 2025/2026 paper did not locate this criterion or the nineteen resulting infinite families. The recent paper itself discusses the nineteen prime exact values but does not discuss connected sums. Originality is asserted only **to the best of our knowledge**. The proof is short and combines classical tools, so an equivalent observation may exist as folklore or under the older term *polygon index*.

## Limitations

- The propagation theorem requires equality in the bridge-stick lower bound \(\operatorname{stick}(K)=2b(K)+2\).
- The general two-factor equality (5) additionally requires a minimum-stick representative of one factor with an external edge.
- The nineteen-family application uses trefoils because both chiralities have the required six-stick external-edge representatives. No claim is made that the nineteen base knots themselves possess external edges in their minimum representatives.
- The result concerns ordinary stick number, not equilateral, lattice, or other restricted stick numbers.
- Originality is to the best of our knowledge; the principal residual risk is an equivalent corollary hidden in older composition literature under different terminology.

## References

1. Y. Sato, *The geometric shapes of polygonal knots*, Bulletin of the Faculty of Education, Yamaguchi University, Pt. 2, 51 (2001), 23--43.  
   https://petit.lib.yamaguchi-u.ac.jp/6699

2. C. C. Adams, B. M. Brennan, D. L. Greilsheimer, A. K. Woo, *Stick Numbers and Composition of Knots and Links*, Journal of Knot Theory and Its Ramifications 6 (1997), 149--161.  
   https://doi.org/10.1142/S0218216597000121

3. J. Schultens, *Additivity of bridge numbers of knots*, Mathematical Proceedings of the Cambridge Philosophical Society 135 (2003), 539--544.  
   https://doi.org/10.1017/S0305004103006832

4. G. T. Jin, *Polygon indices and superbridge indices of torus knots and links*, Journal of Knot Theory and Its Ramifications 6 (1997), 281--289.  
   https://doi.org/10.1142/S0218216597000170

5. N. H. Kuiper, *A new knot invariant*, Mathematische Annalen 278 (1987), 193--209.  
   https://doi.org/10.1007/BF01458070

6. J. Cantarella, A. Rechnitzer, H. Schumacher, C. Shonkwiler, *New Upper Bounds for Stick Numbers*, arXiv:2508.18263 (2025); Journal of Knot Theory and Its Ramifications, 2650008 (2026).  
   https://arxiv.org/abs/2508.18263  
   https://doi.org/10.1142/S0218216526500082

7. KnotInfo, *Stick Number* table description (current database context).  
   https://knotinfo.org/descriptions/polygon_index.html
