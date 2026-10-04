# Labeled enumeration and asymptotic rarity of finite polymorphism-homogeneous monounary algebras
## Finding
Let \(a_n\) be the number of unary functions \(f:[n]\to[n]\) for which the finite monounary algebra \(([n],f)\) is polymorphism-homogeneous. Define formal power series
\[
T_0(z)=z,\qquad T_h(z)=z\bigl(\exp(T_{h-1}(z))-1\bigr)\quad(h\ge1),
\]
and
\[
F_h(z)=\frac{1}{1-z\exp(T_{h-1}(z))}\quad(h\ge1),\qquad P(z)=\frac1{1-z}.
\]
Then the exponential generating function of the labeled polymorphism-homogeneous monounary algebras is the coefficientwise locally finite series
\[
A(z)=P(z)+\sum_{h\ge1}\bigl(F_h(z)-P(z)\bigr),
\qquad
A(z)=\sum_{n\ge0}a_n\frac{z^n}{n!}.
\]
The first positive-order values are
\[
1,4,27,232,2285,25716,324583,4571904,71321769,1225291780.
\]
If \(\rho=W(1)=0.567143290409\ldots\) is the positive solution of \(\rho e^\rho=1\), then
\[
a_n\sim \frac{n!}{1+\rho}\rho^{-n}.
\]
Consequently the proportion among all \(n^n\) unary operations satisfies
\[
\frac{a_n}{n^n}\sim
\frac{\sqrt{2\pi n}}{1+\rho}(e\rho)^{-n},
\]
so polymorphism-homogeneity is exponentially rare among labeled finite monounary algebras.

## Assumptions and scope
A monounary algebra is a finite set equipped with one unary operation. A source is an element outside \(f(A)\), and the height of an element is its distance under forward iteration to the cyclic part of its functional digraph. The input classification is Theorem 4.9 of Tóth--Waldhauser, which states for finite monounary algebras that polymorphism-homogeneity is equivalent to having no sources or having all sources at the same height. The enumerative formulas and asymptotic statement above are the new claims established here.

The count is labeled: two different maps \([n]\to[n]\) are counted separately even when the corresponding monounary algebras are isomorphic. No claim is made here about the number of isomorphism types.

## Proof
Represent a unary operation by its functional digraph. Every weak component consists of a directed cycle with rooted in-trees attached to the cycle vertices. A source is exactly a leaf of one of those attached in-trees. If the common source height is \(h\ge1\), every such leaf is at distance exactly \(h\) from its cycle.

For a rooted attached tree whose root is not a cycle vertex, let \(T_h\) encode the labeled trees in which every leaf is exactly \(h\) levels below the root. For \(h=0\) the root is itself the leaf, giving \(T_0(z)=z\). For \(h\ge1\), the root must have a nonempty labeled set of children, each carrying a \(T_{h-1}\)-tree. The exponential formula therefore gives
\[
T_h(z)=z\bigl(\exp(T_{h-1}(z))-1\bigr).
\]

A cycle vertex is different: even if it has no attached child, it is not a source because it has a predecessor on the cycle. Hence a cycle vertex may carry an arbitrary labeled set of \(T_{h-1}\)-trees, with decoration series
\[
D_h(z)=z\exp(T_{h-1}(z)).
\]
A functional digraph is a labeled set of directed cycles of such decorated vertices. The labeled species identity \(\mathrm{SET}(\mathrm{CYC}(D_h))\) yields
\[
F_h(z)=\exp\!\left(\sum_{k\ge1}\frac{D_h(z)^k}{k}\right)
=\frac{1}{1-D_h(z)}
=\frac{1}{1-z\exp(T_{h-1}(z))}.
\]
This class includes all permutations, because every cycle vertex may choose the empty attached set. The permutations have exponential generating function \(P(z)=1/(1-z)\). A nonbijective finite unary map has at least one source, and if it is polymorphism-homogeneous then its common positive source height is unique. Therefore the classes \(F_h-P\) are disjoint for distinct \(h\), giving
\[
A(z)=P(z)+\sum_{h\ge1}(F_h(z)-P(z)).
\]
This infinite sum is coefficientwise well defined: a nonpermutation with common source height \(h\) needs at least \(h+1\) vertices, so the coefficient of \(z^n\) receives contributions only from \(h<n\).

