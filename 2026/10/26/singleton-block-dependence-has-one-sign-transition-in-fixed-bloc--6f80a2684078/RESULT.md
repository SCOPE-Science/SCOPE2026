# Singleton–block dependence has one sign transition in fixed-block set partitions

## Finding

Let \(n\ge k+2\), \(k\ge3\), and choose uniformly among the set partitions of \([n]\) with exactly \(k\) nonempty blocks. Write \(X_s\) for the number of blocks of size \(s\), and let \(S(m,b)\) denote the Stirling number of the second kind. For integers \(m\ge b\ge1\), define
\[
F_b(m)=\frac{mS(m-1,b-1)}{S(m,b)},\qquad F_1(m)=\mathbf1_{\{m=1\}}.
\]
For every \(2\le s\le n-k+1\), the exact covariance is
\[
\boxed{\operatorname{Cov}(X_1,X_s)=\binom ns\frac{S(n-s,k-1)}{S(n,k)}\bigl(F_{k-1}(n-s)-F_k(n)\bigr).}
\tag{1}
\]
For fixed \(n,k\), the factor before the parentheses is positive, and **the bracket is strictly increasing as \(s\) increases**. It is strictly positive at \(s=n-k+1\). Consequently, the covariance signs, in increasing block size, can only occur in the order negative, possibly a single zero, then positive. In particular a positive-to-negative reversal, two zeros, or multiple sign changes are impossible. The sign for every admissible \(s\) is decided exactly by the displayed Stirling-number ratio.

For every **fixed** \(k\ge3\), the transition occurs asymptotically at a positive fraction of \(n\). More precisely, define \(t_{n,k}\) as the smallest admissible \(s\) with nonnegative covariance. Then, as \(n\to\infty\),
\[
\boxed{\frac{t_{n,k}}{n}\longrightarrow \rho_k
=1-\frac{\log(k/(k-1))}{\log((k-1)/(k-2))}\in(0,1).}
\tag{2}
\]
Thus for any fixed \(u\in(0,\rho_k)\) and \(s_n/n\to u\), the covariance is eventually negative; for \(u\in(\rho_k,1)\) it is eventually positive. For three blocks, \(\rho_3=1-\log(3/2)/\log2\approx0.4150374993\).

Exact zero covariance is possible without independence: for \(n=6,k=3,s=3\), \(\operatorname{Cov}(X_1,X_3)=0\), but \(X_3=1\) forces \(X_1=1\) while \(X_3=0\) permits \(X_1=0\) or \(2\).

## Assumptions and scope

The underlying probability space consists of exactly \(S(n,k)\) equiprobable partitions of the labeled set \([n]\) into \(k\) unordered, nonempty blocks. Singleton count means \(X_1\); a size-\(s\) block is a subset of exactly \(s\) elements. The theorem concerns the cross-covariance for \(s\ge2\), not the variance of \(X_1\). The restriction \(n\ge k+2\) excludes the deterministic one-excess-element case; the restriction \(k\ge3\) permits multiple non-singleton sizes and makes the strictly positive endpoint nondegenerate.

The asymptotic in (2) holds with \(k\) fixed, not for \(k/n\to\alpha>0\). No joint central limit theorem or stochastic ordering of the *whole* block-size vector is claimed.

## Proof

**1. Marked-block deletion.** There are \(\binom nsS(n-s,k-1)\) pairs consisting of a partition with \(k\) blocks and a distinguished size-\(s\) block. By symmetry,
\[
\mathbb E X_s=\binom ns\frac{S(n-s,k-1)}{S(n,k)}.
\tag{3}
\]
Under this size-biased law, delete the marked size-\(s\) block. The remaining partition is uniform on \(n-s\) labels with \(k-1\) blocks. Because \(s\ge2\), deleting the block does not remove any singleton. Marking a singleton similarly gives \(\mathbb E X_1=F_k(n)\). Therefore
\[
\mathbb E(X_1X_s)=\mathbb E X_s\,F_{k-1}(n-s),
\]
which proves (1). Notice that this is a joint-moment argument; an asymptotic result for one block-size count would not establish it.

