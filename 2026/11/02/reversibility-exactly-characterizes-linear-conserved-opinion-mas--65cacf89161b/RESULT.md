# Reversibility exactly characterizes linear conserved opinion mass under confirmation bias

## Finding

For the synchronous confirmation-bias update of Alvim, Amorim, Knight, Quintero, and Valencia, a linear opinion statistic \(L_c(x)=\sum_i c_i x_i\) is conserved for **every** opinion vector \(x\in[0,1]^n\) if and only if its coefficients obey the pairwise weighted detailed-balance equations
\[
\frac{c_i I_{ji}}{d_i}=\frac{c_j I_{ij}}{d_j}\quad\text{for every }i\ne j.
\]
Here \(I_{ji}\) denotes the influence from agent \(j\) to agent \(i\), and \(d_i\) counts the agents with positive influence on \(i\), including \(i\). For a strongly connected graph, a nonzero such statistic exists precisely when the directed influence graph is bidirected and its edge-weight ratios satisfy the multiplicative cycle criterion. When it exists, the invariant space is one-dimensional and its generator has strictly positive coefficients.

Consequently, any connected reciprocal (undirected but not necessarily regular) influence network converges from any initial configuration with at least one non-extreme opinion to the **degree-weighted initial mean**, not in general the arithmetic mean. A strongly connected, balanced, regular three-agent influence network is exhibited below for which *no nonzero constant-coefficient linear opinion statistic is conserved*, although its classical DeGroot update conserves the ordinary mean. Under the reversible hypothesis, the variance also has an explicit geometric contraction bound once the opinion range is strictly smaller than one.

## Assumptions and scope

