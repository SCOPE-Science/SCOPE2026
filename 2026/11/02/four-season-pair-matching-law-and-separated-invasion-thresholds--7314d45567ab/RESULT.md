# Four-season pair-matching law and separated invasion thresholds for bidirectional vector–host transmission

## Finding

Let
\[
M_i(t)=\begin{pmatrix}s&t b_i\\t c_i&s\end{pmatrix},\qquad 0<s<1,\quad b_i,c_i>0,\quad t>0,
\]
for four labeled seasons \(i=1,2,3,4\). The two components represent infected host and vector classes at a disease-free linearization; \(s\) is a common within-season retention fraction, and \(t b_i,t c_i\) are nonnegative expected cross-type infection coefficients. Let \(P_\pi(t)=M_{\pi_1}(t)\cdots M_{\pi_4}(t)\). The rightmost factor acts first; reversing the written order gives chronological order. Write \(R_\pi(t)=\rho(P_\pi(t))\).

Assume the four directed-transmission ratios \(r_i=b_i/c_i\) are distinct, with labels chosen so
\[
0<r_1<r_2<r_3<r_4.
\]
Then the 24 seasonal schedules have exactly three strictly ordered invasion multipliers, with eight schedules in each class. Their multipliers increase strictly in the order of the alternating-position pair sums
\[
\boxed{r_1r_4+r_2r_3<r_1r_3+r_2r_4<r_1r_2+r_3r_4.}
\]
The pairing associated with a schedule \(\pi\) is \(\{\pi_1,\pi_3\}\mid\{\pi_2,\pi_4\}\). The determinant is invariant under schedule permutation, so the stated strict ordering holds for every \(t>0\).

Moreover, each of the three strictly ordered invasion-multiplier classes has a **unique positive contact-intensity threshold** at which its multiplier equals one. If \(t_{\rm high},t_{\rm mid},t_{\rm low}\) denote the respective crossing intensities, then
\[
\boxed{0<t_{\rm high}<t_{\rm mid}<t_{\rm low}<\infty.}
\]
Consequently, every four-season parameter family satisfying the hypotheses has nonempty intensity intervals in which *permuting the same four seasonal transmission matrices changes the invasion verdict* \(R_\pi(t)>1\) versus \(R_\pi(t)<1\). No one-, two-, or three-season permutation is order-sensitive under equal retention, so four is the sharp minimal horizon in this family.

## Assumptions and scope

This is a finite-dimensional discrete-time *local invasion* theorem, not a nonlinear endemicity or stochastic outbreak theorem. The same nonnegative matrix list is repeated each period; the two infected classes have season-invariant, **equal** retention fractions \(s\), while both transfer directions may vary independently. The off-diagonal quantities are mean secondary-infection coefficients, not probabilities constrained to one. Every claim applies to every \(s\in(0,1)\) and strictly positive \(b_i,c_i\) with four distinct ratios, and every positive multiplier \(t\). Schedules differing by cyclic shift or reversal can have equal multipliers; the theorem enumerates all 24 labeled permutations and does not treat calendar dates or empirical season lengths.

## Proof

Put \(X_i=\bigl(\begin{smallmatrix}0&b_i\\c_i&0\end{smallmatrix}\bigr)\), so \(M_i(t)=sI+tX_i\). Any odd product of the \(X_i\)'s is off diagonal, with zero trace, and a product of two has trace \(b_ic_j+c_ib_j\). A product of four has trace \(b_{\pi_1}c_{\pi_2}b_{\pi_3}c_{\pi_4}+c_{\pi_1}b_{\pi_2}c_{\pi_3}b_{\pi_4}\). Expanding the exact trace yields
\[
\operatorname{tr}P_\pi(t)
=2s^4+s^2t^2\sum_{i<j}(b_ic_j+c_ib_j)
+t^4\left(\prod_{i=1}^4c_i\right)
\bigl(r_{\pi_1}r_{\pi_3}+r_{\pi_2}r_{\pi_4}\bigr).
\]
The first two terms are independent of \(\pi\). There are exactly three partitions of four labels into two unordered pairs, and exactly eight of the 24 orders realize each alternating-position partition. Their last terms satisfy
\[
(r_1r_2+r_3r_4)-(r_1r_3+r_2r_4)
=(r_3-r_2)(r_4-r_1)>0,
\]
\[
(r_1r_3+r_2r_4)-(r_1r_4+r_2r_3)
=(r_2-r_1)(r_4-r_3)>0.
\]
The determinant is exactly
\[
\det P_\pi(t)=\prod_{i=1}^4(s^2-t^2b_ic_i),
\]
which is also independent of \(\pi\). Each product is strictly positive entrywise. For two positive \(2\times2\) matrices with the same determinant and differing traces, the Perron root strictly increases with trace: its other eigenvalue is strictly smaller and the characteristic equation gives \(\partial\rho/\partial T=\rho/(\rho-\lambda_2)>0\). This proves the three strict classes for all \(t>0\), even when one or more individual seasonal determinants vanish or become negative.

