# A tricritical spectral onset in an eight-state phosphorylation oscillator

## Finding

Consider a stationary eight-state continuous-time Markov chain formed from an independent four-state phosphorylation cycle and a symmetric two-state gate. The spectral efficiency of the total phosphorylation count has a **complete three-regime phase diagram** as a function of cycle bias and gate-switching rate. In particular, a globally dominant nonzero-frequency peak can emerge *before* the zero-frequency curvature changes sign. The onset is continuous with a square-root frequency law at moderate cycle bias, changes to a quarter-root frequency law at one exactly characterized tricritical bias, and becomes a finite-frequency global-maximizer jump at stronger bias.

Write the cycle rates as \(k_+>0\) forward and \(0\leq k_-\leq k_+\) backward, and let the independent binary gate flip at rate \(r>0\) in each direction. Set
\[
 a=k_++k_->0,\qquad b=k_+-k_-\geq0,\qquad
 s=(b/a)^2\in[0,1],\qquad u=r/a>0.
\]
The observable is the total number of phosphorylated sites: along the four-state cycle \((U,T,ST,S)\), its values are \((0,1,2,1)\), with the gate contributing its state in \(\{0,1\}\). Let \(G(\omega)\) denote its stationary two-sided power spectral density and define
\[
 \eta=1-\frac{G(0)}{\max_{\omega\geq0}G(\omega)}.
\]
Define \(c=1+s\), \(d=3s-1\), and, for \(s>1/3\),
\[
 u_0(s)=\left(\frac{(1+s)^3}{16(3s-1)}\right)^{1/3},\qquad
 F(s)=2^{2/3}(3s-1)^{2/3}-2(1-s)-\frac{(1+s)^2}{3s-1}.
\]
There is exactly one \(s_*\in(1/3,1)\) satisfying \(F(s_*)=0\), with
\[
 s_*=0.9101817562569\ldots,\qquad \sqrt{s_*}=0.9540344628245\ldots.
\]
The following statements are exact for the stated rates.

**Regime I (no spectral excess).** For \(0\leq s\leq1/3\), \(\eta=0\) for every \(u>0\).

**Regime II (continuous onset).** For \(1/3<s\leq s_*\),
\[
 \eta>0\quad\Longleftrightarrow\quad u>u_0(s).
\]
At equality, \(\eta=0\). For each fixed \(s\in(1/3,s_*)\), the global peak frequency as \(\delta=u-u_0(s)\downarrow0\) obeys \(\omega_{\rm pk}/a\sim K_s\delta^{1/2}\) with the explicit positive coefficient specified below. At the tricritical bias \(s=s_*\), the exponent is instead \(1/4\):
\[
 \frac{\omega_{\rm pk}}a\sim
 \left(\frac{48u_0(s_*)^2(3s_*-1)}{3(1+s_*+4u_0(s_*))}\right)^{1/4}\delta^{1/4}.
\]

**Regime III (discontinuous global-peak onset).** For \(s_*<s\leq1\), there is exactly one \(u_c(s)\in(0,u_0(s))\) such that \(\eta>0\) if and only if \(u>u_c(s)\). Define
\[
 A(s,u)=1+s+4u,\quad
 B(s,u)=4u(3s-1)-16u^3-2(1+s)(1-s),\quad
 C(s,u)=16u^3(3s-1)-(1+s)^3.
\]
The threshold is uniquely characterized by
\[
 0<u_c<u_0,\qquad B(s,u_c)>0,\qquad C(s,u_c)<0,\qquad
 B(s,u_c)^2+4A(s,u_c)C(s,u_c)=0.
\]
At \(u=u_c\), the spectrum has **two equal global maximizers**, at \(\omega=0\) and \(\omega=a\sqrt{z_*}>0\), where
\[
 z_*=\frac{B(s,u_c)}{2A(s,u_c)}\in(0,3s-1).
\]
For \(u_c<u<u_0\), \(\eta>0\) even though the zero-frequency point remains a strict local maximum. Thus a criterion based only on low-frequency curvature misses this whole open parameter region. As \(u\downarrow u_c\) from above, the dominant nonzero peak tends to the finite frequency \(a\sqrt{z_*}\).

At the unidirectional-cycle endpoint \(s=1\), the threshold is the unique positive root of
\[
 2u^4-2u^3+3u^2-1=0,
\]
namely \(u_c(1)=0.6283299930390\ldots\), whereas \(u_0(1)=0.6299605249474\ldots\); the tied peak at onset is \(\omega_*/a=0.3422958452082\ldots\). These are distinct despite their numerical proximity. The finite-frequency-onset region also occurs at strictly positive backward hopping rates whenever \(s_*<s<1\).

