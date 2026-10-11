# Outermost-cycle basin selection and logarithmic settling for quantized affine contractions

## Finding
For the discretized affine contraction
\[
f(x)=\lfloor\mu-rx\rfloor,\qquad \mu\in\mathbb R,\quad 0<r<1,
\]
the second iterate \(g=f^2\), restricted to \(\mathbb Z\), has a nonempty interval of consecutive fixed integers, \([L,U]\cap\mathbb Z\). Every integer strictly outside this interval is captured specifically by its *nearest endpoint*, not by an arbitrary internal fixed point. Moreover \(f(j)=L+U-j\) on this interval, so all limiting cycles are explicitly paired. This gives an exact partition into basins, together with the sharp leading coefficient of the settling time from remote integer initial states.

Put \(C_j=\{x\in\mathbb R:f(x)=j\}\) for \(j\in\mathbb Z\). Then
\[
C_j=\left(\frac{\mu-j-1}{r},\frac{\mu-j}{r}\right],\qquad |C_j|=\frac1r.
\]
For any initial real \(x\), set \(j=f(x)\). Its limit cycle is
\[
\Omega(x)=
\begin{cases}
\{L,U\},&j\le L\ \text{or}\ j\ge U,\\
\{j,L+U-j\},&L<j<U.
\end{cases}
\]
For \(L<U\), the basin of the outermost cycle is exactly
\[
\mathcal B_{\mathrm{outer}}=
\left(-\infty,\frac{\mu-U}{r}\right]
\cup\left(\frac{\mu-L-1}{r},\infty\right).
\]
An interior two-point cycle \(\{j,L+U-j\}\) has basin \(C_j\cup C_{L+U-j}\) and Lebesgue measure \(2/r\). The basin of an interior singleton cycle, if present, is one cell of measure \(1/r\). For \(L=U\) the sole fixed point attracts all real initial states.

Let \(\tau(n)\) denote the number of second-iterate steps needed for an integer \(n\) to reach \([L,U]\cap\mathbb Z\), counting \(\tau(n)=0\) for states already in that interval. Then
\[
\tau(n)=\frac{\log|n|}{-2\log r}+O_{r,\mu}(1)
\qquad (|n|\to\infty,\ n\in\mathbb Z).
\]
No extra hypothesis on \(\mu\) or avoidance of floor discontinuities is required.

## Assumptions and scope
The entire real initial-value line is considered, with the usual floor convention \(\lfloor t\rfloor\le t<\lfloor t\rfloor+1\). The parameter \(r\) is fixed strictly between zero and one and \(\mu\) is any fixed real number. \(f^2\) means two compositions, and \(\Omega(x)\) denotes the eventual period-one or period-two orbit (equivalently its finite \(\omega\)-limit set). The asymptotic settling estimate is for integer starting states; any real starting state becomes integer after one application of \(f\). Basin size refers to ordinary Lebesgue measure on \(\mathbb R\).

The endpoints are constructive. Let
\[
q=\frac{\mu}{1+r},\qquad B=\frac1{1-r^2}.
\]
All fixed integers of \(g\) lie in the finite interval \([q-B,q+B]\), so one may evaluate \(g(n)\) over its integer points and take the smallest and largest solutions of \(g(n)=n\). Existence is proved below; this is not a request for an unbounded search.

## Proof
**1. A discrete nonexpansion lemma.** For every integer \(n\), since \(0<r<1\),
\[
f(n+1)-f(n)\in\{-1,0\}.
\]
Because \(f\) is nonincreasing on integers, this implies
\[
g(n+1)-g(n)\in\{0,1\}.
\]
Thus \(g\) is nondecreasing, and \(h(n)=g(n)-n\) is nonincreasing with adjacent differences in \(\{-1,0\}\). This *unit-step* condition is the crucial stronger property beyond mere monotonicity.

**2. A finite consecutive fixed-point interval.** Define the rounding defects \(\varepsilon_n=\mu-rn-f(n)\in[0,1)\) for integers \(n\). Expanding the two floors gives
\[
g(n)=r^2n+(1-r)\mu+r\varepsilon_n-\varepsilon_{f(n)}.
\]
Therefore
\[
h(n)=-(1-r^2)(n-q)+r\varepsilon_n-\varepsilon_{f(n)}.
\]
The final two terms lie strictly between \(-1\) and \(r\). Hence \(h(n)>0\) for all sufficiently negative integers, and \(h(n)<0\) for all sufficiently positive integers. Since \(h\) changes by at most one downward at each integer step, it necessarily takes the value zero. Since it is nonincreasing, its zero set is a finite, nonempty consecutive integer interval \([L,U]\cap\mathbb Z\). If \(g(n)=n\), then
\[
(1-r^2)(n-q)=r\varepsilon_n-\varepsilon_{f(n)},
\]
which implies \(|n-q|<1/(1-r^2)\) and establishes the finite endpoint search.

**3. Endpoint selection.** If \(n<L\), monotonicity of \(h\) and absence of zeros below \(L\) give \(g(n)>n\). Monotonicity of \(g\) and \(g(L)=L\) give \(g(n)\le L\). Thus iterating \(g\) from any integer below \(L\) produces strictly increasing integers, bounded above by \(L\), and terminates exactly at \(L\). Similarly, for \(n>U\), \(g(n)<n\) but \(g(n)\ge U\); the orbit terminates exactly at \(U\). Hence exterior points cannot fall into interior cycles.

