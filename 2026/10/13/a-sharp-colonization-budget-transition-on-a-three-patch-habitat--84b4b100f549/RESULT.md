# A sharp colonization-budget transition on a three-patch habitat path

## Finding

For a homogeneous continuous-time three-patch metapopulation occupying the path \(1-2-3\), with only patch \(2\) occupied initially, let the local extinction rate be \(\mu>0\). The bidirectional colonization rate along \(1-2\) is \(x\ge0\) and that along \(2-3\) is \(y\ge0\), with a fixed rate budget \(x+y=C>0\). The allocations maximizing the expected time \(T(x,y)\) to extinction of the whole metapopulation are **exactly**

\[
\begin{cases}
(C,0)\text{ and }(0,C),&0<C<\mu,\\
(C,0),\ (C/2,C/2),\ (0,C),&C=\mu,\\
(C/2,C/2),&C>\mu.
\end{cases}
\]

The optimal design therefore switches discontinuously from a single active corridor to equally funded corridors at the exact budget-to-extinction-rate ratio \(C/\mu=1\). At the transition there are three, and only three, optimal allocations. The two candidate designs' exact expected-time difference is

\[
T(C/2,C/2)-T(C,0)
=\frac{C^2(C-\mu)}{8\mu^3(2C+3\mu)}.
\]

## Assumptions and scope

There are three distinguishable patches \(V=\{1,2,3\}\) linked only by \(1-2\) and \(2-3\). Each occupied patch independently becomes vacant at rate \(\mu\). A vacant patch is colonized by each occupied neighbor across an edge at its assigned symmetric edge rate; contributions from distinct occupied neighbors add. The empty configuration is absorbing. A single patch, the middle one \(\{2\}\), is occupied at time zero. The rates are time-independent, the budget constraint is linear, and zero rates are permissible. The objective is the mean absorption time, not a finite-horizon survival probability.

Write \(c=C/\mu\), \(\xi=x/\mu\), \(\eta=y/\mu\), \(u=\xi\eta\), and \(A=c^2+7c+6\). Necessarily \(\xi+\eta=c\) and \(0\le u\le c^2/4\), with equality at the upper end exactly at the equal split. An exact expression, valid for all parameters above, is

\[
T(x,y)=\frac{(u+c+2)((c+3)u+A)}{2\mu\bigl(A+(2c+7)u\bigr)}.
\]

## Proof

Rescale time so that \(\mu=1\), and temporarily write \(x,y\) for the resulting dimensionless edge rates. For every nonempty occupied subset \(S\subseteq V\), let \(t_S\) denote mean absorption time starting from \(S\). Its backward equation is \(Qt=\mathbf 1\), where the rows and columns of \(Q\) are indexed in binary-mask order by \(\{1\},\{2\},\{1,2\},\{3\},\{1,3\},\{2,3\},\{1,2,3\}\). For each occupied vertex \(i\in S\), \(Q_{S,S}\) receives \(1\) and \(Q_{S,S\setminus\{i\}}\) receives \(-1\) unless the target is empty; for each vacant \(i\), the birth rate \(r_i(S)=\sum_{j\in S:\{i,j\}\in E}\lambda_{ij}\) is added to \(Q_{S,S}\) and \(-r_i(S)\) to \(Q_{S,S\cup\{i\}}\). This specifies all seven linear equations exactly, including absorption at the empty state. The matrix is invertible because the process has a uniformly positive probability of extinction within a bounded number of jumps from each nonempty configuration.

Set \(c=x+y\), \(u=xy\) and \(A=c^2+7c+6\). Direct determinant expansion of these explicit backward equations gives

\[
\det Q=2(c+2)\bigl(A+(2c+7)u\bigr),
\]

and, when the column indexed by \(\{2\}\) is replaced by the all-ones vector,

\[
\det Q_{\{2\}\leftarrow\mathbf 1}
=(c+2)(u+c+2)\bigl((c+3)u+A\bigr).
\]

All factors in the first determinant are positive for \(c>0\) and \(u\ge0\). Cramer's rule establishes the displayed exact formula for \(t_{\{2\}}\), and rescaling back multiplies the expected time by \(1/\mu\). The accompanying standard-library checker recomputes both determinants as identities in the integer polynomial ring \(\mathbb Z[x,y]\), without numerical interpolation.

