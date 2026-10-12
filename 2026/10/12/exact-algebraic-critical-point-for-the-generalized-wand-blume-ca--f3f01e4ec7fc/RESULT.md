# Exact algebraic critical point for the generalized-wand Blume–Capel HC model
## Finding
For the second-order Cayley-tree Blume–Capel hard-core model with the generalized-wand compatibility graph, define
\[
P(\theta)=3\theta^{12}-7\theta^8+5\theta^4+\theta^3-1.
\]
Let \(\theta_*\) be the unique zero of \(P\) in \((0,1)\). Then
\[
\theta_*=0.658925198843917032768147735098\ldots .
\]
The translation-invariant phase count is exactly
\[
0<\theta<\theta_* \quad\Longrightarrow\quad 3\text{ distinct translation-invariant Gibbs measures},
\]
and
\[
\theta\ge\theta_* \quad\Longrightarrow\quad 1\text{ translation-invariant Gibbs measure}.
\]
Thus the approximate critical value reported in the source has the exact algebraic characterization above.

## Assumptions and scope
The model, compatibility graph, normalization, and positive boundary-law variables are exactly those of Khatamov's generalized-wand Blume–Capel HC model on the Cayley tree of order \(2\). The claim concerns translation-invariant Gibbs measures represented by positive solutions of that boundary-law system. It does not address periodic, weakly periodic, non-splitting, or non-translation-invariant Gibbs measures, nor extremality of the measures.

For the nonsymmetric branch in \(0<\theta<1\), the source derives
\[
\phi(\theta)=\frac{1-\theta^8+\sqrt{D(\theta)}}{2\theta^2},
\qquad
D(\theta)=\theta^{16}-2\theta^8-8\theta^7+8\theta^3+1,
\]
and a quadratic discriminant whose sign is the sign of
\[
F(\theta)=(1-3\theta^4)\phi(\theta)-2\theta.
\]

## Proof
Every zero of \(F\) must satisfy \(\theta<3^{-1/4}\), because for \(\theta\ge3^{-1/4}\) the factor \(1-3\theta^4\) is nonpositive while \(\phi(\theta)>0\) on \((0,1)\). Hence at a zero of \(F\) both sides of
\[
(1-3\theta^4)\sqrt{D(\theta)}=
4\theta^3-(1-3\theta^4)(1-\theta^8)
\]
have the sign required for squaring without introducing a zero with \(F\ne0\). Direct expansion gives
\[
(1-3\theta^4)^2D(\theta)
-
[4\theta^3-(1-3\theta^4)(1-\theta^8)]^2
=
-16\theta^3P(\theta).
\]
Therefore every zero of \(F\) in \((0,1)\) is a zero of \(P\).

It remains to show that \(P\) has only one zero in \((0,1)\). Differentiation gives
\[
P'(\theta)=\theta^2Q(\theta),
\qquad
Q(\theta)=36\theta^9-56\theta^5+20\theta+3
=3+4\theta(\theta^4-1)(9\theta^4-5).
\]
Put \(u=\theta^4\). If \(u\le5/9\), then \(Q(\theta)\ge3\). If \(5/9<u<1\), then
\[
Q(\theta)=3-4\theta(1-u)(9u-5)
>
3-4(1-u)(9u-5).
\]
On \([5/9,1]\), the quadratic \((1-u)(9u-5)\) has maximum \(4/9\), so
\[
Q(\theta)>3-\frac{16}9=\frac{11}9>0.
\]
Thus \(P\) is strictly increasing on \((0,1)\). Since \(P(0)=-1\) and \(P(1)=1\), it has a unique zero \(\theta_*\) there.

Finally, \(F(\theta)\to+\infty\) as \(\theta\downarrow0\), whereas \(F(3^{-1/4})<0\). Thus \(F\) has a zero, and the preceding argument forces it to be \(\theta_*\); there can be no second zero. Consequently the source discriminant is positive exactly for \(0<\theta<\theta_*\), vanishes at \(\theta_*\), and is negative afterward within \((0,1)\). At \(\theta_*\) the two nonsymmetric quadratic roots coincide, so \(z_1=z_2=\phi(\theta_*)/2\); by the source's uniqueness lemma for the symmetric branch this is the already-existing symmetric solution. For \(\theta\ge1\), the source's sign analysis rules out a positive nonsymmetric branch. The stated one-versus-three count follows.

## Verification
The accompanying `verify.py` checks, with exact rational arithmetic, the polynomial elimination identity and brackets the root by
\[
0.6589251988439<\theta_*<0.6589251988440.
\]
It also checks representative source-discriminant signs on both sides of the critical point. These finite calculations are corroborative; the all-parameter conclusion is proved analytically above.

## Relationship to prior work
Khatamov's 2022 paper derives the same generalized-wand boundary-law system and reports an approximate critical value \(\theta_{cr}\approx0.6589252\), using a plotted/computer-assisted discriminant analysis for the nonsymmetric branch. The source does not state the polynomial \(P\), an exact algebraic characterization of the critical point, or the monotonicity argument above. A later 2025 paper that cites Khatamov's work concerns an Ising–SOS model of interacting DNA bubbles rather than this generalized-wand phase boundary. The earlier ordinary-wand Blume–Capel result has a different compatibility graph and critical value \(1\), so it does not imply the present threshold.

## Limitations
The result sharpens only the translation-invariant generalized-wand branch on the order-two Cayley tree. It does not classify periodic or weakly periodic measures, prove extremality, compute thermodynamic free energies, or extend the exact threshold to arbitrary tree order. The literature search did not reveal a published equivalent formulation, but weakly indexed or unpublished calculations remain a residual originality risk.

## References
1. N. M. Khatamov, “Extremality of some Gibbs measures for the Blume–Capel HC-model on a Cayley tree,” Vestnik Udmurtskogo Universiteta. Matematika. Mekhanika. Komp'yuternye Nauki 32(2) (2022), 256–277. DOI: 10.35634/vm220207.
2. N. M. Khatamov, “Translation-Invariant Extreme Gibbs Measures for the Blume–Capel Model With Wand on a Cayley Tree,” Ukrainian Mathematical Journal 72 (2020), 623–641. DOI: 10.1007/s11253-020-01804-y.
3. U. A. Rozikov, N. M. Khatamov, N. N. Malikov, “Gibbs measures of bubble coalescence in an interacting system of DNA molecules for the Ising–SOS model on a Cayley tree,” Vestnik Udmurtskogo Universiteta 35(1) (2025), 96–116. DOI: 10.35634/vm250106.
