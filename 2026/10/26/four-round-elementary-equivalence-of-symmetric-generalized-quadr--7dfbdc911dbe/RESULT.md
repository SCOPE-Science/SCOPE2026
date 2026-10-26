# Four-round elementary equivalence of symmetric generalized-quadrangle incidence graphs

## Finding
Let \(\mathcal Q\) and \(\mathcal Q'\) be arbitrary finite generalized quadrangles of respective orders \((q,q)\) and \((q',q')\), where \(q,q'\ge 2\). Their *uncoloured*, simple, point–line incidence graphs satisfy
\[
L(\mathcal Q)\equiv_4 L(\mathcal Q').
\]
Equivalently, every first-order graph sentence of quantifier rank at most four has the same truth value on both graphs, regardless of parameters or isomorphism type. The uniform bound four is sharp across this family: the incidence graphs of the symplectic quadrangles \(W(3,2)\) and \(W(3,3)\) are distinguished at rank five, but not at rank four.

## Assumptions and scope
A finite generalized quadrangle of order \((q,q)\) has a finite point set and line set, each line incident with \(q+1\) points, each point on \(q+1\) lines, at most one common line through two points, and, for every nonincident point–line pair, a unique shortest incidence path of length three. We assume \(q\ge2\); existence of a quadrangle is part of the quantified hypothesis, and no existence for arbitrary integers is asserted. Its Levi graph \(G\) is simple, bipartite and \((q+1)\)-regular with diameter four and girth eight. The language has only adjacency and equality: neither point/line sorts nor a distinguished vertex are named. Write \(G\equiv_r H\) for agreement on all first-order sentences of rank at most \(r\).

For vertices \(x,y\), write \(d(x,y)\in\{0,1,2,3,4\}\) for their graph distance, and \(\delta(x,y)=\min(d(x,y),3)\). The critical thresholds are three neighbours per vertex, pair-distance supports through radius four, and four quantifier rounds.

## Proof
**Step 1: uniform intersection algebra.** The incidence axioms give intersection array
\[
\{q+1,q,q,q;\ 1,1,1,q+1\}.
\]
Indeed, a vertex has \(q+1\) neighbours; at graph distances one, two, and three each vertex has exactly one neighbour toward the root and exactly \(q\) neighbours away; vertices at distance four have \(q+1\) neighbours toward the root. Uniqueness of paths of length at most three follows from girth eight, and diameter four follows from the generalized-quadrangle axiom. In the distance-matrix algebra let \(D_j\) be the distance-\(j\) matrix and let \(A=D_1\). Then
\[
A D_1=(q+1)D_0+D_2,\quad
A D_2=qD_1+D_3,\quad
A D_3=qD_2+(q+1)D_4,\quad
A D_4=qD_3.
\]
The regularity and these recurrences imply that the coefficient \(p_{ab}^{d}\) of \(D_d\) in \(D_aD_b\) is exactly the number of vertices \(z\) with \(d(x,z)=a\) and \(d(y,z)=b\) for any pair with \(d(x,y)=d\). In the ordered basis \(D_0,\ldots,D_4\), multiplication by \(A\) is the explicit matrix
\[
M=\begin{pmatrix}
0&q+1&0&0&0\\
1&0&q&0&0\\
0&1&0&q&0\\
0&0&1&0&q\\
0&0&0&q+1&0
\end{pmatrix}.
\]
Consequently the multiplication matrices of \(D_0,\ldots,D_4\) are, respectively,
\[
I,\ M,\ M^2-(q+1)I,\ M^3-(2q+1)M,\
\frac{M^4-(3q+1)M^2+q(q+1)I}{q+1}.
\]
For each fixed distance \(d\), the entries \(p_{ab}^{d}\) are the \((d,b)\) entries of the \(a\)-th matrix. Every nonzero coefficient is a polynomial in \(q\) strictly positive for every \(q\ge2\): all expanded coefficients in \(h=q-2\) are nonnegative with positive constant term. Exact symbolic factorization and coefficient verification are in `check_symbolic.py` and `symbolic_output.txt`. Hence the *support* of every distance-intersection number is independent of \(q\ge2\).

After truncation of each of the two distances to three, these supports are as follows. The displayed ordered pairs are \((\delta(x,z),\delta(y,z))\), with \(d(x,y)\) equal to the row label:

| \(d\) | Possible pairs |
|---|---|
| 0 | (0,0), (1,1), (2,2), (3,3) |
| 1 | (0,1), (1,0), (1,2), (2,1), (2,3), (3,2), (3,3) |
| 2 | (0,2), (1,1), (1,3), (2,0), (2,2), (2,3), (3,1), (3,2), (3,3) |
| 3 | (0,3), (1,2), (1,3), (2,1), (2,3), (3,0), (3,1), (3,2), (3,3) |
| 4 | (0,3), (1,3), (2,2), (2,3), (3,0), (3,1), (3,2), (3,3) |

**Step 2: one-step types of triples.** For any ordered triple \((x,y,z)\), its full rank-one type in the graph language is determined *exactly* by
\[
(\delta(x,y),\delta(x,z),\delta(y,z)).
\]
To verify the forward determination, its atomic diagram is plainly determined by this triple. For a fourth vertex \(w\) distinct from the named vertices, existence of each of the eight possible adjacency masks is determined by the three clipped distances. The mask with no adjacency is always realizable: at least two of the three named vertices lie in one bipartition class, and that class contains \((q+1)(q^2+1)>q+4\) vertices; exclude the named vertices and the at most \(q+1\) neighbours of the possible named vertex in the opposite class. Each mask with adjacency to precisely one *distinct* named vertex is realizable, since it has \(q+1\ge3\) neighbours and at most two can be excluded by the other named vertices or their unique common neighbours. For a mask adjacent to exactly two named vertices, girth eight ensures that the vertices must be at distance two and have one unique common neighbour; this neighbour is unusable precisely if it is the third named vertex or is also adjacent to the third. Those conditions are read off from the three clipped distances: they occur, respectively, when the other two distances are both one or both two. Finally a vertex adjacent to all three distinct named vertices exists exactly when their pairwise distances are all two; three different pairwise common neighbours would otherwise form a forbidden six-cycle. If names repeat, collapse the equality classes and apply the analogous one- or two-name cases. Repeated choices of \(w\) among the named vertices have atomic diagrams determined by the original triple. This establishes sufficiency for every rank-one formula by the elementary one-step type recursion.

For necessity, equality and adjacency are atomic; distance two between any two named variables is witnessed either by an already named common neighbour or by one existentially quantified common neighbour. Thus the rank-one type detects, for each pair, whether its distance is zero, one, two, or at least three. In particular, there are 30 possible rank-one ordered triple types, all determined by these clipped distances.

**Step 3: two-step pair types.** By Step 2 and the one-step recursion, the rank-two type of an ordered pair \((x,y)\) is determined by its atomic diagram and the set of truncated distance triples of extensions \((x,y,z)\). Step 1 shows this set depends only on \(d(x,y)\), independent of \(q\). Conversely, all five distances give *different* types. Distances zero, one and two are recognizable from equality, adjacency, and the existence of a common neighbour; distances three and four differ because a pair at distance three has a vertex at truncated distances \((1,2)\), whereas a pair at distance four does not. Hence there are precisely five rank-two ordered pair types in every graph considered, indexed by distances zero through four, with the same meaning in all graphs.

**Step 4: three-step vertex types and four-step sentences.** From each vertex, all five distances zero through four occur: the root-distance layers have respective sizes
\[
1,\quad q+1,\quad q(q+1),\quad q^2(q+1),\quad q^3,
\]
all positive. Thus every vertex, in every graph under discussion, has the same rank-three one-variable type: its one-point extensions realize exactly the five rank-two pair types. Consequently every graph realizes the same singleton set of rank-three vertex types. The back-and-forth characterization of rank-four sentences proves the asserted equivalence.

**Step 5: sharpness.** For \(q=2\) and \(q=3\) the finite symplectic generalized quadrangles \(W(3,2)\) and \(W(3,3)\) exist. Their incidence graphs are respectively three- and four-regular. The rank-five sentence expressing the existence of one vertex adjacent to four mutually distinct vertices separates them. By Steps 1–4, no rank-four sentence does; hence rank five is the least distinguishing rank for this pair.

## Verification
Run `python verify.py` in the package directory; it uses only the standard library, constructs the two finite symplectic quadrangles directly over prime fields two and three, checks graph distances, all rank-one triple profiles, the five rank-two pair profiles and the common rank-four sentence profile, and independently reproduces the five distance-support rows by finite distance-algebra arithmetic. Its actual output is in `verification_output.txt`.

Run `python check_symbolic.py` with SymPy installed for the exact algebraic coefficient certificate. It reconstructs all 125 intersection-number polynomials from the displayed recurrence and proves the parameter-uniform positivity of every nonzero entry by expansion in \(q-2\). Its actual output is in `symbolic_output.txt`. This is a finite symbolic verification of universal polynomial identities, not an extrapolation from the two incidence graphs. The geometric one-step lemma is proved above, rather than treated as a computational guess.

## Relationship to prior work
Tits' generalized polygons and the standard generalized-quadrangle incidence axioms explain the structural setting; distance-regular graph intersection algebra is classical (see Vanhove's Chapter 2 and the standard monograph of Payne–Thas). Libkin's Chapter 3 supplies the general Ehrenfeucht–Fraïssé/back-and-forth equivalence, not this parameter-independent family-specific profile. Previous treatments of projective-plane Levi graphs concern generalized triangles (diameter three, girth six), not generalized quadrangles (diameter four, girth eight); their conclusions do not imply this one. Studies of Vietoris–Rips complexes of generalized quadrangle incidence graphs concern homotopy groups and cannot imply a first-order rank-four equivalence. The present contribution is the explicit rank-one/truncated-distance reduction, the five universal pair profiles, and the sharp logical depth boundary.

