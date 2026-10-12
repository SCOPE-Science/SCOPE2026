# Global Italian domination of crown graphs
## Finding
For every integer \(n\ge5\), let \(\operatorname{Cr}_n=K_{n,n}-M\) be the crown graph with bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), and deleted matching \(M=\{a_i b_i:1\le i\le n\}\). Then
\[
\gamma_{gI}(\operatorname{Cr}_n)=4.
\]
Every minimum function is exactly one of the following: choose one index \(i\) and put \(f(a_i)=f(b_i)=2\), or choose two distinct indices \(i,j\) and put \(f(a_i)=f(b_i)=f(a_j)=f(b_j)=1\); all other labels are zero. Therefore the number of minima is
\[
n+\binom n2=\frac{n(n+1)}2.
\]

## Assumptions and scope
An Italian dominating function is a map \(f:V(G)\to\{0,1,2\}\) such that each zero-labeled vertex \(v\) satisfies \(\sum_{u\in N_G(v)}f(u)\ge2\). A global Italian dominating function satisfies this condition on both \(G\) and \(\overline G\). The theorem is stated for \(n\ge5\). The cubic boundary \(\operatorname{Cr}_4\) has the same pattern by direct verification but is not part of the claim.

## Proof
Write \(x_i=f(a_i)\), \(y_i=f(b_i)\), \(X=\sum_i x_i\), and \(Y=\sum_i y_i\). If \(x_i=0\), then the crown condition and complement condition give
\[
Y-y_i\ge2,\qquad X+y_i\ge2.
\]
If \(y_i=0\), similarly
\[
X-x_i\ge2,\qquad Y+x_i\ge2.
\]
Suppose the weight is at most \(3\). If some matched pair is doubly zero, then \(X\ge2\) and \(Y\ge2\), contradiction. If no pair is doubly zero, every one of the \(n\ge5\) pairs contributes at least one unit, again a contradiction. Hence the weight is at least \(4\).

Now suppose the weight is \(4\). Since \(n\ge5\), some pair is doubly zero, so the preceding inequalities force \(X=Y=2\). If \(x_i=0\), then \(2-y_i\ge2\), hence \(y_i=0\); symmetrically, \(y_i=0\) implies \(x_i=0\). Thus the positive supports on the two sides use the same indices. A positive support of size one forces labels \(2,2\); a support of size two forces labels \(1,1\) on both matched pairs; larger support is impossible because each side sums to \(2\). Both displayed types directly satisfy the Italian condition in the crown graph and its complement, proving the theorem and the count.

## Verification
The included checker exhaustively tests all ternary labelings for \(n=4,5,6\), totaling \(597{,}051\) labelings. It finds value \(4\) and exactly \(15\) minima for \(n=5\) and \(21\) for \(n=6\), matching the theorem. It also directly verifies every predicted minimum function for \(4\le n\le50\).

## Relationship to prior work
Hao, Hu, Wei, and Xu introduced global Italian domination in a paper published online on 4 September 2018; the publisher metadata lists MSC 05C69. Its accessible abstract emphasizes general bounds and tree comparisons. A 2024 survey identifies the same invariant as global Roman \(\{2\}\)-domination and summarizes the initiating work through those tree results. A 2026 follow-up emphasizes relations with Italian domination and, in particular, cubic graphs. The claimed crowns have degree \(n-1\ge4\), so that cubic specialization does not subsume the theorem. Targeted searches under global Italian/global Roman \(\{2\}\), crown graph, and complete-bipartite-minus-perfect-matching aliases found no equivalent crown statement.

## Limitations
Only the minimum layer is classified; the full weight enumerator is not determined. The initiating paper's full text was not accessible through the inspected public routes, leaving a residual literature risk despite targeted searches and the later survey comparison. Finite enumeration is corroborative only; the arbitrary-order result follows from the side-sum proof.

## References
1. G. Hao, K. Hu, S. Wei, Z. Xu, “Global Italian domination in graphs,” Quaestiones Mathematicae 42(8) (2019), 1101–1115, DOI 10.2989/16073606.2018.1506831; published online 4 September 2018.
2. “Survey on Roman \(\{2\}\)-Domination,” Mathematics 12(17) (2024), article 2771, DOI 10.3390/math12172771.
3. G. Hao, Z. Xie, Y. Wu, S. M. Sheikholeslami, “On the global Italian domination of graphs,” Communications in Combinatorics and Optimization 11(4) (2026), 1141–1155, DOI 10.22049/cco.2025.30937.2670.
