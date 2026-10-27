# Brownian top-rank local time for fixed-type complete-feedback card guessing

## Finding
Fix an integer \(n\ge 2\). Shuffle uniformly a deck containing \(m\) cards of each of \(n\) types; reveal and remove one card per round. Before each reveal, guess a type with largest remaining count, breaking ties by any predictable rule that does not observe the next card. Let \(T_{n,m}\) be the number of correct guesses. For \(n\) independent standard Brownian bridges \(B_1,\ldots,B_n\) on \([0,1]\), set
\[
Z_i(u)=B_i(u)-\frac1n\sum_{j=1}^nB_j(u),\qquad
G(u)=Z_{(1)}(u)-Z_{(2)}(u),
\]
where subscripts \((1),(2)\) indicate the two largest coordinates. Let \(L_1^{0,\mathrm{sym}}(G)\) denote **symmetric semimartingale local time**, normalized by
\[
L_1^{0,\mathrm{sym}}(G)
=\lim_{\varepsilon\downarrow0}\frac1{2\varepsilon}
\int_0^1\mathbf1_{\{0\le G(u)<\varepsilon\}}\,d\langle G\rangle_u,
\]
in probability. Then, as \(m\to\infty\) with \(n\) fixed,
\[
\boxed{\quad \frac{T_{n,m}-m}{\sqrt m}
\ \Longrightarrow\ \frac12 L_1^{0,\mathrm{sym}}(G).\quad}
\]
This supplies a fixed-number-of-types score limit, including \(n\ge3\), for which Dey–Manthripragada (2026) explicitly identify the limit as open. The limit is nonnegative. For \(n=2\) it reduces to the established Rayleigh law with cumulative distribution \(1-e^{-x^2}\), \(x\ge0\). The limiting mean (of the compensator, and also of the score under uniform integrability) is \(\frac\pi2\mathbb E[\max_{1\le i\le n}N_i]\), for independent standard normal \(N_i\); in particular it equals \(3\sqrt\pi/4\) for \(n=3\).

## Assumptions and scope
The deck contains exactly \(nm\) cards, \(m\) of each type; \(n\) is any fixed integer at least \(2\), and \(m\) runs through positive integers. The shuffle is uniform over distinct multiset orderings. The guess is chosen before and without knowledge of the next card, from the currently most numerous types; tie-breaking can depend on the past. The Brownian bridges have covariance \(\mathbb E B_i(u)B_i(v)=\min(u,v)-uv\) and are independent prior to centering. The time variable \(u\) is the fraction of the deck already revealed. The occupation-density definition above fixes the factor in the local-time formula; it is the symmetric, not right-sided, local time of a nonnegative semimartingale.

For integers \(0\le k\le nm\), denote remaining counts by \(C_i(k)\), let \(W_k=\max_i C_i(k)\), and let \(I_k\) denote the predictable choice of a maximizer. Put \(t_k=nm-k\), and define the centered path \(Z_i^{(m)}(k/(nm))=(C_i(k)-t_k/n)/\sqrt m\), with linear interpolation. The Gaussian limit \(Z\) has covariance \(\mathbb E Z_i(u)Z_j(v)=(\delta_{ij}-1/n)(\min(u,v)-uv)\).

