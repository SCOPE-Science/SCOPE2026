# A Rayleigh limit law for the least absent odd part of an overpartition

## Finding

Choose an overpartition \(\Pi_n\) of \(n\) uniformly from all \(\overline p(n)\) overpartitions, for each integer \(n\ge1\). Let \(M_n\) be its **least absent positive odd part**: the smallest element of \(\{1,3,5,\ldots\}\) that is missing from \(\Pi_n\), counting a part as present whether overlined or not. This is the odd-restricted *search*, not the ordinary minimal excludant multiplied by an oddness indicator.

As \(n\to\infty\), the random variable \(Y_n=M_n/n^{1/4}\) converges in distribution to a Rayleigh-type law \(Y\) characterized, for all real \(y\ge0\), by
\[
\Pr(Y>y)=\exp(-\pi y^2/16),\qquad f_Y(y)=\frac{\pi y}{8}\exp(-\pi y^2/16)\quad(y>0).
\]
In fact **all positive real moments converge**: for every fixed real \(r>0\),
\[
\lim_{n\to\infty}\mathbb E\big[(M_n/n^{1/4})^r\big]
=\left(\frac{16}{\pi}\right)^{r/2}\Gamma(1+r/2).
\]
Thus \(\mathbb E M_n\sim 2n^{1/4}\) and \(\operatorname{Var}(M_n)\sim(16/\pi-4)n^{1/2}\).

The result also supplies an exact finite-size survival identity. Put
\[
P(q)=\prod_{j\ge1}\frac{1+q^j}{1-q^j},\qquad
h_m(q)=\prod_{i=1}^m\frac{2q^{2i-1}}{1+q^{2i-1}}
\quad(m\ge0),
\]
with the empty product equal to \(1\). For every \(n\ge1\) and \(m\ge0\),
\[
\Pr(M_n>2m-1)=\frac{[q^n]P(q)h_m(q)}{[q^n]P(q)}.
\]
For \(m=0\), interpret the left side as \(1\). Equivalently, the numerator is \(2^m[q^{n-m^2}]P(q)\prod_{i=1}^m(1+q^{2i-1})^{-1}\), where a negative-index coefficient is zero.

## Assumptions and scope

An overpartition is an integer partition where the first occurrence of each part size may be overlined; the total size of the parts is \(n\). The probability measure is uniform on **all** overpartitions of \(n\), not just overpartitions with odd parts. The statistic searches odd candidate sizes only, and any overlined or non-overlined occurrence makes that size present. The distributional assertion covers the complete nonnegative real line, and moment convergence covers each fixed real exponent \(r>0\), not exponents depending on \(n\).

This distinction of statistics is essential: an odd-restricted search is different from retaining the ordinary mex only when the ordinary mex happens to be odd, and it differs from counting only non-overlined occurrences or restricting all parts of the overpartition to be odd.

## Proof

**1. Exact coefficient identity.** A part size \(j\) occurs with arbitrary multiplicity and has local factor \(1+2q^j+2q^{2j}+\cdots=(1+q^j)/(1-q^j)\). Forcing its presence replaces that factor by \(2q^j/(1-q^j)\), a ratio of \(2q^j/(1+q^j)\). Requiring every positive odd size through \(2m-1\) to occur is precisely \(M_n>2m-1\). Multiplication gives the exact identity. Moreover \(\sum_{i=1}^m(2i-1)=m^2\), giving the stated coefficient form.

**2. Boltzmann representation.** For \(t>0\), put \(q=e^{-t}\) and let \((G_j,B_j)_{j\ge1}\) be mutually independent, where \(G_j\) has geometric law \(\Pr(G_j=k)=(1-q^j)q^{jk}\) for \(k\ge0\), and \(B_j\) is Bernoulli with \(\Pr(B_j=1)=q^j/(1+q^j)\). Set \(S=\sum_{j\ge1}j(G_j+B_j)\). The Boltzmann weights give \(\Pr(S=n)=\overline p(n)q^n/P(q)\), so conditioning on \(S=n\) makes the overpartition uniform.

