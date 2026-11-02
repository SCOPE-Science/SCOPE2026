# Prime-divisor onset and exact weakest-multiplier census for the twisted baker map

## Finding
Let \(M\geq2\) be an integer, let \(p\) be its smallest prime divisor, and let \(F\) be the \(M\)-dimensional twisted baker map defined below. For each \(n\geq1\), among the isolated points fixed by \(F^n\), the smallest possible modulus of an eigenvalue of the return derivative is exactly
\[
\boxed{\min_{x\in\operatorname{Fix}(F^n)\setminus N}\;\min_{\lambda\in\operatorname{spec}(DF^n(x))}|\lambda|=2^{\min(n,p)/M}.}
\]
The same minimum is attained by a point of **least period** \(n\). For \(n\leq p\), every isolated fixed point of \(F^n\) has every eigenvalue of modulus \(2^{n/M}\). The first return length at which different eigenvalue moduli occur is exactly \(n=p+1\). Thus the threshold is governed by the smallest prime divisor of dimension (\(3\) in every even dimension, but \(M+1\) in prime dimension).

In fact, the entire finite-period histogram of weakest multipliers is explicit. Fix \(1\leq t\leq n\) right-branch visits; put \(g=\gcd(M,t)\), \(s=t/g\), and \(L=n-t\). For \(r\geq0\), the exact number of isolated points fixed by \(F^n\), with precisely \(t\) right visits and weakest eigenvalue modulus \(2^{(t+gr)/M}\), is
\[
\boxed{
H_{M,n,t}(r)=\sum_{\substack{\ell_0+\cdots+\ell_{g-1}=L\\\ell_j\geq0,\ \min_j\ell_j=r}}
\binom{\ell_0+s}{s}\prod_{j=1}^{g-1}\binom{\ell_j+s-1}{s-1}.}
\]
For \(g=1\) the product is empty and the sum has its usual one-coordinate interpretation. The histogram over all nontrivial fixed points is obtained by summing these numbers over \(t=1,\ldots,n\), grouping equal moduli.

For \(n>p\), the number attaining the global minimum equals
\[
\boxed{E_M(n)=\binom np-\binom{n-p}p-\binom{n-p-1}{p-1},}
\]
using the convention \(\binom ab=0\) when \(a<b\) or \(a<0\). For \(n\leq p\), all \(2^n-1\) isolated fixed points attain the minimum. For fixed \(M\) and \(n\to\infty\),
\[
E_M(n)=\frac{n^{p-1}}{(p-2)!}+O_M(n^{p-2}),
\]
so the fraction of weakest-multiplier points decays exponentially even though the smallest normalized expansion factor \(2^{\min(n,p)/(Mn)}\) tends to one.

## Assumptions and scope
The phase space is \(X=[-1,1]\times[0,1]^{M-1}\), with two branches
\[
F(x_1,\ldots,x_M)=
\begin{cases}
(1+2x_1,x_2,\ldots,x_M),&x_1<0,\\
(1-2x_M,x_1,\ldots,x_{M-1}),&x_1\geq0.
\end{cases}
\]
The nonisolated fixed face \(N=\{x\in X:x_1=-1\}\) is excluded. An isolated point of \(\operatorname{Fix}(F^n)\setminus N\) corresponds to one binary word of length \(n\) containing at least one right symbol, by the established symbolic coding; there are \(2^n-1\) such points. Derivatives use the branch convention, with no periodic orbit on the switching face \(x_1=0\). In this finding, an eigenvalue modulus means the *absolute value of a complex eigenvalue*, not a singular value of the Jacobian.

## Proof
**1. Cyclic weighted Jacobians.** Write \(A_L=\operatorname{diag}(2,1,\ldots,1)\) and let \(A_R\) carry \(e_j\) to \(e_{j+1}\) for \(j<M\) and \(e_M\) to \(-2e_1\). For any word \(w\) with \(t\geq1\) letters \(R\), the Jacobian \(A_w\) is a signed weighted permutation with underlying permutation an advance of \(t\) places on \(M\) coordinates. It has \(g=\gcd(M,t)\) cycles, each of length \(M/g\). An \(R\) advance crosses the signed double edge once per complete revolution. Thus each cycle receives exactly \(s=t/g\) factors of magnitude two, and sign \((-1)^s\), from the \(R\) steps.

**2. Gap occupation.** Uniquely write the itinerary as
\[
w=L^{u_0}R L^{u_1}R\cdots R L^{u_t},\qquad u_j\in\mathbb Z_{\geq0},\quad \sum_{j=0}^t u_j=L=n-t.
\]
Between the \(j\)-th and \((j+1)\)-st right advances, left steps multiply a single coordinate by two. Its cyclic class is \(j\bmod g\), up to simultaneous relabeling of the classes. Therefore, with
\[
\ell_c=\sum_{\substack{0\leq j\leq t\\j\equiv c\pmod g}}u_j\quad(0\leq c<g),
\]
the absolute product of weights on the \(c\)-th permutation cycle is \(2^{s+\ell_c}\). The characteristic polynomial consequently factors as
\[
\det(zI-A_w)=\prod_{c=0}^{g-1}\left(z^{M/g}-(-1)^s2^{s+\ell_c}\right).
\]
Every eigenvalue from cycle \(c\) has modulus \(2^{(t+g\ell_c)/M}\), so the smallest modulus is \(2^{(t+g\min_c\ell_c)/M}\). These statements include negative and complex eigenvalues and do not assume diagonalizability of the real matrix over the reals.

