# Poisson critical window for nested finite-block modal down-interpretations

## Finding
Let \(b\ge2\) be fixed. A Boolean information state with \(n\) atomic coordinates, where \(b\mid n\), may be viewed through an independently sampled partition into \(n/b\) blocks of size \(b\). Its down-interpretation retains precisely those blocks completely present in the original state. Repeating this at fresh information states along a deterministic modal path gives an exactly solvable stochastic semantics.

Fix \(0<p<1\). For each \(n\) divisible by \(b\), let \(X_0\subseteq[n]\) contain each atom independently with probability \(p\). Let \(\mathcal P_1,\mathcal P_2,\ldots\) be independent uniform partitions of \([n]\) into blocks of size \(b\), independent of \(X_0\). Set
\[
X_s=\bigcup\{B\in\mathcal P_s:B\subseteq X_{s-1}\},\qquad K_s=|X_s|.
\]
For \(s\ge1\) write \(Y_s=K_s/b\), the number of retained blocks. Define the falling factorial \((a)_{\underline r}=a(a-1)\cdots(a-r+1)\), with \((a)_{\underline0}=1\).

**Exact transition theorem.** For all integers \(0\le k\le n\) and \(r\ge0\),
\[
\mathbb E[(Y_s)_{\underline r}\mid K_{s-1}=k]
=\left(\frac nb\right)_{\underline r}\frac{(k)_{\underline{br}}}{(n)_{\underline{br}}}
\quad(0\le br\le n),
\]
where the ratio is taken as zero if \(br>k\). Equivalently, for \(0\le j\le\lfloor k/b\rfloor\),
\[
\Pr(K_s=bj\mid K_{s-1}=k)
=\frac1{j!}\sum_{h=0}^{\lfloor k/b\rfloor-j}
\frac{(-1)^h}{h!}\left(\frac nb\right)_{\underline{j+h}}
\frac{(k)_{\underline{b(j+h)}}}{(n)_{\underline{b(j+h)}}}.
\]
All other transition probabilities vanish. Together with \(K_0\sim\operatorname{Bin}(n,p)\), this is an exact finite-depth distribution algorithm, with no independence assumption imposed between retained blocks after a projection.

**Poisson depth theorem.** Let integer depths \(t=t_n\ge1\) satisfy
\[
n p^{b^{t_n}}\longrightarrow\lambda\in(0,\infty)
\qquad(n\to\infty,\ b\mid n).
\]
Then
\[
\boxed{\quad \frac{K_{t_n}}b\ \xrightarrow{d}\ \operatorname{Poisson}(\lambda/b),\qquad
\Pr(K_{t_n}>0)\longrightarrow1-e^{-\lambda/b}.\quad}
\]
In particular, the nontrivial survival window occurs at depths \(t_n=\log_b\log_{1/p}n+O(1)\); because depths are integral, the displayed convergence is asserted along sequences fulfilling its exact scaling hypothesis, not uniformly at arbitrary fractional offsets.

## Assumptions and scope
The base lattice is the finite Boolean lattice \(L=\mathcal P([n])\). A partition \(\mathcal P\) determines the Boolean sublattice \(L_{\mathcal P}\) of unions of its blocks, with its inherited order and ordinary meet and join. Its down-interpretation is
\[
\pi_{\mathcal P}(A)=\bigvee\{C\in L_{\mathcal P}:C\subseteq A\}
=\bigcup\{B\in\mathcal P:B\subseteq A\}.
\]
This is the classical equivalence-class lower approximation; neither that operator nor its single-step idempotence is claimed new.

To realize the process as an actual many-logic modal interpretation, take worlds \(w_0,\ldots,w_t\), with the sole edges \(w_i R w_{i+1}\). Give the terminal world the full Boolean lattice and the earlier worlds the partition sublattices in reverse chronological order. Set the value of proposition \(q\) at \(w_t\) to \(X_0\), and assign any legal values at the other worlds. The one-successor clause for necessity in the cited modal semantics makes \(v_{w_0}(\Box^t q)=X_t\). The result concerns this semantic value, specifically nonbottom, **not** a designated-value satisfaction probability, and makes no assertion for general accessibility relations, arbitrary local lattices, nonuniform partitions, or varying block size.

