# Seven points maximize the positivity defect of quadratic Savitzky–Golay smoothing
## Finding
Fix an integer \(m\ge1\). On the equispaced window \(-m,-m+1,\ldots,m\), fit a polynomial of degree at most two by ordinary unweighted least squares and take its fitted value at the center. By symmetry the degree-three Savitzky--Golay center smoother has exactly the same weights. Write the resulting linear smoother as
\[
\widehat y_0=\sum_{j=-m}^{m}w_{m,j}y_j.
\]
Then
\[
w_{m,j}=
\frac{3\bigl(3m^2+3m-1-5j^2\bigr)}
{(2m+1)(4m^2+4m-3)}.
\]

For bounded nonnegative data
\[
0\le y_j\le M,
\qquad M>0,
\]
the exact worst possible negative center value is
\[
\min \widehat y_0=-M V_m,
\]
where, with
\[
k_m=\left\lfloor\sqrt{\frac{3m^2+3m-1}{5}}\right\rfloor,
\]
one has
\[
V_m=
\frac{(m-k_m)\bigl(10k_m^2+10k_mm+15k_m-8m^2-3m+11\bigr)}
{(2m+1)(4m^2+4m-3)}.
\]
Equivalently,
\[
V_m=
\frac{6}{(2m+1)(4m^2+4m-3)}
\sum_{j=k_m+1}^{m}
\bigl(5j^2-(3m^2+3m-1)\bigr).
\]

The sharp defect is globally largest at the seven-point window \(m=3\):
\[
V_m\le V_3=\frac4{21}
\qquad(m\ge1),
\]
with equality only at \(m=3\). Thus the familiar seven-point quadratic/cubic center smoother
\[
\frac1{21}(-2,3,6,7,6,3,-2)
\]
can return a value as low as \(-4M/21\) from data lying entirely in \([0,M]\).

The defect does not disappear for long windows. In fact,
\[
\lim_{m\to\infty}V_m
=
\frac32\sqrt{\frac35}-1
=0.1618950038\ldots.
\]
Since the weights sum to one, the corresponding \(\ell_\infty\)-to-center amplification, or equivalently the \(\ell_1\) norm of the smoothing kernel, is
\[
\sum_{j=-m}^{m}|w_{m,j}|=1+2V_m,
\]
and therefore tends to
\[
3\sqrt{\frac35}-1
=1.3237900077\ldots.
\]

A strictly positive witness already exists at the global maximizer. For the seven-point rule, take
\[
y_{-3}=y_3=M,
\qquad
y_j=\frac{2M}{25}\quad(|j|\le2).
\]
Every datum lies in \([2M/25,M]\), yet
\[
\widehat y_0=-\frac{2M}{21}<0.
\]

## Assumptions and scope
The statement concerns the classical unweighted Savitzky--Golay center smoother obtained by least-squares fitting on an odd, symmetric, equally spaced window. It covers degree two and, at the center, degree three because odd powers are orthogonal to the constant term on a symmetric window.

The result is an exact finite-window statement in real arithmetic. It does not claim that every Savitzky--Golay implementation uses these boundary-free center coefficients, nor does it analyze endpoint handling, weighted least squares, irregular grids, derivative filters, or nonlinear postprocessing.

The phrase positivity defect means the sharp minimum of the linear center estimate over the data cube \([0,M]^{2m+1}\). It is not a statement about whether an underlying smooth positive function remains positive between samples.

