# Exact all-transient coexistence threshold and finite-size crossover for rule-128 trajectories

## Finding
For the radius-one binary cellular automaton \(F\) on the periodic ring \(\mathbb Z/N\mathbb Z\), where \(F(x)_i=x_{i-1}x_ix_{i+1}\), fix any integer transient length \(p\ge1\), ring length \(N\ge3\), and real chemical potential \(\mu\). Consider the partition function of initial states entering the fixed-point set within \(p\) updates:
\[
Z_{N,p}(\mu)=\sum_{x\in\{0,1\}^N:\;F^{p+1}(x)=F^p(x)}\exp\!\left(\mu\sum_i x_i\right).
\]
Set \(m=2p+1\) and \(z=e^\mu>0\). Define the \(m\)-state run-length matrix \(T_m(z)\), indexed by \(0,\ldots,m-1\), by
\[
(T_m(z))_{r,0}=1\quad(0\le r<m),\qquad (T_m(z))_{r,r+1}=z\quad(0\le r<m-1),
\]
with all other entries zero. **For every such \(p,N,\mu\)**,
\[
Z_{N,p}(\mu)=z^N+\operatorname{tr}\big(T_m(z)^N\big).
\]
Let \(\lambda_m(z)\) be the Perron root of \(T_m(z)\). It is the unique positive solution of
\[
\sum_{r=0}^{m-1}\frac{z^r}{\lambda_m(z)^{r+1}}=1.
\]
The thermodynamic pressure exists and is
\[
P_p(\mu)=\lim_{N\to\infty}\frac{\log Z_{N,p}(\mu)}N
=\max\{\mu,\log\lambda_m(e^\mu)\}.
\]
It has **exactly one first-order transition**, located at
\[
\boxed{\mu_c(p)=\log(2p+1)}.
\]
At this transition, the left and right derivatives of pressure are respectively
\[
\boxed{P_p'(\mu_c^-)=\frac p{p+1},\qquad P_p'(\mu_c^+)=1.}
\]
Thus the density jump is exactly \(1/(p+1)\). At the critical potential, the limiting probability of the all-ones initial state is \(1/2\), and the limiting expected initial density is \((2p+1)/(2p+2)\).

For every fixed real \(t\), set \(\mu_N=\mu_c+t/N\), and use the Gibbs distribution defined by the summands in \(Z_{N,p}(\mu_N)\). Its all-ones probability has the **finite-size scaling limit**
\[
\boxed{\lim_{N\to\infty}\Pr_{N,p,\mu_N}(x=\mathbf 1)=\frac1{1+\exp(-t/(p+1))}.}
\]
The limiting expected initial density in the same window is \(p/(p+1)+(1/(p+1))(1+\exp(-t/(p+1)))^{-1}\). The scaling parameter \(t\) is fixed while \(p\) is fixed and \(N\to\infty\); no joint \(p,N\) limit is asserted.

## Assumptions and scope
The update is synchronous Boolean AND, with periodic spatial indices. The transient condition is *at most* \(p\) steps to a fixed configuration, not exact first-hitting time \(p\). The ring is finite before the limit; \(p\ge1\), \(N\ge3\), \(z>0\). The only fixed states of \(F\) on a ring are the all-zero and all-one states. The two contributions to the partition function are mutually exclusive and correspond to their respective basins. A transition of this weighted initial-condition ensemble is not a dynamical bifurcation of the update rule.

## Proof
**1. Iterates and the exact basin partition.** The Boolean AND product is idempotent. Inductively, for each integer \(q\ge0\),
\[
F^q(x)_i=\prod_{j=-q}^q x_{i+j},
\]
where wrapped indices may repeat without altering a Boolean product. A fixed configuration containing a one has both of its neighbors equal to one, hence is globally all one; otherwise it is all zero. The iterate \(F^p(x)\) is all one if and only if \(x=\mathbf1\). It is all zero precisely when every circular block of \(m=2p+1\) consecutive positions contains a zero, equivalently when the periodic word avoids \(1^m\). Thus the initial states entering the fixed-point set by time \(p\) are the disjoint union of the single all-ones word and circular words avoiding \(1^m\). This equivalence remains true when \(m>N\), because the circular blocks use periodic indices.

**2. Exact finite-volume counting.** The state \(r\in\{0,\ldots,m-1\}\) records the current terminal run of ones. Appending zero resets to state zero with weight one; appending one advances to \(r+1\) with weight \(z\), unless \(r=m-1\), when it is prohibited. A closed state walk of length \(N\) therefore corresponds uniquely to a circular word with a zero and no circular run \(1^m\): the tracked state at each position is uniquely determined by the word's last zero (and bounded run length). Conversely, every such word determines its closed walk, including rings of length shorter than \(m\). The matrix trace counts these words with weight \(z^{\#1}\). The separate all-ones word adds \(z^N\). Hence the asserted partition identity.