**3. Enumerating the histogram.** Because \(g\mid t\), among the \(t+1\) gap indices \(0,\ldots,t\), residue zero occurs \(s+1\) times and every other residue occurs \(s\) times. If their aggregate left counts are prescribed as \((\ell_0,\ldots,\ell_{g-1})\), weak compositions give \(\binom{\ell_0+s}{s}\) ways for the zero-class gaps and \(\binom{\ell_j+s-1}{s-1}\) for each other class. Multiplication and restriction to \(\min\ell_j=r\) yield the asserted exact histogram. Uniqueness of the binary itinerary establishes that it counts distinct isolated periodic points, rather than merely words.

**4. The prime-divisor threshold.** If \(g=1\), there is one permutation cycle, and \(\ell_0=L\); every eigenvalue modulus is \(2^{n/M}\). If \(g\geq2\), then \(t\) shares a nontrivial divisor with \(M\), hence \(t\geq p\). The weakest modulus is therefore at least \(2^{t/M}\geq2^{p/M}\). For \(n\leq p\), either \(g=1\), or \(t=p=n\) with no left steps; all eigenvalue moduli are exactly \(2^{n/M}\). For \(n>p\), take the word \(R^pL^{n-p}\). Now \(g=p\geq2\); all left steps occupy one gap residue, leaving at least one other cycle with \(\ell_c=0\). Its weakest modulus is \(2^{p/M}\), achieving the universal lower bound. The alternative word \(RL^{n-1}\) has \(g=1\) and modulus \(2^{n/M}>2^{p/M}\), so this is the first and a genuine splitting threshold. Each displayed witness word has one cyclic run of each symbol and hence is primitive when \(n>p\); the word \(RL^{n-1}\) is primitive for \(n\leq p\) (and \(R\) is primitive for \(n=1\)). This establishes sharpness even when least period is required.

**5. Exact extremal multiplicity.** For \(n>p\), only \(t=p\) can attain the exponent \(p/M\): words with \(g=1\) have exponent \(n/M\), while \(g\geq2\) gives exponent at least \(t/M\), which exceeds \(p/M\) if \(t>p\). Here \(g=p\), and the weakest value is attained exactly when at least one of the \(p\) gap classes has no left symbols. There are \(\binom np\) words with \(p\) right symbols. Set \(L=n-p\). The weighted generating function for words with all \(p\) classes occupied is
\[
\left(\sum_{j\geq1}(j+1)z^j\right)
\left(\sum_{j\geq1}z^j\right)^{p-1}
=\frac{z^p(2-z)}{(1-z)^{p+1}}.
\]
Its coefficient of \(z^L\) is \(\binom Lp+\binom{L-1}{p-1}\), yielding the displayed subtraction formula. The fixed-\(p\) binomial expansion has leading term \(n^{p-1}/(p-2)!\), giving the asymptotic and the exponential rarity relative to \(2^n-1\).

## Verification
The accompanying standard-library program `check_weakest_spectrum.py` enumerates all binary words for \(2\leq M\leq9\) and \(1\leq n\leq9\), computes their signed monomial Jacobians directly without using the histogram formula, and checks cycle weights, per-\(t\) histograms, global minima, and extremal multiplicities. The command is `python3 check_weakest_spectrum.py`, and the expected final line is `CHECK_OK`. These finite checks are only consistency tests; the proof above covers all positive integers \(n\) and \(M\geq2\).

## Relationship to prior work
Saiki, Takahasi and Yorke introduced the twisted baker map and established its binary symbolic coding, hyperbolic periodic points and nonuniform expansion. A later public result, *Exact real-spectrum residue law for the twisted baker map*, classifies real versus nonreal eigenvalues and gives a characteristic-polynomial factorization with unspecified itinerary-dependent cycle exponents. Neither provides an enumeration of **weakest multiplier sizes across all itinerary words**, the sharp first length \(p+1\) of modulus splitting, or their exact extremal multiplicities. The present gap-occupation enumeration determines those additional integer weights and their joint counts. Takahasi's 2024 study of periodic-point distributions concerns the Dyck shift and a different heterochaos baker family, not the present twisted map.

## Limitations
The histogram counts points fixed by the \(n\)-th iterate (including points of smaller least period); only the existence witness for each sharp minimum is additionally guaranteed to have least period \(n\). The result concerns Jacobian eigenvalue moduli, not singular-value growth or the full Lyapunov distribution of Lebesgue-typical trajectories. The quantitative histogram follows partly from earlier signed-monomial structure; the precise novelty is the all-word multiplicity census and its dimension-arithmetic sharp threshold. Equivalent enumerations in uncatalogued literature remain possible.

## References
1. Y. Saiki, H. Takahasi and J. A. Yorke, *The twisted baker map*, arXiv:2202.04304, first publicly posted 2022-02-09; https://arxiv.org/html/2202.04304v3 (Sections 1–3, especially symbolic coding, Theorem B and Lemmas 2.1–2.6).
2. *Exact real-spectrum residue law for the twisted baker map*, published research record dated 2026-10-11; https://github.com/Resultary/2026/blob/main/2026/10/11/SCOPE-exact-real-spectrum-residue-law-for-the-twisted-baker-map--f1bd1c74fb3b/RESULT.md .
3. H. Takahasi, *Distributions of periodic points for the Dyck shift and the heterochaos baker maps*, arXiv:2409.01261, first publicly posted 2024-09-02; https://arxiv.org/html/2409.01261v1 .
