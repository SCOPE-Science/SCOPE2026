# Three environmental regimes are necessary for an interior optimum in stationary patch occupancy

## Finding
Consider one habitat patch with state \(X\in\{0,1\}\), where zero means empty and one means occupied. Its exogenous environment \(E\) changes autonomously according to a continuous-time Markov chain. In environmental state \(i\), colonization \(0\to1\) occurs at rate \(c_i>0\) and extinction \(1\to0\) at rate \(e_i>0\). Let \(P(q)=\Pr_{\mathrm{stat}}(X=1)\) for environmental switching speed \(q>0\).

**Sharp regime-count boundary.** With one environmental state, occupancy is independent of switching speed. With two states, for every pair of positive base transition rates, multiplying both environmental transition rates by the same speed \(q\) makes \(P(q)\) either strictly monotone or constant: no strict interior optimal speed is possible. With three states, even if every ordered pair of distinct environmental states has identical transition rate \(q\), \(P(q)\) can have a unique strict global maximum at a positive finite speed.

For the three-state example
\[
(c_1,c_2,c_3)=(1,7,7),\qquad(e_1,e_2,e_3)=(1,1,7),
\]
with environmental transitions \(i\to j\) at rate \(q\) for \(i\ne j\),
\[
P(q)=\frac{45q^2+204q+140}{8(9q^2+39q+28)}
=\frac58+\frac{9q}{8(9q^2+39q+28)}.
\]
Thus \(\lim_{q\downarrow0}P(q)=\lim_{q\to\infty}P(q)=5/8\), but every finite \(q>0\) improves occupancy. The **unique** maximizer and its attained value are
\[
q_* = \frac{2\sqrt7}{3},\qquad P(q_*)=\frac{27-\sqrt7}{38}>\frac58.
\]
Three is therefore the least number of environmental regimes that permits a strict interior stationary-occupancy optimum in this class.

## Assumptions and scope
The environment is an autonomous finite-state continuous-time Markov chain, unaffected by patch occupancy. Conditional on the current environment, patch colonization and extinction are memoryless with the positive rates stated above. In the two-state case, the environmental rates are \(1\to2\) at \(qa\) and \(2\to1\) at \(qb\), with \(a,b,q>0\). In the three-state construction, the environment is the symmetric complete three-state chain with off-diagonal generator entries \(q>0\). The stationary joint law exists uniquely for every \(q>0\). Values at \(q=0\) and \(q=\infty\) mean one-sided limits; the joint chain need not have a unique stationary law when \(q=0\).

For the auxiliary \(n\)-regime identity below, \(n\ge2\) and each distinct environmental pair has equal jump rate \(q\). The claim concerns **stationary occupancy**, not transient occupancy, extinction times, multisite persistence, or optimization under a fixed switching cost.

## Proof
Put \(s_i=c_i+e_i>0\) and \(\theta_i=c_i/s_i\), the isolated occupancy probability and total occupancy turnover rate in regime \(i\).

**Two regimes.** The autonomous environment has stationary probabilities \(\pi_1=b/(a+b)\) and \(\pi_2=a/(a+b)\). Set \(u_i=\Pr_{\mathrm{stat}}(E=i,X=1)\). Stationary flux balance yields
\[
(s_1+qa)u_1-qbu_2=\pi_1c_1,\qquad
-qau_1+(s_2+qb)u_2=\pi_2c_2.
\]
The determinant is \(s_1s_2+q(bs_1+as_2)>0\). Solving and summing the two occupied probabilities gives
\[
P(q)=\frac{\pi_1c_1s_2+\pi_2c_2s_1+q(bc_1+ac_2)}
{s_1s_2+q(bs_1+as_2)}.
\]
Differentiating and simplifying produces the exact sign formula
\[
P'(q)=
\frac{ab\,s_1s_2(s_1-s_2)(\theta_1-\theta_2)}
{(a+b)[s_1s_2+q(bs_1+as_2)]^2}.
\]
Its sign does not depend on \(q\). Equality holds identically precisely if \(s_1=s_2\) or \(\theta_1=\theta_2\). This proves the two-regime impossibility, including arbitrary fixed asymmetry in switching rates.

