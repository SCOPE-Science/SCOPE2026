# General-position polynomials, maximal sets, and strict log-concavity of \(\overline{C_n}\)

## Finding
For every integer \(n\ge5\), let \(G_n=\overline{C_n}\), the complement of the simple \(n\)-cycle. A set \(S\subseteq V(G_n)\) is in *general position* if no shortest path contains three of its vertices. There are exactly three mutually exclusive structural forms: (i) independent sets in the original cycle, (ii) its edges as two-vertex sets, and (iii) its three cyclically consecutive vertices. Form (ii) is disjoint from (i); form (iii) is disjoint from both.

Writing \(\psi_n(z)=\sum_{S\text{ in general position}}z^{|S|}\), one obtains the exact all-set polynomial
\[
\boxed{\psi_n(z)=\sum_{k=0}^{\lfloor n/2\rfloor}\frac{n}{n-k}\binom{n-k}{k}z^k+n z^2+n z^3.}
\]
The coefficients in degrees \(0\) through \(\max\{3,\lfloor n/2\rfloor\}\) are **strictly log-concave**, and therefore unimodal.

Define \(M_n(z)=\sum_{S\text{ inclusion-maximal in general position}}z^{|S|}\). The complete maximal-set census is
\[
\boxed{M_n(z)=\begin{cases}
5z^3,&n=5,\\
3z^2+8z^3,&n=6,\\
nz^3+\displaystyle\sum_{k=\lceil n/3\rceil}^{\lfloor n/2\rfloor}\frac{n}{k}\binom{k}{n-2k}z^k,&n\ge7.
\end{cases}}
\]
Consequently the lower general-position number is \(2\) precisely when \(n=6\), and \(3\) otherwise. The upper general-position number is \(\max\{3,\lfloor n/2\rfloor\}\).

## Assumptions and scope
Vertices are labeled \(0,1,\ldots,n-1\), with all indices understood modulo \(n\). The original cycle has edges \(\{i,i+1\}\); in its complement exactly these pairs are nonedges. The parameter \(n\) is an arbitrary integer at least five. A set is *inclusion-maximal* when no vertex can be added while retaining general position, regardless of cardinality. The all-set and maximal-set polynomials count distinct labeled vertex subsets, not isomorphism types. The independence polynomial of the original cycle is \(I(C_n;z)=\sum_k b_{n,k}z^k\), with \(b_{n,k}=\frac{n}{n-k}\binom{n-k}{k}\) and \(b_{n,0}=1\).

## Proof
**1. Reduction to three shapes.** For every \(n\ge5\), two nonadjacent vertices of \(G_n\) are consecutive in the original cycle, and have a common neighbor in \(G_n\); hence \(G_n\) has diameter two. Therefore a forbidden general-position triple is exactly an induced three-vertex path in \(G_n\). Equivalently, \(G_n[S]\) is a disjoint union of cliques, or \(C_n[S]\) is complete multipartite. This follows directly by comparing the induced three-vertex graphs (and is compatible with the general theorem of Anand et al.).

The original cycle is triangle-free and has maximum degree two. Any induced complete multipartite subgraph containing an edge must therefore be a star with at most two leaves. Indeed three nonempty parts would give a triangle. With two parts of sizes \(a,b\), each vertex has degree the opposite part size, so \(a,b\le2\); the case \(a=b=2\) would give an induced four-cycle, impossible in a simple cycle of length at least five. Thus the only edge-containing possibilities are a single edge and a three-vertex path. An induced subgraph with no edge is independent. This is the asserted exhaustive, disjoint classification.

**2. Count all sets.** For \(0<k\le\lfloor n/2\rfloor\), an independent \(k\)-set of the original cycle has cyclic gaps of at least two positions between successive chosen vertices. Rooting at one of its \(k\) chosen vertices gives \(n\binom{n-k-1}{k-1}/k=\frac{n}{n-k}\binom{n-k}{k}\). The empty set contributes one. There are \(n\) cycle edges, and, for \(n\ge5\), exactly \(n\) distinct three-consecutive vertex sets. Their cardinalities separate these extra families from cycle-independent sets, yielding \(\psi_n\).

**3. Count inclusion-maximal sets.** Every consecutive original-cycle triple is inclusion-maximal: adding an outside vertex would give an induced cycle subgraph that is no longer complete multipartite. Every original-cycle adjacent pair extends to such a triple and is never maximal. For an original-cycle independent set of size at least three, any extension in general position must remain original-cycle independent; hence its maximality is exactly maximal independence in \(C_n\). A maximal independent \(k\)-set of the cycle has all cyclic gaps equal to two or three. The number of length-three gaps is \(n-2k\). Rooting at a selected vertex and arranging the gaps gives \(\frac{n}{k}\binom{k}{n-2k}\), supported precisely on \(\lceil n/3\rceil\le k\le\lfloor n/2\rfloor\). Independently maximal two-sets occur only when \(n\le6\); for \(n=5\), all independent pairs lie within a consecutive triple. For \(n=6\), exactly the three opposite pairs are independently maximal and cannot extend to a consecutive triple. Adding the \(n\) maximal consecutive triples gives the claimed cases, and the extrema of their support give the lower and upper general-position numbers.

