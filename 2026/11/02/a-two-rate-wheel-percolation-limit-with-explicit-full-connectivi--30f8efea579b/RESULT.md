# A two-rate wheel-percolation limit with explicit full-connectivity and hub-mass laws

## Finding

Let \(W_{n+1}=K_1\vee C_n\) be the wheel with hub \(o\) and \(n\ge3\) rim vertices. Independently retain every rim edge with probability \(1-a/n\) and every spoke with probability \(b/n\), where \(a,b>0\) are fixed and \(n>\max\{a,b,2\}\). Let \(H_n\) be the number of rim vertices connected to the hub in the retained-edge graph, divided by \(n\).

As \(n\to\infty\), \(H_n\) converges in distribution to a nonconstant random variable \(H_{a,b}\in[0,1]\), whose law is given exactly by the following marked-circle construction. Place independent homogeneous Poisson point processes of intensity \(a\) (cuts) and intensity \(b\) (spoke marks) on a circle of circumference one. A realization with zero or one cut has one rim component, the entire circle; with at least two cuts, the consecutive open arcs are the rim components. An arc is hub-connected if it contains at least one spoke mark. Then \(H_{a,b}\) is the sum of the lengths of hub-connected arcs. When there are no cuts, this convention again means the entire circle is hub-connected precisely if there is at least one spoke mark.

The boundary masses and mean are explicit. Put \(\lambda_{\pm}=(b\pm\sqrt{b^2+4ab})/2\). Then

\[
\Pr(H_{a,b}=0)=e^{-b},\qquad
\Pr(H_{a,b}=1)=e^{-(a+b)}\left(e^{\lambda_+}+e^{\lambda_-}-2\right),
\]

\[
\mathbb E H_{a,b}
=1-(1+a)e^{-(a+b)}
-\frac{a^2}{(a+b)^2}\left(1-(1+a+b)e^{-(a+b)}\right).
\]

Both boundary masses are strictly positive; also \(\Pr(0<H_{a,b}<1)>0\). Thus this two-rate window does not self-average. Since \(0\le H_n\le1\), every fixed nonnegative integer moment of \(H_n\) converges to the corresponding moment of \(H_{a,b}\).

There is also a finite-size exact mean: for \(\delta=a/n\) and \(q=b/n\),

\[
\mathbb EH_n=1-\left((1-\delta)^n+n\delta(1-\delta)^{n-1}\right)(1-q)^n
-\sum_{\ell=1}^{n-1}\ell\delta^2(1-\delta)^{\ell-1}(1-q)^\ell.
\]

For every such \(n\), \(\Pr(H_n=0)=(1-b/n)^n\). All formulas concern the hub component, not the largest component of the graph.

## Assumptions and scope

The underlying graph is the undirected simple wheel \(K_1\vee C_n\); all \(2n\) edge-retention decisions are mutually independent. The parameters \(a,b\) are fixed strictly positive real numbers, and the limits are taken over integers \(n\to\infty\) with the displayed edge probabilities in \((0,1)\). A retained rim edge corresponds to an intact segment of the circle, whereas a retained spoke represents a contact with the hub. Component sizes count rim vertices only; the hub itself is excluded. Arc endpoints have length zero and play no part in the limit.

## Proof

**1. Exact finite mean.** Examine the rim-only component of a fixed rim vertex. It has length \(\ell<n\) exactly if its two bounding rim edges are deleted and its \(\ell-1\) internal edges are retained. There are precisely \(\ell\) positions for the fixed vertex within such a component, so the probability is \(\ell\delta^2(1-\delta)^{\ell-1}\). The entire rim is one connected component if and only if at most one rim edge is deleted; this has probability \((1-\delta)^n+n\delta(1-\delta)^{n-1}\). These cases partition probability one. Given a rim component of \(\ell\) vertices, it fails to reach the hub precisely when all its \(\ell\) spokes are absent, with conditional probability \((1-q)^\ell\). Rotational symmetry and conditioning produce the finite formula. The hub is disconnected from every rim vertex precisely when every spoke is absent, proving the finite zero atom.

**2. The limiting random variable.** Mark each rim edge position \(j/n\) as a cut if that edge is deleted and mark each rim vertex position \(j/n\) as a spoke if its spoke is retained. The two point processes are independent Bernoulli lattices with intensities \(a/n\) and \(b/n\), respectively. Their joint Laplace functionals converge to those of independent homogeneous Poisson point processes on the circle, so the joint point processes converge weakly. Almost surely the limiting processes have finitely many points and no coincident cut/spoke positions. On that full-probability set, the functional summing lengths of cut-arcs containing spoke marks is continuous under convergence of the finite marked point configurations. The mapping theorem gives \(H_n\Rightarrow H_{a,b}\), including the cases with zero or one cut. Boundedness implies convergence of all fixed nonnegative integer moments.

**3. Zero and full-connectivity atoms.** Absence of all spoke marks has probability \(e^{-b}\); conversely any present spoke mark connects its rim site to the hub, so \(H_{a,b}=0\) if and only if there are no spoke marks. For full connectivity, condition on the superposed cut/spoke process. If its total number of points is \(m\ge1\), the ordered cyclic label sequence must contain at least one spoke label \(S\), with no two consecutive cut labels \(C\), including the cyclic wraparound. This is equivalent to every component between consecutive cuts containing a spoke. Assign weights \(b\) to \(S\) and \(a\) to \(C\). The total weight of permitted cyclic words of length \(m\) is \(\operatorname{tr}(M^m)\) for

