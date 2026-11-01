# Lucas equilibrium census and parity-sharp stability in a directed inhibitory logistic ring

## Finding

A one-sided, cyclically coupled population map has an exact fixed-point count governed by Lucas numbers, yet the stable patterns obey a sharply different odd-even classification. For every integer \(n\ge 3\), \(1<r<3\), and \(\gamma>1\), let \(H(u)=\max\{0,\min\{1,u\}\}\) and let \(F:[0,1]^n\to[0,1]^n\) be the synchronous map
\[
 F_i(x)=H\!\left(r x_i(1-x_i-\gamma x_{i+1})\right),\qquad x_{n+1}=x_1.
\]
Write \(h=1-1/r\), \(p=h/(1+\gamma)\), and let \(L_n\) be the Lucas number determined by \(L_0=2\), \(L_1=1\), \(L_{j+2}=L_{j+1}+L_j\). Then:

1. **Complete equilibrium census.** All fixed points are the homogeneous state \(x_i=p\) and exactly one vertex \(x_i=h\mathbf1_{\{i\in S\}}\) for each independent set \(S\) of the undirected cycle graph \(C_n\). Thus the exact number is \(L_n+1\), with no hidden positive, partly clipped, or boundary fixed points.
2. **Checkerboards and parity.** When \(n\) is even, exactly two fixed points are locally exponentially attracting, namely the alternating occupied/vacant configurations. Every other fixed point, including the homogeneous one, is unstable. When \(n\) is odd, all boundary fixed points are unstable.
3. **Complete positive-equilibrium stability condition on odd rings.** For odd \(n\), let \(c_n=\cos(\pi/n)\). The homogeneous state is locally exponentially attracting precisely when
\[
1<\gamma<\frac1{c_n},\qquad
1<r<1+\frac{2(1+\gamma)(1-\gamma c_n)}{1+\gamma^2-2\gamma c_n}.
\]
It is unstable whenever either inequality is reversed strictly (including every \(\gamma\ge1/c_n\)). At equality in the upper bound for \(r\), a complex-conjugate pair of characteristic multipliers has modulus exactly one, so local exponential attraction is lost; no nonlinear bifurcation type is asserted at equality.
4. **Quadratic frustration window.** The allowed strong-inhibition interval for stability of the positive state on an odd ring has width \(\sec(\pi/n)-1\sim\pi^2/(2n^2)\), as \(n\to\infty\) through odd integers.

Consequently, the number of equilibria grows exponentially with ring size while the number of locally exponentially attracting equilibria remains two on even rings and is at most one on odd rings. This is a fixed-point and *local* stability theorem, not a claim about global attractors or recurrent dynamics elsewhere.

## Assumptions and scope

The ring length is an integer \(n\ge3\). The growth factor satisfies \(1<r<3\), so the isolated logistic map has an attracting nonzero equilibrium. Every edge has the same strictly inhibitory strength \(\gamma>1\) directed from site \(i+1\) to site \(i\). Clipping is literal saturation into \([0,1]\), and all stability statements use the relative topology of that cube. A fixed point is called *locally exponentially attracting* if sufficiently close cube trajectories approach it at a geometric rate; *unstable* means Lyapunov unstable. We make no assertion of Lyapunov stability at the precisely neutral positive-equilibrium boundary.

The Lucas convention is \(L_0=2\), \(L_1=1\), \(L_2=3\), \(L_3=4\). An independent set in \(C_n\) is a set of sites containing no pair of cyclic neighbors.

## Proof