It remains to optimize the single scalar \(u\in[0,c^2/4]\). Subtracting the concentrated-corridor value yields

\[
\mu\bigl(T(u)-T(0)\bigr)
=\frac{u((c+3)u+c-2)}{2(A+(2c+7)u)}.
\]

When \(0<c<1\), the numerator's second factor is strictly negative for every feasible \(u\), since

\[
(c+3)u+c-2\le(c+3)c^2/4+c-2
=\frac{(c-1)(c^2+4c+8)}4<0.
\]

Thus only \(u=0\), corresponding to the two concentrated allocations, maximizes the mean. At \(c=1\), the difference is proportional to \(u(4u-1)\), which is negative for \(0<u<1/4\) and zero at both endpoints; the upper endpoint corresponds uniquely to the equal split.

For \(c>1\), subtracting the general value from the equal-split value instead gives

\[
\mu\bigl(T(c^2/4)-T(u)\bigr)
=\frac{(c^2-4u)\bigl((c+6)(c^2-1)+(2c+3)(c+3)u\bigr)}{8(2c+3)(A+(2c+7)u)}.
\]

The right side is strictly positive whenever \(u<c^2/4\) and zero when \(u=c^2/4\). Hence the equal split is the unique maximizer. Evaluating the endpoint difference simplifies to \(c^2(c-1)/(8\mu(2c+3))\), which is the dimensional gap in the Finding. This proves every claim and every equality case.

## Verification

Run `python3 verify_corridor.py` from the directory containing that file. The executable uses only the Python standard library. It builds the seven-state transient generator directly from the specified birth-death rules, proves the two claimed determinant formulas coefficient-by-coefficient over \(\mathbb Z[x,y]\), solves \(64\) distinct rational-rate backward systems exactly, and compares \(707\) rational budget allocations to the analytically selected endpoints. The polynomial identities and inequalities in the proof, rather than the finite rational-rate checks, establish the continuum statement.

## Relationship to prior work

Vuilleumier and Possingham (2006) study colonization asymmetry and metapopulation viability using a discrete-time simulation model on \(100\) patches, rather than the three-patch continuous-time absorption-time optimization studied here. Etienne and Heesterbeek (2001) give management heuristics for stochastic metapopulations. Ross and Pollett (2010) derive management rules in a stochastic Levins-type model. Their population-count approximation does not track the two different occupied singleton states of this weighted path; the present calculation is not a specialization of a count-only closed Markov chain. Nakagiri and coauthors (2024) also discuss possible adverse effects of adding corridors in a three-patch but spatially heterogeneous migration model. The exact symmetric-death budget transition and the three optimal designs at the critical ratio were not identified in the accessible inspected materials; complete comparison with some subscription literature remains unresolved.

## Limitations

This is an exact result for three equal-quality patches and a single initially occupied central patch. It allows a corridor to have zero colonization rate. Requiring every corridor to remain strictly positive, imposing a lower bound, unequal local extinctions, nonlinear spending costs, a different initial occupancy law, seasonality or demographic abundance would change the optimization problem. No empirical fit or field effectiveness claim is made. The finite computational tests are supporting checks; the mathematical proof covers all real positive extinction rates and budgets.

## References

1. Vuilleumier, S. and Possingham, H. P. (2006). *Does colonization asymmetry matter in metapopulations?* Proceedings of the Royal Society B 273, 1637–1642. Published online 29 March 2006. DOI: 10.1098/rspb.2006.3469.
2. Etienne, R. S. and Heesterbeek, J. A. P. (2001). *Rules of Thumb for Conservation of Metapopulations Based on a Stochastic Winking-Patch Model*. The American Naturalist 158, 389–407. DOI: 10.1086/321986.
3. Ross, J. V. and Pollett, P. K. (2010). *Simple rules for ranking and optimally managing metapopulations*. Ecological Modelling 221, 2515–2520. DOI: 10.1016/j.ecolmodel.2010.02.016.
4. Nakagiri, N., Yokoi, H., Morishita, A. and Tainaka, K.-I. (2024). *Three-lattice metapopulation model: Connecting corridor between patches may be harmful due to “hub effect”*. Ecological Complexity 59, 101090. DOI: 10.1016/j.ecocom.2024.101090.
