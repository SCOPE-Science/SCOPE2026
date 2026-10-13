# Exact global rectification-sign law for the two-site disordered exclusion channel

## Finding
Consider the two-site, boundary-driven site-disordered symmetric exclusion process defined below. For any positive departure rates \(a,b\), positive reservoir contact scale \(\kappa\), and reservoir densities \(u,v\in[0,1]\), its stationary left-to-right particle current is
\[
J(u,v)=\frac{ab\kappa(u-v)S(u,v)}{D(u,v)},
\]
where
\[
L=a(1-u)+\kappa u,\quad R=b(1-v)+\kappa v,\quad S=L+R,
\]
\[
D(u,v)=S(LR+aR+bL)+(a-b)\kappa(uL-vR)>0.
\]
Its exact, nonperturbative current-reversal asymmetry is
\[
J(u,v)+J(v,u)=\frac{ab\kappa^2(a-b)(u-v)^2P(u,v)}{D(u,v)D(v,u)},
\]
with
\[
P(u,v)=(a-b)^2(1-u)(1-v)+2ab(2-u-v)+\kappa(a+b)(u+v)>0.
\]
Hence for unequal reservoirs, the current-reversal asymmetry is nonzero **if and only if** the two departure rates are unequal, and its sign is exactly the sign of \(a-b\), independently of the mean density, drive magnitude, and contact scale. The current itself has the sign of \(u-v\). This is a complete all-drive classification for the minimal two-site channel, not an asymptotic or mean-field statement.

## Assumptions and scope
Each site contains zero or one indistinguishable particle, with configurations \(00,10,01,11\). The left reservoir creates a particle at empty site 1 at rate \(\kappa u\) and removes one from occupied site 1 at rate \(a(1-u)\). The right reservoir creates at site 2 at rate \(\kappa v\) and removes at rate \(b(1-v)\). A particle at site 1 jumps to empty site 2 at rate \(a\); a particle at site 2 jumps to empty site 1 at rate \(b\). All stated rate parameters are strictly positive and \(u,v\) may include the endpoints zero and one. This departure-rate disorder, with reservoir detailed-balance rates matched to site departure rates, gives at equal reservoirs the inhomogeneous reversible fugacities \(\kappa u/[a(1-u)]\) and \(\kappa u/[b(1-u)]\) where these expressions are finite.

## Proof
Set \(X=\mathbb E\eta_1\), \(Y=\mathbb E\eta_2\), and \(Z=\mathbb E(\eta_1\eta_2)\) in the stationary state, and write \(U=\kappa u\), \(V=\kappa v\), \(A=a(1-u)\), \(B=b(1-v)\). Since \(L=U+A\), \(R=V+B\), and \(S=L+R\), conservation of particle flow across the left contact, internal bond, and right contact gives
\[
J=U-LX=a(X-Z)-b(Y-Z)=RY-V.
\]
The two-site occupation observable changes only through reservoir events, so its exact stationary balance is
\[
0=U(Y-Z)+V(X-Z)-(A+B)Z,
\quad Z=\frac{UY+VX}{S}.
\]
Substitute \(X=(U-J)/L\) and \(Y=(V+J)/R\) into the last equality and then into the bond current. The constant numerator simplifies to
\[
aUR-bVL-(a-b)UV=ab\kappa(u-v),
\]
which yields the stated formula for \(J\), after multiplication by \(S\).

To see that \(D>0\), if \(a\ge b\), rewrite it as
\[
D=SLR+L\{a(U+R)+bA\}+R\{bS+(a-b)B\}>0.
\]
If \(a<b\), use instead
\[
D=SLR+L\{b(A+R)+aU\}+R\{aS+(b-a)V\}>0.
\]
These identities are direct expansions of the displayed expression for \(D\) and remain positive for reservoir endpoints. The finite Markov chain has a unique stationary distribution (irreducible except at the common endpoints, where its all-empty or all-full absorbing state is unique), so the moment balances characterize the actual stationary current.

