# Exact positivity horizons for truncated-exponential deferred correction on absorbing pure-birth chains

## Finding

For every order \(p\ge2\) and every \(d\ge1\), the bDeC, bDeCu and bDeCdu families share an exact, *sharp* endpoint positivity threshold when applied to an equal-rate absorbing pure-birth chain with \(d\) transient states. The threshold depends on both the order and the chain dimension. In particular, for \(p\ge3\),

\[
H_{p,d}=1\quad(d\ge p),\qquad
H_{p,p-1}=\frac{p}{p-1},\qquad
H_{p,p-2}=\beta_3=1.596071637983\ldots.
\]

At any fixed chain dimension \(d\ge2\), the positivity threshold grows linearly with the formal order and obeys

\[
\lim_{p\to\infty}\frac{H_{p,d}}p=W_0(e^{-1})=0.278464542761\ldots.
\]

The single-transient-state exception is a parity split: the same limit holds for odd orders, whereas even orders have limit \(e^{-1}=0.367879441171\ldots\). These are endpoint stochasticity statements; no positive internal-stage assertion is made.

## Assumptions and scope

Take integer \(p\ge2\), integer \(d\ge1\), and states \(1,\ldots,d,d+1\), with state \(d+1\) absorbing. In row-vector convention the continuous-time Markov generator is the real \((d+1)\)-square matrix

\[
Q_{i,i}=-1,\qquad Q_{i,i+1}=1\quad(1\le i\le d),\qquad Q_{d+1,d+1}=0,
\]

