# Sharp first correction for distinct substrings of a uniform random word

## Result

Let \(X_1,\dots,X_n\) be i.i.d. uniform on an alphabet of fixed size \(d\ge 2\). For each \(k\), let \(D_{n,k}\) be the number of distinct consecutive substrings of length \(k\), and let
\[
D_n=\sum_{k=1}^n D_{n,k}.
\]
Write
\[
T_n=\sum_{k=1}^n(n-k+1)=\frac{n(n+1)}2
\]
for the number of substring positions counted with multiplicity, and define the expected repetition deficit
\[
R_{n,d}=T_n-\mathbb E D_n.
\]
Then, for every fixed \(d\ge2\),
\[
\boxed{R_{n,d}=n\log_d n+O_d(n)}
\]
and hence
\[
\boxed{\mathbb E D_n=\frac{n(n+1)}2-n\log_d n+O_d(n).}
\]
Thus the coefficient of the first logarithmic correction is exactly one.

A finite-\(n\) sandwich is available. Put \(m=\lfloor\log_d n\rfloor\) and \(N_k=n-k+1\). Then
\[
\boxed{
\sum_{k=1}^m(N_k-d^k)
\;\le\;
R_{n,d}
\;\le\;
\sum_{k=1}^m N_k+
\sum_{k=m+1}^n {N_k\choose2}d^{-k}.
}
\]
In particular,
\[
R_{n,d}\le m(n+1)-\frac{m(m+1)}2+
\frac{n^2d^{-m}}{2(d-1)},
\]
while
\[
R_{n,d}\ge m(n+1)-\frac{m(m+1)}2-
\frac{d(d^m-1)}{d-1}.
\]
Both bounds are \(n\log_d n+O_d(n)\).

There is also an additive optimality consequence. If
\[
M_{n,d}=\max_{w\in[d]^n}D_n(w),
\]
then
\[
0\le M_{n,d}-\mathbb E D_n=O_d(n),
\]
and more explicitly the displayed sandwich implies
\[
\boxed{0\le M_{n,d}-\mathbb E D_n\le \frac{3dn}{2(d-1)}.}
\]
Consequently both the maximum and the random expectation have the same first deficit from \(T_n\):
\[
T_n-M_{n,d}=n\log_d n+O_d(n),
\qquad
T_n-\mathbb E D_n=n\log_d n+O_d(n).
\]

## Proof

For a fixed length \(k\), there are \(N_k=n-k+1\) starting positions. Since at most \(d^k\) different length-\(k\) words exist,
\[
D_{n,k}\le d^k,
\]
so deterministically
\[
N_k-D_{n,k}\ge N_k-d^k.
\]
Summing this for \(1\le k\le m=\lfloor\log_d n\rfloor\) gives the lower bound on \(R_{n,d}\).

For the upper bound, let \(M_w\) denote the number of occurrences of a particular length-\(k\) word \(w\). Then
\[
N_k-D_{n,k}
=\sum_w (M_w-1)_+
\le \sum_w {M_w\choose2}.
\]
The right-hand side is the number of equal unordered pairs of length-\(k\) substring positions. For any two distinct starting positions \(i<j\),
\[
\Pr\bigl(X_i\cdots X_{i+k-1}=X_j\cdots X_{j+k-1}\bigr)=d^{-k}.
\]
This remains exact when the two windows overlap. Indeed, if their shift is \(s=j-i<k\), equality imposes period \(s\) on the block of \(k+s\) letters. There are exactly \(s\) free letters, hence \(d^s\) satisfying assignments among \(d^{k+s}\), giving probability \(d^{-k}\). The disjoint case is immediate.

Therefore
\[
\mathbb E(N_k-D_{n,k})\le {N_k\choose2}d^{-k}.
\]
For \(k\le m\), use only the trivial bound \(N_k-D_{n,k}\le N_k\); for \(k>m\), use the collision bound. This proves the finite upper sandwich.

