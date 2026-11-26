# Subsequence universality at a prescribed binary transition density

## Finding

Fix integers \(n\ge2\) and \(0\le t\le m=n-1\). Choose an indexed binary word uniformly among those having exactly \(t\) unequal adjacent pairs. Write \(K\) for its binary scattered-subsequence universality index, namely the largest \(k\) for which every binary word of length \(k\) occurs as a subsequence. The alphabet remains binary even if the sampled word is constant.

The mean under this constraint is
\[
\mathbb E[K\mid t]=(m-t+1)\sum_{\substack{1\le r\le t\\r\ \mathrm{odd}}}\frac{\binom{t}{r}}{\binom{m}{r}}.
\]
Put \(d=\min(t,m-t)\). If \(d>0\), then for every \(s>0\),
\[
\Pr\bigl(|K-\mathbb E[K\mid t]|\ge s\mid t\bigr)\le 2\exp\!\left(-\frac{s^2}{2d}\right).
\]
For \(d=0\) the index is deterministic. In particular, if \(t=t_n\) is any deterministic sequence with \(t_n/(n-1)\to\rho\in[0,1]\), then under these conditional distributions
\[
\frac{K}{n}\ \xrightarrow{\mathbb P}\ \frac{\rho}{1+\rho}.
\]
Thus the limit \(1/3\) from the ordinary uniform binary-word model is replaced by a density-dependent law when the transition budget is fixed. The deviation bound uses the size of the smaller of the two edge sets, rather than the length of the word, so it also gives sub-\(\sqrt n\) concentration when the minority of edge indicators is sublinear.

## Proof

The known binary path-matching identity [1] says that \(K\) is the maximum matching size on the positional path with edges at precisely the unequal adjacent pairs. Indeed, the binary greedy arch decomposition is the standard subsequence-universality criterion [2]. Every complete arch ends in an unequal adjacent pair, and those pairs are disjoint; conversely any left-to-right list of vertex-disjoint unequal adjacent pairs supplies one copy of each letter per pair, hence supports every subsequence of length equal to the list size. A run of \(L\) present edges forms a path on \(L+1\) vertices and contributes \(\lceil L/2\rceil\) to the maximum matching size.

**Exact mean.** Every indicator vector with \(t\) present edges has two possible initial bits, so the indicators are uniform over binary vectors of length \(m\) and weight \(t\). Split the vector at its \(m-t\) zeros, allowing empty runs of ones, to obtain a uniform weak composition \((L_1,\ldots,L_q)\) of \(t\) into \(q=m-t+1\) parts. The number of such compositions is \(\binom mt\); for \(r\le t\) subtracting \(r\) from the first part shows that exactly \(\binom{m-r}{t-r}\) have \(L_1\ge r\). Thus
\[
\mathbb E\!\left[\sum_{i=1}^q\left\lceil\frac{L_i}{2}\right\rceil\right]
=q\sum_{r\ \mathrm{odd},\,1\le r\le t}\Pr(L_1\ge r)
=q\sum_{r\ \mathrm{odd},\,1\le r\le t}\frac{\binom tr}{\binom mr}.
\]
The empty sum is zero when \(t=0\); for \(t=m\) the sole part is \(m\) and the formula gives \(\lceil m/2\rceil=\lfloor n/2\rfloor\).

**Concentration.** Replacing one present edge by one absent edge changes the matching number by at most one: remove the swapped edges to obtain a common subgraph and note that adding either back changes the optimum by zero or one. Represent the smaller of the present and absent edge sets by an ordered sample of \(d\) labels from the \(m\) positions without replacement. For two possible next revealed labels with a fixed history, the remaining completions can be coupled by transposing the two labels. The resulting indicator sets either agree or differ by the single swap just considered, whether the sampled labels are present or absent. The conditional expectations over different next labels therefore have range at most one. Each difference of the Doob martingale has absolute value at most one, since its previous value averages those alternatives. Two-sided Azuma–Hoeffding yields the stated bound for \(d>0\); no sampling is required when \(d=0\).

**Density limit.** At \(0<\rho<1\), for each fixed \(r\) the ratio in the mean formula tends to \(\rho^r\), and the ratios extended by zero above \(t_n\) are bounded by \((t_n/m)^r\). For sufficiently large \(n\) a fixed geometric summable bound applies. As \((m-t_n+1)/n\to1-\rho\), the normalized mean tends to \((1-\rho)\rho/(1-\rho^2)=\rho/(1+\rho)\). The concentration bound makes \((K-\mathbb E[K\mid t_n])/n\) tend to zero in probability. At \(\rho=0\) the deterministic bound \(0\le K\le t_n\) suffices. At \(\rho=1\), the run formula and the total number of path vertices give \(\lceil t_n/2\rceil\le K\le\lfloor n/2\rfloor\), proving the endpoint by squeezing.

## Relationship to prior work and scope

The linear path-matching identity is explicitly stated in [1, Proof §1], even though the main result there concerns circular words. The reset-at-zero transfer matrix in [1, Proof §2] also gives the joint linear enumerator by starting in state zero, leaving the final state free, and omitting the cyclic parity projection. The unrefined binary law is studied in [3]. Neither the structural identity nor the joint enumeration is claimed as new. The focus here is the exact-budget mean representation and the resulting fixed-transition limit and concentration, in an ensemble where the indicators are not independent. The result addresses linear binary words only; it does not imply a conditional central limit theorem or give an optimal deviation constant.

## Reproducibility

Run `python3 verify.py` (standard library only). It uses a path matching recurrence to enumerate all subsets through eleven edge positions for the conditional means, and directly checks the single-swap bound for all subsets through eight positions. These finite computations corroborate the proof; the infinite density limit and the martingale deviation inequality are analytic.

## References

1. *Exact circular subsequence-universality spectrum of binary words*, [record 412ee9869e0f](https://github.com/Resultary/2026/tree/main/2026/10/25/SCOPE-exact-circular-subsequence-universality-spectrum-of-binary-words--412ee9869e0f), Proof §§1–2.
2. L. Barker, P. Fleischmann, K. Harwardt, F. Manea, and D. Nowotka, *Scattered Factor-Universality of Words*, [arXiv:2003.04629](https://arxiv.org/abs/2003.04629), arch factorization.
3. *Closed-form law for binary subsequence universality*, [record e77c4e8d9f37](https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-closed-form-law-for-binary-subsequence-universality--e77c4e8d9f37).
