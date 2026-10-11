# Exact total-variation weaving threshold for Parseval continuous \(g\)-fusion frames
## Finding
For two Parseval continuous \(g\)-fusion families, the exact optimal universal lower and upper weaving bounds are determined by the maximum total-variation separation of their measurement-energy distributions:
\[
\boxed{A_{\mathrm{opt}}=1-\tau,\qquad B_{\mathrm{opt}}=1+\tau,}
\]
where
\[
\tau=\frac12\sup_{\|f\|=1}\int_X |a_f(x)-b_f(x)|\,d\mu(x).
\]
The families are woven precisely when \(\tau<1\). This gives an exact robustness threshold without separately analyzing the lower-frame inequality at each measurable partition. The same parameter is the supremum of the operator norms of the two partial frame-operator differences; only partial, rather than full, differences can detect allocation of energy between channels.

Equivalently, \(\tau=\sup_{\sigma\in\Sigma}\|S_{1,\sigma}-S_{2,\sigma}\|\), where \(S_{i,\sigma}\) is the positive partial frame operator of source \(i\) on \(\sigma\). This converts the exact criterion into a uniform norm bound on **all partial** operator differences; equality of the integrated global operators alone cannot control it.

The classification is sharp for every value \(\tau\in[0,1]\), and even the equality of the two global frame operators does not constrain \(\tau\) below \(1\). In particular, a pair of Parseval families can have identical global frame operator but a weaving with zero lower bound.

## Assumptions and scope
Let \(H\) be a nonzero real or complex Hilbert space and \((X,\Sigma,\mu)\) a measure space. The two continuous \(g\)-fusion families have the same measurable index space, but their fusion subspaces, weights, and fibre analysis maps may differ. Write their scalar energy densities as
\[
a_f(x)=v_1(x)^2\|\Lambda_1(x)P_{F_1(x)}f\|^2,\qquad
b_f(x)=v_2(x)^2\|\Lambda_2(x)P_{F_2(x)}f\|^2.
\]
Assume measurability of these densities and the Parseval identities
\[
\int_X a_f\,d\mu=\int_X b_f\,d\mu=\|f\|^2
\]
for every \(f\in H\). These hypotheses hold for Parseval continuous \(g\)-fusion frames with the ordinary control choice \(T=U=K=I\). The integrals are finite and nonnegative.

A weaving associated with a measurable \(\sigma\subseteq X\) selects the first family on \(\sigma\) and the second on its complement. Its energy is
\[
E_\sigma(f)=\int_\sigma a_f\,d\mu+\int_{X\setminus\sigma}b_f\,d\mu.
\]
The universal lower and upper constants are the infimum and supremum, respectively, of \(E_\sigma(f)\) over measurable \(\sigma\) and unit vectors \(f\). No assumption that either extreme is attained is made.

## Proof
Fix a unit vector \(f\) and abbreviate \(a=a_f\), \(b=b_f\). Both are integrable with total mass one. Since \(\int_X(a-b)\,d\mu=0\),
\[
\int_X\min\{a,b\}\,d\mu
=1-\frac12\int_X|a-b|\,d\mu,
\]
and
\[
\int_X\max\{a,b\}\,d\mu
=1+\frac12\int_X|a-b|\,d\mu.
\]
The measurable choice \(\sigma_f=\{x:a_f(x)\le b_f(x)\}\) satisfies
\[
E_{\sigma_f}(f)=\int_X\min\{a_f,b_f\}\,d\mu.
\]
The complementary choice, with the inequality reversed, attains the pointwise maximum. Therefore, for every fixed unit vector,
\[
\inf_{\sigma\in\Sigma}E_\sigma(f)
=1-\frac12\int_X|a_f-b_f|\,d\mu,
\]
\[
\sup_{\sigma\in\Sigma}E_\sigma(f)
=1+\frac12\int_X|a_f-b_f|\,d\mu.
\]
The optimal universal lower bound is the joint infimum over \(\sigma\) and unit \(f\). Hence the two infima commute:
\[
\inf_{\sigma\in\Sigma}\inf_{\|f\|=1}E_\sigma(f)
=\inf_{\|f\|=1}\inf_{\sigma\in\Sigma}E_\sigma(f)
=1-\tau.
\]
Likewise, the joint supremum gives \(1+\tau\). The optimizing partition may depend on \(f\); no partition uniform in \(f\) is required for these joint extrema. Homogeneity extends the inequalities to arbitrary \(f\). Since both original families are Bessel, every weaving is Bessel; it has a positive universal lower bound exactly when \(1-\tau>0\). This proves the necessary and sufficient condition \(\tau<1\).

For the equivalent operator formulation, let \(S_{1,\sigma}\) and \(S_{2,\sigma}\) be the bounded self-adjoint positive partial frame operators defined by integrating the two local quadratic energy forms over \(\sigma\). Then \(D_\sigma=S_{1,\sigma}-S_{2,\sigma}\) is self-adjoint, and
\[
\|D_\sigma\|=\sup_{\|f\|=1}\left|\int_\sigma(a_f-b_f)\,d\mu\right|.
\]
Since the signed density \(a_f-b_f\) integrates to zero over all of \(X\), its maximum absolute mass on a measurable set equals half its total \(L^1\)-mass. Exchanging the two suprema therefore gives
\[
\tau=\sup_{\sigma\in\Sigma}\|S_{1,\sigma}-S_{2,\sigma}\|.
\]
Every mixed weaving operator equals \(I+D_\sigma\), and \(D_{X\setminus\sigma}=-D_\sigma\). This explains at the operator level why the full-space identity \(D_X=0\) has no implication for the magnitude of the partial differences.

