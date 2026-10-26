# Dissociation and maximal-dissociation enumerators of complete-graph subdivisions

## Finding
For every integer \(n\ge3\), let \(H_n=S(K_n)\) be the graph formed by replacing every edge of the complete graph \(K_n\) with a two-edge path. Define the dissociation polynomial \(D_n(z)=\sum_{F}z^{|F|}\), where the sum runs over vertex subsets \(F\subseteq V(H_n)\) inducing maximum degree at most one. Define \(M_n(z)\) similarly, summing only over inclusion-maximal such sets.

**Theorem.** The complete cardinality polynomials are
\[
D_n(z)=\sum_{a=0}^{n}\binom{n}{a}z^a(1+z)^{\binom{n-a}{2}}(1+(n-a)z)^a,
\]
and
\[
\begin{aligned}
M_n(z)={}&z^n+n z^{2n-2}+\binom n2(2^{n-2}-2)z^{2n-3}\\
&+\sum_{b=3}^{n}\binom nb b^{n-b}z^{2(n-b)+\binom b2}.
\end{aligned}
\]
These formulas count *labeled* subsets of a fixed graph, not graph isomorphism classes. In particular, for \(n\ge4\) the unique smallest inclusion-maximal dissociation set comprises all \(n\) original vertices. For \(n\ge5\), the unique largest one comprises all \(\binom n2\) subdivision vertices. The gap between these two maximal-set cardinalities is \(\binom n2-n\), growing quadratically. The boundary cases are \(M_3(z)=2z^3+3z^4\) and \(M_4(z)=z^4+24z^5+5z^6\).

## Assumptions and scope
All graphs are finite, undirected and simple. Write \(O=\{1,\ldots,n\}\) for the old vertices and \(w_{ij}\) for the degree-two subdivision vertex replacing original edge \(\{i,j\}\). Thus \(V(H_n)=O\sqcup W\), with \(W=\{w_{ij}:1\le i<j\le n\}\); the only neighbors of \(w_{ij}\) are \(i\) and \(j\). A vertex subset is a dissociation set precisely if every selected vertex has at most one selected neighbor. "Inclusion-maximal" is distinct from "maximum cardinality."

For a candidate \(F\), put \(A=F\cap O\) and \(C=O\setminus A\); set \(a=|A|\) and \(b=|C|=n-a\). The term \(\binom n2(2^{n-2}-2)\) in the formula for \(M_n\) is zero when \(n=3\).

## Proof
**Admissible sets.** Fix \(A\subseteq O\) of cardinality \(a\), with \(b=n-a\) omitted old vertices. A selected subdivision vertex cannot have two selected old endpoints, so no subdivision vertex joining two members of \(A\) may occur. For each \(v\in A\), at most one of the \(b\) subdivision vertices \(w_{vc}\), \(c\in C\), may occur, because otherwise the induced degree of \(v\) exceeds one. Conversely, these are the only restrictions: vertices in \(W\) are mutually nonadjacent, selected subdivision vertices with both endpoints in \(C\) are isolated, and those joining \(A\) to \(C\) have exactly one selected neighbor. Consequently the choices are independent: each of the \(\binom b2\) internal subdivision vertices of \(C\) may be chosen or not, while each \(v\in A\) chooses either no cross subdivision vertex or exactly one of \(b\) possibilities. The resulting weight polynomial for this fixed \(A\) is \(z^a(1+z)^{\binom b2}(1+bz)^a\). Summing over the \(\binom na\) possibilities for \(A\) proves the formula for \(D_n\).

**Maximality, necessity.** Suppose first that \(b\ge1\). All \(\binom b2\) subdivision vertices joining two omitted old vertices must be selected; any missing such vertex could be adjoined without violating the degree bound. Each selected original vertex \(v\in A\) must have exactly one selected cross subdivision neighbor, for otherwise one of the \(b\) vertices \(w_{vc}\) could be added. Thus every maximal set with \(b\ge1\) is determined by \(A\), all internal subdivision vertices of \(C\), and a function \(f:A\to C\) choosing the one cross subdivision neighbor of each original vertex in \(A\). Its cardinality is precisely \(2a+\binom b2\).

