# Variance and tail bounds for total distinct-substring complexity

## Setting

Let \(X_1,\dots,X_n\) be independent and uniform on an alphabet of size \(d\ge2\). For \(1\le k\le n\), let \(D_{n,k}\) be the number of distinct contiguous length-\(k\) substrings of \(X_1\cdots X_n\), and put
\[
D_n=\sum_{k=1}^n D_{n,k}.
\]
The exact deterministic maximum is
\[
M_{n,d}=\sum_{k=1}^n\min\{d^k,n-k+1\}.
\]
Write \(G_n=M_{n,d}-D_n\) for the deficit from this maximum.

A recent paper of Godbole asks for variance information capable of clarifying concentration of \(D_n\). Earlier work of Janson, Lonardi and Szpankowski gives a precise mean analysis for the same total complexity, while Ahmadi and Ward obtain second-moment information for fixed-length subword complexity in logarithmic-length regimes. Gaither and Ward study variance of the suffix-tree internal profile at a fixed level. The statements below concern the total statistic summed over all substring lengths.

## Theorem 1: all moments and an exponential tail for the deficit from maximum

For every real \(q\ge1\),
\[
\boxed{
\|G_n\|_q
\le
n\left(\frac d{d-1}+1+\frac q{\log d}\right).
}
\]
Consequently, with
\[
C_d=\frac d{d-1}+1+\frac1{\log d},
\]
one has \(\|G_n\|_q\le C_d qn\) for all \(q\ge1\), and hence
\[
\boxed{
\Pr\{G_n\ge un\}
\le
\exp\!\left(-\frac{u}{eC_d}\right),
\qquad u\ge eC_d.
}
\]
Thus the total number of distinct substrings lies within a linear deficit of its exact deterministic maximum with a dimension-free exponential tail for each fixed alphabet size.

### Proof

The basic identity is that any two length-\(k\) windows have equality probability exactly \(d^{-k}\), even when they overlap. Indeed, if their starting points are separated by \(r<k\), equality imposes period \(r\) on the block of \(k+r\) letters. There are \(d^r\) admissible blocks among \(d^{k+r}\), giving probability \(d^{-k}\). The nonoverlapping case is immediate.

Let \(K=\lfloor\log_d n\rfloor\). For \(k\le K\), simply
\[
0\le M_{n,d,k}-D_{n,k}\le d^k,
\]
so
\[
\sum_{k\le K}(M_{n,d,k}-D_{n,k})
\le\sum_{k=1}^K d^k
\le\frac d{d-1}n.
\]

For \(k>K\), one has \(d^k>n\ge n-k+1=:m_k\), hence \(M_{n,d,k}=m_k\). If \(c_w\) is the multiplicity of a length-\(k\) word \(w\), then
\[
G_{n,k}=m_k-D_{n,k}=\sum_w(c_w-1)_+
\le\sum_w\binom{c_w}{2}=:C_{n,k}.
\]
By the equality-probability identity,
\[
\mathbb EC_{n,k}=\binom{m_k}{2}d^{-k}\le\frac12n^2d^{-k}.
\]
Since \(0\le G_{n,k}\le n\),
\[
\mathbb E G_{n,k}^q
\le n^{q-1}\mathbb EG_{n,k}
\le\frac12n^{q+1}d^{-k}.
\]
Writing \(k=K+j\), \(j\ge1\), and using \(d^{K+1}>n\),
\[
\|G_{n,K+j}\|_q
\le n\,2^{-1/q}d^{-(j-1)/q}.
\]
Minkowski's inequality therefore yields
\[
\left\|\sum_{k>K}G_{n,k}\right\|_q
\le
\frac{n2^{-1/q}}{1-d^{-1/q}}
\le n\left(1+\frac q{\log d}\right),
\]
where \((1-e^{-x})^{-1}\le1+x^{-1}\) was used. Adding the short-length deterministic contribution proves the moment bound. Markov's inequality with \(q=u/(eC_d)\) proves the tail estimate.

## Theorem 2: variance and centered concentration

For \(n\ge2\), define
\[
L_n=\max\left\{2,\left\lceil5\log_d n\right\rceil\right\},
\qquad
c_n=\frac{L_n(L_n-1)}2.
\]
Then
\[
\boxed{
\operatorname{Var}(D_n)\le n(c_n^2+1)=O_d\!\left(n(\log n)^4\right).
}
\]
Moreover, for every \(t\ge1\),
\[
\boxed{
\Pr\{|D_n-\mathbb ED_n|\ge t\}
\le
2\exp\!\left(-\frac{t^2}{2nc_n^2}\right)
+\frac12n^{-3}.
}
\]
In particular, \(D_n\) has a subgaussian central window on scale \(\sqrt n(\log n)^2\), apart from an explicitly bounded exceptional event.

