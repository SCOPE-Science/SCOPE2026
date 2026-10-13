# The first Hamilton–Webster separation is an exact three-claimant cone
## Finding
Consider proportional apportionment with positive claims and no mandatory minimum seat per claimant. Hamilton means the Hare largest-remainder method, and Webster means the major-fractions divisor method, equivalently Sainte-Laguë priorities.

For one seat, Hamilton and Webster have the same full correspondence for any number of claimants: both award the seat to a claimant of maximum size, with the same ties.

For two claimants, Hamilton and Webster have the same full correspondence for every house size, including ties.

Consequently a unique-outcome disagreement first becomes possible with three claimants and two seats. Write their strictly ordered claims as
\[
0<p<q<r.
\]
For house size \(2\), Hamilton and Webster have different unique apportionments if and only if
\[
3q<r<p+3q.
\]
Every point in this open cone has
\[
\operatorname{Hamilton}(p,q,r;2)=(0,1,1)
\]
and
\[
\operatorname{Webster}(p,q,r;2)=(0,0,2).
\]

The two bounding hyperplanes are exactly the tie boundaries. At
\[
r=3q,
\]
Webster ties between \((0,1,1)\) and \((0,0,2)\), while Hamilton uniquely chooses \((0,1,1)\). At
\[
r=p+3q,
\]
Hamilton ties between those two apportionments, while Webster uniquely chooses \((0,0,2)\).

Among primitive positive integer triples, even allowing equal claims before quotienting by permutation, the unique minimum-total profile with distinct unique outcomes is
\[
(p,q,r)=(2,3,10),
\]
whose total claim is \(15\). Hamilton gives \((0,1,1)\); Webster gives \((0,0,2)\).

## Assumptions and scope
The model is the standard mathematical apportionment problem with nonnegative integer seat allocations summing to the prescribed house size. There is no exogenous rule requiring each claimant to receive at least one seat. This makes the theorem directly applicable to party-list proportional representation and to unconstrained resource apportionment; it is not a claim about the constitutional minimum-one-seat rule for U.S. states.

Claims are positive. The three-claimant cone is stated after sorting them strictly as \(p<q<r\), so its interior has no claim-size ties.

Hamilton uses exact quotas, assigns all lower quotas, and then distributes remaining seats to largest fractional remainders. Webster uses nearest-integer divisor rounding, equivalently the odd-divisor priority sequence \(1,3,5,\ldots\).

Correspondences, rather than arbitrary external tie-breaking, are compared. Thus the theorem identifies both strict disagreement and its exact tie boundaries.

## Proof
First consider two claimants with positive claims \(a,b\) and house size \(h\). Let
\[
x=\frac{ha}{a+b}
\]
be the exact quota of the first claimant. Hamilton gives that claimant precisely the integer or integers \(t\) satisfying
\[
|t-x|\le \frac12,
\]
where equality is the familiar largest-remainder tie.

For Webster, an allocation \((t,h-t)\) is feasible exactly when some positive divisor \(D\) makes both nearest-integer roundings valid:
\[
t-\frac12\le \frac aD\le t+\frac12,
\qquad
h-t-\frac12\le \frac bD\le h-t+\frac12.
\]
The two divisor intervals overlap exactly when
\[
b\left(t-\frac12\right)\le a\left(h-t+\frac12\right)
\]
and
\[
a\left(h-t-\frac12\right)\le b\left(t+\frac12\right).
\]
After rearrangement these are exactly
\[
x-\frac12\le t\le x+\frac12.
\]
Hence Hamilton and Webster have identical two-claimant correspondences for every house size.

Now take three strictly ordered claims \(0<p<q<r\) and house size \(2\).

For Webster, the largest first priority is \(r\), so the largest claimant receives the first seat. The only contenders for the second seat are the first priority \(q\) of the middle claimant and the second priority \(r/3\) of the largest claimant, because \(p<q\). Therefore Webster gives both seats to the largest claimant exactly when
\[
\frac r3>q,
\]
or equivalently \(r>3q\). It splits the seats between the two largest claimants when \(r<3q\), with a tie at \(r=3q\).

For Hamilton, let
\[
S=p+q+r.
\]
If \(2r/S<1\), every lower quota is zero and the two largest quotas are those of \(r\) and \(q\), so Hamilton gives \((0,1,1)\).

