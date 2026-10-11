# Tricritical crossover and exact first-order coexistence in an edge-weighted forbidden-transition correspondence

## Finding

Consider three symbols \(S=\{-1,0,1\}\), with every directed edge allowed except \((0,0)\). For a real parameter \(w>0\), assign an edge weight \(w\) exactly when one endpoint is \(0\), and weight \(1\) otherwise. Let \(\gamma(s,t)=\mu(s)Q(s,t)\) be the two-coordinate distribution of a stationary Markov pair, where \(Q\) respects these edges and \(\mu Q=\mu\). Define its edge correlation \(z(\gamma)=\sum_{s,t}\gamma(s,t)st\). At \(\beta\geq0\), maximize the nonlinear pressure
\[
\mathcal P_{w,\beta}=\sup_{\mu Q=\mu}\left\{-\sum_{s,t}\gamma(s,t)\log Q(s,t)+\sum_{s,t}\gamma(s,t)\log W_w(s,t)+\frac{\beta}{2}z(\gamma)^2\right\},
\]
where the sums run only over allowed edges, \(W_w(s,t)=w\) if exactly one endpoint is zero, and \(W_w(s,t)=1\) otherwise. As usual, terms with \(\gamma(s,t)=0\) contribute zero.

Put \(k=1+2w^2>1\), and set
\[
\lambda_k(y)=\cosh y+\sqrt{\sinh^2y+k},\qquad
z_k(y)=\frac{\sinh y}{\sqrt{\sinh^2y+k}},\qquad
R_k(y)=\frac{y}{z_k(y)}\quad(y>0).
\]
Each maximizer is a Perron--Frobenius Markov pair at one of the fields \(y=0\) or \(y=\pm y_\beta\), with the following **complete phase diagram**.

**Continuous side, \(1<k\leq3\).** If \(0\leq\beta\leq\sqrt{k}\), there is exactly one maximizer, at \(y=0\). If \(\beta>\sqrt{k}\), there are exactly two, at the fields \(\pm y_\beta\), where \(y_\beta>0\) is the unique solution of \(R_k(y_\beta)=\beta\). For fixed \(1<k<3\), the positive correlation satisfies \(z_{k,\beta}\sim\sqrt{6/[\sqrt{k}(3-k)]}\,\sqrt{\beta-\sqrt{k}}\) as \(\beta\downarrow\sqrt{k}\). At \(k=3\), its fourth-root order was already established for the unweighted model.

**First-order side, \(k>3\).** There is exactly one positive solution \(y_s(k)\) of
\[
\sinh y\,(\sinh^2y+k)-ky\cosh y=0,
\]
and exactly one positive solution \(y_t(k)>y_s(k)\) of
\[
\log\frac{\lambda_k(y)}{\lambda_k(0)}-\frac{y z_k(y)}2=0.
\]
Define \(\beta_s(k)=R_k(y_s(k))\) and \(\beta_t(k)=R_k(y_t(k))\). Then
\[
\beta_s(k)<\beta_t(k)<\sqrt{k}.
\]
There is one globally maximizing pair at \(y=0\) for \(\beta<\beta_t(k)\), exactly three at \(y=0,\pm y_t(k)\) for \(\beta=\beta_t(k)\), and exactly two at \(y=\pm y_\beta\) for \(\beta>\beta_t(k)\), where \(y_\beta>y_s(k)\) is the unique solution of \(R_k(y_\beta)=\beta\) on the increasing branch. Thus the zero-correlation phase and two symmetry-related nonzero-correlation phases coexist at a **unique** first-order transition. The zero-correlation branch remains locally stable after the nonzero stationary branches first appear at \(\beta_s(k)\); its local-stability boundary \(\sqrt{k}\) is strictly above the global transition.

The nonlinear pressure is explicitly
\[
\mathcal P_{w,\beta}=
\begin{cases}
\log(1+\sqrt{k}),&0\leq\beta\leq\beta_*(k),\\
\log\lambda_k(y_\beta)-\frac\beta2z_k(y_\beta)^2,&\beta>\beta_*(k),
\end{cases}
\]
where \(\beta_*(k)=\sqrt{k}\) if \(k\leq3\), and \(\beta_*(k)=\beta_t(k)\) if \(k>3\). At the first-order transition the two displayed formulas agree.

