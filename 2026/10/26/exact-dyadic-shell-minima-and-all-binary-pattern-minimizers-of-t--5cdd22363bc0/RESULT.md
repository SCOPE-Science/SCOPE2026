# Exact dyadic-shell minima and all binary-pattern minimizers of the cumulative digit deficit

## Finding
For an integer \(n\geq 0\), set \(a(0)=0\) and define \(a(n)\) to be the sum, over the integers from \(1\) through \(n\), of the number of \(1\) digits minus the number of \(0\) digits in their usual (unpadded) binary expansions. This is OEIS A268289.

For every integer \(k\geq1\), the exact minimum on the dyadic shell is
\[
\min_{2^k\leq n<2^{k+1}}a(n)=\left\lfloor\frac{2^{k+1}}3\right\rfloor.
\]
There is also a complete classification of **every** index attaining this minimum. Write an index as \(n=2^k+j-1\), and write \(j\) as an exactly \(k-1\)-digit binary word, allowing leading zeroes, when \(k\geq2\):

* For \(k=1\), the sole minimizing index is \(n=2\).
* For \(k=2h\geq2\), the minimizing words are exactly \(h-1\) consecutive pairs, each independently either `01` or `10`, followed by a final `1`. There are exactly \(2^{h-1}\) minimizing indices.
* For \(k=2h+1\geq3\), the minimizing words are exactly \(h-1\) consecutive pairs, each independently either `01` or `10`, followed by one final pair in `01`, `10`, `11`. There are exactly \(3\cdot2^{h-1}\) minimizing indices.

The first shell minima, for \(k=1,2,3,4,5,6,7\), are \(1,2,5,10,21,42,85\). At \(k=5\), the minimizing indices are \(36,37,38,40,41,42\).

## Assumptions and scope
The quantity \(a(n)\) uses **ordinary, no-leading-zero** binary representations. The range is every integer \(k\geq1\) and the half-open integer shell \([2^k,2^{k+1})\). Multiplicities count distinct minimizing integers; no asymptotic or numerical-precision hypotheses are involved.

Use the standard Takagi function \(\tau:[0,1]\to\mathbb R\),
\[
\tau(x)=\sum_{r=0}^{\infty}2^{-r}\operatorname{dist}(2^r x,\mathbb Z).
\]
At dyadic rational inputs the displayed sum is finite. We write \(H_\ell=\max_{0\leq j\leq2^\ell}2^\ell\tau(j/2^\ell)\) for \(\ell\geq1\).

## Proof
**Step 1: exact dyadic Takagi maxima.** The standard functional equations, readily derived from the series, are
\[
\tau(x)=x+\tfrac12\tau(2x)\quad(0\leq x\leq\tfrac12),\qquad
\tau(x)=1-x+\tfrac12\tau(2x-1)\quad(\tfrac12\leq x\leq1).
\]
They imply symmetry \(\tau(1-x)=\tau(x)\), and, for \(0\leq y\leq1\),
\[
\tau((1+y)/4)=\tau((2+y)/4)=\tfrac12+\tfrac14\tau(y).
\]
If \(M=\max_{[0,1]}\tau\), the first and last quarters satisfy \(\tau(x)\leq\tfrac14+M/2\) and the middle quarters satisfy \(\tau(x)\leq\tfrac12+M/4\). Therefore \(M\leq2/3\); equality holds because \(\tau(1/3)=2/3\). In particular, the outer two quarters have the stronger bound \(\tau(x)\leq1/4+(2/3)/2=7/12\). On a dyadic grid of depth \(\ell\geq3\), the middle quarters contain the point \(x=3/8\), where \(\tau(3/8)=5/8\); hence every grid maximum occurs strictly inside the middle two quarters.

The two displayed quarter identities establish a bijection of **maximizing grid points** at depth \(\ell\geq3\) with two copies of the maximizers at depth \(\ell-2\), obtained by prefixing the binary expansions by `01` or `10`. Their scaled maxima satisfy
\[
H_1=1,\qquad H_2=2,\qquad H_\ell=2^{\ell-1}+H_{\ell-2}\quad(\ell\geq3).
\]
Induction gives \(H_\ell=\lfloor2^{\ell+1}/3\rfloor\). At depth \(1\) the unique maximizing bit is `1`; at depth \(2\), the maximizing words are `01`, `10`, `11`. Repeated prefixing gives exactly the binary descriptions and cardinalities claimed above, with \(\ell=k-1\).

