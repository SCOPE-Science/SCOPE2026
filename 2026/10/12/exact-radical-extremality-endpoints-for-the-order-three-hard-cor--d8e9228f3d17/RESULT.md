# Exact radical extremality endpoints for the order-three hard-core wand model
## Finding
For the fertile three-state hard-core model of wand type on the Cayley tree of order \(3\), consider the symmetric translation-invariant Gibbs measure \(\nu_0\) associated with the positive boundary-law solution \(z_1=z_2=z\). Khakimov and Umirzakova prove that its extremality changes at two numerically evaluated activities, reporting approximately \(0.4421534328\) and \(2.103133692\). Their proof explicitly invokes computer analysis because their closed radical expression for \(z\) is cumbersome.

Those two activities have the exact forms
\[
\widetilde\lambda=\frac{32(7\sqrt{3}-12)}{9},\qquad
\check\lambda=\frac{4(3+\sqrt{3})}{9}.
\]
Accordingly, the source theorem admits the exact reformulation
\[
\widetilde\lambda<\lambda<\check\lambda
\quad\Longrightarrow\quad
\nu_0\text{ is extremal},
\]
and
\[
0<\lambda<\widetilde\lambda\quad\text{or}\quad\lambda>\check\lambda
\quad\Longrightarrow\quad
\nu_0\text{ is non-extremal}.
\]
No assertion is made at \(\lambda=\widetilde\lambda\) or \(\lambda=\check\lambda\), because both source criteria are strict at those points.

## Assumptions and scope
The graph is the fertile three-state hard-core wand graph with allowed pairs \({0,1},{0,2},{1,1},{2,2}\), equal occupied-state activity \(\lambda>0\), and Cayley-tree order \(k=3\). The finding concerns only the symmetric translation-invariant measure \(\nu_0\) determined by \(z_1=z_2=z>0\). It does not classify the other translation-invariant or periodic Gibbs measures that may coexist, and it does not decide extremality at the two equality endpoints.

## Proof
On the symmetric branch, the source equation is
\[
z=\lambda\left(\frac{1+z}{2z}\right)^3.
\]
It is equivalent, without extracting any quartic radicals, to
\[
\lambda=\Lambda(z):=\frac{8z^4}{(1+z)^3},\qquad z>0.
\]
Moreover
\[
\frac{d}{dz}\log\Lambda(z)
=\frac4z-\frac3{1+z}
=\frac{z+4}{z(1+z)}>0,
\]
so \(\Lambda\) is strictly increasing. Since \(\Lambda(1)=1\), the sign of \(z-1\) is determined exactly by whether \(\lambda\) is below or above \(1\); the graphical Maple step used for this sign comparison is unnecessary.

For \(z<1\), the source gives \(\kappa=\gamma=1/(1+z)\). Its sufficient extremality inequality \(3\kappa\gamma<1\) is therefore
\[
\frac3{(1+z)^2}<1
\quad\Longleftrightarrow\quad
z>\sqrt3-1,
\]
while the Kesten--Stigum non-extremality inequality is the strict reverse. Thus the lower endpoint is \(z_-=\sqrt3-1\). Substitution into \(\Lambda\) gives
\[
\Lambda(z_-)
=\frac{8(\sqrt3-1)^4}{(\sqrt3)^3}
=\frac{32(7\sqrt3-12)}9
=0.44215343282539041668\ldots .
\]

For \(z>1\), the source gives \(\kappa=\gamma=z/(1+z)\). Hence its strict extremality criterion is
\[
3\left(\frac{z}{1+z}\right)^2<1
\quad\Longleftrightarrow\quad
z<\frac1{\sqrt3-1}
=\frac{\sqrt3+1}2,
\]
with the Kesten--Stigum condition giving non-extremality under the strict reverse inequality. Thus \(z_+=(\sqrt3+1)/2\), and
\[
\Lambda(z_+)
=\frac{8z_+^4}{(1+z_+)^3}
=\frac{4(3+\sqrt3)}9
=2.1031336922528343527\ldots .
\]
Strict monotonicity of \(\Lambda\) transfers these two exact \(z\)-thresholds to the stated exact activity intervals.

## Verification
The standalone verifier `verify.py` implements arithmetic in \(\mathbb Q(\sqrt3)\), checks both exact substitutions, checks the decimal brackets quoted above, and verifies the positivity of the monotonicity numerator on a representative exact rational grid. The grid is only a replay check; the infinite-domain monotonicity statement is proved analytically by \(z+4>0\) for all \(z>0\).

The source's strict inequalities leave the equality endpoints unresolved. This package therefore does not infer endpoint extremality from numerical proximity or from equality in either criterion.

## Relationship to prior work
Khakimov and Umirzakova derive the order-three wand boundary law, the transition matrix, the Kesten--Stigum non-extremality criterion, and the Martinelli--Sinclair--Weitz type sufficient extremality criterion. In their published proof, they explicitly use Maple to determine the sign of \(z-1\), and Theorem 3 records only the decimal endpoints \(0.4421534328\) and \(2.103133692\). The present calculation removes that numerical step by solving for \(\lambda\) directly as a monotone function of \(z\), and evaluates the two criterion boundaries exactly.

A later paper by Khakimov and Umirzakova studies two-periodic wand measures, gives exact periodic-measure critical values, and studies periodic-measure extremality only on the order-two tree. It does not state these order-three symmetric-measure radical endpoints. That later paper explicitly classifies the same wand three-state hard-core model under MSC 2020 \(82\mathrm{B}26\), with \(60\mathrm{K}35\) secondary.

## Limitations
The result is an exactification of a theorem-level pair of critical activities, not a new global classification of all Gibbs measures. It inherits the source's extremality and non-extremality criteria and does not strengthen them at equality. It does not address extremality of the nonsymmetric translation-invariant measures or of two-periodic measures, nor any Cayley-tree order other than \(3\). Published-record searches found no exact-radical statement for these two activities, but weakly indexed literature could still contain an equivalent algebraic simplification.

## References
1. R. M. Khakimov and K. O. Umirzakova, “Extremality of the unique translation-invariant Gibbs measure for hard-core models on the Cayley tree of order \(k=3\),” arXiv:2008.02162v1; Theoretical and Mathematical Physics 206 (2021), 97–108, DOI:10.1134/S0040577921010062.
2. R. Khakimov and K. Umirzakova, “Periodic Gibbs Measures for Three-State Hard-Core Models in the Case Wand,” Journal of Mathematical Physics, Analysis, Geometry 20 (2024), 66–81, DOI:10.15407/mag20.01.066.
3. U. A. Rozikov and R. M. Khakimov, “Gibbs measures for the fertile three-state hard core models on a Cayley tree,” Queueing Systems 81 (2015), 49–69, DOI:10.1007/s11134-015-9450-1.
