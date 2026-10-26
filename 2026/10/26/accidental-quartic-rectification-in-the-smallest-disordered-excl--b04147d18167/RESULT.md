# Accidental quartic rectification in the smallest disordered exclusion ring

## Finding

For a periodic four-site asymmetric simple exclusion process with two particles and site escape rates \((2,3,4,t)\), \(t>0\), let a particle at site \(i\) hop to an unoccupied neighbor to its right/left at respective rates \(a_i(1\pm\varepsilon)/2\), where \(|\varepsilon|<1\). Let \(J_t(\varepsilon)\) be the stationary signed hopping current **per bond** (total signed hop rate divided by four). Then the exact quadratic response coefficient is

\[
[\varepsilon^2]J_t(\varepsilon)=
-\frac{144t(t-11)(t-3)(t-2)}{(6t+17)^2(9t+26)^2}.
\]

More generally, for arbitrary strictly positive four-site rates \((a,b,c,d)\), put \(X=a+c\), \(Y=b+d\), \(U=a-c\), \(V=b-d\), and \(S=ab+ac+ad+bc+bd+cd\). The complete quadratic-response factorization is

\[
[\varepsilon^2]J_{a,b,c,d}(\varepsilon)=
\frac{abcd\,UV}{S^2(S+ac+bd)^2}
\left[(Y-X)(X^2+Y^2)+U^2(X+3Y)-V^2(3X+Y)\right].
\]

The vanishing of the cubic bracket is an additional cancellation surface beyond the obvious opposite-site equalities \(U=0\) or \(V=0\). The displayed one-parameter family intersects this surface at \(t=2\) and \(t=11\), both without a reflection symmetry.

The zero at \(t=3\) is protected by reflection, but the zeros at \(t=2\) and \(t=11\) are not. In particular, at \(t=11\), where all four site rates are distinct and the profile has no dihedral reflection symmetry, the quadratic contribution vanishes but the even-in-bias part is strictly positive for every \(0<|\varepsilon|<1\). Specifically, with

\[
E(\varepsilon)=51875+38190\varepsilon^2-7025\varepsilon^4,\qquad
O(\varepsilon)=688\varepsilon^3(\varepsilon^2-1),
\]

its exact current and symmetric response are

\[
J_{11}(\varepsilon)=\frac{2112\varepsilon(25-4\varepsilon^2)(1+\varepsilon^2)}{E(\varepsilon)+O(\varepsilon)},
\]
\[
\frac{J_{11}(\varepsilon)+J_{11}(-\varepsilon)}2
=\frac{1453056\varepsilon^4(25-4\varepsilon^2)(1-\varepsilon^4)}{E(\varepsilon)^2-O(\varepsilon)^2}
=\frac{1453056}{107640625}\varepsilon^4+O(\varepsilon^6).
\]

This supplies a nonsymmetric, genuinely interacting example with **quartic, not quadratic, leading rectification**. Moreover, on a three-site periodic site-trap ring every possible particle number has exactly odd current; hence four is the smallest ring size (among rings of at least three sites) admitting any bias rectification in this model.

## Assumptions and scope

The ring has labeled sites modulo its length. Particle occupancy is exclusionary and the particle number is fixed. Every escape rate is strictly positive and every attempted hop to an occupied neighbor is suppressed. The bias \(\varepsilon\) belongs to \((-1,1)\), ensuring a unique stationary law in every nontrivial particle sector. Site rates depend neither on the sign nor the magnitude of the bias. The current is normalized **per bond**, with clockwise hops counted positively; thus it is the expected signed total jump rate divided by the number of sites. Rates \((2,3,4,t)\) represent relative escape rates in a fixed time unit. In this regime the model is a quenched-trap exclusion process, not bond-symmetric disorder.

## Proof

Write \(\alpha=(1+\varepsilon)/2\) and \(\beta=(1-\varepsilon)/2\). For a four-site ring with general rates \((a,b,c,d)\), denote its four adjacent-pair configurations by \(A_i=\{i,i+1\}\), \(i=0,1,2,3\), and its two opposite-pair configurations by \(B_0=\{0,2\}\), \(B_1=\{1,3\}\). Every permitted jump connects an \(A_i\) with one of the \(B_j\). Their oriented rates are as follows:

| State | \(A_i\to B_0\) | \(A_i\to B_1\) | \(B_0\to A_i\) | \(B_1\to A_i\) |
|---|---|---|---|---|
| \(A_0\) | \(\alpha b\) | \(\beta a\) | \(\beta c\) | \(\alpha d\) |
| \(A_1\) | \(\beta b\) | \(\alpha c\) | \(\alpha a\) | \(\beta d\) |
| \(A_2\) | \(\alpha d\) | \(\beta c\) | \(\beta a\) | \(\alpha b\) |
| \(A_3\) | \(\beta d\) | \(\alpha a\) | \(\alpha c\) | \(\beta b\) |

For each row set \(s_i=q(A_i,B_0)+q(A_i,B_1)\), \(u_i=q(B_0,A_i)/s_i\), and \(v_i=q(B_1,A_i)/s_i\). Stationarity implies

