# A sharp fixed-point covariance reversal for the second-largest cycle of a random permutation

## Finding
Let \(\Pi_n\) be uniform on the symmetric group of degree \(n\). Write \(F_n\) for its number of fixed points and \(B_n\) for the **second-largest** length in its descending list of cycle lengths, counting ties and putting \(B_n=0\) when there is only one cycle. For every integer \(n\ge2\),
\[
\operatorname{Cov}(F_n,B_n)
=\mu_{n-1}+\frac{1}{n-1}-\mu_n,
\qquad \mu_j:=\mathbb E[B_j].
\]
The **complete sign classification** is
\[
\operatorname{Cov}(F_n,B_n)>0\quad(2\le n\le5),
\qquad
\operatorname{Cov}(F_n,B_n)<0\quad(n\ge6).
\]
There are no zero-covariance sizes. Let \(\gamma_2=\lim_{n\to\infty}\mathbb E[B_n]/n\), the classical second-ranked permutation-cycle mean fraction of Shepp and Lloyd. The covariance moreover has a finite nonzero limit,
\[
\lim_{n\to\infty}\operatorname{Cov}(F_n,B_n)
=-\gamma_2\approx-0.20958090.
\]

## Assumptions and scope
All permutations are equally likely. A fixed point is a cycle of length one. Distinct cycles of the same length occupy distinct ranks; for instance, two cycles of length \(r\) give first and second lengths both equal to \(r\). The zero convention is applied when the permutation has fewer than two cycles. The theorem concerns ordinary uniformly random permutations, not Ewens parameters other than one. The finite sign statement applies to every integer \(n\ge2\); the limiting assertion uses the classical limit theory of ranked cycle lengths.

## Proof
**Marked fixed-point reduction.** Since \(\mathbb E F_n=1\), exchangeability gives
\[
\mathbb E[F_n B_n]=\mathbb E[B_n\mid\Pi_n(1)=1].
\]
Conditionally, the other \(n-1\) labels form an independent uniform permutation. Adding the designated singleton cycle leaves its second-largest cycle length unchanged unless the remaining permutation consists of a single cycle. A uniform permutation of \(m\) elements is a single cycle with probability \(1/m\). Consequently
\[
\mathbb E[F_n B_n]=\mu_{n-1}+\frac1{n-1},
\]
proving the exact covariance identity.

**Insertion and a positive combinatorial representation.** Construct a uniform permutation of \(m+1\) elements from one of \(m\) elements by inserting the new label into one of the \(m\) existing cycle arrows, or placing it in a new singleton cycle, with each of the \(m+1\) choices equiprobable. For a given permutation of size \(m\), write \(A_m\ge B_m\) for its two largest cycle lengths and \(c_{m,b}\) for the number of its cycles of length \(b\). Define the nonnegative quantity
\[
T_m=\mathbb E\!\left[B_m c_{m,B_m}
\mathbf1_{\{A_m>B_m\ge1\}}\right],
\]
where the product is interpreted as zero when \(B_m=0\). A newly inserted label increases the second-largest length by one precisely if the largest length strictly exceeds the second-largest, and the label is inserted into a cycle of second-largest length. A new singleton cycle increases that length only when the old permutation has exactly one cycle. Thus
\[
(m+1)(\mu_{m+1}-\mu_m)=\frac1m+T_m.
\]
The marked fixed-point identity therefore simplifies to
\[
\boxed{\operatorname{Cov}(F_{m+1},B_{m+1})=\frac{1-T_m}{m+1}.}
\]
This formula is exact even for \(m=1\).

**Uniform strict negativity.** Use the uniform-permutation cycle-type probability: distinct cycle lengths \(a>b\) with \(a+b=m\) occur with probability \(1/(ab)\), so their contribution to \(T_m\) is \(1/a\). Likewise, the three-cycle types \((a,b,1)\) with \(a>b\ge2\) and \(a+b+1=m\) contribute \(1/a\). The two families are disjoint. Hence
\[
T_m\ \ge\ S_m:=
\sum_{b=1}^{\lfloor(m-1)/2\rfloor}\frac1{m-b}
+\sum_{b=2}^{\lfloor(m-3)/2\rfloor}\frac1{m-1-b},
\]
with empty sums zero. Writing \(H_j=\sum_{s=1}^j1/s\), one obtains
\[
S_{2k}=H_{2k-1}+H_{2k-3}-2H_k,
\qquad
S_{2k+1}=H_{2k}+H_{2k-2}-2H_k
\]
for the indicated nonempty-sum regimes. For even \(m=2k\), the difference \(S_{m+2}-S_m\) equals \(1/(2k-2)+1/(2k-1)+1/(2k)+1/(2k+1)-2/(k+1)\), which exceeds \(4/(2k+1)-2/(k+1)>0\). For odd \(m=2k+1\), that difference is \(1/(2k-1)+1/(2k)+1/(2k+1)+1/(2k+2)-2/(k+1)\), which exceeds \(4/(2k+2)-2/(k+1)=0\). Thus \(S_{m+2}>S_m\) within both parity classes. The two exact base values are
\[
S_9=\frac{841}{840}>1,
\qquad
S_{14}=\frac{6527}{6435}>1.
\]
It follows that \(T_m>1\) for all odd \(m\ge9\) and all even \(m\ge14\), proving strictly negative covariance at the corresponding sizes.

