# Disproof of the finite GT-cuspidal criterion at (p,S)=(5,{2,5}) on the class-3 exponent-25 quotient

## Context

Let $X=\mathbf{P}^1_{\mathbf{Q}}\setminus\{0,1,\infty\}$, $\Pi$ its geometric pro-$5$ fundamental group, and $Q_3$ the finite class-3 exponent-$25$ quotient of $\Pi$ with explicit Hall-basis presentation. Push out to $1\to Q_3\to E_3\to G_{\mathbf{Q},S}\to 1$ with $S=\{2,5\}$, where $G_{\mathbf{Q},S}$ is the Galois group of the maximal extension of $\mathbf{Q}$ unramified outside $S$ and $\infty$.

The admitted target asked whether, for a continuous section $s:G_{\mathbf{Q},S}\to E_3$ with Ihara power series $F_s$ truncated at total degree $3$ over $R=\mathbf{Z}/25$ and Soulé invariant $\kappa_3(s)\bmod 25$, the following holds: $s$ satisfies the truncated hexagon and pentagon equations in $Q_3$ and has $\kappa_3(s)=0\bmod 25$ if and only if $s$ is $Q_3$-conjugate into a cuspidal decomposition group $D_0$, $D_1$ or $D_\infty$. A proof of the equivalence or an explicit Hall-coordinate section satisfying the equations and $\kappa_3=0$ but provably non-cuspidal decides it.

## Definitions

- $R=\mathbf{Z}/25$. $L$ is the free nilpotent Lie algebra of class $3$ on generators $A,B$ over $R$, with Hall basis $A,B$ (degree 1), $C=[A,B]$ (degree 2), $D=[A,[A,B]]$, $E=[B,[A,B]]$ (degree 3). $Q_3=\exp(L)$ via truncated Baker–Campbell–Hausdorff (BCH); $|Q_3|=25^5$, exponent $25$ (valid since $5>$ class and denominators $2,12$ are units mod $25$).
- $E_3=Q_3\rtimes G_{\mathbf{Q},S}$ with cyclotomic-weight action $\sigma\cdot v=\chi(\sigma)^k v$ in degree $k$, $\chi$ the mod-$25$ cyclotomic character.
- $\rho_2:G_{\mathbf{Q},S}\to R(1)$ is the Kummer $1$-cocycle of $2\in\mathcal{O}_S^\times$, ramified only at $2$ (hence factors through $G_{\mathbf{Q},S}$).
- For a section $s$, $F_s=\exp(\gamma C+\delta D+\varepsilon E)$ is the commutator part; $\kappa_3(s)$ is the section-dependent degree-$3$ Soulé invariant, i.e. a fixed $R$-linear form in $(\delta,\varepsilon)$ against the cyclotomic-unit ledger.
- Kummer ledger: $H^1(G_{\mathbf{Q},S},R(1))\cong \mathcal{O}_S^\times/25$. Since $\mathbf{Q}$ has class number $1$, $\mathcal{O}_S^\times=\{\pm1\}\times 2^{\mathbf{Z}}\times 5^{\mathbf{Z}}$, and $(-1)^{25}=-1$ kills torsion mod $25$, so $V:=\mathcal{O}_S^\times/25\cong(\mathbf{Z}/25)^2$ via $(2,5)$. The abelianization coordinates are $(b,a)\in V^2$.
- Cuspidal ledgers: $a=1$ (cusp $0$, since $1-t\equiv1$), $b=1$ (cusp $1$, since $t\equiv1$), $b=\pm a$ (cusp $\infty$, diagonal inertia $(xy)^{-1}$; sign invisible mod $25$).

## Result

**Theorem.** Fix $p=5$, $S=\{2,5\}$, $R=\mathbf{Z}/25$ and $Q_3,E_3$ as above. The stated finite GT-cuspidal equivalence is **false**. The section
$$ \phi(\sigma)=\rho_2(\sigma)\cdot V,\qquad V=A+2B,\qquad s(\sigma)=(\exp\phi(\sigma),\sigma)\in E_3 $$
is a genuine continuous section whose commutator part $F_s=1$ satisfies the truncated hexagon (symmetry and $3$-cycle) and pentagon ($5$-cycle) equations with $\kappa_3(s)=0\bmod 25$, while its Kummer ledger $(b,a)=([2],[4])=((1,0),(2,0))$ lies off all cuspidal lines, so no $Q_3$-conjugate of $s$ lands in $D_0,D_1$ or $D_\infty$. Hence the only-if direction fails.

