# Exact labeled age enumerator for a weak-amalgamation forest class

## Finding
Let \(\mathcal G\) be the class of finite acyclic undirected graphs in which no two vertices of degree greater than \(2\) are adjacent. Krawczyk, Kruckman, Kubiś, and Panagiotopoulos use exactly this class as a hereditary JEP example with WAP but not CAP. The whole labeled age has an exact two-state species description.

Let \(L(x)\) be the exponential generating function (EGF) of planted admissible trees whose root has total degree at most \(2\) after the external parent edge is counted, and let \(H(x)\) be the EGF of planted admissible trees whose root has total degree greater than \(2\). Then
\[
L=x(1+L+H),\qquad H=x(e^L-1-L).
\]
If \(P=L+H\), define
\[
T^\bullet=x\left(1+P+\frac{P^2}{2}\right)
+x\left(e^L-1-L-\frac{L^2}{2}\right),
\]
and
\[
U=T^\bullet-\frac{L^2}{2}-LH.
\]
Then \(U\) is the EGF of connected members of \(\mathcal G\), and the EGF of all labeled members is
\[
\boxed{F(x)=e^{U(x)}}.
\]
Equivalently, eliminating \(H\) gives the single implicit equation
\[
L=x(1+L)+x^2(e^L-1-L),
\]
followed by the displayed formulas for \(U\) and \(F\).

The connected labeled counts \(n! [x^n]U(x)\) for \(n=1,\ldots,12\) are
\[
1,1,3,16,125,1206,13867,188504,2972097,53238250,1067540771,23711808132,
\]
and the labeled forest counts \(n![x^n]F(x)\) for \(n=0,\ldots,12\) are
\[
1,1,2,7,38,291,2842,33391,459748,7288273,130922666,2629437009,58418631196.
\]

## Assumptions and scope
Graphs are finite, simple, undirected, and labeled on a fixed \(n\)-element vertex set. “High” means degree greater than \(2\); “low” means degree at most \(2\). The count is for the exact hereditary age \(\mathcal G\), not for isomorphism classes and not for the generic limit's automorphism orbits. The EGF system is formal-power-series algebra, so no analytic convergence assumption is needed.

## Proof
Cut a rooted tree at the edge to its external parent. If the planted root is low, its parent already consumes one incident edge, so it has at most one child. That child may be either low or high. Hence
\[
L=x(1+L+H).
\]
If the planted root is high, it must have at least two children in addition to its parent. Since high vertices may not be adjacent, every child must be low. The children form an unordered labeled set, giving
\[
H=x\,\mathrm{SET}_{\ge2}(L)=x(e^L-1-L).
\]

For a tree rooted at an actual vertex there is no parent edge. A low root has at most two arbitrary planted children, contributing
\[
x\left(1+P+\frac{P^2}{2}\right),\qquad P=L+H.
\]
A high root has at least three children, all low, contributing
\[
x\left(e^L-1-L-\frac{L^2}{2}\right).
\]
Their sum is \(T^\bullet\).

Now root an admissible tree at an undirected edge and cut that edge. The two planted endpoint states may be low-low or low-high, but never high-high, so the edge-rooted EGF is
\[
T^- = \frac{L^2}{2}+LH.
\]
For an oriented edge, the allowed ordered state pairs are low-low, low-high, and high-low, so
\[
T^\rightarrow=L^2+2LH.
\]
The standard tree dissymmetry identity
\[
T+T^\rightarrow=T^\bullet+T^-
\]
therefore gives
\[
U=T=T^\bullet-\frac{L^2}{2}-LH.
\]
Finally, every member of \(\mathcal G\) is a labeled set of connected admissible trees. The labeled SET construction gives \(F=e^U\).

## Verification
The attached `verify.py` performs exact rational formal-power-series arithmetic through order \(12\), reconstructs \(L,H,U,F\), and checks every displayed coefficient. It then verifies the connected counts independently by enumerating every Prüfer code through \(n=7\), and verifies the forest counts independently by enumerating every simple labeled graph through \(n=6\), rejecting cycles and any edge whose two endpoints both have degree greater than \(2\). The replay prints `VERIFY_OK`.

## Relationship to prior work
Krawczyk–Kruckman–Kubiś–Panagiotopoulos introduce \(\mathcal G\) as a weak Fraïssé class and prove WAP while CAP fails; their Section 3.3 specifies exactly the local graph condition used here. Their paper does not state the labeled age EGF above. The retained contribution is the exact global enumeration obtained by resolving the parent-edge degree state and applying tree dissymmetry.

Searches for the defining phrase, for “branching vertices form an independent set,” and for the initial connected and forest coefficient strings did not locate an equivalent generating-function formula. There is residual terminology risk because related trees occur in chemical-graph and spectral-graph literature under specialized names, but the exact sequences also produced no matching enumerator in the searches performed.

## Limitations
The result is an exact labeled enumeration, not an asymptotic analysis. It does not enumerate unlabeled isomorphism types. The originality conclusion is search-bounded: an equivalent species derivation could exist under terminology not captured by the defining phrase or coefficient searches.

## References
1. A. Krawczyk, A. Kruckman, W. Kubiś, A. Panagiotopoulos, “Examples of weak amalgamation classes,” arXiv:1907.09577; *Mathematical Logic Quarterly* 68 (2022), 178–188, DOI 10.1002/malq.202100037.
2. Standard labeled-species dissymmetry for trees: the identity used here is \(T+T^\rightarrow=T^\bullet+T^-\); the proof above specializes it completely to this two-state class.
