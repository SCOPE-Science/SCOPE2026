# Reentrant marginal bailout priorities begin at three banks under proportional recovery

## Finding

For a standard limited-liability, pro-rata clearing network with all bank liabilities normalized to one, strictly positive claims on an outside creditor, and external assets that increase proportionally, **three banks are necessary and sufficient** for the unique optimal recipient of an infinitesimal cash injection to be one bank, then another, then the original bank again. The objective is total gross repayments, including transfers between banks. Optimality concerns the limit of an infinitesimal injection at each fixed economic-strength parameter, not the optimal allocation of a finite bailout budget.

A three-bank network with every directed interbank obligation strictly positive has successive unique optimal recipients bank 1, bank 2, bank 1, on the respective open intervals
\[
0<t<\frac{42}{95},\qquad \frac{42}{95}<t<\frac{126}{61},\qquad \frac{126}{61}<t<6.
\]

With one or two banks this strict reentry is impossible for any admissible liabilities and positive external-asset vector under proportional recovery.

## Assumptions and scope

There are \(n\ge1\) banks, each with total nominal liabilities \(1\). The matrix \(T=(T_{ij})\) has \(T_{ii}=0\), \(T_{ij}\ge0\), and \(\sum_j T_{ij}<1\): \(T_{ij}\) is the fraction of bank \(i\)'s nominal obligation owed to bank \(j\); the remaining strictly positive fraction goes to an outside creditor. All nominal obligations, including external liabilities, stay fixed. At strength \(t>0\), bank \(i\) has exogenous resources \(ta_i\), where \(a_i>0\) is fixed. Cash injections do not change obligations.

The uniquely defined payment vector \(p(t,c)\in[0,1]^n\) for a nonnegative extra injection vector \(c\) solves
\[
p_i(t,c)=\min\left\{1,\;ta_i+c_i+\sum_{j=1}^nT_{ji}p_j(t,c)\right\}.
\]
Existence follows by monotone fixed-point iteration; uniqueness follows because the fixed-point map has \(\ell^1\)-Lipschitz constant at most \(\|T^{\mathsf T}\|_1=\max_j\sum_i(T^{\mathsf T})_{ij}=\max_j\sum_iT_{ji}<1\); the last bound uses the row sums of \(T\). Define the aggregate-payment objective and the marginal-injection gain by
\[
V(t,c)=\sum_{j=1}^n p_j(t,c),\qquad g_i(t)=\lim_{\varepsilon\downarrow0}\frac{V(t,\varepsilon e_i)-V(t,0)}{\varepsilon}.
\]
A unique marginal winner is a bank with \(g_i(t)>g_j(t)\) for every \(j\ne i\). Only parameter intervals with no bank exactly at its solvency boundary are used for the strict-winner assertions.

## Proof

**1. General marginal-gain formula.** Fix a parameter value at which no bank lies at the solvent/default threshold, and let \(D=\{i:p_i(t,0)<1\}\). In a neighborhood, solvent-bank payments are constant at \(1\). On the defaulting coordinates,
\[
(I-T_{DD}^{\mathsf T})p_D=ta_D+T_{D^cD}^{\mathsf T}\mathbf1+c_D.
\]
Because every row sum of \(T\) is less than \(1\), the inverse exists and is entrywise nonnegative. Consequently
\[
g_i(t)=\begin{cases}
\bigl[(I-T_{DD})^{-1}\mathbf1\bigr]_i,&i\in D,\\
0,&i\notin D.
\end{cases}
\]
The gradient is constant while \(D\) is unchanged. This is the standard fixed-default-set threat-index formula; it is the starting point rather than a new theorem about derivatives.

**2. Impossibility for at most two banks.** As \(t\) increases, the clearing vector increases coordinatewise by order preservation, so the strict default set only shrinks (a bank that has become solvent never defaults again). For \(n=1\) the assertion is immediate. For \(n=2\), while both banks default, the vector \(g(t)\) is constant. After the first bank becomes solvent, the only possibly nonzero marginal gain belongs to the remaining defaulting bank. Once that bank becomes solvent, no strict marginal winner exists. Thus, if bank \(i\) is uniquely best initially, then another bank becomes uniquely best, \(i\) cannot become uniquely best a second time. This rules out strict reentry for every two-bank network in the stated class, including degenerate cases with simultaneous solvency events or ties.

