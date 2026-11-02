# Exact openness-response reversals in a two-community partisan voter mean field

## Finding

In the two-community mean-field voter system with strictly opposed intrinsic preferences, greater exposure to the other community need not reduce stationary polarization. At any hyperbolic attracting interior equilibrium, there is an exact sign test for the change in stationary polarization when either community's external-neighbor fraction is varied separately. An admissible stable equilibrium with rational parameters has **positive** polarization sensitivity to the first community's openness and **negative** sensitivity to the second community's openness:
\[
\frac{\partial P^*}{\partial\gamma_1}=\frac{688}{785}>0,
\qquad
\frac{\partial P^*}{\partial\gamma_2}=-\frac{1220}{471}<0.
\]
Consequently, increasing the first community's normalized exposure by a sufficiently small positive amount, with the second's exposure and both preferences fixed, strictly **increases** the equilibrium polarization.

## Assumptions and scope

The two communities have normalized fractions \(x,y\in[0,1]\) holding the positive opinion. The intrinsic biases satisfy \(0<h_1<1\) and \(-1<h_2<0\), and the community external-neighbor fractions satisfy \(0<\gamma_1,\gamma_2<1\). Define
\[
 Q_1=(1-\gamma_1)x+\gamma_1y,\quad
 Q_2=\gamma_2x+(1-\gamma_2)y,\quad
 A_1=1+h_1-2h_1x,\quad A_2=1+h_2-2h_2y.
\]
The continuous deterministic mean-field dynamics, exactly the normalized equations (10) of Zimmaro--Contucci--Kertész (2023), are
\[
 \dot x=F_1=\tfrac12\left[A_1Q_1-(1-h_1)x\right],\qquad
 \dot y=F_2=\tfrac12\left[A_2Q_2-(1-h_2)y\right].
\]
At an interior equilibrium, \(x>y\) (as proved below), and stationary polarization in the source's normalization is \(P^*=x-y\). Put \(J=D_{(x,y)}(F_1,F_2)\) and \(D=\det J\). The sensitivity formulas below concern any interior equilibrium with \(D>0\) and \(\operatorname{tr}J<0\). By the implicit function theorem, a smooth locally attracting equilibrium branch exists under sufficiently small perturbations of either exposure parameter.

## Proof

**Ordering.** Suppose at an interior stationary point that \(x\le y\). Then \(Q_1\ge x\) and \(A_1>0\). Direct rearrangement yields
\[
F_1=h_1x(1-x)+\tfrac12 A_1(Q_1-x)>0,
\]
contradicting stationarity. Hence \(x>y\), and the absolute value in the polarization measure can be dropped locally.

**Exact response.** Write \(J=\begin{pmatrix}a&b\\c&d\end{pmatrix}\), with determinant \(D=ad-bc\). Differentiation of the defining equations gives
\[
\begin{aligned}
\partial_{\gamma_1}F_1&=\tfrac12(y-x)A_1,&\partial_{\gamma_1}F_2&=0,\\
\partial_{\gamma_2}F_1&=0,&\partial_{\gamma_2}F_2&=\tfrac12(x-y)A_2.
\end{aligned}
\]
Moreover, differentiating both vector-field components in the diagonal \((1,1)\) direction yields
\[
a+b=h_1(1-x-Q_1),\qquad c+d=h_2(1-y-Q_2).
\]
Implicit differentiation of \(F_1=F_2=0\) and multiplication by \((1,-1)\) gives the exact identities
\[
\boxed{\frac{\partial P^*}{\partial\gamma_1}
=\frac{(x-y)A_1 h_2(1-y-Q_2)}{2D}},\qquad
\boxed{\frac{\partial P^*}{\partial\gamma_2}
=\frac{(x-y)A_2 h_1(1-x-Q_1)}{2D}}.
\]
Because \(x-y>0\), \(A_1\ge1-h_1>0\), \(A_2\ge1+h_2>0\), and \(D>0\), the two sign tests are
\[
\operatorname{sgn}\frac{\partial P^*}{\partial\gamma_1}=\operatorname{sgn}(y+Q_2-1),\qquad
\operatorname{sgn}\frac{\partial P^*}{\partial\gamma_2}=\operatorname{sgn}(1-x-Q_1).
\]
Equalities identify the zero-response surfaces; the sign tests hold at every attracting hyperbolic interior equilibrium, with no assumption that the biases have equal magnitudes.

