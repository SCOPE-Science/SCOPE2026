# A direct-sum fingerprint law and a sharp \(2143\) component–pattern covariance reversal

## Finding
Let \(\Pi_n\) be uniform among the \(n!\) permutations, let \(K_n\) count the components of its inversion graph, and let \(X_\tau\) count subsequences order-isomorphic to a fixed permutation pattern \(\tau\) of length \(m\), for all integers \(n\ge m\ge2\). Define the *direct-sum cut set* \(D(\tau)=\{j:1\le j<m,\ \{\tau(1),\ldots,\tau(j)\}=\{1,\ldots,j\}\}\). The exact covariance is

\[
\operatorname{Cov}(K_n,X_\tau)=\sum_{k=1}^{n-1}\frac{1}{\binom nk}
\sum_{j=1}^{m-1}\binom kj\binom{n-k}{m-j}
\left(\frac{\mathbf 1_{\{j\in D(\tau)\}}}{j!(m-j)!}-\frac1{m!}\right).
\]

In particular, the entire covariance depends on \(\tau\) only through \(D(\tau)\). For the natural pattern \(\tau=2143=21\oplus21\), whose inversion graph is two disjoint edges, write \(c_n=\operatorname{Cov}(K_n,X_{2143})\). Then

\[
c_n=\frac1{24}\sum_{k=1}^{n-1}\frac{5\binom{k}{2}\binom{n-k}{2}-\binom{k}{1}\binom{n-k}{3}-\binom{k}{3}\binom{n-k}{1}}{\binom nk}.
\]

**Sharp sign reversal:** \(c_n>0\) for exactly \(4\le n\le7\), whereas \(c_n<0\) for every \(n\ge8\); there are no zeros. Specifically \(c_4=1/72\), \(c_7=2/35\), and \(c_8=-1/840\).

## Assumptions and scope
All patterns are ordinary, non-consecutive permutation patterns, and every occurrence is indexed by an increasing list of positions. An inversion-graph edge joins the values of an inversion; connected components are precisely the indecomposable direct-sum blocks. No conditioning on the total number of inversions is imposed. Binomial coefficients with inadmissible lower indices vanish, and the covariance formula covers every integer \(n\ge m\ge2\). The exact sign assertion is solely for pattern \(2143\), \(n\ge4\).

## Proof
For each \(1\le k<n\) let \(J_k\) indicate \(\{\Pi_n(1),\ldots,\Pi_n(k)\}=\{1,\ldots,k\}\). Every direct-sum cut is a boundary between connected components of the inversion graph, whence \(K_n=1+\sum_{k=1}^{n-1}J_k\), and \(\mathbb P(J_k=1)=\binom nk^{-1}\).

Fix \(k\) and an \(m\)-position subsequence with \(j\) chosen positions in the first \(k\) slots and \(m-j\) in the last slots. For \(j=0,m\), conditioning on \(J_k=1\) leaves the pattern uniform, hence the covariance contribution is zero. When \(1\le j<m\), every selected left value is smaller than every selected right value under \(J_k=1\); conditional on this event the left and right relative patterns are independent and uniform. Thus the conditional probability of the full pattern \(\tau\) is \(\mathbf1_{\{j\in D(\tau)\}}/[j!(m-j)!]\), versus \(1/m!\) without the conditioning. There are \(\binom kj\binom{n-k}{m-j}\) such position selections. Multiplying the resulting conditional-minus-unconditional expectation by \(\mathbb P(J_k=1)\) and summing \(k\) proves the universal formula.

For \(2143\), the only proper direct-sum cut occurs at position \(j=2\), so the brackets at \(j=1,2,3\) are, respectively, \(-1/24,5/24,-1/24\), giving the specialized sum. Exact rational evaluations for \(4\le n\le39\), recorded by the accompanying verifier, establish positivity at \(4,5,6,7\) and strict negativity for \(8\le n\le39\).