For sharpness at every parameter, take \(H=\mathbb R^2\), the two-point counting-measure space \(X=\{1,2\}\), and coordinate projections \(P_1,P_2\). For any \(t\in[0,1]\), prescribe positive energy operators
\[
A_1=P_1,\qquad A_2=P_2,
\]
\[
B_1=(1-t)P_1+tP_2,\qquad
B_2=tP_1+(1-t)P_2.
\]
These are implemented by legitimate \(g\)-fusion families with fusion subspaces \(H\), unit weights, and analysis maps \(A_j^{1/2},B_j^{1/2}\); square roots exist and are bounded. Both systems are Parseval because
\[
A_1+A_2=B_1+B_2=I.
\]
Writing \(f=(f_1,f_2)\), the differences of their local energies are
\[
a_f(1)-b_f(1)=t(|f_1|^2-|f_2|^2),
\qquad a_f(2)-b_f(2)=-t(|f_1|^2-|f_2|^2).
\]
Thus, for \(\|f\|=1\),
\[
\frac12\sum_{j=1}^2|a_f(j)-b_f(j)|
=t\bigl||f_1|^2-|f_2|^2\bigr|\le t,
\]
with equality at either coordinate vector, so \(\tau=t\). The mixed weaves have frame operators
\[
A_1+B_2=(1+t)P_1+(1-t)P_2,
\]
\[
B_1+A_2=(1-t)P_1+(1+t)P_2,
\]
whose eigenvalues are exactly \(1-t\) and \(1+t\). Hence the two universal endpoints are attained for every \(t\). At \(t=1\), the first mixed operator is \(2P_1\) and has kernel \(\operatorname{span}\{e_2\}\), although both individual aggregate frame operators equal \(I\). In this boundary case one may also take a **common** fibre map \(\Lambda(1)=\Lambda(2)=I_H\) for both source families, with the first fusion subspaces \(F(1)=\operatorname{span}\{e_1\}\), \(F(2)=\operatorname{span}\{e_2\}\) and the second \(G(1)=\operatorname{span}\{e_2\}\), \(G(2)=\operatorname{span}\{e_1\}\). Thus the example respects even the shared-analysis-map form of the motivating Theorem 2.15.

## Verification
The primary arXiv full text of Ghosh--Samanta (2021) was inspected at its continuous controlled \(K\)-\(g\)-fusion definition, weaving definition, Theorem 2.15, and the complete proof on the next printed page. The theorem prints a full-space integrated difference operator. Its proof requires a sign for a difference integral restricted to the complementary partition, which does not follow merely from positivity of the full-space integral. The phrasing also admits a pointwise-density positivity interpretation; the two interpretations are distinguished rather than conflated.

The continuum of \(2\times2\) examples was checked directly through its diagonal frame operators. Its eigenvalues at the two mixed partitions are \(1\pm t\), and the local total-variation parameter is exactly \(t\), including the boundary cases \(t=0\) and \(t=1\). Elementary numerical checks at several intermediate parameter values reproduce the exact formulas but are not needed for the proof.

## Relationship to prior work
Ghosh--Samanta's 2021 paper studies weaving continuous controlled \(K\)-\(g\)-fusion frames and proposes a positivity-based sufficient criterion in Theorem 2.15. The present result gives an exact necessary-and-sufficient invariant for the Parseval specialization, rather than relying on global positivity of an integrated defect. Global frame-operator equality holds throughout the sharp family even while the weaving threshold ranges from positive to zero.

Bemrose--Casazza--Gröchenig--Lammers--Lynch develop foundational weaving-frame theory, including finite-dimensional spanning criteria and upper-bound estimates. Those results do not specify the statewise total-variation separation of the two Parseval coefficient-energy distributions as an exact universal constant.

Deepshikha--Samanta study woven generalized frames and their operator characterizations, including relationships between individual and universal frame bounds. Their quantitative framework differs from the exact Parseval total-variation equality here. The full relevant theorem and adjacent examples were compared; no claim is made that a failed text search by itself proves novelty.

## Limitations
The exact formulas require both individual families to be Parseval; differently normalized frames need a separate analysis of their unequal total energy functions. Only two source families are covered. The criterion uses a supremum over all unit vectors; computing that supremum may remain difficult for nontrivial infinite-dimensional systems.

The Ghosh--Samanta theorem's printed use of \(U_x\) and \(\Delta(x)\) leaves an interpretive ambiguity about which operator is required to be positive. The \(t=1\) witness refutes **only** the reading in which positivity of the full integrated defect suffices. If the intended hypothesis is positive local defect \(\Delta(x)\) for each \(x\), it is stronger and valid in the ordinary positive setting; the witness does not satisfy it.

## References
1. P. Ghosh and T. K. Samanta, *Weaving continuous controlled K-g-fusion frames in Hilbert spaces*, arXiv:2111.03389v1, 5 November 2021, Theorem 2.15.
2. T. Bemrose, P. G. Casazza, K. Gröchenig, M. C. Lammers, and R. G. Lynch, *Weaving frames*, arXiv:1503.03947, sections on frame bounds and weaving criteria.
3. Deepshikha and A. Samanta, *On weaving generalized frames and generalized Riesz bases*, arXiv:2001.09432, Section 3.
