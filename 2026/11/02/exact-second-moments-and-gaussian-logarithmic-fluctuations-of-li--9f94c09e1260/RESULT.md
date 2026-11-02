# Exact second moments and Gaussian logarithmic fluctuations of limited-permutation ball volumes

## Finding

For every integer \(q\ge2\), let \(X^{(n)}\) be a uniformly random word of length \(n\) over an alphabet of size \(q\). Let \(V_n\) be the number of *distinct* outputs obtainable from \(X^{(n)}\) by one simultaneous layer of arbitrary pairwise disjoint adjacent transpositions, including the empty layer. Put \(p=1-1/q\). Then for every \(n\ge1\), the first and second moment generating functions are

\[
\sum_{n\ge1}\mathbb E[V_n]z^{n-1}=\frac{1+pz}{1-z-pz^2},\qquad
\sum_{n\ge1}\mathbb E[V_n^2]z^{n-1}
=\frac{1+2pz-p^2z^2}{1-(1+p)z-2pz^2+p^2z^3}.
\]

The first-moment identity follows from previously established ball enumerations; the **joint result here** is the exact second moment together with the following fluctuations. Set \(\alpha=(1+\sqrt{1+4p})/2\), and let \(\beta\) be the Perron eigenvalue of the positive-power, nonnegative matrix

\[
R_p=\begin{pmatrix}1&2p&p\\1&p&0\\1&0&0\end{pmatrix},
\]

or, equivalently, its largest positive characteristic root of \(\lambda^3-(1+p)\lambda^2-2p\lambda+p^2=0\). There is a constant \(K_q>0\) such that

\[
\frac{\operatorname{Var}(V_n)}{\mathbb E[V_n]^2}
\sim K_q\left(\frac{\beta}{\alpha^2}\right)^{n-1},
\qquad \beta>\alpha^2.
\]

Let \(F_0=0,F_1=1,F_{k+2}=F_{k+1}+F_k\), and define two absolutely convergent series

\[
\gamma_q=(1-p)^2\sum_{k\ge0}p^k\log F_{k+2},
\qquad
\tau_q^2=(1-p)^2\sum_{k\ge0}p^k
\big(\log F_{k+2}-(k+1)\gamma_q\big)^2>0.
\]

Couple the words as prefixes of one infinite independent uniform \(q\)-ary sequence. Then

\[
\frac{\log V_n}{n}\longrightarrow\gamma_q\quad\text{almost surely},
\qquad
\frac{\log V_n-n\gamma_q}{\sqrt n}
\xrightarrow{\ d\ }N(0,\tau_q^2).
\]

In particular, the typical exponential scale \(e^{\gamma_q n}\) is strictly smaller than the mean's exponential scale \(\alpha^n\). For \(q=2\), numerical evaluations are \(\gamma_2\approx0.285678394376\), \(\tau_2^2\approx0.057612583213\) and \(\beta/\alpha^2\approx1.043690645376\); these decimals are illustrative, not proof inputs.

## Assumptions and scope

The alphabet symbols are labeled, letters are independent and uniform, and the channel is the radius-one \(\ell_\infty\)-limited permutation channel. A legal error applies any set of nonoverlapping swaps of adjacent positions in a single layer. All allowed swaps of equal symbols are ineffective and do not create new outputs. \(V_n\) counts outputs rather than error patterns, so equal outputs are counted once. The displayed expectation is over the random center word only; no probability distribution over channel errors is assumed. The asymptotic statements fix \(q\) while \(n\) tends to infinity, and all logarithms in the limit theorem are natural.

## Proof

**1. Bernoulli boundary reduction and known output representation.** Write \(E_i=\mathbf1\{X_i\ne X_{i+1}\}\) for \(1\le i<n\). Any prescribed zero-one boundary vector containing \(a\) ones is realized by exactly \(q(q-1)^a\) words: choose the first letter, then at each boundary either repeat the preceding letter or choose one of the \(q-1\) different letters. Consequently \(E_1,\ldots,E_{n-1}\) are independent Bernoulli variables with parameter \(p\). A legal effective swap pattern is a subset of \(\{i:E_i=1\}\) with no consecutive indices. Different effective patterns yield different outputs: at the first position at which two patterns differ, a chosen effective swap puts \(X_{i+1}\), rather than \(X_i\), in the output. This standard channel identification is explicitly established in Langberg–Schwartz–Yaakobi (2015, Lemma 8 and Theorem 10) and Kovačević–Kiah–Goyal (arXiv:2509.06692v3, Proposition 4). Thus