Otherwise the largest claimant has lower quota one, and exactly one seat remains. Its fractional remainder is
\[
\frac{2r}{S}-1,
\]
while the middle claimant's remainder is
\[
\frac{2q}{S}.
\]
The smallest claimant has a still smaller remainder. Thus the middle claimant receives the last seat exactly when
\[
\frac{2q}{S}>\frac{2r}{S}-1,
\]
which rearranges to
\[
r<p+3q.
\]
At equality Hamilton ties, and above equality the largest claimant receives both seats.

If Webster splits, then \(r<3q<p+3q\), so Hamilton also splits. Therefore strict unique disagreement occurs exactly when Webster has crossed its threshold but Hamilton has not:
\[
3q<r<p+3q.
\]

For the smallest primitive integer witness, sort positive integers weakly. If \(q=1\), no positive \(p<q\) exists in a strict disagreement. If \(q=2\), the only smaller positive claim is \(p=1\), and the required interval is \(6<r<7\), containing no integer. If \(q=3\), then \(p=1\) gives \(9<r<10\), again empty, while \(p=2\) gives \(9<r<11\), forcing \(r=10\). Hence \((2,3,10)\) is the unique minimum-total primitive witness up to permutation.

## Verification
The embedded `verify_hamilton_webster_two_seat.py` uses only the Python standard library and exact rational arithmetic.

It independently implements Hamilton by exact lower quotas plus exhaustive cutoff ties and Webster by exact Sainte-Laguë priorities plus exhaustive cutoff ties.

The replay checks:
- every strictly ordered integer triple in a box containing \(222680\) triples, verifying disagreement exactly on \(3q<r<p+3q\);
- both tie boundaries exactly;
- Hamilton–Webster correspondence equality for all two-claimant integer problems with claims through \(60\) and house sizes through \(40\);
- one-seat agreement on representative multi-claimant cases;
- the primitive minimum-total witness search, allowing weakly ordered claims, which returns only \((2,3,10)\) at total \(15\).

Run:

`python3 verify_hamilton_webster_two_seat.py`

The first output line must be `VERIFY_OK`.

The universal statements are proved algebraically above; the finite replay is a consistency check and a certificate for the stated integer minimum search.

## Relationship to prior work
Balinski and Young's classical treatment gives the standard Hamilton largest-remainder construction and Webster nearest-integer divisor construction. Their 1975 exposition presents the two rules side by side in the general apportionment problem.

The literature also records the exact two-claimant coincidence: Hamilton and Webster both reduce to the standard nearest-quota solution for every two-claimant problem. This makes the three-claimant case the natural first place to ask how their extensions separate.

The checked literature discusses many differences between Hamilton and divisor methods, including quota and monotonicity behavior, and gives larger numerical examples. It does not, in the inspected material, state the exact three-claimant, two-seat disagreement cone \(3q<r<p+3q\), its two tie boundaries, or the primitive minimum witness \((2,3,10)\).

Targeted searches using Hamilton/Webster, Hare/Sainte-Laguë, two-state equivalence, three-claimant/two-seat language, the exact inequalities, and the exact witness did not locate an equivalent theorem or table.

## Limitations
The three-claimant cone is for house size \(2\) in the unconstrained apportionment model; it does not incorporate statutory minimum-seat requirements.

The result does not classify Hamilton–Webster disagreement at larger house sizes or with four or more claimants.

The two-claimant equivalence is classical rather than new; the contribution is the exact first separation geometry immediately beyond that classical coincidence.

A specialized apportionment exercise, historical note, or unindexed computational table could contain the same small-house cone.

## References
1. M. L. Balinski and H. P. Young, “The Quota Method of Apportionment,” *The American Mathematical Monthly* 82(7), 701–730, 1975. DOI: 10.1080/00029890.1975.11993911.
2. M. L. Balinski and H. P. Young, “The Webster Method of Apportionment,” *Proceedings of the National Academy of Sciences* 77(1), 1–4, 1980. DOI: 10.1073/pnas.77.1.1.
3. H. P. Young, “Dividing the House: Why Congress Should Reinstate an Old Reapportionment Formula,” Brookings Institution, 31 August 2001.