**4. Strict log-concavity.** Write the coefficients of \(\psi_n\) as \(a_k\), and those of the original-cycle independence polynomial as \(b_k\). Then \(a_2=b_2+n\), \(a_3=b_3+n\), and all other coefficients are \(b_k\). The nonzero \(b_k\) satisfy
\[
\frac{b_k}{b_{k-1}}=\frac{(n-2k+2)(n-2k+1)}{k(n-k)}.
\]
This ratio strictly decreases as \(k\) advances up to \(\lfloor n/2\rfloor\): both numerator factors strictly decrease while \(k(n-k)\) strictly increases throughout that range. Hence \(b_k^2>b_{k-1}b_{k+1}\) for every internal positive-support index. It only remains to verify the affected indices \(1,2,3,4\), when internal. Direct polynomial simplification gives
\[
\begin{aligned}
a_1^2-a_0a_2&=\frac{n(n+1)}2,\\
a_2^2-a_1a_3&=\frac{n^2(n^2+12n-49)}{12},\\
a_3^2-a_2a_4&=\frac{n^2}{144}(n^4-15n^3+157n^2-921n+2074),\\
a_4^2-a_3a_5&=\frac{n^2(n-7)(n-6)}{2880}(n^4-11n^3-19n^2+635n-2238).
\end{aligned}
\]
The third line is needed only when \(n\ge8\), and its quartic equals \(t^4+5t^3+82t^2+24t+144\) for \(t=n-5\ge0\). The fourth line is needed only when \(n\ge10\), and its quartic equals \(t^4+29t^3+251t^2+955t+1212\) for \(t=n-10\ge0\). Every displayed defect is therefore strictly positive in its applicable range. This proves strict log-concavity; since the coefficients have no internal zeros, unimodality follows.

## Verification
The independently implemented `verify_gp.py` reconstructs graph distances by breadth-first search and enumerates every vertex subset for each \(5\le n\le14\). It checks general-position membership by geodesic triples, maximality by all single-vertex additions, and both derived counting formulas. Its recorded stdout is in `verification_output.txt`.

A separate exact-arithmetic check, `check_coefficients.py`, evaluates strict log-concavity for all integers \(5\le n\le500\), with result in `coefficient_output.txt`. These finite tests are cross-checks, not substitutes for the infinite-family proof. Reproduction: `python3 verify_gp.py` and `python3 check_coefficients.py`.

## Relationship to prior work
Anand, Chandran, Changat, Klavžar and Thomas prove the general structural criterion for general-position sets, and a diameter-two maximum-number theorem (arXiv:1812.08460; Theorems 3.1 and 4.1). Those foundational statements motivate the induced-subgraph reduction; they do not give this specific anti-cycle polynomial, count all maximal sets, or prove strict coefficient inequalities.

Di Stefano, Klavžar, Krishnakumar, Tuite and Yero introduce and investigate the lower general-position number (arXiv:2306.09965, first publicly submitted 16 June 2023). Their inspected graph families include Kneser graphs, complete-graph line graphs and products, not anti-cycles.

Iršič, Klavžar, Rus and Tuite introduce the general-position polynomial and study cycles, complete bipartite graphs, joins, products, and unimodality (arXiv:2401.05696 / DOI:10.1007/s00025-024-02133-3). Their cycle formula applies to \(C_n\), not \(\overline{C_n}\) except coincidentally at \(n=5\). Their propositions do not state the anti-cycle maximal census or strict log-concavity. Rather's 2026 follow-up (arXiv:2603.06930) studies other graph families and likewise does not supply this statement.

The cycle independence polynomial is classical; it accounts for only the first summand and does not by itself determine which extra sets are general-position sets, maximal-set counts, or the strict inequalities after the two coefficient perturbations.

## Limitations
This theorem concerns simple cycle complements for \(n\ge5\), not arbitrary complements of triangle-free graphs, nor any variant (dual, outer or total) of general position. It does not assert real-rootedness or uniqueness of the general-position polynomial. All finite checks have explicitly bounded ranges. Bibliographic priority remains subject to independent checking, including possible unpublished or unindexed equivalent formulations. Independent scientific review has not been performed.

## References
1. B. S. Anand, U. Chandran S. V., M. Changat, S. Klavžar and E. J. Thomas, *Characterization of general position sets and its applications to cographs and bipartite graphs*, arXiv:1812.08460; https://users.fmf.uni-lj.si/klavzar/preprints/GPnumber-revised.pdf.
2. G. Di Stefano, S. Klavžar, A. Krishnakumar, J. Tuite and I. G. Yero, *Lower General Position Sets in Graphs*, arXiv:2306.09965v1 (16 June 2023); https://users.fmf.uni-lj.si/klavzar/preprints/2306.09965.pdf.
3. V. Iršič, S. Klavžar, M. Rus and J. Tuite, *General Position Polynomials*, Results in Mathematics (2024), DOI:10.1007/s00025-024-02133-3; https://link.springer.com/article/10.1007/s00025-024-02133-3.
4. B. A. Rather, *Explicit Formulas and Unimodality Phenomena for General Position Polynomials*, arXiv:2603.06930 (2026); https://arxiv.org/html/2603.06930.
