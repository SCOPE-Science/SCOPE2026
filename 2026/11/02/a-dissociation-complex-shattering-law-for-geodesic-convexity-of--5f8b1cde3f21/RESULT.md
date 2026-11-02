# A dissociation-complex shattering law for geodesic convexity of wheels

## Finding
For every integer \(m\ge5\), let \(W_{m+1}=K_1\vee C_m\) be the wheel consisting of a rim cycle \(C_m\), with cyclically indexed rim vertices \(v_0,\ldots,v_{m-1}\), and a universal hub \(h\). Let \(\mathcal C_m\) be the family of all geodesically convex vertex subsets, including \(\varnothing\) and \(V(W_{m+1})\); geodesic convexity requires the inclusion of **every** shortest path between each pair of selected vertices. A vertex support \(S\) is VC-shattered when every subset \(T\subseteq S\) equals \(C\cap S\) for some \(C\in\mathcal C_m\).

**Complete support classification.** A support \(S\subseteq V(W_{m+1})\) is shattered if and only if one of the following holds:

* The hub is absent, \(h\notin S\), and the rim support contains no three cyclically consecutive vertices.
* The hub is present and its rim portion \(S\setminus\{h\}\) has size at most one, or consists of exactly two adjacent rim vertices.

In particular, the rim-only shattering complex is **exactly the dissociation complex of the cycle**: its faces are the sets whose induced subgraphs have maximum degree at most one.

Write \(D(C_m;z)\) for the dissociation polynomial of the rim cycle and \(\Phi_m(z)=\sum_{S\text{ shattered}}z^{|S|}\). Then
\[
\boxed{\Phi_m(z)=D(C_m;z)+z+m z^2+m z^3,}
\]
with every coefficient explicit:
\[
\boxed{D(C_m;z)=\sum_{k=0}^{\lfloor2m/3\rfloor}\frac{m}{m-k}\,[t^k](1+t+t^2)^{m-k}\,z^k.}
\]
Here \([t^k]\) means coefficient extraction from a polynomial in \(t\). The formula is integral for every \(k\) in the stated range.

Consequently,
\[
\boxed{\operatorname{VCdim}(\mathcal C_m)=\left\lfloor\frac{2m}{3}\right\rfloor.}
\]
The number of **maximum-cardinality** shattered supports is \(10\) for \(m=5\). For \(m\ge6\), it is
\[
\boxed{
\begin{cases}
3,&m\equiv0\pmod3,\\
m(m+5)/6,&m\equiv1\pmod3,\\
m,&m\equiv2\pmod3.
\end{cases}}
\]
The exceptional \(m=5\) count arises because the five hub-containing shattered triples tie the five maximum rim-only supports. Thus adjoining a single universal hub to a cycle yields an exact family whose VC dimension grows linearly with rim size, despite the well-known constant-dimensional behavior of many bare-cycle convexity systems.

## Assumptions and scope
The graph is finite, simple, undirected, unweighted, with the hub adjacent to all rim vertices; the rim has at least five vertices. Convexity means containing **all** graph geodesics. Hypotheses are **all** convex subsets, not only convex halfspaces and not merely proper nonempty convex subsets. The empty and full vertex sets are retained. The word "dissociation" refers to subsets inducing maximum degree at most one **in the rim cycle**, not in the wheel itself.

## Proof
**1. Classification of convex hypotheses.** In the wheel, two rim vertices at rim distance two have shortest paths both through the hub and through their common rim neighbor. For other nonadjacent rim pairs, a shortest path uses the hub. Therefore any convex set omitting the hub is either empty, a rim singleton, or a pair of adjacent rim vertices. A convex set containing the hub is precisely \(\{h\}\cup X\), where the binary cyclic membership word of the rim subset \(X\) has no local occurrence of \(101\): otherwise two present rim vertices force the missing middle rim vertex along a shortest path. Conversely, when no such pattern occurs, all intermediate vertices on any shortest path between members of \(\{h\}\cup X\) are already present. This proves the normal form.

**2. Rim-only shattered supports.** Suppose the support contains three consecutive rim vertices with the endpoints positive and middle negative. The two endpoints force their middle vertex along a shortest path. This labeling is impossible, so such a support cannot be shattered. Conversely, let \(S\) contain no three consecutive rim vertices. Fix any desired positive subset \(T\subseteq S\). For each negative designated vertex \(s\in S\setminus T\), at least one of its two rim neighbors lies outside \(S\), because otherwise \(S\) would contain a consecutive triple. Choose one such neighbor \(u(s)\), and make both \(s\) and \(u(s)\) rim negatives. Make every other rim vertex positive, and include the hub. Every missing rim vertex has a missing rim neighbor: each chosen pair \(\{s,u(s)\}\) supplies that property even when pairs overlap. Consequently there is no \(101\) rim pattern, so the resulting set is convex by Step 1 and its trace on \(S\) is exactly \(T\). Every trace is realized.