\[
V_n=\sum_{M\subseteq\{1,\ldots,n-1\}\,\mathrm{nonconsecutive}}
\prod_{i\in M}E_i.
\]

An all-one run of \(k\) boundary indicators contributes exactly \(F_{k+2}\) independent sets of the corresponding \(k\)-vertex path. Runs separated by a zero factorize; a zero-length run contributes \(F_2=1\).

**2. First moment and second moment.** Put \(m=n-1\). The conditional matching count on a remaining boundary segment has two states according to whether the immediately previous position was selected. Its expectation evolves through \(Q_p=\left(\begin{smallmatrix}1&p\\1&0\end{smallmatrix}\right)\). Starting from the terminal all-one vector gives the first-moment recurrence \(\mu_0=1\), \(\mu_1=1+p\), \(\mu_m=\mu_{m-1}+p\mu_{m-2}\); this yields the displayed first rational generating function.

For \(V_n^2\), count ordered pairs of legal effective matchings. Record separately whether the preceding index was selected in each matching; by the symmetry of the two matchings, the four states reduce to three, \(00\), \(10/01\), \(11\). Conditional on the next independent Bernoulli flag, their expected suffix-completion vector \(v\) updates as \(v\mapsto R_pv\). Explicitly, the three rows represent the choices \((\varnothing,\varnothing)\) plus two single selections and one double selection (when neither previous selection blocks a swap); the second row permits a selection in only the unblocked matching; the last row permits neither. At zero remaining positions \(v=(1,1,1)^{\mathsf T}\), so \(s_m:=\mathbb E[V_{m+1}^2]=(R_p^m\mathbf1)_1\). Therefore

\[
s_0=1,\quad s_1=1+3p,\quad s_2=1+6p+2p^2,\quad
s_m=(1+p)s_{m-1}+2ps_{m-2}-p^2s_{m-3}\ (m\ge3),
\]

where the recurrence follows from Cayley–Hamilton and the displayed cubic characteristic polynomial. Multiplying its ordinary generating series by the recurrence denominator gives numerator \(1+2pz-p^2z^2\). In particular, the exact variance is \(s_{n-1}-\mu_{n-1}^2\).

**3. Strict exponential relative variance.** Both \(Q_p\) and \(R_p\) are irreducible and aperiodic nonnegative matrices for \(0<p<1\). Perron–Frobenius theory therefore gives \(\mu_m\sim C_1\alpha^m\) and \(s_m\sim C_2\beta^m\) for \(C_1,C_2>0\). The quadratic equation \(\alpha^2=\alpha+p\) allows direct reduction of the cubic \(f_p(\lambda)=\lambda^3-(1+p)\lambda^2-2p\lambda+p^2\):

\[
f_p(\alpha^2)=p\alpha(p-1)<0.
\]

Since \(f_p(\lambda)\to+\infty\) as \(\lambda\to+\infty\), its largest positive root \(\beta\) satisfies \(\beta>\alpha^2\). Consequently the squared mean is exponentially smaller than the second moment, and the variance ratio asymptotic holds with \(K_q=C_2/C_1^2\).

**4. Renewal proof of the logarithmic law.** Parse the independent Bernoulli indicators from left to right into successive complete blocks \(1^K0\), where each \(K\) has \(\Pr(K=k)=(1-p)p^k\) for \(k\ge0\). Complete blocks are independent and identically distributed. Their length and log-volume reward are \(L=K+1\) and \(Y=\log F_{K+2}\). The moments of \(L\) and \(Y\) of every fixed order exist, since \(K\) has a geometric tail and \(\log F_{K+2}=O(K+1)\). Hence the renewal-reward strong law gives

\[
\frac{\log V_n}{n}\to \frac{\mathbb EY}{\mathbb EL}
=(1-p)^2\sum_{k\ge0}p^k\log F_{k+2}=\gamma_q.
\]

For the central limit theorem, center complete-block rewards by \(Z=Y-\gamma_q L\), so \(\mathbb EZ=0\). The ordinary i.i.d. central limit theorem for the partial sums of \(Z\), combined with the renewal-count law and the maximal inequality controlling the random terminal count, gives the renewal-reward CLT with variance \(\mathbb EZ^2/\mathbb EL=\tau_q^2\). The unfinished final block is a trailing run of ones whose length has a uniformly geometric tail, and its log reward is bounded by a constant times that length; it is \(O_{\mathsf P}(1)\), so it does not change the \(\sqrt n\)-scaled CLT. Its length is also \(o(n)\) almost surely by a union bound and Borel–Cantelli, so it does not change the strong law. The variance is strictly positive: \(Y=0,L=1\) on \(K=0\), whereas \(\gamma_q>0\) because \(K=1\) occurs with positive probability and \(F_3=2\).

