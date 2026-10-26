# One-site localization of marked-cycle-length dependence in permutation descents

## Finding

Let \(n\ge3\), and let \(\Pi\) be uniform among permutations of \(\{1,\ldots,n\}\). Denote by \(K\) the length of the cycle containing the distinguished symbol \(1\), and by
\[
D_i=\mathbf 1\{\Pi(i)>\Pi(i+1)\},\qquad 1\le i<n,
\]
the ordinary one-line descent indicators. Then **every \(D_i\) with \(2\le i<n\) is individually independent of \(K\)**, with
\[
\Pr(D_i=1\mid K=k)=\tfrac12,\qquad 2\le i<n,\quad1\le k\le n.
\]
The first descent is the only exception. Its complete conditional law is
\[
\boxed{
\Pr(D_1=1\mid K=k)=q_{n,k}=\begin{cases}
0,& k=1,\\
\dfrac{n+1}{2(n-1)},& k=2,\\
\dfrac{n}{2(n-1)},& 3\le k\le n-1,\\
\dfrac12,& k=n.
\end{cases}}
\]
The middle line's range is empty when \(n=3\). In particular, for every \(n\ge4\) all intermediate marked cycle lengths between \(3\) and \(n-1\) have *identical first-descent probabilities*, although the event that vertex \(1\) has a fixed point forces the first descent to vanish.

Writing \(D=\sum_{i=1}^{n-1}D_i\), it follows that
\[
\mathbb E[D\mid K=k]=\frac{n-2}{2}+q_{n,k},
\]
and
\[
\boxed{\operatorname{Cov}(K,D)
=\operatorname{Cov}(K,D_1)
=\frac{n^2-3n+4}{4n(n-1)}>0.}
\]
Thus the covariance is concentrated at the first position, and it tends to \(1/4\) as \(n\to\infty\). The statement concerns independence of **individual indicators** only; it does not assert independence of the entire vector \((D_2,\ldots,D_{n-1})\) from \(K\).

## Assumptions and scope

A permutation is viewed simultaneously as a bijection and as its one-line word \(\Pi(1)\cdots\Pi(n)\). The marked cycle is the orbit of \(1\) under iteration of \(\Pi\); a descent is a comparison of images at adjacent **positions**, not a descent in standardized cycle notation. Uniformity on the full symmetric group is essential. The theorem holds exactly for all integers \(n\ge3\) and all allowable \(k\), without asymptotic assumptions. The excluded case \(n=2\) has a degenerate full two-cycle and does not satisfy the displayed final line of the conditional formula.

## Proof

**Marked-cycle sampling.** For any \(1\le k\le n\), choose \(k-1\) of the \(n-1\) other symbols, arrange these with \(1\) as a uniformly oriented \(k\)-cycle, then uniformly permute the \(n-k\) remaining symbols. The number of such permutations equals
\[
\binom{n-1}{k-1}(k-1)!(n-k)!=(n-1)!,
\]
so \(K\) is uniform on \(\{1,\ldots,n\}\). This sampling rule also holds conditionally on a specified marked-cycle symbol set.

**Unchanged interior descent probabilities.** Fix \(2\le i<n\) and put \(a=i\), \(b=i+1\). Let \(\tau\) exchange \(a\) and \(b\), leaving all other symbols unchanged. Conjugation \(\Pi\mapsto\tau\Pi\tau\) preserves the uniform law conditional on each \(K=k\), because \(\tau(1)=1\). Put \(X=\Pi(a)\), \(Y=\Pi(b)\). The conjugate has images \((\tau(Y),\tau(X))\) at positions \((a,b)\).

Because \(a,b\) are consecutive integer labels and \(X\ne Y\), the original comparison \(X>Y\) and the conjugated comparison \(\tau(Y)>\tau(X)\) are complementary unless \(\{X,Y\}=\{a,b\}\). For the two exceptional ordered pairs, \((X,Y)=(a,b)\) contributes two non-descents to the involution average, while \((X,Y)=(b,a)\) contributes two descents. Hence the exact identity
\[
\Pr(D_i=1\mid K=k)-\tfrac12
=\frac12\bigl[\Pr(\Pi(a)=b,\Pi(b)=a\mid K=k)
-\Pr(\Pi(a)=a,\Pi(b)=b\mid K=k)\bigr].
\]
The exceptional probabilities are equal: if \(a,b\) are both outside the marked cycle, the complementary permutation is uniform, so the two specified-image events have the same probability; if either lies in the marked cycle, neither event can occur. Indeed, the marked cycle contains \(1\), hence cannot be a two-cycle on \(\{a,b\}\); and no symbol in a nontrivial marked cycle can be fixed. This proves the \(1/2\) conditional law for every interior index. As \(D_i\) is Bernoulli, its conditional law is its full law, proving individual independence of \(K\) and \(D_i\).

**First position.** When \(K=1\), \(\Pi(1)=1\) and \(D_1=0\). For \(K=k\ge2\), put \(A=\Pi(1)\), \(B=\Pi(2)\). The first marked-cycle successor \(A\) is uniform on \(\{2,\ldots,n\}\). If \(A=2\), then \(D_1=1\) exactly when \(k=2\): in that case \(B=1\), whereas for \(k\ge3\) its successor \(B\) exceeds \(2\).

