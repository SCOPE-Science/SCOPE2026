# Three four-round theories of finite affine planes

## Finding

Let \(\mathcal A\) and \(\mathcal B\) be **arbitrary finite affine planes** of respective orders \(q,r\ge2\), not assumed Desarguesian. Regard each as a first-order structure with one domain comprising points and lines, unary predicates \(P,L\) naming the disjoint sorts, equality, and a binary relation \(I(p,\ell)\) for point-on-line incidence. Parallelism is **not** a relation symbol. Then

\[
\mathcal A\equiv_4\mathcal B
\quad\Longleftrightarrow\quad
\min(q,4)=\min(r,4).
\]

Thus precisely three quantifier-rank-four theories occur, represented by affine planes of orders \(2,3,4\), with respectively \(10,21,36\) total elements. Every finite affine plane is equivalent through four quantifier rounds to one of these three representatives, and the uniform \(36\)-element representative bound is sharp within the family.

## Assumptions and scope

An affine plane of order \(q\) has \(q^2\) points, \(q(q+1)\) lines, \(q\) points per line, \(q+1\) lines through each point, exactly one line through any two distinct points, and one line through a given point parallel to a given line. Distinct lines meet in at most one point; their parallel classes have \(q\) lines. The theorem applies to every finite structure satisfying the affine-plane incidence axioms, including non-Desarguesian planes. No affine-coordinate system is assumed in the proof. Quantifier rank means maximal nested first-order quantifier depth, counting both existential and universal quantifiers.

The symbol \(\equiv_4\) means agreement on **all** first-order sentences of quantifier rank at most four in exactly the stated named-sort incidence signature. In particular, this is not a statement about modal formulas with valuations or about a language additionally naming parallelism.

## Proof

**1. Sharp distinctions.** For each integer \(k\ge1\), let \(\Phi_k\) assert that \(k\) pairwise distinct lines cover every point:

\[
\Phi_k:=\exists\ell_1\cdots\exists\ell_k\,\Bigl(
\bigwedge_i L(\ell_i)\land\bigwedge_{i<j}\ell_i\ne\ell_j
\land\forall p\,[P(p)\Rightarrow\bigvee_i I(p,\ell_i)]\Bigr).
\]

This formula has quantifier rank \(k+1\). In a plane of order \(q\), fewer than \(q\) lines cover at most \(kq<q^2\) points. Conversely, the \(q\) lines in a parallel class partition the plane; hence \(\Phi_k\) holds precisely when \(q\le k\), provided \(k\) distinct lines exist (certainly so for \(k=2,3\) and every \(q\ge2\)). In particular, \(\Phi_2\), of rank three, separates order two from every larger order; \(\Phi_3\), of rank four, separates order three from orders at least four. All three claimed classes therefore really are different.

**2. The enhanced configuration invariant.** For ordered selected tuples of at most three entries, record (i) the equality pattern, sorts and all point-line incidences, (ii) whether each pair of distinct selected lines is parallel, (iii) whether three distinct selected points are collinear, and (iv) whether three distinct selected lines are concurrent. Repeated entries are reduced to the distinct-entry case. These are *strategy records*, not additional language symbols. They include the atomic diagram and can be preserved strategically even though not all recorded properties are atomic.

We show that for every pair of affine planes of orders at least four, the following three statements hold uniformly.

(A) Every one-entry record may be matched, and every extension of a matching one-entry record to two entries has a matching extension with the same enhanced two-entry record.

(B) Every extension of a matching enhanced two-entry record to a three-entry record has a matching extension with exactly the same enhanced three-entry record.

(C) Every possible atomic diagram obtained by adding a fourth entry to an enhanced three-entry record occurs over every realization of that record in either plane.

To verify (A) and (B), consider the sort compositions of the previously selected *distinct* entries. For two points, a fresh point may lie on their joining line (there are \(q-2\ge2\) choices) or off it; a fresh line may contain both, exactly one, or neither (lines through neither exist because \(q(q+1)-2(q+1)+1=(q-2)(q+1)+1>0\)). For a point and line, fresh points on and off the line exist, and fresh lines through or avoiding the point may be chosen either parallel or nonparallel to the old line wherever geometrically compatible: when the point is off the old line, the unique through-point parallel and the \(q-2\) additional parallel lines provide the only small exceptional categories, both nonempty for \(q\ge4\). For two parallel lines, a third line may be parallel to both (\(q-2\ge2\) remaining lines) or transverse to both, while points on neither number \(q^2-2q>0\). For two intersecting lines, a third line can pass through their intersection (\(q-1\) choices), be parallel to exactly one (\(q-1\) choices for each), or intersect both at distinct points (\((q-1)^2\) choices). Their point extensions may lie at the intersection, only on one line, or on neither (\((q-1)^2>0\) possibilities for the latter). These descriptions exhaust the possible three-entry enhanced records. All required categories exist for each \(q\ge4\). With fewer than two distinct entries the same assertions are immediate from \(q\ge4\).

For (C), only the distribution of a new element relative to three previously selected distinct entries matters, because the game ends immediately afterward. There are four sort compositions.