**5. Typical/mean pressure gap.** The renewal identity defining the first-moment growth rate implies \(\mathbb E[\exp(Y-L\log\alpha)]=1\). Indeed, using \(\sum_{k\ge0}F_{k+2}u^k=(1+u)/(1-u-u^2)\) with \(u=p/\alpha\), the expectation is exactly one by \(\alpha^2=\alpha+p\). On the other hand \(\mathbb E(Y-\gamma_qL)=0\); strict Jensen (the random variable is nonconstant because \(K=0,1\) both have positive probability) gives \(\mathbb E\exp(Y-\gamma_qL)>1\). The expectation is strictly decreasing in the subtracted exponent, therefore \(\log\alpha>\gamma_q\).

## Verification

The included standalone Python program `verify.py` is standard-library-only. It computes the output set directly by all permitted disjoint adjacent swaps, independently computes the independent-set dynamic program and the boundary-bit enumeration, and compares both moments exactly as rational numbers against the two rational recurrences. It exhausts all words for \(q=2\) through \(n=11\), \(q=3\) through \(n=8\), and \(q=4\) through \(n=7\): 35,778 word cases. It also tests the second-moment matrix recurrence for \(q\in\{2,3,4,7,100\}\) through \(n=79\), checks the cubic separation numerically, and evaluates the convergent renewal constants. These checks corroborate the algebra; the infinite all-length formulas and limit laws rest on the mathematical proof above, not finite experiments. Run `python3 verify.py` and compare stdout with `verify-output.txt`.

## Relationship to prior work

Langberg–Schwartz–Yaakobi (ISIT 2015, Lemma 8 and Theorem 10) established the anti-run product of Fibonacci numbers for an individual ball. Kovačević–Kiah–Goyal (arXiv:2509.06692v3, Proposition 4 and Proposition 6) identified effective disjoint swaps with graph independent sets and gave averaged ball counts, including the first moment. Those are used, not claimed to be new. The q-ary coding studies of Ben Shimon and Zabokritskiy (arXiv:2606.26905 and arXiv:2607.19566) concern collision criteria, constructive code rates and extinction depth, not the distribution of typical error-ball volumes. The additional assertion here is the all-length second moment, strict exponential relative-variance growth, and explicit almost-sure and Gaussian logarithmic fluctuations for a random center. The 2017 expanded journal treatment of the channel was identified but its full text was not accessible in this inspection; it remains a priority risk.

## Limitations

Only the uniformly random center and the single simultaneous layer of disjoint swaps are treated. The result does not cover nonuniform stationary inputs, successive overlapping swaps, general displacement radius, or a random distribution of channel outputs. The proof is mathematical and independently reproducible but no independent mathematical audit or exhaustive publication-priority verification has been performed. Inaccessible published full text may contain partially overlapping claims.

## References

1. M. Langberg, M. Schwartz, E. Yaakobi, *Coding for the \(\ell_\infty\)-Limited Permutation Channel*, ISIT 2015, pp. 1936–1940, https://yaakobi.net.technion.ac.il/files/2015/11/53_Perm_Channel_ISIT15.pdf; expanded journal version, *IEEE Transactions on Information Theory* 63 (2017), DOI https://doi.org/10.1109/TIT.2017.2762676.
2. M. Kovačević, H. M. Kiah, K. Goyal, *Bounds on Codes Correcting Adjacent Transpositions*, first public version September 8, 2025, arXiv:2509.06692; full third version https://arxiv.org/html/2509.06692v3.
3. N. Ben Shimon, A. L. Zabokritskiy, *A \(q\)-ary Local Criterion for the Radius-One Limited Permutation Channel and Almost-Optimal Binary Block-Concatenation Codes*, first posted June 25, 2026, arXiv:2606.26905, https://arxiv.org/abs/2606.26905.
4. N. Ben Shimon, A. L. Zabokritskiy, *Extinction Depth and \(q\)-ary Error-Correcting Codes for the Limited Permutation Channel*, first posted July 21, 2026, arXiv:2607.19566, https://arxiv.org/abs/2607.19566.