Suppose now that \(A>2\), which has probability \((n-2)/(n-1)\). Symmetry under relabeling the symbols \(3,\ldots,n\), fixing \(1,2\), makes the two possible orders of \(A,B\) equiprobable conditional on \(B>2\). Thus
\[
\Pr(A>B\mid A>2,K=k)
=\frac12+\frac12\Pr(B\in\{1,2\}\mid A>2,K=k).
\]
For \(k=2\), the symbol \(2\) lies outside the marked cycle, and the uniform complementary permutation gives
\[
\Pr(B=2\mid A>2,K=2)=\frac1{n-2},\qquad
\Pr(B=1\mid A>2,K=2)=0.
\]
For \(k\ge3\), conditioned on \(A>2\), the symbol \(2\) belongs to the marked cycle with probability \((k-2)/(n-2)\). When it does, it is the predecessor of \(1\) with probability \(1/(k-2)\). Consequently
\[
\Pr(B=1\mid A>2,K=k)=\frac1{n-2}.
\]
If \(3\le k<n\), the symbol \(2\) is outside the marked cycle with probability \((n-k)/(n-2)\), and its image in the independent uniform complement is \(2\) with probability \(1/(n-k)\). Hence
\[
\Pr(B=2\mid A>2,K=k)=\frac1{n-2}\qquad(3\le k<n).
\]
At \(k=n\), there is no complement and this last probability is zero. Combining the four cases with \(\Pr(A=2)=1/(n-1)\) gives the displayed piecewise formula for \(q_{n,k}\).

**Total covariance.** Summation of the indicator identities gives \(\mathbb E[D\mid K=k]=(n-2)/2+q_{n,k}\). Since \(K\) is uniform and each ordinary descent has unconditional probability \(1/2\), the law of total covariance yields
\[
\operatorname{Cov}(K,D)
=\frac1n\sum_{k=1}^n\left(k-\frac{n+1}{2}\right)q_{n,k}
=\frac{n^2-3n+4}{4n(n-1)}.
\]
The same computation applies to \(D_1\), since every other indicator is independent of \(K\). Positivity follows from \(n^2-3n+4=(n-3/2)^2+7/4>0\).

## Verification

The standalone Python 3 program `verify.py` uses only the standard library. Run `python3 verify.py` in a directory containing that file. It exhaustively enumerates all permutations for \(3\le n\le9\), computes \(K\) directly by iterating the orbit of symbol \(1\), and compares the exact rational conditional descent probabilities, conditional expected number of descents, uniform marked-cycle length counts, and covariance against the stated formulas. It reports `VERIFICATION_OK 336` after 336 exact rational and counting assertions. These finite tests detect implementation or formula mistakes on small cases; the unrestricted statement follows from the preceding involution and cycle-decomposition proof.

## Relationship to prior work

Classical work of Reutenauer and Gessel–Reutenauer counts permutations with a given **unmarked cycle type** and a descent set. Diaconis, McGrath, and Pitman, and Fulman, develop related results for riffle shuffles and cycle statistics. Gessel and Zhuang later give generating functions jointly refining descent statistics and unmarked cycle type. These results provide the principal literature context, but a cycle type does not identify which cycle contains the smallest distinguished label; its conditional association with a *position-specific* descent is not obtained merely by summing over cycle types.

A published position-resolved fixed-point/descent covariance theorem gives the \(K=1\) slice of the interior independence law but not the \(K=2,\ldots,n\) marked-cycle-length classification. Another published inversion/cycle-count law concerns the total number of cycles rather than the length of the cycle containing \(1\). Neither statement implies the four-regime first-position law. Elizalde and Troyka (2017, Corollary 4.2) prove the considerably stronger **complete descent-set** law for a single cycle on its first \(n-2\) descent positions. This already includes the \(K=n\) portion of the later-indicator statement in that range; the present theorem does **not** claim that slice as new. The proposed new contribution is uniform conditioning over all intermediate marked-cycle lengths \(2\le K<n\), the four-regime first-site profile, and the exact localization of total covariance. The present finding is a marked-cycle probabilistic refinement, not a claim to have discovered Eulerian numbers or cycle-type generating functions.

## Limitations

The theorem does not claim joint independence of the vector of all later descent indicators from \(K\); their higher-order joint law may depend on the marked cycle. The result is specific to the uniform permutation, the special symbol \(1\), and ordinary adjacent comparisons. Conjugation-invariant cycle-type enumeration is more general in another direction, and an equivalent marked-cycle formulation in older literature cannot be ruled out without broader historical inspection. The 1995 Diaconis–McGrath–Pitman full text remained inaccessible, so historical priority is provisional. Independent scientific validation of this theorem has not been performed.

## References

1. C. Reutenauer, “Number of Permutations with Given Descent Set and Cycle Structure,” *Séminaire Lotharingien de Combinatoire* B21h (1989), scanned original, https://www.mat.univie.ac.at/~slc/s/sc21reutenauer.pdf (first public day not verified).
2. I. M. Gessel and C. Reutenauer, “Counting permutations with given cycle structure and descent set,” *Journal of Combinatorial Theory A* 64 (1993), 189–215, DOI 10.1016/0097-3165(93)90095-P.
3. P. Diaconis, M. McGrath, and J. Pitman, “Riffle shuffles, cycles, and descents,” *Combinatorica* 15 (1995), 11–29, DOI 10.1007/BF01294457 (full text not inspected).
4. J. Fulman, “The combinatorics of biased riffle shuffles,” arXiv:math/9712240 (first submitted 1997-12-09), Sections 3–5, https://arxiv.org/abs/math/9712240.
5. I. M. Gessel and Y. Zhuang, “Plethystic formulas for permutation enumeration,” arXiv:2001.00654v2 (original submitted 2020-01-02), Sections 1 and 7, https://arxiv.org/html/2001.00654v2.

6. S. Elizalde and J. M. Troyka, “Exact and asymptotic enumeration of cyclic permutations according to descent set,” arXiv:1710.05103v3, first submitted 2017-10-13, Corollary 4.2 and Theorem 3.1, https://arxiv.org/html/1710.05103v3.
