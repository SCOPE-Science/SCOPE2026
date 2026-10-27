# Marked inversion participation and decreasing triples: an exact covariance and a central correlation window

## Finding

Let \(n\ge3\) be an integer and let \(\pi\) be uniformly distributed over all permutations of \([n]\). For each position \(1\le i\le n\), define its **inversion participation count**
\[
D_i=\sum_{j<i}\mathbf 1\{\pi(j)>\pi(i)\}+\sum_{j>i}\mathbf 1\{\pi(i)>\pi(j)\},
\]
and let \(T\) be the total number of decreasing subsequences of length three:
\[
T=\sum_{1\le a<b<c\le n}\mathbf 1\{\pi(a)>\pi(b)>\pi(c)\}.
\]
Equivalently, \(D_i\) is the degree of vertex \(i\), and \(T\) is the number of triangles, in the permutation graph of \(\pi\).

The **exact marked covariance law** is
\[
\boxed{\operatorname{Cov}(D_i,T)
=\frac{(n-2)(n-1)(n+1)}{48}
-\frac{(n-3)(i-1)(n-i)}{24}.}
\tag{1}
\]
It is positive for all permitted \(n,i\). For \(n>3\), its largest values occur at the two endpoints, and it decreases toward the central positions.

There is a sharp **correlation-localization scale**. For any sequence of positions \(i_n\in[n]\) such that
\[
\frac{i_n-(n+1)/2}{\sqrt n}\longrightarrow s\in\mathbb R,
\]
one has
\[
\boxed{\operatorname{Corr}(D_{i_n},T)
\longrightarrow \frac54\sqrt{\frac3{13}}\,\frac1{\sqrt{1+2s^2}}.}
\tag{2}
\]
In contrast, if \(\lvert i_n-(n+1)/2\rvert/\sqrt n\to\infty\), then \(\operatorname{Corr}(D_{i_n},T)\to0\). Thus the correlation stays macroscopic only in a position window of order \(\sqrt n\) around the center. Its central limit value is \((5/4)\sqrt{3/13}\), approximately \(0.60048\).

## Assumptions and scope

The permutation is uniform, and all inequalities in the definitions are strict. The position \(i\) refers to the index of an entry, not its value or its rank. All covariance formulas use the standard centered second moment. In particular, \(D_i\) is not the total inversion count: each inversion contributes one to each of its two endpoint participation counts. The results do not assert independence or a joint central limit theorem.

Every statement above holds at each finite integer \(n\ge3\), except the explicitly asymptotic correlation statements, which concern sequences with \(n\to\infty\).

## Proof

**1. Local overlap probabilities.** Replace the random permutation by the relative ranks of independent \(X_1,\ldots,X_n\), each uniform on \([0,1]\). Write \(E_{ab}=\mathbf1\{X_a>X_b\}\) for \(a<b\), and \(Q_{pqr}=\mathbf1\{X_p>X_q>X_r\}\) for \(p<q<r\). Then \(\mathbb E E_{ab}=1/2\) and \(\mathbb E Q_{pqr}=1/6\).

For a fixed edge comparison and a decreasing-triple indicator, their covariance vanishes when all indices are distinct. If both comparison indices belong to the triple, the comparison holds whenever the triple occurs, so the covariance is \(1/6-1/12=1/12\). If exactly one index is shared, let that index occupy the first, middle or last position in the ordered triple. Conditional on the triple, its expected \(X\)-value is respectively \(3/4\), \(1/2\) or \(1/4\). Consequently, the covariance is \(+1/24\) or \(-1/24\) for an extremal shared position according to the outside comparison's orientation, and is zero when the shared position is the middle one. These statements follow by integrating the three uniform order statistics, not by independence of comparisons that share an index.

**2. Summing the overlaps.** Split the sum defining \(T\) into triples that contain \(i\) and those that do not. A triple containing \(i\) contributes \(2(1/12)=1/6\) from the two comparisons in \(D_i\) internal to the triple. The external comparisons for which \(i\) is first or last contribute a signed total
\[
\frac1{24}\left[
\binom{n-i}{2}(n-2i-1)
+\binom{i-1}{2}(2i-n-3)
\right].
\]
The shared-index contribution is zero when \(i\) is the middle of the triple. For triples not containing \(i\), contributions cancel unless the triple straddles \(i\) (its first position is left of \(i\), and its last position is right of \(i\)). Each such triple contributes \(1/12\). There are
\[
\binom{i-1}{2}(n-i)+(i-1)\binom{n-i}{2}
=\frac{(i-1)(n-i)(n-3)}2
\]
such triples. Therefore
\[
\begin{aligned}
\operatorname{Cov}(D_i,T)
&=\frac16\binom{n-1}{2}\\
&\quad+\frac{\binom{n-i}{2}(n-2i-1)+\binom{i-1}{2}(2i-n-3)}{24}\\
&\quad+\frac{(i-1)(n-i)(n-3)}{24},
\end{aligned}
\]
which simplifies exactly to (1). For \(n=3\) the covariance is \(1/6\). For \(n>3\), \((i-1)(n-i)\) is maximized at central positions and minimized at endpoints. Also, \((i-1)(n-i)\le(n-1)^2/4\), so (1) is bounded below by
\[
\frac{(n-1)(n^2+2n-7)}{96}>0\qquad(n\ge3).
\]

**3. Degree variance.** Comparisons that share no index are independent. Two distinct comparisons incident to \(i\) have covariance \(+1/12\) when they point the same way relative to \(i\), and \(-1/12\) otherwise. Summing these covariances and the \(n-1\) individual variances \(1/4\) gives
\[
\boxed{\operatorname{Var}(D_i)
=\frac{2(n-1)+(n-2i+1)^2}{12}.}
\tag{3}
\]

