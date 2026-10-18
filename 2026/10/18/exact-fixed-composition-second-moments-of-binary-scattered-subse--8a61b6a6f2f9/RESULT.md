# Exact fixed-composition second moments of binary scattered-subsequence diversity

## Finding

For a finite binary word \(w\), let \(D(w)\) count its **distinct scattered subsequences, including the empty word**. The empty word is counted once. For integers \(a,b\ge0\), define
\[
U_{a,b}=\sum_{\substack{w\in\{0,1\}^{a+b}\\|w|_0=a}}D(w),\qquad
V_{a,b}=\sum_{\substack{w\in\{0,1\}^{a+b}\\|w|_0=a}}D(w)^2.
\]
Put \(s=x+y\) and define the following polynomials:
\[
\begin{aligned}
Q&=(1-s)^2-xy,\\
K&=1-3s+3(x^2+y^2)+xy-x^3-y^3,\\
P&=1-s-x^2-y^2+x^3+y^3+5xy-2x^2y-2xy^2.
\end{aligned}
\]
Then the following two *formal bivariate power-series* identities hold:
\[
\boxed{\sum_{a,b\ge0}U_{a,b}x^ay^b
=\frac{(1-x)(1-y)}{(1-s)Q}},
\qquad
\boxed{\sum_{a,b\ge0}V_{a,b}x^ay^b
=\frac{(1-x)(1-y)P}{(1-s)QK}}.
\]
In particular, if \(X_{a,b}\) is uniformly random among the \(\binom{a+b}{a}\) words with \(a\) zeros and \(b\) ones, its variance is determined exactly by coefficient extraction:
\[
\boxed{\operatorname{Var}(D(X_{a,b}))
=\frac{[x^ay^b]\,\dfrac{(1-x)(1-y)P}{(1-s)QK}}{\binom{a+b}{a}}
-\left(\frac{[x^ay^b]\,\dfrac{(1-x)(1-y)}{(1-s)Q}}{\binom{a+b}{a}}\right)^2.}
\]
For independent uniform binary letters \(X_n\) of length \(n\), let
\(\lambda_{\pm}=(5\pm\sqrt{17})/4\). A closed specialization is
\[
\boxed{\operatorname{Var}(D(X_n))
=\left(2+\frac8{\sqrt{17}}\right)\lambda_+^n
+\left(2-\frac8{\sqrt{17}}\right)\lambda_-^n
-4\left(\frac94\right)^n}\qquad(n\ge0).
\]
The already-known mean is \(\mathbb E D(X_n)=2(3/2)^n-1\). Consequently,
\[
\operatorname{Var}(D(X_n))\sim
\left(2+\frac8{\sqrt{17}}\right)\lambda_+^n,
\quad
\frac{\operatorname{Var}(D(X_n))}{(\mathbb ED(X_n))^2}
\sim\frac{2+8/\sqrt{17}}4
\left(\frac{5+\sqrt{17}}9\right)^n.
\]
The second-moment identity and its fixed-composition implications are the subject of this finding; the mean formula is explicitly prior work.

## Assumptions and scope

A scattered subsequence preserves relative letter order but may omit arbitrarily many positions. All subsequences are counted as distinct **words**, not as different choices of embedding positions. The exact coefficient formulas hold for all nonnegative \(a,b\), including the empty word \((a,b)=(0,0)\) and constant words. For a fixed composition, the probability measure is uniform on words, not the independent Bernoulli measure; the latter is a separate specialization. All generating functions are identities in \(\mathbb Q[[x,y]]\) and therefore require no analytic convergence assumptions.

## Proof

**Distinct-subsequence states.** Let \(u(w)\) and \(v(w)\) be the numbers of distinct *nonempty* scattered subsequences ending in \(0\) and \(1\), respectively, so \(D(w)=1+u(w)+v(w)\). Appending \(0\) creates exactly one new ending-in-zero subsequence for each old subsequence including the empty one, and leaves ending-in-one subsequences unchanged. Appending \(1\) is symmetric. Thus the state column \((u,v,1)^T\), initialized at \(c=(0,0,1)^T\), evolves under
\[
M_0=\begin{pmatrix}1&1&1\\0&1&0\\0&0&1\end{pmatrix},\qquad
M_1=\begin{pmatrix}1&0&0\\1&1&1\\0&0&1\end{pmatrix}.
\]
Writing \(r=(1,1,1)\), the resulting count is \(D(w)=rM_w c\), where letters are applied in their chronological order, and the empty product is the identity.

**Weighted moment transfer.** Summing the states of all words, with weight \(x\) per \(0\) and \(y\) per \(1\), gives
\[
F_1=r\bigl(I-xM_0-yM_1\bigr)^{-1}c,
\quad
F_2=(r\otimes r)
\bigl(I-x(M_0\otimes M_0)-y(M_1\otimes M_1)\bigr)^{-1}(c\otimes c).
\]
Indeed each inverse is a formal geometric series enumerating all finite products; the tensor product converts \(D(w)^2\) into a single scalar matrix product.

