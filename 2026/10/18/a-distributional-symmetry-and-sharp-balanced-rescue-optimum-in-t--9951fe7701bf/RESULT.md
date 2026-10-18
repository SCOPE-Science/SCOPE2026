# A distributional symmetry and sharp balanced-rescue optimum in two-patch extinction

## Finding

In the continuous-time two-patch binary-occupancy model defined below, begin with both patches occupied. For all local extinction rates \(a,b>0\) and directional recolonization rates \(c,d\ge0\), let \(T_{c,d}\) be the first time that both patches are empty. The entire law of \(T_{c,d}\) is unchanged when \(c\) and \(d\) are exchanged, even when \(a\ne b\). More generally, at a fixed total directional-recolonization intensity \(C=c+d\), the law depends on the allocation only through \(z=cd\). For every \(s>0\), its Laplace transform is strictly decreasing with \(z\). Therefore the balanced allocation \(c=d=C/2\) uniquely minimizes \(\mathbb E[e^{-sT_{c,d}}]\) for **every** \(s>0\) among fixed-budget allocations when \(C>0\), and uniquely maximizes both mean extinction time and its variance. No first-order stochastic dominance is asserted.

Precisely, put \(K=a+b+C\), \(B=abK\), \(H=a^2+ab+b^2+(a+b)C+cd\), and \(A=a^2+3ab+b^2+(a+b)C+cd\). Then
\[
\mathbb E[T_{c,d}]=\frac{H}{B},\qquad
\operatorname{Var}(T_{c,d})=\frac{A^2}{B^2}-\frac{2(2(a+b)+C)}{B}-\frac{4}{K^2}.
\]
At fixed \(C>0\), these two quantities increase strictly with \(cd\); the first increases linearly and the second quadratically.

## Assumptions and scope

States are \(11\) (both occupied), \(10\) (only patch 1 occupied), \(01\) (only patch 2 occupied), and \(00\) (absorbing extinction). An occupied patch 1 becomes empty at rate \(a\), and an occupied patch 2 at rate \(b\), independently of the occupancy of the other patch. When only patch 1 is occupied, successful recolonization of patch 2 occurs at rate \(c\). When only patch 2 is occupied, successful recolonization of patch 1 occurs at rate \(d\). No exogenous colonization occurs after total extinction, no other transitions are allowed, and the initial state is exactly \(11\). This is a finite-state ecological occupancy model, not a population-count model.

For fixed \(C\ge0\), an allocation is any \((c,d)\in[0,\infty)^2\) satisfying \(c+d=C\). No cost equivalence is implied outside this explicitly assumed linear rate budget. Since \(a,b>0\), absorption occurs almost surely and all extinction-time moments are finite.

## Proof

Order the transient states as \((11,10,01)\). The subgenerator and absorption-rate vector are
\[
Q=\begin{pmatrix}-(a+b)&b&a\\ c&-(a+c)&0\\ d&0&-(b+d)\end{pmatrix},\qquad
r=-Q\mathbf 1=\begin{pmatrix}0\\a\\b\end{pmatrix}.
\]
First-step conditioning, or direct inversion of \((sI-Q)\), gives the Laplace transform of the time to absorption from \(11\):
\[
L_{c,d}(s)=\mathbb E[e^{-sT_{c,d}}]
=\frac{ab(2s+K)}{D_{C,cd}(s)},\quad s\ge0,
\]
where
\[
D_{C,z}(s)=s^3+[2(a+b)+C]s^2
+[a^2+3ab+b^2+(a+b)C+z]s+abK.
\]
For completeness, the first-step equations for state-wise transforms \(f_{11},f_{10},f_{01}\) are
\[
(s+a+b)f_{11}=bf_{10}+af_{01},\quad
(s+a+c)f_{10}=a+cf_{11},\quad
(s+b+d)f_{01}=b+df_{11}.
\]
Eliminating \(f_{10}\) and \(f_{01}\) yields the stated rational expression. Its denominator is positive for \(s\ge0\): every displayed coefficient is positive except possibly \(z\), which is nonnegative. Its numerator is positive.

The rational transform depends on \((c,d)\) only through their sum \(C\) and product \(z=cd\). Uniqueness of Laplace transforms of finite nonnegative random variables proves distributional equivalence for any two allocations sharing these values. In particular \((c,d)\) and \((d,c)\) give exactly the same law, despite possibly unequal \(a,b\).

