# Complete first disparity layer for the minimal covering and iterated uncovered sets
## Finding
For a finite tournament \(T\), let \(UC(T)\) denote the uncovered set and let
\[
UC^{\infty}(T)
\]
be the fixed point obtained by repeatedly applying the uncovered-set operator to the induced subtournament on the current choice set.

The **minimal covering set** \(MC(T)\) is the unique inclusion-minimal covering set. Equivalently, it is the unique minimal subset that is externally stable with respect to covering; in tournaments this set is automatically internally stable.

It is known that
\[
MC(T)\subseteq UC^{\infty}(T)
\]
for every tournament, and prior exhaustive work establishes that the disparity index is \(6\).

The complete first disparity layer is
\[
\#\{T:|T|=6,\ MC(T)\ne UC^{\infty}(T)\}=240.
\]
Since there are
\[
2^{\binom 62}=2^{15}=32768
\]
labeled six-alternative tournaments, the exact incidence is
\[
\frac{240}{32768}=\frac{15}{2048}.
\]

Every strict case has the same size pattern:
\[
|MC(T)|=3,
\qquad
UC(T)=UC^{\infty}(T)=A,
\]
where \(A\) is the full six-alternative set. Thus the uncovered operator removes nothing at all, even on its first application, while covering stability selects only half of the alternatives.

Up to relabeling, the \(240\) strict tournaments form exactly **one isomorphism class**. Its labeled orbit has size \(240\), hence its automorphism group has order
\[
\frac{6!}{240}=3.
\]

A canonical representative on alternatives \(A,B,C,D,E,F\) has out-neighborhoods
\[
\begin{aligned}
A&\to\{D,F\},&
B&\to\{A,C,F\},&
C&\to\{A,E\},\\
D&\to\{B,C\},&
E&\to\{A,B,D\},&
F&\to\{C,D,E\}.
\end{aligned}
\]
For this tournament,
\[
MC(T)=\{B,E,F\},
\qquad
UC(T)=UC^{\infty}(T)=\{A,B,C,D,E,F\}.
\]

The three members of \(MC(T)\) are exactly the vertices of outdegree \(3\), and they form the directed cycle
\[
B\to F\to E\to B.
\]
The complementary vertices all have outdegree \(2\) and form the directed cycle
\[
C\to A\to D\to C.
\]
Moreover, external stability is pointwise sharp: in the induced four-vertex tournament obtained by adjoining one excluded alternative to \(MC(T)\), \(B\) uniquely covers \(A\), \(F\) uniquely covers \(C\), and \(E\) uniquely covers \(D\).

Hence the entire first disparity layer is a single highly symmetric obstruction to uncovered-set iteration: all six vertices remain uncovered forever, yet one directed 3-cycle is the unique minimal covering core.

## Assumptions and scope
A tournament is a complete asymmetric directed graph. Covering is the standard tournament covering relation: \(y\) covers \(x\) when \(y\) defeats \(x\) and every alternative defeated by \(x\) is also defeated by \(y\).

The iterated uncovered set is obtained by repeatedly restricting to the current uncovered set until a fixed point is reached.

A covering set is internally stable when all of its members are uncovered in the induced subtournament and externally stable when every excluded alternative becomes covered after being added individually. In tournaments there is a unique inclusion-minimal covering set.

The equality statement through five alternatives and the existence of a six-alternative disparity are prior results. The new claim is the complete labeled and unlabeled classification of the first disparity layer.

No claim is made about the frequency or isomorphism structure of disparities for seven or more alternatives.

## Proof
The verifier exhausts every labeled tournament of orders \(1\) through \(6\).

For the uncovered set, two independent implementations are used. One computes uncovered alternatives from the covering relation. The other uses the equivalent two-step reachability characterization: an alternative is uncovered exactly when every other alternative is reachable from it by a directed path of length at most \(2\). Iterating either implementation gives the same \(UC^{\infty}(T)\) on every tournament in the domain.

The minimal covering set is also computed in two ways. The first enumerates every nonempty subset, tests both internal and external stability, and extracts the unique inclusion-minimal covering set. The second enumerates externally stable subsets only and extracts the unique inclusion-minimal one; the standard tournament theorem that minimal external stability implies internal stability is then checked directly on the resulting set. The two implementations agree on every tournament.

