# Sharp tent-spline frame transition at rational density \(2/5\)

## Finding
For the centered second-order B-spline \(Q_2(s)=(1-|s|)_+\), let \(2<b<5/2\) and \(a=2/(5b)\). The Gabor family \(\{e^{2\pi imb(\cdot)}Q_2(\cdot-na):m,n\in\mathbb Z\}\) is a frame for \(L^2(\mathbb R)\) **if and only if** \(b>21/10\). In particular, within this full open interval of lattice shapes, the Lemvig--Nielsen obstruction \(b\le21/10\) is sharp at the non-integer rational density \(ab=2/5\).

## Assumptions and scope
The convention is \(Q_2(s)=\max\{1-|s|,0\}\), \(ab=2/5\), and \(2<b<5/2\). The assertion neither characterizes other values of \(b\) nor other rational densities. A Gabor frame means uniform positive finite lower and upper frame bounds for all \(f\in L^2(\mathbb R)\). Its equivalence to uniform full row rank of the continuous Zibulski--Zeevi matrix is the standard rational-density characterization quoted as Theorem 4 by Stangl--Frederick.

## Proof
Put \(\varepsilon=b-2\in(0,1/2)\), \(h=2/5\) and \(z=e^{2\pi i\gamma}\). Discarding the common nonzero normalized-Zak factor, define
\[
Z(t,z)=\sum_{m\in\mathbb Z}Q_2((t-m)/b)z^m=E(t,z)+O(t,z),
\]
where \(E\) and \(O\) contain respectively even and odd indices. Direct enumeration of the support, for \(0\le t\le1\), gives
\[
\begin{aligned}
bE(t,z)&=b-t+(\varepsilon+t)z^2+(\varepsilon-t)_+z^{-2},\
bO(t,z)&=(1+\varepsilon-t)z^{-1}+(1+\varepsilon+t)z+(t-1+\varepsilon)_+z^3.
\end{aligned}
\]
The two Zak frequencies \(\gamma\) and \(\gamma+1/2\) consequently form the vector \((E+O,E-O)\); its pairwise-column rank is the same as that of \((E,O)\).

At \(ab=2/5\), the Zibulski--Zeevi matrix has two rows and five columns indexed by \(s=0,\ldots,4\), evaluated at \(x-2s/5\). For \(0\le x\le1/5\), the three columns \(s=0,4,3\) are represented, in that order, by samples \(x,x+h,x+2h\), because the last two arguments differ from these by an even integer; Zak quasi-periodicity multiplies both frequency rows by the same nonzero scalar. It suffices to show either adjacent sample pair has nonzero determinant for every \(x\in[0,1/5]\) and \(|z|=1\).

**Left--left determinant.** If \(0\le u<u+h\le\varepsilon\), neither sample has the right-hand edge contribution. Exact substitution into the displayed formulas gives
\[
b^2z^3\bigl(E(u)O(u+h)-E(u+h)O(u)\bigr)
=h\bigl(-t^3+2t^2+2\varepsilon t+1\bigr),\quad t=z^2.
\]
This real cubic has no root on \(|t|=1\): its evaluations at \(t=1,-1\) are respectively \(2+2\varepsilon\) and \(4-2\varepsilon\), both positive. If it had a nonreal unit root, its conjugate would be a second root, and the root product \(1\) would force the third root \(1\), already excluded.

**Left--central determinant.** If \(0\le u<\varepsilon\le v=u+h\le1-\varepsilon\), let \(L=\varepsilon-u>0\), \(A=1+\varepsilon-v>0\), \(B=1+\varepsilon+v>0\). The exact determinant is
\[
b^2z^3\bigl(E(u)O(v)-E(v)O(u)\bigr)
=-h t(t-1)^2+L(A+Bt),\quad t=z^2.
\]
At \(t=1\) this is \(L(A+B)>0\), while at \(t=-1\) it is \(4h-2Lv>0\), as \(h=2/5\), \(L<1/2\), and \(v\le3/5\). Suppose a nonreal unit root existed. Factoring the cubic as \(-h(t-r)(t^2-2ct+1)\) with real \(r,c\), coefficient comparison gives \(r=LA/h\), \(c=1-r/2\), and \(c=-B/(2A)\). But \(0<LA<(1/2)(11/10)<2h\), so the middle expression is positive, whereas the last is negative: contradiction.

