# Sharp two-coordinate total-variation homogenization over arbitrary probability spaces

## Finding
For every measurable space \((\Omega,\mathcal F)\) and all probability measures \(P_1,P_2,Q_1,Q_2\), put \(\bar P=(P_1+P_2)/2\) and \(\bar Q=(Q_1+Q_2)/2\). Then
\[
\operatorname{TV}(P_1\otimes P_2,Q_1\otimes Q_2)
\geq \frac{2}{3}\operatorname{TV}(\bar P^{\otimes2},\bar Q^{\otimes2}).
\]
The coefficient \(2/3\) is the best possible universal coefficient. It is approached already by laws on three distinct points. Consequently, the exact worst-case amplification of total variation under two-coordinate marginal homogenization is \(3/2\).

## Assumptions and scope
The four measures are arbitrary probabilities on the same measurable space. No atomlessness, mutual absolute continuity, density, moment condition, or bounded support is assumed. Their product measures are defined on the usual product sigma algebra. Throughout, \(\operatorname{TV}(\mu,\nu):=\sup_A|\mu(A)-\nu(A)|\); for a finite alphabet it is one half of the sum of the absolute signed masses. The theorem concerns exactly two independent coordinates; it makes no sharp-constant claim for other numbers of coordinates.

## Proof
Write
\[
\Delta:=\operatorname{TV}(P_1\otimes P_2,Q_1\otimes Q_2),\qquad
 d_i:=\operatorname{TV}(P_i,Q_i)\quad(i=1,2).
\]
The coordinate projections are measurable, hence total-variation data processing gives \(d_1,d_2\leq\Delta\).

Let \(\mathcal L:=\{1,2\}\times\Omega\) with the product sigma algebra and let \(e_i\) denote the Dirac probability at label \(i\). Construct the coordinate-labelled probabilities
\[
L_P=\tfrac12(e_1\otimes P_1+e_2\otimes P_2),\qquad
L_Q=\tfrac12(e_1\otimes Q_1+e_2\otimes Q_2).
\]
Forgetting the label maps \(L_P\) to \(\bar P\) and \(L_Q\) to \(\bar Q\). Data processing for its twofold product therefore yields
\[
\operatorname{TV}(\bar P^{\otimes2},\bar Q^{\otimes2})
\leq \operatorname{TV}(L_P^{\otimes2},L_Q^{\otimes2}).
\]
The four ordered pairs of labels are disjoint measurable cells of the lifted product space. Total variation consequently splits *exactly* over those cells:
\[
\begin{aligned}
\operatorname{TV}(L_P^{\otimes2},L_Q^{\otimes2})
={}&\tfrac14\operatorname{TV}(P_1^{\otimes2},Q_1^{\otimes2})
 +\tfrac12\Delta
 +\tfrac14\operatorname{TV}(P_2^{\otimes2},Q_2^{\otimes2}).
\end{aligned}
\]
Here the two mixed cells give equal contributions because coordinate transposition preserves total variation. For each \(i\), the standard product telescoping decomposition
\[
P_i\otimes P_i-Q_i\otimes Q_i
=(P_i-Q_i)\otimes P_i+Q_i\otimes(P_i-Q_i)
\]
and the signed-measure variation triangle inequality imply
\(\operatorname{TV}(P_i^{\otimes2},Q_i^{\otimes2})\leq2d_i\leq2\Delta\). Therefore
\[
\operatorname{TV}(\bar P^{\otimes2},\bar Q^{\otimes2})
\leq\tfrac14(2\Delta)+\tfrac12\Delta+\tfrac14(2\Delta)
=\tfrac32\Delta,
\]
which proves the asserted universal inequality. All steps apply without modifications to arbitrary measurable spaces.

