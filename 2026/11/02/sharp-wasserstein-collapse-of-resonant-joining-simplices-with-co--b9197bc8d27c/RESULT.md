# Sharp Wasserstein collapse of resonant joining simplices with continuum limit-set stations

## Finding
For every irrational \(\alpha\in\mathbb T=\mathbb R/\mathbb Z\), every integer \(q\ge1\), and every integer \(a\) coprime to \(q\), consider the smooth torus translation
\[
F_{\alpha,a/q}(x,y)=(x+\alpha,\ y+\alpha+a/q)\pmod1.
\]
Let \(d_{\mathbb T}(s,t)=\min_{k\in\mathbb Z}|s-t-k|\) and equip \(\mathbb T^2\) with \(d((x,y),(x',y'))=d_{\mathbb T}(x,x')+d_{\mathbb T}(y,y')\). Define the quotient circle \(Q_q=\mathbb T/(q^{-1}\mathbb Z/\mathbb Z)\), equipped with its quotient metric
\[
\rho_q([c],[c'])=\min_{0\le j<q}d_{\mathbb T}(c,c'+j/q).
\]
For \([c]\in Q_q\), let \(C_{[c]}=\{(x,x+c+j/q):x\in\mathbb T,\ 0\le j<q\}\) and define the Haar orbit-closure probability
\[
\nu_{[c]}=\frac1q\sum_{j=0}^{q-1}\left(x\mapsto(x,x+c+j/q)\right)_\#m,
\]
where \(m\) is normalized Haar measure on \(\mathbb T\). Then the following assertions hold simultaneously.

First, for every \(z\in C_{[c]}\), both its forward and backward limit sets equal \(C_{[c]}\), and \(C_{[c]}\) is the unique limit-set station containing \(z\). Thus the station/self-bridge data have continuum many distinct triples \((C_{[c]},C_{[c]},C_{[c]})\).

Second, the entire simplex \(\mathcal I_q\) of invariant Borel probability measures is exactly \(\{\nu_\eta=\int_{Q_q}\nu_{[c]}\,d\eta([c]):\eta\in\mathcal P(Q_q)\}\). All these invariant measures are joinings of the two unique Haar factor measures. The extreme points are precisely \(\nu_{[c]}\).

Third, for every \(1\le p\le\infty\), the parametrization is an affine isometry:
\[
W_p^{d}(\nu_\eta,\nu_\kappa)=W_p^{\rho_q}(\eta,\kappa),\qquad\eta,\kappa\in\mathcal P(Q_q).
\]
If \(m_2=m\otimes m\), then the sharp metric radius of the entire invariant-joining simplex about \(m_2\) is
\[
\max_{\nu\in\mathcal I_q}W_p^{d}(\nu,m_2)=
\begin{cases}\displaystyle\frac{1}{2q(p+1)^{1/p}},&1\le p<\infty,\\
\displaystyle\frac1{2q},&p=\infty.
\end{cases}
\]
Every extreme point attains the maximum. In particular \(\mathcal I_q\) has continuum many extreme points for every \(q\), yet its Hausdorff \(W_p\)-distance to the singleton \(\{m_2\}\) is exactly the displayed quantity and tends to zero as \(q\to\infty\). For the maps with relative shifts \(1/q\), which converge smoothly to the equal-frequency map as \(q\to\infty\), this also proves failure of lower semicontinuity of the invariant-probability simplex: all their invariant measures tend uniformly to \(m_2\), while the limit map additionally admits the diagonal Haar joining at the fixed strictly positive distance obtained by setting \(q=1\) in the same formula.

Finally, if \(1,\alpha,\beta\) are rationally independent, the product \((x,y)\mapsto(x+\alpha,y+\beta)\) is uniquely ergodic and has only one forward/backward limit-set station, the full torus, even though each factor rotation has the same one-station self-bridge data as the factors in the rational-shift case. The product station data therefore cannot be reconstructed from the **abstract** station/bridge data of the factors alone; this does not assert a failure of functoriality under semiconjugacies.

## Assumptions and scope
Here \(q\) is a positive integer and \(\gcd(a,q)=1\), including \(q=1\), for which the zero rational shift is permitted. The irrationality of \(\alpha\) is essential. Invariant measures are arbitrary Borel probabilities on the compact torus, and \(W_p\) is the standard optimal-transport metric for the stated intrinsic geodesic costs (essential-supremum cost at \(p=\infty\)). The quotient \(Q_q\) has circumference \(1/q\). A station means a subset occurring as an \(\alpha\)- or \(\omega\)-limit set; a self-bridge is a connection with the same incoming and outgoing stations, in the sense of the motivating limit-network construction. No claim is made about a categorical product object.

## Proof
**1. Orbit closures and stations.** Set \(c=y-x\pmod1\). The coordinate change \((x,y)\leftrightarrow(x,c)\) conjugates \(F_{\alpha,a/q}\) to \((x,c)\mapsto(x+\alpha,c+a/q)\). Its \(q\)-fold iterate fixes \(c\) and rotates \(x\) through \(q\alpha\), which is irrational. Consequently each residue class modulo \(q\) is dense on its circle and the full positive and negative orbits are dense in the union of the \(q\) circles indexed by \([c]\). These sets are pairwise disjoint for different \([c]\), and exactly the claimed \(C_{[c]}\). Since every orbit point lies in its own orbit closure, the smallest limit set containing it is the same \(C_{[c]}\), yielding the indicated self-bridge.

**2. All invariant measures.** Let \(\nu\) be \(F_{\alpha,a/q}\)-invariant and transfer it to \((x,c)\) coordinates. Invariance under the \(q\)-fold map \((x,c)\mapsto(x+q\alpha,c)\), followed by disintegration over \(c\), forces almost every conditional law in \(x\) to be invariant under an irrational rotation. By uniqueness of Haar measure for that rotation, each conditional equals \(m\). Thus \(\nu=m\otimes\sigma\) in \((x,c)\) coordinates, where \(\sigma\in\mathcal P(\mathbb T)\) is invariant under the order-\(q\) rotation \(c\mapsto c+a/q\). Since \(a\) is coprime to \(q\), \(\sigma\) is exactly a mixture of uniform probabilities on the \(q\)-point cosets \(c+(q^{-1}\mathbb Z/\mathbb Z)\). The mixing measure is uniquely \(\eta=\pi_\#\sigma\) on \(Q_q\), where \(\pi(c)=[c]\). Conversely every such mixture is invariant. Since each marginal is invariant under an irrational circle rotation, both are Haar. The ergodic components are precisely the \(q\)-circle Haar probabilities \(\nu_{[c]}\), so their measures are exactly the extreme points.

**3. Exact transport isometry.** Let \(\Pi:\mathbb T^2\to Q_q\) be \(\Pi(x,y)=[y-x]\). The triangle inequality on \(\mathbb T\) gives
\[
\rho_q(\Pi(x,y),\Pi(x',y'))\le d_{\mathbb T}(x,x')+d_{\mathbb T}(y,y')=d((x,y),(x',y'));
\]
thus \(\Pi\) is \(1\)-Lipschitz and \(\Pi_\#\nu_\eta=\eta\). By pushing forward any transport plan we obtain the lower bound \(W_p^{\rho_q}(\eta,\kappa)\le W_p^d(\nu_\eta,\nu_\kappa)\), also for \(p=\infty\).

For the reverse inequality take any coupling \(\gamma\) of \(\eta,\kappa\) on \(Q_q^2\). On each pair \(([c],[c'])\), choose representatives whose relative angular displacement has magnitude \(\rho_q([c],[c'])\); compactness and a fixed deterministic tie-breaking rule supply a Borel choice. Sample \(x\) with law \(m\), sample \(j\) uniformly from \(\{0,\dots,q-1\}\), and couple the states \((x,x+c+j/q)\) and \((x,x+c'+j/q)\). Their conditional marginals are exactly \(\nu_{[c]}\) and \(\nu_{[c']}\), and their transport cost is exactly \(\rho_q([c],[c'])\). Integrating this construction against \(\gamma\), then taking an optimal \(\gamma\), proves the opposite inequality for all \(p\in[1,\infty]\).

**4. Sharp radius.** The product Haar measure \(m_2\) corresponds to normalized Haar \(m_{Q_q}\) on the quotient: in \((x,c)\) coordinates both \(x\) and \(c\) are independent uniform angles. For a Dirac mass \(\delta_{[c]}\), the only coupling with \(m_{Q_q}\) transports the point to the uniform quotient circle. As its circumference is \(1/q\),
\[
W_p^{\rho_q}(\delta_{[c]},m_{Q_q})^p
= q\int_{-1/(2q)}^{1/(2q)}|t|^p\,dt
=\frac{1}{(p+1)(2q)^p}
\]
for finite \(p\); the essential maximum equals \(1/(2q)\). Hence every \(\nu_{[c]}\) has the asserted distance. For general \(\nu_\eta\), mix the optimal point-to-Haar transport couplings over \(\eta\); the resulting transport has the same bounded \(p\)-cost, so the displayed upper bound is sharp. Because \(m_2\in\mathcal I_q\), the same supremum is the Hausdorff distance of \(\mathcal I_q\) from \(\{m_2\}\).

**5. Failure of factor-only reconstruction.** Each irrational circle rotation is minimal and uniquely ergodic; its only limit-set station is the whole circle. For rational shifts, Steps 1–2 yield continuum many stations in the product. If \(1,\alpha,\beta\) are rationally independent, Weyl equidistribution/Kronecker's theorem gives dense equidistributed positive and negative orbits in \(\mathbb T^2\) and uniqueness of \(m_2\); the only station is \(\mathbb T^2\). Therefore the two products have different station-and-self-bridge data despite abstractly identical one-station factor data. The examples concern the data retained by the factors, not whether a functor preserves morphism composition.

## Verification
Every proof step above is analytical and holds for all allowed \(q\), \(\alpha\), probabilities and \(p\). The independent standalone script `verify.py` checks exact rational moment identities and discrete ring approximations to the sharp radii for multiple denominators. Its finite computations are corroboration only; no infinite quantifier is inferred from tests. One can reproduce with `python verify.py` using Python's standard library.

## Relationship to prior work
Das, *Network of limit sets in dynamical systems* (arXiv:2610.34265v1, first public 2026-10-25), introduces stations, bridges and functoriality under semiconjugacy; it does not state the rational-resonance station family, exact joining geometry or sharp transport collapse above. Das and Suda, *Joinings in Markov categories* (arXiv:2609.10912v2), explain general joining composition and metric enrichment but do not supply this joint station/transport classification. De la Rue, *An introduction to joinings in ergodic theory* (arXiv:math/0507429v2), already explains graph-supported joinings and the classical non-disjointness of an irrational rotation from itself; these antecedents are not claimed as new. Standard Kronecker equidistribution, Haar uniqueness, and elementary optimal transport are used as known tools and are not claimed as new. The contribution is the combined exact station decomposition, the **all-order isometry** of the full joining simplex, and its sharp \(q^{-1}\) metric-collapse law despite persistent continuum station multiplicity.

## Limitations
The station separation is qualitative, whereas the stated metric collapse uses the particular \(\ell^1\) circle-product distance; other costs may have different exact constants. This is a classification of rigid torus rotations with rational relative phase, not of general coupled nonlinear flows or arbitrary joinings. The rationally independent comparison uses an additional arithmetic hypothesis. Neither the identity of stationary sets nor the quantitative result implies a failure of the motivating paper's functoriality theorem, and there is no independent external audit. Historical priority against unindexed specialized treatments of isometric quotient transport remains open.

## References
1. S. Das, *Network of limit sets in dynamical systems*, arXiv:2610.34265v1 (2026), https://arxiv.org/html/2610.34265v1 (publicly submitted 2026-10-25).
2. S. Das and T. Suda, *Joinings in Markov categories*, arXiv:2609.10912v2 (2026), https://arxiv.org/html/2609.10912v2 (first public 2026-09-09).
3. T. de la Rue, *An introduction to joinings in ergodic theory*, arXiv:math/0507429v2 (2005), https://arxiv.org/pdf/math/0507429 (especially Section 2.2 on graph joinings).
4. Kronecker's density theorem and Weyl's equidistribution criterion for torus rotations (classical); Haar uniqueness and the elementary coupling definition of Wasserstein distance (classical).
