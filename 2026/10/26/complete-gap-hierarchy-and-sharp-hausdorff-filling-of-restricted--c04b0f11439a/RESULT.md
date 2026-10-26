# Complete gap hierarchy and sharp Hausdorff filling of restricted-digit Gauss survivors

## Finding
For each integer \(m\ge2\), let \(T(0)=0\), \(T(x)=1/x-\lfloor1/x\rfloor\) for \(0<x\le1\), and let
\[
K_m=\{x\in[0,1]:T^j(x)\le1/m\text{ for every integer }j\ge0\}.
\]
For \(a\ge m\), write
\[
L_a=\frac1{a+1},\qquad R_a=\frac1{a+1/m},\qquad G_a=(L_a,R_a).
\]
For any finite word \(w=(b_1,\ldots,b_k)\) over integers \(b_i\ge m\), let \(f_w=f_{b_1}\circ\cdots\circ f_{b_k}\), with \(f_b(t)=1/(b+t)\), and put \(f_\varnothing=\mathrm{id}\).

**Complete complementary-gap classification.** The bounded connected components of \([0,1/m]\setminus K_m\) are exactly the pairwise distinct intervals \(f_w(G_a)\), for all \(a\ge m\) and all finite words \(w\) (including the empty word). If \(q_{-1}=0\), \(q_0=1\) and \(q_j=b_jq_{j-1}+q_{j-2}\), then their lengths are exactly
\[
|f_w(G_a)|=\frac{R_a-L_a}{(q_k+q_{k-1}L_a)(q_k+q_{k-1}R_a)}.
\]
Here for \(k=0\) the denominator is understood as \(1\).

**Sharp macroscopic gap.** The unique largest gap is \(G_m\). Under the natural normalization \(mK_m\subset[0,1]\), the exact Hausdorff distance is
\[
\boxed{d_{\mathrm H}(mK_m,[0,1])=\frac{m(m-1)}{2(m^2+1)(m+1)}.}
\]
Consequently \(mK_m\) converges to the full unit interval in Hausdorff distance, with the sharp asymptotic \(m\,d_{\mathrm H}(mK_m,[0,1])\to1/2\). Every \(K_m\) has Lebesgue measure zero, and its gap-length sum equals \(1/m\).

## Assumptions and scope
The assertions concern the standard regular Gauss map, an open hole \((1/m,1]\), every integer \(m\ge2\), and the Euclidean metric on compact subsets of \([0,1]\). Rational points whose iterates reach zero are included exactly when every earlier Gauss iterate is at most \(1/m\). No uniform finite truncation of the countable digit alphabet is assumed. Only Euclidean complement components inside \([0,1/m]\) are called gaps.

## Proof
**1. Complete inverse-branch description.** Every nonzero \(x\in[0,1/m]\) has first continued-fraction digit \(a=\lfloor1/x\rfloor\ge m\), and \(x=f_a(T(x))\). Conversely, for any \(a\ge m\) and \(t\in K_m\), the point \(f_a(t)\) belongs to \(K_m\): it is at most \(1/m\), its first Gauss iterate is \(t\), except that \(t=0\) gives the rational \(1/a\) with Gauss image zero, and later iterates survive. Thus
\[
K_m=\{0\}\cup\bigcup_{a\ge m}f_a(K_m).
\]
The union together with zero is compact: any sequence with first digits tending to infinity converges to zero; fixed first digits preserve compactness recursively. Equivalently, the inverse-branch coding plus terminating zero supplies a compact coded image. Its convex hull is \([0,1/m]\), with both endpoints present.

**2. The first-level gaps.** The convex hull of \(f_a(K_m)\) is the closed interval \(I_a=[1/(a+1/m),1/a]\), with both endpoints in \(K_m\). These hulls are pairwise disjoint and ordered from right to left as \(a\) increases. Their intervening open intervals are precisely \(G_a=(1/(a+1),1/(a+1/m))\). They have endpoints in \(K_m\), while no point inside belongs to \(K_m\).

