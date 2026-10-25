# Maximum scattered-subsequence complexity for binary words with three ones

## Finding

For a finite binary word \(w\), write \(\operatorname{Sub}(w)\) for the **set of distinct scattered subsequences**, including the empty word. The count is by resulting strings, not by embeddings. For each integer \(n\ge3\), let
\[
T_3(n)=\max_{\substack{w\in\{0,1\}^{n}\\ |w|_1=3}}|\operatorname{Sub}(w)|.
\]
Put \(m=n-3=4t+r\), with \(t\ge0\) and \(r\in\{0,1,2,3\}\). Then
\[
T_3(n)=\begin{cases}
(t+2)^2(t^2+4t+1),&r=0,\\
(t+2)(t^3+7t^2+13t+5),&r=1,\\
(t+2)(t^3+8t^2+18t+10),&r=2,\\
(t+1)(t+3)(t^2+7t+11),&r=3.
\end{cases}
\]
There is a complete **unique-maximizer classification up to reversal**. Express a weight-three word uniquely as
\(w=0^a1\,0^b1\,0^c1\,0^d\), with \(a,b,c,d\ge0\). All maximizing gap quadruples are exactly
\[
\begin{array}{c|l}
r& (a,b,c,d)\\\hline
0&(t,t,t,t)\\
1&(t,t+1,t,t),\ (t,t,t+1,t)\\
2&(t,t+1,t+1,t)\\
3&(t,t+1,t+1,t+1),\ (t+1,t+1,t+1,t)
\end{array}
\]
(no other quadruples are optimal). In particular \(T_3(n)=n^4/256+O(n^3)\) as \(n\to\infty\).

## Assumptions and scope

The alphabet is exactly \(\{0,1\}\), length is arbitrary \(n\ge3\), and the number of ones is exactly three. Subsequence means deletion of zero or more symbols without reordering; equal resulting subsequences are counted once. Boundary zero runs may be empty. Bit complementation does not preserve the specified weight except at length six and is not used for equivalence. The four residue classes refer to the number of zeros, not to the total word length.

## Proof

**1. Exact count for fixed gaps.** Let \(S(u)\) count distinct scattered subsequences of a prefix \(u\), including the empty word. On appending a symbol \(x\), if its previous occurrence is at position \(j\), then
\[
S(ux)=2S(u)-S(u[1..j-1]);
\]
if \(x\) has never appeared, the subtracted term is zero. Indeed, the overcounted subsequences are exactly those already obtainable by terminating at the preceding \(x\). Track \((S,P_0,P_1)\), where \(P_x\) is the stored value before the most recent \(x\) (zero when absent). The append matrices are
\[
M_0=\begin{pmatrix}2&-1&0\\1&0&0\\0&0&1\end{pmatrix},\qquad
M_1=\begin{pmatrix}2&0&-1\\0&1&0\\1&0&0\end{pmatrix}.
\]
Starting from \((1,0,0)^\mathsf T\), one has \((M_0-I)^2=0\), hence \(M_0^k=I+k(M_0-I)\). Multiplication of \(M_0^dM_1M_0^cM_1M_0^bM_1M_0^a\) gives
\[
F(a,b,c,d):=|\operatorname{Sub}(w)|
=(a+2)(b+2)(c+2)(d+2)
 -(a+2)(b+2)-(a+2)(d+2)-(c+2)(d+2).\tag{1}
\]
This is an identity for all nonnegative integer gaps, including zero boundaries.

**2. Balancing opposite gaps.** Set \(K=(b+2)(c+2)-1\), so \(K>|b-c|\). When \(a\ge d+2\), directly from (1),
\[
F(a-1,b,c,d+1)-F(a,b,c,d)=K(a-d-1)+(b-c)>0.
\]
The analogous assertion for \(d\ge a+2\) follows by reversal. Similarly, with \(L=(a+2)(d+2)>|a-d|\), whenever \(b\ge c+2\),
\[
F(a,b-1,c+1,d)-F(a,b,c,d)=L(b-c-1)+(a-d)>0,
\]
and the reverse imbalance is likewise improvable. Every maximizer therefore satisfies \(|a-d|\le1\) and \(|b-c|\le1\). Let \(p=a+d=2u+\epsilon\), \(q=b+c=2v+\delta\) with \(\epsilon,\delta\in\{0,1\}\). Since
\[
F(a,b,c,d)-F(a,c,b,d)=(d-a)(b-c),
\]
the best orientation for fixed \(p,q\) is represented by
\[
(a,b,c,d)=(u,v+\delta,v,u+\epsilon),\qquad G_{\epsilon\delta}(u,v):=F(u,v+\delta,v,u+\epsilon).
\tag{2}
\]
The other orientation ties only if one of the two sums is even; in the final winning cases this gives precisely the reversal pairs stated above.

