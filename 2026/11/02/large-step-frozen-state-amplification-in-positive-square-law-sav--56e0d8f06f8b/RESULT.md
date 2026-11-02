# Large-step frozen-state amplification in positive square-law SAV backward Euler

## Finding

Consider the positive-root, square-law backward-Euler scalar auxiliary variable (SAV) step
\[
q(x)=\sqrt{C+x^2/2},\quad c(x)=x/q(x),\qquad
r_{n+1}=\frac{r_n}{\sqrt{1+h c(x_n)^2}},\qquad
x_{n+1}=x_n-hc(x_n)r_{n+1}.
\]
Here \(C>0\), \(h>0\), \(x_0\in\mathbb R\setminus\{0\}\), and the auxiliary variable starts consistently at \(r_0=q(x_0)\). This is the one-degree-of-freedom square-law SAV discretization of the strictly convex gradient flow \(\dot x=-x\), with quadratic energy \(E(x)=x^2/2\).

**Theorem (large-step frozen-state law).** There exists a finite \(H(C,x_0)\) such that, for every fixed \(h\ge H(C,x_0)\), all the iterates are well-defined, \(r_n>0\) at every finite step, and
\[
 r_n\longrightarrow0,\qquad x_n\longrightarrow X_h\ne0
 \quad(n\to\infty).
\]
Writing \(q_0=\sqrt{C+x_0^2/2}\), the limiting physical state satisfies the two-term asymptotic law
\[
 \boxed{X_h=-\operatorname{sgn}(x_0)q_0\sqrt h+x_0+\frac{q_0^2}{x_0}+O_{C,x_0}(h^{-1/2})}
 \quad(h\to\infty),
\]
so its physical objective obeys
\[
 \boxed{E(X_h)=\frac{q_0^2}{2}h+O_{C,x_0}(\sqrt h).}
\]
Nevertheless the exactly dissipated modified energy is \(r_n^2-C\): for every step,
\[
 r_{n+1}^2-r_n^2=-\frac{(x_{n+1}-x_n)^2}{h}\le0.
\]
Thus positivity of the auxiliary variable and unconditional modified-energy dissipation do not by themselves guarantee long-time consistency with the unique physical minimizer.
The frozen limit belongs to the boundary \(r=0\), on which the extended discrete map has an entire line of fixed states \((x,0)\); no finite iterate starts or lands on that boundary.

There is also a completely explicit witness: at \(C=1\), \(x_0=1\), \(h=100\), the sequence converges to \(X_{100}<-9.125\), while \(r_n\downarrow0\). Consequently \(E(X_{100})>41\), although \(E(x_0)=1/2\).

## Assumptions and scope

The continuous model is the scalar ordinary differential equation \(\dot x=-x\), represented with \(\mathcal L=0\), \(\mathcal G=1\) and nonlinear-energy component \(\mathcal E_{\mathcal N}(x)=x^2/2\). The offset \(C\) is strictly positive. All calculations are exact arithmetic. A *single fixed step length* \(h\) is used for the entire infinite iteration; the limit \(n\to\infty\) is taken first, followed by \(h\to\infty\). The result is not a step-size-uniform convergence claim.

One can derive the displayed map from the coupled scheme
\[
\frac{x_{n+1}-x_n}{h}=-\frac{r_{n+1}}{q(x_n)}x_n,
\qquad
r_{n+1}^2-r_n^2=\frac{r_{n+1}}{q(x_n)}x_n(x_{n+1}-x_n),
\]
using the unique positive root of the resulting quadratic equation. The theorem applies to exactly this square-law update, not to all relaxed, exponential, or otherwise modified SAV schemes.

## Proof

**1. Exact scalar map and dissipation.** Substitute the first equation of the coupled scheme into its second equation. With \(c_n=c(x_n)\), this gives
\[
 (1+hc_n^2)r_{n+1}^2=r_n^2.
\]
Its unique positive root is the stated update; substitution back into the first equation gives the state update. Since \(|c(x)|\le\sqrt2\), the map is globally defined, and positive \(r_n\) stays strictly positive. Moreover,
\[
 r_{n+1}^2-r_n^2=-hc_n^2r_{n+1}^2
 =-(x_{n+1}-x_n)^2/h.
\]

**2. First step at large \(h\).** It suffices to assume \(x_0>0\), since reflecting all \(x_n\) changes no \(r_n\). Let \(q_0=q(x_0)\). The first step is exactly
\[
 r_1=\frac{q_0}{\sqrt{1+h x_0^2/q_0^2}},\qquad
 x_1=x_0-\frac{h x_0}{\sqrt{1+h x_0^2/q_0^2}}.
\]
Elementary expansion at \(h\to\infty\) yields
\[
 r_1=\frac{q_0^2}{x_0\sqrt h}+O(h^{-3/2}),\qquad
 x_1=-q_0\sqrt h+x_0+O(h^{-1/2}).
\]
In particular, eventually \(x_1\le-3q_0\sqrt h/4\) and \(r_1\le 2q_0^2/(x_0\sqrt h)\).

