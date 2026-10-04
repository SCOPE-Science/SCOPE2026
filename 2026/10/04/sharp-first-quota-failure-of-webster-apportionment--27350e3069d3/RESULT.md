# Sharp first quota failure of Webster apportionment
## Finding
Consider pure Webster apportionment, also called the major-fractions or Sainte-Laguë divisor method, for positive shares
\[
p_1+p_2+p_3+p_4=1,
\]
with no statutory minimum-seat requirement. In highest-averages form, if entity \(i\) currently has \(a_i\) seats, its next priority is proportional to
\[
\frac{p_i}{2a_i+1}.
\]
Assume the cutoff is strict, so no tie-breaking convention is involved.

The coordinatewise-minimal parameter cell \((s,h)\), ordered by number of entities \(s\) and house size \(h\), in which Webster can violate quota is
\[
(s,h)=(4,3).
\]
Every violation in this cell is an upper-quota violation. After relabeling the violating entity as \(A\), the complete violation chamber is
\[
\frac58<p_A\le\frac23,
\qquad
p_B,p_C,p_D<\frac{p_A}{5}.
\]
In this chamber Webster assigns all three seats to \(A\), although the upper quota of \(A\) is only two.

Under normalized Lebesgue measure on the four-entity share simplex, equivalently the Dirichlet distribution with all parameters equal to one, the probability of a quota violation is exactly
\[
\frac1{1350}.
\]

Among positive integer populations, the least possible total is nine. Up to permutation, the unique least-total witness is
\[
(6,1,1,1),
\]
for which Webster assigns \((3,0,0,0)\) while the upper quota of the largest entity is two.

## Assumptions and scope
An apportionment has \(s\) entities, positive shares summing to one, and a house of \(h\) seats. No entity is guaranteed a seat. Webster is the divisor method with rounding threshold \(a+1/2\), equivalently the sequential priority rule \(p_i/(2a_i+1)\). The theorem excludes ties at the last selected priority.

Entity \(i\) has exact quota \(hp_i\), lower quota \(\lfloor hp_i\rfloor\), and upper quota \(\lceil hp_i\rceil\). A quota violation means receiving fewer than the lower quota or more than the upper quota.

Coordinatewise minimality means that \((4,3)\) admits a violation while every \((s',h')\) with \(s'\le4\), \(h'\le3\), and at least one strict inequality is quota-safe.

## Proof
For one seat quota cannot fail: a positive share has upper quota at least one, while every lower quota is zero.

For two seats, suppose an entity \(A\) receives both seats. Its first two Webster priorities are \(p_A\) and \(p_A/3\). If its upper quota were only one, then \(p_A\le1/2\). To receive both seats uniquely, every rival first priority would have to satisfy
\[
p_j<\frac{p_A}{3}.
\]
With at most three rivals this gives
\[
1-p_A<3\frac{p_A}{3}=p_A,
\]
forcing \(p_A>1/2\), a contradiction. A lower-quota violation with two seats would require some zero-seat entity to have share at least \(1/2\). Keeping its first priority out of the top two would require either two rival first priorities whose shares sum to more than one, or a rival second priority \(p_j/3>p_A\), which would force \(p_j>1\). Thus no cell with \(h\le2\) and \(s\le4\) violates quota.

Now take three seats and at most three entities. A zero-seat entity with lower quota at least one would have \(p_A\ge1/3\). Excluding its first priority from the top three would require three rival priorities above \(p_A\); with at most two rivals, one rival would have to contribute a second priority, forcing \(p_j/3>p_A\) and hence \(p_j>1\). A one-seat entity can violate lower quota only if \(p_A\ge2/3\); then its second priority \(p_A/3\) cannot be pushed below the top three because the total share of all rivals is at most \(1/3\). For upper quota, two seats could violate only if \(p_A\le1/3\), but selecting \(p_A/3\) among the top three is incompatible with the other shares summing to at least \(2/3\); three seats could violate only if \(p_A\le2/3\), while selecting \(p_A/5\) above both rival first priorities would imply
\[
1-p_A<2\frac{p_A}{5},
\]
so \(p_A>5/7>2/3\). Therefore every cell with \(s\le3\) and \(h\le3\) is safe.

It remains to classify \((4,3)\). A lower-quota violation is impossible by the same priority-counting arguments above. An upper-quota violation by an entity receiving two seats would require \(p_A\le1/3\), but then selecting \(p_A/3\) among the top three contradicts the mass carried by the three rivals. Hence any violation must give all three seats to one entity \(A\).

