# Sharp third-moment transition for Gaussian self-generated memory and its algebraic-tail onset laws

## Finding

A Gaussian spatial imprint with a nonnegative hereditary age kernel has a sharp *third-age-moment threshold* separating the usual square-root onset of complete uniform translations from a strictly smaller onset. In the natural normalized polynomial-tail family, this threshold occurs at tail exponent \(p=4\). Every \(p\in(2,4)\) gives an explicitly determined fractional-power speed law, \(p=4\) gives a logarithmically suppressed square root, and \(p>4\) gives a square root with an explicit coefficient.

Specifically, suppose the age weight \(w\) has first moment \(\int_0^\infty s w(s)\,ds=1\), and put \(M_3=\int_0^\infty s^3w(s)\,ds\in(0,\infty]\). With ordinary velocity-memory mass \(0\le\rho<1\), define \(\kappa_c=1-\rho\). There is exactly one positive complete translating speed \(r(\kappa)\) for each \(\kappa>\kappa_c\), and none at or below threshold. In the extended-real convention \(1/\infty=0\),

\[
\lim_{\kappa\downarrow\kappa_c}\frac{r(\kappa)^2}{\kappa-\kappa_c}=\frac{2}{\kappa_c M_3}.
\]

Consequently, a finite positive square-root coefficient exists **if and only if** the third age moment is finite. If that moment is infinite, the onset speed is \(o(\sqrt{\kappa-\kappa_c})\).

For the normalized polynomial age weights

\[
 w_p(s)=(p-1)(p-2)(1+s)^{-p},\qquad p>2,
\]

the sharper formulas, with \(\delta=\kappa-\kappa_c\downarrow0\), are

\[
 r(\kappa)\sim
 \begin{cases}
 \left(\dfrac{\delta}{\kappa_c C_p}\right)^{1/(p-2)},&2<p<4,\\[7pt]
 \sqrt{\dfrac{2\delta}{3\kappa_c\log(1/\delta)}},&p=4,\\[8pt]
 \sqrt{\dfrac{(p-3)(p-4)\delta}{3\kappa_c}},&p>4,
 \end{cases}
\qquad
 C_p=(p-1)2^{1-p/2}\Gamma\left(2-\frac p2\right).
\]

Here \(\sim\) means that the ratio of the two positive quantities tends to one. At fixed \(\kappa>\kappa_c\), the translating directions form exactly the sphere of radius \(r(\kappa)\) in the ambient Euclidean space; this is a statement about **complete uniform translations only**, not about their stability or the absence of other dynamical behaviors.

## Assumptions and scope

Fix an integer \(d\ge1\). Let \(x:\mathbb R\to\mathbb R^d\) be continuously differentiable, and consider the full-history geometric-memory equation

\[
 \dot x(t)=\int_0^\infty m(s)\dot x(t-s)\,ds
 -\kappa\int_0^\infty w(s)\nabla\Phi(x(t)-x(t-s))\,ds,
\qquad
 \Phi(z)=e^{-\lVert z\rVert^2/2}.
\]

Assume \(m,w\ge0\) are measurable and integrable on \((0,\infty)\), \(\int_0^\infty m(s)\,ds=\rho\in[0,1)\), \(w\not\equiv0\), and \(\int_0^\infty sw(s)\,ds=1\). These hypotheses ensure that the hereditary force is well defined on every constant bounded velocity history. A concrete choice is \(m(s)=\rho e^{-s}\); it is the one used for the polynomial-tail corollary. All quantities and limits are real; \(\kappa>0\). The large-time tail of \(w\) is relevant to branch onset, whereas the detailed shape of \(m\) is immaterial for this complete-translation calculation once \(\rho\) is fixed.

The integral \(M_3\) can be infinite; no finite higher age moment is assumed. Stationary paths with \(\dot x\equiv0\) always solve the equation. A complete uniform translation is a path \(x(t)=x_0+vt\) for every real \(t\), whose velocity \(v\) is constant; its position is not required to be bounded.

## Proof

**1. Exact reduction and uniqueness.** For a constant velocity \(v\), the displacement \(x(t)-x(t-s)\) equals \(sv\). Since \(-\nabla\Phi(z)=ze^{-\lVert z\rVert^2/2}\), direct substitution gives

\[
 v=\rho v+\kappa vF(\lVert v\rVert),\qquad
 F(r)=\int_0^\infty sw(s)e^{-r^2s^2/2}\,ds.
\]

