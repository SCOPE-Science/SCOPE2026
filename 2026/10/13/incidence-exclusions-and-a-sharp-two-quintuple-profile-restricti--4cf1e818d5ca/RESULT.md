# Incidence exclusions and a sharp two-quintuple profile restriction for thirteen lines
## Finding
For an arrangement of exactly \(13\) distinct complex projective lines, let \(n_j\) be the number of distinct points on exactly \(j\) lines. Suppose that every line contains at most \(6\) distinct arrangement singular points, that the maximal point multiplicity is \(5\), and that \(n_4=0\).

**Theorem.** If \(n_5=2\), then \(n_3\) belongs to \(\{15,16,18\}\), with the corresponding complete possible multiplicity profiles
\[
(n_2,n_3,n_4,n_5)\in\{(13,15,0,2),(10,16,0,2),(4,18,0,2)\}.
\]
The middle profile \((10,16,0,2)\) occurs for an explicit arrangement over \(\mathbf C\). If \(n_5=3\), the profile \((15,11,0,3)\) is impossible. In particular, the two profiles \((7,17,0,2)\) and \((15,11,0,3)\) listed as numerical possibilities in Dimca--Pokora, Proposition 5.6, are not realizable under its six-points-per-line constraint.

## Assumptions and scope
All geometry is in \(\mathbf P^2_{\mathbf C}\); all \(13\) lines are distinct, and every two intersect. A singular point is any point lying on at least two arrangement lines. Write \(\rho(L)\) for the number of **distinct** singular points lying on line \(L\), and \(n_j(L)\) for the number of those points of multiplicity \(j\). The hypotheses are \(\rho(L)\le6\) for all lines, \(n_j=0\) for \(j\ge6\) and \(j=4\), with the stated \(n_5\). The restrictions are necessary conditions, not an exhaustive geometric classification of all three surviving numerical profiles.

## Proof
**Local counting.** Each line meets the other \(12\) lines counted with multiplicity; hence
\[
 n_2(L)+2n_3(L)+4n_5(L)=12,\qquad
 \rho(L)=n_2(L)+n_3(L)+n_5(L).
\]
Writing \(t=n_5(L)\), subtraction gives
\[
 n_3(L)=12-\rho(L)-3t,\qquad n_2(L)=2\rho(L)-12+2t.
\]
For any line not through a quintuple point, \(t=0\); nonnegativity and \(\rho(L)\le6\) imply \(\rho(L)=6\), \(n_2(L)=0\), \(n_3(L)=6\). In particular, **each such exterior line has no ordinary double point**.

**Exactly two quintuple points.** Denote them by \(A,B\). If their joining line is *absent*, the arrangement consists of five lines through \(A\), five through \(B\), and exactly three exterior lines \(D_1,D_2,D_3\). The latter contribute exactly \(18\) line--triple-point incidences. If the three exterior lines concur, their common point is a triple point (it cannot be on another line, since quadruple points are excluded). It contributes three exterior incidences; the other \(15\) exterior incidences each occur at a triple point containing exactly one exterior line. Thus \(n_3=1+15=16\). If the three exterior lines are not concurrent, their three pairwise intersections are distinct triple points, as the exterior lines have no double points; each contains two exterior lines and one pencil line. They contribute \(6\) exterior incidences; the other \(12\) incidences each represent a triple point with exactly one exterior line. Hence \(n_3=3+12=15\). There can be no triple point involving no exterior line outside \(A,B\): two different lines of a pencil meet only at its center, and an \(A\)-line and a \(B\)-line supply at most two lines.

If \(AB\) *is* one of the arrangement lines, the union of the two five-line pencils has \(9\) lines, so there are exactly \(4\) exterior lines. The joining line \(AB\) already has two quintuple points, consuming \(8\) of its \(12\) intersections with other lines; its remaining \(4\) intersections are with exterior lines. Since exterior lines have no double points and a point of \(AB\) away from \(A,B\) cannot lie on another line of either pencil, the exterior lines pair off at exactly two distinct triple points on \(AB\). Each of the \(4\) cross-pair intersections of exterior lines is off \(AB\), is distinct from the others, and is a triple point with exactly one additional pencil line (no double or quadruple points). Thus the exterior lines have \(24\) triple-point incidences in total: \(4\) at the two points on \(AB\), \(8\) at the four cross-pair points, and \(12\) at twelve further triples each containing a unique exterior line. There are no triple points devoid of exterior lines. Therefore \(n_3=2+4+12=18\).

For every arrangement of \(13\) lines, counting pairs of lines yields
\[
\binom{13}{2}=n_2+3n_3+10n_5.
\]
With \(n_5=2\), we obtain \(n_2=58-3n_3\), proving precisely the three necessary profiles.