For every fixed season, each entry of \(M_i(t)\) is nondecreasing in \(t\), and both off-diagonal entries strictly increase. Hence every entry of \(P_\pi(t)\) strictly increases for \(t>0\). Perron monotonicity implies \(R_\pi(t)\) is continuous and strictly increasing on \(t>0\). At \(t\downarrow0\), \(P_\pi(t)\to s^4 I\), so \(R_\pi(t)\to s^4<1\). At \(t\to\infty\), \(t^{-4}P_\pi(t)\to X_{\pi_1}X_{\pi_2}X_{\pi_3}X_{\pi_4}\), a positive diagonal matrix, giving \(R_\pi(t)\to\infty\). Each class therefore crosses one exactly once. Because high, middle and low classes have strict pointwise order at every \(t>0\), their three threshold intensities satisfy the strict reverse order. The open intervals between consecutive thresholds contain opposite invasion verdicts.

For \(k\le3\) factors, all terms in \(\operatorname{tr}\prod_{i=1}^k(sI+tX_{\pi_i})\) are independent of ordering: traces of odd products of the \(X_i\)'s vanish and only unordered pairs can contribute. The determinant is a product of the same individual determinants. Therefore all permutations for \(k\le3\) have the same characteristic polynomial and Perron multiplier. This establishes sharpness of the four-season minimum.

A fully exact example with both transmission directions varying uses \(s=1/2\) and
\[
(b_i,c_i)\in
\left\{\left(\frac{23}{128},\frac{23}{128}\right),
\left(\frac{23}{48},\frac{23}{96}\right),
\left(\frac{69}{64},\frac{23}{64}\right),
\left(\frac{23}{12},\frac{23}{48}\right)\right\}.
\]
At \(t=1\), the three traces, from lowest to highest, are
\[
\frac{18587429}{18874368},\quad
\frac{37454699}{37748736},\quad
\frac{19147111}{18874368}.
\]
The common determinant is \(160560615985/59373627899904\). Accordingly the three values of \(\det(I-P_\pi)\), from lowest-trace to highest-trace class, are exactly
\[
\frac{1063192662577}{59373627899904},\quad
\frac{623040827953}{59373627899904},\quad
-\frac{697414675919}{59373627899904}.
\]
The determinant lies strictly between zero and one; since the products are positive, their non-Perron eigenvalues are strictly below one. Thus the highest-trace class is supercritical while both other classes are subcritical for this one fixed collection of four transmission pairs.

## Verification

A standalone Python 3 standard-library script `check.py` uses exact rational matrices to check the four-factor trace identity on random rational data and all 24 permutations; checks the one-, two-, and three-factor order invariances; and reproduces the exact threshold-reversal example with rational determinants. Execute `python3 check.py`. The script is corroborative, not a substitute for the algebraic proof for arbitrary positive real parameters.

## Relationship to prior work

Periodic disease growth criteria based on products of positive matrices are classical. Bacaër (2009) gives a broad periodic population-matrix framework; Chitnis, Hardy and Smith (2012) give a periodically forced discrete-time mosquito feeding-cycle model and a periodic-matrix stability criterion; Gao, Lou and Ruan (2014) analyze periodic Ross–Macdonald threshold dynamics. The current theorem is about a distinct, explicitly specified two-type **discrete-time** matrix family rather than a claim for those authors' exact systems.

Four-season pairing comparisons have previously been obtained in the one-varying-direction infected-class special case and in a structurally different two-patch dispersal model; these are not claimed as new here. The added claim is the complete two-direction varying-ratio comparison *together with an all-parameter, strictly separated three-threshold invasion law*. The classical trace and Perron identities are acknowledged as prior mathematics. Historical priority against unavailable general matrix-rearrangement theorems remains provisional.

## Limitations

Equal diagonal retention within and across seasons is essential to the one-to-three-season insensitivity statement; the theorem does not assert analogous cutoffs for unequal retention, nonlinear vector demography, continuous-time season propagators, sampling noise or fluctuating susceptible populations. The threshold separation relies on multiplying *both* transmission directions by the same positive contact intensity. The exact examples are mathematical benchmarks, not calibrated epidemiological forecasts. A sufficiently broad earlier positive-matrix ordering result may encompass these formulas and has not been ruled out independently.

## References

1. N. Bacaër, “Periodic Matrix Population Models: Growth Rate, Basic Reproduction Number, and Entropy,” *Bulletin of Mathematical Biology* 71 (2009), 1781–1792, https://doi.org/10.1007/s11538-009-9426-6, first published 2009-05-02.
2. N. Chitnis, D. Hardy, and T. Smith, “A Periodically-Forced Mathematical Model for the Seasonal Dynamics of Malaria in Mosquitoes,” *Bulletin of Mathematical Biology* 74 (2012), 1098–1124, https://doi.org/10.1007/s11538-011-9710-0, first published 2012-01-05.
3. D. Gao, Y. Lou, and S. Ruan, “A Periodic Ross-Macdonald Model in a Patchy Environment,” *Discrete and Continuous Dynamical Systems B* 19 (2014), 3133–3145, https://doi.org/10.3934/dcdsb.2014.19.3133, published online October 2014.
4. J. Li, “Simple discrete-time malarial models,” *Journal of Difference Equations and Applications* 19 (2013), 649–666, https://doi.org/10.1080/10236198.2012.672566, first published online 2012-04-24.
