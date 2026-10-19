# Conditional occupancy law and second-order cycle–leaf dependence in uniform unicyclic graphs

## Finding

Choose uniformly a **simple connected labeled graph** \(G_n\) with vertex set \(\{1,\ldots,n\}\) and exactly \(n\) edges, \(n\ge 3\). Let \(K_n\) be the length of its unique cycle and let \(L_n\) count degree-one vertices. Write \(h=n-k\), \(3\le k\le n\). The following statements hold.

**Exact cycle and conditional leaf laws.** With \(Z_n=\sum_{j=0}^{n-3}n^j/j!\),
\[
 \Pr(K_n=k)=\frac{n^{n-k}/(n-k)!}{Z_n}.
\]
For \(h\ge1\), conditional on \(K_n=k\), the law of \(L_n\) is exactly that of the number of unoccupied boxes among \(h\) designated boxes when \(h-1\) independent balls are thrown uniformly into \(n\) boxes. Equivalently, for \(0\le r\le h\),
\[
 \mathbb E[(L_n)_r\mid K_n=k]
 =(h)_r\left(1-\frac r n\right)^{h-1},
\]
where \((x)_r=x(x-1)\cdots(x-r+1)\) and \((x)_0=1\). For \(h=0\), \(L_n=0\) deterministically. The complete probability generating function for \(h\ge1\) is
\[
 \mathbb E[t^{L_n}\mid K_n=k]
 =\frac{(h-1)!}{n^{h-1}}[z^{h-1}]
    (e^z+t-1)^h e^{kz}.
\]
In particular, with \(a_n=1-1/n\),
\[
 m_{n,k}:=\mathbb E[L_n\mid K_n=k]
 = (n-k)a_n^{n-k-1}\quad (k<n),\qquad m_{n,n}=0.
\]
The regression \(m_{n,k}\) is **strictly decreasing** in \(k\) for \(3\le k\le n\). Thus, for \(n\ge4\) and every nonconstant nondecreasing function \(g:\{3,\ldots,n\}\to\mathbb R\),
\[
 \operatorname{Cov}(L_n,g(K_n))<0.
\]
Here nonconstant means nonconstant on the possible values \(3,\ldots,n\).

**Distinct fluctuation scales.** As \(n\to\infty\), let \(X=|Z|\) for \(Z\sim N(0,1)\), and let \(Y\sim N(0,e^{-1}-2e^{-2})\), independent of \(X\). Then
\[
 \left(\frac{K_n}{\sqrt n},\frac{L_n-n/e}{\sqrt n}\right)
 \ \Longrightarrow\ (X,Y).
\]
Nevertheless the unscaled conditional leaf regression retains a quadratic memory of the cycle: if \(k_n/\sqrt n\to x\ge0\), then
\[
 m_{n,k_n}-\frac n e\longrightarrow\frac{1-x^2}{2e}.
\]
Consequently,
\[
 \mathbb E L_n=\frac n e+o(1),\qquad
 \frac{\operatorname{Var}(L_n)}n\longrightarrow e^{-1}-2e^{-2},
 \qquad
 \frac{\operatorname{Cov}(K_n,L_n)}{\sqrt n}
 \longrightarrow-\frac{\sqrt{2/\pi}}{2e}.
\]
In particular, the two normalized statistics converge to independent limits even though their finite covariance is strictly negative and has exact order \(\sqrt n\).

## Assumptions and scope

All graphs are finite, simple, connected, and uniformly sampled from the labeled class with equal numbers of edges and vertices. The unique cycle has length at least three. Degree-one vertices are leaves, including those attached directly to the cycle; cycle vertices are never leaves. No claim concerns directed pseudographs, looped or multigraph models, or arbitrary sparse random-graph components without conditioning on connected unicyclic structure. The normal limits are weak convergence, not local limit or finite-sample Gaussianity. The exact formulas include the boundary \(K_n=n\), with the stated separate convention.

## Proof

**1. Cycle decomposition and counting.** Fix \(k\) cycle vertices. There are \((k-1)!/2\) undirected simple cycles on these vertices. Removing their cycle edges leaves an oriented rooted forest with these \(k\) vertices as roots. The classical fixed-root forest count is \(k n^{n-k-1}\); the formula also gives one forest when \(k=n\). Hence the number of graphs with cycle length \(k\) is
\[
 \binom nk\frac{(k-1)!}2\,k n^{n-k-1}
 =\frac{(n-1)!}{2}\frac{n^{n-k}}{(n-k)!}.
\]
Normalize over \(k=3,\ldots,n\) to obtain the asserted cycle law. Equivalently, \(n-K_n\) has exactly the law of \(\operatorname{Poisson}(n)\) conditioned to be at most \(n-3\).