To prove optimality, take three distinct points \(a,b,c\), choose \(0<\varepsilon<1\), and define
\[
P_1=(1-\varepsilon)\delta_a+\varepsilon\delta_b,\quad
P_2=\delta_b,\quad Q_1=\delta_a,\quad
Q_2=(1-\varepsilon)\delta_b+\varepsilon\delta_c.
\]
The heterogeneous product laws share mass \(1-\varepsilon\) at \((a,b)\), while their residual masses \(\varepsilon\) lie at the distinct pairs \((b,b)\) and \((a,c)\). Hence their total variation is exactly \(\varepsilon\).

In the coordinate order \((a,b,c)\), the two averaged marginals are
\[
\bar P=\left(\tfrac{1-\varepsilon}{2},\tfrac{1+\varepsilon}{2},0\right),\qquad
\bar Q=\left(\tfrac12,\tfrac{1-\varepsilon}{2},\tfrac{\varepsilon}{2}\right).
\]
For their ordered twofold products, the *only positive* signed entries of \(\bar P^{\otimes2}-\bar Q^{\otimes2}\) are \((b,b)\), carrying \(\varepsilon\), and \((a,b),(b,a)\), each carrying \(\varepsilon(1-\varepsilon)/4\). Their sum is the total variation,
\[
\operatorname{TV}(\bar P^{\otimes2},\bar Q^{\otimes2})
=\varepsilon+\tfrac12\varepsilon(1-\varepsilon)
=\tfrac12\varepsilon(3-\varepsilon).
\]
Thus the ratio of heterogeneous to homogenized distances is \(2/(3-\varepsilon)\to2/3\) as \(\varepsilon\downarrow0\). No coefficient greater than \(2/3\) can hold on all measurable spaces. This sharpness argument uses a limit of nonidentical pairs, not a claim of attainment at a positive distance.

## Verification
The standalone `verify.py` uses exact rational arithmetic to reconstruct the nine signed cells of the three-point witness for many rational values of \(\varepsilon\), verify the closed formulas, verify the labelled-cell identity on finite probability vectors, and test the universal bound across a finite parameter grid. Run `python3 verify.py` with Python's standard library. These finite computations are consistency checks; the unrestricted inequality and sharp limiting construction are proved above without enumeration.

## Relationship to prior work
Kontorovich, *A homogenization principle for total variation* (arXiv:2604.03882, first available 4 April 2026), established a positive dimension-free homogenization constant for arbitrary measurable spaces and explicitly left identification of the exact optimal constant and extremizers open. Its Theorem 4 gives a constant exceeding \(0.1489\), not the sharp value for two coordinates. The same work introduces coordinate-labelled lifting (Theorem 3). Here that lifting is combined with the exact four-cell decomposition and coordinatewise total-variation bounds to obtain a sharp two-coordinate result; the three-atom obstruction supplies the matching upper bound.

The earlier *TV homogenization inequalities* (arXiv:2601.04079) treats Bernoulli product laws and exhibits an \(8/9\) obstruction in that restricted alphabet. That Bernoulli-specific theory neither covers general three-point laws nor implies the sharp general-alphabet coefficient \(2/3\). Existing bounds on total variation of products and heterogeneous convolutions do not, in the inspected statements, determine this two-coordinate sharp constant.

## Limitations
Only the two-coordinate sharp constant is determined. The result does not identify sharp constants for larger product lengths or classify all extremizing sequences. The three-point witness approaches but does not attain the positive-distance infimum at its limiting parameter. A differently formulated earlier sharp two-coordinate theorem could affect priority; literature searches do not prove uniqueness of the result. Independent validation has not been carried out.

## References
- A. Kontorovich, *A homogenization principle for total variation*, arXiv:2604.03882 (2026), https://arxiv.org/abs/2604.03882 . Relevant: Introduction; Theorems 3 and 4; proof of Theorem 4.
- A. Kontorovich, *TV homogenization inequalities*, arXiv:2601.04079 (2026), https://arxiv.org/abs/2601.04079 . Relevant: Bernoulli restriction; homogenization constant and obstruction discussion.
