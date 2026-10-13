# Signed double Roman \(k\)-domination of crown graphs
## Finding
For \(n\ge 3\), let \(\operatorname{Cr}_n=K_{n,n}-M_n\), where the deleted perfect matching is \(M_n=\{a_i b_i:1\le i\le n\}\). A signed double Roman \(k\)-dominating function is a map \(f:V(\operatorname{Cr}_n)\to\{-1,1,2,3\}\) such that every closed-neighborhood sum is at least \(k\), every vertex labeled \(-1\) has either a neighbor labeled \(3\) or two neighbors labeled \(2\), and every vertex labeled \(1\) has a neighbor labeled at least \(2\).

For every positive integer \(k\), such a function exists if and only if \(1\le k\le 3n\). In that range,
\[
\gamma_{\mathrm{sdR}}^k(\operatorname{Cr}_n)=
\begin{cases}
2k+2,&(n,k)\in\{(3,2),(4,1)\},\\
2k,&\text{otherwise}.
\end{cases}
\]
Thus the regular lower bound is attained for every admissible parameter pair except exactly two small cases.

## Assumptions and scope
All graphs are finite and simple. The integer \(n\) satisfies \(n\ge3\), and \(k\) is a positive integer. The crown graph has bipartition \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\), with all cross-edges except \(a_i b_i\). The claim concerns the signed double Roman \(k\)-domination number as defined by Amjadi et al. and used by Henning and Volkmann.

If \(k>3n\), no admissible function exists because every closed neighborhood has exactly \(n\) vertices and every label is at most \(3\). The formula below therefore concerns exactly the full existence range \(1\le k\le3n\).

## Proof
Write \(x_i=f(a_i)\), \(y_i=f(b_i)\), \(X=\sum_i x_i\), \(Y=\sum_i y_i\), and \(W=X+Y\). Since \(\operatorname{Cr}_n\) is \((n-1)\)-regular, each vertex belongs to exactly \(n\) closed neighborhoods. Summing the \(2n\) closed-neighborhood inequalities gives
\[
nW=\sum_{v\in V}\sum_{u\in N[v]}f(u)\ge2nk,
\]
so every signed double Roman \(k\)-dominating function has \(W\ge2k\).

Suppose first that \(W=2k\). Equality must then hold in every closed-neighborhood inequality. For each \(i\),
\[
x_i+Y-y_i=k,\qquad y_i+X-x_i=k.
\]
Hence \(x_i-y_i=X-k=k-Y\) is independent of \(i\). Calling this common difference \(c\), summing over \(i\) gives \(X-Y=nc\), while the two displayed identities give \(X-Y=2c\). Since \(n\ge3\), it follows that \(c=0\). Therefore
\[
x_i=y_i=:z_i\quad\text{for every }i,\qquad \sum_{i=1}^n z_i=k.
\]
Conversely, any duplicated label vector \((z_1,\ldots,z_n)\) of sum \(k\) makes every closed-neighborhood sum equal to \(k\). Its rescue conditions reduce to two global conditions: if a label \(-1\) occurs, then the vector contains either a label \(3\) or at least two labels \(2\); if a label \(1\) occurs, then the vector contains a label \(2\) or \(3\).

Let \(u_{-},u_1,u_2,u_3\) be the numbers of labels \(-1,1,2,3\). The size and sum conditions are equivalent to
\[
u_-+u_1+u_2+u_3=n,\qquad 2u_1+3u_2+4u_3=n+k.
\]
For \(1\le k\le n\), if \(n\) and \(k\) have the same parity, take
\[
u_3=1,\quad u_2=0,\quad u_1=\frac{n+k-4}{2},\quad u_-=n-u_1-1.
\]
If they have opposite parity, take
\[
u_3=1,\quad u_2=1,\quad u_1=\frac{n+k-7}{2},\quad u_-=n-u_1-2.
\]
The second construction is valid whenever \(n+k\ge7\). Together these cover every \(1\le k\le n\) except \((n,k)=(3,2)\) and \((4,1)\). For \(n<k\le3n\), put \(q=k-n\), and take
\[
u_-=0,\quad u_3=\left\lfloor\frac q2\right\rfloor,\quad u_2=q-2u_3,\quad u_1=n-u_2-u_3.
\]
This has sum \(k\) and satisfies the rescue condition because \(q\ge1\). Thus weight \(2k\) is attained for every nonexceptional admissible pair.