**Finite boundary cases.** The remaining sizes are resolved exactly, without simulation. For any cycle-length partition \(\lambda\vdash n\), let \(c_j(\lambda)\) count its parts of size \(j\); its uniform-permutation probability is
\[
 p(\lambda)=\prod_{j\ge1}\frac{1}{j^{c_j(\lambda)}c_j(\lambda)!}.
\]
Let \(b(\lambda)\) be the second-largest part, or zero for a one-part partition. Then
\[
\mu_n=\sum_{\lambda\vdash n}p(\lambda)b(\lambda),
\qquad
\mathbb E[F_nB_n]=\sum_{\lambda\vdash n}p(\lambda)c_1(\lambda)b(\lambda).
\]
Their exact difference gives the exceptional values:

| \(n\) | \(\operatorname{Cov}(F_n,B_n)\) |
|---:|---:|
| \(2\) | \(1/2\) |
| \(3\) | \(1/3\) |
| \(4\) | \(1/8\) |
| \(5\) | \(1/30\) |
| \(6\) | \(-1/36\) |
| \(7\) | \(-17/420\) |
| \(8\) | \(-433/5760\) |
| \(9\) | \(-3821/45360\) |
| \(11\) | \(-18397/166320\) |
| \(13\) | \(-65384461/518918400\) |

Together with the harmonic bounds, this covers all integers \(n\ge2\).

**The limiting covariance.** Shepp and Lloyd established \(\mu_m/m\to\gamma_2>0\), with the normalized second-largest cycle converging to a distribution supported on positive lengths. The classical probability bound for equal long cycles, also given by Ford, is
\[
\Pr\{\text{two cycles have the same length at least }\ell\}
\le\frac{1}{2(\ell-1)}\quad(\ell\ge2).
\]
For any fixed \(\varepsilon>0\), the event that \(B_m\ge\varepsilon m\) and either of the top two ranks is tied has probability \(O((\varepsilon m)^{-1})\). The probability \(\Pr(B_m<\varepsilon m)\) can be made arbitrarily small asymptotically by choosing \(\varepsilon\) small. Therefore, with probability tending to one, the two largest cycles have distinct lengths and the second-largest length occurs exactly once. On this event, the random variable inside \(T_m\) equals \(B_m\). Both are bounded between zero and \(m\), so \(T_m/m-\mu_m/m\to0\). Hence \(T_m/m\to\gamma_2\), and the exact covariance representation yields \((1-T_m)/(m+1)\to-\gamma_2\).

## Verification
The accompanying standalone `verify.py` computes exact rational moments in two different ways: enumeration of every integer partition with its cycle-index weight, and a cycle-length cutoff recurrence. It also enumerates every individual permutation of orders \(2\) through \(8\), verifies the mixed moment directly, checks the insertion identity through order \(15\), and compares the parity-specific harmonic bounds through order \(300\). The finite checks validate the computation and all exceptional rational values; the all-size sign and asymptotic results rely on the written analytic arguments.

For a second exact algorithm, define \(a_{q,t}\) as the probability that a uniform permutation of \(q\) elements has no cycle of length \(t\) or greater. Set \(a_{0,t}=1\) and
\[
q a_{q,t}=\sum_{j=1}^{\min(q,t-1)}a_{q-j,t}.
\]
Then
\[
\Pr(B_n\ge t)=1-a_{n,t}-\sum_{j=t}^{n}\frac{a_{n-j,t}}j,
\qquad
\mu_n=\sum_{t=1}^n\Pr(B_n\ge t).
\]
These equations, the finite table, and the code permit independent reproduction without external datasets.

## Relationship to prior work
Shepp and Lloyd, *Ordered Cycle Lengths in a Random Permutation* (1966), provide the ordered-cycle distribution, the constant \(\gamma_2\), and a general one-step insertion formula for ranked-cycle moments (their Section 6). The insertion identity is therefore an **acknowledged prior ingredient**, not presented as new. The present claim is the complete sign classification for the fixed-point/second-largest-cycle covariance, with a sharp crossover at size six, plus its negative asymptotic limit. Ford's cycle-type toolkit supplies a standard large-cycle tie probability bound; Mukherjee's fixed-point limit theorems concern a different asymptotic dependence regime. None of the inspected statements gives the sharp finite sign theorem or its limiting covariance in the form claimed here. Related results for the largest-ranked cycle, arbitrary cycle counts, and descent statistics do not imply this specific second-ranked sign reversal without new analysis.

## Limitations
The result is restricted to uniform random permutations and the second-largest cycle. The exact formulas require no unverified conjectures; the limiting constant is a classical result rather than a newly evaluated number. The claim does not assert independence, a multivariate limit law, or analogous thresholds for other Ewens measures or ranks. Literature searches cannot exclude every obscure historical equivalent, and the broad 1966 insertion formula is an especially relevant priority comparison. Independent review has not been performed.

## References
1. L. A. Shepp and S. P. Lloyd, *Ordered Cycle Lengths in a Random Permutation*, Transactions of the American Mathematical Society **121** (1966), 340–357; first publicly presented September 2, 1965. https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Ordered-cycle-lengths-in-a-random-permutation.pdf
2. K. Ford, *Cycle Type of Random Permutations: a Toolkit*, Discrete Analysis (2022), article 9; preprint arXiv:2104.12019. https://arxiv.org/abs/2104.12019
3. S. Mukherjee, *Fixed Points and Cycle Structure of Random Permutations*, arXiv:1509.04552. https://arxiv.org/abs/1509.04552
