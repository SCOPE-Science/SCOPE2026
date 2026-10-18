# Three-household Gini-order rigidity and a sharp four-household reversal under common concave income transformations

## Finding

Let \(n\ge 1\) and let \(x=(x_1,\ldots,x_n)\) and \(y=(y_1,\ldots,y_n)\) be positive, equally weighted income profiles, each listed in nondecreasing order. Assume that they have the same total income and that \(x\) majorizes \(y\), meaning
\[
\sum_{i=1}^n x_i=\sum_{i=1}^n y_i,\qquad
\sum_{i=1}^k x_i\le\sum_{i=1}^k y_i\quad(1\le k<n).
\]
Let \(f:(0,\infty)\to(0,\infty)\) be any nondecreasing concave function, applied identically to both profiles, and define the ordinary relative Gini coefficient
\[
G(z)=\frac{\sum_{1\le i<j\le n}|z_i-z_j|}{n\sum_{i=1}^n z_i}.
\]
For \(n\le3\), the Gini ranking is preserved under every such transformation:
\[
G(f(x_1),\ldots,f(x_n))\ge G(f(y_1),\ldots,f(y_n)).
\]
The household bound is sharp, even if \(f\) is required to be smooth, strictly increasing and strictly concave. At \(n=4\), take
\[
x=(1,1,1,3),\qquad y=(1,1,2,2).
\]
Then \(x\) majorizes \(y\) and \(G(x)=1/4>1/6=G(y)\), whereas for the common top-code \(f(t)=\min\{t,2\}\),
\[
G(f(x))=3/20<1/6=G(f(y)).
\]
The strict reversal persists for the positive, smooth, strictly increasing and strictly concave function \(f(t)=1-8^{-t}\):
\[
G(f(x))=27/1060<1/34=G(f(y)).
\]

## Assumptions and scope

All profiles have equal size, equal household weights, positive incomes and equal *original* totals. The transformation is common to both populations, nondecreasing and concave, and its values are strictly positive. The transformed totals need not coincide. The partial-sum assumption is exactly the finite Lorenz/majorization order; merely having \(G(x)\ge G(y)\) does not suffice for the universal assertion. Ties are allowed. For \(n=1\) both Gini coefficients are zero. A top-code is a concave nondecreasing map that need not be strictly increasing, whereas the smooth example handles strictness without any limiting argument.

## Proof

For a positive vector \(z\) in nondecreasing order write \(S(z)=\sum_i z_i\) and \(N(z)=\sum_{i<j}(z_j-z_i)\). Its relative Gini coefficient is \(G(z)=N(z)/(nS(z))\). Because \(f\) is nondecreasing, transformed entries remain ordered, and because \(x\) majorizes \(y\), its smallest and largest entries obey
\[
x_1\le y_1,\qquad x_n\ge y_n.
\]
Applying the same nondecreasing \(f\) gives
\[
f(x_n)-f(x_1)\ge f(y_n)-f(y_1)\ge0.
\]
The concave form of the finite Hardy--Littlewood--Pólya/Karamata inequality, under the stated equal-total majorization hypothesis, gives
\[
S(f(x))=\sum_i f(x_i)\le\sum_i f(y_i)=S(f(y)).
\]
Both transformed sums are strictly positive. For \(n=2\), \(N(f(z))=f(z_2)-f(z_1)\). For \(n=3\), direct cancellation gives
\[
N(f(z))=\big(f(z_2)-f(z_1)\big)+\big(f(z_3)-f(z_1)\big)+\big(f(z_3)-f(z_2)\big)=2\big(f(z_3)-f(z_1)\big).
\]
Thus for \(n=2,3\) the numerator of \(G(f(x))\) is no smaller than that of \(G(f(y))\), while its positive denominator is no larger. Their ratio ordering follows. The \(n=1\) case is immediate.