**Step 1: Nonzero fixed coordinates.** For any \(x\in[0,1]^n\), \(F_i(x)=0\) if \(x_i=0\). At a fixed point, \(x_i=1\) is impossible: the unclipped argument there is \(-r\gamma x_{i+1}\le0\), so the clipped image is zero. Thus any positive fixed coordinate lies in \((0,1)\), where clipping is inactive, and
\[
x_i=r x_i(1-x_i-\gamma x_{i+1})
\quad\Longrightarrow\quad x_i+\gamma x_{i+1}=h.
\]
If some coordinate vanishes, examine the last positive site of each maximal positive block immediately preceding a zero. Its value is \(h\). A second positive site immediately before it would have value \(h-\gamma h<0\), a contradiction. Therefore every positive block has length one: its support is an independent set, and all its positive coordinates equal \(h\). Conversely every such independent-set vertex is fixed, because a positive site sees a zero successor and a zero coordinate remains zero. If all coordinates are positive, subtract the constant solution \(p\) from \(x_i+\gamma x_{i+1}=h\). The errors satisfy \(y_i=-\gamma y_{i+1}\) around the entire cycle, hence \(y_i=(-\gamma)^n y_i\); since \(\gamma>1\), every error vanishes. This proves the list of all fixed points.

**Step 2: Number of fixed points.** If an independent set omits site one, its remaining choices form a path of length \(n-1\) and there are \(F_{n+1}\) possibilities; if it contains site one, both neighboring sites are omitted and the remaining choices form a path of length \(n-3\), giving \(F_{n-1}\) possibilities. Here \(F_0=0,F_1=1\) and \(F_{j+2}=F_{j+1}+F_j\). The standard identity \(F_{n+1}+F_{n-1}=L_n\) gives \(L_n\) boundary fixed points and one strictly positive point. The same formula covers \(n=3\).

**Step 3: Every nonalternating boundary fixed point is unstable.** Any independent set lacking the alternating property has two adjacent empty sites \(i,i+1\). Keep coordinate \(i+1\) initially zero and perturb the zero coordinate \(i\) to a sufficiently small positive value. Because zero coordinates remain exactly zero under all iterates, \(x_{i+1}(t)=0\) for all \(t\). Thus the perturbed coordinate evolves autonomously by the scalar logistic iteration \(u_{t+1}=r u_t(1-u_t)\) (clipping is inactive on the interval \([0,h]\)). For \(1<r<3\), every sufficiently small \(u_0>0\) grows until it exceeds, say, \(h/2\), proving Lyapunov instability of that fixed vertex. An independent cyclic binary word with neither adjacent ones nor adjacent zeros must alternate; this is possible precisely for even \(n\), with exactly two choices.

**Step 4: Exponential attraction of the even checkerboards.** At an alternating fixed point, each positive site has derivative \(2-r\), whose modulus is strictly below one. At a zero site, its update has a one-sided linear multiplier \(b=\max\{0,r(1-\gamma h)\}\in[0,1)\); the upper saturation bound is inactive in a small neighborhood of this site. Dependence of a zero-site update on its neighboring positive site is quadratic in the small zero coordinate and hence contributes no linear cross term. A positive site's update can depend linearly on the neighboring zero coordinate. Ordering the positive and zero components yields a local one-sided triangular linear part with diagonal coefficients \(2-r\) and \(b\). Equivalently, with the zero variables weighted first, they contract at some factor below one and drive the positive variables through a bounded inhomogeneous term; a weighted maximum norm and continuity of the quadratic remainders make the full local map a contraction. Therefore the two checkerboards are locally exponentially attracting.

**Step 5: Circulant spectrum at the positive state.** Let \(S\) be the cyclic forward-shift operator, \((Sv)_i=v_{i+1}\), and set \(t=(r-1)/(1+\gamma)>0\). At \(x_i=p\), clipping is inactive, and direct differentiation yields
\[
DF(p\mathbf1)=I-t(I+\gamma S),\qquad
\lambda_k=1-t(1+\gamma e^{2\pi ik/n}),\quad k=0,\ldots,n-1.
\]
Writing \(u=\cos(2\pi k/n)\), a multiplier has modulus below one if and only if
\[
 1+\gamma u>0,\qquad
 t<\frac{2(1+\gamma u)}{1+\gamma^2+2\gamma u}.
\]
For \(\gamma>1\), the right-hand side is strictly increasing as a function of \(u\), since its derivative is \(2\gamma(\gamma^2-1)/(1+\gamma^2+2\gamma u)^2>0\). The smallest cyclic cosine is \(-1\) for even \(n\), which yields \(\lambda=1+t(\gamma-1)>1\), establishing instability. For odd \(n\), it is \(-\cos(\pi/n)=-c_n\). Requiring every multiplier to lie strictly inside the unit disk is therefore equivalent to \(\gamma c_n<1\) and the displayed strict upper bound on \(r\). At \(r\) equality, exactly the two conjugate modes with that least cosine have unit modulus, whereas the other modes have modulus less than one. If \(\gamma c_n=1\), these two modes already have modulus greater than one because their real linear coefficient vanishes while their imaginary coefficient does not. Above either sharp bound a multiplier has modulus greater than one. Standard linearization yields local exponential attraction under strict spectral radius below one, and Lyapunov instability above one.