For the asymptotic, \(F_1(z)=1/(1-ze^z)\). Its smallest-modulus singularity is the unique positive \(\rho\) satisfying \(\rho e^\rho=1\): if \(|z|<\rho\), then \(|ze^z|\le |z|e^{|z|}<1\), and equality on \(|z|=\rho\) forces \(z=\rho\). The pole is simple, with local principal part
\[
F_1(z)=\frac{1}{1+\rho}\frac{1}{1-z/\rho}+O(1).
\]
Thus \([z^n]F_1(z)\sim \rho^{-n}/(1+\rho)\).

It remains to bound all \(h\ge2\) uniformly away from \(\rho\). Take \(r=0.58\). Put \(b_0=r\) and \(b_j=r(e^{b_{j-1}}-1)\). Numerically \(b_1=0.4559022898\ldots<r\), so \(b_j\) decreases for \(j\ge1\). Positive coefficients imply \(|T_j(z)|\le b_j\) on \(|z|\le r\). Hence, for \(h\ge2\),
\[
|z\exp(T_{h-1}(z))|\le r\exp(b_1)=0.9150057902\ldots<1.
\]
All \(F_h\) with \(h\ge2\) are therefore uniformly bounded and analytic on \(|z|\le r\). At coefficient \(n\) there are at most \(n-1\) nonzero height terms, so their total contribution is \(O(nr^{-n})=o(\rho^{-n})\). This proves the stated asymptotic. Stirling's formula gives the proportion among all \(n^n\) unary maps.

## Verification
The accompanying `verify.py` independently computes the formal-series coefficients through order ten and brute-forces every unary map on sets of sizes one through seven. The two methods agree exactly, including the decomposition by common source height. It also checks the numerical inequalities used in the analytic separation of the \(h=1\) pole from all \(h\ge2\) strata.

The brute-force totals for sizes one through seven are
\[
1,4,27,232,2285,25716,324583.
\]
The formal-series computation continues with
\[
4571904,71321769,1225291780
\]
for sizes eight through ten.

## Relationship to prior work
Tóth and Waldhauser restate and reprove the classification that a finite monounary algebra is polymorphism-homogeneous exactly when it has no sources or all sources have the same height. Their paper gives this as Theorem 4.9 and attributes the classification to Farkasová and Jakubíková-Studenovská. The earlier paper classifies the structures but, in the sources inspected for this work, does not give a labeled enumeration, an exponential generating function, or the asymptotic density among all unary operations.

The present argument turns the source-height classification into a functional-digraph species decomposition. Literature and database searches were also made for enumeration of unary maps with all sources at the same distance from a cycle, and for the resulting initial sequence; no matching enumeration was located. Related enumerative literature on rooted trees with all leaves on constrained levels concerns a component of the construction rather than this functional-digraph class.

## Limitations
The originality search cannot rule out an equivalent enumeration under an unrelated functional-digraph terminology. In particular, balanced or level-constrained rooted-tree enumeration is a neighboring subject, so the residual risk is an unnoticed reformulation in enumerative-combinatorics literature. The asymptotic proof uses only the labeled model; no unlabeled asymptotic is claimed.

## References
1. E. Tóth and T. Waldhauser, “Polymorphism-homogeneity and universal algebraic geometry,” Discrete Mathematics & Theoretical Computer Science 23:2 (2022), arXiv:2007.04405. The first arXiv version was submitted 8 July 2020. Primary MSC 03C07.
2. Z. Farkasová and D. Jakubíková-Studenovská, “Polymorphism-Homogeneous Monounary Algebras,” Mathematica Slovaca 65 (2015), 359–370, DOI 10.1515/ms-2015-0028.
