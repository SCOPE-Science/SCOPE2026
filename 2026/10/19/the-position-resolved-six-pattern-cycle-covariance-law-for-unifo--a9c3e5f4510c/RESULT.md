# The position-resolved six-pattern cycle-covariance law for uniform permutations

## Finding

Let \(\pi=(\pi_1,\ldots,\pi_n)\) be uniform on the symmetric group \(S_n\). For \(n\ge3\), let \(C_n\) be its number of cycles (in the function \(j\mapsto\pi_j\)). For a window beginning at \(1\le i\le n-2\), let \(I_{\sigma,i}\) indicate that the relative ranks of \((\pi_i,\pi_{i+1},\pi_{i+2})\) form \(\sigma\in S_3\). With \(F_\sigma(n,i)=6n(n-1)(n-2)\operatorname{Cov}(C_n,I_{\sigma,i})\), the entire exact table is

\[
\begin{array}{c|r}
\sigma&F_\sigma(n,i)\\\hline
123&3n-2\\
132&9n-14-12i\\
213&12i-3n-2\\
231&12i-9n+10\\
312&3n-2-12i\\
321&10-3n
\end{array}.
\]

Consequently the six-by-\((n-2)\) covariance array has rank exactly two for all \(n\ge4\), and rank one at \(n=3\). For each \(i\), the separate peak types (132 and 231) and the separate valley types (213 and 312) cancel their location dependence:

\[
\operatorname{Cov}(C_n,I_{132,i}+I_{231,i})=
\operatorname{Cov}(C_n,I_{213,i}+I_{312,i})
=-\frac{2}{3n(n-1)(n-2)}.
\]

The location-refined *six* individual pattern covariances are the main result; the peak/valley sums are checks and do not carry an originality claim. For example, although the two peak types have the same local descent-set indicator, their covariance slopes are respectively \(-12\) and \(+12\) after the common normalization. Thus descent-set-only data cannot resolve this distinction.

## Assumptions and scope

All permutations are equiprobable, with their one-line notation treated as the images of the function on \(\{1,\ldots,n\}\). Cycles are disjoint orbits of this function and not increasing runs or consecutive pattern occurrences in cycle notation. The window is nonwrapping, its three entries are distinct, and \(n\ge3\); no asymptotic assumption is used. Covariance uses ordinary population expectations. The rank of a pattern is the order of its three distinct numerical entries, ranked from smallest to largest.

## Proof

**Conditional completion lemma.** Prescribe an injective partial permutation on \(k\) distinct domain points, and choose uniformly among completions. The prescribed directed arrows decompose into complete directed cycles and directed paths, with isolated unused vertices counted as paths of length zero. Contracting every path to one vertex transforms a completion into an arbitrary permutation on \(n-k\) path-components; every such permutation corresponds to one completion. A closed prescribed cycle remains a cycle. Hence the number of cycles in the completed permutation has conditional expectation \(H_{n-k}+q\), where \(q\) counts complete cycles already formed by the prescribed arrows and \(H_0=0\). Indeed a uniform permutation of \(m\) points has expected cycle count \(H_m\).

For our three-domain window, write the source positions \((a_1,a_2,a_3)=(i,i+1,i+2)\) and the distinct images \((u_1,u_2,u_3)\). Let \(q(u)\) be the number of closed cycles consisting solely of the three prescribed arrows \(a_j\mapsto u_j\). With \(I_{\sigma,i}=1\) exactly on the injections \(u\) of rank pattern \(\sigma\), each pattern class has \((n)_3/6\) injections, where \((n)_3=n(n-1)(n-2)\). Thus

\[
\mathbb E[C_nI_{\sigma,i}]
=\frac{H_{n-3}}6+\frac{1}{(n)_3}
\sum_{u:\operatorname{pat}(u)=\sigma}q(u).
\]

Unconditionally \(\mathbb E C_n=H_n\) and \(\mathbb E I_{\sigma,i}=1/6\). Define \(N_1,N_2,N_3\) as the number (with multiplicity) of closed prescribed one-, two-, and three-cycles over all image injections of pattern \(\sigma\). Their sum is \(\sum q(u)\). By the harmonic identity

\[
(n)_3(H_n-H_{n-3})=3(n-1)(n-2)+3(n-2)+2
=3n^2-6n+2,
\]

we obtain the exact counting identity

\[
6(n)_3\operatorname{Cov}(C_n,I_{\sigma,i})
=6(N_1+N_2+N_3)-(3n^2-6n+2).
\tag{1}
\]

We now count each possible closed cycle within three arrows, independently of other cycles.

For a fixed source \(x=a_j\), a one-cycle is \(u_j=x\). If its image has rank \(r=1,2,3\), the count of other two distinct images is, respectively,

\[
W_1(x)=\binom{n-x}{2},\quad
W_2(x)=(x-1)(n-x),\quad
W_3(x)=\binom{x-1}{2}.
\]

Therefore \(N_1=\sum_{j=1}^3W_{\sigma_j}(a_j)\).

