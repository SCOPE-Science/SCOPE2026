# Sharp exponential onset orders in mass-action reaction networks

## Finding

A finite reaction network determines not just which initially absent species become positive, but the **first nonzero Taylor order** of every such species, independently of the values of its positive reaction-rate constants. The orders satisfy a weighted min-plus recursion on the productive reaction hypergraph. When the largest total reactant molecularity is \(m\geq 1\) and exactly \(s\) initially absent species are eventually activated, the greatest possible finite onset order is exactly
\[
H_m(s)=\begin{cases}s,&m=1,\\\dfrac{m^s-1}{m-1},&m\geq2.\end{cases}
\]
This bound is attained for every pair of integers \(m,s\geq1\) by a serial mass-action network. In particular, bimolecular reactants can produce a species with first nonzero derivative of order \(2^s-1\), despite the species having positive concentration for every sufficiently small positive time.

More precisely, let \(\mathcal S=\{1,\ldots,q\}\) and \(\mathcal R\) be finite. Each reaction \(r\) has input vector \(\alpha_r\in\mathbb N_0^q\), output vector \(\beta_r\in\mathbb N_0^q\), and constant \(k_r>0\). The corresponding solution starts from \(c(0)\in\mathbb R_{\ge0}^q\) and obeys
\[
\dot c_i=\sum_{r\in\mathcal R}(\beta_{ri}-\alpha_{ri})k_r\prod_{j=1}^{q}c_j^{\alpha_{rj}}.
\]
Define \(h_i=0\) if \(c_i(0)>0\). For initially absent species, start with \(h_i=\infty\) and repeatedly apply the update
\[
h_i\leftarrow\min\left\{h_i,\;1+\sum_j\alpha_{rj}h_j:\ r\in\mathcal R,\ \alpha_{ri}=0,\ \beta_{ri}>0\right\},
\]
where any term involving an infinite reactant order is omitted. At most \(q\) rounds of simultaneous updates suffice. If \(h_i=\infty\), then \(c_i(t)\) is identically zero while the solution exists. Otherwise \(h_i\) is exactly the least nonzero Taylor degree of \(c_i(t)\) at zero: there is \(a_i>0\) such that
\[
c_i(t)=a_i t^{h_i}+O(t^{h_i+1})\qquad(t\downarrow0).
\]
The leading coefficients are also explicit. For \(h_i>0\), let \(\mathcal P_i\) be the reactions having \(\alpha_{ri}=0\) and \(\beta_{ri}>0\) that attain the minimum. Then
\[
a_i={1\over h_i}\sum_{r\in\mathcal P_i}\beta_{ri}k_r\prod_j a_j^{\alpha_{rj}},
\]
with \(a_j=c_j(0)\) when \(h_j=0\). This is a finite, positive recursion ordered by increasing finite \(h_j\).

## Assumptions and scope

All reactions use integer nonnegative input/output stoichiometries, strictly positive time-independent mass-action rate constants, and finite species and reaction sets. The initial data are nonnegative. The exponent bound uses \(\sum_j\alpha_{rj}\le m\) for every reaction, with \(m\) a positive integer; no bound on output molecularity is needed. If no initially absent species becomes positive, take \(s=0\) and the bound is vacuous. A zero input vector is allowed, corresponding to external inflow. The conclusion concerns the classical solution on its maximal existence interval and the exact analytic Taylor germ at the initial instant, **not** long-time persistence or a uniform quantitative detection time.

The productive hyperedges are reactions creating species \(i\) **without requiring that same species as a reactant**: precisely \(\alpha_{ri}=0\) and \(\beta_{ri}>0\). Reactions consuming an already-present species, or reactions which need a missing product as a reactant, are treated by the full mass-action ODE but do not directly seed that product. For every finite onset order, the solution becomes strictly positive at that coordinate for all sufficiently small positive times. In fact, the positivity persists at every later finite time of existence by the standard differential inequality described below.

## Proof