**Step 6: Odd-size window.** Taylor expansion of \(\sec z\) at zero gives \(\sec(\pi/n)-1=\pi^2/(2n^2)+O(n^{-4})\). This determines the possible inhibition interval supporting a stable positive equilibrium, regardless of the additional constraint on \(r\), completing the proof.

## Verification

The accompanying `verify.py` is self-contained and uses only the Python standard library. Executing `python3 verify.py` checks, with exact rational arithmetic, that all independent-set candidate points satisfy the clipped fixed equations and that their number equals the Lucas count for \(n=3,\ldots,12\) at three rational parameter pairs. It also checks circulant stability and the sharp odd-ring spectral boundary for \(n=3,\ldots,21\), and even checkerboard fixedness and local multipliers for several even sizes. These are reproducible finite spot checks, not a proof of completeness or a substitute for the all-parameter argument above.

## Relationship to prior work

Baron and Galla's 2026 disordered logistic map studies high-dimensional clipped logistic dynamics with heterogeneous random couplings, concentrating on random-matrix and mean-field instability mechanisms. The present theorem treats an **explicit deterministic, directed, one-sided inhibitory ring**, rather than their random ensemble, and derives a complete support-by-support census and a finite-size stability threshold. Its model is motivated by their clipped coupling formulation; the claim is not inferred from their random results.

Killingback, Loftus and Sundaram analyze competitive coupled-map lattices and spatial symmetry breaking on **undirected** graphs, with their detailed dynamical analysis emphasizing Ricker/Hassell/Maynard-Smith site maps; they explicitly avoid the unbounded negative-value issue of an unclipped logistic competition map. Their treatment does not classify all fixed points and their strict local stability for the directed, clipped ring considered here.

Mareno and English analyze fixed points and bifurcations of a particular **two-component symmetric logistic coupling**. The present arbitrary-size one-way ring, Lucas count, and odd/even spectral criterion are not special cases of that fixed two-dimensional study.

The independent-set count itself is a classical combinatorial fact. The finding is the exact realization and complete local dynamical classification of those patterns under this nonlinear, clipped directed system; the Lucas sequence alone is not claimed as a new identity.

## Limitations

The result is conditional on \(\gamma>1\), \(1<r<3\), identical coupling strengths, a directed cycle, and clipping to \([0,1]\). At the odd-ring spectral equality, the theorem establishes neutral characteristic multipliers and failure of *exponential* attraction but deliberately makes no assertion of Lyapunov stability or bifurcation type. It does not classify periodic attractors, global basins, or chaotic behavior; a ring with no attracting equilibrium need not lack other attractors. No priority claim is made beyond the primary works and available searches considered, and specialized studies of inhibitory ring maps remain a residual literature risk.

## References

1. J. W. Baron and T. Galla, *The disordered logistic map*, arXiv:2609.24402 (publicly posted 21 September 2026). https://arxiv.org/abs/2609.24402
2. T. Killingback, G. Loftus and B. Sundaram, *Competitively Coupled Maps and Spatial Pattern Formation*, arXiv:1204.2463, and *Physical Review E* **87**, 022902 (2013). https://arxiv.org/abs/1204.2463
3. A. Mareno and L. Q. English, *Flip and Neimark–Sacker Bifurcations in a Coupled Logistic Map System*, *Discrete Dynamics in Nature and Society*, 2020, article 4103606. https://doi.org/10.1155/2020/4103606
