# Three incidence obstructions for degree-nine cubic–line freeness

## Finding

Let \(D\subset\mathbb P^2_{\mathbb C}\) be a reduced union of \(k\ge1\) **distinct smooth plane cubics** and \(\ell\ge1\) distinct projective lines, of total degree \(3k+\ell=9\). Assume every singularity of \(D\) is an ordinary node \(A_1\), an ordinary triple point \(D_4\), or a two-branch \(A_5\) singularity. If \(D\) is free, then necessarily
\[
 (k,\ell;n_2,n_3,t_5)=(2,3;3,0,9).
\]
In particular, no such free arrangement consists of one smooth cubic and six lines. This is a **necessary condition, not an existence assertion** for the surviving numerical type.

Among the four degree-nine weak-combinatorics possibilities identified in Talar's 2023 preprint (2024 revision), the three impossible types are
\[
 (1,6;0,7,4),\qquad(1,6;3,5,5),\qquad(2,3;0,2,8).
\]
Here \(n_2,n_3,t_5\) count nodes, ordinary triple points, and \(A_5\) points, respectively.

## Assumptions and scope

All curves and intersections are geometric over \(\mathbb C\). Every cubic component is smooth; the components are distinct; each listed singularity has precisely the analytic branches of its stated type. In particular, an \(A_5\) point comprises exactly two smooth branches of intersection multiplicity three, while an ordinary triple point has three smooth branches with distinct tangent lines. Finiteness and intersection multiplicities are those of ordinary complex projective curves. The statement concerns freeness of the logarithmic derivation module, not near-freeness.

## Proof

**1. Numerical reduction.** Write \(f=t_5\). A free degree-nine curve in this singularity class has minimal Jacobian relation degree \(r=4\). Indeed, the local Arnold exponents of \(A_1,D_4,A_5\) are at least \(2/3\); the Dimca–Sernesi bound gives \(r\ge(2/3)9-2=4\), while free exponents satisfy \(2r\le8\). The free-divisor Tjurina formula therefore yields
\[
 \tau(D)=8^2-4(8-4)=48.
\]
Each node contributes \(1\), ordinary triple \(4\), and \(A_5\) point \(5\), so
\[
 n_2+4n_3+5f=48.\tag{1}
\]
Counting intersections of distinct components with Bézout's theorem gives
\[
 B(k,\ell)=9\binom{k}{2}+3k\ell+\binom{\ell}{2}
             =n_2+3n_3+3f.\tag{2}
\]
For \((k,\ell)=(1,6)\), \(B=33\), and (1)–(2) imply
\[
 n_3=15-2f,\qquad n_2=3f-12.
\]
A line cannot have two order-three contacts with one cubic, hence \(f\le6\). Nonnegativity leaves \(f=4,5,6\). For \(f=6\) the counts are \((n_2,n_3,f)=(6,3,6)\), which violate the necessary orbifold inequality proved by Talar,
\[
 27k+n_2+\frac34 n_3\ge \ell+5f,
\]
because \(27+6+9/4<6+30\). The two remaining numerical types are \((0,7,4)\) and \((3,5,5)\).

For \((k,\ell)=(2,3)\), \(B=30\), and (1)–(2) give
\[
 n_3=18-2f,\qquad n_2=3f-24.
\]
There are at most three \(A_5\) points between the two cubics (their total intersection number is nine), and at most one between each cubic–line pair (six such pairs). Thus \(f\le9\). Nonnegativity forces \(f\in\{8,9\}\), giving \((0,2,8)\) and \((3,0,9)\). These exhaust the four numerical possibilities. No existence is inferred from this integer reduction.

