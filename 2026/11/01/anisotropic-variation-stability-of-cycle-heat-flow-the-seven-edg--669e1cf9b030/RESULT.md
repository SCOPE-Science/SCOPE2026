# Anisotropic variation stability of cycle heat flow: the seven-edge rigidity threshold

## Finding

Let \(C_n\), \(n\ge 3\), be the simple cycle with vertices \(0,\ldots,n-1\), indices read modulo \(n\), and **unit conductances** for its combinatorial Laplacian \(L\). Independently choose **positive variation weights** \(w_0,\ldots,w_{n-1}\) on the successive edges \(\{i,i+1\}\). Put
\[
J_w(f)=\sum_{i=0}^{n-1}w_i|f(i+1)-f(i)|,\qquad H_t=e^{-tL}.
\]
The following is a necessary and sufficient, all-times, all-input classification of
\[
J_w(H_tf)\le J_w(f)\quad\text{for every }f\in\mathbb R^n\text{ and }t\ge0.
\]

* **Three edges:** every positive weight vector works.
* **Four edges:** exactly those weights satisfying \(3(w_i+w_{i+1})\ge w_{i-1}+w_{i+2}\) for all \(i\).
* **Five edges:** exactly those weights satisfying, for all \(i\), both
  \[
  3(w_i+w_{i+1})\ge w_{i-1}+w_{i+2},\qquad
  2(w_i+w_{i+2})\ge w_{i-1}+w_{i+3}.
  \]
* **Six edges:** exactly those weights for which there exists \(S>0\) with
  \[
  w_i+w_{i+3}=S,\qquad 3(w_i+w_{i+2})\ge 2S\quad(\text{every }i).
  \]
* **Seven or more edges:** exactly the constant weight vectors \(w_0=\cdots=w_{n-1}\).

All inequalities are inclusive, and failure of any necessary condition yields an explicit real input with **strict** variation increase at every sufficiently small positive time. In particular, \((2,3,2,3,2,3)\) is a nonuniform contractive six-cycle weight vector, whereas *every* nonuniform weight perturbation on a cycle of at least seven vertices destroys universal contractivity. Positive scalar multiples of any admissible weight vector remain admissible.

## Assumptions and scope

The heat operator uses the **unweighted** (unit-conductance) simple-cycle Laplacian, not the variation weights. All signals are real; the filter is linear and time-continuous. Variation is the weighted \(\ell_1\) norm of the oriented edge differences. The result makes no assertion about nonuniform heat conductances, nonlinear total-variation gradient flow, or circular-valued signals.

For \(n\ge3\), set \(g_i=f(i+1)-f(i)\). Exactly the vectors \(g\in\mathbb R^n\) with \(\sum_i g_i=0\) arise as edge-difference vectors, by integrating around the cycle. Writing \(Q\) for the nearest-neighbor cycle generator \((Qg)_i=g_{i-1}-2g_i+g_{i+1}\), direct subtraction of the vertex heat equations gives \(\partial_tg=Qg\). Consequently the claim is equivalent to contractivity of \(e^{tQ}\) in \(\|g\|_w=\sum_iw_i|g_i|\) on the zero-sum hyperplane.

## Proof

**1. Reduction to two-edge dipoles, with sharp infinitesimal tests.** Every zero-sum real vector \(g\) admits a nonnegative transport decomposition
\[
g=\sum_{i\ne j}\alpha_{ij}(e_i-e_j),\quad\alpha_{ij}\ge0,\qquad
\|g\|_w=\sum_{i\ne j}\alpha_{ij}(w_i+w_j).
\]
Indeed transport the positive coordinates to the negative ones without cancellation. For a dipole \(d=e_i-e_j\), let \(a_{ij}=1\) when the indices are adjacent on the cycle and \(0\) otherwise; write \(a_{ki}\) similarly. Its exact upper right variation derivative under the edge heat equation is
\[
F_{ij}=-(2+a_{ij})(w_i+w_j)+
\sum_{k\notin\{i,j\}}w_k|a_{ki}-a_{kj}|.\tag{1}
\]
At the two nonzero dipole coordinates the generator decreases absolute values at rate \(2+a_{ij}\); at every zero coordinate its initial absolute-value derivative is precisely the magnitude of the difference of the two adjacency indicators. Thus \(F_{ij}>0\) produces an increasing-variation witness for small \(t>0\).

Conversely, for \(0<h<1/3\) the two nonzero coordinates of \((I+hQ)(e_i-e_j)\) keep their respective signs, and every formerly zero coordinate is exactly \(h(Qd)_k\). Thus the dipole variation is **exactly**
\[
\|(I+hQ)(e_i-e_j)\|_w=(w_i+w_j)+hF_{ij}.
\]
If every \(F_{ij}\le0\), the transport decomposition and triangle inequality imply that \(I+hQ\) is contractive on the whole zero-sum hyperplane. Taking sufficiently fine Euler products \((I+tQ/m)^m\to e^{tQ}\) proves \(\|e^{tQ}g\|_w\le\|g\|_w\) for all \(t\ge0\). Hence the complete contraction condition is precisely \(F_{ij}\le0\) for **every unordered pair**.

**2. Cycles of orders three through five.** On a triangle, each dipole has derivative \(-3(w_i+w_j)<0\); in fact \(Q=-3I\) on the zero-sum subspace. On a four-cycle, opposite-edge dipoles have negative derivative \(-2(w_i+w_j)\), while adjacent-edge dipoles give
\[
F_{i,i+1}=-3(w_i+w_{i+1})+w_{i-1}+w_{i+2}.
\]
On a five-cycle the adjacent formula is unchanged, while distance-two dipoles give
\[
F_{i,i+2}=-2(w_i+w_{i+2})+w_{i-1}+w_{i+3}.
\]
These are all possible unordered pairs, proving the first three cases.

