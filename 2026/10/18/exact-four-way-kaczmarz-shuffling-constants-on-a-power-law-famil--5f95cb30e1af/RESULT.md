# Exact four-way Kaczmarz shuffling constants on a power-law family of paired rows

## Finding
For every spectral-edge exponent \(\beta>0\), there is an explicit family of square, full-rank, row-equilibrated real systems with left Gram spectral distribution \(F(\lambda)\sim\lambda^\beta/2\) for which four standard Kaczmarz sampling policies have **exact finite-dimensional mean-square losses** and distinct sharp power-law constants. With one fixed random permutation (SS), independent reshuffling every epoch (RR), alternating a permutation with its reversal (FF), and independent uniform row draws (IID), the limiting test-error constants are respectively proportional to \(4^{-\beta}\), \(3^{-\beta}\), \(2^{-\beta}\), and \(2^{-\beta}\). In particular the sharp IID-to-SS advantage is \(2^\beta\), rather than a constant independent of the spectral-edge exponent.

Specifically, fix \(\beta>0\), integers \(N\ge1\) and \(t\ge1\), and put \(d=2N\),
\[
\lambda_j=(j/N)^{1/\beta},\qquad
c_j=1-\lambda_j,\qquad
h_j=(1+c_j^2)/2,\qquad 1\le j\le N.
\]
The two nonzero rows in coordinate pair \(j\) are
\[
\sqrt d\,e_{2j-1}^{\mathsf T},\qquad
\sqrt d\bigl(c_j e_{2j-1}+\sqrt{1-c_j^2}\,e_{2j}\bigr)^{\mathsf T}.
\]
Let \(X_N\) be the matrix comprising those \(d\) rows. For the homogeneous system \(X_Nx=0\), perform unit-relaxation Kaczmarz projection after each sampled row. Let the starting vector be independent of sampling and satisfy \(\mathbb E[x_0x_0^{\mathsf T}]=I_d/d\). Denote by \(\mathcal E_{\mathrm{scheme}}(N,t)=\mathbb E\|x_{dt}\|_2^2\) the test error after \(t\) epochs, with \(d\) updates per epoch.

Set
\[
a=(1-N^{-1})^{2Nt},\qquad
b_j=\left(1-\frac{1-h_j}{N}\right)^{2Nt}.
\]
Then the **exact** losses are
\[
\begin{aligned}
\mathcal E_{\mathrm{SS}}(N,t)&=\frac1{2N}\sum_{j=1}^N c_j^{4t-2},\\
\mathcal E_{\mathrm{RR}}(N,t)&=\frac1{2N}\sum_{j=1}^N c_j^{2t}h_j^{t-1},\\
\mathcal E_{\mathrm{FF}}(N,t)&=\frac1{2N}\sum_{j=1}^N c_j^{2t},\\
\mathcal E_{\mathrm{IID}}(N,t)&=\frac1{2N}\sum_{j=1}^N\left(2a+\frac{b_j-a}{h_j}\right).
\end{aligned}
\]
For all \(N\ge1,t\ge1\), these satisfy
\[
\mathcal E_{\mathrm{SS}}\le\mathcal E_{\mathrm{RR}}\le\mathcal E_{\mathrm{FF}}\le\mathcal E_{\mathrm{IID}}.
\]
For \(N\ge2,t\ge2\), every inequality is strict. When \(N,t\to\infty\) jointly with \(t^\beta/N\to0\),
\[
\mathcal E_{\mathrm{scheme}}(N,t)
=\frac{\Gamma(\beta+1)}{2(k_{\mathrm{scheme}}t)^\beta}(1+o(1)),
\quad (k_{\mathrm{SS}},k_{\mathrm{RR}},k_{\mathrm{FF}},k_{\mathrm{IID}})=(4,3,2,2).
\]
Hence \(\mathcal E_{\mathrm{IID}}/\mathcal E_{\mathrm{SS}}\to2^\beta\), \(\mathcal E_{\mathrm{RR}}/\mathcal E_{\mathrm{SS}}\to(4/3)^\beta\), and \(\mathcal E_{\mathrm{FF}}/\mathcal E_{\mathrm{RR}}\to(3/2)^\beta\). In particular, \(\beta=1/2\) gives the ratio \(\sqrt2\), but this ratio is not independent of \(\beta\) within the class of row-normalized power-law systems.

## Assumptions and scope
Every claim is in exact arithmetic for real square full-rank consistent systems constructed above, with \(\beta>0\), and the four explicitly defined schemes. SS chooses one uniform random permutation of all \(d\) rows and repeats it; RR chooses independent uniform permutations each epoch; FF alternates one permutation with its exact reversal; IID draws each row independently and uniformly at each of the \(dt\) steps. The starting vector is independent and isotropic in *second moment*: Gaussianity is unnecessary. The expectation includes initialization and any sampling randomness. The asymptotic is a joint limit, not a claim about fixed dimension as epoch count tends to infinity.

