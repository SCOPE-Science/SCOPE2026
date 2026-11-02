# Two connectivity scales and a single cascade window for beta-threshold social networks

## Finding

Consider the Watts irreversible fractional-threshold adoption rule on a locally tree-like random \(k\)-regular network, with independently drawn **unscaled** thresholds \(T\sim\mathrm{Beta}(2,b)\), \(b>0\), and integer degree \(k\ge2\). Write \(\kappa_b(k)\) for the mean reproduction number of the vulnerable branching process. Then
\[
\kappa_b(k)=(k-1)\left[1-\left(1-\frac1k\right)^b\left(1+\frac bk\right)\right].
\]

**Unimodality and connectivity window.** For every real \(b>0\), the continuous extension \(\kappa_b(k)\), \(k>1\), has exactly one strict global maximizer. Consequently the integers satisfying \(\kappa_b(k)>1\) form a single finite interval, possibly empty. Its integer maximizers are one degree or two adjacent degrees. When \(b\ge4\), the supercritical interval is nonempty, starts at degree \(3\), and ends at a uniquely defined finite cutoff \(K_b\). More precisely, if \(c_b>3\) is the unique root of \(\kappa_b(c_b)=1\) on the decreasing side of its peak, then
\[
\{k\in\mathbb Z_{\ge2}:\kappa_b(k)>1\}=\{3,4,\ldots,\lceil c_b\rceil-1\}.
\]

**Two distinct large-\(b\) scales.** Let \(y_0=1.793282132900761\ldots\) be the unique positive solution of \(e^y=1+y+y^2\), other than \(y=0\). For any integer maximizing degree \(k_b^*\),
\[
\frac{k_b^*}{b}\longrightarrow\frac1{y_0}=0.557636738610912\ldots,\qquad
\frac{\max_{k\ge2}\kappa_b(k)}b\longrightarrow
\frac{1-e^{-y_0}(1+y_0)}{y_0}=0.298425607525639\ldots.
\]
The *continuous* upper critical degree has the sharper expansion
\[
c_b=\frac{b^2}{2}-\frac b6-\frac{13}{18}+O(b^{-1}),
\]
whereas the largest supercritical *integer* degree satisfies \(K_b=b^2/2-b/6+O(1)\). Hence the most vulnerable degree is linear in \(b\), while the last degree permitting supercritical vulnerable propagation is quadratic in \(b\).

## Assumptions and scope

The network is uncorrelated, locally tree-like and asymptotically \(k\)-regular. A neighbor with one activated contact adopts exactly if its own threshold is no greater than \(1/k\). Thresholds are independent of one another and of the graph, with density \(f_b(t)=b(b+1)t(1-t)^{b-1}\) for \(0<t<1\). This distribution is *not rescaled to a constant mean*: as \(b\) grows its mean \(2/(b+2)\) changes. The expression \(\kappa_b(k)>1\) is the usual local vulnerable-branching supercriticality condition for infinitesimal seed fractions. It does not assert that every seed generates a macroscopic cascade, or determine cascade probability and final size.

For the shape theorem, \(b\) is any fixed positive real and \(k>1\) is a real variable solely to analyze the discrete degrees. For the explicit interval, \(b\ge4\); for the asymptotics, \(b\to+\infty\). All \(O(\cdot)\) constants are absolute over those latter limits.

## Proof

**1. Exact vulnerability.** The beta density integrates to
\[
F_b(x)=\Pr(T\le x)=1-(1-x)^b(1+bx),\qquad 0\le x\le1.
\]
On a \(k\)-regular locally tree-like network, a vulnerable vertex reached along one edge offers \(k-1\) outward edges. Thus \(\kappa_b(k)=(k-1)F_b(1/k)\).

**2. Unique continuous maximum.** Put \(x=1/k\in(0,1)\) and \(g_b(x)=(1-x)F_b(x)/x\). Direct differentiation, with \(q_b(x)=(1-x)^b[1+bx+b(b+1)x^2]\), gives
\[
g'_b(x)=\frac{q_b(x)-1}{x^2},\qquad
q'_b(x)=b(b+1)x(1-x)^{b-1}[1-(b+2)x].
\]
The function \(q_b\) starts at \(q_b(0)=1\), strictly rises until \(x=1/(b+2)\), then strictly falls to \(q_b(1)=0\). It therefore crosses level \(1\) exactly once at some \(x_b\in(1/(b+2),1)\). Since \(g_b(x)\to0\) at both \(x\downarrow0\) and \(x\uparrow1\), the unique crossing is its strict global maximum. The strictly monotone substitution \(k=1/x\) transfers unimodality to \(\kappa_b(k)\). Thus its superlevel set above \(1\) is an interval, containing at most one finite sequence of integer degrees; strict increase and decrease also restrict integer maximizers to one degree or an adjacent pair. The high-degree tail follows from \(F_b(x)\sim b(b+1)x^2/2\), so this superlevel interval is bounded.

**3. Nonempty window and exact left boundary when \(b\ge4\).** For every finite \(b>0\), \(\kappa_b(2)=F_b(1/2)<1\). Differentiating the complement \((1-x)^b(1+bx)\) with respect to \(b\) shows it is decreasing: its logarithmic derivative \(\log(1-x)+x/(1+bx)<0\). Therefore \(\kappa_b(3)\ge\kappa_4(3)=262/243>1\) for \(b\ge4\). By the single-maximum theorem, the lower continuous crossing lies strictly between \(2\) and \(3\), and the upper crossing \(c_b\) exists uniquely beyond the maximum. The strict inequality at the upper crossing gives the integer endpoint \(K_b=\lceil c_b\rceil-1\), including the case when \(c_b\) is itself an integer.