all other entries being zero. Thus \(\pi'(t)=\pi(t)Q\), and every probability row remains nonnegative and has total mass one in exact continuous time. For a common jump rate \(\lambda>0\), replace the dimensionless step \(h\) throughout by \(\lambda\Delta t\).

Set \(P_j(z)=\sum_{\ell=0}^{j}z^\ell/\ell!\), with \(P_0=1\). Micalizzi and Torlo prove that the scalar stability polynomial of every order-\(p\) bDeC, bDeCu and bDeCdu scheme equals \(P_p\), independently of their subtimenodes (source [1], Theorem 2). On a constant linear matrix problem, the endpoint is consequently precisely \(\pi^+=\pi P_p(hQ)\).

For each *odd* positive integer \(m\), denote by \(\beta_m>0\) the unique positive zero of \(P_m(-h)\). For odd \(m\ge1\) and integer \(r\ge1\), denote by \(\gamma_{m,r}>0\) the unique positive zero of

\[
G_{m,r}(h):=\sum_{j=0}^{m}\frac{(-h)^j}{j!(r+j)}
=\int_0^1t^{r-1}P_m(-ht)\,dt.
\]

Define the finite, nonempty set

\[
\begin{split}
\mathcal B_{p,d}={}&\{\beta_{p-k}:0\le k\le\min(d-1,p-1),\ p-k\text{ odd}\}\\
&\cup\{\gamma_{p-r,r}:1\le r\le\min(d,p-1),\ p-r\text{ odd}\}.
\end{split}
\]

When \(p\) is odd, \(k=0\) supplies a member; when \(p\) is even, \(r=1\) supplies a member. Put \(H_{p,d}=\min\mathcal B_{p,d}\). The central classification is

\[
P_p(hQ)\ge0\text{ entrywise}\quad\Longleftrightarrow\quad0\le h\le H_{p,d}.
\]

The inequality is for all probability-row initial states; special initial states may remain nonnegative beyond the universal threshold. The matrix always has row sums one, even when its entries become negative.

## Proof

**1. An exact matrix-entry factorization.** The transient block of \(Q\) is \(-I+S\), where \(S\) is the upper shift. Fix a starting transient state with \(r\) transient states remaining, including itself. For \(0\le k<r\), its transition-polynomial entry to the transient state \(k\) steps ahead is

\[
A_{p,k}(h)=\frac{h^k}{k!}P_{p-k}(-h)\quad(0\le k\le p),
\]

and vanishes if \(k>p\). This follows from the binomial expansion of \((-I+S)^j\). For the absorbing state the entry is zero when \(r>p\), and otherwise

\[
B_{p,r}(h)=\frac{h^r}{(r-1)!}
\sum_{j=0}^{p-r}\frac{(-h)^j}{j!(r+j)}
=\frac{h^r}{(r-1)!}G_{p-r,r}(h).
\]

Indeed, the absorbing entry of \(Q^j\) is \((-1)^{j-r}\binom{j-1}{r-1}\) for every \(j\ge r\), and zero for \(j<r\). The absorbing row of \(P_p(hQ)\) is the last unit row. Since \(Q\mathbf1=0\) and \(P_p(0)=1\), every row of \(P_p(hQ)\) has sum one. These formulas enumerate *all* potentially nonzero entries.

**2. Each inequality has a single positive failure horizon.** Every even-degree Taylor polynomial \(P_{2j}(-h)\) is strictly positive on \([0,\infty)\) by Taylor's integral remainder for \(e^{-h}\). For odd \(m\), \(P_m(-h)\) has derivative \(-P_{m-1}(-h)<0\), starts at one and has negative leading term, so it has exactly one positive root \(\beta_m\). Likewise, \(G_{m,r}>0\) for even \(m\). For odd \(m\),

\[
G_{m,r}'(h)=-\int_0^1t^rP_{m-1}(-ht)\,dt<0.
\]

It starts at \(1/r\) and tends to negative infinity, so it has exactly one positive root \(\gamma_{m,r}\). Accordingly, every entry inequality is valid on an initial closed interval, and the intersection of all those intervals is exactly \([0,H_{p,d}]\). For any \(h>H_{p,d}\), an explicit transient or absorbing entry is negative; taking its starting-state unit row produces a nonnegative datum with a negative component after one step. This proves both sharpness and the impossibility of a reentrant positivity window.

**3. Dimension staircase.** For odd \(m\), \(P_m(-x)>0\) on \([0,\beta_m)\), hence the integral defining \(G_{m,r}\) remains strictly positive even at \(x=\beta_m\). Thus

\[
\gamma_{m,r}>\beta_m.
\]

The odd-index roots \(\beta_1,\beta_3,\beta_5,\ldots\) strictly increase. To see this, note that the alternating terms at \(h=m\) increase in absolute value through degree \(m\), giving \(P_m(-m)\le0\), hence \(\beta_m\le m\). At that zero,

\[
P_{m+2}(-\beta_m)=\frac{\beta_m^{m+1}}{(m+1)!}
\left(1-\frac{\beta_m}{m+2}\right)>0,
\]

so \(\beta_{m+2}>\beta_m\). Since \(\beta_1=1\), the smallest available odd-degree root determines the staircase whenever an integral constraint does not intervene.

For \(d\ge p\), the transient coefficient with \(k=p-1\) requires \(P_1(-h)=1-h\ge0\), forcing \(h\le1\); all coefficients are nonnegative for \(h\le1\). For \(d=p-1\), the unique smallest absorption root arises at \(r=p-1\), where

\[
G_{1,p-1}(h)=\frac1{p-1}-\frac hp,
\]

so \(h\le p/(p-1)\). All other relevant roots exceed \(\beta_3>3/2\ge p/(p-1)\) for \(p\ge3\). For \(d=p-2\), the transient coefficient with \(k=p-3\) gives \(\beta_3\), and all other relevant odd-index polynomial roots are larger; each applicable integral root is larger than the corresponding polynomial root. This proves all three stated staircase identities.

**4. Fixed-dimension high-order limits.** Let \(\alpha>0\). Taylor's integral remainder, multiplied by \(e^h\), gives for odd \(m\)

\[
e^{h}P_m(-h)=1-\frac{h^{m+1}}{m!}
\int_0^1e^{ht}t^m\,dt.
\]

At \(h=\alpha m\), the integral satisfies the elementary endpoint Laplace estimate

\[
\int_0^1e^{\alpha mt}t^m\,dt
\sim\frac{e^{\alpha m}}{m(1+\alpha)}.
\]

Stirling's formula then shows that the subtracted term has logarithmic exponential growth rate

\[
\frac1m\log\left[\frac{(\alpha m)^{m+1}}{m!}
\int_0^1e^{\alpha mt}t^m\,dt\right]
\longrightarrow\log\alpha+1+\alpha.
\]

Because the expression is strictly increasing in \(h\), its unique root has \(\beta_m/m\to c\), where \(c>0\) is the unique solution of \(c e^{1+c}=1\), namely \(c=W_0(e^{-1})\). For every fixed \(d\ge2\), at least one polynomial constraint has an odd degree \(m=p+O(1)\), so \(H_{p,d}\le\beta_{p+O(1)}\). Every other root in its defining set is either an odd-degree root with index \(p+O(1)\) or an integral root larger than such a polynomial root. Thus the lower and upper bounds both divided by \(p\) tend to \(c\).

For \(d=1\) and odd \(p\), only the polynomial root \(\beta_p\) matters, so the same limit holds. For even \(p\), the diagonal coefficient \(P_p(-h)\) is always positive, while the absorption coefficient is \(1-P_p(-h)\). Thus \(H_{p,1}\) is the unique positive solution of \(P_p(-h)=1\). For even \(p\), the Taylor integral remainder instead reads

\[
P_p(-h)=e^{-h}+\frac{h^{p+1}e^{-h}}{p!}
\int_0^1e^{ht}t^p\,dt.
\]

At \(h=\alpha p\), Stirling and the same Laplace estimate make the second term

\[
\frac{\alpha}{(1+\alpha)\sqrt{2\pi p}}
(e\alpha)^p(1+o(1)).
\]

For \(0<\alpha<e^{-1}\), this tends to zero (and \(P_p(-\alpha p)<1\) for large \(p\)); for \(\alpha>e^{-1}\), it diverges (so \(P_p(-\alpha p)>1\)). Uniqueness of the positive return root gives \(H_{p,1}/p\to e^{-1}\) along even orders. All limits are for fixed \(d\), not joint growth of order and dimension.

## Verification

The accompanying Python standard-library script `verify.py` constructs the full \((d+1)\)-square polynomial matrix using exact `fractions.Fraction` arithmetic independently of the closed-form entry expressions. It compares all transient and absorbing entries for \(2\le p\le10\), \(1\le d\le8\) and six rational values of \(h\), checks every row sum, and tests the sharp \(d=p\) and \(d=p-1\) staircase boundaries for \(3\le p\le10\). Its finite checks passed (`VERIFY_OK`, 10400 counted entry and boundary checks). They are reproducibility checks; they are not substituted for the proof above.

For example, at order four the horizons are \(H_{4,1}=2.785293563405\ldots\), \(H_{4,2}=1.596071637983\ldots\), \(H_{4,3}=4/3\) and \(H_{4,d}=1\) for \(d\ge4\).

## Relationship to prior work

Micalizzi and Torlo [1] supply the method families and their *already known* common stability polynomial. This is not claimed as new. Their linear stability regions do not themselves classify when the matrix polynomial is entrywise nonnegative on a specified finite Markov chain. Horváth [2] analyzes class-uniform Runge–Kutta positivity thresholds and positively invariant cones; its general absolute-monotonicity context explains the sufficient step \(h\le1\) but does not provide this finite-pure-birth dimension staircase, its integral-entry thresholds, or the fixed-dimension parity split. Öffner and Torlo [3] construct modified Patankar deferred-correction schemes designed to preserve positivity by changing the update: those methods have a different, nonlinear endpoint map and are not subject to this unmodified polynomial classification. Published Markov-chain endpoint comparisons for [2/2] Padé [5] and SSP-SDIRK2(2) [6] have different rational stability functions and neither supplies the Taylor-polynomial dimension law. The Lambert-W rate reflects classical real-root asymptotics of exponential partial sums [4]; novelty is not claimed for Szegő-curve theory or for that constant in isolation.

## Limitations

The statements concern equal-rate absorbing pure-birth generators, constant-coefficient linear evolution, exact arithmetic, endpoint positivity for every nonnegative probability row, and the specified bDeC variants. Unequal rates, general generators, positivity of individual internal stages, rounding errors, and all modified Patankar methods require separate analysis. A source-equivalent analysis under older absolute-monotonicity/Jordan-block terminology cannot be ruled out without exhaustive historical coverage. No mathematical independence or external scientific audit is asserted.

## References

[1] L. Micalizzi and D. Torlo, *A New Efficient Explicit Deferred Correction Framework: Analysis and Applications to Hyperbolic PDEs and Adaptivity*, arXiv:2210.02976 (first posted 2022-10-06); *Communications on Applied Mathematics and Computation* 6 (2024), 1629–1664, DOI 10.1007/s42967-023-00294-6. See Section 6, Theorem 2.

[2] Z. Horváth, *On the positivity step size threshold of Runge–Kutta methods*, *Applied Numerical Mathematics* 53 (2005), 341–356, DOI 10.1016/j.apnum.2004.08.026.

[3] P. Öffner and D. Torlo, *Arbitrary high-order, conservative and positive preserving Patankar-type deferred correction schemes*, arXiv:1905.09237 (2019), *Applied Numerical Mathematics* 153 (2020), 15–34.

[4] R. S. Varga, *Asymptotics for the Zeros of the Partial Sums of exp(z)*, in *Scientific Computation on Mathematical Problems and Conjectures*, SIAM, DOI 10.1137/1.9781611970111.ch4; see also classical Szegő-curve theory. The zero-limit constant is contextual prior mathematics, not an independently claimed discovery.

[5] *Eight-state barrier for Markov positivity of the [2/2] Padé map*, publicly accessible scientific result, https://github.com/Resultary/2026/tree/main/2026/9/20/SCOPE-eight-state-pade-markov-positivity-barrier--4aad2a3f58ab.

[6] *Two-state immunity and three-state sharpness for endpoint positivity of SSP-SDIRK2(2)*, publicly accessible scientific result, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-two-state-immunity-and-three-state-sharpness-for-endpoint-positi--46bf11cc19c7.