Fix an integer \(n\ge2\), an influence matrix \(I\in[0,1]^{n\times n}\) with \(I_{ii}=1\), and \(d_i=\#\{j:I_{ji}>0\}\). Define the simultaneous map \(F:[0,1]^n\to[0,1]^n\) by
\[
F_i(x)=x_i+\frac{1}{d_i}\sum_{j=1}^n I_{ji}(1-|x_j-x_i|)(x_j-x_i).
\]
An influence arc \(j\to i\) exists exactly when \(I_{ji}>0\). The word *strongly connected* refers to these directed arcs. A **linear invariant** means a fixed vector \(c\in\mathbb R^n\) for which \(\sum_i c_iF_i(x)=\sum_i c_ix_i\) for every \(x\in[0,1]^n\); this is stronger than conservation along a single trajectory. Reversibility refers to the normalized influence matrix \(W_{ij}=I_{ji}/d_i\), not necessarily to the raw matrix \(I\).

## Proof

**1. Full if-and-only-if criterion.** Write \(g(s)=s(1-|s|)\) and \(a_{ij}=c_iI_{ji}/d_i-c_jI_{ij}/d_j\). Antisymmetry gives the exact identity
\[
L_c(F(x))-L_c(x)=\sum_{i<j}a_{ij}g(x_j-x_i).
\]
When all \(a_{ij}=0\), the right side vanishes. Conversely, suppose it vanishes on all \(x\in[0,1]^n\). In the nonempty open chamber \(0<x_1<\cdots<x_n<1\), each term is the quadratic polynomial \(a_{ij}[(x_j-x_i)-(x_j-x_i)^2]\). Its mixed derivative with respect to \(x_i\) and \(x_j\), for \(i<j\), equals \(2a_{ij}\); all other pair terms have vanishing corresponding mixed derivative. The polynomial is identically zero, so every \(a_{ij}=0\). Thus the pairwise equations are necessary **and** sufficient. This step does not assume connectedness or positivity of \(c\).

**2. Strong connectivity and cycle criterion.** If the support is strongly connected and some coefficient \(c_i=0\), then every arc \(i\to j\) forces \(c_j=0\) by the pairwise equation. Propagation along directed paths forces \(c=0\). If a nonzero solution exists, every coefficient is therefore nonzero; every directed arc must have a reverse arc, and each bidirected edge forces \(c_i\) and \(c_j\) to have the same sign. Hence a generator \(c>0\) exists and is unique up to scale. Put \(h_i=c_i/d_i\). The edge equations become
\[
h_iI_{ji}=h_jI_{ij}.
\]
Choose a root and propagate \(h_j/h_i=I_{ji}/I_{ij}\) along a spanning tree. Positive values are path-independent exactly when every undirected support cycle has product of ratios equal to one; this is the multiplicative cycle criterion. In particular, when \(I_{ij}=I_{ji}\) on every edge, \(h\) is constant and \(c_i\) is proportional to \(d_i\).

**3. Exact consensus and quantitative dissipation.** Suppose the support is strongly connected and admits \(c>0\). Define \(C=\sum_i c_i\) and \(m=C^{-1}\sum_i c_ix_i(0)\). With \(\beta_{ij}(x)=1-|x_j-x_i|\), let
\[
P_{ij}(x)=\frac{I_{ji}\beta_{ij}(x)}{d_i}\quad(i\ne j),\qquad
P_{ii}(x)=1-\sum_{j\ne i}P_{ij}(x).
\]
Each row of \(P(x)\) sums to one, every entry is nonnegative, and \(P_{ii}(x)\ge1/d_i>0\). The update is \(F(x)=P(x)x\). Detailed balance gives \(c_iP_{ij}(x)=c_jP_{ji}(x)\), hence \(\sum_i c_iP_{ij}(x)=c_j\). The mean \(m\) remains invariant.

Set \(V(x)=\sum_i c_i(x_i-m)^2\). Direct expansion, using column stationarity, proves the exact Jensen identity
\[
V(x)-V(F(x))
=\sum_i c_i\sum_{j<k}P_{ij}(x)P_{ik}(x)(x_j-x_k)^2.
\]
If \(r=\max_i x_i(0)-\min_i x_i(0)<1\), convexity of each update ensures every later opinion range is at most \(r\); put \(\delta=1-r>0\). For every bidirected support edge \(\{i,j\}\), set \(w_{ij}=c_iI_{ji}/d_i=c_jI_{ij}/d_j>0\). The Jensen identity, retaining only the pairs \(\{i,j\}\) in rows \(i\) and \(j\), yields
\[
V(F(x))\le V(x)-\delta\sum_{i<j}w_{ij}
\left(\frac1{d_i}+\frac1{d_j}\right)(x_i-x_j)^2.
\]
Define the graph-specific positive constant
\[
\Lambda=\min_{\substack{z\in\mathbb R^n\setminus\{0\}\\\sum_i c_iz_i=0}}
\frac{\sum_{i<j}w_{ij}(d_i^{-1}+d_j^{-1})(z_i-z_j)^2}{\sum_i c_iz_i^2}>0.
\]
Connectedness proves strict positivity. We therefore obtain \(V(x(t))\le(1-\delta\Lambda)^t V(x(0))\) for every integer \(t\ge0\) whenever \(r<1\), with \(0\le1-\delta\Lambda<1\). This proves geometric convergence to the conserved weighted mean.

For completeness, suppose the initial vector has at least one component in \((0,1)\), but its range is one. An interior component remains interior because \(P_{ii}>0\); every adjacent component becomes interior at the next iteration because the influence in both directions is positive and \(0<\beta_{ij}\) when one endpoint is interior. Thus interior opinions spread across the connected bidirected support within its diameter, after which the range is strictly less than one. The same convergence proof then applies. In contrast, every \(\{0,1\}\)-valued initial vector is fixed: equal opinions have zero difference and opposite extremes have zero bias. No claim of universal consensus is made for these radical configurations.

**4. Sharp obstruction despite balancing.** Let the diagonal entries of \(I\) be one and take
\[
I=\begin{pmatrix}
1&1&1/2\\
1/2&1&1\\
1&1/2&1
\end{pmatrix}.
\]
All in-degrees are three, and all incoming and outgoing influence totals are \(5/2\), so this is a regular, balanced, strongly connected, bidirected influence graph. Yet the oriented three-cycle has product \(1\) against reverse product \(1/8\). The cycle criterion rules out any nonzero linear invariant. From \(x=(0,1/3,2/3)\), one update produces \(F(x)=(1/9,8/27,5/9)\), changing the opinion sum from \(1\) to \(26/27\), and the mean by \(-1/81\). Replacing the confirmation-bias factor by one instead would conserve the arithmetic mean because the influence graph is balanced and regular.

**5. Irregular reciprocal example.** For the unweighted three-vertex path with self-influences, \(d=(2,3,2)\). Every nonradical initial state converges to \((2x_1(0)+3x_2(0)+2x_3(0))/7\). In particular, from \((0,0,1/2)\), the consensus is \(1/7\), whereas the ordinary initial mean is \(1/6\).

## Verification

The accompanying independent-of-floating-point script `verify.py`, using Python standard-library rational arithmetic, checks the normalization, pairwise balance equations, exact conserved masses across all \(125\) four-grid configurations on a reciprocal three-vertex path and all \(625\) on an asymmetric reversible four-vertex path. It also verifies the mixed second-difference coefficient identity on a nonreversible triangle and checks the exact rational drift \(-1/27\) in the sum and the conflicting cycle products \(1\) and \(1/8\). The finite checks corroborate, but do not replace, the universal algebraic proof. Run `python verify.py` from the extracted folder.

## Relationship to prior work

Alvim and colleagues introduced the exact discrete-time confirmation-bias update in arXiv:2104.11538, later developed in arXiv:2112.09542; their consensus-value theorem covers regular reciprocal networks. Mangesius, Delvenne, and Mitter (arXiv:1508.00237, Theorem 1) established a weighted average under *assumed* detailed balance for a broader **continuous-time** nonlinear graph differential equation. Accordingly, weighted-mean sufficiency and reversible network mechanisms are pre-existing knowledge. The distinct statement here is a **necessity-and-sufficiency characterization of all fixed linear invariants for the exact discrete-time confirmation-bias map**, with a cycle obstruction, irregular-graph consensus selection, an exact discrete Jensen bound, and a balanced regular counterexample showing why reversibility cannot simply be weakened to balance. This is not a claim of inventing weighted consensus or detailed balance.

## Limitations

The invariant classification requires invariance for every configuration, not merely a particular orbit; no claim excludes nonlinear or trajectory-dependent conserved quantities on nonreversible networks. The convergence and geometric bound apply to strongly connected reversible influence networks, with a nonradical initial coordinate; arbitrary all-radical initial data can be frozen without consensus. The rate \(\Lambda\) depends on the graph and need not be optimal. The model assumes static influences, synchronous updates, self-influence one, and the precise \(1-|x_j-x_i|\) bias. No stochastic, noisy, time-varying, multidimensional or asynchronous extension is claimed. An equivalent if-and-only-if criterion in unindexed nonlinear-consensus literature remains a bibliographic risk.

## References

1. M. S. Alvim, B. Amorim, S. Knight, S. Quintero, F. Valencia, *A Multi-Agent Model for Polarization under Confirmation Bias in Social Networks*, arXiv:2104.11538 (first public 2021-04-23), https://arxiv.org/abs/2104.11538.
2. M. S. Alvim et al., *A Formal Model for Polarization under Confirmation Bias in Social Networks*, arXiv:2112.09542, Definition of the update and Theorem 20, https://arxiv.org/html/2112.09542.
3. H. Mangesius, J.-C. Delvenne, S. K. Mitter, *Gradient and Passive Circuit Structure in a Class of Non-linear Dynamics on a Graph*, arXiv:1508.00237, Theorem 1, https://arxiv.org/pdf/1508.00237.
4. M. S. Alvim, A. Gaspar da Silva, S. Knight, F. Valencia, *A Multi-Agent Model for Opinion Evolution under Cognitive Biases*, arXiv:2402.17615, https://arxiv.org/abs/2402.17615 (different update normalization and hypotheses).