**3. Supports containing the hub.** If \(h\in S\) is queried negatively, the chosen hypothesis must be one of the hub-free convex sets classified in Step 1. Therefore shattering requires at most two queried rim vertices, and if two, they must be adjacent. Conversely, for a hub support with zero, one, or two adjacent rim vertices, every hub-negative labeling is realized by an empty set, a singleton, or the adjacent pair, and every hub-positive labeling by a hub-containing convex set with the selected positive rim vertices (or by the full graph). Hence exactly those supports shatter.

**4. Polynomial and extremal coefficients.** The rim-only admissibility criterion is equivalent to a binary circular word with no three consecutive ones: any selected rim vertex then has at most one selected rim neighbor. If \(k\) positions are selected, let \(j=m-k\) be the number of zeros (at least one). Mark one zero and traverse the circular word: the \(j\) consecutive one-run lengths belong to \(\{0,1,2\}\) and sum to \(k\). Thus the number of marked admissible words equals \(m[t^k](1+t+t^2)^j\), while every unmarked word has exactly \(j\) choices of marked zero. Division by \(j\) yields the displayed formula for \(D(C_m;z)\). Step 3 contributes exactly one shattered hub singleton, \(m\) hub-rim pairs and \(m\) hub-adjacent-rim triples. For the VC bound, sum the \(m\) inequalities \(s_i+s_{i+1}+s_{i+2}\le2\) to get \(3k\le2m\). Equality of the floor is attained by cyclic words built from repetitions of \(110\), with the residual one or two positions filled by \(0\) or \(10\), respectively. The degree of the hub contribution is three, so the total VC dimension is \(\lfloor2m/3\rfloor\) for \(m\ge5\). For highest-degree coefficients, write \(m=3q+r\) with \(r\in\{0,1,2\}\), and take the highest allowed degree \(k=2q+\lfloor2r/3\rfloor\). The coefficient of \(t^k\) in \((1+t+t^2)^{m-k}\) is respectively \(1\), \((q+1)(q+2)/2\), or \(q+1\) for \(r=0,1,2\). Multiplication by \(m/(m-k)\) gives the three maximum-support counts in the statement. For \(m=5\), the additional \(m z^3\) term also reaches maximum degree, explaining the exception. Every assertion follows for every \(m\ge5\).

## Verification
The standalone file `wheel_convexity_check.py` independently constructs the wheel graph and all-pairs graph distances. It exhaustively enumerates the actual convex vertex sets and all shattered supports for \(5\le m\le11\), checking both geometric normal forms and every coefficient of the polynomial. For \(12\le m\le20\), it checks the complete support formula and extremal coefficients directly against cyclic-word enumeration. Run `python3 wheel_convexity_check.py` using the Python standard library. Its final expected line is `ALL_WHEEL_SHATTERING_CHECKS_PASS`. The infinite statement is proved in the preceding paragraphs; finite tests are supplementary reproducibility checks.

## Relationship to prior work
Thiessen and Gärtner study classical online learning of geodesically convex graph vertex sets, including general VC-dimension and mistake bounds, in *Online Learning of Convex Sets on Graphs* (2022), especially Section 4 and Propositions 11–12. The general theory does not provide the explicit wheel shattering complex or its full face polynomial. Tu, Xiao and Lang (2023) study counting dissociation sets in cubic graphs; dissociation sets and their generating polynomial are established combinatorial notions. The present claim is **not** that dissociation polynomials or their cycle coefficients are newly invented: it identifies the precise equivalence of a wheel graph's convex-set shattering supports with cycle dissociation sets and classifies the hub-containing exceptions. Published work on cover-free families of wheels addresses a distinct invariant. The exact-result priority comparison remains limited to the accessible sources and indexed search results.

## Limitations
This theorem concerns wheels with rim size at least five, arbitrary geodesically convex subsets rather than halfspaces, and static VC shattering. It does not assert an exact Littlestone dimension. A broader shattering theorem under different terminology may exist outside the inspected sources; no independent audit or global novelty certification has been performed.

## References
1. Maximilian Thiessen and Thomas Gärtner, *Online Learning of Convex Sets on Graphs*, ECML PKDD 2022, pp. 349–364, DOI `10.1007/978-3-031-26412-2_22`, accessible preprint: https://ecmlpkdd-storage.s3.eu-central-1.amazonaws.com/preprints/2022/lncs13716/lncs13716354.pdf (online publication 2022-09-19).
2. Jianhua Tu, Junyi Xiao and Rongling Lang, *Counting the number of dissociation sets in cubic graphs*, AIMS Mathematics 8 (2023), 10021–10032, DOI `10.3934/math.2023507`, https://www.aimspress.com/aimspress-data/math/2023/5/PDF/math-08-05-507.pdf (published online 2023-02-23).