**A complex witness for the middle profile.** Let \(\zeta\) be a primitive fifth root of unity. Take the \(13\) lines
\[
 x-\zeta^i y=0\quad (0\le i<5),\qquad
 y-\zeta^j z=0\quad (0\le j<5),\qquad
 z-\zeta^k x=0\quad (0\le k<3).
\]
The first two pencils have quintuple centers \([0:0:1]\) and \([1:0:0]\). Their \(25\) mutual crossing points are distinct, and precisely \(15\) lie on one of the final three lines, because the condition \(i+j+k\equiv0\pmod5\) has exactly \(5\) solutions for each of the three \(k\)-values. These are \(15\) triple points; the remaining \(10\) are ordinary double points. The final three lines meet at \([0:1:0]\), giving one more triple point. No other intersection occurs. Each first- or second-pencil line has one quintuple point, three triple points and two double points; each final line has six triple points. Thus \(\rho(L)=6\) for all lines, and the profile is \((10,16,0,2)\).

**Three quintuple points.** Assume for contradiction the profile \((15,11,0,3)\). Counting line--singular-point incidences gives
\[
\sum_{L}\rho(L)=2(15)+3(11)+5(3)=78=13\cdot6.
\]
Every line therefore has exactly \(6\) singular points, and the local identities reduce to \(n_3(L)=6-3t\), \(n_2(L)=2t\), where \(t=n_5(L)\). No line can pass through all three quintuple points, and a line through two of them supports **no triple point**.

The three quintuple points have \(15\) line-incidences in total. Since there are only \(13\) distinct lines, at least two lines connect pairs of quintuple points. If exactly two do, they share a quintuple point, say \(A\), and are \(AB,AC\). The remaining lines comprise \(3\) through \(A\) only, \(4\) through \(B\) only and \(4\) through \(C\) only. The connecting lines support no triple, while each triple requires one line from each of these three remaining pencil classes. But the three \(A\)-only lines each support exactly three triples, allowing at most \(9\), contrary to \(n_3=11\). If instead all three connectors \(AB,AC,BC\) are present, \(12\) distinct lines pass through a quintuple point, leaving one exterior line \(D\). That exterior line has no double intersections. Yet its intersection with connector \(AB\) is away from \(A,B\), and the connector (having two quintuple points) supports no triple, forcing an ordinary double intersection with \(D\). Contradiction. These exhaust the possibilities, proving nonexistence.

## Verification
The standalone \(`verify_incidence.py`\) program uses exact arithmetic in \(\mathbb F_{11}\) with an element of order \(5\), computes all pairwise intersection points of the explicit \(13\)-line witness, and checks the full multiplicity profile, the six-points-per-line property, and basic integer pair-count identities. It prints \(`VERIFY_OK`\). The complex witness and both universal obstructions are established by the proofs above: reduction modulo a finite field alone does not prove a universal nonexistence theorem.

## Relationship to prior work
Dimca and Pokora's *A generalized Terao Conjecture for line arrangements* (arXiv:2609.33584v1, first public 2026-09-27), Proposition 5.6, lists \((7,17,0,2)\) and \((15,11,0,3)\) among \(15\) remaining **numerical** profiles in the \(13\)-line, maximal multiplicity-five case. The present incidence proof eliminates those two profiles as geometrically nonrealizable; it does **not** resolve the conjecture for other profiles. Dimca--Ibadula--Măcinic, *Freeness and near freeness are combinatorial for line arrangements in small degrees* (arXiv:1712.04400v2), proves an earlier result about ordinary freeness for \(13\) lines; its freeness hypotheses do not imply these nonfree-profile exclusions. The Fermat subarrangement is an explicit realization of one surviving numerical type, without any new freeness or syzygy claim.

## Limitations
The trichotomy lists necessary profiles, not the existence of its first and third entries. Only the middle profile is exhibited. The result does not determine minimal Jacobian syzygy degrees, Jacobian-module invariants, free/nearly-free status, or all remaining candidates. Historical implicit coverage by broader incidence combinatorics cannot be completely excluded without exhaustive bibliographic review.

## References
1. A. Dimca and P. Pokora, *A generalized Terao Conjecture for line arrangements*, arXiv:2609.33584v1 (first public 2026-09-27), Proposition 5.6 and its preceding incidence estimates.
2. A. Dimca, D. Ibadula and A. Măcinic, *Freeness and near freeness are combinatorial for line arrangements in small degrees*, arXiv:1712.04400v2 (earlier small-degree freeness comparison).