**3. Perron root, pressure, and uniqueness of the crossing.** For every \(z>0\), the directed graph of \(T_m(z)\) is strongly connected and has a self-loop at state zero; the matrix is primitive. Its Perron root is simple, analytic in \(z\), and strictly dominant over the moduli of all other eigenvalues. An eigenvector or first-return decomposition yields the root equation above. Its left side is strictly decreasing from infinity to zero as \(\lambda\) runs through positive reals, proving uniqueness. Perron–Frobenius gives
\[
\operatorname{tr}(T_m(z)^N)=\lambda_m(z)^N(1+o(1))
\]
for fixed \(z>0\). Therefore the pressure is the maximum of \(\mu\) and \(\log\lambda_m(e^\mu)\). Evaluate the root equation at \(\lambda=z\): the sum is exactly \(m/z\). Since the sum decreases with \(\lambda\), we have \(\lambda_m(z)>z\) for \(z<m\), equality only at \(z=m\), and \(\lambda_m(z)<z\) for \(z>m\). This proves the unique transition at \(\mu=\log m\).

**4. Density slopes.** Define \(\rho(z)=d\log\lambda_m(z)/d\log z\). Differentiate the identity
\[
\sum_{r=0}^{m-1}z^r\lambda_m(z)^{-r-1}=1.
\]
At \(z=\lambda_m(z)=m\), all \(m\) summands equal \(1/m\). Consequently,
\[
\rho(m)=\frac{\sum_{r=0}^{m-1}r}{\sum_{r=0}^{m-1}(r+1)}=\frac{m-1}{m+1}=\frac p{p+1}.
\]
For \(z<m\), pressure follows the Perron branch; for \(z>m\) it is \(\mu\) with derivative one. The two derivatives differ, so the transition is first-order. Analyticity of the Perron root excludes other singularities on either side.

**5. Logistic critical window.** Put \(\mu_N=\log m+t/N\). Analyticity gives
\[
\log\lambda_m(e^{\mu_N})=\log m+\frac{\rho(m)t}{N}+O(N^{-2}).
\]
The primitive matrix has a locally uniform spectral gap around \(z=m\). Hence \(\operatorname{tr}(T_m(e^{\mu_N})^N)=m^N\exp(\rho(m)t+o(1))\), while the isolated all-ones contribution is exactly \(m^N e^t\). Dividing proves the logistic limit with exponent \((1-\rho(m))t=t/(p+1)\). At \(t=0\) the weights tend to equal halves. Differentiating the analytic matrix trace, or using its normalized Perron projection, shows the forbidden-word branch's mean density tends to \(\rho(m)\) in this window. The mixture gives the claimed limiting total density.

## Verification
Run `python3 verify.py` with standard Python, with no additional packages. Its independent finite enumerator evolves the cellular automaton explicitly and compares each admissible weighted state sum to both circular word avoidance and the trace formula. It also compares the full Boolean iterate identity to direct evolution for wrapped neighborhoods and checks rational critical root and density identities. The recorded run passed **8,488 exact assertions**. These finite checks support the formulas but do not prove the infinite-volume claims; those follow from the derivations above.

## Relationship to prior work
Koller and Hudcová (2025), in their Figure 4 and accompanying discussion, study exactly the weighted fixed-point-basin ensemble for elementary cellular automaton rule 128, plot entropy-density curves for several transient lengths, and describe a first-order-like jump for one step. Their general transfer-matrix method counts short trajectories but does not state the exact all-transient crossing \(\mu_c(p)=\log(2p+1)\), density jump \(1/(p+1)\), or the logistic finite-size window derived here. The reduction to an \(m\)-state forbidden-run transfer matrix is significantly smaller than their generic space-time representation. Lind's classical work gives general counting and zeta-function methods for a forbidden word; that foundational method is not claimed as new. Work on letter frequencies of one-forbidden-word shifts also addresses the mixing branch itself, not the competition with the separate all-ones absorbing trajectory. The contribution here is the combined exact dynamical-basin identification and sharp weighted coexistence/scaling laws, not the general transfer-matrix or Perron–Frobenius technique.

## Limitations
The theorem concerns rule 128 only, a fixed finite transient parameter \(p\), periodic rings, and a chemical-potential ensemble on initial states. It does not imply a phase transition in the unweighted dynamical evolution, for general elementary rules, or in a limit where \(p\) grows with \(N\). Generic forbidden-word transfer results could admit an equivalent specialization, and a full-text inspection of every potentially relevant historical source has not been established; priority thus remains provisional despite the explicit literature comparison. Independent external scientific validation has not been performed.

## References
1. C. Koller and B. Hudcová, *Counting Short Trajectories in Elementary Cellular Automata using the Transfer Matrix Method*, arXiv:2508.09768v1 (first posted 13 August 2025), https://arxiv.org/abs/2508.09768 . The full-text Figure 4 discussion was inspected at https://www.researchgate.net/publication/394473434_Counting_Short_Trajectories_in_Elementary_Cellular_Automata_using_the_Transfer_Matrix_Method .
2. D. A. Lind, *Perturbations of Shifts of Finite Type*, SIAM Journal on Discrete Mathematics **2** (1989), 350–365, https://doi.org/10.1137/0402031 .
3. M. Bóna, B. Maga, and J. Richey, *Letter frequency in shifts of finite type with one forbidden word*, arXiv:2606.06655 (2026), https://arxiv.org/abs/2606.06655 .
