# Oriented triple-pattern covariances with cycle count in uniform permutations

## Finding

Let \(\Pi_n\) be uniformly distributed over permutations of \(\{1,\ldots,n\}\), where \(n\ge3\), and let \(K_n\) be its total number of disjoint cycles, including fixed points. For each integer \(1\le a\le n-2\), define \(I_{a,\tau}\) as the indicator that \((\Pi_n(a),\Pi_n(a+1),\Pi_n(a+2))\) has relative order \(\tau\). Specifically, \(132\) and \(231\) distinguish the two orientations of a peak, while \(213\) and \(312\) distinguish the two orientations of a valley.

Put \(Q_n=6n(n-1)(n-2)\). Then **all four orientation-resolved covariances** are

\[
\begin{aligned}
Q_n\operatorname{Cov}(K_n,I_{a,132})&=9n-14-12a,\\
Q_n\operatorname{Cov}(K_n,I_{a,231})&=12a-9n+10,\\
Q_n\operatorname{Cov}(K_n,I_{a,213})&=12a-3n-2,\\
Q_n\operatorname{Cov}(K_n,I_{a,312})&=3n-2-12a.
\end{aligned}
\]

Thus the four covariances exhibit distinct, exactly located sign thresholds. If \(a/n\to x\in(0,1)\), their \(n^2\)-scaled limits in the displayed order are \((9-12x)/6\), \((12x-9)/6\), \((12x-3)/6\), and \((3-12x)/6\). The orientation-specific transitions occur at the fractions \(3/4\) and \(1/4\). In contrast, the un-oriented peak and valley events each have the smaller, position-independent covariance

\[
\operatorname{Cov}(K_n,I_{a,132}+I_{a,231})
=\operatorname{Cov}(K_n,I_{a,213}+I_{a,312})
=-\frac{2}{3n(n-1)(n-2)}.
\]

The sum identity is a consistency consequence, not a separate originality claim. Since \(\mathbb P(I_{a,\tau}=1)=1/6\), each displayed formula also specifies the exact conditional excess \(\mathbb E[K_n\mid I_{a,\tau}=1]-\mathbb E[K_n]=6\operatorname{Cov}(K_n,I_{a,\tau})\).

## Assumptions and scope

The permutation is uniform on the full symmetric group; the words \(132\), \(231\), \(213\), and \(312\) describe consecutive **one-line values**, not cycles in cycle notation and not nonconsecutive classical-pattern occurrences. Both endpoints \(a=1\) and \(a=n-2\), and the smallest size \(n=3\), are included. No independence or asymptotic approximation is assumed.

## Proof

**Completion lemma.** Fix any three distinct positions \(S=\{a,a+1,a+2\}\) and prescribe their three distinct images. Regard the three forced mappings as directed edges of a partial permutation graph. Because all forced sources and targets are distinct, its components are directed open paths and closed directed cycles. Let \(G\) denote the number of directed cycles consisting exclusively of forced edges. Delete each completed forced cycle, and contract each open forced path to one vertex. Exactly three vertices are removed or contracted, leaving \(n-3\) supervertices. Completing the original bijection is in bijection with a uniform permutation of these supervertices, and the original cycle count equals \(G\) plus the reduced cycle count. Consequently,

\[
\mathbb E[K_n\mid\Pi_n(a),\Pi_n(a+1),\Pi_n(a+2)]
=H_{n-3}+G,
\qquad H_0=0,
\]

where \(H_m=\sum_{j=1}^{m}1/j\). This assertion holds also when all three forced edges form one or more completed cycles.

There are three possible forced one-cycles, three possible forced two-cycles, and two possible forced three-cycles. A specified one-cycle has probability \(1/n\), a specified two-cycle has probability \(1/[n(n-1)]\), and a specified three-cycle has probability \(1/[n(n-1)(n-2)]\). Therefore

\[
\mathbb E[G]=\frac3n+\frac3{n(n-1)}+\frac2{n(n-1)(n-2)}.
\]

Write \(F_\tau\) for the number of triple-image assignments of pattern \(\tau\) containing a forced fixed point, counted with multiplicity if there are multiple fixed points; similarly let \(M_\tau\) count forced two-cycles and \(J_\tau\) forced three-cycles. Define, for \(1\le s\le n\),

\[
 f_1(s)=\binom{n-s}{2},\qquad
 f_2(s)=(s-1)(n-s),\qquad
 f_3(s)=\binom{s-1}{2}.
\]

If the pattern rank at position \(s\) is \(r\), exactly \(f_r(s)\) assignments of the other two images make \(\Pi_n(s)=s\); hence