## Proof
**1. Exact moment and inversion.** Condition on \(X_{s-1}=A\), where \(|A|=k\). Any ordered choice of \(r\) distinct blocks of the uniform partition occupies \(br\) distinct uniformly random positions. The probability that every selected block is contained in \(A\) is precisely \((k)_{\underline{br}}/(n)_{\underline{br}}\). Counting ordered selections of blocks proves the falling-factorial-moment identity. The conditional distribution depends on \(A\) only through \(k\), so \((K_s)_{s\ge0}\) is a Markov chain with this transition law. For any bounded nonnegative integer-valued \(Y\), the binomial inversion identity
\[
\mathbf1_{\{Y=j\}}=\sum_{h\ge0}\frac{(-1)^h}{j!h!}(Y)_{\underline{j+h}}
\]
holds pointwise (the sum is finite). Its conditional expectation gives the displayed formula for every transition probability. At depth one, \(Y_1\sim\operatorname{Bin}(n/b,p^b)\), which provides a normalization check.

**2. Conditional concentration before the final projection.** Write \(g_n(k)=\mathbb E[K_s\mid K_{s-1}=k]=n(k)_{\underline b}/(n)_{\underline b}\). If \(I_B\) indicates that a particular fresh partition block is included in a fixed \(k\)-set, then distinct \(I_B,I_C\) are negatively correlated: for \(k\ge2b\),
\[
\frac{(k)_{\underline{2b}}}{(n)_{\underline{2b}}}
\le\left(\frac{(k)_{\underline b}}{(n)_{\underline b}}\right)^2.
\]
Indeed, after choosing the first block, the chance that the second is also included is \((k-b)_{\underline b}/(n-b)_{\underline b}\), at most the unconditional probability \((k)_{\underline b}/(n)_{\underline b}\); for \(k<2b\) the joint probability is zero. Therefore
\[
\operatorname{Var}(Y_s\mid K_{s-1}=k)\le\mathbb E[Y_s\mid K_{s-1}=k],
\qquad \operatorname{Var}(K_s\mid K_{s-1}=k)\le b\,g_n(k).
\]
For \(k\to\infty\), uniformly with \(k\le n\), elementary product expansion gives
\[
g_n(k)=\frac{k^b}{n^{b-1}}\left(1+O_b(k^{-1}+n^{-1})\right).
\]

**3. The large intermediate states.** Set \(a_s=n p^{b^s}\). From \(a_{t_n}\to\lambda>0\) follows \(t_n=O(\log\log n)\) and
\[
a_{t_n-1}=n\left(\frac{a_{t_n}}n\right)^{1/b}
\asymp n^{1-1/b}\longrightarrow\infty.
\]
For all \(0\le s\le t_n-1\), \(a_s\ge a_{t_n-1}\). Take \(\varepsilon_n=n^{-1/12}\). Chernoff's bound gives \(K_0/a_0=1+O(\varepsilon_n)\) with probability tending to one. Inductively, on a state satisfying \(K_{s-1}/a_{s-1}=1+O((2b)^{s-1}\varepsilon_n)\), the expansion of \(g_n\) gives \(g_n(K_{s-1})/a_s=1+O(b(2b)^{s-1}\varepsilon_n+a_{t_n-1}^{-1})\). Conditional Chebyshev and the preceding variance bound yield
\[
\Pr\left(|K_s-g_n(K_{s-1})|>\varepsilon_n g_n(K_{s-1})\mid K_{s-1}\right)
\le\frac{b}{\varepsilon_n^2 g_n(K_{s-1})}
=O_b(n^{-1/3})
\]
through stages \(1\le s\le t_n-1\), uniformly on the induction's good event. There are only \(O(\log\log n)\) such stages, and \((2b)^{t_n}\varepsilon_n\to0\). A union bound and induction therefore prove
\[
K_{t_n-1}/a_{t_n-1}\xrightarrow{\Pr}1.
\]
For the possible boundary \(t_n=1\), the same conclusion is simply binomial concentration of \(K_0\), with \(a_0=np\); in fact under the stated fixed-\(p\) scaling, \(t_n\to\infty\), so the boundary does not occur eventually.

