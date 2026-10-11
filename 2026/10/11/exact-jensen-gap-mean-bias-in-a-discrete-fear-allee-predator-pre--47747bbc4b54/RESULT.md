# Exact Jensen-gap mean bias in a discrete fear–Allee predator–prey model
## Finding
Consider the discrete map
\[
N_{n+1}=N_n\left[1+\frac{h}{\epsilon}\left(\frac{(1-N_n)(N_n-\theta)}{1+fP_n}-P_n\right)\right],\qquad
P_{n+1}=P_n[1+h(N_n-m)].
\]
For \(h,\epsilon,f>0\) and \(0<\theta<m<1\), let \(\mu\) be a compactly supported invariant Borel probability measure with support contained in \((0,\infty)^2\). Write \(\bar N=\int N\,d\mu\), \(\bar P=\int P\,d\mu\), and
\[
J_P=\log\!\left(\int[1+h(N-m)]\,d\mu\right)-\int\log[1+h(N-m)]\,d\mu.
\]
Then
\[
\bar N-m=\frac{e^{J_P}-1}{h}\ge0.
\]
Moreover, equality holds exactly for the Dirac measure at the positive equilibrium. Thus every non-equilibrium compact interior recurrent statistical state has \(\bar N>m\) and gives positive mass to both half-planes \(N<m\) and \(N>m\).

Define
\[
g(N)=(1-N)(N-\theta),\qquad
A(N,P)=1+\frac{h}{\epsilon}\left(\frac{g(N)}{1+fP}-P\right)
\]
and
\[
J_N=\log\int A\,d\mu-\int\log A\,d\mu.
\]
Then the predator mean obeys the exact identity
\[
\bar P=\int\frac{g(N)}{1+fP}\,d\mu-\frac{\epsilon}{h}(e^{J_N}-1),
\]
which yields the universal ceiling
\[
0<\bar P<\frac{(1-\theta)^2}{4}.
\]

For the source's first Hopf parameter set, \(\theta=0.1\) and \(m=0.554\), so every non-equilibrium compact positive recurrent state satisfies \(\bar N>0.554\) and \(\bar P<0.2025\). For the second Hopf set, \(\theta=0.61\) and \(m=0.823\), giving \(\bar N>0.823\) and \(\bar P<0.038025\).
## Assumptions and scope
The parameters satisfy \(h,\epsilon,f>0\) and \(0<\theta<m<1\). The measure \(\mu\) is invariant under the printed discrete map, compactly supported, and supported strictly inside the positive quadrant. These hypotheses ensure that \(N\), \(P\), \(\log N\), and \(\log P\) are bounded on the support and that the multiplicative one-step factors are positive \(\mu\)-almost everywhere. No small-amplitude, local-bifurcation, or ergodicity assumption is used.

The positive equilibrium is
\[
E_*=(m,P_*),\qquad
P_*=\frac{-1+\sqrt{1+4f(1-m)(m-\theta)}}{2f}.
\]
The statement concerns necessary statistics of compact positive recurrence. It does not prove that a periodic orbit, invariant curve, or chaotic invariant measure exists for a particular parameter set.
## Proof
Invariance and positivity give the coboundary identities
\[
\int\log\frac{P\circ F}{P}\,d\mu=0,
\qquad
\int\log\frac{N\circ F}{N}\,d\mu=0.
\]
For the predator coordinate,
\[
\frac{P\circ F}{P}=1+h(N-m),
\]
so
\[
\int\log[1+h(N-m)]\,d\mu=0.
\]
Strict concavity of \(\log\) gives \(J_P\ge0\). Because the multiplier is affine in \(N\),
\[
e^{J_P}=\int[1+h(N-m)]\,d\mu=1+h(\bar N-m),
\]
which proves the exact prey-mean formula.