For each forced positive odd \(j\), conditioning \(G_j+B_j\ge1\) produces the law \(1+G'_j\), where \(G'_j\) is again geometric with parameter \(q^j\). Indeed the unconditioned probabilities for positive multiplicities are \(2(1-q^j)q^{jk}/(1+q^j)\), \(k\ge1\). Hence, given simultaneous presence of odd sizes \(1,3,\ldots,2m-1\), the total-size variable \(S_m\) can be represented as the sum of **all** the original independent geometric contributions \(jG_j\), plus Bernoulli contributions \(jB_j\) from all sizes **outside** that odd set, plus the deterministic shift \(m^2\). Therefore, for every \(t>0\),
\[
\Pr(M_n>2m-1)=h_m(e^{-t})\,\frac{\Pr_t(S_m=n)}{\Pr_t(S=n)}.
\]
This exact conditioning identity is the key to the rigorous transfer from independent Boltzmann parts to fixed size.

**3. Saddle and variance.** Choose the unique \(t_n>0\) with \(\mathbb E_{t_n}S=n\) (strict decrease of the mean from infinity to zero guarantees existence). As \(t\downarrow0\),
\[
\begin{aligned}
\mu(t):=\mathbb E_tS
 &=\sum_{j\ge1}\frac{j}{\sinh(tj)}
 =\frac{\pi^2}{4t^2}+O(t^{-1}),\\
\sigma^2(t):=\operatorname{Var}_t(S)
 &=-\mu'(t)\sim\frac{\pi^2}{2t^3}.
\end{aligned}
\]
For the first asymptotic, use the Riemann sum for the smooth, integrable function \(u/\sinh u\) and \(\int_0^\infty u/\sinh u\,du=\pi^2/4\); differentiation can be justified independently by the analogous variance Riemann sum. Consequently \(t_n\sim\pi/(2\sqrt n)\) and \(\sigma(t_n)\asymp t_n^{-3/2}\).

For \(m\le Kt^{-1/2}\), where \(K>0\) is fixed, the conditioning-induced mean shift and variance reduction satisfy
\[
0\le\mathbb E_t S_m-\mu(t)=\sum_{\substack{j<2m\\j\text{ odd}}}\frac{j}{1+e^{-tj}}=O_K(t^{-1})=o(\sigma(t)),
\]
\[
0\le\sigma^2(t)-\operatorname{Var}_t(S_m)
=\sum_{\substack{j<2m\\j\text{ odd}}}\frac{j^2e^{-tj}}{(1+e^{-tj})^2}
=O_K(t^{-3/2})=o(\sigma^2(t)).
\]

**4. Uniform lattice local limit and a global bound.** Both \(S\) and every \(S_m\) contain the same independent geometric sum \(\sum_{j\ge1}jG_j\). Its characteristic-function modulus is
\[
F_t(\theta)=\prod_{j\ge1}\frac{1-e^{-tj}}{|1-e^{-tj+ij\theta}|}.
\]
There are constants \(c,C>0\) for small \(t\) such that, uniformly for \(-\pi\le\theta\le\pi\),
\[
F_t(\theta)\le
\begin{cases}
\exp(-c\theta^2/t^3),&|\theta|\le t,\\
\exp(-c/t),&t\le|\theta|\le\pi.
\end{cases}
\]
Here are explicit elementary justifications rather than an appeal to an unstated local limit theorem. For \(|\theta|\le t\), use \(1\le j\le\lfloor1/t\rfloor\); then \(|j\theta|\le1\), and the squared factor denominator ratio equals \(1+4e^{-tj}\sin^2(j\theta/2)/(1-e^{-tj})^2\), which is at least \(1+c(j\theta)^2\) for these \(j\). Summing logarithms gives \(-c\theta^2\sum_{j\le1/t}j^2\le-c'\theta^2/t^3\). For \(t\le|\theta|\le\pi\), take \(J=\lceil K_0/t\rceil\) with a sufficiently large fixed \(K_0\). The elementary geometric-series bound \(|\sum_{j=1}^J e^{ij\theta}|\le1/|\sin(\theta/2)|\le\pi/|\theta|\) yields \(\sum_{j=1}^J\sin^2(j\theta/2)\ge J/2-\pi/(2t)\ge J/4\). Since \(e^{-tj}\ge e^{-K_0-1}\) on this range, multiplying the geometric factors gives \(\exp(-c'J)\le\exp(-c''/t)\). In particular,
\[
\int_{-\pi}^{\pi}F_t(\theta)\,d\theta=O(t^{3/2}).
\]

