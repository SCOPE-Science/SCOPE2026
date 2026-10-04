# Exact boundary tail law and quantitative zero entropy for the summable Blaschke sequence
## Finding
Consider the centred degree-two Blaschke sequence from Theorem E of Evdoridou--Fagella--Rippon--Stallard,
\[
f_n(z)=z\frac{z+\lambda_n}{1+\lambda_n z},\qquad 0<\lambda_n<1,\qquad \sum_{n\ge1}(1-\lambda_n)<\infty,
\]
and its forward compositions \(F_n=f_n\circ\cdots\circ f_1\). Let \(F\) be the nonconstant inner-function limit supplied by the forward-iteration theory cited in that paper, and put
\[
L_n=\prod_{j>n}\lambda_j,\qquad d_n=1-L_n.
\]
With \(m\) denoting normalized Lebesgue measure on the unit circle, one has the exact boundary identity
\[
\|F-F_n\|_{L^2(m)}^2=2(1-L_n)=2d_n. \tag{1}
\]

This identity yields a quantitative answer to the paper's question about the metric entropy of its zero-topological-entropy example. For an integer \(q\ge2\), let \(\mathcal A_q\) be the partition of the unit circle into \(q\) equal arcs and set
\[
r_n=\min\!\left\{1,\frac32 q^{2/3}d_n^{1/3}\right\}.
\]
Define
\[
\Psi_q(t)=
\begin{cases}
-t\log t-(1-t)\log(1-t)+t\log(q-1),&0\le t\le 1-1/q,\\
\log q,&1-1/q<t\le1,
\end{cases}
\]
with the continuous convention \(0\log0=0\). If \(E_N(\mathcal A_q)\) denotes the finite-horizon partition entropy in the normalization of the source paper, then for every \(N\ge1\),
\[
E_N(\mathcal A_q)\le
\frac{2\pi}{N+1}\left(2\log q+\sum_{n=1}^N\Psi_q(r_n)\right). \tag{2}
\]
Consequently \(E_N(\mathcal A_q)\to0\). By approximation of arbitrary finite measurable partitions by finite unions of arcs, the metric entropy of this non-autonomous system is exactly zero.

## Assumptions and scope
The statement concerns precisely the sequence in Theorem E of arXiv:2609.31476v1 and assumes only the hypotheses displayed above. The product \(L_n\) is positive because the defect series is summable, and \(L_n\to1\). The result makes no sequence-independent rate claim: the tail \(d_n\) can tend to zero arbitrarily slowly. The logarithms in entropy expressions are natural logarithms, matching the paper's displayed definition up to the fixed normalization by arc length.

The bare qualitative conclusion “metric entropy is zero” is not asserted as independently novel: a recent general partition-precompactness theorem of Li--Yu--Zhong already gives that qualitative implication once precompactness of the pullback partitions is established. The new content assessed here is the exact identity (1) and the explicit tail-product finite-horizon estimate (2), which specialize directly to the open example.

## Proof
Fix \(n\). For \(m>n\), write
\[
H_{m,n}=f_m\circ\cdots\circ f_{n+1},\qquad F_m=H_{m,n}\circ F_n.
\]
The family \(\{H_{m,n}\}_{m>n}\) is normal. If a subsequence converges locally uniformly to \(H_n\), then local uniform convergence \(F_m\to F\) gives \(F=H_n\circ F_n\). Since the finite Blaschke product \(F_n\) maps the unit disc onto itself, this factor \(H_n\) is unique; hence the full tail family converges to it. Moreover,
\[
H_n'(0)=\lim_{m\to\infty}\prod_{j=n+1}^m\lambda_j=L_n>0,
\]
so \(H_n\) is nonconstant. The same forward-iteration theory that supplies \(F\) shows that this tail limit is inner.

Boundary composition therefore gives \(F=H_n\circ F_n\) almost everywhere. Every centred inner function preserves normalized Lebesgue measure on the circle, so
\[
\langle F,F_n\rangle_{L^2(m)}
=\int H_n(F_n(\zeta))\overline{F_n(\zeta)}\,dm(\zeta)
=\int H_n(w)\overline w\,dm(w)
=H_n'(0)=L_n.
\]
Both \(F\) and \(F_n\) are inner and hence have boundary \(L^2(m)\)-norm one. Expanding the squared norm proves (1).

Now let \(X_n\) be the label of the equal arc containing \(F_n(\zeta)\), and let \(Y\) be the label of the equal arc containing \(F(\zeta)\). For \(0<\rho\le\pi/q\), a mismatch \(X_n\ne Y\) implies either that \(F(\zeta)\) lies within angular distance \(\rho\) of one of the \(q\) partition boundaries, or that
\[
|F_n(\zeta)-F(\zeta)|\ge2\sin(\rho/2).
\]
Because \(F\) preserves \(m\), the first event has probability \(q\rho/\pi\). By (1) and Markov's inequality, the second has probability at most
\[
\frac{2d_n}{4\sin^2(\rho/2)}.
\]
Using \(\sin(\rho/2)\ge\rho/\pi\) gives
\[
\mathbb P(X_n\ne Y)\le \frac{q\rho}{\pi}+\frac{\pi^2d_n}{2\rho^2}. \tag{3}
\]
When \(d_n\le q^{-2}\), choosing \(\rho=\pi(d_n/q)^{1/3}\) is admissible and minimizes the right side of (3), yielding
\[
\mathbb P(X_n\ne Y)\le\frac32q^{2/3}d_n^{1/3}.
\]
Otherwise the trivial probability bound one gives the same statement with \(r_n\).