Every row has squared norm \(d\). The Gram matrix \(H_N=X_N^{\mathsf T}X_N/d\) has positive eigenvalues \(1-c_j=\lambda_j\) and \(1+c_j=2-\lambda_j\) for every \(1\le j\le N\); thus each finite system has a unique zero solution. For \(0<\lambda<1\), its empirical spectral CDF is
\[
F_N(\lambda)=\frac{\lfloor N\lambda^\beta\rfloor}{2N},
\]
so \(F_N(\lambda)\to\lambda^\beta/2\), with uniform error at most \(1/(2N)\) on that interval.

## Proof
**1. Exact two-row geometry.** In a given coordinate pair the two Kaczmarz error maps \(P_1,P_2\) are orthogonal rank-one projections onto two lines having absolute inner product \(c_j\). A product of \(q\ge1\) such projections has squared Frobenius norm \(c_j^{2w}\), where \(w\) is the number of changes of row label between consecutive factors. This follows by multiplying rank-one projector factorizations; repeated equal labels contribute factor one, and switches contribute \(c_j\). An unused pair has squared Frobenius norm two. Orthogonal blocks commute, and for an independent isotropic initialization the expected squared solution error is the expected squared Frobenius norm of the global update map divided by \(d\).

**2. The three permutation rules.** Each epoch processes both rows of every pair once. Under SS, the within-pair relative order is fixed, and the two row labels alternate across epochs, making \(2t-1\) switches and giving \(c_j^{4t-2}\). Under FF, every epoch reverses the preceding order; there is one within-epoch switch and no inter-epoch switch, making \(t\) switches and giving \(c_j^{2t}\). Under RR, the relative order of each fixed pair in successive independent permutations is a sequence of independent fair binary labels. There are \(t\) within-epoch switches, plus \(t-1\) independent Bernoulli\((1/2)\) indicators for equal orientation on successive epochs. Consequently
\[
\mathbb E[c_j^{2w}]=c_j^{2t}\left(\frac{1+c_j^2}{2}\right)^{t-1}=c_j^{2t}h_j^{t-1}.
\]
Independence of different pairs' relative orders is not required to calculate the sum of expected block errors.

**3. IID rows.** For each pair the number of times its rows are sampled has law \(K\sim\operatorname{Binomial}(2Nt,1/N)\). Given \(K\ge1\), the labels within that pair are IID fair bits. Their successive change indicators are IID fair bits, hence the conditional expected squared Frobenius norm is \(h_j^{K-1}\). For \(K=0\), the unmodified block contributes two. Therefore
\[
\begin{aligned}
\mathbb E\|M_j\|_F^2
&=2\Pr(K=0)+\mathbb E[\mathbf 1_{K\ge1}h_j^{K-1}]\\
&=2a+(\mathbb E[h_j^K]-a)/h_j
=2a+(b_j-a)/h_j.
\end{aligned}
\]
This gives all four finite formulas.

**4. Finite ordering.** For \(0\le c<1\) and \(h=(1+c^2)/2\), one has \(c^2\le h\le1\) and \(h\ge c\). Thus \(c^{4t-2}\le c^{2t}h^{t-1}\le c^{2t}\). For IID, \(2-1/h\ge0\), and convexity of \(u\mapsto h^u\) for \(h>0\) gives
\[
2a+(b-a)/h=b/h+(2-1/h)a
\ge b/h\ge h^{2t-1}\ge c^{2t}.
\]
Here \(b=\mathbb E[h^K]\ge h^{\mathbb E K}=h^{2t}\) by Jensen, and the last inequality follows from \(h\ge c\) and \(h\ge c^2\). Strictness follows for \(N\ge2,t\ge2\) from at least one pair having \(0<c_j<1\) and a genuinely random IID count.