### Proof

Let \(\Lambda_n\) be the length of the longest repeated substring. The equality-probability identity and a union bound give, for every integer \(L\ge1\),
\[
\Pr\{\Lambda_n\ge L\}
\le\binom n2d^{-L}.
\]
Thus, for
\[
A_n=\{\Lambda_n<L_n\},
\]
we have
\[
p_n:=\Pr(A_n^c)\le\frac12n^{-3}.
\]

If \(x,y\in A_n\) differ in \(r\) coordinates, then for every \(k\ge L_n\) all length-\(k\) windows are distinct in both words, so the corresponding \(D_{n,k}\)'s agree. For \(k<L_n\), changing \(r\) letters replaces at most \(rk\) windows, and hence changes the number of distinct length-\(k\) windows by at most \(rk\). Therefore
\[
|D_n(x)-D_n(y)|
\le r\sum_{k=1}^{L_n-1}k
=r c_n.
\]
So \(D_n\) restricted to \(A_n\) is \(c_n\)-Lipschitz in Hamming distance.

Extend this restriction to a \(c_n\)-Lipschitz function \(F\) on the whole alphabet cube by the McShane extension theorem, then clip it to \([0,N_n]\), where \(N_n=n(n+1)/2\). Clipping preserves the Lipschitz constant and \(F=D_n\) on \(A_n\). Efron--Stein gives
\[
\operatorname{Var}(F)\le\frac12nc_n^2.
\]
Also
\[
\mathbb E(D_n-F)^2\le N_n^2p_n.
\]
Using \(\operatorname{Var}(D_n)\le2\operatorname{Var}(F)+2\mathbb E(D_n-F)^2\), together with \(N_n\le n^2\), gives
\[
\operatorname{Var}(D_n)\le nc_n^2+n.
\]

For the tail bound, \(|\mathbb ED_n-\mathbb EF|\le N_np_n\le(2n)^{-1}\). On \(A_n\), if \(|D_n-\mathbb ED_n|\ge t\) with \(t\ge1\), then \(|F-\mathbb EF|\ge t/2\). McDiarmid's inequality gives
\[
\Pr\{|F-\mathbb EF|\ge t/2\}
\le2\exp\!\left(-\frac{t^2}{2nc_n^2}\right).
\]
Adding \(p_n\) proves the claim.

## Equivalent suffix-array formulation

The standard suffix-array identity
\[
D_n=\frac{n(n+1)}2-\sum_i \operatorname{LCP}_i
\]
shows that the centered variance statement is equivalently a variance bound for the total adjacent-suffix longest-common-prefix sum. This equivalent formulation was included in the literature search; no theorem covering the total statistic above was located.

## Scope and limitations

The bounds are for independent uniform letters and fixed alphabet size. The variance upper bound is not claimed to be sharp; no matching lower bound, asymptotic variance, central limit theorem, or optimal concentration scale is proved. The constants in the deficit tail were not optimized. Extending the argument to nonuniform or dependent sources requires additional work because equal-window probabilities can depend on overlap structure.

The novelty claim is narrow and to the best of our knowledge: it concerns the all-moment/exponential deficit estimate and the variance/concentration bounds for the total all-length distinct-substring count. Precise first-moment asymptotics, the deterministic maximum, fixed-length second-moment theory, and suffix-tree profile variance are prior work. Analytic suffix-tree literature under an alternative additive-functional formulation remains the principal residual originality risk.

## Verification

`artifacts/verify_bounds.py` performs exact finite checks of the overlapping-window collision identity, the deterministic maximum formula on small alphabets, and the good-set Hamming-Lipschitz bound used above. Its output is stored in `artifacts/verification_output.txt`.

## References

1. A. Godbole, *The Expected Number of Distinct Substrings in an Alphabet String*, arXiv:2609.19409 (2026). https://arxiv.org/abs/2609.19409
2. S. Janson, S. Lonardi and W. Szpankowski, *On average sequence complexity*, Theoretical Computer Science 326 (2004), 213--227. https://doi.org/10.1016/j.tcs.2004.06.023
3. A. Flaxman, A. Harrow and G. B. Sorkin, *Strings with Maximally Many Distinct Subsequences and Substrings*, Electronic Journal of Combinatorics 11 (2004), R8. https://doi.org/10.37236/1761
4. A. Ahmadi and M. D. Ward, *Asymptotic Analysis of the kth Subword Complexity*, Entropy 22 (2020), 207. https://doi.org/10.3390/e22020207
5. J. Gaither and M. D. Ward, *Variance of the Internal Profile in Suffix Trees*, arXiv:1605.03390 (2016). https://arxiv.org/abs/1605.03390
