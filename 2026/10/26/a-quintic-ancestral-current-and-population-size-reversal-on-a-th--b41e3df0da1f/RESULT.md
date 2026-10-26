# A quintic ancestral current and population-size reversal on a three-site Fleming–Viot system

## Finding

Consider the stationary ancestral flux in the three-site, uniform-copying Fleming–Viot process, with the labels of particles retained through motion and reset upon killing and rebirth. For three particles and the strictly positive killing family \(k=(1-\varepsilon,1,1+\varepsilon)\), \(-1<\varepsilon<1\), the signed port current \(\Delta_3=F_{02}^{(3)}-F_{20}^{(3)}\) has the **exact identity**

\[
\boxed{\Delta_3(\varepsilon)=\frac{24\varepsilon^5(16-3\varepsilon^2)(38448+479\varepsilon^2)}{(790272+4704\varepsilon^2+279\varepsilon^4+5\varepsilon^6)(11757312-137808\varepsilon^2+840\varepsilon^4+143\varepsilon^6)}.}
\]

The current has the sign of \(\varepsilon\) over the entire admissible interval; at equal killing it vanishes to exact fifth order:

\[
\boxed{\Delta_3(\varepsilon)=\frac{89}{56010528}\varepsilon^5+O(\varepsilon^7).}
\]

Lin and Lu establish for every **fixed** \(N\ge4\) the contrasting expansion

\[
\Delta_N(\varepsilon)=-\frac{2(N-3)(N-2)(N-1)^2}{9N(3N-2)^2(3N-1)^2(3N+1)}\varepsilon^3+O(\varepsilon^5).
\]

In particular their coefficient for four particles is \(-1/157300\). Therefore the ancestral current points in opposite directions for three particles and four particles when \(\varepsilon>0\) is sufficiently small. This last comparison combines the new three-particle result with the **previously published** general-population expansion; no new proof or priority is asserted for that expansion.

## Assumptions and scope

Let \(I=\{0,1,2\}\). Particles move individually at rate \(1\) from any \(i\) to each distinct \(j\). A particle at site \(i\) is killed at rate \(k_i>0\), instantaneously relocates to a uniformly sampled distinct particle, and inherits that donor's label. A donor can be at the same spatial site as the killed particle: these events may change ancestral labels without changing population counts. Throughout the new calculation the particle number is exactly \(N=3\), the killing rates are \(k_0=1-\varepsilon\), \(k_1=1\), \(k_2=1+\varepsilon\), and \(-1<\varepsilon<1\). The count process is finite and irreducible and has a unique stationary probability \(\pi_3\).

For a count triple \(c=(c_0,c_1,c_2)\) with \(\sum c_i=3\) and a distinguished founder at site \(i\), denote by \(h_3(i,d)\) the probability that its ancestral label eventually occupies the entire three-particle system, where \(d\) is the count triple of the other two particles. This fixation probability exists for the finite labelled process. Define

\[
F_{ij}^{(3)}=\sum_{c:c_i>0}\pi_3(c)c_i h_3(j,c-e_i),\qquad
\Delta_3=F_{02}^{(3)}-F_{20}^{(3)}.
\]

These are exactly the transport and current conventions of Lin and Lu, not an alternative normalization. Motion rates on both directed ports are \(1\). Reflection \(0\leftrightarrow2\) reverses the sign of \(\Delta_3\).

## Proof

**1. The ten-state population generator.** Let \(\Omega_3=\{c\in\mathbb N_0^3:\sum c_i=3\}\), with ten elements. For distinct \(a,b\), the total rate of a count transition is

\[
L(c,c-e_a+e_b)=c_a\left(1+\frac{c_bk_a}{2}\right).
\]

The first term is motion and the second is a death whose donor is at \(b\). Same-site copying is not a count transition, but will appear in the next generator. Put the diagonal equal to minus the outgoing sum. Solve the ten stationary equations \(\pi L=0\), replacing one dependent equation by \(\sum_c\pi(c)=1\). Every coefficient lies in \(\mathbb Q(\varepsilon)\).

**2. The eighteen-state founder equation.** Write \(\mathcal H=\{(i,d):i\in I,\ d\in\mathbb N_0^3,\ \sum d_i=2\}\), which has eighteen elements. Define a linear operator on functions \(g:\mathcal H\to\mathbb R\) by

\[
\begin{aligned}
(Tg)(i,d)={}&\sum_{j\ne i}[g(j,d)-g(i,d)]\\
&+\sum_a d_a\sum_{b\ne a}[g(i,d-e_a+e_b)-g(i,d)]-k_i g(i,d)\\
&+\sum_a d_a k_a\left[g(i,d-e_a+e_i)
+\frac12\sum_b(d_b-\mathbf 1_{\{a=b\}})g(i,d-e_a+e_b)-g(i,d)\right].
\end{aligned}
\]

Terms with \(d_a=0\) are omitted. A killed founder loses its label, accounting for \(-k_i g\); deaths of other particles can produce a second descendant of the founder or copy a surviving other particle. This is the exact founder equation in Lin and Lu, Section 3 and Appendix A. The fixation probability solves \(Th=0\). Exchangeability when all three individuals share a site gives the normalization \(h(0,(2,0,0))=1/3\), independent of positive killing rates. With this normalization the eighteen linear equations have a unique solution: under uniform copying on a finite irreducible motion system all labels ultimately coalesce, and the harmonic fixation function is unique once normalized.

