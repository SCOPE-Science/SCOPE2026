# A sharp optimizer-exclusion frontier for random reshuffling despite smaller mean-square error

## Finding
For the simple two-component strongly convex finite-sum objective, constant-step **random reshuffling (RR)** can uniformly improve expected squared error over independent-with-replacement stochastic gradient descent (SGD) while **never returning to an entire neighborhood of the exact minimizer at any noninitial epoch endpoint**. The exclusion begins at the sharp step-size threshold
\[
\eta_c=1-1/\sqrt2.
\]
For every \(\eta_c<\eta\le 1/2\), the RR epoch law has a nonempty open hole around zero, but the independent-sampling SGD invariant law has full interval support and assigns positive probability to every neighborhood of zero. At the natural half-step, the finite-epoch RR and SGD laws have total-variation distance exactly \(1-2^{-m}\) after \(m\) epochs, despite an exact mean-square ratio of \(1/5\). Their respective invariant laws are mutually singular. These are endpoint distributional distinctions, not failures of objective-rate guarantees.

## Assumptions and scope
Let \(f_\pm:\mathbb R\to\mathbb R\) be
\[
f_\pm(x)=\tfrac12(x\mp1)^2,\qquad F(x)=\tfrac12(f_+(x)+f_-(x))=\tfrac12(x^2+1).
\]
The unique minimizer of \(F\) is zero, its second derivative is one, and each component has second derivative one. Initialize both methods at \(X_0=0\), fix \(0<\eta<1\), and write \(r=1-\eta\), \(q=r^2\). A component-gradient update with sampled sign \(s\in\{-1,+1\}\) is \(T_s(x)=rx+\eta s\). In SGD, each sign is a new independent fair sign. In RR, at each epoch, independently choose one of the two equiprobable sign orders \((+1,-1)\) and \((-1,+1)\), then use both updates. Compare only the epoch-end states \(X_{2m}\), after the same \(2m\) component-gradient evaluations. All probability and expectation statements refer to these specified sampling schemes. Invariant laws refer to the epoch Markov chain for RR and the one-step Markov chain for SGD. The two mechanisms are not coupled in any particular joint probability space.

## Proof
**1. Exact epoch recursions and risk.** An RR epoch composes two component steps in either order:
\[
T_{-}\circ T_{+}(x)=q x-\eta^2,\qquad T_{+}\circ T_{-}(x)=q x+\eta^2.
\]
Thus, reversing the independent epoch signs if necessary, for each integer \(m\ge1\),
\[
X_{2m}^{\mathrm{RR}}\ \overset{d}=\ \eta^2\sum_{j=0}^{m-1}q^j\varepsilon_j,\quad
X_{2m}^{\mathrm{SGD}}\ \overset{d}=\ \eta\sum_{j=0}^{2m-1}r^j\xi_j,
\]
where all displayed signs in each sum are independent and symmetric. Taking second moments (all cross terms vanish),
\[
\begin{aligned}
\mathbb E[(X_{2m}^{\mathrm{RR}})^2]&=\eta^4\frac{1-q^{2m}}{1-q^2},\\
\mathbb E[(X_{2m}^{\mathrm{SGD}})^2]&=\eta^2\frac{1-r^{4m}}{1-r^2},\\
\frac{\mathbb E[(X_{2m}^{\mathrm{RR}})^2]}{\mathbb E[(X_{2m}^{\mathrm{SGD}})^2]}&=\frac{\eta^2}{1+r^2}<1.
\end{aligned}
\]
The strict inequality follows from \(0<\eta<1\). Since \(F(x)-F(0)=x^2/2\), this is also the all-epoch excess-objective ratio.

**2. Sharp RR exclusion frontier.** The epoch maps \(R_\pm(x)=qx\pm\eta^2\) are strict contractions. Consequently the unique invariant probability is the infinite symmetric-sign series
\[
Z_{\mathrm{RR}}=\eta^2\sum_{j=0}^{\infty}q^j\varepsilon_j,
\]
with compact support equal to the unique nonempty compact attractor \(K=R_+(K)\cup R_-(K)\). Set \(b=\eta^2/(1-q)\). The convex hull of \(K\) is \([-b,b]\), and its two first-level images are
\[
R_-([-b,b])=[-b,-g],\quad R_+([-b,b])=[g,b],\quad
g=\frac{\eta^2(1-2q)}{1-q}.
\]
When \(q\ge1/2\), these two intervals overlap or meet and their union is exactly \([-b,b]\); uniqueness of the compact attractor implies \(K=[-b,b]\). When \(q<1/2\), the images are disjoint with an open gap \((-g,g)\); iteration yields a strongly separated two-branch Cantor set, hence
\[
\dim_H K=\frac{\log2}{-\log q}.
\]
For completeness, the dimension follows by the upper cover of \(2^n\) level-\(n\) cylinders of diameter \(2bq^n\) and the lower mass-distribution bound: disjoint cylinders of the same depth are separated on the order of \(q^n\), while the fair-sign measure assigns each exactly \(2^{-n}\). The open-gap condition is equivalent to \((1-\eta)^2<1/2\), that is \(\eta>1-1/\sqrt2\). Moreover, in this regime the dominant most-recent sign exceeds the sum of all other possible signed terms, giving, for each \(m\ge1\),
\[
|X_{2m}^{\mathrm{RR}}|\ \ge\ \eta^2\left(1-\sum_{j=1}^{m-1}q^j\right)
=g+\frac{\eta^2q^m}{1-q}>g.
\]
The empty gap is therefore not merely an invariant-law statement: it is never entered by noninitial epoch endpoints from the specified initialization. At or below the threshold, the invariant support is an interval containing zero, so the claimed invariant-support exclusion is impossible. This proves sharpness.