## Assumptions and scope

All statements concern a finite, *stationary*, irreducible continuous-time Markov chain on \(\{U,T,ST,S\}\times\{0,1\}\). The cycle has nearest-neighbor edges in the displayed order, with common clockwise rate \(k_+>0\) and counterclockwise rate \(k_-\in[0,k_+]\). The binary component makes independent symmetric transitions \(0\leftrightarrow1\) with rate \(r>0\). The cycle and binary component have uniform stationary distributions. Although \(k_-=0\) is allowed mathematically, that directed boundary has unbounded conventional edgewise entropy production; no finite-entropy-production statement is made there. All nonzero backward rates correspond to a finite-edge-rate model.

The power spectral density is defined by \(G(\omega)=\int_{-\infty}^{\infty}\operatorname{Cov}(f(X_0,Y_0),f(X_t,Y_t))e^{-i\omega t}\,dt\). Frequency is nonnegative and the maximum is over the full half-line, not a numerical grid or merely stationary points. Positivity of \(\eta\) means that some positive-frequency spectrum value strictly exceeds \(G(0)\); it is not an assertion about the existence of subdominant local bumps. The spectral formula and the model are established prior work, not claimed as original here.

## Proof

**1. Independent covariance reconstruction.** Number the cycle states by \(j=0,1,2,3\) and put \(f_X(j)=(-1,0,1,0)_j\), \(g_X(j)=(0,1,0,-1)_j\), and \(f_Y(y)=y-1/2\). These functions are centered under the uniform stationary measure. For the cycle generator \(Q_X\), direct evaluation of the two directional jumps gives
\[
 Q_Xf_X=-af_X+bg_X,\qquad Q_Xg_X=-bf_X-ag_X,
\]
while \(Q_Yf_Y=-2rf_Y\). The two components are independent, with \(\operatorname{Var}(f_X)=1/2\) and \(\operatorname{Var}(f_Y)=1/4\). Therefore, for every real \(t\),
\[
 \operatorname{Cov}(f(0),f(t))=
 \frac12e^{-a|t|}\cos(bt)+\frac14e^{-2r|t|}.
\]
Its exact bilateral Fourier transform is
\[
 G(\omega)=\frac{a(a^2+b^2+\omega^2)}{(a^2+b^2+\omega^2)^2-4b^2\omega^2}
 +\frac{r}{4r^2+\omega^2}.
\]
This independently checks the normalization of the formula supplied in the motivating source.

**2. Positive rational certificate for the global comparison.** Let \(z=(\omega/a)^2\geq0\) and \(\mathcal G_{s,u}(z)=aG(a\sqrt z)\). Then
\[
 \mathcal G_{s,u}(z)=\frac{c+z}{D_s(z)}+\frac{u}{4u^2+z},\qquad
 D_s(z)=(c+z)^2-4sz=z^2+2(1-s)z+c^2.
\]
For \(0\leq s\leq1\) and \(z\geq0\), \(D_s(z)>0\). Direct common-denominator subtraction yields the **exact identity**
\[
 \mathcal G_{s,u}(z)-\mathcal G_{s,u}(0)=
 \frac{z\,[C(s,u)+B(s,u)z-A(s,u)z^2]}
 {4uc(4u^2+z)D_s(z)}.
\]
Set \(H_{s,u}(z)=C+Bz-Az^2\). Equivalently,
\[
 H_{s,u}(z)=4u(4u^2+z)(d-z)-cD_s(z).
\]
Every denominator above is strictly positive for \(z>0\). Hence \(\eta>0\) precisely when \(H_{s,u}(z)>0\) for some \(z>0\). If \(d\leq0\), the second identity shows \(H<0\) everywhere on \(z>0\), proving Regime I. If \(d>0\), any positive witness must have \(0<z<d\), and on this interval
\[
 \partial_uH_{s,u}(z)=4(d-z)(12u^2+z)>0.
\]
For each such \(z\), \(H\) starts strictly negative at \(u=0\) and tends to positive infinity as \(u\to\infty\). This establishes existence and uniqueness of a global threshold for positivity of the spectral excess, by taking the lowest rate at which one of the witnesses becomes positive; continuity and the compact witness interval \([0,d]\) prevent lost interior thresholds. A more explicit identification is next.