**4. Triple-count variance and its leading constant.** The known leading variance for monotone length-three subsequences is
\[
\operatorname{Var}(T)=\frac{13}{7200}n^5+O(n^4).
\tag{4}
\]
This also follows directly from the rank representation. The first-order projection of \(T\) at index \(j\), conditional on \(X_j=x\), after centering is
\[
\begin{aligned}
H_{j,n}(x)&=\binom{n-j}{2}\left(\frac{x^2}{2}-\frac16\right)
+(j-1)(n-j)\left(x(1-x)-\frac16\right)\\
&\qquad+\binom{j-1}{2}\left(\frac{(1-x)^2}{2}-\frac16\right).
\end{aligned}
\]
Two distinct decreasing triples with disjoint index sets are independent; pairs sharing two or three indices number only \(O(n^4)\). Pairs sharing exactly one index contribute, up to \(O(n^4)\), the sum of \(\operatorname{Var}(H_{j,n}(X_j))\). If \(t=j/n\), then \(n^{-2}H_{j,n}(x)\) tends uniformly to
\[
g_t(x)=\frac{(1-t)^2x^2}{4}+t(1-t)x(1-x)+\frac{t^2(1-x)^2}{4}-\frac1{12}.
\]
Direct rational polynomial integration yields
\[
\int_0^1\int_0^1 g_t(x)^2\,dx\,dt=\frac{13}{7200}.
\]
A Riemann-sum argument, with bounded kernels, establishes (4). This agrees with the known fixed-length subsequence-variance theorem cited below; the constant is **not** claimed to be new.

**5. Correlation window.** Combining (1), (3), and (4), if \((i_n-(n+1)/2)/\sqrt n\to s\) then
\[
\frac{\operatorname{Cov}(D_{i_n},T)}{n^3}\to\frac1{96},\quad
\frac{\operatorname{Var}(D_{i_n})}{n}\to\frac{1+2s^2}{6},\quad
\frac{\operatorname{Var}(T)}{n^5}\to\frac{13}{7200}.
\]
Dividing the covariance by the product of standard deviations gives (2). If the centered position difference dominates \(\sqrt n\), (3) shows that \(\operatorname{Var}(D_{i_n})/n\to\infty\), while (1) gives a uniformly bounded ratio \(\operatorname{Cov}(D_{i_n},T)/n^3\); hence the correlation tends to zero.

## Verification

The included standalone `verify_degree_triangles.py` requires only Python 3's standard library. Running `python3 verify_degree_triangles.py` exhaustively enumerates all permutations through \(n=8\) and checks every position's exact covariance and degree variance against (1) and (3). Independently, it implements the overlap-sum formula in the proof for a range of larger finite parameters, and performs the two-variable polynomial integration for the constant \(13/7200\) using exact rational arithmetic. The program prints `VERIFY_OK` on success.

Finite enumeration and a finite collection of overlap-sum checks are corroboration, not proofs for all integers. The unrestricted proof is the overlap classification, algebraic summation, first-order-projection argument and limiting variance calculation above.

## Relationship to prior work

Işlak and Özdemir (2017) prove a general asymptotic variance theorem for fixed-length monotone subsequence counts in uniform permutations. Their length-three case supplies the constant in (4), and their work is explicitly credited for that part. It does not track the marked-position inversion participation variable in (1) or the correlation window (2).

Bhattacharya and Mukherjee (2015) study degree distributions and degree-process limits for uniform random permutation graphs, which are the graph interpretation of \(D_i\). Gürerk, Işlak and Yıldız (2019) analyze degree moments and clique-count moments separately, but do not state the mixed marked-degree/triangle covariance law or its position-dependent limiting correlation. The preceding proof uses the joint overlap interactions between these two observables.

A published incidence-matrix result gives the complete covariance and precision matrices of *pairwise inversion indicators*. It covers second-order linear combinations of those indicators and is not claimed here. The present statistic \(T\) is cubic in order-comparison indicators and its covariance with \(D_i\) involves fourth-order index configurations and three-observation order constraints; the previously published pair-indicator covariance matrix alone does not determine this mixed moment. Historical equivalence under other terminology remains possible.

## Limitations

The finding concerns a uniform permutation and the specific decreasing length-three count. It does not establish an analogous formula for nonuniform permutations, other pattern lengths, or a multivariate central limit theorem. The leading variance constant was known. The explicit marked mixed covariance and correlation localization are the assessed contributions; no priority claim beyond the inspected literature is made. Other mixed-moment work in random permutation patterns could contain an equivalent result and warrants independent priority review.

## References

1. Ü. Işlak and A. Y. Özdemir, *Asymptotic results on weakly increasing subsequences in random words*, arXiv:1706.09510, first public 2017-06-28; especially Sections 4–5 and Theorem 5.1. https://arxiv.org/abs/1706.09510
2. B. B. Bhattacharya and S. Mukherjee, *Degree Sequence of Random Permutation Graphs*, arXiv:1503.03582, first public 2015-03-12. https://arxiv.org/abs/1503.03582
3. O. Gürerk, Ü. Işlak, and M. A. Yıldız, *A study on random permutation graphs*, arXiv:1901.06678, first public 2019-01-20; especially Sections 2 and 4. https://arxiv.org/abs/1901.06678
4. *Incidence precision law for all inversion indicators of a random permutation*, public mathematical finding, 2026; its exact pair-comparison covariance matrix is a separate known input and does not imply the mixed statistic without higher-order information.
