# Exact reconstruction margin on the order-three hard-core periodic branch
## Finding
For the two-state hard-core model on the Cayley tree of order \(3\), let \(z_1,z_2>0\) be a nontranslation-invariant two-periodic boundary-law pair at activity \(\lambda>27/16\). Put
\[
x=z_1^{1/3},\qquad y=z_2^{1/3},\qquad a=x+y.
\]
Then the whole nontranslation-invariant branch is described by
\[
1<a<\frac43,\qquad xy=a(a-1),\qquad
\lambda=\frac1{a^2(a-1)}.
\]
For the two-step Markov chain attached to this periodic Gibbs measure, the second eigenvalue \(s_2\) and the downward disagreement coefficient \(\kappa\) satisfy the exact identity
\[
s_2=\kappa=(a-1)^2.
\]
The standard hard-core upward-disagreement bound \(\gamma\le\lambda/(1+\lambda)\) therefore yields
\[
9\kappa\gamma
\le
\frac{9(a-1)^2}{1+(a-1)a^2}
<
\frac{27}{43}
<1.
\]
The constant \(27/43\) is the sharp supremum of this upper bound along the open branch, approached as \(\lambda\downarrow27/16\). Hence the previously known extremality of the two nontranslation-invariant periodic measures has a completely analytic reconstruction certificate with a uniform quantitative margin. In addition,
\[
9s_2^2=9(a-1)^4<\frac19,
\]
so the Kesten--Stigum sufficient nonextremality condition is uniformly far from being triggered.

## Assumptions and scope
The Cayley tree has order \(3\), so every vertex has four neighbors. The hard-core model has states \(0,1\), forbids adjacent occupied vertices, and has activity \(\lambda>0\). Only the two nontranslation-invariant two-periodic Gibbs measures existing for \(\lambda>27/16\) are considered. The source normalization is retained:
\[
z_1=\frac1{(1+\lambda z_2)^3},\qquad
z_2=\frac1{(1+\lambda z_1)^3}.
\]
The conclusion concerns the exact branch-specific Markov eigenvalue and the quantitative sufficient extremality certificate. It does not claim a new existence theorem for the periodic measures, and it does not claim that failure of the Kesten--Stigum inequality by itself proves extremality.

## Proof
Set \(x=z_1^{1/3}\) and \(y=z_2^{1/3}\). The source derives, for the nontranslation-invariant branch,
\[
\lambda xy(x+y)=1,
\qquad
x^2+y^2+xy=x+y.
\]
Writing \(a=x+y\) and \(b=xy\), the second relation gives
\[
a^2-b=a,
\qquad
b=a(a-1),
\]
while the first relation gives
\[
\lambda ab=1,
\qquad
\lambda=\frac1{a^2(a-1)}.
\]
The roots \(x,y\) of \(u^2-au+a(a-1)=0\) are positive and distinct exactly when
\[
a(4-3a)>0.
\]
Together with \(a>1\), this gives \(1<a<4/3\). At \(a=4/3\), the activity is \(27/16\), while \(a\downarrow1\) corresponds to \(\lambda\to\infty\).

For the two-step Markov matrix, the source gives
\[
s_2=
\frac{\lambda^2z_1z_2}
{\lambda^2z_1z_2+\lambda(z_1+z_2)+1}.
\]
Since \(z_1z_2=(xy)^3=b^3\),
\[
\lambda^2z_1z_2
=
\frac{a-1}{a}.
\]
Also,
\[
z_1+z_2=x^3+y^3=a^3-3ab,
\]
and therefore
\[
\lambda(z_1+z_2)
=
\frac{3-2a}{a-1}.
\]
Thus the denominator of \(s_2\) collapses to
\[
\frac{a-1}{a}+\frac{3-2a}{a-1}+1
=
\frac1{a(a-1)},
\]
which proves
\[
s_2=(a-1)^2.
\]
The coefficient \(\kappa\) used by the source is
\[
\kappa=
\frac{\lambda^2z_1z_2}
{(1+\lambda z_1)(1+\lambda z_2)}.
\]
Expanding the denominator gives exactly the same denominator as for \(s_2\), so
\[
\kappa=s_2=(a-1)^2.
\]

