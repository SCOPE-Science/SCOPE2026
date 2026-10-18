# Exact two-leader gain transition on complete-graph coronas

## Finding

Let \(m\ge3\) be an integer and let \(G_m=K_m\circ K_1\), the graph formed from a unit-weight complete graph on \(m\) core vertices by attaching one private unit-weight pendant leaf to every core. Select exactly two distinct vertices \(S\) as noisy consensus leaders with the same finite gain \(\kappa>0\), and minimize
\[
J_m(S;\kappa)=\operatorname{tr}\!\left[(L_m+\kappa\operatorname{diag}(\mathbf1_S))^{-1}\right].
\]
The quantity is twice the total steady-state variance for independent unit-intensity disturbances in the standard first-order consensus model.

Define the critical gain
\[
\boxed{\kappa_m=\frac m4\left(m-6+\sqrt{m^2-4m+20}\right)}.
\]
For \(0<\kappa<\kappa_m\), **all and only** the minimizing pairs are two different core vertices. For \(\kappa>\kappa_m\), **all and only** the minimizing pairs comprise one core vertex and the pendant leaf belonging to a *different* core. At equality, both types and no others minimize. In particular, two pendant leaves and a core with its *own* leaf are never optimal. The two optimizing families contain, respectively, \(\binom m2\) and \(m(m-1)\) vertex pairs. The transition has the scaling
\[
\kappa_m=\frac{m^2}{2}-2m+2+O(m^{-1}).
\]
For example, \(\kappa_3=3(\sqrt{17}-3)/4\) and \(\kappa_5=5\). These conclusions cover every integer \(m\ge3\) and every real \(\kappa>0\), without additional symmetry constraints on which two vertices may be selected.

## Assumptions and scope

All original edges have conductance one. Every vertex experiences independent white stochastic forcing of equal intensity; selected leaders additionally use identical positive feedback gain \(\kappa\). There are exactly two distinct leaders. \(L_m\) is the ordinary combinatorial Laplacian; the invertible pinned Laplacian is \(L_m+\kappa\operatorname{diag}(\mathbf1_S)\). The unnormalized inverse trace, rather than half of it, is the optimization criterion. The result concerns selection of leader *locations*, not optimization over gains, edge weights, dynamics with perfect/noiseless leaders, or general coronas with noncomplete cores.

For orbit notation, write \(c_i\) for core vertex \(i\) and \(\ell_i\) for its leaf. The four and only four types of unordered distinct pairs are \(CC=\{c_i,c_j\}\), \(LL=\{\ell_i,\ell_j\}\), \(CO=\{c_i,\ell_i\}\), and \(CX=\{c_i,\ell_j\}\), with \(i\ne j\) wherever two indices are shown.

## Proof

**Step 1: a resolvent allowing exact evaluation of all four pair types.** Order core vertices before leaves, let \(\mathbf J\) be the all-ones matrix of size \(m\), and set \(I=I_m\). The Laplacian is
\[
L_m=\begin{pmatrix}(m+1)I-\mathbf J&-I\\-I&I\end{pmatrix}.
\]
For \(t>0\), eliminate the leaf block from \(L_m+tI_{2m}\). The core-core block \(C(t)\) of its inverse becomes
\[
C(t)=\left(mI-\mathbf J+\frac{t(t+2)}{1+t}I\right)^{-1}
     =v(t)I+\frac{u(t)-v(t)}m\mathbf J,
\]
where
\[
u(t)=\frac{1+t}{t(t+2)},\qquad
v(t)=\frac{1+t}{t(t+2)+m(1+t)}.
\]
Here the formulas denote scalar rational functions at \(t>0\), so no singular inverse is used at \(t=0\). The core-leaf and leaf-leaf blocks of the inverse are \(C(t)/(1+t)\) and \(I/(1+t)+C(t)/(1+t)^2\), respectively. Its determinant satisfies
\[
\det(L_m+tI_{2m})=t(t+2)\left(t^2+(m+2)t+m\right)^{m-1}.
\]
For a pair \(S\), put \(G_S(t)=\big[(L_m+tI_{2m})^{-1}\big]_{S,S}\), a \(2\times2\) principal submatrix. The matrix determinant lemma gives
\[
\det(L_m+tI_{2m}+\kappa\operatorname{diag}(\mathbf1_S))
=\det(L_m+tI_{2m})\det(I_2+\kappa G_S(t)).
\]
For a positive definite matrix \(A\), \(\frac{d}{dt}\log\det(A+tI)|_{t=0}=\operatorname{tr}(A^{-1})\). Thus differentiation of the displayed identity and the limit \(t\downarrow0\), with cancellation of the common simple pole, calculate \(J_m(S;\kappa)\) exactly.