\[
M=\begin{pmatrix}b&a\\b&0\end{pmatrix}.
\]

The term with \(m=1\) correctly includes one spoke and excludes one cut. Poisson superposition assigns each ordered word the factor \(e^{-(a+b)}/m!\). Thus

\[
\Pr(H_{a,b}=1)
=e^{-(a+b)}\sum_{m\ge1}\frac{\operatorname{tr}(M^m)}{m!}
=e^{-(a+b)}(\operatorname{tr}e^M-2).
\]

The eigenvalues of \(M\) are \(\lambda_+\) and \(\lambda_-\), proving the stated formula. The event of exactly two cuts and at least one spoke in precisely one of the two resulting arcs has positive probability for every \(a,b>0\) and satisfies \(0<H_{a,b}<1\).

**4. Mean via the root arc.** Pick a deterministic point on the circle, or equivalently an independent uniform point by stationarity. Let \(L\) be the length of the rim component containing it. If there are zero or one cuts, then \(L=1\), an event of probability \((1+a)e^{-a}\). Otherwise the distances to the first cuts clockwise and anticlockwise are exponentially distributed on the relevant no-cut arcs. For \(0<\ell<1\), integrating over the possible location of the root in its cut interval yields the density

\[
\Pr(L\in d\ell)=a^2\ell e^{-a\ell}\,d\ell,
\quad 0<\ell<1.
\]

Conditional on \(L=\ell\), the probability of no spoke mark in its arc is \(e^{-b\ell}\). By exchangeability and Fubini, \(\mathbb E H_{a,b}=1-\mathbb E[e^{-bL}]\). Therefore

\[
\mathbb EH_{a,b}=1-(1+a)e^{-(a+b)}
-a^2\int_0^1 \ell e^{-(a+b)\ell}\,d\ell,
\]

and evaluation of the integral gives the displayed mean.

## Verification

Run the self-contained standard-library script `python3 wheel_checker.py`. Its independent checks enumerate all retained-edge states of wheels with \(3\le n\le7\), using exact rational weights for two nontrivial parameter pairs, and compare the computed mean and zero atom with the formulas. It also checks the cyclic-word transfer-matrix identity for lengths through eleven and three distinct rational rate pairs; a truncated matrix-exponential series is compared to the closed boundary-atom expression. A numerical quadrature diagnostic independently checks the size-biased arc-length formula. The script reports 91 passing assertions/diagnostics. Computations are not substitutes for the all-size and infinite-limit arguments above.

## Relationship to prior work

Mann, Smith, Mitchell and Dobson (2020) derive generating-function descriptions of bond percolation in randomly clustered networks with cycle and clique motifs; Mann and collaborators (2021) derive exact equations for homogeneous higher-order cycles. Those works concern giant components in random motif ensembles rather than a single growing wheel whose rim and spoke retention probabilities approach opposite extremes. Allard and colleagues (2012, 2015) give general finite-graph percolation recurrences and broad random-network methods, so the *ability to compute an individual finite wheel's component distribution recursively* is not claimed as new. Standard circle-spacing and Poisson-process convergence ideas are also established. The asserted contribution is the concrete two-parameter critical window, explicit nondegenerate hub-mass law, its two boundary atoms, and finite-size and limiting mean identities together. The ordinary one-parameter wheel reliability polynomial concerns the probability that the whole graph remains connected under a common edge-retention probability; it does not directly state this two-rate scaling law.

## Limitations

The theorem does not concern the largest percolated component unless that component includes the hub. It treats a wheel with uniform probabilities within each edge type, and fixed positive scaling parameters; it does not classify other scalings or arbitrary graphs. The distribution on the interior \((0,1)\) is specified constructively but no closed-form density there is asserted. Prior-art comparisons were bounded; independent historical-priority confirmation and independent mathematical audit have not been performed.

## References

- P. Mann, V. A. Smith, J. B. O. Mitchell and S. Dobson, *Percolation in random graphs with higher-order clustering*, first posted June 11, 2020, https://arxiv.org/abs/2006.06744 .
- P. Mann, V. A. Smith, J. Mitchell, C. Jefferson and S. Dobson, *An exact formula for percolation on higher-order cycles*, first posted February 18, 2021, https://arxiv.org/abs/2102.09261 .
- A. Allard, L. Hébert-Dufresne, P.-A. Noël, V. Marceau and L. J. Dubé, *Exact solution of bond percolation on small arbitrary graphs* (2012), https://arxiv.org/abs/1201.4369 .
- A. Allard, L. Hébert-Dufresne, J.-G. Young and L. J. Dubé, *General and exact approach to percolation on random graphs* (2015), https://arxiv.org/abs/1509.01207 .
- *Reliability Polynomial*, Wolfram MathWorld, https://mathworld.wolfram.com/ReliabilityPolynomial.html (background on single-parameter wheel reliability).
