# Optimal-alphabet multicritical transitions from Gaussian quadrature

## Finding

**Theorem (realization, global critical threshold, and minimal alphabet).** For every integer \(q\ge2\), let \(\gamma\) denote the standard normal probability measure, and let \(\mathrm{He}_q\) be its monic orthogonal Hermite polynomial of degree \(q\). Write its distinct real roots as \(x_1<\cdots<x_q\), and let \(w_i>0\) be the normalized \(q\)-point Gaussian quadrature weights, so that \(\sum_i w_i=1\) and
\[
\sum_{i=1}^{q}w_i x_i^j=\int_{\mathbb R}t^j\,d\gamma(t)\quad (0\le j\le 2q-1).
\]
On the one-sided full shift \(\Sigma_q=\{1,\ldots,q\}^{\mathbb N}\), let \(\sigma\) be the left shift, \(\phi(\omega)=\log w_{\omega_0}\), and \(\psi(\omega)=x_{\omega_0}\). For \(\beta\ge0\), set
\[
\Phi_q(\beta)=\sup_{\nu\in\mathcal M_\sigma(\Sigma_q)}\left[h_\nu(\sigma)+\int\phi\,d\nu+\frac{\beta}{2}\left(\int\psi\,d\nu\right)^2\right].
\]
Then the following hold.