**2. Exact leaf distribution.** Given the cycle vertex set and cycle, the rooted forest is uniform. Let \(h=n-k\ge1\), and prescribe a set of \(r\) distinct vertices off the cycle to be leaves. Delete them. They may attach only to one of the remaining \(n-r\) vertices; otherwise one prescribed vertex would have a child. Conversely each of the \((n-r)^r\) choices of their parents, together with a forest on the remaining vertices rooted at the same \(k\) cycle roots, reconstructs a distinct forest with those \(r\) prescribed leaves. The number of remaining forests is \(k(n-r)^{n-r-k-1}\) (interpreted as one when no nonroot remains). Division by \(k n^{h-1}\) gives
\[
 \Pr(\text{specified }r\text{ off-cycle vertices are leaves}\mid K_n=k)
 =\left(1-\frac r n\right)^{h-1}.
\]
For \(r=0\), this is one, as required. Multiplication by \((h)_r\) gives all factorial moments of \(L_n\). In uniform independent occupancy with \(h-1\) balls in \(n\) boxes, exactly the same joint empty-box probabilities hold for any \(r\) designated boxes. The indicator vectors therefore have identical all-subset success probabilities (inclusion-exclusion), proving equality in distribution and the generating function. Explicitly,
\[
 \Pr(L_n=\ell\mid K_n=k)
 =\binom h\ell\sum_{j=0}^{h-\ell}(-1)^j\binom{h-\ell}j
   \left(\frac{n-\ell-j}{n}\right)^{h-1},
 \qquad 0\le\ell\le h.
\]

