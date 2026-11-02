# Unique stationary longitudinal-skewness reversal in a completely reset active Brownian trap

## Finding
For a planar active Brownian particle in an isotropic harmonic trap, with joint Poisson resetting of position and orientation to the origin and the positive horizontal axis, consider the matched-relaxation case in which trap and angular relaxation rates coincide. Write \(p>0\) for dimensionless activity and \(r>0\) for dimensionless resetting rate. The stationary longitudinal third central moment has the exact expression

\[
\kappa_3(r,p)=p\left[A(r)+p^2B(r)\right],
\]
\[
A(r)=\frac{6r(r^2+2r-1)}{(r+1)^2(r+2)(r+3)^2},\quad
B(r)=\frac{2rQ(r)}{(r+1)^6(r+2)(r+3)^2(r+4)(r+9)},
\]
\[
Q(r)=r^7+9r^6+38r^5+84r^4-402r^2-567r-123.
\]

Put \(r_-=\sqrt2-1\) and let \(r_+\) be the unique positive root of \(Q\), lying strictly between \(1\) and \(2\) (approximately \(1.92291776319\)). For **every** \(p>0\), a **unique** \(r_*(p)\in(r_-,r_+)\) satisfies \(\kappa_3(r_*(p),p)=0\). Moreover \(\kappa_3(r,p)<0\) for \(0<r<r_*(p)\), and \(\kappa_3(r,p)>0\) for \(r>r_*(p)\). The function \(p\mapsto r_*(p)\) is strictly increasing, with endpoint limits \(r_-\) at vanishing activity and \(r_+\) at unbounded activity. Equivalently, a positive third central moment can occur at fixed \(r\) and varying \(p\) exactly when \(r>r_-\); inside \((r_-,r_+)\), the unique sign boundary is

\[
p^2=H(r)=-\frac{3(r^2+2r-1)(r+1)^4(r+4)(r+9)}{Q(r)},
\]

and \(H\) increases strictly from zero to infinity. At \(r=1\), the law simplifies to \(\kappa_3(1,p)=p(5-p^2)/80\), so the unique activity sign switch there is \(p=\sqrt5\).

## Assumptions and scope
Let \(\theta_t\) be an angle modulo \(2\pi\) with rotational Brownian motion \(d\theta_t=\sqrt2\,dB_t^{(\theta)}\). Between resets, position \((X_t,Y_t)\) evolves as

\[
dX_t=(-X_t+p\cos\theta_t)dt+\sqrt2\,dB_t^{(x)},\qquad
dY_t=(-Y_t+p\sin\theta_t)dt+\sqrt2\,dB_t^{(y)}.
\]

The three Brownian motions are independent. An independent Poisson process of rate \(r>0\) simultaneously sets \((X,Y,\theta)\) to \((0,0,0)\). The observable is the third *centered* moment of \(X\), equivalently the sign of standardized longitudinal skewness because its variance is strictly positive. This is the physically matched trap/angular relaxation slice \(\beta=1\) of Shee (arXiv:2409.06920); it is not a claim for all trap strengths. Reset direction and the reported longitudinal axis are aligned. Existence and uniqueness of the stationary law follow from regeneration at each reset; all third moments are finite. Statements hold for every positive real \(r\) and \(p\), with no finite-size or weak-activity assumption.

## Proof
**Step 1: Stationary Fourier moments.** Write \(M_{k,n}=\mathbb E[X^k e^{in\theta}]\) for \(k\ge0\), integer \(n\), under the stationary law. The generator acting on \(X^k e^{in\theta}\) and the reset state give

\[
M_{0,0}=1,\quad M_{0,n}=\frac r{r+n^2},\quad M_{k,-n}=M_{k,n},
\]
\[
(r+k+n^2)M_{k,n}=\frac{kp}{2}(M_{k-1,n-1}+M_{k-1,n+1})+k(k-1)M_{k-2,n}\quad (k\ge1),
\]

with the term with negative first index omitted. The last identity follows because \(\partial_x^2X^k=k(k-1)X^{k-2}\), the angular eigenvalue is \(-n^2\), and resetting annihilates positive-degree position monomials. The triangular recurrence gives, without an uncontrolled closure approximation,

\[
\begin{aligned}
m_1&=\mathbb E[X]=\frac{pr}{(r+1)^2},\\
m_2&=\mathbb E[X^2]=\frac2{r+2}+\frac{2p^2}{(r+2)(r+4)},\\
m_3&=\mathbb E[X^3]=\frac{12pr(r+2)}{(r+1)^2(r+3)^2}+\frac{6p^3r(r+5)}{(r+1)^2(r+3)^2(r+9)}.
\end{aligned}
\]

Consequently \(m_3-3m_1m_2+2m_1^3=p[A(r)+p^2B(r)]\), with the stated exact coefficients.

**Step 2: Independent renewal reconstruction.** At a stationary observation time, the backward age \(T\) since the last reset has exponential law of rate \(r\). Conditionally on the age, \(X=pF_T+G_T\), with \(F_T=\int_0^Te^{-(T-s)}\cos(\sqrt2 B_s^{(\theta)})\,ds\) and independent centered Gaussian \(G_T\) of conditional variance \(1-e^{-2T}\). Direct integration of Brownian-angle correlations gives

\[
\mathbb EF_T=\frac r{(r+1)^2},\qquad
\mathbb EF_T^2=\frac2{(r+2)(r+4)},\qquad
\mathbb EF_T^3=\frac{6r(r+5)}{(r+1)^2(r+3)^2(r+9)}.
\]