For a two-cycle on source positions \(x=a_j<y=a_k\), images must be \(u_j=y\) and \(u_k=x\). This is compatible with pattern \(\sigma\) precisely when \(\sigma_j>\sigma_k\). Let \(h\) be the remaining source index and \(r=\sigma_h\). The last image has \(x-1\), \(y-x-1\), or \(n-y\) choices according as \(r=1,2,3\). Summing over the three source pairs gives \(N_2\). A directed three-cycle has image-rank pattern exactly 231 or 312, hence \(N_3=1\) for these two patterns and zero otherwise.

The resulting closed-cycle counts and the right-hand side of (1) are

\[
\begin{array}{c|c|c|c|c}
\sigma&N_1&N_2&N_3&6(N_1+N_2+N_3)-(3n^2-6n+2)\\\hline
123&n(n-1)/2&0&0&3n-2\\
132&(n^2+n-6i-4)/2&i&0&9n-14-12i\\
213&(n^2-5n+6i+2)/2&n-i-1&0&12i-3n-2\\
231&(n^2-7n+6i+6)/2&n-i-2&1&12i-9n+10\\
312&(n^2-n-6i)/2&i-1&1&3n-2-12i\\
321&(n^2-5n+8)/2&n-2&0&10-3n
\end{array}.
\]

These expressions follow by substituting the three position values into the displayed \(W_r\) formulas; the domain \(1\le i\le n-2\) makes every count nonnegative. This proves all six covariance identities, including \(n=3\). Each row is affine in \(i\); hence the cross-covariance array has rank at most two. For \(n\ge4\), the 123 row is nonzero and constant in \(i\), while the 132 row has nonzero slope, proving rank exactly two. For \(n=3\) the single column has rank one because the 123 entry is nonzero. The two peak and two valley sum identities follow by direct addition of the corresponding rows.

## Verification

Run the accompanying standalone `verify.py` with Python 3.9 or later. It uses only the standard library. It enumerates all \(n!\) permutations for every \(3\le n\le8\), computes actual cycle counts by orbit traversal, records six contiguous patterns at all positions, forms exact rational covariances, and matches the table in every cell. It additionally recomputes the prescribed-cycle combinatorial counts and compares them with the closed formulas for every \(3\le n\le150\) and every allowed \(i\). It reports 66,282 exact checks; the proof above, not the finite experiments, establishes the theorem for all \(n\).

## Relationship to prior work

Cycle type versus descent sets is treated by Gessel--Reutenauer (1993), and cycle type versus peaks/valleys by Diaconis--Fulman--Holmes (2011), including a generating-function account. Accordingly, neither aggregate peak dependence nor the existence of general generating-function methods is claimed to be new. Descent-set observations cannot distinguish the two peak subtypes 132 and 231, nor the two valley subtypes 213 and 312; the position-dependent individual covariances here therefore contain information beyond those descent-set marginals.

Parviainen's `Cycles and patterns in permutations` (2006) analyzes patterns in *standard cycle notation*, which is a different random variable from one-line consecutive rank patterns. The work of Elizalde--Noy (2012) studies consecutive pattern distributions without conditioning on the number of cycles. Fu--Li (2018) explicitly distinguishes peak subtypes 132 and 231 and derives joint pattern-count generating functions without a marking for total cycle number or individual window position. Thus the subtype *definition* itself is not novel. The 2020 plethystic treatment by Gessel--Zhuang covers powerful cycle-type/descent-family statistics, but its inspected statements do not give the six position-indexed one-line subtype covariances. Previous exact local inversion--cycle results concern pairwise rank comparisons, which alone do not determine the two distinct order subtypes under the same peak/descent configuration. The present counting lemma can be seen as a specialized finite contraction/projection calculation; novelty is limited to the explicit six-way rank-pattern dependence and its affine position structure.

## Limitations

The theorem assumes a uniform distribution on all permutations, nonwrapping windows of length three, and ordinary cycle count; it makes no claim about nonuniform Ewens weights, larger patterns, higher cumulants, or stochastic ordering. An older general identity for marked consecutive patterns and cycle type could implicitly imply this table even without printing its six entries. In particular the complete Gessel--Reutenauer (1993) text was not inspected; the comparison uses its stated descent-set scope and later accessible primary treatments. These are genuine priority limitations. Verification by brute force is finite and does not certify the absence of prior results. Independent scientific validation has not been carried out.

## References

1. I. Gessel and C. Reutenauer (1993), *Counting permutations with given cycle structure and descent set*, J. Combin. Theory Ser. A 64, 189--215. DOI: `10.1016/0097-3165(93)90095-p`.
2. P. Diaconis, J. Fulman, S. Holmes (2011), *Analysis of casino shelf shuffling machines*, preprint `arxiv:1107.2961`, especially section 3.4 (first public source date 2011-07-14).
3. R. Parviainen (2006), *Cycles and patterns in permutations*, `arxiv:math/0610616`.
4. S. Elizalde and M. Noy (2012), *Clusters, generating functions and asymptotics for consecutive patterns in permutations*, `arxiv:1210.6061`.
5. I. Gessel and Y. Zhuang (2020), *Plethystic formulas for permutation enumeration*, `arxiv:2001.00654`.
6. T. Bakšajeva and E. Manstavičius (2013), *On statistics of permutations chosen from the Ewens distribution*, `arxiv:1303.4540`.
7. A. M. Fu and F. Z. K. Li (2018), *Joint distributions of permutation statistics and the parabolic cylinder functions*, `arxiv:1809.07465`.