**4. Reflection of the periodic core.** The maps \(f\) and \(g=f^2\) commute. If \(j\in[L,U]\cap\mathbb Z\), then \(g(f(j))=f(g(j))=f(j)\), so \(f(j)\) belongs to the same finite interval. Moreover \(f^2(j)=j\), so \(f\) restricts to a bijection on that interval; it is nonincreasing and therefore is the unique order-reversing permutation of its consecutive integer points. Consequently
\[
f(j)=L+U-j\qquad(L\le j\le U).
\]
The pair \(\{L,U\}\) is a two-cycle if \(L<U\); if \(L=U\), it is a fixed point. The interior indices form the other period-two pairs, with at most one central singleton.

**5. Exact real basins and measure.** For each integer \(j\), solving \(j\le\mu-rx<j+1\) gives precisely the half-open quantization cell \(C_j\) stated above. Starting at any real \(x\), one step places the orbit at \(j=f(x)\). Step 3 maps exterior \(j\) to the respective endpoint, while Step 4 fixes each interior \(j\) under \(g\) and pairs it under \(f\). Thus each interior cycle attracts exactly the one or two first-step cells indexed by its points. Distinct cells are disjoint, and each has Lebesgue measure \(1/r\). For \(L<U\), the condition for the outermost cycle is \(f(x)\le L\) or \(f(x)\ge U\), equivalent, using the floor inequalities with their correct boundary inclusions, to
\[
x>\frac{\mu-L-1}{r}\quad\text{or}\quad x\le\frac{\mu-U}{r}.
\]
When \(L=U\), all integers enter this singleton and therefore all real initial points do too.

**6. Sharp logarithmic settling.** The identity in Step 2 has bounded additive error, uniformly over integers: \(g(n)=r^2n+b_n\), \(|b_n|\le |1-r|\,|\mu|+1+r\). Iterating, for all \(n\in\mathbb Z\) and all \(k\ge0\),
\[
\left|g^k(n)-r^{2k}n\right|
\le\frac{|1-r|\,|\mu|+1+r}{1-r^2}=:C.
\]
Take \(K_n=\log|n|/(-2\log r)\). For any fixed sufficiently large \(M>0\), whenever \(k\le K_n-M\), the magnitude of \(r^{2k}n\) exceeds \(\max(|L|,|U|)+C+1\). The iterate cannot yet have reached the fixed interval, giving \(\tau(n)\ge K_n-O_{r,\mu}(1)\). Conversely, for \(k\ge K_n+M\), the same bound confines the integer \(g^k(n)\) to a fixed finite interval, independent of \(n\). By the strictly monotone endpoint selection in Step 3, each of the finitely many states in that interval reaches \([L,U]\) after uniformly finitely many more \(g\)-steps. Hence \(\tau(n)\le K_n+O_{r,\mu}(1)\). Combining the two bounds proves the stated asymptotic with no assumption on the sign of \(n\).

## Verification
The standalone standard-library script `CHECK.py` uses exact rational arithmetic (`fractions.Fraction`) to enumerate 36 rational parameter pairs, compute the finite fixed set, check the reflection law, test exterior endpoint capture, check exact quantization-cell boundaries and sample logarithmic settling residuals. Run it using `python CHECK.py`. Its successful output ends with `CHECK_OK: 36 exact parameter cases and orbit/basin samples`. The infinite-parameter, infinite-orbit and asymptotic statements are established by Steps 1–6 rather than inferred from finite tests.

For a worked exact example, take \(r=9/10\) and \(\mu=1/2\). Then \([L,U]=[-4,4]\cap\mathbb Z\) and \(f(j)=-j\) on this interval. The outermost two-cycle is \(\{-4,4\}\), with basin \(( -\infty,-35/9]\cup(35/9,\infty)\). The inner two-cycle basins each have length \(20/9\), whereas the fixed-point basin at zero has length \(10/9\).

## Relationship to prior work
Hoseana, *The dynamics of one-dimensional quasi-affine maps* (arXiv:2406.14055v1, 20 June 2024), gives the complete two-parameter cycle enumeration and classifies broad types of \(\omega\)-limit sets. In particular, its Theorem 3(vi) states that an exterior orbit in the regime \(-1<\lambda<0\) reaches either a two-cycle or the fixed point; Theorem 3(vii) states that it reaches a two-cycle in the alternative regime. Those statements do not specify which of potentially multiple two-cycles occurs, nor assign their actual attraction basins or quantify finite transient time. The new statement supplies a parameter-uniform selection rule, exact half-open basin boundaries and cell measures, and the sharp logarithmic settling law. The originating theorems on existence and enumeration of periodic points are credited, not reasserted as novelty.

Rozikov, Sattarov and Usmonov, *The dynamical system generated by the floor function* (arXiv:1503.07129v1, 24 March 2015), concerns \(\mu=0\), without the two-parameter cell partition and settling-time result claimed here. We do not assert that independently formulated results cannot exist; in particular the 2025 journal version of the Hoseana paper may contain changes beyond the inspected preprint.

## Limitations
This theorem is confined to negative slopes of magnitude strictly below one; no assertion is made for \(r=1\), expanding or nonnegative slopes, stochastic rounding, or higher-dimensional quantization. The settling-time estimate is asymptotic with a parameter-dependent bounded remainder, not an explicit uniform constant as \(r\uparrow1\). Prior-art comparison is based on the accessible primary preprints and identified related literature, not an exhaustive proof of publication priority. No independent mathematical audit has been performed.

## References
1. J. Hoseana, *The dynamics of one-dimensional quasi-affine maps*, arXiv:2406.14055v1 (20 June 2024), https://arxiv.org/html/2406.14055v1. Journal version: *Journal of Difference Equations and Applications* **31** (2025), 418–433, DOI:10.1080/10236198.2024.2428386.
2. U. A. Rozikov, I. A. Sattarov and J. B. Usmonov, *The dynamical system generated by the floor function*, arXiv:1503.07129v1 (24 March 2015), https://arxiv.org/html/1503.07129v1.