**3. SGD fills that same neighborhood.** The unique SGD invariant law is
\[
Z_{\mathrm{SGD}}=\eta\sum_{j=0}^{\infty}r^j\xi_j.
\]
Its support is the attractor of \(S_\pm(x)=rx\pm\eta\). Its convex hull is \([-1,1]\). The two images of this interval are \([-1,2r-1]\) and \([1-2r,1]\), which cover the full interval exactly when \(r\ge1/2\), equivalently \(\eta\le1/2\). Thus in the nonempty intersection \(1-1/\sqrt2<\eta\le1/2\), the RR invariant law excludes a positive-radius neighborhood of the minimizer, while the SGD invariant law has full support and therefore positive probability in every open neighborhood of zero. The latter conclusion is about support; no uniform density is claimed for general \(\eta\).

**4. Exact finite-horizon statistical separation at \(\eta=1/2\).** Here \(r=1/2\), \(q=1/4\), and
\[
Z_{\mathrm{RR}}=\tfrac14\sum_{j\ge0}4^{-j}\varepsilon_j,\qquad
Z_{\mathrm{SGD}}=\tfrac12\sum_{j\ge0}2^{-j}\xi_j.
\]
The second law is uniform on \([-1,1]\), by the fair binary expansion of a uniform \([0,1]\) random variable. The first is non-atomic with Cantor support, Hausdorff dimension \(\log2/\log4=1/2\), and a gap \((-1/6,1/6)\). It is therefore singular relative to Lebesgue measure and to the SGD stationary law, so the stationary total-variation distance is one.

At the finite time \(2m\), independent-sampling SGD puts mass \(2^{-2m}\) on each of \(2^{2m}\) distinct dyadic grid states. RR restricts the sign strings to those in which each consecutive pair contains one plus and one minus. There are exactly \(2^m\) such strings; their states are distinct by injectivity of the fixed-length base-two expansion. The RR distribution is precisely the SGD distribution conditioned on this subset and gives each of its states mass \(2^{-m}\). Consequently
\[
\left\|\mathcal L(X_{2m}^{\mathrm{RR}})-\mathcal L(X_{2m}^{\mathrm{SGD}})\right\|_{\mathrm{TV}}=1-2^{-m}.
\]
The one-fifth mean-square ratio follows from Step 1. For \(m=2\), RR is uniform on \(\{-5/16,-3/16,3/16,5/16\}\), whereas SGD is uniform on the sixteen odd-sixteenth grid sites between \(-15/16\) and \(15/16\). Thus \(\mathbb P_{\mathrm{RR}}(|X_4|<1/8)=0\), \(\mathbb P_{\mathrm{SGD}}(|X_4|<1/8)=1/8\), and their corresponding squared errors are \(17/256\) and \(85/256\). Finally, standard contraction couplings show weak convergence to each unique invariant law; no total-variation convergence of an individual discrete finite-time law to a nonatomic limit is asserted.

## Verification
The standalone `rr_support_check.py` evaluates the exact rational update laws for five step sizes and epochs one through six, independently compares the resulting second moments with both formulas, checks the RR finite gap in the separated regime, and checks the precise half-step TV identity for epochs one through seven. It also reproduces the four-gradient small-ball comparison. All checks passed when executed from the extracted package. These finite computations corroborate, but do not replace, the infinite-series, compact-attractor, or Hausdorff-dimension arguments above.

## Relationship to prior work
Z. Liu (2026) proves broad RR expected **averaged-iterate rate** guarantees; the formal theorem uses step sizes at most \(1/(6\widehat L)\). The support-exclusion steps here exceed \(1-1/\sqrt2\), so no conflict or extension of that averaged theorem is claimed. Ying, Yuan, Vlaski, and Sayed (2018) give quadratic RR steady-state **mean-square** formulas and explain periodic behavior. Those results motivate, and can already support parts of, the squared-error comparison; variance control alone does not specify the support hole or exact TV separation. The IFS/Bernoulli-convolution support-dimension facts are classical and are not claimed to be new by themselves. The contribution is the sharp alignment of that support transition with the RR-versus-SGD sampling comparison and the exactly quantified all-epoch distributional separation on the same optimization problem.

## Limitations
This is an exact two-component one-dimensional equal-curvature quadratic, with independent fresh permutations, fixed step size, and initial state zero. Its no-return conclusion concerns epoch endpoints, not the interior iterate within an epoch. The steady-state support classification extends to arbitrary initial states through weak convergence, but the uniform finite-time exclusion bound is stated only for zero initialization. No conclusions are made about decaying steps, minibatches, different curvatures, more than two components, averaging, or practical training losses. Classic Bernoulli convolutions and specialized stochastic-gradient literature may contain equivalent presentations; independent priority review is still needed. The exceptional step \(\eta=1/2\) is used only for the explicit uniform law and exact finite-time TV calculation; the strict optimizer-gap interval is open in step size.

## References
1. Zijian Liu, *Random Reshuffling Dominates Stochastic Gradient Descent*, arXiv:2606.32005v1 (first public June 30, 2026), https://arxiv.org/html/2606.32005v1.
2. B. Ying, K. Yuan, V. Vlaski, and A. H. Sayed, *Stochastic Learning under Random Reshuffling with Constant Step-sizes*, arXiv:1803.07964v2, https://arxiv.org/html/1803.07964v2.
3. *High Probability Guarantees for Random Reshuffling*, arXiv:2311.11841v4, https://arxiv.org/html/2311.11841v4.