**3. The six-cycle exception.** For any \(n\ge6\), two edges separated by three steps have disjoint neighbor sets. Define \(v_i=w_i+w_{i+3}\). Equation (1) then reads
\[
F_{i,i+3}=v_{i-1}-2v_i+v_{i+1}.
\]
Summing over \(i\) gives zero. If every derivative is nonpositive, every one must therefore vanish, so the periodic discrete harmonic sequence \(v_i\) is constant: \(w_i+w_{i+3}=S\).

For \(n=6\), equation (1) for distance-two dipoles becomes
\[
F_{i,i+2}=2S-3(w_i+w_{i+2}),
\]
so their nonpositivity is precisely the stated second condition. Adjacent pairs now satisfy \(F_{i,i+1}=S-3(w_i+w_{i+1})\); the two distance-two inequalities indexed by \(i-1\) and \(i\) add to
\[
w_i+w_{i+1}+S\ge\tfrac43 S,
\]
so adjacent derivatives also cannot be positive. Thus the displayed six-cycle conditions are sufficient as well as necessary.

**4. Rigidity from seven edges onward.** For \(n=7\), the distance-three argument again forces \(w_i+w_{i+3}=S\). Hence \(w_i=w_{i+6}\) for every \(i\), and since adding six cycles through every residue class modulo seven, all weights coincide.

For \(n\ge8\), two edges four steps apart also have disjoint neighbor sets. Applying the same zero-sum/harmonic argument to \(u_i=w_i+w_{i+4}\) shows \(u_i\) is constant. Both \(w_i+w_{i+3}=S\) and \(w_i+w_{i+4}=T\) therefore hold. Subtraction makes \(w_{i+4}-w_{i+3}=T-S\) independent of \(i\). Summing these common consecutive differences around the cycle forces \(T-S=0\), whence all \(w_i\) coincide. Conversely, when all weights equal, \(e^{tQ}\) is a nonnegative stochastic matrix and contracts \(\ell_1\); this holds on the zero-sum subspace in particular. This proves the full classification. \(\square\)

## Verification

The standalone script `check.py` implements (1) and the five classification regimes independently, using exact integer arithmetic for all discrete inequalities. It checks 5,458 exhaustively enumerated positive weight profiles at orders three through nine, 5,400 additional random profiles at orders three through twenty, 160 independent matrix-exponential directional-derivative comparisons, 30 strict small-time amplification witnesses, and 805 finite-time dipole contraction comparisons. All executed successfully. Run with `python check.py` using Python 3 and NumPy/SciPy. These finite checks test signs, boundary cases, and the specified heat operator; the above argument proves the unrestricted statement.

## Relationship to prior work

The 2013 preprint and 2014 article by van Gennip, Guillen, Osting and Bertozzi establish graph total variation, the cut interpretation, and connections to graph heat-driven threshold dynamics. Those definitions motivate the variation functional here. Their studied processes include thresholding after heat diffusion, whereas the present statement classifies **unthresholded** heat-flow contraction for an independent, arbitrary positive variation-weight profile on one cycle. In their article's introduction, graph calculus, MBO sections, discussion and results, no all-cycle anisotropic heat-contraction rigidity classification was identified.

Grasmair and Lenzen investigate spatially anisotropic total-variation regularization in continuum image processing; their spatial-domain variational minimizers differ from the finite cycle's linear heat semigroup and from all-time edge-variation contraction. Cremers and Strekalovskiy study variation of signals whose **values** lie on a circle, rather than real-valued signals whose **domain graph** is a cycle. General finite-dimensional dissipativity/positive-semigroup principles can motivate the dipole reduction but do not by themselves state the seven-edge rigidity threshold or the exceptional six-cycle classification. Prior research on heat variation contraction for other graph families does not imply this anisotropic cycle statement.

## Limitations

The heat conductances are fixed to one; varying them would change the edge generator and the classification. Positive variation weights are not vertex masses or heat conductances. The classification is specific to simple cycles, not arbitrary connected graphs or discrete-time averaging. A literature search cannot establish uniqueness of the theorem; an implicit equivalent calculation in classical finite-dimensional dissipativity or finite-difference literature remains a risk. No independent mathematical review has yet been carried out.

## References

1. Y. van Gennip, N. Guillen, B. Osting, A. L. Bertozzi, *Mean curvature, threshold dynamics, and phase field theory on finite graphs*, arXiv:1307.0045, first submitted 2013-06-28; *Milan Journal of Mathematics* **82** (2014), 3–65, doi:10.1007/s00032-014-0216-8. Full text: https://arxiv.org/abs/1307.0045 .
2. M. Grasmair, F. Lenzen, *Anisotropic Total Variation Filtering*, *Applied Mathematics and Optimization* **62** (2010), 323–339, doi:10.1007/s00245-010-9105-x. Accessible manuscript: https://www.csc.univie.ac.at/paper/GraLen10.pdf .
3. D. Cremers, E. Strekalovskiy, *Total Cyclic Variation and Generalizations*, *Journal of Mathematical Imaging and Vision* **47** (2013), 258–277, doi:10.1007/s10851-012-0396-1. Accessible manuscript: https://cvai.cit.tum.de/_media/spezial/bib/cremers_strekalovskiy_jmiv12.pdf .
