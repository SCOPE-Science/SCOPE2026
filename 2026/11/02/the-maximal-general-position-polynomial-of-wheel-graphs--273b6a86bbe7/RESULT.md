# The maximal general-position polynomial of wheel graphs

## Finding
Let \(W_n=K_1\vee C_n\) be the wheel with \(n\ge5\) rim vertices and one hub. A vertex subset is in *general position* if no shortest path contains three selected vertices. Let \(A_n(z)\) count **inclusion-maximal** general-position subsets by cardinality, counting the labeled rim vertices individually. Then

\[
\boxed{A_n(z)=nz^3-n[u^n]\log\!\left(1-zu^2-z^2u^3-z^2u^4+z^3u^6\right).}
\]

The formal logarithm is expanded at \(u=0\); its coefficient is a polynomial in \(z\). The \(n\) hub-containing maximal sets have size three. Every other maximal set lies entirely on the rim and has a unique circular decomposition into runs of selected vertices of length one or two separated by runs of unselected vertices of length one or two. An unselected run of length two is permitted precisely when its two neighboring selected runs both have length two. Conversely every such circular pattern is maximal.

The smallest rim-only maximal set has size \(\lceil n/2\rceil\). Its exact number is

\[
L_{n,\min}=\begin{cases}
n\lfloor(n+1)/4\rfloor,&n\text{ odd},\\
2+4\mathbf1_{\{4\mid n\}},&n\text{ even}.
\end{cases}
\]

For \(n\ge6\), the largest general-position sets have size \(\lfloor2n/3\rfloor\); the number of these sets is

\[
L_{n,\max}=\begin{cases}
3,&n=3k,\\
n(k+2)/2,&n=3k+1,\\
n,&n=3k+2,
\end{cases}
\]

with \(k\) a positive integer and the displayed cases restricted to \(n\ge6\). In particular, the size of the smallest maximal set of \(W_n\) is three; this scalar observation is not asserted as new.

The total number of maximal sets also has a precise exponential asymptotic:
\[
A_n(1)=n+\alpha^n+O(1),\qquad \alpha=1.40126836793985\ldots,
\]
where \(\alpha\) is the unique real root greater than one of \(\lambda^6-\lambda^4-\lambda^3-\lambda^2+1=0\). The error in the displayed estimate has absolute value at most five.

## Assumptions and scope
Graphs are simple, undirected and finite. The definition \(W_n=K_1\vee C_n\) uses **rim order** \(n\), not total wheel order; the wheel therefore has \(n+1\) vertices. The claim covers every integer \(n\ge5\). A general-position set is *inclusion-maximal* when no omitted vertex can be added without violating general position; it need not have maximum cardinality. The coefficient of \(z^j\) in \(A_n\) counts sets of cardinality \(j\), not sequences or isomorphism orbits. For completeness, the smaller wheel \(W_4\) has maximal-set polynomial \(2z^2+4z^3\), and \(W_3=K_4\) has \(z^4\); these are outside the displayed general formula's domain.

## Proof
**1. Geodesic characterization.** The diameter of \(W_n\) is two. A set omitting the hub is in general position exactly when it contains no three consecutive rim vertices: any selected path of three successive rim vertices has endpoints at distance two, while an internal rim vertex of any length-two geodesic between rim vertices must lie in such a triple. If the hub belongs to a general-position set, the selected rim vertices must be pairwise adjacent; otherwise the hub lies on their two-edge geodesic. Since a cycle of length at least five has clique number two, a maximal hub-containing set consists of the hub and the two endpoints of one rim edge, giving precisely \(n\) maximal sets of size three.