**Step 2: the four rational orbit values.** Direct substitution and collection of terms produce (\(k\) abbreviates \(\kappa\) *only within the following display*)
\[
\begin{aligned}
J_{CC}&=\frac{k^2(m^2+3m-6)+k(m^3+4m^2-4m)+m^3}{km(k+m)},\\
J_{LL}&=\frac{k^2(2m^3+2m^2-5m-6)+k(3m^3+2m^2-4m)+m^3}{km(k(m+1)+m)},\\
J_{CO}&=\frac{k^2(m^2+3m-4)+k(4m^2+6m-8)+2m^2}{km(k+2)},\\
J_{CX}&=\frac{k^2(m^3+5m^2-2m-12)+k(4m^3+6m^2-8m)+2m^3}{km(k(m+2)+2m)}.
\end{aligned}
\]
Each equals the inverse trace for *every* pair in its automorphism orbit, and every pair belongs to one of the four orbits.

**Step 3: eliminate dominated locations.** Exact subtraction gives
\[
J_{CC}-J_{CO}=-\frac{2k^2+k(m^2+4)+m^3}{m(k+2)(k+m)}<0,
\]
and
\[
J_{CC}-J_{LL}=-\frac{k^2(m^2-2m-2)+km(m-3)(m+2)+m^2(m-2)}{(k+m)(k(m+1)+m)}<0.
\]
Indeed every denominator is positive. For \(m\ge3\), the first numerator is strictly positive and the second is strictly positive because \(m^2-2m-2>0\), \(m-3\ge0\), and \(m-2>0\). Therefore neither \(CO\) nor \(LL\) can minimize.

**Step 4: solve the remaining sharp comparison.** Again exactly,
\[
J_{CC}-J_{CX}=\frac{2k^2+m(6-m)k-m^2(m-2)}{(k+m)(k(m+2)+2m)}.
\]
The denominator is positive. The numerator is a quadratic with positive leading coefficient and negative constant term for \(m\ge3\); hence it has precisely one positive zero, namely the displayed \(\kappa_m\). It is negative below this zero and positive above it. Combining with Step 3 gives the complete set of minimizers and proves the strictness and equality statements. The asymptotic law follows by expanding the square root in \(\kappa_m\). \(\square\)

## Verification

The included standalone `verify.py` reconstructs all four rational expressions from the \(2\times2\) determinant expansion of the exact resolvent, symbolically verifies the three comparisons decisive for global optimality, and independently forms the full pinned Laplacian with exact rational entries. It exhaustively evaluates all unordered leader pairs for \(m=3,4,5,6,7\) and the four gains \(\kappa\in\{1/5,1,5,100\}\): 980 exact-rational direct-matrix comparisons, including the equality instance \(m=5,\kappa=5\). Every tested entry agrees with the formulas and classified optimum. Run `python verify.py` with SymPy installed. The theorem for all graph orders and all positive gains follows from Steps 1–4; the finite checks are not a substitute for that proof.

## Relationship to prior work

Lin, Fardad, and Jovanović (first publicly posted 2013-02-03) formulate the noise-corrupted leader-placement problem using precisely this inverse-trace criterion, and present general optimization/approximation methods. Fitch and Leonard (first publicly posted 2014-07-07) derive a graph-wide two-leader joint-centrality formula and explicitly solve cycle examples. Patterson, Yi, and Zhang (2017) derive resistance-distance-based performance formulas and solve selected paths, cycles and rooted trees. Those general identities provide methods for evaluating objective values but do not, in the inspected texts, state this corona family's all-gain classification or its algebraic phase boundary. In particular, their general optimization characterization requires evaluating and comparing locations before the sharp threshold follows.

This claim is distinct from a fastest-mixing Markov-chain optimization on the same underlying corona graph: that task optimizes edge transition probabilities and a spectral mixing rate, whereas this one fixes unit edges and optimizes a two-element leader set for a pinned inverse trace.

## Limitations

No independent audit has been performed. Originality assessment is necessarily limited to inspected accessible sources and targeted literature/database searches; an unindexed equivalent result remains possible. The theorem does not optimize the feedback gain or edge weights and does not extend automatically from a complete graph to a general corona base. The factor \(1/2\) converting inverse trace into stationary variance must be retained when physical variance, rather than \(J_m\), is quoted. Direct finite matrix evaluations validate examples but do not establish the infinite-parameter claim.

## References

1. F. Lin, M. Fardad and M. R. Jovanović, *Algorithms for Leader Selection in Stochastically Forced Consensus Networks*, arXiv:1302.0450, first public version 2013-02-03; IEEE Transactions on Automatic Control 59 (2014), 1789–1802. https://arxiv.org/abs/1302.0450
2. K. E. Fitch and N. E. Leonard, *Joint Centrality Distinguishes Optimal Leaders in Noisy Networks*, arXiv:1407.1569, first public version 2014-07-07. https://arxiv.org/abs/1407.1569
3. S. Patterson, Y. Yi and Z. Zhang, *A Resistance Distance-Based Approach for Optimal Leader Selection in Noisy Consensus Networks*, arXiv:1708.06873, first public version 2017-08-23. https://arxiv.org/abs/1708.06873
