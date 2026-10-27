# Robust four-census host-only parameter aliases in the Nicholson–Bailey model

## Finding
For the positive Nicholson–Bailey host–parasitoid model with a *known* unit searching coefficient,
\[
H_{n+1}=R H_n e^{-P_n},\qquad P_{n+1}=cH_n(1-e^{-P_n}),\quad R,c,H_0,P_0>0,
\]
there is an **open set of nonconstant, noise-free four-census host histories** \((H_0,H_1,H_2,H_3)\) for which **at least two distinct strictly positive parameter triples** \((R,c,P_0)\) produce exactly the same four observed host abundances. Both parameterizations are *locally isolated*: this is a robust failure of global, rather than of local, identifiability.

An exact witness starts with \(H_0=1\) and uses the two parameter triples
\[
(R,c,P_0)=(2,\log 2,\log 2),\qquad (R,c,P_0)=(4,2\log 2,2\log 2).
\]
Their common host-only observations are
\[
(H_0,H_1,H_2,H_3)=\left(1,1,\sqrt2,\sqrt2\,2^{1/\sqrt2}\right).
\]
The next host census separates these *particular two* trajectories exactly:
\[
\frac{H_4^{(R=4)}}{H_4^{(R=2)}}=2^{1-\sqrt2}<1.
\]
No general five-census identifiability theorem is asserted.

## Assumptions and scope
The two models have strictly positive, real-valued host and parasitoid abundances and constant parameters at all integer generations. The searching/attack coefficient is fixed at \(a=1\) in both models. The only observations are exact host abundances at four successive generations; parasitoids are latent. The reproduction multiplier, offspring coefficient and initial parasitoid abundance are unknown. This is finite-horizon *global observational aliasing*, not a claim of infinite-trajectory structural nonidentifiability. Host counts are modeled as densities, not constrained to integers.

## Proof
**1. Eliminate the latent population.** For arbitrary positive host observations, put \(r_j=H_{j+1}/H_j\), \(j=0,1,2\). A model reproducing them must have \(R>\max(r_0,r_1,r_2)\) and
\[
P_j=\log(R/r_j),\qquad j=0,1,2.
\]
The parasitoid equation at \(j=0,1\) is therefore equivalent to
\[
\log(R/r_1)=cH_0(1-r_0/R),\qquad
\log(R/r_2)=cH_0r_0(1-r_1/R).
\]
Thus a proposed \(R>\max(r_0,r_1,r_2)\) is compatible with the four hosts **if and only if**
\[
F(R;r_0,r_1,r_2):=
\frac{\log(R/r_1)}{1-r_0/R}
-\frac{\log(R/r_2)}{r_0(1-r_1/R)}=0.
\]
For any such root, choose \(P_0=\log(R/r_0)>0\) and
\[
c=\frac{\log(R/r_1)}{H_0(1-r_0/R)}>0.
\]
The recurrences then reproduce all four observed host abundances, proving sufficiency as well as necessity.

**2. Construct two exact aliases.** Write \(L=\log2\), \(b=\sqrt2\), and \(d=2^{1/\sqrt2}\). Starting from \(H_0=1\), either stated parameter triple has \(H_1=1\). For \((R,c)=(2,L)\), the next parasitoid states satisfy
\[
P_1=L/2,\qquad P_2=L(1-1/b).
\]
For \((R,c)=(4,2L)\), they satisfy
\[
P_1=3L/2,\qquad P_2=2L(1-1/(2b)).
\]
Direct substitution gives \(H_2=b\) and \(H_3=bd\) for both trajectories. In particular \(F(2;1,b,d)=F(4;1,b,d)=0\), with admissible positive states and parameters throughout.