* **Three points.** A fourth point has no incidence atoms with them, and an unused point exists. A new line may pass through none, one, two, or all of the three points exactly when allowed by their collinearity. If the points are collinear, their joining line contains all three and no line contains exactly two. If noncollinear, each pair has a joining line containing exactly that pair and no line contains all three. Each individual point has at least \(q-1\ge3\) other lines through it avoiding the other two. A line avoiding all three exists because at most \(3(q+1)\) of \(q(q+1)\) lines pass through any of them and \((q-3)(q+1)>0\).
* **Three lines.** A fourth line can be chosen distinct from all three, with no incidence atoms to them. A new point has any incidence subset of the three lines compatible with their parallel/concurrent records. A singleton-incidence witness exists on each line, since at most two of its \(q\) points lie on the other lines (\(q-2\ge2\)). A point incident with neither of the three exists since their union has size at most \(3q<q^2\). Pair-only incidences occur exactly for intersecting pairs whose intersection is not on the third line; a triple intersection occurs exactly when the three lines are concurrent. Thus the possibilities are record-determined.
* **Two points and one line.** A fourth point can be selected fresh on or off the line, with at least \(q-2\ge2\) and \(q^2-q-2>0\) available points respectively. A fresh line may contain both points only when their unique joining line is not the selected line, and may contain either one or neither otherwise; all applicable categories have multiple witnesses when \(q\ge4\). Existing entries can of course be copied.
* **Two lines and one point.** A fresh point can have any membership subset of the two lines consistent with their parallel/intersection flag and whether their intersection is already the selected point. Single-line witnesses exist (at least \(q-2\) after excluding selected entries), and a point on neither exists because at least \(q^2-2q-1>0\) lie outside both lines and the selected point. A fresh line through the selected point exists apart from the two old lines (at least \(q-1\ge3\) choices), as does a line avoiding that point. No line-line incidence atom is present.

Every remaining case with repeated entries is obtained from one of the corresponding smaller-distinct-entry cases, using the same equality records. This establishes (C).

**3. Four-round game.** In a four-round Ehrenfeucht–Fraïssé game, Duplicator matches the first selection by sort, uses (A) for the second, (B) for the third, and (C) for the fourth. The four selected elements then have identical equality, sort and incidence atoms. This is a winning strategy from either starting plane; consequently all finite affine planes of order at least four satisfy the same rank-four sentences. Combined with the separating sentences in step 1, it proves the displayed classification and the sharp representative bound. \(\square\)

## Verification

The universal equivalence is a mathematical proof from the incidence axioms; computations below test boundary behavior and independently reconstruct all four-round types in small coordinate planes. No finite pattern is extrapolated to obtain the infinite result.

`affine_types.cpp` generates the plane over the prime fields of orders \(2,3,5,7\) and over \(\mathbb F_4\), using \(u^2+u+1\). It builds exact atomic diagrams of four selected elements and recursively interns every set of one-point-extension types, including repeated selections. Running `reproduce.sh` gives distinct complete four-round types for orders \(2,3\), and a single shared type for \(4,5,7\). `affine_independent.py` independently computes immutable sets of recursively nested types over orders \(2,3,4\), reproducing the three distinct theories. `affine_atlas.py` separately computes enhanced configurations and allowed extensions, finding exactly \(1,2,9,64\) record types at lengths zero through three in both affine planes of orders four and five, with identical extension sets. The outputs are embedded as `computed_types.txt`, `independent_output.txt` and `atlas_output.txt`. These are reproducible checks, not substitutes for the incidence-axiom argument.

## Relationship to prior work

Hodkinson and Hussain, *The modal logic of affine planes is not finitely axiomatisable* (2008), consider a richer two-sorted **modal** language that includes parallelism and valuation-dependent formulas, proving a non-finite-axiomatizability theorem. Their section 2.3 provides the affine-plane incidence axioms; theorem 3.12 addresses modal axiom systems. The present fixed-depth classical first-order incidence classification is not the statement or consequence of that theorem.

Durt, Englert, Bengtsson and Życzkowski, *On mutually unbiased bases* (arXiv:1004.3348, first posted April 20, 2010), discuss the standard prime-power affine planes and their relation to other structures; they do not address bounded-rank first-order equivalence. Broader finite-model-theory Ehrenfeucht–Fraïssé principles justify the game interpretation, but supply no family-specific sharp threshold without the geometric case analysis. Literature searches did not locate the three-class statement, although absence from search indexes cannot establish historical uniqueness.

## Limitations

Only quantifier rank four in the named-point/line-sort **incidence-only** first-order language is classified. Adding a named parallelism predicate, arithmetic coordinates, constants or extra relations may change the rank-four theory. No classification for higher ranks, higher-dimensional affine spaces, or all finite linear spaces is claimed. Computations cover Desarguesian planes of orders \(2,3,4,5,7\); the universal argument covers abstract finite affine planes irrespective of coordinatizability. Independent mathematical audit has not been performed. The historical-priority search was extensive but not exhaustive; a 2008 published paper has no day-verified first-public timestamp, while the cited arXiv source has the verified public date 2010-04-20, which is used only as a documented dating anchor, not a claim about first-ever publication of the theorem.

## References

1. I. Hodkinson and A. Hussain, *The modal logic of affine planes is not finitely axiomatisable*, Journal of Symbolic Logic **73** (2008), 940–952, DOI 10.2178/jsl/1230396757; author-hosted full text: https://www.doc.ic.ac.uk/~imh/papers/affine.pdf.
2. T. Durt, B.-G. Englert, I. Bengtsson and K. Życzkowski, *On mutually unbiased bases*, arXiv:1004.3348, first version publicly posted 2010-04-20, https://arxiv.org/abs/1004.3348.
3. P. Balbiani and V. Goranko, *Modal logics for parallelism, orthogonality, and affine geometries*, Journal of Applied Non-Classical Logics **12** (2002), 365–398 (related modal-language background, referenced by [1]; complete text not inspected).