1. For \(0\le\beta\le1\), the pressure satisfies \(\Phi_q(\beta)=0\), and its **unique** equilibrium measure is the Bernoulli measure of one-symbol weights \((w_1,\ldots,w_q)\). For every \(\beta>1\), the pressure is strictly positive and there are at least two equilibrium measures with opposite nonzero magnetizations.
2. There exists \(\varepsilon_q>0\) such that for \(1<\beta<1+\varepsilon_q\) there are **exactly two** equilibrium measures. They are Bernoulli laws with weights proportional to \(w_i e^{\pm y_q(\beta)x_i}\), where \(y_q(\beta)>0\) uniquely solves \(y=\beta P_q'(y)\) near zero and
\[
P_q(y):=\log\sum_{i=1}^{q}w_i e^{yx_i},\qquad
m_q(\beta)=P_q'(y_q(\beta))=\frac{y_q(\beta)}{\beta}.
\]
Writing \(C_q=((2q-1)!/q!)^{1/(2q-2)}\), the positive magnetization and pressure have the **sharp** asymptotics
\[
m_q(\beta)\sim C_q(\beta-1)^{1/(2q-2)},\qquad
\Phi_q(\beta)\sim\frac{(q-1)q!}{(2q)!}C_q^{2q}(\beta-1)^{q/(q-1)}
\quad(\beta\downarrow1).
\]
3. Among **symmetric probability measures of finite support** on \(\mathbb R\) with mean zero, variance one and all moments through degree \(2q-2\) identical to those of \(\gamma\), there are at least \(q\) support points. When there are exactly \(q\), the support is precisely the zero set of \(\mathrm{He}_q\) and the weights are the unique Gaussian quadrature weights. In particular the number of symbols in this moment-cancellation realization is optimal and the optimal symmetric law is rigid.

The first non-Gaussian term of the linear pressure is explicit:
\[
P_q(y)=\frac{y^2}{2}-\frac{q!}{(2q)!}y^{2q}+O(y^{2q+2}),
\qquad y\longrightarrow0.
\]
The first previously nonillustrated member \(q=4\) uses the four roots of \(\mathrm{He}_4(x)=x^4-6x^2+3\) and has exponent \(1/6\). The cases \(q=2\) and \(q=3\) recover, respectively, the classical square-root and tricritical fourth-root exponents in a weighted full-shift representation.

## Assumptions and scope

All alphabets are finite; \(q\) is an **arbitrary fixed integer** at least two. The shift is full and one-sided, logarithms are natural, and entropy is measure-theoretic Kolmogorov–Sinai entropy. The baseline potential \(\phi\) is **independent of** \(\beta\); the nonlinear term is quadratic in the single coordinate observable \(\psi\). Because the weights are positive, \(\phi\) is bounded and continuous. All equilibrium statements concern the supremum over **all invariant Borel probability measures**, not only Markov or Bernoulli candidates. 'Exactly two' above the transition is asserted only on a (possibly \(q\)-dependent) punctured right neighborhood, not for every \(\beta>1\).

The comparison/minimality class in part 3 is the class of symmetric positive probability laws with the specified Gaussian moments. For a symmetric variance-one single-site law, vanishing fourth through \((2q-2)\)-nd cumulants is equivalent to this moment agreement. No minimum claim is made for asymmetric models, multicomponent nonlinear energies, different mechanisms producing critical exponents, or nonlinearities of degree other than two.

## Proof

**1. Gaussian quadrature and strict exponential-moment inequality.** The probabilists' Hermite polynomial is the monic polynomial orthogonal to every polynomial of degree below \(q\) under \(\gamma\). Orthogonality to lower degrees gives exactly \(q\) simple real roots, symmetric about zero. The Lagrange cardinal polynomials \(\ell_i\) on these nodes have degree \(q-1\). Put \(w_i=\int\ell_i(t)\,d\gamma(t)\). Divide any polynomial of degree at most \(2q-1\) by \(\mathrm{He}_q\): the quotient has degree at most \(q-1\), so the orthogonality and cardinal identities prove exact quadrature. Applying it to \(\ell_i^2\) gives \(w_i=\int\ell_i(t)^2\,d\gamma(t)>0\). In particular \(\sum_iw_i=1\).

Fix any real \(y\ne0\). Let \(H_y\) be the unique polynomial of degree at most \(2q-1\) that matches both the values and first derivatives of \(f_y(t)=e^{yt}\) at all \(q\) nodes. The Hermite interpolation remainder has the pointwise form
\[
f_y(t)-H_y(t)=\frac{y^{2q}e^{y\xi_t}}{(2q)!}\prod_{i=1}^{q}(t-x_i)^2\ge0.
\]
For any \(t\) not a quadrature node the inequality is strict. Here \(\xi_t\) lies in the convex hull of \(t\) and the nodes; the general interpolation remainder applies equally outside the node interval. Since quadrature integrates \(H_y\) exactly and agrees with \(f_y\) at all nodes,
\[
\sum_iw_i e^{yx_i}=\int H_y\,d\gamma
<\int e^{yt}\,d\gamma=e^{y^2/2}
\qquad(y\ne0).
\]
Thus \(P_q(y)<y^2/2\) for **every** nonzero real field, not merely infinitesimally.

**2. First unmatched moment and pressure expansion.** Orthogonality and integration by parts give \(\int \mathrm{He}_q(t)^2\,d\gamma(t)=q!\). The monic polynomial \(t^{2q}-\mathrm{He}_q(t)^2\) has degree at most \(2q-1\); evaluating this polynomial by exact quadrature yields
\[
\int t^{2q}\,d\gamma(t)-\sum_iw_i x_i^{2q}=q!.
\]
Every lower moment is Gaussian. Symmetry makes every odd moment vanish. Comparing the moment generating functions with \(e^{y^2/2}\), then taking logarithms, proves the displayed expansion
\(P_q(y)=y^2/2-a_qy^{2q}+O(y^{2q+2})\), with \(a_q=q!/(2q)!>0\), and hence
\[
P_q'(y)=y-2qa_qy^{2q-1}+O(y^{2q+1}).
\]
In particular \(P_q''(0)=1\).

**3. Exact reduction over all invariant measures.** Let \(p=(p_i)\) be the first-coordinate marginal of an invariant measure. Its entropy rate obeys \(h_\nu(\sigma)\le-\sum_i p_i\log p_i\), with equality precisely for the Bernoulli measure with marginal \(p\). Hence the infinite-dimensional variational principle reduces exactly to the finite simplex problem
\[
\Phi_q(\beta)=\max_{p_i\ge0,\,\sum_i p_i=1}\left[-\sum_i p_i\log\frac{p_i}{w_i}+\frac{\beta}{2}\left(\sum_i p_ix_i\right)^2\right].
\]
For every \(\beta>0\), the elementary quadratic identity
\(\beta m^2/2=\sup_y\{ym-y^2/(2\beta)\}\) and the Gibbs variational formula over \(p\) yield
\[
\Phi_q(\beta)=\max_{y\in\mathbb R}\left[P_q(y)-\frac{y^2}{2\beta}\right]=:\max_y F_\beta(y).
\]
The maximizing marginal at any maximizing field \(y\) is unique and has weights \(p_i(y)=w_i e^{yx_i-P_q(y)}\). Conversely, any original equilibrium yields such a field. The one-dimensional maximum exists because \(P_q(y)\le |y|\max_i|x_i|\) and therefore \(F_\beta(y)\to-\infty\) as \(|y|\to\infty\).

**4. Sharp location of the transition.** For \(0<\beta\le1\), the strict inequality in Step 1 implies \(F_\beta(y)<0\) for \(y\ne0\), whereas \(F_\beta(0)=0\). The same unique Bernoulli law maximizes directly at \(\beta=0\), proving the entire subcritical and critical regime. For \(\beta>1\), \(F_\beta''(0)=1-1/\beta>0\), so \(F_\beta(y)>0\) at sufficiently small nonzero fields. Coercivity gives a nonzero global maximizer, and evenness produces its distinct negative counterpart.

**5. Two and only two branches near criticality.** At \(\beta=1\), \(F_1\) has a strict global maximum at zero, and is uniformly negative outside any chosen neighborhood of zero, using coercivity. Consequently all maximizers of \(F_\beta\) tend to zero as \(\beta\downarrow1\). By Step 2, for small positive \(y\),
\[
\frac{P_q'(y)}{y}=1-2qa_q y^{2q-2}+O(y^{2q})
\]
is strictly decreasing from one. The critical equation \(F_\beta'(y)=0\) is \(P_q'(y)/y=1/\beta\); for \(\beta>1\) sufficiently close to one, it therefore has **exactly one** positive solution among possible maximizers, plus its negative. The maximizing measures are the corresponding two tilted Bernoulli measures; no additional invariant maximizers exist by Step 3.

**6. Critical exponent and pressure constant.** Set \(\delta=\beta-1\) and let \(y_q(\beta)>0\) be the positive maximizing field. The critical equation and Step 2 give
\[
y_q(\beta)^{2q-2}\sim \frac{\delta}{2qa_q}=\frac{(2q-1)!}{q!}\,\delta.
\]
Since \(m_q(\beta)=y_q(\beta)/\beta\), this proves the magnetization constant. Substitution into
\(F_\beta(y)=(1-1/\beta)y^2/2-a_qy^{2q}+O(y^{2q+2})\) yields
\[
\Phi_q(\beta)\sim(q-1)a_q\,y_q(\beta)^{2q}\sim(q-1)a_q C_q^{2q}\delta^{q/(q-1)}.
\]
This gives the pressure constant and exponent, not just an order-of-magnitude estimate.

**7. Optimality and rigidity.** Let \(\rho\) be a symmetric probability measure supported on \(K\) distinct points \(s_1,\ldots,s_K\) with the same moments as \(\gamma\) through degree \(2q-2\). If \(K\le q-1\), the polynomial \(V(t)=\prod_{i=1}^{K}(t-s_i)^2\) has degree at most \(2q-2\) and integral zero under \(\rho\), but a strictly positive integral under the absolutely continuous \(\gamma\): contradiction. Thus \(K\ge q\). If \(K=q\), let \(v(t)=\prod_i(t-s_i)\), monic degree \(q\). Moment equality implies \(\int v(t)r(t)\,d\gamma(t)=0\) for every polynomial \(r\) of degree at most \(q-2\). Orthogonal-polynomial expansion therefore gives \(v=\mathrm{He}_q+c\mathrm{He}_{q-1}\). Symmetry of the support forces \(v(-t)=(-1)^qv(t)\), while the two Hermite terms have opposite parity, so \(c=0\). The support is the Hermite root set. Matching moments through degree \(q-1\) then uniquely determines the weights by invertibility of the Vandermonde matrix, giving precisely \((w_i)\). This establishes both the alphabet bound and the symmetric minimal-law classification.

## Verification

The verification script `verify.py` checks positive, normalized and reflected quadrature weights; equality of all moments through degree \(2q-1\); the precise \(q!\) degree-\(2q\) moment deficit; and strict sub-Gaussian exponential moments at several nonzero fields, for each \(2\le q\le9\). The command `python verify.py` passed 128 finite diagnostics with NumPy. This is **supporting finite evidence only**: Steps 1–7 prove the infinite family, global field inequality, phase classification and alphabet bound. The interpolation remainder, Gaussian norm identity and variational reduction are all stated at the general parameter \(q\), and no numerical sign check substitutes for them.

## Relationship to prior work

Tang–Yang–Li [1, Theorem 6.8] give a **conditional** Taylor-coefficient criterion for exponents in the correspondence version of nonlinear thermodynamic formalism and explicitly analyze a three-state forbidden-edge fourth-root example [1, Proposition 7.9]. The present theorem provides, for every \(q\), a positive minimal-alphabet *full-shift* realization with explicit non-Gaussian cumulant, a global comparison excluding earlier phase transitions, a sharp pressure coefficient, and rigidity among minimal symmetric moment-matching spin laws. The general conditional Taylor criterion does not construct these quadrature potentials or imply the lower bound on the number of states.

Buzzi–Kloeckner–Leplaideur [2] establish nonlinear thermodynamic variational principles and examine classical and asymmetric Curie–Weiss and Potts examples, not the general Hermite-node family or its support minimality. Bru–de Siqueira Pedra–Lopes [3] provide broad convex-duality linearization; the scalar reduction in Step 3 is a special elementary case of that paradigm, **not** presented as a new duality theorem. The fourth-root member \(q=3\) is related to standard tricritical spin-one behavior; the result's specific contribution is the uniform construction for **all** higher orders together with the sharp support and uniqueness statements.

## Limitations

The exact count of equilibria above criticality is proved **only for** \(1<\beta<1+\varepsilon_q\); for arbitrary \(\beta>1\) only existence of a nonzero symmetric pair is claimed. The baseline one-site weights are deliberately tuned (the problem is not the uniformly weighted full shift); the support may vary with \(q\). The optimality/uniqueness theorem is restricted to symmetric variance-one atomic laws satisfying Gaussian moment cancellation, and does not rule out different mechanisms on fewer symbols. The elementary Gaussian quadrature and mean-field duality ingredients are classical; no claim of originality is made for those individual tools or for the standard two- and three-spin critical cases. No central-limit theorem, finite-size scaling law, universality under perturbations, or independent validation is asserted.

## References

[1] Dingxuan Tang, Rui Yang and Zhiming Li, *Nonlinear Thermodynamic Formalism for Correspondences*, arXiv:2609.25915v1, first posted 2026-09-22, Sections 6.4 and 7.6, https://arxiv.org/html/2609.25915 .

[2] Jérôme Buzzi, Benoît Kloeckner and Renaud Leplaideur, *Nonlinear thermodynamical formalism*, arXiv:2002.00576, especially Sections 1.4 and 5, https://arxiv.org/html/2002.00576 .

[3] Jean-Bernard Bru, Walter de Siqueira Pedra and Artur Oscar Lopes, *Abstract Theory of Bogoliubov Linearizations with Application to Nonlinear Thermodynamic Formalism*, arXiv:2605.23576, especially Sections 2.6–2.7, https://arxiv.org/html/2605.23576 .

[4] Renaud Leplaideur and Frédérique Watbled, *Curie–Weiss Type Models for General Spin Spaces and Quadratic Pressure in Ergodic Theory*, Journal of Statistical Physics 181 (2020), 263–292, doi:10.1007/s10955-020-02579-z (abstract/publisher preview accessible; complete text not assessed).