To prove negativity for *every* \(n\ge40\), put \(A_k=\binom k1\binom{n-k}3\), \(B_k=\binom k2\binom{n-k}2\), \(C_k=\binom k3\binom{n-k}1\). Retain the negative contributions at \(k=1,n-1\), which total \(-D_n\), where \(D_n=(n-1)(n-2)(n-3)/(72n)\). Drop the remaining negative terms to bound

\[
c_n\le-D_n+\frac5{24}\sum_{k=2}^{n-2}\frac{B_k}{\binom nk}.
\]

At \(k=2,n-2\), the ratio is at most \(1\); at \(k=3,n-3\), it is at most \(9/n\). For \(4\le k\le n-4\), \(B_k\le n^4/64\) by \(k(n-k)\le n^2/4\), while \(\binom nk\ge\binom n4\), yielding \(B_k/\binom nk\le3n^3/[8(n-1)(n-2)(n-3)]<1/2\) for \(n\ge40\). Consequently

\[
c_n<-D_n+\frac5{24}\left(2+\frac{18}{n}+\frac{n-7}{2}\right)<-\frac{n^2}{100}+\frac{5n}{48}<0\qquad(n\ge40).
\]

Here \(D_n\ge n^2/100\) follows from \((1-1/n)(1-2/n)(1-3/n)\ge(39/40)(38/40)(37/40)>72/100\) for \(n\ge40\); the penultimate inequality uses \(2+18/n+(n-7)/2<n/2\) for \(n\ge40\). This completes the all-size sign proof.

## Verification
The accompanying self-contained `verify.py` uses exact rational arithmetic and independently enumerates uniform permutations for patterns of lengths two, three and four. It tests the general formula against direct enumeration for every such pattern through the coded range, and tests the \(2143\) signs for each integer \(4\le n\le39\). The infinite range is justified by the explicit inequalities in the proof, not by the finite computation. Run with `python3 verify.py` using only the Python standard library.

## Relationship to prior work
Acan and Pittel, *On the Connected Components of a Random Permutation Graph with a Given Number of Edges* (arXiv:1211.0246, publicly posted November 1, 2012), establish the direct-sum/graph-connectivity correspondence and analyze component counts conditioned on the inversion total; they do not establish the mixed moment with pattern occurrences. Janson, Nakamura and Zeilberger, *On the Asymptotic Statistics of the Number of Occurrences of Multiple Permutation Patterns* (arXiv:1312.3955, publicly posted December 13, 2013), analyze joint moments of **pattern-count variables**, not the number of direct-sum components. Atkinson, *Permutations which are the union of an increasing and a decreasing subsequence* (Electronic Journal of Combinatorics 5, R6, January 10, 1998), concerns the natural role of pattern \(2143\) in skew-merged pattern avoidance, not this covariance. These statements can coexist; neither the known component law nor known pattern-to-pattern covariance yields the cross-statistic formula without a new mixed calculation. A stronger general combinatorial moment identity elsewhere could imply it; historical priority is not certified.

## Limitations
The theorem concerns uniform permutations and ordinary patterns only, not Mallows laws or contiguous-pattern occurrences. The finite verification is not itself a proof for infinite \(n\), and the non-computational inequality handles the infinite tail. The comparison literature was not exhaustive, particularly older literature on decomposition-weighted pattern enumeration; claims of absolute historical originality require further independent checking. No independent audit has been performed.

## References
1. M. D. Atkinson, *Permutations which are the union of an increasing and a decreasing subsequence*, Electronic Journal of Combinatorics 5 (1998), R6, https://doi.org/10.37236/1344 (public January 10, 1998).
2. H. Acan and B. Pittel, *On the Connected Components of a Random Permutation Graph with a Given Number of Edges*, https://arxiv.org/abs/1211.0246 (public November 1, 2012).
3. S. Janson, B. Nakamura and D. Zeilberger, *On the Asymptotic Statistics of the Number of Occurrences of Multiple Permutation Patterns*, https://arxiv.org/abs/1312.3955 (public December 13, 2013).
