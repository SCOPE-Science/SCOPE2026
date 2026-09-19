# Shannon first correction and L1 concentration for distinct substrings of nonuniform i.i.d. words

## Result

Let \(X_1,\dots,X_n\) be i.i.d. on a finite alphabet \(\mathcal A\), with support probabilities \(p_a>0\), at least two symbols in the support, and Shannon entropy in nats
\[
H=-\sum_{a\in\mathcal A}p_a\log p_a>0.
\]
Let \(D_n\) be the number of distinct nonempty contiguous substrings of \(X_1\cdots X_n\). Write
\[
T_n=\frac{n(n+1)}2,
\qquad
R_n=T_n-D_n,
\]
so \(R_n\) is the deficit from counting every substring occurrence as distinct.

Then
\[
\boxed{
\mathbb E R_n=\frac{n\log n}{H}+O_{\mathbf p}(n)
}
\]
and hence
\[
\boxed{
\mathbb E D_n
=\frac{n(n+1)}2-\frac{n\log n}{H}+O_{\mathbf p}(n).
}
\]
Moreover,
\[
\boxed{
\frac{R_n}{n\log n}\longrightarrow \frac1H
\quad\text{in }L^1,
}
\]
so in particular
\[
D_n
=\frac{n(n+1)}2-\frac{n\log n}{H}+o_{L^1}(n\log n)
\]
and
\[
\frac{D_n-\mathbb E D_n}{n\log n}\longrightarrow0
\quad\text{in }L^1.
\]
The constants hidden in \(O_{\mathbf p}(n)\) may depend on the fixed source distribution \(\mathbf p\).

For the uniform source on \(d\) symbols, \(H=\log d\), so the coefficient reduces to \(n\log_d n\). This uniform specialization is not claimed as new: Janson, Lonardi and Szpankowski (2004) proved a substantially sharper expansion, including the order-\(n\) periodic term, for unbiased memoryless sources.

## Why the nonuniform coefficient is Shannon entropy

For a random length-\(k\) word \(W_k\), put
\[
S_k=-\log \mathbb P(W_k)
=\sum_{i=1}^k Z_i,
\qquad
Z_i=-\log p_{X_i}.
\]
Thus \(\mathbb E Z_i=H\). The transition between mostly repeated and mostly unique length-\(k\) blocks occurs when a typical block probability is of order \(1/n\), i.e. when \(S_k\approx\log n\). The number of lengths before this threshold is therefore \((\log n)/H\); each such length contributes order \(n\) to the repeat deficit. The proof below makes this renewal picture quantitative while controlling overlapping blocks directly.

## Proof of the expectation asymptotic

Let
\[
m_k=n-k+1,
\]
and let \(D_{n,k}\) be the number of distinct length-\(k\) blocks. Then
\[
R_n=\sum_{k=1}^n R_{n,k},
\qquad
R_{n,k}=m_k-D_{n,k}.
\]
Set
\[
z_-=-\log p_{\max}>0,
\qquad
z_+=-\log p_{\min}<\infty.
\]
Hence every increment of \(S_k\) lies in \([z_-,z_+]\).

### Lower bound

For any word \(w\) of length \(k\), the probability that \(w\) occurs among the \(m_k\) starting positions is at most
\[
\min\{1,m_k p_w\}.
\]
Therefore
\[
\mathbb E D_{n,k}
\le \sum_w \min\{1,m_kp_w\}
= m_k\,\mathbb E\min\left\{1,\frac{e^{S_k}}{m_k}\right\},
\]
which gives
\[
\mathbb E R_{n,k}
\ge \mathbb E(m_k-e^{S_k})_+.
\]
The map \(x\mapsto(x-e^{S_k})_+\) is 1-Lipschitz. If \((n-e^{S_k})_+>0\), then \(S_k<\log n\), so necessarily \(k\le (\log n)/z_-\). Consequently
\[
\mathbb E R_n
\ge n A(\log n)-O((\log n)^2),
\]
where
\[
A(t)=\sum_{k\ge1}\mathbb E(1-e^{S_k-t})_+.
\]
Define the renewal count
\[
N(t)=\max\{k:S_k\le t\}.
\]
Pathwise,
\[
A(t)=\mathbb E\left[N(t)-\sum_{k\le N(t)}e^{S_k-t}\right].
\]
Because the increments are at least \(z_-\), the exponential sum is uniformly bounded by a geometric series. If \(\tau=N(t)+1\), then
\[
t<S_\tau\le t+z_+.
\]
Since \(\tau\) is bounded for fixed \(t\), Wald's identity applies and yields
\[
H\,\mathbb E\tau=\mathbb E S_\tau=t+O(1).
\]
Thus
\[
\mathbb E N(t)=\frac{t}{H}+O(1),
\qquad
A(t)=\frac{t}{H}+O(1),
\]
and therefore
\[
\mathbb E R_n\ge \frac{n\log n}{H}-O(n).
\]