**2. Strict decrease of expected singletons with sample size at fixed block count.** Fix \(b\ge2\). Let \(a_j=1/j!\) for \(j\ge1\) and \(a_j=0\) for \(j\le0\). Put \(w_b=a^{*b}\), where \(*\) is discrete convolution. The composition weights are
\[
w_b(m)=\sum_{\substack{j_1+\cdots+j_b=m\\j_i\ge1}}\frac1{j_1!\cdots j_b!}
=\frac{b!}{m!}S(m,b).
\]
Choose a uniformly random surjection from \([m]\) onto \([b]\); its vector of ordered fiber sizes \((Y_1,\ldots,Y_b)\) has probability proportional to \(\prod_i1/Y_i!\) conditional on \(\sum_iY_i=m\). Accordingly,
\[
\Pr_m\{Y_1=j\}=
\frac{a_jw_{b-1}(m-j)}{w_b(m)}.
\tag{4}
\]
The nonzero entries of \(a\) are log-concave, with no internal zeros. Convolution preserves log-concavity for nonnegative sequences supported on integer intervals: the Toeplitz matrix \(T_a(i,j)=a_{j-i}\) has all ordered \(2\)-by-\(2\) minors nonnegative exactly when \(a\) is log-concave; since \(T_{a*b}=T_aT_b\), the Cauchy–Binet identity gives the same property for \(a*b\). Here all coefficient sums in a fixed minor are finite. Therefore \(w_{b-1}\) is log-concave.

For consecutive total sizes \(m,m+1\), the ratio of (4) at these sizes is proportional, on the common support, to
\[
\frac{w_{b-1}(m+1-j)}{w_{b-1}(m-j)}.
\]
By log-concavity this ratio is nondecreasing in \(j\); moreover \(m+1\) has the additional possible largest fiber size \(j=m-b+2\), with positive weight, whereas the largest at \(m\) is \(m-b+1\). Hence the size distribution strictly shifts upward in monotone likelihood ratio order, and in particular \(\Pr_{m+1}(Y_1=1)<\Pr_m(Y_1=1)\). By symmetry of the \(b\) fibers,
\[
F_b(m)=b\Pr_m\{Y_1=1\}
\]
is strictly decreasing for every integer \(m\ge b\).

**3. One sign change and endpoint.** For fixed \(n,k\), the residual size \(n-s\) decreases strictly as \(s\) increases. Applying step 2 to \(b=k-1\) proves that the bracket in (1) strictly increases. At maximal allowed \(s=n-k+1\), all \(k-1\) residual blocks are singletons, hence \(F_{k-1}(k-1)=k-1\). Every partition with \(n\ge k+2\) has at most \(k-1\) singleton blocks, and there exist partitions with at most \(k-2\) (two blocks of size at least two). Thus \(F_k(n)<k-1\). The last covariance is strictly positive. Strict monotonicity implies at most one zero and the stated sign order, including cases in which no negative size occurs.

**4. Fixed-\(k\) asymptotics.** Inclusion–exclusion yields
\[
S(m,b)=\frac1{b!}\sum_{j=0}^{b}(-1)^{b-j}\binom bj j^m
=\frac{b^m}{b!}\left(1+O_b\left(((b-1)/b)^m\right)\right)
\]
for each fixed \(b\ge2\), and \(S(m,1)=1\). Thus
\[
F_b(m)=\frac{mb}{b-1}\left(\frac{b-1}{b}\right)^m(1+o(1))
\tag{5}
\]
for fixed \(b\ge2\). Write \(A_k=\log((k-1)/(k-2))>0\) and \(B_k=\log(k/(k-1))>0\), with \(B_k<A_k\). For sequences \(s/n\to u\in(0,1)\), \(m=n-s\to\infty\), and (5) gives
\[
\frac1n\log\frac{F_{k-1}(n-s)}{F_k(n)}
\longrightarrow -A_k(1-u)+B_k=A_k(u-\rho_k).
\tag{6}
\]
It is negative for \(u<\rho_k\) and positive for \(u>\rho_k\). Since \(F_{k-1}(n-s)-F_k(n)\) is strictly increasing in \(s\), equation (6) forces the first nonnegative index to satisfy (2). This proves the sharp macroscopic boundary for fixed \(k\).

**5. Exact zero example.** The \(90=S(6,3)\) partitions of six elements into three blocks split by size profile into \(15\) of type \((4,1,1)\), \(60\) of type \((3,2,1)\), and \(15\) of type \((2,2,2)\). Consequently \(\mathbb E X_1=1\); \(X_3=1\) only in the middle profile, where \(X_1=1\). Hence \(\mathbb E(X_1X_3)=\mathbb E X_3\), proving zero covariance and the stated dependence.

