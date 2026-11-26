# Sharp payoff-blindness threshold for network public-goods imitation

## Finding and scope

Let \(G=(V,E)\) be a finite connected simple \(d\)-regular graph with \(d\ge1\). A profile is \(s\in\{0,1\}^V\), with \(s_v=1\) for a cooperator. In each closed-neighborhood group \(N[z]\), each cooperator contributes \(r>0\) units of benefit to the shared pool and pays a cost of one. Each member receives an equal share of the pool, and payoffs are accumulated across all groups a vertex joins. Thus a cooperator pays \(d+1\) in all. Let \(A\) be the adjacency matrix and \(M=(I+A)^2\). For adjacent \(x,y\) set
\[
h_z=M_{xz}-M_{yz},\qquad a_{xy}=d-1-|N(x)\cap N(y)|,\qquad H_{xy}=\tfrac12\sum_z |h_z|.
\]
Define
\[
\Theta_G(r)=\max_{\{x,y\}\in E}\max\left\{
 \left|\frac{r H_{xy}}{d+1}-(d+1)\right|,
 \left|\frac{r(2a_{xy}-H_{xy})}{d+1}-(d+1)\right|
 \right\}.
\]

Use a fixed cutoff \(\varepsilon\ge0\): replace a payoff difference \(\Delta\) by zero if \(|\Delta|<\varepsilon\), otherwise pass it unchanged to the Fermi rule at any finite temperature \(K>0\). Every opposite-strategy adjacent comparison is a fair coin in every profile **if and only if**
\[
\boxed{\Theta_G(r)=0\quad\text{or}\quad \varepsilon>\Theta_G(r).}
\]
In particular, at a *positive* threshold equality is not enough. At a zero threshold all raw differences on discordant edges already vanish, including when \(\varepsilon=0\). This exceptional case occurs on \(C_4\) at \(r=9\).

For \(G=C_L\square C_L\), \(L\ge6\),
\[
\Theta_G(r)=\max\{5+r,|11r/5-5|\}=
\begin{cases}5+r,&0<r\le25/3,\\11r/5-5,&r\ge25/3.\end{cases}
\]
In contrast, \(\Theta_{K_5}(r)=5\) for all \(r>0\), despite the same degree. In the payoff-blind regime, the asynchronous protocol that chooses a vertex uniformly and one of its neighbors uniformly is a lazy voter process. From \(b\) cooperators on \(n=|V|\) vertices it reaches consensus almost surely, with all-cooperator fixation probability \(b/n\).

## Proof

**Exact payoffs and extremizers.** A vertex \(v\) is a member of the groups centered at \(N[v]\). The sum of cooperator counts over those groups is \((Ms)_v\), so \(\pi_v=r(Ms)_v/(d+1)-(d+1)s_v\). Fix \(s_x=1,s_y=0\). Each row of \(M\) sums to \((d+1)^2\), making \(\sum_z h_z=0\). By simplicity and regularity, \(M_{xx}=d+1\), \(M_{xy}=2+|N(x)\cap N(y)|\), and therefore \(h_x=a_{xy}\ge0\) and \(h_y=-a_{xy}\). The sums of the positive and negative coefficients are \(H_{xy}\) and \(-H_{xy}\). Maximizing \(h\cdot s\) sets the free positive coefficients' spins to one and the free negative ones' spins to zero, yielding \(H_{xy}\). Minimizing takes the opposite free choices, yielding \(a_{xy}-(H_{xy}-a_{xy})=2a_{xy}-H_{xy}\). Both endpoints are attained with the prescribed opposite endpoint states. Reversing those states by complementing the whole configuration negates \(\pi_x-\pi_y\), since \(\sum_z h_z=0\). The largest absolute payoff difference over all eligible comparisons is consequently exactly \(\Theta_G(r)\).

**The zero case and the strict positive boundary.** The Fermi probability \(1/(1+\exp(\Delta_{\mathrm{eff}}/K))\) equals \(1/2\) exactly when \(\Delta_{\mathrm{eff}}=0\). A zero raw difference stays zero at every cutoff. A nonzero one becomes zero exactly if its magnitude is strictly below the cutoff. When \(\Theta_G(r)>0\), an attained maximum therefore prevents payoff blindness for every \(\varepsilon\le\Theta_G(r)\), and every comparison is neutral for \(\varepsilon>\Theta_G(r)\). On \(C_4\), \((I+A)^2=I+2J\), where \(J\) has every entry equal to one: diagonal counts are 3, and adjacent and opposite off-diagonal counts are both 2. Thus \(\pi_x-\pi_y=(r/3-3)(s_x-s_y)\), identically zero at \(r=9\).

**Torus and clique.** On the torus write \(x=(0,0),y=(1,0)\); the stencil lies in \([-2,3]\times[-2,2]\), so there are no identifications for \(L\ge6\). The row at the origin has value 5 at the origin, 2 at the four axial neighbors and the four diagonal neighbors, and 1 at the four second axial neighbors. Subtract its translate by \((1,0)\). The positive coefficients are 3 at \((0,0)\), 2 at \((-1,\pm1)\), and 1 at \((-1,0),(-2,0),(0,\pm2)\). Reflection in the line between the endpoints negates the coefficients, giving the remaining nonzero values. Thus \(a=3\), \(H=11\), and the two contrast endpoints are \(-5\) and \(11\). The affine payoff endpoints are \(-5-r\) and \(11r/5-5\), giving the displayed maximum and crossover. On \(K_5\) every group is all five vertices, so benefit is the same at all vertices and a discordant comparison has magnitude 5.

**Fixation.** The probability of selecting each ordered edge is \(1/(nd)\). Under payoff blindness each endpoint copies an opposite-strategy neighbor with probability \(1/2\); same-strategy copies do not change the profile. The opposing ordered orientations cancel their expected increments in the cooperator count, which is a bounded martingale. From any non-consensus profile a finite sequence of copies along a spanning tree leads to consensus with positive probability. Finiteness then implies almost-sure absorption. Applying bounded convergence to the expected cooperator count gives the initial fraction as the probability of all-cooperator fixation.

## Verification and limitations

The included standard-library `verify.py` directly sums group payoffs on every profile of \(C_4\) and \(K_5\) at selected rational values of \(r\). It includes the equality \(r=9,\varepsilon=0\) on \(C_4\) and checks strictness at positive examples. It obtains the torus contrast by differences of closed-neighborhood incidence counts and enumerates the free nonzero stencil on sides 6, 7 and 10. These finite corroborations do not replace the proof. The theorem fixes the shared-pool payoff and cost convention, regular graph, finite positive temperature and constant cutoff; it does not address mutation, conformity, weighted groups, dynamically estimated thresholds, or the behavior below a positive threshold. Only the fixation claim needs the specified update schedule.

## Relationship to prior work

Javarone and Singh, *Strategy Revision Phase with Payoff Threshold in the Public Goods Game*, J. Stat. Mech. (2024) 023404, [doi:10.1088/1742-5468/ad2449](https://doi.org/10.1088/1742-5468/ad2449), §2.1, use strict payoff-difference thresholding and simulation-calibrated cutoffs. The question here is instead the exact cutoff derived from the largest statewise discordant-edge contrast. The shared-pool overlapping-group convention is standard; see Perc et al., J. R. Soc. Interface 10 (2013), 20120997. The voter martingale is classical, and the finite-cutoff criterion is distinct from a large-noise limit for unthresholded imitation. These comparisons do not establish historical priority.
