# Lipschitz foliations alone force minimality for irrational twist maps
## Finding
Let \(f\in\mathrm{Diff}_{\mathrm{tw}}^1(\mathbf T^2)\) be an area-preserving twist diffeomorphism whose vertical rotation set is the singleton \(\{\alpha\}\), with \(\alpha\notin\mathbf Q\). Let \(\mathcal F_G=\{\operatorname{Graph}(\phi_t)\}_{t\in\mathbf T^1}\) be the invariant foliation from Addas-Zanata and Lazaro Aguirre, reparametrized as in their Section 3.3.1 so that \(\phi_t(0)=t\).

If \(\mathcal F_G\) is a Lipschitz foliation in their Definition (8), then \(f\) is minimal. Thus the additional hypothesis in their Theorem C that the induced leaf dynamics be bi-Lipschitz conjugate to \(R_\alpha\) is redundant.

More precisely, if \(P:\mathbf T^2\to\mathbf T^1\) denotes projection along leaves and \(\psi:\mathbf T^1\to\mathbf T^1\) is the induced leaf map, then the probability
\[
\nu=P_*\operatorname{Leb}_{\mathbf T^2}
\]
is \(\psi\)-invariant. If \(K_{\mathrm{Fol}}\) is the transverse Lipschitz constant, then every oriented arc \(I\) short enough to admit an ordered lift satisfies
\[
K_{\mathrm{Fol}}^{-1}|I|\le \nu(I)\le K_{\mathrm{Fol}}|I|.
\]
Consequently the distribution coordinate of \(\nu\) is bi-Lipschitz and conjugates \(\psi\) to the irrational rotation of angle \(\alpha\).

## Assumptions and scope
The assumptions are exactly those of Theorem A of arXiv:2609.27102v1 together with the one remaining regularity condition that the invariant foliation itself is Lipschitz in the transverse sense of Definition (8). The result does not claim that the invariant foliation produced by Theorem A is automatically Lipschitz as a foliation; Theorem A only supplies a foliation whose individual graph leaves have a uniform Lipschitz bound.

The leaf parameter is the intersection with the transversal \(V_0=\{0\}\times\mathbf T^1\), so \(\phi_t(0)=t\). The induced map \(\psi\) is the orientation-preserving circle homeomorphism defined by \(f(\operatorname{Graph}(\phi_t))=\operatorname{Graph}(\phi_{\psi(t)})\). Proposition 3.16 of the source proves that \(\psi\) is topologically conjugate to \(R_\alpha\), and Lemma 3.17 proves that \(\psi\) itself is bi-Lipschitz when the foliation is Lipschitz.

## Proof
Let \(P:\mathbf T^2\to\mathbf T^1\) be the leaf projection from Section 3.3.1 of the source: \(P(z)=t\) exactly when \(z\in\operatorname{Graph}(\phi_t)\). Invariance of the foliation gives the equivariance identity
\[
P\circ f=\psi\circ P.
\]
Since \(f\) preserves normalized Lebesgue area, the pushforward probability \(\nu=P_*\operatorname{Leb}_{\mathbf T^2}\) satisfies \(\psi_*\nu=\nu\).