**3. Exact rational elimination.** Order the ten count states lexicographically and the eighteen founder states by \(i\) followed by lexicographic order of \(d\). Both coefficient matrices are affine-linear in \(\varepsilon\). The accompanying `verify_fleming_viot.py` constructs these matrices from the two displayed generators, solves them by exact rational-function Gaussian elimination over \(\mathbb Q(\varepsilon)\), and checks every stationary equation and all eighteen normalized founder equations as rational identities. Substitute the solutions into

\[
\Delta_3=\sum_{c:c_0>0}\pi_3(c)c_0h_3(2,c-e_0)
-\sum_{c:c_2>0}\pi_3(c)c_2h_3(0,c-e_2).
\]

Exact polynomial reduction factors the numerator as \(24\varepsilon^5(16-3\varepsilon^2)(38448+479\varepsilon^2)\) and the two denominator factors as printed under Finding. The verifier checks equality of the derived rational function and the displayed closed form by cancelling their difference to exactly zero. This finite exact elimination is an algebraic proof, not an extrapolation from numerical samples.

**4. Signs and response order.** Put \(u=\varepsilon^2\), so \(0\le u<1\). The first denominator factor is strictly positive. The second is bounded below by \(11757312-137808>0\), since the quadratic and cubic terms in \(u\) are nonnegative. Also \(16-3u>13>0\) and \(38448+479u>0\). Therefore the fraction has precisely the sign of \(\varepsilon\). Dividing by \(\varepsilon^5\) and taking \(\varepsilon\to0\) yields \(89/56010528\); all lower odd terms and all even terms vanish. The displayed \(O(\varepsilon^7)\) remainder follows from the rational formula and its parity.

**5. Population reversal.** Lin and Lu, Proposition 5.2, already prove the negative cubic expansion for every fixed \(N\ge4\). Its coefficient is strictly negative when \(N\ge4\); our global positivity for \(N=3\) therefore proves the asserted opposite directions for sufficiently small positive \(\varepsilon\), without claiming any uniform threshold in \(N\).

## Verification

The standalone verification script is `verify_fleming_viot.py` and requires Python 3 with SymPy. Run `python verify_fleming_viot.py`; a reference execution is embedded in `verification_output.txt`. In addition to independently reconstructing the ten-state and eighteen-state equations and checking the symbolic identity, it constructs a separate **two-colour absorbing Markov chain with thirty-six transient states**. The latter computes distinguished-label fixation without using the founder harmonic matrix. It checks the current at \(\varepsilon=1/2\) and \(\varepsilon=1/4\) against the exact formula and reproduces the independently published \(\Delta_3(1,2,4)=421413160/139117744582101\). This numerical-parameter verification is auxiliary to the exact all-parameter rational identity. Matrix nonsingularity and fixation interpretation rely on the standard finite-chain irreducibility and coalescence argument stated above.

## Relationship to prior work

Lin and Lu, *Ancestral circulation beyond two Fleming–Viot particles* (arXiv:2610.12589v1), introduce this current, prove its conservation and universal zero for two particles, give a positive three-particle example at a **different** killing vector \((1,2,4)\), and establish the cubic response for the family \((1-\varepsilon,1,1+\varepsilon)\) only for \(N\ge4\). They explicitly observe the cancellation of their cubic coefficient when \(N=3\) and do not obtain the three-particle quintic or this family's global sign. The present new finding supplies exactly that exceptional response and the resulting three-versus-four direction reversal.

Lin and Lu, *Branching explosion of Brownian Fleming–Viot systems* (arXiv:2610.18802v1), study continuous Brownian motion and a two-harmonic **periodic** killing profile, obtaining a nonzero cubic inherited Euclidean displacement current. That continuous-space displacement current is not the three-site port current here and does not give the rational identity. Cloez and Thai, *Fleming–Viot processes: two explicit examples* (2016), derive homogeneous-killing invariant laws and spectral estimates on complete graphs; their complete-graph calculation does not treat heterogeneous three-site ancestral fixation currents. Bieniek and Burdzy (2018) study the spine and its large-population distribution; the inspected abstract does not assert an exact finite three-particle sign law. These comparisons leave normal historical-priority risk, not a proof of uniqueness.

## Limitations

The exact formula concerns three particles, three complete-graph sites, unit motion rates, uniform copying and the specified one-parameter positive killing family. It does not classify arbitrary killing triples, nonlinear response on other graphs, or every sign for \(N\ge4\) over the full interval. The population-reversal corollary is for each fixed larger population at sufficiently small contrast and uses the cited earlier cubic theorem. Finite rational algebra is exact for this model, but the present review is not independent mathematical validation. Historical coverage under alternative terminology cannot be ruled out categorically.

## References

1. Y. Lin and T. Lu, *Ancestral circulation beyond two Fleming–Viot particles*, arXiv:2610.12589v1 (first posted 2026-10-08), https://arxiv.org/html/2610.12589v1. Especially Sections 1, 3, 5 and Appendices A–B.
2. Y. Lin and T. Lu, *Branching explosion of Brownian Fleming–Viot systems*, arXiv:2610.18802v1 (first posted 2026-10-13), https://arxiv.org/abs/2610.18802. Especially Sections 1 and 3.
3. B. Cloez and M.-N. Thai, *Fleming–Viot processes: two explicit examples*, ALEA 13 (2016), 337–356, https://alea.impa.br/articles/v13/13-14.pdf.
4. M. Bieniek and K. Burdzy, *The distribution of the spine of a Fleming–Viot type process*, Stochastic Processes and their Applications 128 (2018), 3751–3777, arXiv:1507.06855.
