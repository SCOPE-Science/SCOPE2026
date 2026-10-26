# Four-point cyclic translate classes: an exact autocorrelation criterion for online shattering

## Finding

**Theorem.** Let \(n\ge8\), \(G=\mathbb Z/n\mathbb Z\), and let \(A\subset G\) have exactly four elements. Consider the concept family of all *distinct* translates
\[
\mathcal T(A)=\{h_c:c\in G\},\qquad h_c(x)=\mathbf 1[x\in A+c].
\]
Write \(H=\{t\in G:A+t=A\}\), \(q=|H|\), and \(\lambda_A(t)=|A\cap(A+t)|\) for \(t\ne0\). Then
\[
\operatorname{Ldim}(\mathcal T(A))=
\begin{cases}
1,&q=4,\\
3,&q=1\text{ and }\exists t\ne0:\lambda_A(t)=2,\\
2,&\text{otherwise}.
\end{cases}
\]
In particular, for every \(n\ge15\), the aperiodic sets \(\{0,1,3,7\}\) and \(\{0,1,2,3\}\) yield \(n\) distinct hypotheses apiece, each supported on four points, but have Littlestone dimensions two and three respectively. Their difference is detected exactly by the multiplicity of differences in the cyclic group, not by hypothesis counts or individual support sizes.

## Assumptions and scope

The domain is the entire finite cyclic group \(G\), and a membership query may be any \(x\in G\). The hypothesis family consists of Boolean indicators of distinct translated four-subsets. The order of the group is at least eight. A complete binary tree is Littlestone-shattered if every possible sequence of edge labels along every root-to-leaf path is realized by at least one hypothesis. The dimension is its maximum depth, with dimension zero for a singleton class.

For \(A\subset G\), the stabilizer \(H\) is a subgroup and \(q=|H|\) divides \(|A|=4\), so \(q\in\{1,2,4\}\). The number of distinct translates is \(n/q\). The correlation \(\lambda_A(t)\) counts ordered differences equal to \(t\): it is the number of \(a\in A\) for which \(a-t\in A\).

## Proof

**One-point and two-point version-space facts.** Every set of \(m\) distinct Boolean hypotheses has Littlestone dimension at most \(\lfloor\log_2m\rfloor\), since the leaves of a complete shattered tree need mutually distinct witnesses. A version space of at least two *distinct* hypotheses has dimension at least one: some query separates two of them. More generally, if a root query has at least two distinct hypotheses under *each* label, the whole class shatters a tree of depth two, by choosing a distinguishing query separately in each branch.

**Period reduction.** Since \(H\) acts freely by translations, each orbit of its action on \(G\) has \(q\) points. The set \(A\) is a union of such orbits. Because \(|A|=4\), only \(q=1,2,4\) are possible, and \(\mathcal T(A)\) is naturally identified with the translate family of \(A/H\) on the quotient \(G/H\), which has \(n/q\) elements and \(4/q\) positive centers at each query.

If \(q=4\), \(A/H\) is a singleton. A positive answer determines the unique hypothesis, so depth two is impossible; since the quotient contains at least two elements, depth one is possible. Thus the dimension is exactly one.

If \(q=2\), the quotient contains \(n/2\ge4\) points and each query has exactly two positive hypotheses and at least two negative hypotheses. All quotient translates are distinct by the definition of the *full* stabilizer. The two-point version-space fact gives depth two, while the two-element positive branch prevents depth three. Thus the dimension is exactly two.

**Aperiodic case.** Now let \(q=1\). There are exactly \(n\) distinct hypotheses. Each query has four positive hypotheses and \(n-4\ge4\) negative hypotheses, so the class shatters depth two. Every possible depth-three tree must start with a positive branch containing only four hypotheses, so depth four is impossible by the elementary cardinality bound.

