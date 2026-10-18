# Sharp pure-pulse vaccination cutoff for a two-season epidemic

## Finding
Let a yearly transmission environment have one high season, of length \(h\), immediately after an upward transmission jump. Write the high and low rates as \(\beta_H>\beta_L>0\). Among **all nonnegative periodic vaccination measures** of prescribed mass \(B\) per period, a single pulse at the start of the high season uniquely minimizes the disease-free invasion reproduction number **if and only if**
\[
0<B\le B_*:=\min\left\{\log\frac{\beta_H}{\alpha},\ \log\frac{\alpha}{\beta_L}\right\},\qquad
\alpha:=\frac{\beta_H(1-e^{-\delta h})+\beta_L(e^{-\delta h}-e^{-\delta T})}{1-e^{-\delta T}}.
\]
Here \(\delta>0\) is the combined waning/demographic return rate, and \(T>h>0\) is the period. If \(B>B_*\), a two-pulse schedule obtained by relocating a sufficiently small positive portion of the budget strictly improves the reproduction number. Thus the boundary is sharp, including equality. For the two-level seasonal example with \(\delta=T=1\), \(h=1/2\), \(\beta_H=7/4\), and \(\beta_L=1/4\), the exact cutoff is \(B_*=0.3909799575971128\ldots\), resolving the numerically observed transition near \(0.4\) in [1, Sect. 7].

Throughout the pure-pulse range, the minimum weighted susceptible exposure is explicit:
\[
J_{\min}(B)=\beta_H h+\beta_L(T-h)-\frac{1-e^{-B}}{1-e^{-B-\delta T}}
\frac{\beta_H(1-e^{-\delta h})+\beta_L(e^{-\delta h}-e^{-\delta T})}{\delta}.
\]
The reproduction number is \(J_{\min}(B)/[T(\gamma+\mu)]\), in the notation of the disease-free SIRVS linearization of [1]; this positive normalizing factor does not change the minimizer.