If \(J_P=0\), equality in strict Jensen implies that \(1+h(N-m)\) is constant \(\mu\)-almost everywhere. Its logarithmic mean is zero, so it equals \(1\), hence \(N=m\) almost everywhere. Invariance then forces \(N\circ F=m\) almost everywhere. The prey update therefore has multiplier one, so
\[
P=\frac{(1-m)(m-\theta)}{1+fP}
\]
almost everywhere. The positive solution is uniquely \(P=P_*\), proving \(\mu=\delta_{E_*}\). Conversely the equilibrium Dirac measure has \(J_P=0\). Thus a non-equilibrium invariant measure has \(J_P>0\) and \(\bar N>m\).

For such a non-equilibrium measure, \(\log[1+h(N-m)]\) is nonconstant with integral zero. It must be positive on a set of positive measure and negative on a set of positive measure. Because its sign is the sign of \(N-m\), the support has positive mass on both sides of the equilibrium prey level.

For the prey coordinate, invariance similarly gives \(\int\log A\,d\mu=0\), hence \(J_N\ge0\) and
\[
e^{J_N}=\int A\,d\mu
=1+\frac{h}{\epsilon}\left(\int\frac{g(N)}{1+fP}\,d\mu-\bar P\right).
\]
Rearranging proves the exact predator-mean identity. Finally,
\[
g(N)=\frac{(1-\theta)^2}{4}-\left(N-\frac{1+\theta}{2}\right)^2.
\]
Since \(P>0\) and \(f>0\), pointwise
\[
\frac{g(N)}{1+fP}<\frac{(1-\theta)^2}{4}.
\]
Together with \(J_N\ge0\), this yields \(0<\bar P<(1-\theta)^2/4\).
## Verification
The accompanying `verify.py` checks the equilibrium algebra, the two Jensen-gap rearrangements, the completed-square identity for \(g\), and the exact numerical ceilings used for the two source parameter sets. The proof of strictness is analytic: it uses equality conditions in Jensen's inequality and the uniqueness of the positive root of \(P(1+fP)=(1-m)(m-\theta)\).
## Relationship to prior work
Hong and Zhang introduce the discrete map, identify its positive equilibrium, and analyze local stability, flip and Hopf bifurcations, and numerical chaotic behavior. Their open-access article gives the exact update equations used here and reports periodic and chaotic regimes. The present statement instead constrains every compact positive invariant probability measure, independent of local amplitude and independent of which recurrent regime is realized.

The closest earlier literature located in the source's bibliography and targeted searches concerns local bifurcations, invariant curves, and chaos of discrete predator–prey maps. Those results do not imply the exact logarithmic Jensen-gap identity above. The mechanism is specifically the invariant logarithmic predator growth factor \(1+h(N-m)\), whose geometric mean is forced to one while its arithmetic mean is larger unless the recurrent state is the equilibrium.
## Limitations
The theorem applies only to compact invariant measures whose support stays strictly inside the positive quadrant. It gives necessary recurrence statistics, not existence or stability. It does not classify all invariant measures touching the boundary, and it does not prove that the numerical trajectories displayed in the source have converged to an invariant probability measure. The predator ceiling is universal but is not claimed to be sharp for every parameter set.
## References
1. B. Hong and C. Zhang, “Bifurcations and chaotic behavior of a predator-prey model with discrete time,” *AIMS Mathematics* 8 (2023), 13390–13410, DOI 10.3934/math.2023678.
2. X. Li and X. Shao, “Flip bifurcation and Neimark-Sacker bifurcation in a discrete predator-prey model with Michaelis-Menten functional response,” *Electronic Research Archive* 31 (2023), 37–57, DOI 10.3934/era.2023003.
3. A. Singh and P. Malik, “Bifurcations in a modified Leslie-Gower predator-prey discrete model with Michaelis-Menten prey harvesting,” *Journal of Applied Mathematics and Computing* 67 (2021), 143–174, DOI 10.1007/s12190-020-01491-9.
