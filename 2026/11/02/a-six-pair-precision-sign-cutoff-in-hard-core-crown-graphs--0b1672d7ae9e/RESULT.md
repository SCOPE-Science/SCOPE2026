# A six-pair precision-sign cutoff in hard-core crown graphs

## Finding

Let \(G_n\) be the crown graph obtained from the complete bipartite graph on two parts \(A=\{a_1,\ldots,a_n\}\), \(B=\{b_1,\ldots,b_n\}\) by deleting the perfect matching \(\{a_ib_i\colon 1\le i\le n\}\). Sample an independent vertex set \(I\) with probability proportional to \(\lambda^{|I|}\) for \(\lambda>0\). Let \(X_v=\mathbf 1_{\{v\in I\}}\) and \(Q=\operatorname{Cov}(X)^{-1}\), in the coordinate ordering \(a_1,\ldots,a_n,b_1,\ldots,b_n\).

For every index \(i\) and every positive fugacity, \(Q_{a_ib_i}\) has the following complete classification at orders \(2\le n\le6\):

* \(n=2\): the entry is zero.
* \(n=3\): the entry is strictly negative.
* \(n=4\): it is negative below the unique positive root \(\alpha_4\) of \(z^4+4z^3-8z^2-18z-3\), zero at \(\alpha_4\), and positive above; \(\alpha_4\approx2.45359450246\).
* \(n=5\): it is negative below the unique positive root \(\alpha_5\) of \(z^6+11z^5+49z^4+117z^3+124z^2+28z-24\), zero there, and positive above; \(\alpha_5\approx0.30606179495\).
* \(n=6\): the entry is strictly positive.

Hence \(n=6\) is the **least** member of this family for which the deleted-matching precision entry is positive at **every** fugacity. Moreover, for every \(n\ge3\), the matched pair has strictly **negative marginal covariance**. Its nonzero precision entry and even its sign therefore need not reflect either the marginal sign or its exact conditional independence given every remaining occupation indicator.

## Assumptions and scope

Here a crown graph has \(n\ge2\), simple undirected edges \(a_ib_j\) exactly when \(i\ne j\). The hard-core measure assigns mass \(\lambda^{|I|}/Z\) to each independent set \(I\). The word *precision* denotes the inverse **ordinary covariance** matrix; it does not mean the matrix of canonical Gibbs interaction coefficients. A full-order linear partial correlation between \(a_i,b_i\) has sign opposite to \(Q_{a_ib_i}\). The specified two occupation variables are conditionally independent given the rest, because they are nonadjacent vertices in this positive-fugacity hard-core graphical model. No claim about the precision sign for \(n\ge7\) is made.

## Proof

**1. Exact law and positive definiteness.** Every independent set is wholly contained in \(A\), wholly contained in \(B\), or is precisely one matched pair \(\{a_i,b_i\}\): any mixed independent set must have both of its vertices in a single deleted pair. Counting the empty state only once gives, with \(t=1+\lambda\),
\[
Z=2t^n-1+n\lambda^2.
\]
The empty set and all singleton sets have strictly positive probability. Therefore if a linear combination of all \(2n\) indicators were almost surely constant, evaluating it at the empty set and then every singleton would force every coefficient to vanish. Thus the full covariance matrix is positive definite.

**2. Covariance reduction.** By symmetry, the common mean \(p\), same-side distinct-pair joint moment \(u\), and matched opposite-side joint moment \(v\) are
\[
p=\frac{\lambda t^{n-1}+\lambda^2}{Z},\qquad
u=\frac{\lambda^2t^{n-2}}{Z},\qquad
v=\frac{\lambda^2}{Z}.
\]
Unmatched opposite-side joint moments vanish. Put \(J_n\) for the all-ones matrix and \(I_n\) for the identity. The covariance has blocks
\[
\Sigma=\begin{pmatrix}H&B\\B&H\end{pmatrix},\quad
H=(p-u)I_n+(u-p^2)J_n,\quad B=vI_n-p^2J_n.
\]
The orthogonal symmetric/antisymmetric modes reduce it to matrices \(H+B=a_+I_n+b_+J_n\) and \(H-B=a_-I_n+b_-J_n\), with \(h=t^{n-2}\) and
\[
a_+=\frac{\lambda(h+2\lambda)}Z,\quad b_+=u-2p^2,\quad
a_-=\frac{\lambda h}{Z},\quad b_-=u.
\]
For \(M=aI_n+bJ_n\) with positive eigenvalues, the diagonal entry of its inverse is \((a+(n-1)b)/(a(a+nb))\). Consequently the matched-pair precision entry is one half of the diagonal of \((H+B)^{-1}-(H-B)^{-1}\).

**3. A sign-polynomial identity.** Write
\[
K=[h(1+n\lambda)+2\lambda]Z-2n\lambda(th+\lambda)^2,\\
L=[h(1+(n-1)\lambda)+2\lambda]Z-2(n-1)\lambda(th+\lambda)^2,
\]
and set
\[
E_n=h(1+n\lambda)L-(h+2\lambda)(1+(n-1)\lambda)K.
\]
Substitution into the previous inverse formula gives the exact identity
\[
Q_{a_ib_i}=\frac{ZE_n}{2\lambda h(1+n\lambda)(h+2\lambda)K}.
\]
Every denominator factor is strictly positive: \(Z,\lambda,h,1+n\lambda,h+2\lambda>0\), and \(K>0\) because the positive eigenvalue \(a_++nb_+\) is \(\lambda K/Z^2\). Thus the sign of precision is **exactly** the sign of the polynomial \(E_n\), with no analytic approximation.