**Maximality, sufficiency and exceptional boundary.** Under this description, no further subdivision vertex can be added: those internal to \(C\) are already present; those internal to \(A\) would have induced degree two; and a missing cross vertex would raise its endpoint's induced degree from one to two. A missing original vertex \(c\in C\) can be added only if it has at most one selected internal subdivision neighbor (there are \(b-1\) such neighbors) *and* no selected cross subdivision vertex \(w_{vc}\) whose other endpoint \(v\in A\) is selected (such an edge vertex would then gain a second selected neighbor). Thus \(c\) cannot be added if and only if \(b-1\ge2\) or \(c\in f(A)\). If \(b\ge3\), maximality is automatic, with \(b^a\) functions. If \(b=2\), maximality holds precisely when \(f\) is surjective onto \(C\), giving \(2^a-2\) functions by inclusion–exclusion. If \(b=1\), all \(v\in A\) map to its unique element, and because \(n\ge3\) makes \(a\ge2\), the lone omitted old vertex cannot be added. There is therefore one maximal set per choice of its omitted original, giving \(n\) choices. Finally, if \(b=0\), all old vertices are selected and no subdivision vertex can be selected; this set is maximal, giving the solitary term \(z^n\). Counting choices of \(C\) proves the formula for \(M_n\), including all boundary cases.

**Extremal cardinalities.** For \(b\ge1\), the maximal-set size is \(f_n(b)=2(n-b)+\binom b2\). This convex quadratic is minimized on positive integers at \(b=2\) or \(b=3\), where it equals \(2n-3\), and its maximum on \(1\le b\le n\) occurs at \(b=1\) or \(b=n\), with respective values \(2n-2\) and \(\binom n2\). For \(n\ge4\), \(2n-3>n\), making the all-original set the unique minimum-cardinality maximal set. For \(n\ge5\), \(\binom n2>2n-2\), making the all-subdivision set the unique maximum-cardinality maximal set. Direct substitution handles \(n=3,4\). The second polynomial retains all intermediate cardinality gaps and their exact multiplicities.

## Verification
Run `python3 verify_subdivision.py` using Python 3 and its standard library. The accompanying `verification_output.txt` records all checks. The verifier reconstructs the graph directly from the incidence edges, checks the induced degree of every selected vertex, tests inclusion-maximality by trial insertion of every missing vertex, and independently compares *every coefficient* and the profile by number of omitted old vertices for \(n=3,4,5,6\). It exhaustively examines \(2^{6}+2^{10}+2^{15}+2^{21}=2{,}131{,}008\) vertex subsets. These finite tests do not establish the infinitely quantified theorem; the argument above does.

## Relationship to prior work
Brešar, Hartnell, and Rall (2017) introduced and structurally studied uniform dissociation and the equivalence between dissociation-set complements and three-vertex-path covers. Their classification of uniformly dissociated graphs does not enumerate all inclusion-maximal sets of full complete-graph subdivisions. Tu, Li, and Du (2021) prove universal bounds and extremal classifications for numbers of maximal dissociation sets in general and triangle-free graphs, but not the exact two-polynomial formulas or the fiber-surjectivity condition for this family. Tu, Xiao, and Lang (2023) give coefficient/partition-function bounds for cubic graphs, rather than the present variable-degree incidence graphs. The displayed explicit counts and maximality classification were not found in the inspected literature; the possibility of an equivalent unindexed result is an outstanding priority risk.

## Limitations
The formulas concern full one-edge subdivisions of \(K_n\), for \(n\ge3\); they do not extend automatically to partial subdivisions or arbitrary base graphs. A generic finite sum should not be confused with a polynomial-time coefficient algorithm for large \(n\). Earlier general definitions, equivalences, bounds and complexity results are not claimed as new. No independent mathematical audit has been performed, and coverage of unindexed literature is not guaranteed.

## References
1. B. Brešar, B. L. Hartnell and D. F. Rall, *Uniformly dissociated graphs*, Ars Mathematica Contemporanea 13 (2017), 293–306. DOI: 10.26493/1855-3974.1013.46a. First public online 2017-03-09.
2. J. Tu, Y. Li and J. Du, *Maximal and Maximum Dissociation Sets in General and Triangle-Free Graphs*, arXiv:2103.01402v1 (2021-03-02). https://arxiv.org/abs/2103.01402
3. J. Tu, J. Xiao and R. Lang, *Counting the number of dissociation sets in cubic graphs*, AIMS Mathematics 8 (2023), 10021–10032. DOI: 10.3934/math.2023507.
