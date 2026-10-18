# A three-season orientation law for a two-stage population

## Finding

For a positive two-stage stage-structured population with **season-independent adult fecundity**, three seasonal environments admit an exact, geometric ordering test for long-run growth. Let the season matrices be
\[
L_i=\begin{pmatrix}0&b\\s_i&a_i\end{pmatrix},\qquad b>0,\quad 0<s_i<1,\quad 0<a_i<1,\quad i=1,2,3.
\]
The first coordinate counts juveniles and the second adults: adults produce \(b\) juveniles per step, juveniles mature with probability \(s_i\), and adults survive in the adult class with probability \(a_i\). Each ordered matrix word \(ijk\) has a three-step growth factor \(\Lambda_{ijk}=\rho(L_iL_jL_k)\). Matrix words are written in multiplication order; the first chronological transition is the rightmost factor.

Define the signed demographic area
\[
\Delta=\det\begin{pmatrix}1&a_1&s_1\\1&a_2&s_2\\1&a_3&s_3\end{pmatrix}.
\]
All six permutations form exactly two *possible spectral classes* (the two classes may coincide). Specifically,
\[
\boxed{\operatorname{sgn}(\Lambda_{123}-\Lambda_{132})=\operatorname{sgn}(\Delta).}
\]
Thus \(\Delta>0\) selects one strict best cyclic class, \(\Delta<0\) selects the other, and **every ordering is equally good exactly when the three points \((a_i,s_i)\) are collinear**. One or two phases cannot exhibit an ordering effect under rearrangement, so three is sharp.

**A stronger viability classification holds for every triple of admissible survival pairs.** If \(\Delta\ne0\), there is a nonempty open interval of shared fecundities \(b\) for which one orientation has \(\Lambda>1\) while the other has \(\Lambda<1\). If \(\Delta=0\), no choice of shared \(b\) can create such an ordering-dependent growth verdict. The two critical fecundities are the unique positive roots of the cubic equations proved below.

In particular, ordering alone can reverse the low-density extinction/growth threshold with every survival probability strictly between zero and one and with the same fecundity in every phase. For
\[
(a_1,a_2,a_3)=(\tfrac14,\tfrac12,\tfrac34),\quad
(s_1,s_2,s_3)=(\tfrac14,\tfrac34,\tfrac14),\quad b=\tfrac43,
\]
one has \(\Lambda_{123}<1<\Lambda_{132}\). The two permutations use exactly the same three seasonal matrices.

## Assumptions and scope

The state is a nonnegative column vector of expected juvenile and adult abundances. For each phase \(i\), the linear low-density recurrence is \(z_{t+1}=L_i z_t\), with \(b>0\) fixed across phases, juvenile maturation probability \(s_i\in(0,1)\), and adult staying probability \(a_i\in(0,1)\). The model has no density dependence, migration, stochastic demographic noise, or stage-dependent fecundity in addition to the displayed entries. The three specified phases repeat cyclically indefinitely; a phase rearrangement changes their order but not their matrices. A three-step factor greater than one means exponential growth in this linear model, while a factor below one means exponential decay. It does not alone establish nonlinear persistence or finite-population survival.

## Proof

**(1) Permutation reduction and minimum phase count.** Cyclic rotation of any product leaves its characteristic polynomial unchanged: \(\operatorname{tr}(ABC)=\operatorname{tr}(BCA)\) and \(\det(ABC)=\det(BCA)\). All three matrices are invertible, although this is not necessary for the trace argument. For three factors the six orders split into the cyclic classes of words \(123\) and \(132\). For two factors, \(AB\) and \(BA\) have identical trace and determinant (indeed identical eigenvalues); one factor admits no nontrivial permutation. Hence an order effect first becomes possible at three phases.

**(2) Exact orientation identity.** Direct multiplication and collection of the diagonal terms gives
\[
\begin{aligned}
T_{123}-T_{132}&=\operatorname{tr}(L_1L_2L_3)-\operatorname{tr}(L_1L_3L_2)\\
&=b\,[a_1(s_2-s_3)+a_2(s_3-s_1)+a_3(s_1-s_2)]\\
&=b\Delta.
\end{aligned}
\]
In both orders the determinant is
\[
\det(L_1L_2L_3)=\det(L_1L_3L_2)=-b^3s_1s_2s_3=-d,\qquad d>0.
\]
The two product matrices have strictly positive entries since each \(a_i,s_i,b\) is positive. For either product, its Perron root is the positive root of \(x^2-Tx-d\), namely
\[
\Lambda(T)=\frac{T+\sqrt{T^2+4d}}{2}.
\]
Since \(T>0\), \(\Lambda(T)\) increases strictly with \(T\). Therefore \(\operatorname{sgn}(\Lambda_{123}-\Lambda_{132})=\operatorname{sgn}(b\Delta)=\operatorname{sgn}(\Delta)\). The determinant \(\Delta\) vanishes precisely when the three planar demographic points are collinear, proving the necessary-and-sufficient equality characterization for all six orders.