\[
\pi(A_i)=u_i x+v_i y,\quad x=\pi(B_0),\quad y=\pi(B_1).
\]

The remaining stationary equations reduce to a two-state balance relation

\[
x\sum_i u_iq(A_i,B_1)=y\sum_i v_iq(A_i,B_0).
\]

Together with \(x+y+\sum_i\pi(A_i)=1\), this gives a unique rational stationary law. Its current is the sum, over configurations, of the signed allowed-hop rates times their stationary probabilities, divided by four. Twice differentiating the resulting rational current at zero and collecting the opposite-site sums and differences gives the displayed general factorization. Substitution of \((a,b,c,d)=(2,3,4,t)\) then gives the one-parameter coefficient. The standalone `verification.py` independently constructs all six generator rows and checks this identity against the two-state elimination.

For \(t=11\), the same elimination yields the displayed rational expression for \(J_{11}\). Its numerator is odd; the denominator separates into the displayed even and odd parts. Algebra therefore gives the exact symmetric response. On \(|\varepsilon|\le1\),

\[
E(\varepsilon)\ge51875-7025=44850>688\ge |O(\varepsilon)|,
\]

so the denominator of the symmetric response is strictly positive. Because \(25-4\varepsilon^2>0\), \(1-\varepsilon^4>0\), and \(\varepsilon^4>0\) for \(0<|\varepsilon|<1\), the symmetric response is strictly positive there. Taylor expansion at zero gives the positive quartic coefficient, with no quadratic term. At \(t=11\), all four rates differ, so no reflection or rotation can map the rate profile to its reversal; the bond-bias ratio is nonuniform since it is proportional to \(a_i/a_{i+1}\).

For minimality, on a three-site ring the one-particle current is \(J_1(\varepsilon)=\varepsilon/(1/a+1/b+1/c)\). The two-particle sector is a one-vacancy three-state chain; exact stationarity yields

\[
J_2(\varepsilon)=\frac{abc\varepsilon(3+\varepsilon^2)}{(a+b+c)^2-\varepsilon^2(a^2+b^2+c^2-2ab-2ac-2bc)}.
\]

Both are odd in \(\varepsilon\), while the zero- and full-particle sectors have zero current. The four-site \(t=11\) witness proves sharpness of this lower-size obstruction.

## Verification

Run `python verification.py` with SymPy installed. The script constructs the exact continuous-time exclusion generator from allowed particle hops, solves its stationary equations over rational fields for twelve parameter-bias combinations, independently derives the four-site Schur complement formula, checks the full rational current and its even part symbolically, verifies the general quadratic coefficient and its three positive zeros, and reconstructs the three-site exact parity formulas. This is finite-dimensional exact algebra, not an extrapolation from Monte Carlo samples. A symbolic algebra system serves only to perform identities also specified by the displayed six-state transition table. The positivity and minimality arguments are mathematical deductions from the identities.

## Relationship to prior work

Sakai and Akimoto, *Symmetry Breaking of Current Response in Disordered Exclusion Processes* (arXiv:2512.03316v1, first publicly posted 2025-12-03), formulate the site-trap and bond-trap dynamics and discuss bias-reversal symmetry. Their Section III.D (and Appendix C in the accessible later version) singles out bond-uniformity and spatial inversion as mechanisms suppressing quadratic rectification, and conjectures a quadratic term otherwise. The present exact four-site family gives two nonsymmetric cancellation points and a quartic leading response at one of them, so it is **not** a claim that generic site disorder preserves reversal symmetry. The same paper already notes that the single-particle trap current is odd; the additional three-site two-particle identity is used here only to locate the smallest ring exhibiting the phenomenon.

Juhász, Santen and Iglói, *Partially Asymmetric Exclusion Processes with Sitewise Disorder* (arXiv:cond-mat/0607366v1, 2006), analyze finite-system bottlenecks and scaling of stationary currents in strongly disordered systems. Their general interacting-particle analysis does not state the exact four-site quartic cancellation. General finite-state matrix-tree methods guarantee computability of these currents but do not by themselves identify the accidental cancellation locus or its leading quartic order.

## Limitations

The theorem is for fixed finite rings with complete exclusion and site-dependent escape rates, not an infinite-volume current law. The tuned cancellation is exceptional; away from the three displayed zeros the quadratic coefficient is nonzero. The result does not imply universal quartic response in quenched disorder, nor classify all four-site profiles at all biases. All exact formulas are for \(|\varepsilon|<1\); the current extends continuously to totally directed limiting rates, but irreducibility at the boundary is not assumed. The result is a mathematical priority claim subject to independent literature assessment; it is not an experimentally verified transport mechanism.

## References

1. I. Sakai and T. Akimoto, *Symmetry Breaking of Current Response in Disordered Exclusion Processes*, arXiv:2512.03316v1 (2025-12-03); accessible revised full text: https://arxiv.org/pdf/2512.03316.
2. R. Juhász, L. Santen and F. Iglói, *Partially Asymmetric Exclusion Processes with Sitewise Disorder*, arXiv:cond-mat/0607366v1 (2006), https://arxiv.org/pdf/cond-mat/0607366.
