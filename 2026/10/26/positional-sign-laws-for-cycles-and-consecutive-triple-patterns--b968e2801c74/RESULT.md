# Positional sign laws for cycles and consecutive triple patterns in uniform permutations

## Finding

Let \(n\ge3\), let \(\Pi\) be uniform on the symmetric group \(S_n\), and let \(C\) be its number of cycles, including fixed points. For each \(1\le a\le n-2\) and each three-letter pattern \(\sigma\in S_3\), let \(I_{\sigma,a}\) indicate that the three one-line entries \(\Pi(a),\Pi(a+1),\Pi(a+2)\) have relative order \(\sigma\).

Define \(B_n=\binom n3\) and the following **integer** entries \(t_\sigma(n,a)\):

| \(\sigma\) | \(t_\sigma(n,a)\) |
|---|---|
| \(123\) | \(3n-2\) |
| \(132\) | \(-12a+9n-14\) |
| \(213\) | \(12a-3n-2\) |
| \(231\) | \(12a-9n+10\) |
| \(312\) | \(-12a+3n-2\) |
| \(321\) | \(-3n+10\) |

Then **all six exact positional covariances** are
\[
\boxed{\operatorname{Cov}(C,I_{\sigma,a})=\frac{t_\sigma(n,a)}{36B_n}.}
\]
Every such covariance is *nonzero* because \(t_\sigma(n,a)\equiv1\pmod3\). For \(n\ge4\), the \(123\) covariance is positive and the \(321\) covariance is negative at every position; at \(n=3\), the \(321\) covariance is positive. For \(132\) and \(213\), the signs change strictly once as the window moves from left to right, for every \(n\ge4\). The same holds for \(231\) and \(312\) when \(n\ge5\). The four switch locations follow exactly from the displayed affine expressions (without a zero case), with asymptotic fractions \(3/4\) and \(1/4\).

If \(N_\sigma=\sum_{a=1}^{n-2}I_{\sigma,a}\) is the total count of the consecutive pattern, then
\[
\boxed{\operatorname{Cov}(C,N_\sigma)=\frac{g_\sigma(n)}{6n(n-1)},}
\]
where \(g_{123}=3n-2\), \(g_{132}=g_{213}=3n-8\), \(g_{231}=g_{312}=-3n+4\), and \(g_{321}=-3n+10\). In particular, the peak count (patterns \(132\) and \(231\)) has covariance \(-2/[3n(n-1)]\) with the number of cycles.

## Assumptions and scope

A permutation \(\pi:[n]\to[n]\) is viewed in its **ordinary one-line form** \((\pi(1),\ldots,\pi(n))\); the three-letter pattern of a triple of distinct entries is obtained by replacing the smallest entry by 1, the middle by 2, and the largest by 3. Cycle count is computed from the functional map \(i\mapsto\pi(i)\), not from a standardized cycle word. The model is uniformly random over all \(n!\) permutations. All identities hold for every integer \(n\ge3\) and each admissible start index \(a\).

## Proof

**Lemma (partial permutation completion).** Fix any injection \(f:D\to[n]\), where \(D\subseteq[n]\) has cardinality \(r\). Regard its prescribed arrows \(i\to f(i)\) as a directed graph, and let \(c_0(f)\) count its closed directed cycles. If \(\Pi\) is conditioned to agree with \(f\) on \(D\), then
\[
\mathbb E[C\mid\Pi|_D=f]=c_0(f)+H_{n-r},\qquad H_m=\sum_{j=1}^m\frac1j,\quad H_0=0.
\]
Indeed, remove the already closed cycle components and contract each maximal open directed path (including an isolated vertex) to a single vertex. There are exactly \(n-r\) such open paths: each specified non-cycle arrow contracts one edge, and every already closed cycle uses equally many vertices and arrows. Every bijective completion of the prescribed arrows corresponds bijectively to a permutation of these \(n-r\) paths. Under a uniform completion this is a uniform permutation, with mean cycle count \(H_{n-r}\); the closed cycles contribute \(c_0(f)\) deterministically. This proves the lemma, including \(r=n\).

Fix \(a\) and a pattern \(\sigma\). Conditional on \(I_{\sigma,a}=1\), the unordered set of the three image values at the specified positions is uniform among the \(B_n\) three-element subsets of \([n]\). For each such subset, exactly one assignment gives the pattern \(\sigma\). Apply the lemma with \(D=\{a,a+1,a+2\}\), \(r=3\). It remains to count the aggregate number \(K_\sigma(n,a)\) of directed cycles of lengths 1, 2, or 3 in the partial three-arrow graph, over all \(B_n\) possible image subsets.

