# A circulation–area law for occupation under three-stage habitat succession

## Finding

In a habitat with three Markovian successional stages, reversing the direction of habitat transitions while preserving their stationary stage proportions changes the stationary occupancy of a focal species by an **exact product** of (i) habitat probability circulation and (ii) the oriented area formed by the three colonization–survival parameter points. More precisely, with the definitions below,

\[
\mathcal U(P)-\mathcal U(P^*)=\frac{J\mathcal A}{\det(I-PD)},
\qquad
\mathcal A=c_1(s_2-s_3)+c_2(s_3-s_1)+c_3(s_1-s_2).
\]

The denominator is strictly positive. Consequently the direction of the occupancy change is exactly the sign of \(J\mathcal A\), and the two stationary occupancies are equal **if and only if** either the landscape chain is reversible or the three points \((c_i,s_i)\) are collinear. This criterion is independent of the individual stage residence probabilities except through the magnitude and sign of the stationary circulation. Three habitat stages are the minimum possible number for a nonzero reversal effect under these assumptions.

## Assumptions and scope

Let \(Y_t\) be a stationary, irreducible, discrete-time Markov chain on the three states \(\{1,2,3\}\), with row-stochastic transition matrix \(P\) and unique strictly positive invariant row probability vector \(\pi\). Let \(X_t\in\{0,1\}\) represent the occupancy of one patch. For each stage \(i\), fix \(0<c_i<1\) and \(0<s_i<1\). Conditional on \(Y_t=i\) and \(X_t\), generate occupancy at the next observation according to

\[
\Pr(X_{t+1}=1\mid X_t=0,Y_t=i)=c_i,\qquad
\Pr(X_{t+1}=1\mid X_t=1,Y_t=i)=s_i.
\]

Generate \(Y_{t+1}\) using \(P\), independently of the new occupancy conditional on \((X_t,Y_t)\). Define the reversed habitat chain by \(P^*=\Pi^{-1}P^{\mathsf T}\Pi\), where \(\Pi=\operatorname{diag}(\pi_1,\pi_2,\pi_3)\). Both experiments use the same \(c_i,s_i\), and each is evaluated in its joint stationary law. Let \(\mathcal U(P)=\Pr_P(X=1)\) and let \(D=\operatorname{diag}(s_1-c_1,s_2-c_2,s_3-c_3)\). Define the signed stationary landscape current by

\[
J=\pi_1P_{12}-\pi_2P_{21}
=\pi_2P_{23}-\pi_3P_{32}
=\pi_3P_{31}-\pi_1P_{13}.
\]

The equalities follow from stationary flow balance. The theorem concerns a patch with stage-dependent colonization influx, not a self-consistently closed finite metapopulation whose immigration vanishes when all patches are empty. Periodicity of \(P\) is allowed because the statement concerns stationarity, not convergence of its marginal from arbitrary initial phases.

## Proof

**Existence and the resolvent.** Put \(d_i=s_i-c_i\), so \(|d_i|<1\). Let \(q_i=\Pr(X=1,Y=i)\) in a joint stationary law. Since the habitat marginal is \(\pi\), the occupied joint row vector satisfies

\[
q=(qD+\pi\operatorname{diag}(c_1,c_2,c_3))P.
\]

Because \(\|PD\|_{\infty}\leq\max_i|d_i|<1\), the resolvent is defined. The unique solution determines the unique joint stationary distribution, and the sum of occupied probabilities is

\[
\mathcal U(P)=\pi\operatorname{diag}(c_1,c_2,c_3)(I-PD)^{-1}{\bf1}.
\]

This also follows by substituting \(q=\pi\operatorname{diag}(c)P(I-DP)^{-1}\) and using \(P(I-DP)^{-1}{\bf1}=(I-PD)^{-1}{\bf1}\).

**Common positive denominator.** Since \(P^*=\Pi^{-1}P^{\mathsf T}\Pi\) and \(D\Pi=\Pi D\),

\[
\det(I-P^*D)=\det(I-P^{\mathsf T}D)
=\det(I-DP)=\det(I-PD)=:\Delta.
\]

All eigenvalues of \(PD\) lie strictly inside the unit disk. Thus the real factors \(1-\lambda\) are positive and conjugate pairs contribute positive products; therefore \(\Delta>0\).

**Three-state cofactor identity.** Write the stationary edge flow matrix \(F=\Pi P\). Every three-state stationary flow has, for some symmetric pair flows \(h_{12},h_{23},h_{31}\), the representation

\[
F=\begin{pmatrix}
\pi_1-h_{12}-h_{31}&h_{12}+J/2&h_{31}-J/2\\
h_{12}-J/2&\pi_2-h_{12}-h_{23}&h_{23}+J/2\\
h_{31}+J/2&h_{23}-J/2&\pi_3-h_{23}-h_{31}
\end{pmatrix}.
\]