All three seats go to \(A\) exactly when its third priority beats every rival first priority:
\[
\frac{p_A}{5}>
\max(p_B,p_C,p_D).
\]
Upper quota is then violated exactly when
\[
3p_A\le2.
\]
The strict priority inequalities also imply
\[
1-p_A<3\frac{p_A}{5},
\]
so \(p_A>5/8\). This proves the complete chamber
\[
\frac58<p_A\le\frac23,
\qquad p_j<\frac{p_A}{5}\ (j\ne A).
\]
It is nonempty, so \((4,3)\) is the coordinatewise-minimal failure cell.

For the probability, fix the violating label \(A\) and write \(x=p_A\). Conditional on \(x\), normalize the other three shares by \(1-x\). Their cap is
\[
t=\frac{x}{5(1-x)},
\]
which ranges from \(1/3\) to \(2/5\). For a uniform point on the two-simplex,
\[
\Pr(\max Y_j<t)=1-3(1-t)^2+3(1-2t)^2=(3t-1)^2.
\]
The marginal density of \(x\) is \(3(1-x)^2\), so the fixed-label probability is
\[
\int_{5/8}^{2/3}3(1-x)^2\left(\frac{3x}{5(1-x)}-1\right)^2dx
=
\int_{5/8}^{2/3}\frac{3(8x-5)^2}{25}\,dx
=
\frac1{5400}.
\]
The four labeled chambers are disjoint, giving total probability \(4/5400=1/1350\).

For positive integer populations, write the dominant population as \(a\). The chamber requires \(a>5b\), \(a>5c\), and \(a>5d\), so \(a\ge6\). At total nine, \((6,1,1,1)\) satisfies the strict quotient inequalities and has exact quota two for the dominant entity. No smaller total can satisfy \(a\ge6\) with three positive rivals, proving minimality and uniqueness up to permutation.

## Verification
The embedded `verify_webster43_quota_boundary.py` uses exact integer and rational arithmetic. It implements Webster by sequential priorities and independently checks the corresponding divisor interval for each strict allocation.

The verifier exhausts all positive integer profiles through total population \(40\) in every coordinatewise predecessor cell, finding no quota violation. In \((4,3)\) it requires exact agreement between actual violations and the analytic chamber, verifies that every violation is an upper-quota failure with allocation \((3,0,0,0)\) after relabeling, and confirms the unique least-total sorted witness \((6,1,1,1)\). It also evaluates the simplex integral exactly as \(1/1350\).

These finite sweeps are consistency checks for the analytic proof and are not used to infer the continuum theorem.

Run:

`python3 verify_webster43_quota_boundary.py`

The first line must be `VERIFY_OK`.

## Relationship to prior work
Balinski and Young's 1980 paper gives the divisor formulation of Webster, with divisor criterion \(d(a)=a+1/2\), and states that Webster rounds modified quotas to the nearest integer. It also proves a striking three-entity boundary theorem: Webster is the unique divisor method satisfying quota for every three-entity problem. Thus Webster's general quota behavior and its special safety at three entities are prior work, not part of the novelty claim.

The same paper proves that no population-monotone method can satisfy quota uniformly once there are at least four entities and the house is sufficiently large. That theorem is qualitative and asymptotic in the house size. It does not identify the smallest four-entity house in which Webster itself fails, nor the geometry or measure of that first failure.

The contribution here is the exact local boundary: the first cell \((4,3)\), its complete tie-independent chamber, the exact uniform-simplex probability \(1/1350\), and the unique least-total integer witness \((6,1,1,1)\).

## Limitations
The theorem concerns pure mathematical apportionment without a statutory one-seat minimum. In applications that mandate one seat per entity, the smallest admissible house can differ.

The probability is with respect to uniform Lebesgue measure on the share simplex, not an empirical population model.

The literature search found no source stating the full \((4,3)\) chamber, probability, and integer-minimal witness. An unindexed historical note, exercise, thesis, or supplementary computation could contain an equivalent calculation.

## References
1. M. L. Balinski and H. P. Young, “A New Method for Congressional Apportionment,” *Proceedings of the National Academy of Sciences USA* 71 (1974), 4602–4606. DOI: 10.1073/pnas.71.11.4602.
2. M. L. Balinski and H. P. Young, “The Quota Method of Apportionment,” *American Mathematical Monthly* 82 (1975), 701–730. DOI: 10.1080/00029890.1975.11993911.
3. M. L. Balinski and H. P. Young, “The Webster Method of Apportionment,” *Proceedings of the National Academy of Sciences USA* 77 (1980), 1–4. DOI: 10.1073/pnas.77.1.1.
