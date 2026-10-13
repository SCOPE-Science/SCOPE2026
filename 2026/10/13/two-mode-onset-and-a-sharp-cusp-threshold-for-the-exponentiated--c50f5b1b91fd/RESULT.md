# Two-mode onset and a sharp cusp threshold for the exponentiated Haq density

## Finding

Let \(X\) have the exponentiated Haq distribution of Alharthi (2025), with parameters \(\delta>0\), \(\tau>0\), and cumulative distribution function
\[
F_{\delta,\tau}(x)=\left[1-e^{-\tau x}\frac{(1+\tau)^2+\tau x+(\tau x)^2/2}{(1+\tau)^2}\right]^\delta,
\qquad x\ge0.
\]
Set \(\varepsilon=\delta-1\), \(y=\tau x\), \(k=2\tau(\tau+2)\), and
\[
\tau_c=\sqrt{\frac32}-1=0.224744871391589\ldots.
\]
**Theorem (sharp small-exponentiation modal dichotomy).** For each fixed \(\tau>0\), there exists \(\varepsilon_0(\tau)>0\) such that, for every \(0<\varepsilon<\varepsilon_0(\tau)\), the density of \(X\) has **exactly two strict interior local maxima and one strict interior local minimum** if \(0<\tau\le\tau_c\), but **exactly one strict interior local maximum and no other interior stationary point** if \(\tau>\tau_c\). In particular, the bimodality condition in this specified near-\(\delta=1\) regime is sharp, and equality belongs to the bimodal side.

The first maximum lies at a rescaled coordinate \(y_1=\varepsilon+O_\tau(\varepsilon^2)\). If \(\tau<\tau_c\), let \(s=\sqrt{1-k}>0\), \(y_-=1-s\), \(y_+=1+s\). The intervening minimum and the second maximum satisfy
\[
\begin{aligned}
y_2&=y_- -\varepsilon\frac{B_\tau(y_-)(y_-^2+k)}{2s}+O_\tau(\varepsilon^2),\\
y_3&=y_+ +\varepsilon\frac{B_\tau(y_+)(y_+^2+k)}{2s}+O_\tau(\varepsilon^2),
\end{aligned}
\]
where the positive function \(B_\tau\) is defined in the proof. At the critical value \(\tau=\tau_c\), the two non-origin stationary points instead split with a square-root scale:
\[
y_2=1-\frac{2}{\sqrt{3(e-2)}}\sqrt\varepsilon+O(\varepsilon),\qquad
y_3=1+\frac{2}{\sqrt{3(e-2)}}\sqrt\varepsilon+O(\varepsilon).
\]
All locations \(x_j\) in the original lifetime coordinate equal \(y_j/\tau\). These assertions concern *local* modes; there is no claim that both maxima have equal or globally maximal height.

## Assumptions and scope

The shape and rate parameters satisfy \(\delta>0\), \(\tau>0\); the proof concerns each fixed \(\tau\) and \(\delta=1+\varepsilon\) with \(\varepsilon\) sufficiently small and positive. The threshold is exact, while the admissible smallness bound \(\varepsilon_0(\tau)\) is existential and is not claimed to be uniform as \(\tau\to\tau_c\) or \(\tau\to0\). In all parts of the theorem, stationary points are counted in the open support \(x>0\). At \(\delta>1\), the density approaches zero as \(x\downarrow0\), so there is no boundary peak to count as an interior mode. The theorem makes no assertion about general \(\delta\) far from one or about hazard-rate modality.

## Proof

