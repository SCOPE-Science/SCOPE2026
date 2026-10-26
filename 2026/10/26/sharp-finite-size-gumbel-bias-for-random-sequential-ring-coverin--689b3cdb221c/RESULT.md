# Sharp finite-size Gumbel bias for random sequential ring covering

## Finding
Fix any integer \(\ell\ge2\). On a periodic chain of \(n\ge\ell+1\) sites, each of the \(n\) contiguous \(\ell\)-site deposition locations receives proposals according to its own independent rate-one Poisson process. A proposed segment is retained precisely when it covers at least one previously uncovered site; otherwise it is discarded. Let \(T_{n,\ell}\) be the first time all sites are covered. Define \(G(x)=\exp(-e^{-x})\).

For every fixed real \(x\), the exact sharp first finite-size correction is
\[
\mathbb P\{\ell T_{n,\ell}-\log n\le x\}
=G(x)\left[1+n^{-1/\ell}e^{-(1+1/\ell)x}+O_{\ell,x}(n^{-2/\ell}+n^{-1})\right].
\]
The remainder is uniform as \(x\) varies over any compact subset of \(\mathbb R\). In particular,
\[
\lim_{n\to\infty}n^{1/\ell}\left(\frac{\mathbb P\{\ell T_{n,\ell}-\log n\le x\}}{G(x)}-1\right)
=e^{-(1+1/\ell)x}>0.
\]
This is a strictly positive finite-size completion bias of order \(n^{-1/\ell}\), larger than the \(n^{-1}\) finite-size correction for independent single-site coupons when \(\ell>1\). The limiting Gumbel law itself is established in earlier literature; only the stated sharp correction and the associated evaluated finite-size covering transform are assessed here.

An exact finite-chain formula accompanies the asymptotic. Put \(q=e^{-t}\) and define the \(\ell\)-by-\(\ell\) matrix \(M_\ell(q)\), indexed by \(j,k\in\{0,\ldots,\ell-1\}\), by
\[
[M_\ell(q)]_{j,0}=1-q,\qquad [M_\ell(q)]_{j,j+1}=q\quad(0\le j<\ell-1),
\]
with all other entries zero. For every \(n\ge\ell+1\) and \(t\ge0\),
\[
\mathbb P(T_{n,\ell}\le t)=\operatorname{tr}(M_\ell(e^{-t})^n).
\]

## Assumptions and scope
The periodic chain has exactly \(n\) labeled vertices and \(n\) distinct deposition anchors. The attempted segment anchored at \(i\) contains vertices \(i,i+1,\ldots,i+\ell-1\) modulo \(n\). The process begins empty; all Poisson proposal clocks are independent and have the stated unit rate; successful segments remain deposited. Time is measured in units of attempts per anchor, rather than one proposal per whole ring. The integer \(\ell\) is fixed as \(n\to\infty\). No continuum limit, randomly varying segment length, or irreversible exclusion-only adsorption is asserted.

## Proof
**1. Reduction to a finite word.** A segment rejected at time \(s\) already covers only previously covered vertices. Such a rejection cannot prevent future covering. More strongly, an anchor that has proposed at least once cannot later create a new covered vertex: its entire footprint was covered by that first proposal, whether accepted or rejected. Consequently site \(i\) is uncovered at time \(t\) if and only if none of the \(\ell\) anchors \(i-\ell+1,\ldots,i\) has proposed by time \(t\). The first-arrival indicators of the anchors are independent Bernoulli variables, equal to zero with probability \(q=e^{-t}\). Full coverage is equivalent to the resulting cyclic binary word containing no run of \(\ell\) consecutive zeros.

**2. Exact cyclic transfer.** The state \(j\) records the current trailing-zero run, with \(0\le j<\ell\). A one resets the state to zero with weight \(1-q\), while a zero sends \(j\) to \(j+1\) with weight \(q\) when allowed. A permitted cyclic word has at least one one and therefore determines a unique compatible cyclic state sequence; conversely, any closed transfer walk determines such a permitted word. Taking the weighted sum of closed walks gives the stated matrix trace. It covers the boundary cases \(q=0\) and \(q=1\), as well as all intermediate times.

**3. Principal eigenvalue.** The characteristic polynomial of the transfer matrix is
\[
\chi_\ell(\lambda,q)=\lambda^\ell-(1-q)\sum_{j=0}^{\ell-1}q^j\lambda^{\ell-1-j}.
\]
At \(q=0\) its simple leading root is \(1\), and its remaining roots vanish. Let \(\Lambda(q)\) be the real simple root near one; write \(\delta(q)=1-\Lambda(q)\). Multiplying the eigenvalue equation by \(\Lambda-q\) gives
\[
\delta(q)(1-\delta(q))^\ell=(1-q)q^\ell.
\]
By analyticity and \(\delta(q)=O(q^\ell)\),
\[
\delta(q)=q^\ell-q^{\ell+1}+O_\ell(q^{2\ell}),\qquad
\log\Lambda(q)=-q^\ell+q^{\ell+1}+O_\ell(q^{2\ell}).
\]
To control the other roots, substitute \(\lambda=qz\) into \(\chi_\ell\), divide by \(q^{\ell-1}\), and let \(q\downarrow0\). The limiting equation \(1+z+\cdots+z^{\ell-1}=0\) has \(\ell-1\) finite simple nonzero roots. Therefore all nonprincipal eigenvalues are \(O_\ell(q)\), uniformly for sufficiently small \(q\). The exact matrix trace hence satisfies
\[
\operatorname{tr}(M_\ell(q)^n)=\Lambda(q)^n+O_\ell(\ell(C_\ell q)^n).
\]
This remains true if repeated eigenvalues occur away from the small-\(q\) region, since only the limiting regime is required.

