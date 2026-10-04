# Complete five-alternative Banks–minimal-covering disparity layer
## Finding
Let \(T\) be a finite tournament.

The **Banks set** \(BA(T)\) consists of the maximal elements of inclusion-maximal transitive subtournaments.

The **minimal covering set** \(MC(T)\) is the unique inclusion-minimal covering set. Equivalently, it is the unique inclusion-minimal set \(B\) such that, for every \(x\notin B\), the alternative \(x\) is not uncovered in the subtournament induced by \(B\cup\{x\}\).

Prior work establishes that \(BA(T)\) and \(MC(T)\) agree on every tournament of order at most \(4\), and that order \(5\) is the first order where they can differ.

The complete first disparity layer is:
\[
\#\{T:\ |T|=5,\ BA(T)\ne MC(T)\}=120.
\]

Since there are
\[
2^{\binom52}=2^{10}=1024
\]
labeled five-alternative tournaments, the exact uniform incidence is
\[
\frac{120}{1024}=\frac{15}{128}.
\]

Every strict case has the same set relation and the same choice-set sizes:
\[
MC(T)\subsetneq BA(T),\qquad |MC(T)|=3,\qquad |BA(T)|=4.
\]

Moreover, all \(120\) strict tournaments form a single isomorphism class. Its labeled orbit has size
\[
120=5!,
\]
so the canonical tournament has trivial automorphism group.

Using alternatives \(A,B,C,D,E\), one canonical representative has out-neighborhoods
\[
\begin{aligned}
A&\to\{B,E\},\\
B&\to\{D\},\\
C&\to\{A,B\},\\
D&\to\{A,C\},\\
E&\to\{B,C,D\}.
\end{aligned}
\]
For this tournament,
\[
BA(T)=\{A,C,D,E\},
\qquad
MC(T)=\{A,D,E\}.
\]
Its outdegree vector in the displayed labeling is
\[
(2,1,2,2,3).
\]

Thus the entire first Banks–minimal-covering disparity layer consists only of relabelings of one asymmetric tournament, and the first discrepancy always removes exactly one Banks alternative when passing to the minimal covering set.

## Assumptions and scope
A tournament is a complete asymmetric directed graph.

A subtournament is transitive when its dominance relation is a linear order. The Banks set takes the top alternative of every inclusion-maximal transitive subtournament.

For a subset \(B\), an outside alternative \(x\) is excluded by covering stability when some \(y\in B\) covers \(x\) in the subtournament induced by \(B\cup\{x\}\). The minimal covering set is the unique inclusion-minimal externally stable set for the uncovered-set relation.

The complete census covers every labeled tournament of orders \(1,\ldots,5\). The order-\(5\) disparity threshold itself is prior work; the new claim is the exact labeled count and isomorphism classification of the entire threshold layer.

No statement is made about the frequency or isomorphism structure of disparities at order \(6\) or above.

## Proof
For each order \(n\le5\), every one of the
\[
2^{\binom n2}
\]
labeled tournaments is enumerated.

The Banks set is computed independently in two ways.

First, a dynamic program marks transitive subsets by repeatedly deleting a maximal vertex. An inclusion-maximal transitive subset contributes its unique maximal vertex to \(BA(T)\).

Second, a tournament subset is declared transitive exactly when it contains no directed \(3\)-cycle. Inclusion-maximal subsets under this independent criterion are found directly, and their unique dominating vertices are collected.

The two Banks implementations agree on every tournament through order \(5\).

The minimal covering set is also computed independently in two ways.

First, every nonempty subset \(B\) is tested for uncovered-set stability: for every \(x\notin B\),
\[
x\notin UC(B\cup\{x\}).
\]
The unique inclusion-minimal stable set is returned.

Second, every subset \(B\) is tested directly against the covering definition: for each \(x\notin B\), some \(y\in B\) must defeat \(x\) and defeat every member of \(B\) that is defeated by \(x\). Again the unique inclusion-minimal qualifying set is returned.