**Strict exact example.** Choose
\[
\gamma_1=\gamma_2=\tfrac14,\quad h_1=\tfrac5{28},\quad h_2=-\tfrac2{19},\quad
(x^*,y^*)=(\tfrac9{10},\tfrac34).
\]
These are strictly admissible, and substitution gives \(Q_1=69/80\), \(Q_2=63/80\), and \(F_1=F_2=0\). The Jacobian at this point is
\[
J=\begin{pmatrix}-109/448&3/28\\5/38&-3/40\end{pmatrix},
\qquad\operatorname{tr}J=-\tfrac{713}{2240}<0,
\quad\det J=\tfrac{1413}{340480}>0.
\]
Both eigenvalues therefore have strictly negative real parts. Since \(y^*+Q_2=123/80>1\) and \(x^*+Q_1=141/80>1\), exact substitution into the sensitivity identities gives the two fractions in the Finding section. The implicit function theorem and hyperbolic stability show that these inequalities persist along smooth, locally attracting equilibrium branches for all sufficiently small positive/negative parameter perturbations. In particular, a strictly positive increase in polarization results from increasing \(\gamma_1\) sufficiently slightly while holding \(\gamma_2,h_1,h_2\) fixed.

**Undirected-network realization.** Equal community sizes \(\alpha=1/2\) and symmetric stochastic-block connection probabilities \(p_{12}=p_{21}=1/4\), \(p_{11}=p_{22}=3/4\) realize \(\gamma_1=\gamma_2=1/4\). Decreasing \(p_{11}\) slightly with \(p_{12},p_{21},p_{22}\) unchanged increases only \(\gamma_1\), preserving valid undirected connection probabilities. Thus the strict reversal lies within the ordinary undirected-block parameter domain, rather than requiring directed mixing.

## Verification

The accompanying standalone `verification.py` uses symbolic rational arithmetic to reconstruct both mean-field components, the complete Jacobian, the two inverse-Jacobian sensitivity identities, and the strict exact equilibrium. Its exact assertions verify the rational Jacobian, trace, determinant, derivatives, source-model consensus tests, and block-mixing realization. Run with `python verification.py` with SymPy installed. The all-parameter sensitivity formulas are analytic identities; no numerical grid, simulation, or sampled parameter set is treated as their proof.

## Relationship to prior work

Zimmaro, Contucci, and Kertész (2023), Section 3.2, equations (10)--(16), introduce this modular voter mean field and determine consensus thresholds. Their figures investigate stationary polarization numerically under changes in modularity, describing increased polarization under segregation in investigated regimes. They do not state the two exact *separate* openness derivatives or the stable reversal at an admissible rational parameter point. The present theorem uses exactly their model, not a redefined update rule. Masuda, Gibert, and Redner (2010) and Masuda and Redner (2011) study partisan voting and consensus, principally without the independently variable two-community external-neighbor fractions. Peralta, Neri, Kertész, and Iñiguez (2021) analyze a distinct mechanism of algorithmic filtering and do not establish these mean-field response identities. The result provides a precise qualification to any universal inference that decreasing segregation must reduce steady-state polarization.

## Limitations

The theorem is for the deterministic two-community mean-field closure, not a statement about finite random networks, their stationary stochastic distributions, or their finite-population consensus times. The derivative claims are **local** in parameter space on a hyperbolic attracting interior branch; they do not imply a global monotonicity reversal over all openness values. No uniqueness or global attraction of interior equilibria is asserted. The displayed strict witness uses unequal intrinsic bias magnitudes; nothing is claimed for all possible symmetric-bias cases. Scholarly novelty is assessed relative to the cited material; unindexed equivalent results remain a bibliographic risk. Independent validation has not been performed.

## References

1. F. Zimmaro, P. Contucci, J. Kertész, *Voter-like Dynamics with Conflicting Preferences on Modular Networks*, arXiv:2303.09587 (first posted 2023-03-16); *Entropy* **25** (2023), 838, DOI:10.3390/e25060838.
2. N. Masuda, N. Gibert, S. Redner, *Heterogeneous Voter Models*, *Physical Review E* **82** (2010), 010103, arXiv:1003.0768.
3. N. Masuda, S. Redner, *Can Partisan Voting Lead to Truth?*, *Journal of Statistical Mechanics* (2011), L02002, arXiv:1012.2462.
4. A. F. Peralta, M. Neri, J. Kertész, G. Iñiguez, *Effect of algorithmic bias and network structure on coexistence, consensus, and polarization of opinions*, *Physical Review E* **104** (2021), 044312.
