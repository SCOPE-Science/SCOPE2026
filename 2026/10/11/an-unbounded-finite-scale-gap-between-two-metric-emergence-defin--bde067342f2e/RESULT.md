# An unbounded finite-scale gap between two metric emergence definitions

## Finding
Let \(X=\{0,1\}^{\mathbb N_0}\) with the one-sided left shift \(\sigma\) and the compatible metric
\[d(x,y)=\sum_{r=0}^{\infty}2^{-r-1}|x_r-y_r|.\]
Write \(W_1\) for the induced Wasserstein distance on probability measures on \(X\). For every integer \(k\ge2\), there is an explicit probability measure \(\mu_k\), supported on precisely \(k\) points, with the following **simultaneous conclusions** for the two metric emergences of Berger [1, Definitions 1.1--1.2]:
\[
\mathscr E_{\mu_k}(\sigma)(\varepsilon)=1\quad\text{if and only if }\varepsilon>1/k,
\qquad
\mathscr E'_{\mu_k}(\sigma)(\varepsilon)=\left\lfloor\frac{1}{2\varepsilon}\right\rfloor+1\quad\text{for every }\varepsilon>0.
\]
In particular, at \(\varepsilon=2/k\), the former is \(1\), while the latter is \(\lfloor k/4\rfloor+1\), which diverges as \(k\to\infty\). Both functions use the same finite set of common prototype probability measures for all sample points, rather than prototypes chosen separately by orbit.

## Assumptions and scope
The reference measures \(\mu_k\) are **not invariant** under \(\sigma\). This is permitted in [1, Section 1.1], which explicitly treats a compact metric space, a measurable self-map, and any reference probability measure. The definitions use a **strict** error inequality \(<\varepsilon\). For a finite prototype set \(Q\subset\mathcal M(X)\), let \(\operatorname{dist}_{W_1}(\eta,Q)=\min_{q\in Q}W_1(\eta,q)\) and let \(e_n(x)=n^{-1}\sum_{t=0}^{n-1}\delta_{\sigma^t x}\). The ordinary metric emergence minimizes \(|Q|\) subject to
\[\limsup_{n\to\infty}\int\operatorname{dist}_{W_1}(e_n(x),Q)\,d\mu_k(x)<\varepsilon,\]
whereas the second metric emergence minimizes \(|Q|\) subject to
\[\int\limsup_{n\to\infty}\operatorname{dist}_{W_1}(e_n(x),Q)\,d\mu_k(x)<\varepsilon.\]
All claims refer to the displayed binary metric, not an unspecified equivalent metric or a different Wasserstein order.

## Proof
**Explicit construction.** Construct \(k\) infinite binary strings \(x^{(1)},\ldots,x^{(k)}\) simultaneously in stages. Put \(T_0=0\). At stage \(s\ge1\), let
\[L_s=(T_{s-1}+1)^2,\qquad R_s=(T_{s-1}+L_s+1)^2,\qquad T_s=T_{s-1}+L_s+R_s.\]
During the first \(L_s\) positions of the stage, put a \(1\) only in the string indexed by \(a_s=1+((s-1)\bmod k)\), and put \(0\) in all other strings. During the remaining \(R_s\) positions put \(0\) in all \(k\) strings. Set \(\mu_k=k^{-1}\sum_{j=1}^k\delta_{x^{(j)}}\). Each \(x^{(j)}\) is distinct because each index is active infinitely often. At every coordinate \(q\ge0\),
\[\sum_{j=1}^k x^{(j)}_q\le1.\tag{1}\]

**One prototype controls ordinary emergence.** Let \(z_0=0^\infty\). Coupling the empirical measure to the single Dirac measure \(\delta_{z_0}\) gives an equality
\[W_1(e_n(x^{(j)}),\delta_{z_0})=\frac1n\sum_{t=0}^{n-1}d(\sigma^t x^{(j)},z_0).\]
Thus nonnegativity, the summable metric, and (1) yield for every \(n\ge1\)
\[
\frac1k\sum_{j=1}^k W_1(e_n(x^{(j)}),\delta_{z_0})
=\frac1{kn}\sum_{t<n}\sum_{r\ge0}2^{-r-1}\sum_{j=1}^k x^{(j)}_{t+r}
\le\frac1k.
\]
For every \(\varepsilon>1/k\), one prototype therefore satisfies the strict definition; by nonemptiness the minimum count is exactly \(1\). Conversely, fix any one prototype \(q\in\mathcal M(X)\). At the end of each one-block, the active orbit's empirical measure tends to \(\delta_{z_1}\), while each inactive orbit tends to \(\delta_{z_0}\), since \(L_s/T_{s-1}\to\infty\) and the preceding reset dominates every older stage. Along these times, the averaged one-prototype cost tends to
\[\frac{k-1}{k}W_1(\delta_{z_0},q)+\frac1k W_1(\delta_{z_1},q)
\ge\frac1k+\frac{k-2}{k}W_1(\delta_{z_0},q)\ge\frac1k,\]
using \(W_1(\delta_{z_1},q)\ge1-W_1(\delta_{z_0},q)\) and \(k\ge2\). Thus **no single prototype** satisfies the strict tolerance when \(\varepsilon\le1/k\), proving the claimed if-and-only-if.