**1. Positive production separates from terms containing the species.** For every coordinate \(i\), partition the right side into reactions with \(\alpha_{ri}=0\) and reactions with \(\alpha_{ri}\ge1\). The first group contributes only nonnegative terms because \(\beta_{ri}\ge0\), while every term in the second group contains a factor \(c_i\). Thus
\[
\dot c_i=P_i(c)+c_iQ_i(c),\qquad
P_i(c)=\sum_{\substack{r:\alpha_{ri}=0}}\beta_{ri}k_rc^{\alpha_r}\ge0,
\]
where \(Q_i\) is a polynomial and \(c^{\alpha_r}=\prod_jc_j^{\alpha_{rj}}\). By variation of constants, for an initially absent coordinate,
\[
c_i(t)=\int_0^t P_i(c(u))\exp\!\left(\int_u^tQ_i(c(v))\,dv\right)du.
\]
The exponential is strictly positive. A coordinate initially present remains positive at finite positive times because its equation has nonnegative forcing and a bounded coefficient \(Q_i\) on every compact solution interval.

**2. Exact support and finite constructive orders.** Begin with \(S_0=\{i:c_i(0)>0\}\); at each closure round adjoin each product of a reaction whose entire reactant multiset is already in the current set. Every newly added species has an input-available producing reaction. The integral formula and induction therefore make it positive for every positive time within existence. Conversely, if a species is outside the eventual closure, every reaction that could produce it from a boundary face requires at least one species outside that face. The face with all outside concentrations zero is forward invariant by uniqueness of the polynomial ODE. Hence no outside species appears. This proves that exactly the species in the closure become positive.

Because polynomial ODE solutions are real analytic near the initial time, a coordinate in the closure has an expansion \(c_i(t)=a_it^{h_i}+O(t^{h_i+1})\) with a finite nonnegative integer exponent and \(a_i>0\); initially present species have \(h_i=0\). If a productive reaction \(r\) uses only species with finite orders, its monomial has leading term
\[
c(t)^{\alpha_r}=\left(\prod_j a_j^{\alpha_{rj}}\right)t^{\sum_j\alpha_{rj}h_j}+\text{higher powers}.
\]
Every coefficient in \(P_i\) is nonnegative, so the smallest such exponent cannot cancel with another. The integrating factor in step 1 is \(1+O(t)\) uniformly for \(0\le u\le t\). Integrating the first nonzero term gives precisely
\[
h_i=1+\min_{\substack{r:\alpha_{ri}=0,\ \beta_{ri}>0}}\sum_j\alpha_{rj}h_j
\]
with the stated positive coefficient recursion. If no productive reaction has all finite-order reactants, the coordinate is outside the closure and identically zero. In every minimizer, a reactant with nonzero multiplicity has \(h_j\le h_i-1\). Thus the coefficient recursion is acyclic when ordered by the integer \(h_i\), even if the full reaction hypergraph contains cycles.

Equivalently, a production derivation tree assigns a cost \(0\) to each initially positive leaf and cost \(1+\sum_j\alpha_{rj}(\text{child cost})\) to a productive reaction node. The minimum cost for a target is its \(h_i\). In any minimum-cost derivation, no initially absent species repeats along an ancestor–descendant path: a repeated descendant gives an admissible smaller-cost derivation of the same species, because each intervening reaction contributes a strictly positive unit. Hence at most \(q\) simultaneous relaxation rounds recover all finite minima (or \(s\) rounds if \(s\) initially absent species are reached).

**3. Universal sharp bound.** Suppose exactly \(s\) initially absent species belong to the closure. Define \(H_0=0\) and \(H_\ell=1+mH_{\ell-1}\). By induction, every species first added by the \(\ell\)-th closure round has \(h_i\le H_\ell\): a witnessing reaction has at most \(m\) input molecules, all from earlier rounds with orders at most \(H_{\ell-1}\). There are at most \(s\) nonempty rounds. Consequently \(h_i\le H_s\) for every activated species, and solving the recurrence gives the claimed formula.

**4. Sharpness at every molecularity and size.** Fix integers \(m,s\ge1\). Consider \(s\) species, initially all at concentration zero, and the unit-rate reactions
\[
\varnothing\longrightarrow X_1,\qquad
mX_j\longrightarrow(m-1)X_j+X_{j+1}\quad(1\le j<s).
\]
Every reaction has at most \(m\) reactants and no product requires its own presence. The dynamics are triangular: \(\dot x_1=1-x_1^m\) when \(s>1\), \(\dot x_j=x_{j-1}^m-x_j^m\) for \(1<j<s\), and \(\dot x_s=x_{s-1}^m\) for \(s>1\). For \(s=1\), simply \(\dot x_1=1\). Starting at zero, the recursion yields \(h_1=1\) and \(h_{j+1}=1+mh_j\), so \(h_s=H_s\). When \(m=2\) and \(s=4\), the orders are \(1,3,7,15\), and the leading coefficients for unit rates are \(1,1/3,1/63,1/59535\). This proves sharpness even with binary reactant complexes when \(m=2\). \(\square\)