**3. Strict negative regression.** For \(h\ge2\),
\[
 h a_n^{h-1}-(h-1)a_n^{h-2}
 =a_n^{h-2}\left(1-\frac h n\right)>0,
\]
and \(h=1\) has mean one, versus zero for \(h=0\). As \(k=n-h\), the conditional mean decreases strictly with \(k\). If \(K_n'\) is an independent copy, then
\[
 2\operatorname{Cov}(m_{n,K_n},g(K_n))
 =\mathbb E[(m_{n,K_n}-m_{n,K_n'})(g(K_n)-g(K_n'))].
\]
Every factor product is nonpositive; since each cycle length in \(3,\ldots,n\) has positive probability and \(g\) is nonconstant and nondecreasing, the expectation is strictly negative. The law of total covariance finishes this part.

**4. Half-normal cycle scale and second-order regression.** The Poisson representation and the ordinary Poisson central limit theorem yield
\[
 K_n/\sqrt n\Longrightarrow |N(0,1)|.
\]
This convergence holds with every fixed positive moment by Poisson exponential-tail bounds and the fact that \(\Pr(\operatorname{Poisson}(n)\le n-3)\to1/2\). For \(k=x\sqrt n+o(\sqrt n)\), expand
\[
 \log\left(\frac{m_{n,k}}n\right)
 =\log(1-k/n)+(n-k-1)\log(1-1/n)
 =-1+\frac{1-k^2/n}{2n}+o(n^{-1}).
\]
The remainder is uniform for \(k\le A\sqrt n\), for every fixed \(A\), and polynomially dominated after truncating at \(k\le n/2\); the complementary Poisson probability is exponentially small. Thus
\[
 m_{n,K_n}-n/e=\frac{1-(K_n/\sqrt n)^2}{2e}+o_{L^2}(1).
\]
Taking expectations and the mixed covariance with \(K_n/\sqrt n\), and using \(\mathbb EX=\sqrt{2/\pi}\), \(\mathbb EX^2=1\), \(\mathbb EX^3=2\sqrt{2/\pi}\), proves the mean and covariance asymptotics.

**5. Conditional variance and Gaussian fluctuations.** In the occupancy law, put
\[
 p=(1-1/n)^{h-1},\qquad p_2=(1-2/n)^{h-1}.
\]
The exact conditional variance is
\[
 \operatorname{Var}(L_n\mid K_n=k)
 =hp(1-p)+h(h-1)(p_2-p^2).
\]
For \(k=O(\sqrt n)\), this is \(n(e^{-1}-2e^{-2})+o(n)\), uniformly over bounded \(k/\sqrt n\).

For completeness, a standard lattice local-CLT argument for occupancy gives the required conditional normal law uniformly on that range. Take independent \(P_i\sim\operatorname{Poisson}(\lambda)\), where \(\lambda=(h-1)/n\); let \(S=\sum_{i=1}^nP_i\), and \(T=\sum_{i=1}^h\mathbf1\{P_i=0\}\). Given \(S=h-1\), \(T\) has exactly the same occupancy law as \(L_n\mid K_n=k\). With \(p_0=e^{-\lambda}\), the covariance matrix per vertex of the unconditioned vector \((S,T)\) tends to
\[
 \begin{pmatrix}
 1&-e^{-1}\\
 -e^{-1}&e^{-1}(1-e^{-1})
 \end{pmatrix}.
\]
It is positive definite, and its conditional Schur complement is \(e^{-1}-2e^{-2}>0\). To justify local conditioning rather than only a bivariate weak limit, apply two-dimensional Fourier inversion to the independent summands. Their joint support, including \((P_i,\mathbf1\{P_i=0\})=(0,1),(1,0),(2,0)\) for marked indices, spans the full integer lattice. The characteristic function has modulus strictly less than one away from its dual lattice; on a shrinking neighborhood of the origin its logarithm has a uniform quadratic expansion because \(\lambda\to1\) and \(h/n\to1\). The complementary Fourier integral is exponentially small, while the main integral gives the bivariate Gaussian local limit. Dividing by the one-dimensional Poisson local probability \(\Pr(S=h-1)\sim(2\pi n)^{-1/2}\) proves
\[
 \frac{L_n-m_{n,k}}{\sqrt n}\ \Big|\ (K_n=k)
 \Longrightarrow N(0,e^{-1}-2e^{-2})
\]
uniformly for \(k\le A\sqrt n\) for every fixed \(A\). Because \(K_n/\sqrt n\) is tight and \((m_{n,K_n}-n/e)/\sqrt n\to0\) in probability, conditioning on \(K_n\) proves the independent joint limit. Finally, the law of total variance and the exact conditional variance yield \(\operatorname{Var}(L_n)/n\to e^{-1}-2e^{-2}\). This completes the proof.

## Verification

The standalone file `verify_unicyclic.py` uses only Python's standard library. It enumerates all simple graphs with \(n\) edges and \(n\) labeled vertices for \(3\le n\le7\), selects the connected graphs, recovers unique cycle length by peeling leaves, and verifies the exact joint counts against the closed inclusion-exclusion formula. It also checks the conditional factorial moments and strict mean regression using exact integer or rational arithmetic. Executing `python verify_unicyclic.py` produced five complete-size enumeration checks and 86 exact aggregate identity checks (68,295 connected unicyclic graphs at \(n=7\)). All checks passed. Finite enumeration is corroboration, not a proof of the all-order identity or weak limits.

## Relationship to prior work

The rooted-forest factor \(k n^{n-k-1}\) and unicyclic enumeration are classical; in particular, Moon's *Counting Labelled Trees*, Sections 3.5–3.6, gives the fixed-root forest and directed unicyclic enumeration. Janson–Knuth–Łuczak–Pittel explain the rooted-tree cycle construction and connected-unicyclic generating function; those components are treated as **known** here. The proposed contribution is the **conditional leaf occupancy identity for the simple connected unicyclic ensemble**, its universal strict negative cycle–leaf regression, and the second-order dependence scale \(\sqrt n\) that coexists with independent Gaussian/half-normal leading fluctuations.

Drmota–Fusy–Kang–Kraus–Rué establish general degree-count normal limits for uniform graphs sampled from *subcritical block-stable classes*. Their graph-class ensemble is not the sequence of connected unicyclic graphs with exactly one cycle, and their results do not identify this conditional occupancy law or the mixed covariance constant. The results are therefore methodologically related, but do not directly give the stated joint law. A general previously published bivariate cycle/degree generating function could nevertheless contain these conclusions implicitly; historical priority is not independently established.

## Limitations

The probabilistic identity is exact for the specified finite simple unicyclic class, not for all cacti, connected sparse graphs of arbitrary excess, directed random mappings, or trees. The Gaussian statement is a weak limit, and does not assert finite \(n\) independence: indeed the covariance is negative. The all-finite occupancy representation uses the classical forest count, while the asymptotic analysis additionally requires standard Poisson central and lattice-local limit estimates. The literature survey is bounded and cannot rule out implicit coverage in broad enumerative texts; no independent historical-priority audit has been performed.

## References

1. J. W. Moon, *Counting Labelled Trees*, Canadian Mathematical Monographs 1 (1970), Sections 3.5–3.6. Public scan: https://www.math.ucla.edu/~pak/hidden/papers/Moon-counting_labelled_trees.pdf
2. S. Janson, D. E. Knuth, T. Łuczak, and B. Pittel, *The Birth of the Giant Component*, original public preprint 1 October 1993, arXiv:math/9310236v1, especially Section 3. https://arxiv.org/pdf/math/9310236
3. M. Drmota, É. Fusy, M. Kang, V. Kraus, and J. Rué, *Asymptotic Study of Subcritical Graph Classes*, first public preprint 24 March 2010, arXiv:1003.4699, especially Sections 1 and 8. https://arxiv.org/abs/1003.4699
4. M. Noy, *Graph Enumeration*, in *Handbook of Enumerative Combinatorics*, Chapter 6, Section 6.1, for the classical fixed-root forest count. https://web.mat.upc.edu/marc.noy/uploads/2013/05/enhandbook-419-458.pdf