**Step 1: exact normalized derivative.** Write \(D=2(1+\tau)^2\) and \(k=D-2\). Direct differentiation of the stated CDF gives
\[
G_\tau(y)=1-e^{-y}\frac{y^2+2y+D}{D},\qquad
g_\tau(y)=G_\tau'(y)=e^{-y}\frac{y^2+k}{D}.
\]
For \(y>0\), both \(G_\tau(y)\) and \(g_\tau(y)\) are strictly positive; \(G_\tau(y)\) increases from zero to one. The lifetime density is \(f_{\delta,\tau}(x)=\tau\delta\,g_\tau(y)G_\tau(y)^{\delta-1}\). Its logarithmic derivative with respect to \(y\) therefore is
\[
L_{\tau,\varepsilon}(y)
=\frac{d}{dy}\log f_{1+\varepsilon,\tau}(y/\tau)
=A_\tau(y)+\varepsilon B_\tau(y),
\]
where
\[
A_\tau(y)=\frac{2y}{y^2+k}-1
=-\frac{(y-1)^2+k-1}{y^2+k},\qquad
B_\tau(y)=\frac{g_\tau(y)}{G_\tau(y)}>0.
\]
The zeros and signs of \(L\) are exactly those of the derivative of the strictly positive density on \(y>0\). Also \(A_\tau(y)\to-1\) and \(B_\tau(y)\to0\) as \(y\to\infty\).

**Step 2: the new near-origin maximum.** Since \(G_\tau(y)=g_\tau(0)y+O_\tau(y^2)\) with \(g_\tau(0)=k/D>0\), the function \(yB_\tau(y)\) has a real-analytic extension across \(y=0\), with value one there. Thus
\[
H_{\tau}(y,\varepsilon):=yA_\tau(y)+\varepsilon yB_\tau(y)
\]
extends analytically near \((0,0)\). Its first derivatives satisfy
\[
H_\tau(0,0)=0,\qquad
\partial_yH_\tau(0,0)=A_\tau(0)=-1,\qquad
\partial_\varepsilon H_\tau(0,0)=1.
\]
The implicit-function theorem gives exactly one zero near the origin, \(y_1(\varepsilon)=\varepsilon+O_\tau(\varepsilon^2)>0\). Because \(L_{\tau,\varepsilon}(y)\sim\varepsilon/y-1+O_\tau(\varepsilon+y)\) as \(y\downarrow0\), this zero changes the sign from positive to negative. It is a strict interior local maximum.

