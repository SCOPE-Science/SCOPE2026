# A unique persistence-ranking reversal between four-patch star and path reintroduction sites

## Finding

Consider two four-patch habitat networks with three undirected colonization links: the star and the path. Occupied patches die at unit rate; an empty patch is colonized at rate \(\lambda\) per occupied neighboring patch, independently, where \(\lambda>0\). Begin with precisely one occupied patch and let \(T_G(v;\lambda)\) be the mean time until every patch is empty. Denote the four inequivalent network–source choices by \(S_c\) (star center), \(S_l\) (star leaf), \(P_i\) (path internal vertex), and \(P_e\) (path endpoint), using the same symbols for their mean extinction times.

**Theorem.** A unique number \(\rho\in(5,6)\), approximately \(5.17091139563469\), is the positive root of
\[
Q(z)=108z^8+309z^7-1592z^6-9631z^5-21648z^4-26628z^3-19080z^2-7560z-1296.
\]
For every \(0<\lambda<\rho\), the complete strict ranking is
\[
S_c>P_i>S_l>P_e.
\]
For every \(\lambda>\rho\), the complete strict ranking is
\[
S_c>S_l>P_i>P_e.
\]
At \(\lambda=\rho\), only \(S_l=P_i\) is tied; the outer inequalities remain strict. In particular, among connected trees, order four is the first order at which two distinct tree shapes even exist, and at that order the ranking of their **single-patch introduction sites** genuinely depends on the colonization-to-extinction ratio.

## Assumptions and scope

All networks are simple, undirected, unweighted, connected trees. The continuous-time Markov process has occupancy set \(U\subseteq V(G)\), absorbs at \(\varnothing\), removes each \(v\in U\) at rate one, and adds each \(w\notin U\) at rate \(\lambda |N_G(w)\cap U|\). The initial state is exactly \(\{v\}\); the comparison never averages over introduction sites. By rescaling time, a common positive local-extinction rate could instead be used, with \(\lambda\) interpreted as colonization divided by extinction rate. No other transitions, spontaneous colonization, or immigration are allowed.

## Proof

**1. Exact backward equations and finiteness.** For nonempty \(U\subseteq V(G)\), write \(t_U=\mathbb E_U[\tau_\varnothing]\) and \(b(U)=\sum_{w\notin U}|N_G(w)\cap U|\). Set \(t_\varnothing=0\). Conditioning on the next transition gives the nonsingular finite linear system
\[
\bigl(|U|+\lambda b(U)\bigr)t_U
-\sum_{v\in U}t_{U\setminus\{v\}}
-\lambda\sum_{w\notin U}|N_G(w)\cap U|t_{U\cup\{w\}}=1.
\]
The sum over removal terms uses \(t_\varnothing=0\). From every nonempty configuration a sequence of deaths without births has positive probability, uniformly over the finite state space; hence absorption occurs almost surely with finite mean. Therefore the \(15\times15\) transient generator matrix is invertible for every \(\lambda>0\).

**2. Exact expressions.** Put \(z=\lambda\) and introduce the strictly positive polynomials
\[
A(z)=(3z+2)(4z+3),\qquad
C(z)=(4z^2+9z+6)(12z^3+31z^2+32z+12),\quad B(z)=A(z)C(z).
\]
Solving the displayed backward system on the two trees gives the four single-patch times:
\[
\begin{aligned}
S_c&=\frac{3z^5+16z^4+40z^3+69z^2+52z+12}{2A(z)},\\
S_l&=\frac{9z^5+42z^4+94z^3+153z^2+120z+36}{6A(z)},\\
P_e&=\frac{12z^8+88z^7+321z^6+800z^5+1420z^4+1742z^3+1404z^2+672z+144}{2C(z)},\\
P_i&=\frac{12z^8+94z^7+368z^6+975z^5+1783z^4+2176z^3+1680z^2+744z+144}{2C(z)}.
\end{aligned}
\]
These are **identities for all positive real \(z\)**, not extrapolations from sample rates. Here is an exact finite certificate for the rational identities: each entry of the \(15\times15\) backward matrix is a polynomial of degree at most one. By Cramer's rule, its determinant has degree at most \(15\) and the numerator obtained by replacing one column with the constant all-ones right side has degree at most \(14\). For the displayed candidate rational functions, numerator degrees are at most \(8\) and denominator degrees at most \(5\). Therefore each cross-multiplied identity has degree at most \(\max(14+5,15+8)=23\). The accompanying standard-library checker solves both backward systems **exactly over the rationals** at all \(24\) distinct positive rates \(z=1,\ldots,24\), and matches every one of the four expressions at each rate. A polynomial of degree at most \(23\) vanishing at these \(24\) points vanishes identically. This supplies an exact all-parameter certificate independent of unbounded numerical experiments. The checker also verifies the coefficient identities used below directly.

