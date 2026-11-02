# Four unrestricted two-variable theories of orthogonal polarities in finite projective planes

## Finding

Let \(\Pi\) be any finite projective plane of order \(q\ge2\), and let \(\pi\) be a polarity with exactly \(q+1\) absolute points. On the points of \(\Pi\), define a symmetric binary relation
\[
R(x,y)\quad\Longleftrightarrow\quad y\in\pi(x).
\]
**Loops are retained:** \(R(x,x)\) holds exactly at an absolute point. Denote this one-sorted structure by \(\mathcal P(\Pi,\pi)\). The language contains only \(R\) and equality, with no named polarity map, no point-line sorts, and no counting quantifiers.

**Theorem.** Two such structures satisfy exactly the same first-order sentences using at most two reusable variable symbols, at *every* quantifier depth, if and only if their orders belong to the same one of these four phases:
\[
\{2\},\qquad \{q:q\ge4\text{ and }q\text{ even}\},\qquad
\{3\},\qquad \{q:q\ge5\text{ and }q\text{ odd}\}.
\]
Only orders at which an eligible projective plane exists occur in the displayed sets. In particular, the classification holds without Desarguesian or field-coordinate assumptions. Each phase is nonempty, witnessed by the Desarguesian planes of orders \(2,4,3,5\), respectively. The family has exactly four unrestricted \(\mathrm{FO}^{2}\)-theories and exactly one \(\mathrm{FO}^{1}\)-theory. Thus two is the minimum variable width that distinguishes any two phases.

## Assumptions and scope

A finite projective plane of order \(q\) has \(q^{2}+q+1\) points and lines, with \(q+1\) on each line and through each point; distinct points determine a line, and distinct lines meet in one point. A polarity \(\pi\) bijectively interchanges points and lines, satisfies \(\pi^{2}=1\), and preserves reversed incidence. A point is *absolute* when it lies on its polar line. Here *orthogonal* means exactly \(q+1\) absolute points; no coordinatization is assumed. Let \(A\) denote this set.

The use of the full incidence relation \(R\), including \(R(x,x)\), is essential. The assertion is not about the customary **simple** polarity graph with loops removed. It is also not an assertion about counting logic, higher-variable logic, or polarities with other numbers of absolute points.

## Proof

**1. Parity and the absolute-point configuration.** If distinct absolute points \(a,b\) satisfied \(b\in\pi(a)\), reciprocity would give \(a\in\pi(b)\). Since both are absolute, the two lines \(\pi(a)\) and \(\pi(b)\) would each be the unique line through \(a,b\), contradicting injectivity of the polarity. Thus the polar line of each \(a\in A\) contains **exactly one** absolute point, namely \(a\).

If a line \(\ell\) is nonabsolute (its pole \(p=\pi(\ell)\) does not lie on \(\ell\)), then \(x\mapsto\ell\cap\pi(x)\) is an involution on the \(q+1\) points of \(\ell\). It is well defined because \(p\in\pi(x)\) for every \(x\in\ell\); it is involutive by polarity reciprocity; and its fixed points are exactly \(A\cap\ell\). Therefore
\[
|A\cap\ell|\equiv q+1\pmod 2.
\]
If \(q\) is odd, each nonabsolute line through an absolute point \(a\) has at least one further absolute point (even intersection). There are \(q\) such lines through \(a\), and exactly \(q\) other absolute points, each on exactly one of them. Hence each contains exactly one further absolute point. Consequently \(A\) is an oval: no three absolute points lie on a line. Its polar lines are its tangents.

If \(q\) is even, each nonabsolute line has an odd, hence positive, number of absolute points; every absolute line already meets \(A\). Thus \(A\), of size \(q+1\), meets every line. Any blocking set of size \(q+1\) is a line: otherwise take a line through two of its points but not all of them, and a point outside the blocking set on that line. The other \(q\) lines through that point require \(q\) distinct blocking points off the selected line, yielding at least \(q+2\) total. Therefore \(A\) is a line \(L\). This line is nonabsolute, since an absolute line contains only one absolute point, whereas \(L\) contains \(q+1\). Write \(c=\pi(L)\); then \(c\notin L\) and \(\pi(c)=L\).