## Limitations
The theorem is proved for *symmetric* orders \((q,q)\) with \(q\ge2\), not for general orders \((s,t)\) with \(s\ne t\); it makes no claim about coloured incidence languages, first-order rank five beyond the exhibited separating pair, or arbitrary finite regular bipartite graphs. The polynomial positivity certificate uses classical distance-regular intersection identities; verification of the general geometric extension argument is mathematical, not an independent human audit. An equivalent statement in unindexed historical sources or folklore cannot be excluded. Full text of the Payne–Thas monograph was not retrieved in this investigation.

## References
1. S. E. Payne and J. A. Thas, *Finite Generalized Quadrangles*, first edition (1984), second edition (2009), https://ems.press/books/elm/67 .
2. F. Vanhove, *Incidence geometry from an algebraic graph theory point of view*, PhD thesis, Ghent University (2011), Chapter 2 and Chapter 6, https://biblio.ugent.be/publication/1209078 .
3. L. Libkin, *Elements of Finite Model Theory*, Springer (2004), Chapter 3, Theorems 3.9 and 3.18, https://homepages.inf.ed.ac.uk/libkin/fmt/fmt.pdf .
4. J. Tits, *Sur la trialité et certains groupes qui s'en déduisent*, Publications Mathématiques de l'IHÉS **2** (1959), 13–60.