**Symmetric \(n\)-regime reduction.** For the complete environmental generator with all off-diagonal rates \(q\), the stationary environment marginal is uniform, \(1/n\). Define \(u_i=\Pr(E=i,X=1)\) and \(P=\sum_i u_i\). Stationary flux balance reads
\[
(s_i+nq)u_i-qP=\frac{c_i}{n}.
\]
Hence \(u_i=(c_i/n+qP)/(s_i+nq)\). Sum and use
\(\sum_i s_i/(s_i+nq)=n-nq\sum_i1/(s_i+nq)\) to obtain the exact identity
\[
\boxed{P(q)=\frac{\sum_{i=1}^n c_i/(s_i+nq)}
{\sum_{i=1}^n s_i/(s_i+nq)}.}
\]
Every denominator is positive. This is a varying-weight average of the isolated occupancies \(\theta_i\), with weights proportional to \(s_i/(s_i+nq)\). It also immediately gives the slow-switching limit \(\sum_i\theta_i/n\) and fast-switching limit \(\sum_i c_i/\sum_i s_i\).

**Three-regime sharp example.** For \(c=(1,7,7)\) and \(e=(1,1,7)\), substitute \(s=(2,8,14)\) into the boxed formula and clear positive denominators. Direct expansion gives the rational expression in the Finding. Its derivative is
\[
P'(q)=\frac{9(28-9q^2)}{8(9q^2+39q+28)^2}.
\]
It is positive for \(0<q<2\sqrt7/3\), zero at \(q=2\sqrt7/3\), and negative for all larger \(q\). The listed stationary limits and maximum follow by substitution. A strict interior maximum is impossible with fewer than three regimes by the preceding two-regime theorem. This completes the proof.

## Verification
The accompanying `verify.py` builds the full \(2n\)-state continuous-time generator independently of the closed formulas, solves its stationary linear system with exact rational arithmetic, and compares both representations for 319 rational parameter cases across two, three, and four environmental regimes, including asymmetric two-state switching. It also symbolically checks the three-state rational law, derivative, stationary endpoint limits, the unique critical speed, and the exact value at the optimum. Execute with `python verify.py` in an environment with SymPy. The universal statements rest on the displayed algebra, not on these finite checks.

## Relationship to prior work
MacKenzie and colleagues (2003) developed occupancy models with separate colonization and extinction processes. Yackulic and colleagues (2015) analyzed how different fixed environmental colonization–extinction rates change transient occupancy and environmental association; their displayed two-environment equations keep environmental identity fixed, not Markov switching. Fidino, Simonis and Magle (2018) give a general multi-state occupancy framework and calculate stationary occupancy from transition matrices, but their inspected analysis does not classify the effect of a **common environmental switching-speed multiplier**, establish the two-regime monotonicity obstruction, or give the three-regime sharp counterexample. Smith (2017) considers spatial metapopulations in stochastic environments and addresses extinction conditions; only its accessible abstract was inspected. Generic finite-state Markov-chain stationary linear algebra can reproduce an example once specified; the claim here is the sharp qualitative *minimum number of environmental states* needed for nonmonotonic response, with an exact optimizable witness, not the existence of stationary distributions.

## Limitations
The theorem does not claim that two-regime stochastic ecological models in general have monotone responses: internal density dynamics, feedback, catastrophe processes, habitat interactions, and different objective functions may create other behavior. Only environmental transition rates are multiplied by \(q\); local colonization and extinction rates remain fixed. The complete-graph \(n\)-state identity assumes symmetric all-to-all environmental transition rates. The numbers in the example are dimensionless rates and are not estimates from field observations. A more general treatment of stationary responses to environmental switching could encompass parts of the claim; the originality comparison is based on accessible primary literature and targeted research records, not exhaustive historical certification.

## References
1. MacKenzie, D. I., Nichols, J. D., Hines, J. E., Knutson, M. G. & Franklin, A. B. (2003). Estimating site occupancy, colonization, and local extinction when a species is detected imperfectly. *Ecology*, 84, 2200–2207. doi:10.1890/02-3090.
2. Yackulic, C. B., Nichols, J. D., Reid, J. & Der, R. (2015). To predict the niche, model colonization and extinction. *Ecology*, 96, 16–23. doi:10.1890/14-1361.1. Full text: https://research.fs.usda.gov/download/treesearch/49806.pdf.
3. Fidino, M., Simonis, J. L. & Magle, S. B. (2018, online). A multistate dynamic occupancy model to estimate local colonization–extinction rates and patterns of co-occurrence between two or more interacting species. *Methods in Ecology and Evolution*. doi:10.1111/2041-210X.13117.
4. Smith, A. G. (2017). A spatially structured metapopulation model within a stochastic environment. *Mathematical Biosciences*, 291, 46–55. doi:10.1016/j.mbs.2017.07.003 (abstract inspected; full text not accessed).