## Assumptions and scope
Fix \(\delta>0\), \(T>h>0\), and \(\beta_H>\beta_L>0\). Set the \(T\)-periodic transmission function \(\beta(t)=\beta_H\) for \(t\bmod T\in[0,h)\), and \(\beta(t)=\beta_L\) otherwise. The admissible class comprises **all nonnegative \(T\)-periodic locally finite Borel measures** \(m\) with \(m([0,T))=B\). Absolutely continuous, atomic, mixed, and singular-continuous schedules are all permitted. For an atom of mass \(b\) at time \(s\), susceptible fraction satisfies \(S(s+)=e^{-b}S(s-)\). Between pulses the disease-free equation is \(S'=\delta(1-S)-\eta S\) for vaccination density \(\eta\). For a general measure the unique positive periodic trajectory is defined by the corresponding multiplicative-measure evolution. The objective is
\[
J(m)=\int_0^T\beta(t)S_m(t)\,dt.
\]
Only disease-free linearized invasion is optimized, not infection prevalence, attack rate, vaccine doses actually taken up, or a stochastic epidemic outcome. The budget measures cumulative offered per-capita vaccination intensity, not a hard cap on the distinct number of vaccine recipients. The pulse time is \(0\bmod T\), where transmission jumps from low to high; the value of the transmission function exactly at a switching point is immaterial.

## Proof
**1. Existence of the periodic trajectory and strict convexity.** Put \(E=e^{-\delta T}\), \(q=e^{-B}\). For \(0<u<T\), let \(m((t-u,t])\) denote the mass on the positively oriented cyclic arc of length \(u\) ending at \(t\). Variation of constants over the infinite past and summation of full previous periods give, for almost every \(t\),
\[
S_m(t)=\frac{\delta}{1-qE}\int_0^T e^{-\delta u-m((t-u,t])}\,du.
\tag{1}
\]
In particular \(S_m>0\) and is periodic, while the multiplicative transition over a period has contraction factor \(qE<1\), proving uniqueness. Because every feasible measure has the same total mass \(B\), the denominator in (1) is fixed. For each arc the exponential of minus its mass is convex in \(m\); thus \(J\) is convex. It is **strictly** convex: if two periodic measures differ, their masses differ on a set of positive two-dimensional measure of cyclic arcs \((t-u,t]\), and \(\beta(t)>0\) gives a strict integrated Jensen inequality. Indeed if the arc integrals of a signed measure vanished for almost all \((t,u)\), the cumulative distribution function would be almost everywhere constant, forcing that signed measure to be zero. This argument also covers atoms and singular-continuous controls.

**2. Candidate trajectory and marginal-value function.** Take \(m_0=B\sum_{k\in\mathbb Z}\delta_{kT}\), let \(A=(1-q)/(1-qE)\), and define
\[
F=\int_0^T\beta(t)e^{-\delta t}\,dt
=\frac{\beta_H(1-e^{-\delta h})+\beta_L(e^{-\delta h}-E)}{\delta},
\qquad G(s)=\int_s^T\beta(t)e^{-\delta t}\,dt.
\]
The periodic trajectory just after its pulse is \(S_{m_0}(0+)=q(1-E)/(1-qE)\), and for \(0<t<T\) it is
\[
S_{m_0}(t)=1-Ae^{-\delta t}.
\tag{2}
\]
Thus \(J(m_0)=\beta_H h+\beta_L(T-h)-AF\). An infinitesimal pulse at \(s\bmod T\), while holding the rest of the candidate schedule fixed, reduces \(J\) at rate
\[
H(s)=(e^{\delta s}-A)\left(G(s)+\frac{qEF}{1-qE}\right),
\qquad 0\le s\le T.
\tag{3}
\]
To derive (3), the first-order susceptible reduction at \(s\) equals the pre-insertion susceptible level in (2). Propagate it forward with factor \(e^{-\delta(t-s)}\), multiplying by \(q\) whenever the candidate pulse at a subsequent multiple of \(T\) is crossed; sum the resulting geometric series over future periods. Equation (3) is the integrated transmission-weighted response. Direct substitution verifies \(H(0)=H(T)=q(1-E)F/(1-qE)^2\).

The directional derivative in any feasible direction \(m-m_0\), with \(m\) of total mass \(B\), is
\[
\left.\frac{d}{d\varepsilon}J((1-\varepsilon)m_0+\varepsilon m)\right|_{\varepsilon=0+}
=\int_{[0,T)}\bigl(H(0)-H(s)\bigr)\,m(ds).
\tag{4}
\]
This follows first for finite atomic perturbations from (3) and then for all finite measures by the bounded continuous marginal-value kernel and dominated convergence in (1). By convexity and (4), \(m_0\) is globally optimal **if and only if** \(H(s)\le H(0)\) for all \(s\in[0,T]\); necessity uses the competitor \((B-\varepsilon)\delta_0+\varepsilon\delta_s\). Strict convexity ensures uniqueness whenever optimality holds.

**3. An exact two-endpoint test.** On either open constant-transmission season, with transmission \(b\), one can write
\[
G(s)+\frac{qEF}{1-qE}=\frac b\delta e^{-\delta s}+C_b
\quad\Rightarrow\quad
H'(s)=\delta C_b e^{\delta s}+b A e^{-\delta s}.
\tag{5}
\]
The one-sided endpoint derivatives are
\[
H'(0+)=\frac{(1-E)(\alpha-q\beta_H)}{1-qE},\qquad
H'(T-)=\frac{(1-E)(q\alpha-\beta_L)}{1-qE},
\qquad\alpha=\frac{\delta F}{1-E}.
\tag{6}
\]
If \(H'(0+)\le0\), (5) implies \(C_{\beta_H}<0\). Hence \(H''(s)=\delta^2 C_{\beta_H}e^{\delta s}-\delta\beta_H A e^{-\delta s}<0\) on \((0,h)\), so \(H\) decreases strictly throughout the high season. If \(H'(T-)\ge0\), (5) implies \(H'>0\) throughout \((h,T)\): if \(C_{\beta_L}\ge0\) both terms of (5) are nonnegative with one strictly positive, while if \(C_{\beta_L}<0\), then \(H''<0\), making all earlier derivatives greater than or equal to \(H'(T-)\). Thus \(H\) increases strictly throughout the low season. Since \(H(0)=H(T)\), both endpoint inequalities suffice for \(H(s)<H(0)\) at every interior \(s\), including the switch \(h\).

Conversely, if \(H'(0+)>0\), then \(H(s)>H(0)\) at some sufficiently small \(s>0\). If \(H'(T-)<0\), then \(H(s)>H(T)=H(0)\) at some \(s<T\). Either case contradicts the first-order optimality condition. Consequently the two endpoint inequalities are simultaneously **necessary and sufficient**. As \(q=e^{-B}\), they become \(q\ge \alpha/\beta_H\) and \(q\ge\beta_L/\alpha\), equivalent to the claimed \(B\le B_*\). Both logarithms are strictly positive because \(\beta_L<\alpha<\beta_H\). Equality is included; even there the derivative arguments give strict interior separation. For \(B>B_*\), the adverse one-sided derivative supplies an improving two-pulse competitor by (4). This completes the proof for every admissible vaccination measure.

## Verification
Run `python3 verify.py` using only the Python standard library. The verifier computes the periodic susceptibility exactly for arbitrary finite pulse schedules using affine period maps and elementary exponential integrals, independently of the marginal-value calculation. It checks 54 first-order variations (including endpoint and above-threshold cases), 150 random positive-parameter families below and above the predicted boundary, and the printed school-term cutoff. Successful output begins `VERIFY_OK`. These finite samples check calculations but do **not** constitute the proof for continuous or singular schedules; equations (1)–(6) provide that proof.

For the parameters in [1, Fig. 9], after shifting time origin to the upward jump, \(\alpha=1.183688996802782\ldots\), yielding \(B_*=\log[(7/4)/\alpha]=0.3909799575971128\ldots\). At annual budget \(B=1/4\), a single pulse has \(J=0.768030944901295\ldots\), less than the uniform-rate budget's \(J=0.8\). At \(B=1/2\), relocating a sufficiently small pulse to the beginning of the high season strictly improves on a single pulse, as both the analytic derivative and independent affine-map calculation verify.

## Relationship to prior work
Gavish and Katriel [1] introduce this SIRVS vaccination objective over nonnegative periodic measures, prove structural properties of optimal schedules, and report numerically that the indicated two-level seasonal profile has pure pulse optimum for annual budget below approximately \(0.4\) (their Fig. 9). They explicitly leave analytical characterization of pulses at an upward transmission discontinuity incomplete (Theorem 10 and Sect. 7). The general mathematical study by Gavish and Katriel [2] proves strict convexity and an abstract necessary-and-sufficient first-variation condition for periodic measure controls (Lemmas 1 and 5); its Theorem 5 and Example 6 do **not** give this model-specific sharp cutoff. Those general variational tools are therefore **prior results**, not new claims here. The new contribution is the closed-form **two-endpoint reduction** and its sharp necessary-and-sufficient threshold for the full admissible measure class, with an explicit minimum value in the pure-pulse phase. Earlier pulse vaccination and periodic SIR analyses [3,4] concern different vaccination assumptions or analyze prescribed pulse strategies rather than this optimization over all measure-valued schedules. The mathematical result may still be a special case of a broader, not yet identified theorem for weighted positive bilinear control systems; the literature comparison is not an independent certification of novelty.

## Limitations
The theorem does not determine the post-cutoff mixture of continuous and atomic vaccination, and it does not claim any optimality for infection prevalence, attack rate, or final epidemic size when the disease is endemic. It assumes instantaneous perfect pulses in a disease-free linearization, constant rates within exactly two seasons, fixed total annual vaccination intensity, and no cap on vaccination intensity. Biological and logistical restrictions may make concentrated pulses infeasible. The proven bound is specific to the piecewise-constant two-season profile, not arbitrary forcing. A mathematical originality risk remains from possible unpublished or unindexed general control results. Independent audit has not been performed.

## References
[1] N. Gavish and G. Katriel, *Optimal Vaccination for Contagious Diseases with Seasonal Transmission*, Bulletin of Mathematical Biology 88, article 170 (first public 2026-09-02), DOI: 10.1007/s11538-026-01741-0, https://link.springer.com/article/10.1007/s11538-026-01741-0 . See Sect. 2, Theorem 10, and Sect. 7/Fig. 9.

[2] N. Gavish and G. Katriel, *Optimal Regulation in a Time-Periodic Environment: Insights from a Simple Model*, Applied Mathematics & Optimization (2026), DOI: 10.1007/s00245-025-10374-z, https://link.springer.com/article/10.1007/s00245-025-10374-z . See Sect. 2, Sect. 3.4, and Sect. 4.1 (strict convexity, switching condition).

[3] N. O. Onyango and J. Müller, *Determination of optimal vaccination strategies using an orbital stability threshold from periodically driven systems*, Journal of Mathematical Biology 68 (2014), 763–784, DOI: 10.1007/s00285-013-0648-8 (different susceptible-only, lasting-immunity model).

[4] J. P. S. M. de Carvalho and A. A. Rodrigues, *Pulse vaccination in a SIR model: global dynamics, bifurcations and seasonality*, arXiv:2312.02306 (2023), https://arxiv.org/abs/2312.02306 (fixed pulse strategies and epidemic dynamics).
