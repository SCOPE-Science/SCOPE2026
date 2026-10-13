# Sharp asymmetric power-copula simplex and opposing-tail envelope

## Finding

Fix \(0<s\le1\). For nonnegative \(a,b\), consider
\[
C_{s,a,b}(u,v)=u^{1+a(v^{-s}-1)}v^{1+b(u^{-s}-1)},\qquad 0<u,v\le1,
\]
with \(C(u,0)=C(0,v)=0\). This two-directional variable-power family is a copula **exactly** on the sharp simplex
\[
\boxed{a\ge0,\quad b\ge0,\quad s(a+b)\le1.}
\]
Every admissible member has positive density throughout the interior and is negatively quadrant dependent; the copula is reverse-regular of order two whenever \(a+b>0\).

Let \(L_{UL}\) and \(L_{LR}\) denote the conditional opposite-corner tail limits, respectively \(\Pr(V>1-t\mid U\le t)\) and \(\Pr(V\le t\mid U>1-t)\) as \(t\downarrow0\), where \(U,V\) are uniform margins with this copula. Their values are
\[
(L_{UL},L_{LR})=\begin{cases}
(0,0),&0<s<1,\\
(1-e^{-b},\ 1-e^{-a}),&s=1.
\end{cases}
\]
Consequently the exact attainable two-tail set over the entire family is
\[
\boxed{\mathcal T=\left\{(x,y)\in[0,1)^2:\ (1-x)(1-y)\ge e^{-1}\right\}.}
\]
The frontier is attained when \(s=1\) and \(a+b=1\). Conversely any \((x,y)\in\mathcal T\) comes from \(s=1\), \(a=-\log(1-y)\), \(b=-\log(1-x)\). In particular, the two directional tail limits identify the directional weights when \(s=1\), but the complete diagonal section alone does not.

Writing \(r=a+b\), the exact diagonal is
\[
C_{s,a,b}(t,t)=t^{2+r(t^{-s}-1)}.
\]
The lower-left and upper-right classical tail coefficients are zero for every member. More precisely, the upper-right joint exceedance \(J(t)=\Pr(U>1-t,V>1-t)\) obeys
\[
J(t)=\begin{cases}
(1-sr)t^2+O(t^3),&sr<1,\\
(1-s/2)t^3+O(t^4),&sr=1.
\end{cases}
\]
The change from quadratic to cubic decay holds throughout the sharp validity boundary, regardless of the split between \(a\) and \(b\).

## Assumptions and scope

The result concerns the displayed family **only**, with \(0<s\le1\) and \(a,b\ge0\); it makes no claim about signed directional weights or exponents beyond this range. Endpoints are defined continuously with the stated margins. All limits use one common threshold \(t\downarrow0\) in each margin. A strict interior density and a probability distribution, not merely pointwise values below one, are asserted. The fixed symmetric Stingray is obtained by \(a=b=1/2\), with \(s=-\delta\); its published one-sided candidate is \(a=0,b=1/2\).

## Proof

Write \(A=u^{-s}\ge1\), \(B=v^{-s}\ge1\), \(\ell_u=-\log u\ge0\), and \(\ell_v=-\log v\ge0\). Logarithmic differentiation gives
\[
\frac{\partial_u C}{C}=\frac{P}{u},\quad
\frac{\partial_v C}{C}=\frac{Q}{v},\quad
P=1+a(B-1)+sbA\ell_v,\quad
Q=1+b(A-1)+saB\ell_u.
\]
The mixed derivative of \(\log C\) is \(-s(aB+bA)/(uv)\), hence
\[
c(u,v)=\frac{C(u,v)}{uv}\left(PQ-s(aB+bA)\right).
\]
Since \(P\ge1+a(B-1)\) and \(Q\ge1+b(A-1)\), with every factor nonnegative,
\[
PQ-s(aB+bA)\ge
1-s(a+b)+(1-s)\big[a(B-1)+b(A-1)\big]+ab(A-1)(B-1)\ge0
\]
whenever \(s(a+b)\le1\). In the open square the omitted logarithmic terms make the inequality strict if \(a+b>0\); if both weights vanish, \(c=1\). The function has the correct upper margins and is zero on lower edges, with \(0\le C(u,v)\le uv\le\min\{u,v\}\), so it is continuous on the closed square. Nonnegative mixed density implies nonnegative volumes for every rectangle, including boundary rectangles by continuity. This proves copula sufficiency and full interior support. Conversely, as \((u,v)\to(1,1)\), \(c(u,v)\to1-s(a+b)\); if this is negative, nearby sufficiently small rectangles have negative volume. Thus the simplex is necessary.

For \(a+b>0\), \(C\le uv\) is strict in the interior. Moreover, \(\partial_{uv}\log C=-s(a v^{-s}+b u^{-s})/(uv)<0\), which is precisely reverse-regularity of order two; equality holds for independence.

