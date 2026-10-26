# Minimal forts of sunlet graphs: a quadratic census and a lifting obstruction

## Finding

For every integer \(n\geq 3\), let \(S_n=C_n\circ K_1\) be the sunlet with cyclic rim vertices \(v_i\) and their private leaves \(w_i\), indexed by \(i\in\mathbb Z/n\mathbb Z\). A *fort* is a nonempty vertex set \(F\) such that every vertex outside \(F\) has either zero or at least two neighbors inside \(F\); it is *minimal* if it contains no smaller nonempty fort.

**Theorem.** The number \(M_n\) of inclusion-minimal forts of \(S_n\), with named vertices, is exactly
\[
 M_n=\begin{cases}
 n(n+1)/2,&n\text{ odd},\\
 n(n-2)/2+2,&n\text{ even}.
 \end{cases}
\]
In particular, \(M_n\sim n^2/2\), and all minimal forts have the explicit connected-support description given below.

For any nonempty \(X\subseteq\mathbb Z/n\mathbb Z\), define \(B(X)\) to consist of the rim vertices \(v_i\) with \(i\in X\), together with a leaf \(w_i\) if either \(i\in X\) or \(i\notin X\) has exactly one cyclic neighbor in \(X\). Define \(H_X\) on vertex set \(X\): join \(i-1\) and \(i+1\) whenever \(i\notin X\) and both \(i-1,i+1\in X\). Then \(X\mapsto B(X)\) is a bijection from those nonempty \(X\) for which \(H_X\) is connected onto all minimal forts of \(S_n\).

There is also a concrete obstruction to the minimal-fort lifting assertion in Proposition 23 of Becker--Cameron--Hanely--Ong--Previte (arXiv:2404.05963v1): the minimal fort \(\{v_0,v_1,v_3,v_4\}\) of \(C_6\) lifts to a fort containing the proper fort \(\{v_1,v_3,w_0,w_1,w_3,w_4\}\) of \(S_6\). The asserted exponential lower bound for sunlets in that preprint's Corollary 24 is incompatible with the exact count; for example \(M_{18}=146\), whereas its rounded plastic-ratio lower bound is \(158\). These comparisons concern the identifiable 2024 preprint version; the status of later textual revisions has not been independently established.

## Assumptions and scope

All graphs are finite, simple, and undirected. The corona has exactly one private leaf at every rim vertex. Vertices, not graph-isomorphism classes, are counted. A fort is *inclusion*-minimal, not necessarily of minimum cardinality. The cycle has at least three vertices, and indices are cyclic. No assertion concerns arbitrary coronas or other definitions of zero forcing.

## Proof

**1. Canonical leaf choices.** Write \(x_i=1\) if \(v_i\in F\) and \(y_i=1\) if \(w_i\in F\). The leaf outside \(F\) has exactly one neighbor in \(F\) if \(y_i=0,x_i=1\), so \(x_i=1\) forces \(y_i=1\). When \(x_i=0\), the outside rim vertex has \(x_{i-1}+x_{i+1}+y_i\) neighbors in \(F\), a quantity forbidden to equal one. Thus \(y_i=0\) if both cyclic neighbors have value zero, \(y_i=1\) if exactly one has value one, and either choice is allowed if both have value one. In the last case removing \(w_i\) preserves the fort, so such an optional leaf cannot occur in a minimal fort. A fort with no selected rim vertex would have an outside rim vertex with exactly one selected leaf neighbor, unless it were empty; hence every fort has nonempty rim support. We have shown both that every nonempty \(X\) determines a fort \(B(X)\), and that every minimal fort is some \(B(X)\).

**2. Inclusion reduction.** Fix a nonempty \(X\). For any nonempty \(Y\subseteq X\), the canonical fort \(B(Y)\) is contained in \(B(X)\) if and only if
\[
  1_{i-1\in Y}=1_{i+1\in Y}
  \quad\text{for every }i\notin X\text{ with }i-1,i+1\in X.
\]
Indeed, the only absent leaf in \(B(X)\) that might be newly required by \(B(Y)\) is at an \(i\notin X\) with *both* cyclic neighbors in \(X\); its appearance is required precisely when just one of those two neighbors remains in \(Y\). Every other leaf needed by \(B(Y)\) was already in \(B(X)\). Conversely, for any nonempty fort \(F'\subseteq B(X)\), its nonempty rim support \(Y\) has \(B(Y)\subseteq F'\), by the mandatory-leaf conditions. Therefore a smaller fort exists inside \(B(X)\) exactly when a nonempty proper \(Y\subset X\) satisfies the displayed equalities.

**3. Connectivity criterion.** The equalities of step 2 require \(Y\) to be a union of connected components of \(H_X\). There is a nonempty proper such union exactly when \(H_X\) is disconnected. Hence \(B(X)\) is minimal if and only if \(H_X\) is connected. This proves the structural bijection.

