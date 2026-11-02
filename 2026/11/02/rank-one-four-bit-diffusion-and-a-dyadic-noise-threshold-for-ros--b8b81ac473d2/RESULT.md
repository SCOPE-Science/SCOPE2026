# Rank-one four-bit diffusion and a dyadic noise threshold for Rosenblatt baker maps

## Finding

A prescribed invariant distribution need not determine the fluctuations of a deterministic sampling orbit. In the two-dimensional Rosenblatt construction of Fox, Hsiao and Lee [1], the following theorem gives an exact fluctuation classification for a particularly natural family of paired quantile observables.

Let \(R=(R_1,R_2)\) be an invertible Rosenblatt transform for a strictly positive continuous probability density on a rectangle. Write
\[
B(u,v)=\left(2u\bmod 1,\frac{v+\lfloor2u\rfloor}{2}\right),\qquad F_B=R^{-1}\circ B\circ R.
\]
Start \(X_0\) with the prescribed probability and write \(X_j=F_B^j(X_0)\). For \(1\le m\le4\), \(1\le k<2^m\), and \(q=k/2^m\), define the centered paired-quantile difference
\[
G_{m,k}(x)=\mathbf1_{\{R_1(x)<q\}}-\mathbf1_{\{R_2(x)<q\}},\qquad
S_N(m,k)=\sum_{j=0}^{N-1}G_{m,k}(X_j).
\]
Both indicators have stationary expectation \(q\), so their difference is centered.

**Theorem (sharp binary-resolution threshold).** For every dyadic threshold of denominator at most eight, the sums \(S_N(m,k)\) are uniformly bounded in \(N\), almost surely. At denominator sixteen they remain uniformly bounded except at the four thresholds
\[
q\in\left\{\frac3{16},\frac5{16},\frac{11}{16},\frac{13}{16}\right\}.
\]
At each of these four thresholds, and only these among the denominator-sixteen thresholds,
\[
\lim_{N\to\infty}\frac{\operatorname{Var}(S_N(4,k))}{N}=\frac1{32},
\qquad
\frac{S_N(4,k)}{\sqrt N}\Longrightarrow\mathcal N\left(0,\frac1{32}\right).
\]
The assertions are independent of the chosen positive target density.

The phenomenon follows from a stronger **rank-one diffusion law**. For a function \(h:\{0,1\}^{4}\to\mathbb R\) with \(h(w^{\mathrm{rev}})=-h(w)\), define
\[
\mathcal L(h)=h(0010)-h(0011)+h(0101)+h(1011).
\]
For the stationary baker bit process \((\varepsilon_j)_{j\in\mathbb Z}\), let
\[
Z_j(h)=h(\varepsilon_j\varepsilon_{j+1}\varepsilon_{j+2}\varepsilon_{j+3}).
\]
Then
\[
\boxed{\lim_{N\to\infty}\frac1N\operatorname{Var}\left(\sum_{j=0}^{N-1}Z_j(h)\right)=\frac{\mathcal L(h)^2}{32}.}
\]
If \(\mathcal L(h)=0\), the partial sums are uniformly bounded on every binary orbit. Otherwise the normalized sums converge to the centered normal law with this positive variance. Thus the entire six-dimensional space of four-bit reversal-odd observables has only one diffusive direction.

For comparison, use the **same** transform \(R\) but replace \(B\) by the independent-coordinate tent map \(U_T(u,v)=(T(u),T(v))\), \(T(u)=1-2|u-1/2|\). The half-quantile difference \(G_{1,1}(X_j)\) is then an independent, identically distributed centered sequence with variance \(1/2\) per step. Under \(F_B\) the same observable has \(|S_N(1,1)|\le1\) for every nonambiguous orbit. Both systems preserve the identical target probability.

## Assumptions and scope

The state space is a compact two-dimensional rectangle and the target density is continuous, strictly positive, and normalized. The Rosenblatt transform is defined by its first marginal and conditional second-coordinate cumulative distributions; positivity gives an almost-everywhere invertible transport to the unit square. The baker and tent maps are understood modulo their zero-measure branch boundaries, and all limit laws use stationary initialization from the target density. Binary expansions of dyadic rationals are excluded, a stationary null event. A statement that sums are bounded on every symbolic orbit applies to the unambiguous bi-infinite bit representation. No assertion is made for other thresholds, arbitrary nonstationary distributions, or floating-point implementations.

## Proof