**Sharp tricritical asymptotics.** For \(\tau=k-3\downarrow0\) from the first-order side,
\[
\boxed{\begin{aligned}
\frac{\beta_s(k)}{\sqrt{k}}&=1-\frac{5}{216}\tau^2+o(\tau^2),\\
\frac{\beta_t(k)}{\sqrt{k}}&=1-\frac{5}{288}\tau^2+o(\tau^2),\\
\frac{y_s(k)^2}{\tau}&\longrightarrow\frac56,\qquad
\frac{y_t(k)^2}{\tau}\longrightarrow\frac54,\\
\frac{z_k(y_t(k))}{\sqrt\tau}&\longrightarrow\sqrt{\frac5{12}}.
\end{aligned}}
\]
In particular, the first-order discontinuity vanishes as \(\sqrt{k-3}\), whereas the metastability interval shrinks quadratically in \(k-3\).

There is also a matched **continuous-side crossover**. Fix \(b\geq0\), let \(\varepsilon=3-k\downarrow0\), and choose \(\beta=\sqrt{k}(1+b\varepsilon^2)\). Write \(z_{k,\beta}\geq0\) for the nonnegative correlation of a global maximizer (zero when \(b=0\)). Then
\[
\boxed{\lim_{\varepsilon\downarrow0}\frac{z_{k,\beta}}{\sqrt\varepsilon}=
\sqrt{\frac{\sqrt{25+1080b}-5}{18}}.}
\]
This explicitly interpolates between the ordinary quadratic response and the fourth-root critical degeneracy.

## Assumptions and scope

All quantities are finite-state and real. The edge weight \(w\) is fixed and strictly positive, and \(k\) is a real parameter strictly exceeding \(1\), not necessarily an integer. The inverse-temperature coefficient satisfies \(\beta\geq0\). The entropy is the stationary one-step conditional entropy, not the entropy of the one-coordinate marginal. The claims concern global maximizers over **all** stationary kernels supported on the eight allowed directed edges, including possible reducible kernels, rather than only local self-consistency solutions. A stationary pair is identified by its two-coordinate distribution; at the maximizers all three symbol masses are positive.

For a specified field \(y\), the kernel and stationary distribution are explicit. In symbol order \((-1,0,1)\), put
\[
B_{w,y}=\begin{pmatrix}e^y&w&e^{-y}\\w&0&w\\e^{-y}&w&e^y\end{pmatrix},\qquad
r_y=\left(1,\frac{2w}{\lambda_k(y)},1\right).
\]
Then \(\mu_y(s)=r_y(s)^2/\sum_t r_y(t)^2\) and \(Q_y(s,t)=B_{w,y}(s,t)r_y(t)/(\lambda_k(y)r_y(s))\). The opposite-field phases have identical one-coordinate marginals but different edge distributions; their correlations are \(\pm z_k(y)\).

## Proof