The centered third cumulant remainders of \(S\) and \(S_m\), uniformly in \(m\), are bounded by \(O(t^{-4}|\theta|^3)\) on \(|\theta|\le Rt^{3/2}\) for fixed \(R\); this follows by summing the independent geometric and Bernoulli third absolute centered moments. Thus their characteristic functions have the Gaussian central expansion at scale \(\sigma(t)^{-1}\), uniformly for \(m\le Kt^{-1/2}\). Fourier inversion, the two displayed off-center bounds and the mean/variance estimates from Step 3 give
\[
\Pr_{t_n}(S=n)\sim\frac1{\sqrt{2\pi}\,\sigma(t_n)},
\qquad
\sup_{0\le m\le Kt_n^{-1/2}}
\left|\sqrt{2\pi}\,\sigma(t_n)\Pr_{t_n}(S_m=n)-1\right|\to0.
\]
For arbitrary \(m\ge0\), Fourier inversion and the **common geometric factor** give \(\Pr_{t_n}(S_m=n)\le Ct_n^{3/2}\), whereas \(\Pr_{t_n}(S=n)\ge ct_n^{3/2}\) for large \(n\). Consequently the probability ratio in Step 2 is bounded by an absolute constant for **all** \(m\).

**5. Sharp limiting survival.** The forced-presence probability obeys the exact identity
\[
h_m(e^{-t})=\prod_{i=1}^m\frac{e^{-t(2i-1)/2}}{\cosh(t(2i-1)/2)},
\quad
\log h_m(e^{-t})=-\frac{tm^2}{2}+O(t^2m^3)
\]
uniformly for \(m=O(t^{-1/2})\). Set \(m=\lfloor y n^{1/4}/2\rfloor\) for fixed \(y>0\); integer rounding has no effect. By Step 4 the conditional/local-limit ratio tends to \(1\), and the leading logarithm tends to \(-\pi y^2/16\). Since \(M_n\) is odd and positive, this proves the stated survival limit at every \(y\ge0\) (at zero, the survival is exactly \(1\)). Differentiating the limiting survival determines the stated limiting density.

**6. Uniform tails and every moment.** Because \(\cosh u\ge1\), Step 5 gives \(h_m(e^{-t})\le e^{-tm^2/2}\) for every \(m,t\). The all-\(m\) probability-ratio bound from Step 4 implies
\[
\Pr(M_n>2m-1)\le C\exp(-t_nm^2/2),\qquad m\ge0,
\]
for all sufficiently large \(n\). Since \(t_n\sqrt n\to\pi/2\), the rescaled survival functions admit a uniform Gaussian-tail majorant \(C'e^{-c'y^2}\). Hence \((M_n/n^{1/4})^r\) is uniformly integrable for each fixed real \(r>0\). The layer-cake identity, dominated convergence, and \(\int_0^\infty r y^{r-1}e^{-\pi y^2/16}\,dy=(16/\pi)^{r/2}\Gamma(1+r/2)\) prove all moment limits. The stated first and second moments yield the variance constant.

## Verification