**1. Bernoulli representation.** Under normalized Lebesgue measure on the square, the baker map has a two-sided independent fair-bit representation
\[
u_j=0.\varepsilon_j\varepsilon_{j+1}\cdots\quad\text{and}\quad
v_j=0.\varepsilon_{j-1}\varepsilon_{j-2}\cdots.
\]
Here \((u_j,v_j)=B^j(R(X_0))\). Invariance and independence of the binary digits follow either from the equal-area affine branches or from the elementary cylinder measure formula. Conjugation by \(R\) preserves the joint distribution of all observables expressed through \(R(X_j)\).

For a binary word \(w\) of length \(m\), let \(\phi_{m,k}(w)\) be the indicator that its numerical binary value is strictly less than \(k\), and define \(h_{m,k}(w)=\phi_{m,k}(w)-\phi_{m,k}(w^{\mathrm{rev}})\). Put \(W_j=\varepsilon_j\cdots\varepsilon_{j+m-1}\). Directly shifting the two digit windows yields the **exact** identity
\[
\begin{aligned}
S_N(m,k)&=\sum_{j=0}^{N-1}h_{m,k}(W_j)+E_{N,m,k},\\
E_{N,m,k}&=\sum_{j=N-m}^{N-1}\phi_{m,k}(W_j^{\mathrm{rev}})
-\sum_{j=-m}^{-1}\phi_{m,k}(W_j^{\mathrm{rev}}),
\end{aligned}
\]
where \(|E_{N,m,k}|\le2m\) for all \(N\). Therefore the quantile difference and the reversal-odd block observable have the same limiting variance and normal limit, and bounded sums for the latter imply bounded sums for the former.

**2. Short reversal-odd blocks are coboundaries.** Every reversal-odd one-bit function is zero. A reversal-odd two-bit function is a multiple of the signed word indicator \(\mathbf1_{01}-\mathbf1_{10}\), which is the difference of a one-bit potential at the end and start of its edge. For length three, the reversal-odd space is spanned by \(\mathbf1_{001}-\mathbf1_{100}\) and \(\mathbf1_{011}-\mathbf1_{110}\). On the binary two-bit vertex order \((00,01,10,11)\), corresponding potentials are \((0,1,1,1)\) and \((0,0,0,1)\). Consequently all such block sums telescope and are bounded independently of their length.

**3. The complete four-bit coboundary obstruction.** The six nonpalindromic reversal pairs are
\[
(0001,1000),\ (0010,0100),\ (0011,1100),\ (0101,1010),\ (0111,1110),\ (1011,1101).
\]
Write \(a_i\), for \(0\le i\le5\), for the value of \(h\) on the first word in pair \(i\); reversal determines the other values. Then \(\mathcal L(h)=a_1-a_2+a_3+a_5\). If \(\mathcal L(h)=0\), the following values on three-bit vertices define a potential \(V\), in lexicographic order:
\[
\begin{array}{c|cccccccc}
w&000&001&010&011&100&101&110&111\\\hline
V(w)&0&a_0&a_0+a_1&a_0+a_1+a_3+a_5&a_0&a_0+a_1+a_3&a_0+a_1+a_3+a_5&a_0+a_1+a_3+a_4+a_5.
\end{array}
\]
Substitution on all sixteen binary four-bit edges proves
\[
h(b_0b_1b_2b_3)=V(b_1b_2b_3)-V(b_0b_1b_2).
\]
The telescoping sum is thus bounded. Conversely, take \(e=\mathbf1_{0010}-\mathbf1_{0100}\), which has \(\mathcal L(e)=1\). For every reversal-odd \(h\), the function \(h-\mathcal L(h)e\) has zero obstruction and hence is a coboundary. In particular, the quotient of reversal-odd four-bit functions by these coboundaries is one-dimensional.

**4. Exact variance and central limit theorem.** The stationary sequence \(e(W_j)\) is three-dependent and centered. Its exact covariance values at lags zero through three are respectively
\[
\gamma_0=\frac18,\qquad \gamma_1=-\frac1{32},\qquad
\gamma_2=-\frac1{64},\qquad \gamma_3=0,
\]
and every later lag has zero covariance. These values follow by counting all binary words of lengths four through seven; they are also independently recomputed using the accompanying exact-rational program. Thus
\[
\gamma_0+2(\gamma_1+\gamma_2+\gamma_3)=\frac1{32}.
\]
The bounded coboundary part does not change a variance divided by \(N\), and because its two endpoint terms each depend on finitely many bits, it introduces only a bounded correction to the variance itself. The bounded finite-dependent central limit theorem for \(e(W_j)\), combined with the same telescoping decomposition, gives the asserted normal limit whenever \(\mathcal L(h)\ne0\). If \(\mathcal L(h)=0\), the exact coboundary identity proves the stronger deterministic bounded-sums conclusion.