**Step 2: transfer to the cumulative digit deficit.** Baruchel's identity for the cumulated deficient binary digit sum is, when \(2^k\leq n<2^{k+1}\),
\[
a(n)=n-2^k\tau\left(\frac{n+1}{2^k}-1\right).
\]
Write \(n=2^k+j-1\) with \(1\leq j\leq2^k\). The expression becomes
\[
a(n)=2^k-1-2^k\left(\tau(j/2^k)-j/2^k\right).
\]
If \(1\leq j\leq2^{k-1}\), the first Takagi functional equation gives
\[
2^k\left(\tau(j/2^k)-j/2^k\right)=2^{k-1}\tau(j/2^{k-1}).
\]
Its maximum is \(H_{k-1}=\lfloor2^k/3\rfloor\) for \(k\geq2\). If \(j>2^{k-1}\), the bound \(\tau\leq2/3\) yields
\[
\tau(j/2^k)-j/2^k<\tfrac16,
\]
whereas \(H_{k-1}/2^k\geq1/4\) for \(k\geq2\). Thus no index in the upper half can attain the minimum. The exact minimum is therefore
\[
2^k-1-\left\lfloor\frac{2^k}{3}\right\rfloor
=\left\lfloor\frac{2^{k+1}}3\right\rfloor.
\]
The maximizing indices in the first half are precisely those classified in Step 1. Finally, direct evaluation gives \(a(2)=1\) and \(a(3)=3\), so the case \(k=1\) is included.

## Verification
The standalone Python 3 script `verify.py` separately accumulates digit defects by integer `bit_count()` and `bit_length()` for every integer in the first seventeen complete shells, checking each minimum and its entire minimizing set. In another loop it computes scaled Takagi values using the **integer tent-function sum** on dyadic grids of depths \(1\) through \(15\), checking the independently generated grid maximizer set at every depth. It uses only Python's standard library and terminates with an explicit `VERIFIED` message. Its finite checks support but are not substituted for the all-depth argument in the proof.

## Relationship to prior work
Baruchel (2019), Proposition 3.3, supplies the digit-deficit/Takagi identity; his Section 6.6 proves an upper bound for a dyadic-shell minimum but explicitly notes that its attainment as a minimum was not proved. The present theorem proves equality **for every shell** and classifies all minimizing indices. The pre-existing global maximum \(2/3\) and the self-similar structure of the Takagi function are not claimed as new. Krüppel (2007) studies the continuous function's extrema; Monroe (2021/2024) proves formulas for Takagi values on dyadic rationals. The finite-grid classification and its consequence for the particular integer sequence were not identified in the inspected passages. Known Takagi statements or later literature may imply this result indirectly, an originality limitation stated below.

## Limitations
This determines minima on dyadic shells, not maxima or full value distributions. The extremizer parametrization refers to the auxiliary offset \(j=n-2^k+1\), not the ordinary bits of \(n\) itself. Independent scholarly review, priority certification, and exhaustive examination of all Takagi extremal literature have not been performed. An unindexed equivalent classification could exist.

## References
1. Thomas Baruchel, *Properties of the cumulated deficient binary digit sum*, arXiv:1908.02250, first posted 6 August 2019; especially Sections 3.3 and 6.6. https://arxiv.org/html/1908.02250v3
2. OEIS A268289, *Cumulated deficient binary digit sum*. https://oeis.org/A268289
3. Laura Monroe, *Takagi Function Identities on Dyadic Rationals*, arXiv:2111.05996, initially posted 2021. https://arxiv.org/html/2111.05996v3
4. M. Krüppel, *On the extrema and improper derivatives of Takagi's continuous nowhere differentiable function*, 2007. https://www.math.uni-rostock.de/math/pub/romako/heft62/kru62.pdf