**(3) Every noncollinear triple admits an ordering-dependent invasion interval.** The two trace expressions from multiplication have the form
\[
T_{123}=a_1a_2a_3+bC_{123},\quad C_{123}=a_1s_2+a_2s_3+a_3s_1>0,
\]
\[
T_{132}=a_1a_2a_3+bC_{132},\quad C_{132}=a_1s_3+a_2s_1+a_3s_2>0.
\]
Write \(S=s_1s_2s_3>0\) and \(A=a_1a_2a_3\in(0,1)\). The positive Perron root for either order is greater than one exactly when its characteristic polynomial at one is negative:
\[
F_{\pi}(b)=1-A-bC_{\pi}-b^3S<0.
\]
For each order, \(F_{\pi}(0)=1-A>0\), \(F_{\pi}(b)\to-\infty\) as \(b\to\infty\), and \(F_{\pi}\) is strictly decreasing for every \(b\ge0\). It has a unique positive zero \(b_{\pi}^*\). Because
\[
F_{123}(b)-F_{132}(b)=-b\Delta,
\]
these critical fecundities are unequal exactly when \(\Delta\ne0\). If \(\Delta>0\), then \(b_{123}^*<b_{132}^*\), and every \(b\in(b_{123}^*,b_{132}^*)\) gives \(\Lambda_{123}>1>\Lambda_{132}\); for \(\Delta<0\) the inequalities reverse. If \(\Delta=0\), all ordering growth factors coincide for every \(b>0\). Thus noncollinearity is necessary and sufficient for some common fecundity to make timing alone decide the linear growth verdict.

**(4) An exact rational interval witness.** For the rational parameters in the finding, direct multiplication yields
\[
T_{123}=\frac{73}{96},\qquad T_{132}=\frac{35}{32},\qquad d=\frac19.
\]
The characteristic polynomials are \(x^2-T_{ijk}x-1/9\), and at \(x=1\) their values are
\[
1-T_{123}-\frac19=\frac{37}{288}>0,\qquad
1-T_{132}-\frac19=-\frac{59}{288}<0.
\]
Each quadratic is negative at zero and has exactly one positive root. Accordingly, \(\Lambda_{123}<1<\Lambda_{132}\), proving a growth-versus-decline reversal using only seasonal reordering. Here \(\Delta=-1/4\) and \(T_{123}-T_{132}=-1/3\), as required.

## Verification

Run `python3 leslie_symbolic.py` (requires SymPy) to verify the symbolic identity, determinant, and exact rational threshold values. Separately run `python3 leslie_fraction.py` (Python standard library only) to reproduce the example by direct rational matrix multiplication and test the identity and two-class reduction on 1,728 additional rational parameter triples. Both commands were executed successfully. The universal proof is the direct symbolic argument above; a finite parameter sample alone would not establish it.

## Relationship to prior work

Leslie (1945) introduced matrix descriptions of demographic stages and explicitly recognized changing projection matrices over time; the present stage matrices use that framework. Cushing and Ackleh (published online 2011) developed reproduction-number and invasion-threshold theory for periodic matrices, including detailed period-two Leslie calculations; they do not state the signed-area criterion for three fixed-fecundity stage matrices. Caswell and Shyu (2012), as reproduced and extended in Caswell's open chapter (2019), develop sensitivities of arbitrary periodic demographic products to stage-specific parameters. Their general framework can calculate growth numerically or by differentiation but does not state the complete two-orientation geometric classification or the open-interval viability classification and exact strict survival-versus-decline counterexample here.

The novelty claim is restricted to this complete three-phase ordering and viability result for the displayed stage matrix family. It is not a new general matrix theory or a new general criterion for Perron roots. A published result using different terminology or the general trace-commutator identity may imply portions of the theorem; remaining comparison risk is documented in the accompanying review.

## Limitations

The conclusion assumes two stages, constant adult fecundity, strictly positive vital rates and a repeated deterministic schedule. Collinear seasonal demographic pairs eliminate orientation differences in this particular family, not all possible transient or stage-distribution differences. The ordering theorem compares asymptotic linear rates only; it is not a prediction of real population viability without ecological calibration. The accessible literature does not rule out an earlier equivalent orientation identity under another description, and independent scientific audit has not been performed.

## References

- Leslie, P. H. (1945). “On the Use of Matrices in Certain Population Mathematics.” *Biometrika* 33(3), 183–212. DOI: 10.1093/biomet/33.3.183. First public record: 1945-11-01. Accessible scan: https://jxshix.people.wm.edu/2009-harbin-course/classic/leslie.pdf.
- Cushing, J. M. and Ackleh, A. S. (2012). “A net reproductive number for periodic matrix models.” *Journal of Biological Dynamics* 6(2), 166–188. DOI: 10.1080/17513758.2010.544410. Published online 2011-02-18.
- Caswell, H. and Shyu, E. (2012). “Sensitivity analysis of periodic matrix population models.” *Theoretical Population Biology* 82, 329–339. DOI: 10.1016/j.tpb.2012.03.008.
- Caswell, H. (2019). “Periodic Models.” *Sensitivity Analysis: Matrix Methods in Demography and Ecology*, chapter 8. DOI: 10.1007/978-3-030-10534-1_8. Open chapter: https://link.springer.com/chapter/10.1007/978-3-030-10534-1_8.