**Reflection and coverage.** Evenness of \(Q_2\) yields \(Z(1-t,z)=zZ(t,z^{-1})\). On replacing \(z\) by \(-z\), this identity also gives the corresponding two-row Zak relation, up to nonzero diagonal factors and a change from \(z\) to \(z^{-1}\). Therefore the above two left-side determinant lemmas apply symmetrically to two right-side samples, including right--central pairs in reverse order.

Suppose now \(\varepsilon>1/10\). Set \(y_0=x\), \(y_1=x+h\), \(y_2=x+2h\). If \(y_1<\varepsilon\), the first pair is left--left. If \(y_1>1-\varepsilon\), the last pair is right--right. Otherwise \(\varepsilon\le y_1\le1-\varepsilon\). When \(y_0<\varepsilon\), the first pair is left--central. When \(y_0\ge\varepsilon\), the inequality \(y_2\ge\varepsilon+4/5>1-\varepsilon\) shows that the last pair is central--right. Every case supplies a nonzero determinant for all \(|z|=1\). The matrix is continuous on the compact Zak torus up to unit-modulus quasi-periodic row factors, so its least singular value has a strictly positive uniform minimum. The Zibulski--Zeevi characterization proves the frame property.

For \(0<\varepsilon\le1/10\), take \(x=\varepsilon\), \(z=-1\). The five wrapped column sample positions constitute the grid \(\{\varepsilon+j/5:0\le j\le4\}\), contained in \([\varepsilon,1-\varepsilon]\). There, directly from the Zak formulas, \(E(t,-1)=O(t,-1)\), so \(Z(t,-1)=0\) for all five columns, modulo nonzero quasi-periodicity factors. Thus a full frequency row vanishes at a fiber, and by continuity the essential lower singular-value bound is zero. Hence the Gabor system is not a frame. This also follows from Lemvig--Nielsen's general necessary condition as Theorem 1 in Stangl--Frederick.

## Verification
The standalone `checker.py` symbolically reconstructs both determinant polynomials and verifies representative exact nonframe-row cancellations. Its finite calculations are not used to infer the universal inequalities: the two unit-circle arguments and the four exhaustive geometric cases constitute the infinite proof. The matrix criterion is quoted with its parameter and normalizations from the cited 2026 paper.

## Relationship to prior work
Stangl and Frederick (arXiv:2609.00481, first public 2026-08-31), in Theorems 1, 3, and 4, prove the nonframe obstruction for general reduced \(p/q\), the sharp converse only for \(p=1\), and the Zibulski--Zeevi criterion; they explicitly leave the converse when \(p>1\) open. The present statement treats the concrete new slice \(p=2,q=5,2<b<5/2\) through two-column minor certificates; it is not a consequence of their \(p=1\) theorem. Earlier B-spline frame-set literature proves other nonframe and sufficient-frame regions; none of the inspected statements directly establishes this entire sharp slice.

## Limitations
No optimal numerical frame bounds, global extension in \(b\), or arbitrary \(p/q\) converse is claimed. The comparison does not establish absolute historical priority and remains subject to independent mathematical review. The claim presumes the standard Zibulski--Zeevi characterization and its normalizations; the elementary determinant identities were independently checked.

## References
1. A. Stangl and C. Frederick, *The frameset of the second-order B-Spline along \(ab=1/q\)*, arXiv:2609.00481v1 (2026-08-31), especially Theorems 1, 3, 4 and Section 3. https://arxiv.org/abs/2609.00481
2. A. G. D. Atindehou, C. Frederick, Y. B. Kouagou, and K. A. Okoudjou, *On the frame set of the second-order B-spline*, arXiv:1806.05614. https://arxiv.org/abs/1806.05614
3. K. H. Nielsen, *The Frame Set of Gabor Systems with B-spline Generators*, master's thesis, 2015.
4. M. Hasannasab and J. Lemvig, *The zero set of the Zak transform of B-splines with applications to Gabor frames*, arXiv:2609.13116 (2026). https://arxiv.org/abs/2609.13116