## Verification

The included standalone Python script `activation_checker.py` computes the first eleven exact Taylor coefficients of random small mass-action systems using rational arithmetic; it independently computes the hypergraph orders and their leading coefficients and checks agreement. It also checks the extremal serial construction for molecularities \(m=1,2,3\) and sizes up to four. Running `python activation_checker.py` produced `PASS: 152 exact rational checks; sharp chains for m=1,2,3 and s<=4`. The script is finite diagnostic support, not an exhaustive classification or a substitute for the analytic proof. The universal statements follow from steps 1–4.

## Relationship to prior work

Peter and Ibrahim, *A Structural Theory of Admissible Transitions in Biological Reaction Networks* (arXiv:2608.27201v1, first public 27 August 2026), establish closure-building and species-presence transitions without assigning a quantitative order of appearance. Their Sections 2–5 and the original result statements distinguish structure from kinetics and describe quantitative refinements as future work. The theorem here specializes to polynomial mass-action kinetics and computes the first nonzero time-Taylor order as an invariant of the reaction structure, together with a sharp molecularity-dependent bound.

Vance, Arkin and Ross, *Determination of causal connectivities of species in reaction networks* (PNAS 99, 2002), study how perturbation pulses propagate from equilibria or stationary states and how extrema reflect reaction connectivity. Their first-order-chain observations motivate onset-order questions, but the published analysis does not assert the all-zero-boundary min-plus recursion or the sharp exponential degree bound for arbitrary mass-action reaction hypergraphs.

Soliman, Fages and Radulescu, *A constraint solving approach to model reduction by tropical equilibration* (Algorithms for Molecular Biology 9, 2014), apply min-plus algebra to balancing dominant monomials in parameter-scale model reduction and fast/slow equilibration. That is methodologically related but compares distinct asymptotic objects: equilibrium constraints versus positive production at the initial-time boundary. General chemical-organization theory also supplies closure notions; a closure predicate alone does not determine the magnitude of the leading Taylor derivative.

## Limitations

Strict positivity of all stated reaction-rate constants is essential for rate-independent orders: zero rates change the productive hypergraph. Mass-action polynomial kinetics and nonnegative initial data are essential for the no-cancellation argument. The bound is sharp as a function of reactant molecularity and activated species count but says nothing about optimal simulation step sizes, absolute detection times for specified thresholds, or long-time persistence. A very high onset order can coexist with instantaneous positivity because \(t^{h_i}>0\) for every \(t>0\). No claim is made about models with externally imposed discontinuous interventions, negative reaction fluxes, delays, or nonanalytic kinetics. The min-plus method shares ideas with older tropical and network-connectivity methods; the possibility of an equivalent unindexed formulation is a residual originality risk.

## References

1. S. Peter and B. Ibrahim, *A Structural Theory of Admissible Transitions in Biological Reaction Networks*, arXiv:2608.27201v1 (27 August 2026), https://arxiv.org/abs/2608.27201 ; lawful full-text mirror https://borowiecki.dev/pdf/2608.27201 .
2. W. Vance, A. Arkin and J. Ross, *Determination of causal connectivities of species in reaction networks*, Proceedings of the National Academy of Sciences 99 (2002), 5816–5821, https://doi.org/10.1073/pnas.022049699 .
3. S. Soliman, F. Fages and O. Radulescu, *A constraint solving approach to model reduction by tropical equilibration*, Algorithms for Molecular Biology 9 (2014), article 24, https://doi.org/10.1186/s13015-014-0024-2 .
4. S. Peter, B. Ibrahim and P. Dittrich, *Linking Network Structure and Dynamics to Describe the Set of Persistent Species in Reaction Diffusion Systems*, SIAM Journal on Applied Dynamical Systems 20 (2021), 2037–2076, https://doi.org/10.1137/21M1396708 (background on structural presence and persistence; only the accessible abstract was examined).