**4. Counting for even \(n\).** Let \(n=2p\) with \(p\geq2\). Each edge of \(H_X\) joins rim positions of equal parity. Connectedness therefore forces \(X\) to lie in one parity class. All opposite-parity positions are then absent, so the available edges of \(H_X\) are exactly consecutive edges around the \(p\)-vertex cyclic parity class. A nonempty connected subset is a proper cyclic interval of length \(k\) for some \(1\leq k<p\), or the entire class. There are \(p\) intervals for every such \(k\), plus one complete class, for each of the two parities. This gives \(M_{2p}=2(p(p-1)+1)=n(n-2)/2+2\). When \(p=2\), the cyclic parity class is interpreted as an ordinary two-vertex edge; the same count holds.

**5. Counting for odd \(n\).** The step-two successor \(i\mapsto i+2\pmod n\) traverses all rim indices in a single cycle. Since an edge \(i\leftrightarrow i+2\) in \(H_X\) requires its intermediate index \(i+1\notin X\), a connected \(X\) is a proper consecutive interval in the step-two cycle. An interval of size \(k\) is admissible exactly when its \(k-1\) intermediate rim indices avoid the \(k\) selected ones. This holds if and only if \(1\leq k\leq(n+1)/2\): the first possible coincidence between a selected step-two position and an intermediate one is a difference of \((n+1)/2\) steps modulo \(n\). Each admissible \(k\) has exactly \(n\) distinct choices of starting position; all resulting supports are distinct. Thus \(M_n=n(n+1)/2\) for odd \(n\), proving the theorem.

**6. Explicit lifting obstruction.** In \(C_6\), the set \(X=\{0,1,3,4\}\) is a fort: the outside vertices \(2,5\) each have two neighbors in \(X\). It is minimal: removing any one of \(0,1,3,4\) leaves an outside vertex with exactly one selected neighbor, and no two selected vertices form a fort (direct inspection of the six-cycle), so no proper subset is a fort. Its straightforward lift \(\widehat F=\{v_0,v_1,v_3,v_4,w_0,w_1,w_3,w_4\}\) is a fort. But \(B(\{1,3\})=\{v_1,v_3,w_0,w_1,w_3,w_4\}\) is a proper subset of \(\widehat F\) and a fort, as can be checked at all unselected rim and leaf vertices. Hence \(\widehat F\) is not minimal.

## Verification

Run the standalone `verify.py` with standard Python 3; `verification_output.txt` records the actual run. An implementation independent of the connectivity criterion enumerates **every nonempty vertex subset** of \(S_n\) for \(3\leq n\leq9\), applies the original neighborhood definition, extracts inclusion-minimal forts, and compares them with the canonical connected-support list. This exhausts 349,497 vertex subsets and gives counts \(6,6,15,14,28,26,45\). Separately, direct enumeration of all nonempty rim supports verifies the connected-support formula through \(n=18\), including the count \(146\). The six-cycle obstruction is checked against the original fort predicate and every proper subset of the proposed cycle fort.

The computations confirm finite cases only. Steps 1--5 are the proof for all orders; step 6 is independently checkable without relying on large enumeration.

## Relationship to prior work

Becker, Cameron, Hanely, Ong and Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963v1 (first public posting 9 April 2024), provide the fort definition, path/cycle results, a claimed lifting construction in Proposition 23, and an exponential lower bound for sunlets in Corollary 24. The present exact enumeration is neither implied by that lower bound nor by their cycle counts; the explicit six-cycle construction above conflicts with the lifting assertion as stated in that preprint. The contradiction is mathematical, not merely terminological: all sets are specified in the same corona graph and satisfy the original fort definition. A separate literature search found no existing complete sunlet minimal-fort enumeration or equivalent maximal-failed-zero-forcing classification. The pertinent complete Section 5.2, including the proof of Proposition 23, was read in the arXiv HTML rendering.

## Limitations

The result concerns only one-leaf sunlets and named minimal forts. It does not establish counts for general coronas, higher-leaf coronas, other zero forcing rules, or forts up to automorphism. Searches cannot rule out unpublished or unindexed equivalent work; the later journal wording of the cited claim was not verified against its full text. The complete enumeration is proved algebraically, not by the finite verifier. The assertion about the earlier preprint is restricted to the text of arXiv:2404.05963v1.

## References

1. P. Becker, T. R. Cameron, D. Hanely, B. Ong and J. P. Previte, *On the number of minimal forts of a graph*, arXiv:2404.05963v1, 9 April 2024, Sections 2 and 5.2; https://arxiv.org/html/2404.05963 .
2. L. Gomez, K. Rubi, J. Terrazas and D. A. Narayan, *All Graphs with a Failed Zero Forcing Number of Two*, Symmetry **13** (2021), 2221, https://doi.org/10.3390/sym13112221 (background for failed zero forcing).