**5. Sharp power-law constants.** Write \(\lambda=(j/N)^{1/\beta}\). Each of the four finite-sum summands is a nonincreasing nonnegative function \(g_{N,t}(\lambda)\) of \(\lambda\in[0,1]\), bounded at zero by two. For the IID summand this is also immediate from its conditional expectation: increasing \(c=1-\lambda\) increases every term \(h^{K-1}\), with \(K\)'s law fixed. Hence monotone right-Riemann sums give, uniformly in \(t\),
\[
\frac1{2N}\sum_{j=1}^N g_{N,t}((j/N)^{1/\beta})
=\frac12\int_0^1\!\beta\lambda^{\beta-1}g_{N,t}(\lambda)\,d\lambda+O(N^{-1}).
\]
The exact kernels under SS, RR and FF are respectively \((1-\lambda)^{4t-2}\), \((1-\lambda)^{2t}(1-\lambda+\lambda^2/2)^{t-1}\), and \((1-\lambda)^{2t}\). For IID, the kernel is \(2a+(b(\lambda)-a)/(1-\lambda+\lambda^2/2)\), with
\[
b(\lambda)=\bigl(1-(\lambda-\lambda^2/2)/N\bigr)^{2Nt}.
\]
For each fixed \(v\ge0\), substituting \(\lambda=v/t\) makes the four kernels converge in the joint limit to \(e^{-4v},e^{-3v},e^{-2v},e^{-2v}\). Each has a uniform integrable exponential upper bound on the rescaled half-line, apart from an exponentially small \(O(e^{-2t})\) IID term. For example \(b(\lambda)\le e^{-t\lambda}\), and \(1-\lambda+\lambda^2/2\ge1/2\). Dominated convergence after the substitution \(v=t\lambda\) yields
\[
\lim t^\beta\int_0^1\beta\lambda^{\beta-1}g_{N,t}(\lambda)\,d\lambda
=\beta\int_0^\infty v^{\beta-1}e^{-k v}\,dv
=\frac{\Gamma(\beta+1)}{k^\beta}.
\]
The discretization remainder is \(o(t^{-\beta})\) precisely under \(t^\beta/N\to0\). Combining the integral limit and the normalization \(1/2\) proves the stated asymptotic constants and ratios.

## Verification
The standalone `verify_pair_shuffling.py` uses exact rational arithmetic to enumerate all row-label histories for a two-row pair through four epochs and checks all four formulas. It checks the finite four-way ordering on additional nonuniform pairs, and compares the derived constants against finite power-law systems in three spectral regimes. Run:

`python3 verify_pair_shuffling.py`

The code's recorded successful run checked 386 exact enumeration histories and 28 additional finite/asymptotic comparisons (414 checks total). The asymptotic proof is analytical; these computations do not replace it.

## Relationship to prior work
Ahle, Bulatov, De Sa and Ré (2026), arXiv:2609.36271, analyze normalized Kaczmarz on power-law spectra, derive exact Gaussian-data SS/FF/IID constants at edge exponent \(1/2\), and formulate a broader shuffling-gap conjecture. The present deterministic coherent-pair family instead gives finite formulas for **all four** policies, including RR, for every \(\beta>0\), and the exact exponent-dependent advantage \(2^\beta\). This does **not** contradict their formal conjecture of a positive SS advantage depending on \(\beta\); it shows that the numerical \(\sqrt2\) ratio from their Gaussian example is not constant across all spectral-edge exponents in this model.

Yun, Sra and Jadbabaie (2021), arXiv:2103.07079, study SS-versus-RR matrix-norm inequalities and prove special cases for two factors. Those inequalities do not yield the four explicit isotropic error traces or the joint power-law constants here. Liu (2026), arXiv:2606.32005, proves general convergence-rate dominance of RR over SGD under assumptions on smooth convex objectives; those estimates do not compute these finite-horizon probabilities or leading constants. Classical alternating-projection identities underlie the local two-row calculation and are not claimed as novel by themselves.

## Limitations
These are deliberately structured diagonal-by-pairs, row-equilibrated, exactly consistent systems. The law does not assert universality over all datasets with the same spectral CDF; eigenvector/row-coherence geometry matters. The theorem concerns expected squared Euclidean error under isotropic initialization, not worst-case initialization, adaptive row sampling, nonunit relaxation, numerical rounding, wall-clock costs, or general noncommuting dense data. The leading constants require the stated joint subcritical regime; fixed finite systems eventually converge exponentially. The statistical near-Wick hypotheses used for some results in the motivating article are not invoked here. Bibliographic equivalence in broader alternating-projection or shuffling literature cannot be ruled out absolutely.

## References
1. T. D. Ahle, Y. Bulatov, C. De Sa and C. Ré, *Stochastic Optimization Under Power-Law Spectra: Tight Bounds and Shuffling Analysis*, arXiv:2609.36271v1 (first public September 28, 2026), https://arxiv.org/abs/2609.36271.
2. C. Yun, S. Sra and A. Jadbabaie, *Can Single-Shuffle SGD be Better than Reshuffling SGD and GD?*, arXiv:2103.07079 (first public March 12, 2021), https://arxiv.org/abs/2103.07079.
3. Z. Liu, *Random Reshuffling Dominates Stochastic Gradient Descent*, arXiv:2606.32005 (first public June 30, 2026), https://arxiv.org/abs/2606.32005.
4. C. De Sa, *Random Reshuffling is Not Always Better*, Advances in Neural Information Processing Systems 33 (2020), https://papers.neurips.cc/paper_files/paper/2020/hash/42299f06ee419aa5d9d07798b56779e2-Abstract.html.