## Proof / Evidence

**Lemma 1 (genuine section).** All values $\phi(\sigma)$ are collinear (scalar multiples of $V$), so every bracket $[\phi(\sigma),\phi(\tau)]$ vanishes and BCH multiplication is ordinary addition on the line $R\cdot V$. The line is $G$-stable (homogeneous weight $1$). Hence $\phi(\sigma\tau)=\phi(\sigma)+\sigma\cdot\phi(\tau)=\phi(\sigma)\ast\sigma\cdot\phi(\tau)$ exactly, using the Kummer cocycle identity for $\rho_2$. So $s$ is a continuous homomorphism splitting $E_3\to G_{\mathbf{Q},S}$. Machine-checked over all residues mod $25$ and representative Frobenius weights ($5000$ cases).

**Lemma 2 (hexagon, pentagon, $\kappa_3$).** $F_s=\exp(0)=1$ identically ($\gamma=\delta=\varepsilon=0$). Then $1$ satisfies $\Phi(Y,X)=\Phi(X,Y)^{-1}$, $\Phi(Z,X)\Phi(Y,Z)\Phi(X,Y)=1$ and the $5$-cycle pentagon relation trivially. The degree-$3$ Hall components vanish identically, so every fixed $R$-linear Soulé form $\kappa_3$ gives $0\bmod 25$. Remark: no degree-$2$ obstruction either — $a=2b$ and $b\cup b$ is $2$-torsion, so $b\cup a=2(b\cup b)=0$ since $2$ is a unit mod $25$; the lift with zero higher terms is exhibited explicitly. Collinear cup vanishes (checked over all $25^2$ pairs).

**Lemma 3 (provably non-cuspidal).** The ledger is $(b,a)=([2],[4])$ with $[2]$ of exact order $25$. Cuspidal sections lie on $a=1$, $b=1$, or $b=\pm a$. Here $a\ne1$, $b\ne1$, $b-a=-[2]\ne1$, $b+a=[8]\ne1$ under either sign convention. $Q_3$-conjugation changes a section by a coboundary, preserving its class in $H^1(G,Q_3^{\mathrm{ab}})$; hence no $Q_3$-conjugate lands in $D_0,D_1,D_\infty$.

Therefore $s$ satisfies all hypotheses but violates the conclusion; the iff at level $(3,25,S)$ is disproved. The if direction is unaffected: cuspidal rank-$1$ lifts with $F=1$ also satisfy the equations.

## Limitations

Finite-level statement only: says nothing about the full pro-$5$ or infinite-level GT-cuspidal conjecture or section conjecture. $\kappa_3=0$ is read as the section-dependent degree-$3$ Soulé invariant (standard graded-piece reading), which vanishes because the degree-$3$ part vanishes identically. Cuspidal ledger lines use the standard Hensel/residue-characteristic-zero identification ($25\ne0$ in residue characteristic), robust under both diagonal sign conventions.

## Reproducibility

`output/artifacts/verify.py` (run `python3 output/artifacts/verify.py`) checks: $V$-structure and exact order $25$; ledger off all cuspidal lines (both signs); cocycle identity on $5000$ $(\chi,r_1,r_2)$ cases; hexagon symmetry/$3$-cycle and pentagon $5$-cycle at $F=1$; $\kappa_3=0$; BCH associativity ($300$ triples), exponent $25$, $G$-equivariance; vanishing collinear cup. Output: ALL CHECKS PASSED. BCH uses $1/2=13$, $1/12=23\bmod25$; $G$-action by weights $(1,1,2,3,3)$.

## References

- Dror Bar-Natan, On associators and the Grothendieck-Teichmuller group I (1996/1998).
- Hidekazu Furusho, Pentagon and hexagon equations (Annals of Mathematics report).
- Yuichiro Hoshi, Shinichi Mochizuki, Partial Combinatorial Cuspidalization; Topics Surrounding Combinatorial Anabelian Geometry (Springer 2022).
- Pierre Lochak, Hiroaki Nakamura, Leila Schneps, Eigenloci of 5 point configurations and the Grothendieck-Teichmuller group.
- Hiroaki Nakamura, Some classical views on the parameters of the Grothendieck-Teichmuller group.
- Standard S-unit/Kummer theory: $\mathbf{Q}$ class number $1$; $\mathcal{O}_{\{2,5\}}^\times/25\cong(\mathbf{Z}/25)^2$.