**4. Critical-window expansion.** Set \(t=(\log n+x)/\ell\), so \(q=n^{-1/\ell}e^{-x/\ell}\). Then
\[
n\log\Lambda(q)=-e^{-x}+n^{-1/\ell}e^{-(1+1/\ell)x}
+O_{\ell,x}(n^{-1}).
\]
Exponentiating produces the claimed CDF. The square of the explicit first correction contributes \(O(n^{-2/\ell})\) in the exponential expansion. The nonprincipal spectral contribution is smaller than every fixed power of \(n^{-1}\). All analytic expansions and spectral estimates are uniform on compact \(x\)-intervals, proving the asserted uniform remainder. The coefficient is strictly positive for every finite \(x\), so the order \(n^{-1/\ell}\) is sharp.

## Verification
The accompanying `check.py` (Python 3 with `mpmath`) reproduces 136 passing assertions. Ninety use exact rational arithmetic to match the transfer trace against exhaustive independent enumeration of cyclic binary words for \(\ell\in\{2,3,4,5\}\), all \(n\) from \(\ell\) through ten, and three Bernoulli parameters. Further high-precision checks verify the leading-eigenvalue expansion and its first correction for three segment lengths over several system sizes. Three direct kinetic simulations explicitly apply the accept-if-new-site rule and agree with the exact law within specified Monte Carlo tolerances. The infinite-volume asymptotic is proved in the preceding paragraphs; experiments are supplementary checks and not a substitute for the proof.

## Relationship to prior work
Krapivsky, *Random Sequential Covering* (arXiv:2209.03992, publicly posted September 8, 2022), introduced the irreversible accept-if-adds-coverage lattice model and studied dimer and longer-segment coverage and congested configurations. The finite-ring discussion provides final accepted-deposition counts and discusses conventional cover probabilities; it does not evaluate the displayed sharp continuous-time first correction.

Campos and Teixeira, *Covering Distributions* (arXiv:2401.15208, publicly posted January 26, 2024), treat random-length arcs on discrete circles. Theorem A already implies the leading Gumbel limit, including constant segment lengths after the appropriate clock-rate conversion. This first-order theorem is not presented as new here. The inspected treatment establishes the weak limit rather than the positive \(n^{-1/\ell}\) correction with its coefficient.

Falgas-Ravry, Larsson and Markström, *Speed and concentration of the covering time for structured coupon collectors* (arXiv:1601.04455; *Advances in Applied Probability* 52 (2020)), analyze a much broader random-covering class with concentration and mean-scale results; their results do not give the specialized evaluated cyclic finite-size coefficient.

Janson, *Random coverings of the circle by arcs with restricted endpoints*, *Journal of Applied Probability* 25 (1988), 215–219, studies closely related discrete-circle asymptotic coverage. Only its abstract and bibliographic record could be inspected; the full text was not accessible through the attempted channels. It remains a specific priority risk for the claimed second-order correction. Established inclusion–exclusion and finite-state transfer techniques are acknowledged as methods, not new results.

## Limitations
The result requires fixed integer segment length and independent Poisson clocks per deposition anchor. It does not cover growing segment sizes, nonuniform anchoring, rejection-on-any-overlap adsorption, arbitrary arc-size distributions, or a continuum circle. A finite-size expansion on compact normalized-time windows does not itself give an asymptotic expansion for the expectation without separate uniform-integrability bounds. Independent scholarly priority review has not been performed. The inaccessible 1988 paper may include a specialization relevant to priority; the published overlapping leading-order results are fully credited.

## References
1. P. L. Krapivsky, *Random Sequential Covering*, arXiv:2209.03992 (first version 2022-09-08), https://arxiv.org/abs/2209.03992 .
2. A. M. Campos and A. Teixeira, *Covering Distributions*, arXiv:2401.15208 (first version 2024-01-26), https://arxiv.org/abs/2401.15208 .
3. V. Falgas-Ravry, J. Larsson and K. Markström, *Speed and concentration of the covering time for structured coupon collectors*, *Adv. Appl. Probab.* 52 (2020), 433–462, arXiv:1601.04455, https://arxiv.org/abs/1601.04455 .
4. S. Janson, *Random coverings of the circle by arcs with restricted endpoints*, *J. Appl. Probab.* 25 (1988), 215–219, https://doi.org/10.2307/3214248 .
