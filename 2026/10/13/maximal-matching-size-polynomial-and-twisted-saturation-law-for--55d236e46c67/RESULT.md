# Maximal-matching size polynomial and twisted saturation law for Möbius ladders

## Finding
Let \(M_{2n}\) denote the labeled Möbius ladder on \(2n\) vertices, with \(n\ge3\). For a matching \(F\), maximal means inclusion-maximal, not necessarily largest. Define its cardinality enumerator by
\[
P_n(z)=\sum_{F\text{ an inclusion-maximal matching of }M_{2n}}z^{|F|}.
\]
Put
\[
\begin{aligned}
Q_+(t,z)&=1-2zt-z^2t^3+z^3t^3-z^3t^4-z^4t^5,\\
Q_-(t,z)&=1+zt-z^2t^3.
\end{aligned}
\]
Then the full cardinality distribution, simultaneously for every integer \(n\ge3\), is
\[
\boxed{\sum_{n\ge3}P_n(z)t^n=-t\frac{\partial}{\partial t}\log\!\left(\frac{Q_+(t,z)}{Q_-(t,z)}\right)-3zt-3z^2t^2.}
\]
In particular, the saturation number (minimum cardinality of an inclusion-maximal matching) is
\[
\boxed{s(M_{2n})=\left\lfloor\frac{2n}{3}\right\rfloor+1.}
\]
The exact number of maximal matchings attaining this minimum is
\[
\boxed{
[z^{s(M_{2n})}]P_n(z)=
\begin{cases}
6,&n=3,\\
2r(7r^2-2r-3),&n=3r,\ r\ge2,\\
4n,&n=3r+1,\ r\ge1,\\
\dfrac{n(4n-2)}{3},&n=3r+2,\ r\ge1.
\end{cases}}
\]
The twist removes every would-be maximal matching of cardinality \(2n/3\) when \(3\mid n\). The polynomial also provides counts at every other size, not only at the minimum.

## Assumptions and scope
The vertex set is \(\{(i,a):0\le i<n,\ a\in\{0,1\}\}\), with edges joining \((i,0)\) to \((i,1)\); joining \((i,a)\) to \((i+1,a)\) when \(i<n-1\); and joining \((n-1,a)\) to \((0,1-a)\). Edges and vertices are distinguished by these labels. For \(n\ge3\) this is a simple cubic graph isomorphic to the cycle on \(2n\) vertices with diametric chords. No quotient by graph automorphisms is taken. A matching is maximal precisely when the vertices left unmatched form an independent set, since any edge between two unmatched vertices could otherwise be added.

## Proof
**1. Local encoding and bijection.** In each column record a pair of states, one per rail. The letter \(U\) means the vertex is unmatched; \(L\) means it is matched along its rail to the preceding column; \(R\) means it is matched along its rail to the next column. A selected rung is recorded as the exceptional state \((V,V)\). The rung itself rules out \((U,U)\). Thus there are exactly nine allowed states: \((V,V)\) and all eight members of \(\{U,L,R\}^2\setminus\{(U,U)\}\).

For consecutive states \(a,b\), impose, independently on each rail coordinate \(j\),
\[
(a_j=R)\ \Longleftrightarrow\ (b_j=L),
\qquad \neg(a_j=U\text{ and }b_j=U).
\]
The equivalence ensures each rail matching edge is recorded consistently at both endpoints; the second condition prevents adjacent unmatched endpoints. Rung edges are accounted for by the permitted states. Give state \(a\) the weight \(z^{w(a)}\), with \(w(V,V)=1\) and otherwise \(w(a)\) equal to the number of \(R\) letters in \(a\). Hence each selected edge contributes exactly one factor \(z\), with rail edges charged only at their left endpoint. A compatible cyclic state sequence therefore gives one and only one maximal matching, and conversely.

Let \(T(z)\) be the nine-by-nine matrix indexed by these states whose entry is \(z^{w(a)}\) if the transition from \(a\) to \(b\) is compatible, and zero otherwise. Let \(S\) transpose the two rail coordinates (and fix \((V,V)\)). The Möbius identification transposes the rails across the final boundary, so the exact polynomial is
\[
P_n(z)=\operatorname{tr}(T(z)^nS),\qquad n\ge3.
\]
This is a bijective equality, not an approximation or finite-state heuristic.

**2. Exact determinant and generating function.** The transfer matrix commutes with \(S\). The \(+1\) eigenspace of \(S\) has dimension six (three fixed states and three symmetric pairs), and the \(-1\) eigenspace has dimension three. In the explicit basis consisting of fixed-state vectors followed by symmetric and antisymmetric sums, direct integer-polynomial determinant calculation gives
\[
\det(I-tT|_{+})=Q_+(t,z),\qquad
\det(I-tT|_{-})=Q_-(t,z).
\]
The accompanying script constructs both matrices from the nine stated states and recomputes both determinants exactly; no numerical fitting is involved. The formal identity
\( -t\partial_t\log\det(I-tA)=\sum_{m\ge1}\operatorname{tr}(A^m)t^m\)
then gives the ratio because \(S\) acts with opposite signs on the two eigenspaces. The formal terms of degrees one and two are \(3zt\) and \(3z^2t^2\), which are omitted since the simple Möbius-ladder family begins at \(n=3\). This proves the complete generating function.

