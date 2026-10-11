# Beta-layer concentration transition in asymmetric cubic global centers

## Finding

Consider the cubic polynomial vector field
\[
\dot x=y(1+\alpha x^2),\qquad \dot y=-x(1+\beta y^2),\qquad \alpha,\beta>0.
\]
For the nonstationary periodic orbit through \((A,0)\), \(A>0\), put
\[
L=\log(1+\alpha A^2),\quad q=\frac{\beta}{\alpha},\quad
U(t)=\frac{\log(1+\alpha x(t)^2)}{L}\in[0,1].
\]
Let \(T_{q,L}\) be its minimal period in original physical time, and let \(\mu_{q,L}\) be the pushforward of normalized time measure \(dt/T_{q,L}\) under \(t\mapsto U(t)\).

**Exact finite-amplitude law.** For every \(L>0\) and \(q>0\), this probability measure has the density
\[
\frac{d\mu_{q,L}}{du}=\frac{e^{(q-1)Lu/2}}{Z_{q,L}\sqrt{(1-e^{-Lu})(1-e^{-qL(1-u)})}},\qquad 0<u<1,
\]
where \(Z_{q,L}\) is the integral of the numerator over \((0,1)\). The exact original-time period is
\[
T_{q,L}=2L\sqrt q\,e^{-qL/2}Z_{q,L}.
\]

**Asymmetric concentration.** Write \(B(v,w)=\int_0^1 t^{v-1}(1-t)^{w-1}\,dt\). If \(q>1\) is fixed, then \(\mu_{q,L}\Rightarrow\delta_1\), and under \(\mu_{q,L}\) the variable \(S=L(1-U)\) converges weakly to the absolutely continuous probability law
\[
f_q(s)=\frac{q\,e^{-(q-1)s/2}}{B((q-1)/(2q),1/2)\sqrt{1-e^{-qs}}},\qquad s>0.
\]
Moreover,
\[
T_{q,L}\sim\frac{2}{\sqrt q}B\!\left(\frac{q-1}{2q},\frac12\right)e^{-L/2}.
\]
If \(0<q<1\) is fixed, then \(\mu_{q,L}\Rightarrow\delta_0\); the variable \(S=LU\) converges to the probability density
\[
g_q(s)=\frac{e^{-(1-q)s/2}}{B((1-q)/2,1/2)\sqrt{1-e^{-s}}},\qquad s>0,
\]
while
\[
T_{q,L}\sim2\sqrt q\,B\!\left(\frac{1-q}{2},\frac12\right)e^{-qL/2}.
\]

**Critical finite-size crossover.** Fix any \(\gamma\in\mathbb R\setminus\{0\}\). For \(L\) sufficiently large set \(q_L=1+\gamma/L>0\); this means the second nonlinear coefficient is adjusted with the orbit energy. Then
\[
\mu_{q_L,L}\Rightarrow\frac{e^{\gamma u/2}}{\int_0^1e^{\gamma v/2}\,dv}\,du,
\qquad
T_{q_L,L}\sim 2Le^{-L/2}e^{-\gamma/2}\int_0^1e^{\gamma v/2}\,dv.
\]
Thus the balanced phase limit is singular: every fixed nonzero coefficient contrast selects a single logarithmic endpoint, but contrast of order inverse-log-energy has a nondegenerate, exponentially tilted distribution. The balanced system itself is not asserted as new here.

## Assumptions and scope

The theorem concerns real \(\alpha>0\) and \(\beta>0\), fixed and unequal for the two endpoint laws. The crossover considers a family of vector fields with \(\beta=\alpha q_L\) and fixed \(\alpha\). All limiting statements take \(A\to\infty\), equivalently \(L\to\infty\). Weak convergence is convergence of integrals against every bounded continuous test function on the indicated compact interval or on \([0,\infty)\) in the rescaled cases. Neither an open-boundary coefficient \(\alpha=0\) nor a general joint limit with arbitrary varying ratios is claimed.

## Proof

**1. Compact periodic levels.** Direct differentiation shows that
\[
H(x,y)=\frac{\log(1+\alpha x^2)}{\alpha}+\frac{\log(1+\beta y^2)}{\beta}
\]
is conserved. For each \(A>0\), the positive level through \((A,0)\) is a smooth, compact, simple closed curve: in every quadrant each nonnegative coordinate is a unique continuous decreasing function of the other, both intercepts are finite, and the level has nonvanishing gradient. The vector field has no equilibrium on it. Hence the flow traverses it periodically, with one traversal per minimal period. Invariance under half-turns and coordinate reflections combined with time reversal makes all four quadrant durations equal.

**2. Exact time density.** On the first quadrant, traversed from the positive \(y\)-axis toward the positive \(x\)-axis, the first integral gives
\[
1+\alpha x^2=e^{Lu},\qquad 1+\beta y^2=e^{qL(1-u)}.
\]
The positive velocity \(\dot x=y(1+\alpha x^2)\) implies
\[
\frac{dt}{du}=\frac{L\sqrt q}{2}e^{-qL/2}\,
\frac{e^{(q-1)Lu/2}}{\sqrt{(1-e^{-Lu})(1-e^{-qL(1-u)})}}.
\]
Each quadrant has the same normalized \(U\)-distribution, by reversing the direction of its \(x\)-motion where necessary. Integrating and multiplying by four proves both exact formulas.