**Step 3: fixed subcritical parameters.** For \(k<1\), the unperturbed function \(A_\tau\) has precisely two additional positive simple zeros \(y_-=1-\sqrt{1-k}\) and \(y_+=1+\sqrt{1-k}\), with sign pattern negative, positive, negative across the three intervening intervals. At either zero,
\[
A_\tau'(y_\pm)=-\frac{2(y_\pm-1)}{y_\pm^2+k}\ne0.
\]
Applying the implicit-function theorem separately at these zeros of \(L\) gives unique nearby roots \(y_2\) and \(y_3\), with first-order displacements \(-\varepsilon B_\tau(y_\pm)/A_\tau'(y_\pm)\) as displayed above. Their signs correspond to a minimum and a second maximum. No other positive roots arise: choose disjoint neighborhoods of the three limiting roots; on a compact set outside those neighborhoods, \(A_\tau\) is bounded away from zero, and on a sufficiently large tail, \(A_\tau\) is bounded above by a negative constant while \(B_\tau\) is bounded. Shrinking \(\varepsilon>0\) preserves every required sign and excludes extra roots.

**Step 4: fixed supercritical parameters.** When \(k>1\), \(A_\tau(y)<0\) for every \(y\ge0\). The compact-away-from-origin and tail argument in Step 3 implies that \(L\) has no zero beyond the unique near-origin root for all sufficiently small \(\varepsilon>0\). Thus the density has exactly one interior mode.

**Step 5: critical coalescence.** When \(k=1\), equivalently \(\tau=\tau_c\),
\[
A_{\tau_c}(y)=-\frac{(y-1)^2}{y^2+1},\qquad
A_{\tau_c}''(1)=-1.
\]
At \(y=1\), the perturbed logarithmic derivative is \(\varepsilon B_{\tau_c}(1)>0\). Select a small fixed neighborhood of one in which \(A_{\tau_c}''<0\); by continuity, \(\partial_y^2 L_{\tau_c,\varepsilon}<0\) there for sufficiently small \(\varepsilon\). Its values at the neighborhood endpoints remain negative, hence strict concavity yields exactly two simple zeros, one on each side of one. Outside this neighborhood and the near-origin neighborhood, the same compact/tail argument excludes others. Finally, because \(D=3\),
\[
B_{\tau_c}(1)=\frac{2}{3(e-2)},\qquad
L_{\tau_c,\varepsilon}(1+z)=-\frac{z^2}{2}+\varepsilon B_{\tau_c}(1)+O(z^3+\varepsilon|z|).
\]
It follows that \(z=\pm 2\sqrt{\varepsilon}/\sqrt{3(e-2)}+O(\varepsilon)\). With the new near-origin maximum, the sign pattern is positive, negative, positive, negative, giving exactly the same two-maxima/one-minimum classification as the strictly subcritical case. This completes the proof.

## Verification

The included `verify_modal_bifurcation.py` uses symbolic differentiation to check the Haq CDF derivative, the exact logarithmic derivative, the critical value and curvature; it then calculates stationary points at \(\tau=0.2\), \(\tau=\tau_c\), and \(\tau=0.25\), with \(\varepsilon=0.01,0.001,0.0001\). For example, at \(\tau=0.2\) and \(\delta=1.01\), the three numerically located \(y\)-stationary points are approximately \(0.010185705334538\), \(0.627507052557995\), and \(1.373938385248605\). At \(\tau=\tau_c\), the two roots around one exhibit the predicted square-root splitting. The finite-grid bracketing is a check and **does not prove an exhaustive root census**; the global small-\(\varepsilon\) root count follows from Steps 2–5. Run the script with Python and the `sympy` and `mpmath` packages.

## Relationship to prior work

Alharthi (2025), equations (3)–(4) and its density-shape discussion on pages 22499–22501, introduced and displayed the exact exponentiated Haq law, but did not provide this small-exponentiation two-mode criterion, the three-root proof, or its critical square-root splitting. Ahsan-ul-Haq (2022), Section 2.1, previously identified the baseline Haq interior-mode cutoff \((\sqrt6-2)/2\) through the derivative quadratic. **That underlying baseline cutoff and the general exponentiated-CDF construction are not claimed as new.** The new assertion concerns how the *interior critical points of the exponentiated density* change on turning on a small positive exponentiation parameter, including the new near-origin maximum, strict root census and degenerate collision law. Tashkandy and coauthors (2023) study a power transformation of the underlying lifetime variable, not the present CDF-power family, so their density-shape plots do not cover the stated model and quantifiers.

## Limitations

The classification is local in the exponentiation parameter: the theorem deliberately neither determines the complete modality phase diagram for arbitrary \(\delta>1\), nor decides which of the two local maxima is globally highest. The existence of \(\varepsilon_0(\tau)\) is proven but not converted into a numerical uniform cutoff; in particular, no uniform conclusion across the critical \(\tau\) curve is inferred. It does not characterize hazard shapes, mixture identifiability, or likelihood optimization. Numerical checker outputs are corroboration rather than infinite proofs. A mathematically equivalent result outside the inspected primary and related literature cannot be excluded without independent broader review.

## References

1. A. S. Alharthi, "An exponentiated Haq distribution: Theoretical aspects, estimation, and modeling of radiation and COVID-19 datasets," *AIMS Mathematics* **10** (2025), 22497–22530. DOI: 10.3934/math.20251002. Open full text: https://www.aimspress.com/aimspress-data/math/2025/9/PDF/math-10-09-1002.pdf.
2. M. Ahsan-ul-Haq, "Statistical Analysis of Haq Distribution: Estimation and Applications," *Pakistan Journal of Statistics* **38** (2022), 473–490, Section 2.1. Full text: https://www.researchgate.net/publication/362822858_Statistical_Analysis_of_Haq_Distribution_Estimation_and_Applications.
3. Y. Tashkandy et al., "Modeling COVID-19 Real Data Set by a New Extension of Haq Distribution," *Axioms* **12** (2023), 327. DOI: 10.3390/axioms12040327.
4. R. C. Gupta, P. L. Gupta, and R. D. Gupta, "Modeling failure time data by Lehmann alternatives," *Communications in Statistics—Theory and Methods* **27** (1998), 887–904. DOI: 10.1080/03610929808832134 (general exponentiation background).