**3. Prove the ambiguity persists on an open set.** For the fixed witness \((r_0,r_1,r_2)=(1,b,d)\), set
\[
K(R)=\frac{\log(R/b)}{1-1/R}.
\]
At any root of \(F(R;1,b,d)\), differentiating the two fractions and using their equality yields
\[
\frac{\partial F}{\partial R}(R;1,b,d)=
\frac{(1-b)(1-K(R))}{(R-1)(R-b)}.
\]
At the two roots, \(K(2)=L\) and \(K(4)=2L\). Since \(\tfrac12<L<1\), and \(b>1\), the derivatives have opposite **nonzero** signs: the derivative is negative at \(2\) and positive at \(4\). The implicit function theorem therefore supplies smooth, separated admissible roots near \(2\) and \(4\) for every \((r_0,r_1,r_2)\) in a common open neighborhood of \((1,b,d)\). Perturbing also \(H_0>0\) only changes the positive reconstructed offspring coefficients. Since \(b\ne1\), a smaller neighborhood still consists of nonconstant host histories. The claim holds on an open set in the four-dimensional space of positive host histories.

**4. Exhibit an exact distinguishing fifth census.** Since \(H_2=b\) and \(H_3=bd\) agree, the parasitoid recurrence gives
\[
P_3^{(2)}=Lb(1-d/2),\qquad P_3^{(4)}=2Lb(1-d/4).
\]
Consequently
\[
\log\frac{H_4^{(4)}}{H_4^{(2)}}
=\log(4/2)-(P_3^{(4)}-P_3^{(2)})
=L(1-b),
\]
which proves the claimed strict ratio.

## Verification
Run the bundled standard-library script `verify_alias.py` with `python3 verify_alias.py`. It replays both four-census trajectories and the fifth-census ratio, evaluates the compatibility roots and their nonzero derivatives, and checks 500 nearby perturbed data vectors. Finite numerical experiments are verification aids only; exact recurrences and the implicit function theorem prove the infinite open-neighborhood assertion.

## Relationship to prior work
Nicholson and Bailey (1935) introduced the classical host–parasitoid modeling framework; Hassell's accessible review reproduces the precise two-equation map and discusses the ecological difficulty of calibrating demographic components, without a stated four-census two-branch result. The broader structural-identifiability literature of Vajda–Rabitz, Evans et al., and Anstett et al. addresses different models or general state-isomorphism methods. Those results motivate the distinction between local and global identifiability but do not, in the inspected available material, imply the exact positive Nicholson–Bailey witness and its two simple inverse roots. Searching for the model under host-only, partial-output, inverse-recurrence, and parameter-alias formulations did not identify an equivalent prior statement; absence from search results is not proof of historical novelty. The original 1935 full text and several general-theory papers were not fully accessible, and broader coverage is a genuine residual risk.

## Limitations
The result establishes at least two, not exactly two, admissible solutions for histories in an open set. It does not classify all four-census histories, prove universal five-census recovery, establish infinite-horizon nonidentifiability, or address noisy observations. Observing parasitoids, externally fixing a demographic parameter, or imposing different biological bounds could remove the exhibited ambiguity. The original 1935 paper's publisher gives September 1935 without a verified day; a secondary bibliographic record indexes September 1, 1935, so the day of first public release remains bibliographically uncertain without affecting archive eligibility.

## References
1. Nicholson, A. J., and Bailey, V. A. (1935). *The Balance of Animal Populations—Part I*. *Proceedings of the Zoological Society of London* 105, 551–598. DOI: 10.1111/j.1096-3642.1935.tb01680.x.
2. Hassell, M. P. (2001 online). *Host–parasitoid population dynamics*. *Journal of Animal Ecology* 69, 543–566. DOI: 10.1046/j.1365-2656.2000.00445.x.
3. Vajda, S., and Rabitz, H. (1989). *State Isomorphism Approach to Global Identifiability of Nonlinear Systems*. *IEEE Transactions on Automatic Control* 34, 220–223. DOI: 10.1109/9.21105.
4. Evans, N. D., et al. (2005). *The structural identifiability of the susceptible infected recovered model with seasonal forcing*. *Mathematical Biosciences* 194, 175–197. DOI: 10.1016/j.mbs.2004.10.011.
5. Anstett, F., Bloch, G., Millérioux, G., and Denis-Vidal, L. (2008). *Identifiability of discrete-time nonlinear systems: The local state isomorphism approach*. *Automatica* 44, 2884–2889. DOI: 10.1016/j.automatica.2008.03.019.