**2. Exact classification without the hub.** A maximal hub-free set must avoid \(111\) in its cyclic zero-one word. Each run of ones consequently has length one or two. A run of zeros of length at least three has an interior zero that could be flipped to one without creating \(111\), contradicting maximality. An isolated zero is always blocked, since its two neighbors are ones. If two consecutive zeros occur, flipping the first can create \(111\) only when the immediately preceding two vertices are ones; flipping the second can create \(111\) only when the immediately following two vertices are ones. Thus a zero-run of length two is blocked if and only if it has a two-vertex one-run on each side. This proves the claimed run criterion, including its converse. In each paired run \((a_i,b_i)\), with \(a_i\) the selected-run length and \(b_i\) the subsequent zero-run length, we have \(b_i\le a_i\), so selected vertices are at least as numerous as unselected vertices. For \(n\ge5\), there are at least three selected rim vertices. They cannot all form a clique; hence adding the hub also violates general position. Therefore the cyclic maximal \(111\)-avoiding words are precisely the hub-free maximal sets in \(W_n\).

**3. Exact polynomial.** Index the lengths of successive selected runs by \(a,b\in\{1,2\}\). The transfer from one selected run of length \(a\) to the next of length \(b\), including the intervening zero-run, has weight \((uz)^a(u+\mathbf1_{\{a=b=2\}}u^2)\). The transfer matrix is
\[
T(u,z)=\begin{pmatrix}u^2z&u^2z\\u^3z^2&u^3z^2+u^4z^2\end{pmatrix}.
\]
A circular pattern of length \(n\) containing \(t\) selected runs is counted by \(n\operatorname{tr}(T^t)/t\) after extracting its coefficient of \(u^n\): this chooses an indexed rim position for the beginning of a run and then removes the \(t\)-fold choice of distinguished run. The identity
\[
\sum_{t\ge1}\frac{\operatorname{tr}(T^t)}t=-\log\det(I-T)
\]
holds as a formal power series, and
\[
\det(I-T)=1-zu^2-z^2u^3-z^2u^4+z^3u^6.
\]
Adding the hub-containing configurations gives the claimed formula for \(A_n(z)\).

**4. Smallest rim-only maximal sets.** The inequalities \(b_i\le a_i\) imply \(|S|\ge\lceil n/2\rceil\). Equality for even \(n\) requires \(b_i=a_i\) for all \(i\). If any \(a_i=2\), the required neighboring-run condition forces all selected runs to have length two; the resulting word is a rotation of \(1100\) repeated and is possible exactly when \(4\mid n\), yielding four labeled patterns. Otherwise all runs have length one, giving the two alternating patterns. For odd \(n\), equality requires exactly one exceptional pair \((a_i,b_i)=(2,1)\), all others having equal entries. All length-two one-runs then form one cyclic block of \(q\ge1\) runs, terminated by that exceptional pair, followed by length-one runs; the overall length is \(4q-1+2r=n\), where \(r\ge0\) is the number of length-one runs. Thus \(1\le q\le\lfloor(n+1)/4\rfloor\), and for each \(q\), the unique exceptional pair gives exactly \(n\) labeled rotations. All these patterns meet the criterion, proving the stated count.

**5. Largest maximal sets.** Among the rim words avoiding \(111\), the number of zeros is at least \(\lceil n/3\rceil\), with equality achievable; their largest size is therefore \(\lfloor2n/3\rfloor\). For \(n=3k\), exactly three rotations of \(110\) repeated attain equality. For \(n=3k+2\), there is exactly one one-run gap of length one between successive zeros and all other gaps contain two ones, giving \(n\) labeled configurations. For \(n=3k+1\), the total deficit from two ones in each of the \(k+1\) gaps is two: either one zero-length gap (\(n\) configurations), or two one-length gaps (\(n\binom{k+1}{2}/(k+1)=nk/2\) configurations). Each such word is maximal. Hub-containing maximal sets have size only three, which is strictly smaller when \(n\ge6\). The formula for \(L_{n,\max}\) follows.