**3. All deeper gaps and exact lengths.** A connected component of the complement either lies between two first-level hulls or lies strictly inside one such hull. In the latter case its preimage by the homeomorphism \(f_a:[0,1/m]\to I_a\) is a component of the complement. Iterate this alternative. If no first-level gap is ever reached, the component lies in nested depth-\(j\) cylinder hulls, whose lengths are at most \((1/m)m^{-2j}\), because \(|f_b'(t)|=(b+t)^{-2}\le m^{-2}\). A nonempty open interval cannot be contained in hulls of vanishing length. Thus every gap is \(f_w(G_a)\), and uniqueness follows from disjoint cylinder interiors and the uniqueness of the earliest removed stage.

For \(w=(b_1,\ldots,b_k)\), the standard convergent continuant identity gives
\[
f_w(t)=\frac{p_k+p_{k-1}t}{q_k+q_{k-1}t},\qquad |p_kq_{k-1}-p_{k-1}q_k|=1,
\]
with \(p_{-1}=1,p_0=0\), \(p_j=b_jp_{j-1}+p_{j-2}\). Subtracting the two Möbius values at \(L_a,R_a\) gives the displayed exact gap-length formula, valid also for the empty word.

**4. Unique maximal gap and Hausdorff distance.** The primary gap lengths are
\[
\delta_a=R_a-L_a=\frac{1-1/m}{(a+1/m)(a+1)},
\]
strictly decreasing with \(a\ge m\). Every nonempty prefix \(w\) contracts lengths by at most \(m^{-2|w|}<1\), so no descendant gap can match \(\delta_m\). Therefore \(G_m\) alone is maximal. For a compact subset of an interval containing both endpoints, the Hausdorff distance to the entire interval is half the supremum of its complementary-gap lengths (attained at a midpoint). Scaling gives
\[
d_{\mathrm H}(mK_m,[0,1])=\frac m2\,\delta_m
=\frac{m(m-1)}{2(m^2+1)(m+1)}.
\]
The asymptotic follows by dividing numerator and denominator by appropriate powers of \(m\).

**5. Zero measure and total gap length.** The sum of the inverse-branch Lipschitz constants is \(c_m=\sum_{a\ge m}a^{-2}<1\), since \(m\ge2\). The union of all depth-\(j\) cylinder hulls has total length at most \(c_m^j/m\). Their intersection together with countably many terminating coded endpoints contains \(K_m\); hence \(K_m\) has Lebesgue measure zero. Since its complement is exactly the disjoint union of the listed open intervals in a hull of length \(1/m\), their lengths sum to \(1/m\).

## Verification
The included standalone `verify.py` uses exact rational arithmetic to compare the continuant formula with explicit compositions for \(m=2,\ldots,8\), word lengths \(0,1,2,3\), and finite digit subranges; it also tests strict maximal-gap inequalities and endpoints. It reports `VERIFY_OK exact_rational_gap_checks= 2975`. These finite checks do not establish the arbitrary-depth or arbitrary-digit theorem: that follows from the inverse-branch and contraction proof above.

## Relationship to prior work
Liu and Liao (2026) study the same Gauss survivor family for arbitrary hole parameters, proving an exact plateau structure and that its Hausdorff dimension jumps from \(0\) at parameter zero to the limiting value \(1/2\) from above. The result here concerns a different observable: **all actual Euclidean gap lengths** at the canonical reciprocal thresholds, and a sharp *Hausdorff-metric filling rate after rescaling*, rather than Hausdorff dimension. Their paper was examined in HTML through its sections and conclusions; no such exact gap hierarchy or Hausdorff-distance formula was found.

Mauldin and Urbański developed the general conformal iterated-function-system theory and its application to continued fractions with restricted partial quotients. Standard inverse-branch methods are used here and not claimed as new. The stated specialized numerical distance and all-gap formula were not established by the accessible comparisons; a complete examination of the 1999 paper was unavailable, and an equivalent older parameterization is a residual priority risk.

## Limitations
This theorem addresses the canonical reciprocal parameters \(1/m\), not arbitrary Gauss holes. It is a geometric classification, not a new Hausdorff-dimension formula or a claim about regularity of dimension plateaus. Historical priority has only been checked to the extent described above. The result has not received independent verification.

## References
1. C. Liu and L. Liao, *Survivor Set of Gauss Map with a Hole at 1*, arXiv:2610.14534v1, submitted 2026-10-10, https://arxiv.org/html/2610.14534v1.
2. R. D. Mauldin and M. Urbański, *Dimensions and Measures in Infinite Iterated Function Systems*, Proc. London Math. Soc. 73 (1996), 105–154, doi:10.1112/plms/s3-73.1.105.
3. R. D. Mauldin and M. Urbański, *Conformal Iterated Function Systems with Applications to the Geometry of Continued Fractions*, Trans. Amer. Math. Soc. 351 (1999), 4995–5025, doi:10.1090/S0002-9947-99-02268-0.
4. R. D. Mauldin and M. Urbański, *The doubling property of conformal measures of infinite iterated function systems*, J. Number Theory 102 (2003), 23–40, doi:10.1016/S0022-314X(03)00065-9.