**3. Minimum and exact multiplicities.** To expose the lowest possible matching size, make the formal monomial substitution \(t=u/w^2\), \(z=w^3\). A coefficient \(z^kt^n\) becomes \(u^nw^{3k-2n}\). Under this substitution the two determinant factors become
\[
\begin{aligned}
\widetilde Q_+&=1-u^3-(2u+u^4)w-u^5w^2+u^3w^3,\\
\widetilde Q_-&=1-u^3+uw.
\end{aligned}
\]
The coefficient of \(w^0\) in the logarithm of their ratio cancels. Every other term has strictly positive power of \(w\), so no maximal matching can have \(3k-2n\le0\). This proves the lower bound \(k\ge\lfloor2n/3\rfloor+1\), with the stronger-than-ceiling bound at multiples of three.

For positivity and exact enumeration at that bound, write \(A=1-u^3\), and let \(L_j(u)\) be the coefficient of \(w^j\) in \(\log(\widetilde Q_+/\widetilde Q_-)\). Formal Taylor expansion, exact through degree three in \(w\), yields
\[
\begin{aligned}
L_1&=-\frac{3u+u^4}{A},\\
L_2&=-\frac{u^5}{A}-\frac{3u^2+4u^5+u^8}{2A^2},\\
L_3&=\frac{u^3}{A}-\frac{2u^6+u^9}{A^2}
-\frac{9u^3+12u^6+6u^9+u^{12}}{3A^3}.
\end{aligned}
\]
At \(n=3r+1\), the first admissible excess \(3k-2n\) is one. Using \(A^{-1}=\sum_{j\ge0}u^{3j}\) in \(-uL_1'(u)\) gives \(4n\) for \(r\ge1\). At \(n=3r+2\), the first admissible excess is two. Using \(A^{-2}=\sum_{j\ge0}(j+1)u^{3j}\) gives \(n(4n-2)/3\) for \(r\ge1\). At \(n=3r\), the first admissible excess is three; expanding \(A^{-3}=\sum_{j\ge0}\binom{j+2}{2}u^{3j}\) in \(-uL_3'(u)\) gives \(6\) at \(r=1\) and \(2r(7r^2-2r-3)\) at \(r\ge2\). All these quantities are strictly positive, so the lower bound is sharp and the minimum multiplicity formulas are exact. The argument applies to all eligible integers; no finite truncation is used to extrapolate the theorem.

## Verification
The attached `verify.py` (Python 3 plus SymPy) independently constructs the nine states and both symmetry blocks, checks the two determinant identities over integer polynomials, and uses Newton recurrences to recover every coefficient through \(n=40\). A separate exhaustive recursive enumeration of matchings checks the **complete size distribution** for each \(3\le n\le10\), with no transfer-matrix assumptions. Formal series checks confirm the three lowest-excess coefficients through order 54. Substituting \(z=1\) agrees with OEIS A284710 for \(3\le n\le28\).

Examples: \(P_3(z)=6z^3\), \(P_4(z)=16z^3+7z^4\), and \(P_5(z)=30z^4+13z^5\). The symbolic identities and bijection prove the unrestricted statement; finite checks are consistency evidence only.

## Relationship to prior work
The ungraded count \(P_n(1)\) is already known: OEIS A284710 gives its recurrence and scalar generating function. The ordinary matching polynomial displayed for Möbius ladders in MathWorld counts **all** matchings, whereas \(P_n(z)\) counts only inclusion-maximal matchings. Existing exact formulas for perfect matchings cover the highest cardinality alone. The present claim is the full maximal-matching size distribution and its extremal cardinality law, not the ungraded total or the existing perfect-matching count. General structural recurrences for Möbius ladders and circulant graphs were previously studied by McSorley and by Golin, Leung, and Wang; the statement here does not claim a new general transfer-matrix method.

## Limitations
The theorem covers labeled Möbius ladders with \(n\ge3\), and does not classify matchings up to graph automorphism or extend to arbitrary cubic graphs. The mathematical proof is exact but has not received independent review. McSorley's 1998 *Counting Structures in the Möbius Ladder* is highly relevant; its abstract and bibliographic record were accessible, but its complete text was not. Thus prior appearance of an equivalent cardinality-refined enumeration in that paper cannot be excluded by the available comparison. A search of known records is not a proof of priority.

## References
1. J. P. McSorley, *Counting Structures in the Möbius Ladder*, Discrete Mathematics 184 (1998), 137–164, DOI: 10.1016/S0012-365X(97)00086-1; repository abstract: https://opensiuc.lib.siu.edu/math_articles/93/ .
2. E. W. Weisstein, *Number of maximal matchings in the n-Moebius ladder*, OEIS A284710 (2017), https://oeis.org/A284710 .
3. E. W. Weisstein, *Möbius Ladder*, MathWorld, https://mathworld.wolfram.com/MoebiusLadder.html .
4. M. J. Golin, Y. C. Leung, and Y. Wang, *Counting Spanning Trees and Other Structures in Non-constant-jump Circulant Graphs*, ISAAC 2004, LNCS 3341, pp. 508–521, https://www.cse.ust.hk/~golin/pubs/golin_Isaac_04.pdf .
5. D. Jakobson and I. Rivin, *On some extremal problems in graph theory*, public arXiv version of 1999-07-08, arXiv:math/9907050v1, https://arxiv.org/abs/math/9907050 .
6. s.-m. belcastro, *Domino Tilings of 2 by n Grids (or Perfect Matchings of Grid Graphs) on Surfaces*, Journal of Integer Sequences 26 (2023), Article 23.5.6, https://cs.uwaterloo.ca/journals/JIS/VOL26/Belcastro/belcastro4.pdf .