**2. Odd-order geometric types and extension counts.** Assume \(q\ge3\) is odd. A nonabsolute point lies on either zero or two tangents to the oval: at most two because its polar meets the oval in at most two points, and an even number because the \(q+1\) oval points are partitioned among its lines into sets of sizes zero, one, or two. Call the zero-tangent points \(I\) (internal) and two-tangent points \(E\) (external). By reciprocity, the polar of a point in \(I\) is an exterior line, while the polar of a point in \(E\) is a secant line. Counting incidences between the \(q+1\) tangents and their \(q\) nonabsolute points yields
\[
|A|=q+1,\qquad |E|=\frac{q(q+1)}2,\qquad |I|=\frac{q(q-1)}2.
\]
On a secant line, the two tangents at its absolute points meet the line at those points. The other \(q-1\) tangents intersect it at nonabsolute points, each external point being counted twice. Thus a secant contains \((q-1)/2\) external and \((q-1)/2\) internal points. Similarly, an exterior line contains \((q+1)/2\) of each. A tangent contains its single absolute point and \(q\) external points.

The following table gives, for every anchor \(x\) of row type and every target type, the number of **distinct** targets \(y\ne x\) satisfying \(R(x,y)\):

| Anchor | Targets in \(A\) | Targets in \(E\) | Targets in \(I\) |
|---|---:|---:|---:|
| \(A\) | \(0\) | \(q\) | \(0\) |
| \(E\) | \(2\) | \((q-1)/2\) | \((q-1)/2\) |
| \(I\) | \(0\) | \((q+1)/2\) | \((q+1)/2\) |

Distinct nonneighbor counts equal the target-class size, minus the corresponding displayed entry, and minus one when the anchor itself belongs to that target class. All zero/nonzero patterns are independent of odd \(q\ge3\), **except** that the number of distinct nonneighbors of an internal point that are also internal is
\[
\frac{(q-3)(q+1)}2,
\]
which vanishes exactly when \(q=3\).

**3. Even-order geometric types and extension counts.** Assume \(q\ge2\) is even. The absolute points form the line \(A=L\). Let \(C=\{c\}\) consist of its pole; let \(N\) be all remaining points. Their sizes are
\[
|A|=q+1,\qquad |C|=1,\qquad |N|=q^{2}-1.
\]
The polar line of an absolute point contains itself, \(c\), and \(q-1\) members of \(N\). The polar line of \(c\) is \(L\), containing exactly all absolute points. The polar line of any member of \(N\) meets \(L\) in exactly one absolute point, misses \(c\), and contains \(q\) members of \(N\). Therefore the distinct-neighbor counts are

| Anchor | Targets in \(A\) | Targets in \(C\) | Targets in \(N\) |
|---|---:|---:|---:|
| \(A\) | \(0\) | \(1\) | \(q-1\) |
| \(C\) | \(q+1\) | \(0\) | \(0\) |
| \(N\) | \(1\) | \(0\) | \(q\) |

The only zero/nonzero pattern that varies among even orders is the number of distinct nonneighbors inside \(N\), namely
\[
(q^{2}-1)-1-q=(q-2)(q+1),
\]
which vanishes exactly when \(q=2\).

**4. Two-variable definability and permanent pebble games.** The geometric types above are defined with only two variable symbols. Let \(A(x)\) abbreviate \(R(x,x)\). In odd order, let
\[
I(x):=\neg A(x)\land\forall y\bigl(A(y)\rightarrow\neg R(x,y)\bigr),\quad E(x):=\neg A(x)\land\neg I(x).
\]
In even order, let
\[
C(x):=\neg A(x)\land\forall y\bigl(R(x,y)\rightarrow A(y)\bigr),\quad N(x):=\neg A(x)\land\neg C(x).
\]
The formula \(\exists x\,C(x)\) distinguishes even from odd order: in odd order, every nonabsolute point has at least one nonabsolute polar neighbor, whereas the even-order pole \(c\) has none. (The abbreviation \(C(x)\) is interpreted by its defining formula in either structure.)

