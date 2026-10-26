# Selective veto subdivision can amplify voting-power concentration nearly \(t\)-fold

## Finding
For every integer \(a,m,t\ge1\), define a simple approval-voting game with \(t\) common veto seats and \(m\) disjoint, alternative committees of \(a\) seats each. A coalition wins precisely when it contains all veto seats and at least one entire committee. Let \(C\) be the squared Euclidean norm of the normalized Deegan–Packel power vector, as in Abe's voting-power concentration index. Then
\[
 C_{a,m}(t)=\frac{mt+a}{m(a+t)^2}.
\]
Selective subdivision of the original single veto seat into \(t\ge2\) jointly necessary veto seats, without changing the committees, **strictly increases** this concentration if and only if
\[
 m(a^2-t)>a(2a+t+1).
\]
For fixed \(t\ge2\), the amplification ratio is always strictly less than \(t\), and its supremum over positive integers \(a,m\) equals \(t\). In the family just defined, a concentration increase from one to two veto seats first becomes possible with **13 original voters**, namely \(a=3\), \(m=4\): concentration rises from \(7/64\) to \(11/100\) when the electorate expands from 13 to 14. For any fixed \(a,m\), concentration is nondecreasing and then nonincreasing as the number of veto seats grows, with at most one adjacent equality; eventually it tends to zero. These statements concern the specified family and this precise normalized index.

## Assumptions and scope
A simple game on a finite voter set is a monotone map from coalitions to losing/winning statuses, with the empty coalition losing and the grand coalition winning. Let \(V_t\) consist of \(t\ge1\) veto seats, and let \(L_1,\ldots,L_m\) be pairwise disjoint sets, each of size \(a\ge1\), also disjoint from \(V_t\). The minimal winning coalitions are exactly \(S_j=V_t\cup L_j\), for \(1\le j\le m\). These sets have the same cardinality \(a+t\) and are pairwise incomparable, so there are no other minimal winning coalitions.

If \(\mathcal M\) is the nonempty minimal winning family, the normalized Deegan–Packel index of a seat \(i\) is defined by
\[
 DP_i=\frac1{|\mathcal M|}\sum_{S\in\mathcal M:\,i\in S}\frac1{|S|},\qquad \sum_iDP_i=1.
\]
The concentration of voting power is \(C=\sum_i DP_i^2\). All statements quantify over positive integers \(a,m,t\) subject only to the displayed conditions; in the original electorate of the subdivision comparison there are \(1+am\) seats, and after subdivision there are \(t+am\) seats. The comparison changes the winning rule deliberately: the newly introduced veto seats must all approve.

## Proof
**Index formula.** Each of the \(t\) veto seats belongs to all \(m\) minimal coalitions and hence has \(DP=1/(a+t)\). Each of the \(am\) committee seats belongs to exactly one minimal coalition and hence has \(DP=1/[m(a+t)]\). Squaring and summing yields
\[
 C_{a,m}(t)=\frac{t}{(a+t)^2}+\frac{am}{m^2(a+t)^2}=\frac{mt+a}{m(a+t)^2}.
\]

**Exact threshold.** Since all denominators are positive, for integer \(t\ge2\), \(C_{a,m}(t)>C_{a,m}(1)\) is equivalent to
\[
 (mt+a)(a+1)^2>(m+a)(a+t)^2.
\]
The left-minus-right side factors *exactly* as
\[
 (t-1)\big[m(a^2-t)-a(2a+t+1)\big].
\]
Because \(t-1>0\), this proves the strict threshold; equality and reversal are obtained by replacing \(>\) with \(=\) or \(<\).

**Sharp amplification.** Division by the baseline gives
\[
 \frac{C_{a,m}(t)}{C_{a,m}(1)}
 =\frac{t+a/m}{1+a/m}\left(\frac{a+1}{a+t}\right)^2<t
\]
for all \(t\ge2\): the first factor is strictly less than \(t\) and the second is less than one. For any fixed such \(t\), choose \(m=a^2\) and let the positive integer \(a\) tend to infinity. The first factor tends to \(t\), and the second tends to one. Therefore the supremum equals \(t\) and is not attained by finite parameters.

**Sharp minimum within the family.** At \(t=2\), a strict increase requires \(m(a^2-2)>a(2a+3)\). No \(m\le2\) works: for \(a\ge2\) the left-minus-right side is at most \(-3a-4\), and for \(a=1\) it equals \(-m-5<0\). In particular, no \(a=1\) works; for \(a=2\) one needs \(m\ge8\), giving at least 17 initial seats; for \(a=3\), the first admissible value is \(m=4\), giving 13 initial seats. For \(a\ge4\), necessarily \(m\ge3\), so \(1+am\ge13\). Thus no smaller initial electorate in this family works. At \(a=3,m=4\), directly \(C(1)=7/64\), \(C(2)=11/100\), and their difference is \(1/1600>0\).

**Dependence on subdivision count.** Exact comparison of adjacent terms shows
\[
 \operatorname{sgn}(C_{a,m}(t+1)-C_{a,m}(t))
 =\operatorname{sgn}\big[m(a^2-t(t+1))-a(2a+2t+1)\big].
\]
For every integer \(t\ge1\), the expression inside the final sign is strictly decreasing in \(t\), so the sequence can switch from increasing to decreasing at most once, with at most one neighboring tie. Finally \(C(t)=(mt+a)/[m(a+t)^2]\to0\) as \(t\to\infty\).

## Verification
Run `python3 verify.py` using Python 3 and its standard library. The program independently constructs the minimal winning coalition sets, computes the normalized Deegan–Packel vector by exact `Fraction` arithmetic, and compares with every closed formula for 880 parameter triples (\(1\le a\le11\), \(1\le m\le10\), \(1\le t\le8\)). It also tests the 13-seat witness and excludes smaller members of this family, checks the adjacent sign, and tests sharp amplification along a large explicit family. Exact finite checks test implementation and algebra but are not substitutes for the general factorization and limiting arguments above.

## Relationship to prior work
The power index is due to Deegan and Packel (1978). Abe (2026) defines and studies the squared Deegan–Packel power concentration and proves that **uniform** replication of *every* player into the same number of jointly required seats scales concentration by the inverse replication factor. That result is not contradicted: the present operation replicates **only the common veto position**, leaving all committee seats intact. Abe also examines voting-system extensions by enlarging classes of seats; the exact selective-veto criterion and nearly \(t\)-fold rise proved here address a different structural operation. Other studies of merging/annexation, and of power-index ordinal rankings, do not directly supply this selective-splitting concentration formula. The claim of novelty is specifically the sharp structural comparison and its amplification and minimal-family consequences, not the definition or general properties of the index.

## Limitations
The 13-voter minimum holds **only** for this disjoint-committee petal family, not for all simple or weighted voting games. The expanded rule is a conjunctive subdivision of a veto role, not replacement by independently substitutable delegates. The result makes no claim about the desirability of this institutional operation, empirical prevalence, or any other power index. Prior specialized literature on player splitting may contain equivalent special cases; mathematical priority is provisional pending independent review. The scientific review reported separately is not independent validation.

## References
- Takaaki Abe, *Measuring Concentration of Power in Approval Voting Games*, arXiv:2606.05655, first posted June 4, 2026. https://arxiv.org/abs/2606.05655
- J. Deegan and E. W. Packel, *A New Index of Power for Simple n-Person Games*, International Journal of Game Theory **7** (1978), 113–123.
- T. A. Lasisi and R. N. Allan, *Annexations and Merging in Weighted Voting Games* (2011); comparison limited to accessible abstract.