\[
F_\tau=f_{\tau_1}(a)+f_{\tau_2}(a+1)+f_{\tau_3}(a+2).
\]

For two-cycles, force in turn the swaps of positions \((a,a+1)\), \((a,a+2)\), and \((a+1,a+2)\), then count admissible values of the remaining image. For the four patterns in displayed order, this gives

\[
\begin{array}{c|rrrr}
\tau&132&231&213&312\\\hline
M_\tau&a&n-a-2&n-a-1&a-1\\
J_\tau&0&1&0&1
\end{array}
\]

(the only fully forced three-cycles have one-line patterns \(231\) and \(312\)). Each pattern has probability \(1/6\), and each assigned triple has probability \(1/[n(n-1)(n-2)]\). The completion lemma now gives the **exact counting identity**

\[
6n(n-1)(n-2)\operatorname{Cov}(K_n,I_{a,\tau})
=6(F_\tau+M_\tau+J_\tau)-3n(n-2)-2.
\]

Substituting the four \(F_\tau\) values and the two small count tables simplifies, respectively, to \(9n-14-12a\), \(12a-9n+10\), \(12a-3n-2\), and \(3n-2-12a\), proving all formulas. Positive denominators show that each sign threshold is exactly where its affine numerator vanishes. Dividing by \(n\), with \(a/n\to x\), yields the stated macroscopic transition fractions. Adding the two peak or valley formulas yields the final cancellation identity.

## Verification

The self-contained Python 3 program `verify_ordinal_cycle.py` uses integer and rational arithmetic, without external packages. Execute:

```sh
python3 verify_ordinal_cycle.py
```

It exhaustively enumerates all \(409{,}110\) permutations of sizes \(3\) through \(9\), computes cycle counts directly from cycle decomposition, and compares all \(168\) location-pattern covariance cells against the six-pattern consistency table (which contains the four finding patterns). It separately checks \(745{,}506\) exact symbolic-substitution cells over \(3\le n\le500\). All assertions passed. These finite checks guard implementation and algebra but are **not** the proof of the formulas for all sizes; the completion and counting argument above supplies that proof.

## Relationship to prior work

Maples, Nikeghbali, and Zeindler analyze the random-permutation cycle count under generalized Ewens laws [1]. Fu and Li treat separate orientation-resolved peak-pattern counts (\(132\) versus \(231\)), without a joint statistic for disjoint cycles [2]. Fulman, Kim, and Lee examine peaks conditional on conjugacy class and identify an earlier generating function enumerating **aggregate peak number** by cycle type [3]. Gessel and Zhuang give powerful joint distributions of **descent-set-based** statistics with cycle type, including peaks and descents [4]; their formulas account for coarser peak/cycle dependence but do not record the direction-resolved, location-dependent four-row covariance kernel. The distinction matters because \(132\) and \(231\) have identical adjacent ascent/descent signatures yet different contributions here. Earlier Gessel–Reutenauer descent-set enumeration likewise gives coarser information [5].

## Limitations

This is a first-moment, uniform-permutation statement, not a joint-distribution theorem or an Ewens-parameter extension. It does not claim novelty for aggregate peak-versus-cycle formulas already accessible through published generating functions. A more general historical pattern-by-cycle generating function could encode the oriented kernel indirectly; bibliographic searches and the inspected full texts cannot establish absolute priority. There is no independent audit. The closed form does not follow from finite enumeration alone.

## References

[1] K. Maples, A. Nikeghbali, D. Zeindler, *On the number of cycles in a random permutation*, arXiv:1203.4132v1 (public 2012-03-19), https://arxiv.org/html/1203.4132v1 .

[2] A. M. Fu, F. Z. K. Li, *Joint Distributions of Permutation Statistics and the Parabolic Cylinder Functions*, arXiv:1809.07465v1 (2018), https://arxiv.org/pdf/1809.07465 .

[3] J. Fulman, G. B. Kim, S. Lee, *Central limit theorem for peaks of a random permutation in a fixed conjugacy class*, arXiv:1902.00978v1 (2019), https://arxiv.org/html/1902.00978v1 .

[4] I. M. Gessel, Y. Zhuang, *Plethystic formulas for permutation enumeration*, arXiv:2001.00654v2 (2020), https://arxiv.org/pdf/2001.00654 .

[5] I. M. Gessel, C. Reutenauer, *Counting permutations with given cycle structure and descent set*, J. Combin. Theory Ser. A **64** (1993), 189–215, https://doi.org/10.1016/0097-3165(93)90095-P .