Within the even-order family, the two-variable sentence
\[
\exists x\bigl(N(x)\land\exists y\bigl(N(y)\land x\ne y\land\neg R(x,y)\bigr)\bigr)
\]
is true exactly for \(q\ge4\). Within the odd-order family, the analogous sentence with \(I\) in place of \(N\) is true exactly for \(q\ge5\). Bound variables in the abbreviations are alpha-renamed as necessary, so only the two symbols \(x,y\) are used throughout.

Conversely, consider two structures from the same phase. In the *two-pebble* game Duplicator preserves the unary types just defined, equality of pebbled points, and the truth of \(R\) between the pebbles. A move onto the already-pebbled point is matched by equality. For a move to a distinct point, the target type and the choice of adjacency/nonadjacency to the stationary pebble determine the required response. The two tables and their complementary counts prove that every such response exists in both structures: the sets of positive target counts agree exactly within each phase. This strategy survives every number of rounds and is symmetric between the structures. Hence it proves unrestricted \(\mathrm{FO}^{2}\)-equivalence. Finally, the only one-variable atomic information is equality and \(R(x,x)\); every eligible structure has both absolute and nonabsolute points, so all share the same \(\mathrm{FO}^{1}\)-theory. The classification follows.

## Verification

The package contains two runnable standard-library Python scripts. Run `python verify_geometry.py` to enumerate canonical projective points for prime fields and several extension fields, check every geometric type count and every row of the two neighbor tables **for every point**, and check the unique common polar neighbor of each pair of distinct points. Run `python verify_fo2.py` in the same directory to compute non-counting two-pebble logical-type refinement from adjacency and loops alone (without the geometric types), to a fixed point, and compare all ordered instance pairs. Recorded outputs are `geometry_output.txt` and `fo2_output.txt`; these files were produced by executing the scripts.

The tested field orders are \(2,3,4,5,7,8,9,11,13,16,25\). These finite checks include characteristic two and odd characteristic, prime and nonprime field orders, and the sharp exceptional cases. They do **not** test arbitrary non-Desarguesian planes, and do not substitute for the all-planes proof in the preceding section.

## Relationship to prior work

The orthogonal polarity graph of a finite projective plane is classical; the underlying construction goes back to Brown and to Erdős, Rényi, and Sós (1966). Tait and Timmons, *Orthogonal polarity graphs and Sidon sets* (arXiv:1403.4489, posted 2014-03-18), study induced subgraphs, saturation and extremal graph constructions. Their later *Independent sets in polarity graphs* (arXiv:1601.05058, posted 2016-01-19), explicitly defines the loop-added orthogonal polarity graph and studies its spectral, independence and coloring properties, including non-Desarguesian planes. Neither inspected paper gives a complete non-counting two-variable logical equivalence classification or the four small-order/parity phases. Standard two-pebble games provide the logical method, but the exact geometric extension tables are the additional substantive input here. The priority comparison is qualified; a stronger result under other terminology might imply this classification.

## Limitations

This theorem applies only when a finite projective plane admits a polarity with exactly \(q+1\) absolute points. It does not assert existence of such a polarity for every numerical order. Retaining loops is part of the signature; removing loops erases the unary absolute-point information on which the phase distinction depends. It does not classify other polarities, arbitrary finite point-line incidence structures, counting logic, or higher variable widths. The structural parity argument and extension counts are proved for all eligible planes, but the computational reproduction covers only listed coordinatized examples. No independent mathematical audit or exhaustive historical priority check has been performed.

## References

1. P. Erdős, A. Rényi, and V. T. Sós, *On a problem of graph theory*, Studia Sci. Math. Hungar. **1** (1966), 215–235. Bibliographic record: https://real.mtak.hu/110437/ .
2. M. Tait and C. Timmons, *Orthogonal polarity graphs and Sidon sets*, arXiv:1403.4489, initial public posting 2014-03-18; full text: https://arxiv.org/html/1403.4489v3 .
3. M. Tait and C. Timmons, *Independent sets in polarity graphs*, arXiv:1601.05058, initial public posting 2016-01-19; full text: https://arxiv.org/html/1601.05058v1 .
4. P. G. Kolaitis and J. A. Väänänen, *Generalized quantifiers and pebble games on finite structures*, LICS (1992), 348–359; bibliographic record: https://www.lfcs.inf.ed.ac.uk/events/lics/1992/KolaitisVaananen-Generalizedquantifi.html .