The integrals converge because \(\int sw=1\). This is the translating-speed identity of Vrabel's Theorem 13, specialized to the Gaussian imprint. For \(v\ne0\), it is equivalent to \(\kappa F(\lVert v\rVert)=\kappa_c\). Dominated convergence gives continuity of \(F\) and \(F(0)=1\). For \(0\le r_1<r_2\), the Gaussian factor decreases strictly for every \(s>0\); since \(sw(s)\) has positive mass, \(F(r_2)<F(r_1)\). Dominated convergence also gives \(F(r)\to0\) as \(r\to\infty\). Thus there is exactly one \(r>0\) for \(\kappa>\kappa_c\), and none for \(\kappa\le\kappa_c\). The radial response implies that all and only velocity vectors with that magnitude give nonzero uniform translations.

**2. A sharp moment criterion without tail regularity.** Set

\[
 \Delta(r)=1-F(r)=\int_0^\infty sw(s)\bigl(1-e^{-r^2s^2/2}\bigr)\,ds.
\]

For each fixed \(s>0\),

\[
 \frac{1-e^{-r^2s^2/2}}{r^2}\longrightarrow\frac{s^2}{2}
 \quad\text{as }r\downarrow0.
\]

Moreover, the displayed quotient increases as \(r\downarrow0\), since \((1-e^{-y})/y\) decreases on \((0,\infty)\). Monotone convergence therefore proves the **extended-real limit**

\[
 \lim_{r\downarrow0}\frac{\Delta(r)}{r^2}=\frac{M_3}{2}\in(0,\infty].
\]

Writing \(\delta=\kappa-\kappa_c\) and using the exact branch equation gives \(\Delta(r(\kappa))=\delta/(\kappa_c+\delta)\). Since \(r(\kappa)\downarrow0\),

\[
 \frac{r(\kappa)^2}{\delta}
 =\frac1{\kappa_c+\delta}\frac{r(\kappa)^2}{\Delta(r(\kappa))}
 \longrightarrow\frac{2}{\kappa_c M_3},
\]

with the stated infinite-moment convention. The equivalence between finite third moment and a nonzero square-root coefficient follows because \(M_3>0\).

**3. Normalization and explicit response for algebraic memory.** For \(p>2\), the beta integral yields

\[
 \int_0^\infty s(1+s)^{-p}\,ds
 =\frac{1}{(p-1)(p-2)}.
\]

Hence \(w_p\) has first age moment one. Let \(B_p=(p-1)(p-2)\). Its response deficit is

\[
 \Delta_p(r)=B_p\int_0^\infty s(1+s)^{-p}
       \bigl(1-e^{-r^2s^2/2}\bigr)\,ds.
\]

**4. Algebraic-tail regime \(2<p<4\).** Change variables \(u=rs\):

\[
 \frac{\Delta_p(r)}{r^{p-2}}
 =B_p\int_0^\infty\frac{u}{(u+r)^p}
       \bigl(1-e^{-u^2/2}\bigr)\,du.
\]

For every \(r>0\), the integrand is bounded by \(u^{1-p}(1-e^{-u^2/2})\). This majorant behaves as \(u^{3-p}/2\) at zero and as \(u^{1-p}\) at infinity; it is integrable exactly for \(2<p<4\). Dominated convergence shows

\[
 \Delta_p(r)\sim B_pr^{p-2}
       \int_0^\infty u^{1-p}(1-e^{-u^2/2})\,du.
\]

With \(t=u^2/2\), an integration by parts evaluates the remaining integral as

\[
 \int_0^\infty u^{1-p}(1-e^{-u^2/2})\,du
 =\frac{2^{1-p/2}}{p-2}\Gamma\left(2-\frac p2\right).
\]

The boundary terms vanish because \(2<p<4\). This yields \(\Delta_p(r)\sim C_pr^{p-2}\) with the positive constant in the statement. Substituting \(\Delta_p(r(\kappa))=\delta/(\kappa_c+\delta)\) gives the first speed law.

**5. Critical logarithmic regime \(p=4\).** Here \(B_4=6\). Split the deficit integral at \(s=1/r\). On \(s\le1/r\), the inequality \(\lvert1-e^{-y}-y\rvert\le y^2/2\) for \(y\ge0\) implies