**3. Regime \(q>1\).** Substitute \(s=L(1-u)\). The density's unnormalized integral becomes
\[
Z_{q,L}=\frac{e^{(q-1)L/2}}{L}\int_0^L
\frac{e^{-(q-1)s/2}}{\sqrt{(1-e^{-(L-s)})(1-e^{-qs})}}\,ds.
\]
The integral converges to
\[
I_q=\int_0^\infty\frac{e^{-(q-1)s/2}}{\sqrt{1-e^{-qs}}}\,ds
=\frac1q B\!\left(\frac{q-1}{2q},\frac12\right).
\]
For rigor, split at \(s=L/2\). On the first half the integrands are dominated by a constant times the displayed integrable limit, which behaves like \(s^{-1/2}\) near zero and decays exponentially. On the second half the exponential factor is at most \(e^{-(q-1)L/4}\), and the remaining possible singularity is bounded by a constant times \(1+(L-s)^{-1/2}\). Its integral vanishes. Dominated convergence applies to the numerator with any bounded continuous test function of \(s\), proving the stated weak limit and normalization. The endpoint localization of \(U\) follows because \(1-U=S/L\) and the laws of \(S\) are tight. Substitution into the exact period gives the stated beta coefficient.

**4. Regime \(0<q<1\).** Put \(s=Lu\). Then
\[
Z_{q,L}=\frac1L\int_0^L
\frac{e^{-(1-q)s/2}}{\sqrt{(1-e^{-s})(1-e^{-q(L-s)})}}\,ds.
\]
Splitting at \(L/2\) and using the same integrable endpoint estimates gives the limit
\[
J_q=\int_0^\infty\frac{e^{-(1-q)s/2}}{\sqrt{1-e^{-s}}}\,ds
=B\!\left(\frac{1-q}{2},\frac12\right).
\]
The normalized measures converge under the rescaling \(S=LU\), so \(U\to0\) in probability, and the period constant follows.

**5. Critical crossover.** With \(q_L=1+\gamma/L\), the exact integrand in \(Z_{q_L,L}\) is \(e^{\gamma u/2}w_L(u)\), where
\[
w_L(u)=[(1-e^{-Lu})(1-e^{-(L+\gamma)(1-u)})]^{-1/2}.
\]
For every interior \(u\), \(w_L(u)\to1\). For sufficiently large \(L\), an integrable bound of the form \(C[u(1-u)]^{-1/2}\) holds uniformly because \(1-e^{-Lv}\ge(1-e^{-1})v\) for \(0\le v\le1\), and similarly for the second factor. Dominated convergence proves the tilted distribution and \(Z_{q_L,L}\to\int_0^1e^{\gamma u/2}\,du\). Since \(\sqrt{q_L}\to1\) and \(e^{-q_LL/2}=e^{-L/2}e^{-\gamma/2}\), the period limit follows. This completes the proof.

## Verification

The algebraic first-integral identity and the time-change formula were independently reconstructed from the displayed differential equations. A standalone standard-library script `verify.py` computes the finite-amplitude quadrature after a square-root-desingularizing substitution, compares the two beta-asymptotic period constants, and checks the crossover. Its finite tests are checks of arithmetic and normalization, not proofs of weak convergence, which follows from the analytic dominated-convergence arguments above.

## Relationship to prior work

Llibre and Rondón's classification, first released on 2023-10-11 as arXiv:2310.07454v1, proves that the origin is a global center for the unequal-coefficient cubic subfamily: their Theorem 2(e) and equation (33) specialize to the present vector field with \(\alpha=-2(2b_1+c_1)>0\) and \(\beta=4b_1>0\). Their Theorem 2(a) contains the equal-coefficient boundary. The present result does not claim either global-center classification or the balanced subfamily. It adds the original-physical-time occupation laws, explicit beta-normalized boundary layers, distinct decay exponents, and inverse-logarithmic coefficient crossover in the unequal-coefficient region. García-Saldaña, Llibre and Valls give an earlier broad linear-type global-center classification; no priority is claimed for global-center existence.

## Limitations

No claim is made for the \(\alpha=0\) boundary or any ratios tending to zero or infinity with energy. The two endpoint formulas require a fixed unequal ratio. The crossover assumes specifically \(q_L=1+\gamma/L\) with fixed nonzero \(\gamma\). The existence and period of the balanced subfamily were already studied separately and are not claimed here. Earlier broad center classifications and not fully accessible quantitative literature leave a residual publication-priority risk; the source searches do not prove exhaustive novelty. The result proves asymptotic distributions, not a quantitative uniform total-variation error or a global period-monotonicity theorem.

## References

1. J. Llibre and G. Rondón, *Global centers of a class of cubic polynomial differential systems*, arXiv:2310.07454v1, first posted 2023-10-11, Theorem 2(e), equation (33); full text: https://arxiv.org/html/2310.07454v1.
2. J. D. García-Saldaña, J. Llibre and C. Valls, *Linear type global centers of linear systems with cubic homogeneous nonlinearities*, Rendiconti del Circolo Matematico di Palermo 69 (2020), 771–785, DOI:10.1007/s12215-019-00433-0.