**4. Linear scale of the maximizer.** Let \(y=bx\) and keep \(y>0\) fixed as \(b\to\infty\). The defining crossing equation becomes
\[
q_b(y/b)\longrightarrow e^{-y}(1+y+y^2).
\]
The limiting function exceeds \(1\) for all sufficiently small positive \(y\), and eventually falls below \(1\). Its unique positive crossing \(y_0\) satisfies \(e^{y_0}=1+y_0+y_0^2\). Because \(b x_b>b/(b+2)\) and, for a fixed sufficiently large \(Y\), \(q_b(Y/b)<1\) for all large \(b\), these crossings are confined to a compact interval in \((0,\infty)\). Uniform convergence there implies \(b x_b\to y_0\). Hence \(k_b^{\mathrm{cont}}/b\to1/y_0\). The continuous maximizer is bracketed by its two adjacent integer degrees, so integer maximizers have the same ratio. In the same scaling, \(\kappa_b(b/y)/b\to[1-e^{-y}(1+y)]/y\), yielding the displayed maximum coefficient.

**5. Quadratic scale and second correction of the upper endpoint.** Uniformly for bounded real \(t\) at \(k=b^2/2+t b\), the integral in Step 1 admits the expansion
\[
F_b(1/k)=\frac{b(b+1)}{2k^2}-\frac{b(b^2-1)}{3k^3}
+\frac{b(b+1)(b-1)(b-2)}{8k^4}+O\!\left(\frac{b^5}{k^5}\right).
\]
Multiplication by \(k-1\) and expansion in \(1/b\) yield
\[
\kappa_b(b^2/2+t b)=1+\frac{-2t-1/3}{b}
+\frac{4t^2+(10/3)t-1}{b^2}+O(b^{-3}).
\]
The signs for \(t=-1/6\pm\varepsilon\) show \(c_b=b^2/2-b/6+o(b)\). Substituting \(k=b^2/2-b/6+u\), for bounded \(u\), sharpens the expansion to
\[
\kappa_b(k)=1+\frac{-2u-13/9}{b^2}+O(b^{-3}).
\]
The sign changes at \(u=-13/18+O(b^{-1})\). Since the unique decreasing-side crossing is already located in this quadratic region, this proves \(c_b=b^2/2-b/6-13/18+O(b^{-1})\). Rounding \(c_b\) to the integer cutoff introduces at most one unit, proving the asserted \(K_b\) expansion.

## Verification

The standalone `checker.py` uses exact rational beta-CDF calculations and an independent polynomial-integral representation for integral \(b\), verifies unimodality and contiguous integer superlevel sets on finite parameter ranges, checks the explicit degree-3 boundary, and compares numerical quadrature, maximizer roots and upper-root asymptotics. Execute `python checker.py` with Python 3, NumPy and SciPy installed. Its reported successful run completed 78,629 exact-rational comparisons and supplementary numerical checks. The code is a finite consistency check, not a substitute for the preceding universal proof.

## Relationship to prior work

Watts (2002) introduced vulnerable-cluster propagation and the qualitative finite-connectivity cascade window. Meador-Woodruff and Ghoshal (2026, first public version October 24) provide the general degree-distribution branching formula, beta thresholds and large-connectivity scaling for beta-binomial or Poisson degree ensembles with fixed-mean rescaling; the original paper explicitly distinguishes such rescaled distributions from unscaled Beta shapes. Fontanari (2026) considers beta thresholds in a different, fully connected finite-population Granovetter model. Those treatments supply models and qualitative mechanisms but do not, in the available inspected material, state the exact all-\(b\) regular-degree unimodality, the linear maximizer or the quadratic upper cutoff for this unscaled \(\mathrm{Beta}(2,b)\) family. The formula in Step 1 is a specialization of known branching theory; the new mathematical claim is the exact shape-and-two-scale classification and its sharp boundary expansion.

## Limitations

The theorem is about a locally tree-like branching criterion, not a complete nonlinear diffusion or finite-size cascade law. It assumes a regular degree distribution, independent thresholds, no clustering and a changing beta mean. It does not establish that the exact result extends to rescaled fixed-mean beta thresholds, degree-correlated or heterogeneous networks. A previously unindexed equivalent derivation is a priority risk; published qualitative cascade windows are not claimed as new. No independent scientific validation has been performed.

## References

1. D. J. Watts, “A simple model of global cascades on random networks,” *PNAS* **99** (2002), 5766–5771. https://doi.org/10.1073/pnas.082090499 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC122850/
2. A. Meador-Woodruff and G. Ghoshal, “Interplay Between Network Heterogeneity and Activation Thresholds in Global Cascades,” arXiv:2610.33927v1 (first submitted October 24, 2026), https://arxiv.org/html/2610.33927v1
3. J. F. Fontanari, “Exact Solution of Granovetter’s Threshold Model for a Finite Population,” arXiv:2606.25921 (2026), https://arxiv.org/abs/2606.25921