### Upper bound

Scan the \(m_k\) length-\(k\) blocks from left to right. Exactly \(R_{n,k}\) starting positions repeat a block seen earlier.

Condition on the current block being \(w\). Any preceding non-overlapping block equals it with probability \(p_w\), so the union bound gives a contribution at most
\[
\min\{1,np_w\}.
\]
Averaging over \(w\) gives
\[
\mathbb E\min\{1,ne^{-S_k}\}.
\]

It remains to control overlaps. Let \(a=p_{\max}<1\) and \(q=\sum_a p_a^2\le a\). Equality of two length-\(k\) blocks whose starts differ by \(r\in\{1,\dots,k-1\}\) forces a length-\(k+r\) word of period \(r\). Its coordinates split into \(r\) equivalence classes of sizes \(\ell_1,\dots,\ell_r\ge2\), and the matching probability is
\[
\prod_{j=1}^r\sum_a p_a^{\ell_j}.
\]
Since
\[
\sum_a p_a^\ell\le a^{\ell-2}q,
\]
the product is at most
\[
q^r a^{k-r}\le a^k.
\]
There are fewer than \(k\) possible overlap shifts. Hence
\[
\mathbb E R_{n,k}
\le n\,\mathbb E\min\{1,ne^{-S_k}\}+nk a^k.
\]
Summing over \(k\),
\[
\mathbb E R_n
\le n B(\log n)+n\sum_{k\ge1}ka^k,
\]
where
\[
B(t)=\sum_{k\ge1}\mathbb E\min\{1,e^{t-S_k}\}.
\]
Again using \(N(t)\),
\[
B(t)=\mathbb E\left[N(t)+\sum_{k>N(t)}e^{t-S_k}\right].
\]
The tail exponential sum is uniformly bounded because every increment is at least \(z_-\), while \(\mathbb E N(t)=t/H+O(1)\). Thus
\[
B(t)=\frac{t}{H}+O(1),
\]
and the geometric overlap term is finite. Therefore
\[
\mathbb E R_n\le \frac{n\log n}{H}+O(n).
\]
Combining the two bounds proves the expectation formula.

## Proof of the L1 law

Fix \(\varepsilon\in(0,1)\) and define
\[
k_-=
\left\lfloor\frac{(1-\varepsilon)\log n}{H}\right\rfloor,
\qquad
k_+=
\left\lceil\frac{(1+\varepsilon)\log n}{H}\right\rceil.
\]

For \(k\le k_-\), the previous occurrence bound implies
\[
\mathbb E D_{n,k}
\le n\,\mathbb E\min\{1,e^{S_k}/n\}.
\]
Since \(Z_i\) are bounded and \(\mathbb E S_k=kH\), Hoeffding's inequality gives, uniformly for \(k\le k_-\),
\[
\mathbb P\!\left(S_k>(1-\varepsilon/2)\log n\right)
\le n^{-c_\varepsilon}
\]
for some \(c_\varepsilon>0\), with a constant depending only on \(\varepsilon\) and the fixed source (if the threshold exceeds the maximal possible \(S_k\), the probability is simply zero). On the complementary event, \(e^{S_k}/n\le n^{-\varepsilon/2}\). Therefore
\[
\mathbb E\sum_{k\le k_-}D_{n,k}=o(n\log n).
\]
Since
\[
R_n\ge \sum_{k\le k_-}(n-k+1)-\sum_{k\le k_-}D_{n,k},
\]
it follows that
\[
\mathbb E\left[
\left(
\frac{1-\varepsilon}{H}-\frac{R_n}{n\log n}
\right)_+
\right]\to0.
\]

For the upper tail,
\[
R_n\le nk_+ + \sum_{k>k_+}R_{n,k}.
\]
Choose \(\delta>0\) so that \((1-\delta)(1+\varepsilon)>1\). The upper bound already proved gives
\[
\mathbb E R_{n,k}
\le n\left[
\mathbb P(S_k<(1-\delta)kH)
+n e^{-(1-\delta)kH}
+k a^k
\right].
\]
Hoeffding's inequality and the two geometric tails imply
\[
\mathbb E\sum_{k>k_+}R_{n,k}=o(n\log n).
\]
Hence
\[
\mathbb E\left[
\left(
\frac{R_n}{n\log n}-\frac{1+\varepsilon}{H}
\right)_+
\right]\to0.
\]
The two one-sided estimates imply
\[
\limsup_{n\to\infty}
\mathbb E\left|
\frac{R_n}{n\log n}-\frac1H
\right|
\le \frac{\varepsilon}{H}.
\]
Letting \(\varepsilon\downarrow0\) proves the \(L^1\) convergence.

## Relation to prior work

