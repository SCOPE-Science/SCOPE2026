# Random first-order neighbor-profile corrections at perfect preferential resetting

## Finding
For the impurity monkey walk defined below, the usual limiting empirical spatial profile at perfect off-origin relocation has *random first-order corrections* at the same logarithmic scale as its vanishing origin mass. For each nearest-neighbor direction \(j\),
\[
\boxed{\log(n+1)\left(\frac{N_{j,n}}{n+1}-\frac1{2d}\right)\longrightarrow\frac{R_{j,\infty}-1/(2d)}{1-\xi_0}\quad\text{almost surely}.}
\]
Here \(R_{j,\infty}\) is a finite, nondegenerate random variable defined as the almost-sure limit of the centered neighbor count divided by the origin-visit count. The random vector has zero coordinate sum, so its directional component is distinct from the deterministic missing-mass correction.

## Assumptions and scope
Fix an integer \(d\ge1\), \(\xi_0\in(0,1)\), and start at \(W_0=0\) in \(\mathbb Z^d\). At time \(n\), when \(W_n=0\), the next position is a uniformly selected position from times \(0,\ldots,n\) with probability \(\xi_0\), or a uniformly chosen nearest neighbor with probability \(a=1-\xi_0\). When \(W_n\ne0\), the next position is always a uniformly selected historical position. Let \(m=2d\), index the neighbors by \(j=1,\ldots,m\), put \(K=n+1\), \(J_n=\mathbf1_{\{W_n=0\}}\), and define \(C_n=\sum_{t=0}^nJ_t\), \(N_{j,n}=\sum_{t=0}^n\mathbf1_{\{W_t=e_j\}}\). Only the origin and these \(m\) neighbors can ever be visited. Define
\[
D_{j,n}=N_{j,n}-\frac{K-C_n}{m},\qquad R_{j,n}=\frac{D_{j,n}}{C_n}.
\]
All convergence statements are almost sure as integer \(n\to\infty\) at the exact off-origin relocation parameter one; no uniformity in parameters is claimed.

## Proof
**Origin-mass input (proved here).** Set \(f_n=C_n/K\) and \(b_n=1-aJ_n\). The exact conditional law is
\[
q_{0,n}:=\Pr(W_{n+1}=0\mid\mathcal F_n)=b_nf_n.
\]
Thus \(\mathbb E[f_{n+1}-f_n\mid\mathcal F_n]=-af_nJ_n/(K+1)\). The bounded nonnegative supermartingale \(f_n\) converges, and the centered part has square-summable increments. Consequently \(\sum_nf_nJ_n/(K+1)<\infty\) almost surely. A positive limiting fraction would imply, by summation by parts, \(\sum_nJ_n/(K+1)=\infty\), a contradiction. Therefore \(f_n\to0\) almost surely.

To control negative powers of \(C_n\), observe that \(\log C_{n+1}-\log C_n=J_{n+1}\log(1+1/C_n)\). Its conditional mean is at least \(\xi_0\log2/K\), while the conditional variance of its centered part is at most \(1/K\). Martingale convergence after division by \(\log(n+3)\), followed by Kronecker's lemma, gives \(C_n\ge K^\eta\) eventually almost surely for some deterministic \(\eta>0\). Now the conditional mean equals \(b_n/K+O(1/(KC_n))\) and its variance is at most \(1/(KC_n)\), which are summable error bounds. Therefore
\[
\log C_n=\sum_{k<n}\frac{1-aJ_k}{k+1}+O_\omega(1).
\]
Since \(f_n\to0\), summation by parts gives \(\sum_{k<n}J_k/(k+1)=o(\log n)\), and hence \(\log C_n/\log K\to1\). In particular \(C_n\ge K^{3/4}\) eventually almost surely. For \(Q_n=K/C_n\), direct conditioning on the two possible next origin indicators yields
\[
\mathbb E[Q_{n+1}-Q_n\mid\mathcal F_n]=\frac{aJ_n}{C_n}+r_n,\qquad 0\le r_n\le C_n^{-2},
\]
with centered conditional variance at most \(4K/C_n^3\). Both error series are almost surely summable. Since \(\sum_{k<n}J_k/C_k=H_{C_n}-J_n/C_n\), where \(H_l=\sum_{r=1}^l1/r\), the inverse origin fraction obeys \(Q_n-a\log C_n\to L\) for some finite random \(L\). Hence \(Q_n/\log K\to a\), or equivalently
\[
\frac{C_n\log K}{K}\longrightarrow\frac1a.
\tag{1}
\]
This origin input is reconstructed to make the directional result independent of any prior unverified record.

**Exact directional ratio drift.** Conditional on the full past, the probability of next visiting neighbor \(j\) is
\[
q_{j,n}=b_n\frac{N_{j,n}}K+\frac{aJ_n}{m}.
\]
It follows that \(\mathbb E[D_{j,n+1}-D_{j,n}\mid\mathcal F_n]=b_nD_{j,n}/K\). An origin arrival leaves \(D_{j,n}\) unchanged but increases \(C_n\) by one, whereas a neighbor arrival changes \(D_{j,n}\) by \(\mathbf1_{\{\text{neighbor }j\}}-1/m\). Directly,
\[
\boxed{\mathbb E[R_{j,n+1}-R_{j,n}\mid\mathcal F_n]
=\frac{b_n}{K(C_n+1)}R_{j,n}.}
\tag{2}
\]
As \(\lvert D_{j,n}\rvert\le K-C_n\), the absolute conditional drift in (2) is bounded by \(C_n^{-2}\). Moreover,
\[
\mathbb E[(R_{j,n+1}-R_{j,n})^2\mid\mathcal F_n]
\le C_n^{-2}+\frac{K}{C_n(C_n+1)^2}
\le C_n^{-2}+KC_n^{-3}.
\tag{3}
\]
The right-hand sides are almost surely summable by the origin growth bound. Martingale convergence and summability of the predictable drift prove \(R_{j,n}\to R_{j,\infty}\in\mathbb R\) almost surely for each of the finitely many neighbors. Their sum is identically zero. The identity
\[
\frac{N_{j,n}}K-\frac1m=\frac{C_n}{K}\left(R_{j,n}-\frac1m\right)
\]
and (1) give the displayed logarithmic correction.