**Finite polynomial certificate, including the nontrivial nine-dimensional identity.** Set \(t=1-x-y\), \(L=1-x\), \(R=1-y\), and \(H=tQK\). Direct multiplication gives
\[
(I-xM_0-yM_1)
\begin{pmatrix}xL\\yR\\Q\end{pmatrix}=tQ\,c,
\qquad
r\begin{pmatrix}xL\\yR\\Q\end{pmatrix}=LR.
\]
For the square moment, define \(C=2xyLR(2-x-y)\) and the nine-entry column
\[
h=\begin{pmatrix}
xLP\\ C\\xLK\\C\\yRP\\yRK\\xLK\\yRK\\QK
\end{pmatrix}.
\]
In the standard row-major tensor basis, direct polynomial multiplication verifies the *exact* identities
\[
\bigl(I-x(M_0\otimes M_0)-y(M_1\otimes M_1)\bigr)h
=H(c\otimes c),\qquad(r\otimes r)h=LRP.
\]
All identities in this paragraph are polynomial equalities in \(\mathbb Z[x,y]\); a self-contained exact-arithmetic checker for these displayed certificates is provided in `verify.py`. Since \(t,Q,K\) have constant term \(1\), division is valid in the formal power-series ring. The displayed generating functions follow **for all compositions**, with no finite-length inference.

**Uniform independent specialization.** Substituting \(x=y=z/2\) into \(F_1,F_2\) weights each length-\(n\) word by \(2^{-n}\). The first-moment series gives \(\mathbb ED(X_n)=2(3/2)^n-1\). The second-moment series reduces by partial fractions to
\[
\mathbb E[D(X_n)^2]=
\left(2+\frac8{\sqrt{17}}\right)\lambda_+^n
+\left(2-\frac8{\sqrt{17}}\right)\lambda_-^n
-4\left(\frac32\right)^n+1.
\]
Subtracting \((2(3/2)^n-1)^2\) gives the boxed variance formula. Finally \(\lambda_-<\lambda_+\) and \(\lambda_+>9/4\) because \(\sqrt{17}>4\). Hence the asymptotic statements, including divergence of the squared coefficient of variation.

## Verification

Run `python3 verify.py` with the Python 3 standard library. It checks the *symbolic polynomial transfer certificates* exactly, rather than merely testing finitely many coefficients. Separately it checks the rational generating-function coefficients against every binary word up to length \(11\), validates a genuinely independent explicit set-of-subsequences construction through length \(9\), and checks the independent-letter specializations through length \(31\) using rational arithmetic. The expected final lines begin with `VERIFY_OK` and `SYMBOLIC_OK`. The polynomial certificates together with the state recurrence constitute a complete proof; finite enumeration is corroborative only.

## Relationship to prior work

Flaxman, Harrow, and Sorkin (2004) study extremal distinct-subsequence counts and comparisons with random words. Collins (2013) establishes the uniform binary random-word **mean** and fixed-length mean estimates. Biers-Ariel, Godbole, and Kelley (2018; preprint 2017) extend first-moment results to biased binary and other sources. None of those inspected works states the present fixed-composition **second-moment** bivariate function or the uniform-source variance specialization. The transfer-matrix technique is elementary standard methodology, not claimed as invented here. The present claim concerns the evaluated two-variable second moment and its fluctuations, rather than an algorithm to count subsequences in an individual word.

## Limitations

The proof concerns the binary alphabet, exact total diversity over *all* scattered subsequence lengths, and either uniformly fixed compositions or iid uniform binary words. It does not provide a local limit theorem, a full distribution, sharp tail probabilities, multivariate covariance of counts at individual lengths, or a nonuniform Markov-source variance. It does not assert novelty of the deterministic subsequence-count recurrence or of known expectation formulas. As for any literature comparison, an equivalent result in incompletely indexed publications may exist; neither a failed database search nor the finite computation alone establishes novelty.

## References

1. A. Flaxman, A. W. Harrow and G. B. Sorkin, *Strings with Maximally Many Distinct Subsequences and Substrings*, Electronic Journal of Combinatorics 11 (2004), R8, DOI: 10.37236/1761. Published January 5, 2004. https://doi.org/10.37236/1761
2. M. J. Collins, *The Number of Distinct Subsequences of a Random Binary String*, arXiv:1310.7288, first posted October 28, 2013. https://arxiv.org/abs/1310.7288
3. Y. Biers-Ariel, A. Godbole and E. Kelley, *Expected Number of Distinct Subsequences in Randomly Generated Binary Strings*, DMTCS 19(2) (2018), paper 10, DOI: 10.23638/DMTCS-19-2-10 (first preprint 2017). https://doi.org/10.23638/DMTCS-19-2-10
