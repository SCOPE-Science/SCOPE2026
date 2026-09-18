# Review

**Same-model review: passed. Cross-model review: not yet performed.**

## Correctness

The stationary target follows from the standard equilibrium-age identity
\[
\mathbb P(A=a)=\mathbb P(L\ge a+1)/\mu.
\]
Because the mark law is atomless, the next observation's mark can occur in the preceding sample only inside its current renewal block. For \(n>\zeta\), this gives
\[
S_{\le\zeta,n}
=\mathbb P(A\le\zeta)
=\mathbb E\min(L,\zeta+1)/\mu.
\]

The central combinatorial identity was checked algebraically rank by rank. In a complete block of length \(\ell\), a point at rank \(r\) retains
\[
\max(r-1,\ell-\tau)
\]
same-mark observations after its one-sided forward window is deleted. The local count is therefore at most \(\zeta\) if and only if
\[
r\le\zeta+1,\qquad \ell\le\tau+\zeta,
\]
so the block reward is exactly
\[
R_{\zeta,\tau}(\ell)
=\min(\ell,\zeta+1)\mathbf 1\{\ell\le\tau+\zeta\}.
\]
Renewal reward then yields the fixed-window limit, and subtracting from the target reduces the bias exactly to
\[
(\zeta+1)\mathbb P(L>\tau+\zeta)/\mu.
\]

Sanity checks include \(L\equiv1\), where the process is i.i.d. diffuse and every stated bias is zero; \(L\equiv d>1\), where ordinary surprise is \(1/d\) and a fixed window has zero limiting estimate for \(\tau<d\) but exact limiting target for \(\tau\ge d\); and geometric blocks, where the general formula reduces to \(p(1-p)^\tau\) for ordinary surprise.

For growing windows, the regenerative reward is \(h_\zeta(L)-d_n(L)\) with
\[
d_n(L)=(\zeta+1)\mathbf 1\{L>\tau_n+\zeta\}.
\]
The centered difference from the full reward tends to zero in \(L^2\) because \(q_n\to0\) and \(\mathbb E L^2<\infty\). The ordinary renewal-reward CLT therefore supplies the same asymptotic variance, while the exact mean difference contributes
\[
-(\zeta+1)\sqrt n\,q_n/\mu.
\]
The restriction \(\tau_n=o(\sqrt n)\) makes the sample-end truncation of the one-sided windows negligible at root-\(n\) scale. These checks also prevent an otherwise easy boundary-error omission.

## Originality

The one-sided leave-a-window-out estimator is due to Nakul, Muthukumar and Pananjady (2026), and the general fact that leave-one-out/Good--Turing can fail under dependence is established prior art. Windowed Good--Turing for Markov missing mass was developed by Pananjady, Muthukumar and Thangaraj (2024), including low-count extensions; Nakul, Muthukumar and Pananjady (2025) treat stationary mass frequency by frequency under mixing.

Duplication models are also prior art. Chandra, Thangaraj and Rajaraman (2022) analyze geometrically repeated i.i.d. samples and a modified Good--Turing estimator, and Chandra and Thangaraj (2024) study missing mass under random duplications. Accordingly, no claim is made that renewal blocks, sticky repetitions, Good--Turing bias under dependence, or window deletion are themselves new.

The claimed contribution is narrower: for the stationary atomlessly marked renewal family, the exact one-sided count-surprise bias
\[
B_\zeta(\tau)
=
(\zeta+1)\mathbb P(L>\tau+\zeta)/\mu,
\]
the corresponding necessary-and-sufficient fixed-window unbiasedness condition, and the root-\(n\) window phase governed by
\[
\sqrt n\,\mathbb P(L>\tau_n+\zeta).
\]
Targeted searches by renewal/regenerative terminology, Good--Turing/leave-a-window-out terminology, count-surprise terminology, sticky-channel terminology, and the source-paper identifier did not locate these statements in the inspected sources.

The full theorem/proof text of Chandra and Thangaraj, *Missing Mass Under Random Duplications* (ISIT 2024, DOI 10.1109/ISIT57864.2024.10619664), was not inspected; bibliographic records and surrounding duplication literature were inspected. Since that paper is directly about random repetitions, it is the principal residual originality risk. The originality judgment is therefore explicitly to the best of our knowledge and limited to the exact one-sided next-token formulas above.

## Value

The result converts a generic dependence difficulty into an exact structural law. In this regenerative family, the entire asymptotic bias of a window of length \(\tau\) is the residual block-length tail at \(\tau+\zeta\). This gives a sharp explanation of when a finite window is enough, when every finite window remains biased, and how quickly a growing window must increase to preserve root-\(n\) centering.

The geometric and polynomial-tail corollaries show that the appropriate window scale can be logarithmic or a power of \(n\), even though the estimator is the same. This distinguishes the dependence feature that controls bias from a single generic mixing-time summary and gives an interpretable benchmark for broader next-token functional theory.

## Limitations

The exact formulas rely on atomless marks and therefore do not include cross-block symbol collisions. The root-\(n\) theorem assumes a finite second moment for block length and \(\tau_n=o(\sqrt n)\). Only the one-sided forward-window construction is analyzed. The result does not provide a minimax bound over arbitrary stationary or mixing processes. An equivalent formulation may remain in duplication-specific literature that was not fully inspectable.
