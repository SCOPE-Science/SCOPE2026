# Complete binary length-four substring-permutation ball-size law

## Finding

Let \(n\ge4\), and let \(\mathcal P_4(x)\) consist of the distinct binary length-\(n\) words obtained from \(x\in\{0,1\}^n\) by arbitrarily permuting the symbols in one contiguous, non-wrapping window of exactly four symbols. The identity permutation is allowed. Write \(B_n(x)=|\mathcal P_4(x)|\), and let \(D_n(x)=3n-6-B_n(x)\). For each integer \(d\ge0\), define
\[
N_{n,d}=|\{x\in\{0,1\}^n:D_n(x)=d\}|.
\]

A four-state rational transfer function gives the **entire finite-length law**, for every \(n\ge4\):
\[
\sum_{n\ge4}\sum_{d\ge0}N_{n,d}s^{n-4}z^d
=2\mathbf1^{\mathsf T}A(z)(I-sA(z))^{-1}b(z),
\]
where
\[
A(z)=\begin{pmatrix}z^3&z^2&0&0\\0&0&z^2&1\\0&0&1&z^2\\1&1&0&0\end{pmatrix},\qquad
b(z)=\begin{pmatrix}z^2\\1\\1\\1\end{pmatrix},\qquad
\mathbf1=(1,1,1,1)^{\mathsf T}.
\]
This is an identity of formal power series in \(s,z\), not merely an asymptotic identity.

Its leading deficiency coefficients are, for all \(n\ge4\),
\[
\begin{aligned}
N_{n,0}&=6, & N_{n,1}&=N_{n,3}=0,\\
N_{n,2}&=6n-16, &N_{n,4}&=3(n-3)(n-4),\\
N_{n,5}&=2(n-3).
\end{aligned}
\]
Consequently the largest ball has exactly \(3n-6\) distinct outputs and is attained by **exactly six words**: the \(n\)-symbol prefixes of the two shifts of \(0101\ldots\) and the four shifts of \(00110011\ldots\). In particular, the chance of a maximal ball under a uniform random center is precisely \(6/2^n\).

If \(X_n\) is uniformly distributed on \(\{0,1\}^n\), then
\[
\mathbb E B_n(X_n)=\frac{15n-25}{8},\qquad
\operatorname{Var}(B_n(X_n))=
\begin{cases}159/64,&n=4,\\(119n-319)/64,&n\ge5.\end{cases}
\]
Furthermore,
\[
\frac{B_n(X_n)-(15n-25)/8}{\sqrt{(119n-319)/64}}
\ \Longrightarrow\ N(0,1)\qquad(n\to\infty).
\]

## Assumptions and scope

The alphabet is exactly binary, the corrupted window has length exactly four, no wraparound is allowed, and any permutation—including the identity—may be applied to that window. Multiple permutations or windows giving the same output are counted only once. Uniformity is used only for the stated probabilistic laws, not for the transfer identity or the extremal formulas. The source is the entire binary cube, not a selected error-correcting code.

## Proof

**1. Pointwise first-difference decomposition.** Fix a binary center \(x=(x_1,\ldots,x_n)\). Every distinct nonidentity output has a unique first coordinate at which it differs from \(x\). For \(i\le n-3\), first differences at \(i\) can be represented by a permutation of \(x_i,x_{i+1},x_{i+2},x_{i+3}\) changing its first bit to \(1-x_i\). Given the original quadruple \((a,b,c,d)\), the remaining three output positions must contain \(b+c+d+2a-1\) ones. Thus their number is exactly
\[
f(a,b,c,d)=\binom{3}{b+c+d+2a-1},
\]
with an out-of-range binomial coefficient defined to be zero. This representation also covers outputs first produced using a window beginning earlier: unchanged symbols preceding the first difference may be omitted from the permutation and the shorter rearrangement extended by unchanged symbols to a four-window beginning at the first difference. Outputs whose first difference is among the last three coordinates, together with the unchanged center, number
\[
h(a,b,c)=\binom3{a+b+c},
\]
where \((a,b,c)\) is the last triple. Therefore
\[
B_n(x)=\sum_{i=1}^{n-3}f(x_i,x_{i+1},x_{i+2},x_{i+3})
+h(x_{n-2},x_{n-1},x_n).
\]
The same pointwise decomposition for general window length is given in Chen--Milenkovic, arXiv:2610.15701v1, Section II; it is used here as an established starting lemma. The displayed binary four-window count also follows directly from the first-difference argument above.

**2. Exact distribution.** One has \(f\in\{0,1,3\}\) and \(h\in\{1,3\}\). Each quadruple contributes a deficiency \(3-f\), and the last triple contributes \(3-h\). A three-bit suffix is sufficient to update these weights when a bit is appended. Complementing all bits preserves both deficiencies, so the eight suffixes fall into four paired states, represented in the order \(000,001,010,011\). The matrix of transition monomials for the deficiencies is exactly \(A(z)\) above: a transition adds the bit \(e\), moves \((a,b,c)\) to \((b,c,e)\), and has weight \(z^{3-f(a,b,c,e)}\). The terminal vector has weights \(z^{3-h}\), giving \(b(z)\). All four representative states have two initial triples once complements are included. For \(n\ge4\), summing all paths of \(n-3\) transitions proves
\[
\sum_d N_{n,d}z^d=2\mathbf1^{\mathsf T}A(z)^{n-3}b(z).
\]
Summing over \(n\) proves the asserted rational transfer identity. Direct expansion of the four-by-four inverse yields the following exact coefficient identities:
\[
\begin{array}{c|cccccc}
 d&0&1&2&3&4&5\\\hline
 [z^d]\displaystyle\sum_{n\ge4}\sum_jN_{n,j}s^{n-4}z^j
 &\dfrac6{1-s}&0&\dfrac{8-2s}{(1-s)^2}&0&\dfrac{6s}{(1-s)^3}&\dfrac2{(1-s)^2}.
\end{array}
\]
Using \([s^r](1-s)^{-a}=\binom{r+a-1}{a-1}\) gives all explicit deficit counts in the finding.