\[
 \int_0^{1/r}\frac{s}{(1+s)^4}
  \bigl(1-e^{-r^2s^2/2}\bigr)\,ds
 =\frac{r^2}{2}\int_0^{1/r}\frac{s^3}{(1+s)^4}\,ds+O(r^2).
\]

The remainder is \(O(r^4\int_0^{1/r}s^5(1+s)^{-4}ds)=O(r^2)\). The portion \(s\ge1/r\) is bounded by \(\int_{1/r}^\infty s(1+s)^{-4}\,ds=O(r^2)\). Finally,

\[
 \int_0^{1/r}\frac{s^3}{(1+s)^4}\,ds
   =\log(1/r)+O(1),
\]

so \(\Delta_4(r)=3r^2\log(1/r)+O(r^2)\). Inverting the branch identity first gives \(\log(1/r(\kappa))\sim\tfrac12\log(1/\delta)\), then

\[
 r(\kappa)^2\sim\frac{2\delta}{3\kappa_c\log(1/\delta)}.
\]

**6. Finite-third-moment regime \(p>4\).** The beta integral also gives

\[
 M_3=B_p\int_0^\infty s^3(1+s)^{-p}\,ds
      =\frac{6}{(p-3)(p-4)}.
\]

Part 2 implies \(\Delta_p(r)\sim3r^2/((p-3)(p-4))\), and direct inversion supplies the third displayed speed law. All asymptotics concern \(\kappa\downarrow\kappa_c\) from above, with \(p\) fixed. This completes the proof.

## Verification

The companion `CHECK.py` performs transformed Simpson quadratures for four integer exponents, checks exact first-age-moment normalizations and selected small-speed coefficients, and records the finite-scale comparisons in `CHECK_OUTPUT.txt`. The executable is a finite diagnostic only: it does not prove uniqueness for all positive speeds, monotone-convergence statements, or asymptotic limits. Those follow from the argument above. Reproduce with `python3 CHECK.py` in the directory containing the two files.

## Relationship to prior work

Vrabel, *Geometric Stability of Dynamical Systems with Self-Generated State-Space Memory* (arXiv:2610.24152v1, 16 October 2026), introduces the full-history equation, its exact traveling-speed response, and a Taylor branch-orientation expansion under a finite fifth age moment; see especially Theorem 13, Theorem 15, and Proposition 16. The exact response equation and the threshold concept are **prior results** and are not claimed to be new here. The contribution is the necessary-and-sufficient **third age-moment criterion** and the three explicit onset laws for normalized algebraic temporal tails, including the non-quadratic and logarithmic regimes for which that finite-fifth-moment expansion is unavailable.

Sarkar, *The Memory Engine: Self-Organized Coherence from Internal Feedback* (arXiv:2505.21711v1), studies stochastic feedback with exponentially relaxing Gaussian spatial memories, and Lutier, van Wijland, and Fournier, *Self-Trapping of Microorganisms Steering Toward their Own Trail* (arXiv:2512.09597v1), studies orientational self-trapping by trails. These supply related physical and dynamical motivation but not the stated third-moment translating-speed cutoff for this hereditary operator. Standard gamma/beta and Laplace-tail calculations are mathematical tools, not novelty claims. Earlier general Tauberian theory may imply related scalar integral asymptotics; the claim is confined to the proved response and branch classification in this geometric-memory model.

## Limitations

The result classifies complete paths with exactly constant velocity, not arbitrary complete solutions, basins, or translating-state stability. It assumes a Gaussian radial imprint and fixed nonnegative age weights; the specific sharp coefficients for polynomial tails need not persist for other spatial profiles or differently normalized tails. A subnormal velocity-memory mass \(\rho<1\) is essential. No statement of globally attracting motion, robust stability under perturbation, or optimality among all memory models is made. Historical priority beyond the inspected sources remains subject to independent literature review.

## References

1. R. Vrabel, *Geometric Stability of Dynamical Systems with Self-Generated State-Space Memory*, arXiv:2610.24152v1 (2026), https://arxiv.org/html/2610.24152v1.
2. A. Sarkar, *The Memory Engine: Self-Organized Coherence from Internal Feedback*, arXiv:2505.21711v1 (2025), https://arxiv.org/html/2505.21711v1.
3. A. Lutier, F. van Wijland, and J.-B. Fournier, *Self-Trapping of Microorganisms Steering Toward their Own Trail*, arXiv:2512.09597v1 (2025), https://arxiv.org/html/2512.09597v1.