**The same entire segment is the cluster set for every orbit.** Let \(z_1=1^\infty\), \(p_{j,n}=n^{-1}\sum_{t<n}x^{(j)}_t\), and \(\nu_t=(1-t)\delta_{z_0}+t\delta_{z_1}\), \(0\le t\le1\). Then
\[W_1(e_n(x^{(j)}),\nu_{p_{j,n}})\longrightarrow0\quad(n\to\infty).\tag{2}\]
Indeed, couple each term \(\delta_{\sigma^t x^{(j)}}\) with \(\delta_{z_{x^{(j)}_t}}\). Fix a window length \(h\). For stage \(s\), there are at most \(2s+2\) boundaries where the letter in any one string changes up to position \(n+h\) if \(T_{s-1}\le n<T_s\), apart from at most \(h\) future boundaries; each boundary spoils at most \(h\) windows starting before \(n\). Since \(n\ge T_{s-1}\) and \(s/T_{s-1}\to0\), the fraction of spoiled windows is \(o(1)\) for fixed \(h\). All other orbit points are within \(2^{-h}\) of their constant-letter sequences. Thus the coupling cost is at most \(2^{-h}+o(1)\), proving (2) as \(h\to\infty\).

For every index \(j\), infinitely many active stages end with \(p_{j,n}\to1\), because \(L_s/T_{s-1}\to\infty\), while every stage's reset ends with \(p_{j,n}\to0\), because \(R_s/(T_{s-1}+L_s)\to\infty\). As \(|p_{j,n+1}-p_{j,n}|\le1/(n+1)\), the cluster set of \((p_{j,n})_n\) is the full interval \([0,1]\). By (2), **for all \(j\)**,
\[\operatorname{Acc}_{n\to\infty} e_n(x^{(j)})=S:=\{\nu_t:0\le t\le1\}.\tag{3}\]
(The use of \(\operatorname{Acc}\) denotes the set of all subsequential weak, equivalently \(W_1\), limits.)

**Exact second emergence.** For any finite common prototype set \(Q\), continuity of distance to \(Q\) and (3) imply
\[\limsup_{n\to\infty}\operatorname{dist}_{W_1}(e_n(x^{(j)}),Q)=\max_{0\le t\le1}\operatorname{dist}_{W_1}(\nu_t,Q),\]
independent of \(j\). Its average under \(\mu_k\) is the same expression. Because \(d(z_0,z_1)=1\),
\[W_1(\nu_s,\nu_t)=|s-t|.\tag{4}\]
For \(N\) prototype measures in \(\mathcal M(X)\), any radius \(r\) Wasserstein ball intersects the segment \(S\) in a subset having \(t\)-diameter at most \(2r\), by the triangle inequality and (4). To cover the entire unit parameter interval, necessarily \(2Nr\ge1\). Equality is attained by choosing the \(N\) centers \(\nu_{(2a-1)/(2N)}\), \(1\le a\le N\), for which the maximal distance equals \(1/(2N)\). Consequently the **exact** optimal error for \(N\) common prototypes in the second emergence is \(1/(2N)\), and the strict inequality \(1/(2N)<\varepsilon\) yields
\[\mathscr E'_{\mu_k}(\sigma)(\varepsilon)=\lfloor(2\varepsilon)^{-1}\rfloor+1.\]
This proves the claim.

## Verification
All steps are analytic. The sequences are completely specified by the integer recurrences for \(L_s,R_s,T_s\); no probabilistic typicality, finite truncation, or numerical data are used as proof. Reproduction consists of checking the one-hot identity (1), the constant-block empirical approximation (2), and the exact interval covering argument (3)--(4). For every \(k\), the ordinary emergence has exactly one prototype if and only if \(\varepsilon>1/k\); the precise number of ordinary prototypes below or at that threshold is **not** claimed.

## Relationship to prior work
Berger's new second metric emergence moves \(\limsup\) inside the reference-measure integral [1, Definitions 1.1--1.2]; his Proposition 1.3 proves equality for empirical systems, and Theorem 1.4 identifies the finite small-scale second-emergence regime. The construction here occupies the complementary nonempirical regime and gives a precise, unbounded **finite-resolution** separation not asserted by those results. His Theorem 4.18 concerns existence of a measure with matching second/topological emergence order, rather than the comparison of the two metric emergences for the same finitely supported reference measure.

Berger--Bochi [2] establishes emergence/quantization theory, particularly for invariant measures, but precedes Definition 1.2 in [1]. Kiriki--Nakano--Soma [3] establishes pointwise emergence and irregular-orbit richness in shifts, but its pointwise prototypes can be associated to a single orbit; it does not give the simultaneous \(k\)-orbit anti-synchronization needed to keep the ordinary **integrated** metric emergence at one while making the second integrated emergence arbitrarily large. The present result does not contradict the classical quantization of individual empirical cluster sets.

## Limitations
The reference measure is finitely supported and intentionally non-invariant; the example does not establish a comparable gap for Lebesgue reference measure on a smooth manifold or an invariant measure. For the first emergence, only its exact one-prototype threshold is determined; its exact number of prototypes at smaller tolerances is not established. The second emergence's coefficient depends on the chosen normalization \(d(z_0,z_1)=1\). This construction proves an explicit finite-resolution effect, not a high-emergence-order theorem.

## References
[1] P. Berger, *Emergence in dynamical systems*, arXiv:2609.28264v1 (first public 2026-09-23), especially Definitions 1.1--1.2, Proposition 1.3, Theorem 1.4, and Theorem 4.18. https://arxiv.org/pdf/2609.28264

[2] P. Berger and J. Bochi, *On Emergence and Complexity of Ergodic Decompositions*, arXiv:1901.03300 (2019); *Advances in Mathematics* 390 (2021), 107904. https://arxiv.org/abs/1901.03300

[3] S. Kiriki, Y. Nakano, and T. Soma, *Emergence via non-existence of averages*, arXiv:1904.03424v3 (2022); *Advances in Mathematics* 400 (2022), 108254, Sections 1.1 and 1.3. https://arxiv.org/pdf/1904.03424