For either exceptional pair, \(n+k=5\). The equation \(2u_1+3u_2+4u_3=5\) has only the nonnegative solution \(u_1=u_2=1\), \(u_3=0\). It leaves at least one label \(-1\), but provides only one label \(2\) and no label \(3\), so the \(-1\) rescue condition fails. Hence weight \(2k\) is impossible.

It remains to exclude weight \(2k+1\) in the two exceptional cases. If \(W=2k+1\), define
\[
s_i=x_i+Y-y_i,\qquad t_i=y_i+X-x_i.
\]
Then \(s_i+t_i=2k+1\) and \(s_i,t_i\ge k\), so \(s_i-t_i\in\{-1,1\}\). Put \(C=Y-X\), and let \(r\) be the number of indices with \(s_i-t_i=1\). Since
\[
s_i-t_i=2(x_i-y_i)+C,
\]
summing gives
\[
2r-n=(n-2)C.
\]
For \((n,k)=(4,1)\), swapping the two shores if necessary yields \(C=1\), hence \(X=1\), \(Y=2\), and \(r=3\). Three matched pairs must have equal labels and the fourth has \(x_i-y_i=-1\), so that exceptional pair is either \((1,2)\) or \((2,3)\). In the first case the three equal labels must be \(-1,-1,2\); in the second they must be \(-1,-1,1\). In either case, a \(-1\)-labeled vertex on the \(B\)-shore sees exactly one label \(2\) and no label \(3\) among its neighbors, contradicting the rescue condition.

For \((n,k)=(3,2)\), after swapping shores if needed, \(C\in\{1,3\}\). If \(C=3\), then all three differences satisfy \(x_i-y_i=-1\), forcing every \(x_i\ge1\), contrary to \(X=1\). If \(C=1\), then two pairs have equal labels and one has difference \(-1\). If that pair is \((1,2)\), the two equal labels must be \(-1,2\); if it is \((2,3)\), they must be \(-1,1\). Again a \(-1\)-labeled vertex has only one neighboring label \(2\) and no neighboring label \(3\), a contradiction.

Finally, the duplicated vectors \((-1,1,3)\) for \((n,k)=(3,2)\) and \((-1,-1,1,3)\) for \((n,k)=(4,1)\) have respective weights \(6=2k+2\) and \(4=2k+2\), satisfy all rescue conditions, and have every closed-neighborhood sum at least \(k\). This proves the formula.

## Verification
A standalone verifier exhaustively checks every labeling in \(\{-1,1,2,3\}^{2n}\) for \(n=3,4,5\), computes feasibility directly from the defining rescue conditions and closed-neighborhood sums, and compares the resulting minima for every \(1\le k\le3n\) with the theorem. It also checks the explicit constructions above for every \(3\le n\le40\) and every admissible \(k\), including the two exceptional witnesses. The finite computation is a stress test only; the arbitrary-\(n\) conclusion follows from the proof.

## Relationship to prior work
Henning and Volkmann determine the same invariant for balanced complete bipartite graphs. In particular, for \(k\ge2\) and \(p\ge k+1\), they prove
\[
\gamma_{\mathrm{sdR}}^k(K_{p,p})=2k+2.
\]
The crown graph is obtained from \(K_{n,n}\) by deleting one perfect matching, but the cited balanced-biclique theorem does not cover this deletion. The present result shows that the deletion makes the regular lower bound \(2k\) sharp throughout almost the entire existence range, with only two small exceptions. The foundational 2018 paper also treats complete bipartite graphs but not this matching-deleted family in the inspected text.

Targeted searches used the aliases “crown graph”, “complete bipartite minus a perfect matching”, “matching-deleted complete bipartite”, and “bipartite Kneser \(H(n,1)\)”, together with the exact invariant name and notation. No covering statement was located. A residual risk remains that an equivalent result is indexed under a different alias or appears in literature not surfaced by those searches.

## Limitations
The originality conclusion is a literature comparison, not a proof that no equivalent statement exists anywhere. The earliest verified public date used for the recent literature lead is the publisher's publication date, \(2025\)-\(07\)-\(21\); no earlier public version was located in the searches performed. The verification script checks only finite orders and is not used as a substitute for the analytic proof.

## References
1. M. A. Henning and L. Volkmann, “More results on the signed double Roman \(k\)-domination in graphs,” Aequationes Mathematicae 99 (2025), 1903–1921. DOI: 10.1007/s00010-025-01192-3.
2. J. Amjadi, H. Yang, S. Nazari-Moghaddam, S. M. Sheikholeslami, and Z. Shao, “Signed double Roman \(k\)-domination in graphs,” Australasian Journal of Combinatorics 72(1) (2018), 82–105.