Martinelli, Sinclair, and Weitz prove for the hard-core model that
\[
\gamma\le\frac\lambda{1+\lambda}.
\]
Put \(t=a-1\in(0,1/3)\). Since \(\lambda=1/[t(1+t)^2]\),
\[
9\kappa\gamma
\le
F(t):=
\frac{9t^2}{1+t(1+t)^2}.
\]
A direct differentiation gives
\[
F'(t)=
\frac{9t(2+t-t^3)}{(1+t+2t^2+t^3)^2}>0
\qquad (0<t<1/3).
\]
Hence
\[
F(t)<F(1/3)=\frac{27}{43}<1.
\]
The reconstruction criterion used in the source therefore proves extremality for every \(\lambda>27/16\) without any graphical monotonicity step. Finally,
\[
9s_2^2=9t^4<9\left(\frac13\right)^4=\frac19.
\]

## Verification
The proof is symbolic and does not depend on finite enumeration. The accompanying `verify.py` uses exact rational arithmetic to replay the identities for many rational values of \(t\in(0,1/3)\), checks the strict certificate against \(27/43\), and checks the endpoint values exactly. These finite checks are corroborative only; the inequalities above follow analytically from the displayed formulas.

The nonstandard bound \(\gamma\le\lambda/(1+\lambda)\) was checked in the full preprint of Martinelli--Sinclair--Weitz, Theorem 5.1(i). The defining branch equations, the two-step eigenvalue, the \(\kappa\) formula, and the use of the criterion \(9\kappa\gamma<1\) were checked in the full text of the primary hard-core source.

## Relationship to prior work
Rozikov, Khakimov, and Makhammadaliev prove existence and extremality of the two nontranslation-invariant periodic measures for the order-three hard-core model. For \(k=3\), they introduce \(a=x+y\), solve the branch through a cubic/Cardano expression, and report computer-assisted graphical checks for the remaining monotonicity inequalities in their reconstruction argument. Their paper does not state
\[
s_2=\kappa=(a-1)^2
\]
or the uniform bound
\[
9\kappa\gamma<27/43.
\]
Martinelli--Sinclair--Weitz provide the general hard-core estimate \(\gamma\le\lambda/(1+\lambda)\), but do not specialize it to this periodic branch or derive the exact branch eigenvalue above.

A broader countable-state hard-core boundary-law parameterization includes the two-state branch after specialization, but that parameterization does not determine the branch-specific two-step Markov eigenvalue, the reconstruction coefficient, or the quantitative extremality margin proved here. Thus the contribution is not a new existence theorem and not a rephrasing of the known extremality statement; it is the exact reconstruction certificate and its sharp uniform bound.

## Limitations
The result is specific to the two-state hard-core model on the Cayley tree of order \(3\) and to its nontranslation-invariant two-periodic branch. The bound \(27/43\) is the sharp supremum of this particular sufficient-certificate upper bound, not a claim about an optimal general reconstruction threshold. The Kesten--Stigum inequality is only a sufficient nonextremality test, so its failure is not used as a proof of extremality. No claim is made about other tree orders or other periodicity classes.

## References
1. U. A. Rozikov, R. M. Khakimov, M. T. Makhammadaliev, *Periodic Gibbs measures for the two states HC model on a Cayley tree*, arXiv:2111.11163v1; published as *Gibbs periodic measures for a two-state HC-model on a Cayley tree*, Contemporary Mathematics. Fundamental Directions 68 (2022), 95--109, DOI:10.22363/2413-3639-2022-68-1-95-109.
2. F. Martinelli, A. Sinclair, D. Weitz, *Fast mixing for independent sets, colorings, and other models on trees*, Random Structures & Algorithms 31 (2007), 134--172, DOI:10.1002/rsa.20132.