The number of specified loops at position \(a+i\), where \(i=0,1,2\) and the image there has rank \(q=\sigma_{i+1}\), is
\[
\binom{a+i-1}{q-1}\binom{n-a-i}{3-q}.
\]
A specified two-cycle between positions \(u<v\) is possible only if the pattern orders the image at \(u\) above the image at \(v\); then these two images must be \(v\) and \(u\), respectively. The remaining third image must lie below \(u\), between \(u\) and \(v\), or above \(v\) according to its rank, yielding respectively \(u-1\), \(v-u-1\), or \(n-v\) possibilities. Finally, a three-cycle on these three positions requires the image subset to equal the position subset, and occurs precisely for \(\sigma=231\) or \(\sigma=312\), once in either case.

Adding these disjoint cycle-length contributions and simplifying gives the complete table
\[
\begin{array}{c|c}
\sigma&K_\sigma(n,a)\\\hline
123&n(n-1)/2\\
132&(n^2+n-4a-4)/2\\
213&(n^2-3n+4a)/2\\
231&(n^2-5n+4a+4)/2\\
312&(n^2-n-4a)/2\\
321&(n^2-3n+4)/2
\end{array}
\]
For example, \(K_{132}(n,a)=\binom{n-a}{2}+\binom a2+(a+1)(n-a-2)+a\), where the four terms enumerate three loop placements and the single eligible two-cycle. This independently demonstrates the counting rule in a nonsymmetric case.

Consequently,
\[
\mathbb E[C\mid I_{\sigma,a}=1]=H_{n-3}+\frac{K_\sigma(n,a)}{B_n}.
\]
For an unconditional uniform permutation \(\mathbb EC=H_n\), and
\[
B_n(H_n-H_{n-3})=\frac{3n^2-6n+2}{6}.
\]
The difference \(K_\sigma-B_n(H_n-H_{n-3})\) is \(t_\sigma(n,a)/6\). Since \(\Pr(I_{\sigma,a}=1)=1/6\), this yields the asserted covariance \(t_\sigma/(36B_n)\). All six numerators are congruent to 1 modulo 3, so no covariance can vanish. Their slopes and endpoint values give the asserted sign changes and smallest lengths. Summing over \(a=1,\ldots,n-2\) gives the six stated global covariances.

## Verification

Run the included standard-library checker with `python3 verify.py`. It independently enumerates all permutations through \(n=8\) and compares every triple-pattern covariance and every total-pattern covariance with the theorem using exact rational arithmetic. It also independently enumerates completions of seeded partial injections through \(n=7\) and verifies the completion lemma. Its completed run reported 900 exact assertions. These finite computations supplement the all-\(n\) proof rather than substitute for it.

## Relationship to prior work

Parviainen (2006) studies joint patterns and cycle counts chiefly when the patterns are read from a *standardized cycle word*. The explicit distinction from ordinary one-line pattern events appears in that paper's introduction and definitions; the two joint laws are not interchangeable. Elizalde (2015) surveys one-line consecutive-pattern enumeration and its statistical applications but does not supply their positional joint covariances with the permutation's number of cycles. A published inversion-gap formula provides \(\operatorname{Cov}(C,{\bf1}\{\Pi(i)>\Pi(j)\})\) for a **single pair** of positions; this is a lower-order comparison, not a formula for three-letter pattern events (which are intersections of pair comparisons). The present table resolves all six three-letter events and their position-dependent sign phases.

## Limitations

The theorem concerns first mixed moments, not conditional stochastic ordering, higher mixed moments, nonuniform permutation laws, or patterns of length four or greater. The completion lemma is elementary and older enumerative literature may imply aspects of this table under another encoding; exhaustive historical priority has not been established. The exact sign cutoffs at finite \(n\) are given by the integer numerators, not by rounding the asymptotic fractions.

## References

1. R. Parviainen, “Cycles and patterns in permutations,” arXiv:math/0610616, first public version 2006-10-20, https://arxiv.org/abs/math/0610616.
2. S. Elizalde, “A survey of consecutive patterns in permutations,” arXiv:1504.07265, first public version 2015-04-27, https://arxiv.org/abs/1504.07265.
3. “Linear inversion-gap profile for cycle count in a uniform random permutation,” public research record (2026), https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-linear-inversion-gap-profile-for-cycle-count-in-a-uniform-random--efaa92233051.