**3. Sharp maximum and all equality words.** From \(f\le3\) and \(h\le3\) follows \(B_n(x)\le3n-6\). In an equality word, every four-window must have \(f=3\) and its final triple must have \(h=3\). The permitted maximal transitions on the three-bit suffixes, after deleting edges that cannot reach a valid terminal triple, form exactly two disjoint directed cycles: \(010\leftrightarrow101\) and \(001\to011\to110\to100\to001\). There are therefore two plus four possible initial phases, yielding the six stated period-two or period-four words. Conversely every listed word realizes every local maximum and the terminal maximum.

**4. Exact moments.** For independent fair input bits, put \(Y_i=f(X_i,X_{i+1},X_{i+2},X_{i+3})\) and \(H=h(X_{n-2},X_{n-1},X_n)\). Enumeration of \(16\) quadruples and their overlaps gives
\[
\mathbb EY_i=15/8,\quad \operatorname{Var}(Y_i)=87/64,\quad
\operatorname{Cov}(Y_i,Y_{i+j})=\begin{cases}11/64,&j=1,\\5/64,&j=2,\\0,&j\ge3.\end{cases}
\]
Also \(\mathbb EH=5/2\), \(\operatorname{Var}(H)=3/4\); the covariances with the final one and two \(Y\)'s are \(3/16\) and \(1/16\) respectively (earlier terms have zero covariance). Summing these exact covariances over the \(n-3\) windows gives the claimed expectation and the stated variance for \(n=4\) and \(n\ge5\).

**5. Limit law.** The bounded sequence \((Y_i)\) is stationary and three-dependent, with long-run variance
\[
\sigma^2=87/64+2(11/64+5/64)=119/64>0.
\]
Partition the centered sum into blocks of length \(\lfloor n^{1/3}\rfloor\), separated by three discarded terms. Retained blocks are independent; their maximum absolute magnitude is \(O(n^{1/3})=o(\sqrt n)\), so Lindeberg's theorem applies. The total variance of discarded terms is \(O(n^{2/3})=o(n)\) by finite dependence, while the bounded terminal \(H\) is negligible on the \(\sqrt n\) scale. The variance formula supplies the exact finite-\(n\) normalization. This proves the displayed central limit theorem.

## Verification

Run `python verify_binary_four_permutation_ball.py` and `python verify_deficit_formal.py` from the directory containing this file and the verifiers. The latter is a pure-standard-library, integer-polynomial determinant certificate: it checks, modulo \(z^6\), the exact identity between the four-state rational generating function and the asserted first six deficiency coefficients, with no finite-length truncation. The former script builds all distinct outputs by all permutations in all four-windows, without using the local counting formula. A second independently implemented suffix-dynamic-programming routine computes the entire histogram and its exact rational first two moments. Exhaustive comparison covers all \(8{,}176\) binary centers of lengths \(4\) through \(12\), while transfer-based checks cover lengths \(4\) through \(35\). Every checked length also verifies the maximizing-center phases and near-maximal counts. Recorded output is in `verification_output.txt` and `formal_coefficient_output.txt`. The infinite statements rely on the arguments above, not on finite enumeration.

## Relationship to prior work

Chen and Milenkovic, *Correcting Burst Errors with Applications to DNA-Based Data Storage*, arXiv:2610.15701v1 (publicly submitted 11 October 2026), introduced this substring-permutation model and proved the general center-dependent first-difference formula and mean; their work also derives concentration bounds and coding constructions. Those formulas and results are credited, not claimed anew. The contribution here is the exact four-window **population distribution**, a four-state generating function, full maximizer classification, polynomial near-maximal population counts, a closed finite variance, and the Gaussian fluctuation law. The cited work's center-dependent expression computationally determines individual ball sizes but does not present those evaluated global classifications and stochastic laws.

Related binary local-error metrics—single deletion, two deletions, cyclic substring shifts, and simultaneous disjoint adjacent swaps—have different sets of admissible outputs. Their extrema and random-center fluctuations therefore do not imply this exact unrestricted four-symbol permutation result. The absence of an identified matching result in searched records is not a proof of uniqueness.

## Limitations

The theorem does not address cyclic-only shifts, more than one corrupted window, arbitrary alphabet sizes, or code-size optimality. In particular, the word-maximization statement is not a bound on optimal code cardinality, and the CLT does not claim independent outputs. The mean and first-difference identity are previously known. Novelty beyond inspected work remains subject to independent literature review; no independent audit has been performed.

## References

1. Y.-P. Chen and O. Milenkovic, *Correcting Burst Errors with Applications to DNA-Based Data Storage*, arXiv:2610.15701v1, 11 October 2026, Section II, especially the formula for \(\phi_k\) and the mean. https://arxiv.org/html/2610.15701v1
2. W. Hoeffding and H. Robbins, *The central limit theorem for dependent random variables*, Duke Mathematical Journal 15 (1948), 773–780. The proof above also gives an elementary independent-block reduction, so this classical result is background rather than a missing hypothesis.