**4. Poisson law at the final stage.** Let \(k_n\) be any deterministic sequence with \(k_n/a_{t_n-1}\to1\). Then \(k_n\to\infty\), \(k_n/n\to0\), and
\[
\frac{k_n^b}{n^{b-1}}\longrightarrow\lambda.
\]
For each fixed nonnegative integer \(r\), the exact conditional moment identity yields
\[
\left(\frac nb\right)_{\underline r}\frac{(k_n)_{\underline{br}}}{(n)_{\underline{br}}}
\longrightarrow(\lambda/b)^r.
\]
These are the factorial moments of \(\operatorname{Poisson}(\lambda/b)\). The Poisson law is moment-determinate; thus \(Y_{t_n}\), conditionally on such \(k_n\), converges in distribution to that law. The concentration of \(K_{t_n-1}\) and a subsequence argument make this conditional limit unconditional. Finally, \(\Pr(Y_{t_n}=0)\to e^{-\lambda/b}\) since the variables are integer-valued and the limiting Poisson law has an isolated zero atom. This proves both assertions.

## Verification
The standalone `checker.py` computes factorial-moment transitions by exact rational arithmetic and, independently, enumerates every balanced partition for all cardinalities \(0\le k\le n\) in the nine cases \((n,b)=(2,2),(4,2),(6,2),(8,2),(3,3),(6,3),(9,3),(4,4),(8,4)\). It additionally exhaustively propagates all subsets of \([n]\) and all independently chosen partitions through multiple steps, checking the resulting distribution against the moment-based Markov recursion. The included finite examples give \(\Pr(K_2=0)=13/16\) for \((n,b,p)=(4,2,1/2)\) and \(77/80\) for \((6,3,1/2)\). These tests validate normalization and small finite cases; they are not an infinite proof. Reproduce with `python3 checker.py`; the expected last line is `ALL_CHECKS_OK`.

## Relationship to prior work
Martins, Rodrigues, Coniglio and Freire (2026), Definitions 2.1, 2.2, 2.5 and 2.6, introduce down-complete sublattices and the modal down-interpretation used here. Freire and Martins (2022) had already developed a common-lattice framework for combining modal worlds. Pawlak's classical lower approximation on equivalence classes is precisely the individual projection \(\pi_{\mathcal P}\). None of these individual operators or modal semantics is asserted novel. The additional result established here is the exact stochastic transition spectrum for **independent uniform fixed-size partitions**, together with the Poisson critical law at increasing modal depth. Existing results on one or two random partition overlaps and on rough approximations do not, from their inspected statements, imply this particular iterated-depth law. Priority is not established against all older probability or rough-set literature.

## Limitations
The theorem uses a uniform random balanced partition at each stage, independent across stages, and a Bernoulli initial valuation, with fixed block size \(b\ge2\). General partition-size laws, correlated partitions, random accessibility, and variable block size are outside its scope. The Poisson limit is along integer-depth subsequences satisfying \(np^{b^{t_n}}\to\lambda\in(0,\infty)\), and no rate of convergence is claimed. The observation concerns a semantic value rather than formula validity or independent assessment. The originality comparison is best-effort and does not exclude unpublished or differently named prior results.

## References
1. M. A. Martins, A. Rodrigues, M. E. Coniglio and A. R. Freire, *On Many-logic modal structures and information-based logics* (2026), arXiv:2605.07898, https://arxiv.org/abs/2605.07898 ; Journal of Logic, Language and Information, https://doi.org/10.1007/s10849-026-09467-x .
2. A. R. Freire and M. A. Martins, *Essay on modality across different logics* (2022), arXiv:2203.00673, https://arxiv.org/abs/2203.00673 .
3. Z. Pawlak, *Rough sets*, International Journal of Computer and Information Sciences 11 (1982), 341–356, https://doi.org/10.1007/BF01001956 .
4. C. Cornelis, M. De Cock and A. M. Radzikowska, *Fuzzy Rough Sets: From Theory into Practice*, Handbook of Granular Computing (2008), https://doi.org/10.1002/9780470724163.ch24 .
