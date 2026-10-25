# Phase collapse and antipodal spectrum in conjunctions of Sturmian shifts

## Finding
Fix any irrational \(\alpha\in(0,1)\). Let \(X_\alpha\subset\{0,1\}^{\mathbb Z}\) be the two-sided Sturmian shift obtained by coding the irrational rotation \(t\mapsto t+\alpha\pmod1\) using the interval \(I=[0,\alpha)\). Define the coordinatewise conjunction factor
\[
Y_\alpha=\{(u_n v_n)_{n\in\mathbb Z}:u,v\in X_\alpha\}.
\]
For \(0\le\delta\le1/2\), let \(\nu_\delta\) be the law of the stationary binary process
\[
W_n=\mathbf1_I(T^n t)\,\mathbf1_I(T^n(t-\delta)),\qquad t\text{ Haar-uniform on }\mathbb T=\mathbb R/\mathbb Z.
\]
Then the following is a complete classification of the invariant-measure geometry of \(Y_\alpha\).

1. Every shift-ergodic Borel probability measure on \(Y_\alpha\) equals some \(\nu_\delta\). For \(\alpha<1/2\), \(\nu_\delta=\nu_{\delta'}\) precisely when either \(\delta=\delta'<\alpha\), or \(\delta,\delta'\in[\alpha,1/2]\); the latter measures all equal the Dirac measure \(\delta_{0^{\mathbb Z}}\). For \(\alpha>1/2\), \(\nu_\delta=\nu_{\delta'}\) precisely when \(\delta=\delta'\).
2. The invariant-measure simplex is affinely homeomorphic to \(\mathcal P([0,\alpha])\) when \(\alpha<1/2\), and to \(\mathcal P([0,1/2])\) when \(\alpha>1/2\). In the short-window case the endpoint of \([0,\alpha]\) corresponds to \(\delta_{0^{\mathbb Z}}\).
3. Every non-Dirac \(\nu_\delta\) has pure point, multiplicity-one measure-theoretic spectrum. Its eigenvalue group is \(\{e^{2\pi i k\alpha}:k\in\mathbb Z\}\), except when \(\alpha>1/2\) and \(\delta=1/2\), in which case the group is exactly \(\{e^{2\pi i 2k\alpha}:k\in\mathbb Z\}\). Thus precisely one nonconstant ergodic measure, at antipodal phase and only in the long-window regime, loses all odd Fourier modes.
4. The topological entropy of \(Y_\alpha\) is zero. Nevertheless it supports uncountably many ergodic invariant probabilities for every irrational \(\alpha\in(0,1)\).

The one-symbol output frequency \(\rho_\delta=\nu_\delta([1])\) is explicit:
\[
\rho_\delta=
\begin{cases}
\max(\alpha-\delta,0),&\alpha<1/2,\\
\alpha-\delta,&\alpha>1/2,\ \delta\le1-\alpha,\\
2\alpha-1,&\alpha>1/2,\ \delta\ge1-\alpha.
\end{cases}
\]
When \(\alpha>1/2\) the frequency has a nontrivial flat interval, but the measures throughout that interval remain different. They can be distinguished by an exact Fourier coefficient of their two-point correlations.

## Assumptions and scope
The rotation angle \(\alpha\) is irrational and strictly between zero and one, so it cannot equal \(1/2\). The two components have the *same* angle, and the conjunction is taken coordinatewise. Coding endpoint conventions matter for individual sequences, but not for the classified invariant probability measures. The factor is the compact shift image of the whole two-sided Sturmian product, not merely the image of nonsingular phase codings. Here \(\mathcal P(K)\) denotes the Borel probability measures on compact \(K\) with their weak-* topology. Eigenvalue groups refer to Koopman operators on the ergodic invariant measures, not to the topological spectrum of the entire nonminimal factor.

## Proof
**(1) Reduction to relative phases.** The Sturmian shift has the standard almost-one-to-one circle-rotation factor; the exceptional double codings lie over a countable union of rotation orbits. Every invariant probability on its product has each marginal equal to the uniquely ergodic Sturmian measure. The countable exceptional sets therefore have measure zero under either marginal. Almost everywhere, the product is the torus rotation \((t,s)\mapsto(t+\alpha,s+\alpha)\). Its invariant ergodic probabilities are exactly Haar probabilities on the cosets \(s-t=d\), \(d\in\mathbb T\): indeed the difference is invariant, and the restricted diagonal rotation is irrational and uniquely ergodic. Every ergodic probability on the image factor has an ergodic invariant lift through the continuous, onto factor map (take an invariant lift and an ergodic component). Therefore its law is the intersection coding of phases separated by \(d\). Interchanging the input coordinates changes \(d\) to \(-d\) without changing the output; translation invariance of Haar then permits the unique representative \(\delta=\min(d,1-d)\in[0,1/2]\).

**(2) Interval geometry and output frequencies.** After translating phase, the observation window is \(J_\delta=I\cap(I+\delta)\). For \(\alpha<1/2\), it is \([\delta,\alpha)\) if \(\delta<\alpha\) and empty otherwise. For \(\alpha>1/2\), it is \([\delta,\alpha)\) when \(\delta\le1-\alpha\), and otherwise it is the disjoint union
\[
J_\delta=[0,\alpha+\delta-1)\cup[\delta,\alpha).
\]
These identities prove the displayed frequency formula. When \(\alpha<1/2\), distinct \(\delta<\alpha\) have distinct frequencies, while every \(\delta\ge\alpha\) gives the deterministic all-zero law. When \(\alpha>1/2\), distinct \(\delta<1-\alpha\) have distinct frequencies, which exceed the plateau value \(2\alpha-1\).

**(3) Distinguishing the long-window plateau.** Let \(C_\delta(n)=\int W_0W_n\,d\nu_\delta\). Parseval and irrationality give the *exact* Bohr coefficient
\[
\lim_{N\to\infty}\frac1N\sum_{n=0}^{N-1}C_\delta(n)e^{-2\pi in\alpha}
=\left|\widehat{\mathbf1_{J_\delta}}(1)\right|^2.
\]
This identity holds because \(C_\delta(n)=\sum_{k\in\mathbb Z}|\widehat{\mathbf1_{J_\delta}}(k)|^2e^{2\pi ikn\alpha}\) and the sum converges absolutely. For \(\alpha>1/2\) and \(1-\alpha\le\delta\le1/2\), the complement of \(J_\delta\) is the union of two equal-length arcs, each of length \(1-\alpha\), whose initial points differ circularly by \(\delta\). Direct integration yields
\[
\left|\widehat{\mathbf1_{J_\delta}}(1)\right|
=\frac{2\sin(\pi(1-\alpha))}{\pi}\cos(\pi\delta).
\]
This is strictly decreasing across that entire plateau (including its endpoints). Thus its measures are pairwise distinct, including the antipodal endpoint. Frequency separates every plateau law from every law in the preceding nonflat branch.

**(4) Isomorphism and spectrum.** For any finite union \(J\) of nondegenerate intervals, let \(H(J)=\{h\in\mathbb T:\mathbf1_J(\cdot+h)=\mathbf1_J(\cdot)\text{ a.e.}\}\). The bi-infinite coding of an irrational rotation by \(\mathbf1_J\) is a measurable isomorphism from the rotation on \(\mathbb T/H(J)\): if two phases have equal full codings and avoid the countable endpoint orbits, their dense rotation orbits show that translating \(J\) by their difference leaves its indicator equal almost everywhere; conversely every stabilizer element leaves a.e. coding unchanged. For all nonempty windows here, \(H(J_\delta)\) is trivial except when \(\alpha>1/2,\delta=1/2\). In the long-window two-component case a nontrivial finite translation stabilizer would have to exchange components of equal lengths, requiring \(\alpha-\delta=\alpha+\delta-1\), i.e. \(\delta=1/2\); the half-turn then does exchange them. No single proper circular interval has nontrivial translation stabilizer, and a two-component set cannot have a stabilizer of order greater than two. The characters of \(\mathbb T/H(J)\) are precisely those integer frequencies that annihilate \(H(J)\), proving the stated eigenvalue groups and multiplicity one.

**(5) All invariant measures and entropy.** The phase-to-law map is weak-* continuous: symmetric differences between the translating finite-interval windows have length tending to zero, so every finite cylinder probability varies continuously. The identification in (2)--(3) gives a continuous injective parametrization by the compact interval \([0,\alpha]\) in the short-window case (collapsing the upper phase range to its endpoint), and by \([0,1/2]\) in the long-window case. Every invariant measure decomposes uniquely over its ergodic components, and all ergodic components have just been classified, so the resulting map from the probability measures on the parameter interval to the invariant-measure simplex is a continuous affine bijection, hence a homeomorphism. Finally, Sturmian shifts have zero topological entropy, as does their product and every shift factor; and each listed positive-length parameter interval supplies a continuum of distinct ergodic measures.

## Verification
The accompanying standalone `verify.py` uses exact rational arithmetic to test the circular-arc intersection length and first Fourier modulus across 2,980 independent rational configurations; checks exact half-turn symmetry at four long-window parameters; and compares stationary densities with 14 finite orbit averages for two irrational angles. Run `python3 verify.py` from this directory. These tests verify the formulas at sampled values only. The unrestricted classification, spectral assertion, and entropy conclusion are proved in the preceding five steps and do not depend on the samples.

## Relationship to prior work
Berstel and Vuillon, *Coding rotations on intervals* (first publicly posted 2001-06-26, arXiv:math/0106217v1), develop the general recoding of circle interval partitions by Sturmian sequences. Their Sections 4--5, including Lemmas 5.1--5.3, explicitly analyze intersections of circle intervals; that interval geometry is prior work, not claimed here. Frid and Jamet, *The number of binary rotation words* (arXiv:1302.3722v1, posted 2013-02-15), count finite rotation words and use pairs of equal-slope Sturmian codings (Section 3). Neither inspected full text states the present coordinatewise-AND invariant-measure equivalence classes, the flat-frequency-but-distinct-measures regime, or the exceptional pure-point spectral subgroup at antipodal relative phase. Standard irrational-rotation ergodic decomposition and spectral theory are inputs, not new lemmas. A previously established parity/XOR factor of the same Sturmian product has different fibres and a different phase-identification law: there the only zero-output phase is zero separation, whereas conjunction collapses an entire interval of separations when \(\alpha<1/2\).

## Limitations
This does not classify individual topological preimage fibres of the conjunction map, and singular endpoint codings can yield configurations that have zero probability under all ergodic measures considered. The proof gives a measure-theoretic classification, not a claimed topological conjugacy of the entire factor to a family of rotations. The result is specific to identical irrational angles and the canonical interval of length \(\alpha\). Its originality is assessed against the inspected sources, not all unpublished or unindexed literature; especially the interval geometry and general rotation-factor principles are established prior work. No independent external mathematical audit has been carried out.

## References
1. J. Berstel and L. Vuillon, *Coding rotations on intervals*, arXiv:math/0106217v1 (posted 2001-06-26), Theoretical Computer Science 281 (2002), 99--107. In particular, Sections 4--5 and Lemmas 5.1--5.3.
2. A. Frid and D. Jamet, *The number of binary rotation words*, arXiv:1302.3722v1 (posted 2013-02-15), RAIRO Theoretical Informatics and Applications 48 (2014), 453--465, especially Section 3.
3. M. Lothaire, *Algebraic Combinatorics on Words*, Cambridge University Press (2002), Chapter 2 (classical Sturmian and irrational-rotation background).