The two minimal-covering implementations agree on every tournament through order \(5\).

The exact order-\(5\) joint histogram is
\[
\begin{array}{c|r}
(|BA|,|MC|,\text{equal?}) & \text{count}\\ \hline
(1,1,\text{yes}) & 320\\
(3,3,\text{yes}) & 520\\
(5,5,\text{yes}) & 64\\
(4,3,\text{no}) & 120.
\end{array}
\]
No disparity occurs at smaller orders.

Every one of the \(120\) strict tournaments is then canonicalized under all
\[
5!=120
\]
permutations of the alternative labels. Exactly one canonical bit encoding occurs, namely \(41\), and it occurs \(120\) times.

The orbit of this representative itself has \(120\) distinct labeled tournaments, proving that its automorphism group is trivial and that the orbit is exactly the full first-disparity layer.

## Verification
The embedded `verify_banks_minimal_covering_first_layer.py` uses only the Python standard library and exact finite enumeration.

It verifies:
- every labeled tournament of orders \(1,\ldots,5\);
- equality \(BA(T)=MC(T)\) through order \(4\);
- two independent Banks-set computations;
- two independent minimal-covering-set computations;
- the exact order-\(5\) histogram \(320,520,64,120\);
- exactly \(120\) strict cases and probability \(15/128\);
- strict containment \(MC(T)\subsetneq BA(T)\) in every divergent case;
- choice-set sizes \((4,3)\) in every divergent case;
- exactly one divergent isomorphism class;
- orbit size \(120\) and automorphism-group order \(1\);
- the canonical representative with encoding \(41\), the displayed out-neighborhoods, and the displayed choice sets.

Run:

`python3 verify_banks_minimal_covering_first_layer.py`

The first output line must be `VERIFY_OK`.

## Relationship to prior work
Brandt's tournament-solution framework defines the Banks set as the maximal elements of inclusion-maximal transitive subsets and the minimal covering set as the unique minimal stable set with respect to the uncovered set.

Brandt, Dau, and Seedig systematically studied disparity indices between tournament solutions. Their exhaustive analysis establishes that a five-alternative tournament is minimal for \(BA\ne MC\). They display one such tournament in which
\[
BA(T)=UC(T)
\]
has four alternatives while
\[
MC(T)=UC^\infty(T)
\]
has three.

That threshold and witness are treated as prior. The contribution here is the complete threshold-layer classification: exactly \(120\) labeled strict cases, all with the same containment and size pattern, and exactly one unlabeled asymmetric tournament.

The later survey literature records the same five-alternative Banks–minimal-covering disparity threshold but does not supply the \(120\)-tournament census or one-orbit classification.

Targeted searches for the exact count \(120\), the fraction \(15/128\), and a one-isomorphism-class five-alternative Banks–minimal-covering census did not locate an equivalent published statement.

## Limitations
The theorem is a complete finite classification only through the first disparity order.

The order-\(5\) threshold itself is not new.

The originality search did not locate the exact census, but an unindexed historical computation, thesis appendix, teaching dataset, or unpublished output from an earlier tournament enumeration could contain the same result.

The original Banks and Dutta articles are historically earlier than the day-resolved archive anchor used in the metadata; no exact public day was invented for those older sources.

## References
1. F. Brandt, “Minimal Stable Sets in Tournaments,” arXiv:0803.2138, first submitted 14 March 2008; later *Journal of Economic Theory* 146(4) (2011), 1481–1499.
2. F. Brandt, A. Dau, and H. G. Seedig, “Bounds on the disparity and separation of tournament solutions,” *Discrete Applied Mathematics* 187 (2015), 41–49. DOI: 10.1016/j.dam.2015.01.041.
3. J. S. Banks, “Sophisticated Voting Outcomes and Agenda Control,” *Social Choice and Welfare* 1(4) (1985), 295–306.
4. B. Dutta, “Covering sets and a new Condorcet choice correspondence,” *Journal of Economic Theory* 44 (1988), 63–80.