Its transpose is the flow matrix of \(P^*\). With \(w=\pi\operatorname{diag}(c_1,c_2,c_3)\), expansion of the three-by-three adjugates gives the exact polynomial identity

\[
w\bigl[\operatorname{adj}(I-PD)-\operatorname{adj}(I-P^*D)\bigr]{\bf1}
=J\left[c_1(d_2-d_3)+c_2(d_3-d_1)+c_3(d_1-d_2)\right].
\]

This expansion does not assume distinct stages or nonzero \(J\), and all denominators introduced in the representation are the positive \(\pi_i\). The accompanying `check.py` reconstructs the unrestricted symbolic flow matrix and establishes both this numerator identity and the common-determinant identity by exact polynomial cancellation. Since \(d_i=s_i-c_i\), the bracket equals \(\mathcal A\). Cramer's rule and \(\Delta>0\) prove the stated formula and sign/equality classification.

**Minimality.** Every irreducible chain with one or two states obeys detailed balance, so \(P=P^*\) and has zero reversal effect. In three states, \(J=0\) is equivalent to detailed balance. A nonzero area occurs exactly when the points \((c_1,s_1),(c_2,s_2),(c_3,s_3)\) are not collinear. The example below shows both conditions can hold simultaneously within the strict probability domain.

## Verification

An exact rational example has

\[
P=\begin{pmatrix}
1/2&7/20&3/20\\
1/10&1/2&2/5\\
7/50&4/25&7/10
\end{pmatrix},\quad
\pi=(1/5,3/10,1/2),\quad
c=(1/10,1/5,2/5),\quad
s=(4/5,3/5,9/10).
\]

Here \(J=1/25\), \(\mathcal A=7/100\) and \(\Delta=6287/20000\). Direct six-state stationary calculations give

\[
\mathcal U(P)=\frac{18043}{31435},\qquad
\mathcal U(P^*)=\frac{17763}{31435},\qquad
\mathcal U(P)-\mathcal U(P^*)=\frac{56}{6287}>0.
\]

Run `python check.py` with Python 3 and SymPy. It carries out the exact symbolic cofactor identities for unrestricted three-state stationary flows, directly solves the two six-state occupation/environment chains in the example, and tests 50 rational parameter cases against independent joint-chain stationary calculations. The finite tests are supplementary checks, not a replacement for the displayed general algebraic argument.

## Relationship to prior work

McVinish, Pollett and Chan (first available as an arXiv preprint in December 2014) developed a general Markovian-landscape incidence-function metapopulation model, including a dual environmental chain and occupancy recursions. Their model supplies the ecological motivation and related general framework, but the inspected model, equilibrium and discussion sections do not state the three-stage reversal-difference product, its complete zero/sign characterization, or the minimality result. The result here uses independent stage-dependent colonization probabilities and does not assert the full nonlinear, spatial persistence criterion of their model.

Solow and Smith (2006) explicitly reverse ecological succession chains to reconstruct backward first-passage histories. Their reverse-chain formula supplies a relevant structural antecedent, but the inspected full article does not introduce an additional binary occupancy layer or compare its forward-versus-reverse stationary abundance. Hill, Witman and Caswell (2004) analyze empirical ecological succession transition matrices and stationary communities; the available abstract does not establish the coupled model's orientation criterion. General finite-state Markov resolvent methods compute occupation in either direction, and could provide a broader algebraic route to the identity; establishing absence of equivalent formulations everywhere is not claimed.

## Limitations

The result is exact for one binary occupancy variable under independent external colonization influx. It does not imply a change in the stationary landscape-stage proportions, prove persistence of a self-exciting metapopulation, handle more than three stages with a single universal area, or compare time-dependent nonstationary populations. A three-state reversible chain or collinear colonization/survival points produces no effect. The complete Hill–Witman–Caswell paper was not available for full-text comparison, and a broader Markov-modulated affine-recursion theorem could subsume the algebraic identity. Independent validation has not been performed.

## References

1. R. McVinish, P. K. Pollett and Y. S. Chan, *A metapopulation model with Markovian landscape dynamics*, arXiv:1412.0719, first posted 2014-12-01, journal DOI: 10.1016/j.tpb.2016.08.005. https://arxiv.org/abs/1412.0719
2. A. R. Solow and W. K. Smith, *Using Markov chain successional models backwards*, Journal of Applied Ecology 43 (2006), 185–188. DOI: 10.1111/j.1365-2664.2005.01127.x. https://besjournals.onlinelibrary.wiley.com/doi/10.1111/j.1365-2664.2005.01127.x
3. M. F. Hill, J. D. Witman and H. Caswell, *Markov Chain Analysis of Succession in a Rocky Subtidal Community*, American Naturalist 164 (2004), E46–E61. DOI: 10.1086/422340. https://www.journals.uchicago.edu/doi/10.1086/422340