**The limits are genuinely random.** The binary origin-indicator path \((J_n)\) is autonomous: its transition probabilities \(q_{0,n}=b_nC_n/K\) do not depend on which neighbor labels have occurred. Let \(\tau\) be the first nonorigin visit; it is finite almost surely and its neighbor direction \(U\) is uniform and independent of the entire binary path. Conditional on that path, the directional ratio \(R_{j,n}\), at an origin arrival, scales by \(C_n/(C_n+1)\); conditional on a nonorigin arrival, it has conditional mean multiplied by
\[
1+\frac{b_n}{K(1-q_{0,n})}.
\]
Let \(h_\tau=1\) and let \(h_n\) be the product of these strictly positive factors along the fixed binary path from \(\tau\) to \(n\). Then \(R_{j,n}/h_n\) is a martingale under the conditional law of the neighbor labels. To see that \(h_n\to h_\infty\in(0,\infty)\), denote its one-step factor by \(\gamma_n\). Conditional on the past of the autonomous binary process,
\[
\begin{aligned}
\mathbb E[\log\gamma_n\mid\mathcal F_n^J]
&=q_{0,n}\log\frac{C_n}{C_n+1}
 +(1-q_{0,n})\log\left(1+\frac{b_n}{K(1-q_{0,n})}\right)\\
&=O\left(\frac1{KC_n}+\frac1{K^2}\right),\\
\mathbb E[(\log\gamma_n)^2\mid\mathcal F_n^J]
&=O\left(\frac1{KC_n}+\frac1{K^2}\right),
\end{aligned}
\]
where \(q_{0,n}\to0\) ensures the denominators are bounded away from zero eventually. The bounds are summable; the martingale convergence theorem implies convergence of \(\sum\log\gamma_n\) to a finite real number. On each such binary path, the conditional martingale \(R_{j,n}/h_n\) has square-summable conditional variances because \(h_n\) is bounded above and below and its neighbor-label increments are at most a constant times \(1/C_n\); hence it converges in conditional \(L^2\). Consequently,
\[
\mathbb E[R_{j,\infty}\mid (J_k)_{k\ge0},U]
= h_\infty\frac{\mathbf1_{\{U=j\}}-1/m}{C_\tau}.
\]
As \(m\ge2\), this conditional expectation takes two distinct values with positive probability (depending on \(U\)). Thus every \(R_{j,\infty}\) is nondegenerate.

## Verification
The included standard-library `verify.py` checks the conditional neighbor probabilities and exact rational drift identity (2) across 3,990 finite configurations. It prints `EXACT_CONDITIONAL_IDENTITIES_OK 3990` when run with Python 3. The finite tests are consistency checks, not a proof of the almost-sure limit; the latter follows from the analytical arguments above.

## Relationship to prior work
Armfield and Mailler (2026, arXiv:2610.21864v1) prove occupation-measure localization for impurity monkey walks with the off-origin relocation parameter in an open interval below one. Their theorem does not assert the random directional first-order correction at the singular endpoint. Boyer, Falcón-Cortés, Giuggioli and Majumdar (2019, arXiv:1902.00817) describe an endpoint stationary-profile concentration at nearest neighbors and vanishing origin mass via self-consistency equations; the limiting equal-neighbor fractions are not claimed to be new here. A previously obtained sharp pathwise origin-visit count law addresses \(C_n\) alone and is recovered as an input above; it neither states nor implies, without additional stochastic analysis, the nondegenerate random directional correction. The contribution is the joint almost-sure random limit of centered neighbor counts normalized by origin count, including its nondegeneracy.

## Limitations
The model has one origin impurity, initially at the origin, with positive probability of a fresh nearest-neighbor move at that site and perfect relocation everywhere else. No explicit law, moment bound, or independence claim for the vector \(R_\infty\) is established. The result does not apply directly to the open-parameter regime below perfect off-origin relocation. A broader unlocated reinforced-urn theorem might imply the correction. Independent validation is not claimed.

## References
1. W. Armfield and C. Mailler, *Localisation of the monkey walk with an “impurity” at the origin*, arXiv:2610.21864v1, first posted 15 October 2026, https://arxiv.org/abs/2610.21864.
2. D. Boyer, A. Falcón-Cortés, L. Giuggioli, and S. N. Majumdar, *Anderson-like localization transition of random walks with resetting*, arXiv:1902.00817, https://arxiv.org/abs/1902.00817.
3. C. Mailler and G. Uribe Bravo, *Random walks with preferential relocations and fading memory: a study through random recursive trees*, arXiv:1810.02735, https://arxiv.org/abs/1810.02735.