**3. Two-unit transfer across gap pairs.** For \(v\ge1\), set \(\Delta_{\epsilon\delta}(u,v)=G_{\epsilon\delta}(u+1,v-1)-G_{\epsilon\delta}(u,v)\). Expanding (1) yields the four exact identities
\[
\begin{aligned}
\Delta_{00}&=-2u^2v-3u^2+2uv^2-4uv-10u+5v^2-10,\\
\Delta_{01}&=-(v+2)(2u^2-2uv+6u-5v+5),\\
\Delta_{10}&=-2u^2v-3u^2+2uv^2-6uv-13u+6v^2-2v-15,\\
\Delta_{11}&=-2(v+2)(u^2-uv+4u-3v+4).
\end{aligned}\tag{3}
\]
For \(\epsilon\delta\in\{00,10,11\}\), the differences are negative when \(1\le v\le u+1\) and positive when \(v\ge u+2\). For \(01\), they are negative for \(1\le v\le u\), positive for \(v\ge u+1\), except \(\Delta_{01}(0,1)=0\). These signs can be checked without relying on numerical experiments: every expression (3) is a convex quadratic in \(v\), is negative at \(v=0\), and at its last-negative threshold; its value at the immediately next integer is positive (or zero at the stated exceptional pair), and its slope thereafter increases. The boundary substitutions are
\[
\begin{array}{c|ccc}
 &\Delta(u,u)&\Delta(u,u+1)&\Delta(u,u+2)\\\hline
00&-2(u^2+5u+5)&-2u-5&2(u^2+5u+5)\\
01&-(u+2)(u+5)&u(u+3)&(u+4)(3u+5)\\
10&-3(u^2+5u+5)&-u^2-7u-11&u^2+5u+5\\
11&-2(u+2)(u+4)&-2(u+3)&2(u+2)(u+4)
\end{array}
\]
(the displayed boundary values, combined with convexity and negativity at zero, give the signs). Therefore, at a fixed \(m=p+q\), optimizing inside either parity class reduces to a single adjacent pair of nearly equal \(u,v\), with only an inessential tie for the losing parity class at \(m=3\).

**4. Final comparison and equality.** The parity-class candidates for \(m=4t+r\) are, in the order (winner; other parity):
\[
\begin{array}{c|cc|c}
r&\text{winner }(a,b,c,d)&\text{other parity }(a,b,c,d)&\text{winner excess}\\\hline
0&(t,t,t,t)&(t-1,t+1,t,t)&t^2+3t+1\\
1&(t,t+1,t,t)&(t,t,t,t+1)&t+2\\
2&(t,t+1,t+1,t)&(t,t+1,t,t+1)&t+2\\
3&(t,t+1,t+1,t+1)&(t+1,t+1,t,t+1)&t+3
\end{array}
\]
At \(r=0,t=0\), the other-parity candidate is inadmissible, so the winner is immediate. All remaining excesses are positive. Substitution into (1) gives the displayed four polynomials. Strictness in both balancing steps and the parity comparisons supplies the complete equality characterization. The leading term is \((m/4)^4\), so the asymptotic assertion follows.

## Verification

The standalone `check.py` performs two independent counting methods: direct construction of sets of subsequences for all gap quadruples with at most seven zeros, and the previous-symbol dynamic recurrence for all 73,815 quadruples with at most 34 zeros. It checks (1), the maximum polynomials, **all** maximizing quadruples, and the signs of the four transfer differences on a finite diagnostic grid. Its output is provided in the accompanying verification note. These finite checks corroborate, but do not replace, the symbolic equalities and all-length inequalities in the proof.

## Relationship to prior work

Flaxman, Harrow, and Sorkin (2004) solve the **unconstrained** length-\(n\) distinct-subsequence maximization problem, yielding an alternating binary optimum. Fixing the number of ones to three excludes that optimum for all sufficiently large lengths and forces a different, quartic rather than exponential, regime. Liron and Langberg (first public preprint 2012) optimize deletion-descendant cardinalities at a fixed **number of runs**, especially the equal-run-length case; fixing the Parikh count to precisely three ones instead constrains the runs of ones to total length three. Neither checked theorem specifies (1), the four weight-three polynomials, or the equality classification. The comparison is at the level of optimization domains and theorem implications, not wording alone.

## Limitations

The theorem addresses the union of scattered subsequences of *all* lengths, not the cardinality of every separate deletion sphere. It does not classify other Hamming weights. Published-source comparisons cannot exclude an unindexed or uninspected equivalent extremal result. No external independent validation has been performed.

## References

1. A. Flaxman, A. W. Harrow, G. B. Sorkin, “Strings with Maximally Many Distinct Subsequences and Substrings,” *Electronic Journal of Combinatorics* 11 (2004), R8, DOI: 10.37236/1761; openly available paper: https://www.combinatorics.org/ojs/index.php/eljc/article/download/v11i1r8/pdf .
2. Y. Liron, M. Langberg, “A Characterization of the Number of Subsequences Obtained via the Deletion Channel,” first preprint 2012-02-08, arXiv:1202.1644, https://arxiv.org/abs/1202.1644 .
3. M. J. Collins, “The Number of Distinct Subsequences of a Random Binary String,” first preprint 2013-10-28, arXiv:1310.7288, https://arxiv.org/abs/1310.7288 .