Let \(e_n=\mathbb P(X_n\ne Y)\). Fano's inequality gives
\[
H(X_n\mid Y)\le -e_n\log e_n-(1-e_n)\log(1-e_n)+e_n\log(q-1).
\]
The right-hand side increases on \([0,1-1/q]\) and never exceeds \(\log q\), hence
\[
H(X_n\mid Y)\le\Psi_q(r_n).
\]
Using \(H(Y)\le\log q\), \(H(X_0\mid Y)\le\log q\), and the chain rule,
\[
H(X_0,\ldots,X_N)
\le H(Y)+\sum_{n=0}^N H(X_n\mid Y)
\le2\log q+\sum_{n=1}^N\Psi_q(r_n).
\]
The source entropy uses unnormalized arc length rather than the probability measure \(m\), multiplying normalized Shannon entropy by \(2\pi\). This is exactly (2). Since \(d_n\to0\), one has \(r_n\to0\) and \(\Psi_q(r_n)\to0\); Cesaro convergence proves the equal-arc entropy limit.

Finally, let \(\mathcal P\) be any finite measurable partition. By regularity of Lebesgue measure, for every \(\eta>0\) there is a finite partition \(\mathcal B\), each atom a finite union of arcs, with \(H(\mathcal P\mid\mathcal B)<\eta\). The same boundary-neighborhood argument and (1) give zero entropy for \(\mathcal B\). Since every \(F_n\) preserves \(m\),
\[
H\!\left(\bigvee_{n=0}^N F_n^{-1}\mathcal P\right)
\le H\!\left(\bigvee_{n=0}^N F_n^{-1}\mathcal B\right)+(N+1)H(\mathcal P\mid\mathcal B).
\]
Divide by \(N+1\), take the limsup, and then let \(\eta\downarrow0\). Thus every finite partition has zero metric entropy, so the supremum defining the metric entropy is zero.

## Verification
The proof is analytic and uses no finite computation. The critical checks are: uniqueness of the tail factor through surjectivity of the finite Blaschke product; positivity of \(L_n\); the inner-product identity \(\langle H_n,z\rangle=H_n'(0)\); preservation of normalized Lebesgue measure by centred inner functions; optimization of (3); the monotone envelope in Fano's inequality; and the normalization factor \(2\pi\) from the source's arc-length convention. The elementary product bound
\[
0\le d_n=1-\prod_{j>n}\lambda_j\le\sum_{j>n}(1-\lambda_j)
\]
provides a direct version of (2) in terms of the original summable tail.

## Relationship to prior work
Evdoridou--Fagella--Rippon--Stallard prove that this exact sequence has zero topological entropy and explicitly ask whether its metric entropy is also zero. Their proof supplies the dynamical setting and cites Ferreira for local uniform convergence to a nonconstant inner, indeed Blaschke, limit. Ferreira's 2023 results establish the relevant forward-limit structure but do not state (1) or the finite-horizon entropy estimate (2).

Li--Yu--Zhong prove a substantially broader 2026 equivalence between Rokhlin precompactness of bounded-cardinality families of finite partitions and zero maximal pattern entropy. That theorem covers the qualitative zero-entropy implication once the present convergence establishes precompactness, so qualitative zero by itself is treated here as prior-covered. The exact boundary distance \(2(1-L_n)\) and the explicit cube-root tail-product estimate in (2) were not found in that theorem, in the motivating paper, or in the other directly inspected sources. Kawan's general non-autonomous entropy framework supplies definitions and comparison tools rather than this tail law.

## Limitations
The entropy rate in (2) is tailored to equal-arc partitions; arbitrary finite partitions are handled qualitatively by approximation. No claim is made that the cube-root exponent is optimal, nor is a universal rate possible without a quantitative decay assumption on the summable tail. The exact norm identity uses the special centred-inner and forward-factor structure of this sequence. An elementary identity of this kind could conceivably be known as folklore in Hardy-space or composition-operator theory even though targeted searches did not locate the stated tail-product application.

## References
1. V. Evdoridou, N. Fagella, P. J. Rippon, G. M. Stallard, “Non-autonomous dynamics of inner functions: mixing and entropy,” arXiv:2609.31476v1 (2026).
2. G. R. Ferreira, “A note on forward iteration of inner functions,” Bulletin of the London Mathematical Society 55 (2023), 1143--1153, DOI:10.1112/blms.12779.
3. J. Li, T. Yu, X. Zhong, “The equivalence of precompactness, zero maximal pattern entropy and bounded mean complexity for finite partitions,” arXiv:2603.19772v1 (2026).
4. C. Kawan, “Metric entropy of nonautonomous dynamical systems,” Nonautonomous Dynamical Systems 1 (2014), 26--52, DOI:10.2478/msds-2013-0003.