For every tournament the verifier also checks
\[
MC(T)\subseteq UC^{\infty}(T).
\]
No disparity occurs for orders at most \(5\). At order \(6\), the full joint-size histogram is
\[
\begin{array}{c|r}
(|MC|,|UC^{\infty}|,\text{equal?}) & \text{count}\\ \hline
(1,1,\text{yes}) & 6144\\
(3,3,\text{yes}) & 20240\\
(5,5,\text{yes}) & 4704\\
(6,6,\text{yes}) & 1440\\
(3,6,\text{no}) & 240.
\end{array}
\]
Thus the only strict size pattern is \((3,6)\).

Every strict tournament is then canonicalized under all \(6!\) permutations of the alternatives. Exactly one canonical bit encoding occurs, `1332`, and it occurs \(240\) times. Direct permutation replay finds exactly three automorphisms of the canonical representative.

For the canonical representative, the verifier directly checks that the full uncovered set is already all six alternatives, that the unique minimal covering set is \(\{B,E,F\}\), that its members are exactly the outdegree-\(3\) vertices, and that the external coverers of \(A,C,D\) are respectively \(B,F,E\).

## Verification
The embedded `verify_mc_ucinf_first_layer.py` uses only the Python standard library and exact finite enumeration.

It verifies:
- every labeled tournament of orders \(1\) through \(6\);
- two independent uncovered-set implementations;
- two independent minimal-covering-set characterizations;
- \(MC(T)\subseteq UC^{\infty}(T)\) throughout the domain;
- equality for all tournaments through order \(5\);
- exactly \(240\) strict order-\(6\) cases;
- exact incidence \(15/2048\);
- the complete order-\(6\) joint-size histogram;
- the universal strict pattern \((3,6)\);
- exactly one strict isomorphism class;
- orbit size \(240\) and automorphism-group order \(3\);
- the displayed canonical out-neighborhoods and covering witnesses.

Run:

`python3 verify_mc_ucinf_first_layer.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Brandt and Fischer describe the iterated uncovered set as the natural repeated-uncovered refinement and the minimal covering set as Dutta's stability refinement. Their full text explicitly states that minimal covering sets are always contained in the corresponding iterated uncovered set and gives the standard internal/external stability definition.

Brandt, Dau, and Seedig systematically define disparity indices and exhaustively analyze non-isomorphic tournaments through order \(10\). Their published Table 1 records disparity index
\[
d(MC,UC^{\infty})=6.
\]
Thus the threshold itself is prior work and is not claimed here.

The contribution here is the complete structure of that threshold layer: exactly \(240\) labeled tournaments, only one strict size pattern, one isomorphism class, automorphism-group order \(3\), and the fact that the uncovered operator is already at the full-set fixed point in every strict case.

Targeted searches using both solution names, the order-six threshold, the exact count \(240\), the reduced incidence \(15/2048\), and the one-isomorphism-class formulation did not locate an equivalent published theorem or table.

## Limitations
This is a complete finite classification at the first known disparity order, not a formula for larger tournaments.

The 2015 exhaustive study necessarily encountered the relevant order-six tournaments while determining the disparity index, but its published paper does not report their labeled count or isomorphism census. Unpublished computation files associated with that study could contain equivalent data.

The canonical integer encoding is only a reproducibility convention; the scientific statement is invariant under relabeling.

## References
1. F. Brandt, “Minimal Stable Sets in Tournaments,” arXiv:0803.2138, first submitted 14 March 2008; later *Journal of Economic Theory* 146(4) (2011), 1481–1499. DOI: 10.1016/j.jet.2011.05.004.
2. F. Brandt and F. Fischer, “Computing the minimal covering set,” *Mathematical Social Sciences* 56(2) (2008), 254–268. DOI: 10.1016/j.mathsocsci.2008.04.001.
3. F. Brandt, A. Dau, and H. G. Seedig, “Bounds on the disparity and separation of tournament solutions,” *Discrete Applied Mathematics* 187 (2015), 41–49. DOI: 10.1016/j.dam.2015.01.041.
4. B. Dutta, “Covering sets and a new Condorcet choice correspondence,” *Journal of Economic Theory* 44(1) (1988), 63–80.