## Proof
Let
\[
S_0=2m+1,
\qquad
S_2=\sum_{j=-m}^{m}j^2=\frac{m(m+1)(2m+1)}3,
\]
and
\[
S_4=\sum_{j=-m}^{m}j^4
=\frac{m(m+1)(2m+1)(3m^2+3m-1)}{15}.
\]
For the quadratic fit \(a+bj+cj^2\), symmetry decouples \(b\), while \((a,c)\) solve
\[
\begin{pmatrix}S_0&S_2\\S_2&S_4\end{pmatrix}
\begin{pmatrix}a\\c\end{pmatrix}
=
\begin{pmatrix}\sum y_j\\\sum j^2y_j\end{pmatrix}.
\]
Solving for \(a\) gives the stated weight formula
\[
w_{m,j}=
\frac{S_4-S_2j^2}{S_0S_4-S_2^2}
=
\frac{3(3m^2+3m-1-5j^2)}{(2m+1)(4m^2+4m-3)}.
\]
The same center weights apply to a cubic fit because the odd columns are orthogonal to the even columns.

Put
\[
A_m=3m^2+3m-1,
\qquad
D_m=(2m+1)(4m^2+4m-3).
\]
Then \(w_{m,j}<0\) exactly when \(5j^2>A_m\), namely when \(|j|>k_m\). Since \(\widehat y_0\) is linear in the independent box variables \(0\le y_j\le M\), its minimum is obtained by taking \(y_j=M\) at every negative coefficient and \(y_j=0\) at every nonnegative coefficient. Hence
\[
V_m=-\sum_{w_{m,j}<0}w_{m,j}
=
\frac{6}{D_m}
\sum_{j=k_m+1}^{m}(5j^2-A_m).
\]
Using the formula for a sum of squares gives the displayed closed form for \(V_m\).

Direct exact evaluation gives
\[
V_1=0,
\qquad
V_2=\frac6{35},
\qquad
V_3=\frac4{21}.
\]
The accompanying exact-rational verification checks
\[
V_m<\frac4{21}
\qquad(4\le m\le27).
\]
It remains to prove the tail uniformly.

Set
\[
a_m=\sqrt{\frac{A_m}{5}},
\qquad
\alpha_m=\frac{a_m}{m+1},
\qquad
F_m=\frac{(m+1)^3}{D_m},
\]
and
\[
g(\alpha)=\frac13-\alpha^2+\frac23\alpha^3.
\]
Because \(x^2-a_m^2\) is increasing for \(x\ge a_m\),
\[
\sum_{j=k_m+1}^{m}(j^2-a_m^2)
<
\int_{a_m}^{m+1}(x^2-a_m^2)\,dx.
\]
Therefore
\[
V_m<30F_mg(\alpha_m).
\]
Moreover,
\[
\alpha_m^2=
\frac{3m^2+3m-1}{5(m+1)^2}
\]
is strictly increasing because
\[
\alpha_{m+1}^2-\alpha_m^2
=
\frac{3m^2+11m+9}{5(m+1)^2(m+2)^2}>0.
\]
On \((0,1)\),
\[
g'(\alpha)=2\alpha(\alpha-1)<0.
\]
Also
\[
F_{m+1}-F_m
=
-\frac{3m^2+13m+13}
{(2m-1)(2m+1)(2m+3)(2m+5)}<0.
\]
Thus for every \(m\ge28\),
\[
V_m<30F_{28}g(\alpha_{28}).
\]
Here
\[
\alpha_{28}=\frac{\sqrt{487}}{29},
\qquad
F_{28}=\frac{24389}{184965}.
\]
A direct simplification gives
\[
\frac4{21}-30F_{28}g(\alpha_{28})
=
\frac{100348}{86317}
-
\frac{1948\sqrt{487}}{36993}.
\]
This is positive because it is equivalent to
\[
\sqrt{487}<\frac{75261}{3409},
\]
and
\[
\left(\frac{75261}{3409}\right)^2-487
=
\frac{4654274}{11621281}>0.
\]
Hence \(m=3\) is the unique global maximizer.

Finally, since \(k_m/m\to\sqrt{3/5}\), divide the exact sum by \(m^3\) and use the elementary Riemann-sum limit to obtain
\[
V_m\to
\frac{3}{2}\sqrt{\frac35}-1.
\]
The kernel \(\ell_1\) identity follows from \(\sum_jw_{m,j}=1\): the total positive mass is \(1+V_m\) and the total negative mass is \(-V_m\).

