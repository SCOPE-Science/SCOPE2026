# A quadratic pairwise game where assortativity creates an evolutionary branching point
## Finding
Consider the assortative continuous-game invasion fitness
\[
\varphi_x^r(y)=r\pi(y,y)+(1-r)\pi(y,x)-\pi(x,x),\qquad 0\le r\le 1,
\]
for traits \(x,y\in[0,1]\).  For the smooth quadratic payoff
\[
\pi(x,y)=-\frac12\left(x-\frac12\right)^2-\left(x-\frac12\right)\left(y-\frac12\right)+2\left(y-\frac12\right)^2,
\]
the interior singular strategy \(x^\star=\tfrac12\) is convergence stable for \(r<\tfrac23\).  Its evolutionary character changes sharply with assortativity: it is an ESS for \(0\le r<\tfrac12\), is neutral at \(r=\tfrac12\), and is an evolutionary branching point for \(\tfrac12<r<\tfrac23\).  Hence increasing positive assortativity can create, rather than inhibit, evolutionary branching in the generic pairwise assortative formalism.

This supplies a concrete boundary to the broad conjecture of Iyer and Killingback that the inhibiting effect of assortative interactions on branching is a general phenomenon.  It does not contradict their proved conclusions for the continuous snowdrift or continuous tragedy-of-the-commons payoff classes.
## Assumptions and scope
The population is monomorphic at resident trait \(x\), a rare mutant has trait \(y\), and assortment follows the model in which an individual meets its own type with probability \(r\) and otherwise samples randomly.  The adaptive-dynamics criteria are those used by Iyer and Killingback: a singular strategy is convergence stable when the derivative of the selection gradient is negative; a convergence-stable singular strategy is an ESS when mutant-direction invasion curvature is negative and an evolutionary branching point when it is positive.

The claim concerns the local adaptive-dynamics branching criterion for a smooth pairwise game.  The payoff is deliberately generic: no monotone benefit-cost decomposition, social-dilemma interpretation, or public-goods structure is assumed.
## Proof
For any \(C^2\) pairwise payoff, differentiation of the invasion fitness gives the selection gradient
\[
D_r(x)=\left.\frac{\partial\varphi_x^r(y)}{\partial y}\right|_{y=x}
      =\pi_1(x,x)+r\pi_2(x,x).
\]
At a singular strategy, the convergence slope and mutant-direction curvature are
\[
C_r=\frac{dD_r}{dx}=\pi_{11}+(1+r)\pi_{12}+r\pi_{22},
\qquad
B_r=\left.\frac{\partial^2\varphi_x^r(y)}{\partial y^2}\right|_{y=x}
=\pi_{11}+2r\pi_{12}+r\pi_{22}.
\]
Thus
\[
B_r-C_r=(r-1)\pi_{12}.
\]
This identity already shows that the relative movement of convergence and disruptive-selection curvatures is controlled by the mixed payoff curvature; no sign follows from assortment alone.

For the displayed quadratic payoff,
\[
\pi_{11}=-1,\qquad \pi_{12}=-1,\qquad \pi_{22}=4.
\]
Writing \(z=x-\tfrac12\), the diagonal first derivatives are \(\pi_1(x,x)=-2z\) and \(\pi_2(x,x)=3z\).  Therefore
\[
D_r(x)=(-2+3r)\left(x-\frac12\right).
\]
Except at the degenerate value \(r=\tfrac23\), the unique interior singular strategy is \(x^\star=\tfrac12\), and
\[
D_r'(x^\star)=-2+3r.
\]
Hence \(x^\star\) is convergence stable exactly when \(r<\tfrac23\).

At \(x^\star=\tfrac12\), put \(t=y-\tfrac12\).  Direct substitution gives
\[
\pi(y,y)=\frac12t^2,\qquad \pi\left(y,\frac12\right)=-\frac12t^2,
\qquad \pi\left(\frac12,\frac12\right)=0,
\]
so the invasion fitness is exactly
\[
\varphi_{1/2}^r(y)=\frac{2r-1}{2}\left(y-\frac12\right)^2.
\]
Consequently the singular strategy is a strict local invasion-fitness maximum for \(r<\tfrac12\), neutral for \(r=\tfrac12\), and a strict local minimum for \(r>\tfrac12\).  Combining this with convergence stability proves that \(x^\star\) is an evolutionary branching point throughout \(\tfrac12<r<\tfrac23\).  In particular, moving from \(r<\tfrac12\) to this interval changes the same convergence-stable singular strategy from ESS to branching point.
## Verification
The algebra was independently replayed symbolically from the stated payoff and invasion-fitness definition.  The checker differentiates the exact polynomial, verifies \(D_r(x)=(-2+3r)(x-\tfrac12)\), verifies the mutant curvature \(-1+2r\), and verifies the exact resident-singular invasion fitness \(\tfrac{2r-1}{2}(y-\tfrac12)^2\).  It also checks representative rational values on both sides of the \(r=\tfrac12\) threshold.

The proof is exact; no finite simulation or numerical enumeration is used to infer the interval claim.
## Relationship to prior work
Iyer and Killingback introduced the invasion-fitness formula above for generic pairwise continuous games with assortment and proved, for their continuous snowdrift and tragedy-of-the-commons examples, that increasing assortment suppresses evolutionary branching.  They then conjectured that this inhibiting effect holds more broadly.  The present quadratic payoff stays inside their generic pairwise invasion formalism but outside those special payoff families, and it reverses the qualitative effect.

Coder Gylling and Brännström likewise found reduced branching with increasing relatedness in an additive nonlinear public-goods class.  Their benefit-cost assumptions do not imply the present payoff, whose mixed curvature is negative and whose partner-only quadratic term is essential to the threshold separation.  Leeks, dos Santos, and West observed branching in a symbiont simulation in which transmission and relatedness interact, but reported that the causal influences could not be disentangled in branching runs; this does not give the fixed-assortment counterexample above.  Jensen and Rigos analyze non-random matching for finite pure-strategy games, not continuous-trait adaptive-dynamics branching.
## Limitations
The payoff is a mathematical continuous game, not a demonstrated social dilemma and not constrained to the monotone benefit-cost forms used in the motivating cooperation models.  The result therefore rules out an unqualified general inhibition principle but leaves open whether inhibition follows under additional biologically motivated curvature, monotonicity, or public-goods assumptions.

The claim is local in the standard adaptive-dynamics sense.  It establishes the branching-point criterion but does not analyze the subsequent dimorphic trajectory, finite-population stochasticity, non-small mutations, or endogenous assortment.  At \(r=\tfrac12\) and \(r=\tfrac23\) degeneracies occur and are excluded from the strict branching interval.
## References
1. S. Iyer and T. Killingback, “Evolution of Cooperation in Social Dilemmas with Assortative Interactions,” *Games* 11(4), 41 (2020). DOI: 10.3390/g11040041.
2. K. Coder Gylling and Å. Brännström, “Effects of Relatedness on the Evolution of Cooperation in Nonlinear Public Goods Games,” *Games* 9(4), 87 (2018). DOI: 10.3390/g9040087.
3. A. Leeks, M. dos Santos, and S. A. West, “Transmission, relatedness, and the evolution of cooperative symbionts,” *Journal of Evolutionary Biology* 32, 1036–1045 (2019). DOI: 10.1111/jeb.13505.
4. M. K. Jensen and A. Rigos, “Evolutionary games and matching rules,” *International Journal of Game Theory* 47, 707–735 (2018). DOI: 10.1007/s00182-018-0630-1.