Let \(S'=S(v,u)\), \(D'=D(v,u)\). Direct polynomial expansion, or expansion of the two preceding definitions, gives the exact identity
\[
S D'-S'D=\kappa(a-b)(u-v)P(u,v).
\]
As \(J(v,u)=-ab\kappa(u-v)S'/D'\), subtracting the two fractions gives the claimed reversal formula. Finally, \(P>0\): all its displayed summands are nonnegative for \(0\le u,v\le1\), and at least one is strictly positive since \(a,b,\kappa>0\) and either \(u+v>0\) or \(2-u-v>0\). Thus the two signs and the iff statement follow without a perturbation expansion.

## Verification
Run `python3 verify.py` using only Python's standard library. It independently assembles the full four-configuration continuous-time Markov generator, solves the stationary system with exact rational Gaussian elimination, and compares the bond current to both symbolic formulas for 1,600 rational parameter/reservoir combinations. It checks the positive denominator and exact signs, including all reservoir-density endpoints, and 960 nonzero rectification cases. The recorded output is `CHECK_OK stationary_chain_cases 1600 nonzero_rectification_cases 960 example_current 36/173 example_reverse -44/237`. For the illustrative parameters \((a,b,\kappa,u,v)=(2,1,1,3/4,1/4)\), current reversal changes \(36/173\) into \(-44/237\), leaving a positive sum \(920/41001\). The infinite continuum of parameters is covered by the algebraic proof, not by finite enumerations.

## Relationship to prior work
Sakai and Akimoto (arXiv:2609.03560v1, first posted 2026-09-03) investigate site-dependent exclusion under boundary-density driving. Their abstract explicitly describes Galerkin and higher-order closure approximations; they motivate sample-specific rectification and prove a reflection-symmetry obstruction in the studied regime. The result here isolates the smallest interacting channel and supplies an exact stationary current and all-drive iff/sign classification: reflection asymmetry becomes sufficient in this two-site model. It is not a claim that the underlying rectification phenomenon, the equilibrium site fugacities, or the reflection argument are new.

Sakai and Akimoto (arXiv:2512.03316v1; Phys. Rev. E 113, 044123) study reversal of an imposed bulk bias and a spatial bond-bias-ratio criterion, a different drive and observable comparison. Homogeneous open exclusion is classical background, exemplified by Derrida, Douçot, and Roche (J. Stat. Phys. 115, 717–748, 2004). Comparisons used accessible abstracts and substantive third-party literature overviews; the relevant primary full texts were not obtainable during this assessment, leaving explicit implicit-coverage risk. This mathematical claim is self-contained and does not depend on a purported absence from inaccessible material.

## Limitations
The theorem covers exactly two sites, with the stated matched boundary contact rates and symmetric departure-rate hopping; it does not prove sufficiency of broken reflection symmetry for longer disordered chains. Different reservoir contact conventions can yield a different model and current. The exact nonzero asymmetry concerns unequal reservoir densities; at equal densities it is zero even when \(a\ne b\). No limit in chain length or disorder-distribution theorem is established. Full-primary-text priority comparison remains incomplete, and independent scholarly assessment is not asserted.

## References
1. I. Sakai and T. Akimoto, *Sample-specific rectification-like response in a boundary-driven exclusion process*, arXiv:2609.03560v1 (first posted 2026-09-03), https://arxiv.org/abs/2609.03560.
2. I. Sakai and T. Akimoto, *Symmetry Breaking of Current Response in Disordered Exclusion Processes*, arXiv:2512.03316v1 (2025); *Physical Review E* **113**, 044123 (2026), DOI:10.1103/21vm-n8gp.
3. B. Derrida, B. Douçot, and P.-E. Roche, *Current fluctuations in the one-dimensional symmetric exclusion process with open boundaries*, *Journal of Statistical Physics* **115**, 717–748 (2004).