## Proof
**1. Exact discrete rank-regulator identity.** Let \(\xi_{k+1}\) be the type of the next revealed card, and \(A_k=\mathbf1_{\{\xi_{k+1}=I_k\}}\). The maximum remaining count decreases by one precisely when a card of the *unique* maximum type is removed; otherwise it stays constant. Hence \(W_k-W_{k+1}\in\{0,1\}\), and the telescoping identity \(W_0-W_{nm}=m\) gives
\[
T_{n,m}-m=\sum_{k=0}^{nm-1}\bigl[A_k-(W_k-W_{k+1})\bigr]
=\sum_{k=0}^{nm-1}\mathbf1_{\{A_k=1,\;\#\arg\max_i C_i(k)\ge2\}}.
\]
Equivalently, since a common centering cancels,
\[
\frac{T_{n,m}-m}{\sqrt m}
=\sum_{k=0}^{nm-1}\left[\Delta Z_{(1)}^{(m)}(k)
-\Delta Z_{I_k}^{(m)}(k)\right],
\]
where \(\Delta\) denotes the subsequent minus preceding value. This exactly identifies the excess score as a discrete convexity regulator at top-rank collisions; no probabilistic approximation has yet been made.

**2. Joint bridge/martingale limit.** Given the past, \(\mathbb P(\xi_{k+1}=i\mid\mathcal F_k)=C_i(k)/t_k\). Set
\[
M_i^{(m)}(u)=\frac1{\sqrt m}\sum_{k<unm}
\left(\mathbf1_{\{\xi_{k+1}=i\}}-\frac{C_i(k)}{t_k}\right).
\]
The exact count recursion reads
\[
\Delta Z_i^{(m)}(k)=-\Delta M_i^{(m)}(k)
-\frac{Z_i^{(m)}(k/(nm))}{t_k}.
\]
On each \([0,1-\eta]\), \(\eta>0\), multivariate hypergeometric tightness and martingale quadratic-variation convergence give
\[
(Z^{(m)},M^{(m)})\Longrightarrow(Z,M),\qquad
 dZ_i(u)=-\frac{Z_i(u)}{1-u}\,du-dM_i(u),
\]
where \(M\) is Brownian motion in the hyperplane of centered vectors with \(d\langle M_i,M_j\rangle_u=(\delta_{ij}-1/n)\,du\). The limit \(Z\) is a centered vector of Brownian bridges (the sign of the driving Brownian motion is immaterial). To see the predictable quadratic-variation limit, use the hypergeometric law of large numbers \(C_i(k)/t_k\to1/n\) uniformly on each compact subinterval of \([0,1)\); the jump sizes are at most \(m^{-1/2}\), giving Lindeberg automatically. The limiting linear stochastic equation has a unique solution.

**3. Continuous score decomposition, including the endpoint.** Let \(S_{n,m}=\sum_{k=0}^{nm-1}W_k/t_k\) be the predictable compensator. The identity \(W_k=t_k/n+\sqrt m\, Z_{(1)}^{(m)}(k/(nm))\) gives
\[
\frac{S_{n,m}-m}{\sqrt m}
=\sum_{k=0}^{nm-1}\frac{Z_{(1)}^{(m)}(k/(nm))}{t_k}
\Longrightarrow \int_0^1\frac{Z_{(1)}(u)}{1-u}\,du.
\]
The improper integral exists in \(L^1\), because the hypergeometric variance bound gives \(\mathbb E\max_i|Z_i^{(m)}(u)|\le C_n\sqrt{1-u}\) and the expected contribution from \(u>1-\eta\) is at most \(C_n\sqrt\eta\), uniformly in \(m\). The contribution from \(u<\eta\) is likewise negligible.

The compensated score is the martingale \(T_{n,m}-S_{n,m}=\sqrt m\sum_k\Delta M_{I_k}^{(m)}(k)\). The joint convergence in step 2 and the stochastic-integral convergence theorem yield, jointly with the preceding display,
\[
\frac{T_{n,m}-S_{n,m}}{\sqrt m}
\Longrightarrow\int_0^1\sum_{i=1}^n\mathbf1_{\{I(u)=i\}}\,dM_i(u),
\]
where \(I(u)\) is the almost-everywhere unique maximizer of \(Z(u)\). For the selector discontinuity, first replace each indicator on \([\eta,1-\eta]\) by smooth softmax weights; apply the joint martingale invariance principle to these continuous integrands; then remove smoothing using the Itô isometry and the fact that the time spent within \(\varepsilon\) of a top-coordinate tie tends to zero as \(\varepsilon\downarrow0\). The latter follows by integrating the bounded-time Gaussian tie-probabilities at each \(u\in(0,1)\). Both endpoint stochastic-integral tails have \(L^2\) norm at most \(C_n\sqrt\eta\), uniformly in \(m\). Thus arbitrary predictable choices on exact ties give the same limit.

**4. Brownian rank local time.** A nondegenerate two-dimensional Brownian-bridge difference avoids its origin on \((0,1)\) almost surely, so three or more coordinates do not coincide at a top rank at positive interior times. The standard ranked-semimartingale Tanaka formula therefore reads
\[
 dZ_{(1)}(u)=\sum_i\mathbf1_{\{I(u)=i\}}dZ_i(u)
+\frac12\,dL_u^{0,\mathrm{sym}}(G).
\]
Substitute the stochastic equation from step 2 and integrate. Since \(Z_{(1)}(0)=Z_{(1)}(1)=0\) almost surely,
\[
\int_0^1\frac{Z_{(1)}(u)}{1-u}\,du
+\int_0^1\sum_i\mathbf1_{\{I(u)=i\}}dM_i(u)
=\frac12L_1^{0,\mathrm{sym}}(G).
\]
The finite limit exists because the drift integral is \(L^1\) and the martingale integral is \(L^2\). Combining steps 3 and 4 proves the distributional claim.

**5. Normalization and mean checks.** For \(n=2\), \(G=|B_1-B_2|\), and the symmetric local time of this reflected bridge equals the symmetric local time of its signed difference. Since \(B_1-B_2\) is \(\sqrt2\) times a standard Brownian bridge, the limit is \(\frac1{\sqrt2}L_1^0(B)\), whose Rayleigh CDF is \(1-e^{-x^2}\). For general fixed \(n\), \(\mathbb E Z_{(1)}(u)=\sqrt{u(1-u)}\,\mathbb E\max_iN_i\); hence the compensator-limit mean is \(\frac\pi2\mathbb E\max_iN_i\). The hypergeometric endpoint estimates and dominated convergence give convergence of the scaled score means through their exact equality with the compensator means. Since the scaled scores are nonnegative and converge in law to a variable whose expectation agrees by the rank-Tanaka identity, uniform integrability follows as a consequence of convergence in distribution plus convergence of means.

## Verification
Run \(\texttt{python verify.py}\) with the Python standard library. Exhaustive enumeration of \(4362\) distinct finite multiset decks, at parameter pairs \((n,m)=(2,1),(2,4),(3,2),(3,3),(4,2)\), verifies the pathwise rank-collision identity and exact equality of expected score and compensator. Seeded numerical simulations at \(m=400\) for \(n=2,3\) provide low-power consistency checks against the predicted means. Neither enumeration nor simulation proves convergence; the limiting assertion uses steps 2–4.

## Relationship to prior work
Dey and Manthripragada, *Limit Theorems for the Complete Feedback Card Guessing Game* (arXiv:2610.17479v1, first public 2026-10-12), Proposition 1.4 and Section 5, obtain the fixed-type compensator's Brownian-bridge integral limit. Their introduction expressly leaves the limiting law of the **actual score** open for fixed \(n\ge3\). In contrast the present result retains the compensator's martingale remainder at the same scale and identifies the sum through top-rank collision local time. Kuba and Panholzer, *On Card guessing with two types of cards* (arXiv:2303.04609v1, 2023), establish the two-type special case; the \(n=2\) specialization here agrees with their Rayleigh limit. General semimartingale rank decompositions, such as Ghomrasni–Menoukeu Pamen (arXiv:0807.5001), supply a standard local-time identity but do not themselves provide the model-specific stochastic-process convergence of the score. Searches of related literature and mathematical research records identified no direct fixed-\(n\ge3\) score-law statement. This is a qualified originality assessment, not proof of exhaustive priority.

## Limitations
The number of types is fixed; this theorem neither gives a joint \(n,m\to\infty\) limit nor a closed-form CDF for \(n\ge3\). The convergence is weak; no numerical rate is claimed. The local-time functional is stated with symmetric occupation-density normalization, which is important for the factor \(1/2\). Stochastic-integral convergence relies on the standard bounded-jump martingale FCLT and stochastic-integral stability after smoothing the argmax selector. An independent audit has not been performed. Broader unpublished or non-indexed work on ranked bridge local times may overlap with the final distributional identity.

## References
1. P. S. Dey and J. M. Manthripragada, *Limit Theorems for the Complete Feedback Card Guessing Game*, arXiv:2610.17479v1 (2026), https://arxiv.org/html/2610.17479v1.
2. M. Kuba and A. Panholzer, *On Card guessing with two types of cards*, arXiv:2303.04609v1 (2023), https://arxiv.org/html/2303.04609v1.
3. R. Ghomrasni and O. Menoukeu Pamen, *Decomposition of order statistics of semimartingales using local times*, arXiv:0807.5001 (2008), https://arxiv.org/abs/0807.5001.
