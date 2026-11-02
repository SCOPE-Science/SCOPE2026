# Four unrestricted four-variable theories of projective collinearity geometries

## Finding

Let \(\mathscr P\) be the family consisting of all finite projective spaces \(\mathrm{PG}(d,q)\), where \(d\geq1\) and \(q\geq2\) is a prime power, together with all finite projective planes (including non-Desarguesian planes) of order \(q\geq2\). For a general plane take its geometric dimension to be two. In every member, retain **only the points**, equality, and the inclusive ternary relation \(C(x,y,z)\) meaning that the three points are collinear. Repeated arguments always satisfy \(C\). There are no named lines, parameters, coordinates, functions, counting quantifiers, or constants.

**Theorem.** For \(\mathcal P,\mathcal Q\in\mathscr P\), their point-only collinearity structures satisfy exactly the same unrestricted-depth first-order sentences using at most four variable symbols if and only if the following two bits agree: (a) whether the projective dimension is one or at least two, and (b) whether the order is two or at least three. Thus there are **exactly four** complete noncounting \(\mathrm{FO}^{4}\) theories in this family, with respective smallest members

| Projective dimension | Order | Smallest representative | Points |
| --- | --- | --- | ---: |
| One | Two | \(\mathrm{PG}(1,2)\) | 3 |
| One | At least three | \(\mathrm{PG}(1,3)\) | 4 |
| At least two | Two | \(\mathrm{PG}(2,2)\) | 7 |
| At least two | At least three | \(\mathrm{PG}(2,3)\) | 13 |

The sharp uniform smallest-representative bound is **13 points**. In the same family, \(\mathrm{FO}^{2}\) has exactly one complete theory, and \(\mathrm{FO}^{3}\) has exactly two, distinguished only by projective dimension one versus at least two. Consequently the number of unrestricted-depth theories at variable widths two, three, and four is respectively \(1,2,4\).

The width-four dimension collapse is sharp: for any two projective spaces of dimensions two and at least three, a five-variable sentence asserting the existence of two skew lines distinguishes them (in the point-only collinearity language). In particular, even finite projective planes of different orders and arbitrary non-Desarguesian type lie in one \(\mathrm{FO}^{4}\) class whenever both orders are at least three; higher-dimensional spaces join the same class.

## Assumptions and scope

Every finite projective plane has an integer order \(q\ge2\), exactly \(q+1\) points on each line, \(q^2+q+1\) points in total, a unique line through each pair of distinct points, and a unique intersection of distinct lines. These facts hold without Desarguesian assumptions. A projective space of dimension at least two over \(\mathbb F_q\) contains a copy of \(\mathrm{PG}(2,q)\) on the span of any noncollinear triple and has \(q+1\) points on each line. A projective line has exactly \(q+1\) points, all collinear.

The signatures and formulae are finite-variable **relational** first-order logic with equality; quantifier depth is unrestricted. Inclusive collinearity makes \(C(x,x,y)\) always true, so all repeated-argument cases must be preserved as well as distinct triples. Statements about point-line incidence languages, finite quantifier ranks, or signatures naming coordinates are not equivalent assertions.

## Proof

**1. Three stationary points and one movable point.** For any three currently stationary pebble positions, equality and the truth values of \(C\) on all triples of occupied positions are determined by the equalities among the stationary points and, when they are distinct, whether they are collinear. We enumerate *all* possible fresh-point atomic extension patterns.

If there are zero or one distinct stationary points, a new point distinct from the stationary set always exists. If there are exactly two distinct stationary points \(a,b\), the line \(ab\) contains exactly \(q-1\ge1\) further points. In dimension at least two there are also points outside \(ab\), since already a projective plane has \(q^2\) points off each line. In dimension one every point is on the line.

Suppose there are three distinct stationary points \(a,b,c\) on a line \(\ell\). The number of further points on \(\ell\) is \(q-2\); this is zero exactly when \(q=2\), and positive exactly when \(q\ge3\). In dimension at least two there are also points off \(\ell\). Any fresh point on \(\ell\) is collinear with every pair from \(\{a,b,c\}\), while any off-line point is collinear with none of those pairs. There is no other possible pattern.

Now suppose \(a,b,c\) are noncollinear. Their three joining lines are pairwise distinct and meet only at \(a,b,c\). Each side line contains \(q-1\ge1\) new points. Inside the projective plane they span, the number of points on none of the three sides is
\[
(q^2+q+1)-\bigl(3+3(q-1)\bigr)=(q-1)^2\ge1.
\]
For a fresh point, the only possible collinearity patterns with the three pairs are: on exactly one specified side, or on none. All four patterns exist in every ambient dimension at least two and for every \(q\ge2\).

The full extension support, including responses equal to an already selected point, therefore depends **only** on whether the dimension is one or at least two and whether \(q=2\) or \(q\ge3\). No numerical incidence count is used as a logical invariant; only whether the relevant number is zero matters.