Furthermore \(\mathbb E[F_T(1-e^{-2T})]=r/(r+1)^2-r/(r+3)^2\). Substitution reproduces all three raw moments above. For reproducibility, the third active-factor integral can be evaluated by splitting \(0<s_1<s_2<s_3<T\) and summing eight Gaussian sign choices \((a,b,c)\in\{-1,1\}^3\):

\[
\mathbb EF_T^3=\frac{6r}{8(r+3)^2}\sum_{a,b,c=\pm1}\frac1{\bigl[r+(a+b+c)^2\bigr]\bigl[r+1+(b+c)^2\bigr]}.
\]

This independently verifies the angular-frequency recurrence, including all diffusion and reset-age factors.

**Step 3: Exact sign classification.** The coefficient \(A\) changes from negative to positive at the unique positive root \(r_-=\sqrt2-1\) of \(r^2+2r-1\). The nonzero coefficient sequence of \(Q\), in descending order, has precisely one sign change. Descartes' rule, \(Q(0)=-123<0\), \(Q(1)=-960<0\) and \(Q(2)=399>0\), show that \(Q\) has exactly one positive root \(r_+\in(1,2)\); this root is simple. Hence \(B<0\) below \(r_+\) and \(B>0\) above. The only region where the two terms can compete is \((r_-,r_+)\). Here \(p^2=H(r)=-A(r)/B(r)\), which is strictly positive. Direct exact differentiation yields

\[
H'(r)=-\frac{3(r+1)^3P(r)}{Q(r)^2},
\]
\[
\begin{aligned}
P(r)={}&r^{11}+15r^{10}+110r^9+610r^8+1985r^7-2133r^6\\
&-45871r^5-165861r^4-262410r^3-166290r^2-18999r-9957.
\end{aligned}
\]

For \(0<r\le2\), the sum of the *positive* terms obeys

\[
r^7(r^4+15r^3+110r^2+610r+1985)\le15124r^5<45871r^5.
\]

All other terms of \(P\) are strictly negative. Thus \(P(r)<0\) throughout \((0,2]\), so \(H'(r)>0\) on \((r_-,r_+)\). Finally \(H(r)\to0\) as \(r\downarrow r_-\) and \(H(r)\to+\infty\) as \(r\uparrow r_+\). The intermediate value theorem proves existence, uniqueness, and monotonic dependence of \(r_*(p)=H^{-1}(p^2)\). The signs outside the intermediate interval follow immediately from those of \(A\) and \(B\). This proves all claims.

## Verification
Run `python verify.py` with dependencies in `requirements.txt`. The verifier reconstructs each raw moment from the exact generator recurrence; independently reconstructs them from reset-age angular Gaussian integrals; verifies the central-moment factorization and \(r=1\) benchmark; differentiates \(H\) symbolically; verifies the unique positive-root sign-variation certificate and the strict global polynomial bound on \((0,2]\); and tests representative signs. These algebraic tests are reproducibility checks. The infinite-parameter uniqueness conclusion follows from the inequalities and Descartes' rule proved above, not from numerical sampling.

## Relationship to prior work
Shee, arXiv:2409.06920 (first public 2024-09-11), derives the model's moment generator, mean parallel displacement, mean-square displacement, radial fourth moment, and radial excess-kurtosis phase diagrams. The generator/renewal construction is prior work; the result here concerns an explicitly evaluated **stationary longitudinal third *central* moment** and its all-activity unique reset-rate sign reversal, not radial kurtosis. Baouche et al., arXiv:2405.06769, establish transient longitudinal skewness for **orientational-only resetting without trapping or positional resetting**; its long-time normalized skewness vanishes and does not determine this stationary classification. Olsen, arXiv:2310.04840, derives moments and sign-changing skewness for **reset-distributed trapped Ornstein-Uhlenbeck/run-and-tumble systems**, not a Brownian-angle-propelled particle jointly reset in position and orientation. Kumar, Sadekar and Basu, arXiv:2008.03294, analyze joint resetting for an **untrapped** active Brownian particle; they do not resolve the present matched-harmonic-trap threshold. The parent moment recurrence implies that exact third moments are in principle derivable, but does not itself state or prove this sharp sign theorem. A comprehensive novelty or publication-priority certification is not claimed.

## Limitations
The theorem is restricted to \(\beta=1\), positive activity, positive reset rates, complete joint resetting, equal isotropic translational diffusion components, and a fixed reset orientation. The sign of a third central moment classifies skewness, not multimodality, Gaussianity, thermodynamic phases, or a full distributional ordering. No proof is claimed for arbitrary trap strength or non-Poisson reset clocks. Literature comparisons are limited to inspected accessible sources and the described searches; broader undiscovered coverage remains possible. No independent scientific audit has been performed.

## References
1. A. Shee, *Active Brownian particle under stochastic position and orientation resetting in a harmonic trap*, arXiv:2409.06920 (first public 2024-09-11), https://arxiv.org/abs/2409.06920.
2. Y. Baouche, T. Franosch, M. Meiners and C. Kurzthaler, *Active Brownian particle under stochastic orientational resetting*, arXiv:2405.06769 (2024), https://arxiv.org/abs/2405.06769.
3. K. S. Olsen, *Steady-state moments under resetting to a distribution*, arXiv:2310.04840 (2023), https://arxiv.org/abs/2310.04840.
4. V. Kumar, O. Sadekar and U. Basu, *Active Brownian Motion in two-dimensions under Stochastic Resetting*, arXiv:2008.03294 (2020), https://arxiv.org/abs/2008.03294.