**3. A fully connected three-bank witness.** Choose
\[
T=\begin{pmatrix}
0&1/10&4/5\\
2/5&0&3/10\\
3/10&3/10&0
\end{pmatrix},\qquad
 a=\begin{pmatrix}1/20\\3/10\\1\end{pmatrix}.
\]
All six off-diagonal fractions are positive. The respective fractions owed to outside creditors are \(1/10\), \(3/10\), \(2/5\), so strict outside obligations hold. Solving the three linear clearing systems and matching at solvency boundaries yields, exactly,
\[
p(t,0)=\begin{cases}
\bigl(7t/6,\;23t/21,\;95t/42\bigr),&0<t<42/95,\\
\bigl(17t/96+7/16,\;61t/192+11/32,\;1\bigr),&42/95<t<126/61,\\
\bigl(7/10+t/20,\;1,\;1\bigr),&126/61<t<6,\\
(1,1,1),&t>6.
\end{cases}
\]
The payment vector is continuous at each listed boundary. Substitution into the fixed-point equation verifies each branch throughout its interval: each resource residual is affine in \(t\), so its weak inequalities at both endpoints, together with one interior strict test, establish the indicated default set over the whole open interval. Equivalently, the three strict default sets are successively \(\{1,2,3\}\), \(\{1,2\}\), and \(\{1\}\).

By the formula from Step 1, on those intervals the marginal-gain vectors are respectively
\[
 g(t)=\begin{cases}
(416/105,\;374/105,\;114/35),&0<t<42/95,\\
(55/48,\;35/24,\;0),&42/95<t<126/61,\\
(1,\;0,\;0),&126/61<t<6,\\
(0,0,0),&t>6.
\end{cases}
\]
Since \(416/105>374/105>114/35\) and \(35/24>55/48>0\), the unique best recipient is bank 1, then bank 2, then bank 1. The comparison at the isolated boundary parameters is not part of the claim; above \(t=6\) all banks are solvent and no unique marginal recipient exists. This completes the sharpness proof.

## Verification

Run `python3 verify.py` using only Python's standard library. The checker independently solves clearing payments by enumerating every candidate default subset, using exact rational Gaussian elimination and verifying the complete fixed-point conditions. It also checks each fixed-default-set gain vector, all three exact breakpoint identities, and the strict winner comparisons. At three rational interior parameters it independently solves both the original and finitely injected clearing problems, confirming that an injection of \(1/1000\) has exactly the asserted local gain. The finite checks confirm the witness; the two-bank universal bound follows from the mathematical argument above, not from enumeration.

## Relationship to prior work

Eisenberg and Noe established the underlying pro-rata clearing framework. Demange (2012, revised 2015), especially Propositions 1–2, established piecewise-affine repayment sensitivity, the default-set threat index, and optimal targeting of sufficiently small injections. These are **not** claimed as new. Demange also gives an explicit *non-monotone finite-budget targeting* example in Section 3.2.4; it changes the total injected amount while holding the pre-intervention cash flows fixed. The present statement changes all banks' pre-intervention exogenous resources proportionally, always compares only infinitesimal injections at that baseline, and identifies the smallest number of banks for a strict \(1\to2\to1\) global-winner sequence. Li, Lin, Peleato-Inarrea and Pollak analyze optimal systemic-risk mitigation over finite allocations using the same clearing mechanism; a general finite-allocation optimizer does not itself state this sharp dimension-and-reentry theorem. The example is a specialized consequence of established fixed-set sensitivities plus an exact construction and a minimality proof, not a new theory of clearing payments.

## Limitations

The objective counts interbank payments as well as repayments to external creditors, so it is not the same as net welfare or recovery paid only to outside creditors. The intervention is infinitesimal, not a possibly large finite bailout. No claim is made for bankruptcy costs, fire sales, strategic response, derivative obligations, heterogeneous recovery of contractual debt, or data-calibrated regulation. The exact network is an illustrative existence construction, not an empirical banking system. Potential equivalent coverage in more specialized work on threat-index priority sequences remains an originality risk; no independent scientific audit has been performed.

## References

1. L. Eisenberg and T. H. Noe, "Systemic Risk in Financial Systems," *Management Science* **47** (2001), 236–249. DOI `10.1287/mnsc.47.2.236.9835`.
2. G. Demange, "Contagion in Financial Networks: A Threat Index," CEPR Discussion Paper DP8793 (first published February 1, 2012); later CESifo Working Paper 5307 (April 2015). `https://www.ifo.de/DocDL/cesifo1_wp5307.pdf` (especially §§3.1, 3.2.1, 3.2.4).
3. X. Li, F. Lin, M. Peleato-Inarrea, and S. Pollak, "Optimal Monitoring and Mitigation of Systemic Risk in Financial Networks," arXiv `1410.2570`, first submitted October 9, 2014. `https://arxiv.org/abs/1410.2570`.