**3. Low-frequency curvature threshold and unique tricritical bias.** At \(z=0\), \(H=C=16u^3d-c^3\), so it changes sign at exactly \(u_0(s)\). At \(u=u_0\), \(C=0\) and
\[
 B(s,u_0)=cF(s),\qquad
 F'(s)=2^{5/3}d^{-1/3}+2+\frac{(1+s)(5-3s)}{d^2}>0.
\]
The continuous function \(F\) tends to \(-\infty\) at \(s\downarrow1/3\), while \(F(1)=2^{4/3}-2>0\). Thus it has precisely one root \(s_*\). When \(1/3<s\leq s_*\), at \(u=u_0\) one has \(H(z)=Bz-Az^2<0\) for every \(z>0\). The strict monotonicity in \(u\) on the only possible positive-witness interval proves absence of excess for all \(u\leq u_0\). When \(u>u_0\), \(C>0\), so \(H(z)>0\) for all sufficiently small positive \(z\). This proves Regime II including equality.

**4. Interior finite-frequency threshold for stronger bias.** When \(s_*<s\leq1\), at \(u=u_0\) the coefficient \(B>0\) and \(C=0\), so sufficiently small positive \(z\) already have \(H(z)>0\). Strict monotonicity in \(u\) implies that positivity first occurs at some \(u_c<u_0\); at \(u=0\), the entire interval \([0,d]\) is strictly negative, ensuring \(u_c>0\). Since \(C(s,u_c)<0\), and \(H(0)<0\) and \(H(d)<0\), contact with zero must occur at an interior maximizer. The strictly concave quadratic \(H=C+Bz-Az^2\) therefore has a double root at the positive vertex \(z_*=B/(2A)\in(0,d)\), giving the discriminant equation and sign inequalities. Conversely, any \(u\in(0,u_0)\) obeying this double-root condition with a positive vertex is the first threshold by the same strict monotonicity, so the displayed algebraic characterization is unique. At \(u_c\), the subtraction identity shows \(G(0)=G(a\sqrt{z_*})\) and strictly smaller values elsewhere except at those two frequencies. For \(u_c<u<u_0\), the positive quadratic witness persists while \(C<0\); in particular \(G(\omega)-G(0)<0\) for all sufficiently small positive \(\omega\), which proves the stated coexistence of a strict local zero-frequency maximum and a larger nonzero-frequency maximum.

For \(s=1\), direct expansion gives the exact discriminant factorization
\[
 B(1,u)^2+4A(1,u)C(1,u)=64(2u^2+2u+1)(2u^4-2u^3+3u^2-1).
\]
The quartic factor increases strictly on \(u>0\), since its derivative is \(2u(4u^2-3u+3)>0\), and crosses zero once. Its positive root satisfies the necessary sign inequalities, producing the endpoint numbers in the finding.

**5. Frequency-onset laws.** Fix \(1/3<s<s_*\), set \(\delta=u-u_0>0\), and abbreviate
\[
 A_0=A(s,u_0)>0,\quad B_0=B(s,u_0)<0,\quad C_1=48u_0^2d>0.
\]
The numerator satisfies \(H(z)=C_1\delta+B_0z+O(\delta^2+\delta z+z^2)\). The positive denominator in the subtraction formula is analytic and bounded away from zero near \((z,\delta)=(0,0)\). Differentiation with respect to \(z\), followed by the implicit-function theorem at the nondegenerate derivative \(2B_0<0\), yields the unique local maximizer
\[
 z_{\rm pk}=\frac{C_1}{-2B_0}\delta+O(\delta^2).
\]
At the threshold the global spectrum has a strict maximum only at \(z=0\), so compactness and decay of the spectrum at infinity ensure this nearby maximizer is global for sufficiently small \(\delta>0\). Therefore \(\omega_{\rm pk}/a\sim[C_1/(-2B_0)]^{1/2}\delta^{1/2}\).

At \(s=s_*\), instead \(B_0=0\) and \(H(z)=C_1\delta-A_0z^2+O(\delta^2+\delta z+\delta z^2)\). Differentiating the full spectral excess and rescaling \(z=\delta^{1/2}y\) gives the leading stationarity condition \(C_1-3A_0y^2=0\), with a strict positive solution. Thus
\[
 z_{\rm pk}\sim\sqrt{\frac{C_1}{3A_0}}\,\delta^{1/2},\qquad
 \omega_{\rm pk}/a\sim\left(\frac{C_1}{3A_0}\right)^{1/4}\delta^{1/4}.
\]
The same strict global-maximizer argument applies because the threshold spectrum is strictly below the value at zero for every \(z>0\). Finally, when \(s>s_*\), at onset the isolated interior tied maximum \(z_*\) is nondegenerate and all other positive frequencies except zero have lower values. It consequently persists as the global positive-frequency maximizer immediately above \(u_c\) and tends to \(z_*\), demonstrating the finite jump.