**3. A bootstrap excluding return to the origin.** Suppose \(x_j\le-q_0\sqrt h/2\) for \(1\le j\le N\). When \(h\) is sufficiently large, this forces \(x_j^2\ge2C\) and therefore
\[
 c(x_j)^2=\frac{x_j^2}{C+x_j^2/2}\ge1,
 \qquad r_{j+1}\le\frac{r_j}{\sqrt{1+h}}.
\]
Since \(|c|\le\sqrt2\), the cumulative state displacement after the first step, up to and including any such \(N\), is at most
\[
 \sum_{j=1}^{N}|x_{j+1}-x_j|
 \le \frac{h\sqrt2\,r_1}{\sqrt{1+h}-1}=O_{C,x_0}(1).
\]
For all sufficiently large \(h\), this is smaller than \(q_0\sqrt h/4\). Hence \(x_{N+1}\le-q_0\sqrt h/2\) too. Induction proves the bound for every \(j\ge1\). The geometric estimate gives \(r_n\to0\), while absolute summability gives a limit \(X_h\le-q_0\sqrt h/2<0\).

**4. Sharp constant term.** The bootstrap implies \(x_1=-q_0\sqrt h+O(1)\), so
\[
 c(x_1)=-\sqrt2+O(h^{-1}),\qquad
 r_2=\frac{q_0^2}{\sqrt2\,x_0 h}+O(h^{-2}),
\]
and consequently \(x_2-x_1=q_0^2/x_0+O(h^{-1})\). The residual displacement after step two is bounded by
\[
 \sum_{j=2}^{\infty}|x_{j+1}-x_j|
 \le \frac{h\sqrt2\,r_2}{\sqrt{1+h}-1}
 =O_{C,x_0}(h^{-1/2}).
\]
Combining this with the first-step expansion proves the two-term formula. Squaring gives the physical-energy asymptotic. Reflection supplies the \(x_0<0\) case.

**5. Exact numerical witness, without relying on numerics.** For \(C=x_0=1\), \(h=100\),
\[
 x_1=1-100\sqrt{3/203}<-11,\qquad
 r_1=3/\sqrt{406}<3/20.
\]
Whenever \(x\le-8\), \(c(x)^2\ge64/33\); hence the next auxiliary value is less than the previous one divided by \(13\). The entire total displacement after step one is then less than
\[
 100\sqrt2\frac{r_1}{12}
 <\frac{100(3/2)(3/20)}{12}=15/8.
\]
The bootstrap closes because \(-11+15/8=-73/8=-9.125<-8\). Therefore the limit exists below \(-73/8\), and the asserted energy gap follows.

## Verification

The standalone `verify_sav.py` checks the exact recurrence and dissipation numerically over 300 reproducible parameter samples, tests the explicit \(h=100\) witness, and checks the two-term large-step remainder over four initial conditions and three increasing step lengths each. Run with `python verify_sav.py` using Python 3 and only its standard library. These finite tests are supplementary; the preceding inequalities prove the statements for all admissible parameters in the specified range.

## Relationship to prior work

Huang, Liu, Wang and Yan (2026) introduce positivity-preserving square-law SAV backward-Euler and Crank–Nicolson schemes and establish positive roots and modified-energy dissipation. The present statement isolates an elementary scalar specialization and proves its *infinite-iteration, large-step physical-state behavior*, rather than the positivity or discrete modified-energy law itself.

Bouchriti, Pierre and Alaa (2020) showed for earlier SAV formulations that a modified discrete stationary equation can differ from the original physical stationary equation. Jiang, Zhang and Zhao (2021) developed relaxation to address SAV consistency with physical energy. These establish why the issue matters, but the specific fixed-step positive-root recurrence, consistent-initialization trajectory, and sharp \(\sqrt h\) frozen-state expansion do not follow from those cited general observations alone. Historical priority remains open, including the possibility of an equivalent scalar calculation elsewhere.

## Limitations

The finding is one-dimensional, uses an unmodified square-law auxiliary update, and studies fixed-step exact arithmetic. The source manuscript's full later sections could not be checked at the final comparison stage; overlap with an uninspected example is an explicit residual priority risk. This theorem neither contradicts finite-time small-step convergence results nor proves any failure of the fully spatially discrete PDE under small-step scaling. An external independent mathematical audit has not been performed.

## References

1. Q.-A. Huang, Z.-H. Liu, Y.-W. Wang and L.-N. Yan, *Positivity-preserving scalar auxiliary variable schemes for gradient flows via a quadratic reformulation*, arXiv:2610.01063v1 (first public 2026-10-01), https://arxiv.org/abs/2610.01063.
2. A. Bouchriti, M. Pierre and N. E. Alaa, *Remarks on the asymptotic behavior of scalar auxiliary variable (SAV) schemes for gradient-like flows*, J. Appl. Anal. Comput. 10 (2020), 2198–2219, https://doi.org/10.11948/20190373.
3. M. Jiang, Z. Zhang and J. Zhao, *Improving the Accuracy and Consistency of the Scalar Auxiliary Variable (SAV) Method with Relaxation*, arXiv:2104.06620 (2021), https://arxiv.org/abs/2104.06620.
4. J. Shen, J. Xu and J. Yang, *The scalar auxiliary variable (SAV) approach for gradient flows*, J. Comput. Phys. 353 (2018), 407–416, https://doi.org/10.1016/j.jcp.2017.10.021.