Direct substitution \(h=(1+\lambda)^{n-2}\) and exact polynomial multiplication yield
\[
\begin{aligned}
E_2&=0,\\
E_3&=-2\lambda^5(1+3\lambda),\\
E_4&=2\lambda^5 P_4(\lambda),\\
E_5&=2\lambda^6 P_5(\lambda),\\
E_6&=2\lambda^5 P_6(\lambda),
\end{aligned}
\]
where
\[
\begin{aligned}
P_4(z)&=z^4+4z^3-8z^2-18z-3,\\
P_5(z)&=z^6+11z^5+49z^4+117z^3+124z^2+28z-24,\\
P_6(z)&=z^{10}+14z^9+91z^8+356z^7+921z^6\\
&\quad+1640z^5+1945z^4+1400z^3+520z^2+80z+20.
\end{aligned}
\]
The real coefficient sequences of \(P_4\) and \(P_5\), listed in descending degrees, have exactly one sign change. Their values at zero are strictly negative and their leading coefficients are positive. The intermediate-value theorem ensures a positive root; Descartes' rule of signs ensures **only one** positive root, counting multiplicities, and continuity supplies the stated signs. Every coefficient of \(P_6\) is positive, so \(P_6(z)>0\) for every \(z>0\). This proves all five cases and minimality of the sixth order.

**4. Marginal sign and the distinction from conditional independence.** For each matched pair,
\[
\operatorname{Cov}(X_{a_i},X_{b_i})=v-p^2=\frac{\lambda^2}{Z^2}\left((n-1)\lambda^2-(t^{n-1}-1)^2\right).
\]
For \(n\ge3\), Bernoulli's inequality gives \(t^{n-1}-1\ge(n-1)\lambda>\sqrt{n-1}\,\lambda\), establishing strict negativity. The graphical-model conditional independence holds because fixing all other occupations leaves the two nonadjacent vertices with independent allowable occupation decisions. This conditional independence does **not** force the inverse of the **unconditional covariance** to be zero in this non-Gaussian model.

## Verification

The standalone file `verify_crown.py` uses only the standard Python library. It expands the displayed polynomial identities exactly over the integers for all five orders. Independently, it exhausts all \(2^{2n}\) binary configurations for \(2\le n\le6\), for five rational fugacities each, filters independent sets using the actual edge definition, builds their exact rational covariance matrices, inverts them by rational Gaussian elimination, and compares moments, matrix products, and the precision identity. Execution reports **4030 passing exact checks**. Symbolic expansion verifies the stated polynomial identities; finite numerical cases alone would not establish all-fugacity signs.

Run `python3 verify_crown.py` in the directory containing this document and the checker.

## Relationship to prior work

The partition function \(Z=2(1+\lambda)^n-1+n\lambda^2\) is the **known independence polynomial** of a crown graph (MathWorld); no originality is claimed for this counting formula. The hard-core model and influence-matrix machinery are discussed by Efthymiou (2022, Sections 2.2 and 3, Theorem 2.2), which studies spectral bounds and mixing rather than the *inverse ordinary covariance* of crown-graph vertex occupations. Marsman et al. (2022) analyze Ising network interaction-coefficient recovery and conditional-independence structure, not the same covariance inverse or the stated fugacity thresholds. The two notions of a precision matrix must not be confused.

Existing exact results about crown-graph maximal stable sets and metric parameters concern deterministic graph invariants; exact results about monomer–dimer matching indicator precision on complete graphs concern a different probability space. None of the materially checked sources identified the displayed \(n=4,5\) critical thresholds or the \(n=6\) all-fugacity cutoff. Search failure alone is not proof of historical priority. General hard-core covariance identities may allow this specialization implicitly; see limitations.

## Limitations

The precision sign diagram is proved only for \(2\le n\le6\); no asymptotic conclusion about increasing \(n\) or heterogeneous fugacities is established. Ordinary linear partial correlations are not conditional independence tests outside the Gaussian setting. The proof is self-contained, but an earlier implicit calculation in hard-core model or multivariate independence-polynomial literature remains a priority risk. Independent review has not been performed.

## References

1. C. Efthymiou, *Spectral Independence Beyond Uniqueness using the topological method*, first public 2022-11-07, arXiv:2211.03753v1, https://arxiv.org/html/2211.03753v1 . Particularly Sections 2.2, 3, and 10.
2. M. Marsman, K. Huth, L. J. Waldorp and I. Ntzoufras, *Objective Bayesian Edge Screening and Structure Selection for Ising Networks*, Psychometrika 87 (2022), online 2022-02-22, https://doi.org/10.1007/s11336-022-09848-8 .
3. E. W. Weisstein, *Crown Graph*, Wolfram MathWorld, https://mathworld.wolfram.com/CrownGraph.html ; lists the same independence polynomial.
4. Descartes' rule of signs and the inverse formula for a rank-one perturbation of a scalar matrix (classical algebra; rederived where used).