The accompanying `verify.py` uses integer power-series arithmetic in two genuinely different ways: (a) multiplying the local factors for unrestricted and forced-positive odd parts directly, and (b) dividing the complete overpartition series by \(\prod_{i\le m}(1+q^{2i-1})\), then shifting and multiplying by \(2^m\). It compares every coefficient for \(0\le n\le170\) and \(0\le m\le13\), a total of \(2394\) exact comparisons, verifies each coefficient is a count between zero and \(\overline p(n)\), and checks monotonicity in \(m\). Invoke with `python3 verify.py`. These finite calculations check the exact identity but cannot certify the limiting law; the latter is proved in Steps 2–6.

## Relationship to prior work

Bhoria, Eyyunni and Santra, *On the number of missing integers in partitions* (arXiv:2604.12557, April 14, 2026), study the complete set and number of missing part sizes for overpartitions. The first missing odd size is a complementary order statistic; their enumeration does not determine its distribution.

Veena V S and S N Fathima, *On the sum of odd minimal excludants over overpartitions* (arXiv:2609.32207, first public September 26, 2026), study the **different** statistic that retains the ordinary smallest absent positive integer only if it is odd. They explicitly distinguish this from an odd-restricted search. Their results concern its summatory generating function, congruences and first-moment asymptotic; they do not give the distribution of the present odd-restricted-search statistic. The difference is substantive: an overpartition missing \(2\) but containing \(1\) and \(3\) has ordinary mex \(2\), hence odd-indicator mex zero, but least absent odd part at least \(5\).

Dhar, Mukhopadhyay and Sarma, *On new minimal excludants of overpartitions related to some \(q\)-series of Ramanujan* (arXiv:2409.06121, first public September 10, 2024), define an odd-restricted overpartition mex **for overpartitions containing only odd parts**, rather than all overpartitions, and establish generating-function identities. Chern and Xia (arXiv:2507.14431, July 19, 2025) prove moment asymptotics for generalized mex in **ordinary integer partitions**, not overpartitions. Donato (arXiv:2507.04402, July 6, 2025) considers sums for the overlined-only and all-part **ordinary mex**, not the first absent odd part over all overpartitions. Bhoria, Eyyunni and Santra (arXiv:2604.12557, April 14, 2026) count total missing integers in partitions and overpartitions, a distinct statistic.

No equivalent law or covering theorem was found in the searches described in `AUDIT.json`, but negative searches cannot prove global priority.

## Limitations

The theorem concerns the uniform fixed-size overpartition model and a single odd-restricted presence statistic, not overpartitions restricted to odd parts, the parity-filtered ordinary mex, or thresholds growing with \(n\) faster than a fixed multiple of \(n^{1/4}\). The result is an unrestricted mathematical proof for each fixed moment exponent; the finite verifier checks only low degrees. An earlier result under another formulation of partition Gibbs conditioning or a general combinatorial limit theorem might subsume this specialization; independent priority review is not performed.

## References

1. S. C. Bhoria, P. Eyyunni and S. Santra, *On the number of missing integers in partitions*, arXiv:2604.12557, April 14, 2026. https://arxiv.org/abs/2604.12557
2. Veena V S and S N Fathima, *On the sum of odd minimal excludants over overpartitions*, arXiv:2609.32207, first published September 26, 2026. https://arxiv.org/abs/2609.32207
3. A. Dhar, A. Mukhopadhyay and R. Sarma, *On new minimal excludants of overpartitions related to some q-series of Ramanujan*, arXiv:2409.06121, September 10, 2024. https://arxiv.org/abs/2409.06121
4. S. Chern and E. X. W. Xia, *Asymptotics for moments of the minimal partition excludant in congruence classes*, arXiv:2507.14431, July 19, 2025. https://arxiv.org/abs/2507.14431
5. J. A. L. Donato, *On Minimal Excludant over Overpartitions*, arXiv:2507.04402, July 6, 2025. https://arxiv.org/abs/2507.04402