**5. All dyadic thresholds through sixteen.** The short-denominator assertion follows from Step 2. For denominator sixteen, evaluate \(\mathcal L(h_{4,k})\) using the four indicated reversal pairs:
\[
\begin{aligned}
\mathcal L(h_{4,k})={}&(\mathbf1_{\{2<k\}}-\mathbf1_{\{4<k\}})
-(\mathbf1_{\{3<k\}}-\mathbf1_{\{12<k\}})\\
&+(\mathbf1_{\{5<k\}}-\mathbf1_{\{10<k\}})
+(\mathbf1_{\{11<k\}}-\mathbf1_{\{13<k\}}).
\end{aligned}
\]
For integers \(1\le k\le15\), this equals \(+1\) at \(k=3,13\), \(-1\) at \(k=5,11\), and zero everywhere else. The full variance and limit-law classification now follows from Steps 1–4.

**6. Different sampler, identical target.** The product of two full-branch symmetric tent maps preserves product Lebesgue measure. Each itinerary label \(\mathbf1_{\{u<1/2\}}\) is a fair independent Bernoulli digit; under the product map the two digit sequences are independent. Their difference has stationary variance \(1/2\) and independent increments. Under the baker map the same quantity is \(\varepsilon_{j-1}-\varepsilon_j\), so its length-\(N\) sum is precisely \(\varepsilon_{-1}-\varepsilon_{N-1}\). Applying \(R^{-1}\) to either sampler gives the same prescribed invariant probability, completing the comparison.

## Verification

The standalone standard-library Python program `verify.py` checks the complete six-by-six bilinear Green–Kubo matrix using exact fractions. In the ordered reversal-pair basis above it is exactly \(vv^{\mathsf T}/32\), where \(v=(0,1,-1,1,0,1)\). The program also checks every short-block reversal-odd basis vector is a graph coboundary, every four-bit graph-potential generator, and all fifteen four-bit quantile thresholds. The analytical derivation above, including all sixteen graph edges and the four covariance values, is the proof; numerical experiments are not used to extrapolate to an infinite-time statement.

To reproduce with Python 3, execute `python verify.py` in the directory containing the file. No third-party dependencies or random seeds are required.

## Relationship to prior work

Fox, Hsiao and Lee [1] prove the Rosenblatt conjugacy factorization and explicitly construct both baker-based and componentwise triangular-map samplers in their Sections 4 and 6. Those maps, their preservation of the target law, and the classical two-sided Bernoulli description of the baker map are prior facts and are not claimed here. Their inspected sections discuss invariant densities, Lyapunov exponents, and examples, but do not state the rank-one time-reversal-odd diffusion form, the sharp four-bit threshold set, or the contrast between bounded baker half-quantile errors and iid tent errors.

The classical binary symbolic representation [2] and finite-dependent central limit theorem are used only as tools. Search-based comparisons found no published statement covering the exact rank-one formula or the paired-quantile cutoff; absence of a retrieved match is not a proof of global publication novelty.

## Limitations

The distinction concerns the chosen *paired Rosenblatt quantile observable*, not all observables of the preserved distribution. The threshold classification stops at word length four and is not a claim that every longer binary threshold has positive variance. The Gaussian theorem requires stationary initial conditions; exceptional dyadic expansions form a null set. The target density must admit the stated invertible transport. Mathematical priority could be affected by unindexed or unavailable work, and independent mathematical audit has not occurred.

## References

[1] C. Fox, L.-J. Hsiao and J.-E. Lee, *Solutions of the Multivariate Inverse Frobenius–Perron Problem*, arXiv:2106.00177 (first public version, 1 June 2021); *Entropy* 23 (2021), article 838, DOI 10.3390/e23070838. Open full text: https://pmc.ncbi.nlm.nih.gov/articles/PMC8306100/.

[2] *Quantized baker map*, Scholarpedia, section "Symbolic dynamics", https://var.scholarpedia.org/article/Quantized_baker_map. Cited only for the established binary-shift representation, not for the new variance classification.