Janson, Lonardi and Szpankowski (2004) studied the same total distinct-substring count (the complexity index). For strongly mixing stationary sources they proved the leading statement \(\mathbb E D_n=n(n+1)/2-O(n\log n)\) and a bounded-in-probability deficit at the \(n\log n\) scale. For unbiased memoryless sources they proved the much sharper expansion
\[
\mathbb E D_n
=\frac{n(n+1)}2-n\log_d n+
\bigl(\text{explicit constant}+\text{periodic term}+o(1)\bigr)n.
\]
The present result is therefore not a new uniform-source asymptotic. Its contribution is the explicit Shannon coefficient \(1/H\), with an \(O(n)\) remainder, for arbitrary fixed finite nonuniform i.i.d. sources, together with the \(L^1\) first-correction law.

Gheorghiciuc and Ward (2007) precisely analyzed expected \(k\)-subword complexity, including Bernoulli-source correlation-polynomial machinery. Ahmadi and Ward (2020) analyzed first and second factorial moments of the \(k\)-subword complexity for nonuniform binary memoryless sources when \(k=\Theta(\log n)\); their transition ranges explicitly include the Shannon scale \(k\approx(\log n)/H\). They distinguish this fixed-\(k\) statistic from the all-length complexity index and do not state the all-length Shannon-coefficient formula above.

The recent preprint by Godbole (2026) studies the all-length statistic and mentions general letter probabilities in its setup, but its proved asymptotic bounds are for uniform sources. It also asks about concentration around the mean. The \(L^1\) statement here gives a coarse concentration result at the first-correction scale \(n\log n\); it does not determine the variance or the finer fluctuation scale.

## Originality scope and limitations

To the best of our knowledge, the specific claims made here are:

- the all-length nonuniform i.i.d. expectation correction \(n\log n/H\) with \(O(n)\) remainder;
- the corresponding \(L^1\) law for the repeat deficit;
- the direct overlap control showing that the Shannon renewal threshold remains decisive despite overlapping substring windows.

No originality is claimed for the uniform-source correction, for general renewal facts, for Shannon-McMillan-type entropy heuristics, or for fixed-length \(k\)-subword asymptotics.

The most relevant residual literature risks are older average-subword-complexity and entropy-from-subword-complexity work. Janson–Lonardi–Szpankowski (2004) was inspected directly and its sharper memoryless theorem is explicitly restricted to unbiased sources. Ahmadi–Ward (2020) was inspected in full-text HTML and explicitly treats the fixed-\(k\) statistic rather than the all-length complexity index. The full text of Ivanko (2008), *Exact approximation of average subword complexity of finite random words over finite alphabet*, was not inspected; the accessible 2009 exposition of that work uses a uniform random-word model. Dębowski's entropy-estimation chapter was identified and its abstract inspected, but the complete chapter was not checked line by line. These sources leave a residual possibility that an equivalent nonuniform total-complexity statement appears under different terminology.

The theorem assumes a fixed finite i.i.d. source with at least two positive-probability symbols. It does not cover growing alphabets, Markov or more general dependent sources, or source distributions varying with \(n\). The \(O(n)\) remainder is not sharpened to a constant or periodic term. The \(L^1\) result is only a first-correction-scale concentration statement and does not identify \(\operatorname{Var}(D_n)\) or the limiting fluctuation law.

## Reproducibility

`artifacts/verify_monte_carlo.py` computes exact distinct-substring counts for each simulated word using a suffix automaton and compares the empirical repeat-deficit ratio \(R_n/(n\log n)\) with \(1/H\) for two nonuniform sources. `artifacts/verification.txt` records a deterministic-seed run. The numerical check is supplementary; the theorem is proved analytically above.

## References

1. Anant Godbole, *The Expected Number of Distinct Substrings in an Alphabet String*, arXiv:2609.19409v1 (2026). https://arxiv.org/abs/2609.19409
2. Svante Janson, Stefano Lonardi, Wojciech Szpankowski, *On average sequence complexity*, Theoretical Computer Science 326 (2004), 213–227. https://doi.org/10.1016/j.tcs.2004.06.023
3. Lida Ahmadi, Mark Daniel Ward, *Asymptotic Analysis of the kth Subword Complexity*, Entropy 22 (2020), 207. https://doi.org/10.3390/e22020207
4. Irina Gheorghiciuc, Mark Daniel Ward, *On Correlation Polynomials and Subword Complexity*, DMTCS Proceedings AH (2007). https://doi.org/10.46298/dmtcs.3553
5. Łukasz Dębowski, *Estimation of Entropy from Subword Complexity*, in Challenges in Computational Statistics and Data Mining (2015/2016), 53–70. https://doi.org/10.1007/978-3-319-18781-5_4
6. Evgeny E. Ivanko, *Exact approximation of average subword complexity of finite random words over finite alphabet*, Trudy Instituta Matematiki i Mekhaniki UrO RAN 14(4) (2008), 185–189. Bibliographic record cited in Ref. 5; a 2009 exposition is available at https://doi.org/10.5220/0002273000050009