**2. Unbounded four-pebble back-and-forth.** Between two structures in the same class, maintain a partial isomorphism on at most four labelled pebble pairs. When Spoiler moves any one pebble, at most three remain. Match its new position using the preceding extension-support table. Equality with a stationary point is copied directly; otherwise choose a fresh point with precisely the same collinearity pattern relative to each pair of stationary points. By the table such a point exists in the other structure. All atomic relations on the four occupied positions then agree. This strategy works for arbitrarily many moves. The unrestricted-depth \(\mathrm{FO}^{4}\) equivalence follows from the standard pebble-game characterization.

**3. Separation and minimal representatives.** The three-variable sentence saying that some triple of distinct points is noncollinear holds exactly in dimension at least two. The four-variable sentence saying that some four distinct points are collinear holds exactly for order at least three. These two tests realize every combination of the two bits and separate all four classes. The least number of points in each class is respectively \(3,4,7,13\), as exhibited above: all other members either have a larger order or a larger dimension. The four-class classification and the sharp 13-point uniform bound follow.

With only two variable symbols, every atomic instance of \(C\) necessarily repeats an argument and is true; all domains have at least three points, hence every member has the same complete \(\mathrm{FO}^{2}\) theory. With three variables, an exact back-and-forth on at most two stationary points uses the two-point extension cases above, which depend only on whether a point can be noncollinear with the two selected distinct points. Thus all projective lines form one \(\mathrm{FO}^{3}\) class and all members of dimension at least two form another. The displayed noncollinearity sentence separates the two.

**4. Sharpness of the dimension blindness.** With five variable symbols one can assert that four pairwise distinct points \(a,b,c,d\) determine two disjoint lines by requiring that no point \(z\) lies on both \(ab\) and \(cd\):
\[
\exists a\,\exists b\,\exists c\,\exists d\,\bigl(
 a\ne b\wedge a\ne c\wedge a\ne d\wedge
 b\ne c\wedge b\ne d\wedge c\ne d
 \wedge\forall z\,\neg(C(a,b,z)\wedge C(c,d,z))\bigr).
\]
Every two lines in a projective plane meet, so the sentence fails in dimension two. Projective spaces of dimension at least three contain skew lines, so it holds there. Hence four is exactly the largest variable width at which the proposed cross-dimensional equivalence persists.

## Verification

The standalone program `verify.py` constructs point-only collinearity structures by exact finite-field arithmetic, including \(\mathbb F_4\) as a quadratic extension. For every ordered triple of stationary elements it independently enumerates all patterns of equality and collinearity with a fourth point and verifies that the support is constant within each atomic triple type. It compares these complete supports across the four claimed classes.

Executed instances were projective dimensions one, two and three with orders \(2,3,4,5\) in the combinations recorded by `verify_output.txt`. In total, 109,399 ordered triples were examined; all classwise templates agreed, and the four templates were distinct. The finite enumeration corroborates the extension table; it does not prove the theorem for arbitrary orders, non-Desarguesian planes, or unbounded dimensions. Those cases are covered by the preceding axiomatic proof.

Reproduce with `python3 verify.py` from the directory containing that file. Python's standard library suffices.

## Relationship to prior work

Grohe and Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990 (initially public 9 April 2012), §2, give the general characterization of noncounting finite-variable equivalence by pebble games. Their results do not furnish the projective-collinearity extension support or the four-class classification by themselves. Bartoli, Davydov, Giulietti, Marcugini and Pambianco, *On upper bounds on the smallest size of a saturating set in a projective plane*, arXiv:1505.01426 (initially public 6 May 2015), explicitly treat projective planes without Desarguesian assumptions and higher-dimensional projective spaces, but study saturating sets and covering codes, not finite-variable logical equivalence.

Known bounded-quantifier-rank classifications in two-sorted incidence languages do not, without an additional interpretation preserving variable width and arbitrary quantifier depth, establish equivalence in this ternary point-only language. The present result concerns unbounded quantifier depth but only four reusable variable symbols.

## Limitations

The claim is restricted to the specified family and the pure inclusive ternary collinearity signature. It excludes arbitrary partial linear spaces, affine geometries, named lines and hyperplanes, coordinates, function symbols, counting quantifiers, and first-order logic with five or more variables. The five-variable skew-line observation is a boundary result, not a complete \(\mathrm{FO}^{5}\) classification. The algebraic finite checks are not an exhaustive census of non-Desarguesian planes. The literature comparison supports qualified originality rather than an exhaustive priority guarantee. Independent mathematical auditing has not been performed.

## References

1. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, arXiv:1204.1990, first public 2012-04-09, especially §2. https://arxiv.org/html/1204.1990v3
2. D. Bartoli, A. A. Davydov, M. Giulietti, S. Marcugini, F. Pambianco, *On upper bounds on the smallest size of a saturating set in a projective plane*, arXiv:1505.01426, first public 2015-05-06, §§1–2 and 5. https://arxiv.org/html/1505.01426v3