## Verification

Run the supplied standalone Python 3 file `verify.py` with `python3 verify.py`. It requires only the Python standard library. It exhausts all restricted-growth strings for \(4\le n\le9\), checks every admissible conditional covariance against exact rational enumeration, then checks strict monotonicity and one-crossing signs for \(3\le k\le15\), \(k+2\le n\le320\), using exact Stirling recurrence values. It also checks the zero-covariance example and the fixed-\(k\) asymptotic threshold numerically for \(n=300\).

These finite tests are not a proof for unrestricted \(n,k\). The all-parameter proof is steps 1–5 above, including the log-concavity convolution lemma and the fixed-\(k\) inclusion–exclusion estimate. The ratio limit is for \(k\) fixed only.

## Relationship to prior work

Arratia and DeSalvo (arXiv:1807.03926, first public 2018-07-11) study **exactly the same fixed-block uniform set-partition law** and prove Poisson-process approximations for the full component profile in the near-diagonal regime \(n-k\asymp\sqrt n\). That regime can explain leading covariance signs for certain small sizes, but their main results do not provide the exact all-finite-parameter covariance (1), strict one-crossing statement across arbitrary size, or the fixed-\(k\) macroscopic threshold (2). Their general low-rank assembly framework (arXiv:1606.04642) is also relevant but concerns different asymptotic regimes.

Timashev (2003) studies exactly fixed-block set partitions and gives marginal size-count expectations, variances, and limiting laws. Its Russian full text was inspected at the level of the model, statement of theorems, and formulae; the corresponding English version was not obtained. An undiscovered multivariate mixed-moment or inequality in that work remains a priority risk. Mutafchiev and Savov (arXiv:1811.07951, first public 2018-11-19) analyze the **unconditioned** maximum block-size multiplicity, not fixed-\(k\) mixed covariance.

The published result “Block-size counts switch covariance sign at the Lambert-W scale” establishes covariance of a size count with the **random total block count** in unconditioned uniform set partitions. Conditioning to a deterministic \(k\) makes that total-block covariance identically zero; it does not yield (1) or (2). The classical partial Bell polynomial encodes all block-profile moments, so the mixed-moment identity in step 1 is algebraically obtainable from standard generating functions. The added assertions being assessed are strict monotonicity of the conditional singleton profile and the resulting finite-size sign classification plus fixed-\(k\) sharp threshold. A corresponding result for noncrossing partitions uses a different, composition-weighted probability law and does not imply this Stirling-weighted conclusion.

## Limitations

This result does not claim the marked-block counting identity as a new enumeration principle, nor that the one-crossing phenomenon extends to two arbitrary non-singleton block sizes. No asymptotic statement is made when \(k\) grows with \(n\). The finite threshold is computed from Stirling numbers, and its exact integer location need not have a simple closed form. Earlier complete factorial-moment or conditional occupancy literature could contain equivalent sign monotonicity; historical priority is not independently established. The proof is mathematical, but independent expert audit has not been performed.

## References

1. R. Arratia and S. DeSalvo, “Attacks and alignments: rooks, set partitions, and permutations,” arXiv:1807.03926 (first submitted 2018-07-11), later *Australasian Journal of Combinatorics*.
2. A. N. Timashev, “Random partitions of sets with a known number of blocks,” *Diskretnaya Matematika* 15 (2003), 138–148; English version *Discrete Mathematics and Applications* 13 (2003), 307–317; DOI 10.4213/dm201.
3. L. Mutafchiev and M. Savov, “On the maximal multiplicity of block sizes in a random set partition,” arXiv:1811.07951 (first submitted 2018-11-19); *Random Structures & Algorithms* 56 (2020), 867–891.
4. R. Arratia and S. DeSalvo, “Poisson and independent process approximation for random combinatorial structures with a given number of components,” arXiv:1606.04642 (first submitted 2016-06-15).
5. “Block-size counts switch covariance sign at the Lambert-W scale,” published mathematical research record, 2026-10-04, identifier 8198e77842ad, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-block-size-counts-switch-covariance-sign-at-the-lambert-w-scale--8198e77842ad.