For the strictly positive seven-point witness, the two edge weights total \(-4/21\), while the five nonnegative weights total \(25/21\). Therefore
\[
\widehat y_0
=M\left(-\frac4{21}+\frac2{25}\frac{25}{21}\right)
=-\frac{2M}{21}.
\]

## Verification
The accompanying `verify.py` uses exact rational arithmetic. It reconstructs the least-squares center weights from the closed form, checks reproduction of constants, linear functions, and quadratics, verifies the original five- and seven-point coefficient tables, and confirms that the cube minimum equals the total negative coefficient mass.

It evaluates \(V_m\) exactly for \(1\le m\le27\), confirms that \(m=3\) uniquely maximizes that finite range, and checks the exact rational identities used in the uniform \(m\ge28\) tail proof, including the square comparison that removes the remaining radical. It also checks the strictly positive seven-point witness exactly.

The all-window maximum and asymptotic limit are proved analytically above; finite computation is supplementary.

## Relationship to prior work
Savitzky and Golay introduced least-squares polynomial smoothing by fixed convolution coefficients and tabulated the quadratic/cubic center coefficients for windows from five through twenty-five points. In particular, their table contains the five-point rule proportional to \((-3,12,17,12,-3)\) and the seven-point rule proportional to \((-2,3,6,7,6,3,-2)\). Those coefficients and the least-squares construction are prior work.

Marchand and Marmet later emphasized pitfalls of least-squares polynomial smoothing, including transmission zeros, phase reversals, and overshoots for long sequences. More recent analysis likewise highlights negative excursions and ringing in Savitzky--Golay kernels. Thus the qualitative fact that these smoothers can create artifacts or use negative coefficients is not claimed here.

The present result isolates a different exact robustness invariant: the worst center undershoot over all bounded nonnegative data, for every odd quadratic/cubic window. It supplies a closed formula, proves that the seven-point window is the unique global worst case, and identifies the nonzero infinite-window defect. Targeted literature searches under positivity preservation, negative coefficient mass, kernel \(\ell_1\) norm, overshoot, and least-squares smoothing did not locate this all-window sharp statement.

## Limitations
The proof treats only the center value of the classical symmetric unweighted degree-two/degree-three Savitzky--Golay smoother. Higher polynomial degrees have different sign patterns, and endpoint formulas are not covered.

The negative-mass functional is a worst-case box-data criterion. It does not quantify typical noise reduction, frequency response, or mean-square error for a stochastic signal model.

The most directly relevant 1983 paper on pitfalls of least-squares polynomial smoothing was available through its abstract and bibliographic record, but a verified full-text copy was not recovered through the lawful open and institutional routes attempted. Consequently, an equivalent negative-mass calculation hidden in that paper cannot be excluded. Older signal-processing literature may also phrase the same quantity as an \(\ell_1\) kernel norm or deterministic gain; this remains a residual originality risk.

## References
1. Abraham Savitzky and Marcel J. E. Golay, *Smoothing and Differentiation of Data by Simplified Least Squares Procedures*, Analytical Chemistry 36 (1964), 1627--1639, DOI: 10.1021/ac60214a047.
2. Patrick Marchand and Louis Marmet, *Binomial smoothing filter: A way to avoid some pitfalls of least-squares polynomial smoothing*, Review of Scientific Instruments 54 (1983), 1034--1041, DOI: 10.1063/1.1137498.
3. David W. Scott and Wade R. Scott, *Efficient Methods for Data Smoothing*, SIAM Journal on Numerical Analysis 26 (1989), 681--692, DOI: 10.1137/0726040.
4. Manfred Schmid, David Rath, and Ulrich Diebold, *Why and How Savitzky--Golay Filters Should Be Replaced*, ACS Measurement Science Au 2 (2022), 185--196, DOI: 10.1021/acsmeasuresciau.1c00054.