Finally,
\[
\sum_{k=1}^mN_k=m(n+1)-\frac{m(m+1)}2
=n\log_dn+O_d(n),
\]
\[
\sum_{k=1}^m d^k=\frac{d(d^m-1)}{d-1}=O_d(n),
\]
and
\[
\sum_{k=m+1}^n {N_k\choose2}d^{-k}
\le \frac{n^2}{2}\sum_{k=m+1}^{\infty}d^{-k}
=\frac{n^2d^{-m}}{2(d-1)}=O_d(n).
\]
This yields the asymptotic formula.

For the maximum, every word obeys the deterministic lower-deficit bound, hence \(M_{n,d}\le T_n-L\), where \(L\) is the lower side of the sandwich. Also \(M_{n,d}\ge\mathbb E D_n\ge T_n-U\), where \(U\) is its upper side. Thus \(M_{n,d}-\mathbb E D_n\le U-L\). Using \(d^m\le n\) and \(d^{-m}\le d/n\) gives
\[
U-L\le \frac{dn}{d-1}+\frac{dn}{2(d-1)}
=\frac{3dn}{2(d-1)}.
\]

## Relation to prior literature

Flaxman, Harrow and Sorkin (2004) proved that a uniform random word has an asymptotically maximal number of distinct substrings. Their random-string comparison localizes the potentially nonoptimal substring lengths to the transition region between roughly \(\log_d n\) and \(2\log_d n\), but does not state the additive first correction above.

Ahmadi and Ward (2020) developed precise asymptotics for the number of distinct substrings at a fixed length \(k=\Theta(\log n)\), especially for nonuniform binary memoryless sources. That work concerns the level profile rather than the all-length sum considered here.

Godbole (2026) returned explicitly to \(\mathbb E D_n\). In the binary uniform case, Theorem 2.3 gives
\[
\mathbb E D_n\ge \frac{n^2}{2}\left(1-\frac{6\log_2n}{n}\right),
\]
and for uniform alphabets \(d\ge3\), equation (30) gives a loss of order \(2n\log_dn\) relative to \(n^2/2\). The present result identifies the true first logarithmic loss as \(n\log_d n\), with coefficient one, and gives a direct finite sandwich requiring no Poisson approximation.

An independent finite-computation literature also exists: OEIS A340885 records exact totals of subword complexity over binary words for small \(n\). Those data are compatible with the theorem but do not, in the material inspected, state this asymptotic correction.

## Reproducibility

`artifacts/verify_bounds.py` exhaustively enumerates all binary words through length 16 and all ternary words through length 10. It computes \(\mathbb E D_n\), the deficit \(R_{n,d}\), and both sides of the finite sandwich, and asserts the inequalities exactly up to floating-point representation of the geometric tail. Its output is recorded in `artifacts/verification.txt`.

## Limitations

The theorem assumes a fixed finite alphabet and uniform independent letters. For a nonuniform memoryless source, overlapping-match probabilities depend on the shift and the dominant transition scale need not be \(\log_d n\), so the proof does not automatically extend. The \(O_d(n)\) remainder is not resolved to a constant or periodic second-order term. No concentration or variance theorem for \(D_n\) is claimed.

The originality claim is only to the best of our knowledge. Older suffix-tree/trie analyses may contain sufficiently general path-length statements from which the same all-length correction follows as a specialization, even if the distinct-substring formulation and coefficient-one theorem are not stated explicitly in the sources located here.

## References

1. A. Godbole, *The Expected Number of Distinct Substrings in an Alphabet String*, arXiv:2609.19409 (2026). https://arxiv.org/abs/2609.19409
2. A. Flaxman, A. W. Harrow, G. B. Sorkin, *Strings with Maximally Many Distinct Subsequences and Substrings*, Electronic Journal of Combinatorics 11 (2004), R8. https://doi.org/10.37236/1761
3. L. Ahmadi, M. D. Ward, *Asymptotic Analysis of the kth Subword Complexity*, Entropy 22(2):207 (2020). https://doi.org/10.3390/e22020207
4. OEIS A340885, *Sum of subword complexity of all binary strings of length n*. https://oeis.org/A340885