Fix any root query, say \(x=0\), and let \(P\) be its four positive hypotheses. The number of hypotheses positive at both \(0\) and \(y\) is \(\lambda_A(y)\), up to replacing \(y\) by its negative (which leaves existence unaffected). A depth-two tree on the four hypotheses in \(P\) requires its first query to split them exactly two versus two, hence necessarily \(\lambda_A(y)=2\) for some nonzero \(y\). Thus if every nonzero correlation differs from two, a depth-three tree is impossible and the dimension is two.

Conversely, suppose \(\lambda_A(y)=2\) for some \(y\ne0\). Ask first at \(0\), then at \(y\) in *both* branches. Across the four label pairs \((1,1),(1,0),(0,1),(0,0)\), the version-space cardinalities are respectively
\[
2,\quad2,\quad2,\quad n-6.
\]
All are at least two because \(n\ge8\). Since distinct translates define distinct Boolean functions, each of these four version spaces contains two functions distinguished by a suitable third query. Choose that third query independently in each branch. This yields a complete shattered tree of depth three, proving the claimed equivalence.

**Sharp family separation.** For \(n\ge15\), the twelve nonzero ordered differences of \(A=\{0,1,3,7\}\) are represented exactly once each: they are \(\pm1,\pm2,\pm3,\pm4,\pm6,\pm7\), all distinct modulo \(n\). Thus \(\lambda_A(t)\le1\) for nonzero \(t\) and \(A\) is aperiodic, giving dimension two. For \(B=\{0,1,2,3\}\), the translate by two overlaps \(B\) in exactly \(\{2,3\}\), and \(B\) is aperiodic for \(n\ge8\); its dimension is three. Both classes have \(n\) distinct hypotheses, all of four-point support. \(\square\)

## Verification

The included `verify_four_shifts.py` implements an *independent* recursive depth-checking solver over actual Boolean hypothesis tables. It constructs the unique distinct translates, tests depth zero through three via all possible adaptive queries, and checks its output against the closed criterion above for **all 20,293 four-element subsets of cyclic groups of orders 8 through 20**. It also builds and checks actual shattered-tree witnesses for representative cases (dimensions one, two and three), including the cyclic \((13,4,1)\) difference set \(\{0,1,3,9\}\). Run `python3 verify_four_shifts.py` with Python 3.8 or later. The checked output is supplied as `verification_output.txt`; finite checks complement, but do not replace, the proof for all \(n\ge8\).

## Relationship to prior work

Ghazi–Golowich–Kumar–Manurangsi develop general Littlestone-dimension closure bounds, not sharp dimension formulas for fixed-size cyclic translation orbits. Malliaris–Moran connect Littlestone trees and finite model-theoretic stability, without evaluating these cyclic classes. Aaronson–Ellis–Leader study the union-closed family generated by **all unions** of translates of a fixed set, not the Littlestone dimension of the individual translate family. Their general objects are relevant, but their conclusion does not imply this three-valued dimension classification. The exact threshold here uses nonzero autocorrelation multiplicity \(2\), rather than only cardinality of the support, number of translates, or asymptotic learning bounds.

## Limitations

The classification is only claimed for four-element supports on cyclic groups of order \(n\ge8\); smaller groups and supports of other cardinalities are outside scope. The result does not classify all possible VC dimensions or all Littlestone dimensions of arbitrary finite translate families. An exhaustive finite check is not a proof for unbounded group order; the proof above provides that step. Publication-priority searches cannot exclude every differently named earlier treatment of four-uniform circulant designs or cyclic translation systems. No independent scientific audit has been performed.

## References

1. B. Ghazi, N. Golowich, R. Kumar, P. Manurangsi, *Near-tight closure bounds for Littlestone and threshold dimensions*, arXiv:2007.03668v1 (first public 2020-07-07), especially Section 2.
2. J. Aaronson, D. Ellis, I. Leader, *A note on transitive union-closed families*, arXiv:2010.08795 (first public 2020-10-17), especially Theorem 2 and its proof.
3. M. Malliaris, S. Moran, *Agnostic Online Learning and Excellent Sets*, arXiv:2108.05569 (first public 2021-08-12), especially the online-learning introduction and subsequent stable-class theorems.