The upper-left limit is
\[
L_{UL}=\lim_{t\downarrow0}\left(1-\frac{C(t,1-t)}{t}\right),\quad
\frac{C(t,1-t)}{t}
=t^{a((1-t)^{-s}-1)}(1-t)^{1+b(t^{-s}-1)}.
\]
The logarithm of the first factor tends to zero because \(((1-t)^{-s}-1)\log t=O(t\log t)\). The second factor has logarithm \((1+b(t^{-s}-1))\log(1-t)=-bt^{1-s}(1+o(1))+o(1)\). Therefore the first conditional coefficient is zero for \(s<1\), and \(1-e^{-b}\) for \(s=1\). Interchanging \(u,v\) proves the lower-right formula with \(a\). At \(s=1\), invert the two maps and use \(a+b\le1\) to obtain the exact curved region, including necessity, sufficiency and frontier attainment. When \(s<1\), only the origin arises, which is already in the region.

Substitution \(u=v=t\) gives the diagonal identity. The lower-left coefficient \(\lim_{t\downarrow0} C(t,t)/t\) vanishes even at \(a=b=0\). Expanding \(C(1-t,1-t)\) about \(t=0\), or integrating the density, gives \(J(t)=(1-sr)t^2+O(t^3)\) in the interior. When \(sr=1\), the leading density near \((1,1)\), writing \(u=1-x\), \(v=1-y\), becomes
\[
c(1-x,1-y)=(1-s^2b)x+(1-s^2a)y+O((x+y)^2).
\]
Integrating over \((x,y)\in[0,t]^2\) yields \(J(t)=[1-s^2(a+b)/2]t^3+O(t^4)=(1-s/2)t^3+O(t^4)\). Both upper-right tail coefficients are consequently zero. This completes the proof.

## Verification

A standalone script, `CHECK.py`, reproduces the mixed-density formula using central differences at 150 sample points on six admissible parameter triples. At 70-decimal precision it also checks six pairs of opposite-tail limits, the quadratic/cubic upper-right asymptotics, a negative-density witness outside the simplex, and identical diagonals with unequal directional weights. These finite checks provide computational safeguards; the proof for all admissible real parameters is the preceding algebra and limits. Run with Python 3 and the documented dependency in `requirements.txt`.

For illustration at \(s=1\), \(a=0.7\), \(b=0.3\), the ordered coefficients are approximately \((L_{UL},L_{LR})=(0.259181779318,0.503414696209)\). Reversing the weights swaps these coefficients but preserves the entire diagonal and its upper-right decay.

## Relationship to prior work

Papadopoulos's Stingray construction gives exactly the symmetric subfamily \(a=b=1/2\), its opposite-corner coefficient \(1-e^{-1/2}\) at \(s=1\), and explicitly proposes (without studying) a single-sided asymmetric expression corresponding to \(a=0,b=1/2\). Those formulas and limits are prior results, not reintroduced findings. The new statement is the **complete independently weighted, common-power simplex** and its exact two-dimensional tail frontier, together with the upper-right boundary transition and diagonal indistinguishability.

Chesneau's 2023 variable-power work contains the symmetric \(s=1\), \(a=b\) PVP2 family, and an asymmetric Khoudraji power transformation whose reciprocal exponents and two coefficients are linked, rather than both powers being \(s\) with independent \(a,b\). Chesneau's 2023 one-variable-power (IP) construction includes the single-direction faces \(a=0\) or \(b=0\). These genuine overlaps delimit, but do not imply, the full two-sided feasible region or its directional-tail tradeoff.

## Limitations

The theorem does not classify signed weights, other exponent functions, or copula behavior outside the displayed family. Tail asymptotics are population limits: no finite-sample statistical estimator, confidence interval, or practical identification rate is established. The priority comparison with a relevant 2024 variable-power paper remains unresolved because its complete text was inaccessible; equivalent broader constructions remain a priority risk.

## References

1. A. Papadopoulos, *The Stingray Copula for Negative Dependence*, posted 19 December 2025, preprint `202512.1777`, https://www.preprints.org/manuscript/202512.1777; journal version, *Stats* 9 (2026), article 13, https://doi.org/10.3390/stats9010013.
2. C. Chesneau, *Some new developments on variable-power copulas*, *Applicationes Mathematicae* 50 (2023), 35–54, https://doi.org/10.4064/am2483-11-2023; the full open paper includes Proposition 3.2 and the asymmetric transformation.
3. C. Chesneau, *Theoretical Validation of New Two-Dimensional One-Variable-Power Copulas*, *Axioms* 12 (2023), article 392, https://doi.org/10.3390/axioms12040392.
4. C. Chesneau, *Solutions to two open problems on bivariate variable-power copulas*, *Bulletin of Computational Applied Mathematics* 12(1) (2024), publicly available abstract, https://sites.google.com/usb.ve/bullcompama/table-of-contents/abstract-92.