Now take an oriented arc \(I=[s,t]\subset\mathbf T^1\) short enough that \(s<t\) can be chosen in one lift to \(\mathbb R\). Choose the corresponding lifted graph functions \(\widehat\phi_s\) and \(\widehat\phi_t\) with \(\widehat\phi_s(0)=s\) and \(\widehat\phi_t(0)=t\). Because distinct leaves are disjoint and ordered, \(\widehat\phi_t(x)-\widehat\phi_s(x)>0\) for every \(x\). The Lipschitz-foliation condition, with \(x'=0\), gives
\[
\frac{t-s}{K_{\mathrm{Fol}}}
\le \widehat\phi_t(x)-\widehat\phi_s(x)
\le K_{\mathrm{Fol}}(t-s)
\qquad\text{for every }x\in\mathbf T^1.
\]
The set \(P^{-1}(I)\), up to its two zero-area boundary leaves, is exactly the strip between these two graphs. Fubini's theorem therefore yields
\[
\nu(I)=\int_0^1
\bigl(\widehat\phi_t(x)-\widehat\phi_s(x)\bigr)\,dx,
\]
and hence
\[
K_{\mathrm{Fol}}^{-1}|I|\le\nu(I)\le K_{\mathrm{Fol}}|I|.
\]

Lift \(\nu\) periodically to a measure on \(\mathbb R\), and define the increasing lift \(H:\mathbb R\to\mathbb R\) by \(H(0)=0\), \(H(x+1)=H(x)+1\), and
\[
H(t)-H(s)=\nu([s,t])
\]
for \(s<t\) within one fundamental lift, extended by periodicity. The preceding two-sided arc estimate shows that both \(H\) and \(H^{-1}\) are Lipschitz.

Let \(\Psi:\mathbb R\to\mathbb R\) be an increasing lift of \(\psi\). Since \(\nu\) is \(\psi\)-invariant, the \(\nu\)-mass of every lifted interval is preserved. Thus for all \(s<t\),
\[
H(\Psi(t))-H(\Psi(s))=H(t)-H(s).
\]
It follows that \(H(\Psi(t))-H(t)\) is constant in \(t\). Therefore the circle homeomorphism induced by \(H\) conjugates \(\psi\) to a rigid rotation. Rotation number is invariant under orientation-preserving conjugacy, and Proposition 3.16 identifies the rotation number of \(\psi\) with \(\alpha\); hence the rigid rotation is \(R_\alpha\). The conjugacy is bi-Lipschitz by the two-sided arc estimate.

All hypotheses of Theorem C are now satisfied, so \(f\) is minimal.

## Verification
The proof uses only the source's leaf parametrization, its Lipschitz-foliation inequality, area preservation, Fubini's theorem, and elementary circle dynamics. The critical point is that transverse Lipschitz control converts area of a strip between two leaves into a quantity uniformly comparable with the distance between their leaf parameters. That comparison turns the invariant transverse marginal into a bi-Lipschitz coordinate.

Boundary cases were checked as follows. Arcs crossing the chosen cut are handled by periodic lifts. Boundary leaves have two-dimensional Lebesgue measure zero because they are Lipschitz graphs. No differentiability of the leaf parameter is used. The argument does not assert that the foliation from Theorem A is automatically Lipschitz in the transverse sense.

## Relationship to prior work
Addas-Zanata and Lazaro Aguirre prove in Theorem C of arXiv:2609.27102v1 that minimality follows when the invariant foliation is Lipschitz and the induced leaf map is bi-Lipschitz conjugate to \(R_\alpha\). Their Lemma 3.17 proves that the induced leaf map itself is bi-Lipschitz under the foliation hypothesis, but the paper explicitly keeps bi-Lipschitz regularity of the conjugacy as a separate assumption. The invariant transverse-area marginal above supplies that missing regularity.

Arnaud and Zavidovique, arXiv:2011.01546, prove Arnol'd--Liouville coordinate results for symplectic twist maps of the annulus in the different integrable regime where every leaf is individually invariant. Their result does not cover the present torus Dehn-twist setting, where the map permutes the leaves through an irrational circle action.

Targeted searches for the source title, the removal of the conjugacy hypothesis, invariant transverse measures, and bi-Lipschitz circle conjugacies found no statement implying this theorem.

## Limitations
The conclusion still depends on the invariant foliation being Lipschitz transversely. It therefore does not settle the source's broader question of whether every area-preserving twist map with a singleton irrational vertical rotation set is minimal. The proof also uses area preservation essentially to make the transverse marginal invariant. A merely non-wandering map does not supply the same argument.

The focal preprint is recent, so a later revision or an unindexed note could contain the same observation. The comparison with older integrability results is limited to the different leafwise-invariant annulus regime described above.

## References
1. Salvador Addas-Zanata and Julian Lazaro Aguirre, *Foliations and minimality for twist maps*, arXiv:2609.27102v1, 2026. In particular Definition (8), Theorem C, Proposition 3.16, Lemma 3.17, and Lemma 3.21.
2. Marie-Claude Arnaud and Maxime Zavidovique, *Actions of symplectic homeomorphisms/diffeomorphisms on foliations by curves in dimension 2*, arXiv:2011.01546; Ergodic Theory and Dynamical Systems 43 (2023), 794--826.