**1. Exact linear pressure and reduction.** The positive matrix \(B_{w,y}\) on allowed edges is primitive. Its antisymmetric eigenvalue is \(2\sinh y\), and its positive symmetric eigenvalue is \(\lambda_k(y)\), with positive eigenvector \(r_y\) as stated. The Perron--Frobenius formulas produce its unique maximizing stationary Markov pair. Differentiating its pressure \(P_k(y)=\log\lambda_k(y)\) gives \(P_k'(y)=z_k(y)\), while
\[
z_k'(y)=\frac{k\cosh y}{(\sinh^2y+k)^{3/2}}>0.
\]
Consequently, \(y\mapsto z_k(y)\) is an odd, strictly increasing bijection from \(\mathbb R\) onto \((-1,1)\).

Let \(h_k(z)\) denote the maximal *weighted* entropy \(h_\mu(Q)+\int\log W_w\,d\gamma\) among stationary pairs of correlation \(z\). The finite-state linear variational principle and Legendre duality yield \(h_k(z)=P_k(y)-yz\) at \(z=z_k(y)\) and \(h_k'(z)=-y\) on \((-1,1)\). At the endpoints the one-sided derivative of \(h_k\) diverges in magnitude, so a maximizer of \(h_k(z)+\beta z^2/2\) cannot occur at \(\pm1\) for finite \(\beta\). Its stationary equation is therefore
\[
\beta z=y,\qquad\text{equivalently}\qquad R_k(y)=\beta\quad(y>0).
\]
By strict linear-equilibrium uniqueness, every global maximizing correlation identifies exactly one stationary Markov pair. Reflection of the symbols sends \(y\) to \(-y\).

**2. Global shape of the response ratio.** Set
\[
N_k(y)=\sinh y\,(\sinh^2y+k)-ky\cosh y.
\]
Direct differentiation gives
\[
N_k(0)=0,\qquad N_k'(y)=\sinh y\,[3\sinh y\cosh y-ky],
\]
while the sign of \(R_k'(y)\) agrees with the sign of \(N_k(y)\). The ratio \(3\sinh y\cosh y/y\) increases strictly from \(3\) to infinity, since \(\sinh(2y)/(2y)\) does. If \(1<k\leq3\), then \(N_k(y)>0\) for every \(y>0\). Together with \(R_k(0+)=\sqrt{k}\) and \(R_k(y)\to\infty\), this proves the asserted continuous-side global maximizers by the sign of
\[
\frac{d}{dz}\left(h_k(z)+\frac\beta2z^2\right)=z\,[\beta-R_k(y)]\qquad(z=z_k(y)>0).
\]
If \(k>3\), the derivative \(N_k'\) is negative before one positive point and positive afterward. Since \(N_k\to\infty\), it vanishes once at \(y_s>0\). Thus \(R_k\) decreases from \(\sqrt{k}\) to its sole minimum \(\beta_s\), then increases to infinity. For \(\beta_s<\beta<\sqrt{k}\), the smaller positive nonzero stationary point is a local minimum of the constrained free energy and the larger is a local maximum; \(z=0\) is also a local maximum.

**3. Unique global coexistence.** At any positive stationary point \(\beta=R_k(y)\), the free-energy difference between that point and \(z=0\) is
\[
C_k(y)=P_k(y)-P_k(0)-\frac{y z_k(y)}2.
\]
Its derivative \(C_k'(y)=[z_k(y)-y z_k'(y)]/2\) has the same sign as \(R_k'(y)\). Therefore for \(k>3\), \(C_k\) strictly decreases from \(0\) to a negative minimum at \(y_s\), and then strictly increases to infinity: \(P_k(y)=y+o(1)\) and \(z_k(y)\to1\) as \(y\to\infty\). This proves existence and uniqueness of \(y_t>y_s\). On the increasing large-field branch, the free-energy difference is strictly increasing with \(\beta\) because its derivative is \(z^2/2>0\), while the zero-field value stays constant. The nonzero branch has positive advantage at \(\beta=\sqrt{k}\), where the origin is not a local maximum. Hence \(\beta_s<\beta_t<\sqrt{k}\), and the complete global-maximizer count follows. At \(\beta_t\), the left and right pressure slopes are respectively \(0\) and \(z_k(y_t)^2/2\); it is a genuine first-order transition.

**4. Matched tricritical expansion.** A Taylor expansion, valid uniformly for \(k\) in a neighborhood of \(3\), gives
\[
\frac{R_k(y)}{\sqrt{k}}=1+\frac{3-k}{6k}y^2+
\frac{7k^2+30k-45}{360k^2}y^4+O(y^6).
\]
For \(k=3+\tau\), take \(y=\sqrt\tau\,u\) and \(\beta=\sqrt{k}(1+b\tau^2)\). Taylor expansion of the **full** free-energy difference at the indicated correlation gives, locally uniformly for bounded \(u,b\),
\[
\frac{h_k(z_k(y))+\frac\beta2z_k(y)^2-h_k(0)}{\tau^3}
\longrightarrow \frac1{\sqrt3}\left(\frac{bu^2}{2}+\frac{u^4}{72}-\frac{u^6}{180}\right).
\]
Its positive stationary points satisfy \(b=-u^2/18+u^4/30\). The nonzero spinodal has \(u_s^2=5/6\), giving \(b_s=-5/216\). At coexistence the stationary free-energy difference also vanishes, and substitution shows \(u_t^2=5/4\), giving \(b_t=-5/288\). To justify the scales rather than merely identify subsequential limits, note that positivity of \(N_3(y)\) and \(C_3(y)\) for every fixed \(y>0\), together with the uniqueness arguments above, implies \(y_s,y_t\to0\). Uniform Taylor expansions at \(k=3+\tau\) sharpen the stationarity equations to
\[
\frac{R_k'(y)}{\sqrt{k}\,y}=-\frac{\tau}{9}+\frac{2}{15}y^2+O(\tau^2+\tau y^2+y^4),
\]
and
\[
C_k(y)=\sqrt3\left(-\frac{\tau y^4}{216}+\frac{y^6}{270}\right)
+O(\tau^2 y^4+\tau y^6+y^8).
\]
Dividing the respective root equations by the displayed lowest powers of \(y\) forces \(y_s^2/\tau\to5/6\) and \(y_t^2/\tau\to5/4\); in particular neither root can approach zero on a scale incompatible with \(\sqrt\tau\). Since \(z_k(y)/y\to1/\sqrt3\), the asserted order-parameter jump follows.

For \(k=3-\varepsilon\), the same ratio expansion with \(y=\sqrt\varepsilon\,u\) gives
\[
\frac{R_k(\sqrt\varepsilon\,u)}{\sqrt k}=1+\varepsilon^2\left(\frac{u^2}{18}+\frac{u^4}{30}\right)+o(\varepsilon^2).
\]
For any fixed \(b>0\) there is a unique positive solution with \(u^2\to(\sqrt{25+1080b}-5)/6\); division of \(z_k\) by \(\sqrt\varepsilon\) yields the announced crossover. At \(b=0\) the unique maximizer is exactly zero. This completes the proof.

## Verification

The standalone `verify.py` checks the matrix's Perron eigenvector, the derivative identity, the general fourth-order response expansion, the sixth-order matched free-energy expansion, explicit Markov stationarity, the coexistence equations, and numerical approach to both crossover regimes, using exact symbolic algebra where applicable and high-precision numerics otherwise. Run `python verify.py` after installing the packages in `requirements.txt`. These are **finite diagnostic checks**, not a replacement for the global monotonicity and asymptotic arguments above. The checker and its dependency specification accompany this statement.

## Relationship to prior work

Tang, Yang, and Li [1], Proposition 7.9, prove the \(k=3\) unweighted case and its fourth-root transition. Their Section 6 develops the one-dimensional Legendre and Taylor machinery, and Section 8 explicitly identifies joint cubic--quintic crossover as a direction for further work. The present theorem introduces a geometrically natural transition-edge weight, determines the entire two-parameter global phase diagram including the **discontinuous side**, and computes the precise coexistence, spinodal, and jump constants. None of these claims follow numerically just from the \(k=3\) calculation.

Buzzi, Kloeckner, and Leplaideur [2] establish a general nonlinear formalism and exhibit other metastable Curie--Weiss models. Ostilli and Mukhamedov [3] analyze three-state Potts models with different nearest-neighbor and mean-field interactions. These works supply context and related mechanisms but not the stated forbidden-edge correlation model or its exact joint scaling. General Landau tricritical theory predicts the qualitative sixth-order competition; the model-specific global uniqueness and numerical constants require the exact spectral response.

## Limitations

The result covers only positive transition-edge weights and the indicated quadratic **edge-correlation** energy. It does not claim a universal first-order diagram for every three-state model, a theorem for arbitrary perturbations of an analytic pressure, finite-size fluctuation scaling, or kinetics of metastable escape. The crossover laws concern \(k\to3\) with their explicitly specified simultaneous temperature scalings. The literature comparison reduces, but does not eliminate, the possibility of an equivalent calculation in older statistical-mechanics treatments of spin-one or hard-core mean-field models. Independent validation has not been performed.

## References

[1] D. Tang, R. Yang, and Z. Li, *Nonlinear thermodynamic formalism for correspondences*, arXiv:2609.25915v1 (first public version September 22, 2026), especially Sections 6.4--6.5, 7.1, 7.6, and 8. https://arxiv.org/pdf/2609.25915

[2] J. Buzzi, B. Kloeckner, and R. Leplaideur, *Nonlinear thermodynamical formalism*, Annales Henri Lebesgue 6 (2023), DOI:10.5802/ahl.192, especially Sections 1.6 and 4.2--4.3. https://ahl.centre-mersenne.org/item/10.5802/ahl.192.pdf

[3] M. Ostilli and F. Mukhamedov, *1D Three-state mean-field Potts model with first- and second-order phase transitions*, arXiv:1205.6777 (2012), Sections 2--4 and Conclusions. https://arxiv.org/pdf/1205.6777