**2. One cubic and six lines.** Let \(t\) denote triple points involving three lines, and \(u\) ordinary triple points involving the cubic and exactly two lines, so \(n_3=t+u\). Each of the six lines meets only five other lines, so belongs to at most two triple points of the first kind. Counting line–triple incidences yields
\[
 3t\le6\cdot2,\qquad t\le4.\tag{3}
\]
Every \(A_5\) point is an order-three cubic–line tangency. Bézout implies its line meets the cubic nowhere else; moreover a line occurring in a mixed ordinary triple is transverse to the cubic at that point. Consequently the \(f\) flex-tangent lines are distinct and cannot occur in mixed triples. A mixed triple uses a pair of the other \(6-f\) lines, and each pair has only one intersection point. Therefore
\[
 u\le \binom{6-f}{2}.\tag{4}
\]
For \((n_2,n_3,f)=(0,7,4)\), (3) requires \(u\ge7-4=3\), while (4) gives \(u\le\binom22=1\), a contradiction. For \((3,5,5)\), (4) gives \(u=0\), hence \(t=5\), contradicting (3). Therefore **neither** one-cubic–six-line numerical type can occur.

**3. Two cubics and three lines.** Suppose \((n_2,n_3,f)=(0,2,8)\). The three lines have three pairwise line–line incidences. If they are not concurrent, their three distinct pairwise intersections cannot be nodes, because \(n_2=0\); nor can they be \(A_5\) points, because two distinct lines meet transversely. Each would therefore need to be an ordinary triple point, contradicting \(n_3=2\). Hence the three lines are concurrent at one ordinary triple point. No cubic passes through that point, since this would create more than three smooth branches.

The sole other triple point must contain **both** cubic components and exactly one line: no further two lines can intersect away from their concurrency point. At this triple the two cubics meet transversely, with local intersection multiplicity one. Every other intersection of those two cubics is an \(A_5\) point, contributing intersection multiplicity three, because nodes and further ordinary triples are absent. Bézout would therefore force \(9=1+3a\) for some nonnegative integer \(a\), which is impossible modulo three. Thus \((2,3;0,2,8)\) cannot occur.

The only remaining possibility is \((2,3;3,0,9)\), establishing the stated necessary condition. \(\square\)

## Verification

The self-contained `CHECK.py` enumerates all nonnegative integer solutions of (1)–(2), verifies the necessary orbifold bound and upper bound on \(A_5\) contacts, and checks the integer inequalities excluding three types. Execute `python3 CHECK.py` in a directory containing this document and the script. Its successful output is `CHECK_OK: four numerical types; three excluded by incidence conditions`. The script verifies integer computations; the geometric arguments about flex lines, concurrency, and intersection multiplicities are the proof above and do **not** follow from finite enumeration.

## Relationship to prior work

Talar's *On cubic-line arrangements with simple singularities* (arXiv:2305.01530, initially public on 2023-05-02; version 2 dated 2024-03-26) proves the orbifold bound and identifies exactly the four possible degree-nine numerical types, explicitly leaving their geometric realization unresolved (Section 3, especially Theorem 3.5 and the preceding discussion). The present result goes beyond that numerical list by ruling out three types through incidence constraints. In *Construction of free curves by adding lines to a given curve* (arXiv:2301.01117, initially public on 2023-01-03), Dimca–Ilardi–Pokora–Sticlaru construct several free curves using flex lines and other singularities; those constructions do not assert the present nonrealizability result for arrangements with only \(A_1,D_4,A_5\) singularities. Existing concrete degree-six and degree-seven cubic–line examples also do not imply a degree-nine nonexistence statement.

## Limitations

The numerical type \((2,3;3,0,9)\) remains unresolved: it is not asserted to exist or to be free. The conclusion assumes all cubic components smooth and all singularities exactly among the specified three analytic types over \(\mathbb C\); it does not extend to arbitrary singular cubic components, additional singularities, near-free curves, or positive characteristic. The proof does not classify projective equivalence classes or infinitesimal realization schemes. Exhaustive coverage of the global literature is not claimed.

## References

1. P. Talar, *On cubic-line arrangements with simple singularities*, arXiv:2305.01530v2 (2024 revision of 2023 preprint), Section 3 and Theorem 2.2. https://arxiv.org/html/2305.01530v2
2. A. Dimca, G. Ilardi, P. Pokora, G. Sticlaru, *Construction of free curves by adding lines to a given curve*, arXiv:2301.01117v4 (2023), especially Introduction and Sections 5–6. https://arxiv.org/html/2301.01117v4
3. A. Dimca and E. Sernesi, *Syzygies and logarithmic vector fields along plane curves*, Journal de l'École polytechnique — Mathématiques 1 (2014), 247–267; inequality used in Reference 1.