**6. Growth.** At \(z=1\), write \(D(u)=1-u^2-u^3-u^4+u^6=\prod_{j=1}^6(1-\lambda_j u)\). Then the formal logarithm yields the exact identity \(A_n(1)=n+\sum_{j=1}^6\lambda_j^n\). The \(\lambda_j\) are the roots of \(p(\lambda)=\lambda^6-\lambda^4-\lambda^3-\lambda^2+1\). Dividing \(p(\lambda)\) by \(\lambda^3\) and putting \(t=\lambda+\lambda^{-1}\) gives \(t^3-4t-1=0\). This cubic has one root greater than two, one in \((-2,-1)\), and one in \((-1,0)\), by the intermediate value theorem and its degree. The root greater than two produces a reciprocal pair \(\alpha,\alpha^{-1}\) with \(\alpha>1\); the two interior roots produce four roots on the unit circle. Thus \(|A_n(1)-n-\alpha^n|\le\alpha^{-n}+4\le5\).

## Verification
The standalone `verify.py` uses breadth-first search on the actual wheel graph to compute all shortest-path distances and forbidden geodesic triples. It enumerates **every** vertex subset for each \(5\le n\le13\), independently tests general position and inclusion-maximality, and compares each maximal-set polynomial coefficient with a separately implemented formal-power-series calculation of the claimed formula. It also checks the hub/rim dichotomy, the two extremal cardinalities and the extremal counts. A run of the packaged source produces `VERIFY_OK`; `verification_output.txt` records every checked case. These finite tests are a corroboration, not a substitute for the proof for arbitrary \(n\).

## Relationship to prior work
Yao, He, Ji and Li (2020, arXiv:2002.03108), Theorem 4.1, determine the **largest cardinality** of a general-position set in wheels, and the corresponding scalar is credited here. Iršič, Klavžar, Rus and Tuite (2024, arXiv:2401.05696), Proposition 3.3, evaluate the ordinary general-position polynomial of graph joins in terms of clique polynomials. That theorem counts all eligible sets, not only inclusion-maximal ones; it does not give their cardinality spectrum. Di Stefano and collaborators (2023, arXiv:2306.09965) introduce the *lower* general-position number. Kruft Welton and collaborators (2024, arXiv:2404.19451), Corollary 2.5, use wheel triangles as terminal sets in Cartesian products. Neither scalar/terminal result provides the present maximal-set generating function.

There is a useful, explicitly acknowledged equivalence: hub-free maximal general-position sets of \(K_1\vee C_n\) are maximal *dissociation sets* of \(C_n\) (vertex subsets inducing maximum degree one). Earlier dissociation-set results may overlap with this component. Tian and Tu, *Enumerating maximal dissociation sets in three classes of grid graphs* (2024, DOI:10.1016/j.amc.2024.128711), study related state-matrix enumerations; its full text was unavailable for a decisive scope comparison. The precise risk is that a cyclic-grid specialization may already give the rim enumerator. The new assertion is consequently a best-knowledge statement rather than a demonstrated priority claim.

## Limitations
The result is restricted to ordinary general position on wheels with at least five rim vertices and to labeled vertex subsets; it does not establish a general formula for arbitrary joins or other general-position variants. The asymptotic concerns the number of inclusion-maximal sets, not the number of all general-position sets. Prior-publication priority remains uncertain because some relevant dissociation-enumeration material could not be inspected in full. No independent external validation has been performed.

## References
1. Y. Yao, M. He, S. Ji, G. Li, *On the general position set of two classes of graphs*, arXiv:2002.03108 (first submitted 2020-02-08), Section 4, Theorem 4.1.
2. V. Iršič, S. Klavžar, G. Rus, J. Tuite, *General Position Polynomials*, arXiv:2401.05696 (first submitted 2024-01-11), Proposition 3.3; *Results in Mathematics* 79 (2024), article 110.
3. G. Di Stefano et al., *Lower General Position Sets in Graphs*, arXiv:2306.09965 (2023), Definition 1.2 and Sections 1–2.
4. E. Kruft Welton et al., *Lower General Position in Cartesian Products*, arXiv:2404.19451 (2024), Section 2, Corollary 2.5.
5. Y. Tian, J. Tu, *Enumerating maximal dissociation sets in three classes of grid graphs*, *Applied Mathematics and Computation* 474 (2024), 128711; DOI:10.1016/j.amc.2024.128711 (abstract available; full text not inspected).