For fixed \(C\), write \(D_{C,z}(s)=D_{C,0}(s)+sz\). Whenever \(s>0\) and \(z_2>z_1\ge0\),
\[
L_{z_1}(s)-L_{z_2}(s)
=\frac{ab(2s+K)s(z_2-z_1)}{D_{C,z_1}(s)D_{C,z_2}(s)}>0.
\]
The arithmetic-geometric mean inequality gives \(cd\le C^2/4\), with equality precisely at \(c=d=C/2\). This proves the strict simultaneous Laplace-transform optimum for \(C>0\). For \(C=0\), the allocation is unique.

Differentiate the rational Laplace transform at \(s=0\): \(\mathbb E[T]=-L'(0)\), \(\mathbb E[T^2]=L''(0)\), and variance is \(L''(0)-L'(0)^2\). This gives the displayed moment formulas. Holding \(C\) fixed and writing \(z=cd\),
\[
\frac{\partial\mathbb E[T]}{\partial z}=\frac1B>0,\qquad
\frac{\partial\operatorname{Var}(T)}{\partial z}=\frac{2A}{B^2}>0.
\]
Thus the same unique allocation maximizes both moments. This does not prove minimization of variance, universal stochastic dominance, or an optimal allocation when effort changes \(a\), \(b\), or the colonization-rate budget.

## Verification

The standalone `verify.py` uses symbolic inversion of the three-state transient generator to verify the Laplace identity and differentiated moments, then recomputes five exact-rational allocations. For \(a=4\), \(b=1\), and \(C=2\), allocating all recolonization in either direction gives **the same** transform and moments:
\[
L(1)=\frac9{20},\quad \mathbb E[T]=\frac{31}{28},\quad
\operatorname{Var}(T)=\frac{785}{784}.
\]
For the balanced allocation \(c=d=1\):
\[
L(1)=\frac49<\frac9{20},\quad
\mathbb E[T]=\frac87>\frac{31}{28},\quad
\operatorname{Var}(T)=\frac{54}{49}>\frac{785}{784}.
\]
These rational checks illustrate the theorem; the proof above applies to every admissible real parameter.

## Relationship to prior work

Vuilleumier and Possingham (2006) investigate colonization asymmetry and metapopulation viability through Monte Carlo simulation over larger patch systems. Their published qualitative asymmetry results motivate studying exact distributional consequences; the accessible account does not supply this two-patch fixed-budget Laplace identity. Etienne and Heesterbeek (2001) investigate conservation rules governing colonization and extinction controls, and Nicol and Possingham (2010) optimize restoration decisions with dynamic programming. Their reported optimization frameworks differ from the fixed total of two directional successful-colonization rates considered here. These comparisons are limited by incomplete access to some full texts; an overlooked specialization remains possible. The elementary general identity \(L(s)=e_{11}^{\mathsf T}(sI-Q)^{-1}r\) for absorbing chains is standard and not claimed as new. The contribution is the two-patch cancellation, complete allocation-law invariant, and simultaneous sharp optimum.

## Limitations

The theorem concerns extinction from initially full occupancy. It does not assert invariance from a singly occupied patch or from arbitrary initial mixtures. The result depends on constant exponential holding rates, absence of external immigration from extinction, and a fixed sum of **successful recolonization intensities**, not on fixed movement probabilities, expenditures, or habitat areas. Laplace-transform order is weaker than usual stochastic order. The exact distributional invariance need not persist with more than two patches. Some potentially relevant historical material was not fully accessible, so bibliographic uniqueness is not certified. Independent audit has not been performed.

## References

1. Vuilleumier, S. & Possingham, H. P. (2006), Does colonization asymmetry matter in metapopulations?, Proceedings of the Royal Society B 273, 1637–1642, DOI 10.1098/rspb.2006.3469 (online March 29, 2006).
2. Etienne, R. S. & Heesterbeek, J. A. P. (2001), Rules of thumb for conservation of metapopulations based on a stochastic winking-patch model, American Naturalist 158, 389–407, DOI 10.1086/321986.
3. Nicol, S. C. & Possingham, H. P. (2010), Should metapopulation restoration strategies increase patch area or number of patches?, Ecological Applications 20, 566–581, DOI 10.1890/08-2216.1.