## Verification

Run `python3 verify.py` with a standard Python 3 installation. The standalone script constructs the eight-state Markov generator for several rational transition-rate families, verifies its stationary invariance and centered eigenfunction identities exactly, checks 320 rational instances of both algebraic spectrum-subtraction formulas (640 exact identities), checks the endpoint quartic factorization at rational values, locates and tests the tricritical and tangency thresholds, and tests the predicted peak-frequency scaling using a cancellation-resistant excess expression. A completed replay returned `PASS: 783 deterministic exact and floating-point checks`.

These checks test finite examples and exact rational algebra; the statements for all real parameters, existence, uniqueness and asymptotic laws follow from the proof above, not from an enumeration of examples. All helper code required for replay is included. The approximation constants in numerical displays are indicative and not used to certify exact inequalities.

## Relationship to prior work

Jia (2026), arXiv:2610.23310v1, Eq. (31)–(33), introduced the independent four-cycle-plus-gate Markov model and derived its exact power spectrum. Its Eq. (34) supplies a *sufficient* onset criterion, equivalent here to \(C(s,u)>0\); that condition is not necessary. The work above identifies precisely the parameter region where it is not necessary, proves the complete necessity-and-sufficiency classification, and characterizes the distinct frequency-onset exponents. The source also establishes broad spectral efficiency and dissipation upper bounds; none are claimed anew.

Jia, Qian and Zhang (2019), arXiv:1909.09769, analyzed a different feedback-driven hybrid gene-expression model with exact spectral formulas and stochastic bifurcations. The published phase structure concerns that generator and feedback parameters, and does not by itself imply the product-generator threshold \(s_*\), the finite-frequency tie, or the quarter-root law. Thomas and colleagues (2013) studied approximate noisy biochemical spectral peaks near Hopf bifurcations, not this exact finite-state global comparison. Related general stochastic-resonance spectrum results, including Löfstedt and Coppersmith (1994), concern periodic forcing or bistable switching rather than this stationary additive cycle-plus-gate observable. These comparisons identify contextual literature rather than establishing exhaustive novelty.

## Limitations

This is an exactly solvable, *independent* binary gate and homogeneous four-cycle. Coupling the gate to the phosphorylation rates, nonuniform cycle rates, asymmetric gate switching, other observables, and finite-sample spectral estimation fall outside the theorem. The result classifies positive spectral efficiency and location of the leading peak, not the sign of every derivative of the spectrum or whether all secondary local extrema exist. The endpoint \(k_-=0\) has mathematically well-defined irreducible dynamics but unbounded conventional entropy-production accounting. The theorem contains no inference about an actual cyanobacterial experimental transition.

The four-cycle-plus-gate spectral formula is previously known. The novelty assessment concerns only the sharp global comparison and onset laws; a more general unlocated theorem for positive rational spectra could imply parts of them. Some related publisher-hosted articles were inspected only at abstract level, so independent publication-priority verification remains necessary. Finite checks are not a substitute for an independent audit.

## References

1. Chen Jia, “Fundamental Bounds on the Oscillation Efficiency of Markov Networks,” arXiv:2610.23310v1 (first public posting 2026-10-16), especially Eqs. (31)–(34) and accompanying discussion. https://arxiv.org/html/2610.23310v1
2. Chen Jia, Hong Qian, Michael Q. Zhang, “Exact power spectrum in a minimal hybrid model of stochastic gene expression oscillations,” arXiv:1909.09769 (2019). https://arxiv.org/abs/1909.09769
3. Philipp Thomas, Arthur V. Straube, Jens Timmer, Christian Fleck, Ramon Grima, “Signatures of nonlinearity in single cell noise-induced oscillations,” *Journal of Theoretical Biology* **335**, 222–234 (2013), DOI: 10.1016/j.jtbi.2013.06.021. https://pubmed.ncbi.nlm.nih.gov/23831270/
4. R. Löfstedt and S. N. Coppersmith, “Stochastic resonance: Nonperturbative calculation of power spectra and residence-time distributions,” *Physical Review E* **49**, 4821 (1994), DOI: 10.1103/PhysRevE.49.4821. https://doi.org/10.1103/PhysRevE.49.4821