For sharpness at \(n=4\), the increasing partial sums of \(x\) are \((1,2,3,6)\) and of \(y\) are \((1,2,4,6)\), so \(x\) majorizes \(y\). Direct application of the pairwise-difference definition gives
\[
G(x)=\frac{6}{4\cdot6}=\frac14,\qquad
G(y)=\frac{4}{4\cdot6}=\frac16.
\]
Under \(f(t)=\min\{t,2\}\), the images are \((1,1,1,2)\) and \((1,1,2,2)\), with totals \(5\) and \(6\), and pairwise-difference sums \(3\) and \(4\). Thus \(3/20<1/6\), with difference \(-1/60\).

For the strictly concave version set \(f(t)=1-8^{-t}\) for all \(t>0\). Then \(f(t)>0\), its derivative is \((\log8)8^{-t}>0\), and its second derivative is \(- (\log8)^2 8^{-t}<0\). Exactly,
\[
f(1)=7/8,\quad f(2)=63/64,\quad f(3)=511/512.
\]
Consequently \(G(f(x))=27/1060\), \(G(f(y))=1/34\), and their difference is \(-71/18020<0\). This proves strict robustness and sharpness.

## Verification

A standalone dependency-free script, `verify_gini.py`, independently evaluates the relative Gini by both the pairwise-difference and ordered-weight formulas using exact rational arithmetic. It checks both original and transformed four-household inequalities and the exact strict-concavity witness. It also tests the stated lower-dimensional comparison for 1,685 transformations of small integer majorization pairs and cross-checks the two Gini formulas on 329 positive integer profiles. Run `python3 verify_gini.py`; the resulting output includes `VERIFY_OK majorization=PASS` and exact reported fractions. These finite checks confirm the arithmetic; the universal \(n\le3\) statement rests on the proof above rather than the finite enumeration.

## Relationship to prior work

Fellman (2016), Theorems 1--4, studies transformations that Lorenz-improve a *given* distribution and compares *two transformations of the same* distribution. Those results motivate the question but do not assert that applying a *single common* concave transformation preserves the Gini ordering of *two distinct* Lorenz-ordered finite populations, or establish a minimal household count for failure. Bishop--Chiou--Formby (1994) documents empirical ordinal income-inequality effects of top-coding; Larrimore--Burkhauser--Feng--Zayatz (2008) studies top-code corrections for survey income inequality. Neither is cited as establishing the sharp three/four-household theorem. The endpoint calculation and finite concave majorization inequality used in the proof are standard; only the combined sharp comparison claim is assessed here.

## Limitations

This is a finite equally weighted mathematical comparison, not an estimate for real survey data. It does not extend the three-household guarantee to arbitrary income pairs lacking majorization, unequal household weights, negative or zero outputs of the transformation, or four-or-more household profiles. Its sharpness witness establishes existence, not prevalence or a maximal reversal size. A relevant 1994 article's full text could not be examined, so full prior-art exclusion is not claimed. No independent scientific audit has been performed.

## References

- Johan Fellman (2016), *Transformations and Lorenz Curves: Sufficient and Necessary Conditions*, Theoretical Economics Letters 6, 442--449. First published 2016-06-06. DOI: 10.4236/tel.2016.63050; https://www.scirp.org/pdf/tel_2016060615565238.pdf.
- John A. Bishop, Jong-Rong Chiou and John P. Formby (1994), *Truncation Bias and the Ordinal Evaluation of Income Inequality*, Journal of Business & Economic Statistics 12(1), 123--127. DOI: 10.1080/07350015.1994.10509995. Abstract inspected; full text unavailable.
- Jeff Larrimore, Richard V. Burkhauser, Shuaizhang Feng and Laura Zayatz (2008), *Consistent Cell Means for Topcoded Incomes in the Public Use March CPS (1976--2007)*, U.S. Census CES Working Paper 08-06. https://www2.census.gov/ces/wp/2008/CES-WP-08-06.pdf.
- The finite Hardy--Littlewood--Pólya majorization theorem and Karamata's inequality (standard facts invoked only in the indicated finite form).
