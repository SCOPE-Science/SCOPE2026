# Critical weak Cesàro endpoints for regularly varying backward shifts

## Finding
Fix \(1\le p<\infty\) and \(0<\alpha<1/p\). Put \(\beta=\alpha p\in(0,1)\) and \(q_0=1/\alpha=p/\beta\). Let \(L:[1,\infty)\to(0,\infty)\) be measurable and slowly varying at infinity, with \(L\) and \(1/L\) bounded on each compact interval. Set \(a_j=j^\alpha L(j)\) for integers \(j\ge1\), and define the positive backward weighted shift on real or complex \(\ell_p(\mathbb N)\) by
\[
We_1=0,\qquad We_j=\frac{a_j}{a_{j-1}}e_{j-1}\quad(j\ge2).
\]
For \(q\ge1\), introduce the weak Cesàro orbital quantity
\[
\mathcal W_q(W)=\sup_{N\ge1}\sup_{x\ne0}\sup_{\lambda>0}
\frac{\lambda}{\|x\|_p}
\left(\frac{\#\{0\le k<N:\|W^kx\|_p>\lambda\}}{N}\right)^{1/q}.
\]
Then \(W\) is bounded and the following are equivalent:

1. \(\mathcal W_{q_0}(W)<\infty\).
2. \(L\) is *almost decreasing on the integers*, meaning
\[
C_L:=\sup_{j\ge s\ge1}\frac{L(j)}{L(s)}<\infty.
\]

In fact, if \(B_L:=\sup_{s\ge1,\,s\le t\le2s,\,t\in\mathbb N}L(t)/L(s)\), where \(s\) also ranges over positive integers, then \(B_L<\infty\) and the quantitative bounds are
\[
\frac{C_L}{2^\alpha B_L}\le \max\!\left\{\frac1{2^\alpha},\mathcal W_{q_0}(W)\right\},
\qquad
\mathcal W_{q_0}(W)\le \frac{C_L}{(1-\beta)^{1/p}}.
\]
Here the right inequality applies when \(C_L<\infty\); the first is interpreted in the extended sense if \(C_L=\infty\). Equivalently, and more transparently, \(C_L\le B_L\max\{1,2^\alpha\mathcal W_{q_0}(W)\}\).

Regardless of whether \(C_L\) is finite, the strong exponent profile has the same sharp cutoff:
\[
\sup_{N\ge1}\sup_{x\ne0}\frac{1}{N\|x\|_p^q}
\sum_{k=0}^{N-1}\|W^kx\|_p^q<\infty
\quad\Longleftrightarrow\quad 1\le q<q_0.
\]
In particular, the strong critical exponent \(q_0\) always fails; the weak critical exponent survives precisely for almost-decreasing \(L\). For \(L(j)=\log(e+j)^\gamma\), weak \(q_0\)-Cesàro boundedness holds exactly when \(\gamma\le0\), although the strong exponent range does not depend on \(\gamma\).

The criterion also distinguishes truly oscillatory slowly varying factors: \(L(t)=\exp(\sin(\log\log(e+t)))\) is bounded above and below and therefore preserves the weak endpoint, whereas \(L(t)=\exp(\sqrt{\log(e+t)}\sin(\log\log(e+t)))\) is slowly varying but has unbounded upward ratios, so its weak endpoint fails. In the latter case, the derivative of the exponent with respect to \(\log t\) tends to zero, while alternating troughs and peaks have unbounded height differences.

## Assumptions and scope
Slow variation means \(L(tx)/L(x)\to1\) as \(x\to\infty\) for every fixed \(t>0\). The measurability and local two-sided boundedness hypotheses ensure the uniform convergence theorem for slowly varying functions and Potter bounds. Their integer consequences, used below, are: for every \(\varepsilon>0\) there is a finite \(P_\varepsilon\) such that
\[
\frac{L(j)}{L(s)}\le P_\varepsilon\left(\frac js\right)^\varepsilon
\qquad (j\ge s\ge1),
\]
and the finite local-doubling bound \(B_L\) in the finding. Both statements follow from local uniformity over ratios in \([1,2]\), iteration over dyadic scales, and adjustment of the finitely many small denominator indices. In particular \(L(j)/L(j-1)\to1\); hence \(W\) is bounded. Only scalar positive weights are considered, with arbitrary (possibly oscillating) slowly varying factors.

The weak condition is uniform simultaneously over horizon \(N\), vector \(x\), and threshold \(\lambda\); it is not weak convergence of any individual orbit. The strong estimate uses Cesàro means of \(q\)-th powers, not powers of the Cesàro mean.

## Proof
**1. Telescoping.** For every integer \(k\ge0\),
\[
\|W^kx\|_p^p=\sum_{j>k}|x_j|^p\left(\frac{a_j}{a_{j-k}}\right)^p.
\]
All the summands are nonnegative, so Tonelli's theorem applies. Put \(b_j=|x_j|^p\), \(B=\sum_jb_j=\|x\|_p^p\), and \(\beta=\alpha p\).

**2. Uniform weak endpoint from almost-decrease.** Assume \(C_L<\infty\). For \(j>k\),
\[
\left(\frac{a_j}{a_{j-k}}\right)^p
\le C_L^p\left(\frac{j}{j-k}\right)^\beta.
\]
Fix integers \(N\ge1\), \(1\le m\le N\), and a set \(E\subset\{0,\ldots,N-1\}\) of cardinality \(m\). For every integer \(j\ge1\),
\[
\sum_{\substack{k\in E\\k<j}}
\left(\frac{j}{j-k}\right)^\beta
\le N^\beta\sum_{r=1}^{m}r^{-\beta}
\le \frac{N^\beta m^{1-\beta}}{1-\beta}. \tag{1}
\]
For \(j\le N\), the largest \(m\) contributing terms are bounded by \(j^\beta r^{-\beta}\), \(1\le r\le m\). For \(j>N\), the term at \(k\) is at most \((N/(N-k))^\beta\); its largest \(m\) values obey the same bound. The final estimate is the elementary integral bound on \(\sum_{r\le m}r^{-\beta}\).

Choose \(E=\{0\le k<N:\|W^kx\|_p>\lambda\}\), with \(|E|=m>0\). Summing the iterate identity and using (1) gives
\[
 m\lambda^p<C_L^p\sum_j b_j
 \sum_{\substack{k\in E\\k<j}}\left(\frac j{j-k}\right)^\beta
 \le\frac{C_L^p}{1-\beta}N^\beta m^{1-\beta}\|x\|_p^p.
\]
Since \(\beta/p=1/q_0\), it follows that
\[
 \lambda\left(\frac mN\right)^{1/q_0}
 \le C_L(1-\beta)^{-1/p}\|x\|_p.
\]
The case \(m=0\) is immediate, proving the asserted upper estimate.

**3. Necessity from a density block of one basis orbit.** The uniform convergence theorem gives \(B_L<\infty\). Fix positive integers \(s\) and \(j\ge2s\), take \(x=e_j\) and \(N=j\). For each of the \(s+1\) indices \(k=j-2s,\ldots,j-s\), the residual index \(t=j-k\) belongs to \([s,2s]\), and therefore
\[
 \|W^ke_j\|_p=\frac{j^\alpha L(j)}{t^\alpha L(t)}
 \ge\left(\frac{j}{2s}\right)^\alpha
 \frac{L(j)}{B_LL(s)}.
\]
Take a threshold approaching the displayed lower bound from below. By definition of \(\mathcal W_{q_0}\),
\[
\mathcal W_{q_0}(W)\ge
\left(\frac{j}{2s}\right)^\alpha\frac{L(j)}{B_LL(s)}
\left(\frac{s+1}{j}\right)^\alpha
\ge2^{-\alpha}B_L^{-1}\frac{L(j)}{L(s)}.
\]
If \(s\le j<2s\), the ratio \(L(j)/L(s)\) is already at most \(B_L\). Taking the supremum proves \(C_L\le B_L\max\{1,2^\alpha\mathcal W_{q_0}(W)\}\), and hence necessity.

**4. Every subcritical strong moment holds.** Fix \(p\le q<q_0\). Choose \(\varepsilon>0\) with \(\eta=q(\alpha+\varepsilon)<1\). Potter's inequality gives \((a_j/a_s)^q\le P_\varepsilon^q(j/s)^\eta\) for \(j\ge s\). For every \(j,N\ge1\), the same elementary column estimate gives
\[
\frac1N\sum_{0\le k<\min\{j,N\}}
\left(\frac{a_j}{a_{j-k}}\right)^q
\le\frac{P_\varepsilon^q}{1-\eta}.\tag{2}
\]
Indeed, for \(j\le N\) use \(j^\eta N^{-1}\sum_{s=1}^j s^{-\eta}\), and for \(j>N\) use \(N^\eta N^{-1}\sum_{s=1}^N s^{-\eta}\). For \(x\ne0\), Jensen's inequality applied to the probability weights \(b_j/B\) and exponent \(q/p\ge1\) yields
\[
\|W^kx\|_p^q\le\|x\|_p^q
\sum_{j>k}\frac{b_j}{B}\left(\frac{a_j}{a_{j-k}}\right)^q.
\]
Sum in \(k\) and apply (2), obtaining the uniform strong \(q\)-Cesàro estimate. Taking \(q=p\) and using monotonicity of normalized finite \(L^r\) norms covers \(1\le q<p\).

**5. The endpoint and all larger strong moments fail.** For \(x=e_j\) and \(N=j\), at \(q=q_0\),
\[
\frac1j\sum_{k=0}^{j-1}\|W^ke_j\|_p^{q_0}
=\sum_{s=1}^j\frac1s
 \left(\frac{L(j)}{L(s)}\right)^{q_0}. \tag{3}
\]
For every fixed \(R>1\), uniform slow variation on \([1/R,1]\) implies that the contribution from \(j/R\le s\le j\) has lower limit at least \(\log R\). As \(R\) is arbitrary, (3) diverges as \(j\to\infty\), even if \(L\) tends to zero. Finally, if \(q>q_0\), the single time \(k=j-1\) gives
\[
\frac1j\|W^{j-1}e_j\|_p^q
=\frac{j^{\alpha q-1}L(j)^q}{L(1)^q}\longrightarrow\infty,
\]
since a positive slowly varying function is smaller than any positive power and larger than any negative power eventually. This completes the strong cutoff and the theorem. \(\square\)

## Verification
The proof uses exact iterate identities, the finite combinatorial estimate (1), Jensen's inequality, uniform slow variation, and the standard Potter bound. The necessity proof treats the full infinite family of pairs \((s,j)\), not a finite truncation. The endpoint divergence in (3) follows from every fixed multiplicative terminal block and therefore does not require monotonicity of \(L\). The accompanying standalone program checks finite kernel bounds and logarithmic examples; it is not a substitute for the analytic argument.

## Relationship to prior work
Abbar, Arnold, and Coine [1, Theorem 3.4] characterize **strong** \(q\)-absolute Cesàro boundedness of weighted shifts, and give examples involving logarithmic factors. Arnold [2, Theorem 3.1 and Example 3.2] proves the sharp **strong** self-improvement interval and its pure-power extremal shift; his weak-type estimate in Section 4 is instead governed by Banach-space type. The publicly available finding [3] establishes the weak \(q_0\) endpoint for the *unmodified* pure-power shift \(L\equiv1\). Those results are prior input, not claimed as new here. The assertion distinguished here is the necessary-and-sufficient almost-decrease criterion for **arbitrary, including oscillating, slowly varying multipliers**, together with the invariance of the complete strong exponent range. Neither a strong-endpoint failure nor the unperturbed weak-endpoint theorem alone implies this classification. The comparison is limited to the inspected literature and does not certify global priority.

## Limitations
The equivalence is proved for telescoping positive backward shifts with regularly varying weights and \(0<\alpha<1/p\), not for every absolutely Cesàro bounded operator or arbitrary nonregular weights. No optimal universal numerical weak constant is claimed. No independent scientific verification or proof of bibliographic uniqueness has been performed. Standard uniform-convergence and Potter estimates for slowly varying functions are invoked with their stated regularity hypotheses.

## References
1. A. Abbar, L. Arnold, C. Coine, *On absolutely Cesàro bounded operators*, arXiv:2609.24601v1, first public 2026-09-21, especially Theorem 3.4 and Example 3.12.
2. L. Arnold, *Self-improvement for absolutely Cesàro bounded operators*, arXiv:2610.00271v1, first public 2026-09-24, especially Theorem 3.1, Example 3.2, and Section 4.
3. *Weak-\(L^{q_0}\) endpoint for the extremal Cesàro self-improvement shift*, publicly available published-finding corpus research finding (2026-10-04), identifier `c1795c3e8b5a`, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-weak-l-q-0-endpoint-for-the-extremal-ces-ro-self-improvement-shi--c1795c3e8b5a .
4. N. H. Bingham, C. M. Goldie, J. L. Teugels, *Regular Variation*, Cambridge University Press (1987), uniform convergence theorem and Potter bounds.