**3. All comparisons.** Exact polynomial subtraction gives
\[
\begin{aligned}
S_c-P_e&=\frac{zR_{ce}(z)}{2B(z)},\\
S_c-P_i&=\frac{z(z+1)R_{ci}(z)}{2B(z)},\\
S_l-P_e&=\frac{z^2R_{le}(z)}{6B(z)},\\
S_l-P_i&=\frac{zQ(z)}{6B(z)},
\end{aligned}
\]
where
\[
\begin{aligned}
R_{ce}(z)={}&204z^8+1649z^7+6237z^6+14350z^5+21743z^4+21880z^3+14088z^2+5256z+864,\\
R_{ci}(z)={}&132z^7+851z^6+2451z^5+4286z^4+5028z^3+3984z^2+1944z+432,\\
R_{le}(z)={}&324z^7+2307z^6+7213z^5+13208z^4+15639z^3+11976z^2+5400z+1080.
\end{aligned}
\]
All three \(R\)-polynomials have strictly positive coefficients. Moreover, direct subtraction of the formulas in Step 2 shows
\[
S_c-S_l=\frac{z(3z^3+13z^2+27z+18)}{3A(z)}>0
\]
and
\[
P_i-P_e=\frac{z(6z^6+47z^5+175z^4+363z^3+434z^2+276z+72)}{2C(z)}>0.
\]
Thus every required order comparison except \(S_l\) versus \(P_i\) is independent of \(z\).

**4. Exactly one crossing.** In descending powers, \(Q\) has coefficient signs \((+,+,-,-,-,-,-,-,-)\), hence exactly one sign change. Descartes' rule of signs gives at most one positive root, counted with multiplicity. Since \(Q(5)=-6018346<0\) and \(Q(6)=84190752>0\), continuity supplies such a root, proving its uniqueness; the signs on either side then follow. Since \(B(z)>0\) for \(z>0\), this exactly determines the sign of \(S_l-P_i\) and yields the claimed rankings.

Finally, there is only one unlabeled connected tree for every order below four, whereas \(K_{1,3}\) and \(P_4\) are the two nonisomorphic connected four-vertex trees. Both have four vertices and three edges, so size and edge count do not explain the reversal.

## Verification

Run `python3 verify.py` in the same directory as this document; the script depends only on the Python 3 standard library. It reconstructs the complete \(15\)-state backward matrices at 24 distinct rational rates per graph, solves them using exact `fractions.Fraction` elimination, verifies the four rational formulas, checks six polynomial comparison identities coefficient by coefficient, and checks the sign-change/root bracket. Expected first line:

`VERIFY_OK polynomial_identities=6 exact_system_solves=48`

The degree-bound argument above promotes the 24-point identity test to a rigorous all-rate polynomial identity check. It does **not** assert that a finite scan independently establishes root uniqueness; that conclusion comes from Descartes' rule and the displayed exact endpoint signs.

## Relationship to prior work

Barbillon et al. (arXiv:1404.4287) motivated finite-patch extinction–colonization questions and analyzed the effect of network topology on variety persistence. Their explicitly discrete-generation extinction-then-colonization dynamics and predominantly all-occupied initial conditions are not the present continuous-time single-source optimization problem. Mountford et al. (arXiv:1203.2972) establish high-level asymptotics for contact-process extinction times on growing graphs, generally from full occupancy, without giving this exact order-four ranking. Van de Bovenkamp and Van Mieghem (DOI 10.1103/PhysRevE.92.032806) derive exact mean SIS survival expressions for complete graphs and stars. Their announced scope overlaps the star side of our calculation; complete text was not accessible for a decisive full-document comparison, so undocumented coverage of part of the present finite comparison remains possible. The new conclusion is the **joint path-versus-star, site-sensitive, all-rate complete ranking and its unique switch**, rather than the general Markov-chain method or any stand-alone formula for star survival.

## Limitations

The theorem concerns exact mean extinction times in a four-vertex, homogeneous, independent continuous-time model with exactly one initial occupied patch. It does not apply without further analysis to discrete-time colonization protocols, heterogeneous rates, repeated introduction, multispecies interactions, partially occupied random initial states, or comparisons of arbitrary larger trees. The exact crossing is a theoretical decision boundary; no empirical detection or statistical robustness is asserted. The closest known star-survival article was only accessible at the abstract level, which is an originality risk. No claim of independent replication or external certification is made.

## References

1. T. Mountford, J.-C. Mourrat, D. Valesin and Q. Yao, *Exponential extinction time of the contact process on finite graphs*, arXiv:1203.2972 (first posted 2012-03-13); subsequently *Stochastic Processes and their Applications* 126 (2016), 1974–2013, DOI:10.1016/j.spa.2016.01.001.
2. P. Barbillon, M. Thomas, I. Goldringer, F. Hospital and S. Robin, *Network impact on persistence in a finite population dynamic diffusion model: application to an emergent seed exchange network*, arXiv:1404.4287 (first posted 2014-04-16); DOI:10.1016/j.jtbi.2014.10.032.
3. R. van de Bovenkamp and P. Van Mieghem, *Survival time of the susceptible-infected-susceptible infection process on a graph*, *Physical Review E* 92 (2015), 032806, DOI:10.1103/PhysRevE.92.032806.
