# A parity-sawtooth law for conditional Wilcoxon variance under fixed-composition runs

## Finding

Let a binary word be uniformly chosen among all words containing exactly \(a\geq1\) ones and \(b\geq1\) zeros. Let \(R\) count its maximal nonempty constant-symbol runs and let \(U\) count pairs of positions \(i<j\) with a one at \(i\) and a zero at \(j\). Thus \(U\) is one orientation of the two-sample Mann–Whitney statistic, and \(U-ab/2\) is the centered Wilcoxon rank statistic, up to sign. Set \(V_k=\operatorname{Var}(U\mid R=k)\) for every feasible \(k\).

The conditional mean is independent of the run count:
\[
\mathbb E[U\mid R=k]=ab/2.
\]
For every feasible even count \(k=2r\), where \(1\leq r\leq\min(a,b)\),
\[
V_{2r}=\frac{ab\bigl[2abr+4ab-(a+b)(r^2+r-2)+r^2-r\bigr]}{12r(r+1)}.
\]
For every feasible odd count \(k=2r+1\), where \(r\geq1\), \(r\leq\min(a,b)\), and \(r<\max(a,b)\), define
\[
W(a,b;r)=\frac{ab\bigl[2ab-(a+b)r+a-3b+r-1\bigr]}{12(r+1)}.
\]
Then
\[
V_{2r+1}=\frac{(a-r)W(a,b;r)+(b-r)W(b,a;r)}{a+b-2r}.
\]
These formulas have three universal strict ordering properties whenever the named run counts are feasible:
\[
\begin{aligned}
V_{2r}&>V_{2r+2},\\
V_{2r+1}&>V_{2r+3},\\
V_{2r}&>V_{2r+1}<V_{2r+2}.
\end{aligned}
\]
In particular, the conditional variance decreases separately along both parity subsequences, yet **every feasible odd count with both neighboring even counts is a strict local minimum**. The dependence is not a globally decreasing variance curve. For instance, when \(a=b=3\), the conditional variances at run counts \(2,3,4,5,6\) are respectively \(81/4,9/4,25/4,1/4,9/4\).

## Assumptions and scope

All words are equally likely, and only the fixed counts \(a,b\) are conditioned upon. The exact feasible run counts are \(2,3,\ldots,2\min(a,b)\) and additionally \(2\min(a,b)+1\) when \(a\ne b\). An inequality is asserted only if both sides are defined. Thus the assertions include \(a=1\) or \(b=1\), and have no unmentioned asymptotic or symmetry restriction. The uncentered and centered versions of \(U\) have the same conditional variance.

## Proof

**1. Conditioning on run lengths.** A uniform ordered positive composition \(X=(X_1,\ldots,X_p)\) of \(a\) has
\[
\mathbb E X=(a/p)\mathbf 1,\qquad
\operatorname{Cov}(X)=\alpha(pI_p-J_p),\qquad
\alpha=\frac{a(a-p)}{p^2(p+1)}.
\]
The covariance follows by writing \(X_i=1+Y_i\), where the weak composition \(Y\) of \(a-p\) is uniform; stars and bars gives \(\operatorname{Var}(X_i)=a(a-p)(p-1)/[p^2(p+1)]\) and the fixed-sum constraint gives the off-diagonal covariances. These formulas also cover \(p=1\) and \(p=a\). Conditional on a prescribed pattern of alternating one-runs and zero-runs, the positive compositions of the two colors are independent and uniform. The zero-run lengths \(Y\) obey the analogous formula \(\operatorname{Cov}(Y)=\beta(qI_q-J_q)\), with \(\beta=b(b-q)/[q^2(q+1)]\).

Let \(M\) be the \(p\times q\) indicator matrix for which one-run precedes which zero-run, so \(U=X^\mathsf TMY\). Put \(t=\mathbf1^\mathsf TM\mathbf1\), \(h=\|M\mathbf1\|^2\), and \(j=\|M^\mathsf T\mathbf1\|^2\). Independent centered expansion, using the fact that \(M\) is zero-one, yields
\[
\operatorname{Var}(U\mid\text{run pattern})
=\left(\frac bq\right)^2\alpha(ph-t^2)
+\left(\frac ap\right)^2\beta(qj-t^2)
+\alpha\beta(pqt-ph-qj+t^2).
\tag{1}
\]
Here the last term is the trace \(\operatorname{tr}[\operatorname{Cov}(X)M\operatorname{Cov}(Y)M^\mathsf T]\). No independence of individual run lengths is assumed.

**2. Even and odd formulas.** A word with \(2r\) runs has \(p=q=r\), with equally likely start/end orientations. For the orientation beginning with a one-run and ending with a zero-run, \(M_{ij}=\mathbf1\{i\le j\}\), so
\[
t=\frac{r(r+1)}2,\qquad h=j=\frac{r(r+1)(2r+1)}6.
\]
Its conditional mean is \(ab(r+1)/(2r)\); reversing the word changes \(U\) to \(ab-U\) and yields mean \(ab(r-1)/(2r)\) and the same within-orientation variance. The mixture adds \((ab/(2r))^2\) to formula (1), giving exactly the stated \(V_{2r}\).

For \(2r+1\) runs beginning and ending in ones, \(p=r+1,q=r\), and the same three matrix statistics \(t,h,j\) apply (the last row of \(M\) is zero). Formula (1) simplifies to \(W(a,b;r)\); its mean is \(ab/2\). Swapping the two colors gives the other orientation's variance \(W(b,a;r)\) and the same mean. The respective orientation counts are \(\binom{a-1}{r}\binom{b-1}{r-1}\) and \(\binom{a-1}{r-1}\binom{b-1}{r}\). Thus their conditional probabilities are \((a-r)/(a+b-2r)\) and \((b-r)/(a+b-2r)\), proving the odd formula. Reversal symmetry proves \(\mathbb E[U\mid R]=ab/2\) for both parities.

**3. The strict parity-sawtooth inequalities.** Direct common-denominator calculation gives
\[
V_{2r}-V_{2r+2}=
\frac{ab\bigl[abr+4ab+2a+2b-r\bigr]}{6r(r+1)(r+2)}>0.
\tag{2}
\]
For a feasible odd count \(2r+1\), write \(a=r+x,b=r+y\), with \(x,y\geq0\), \(x+y>0\). The immediately preceding even count exists, and
\[
V_{2r}-V_{2r+1}=
\frac{ab(a+b)\bigl[r(x+y)+2xy+x+y\bigr]}{6r(r+1)(a+b-2r)}>0.
\tag{3}
\]
When \(2r+2\) is also feasible write instead \(a=r+1+x,b=r+1+y\), \(x,y\geq0\). Then
\[
V_{2r+2}-V_{2r+1}=
\frac{abG}{6(r+1)(r+2)(a+b-2r)},
\]
where
\[
G=x^2y+xy^2+(4r+10)xy+(r^2+6r+8)(x+y)+2r^2+8r+8>0.
\tag{4}
\]
Finally, for two feasible consecutive odd counts, write \(a=r+1+x,b=r+1+y\), \(x,y\geq0\), \(x+y>0\). Their variance difference is
\[
V_{2r+1}-V_{2r+3}=
\frac{abH}{6(r+1)(r+2)(a+b-2r)(a+b-2r-2)},
\]
where
\[
\begin{aligned}
H={}&x^3y+xy^3+2x^2y^2+(r+2)(x^3+y^3)\\
&+(3r+4)(x^2y+xy^2)+(r^2+2r)(x^2+y^2)\\
&+(2r^2+12r+8)xy+(2r^2+4r)(x+y)>0.
\end{aligned}
\tag{5}
\]
All denominators here are strictly positive on the specified feasible domains. Each numerator's displayed positive-coefficient representation establishes the sign for all sizes; the integer cases at the extreme boundaries are included. Equations (2)–(5) prove the theorem.

## Verification

Run `python verify.py` in an environment with Python 3.9+ and SymPy. Its exact symbolic checks reconstruct the bilinear variance formulas, verify the four difference identities and the positive-polynomial substitutions. Independent exhaustive binary-word enumeration verifies every conditional mean, variance and feasible ordering through length 15; a larger rational-arithmetic grid provides additional corroboration. The symbolic difference identities and positivity argument, rather than the bounded enumeration, establish the infinite assertions.

A second consistency check is that averaging the conditional variance over run counts recovers the classical unconditional inversion variance \(ab(a+b+1)/12\). The conditional means being constant also imply \(\operatorname{Cov}(U,R)=0\), while the nonconstant variances show lack of independence whenever two conditional variances differ.

## Relationship to prior work

The two-letter inversion count and its unconditional variance are classical Gaussian-binomial/Mahonian facts (Canfield, Janson and Zeilberger, 2009). Fixed-content run-count enumeration and the distinction between odd and even run patterns are likewise classical (Kazemi and Jafari, 2014, Section 2; Balado and Silvestre, 2026, Sections 4 and 7). These foundations do not provide the conditional rank-sum variance profile or its strict parity-sawtooth inequalities. The result isolates a second-order dependence that is invisible to the zero covariance between the untransformed rank-sum and total runs.

## Limitations

The theorem addresses the exact permutation null with prescribed binary class sizes, not nonuniform binary words, dependent samples, tied ranks or conditional tail probabilities. It does not assert stochastic or likelihood-ratio ordering of the entire conditional rank-sum distributions. The novelty comparison is limited by possible older treatments of the joint run–inversion distribution; a stronger historical identity not recovered in the literature search could affect priority. Independent external validation has not been performed.

## References

1. E. R. Canfield, S. Janson, and D. Zeilberger, *The Mahonian probability distribution on words is asymptotically normal*, arXiv:0908.2089, first publicly posted 2009-08-14. https://arxiv.org/abs/0908.2089
2. M. R. Kazemi and A. A. Jafari, *Characterization of Order Statistics in Two Runs Using Conditional Expectation*, arXiv:1410.8167, first publicly posted 2014-10-29. https://arxiv.org/abs/1410.8167
3. F. Balado and G. C. M. Silvestre, *Systematic Enumeration of Fundamental Quantities Involving Runs in Binary Strings*, arXiv:2602.10005, first publicly posted 2026-02-10 (supporting later literature). https://arxiv.org/abs/2602.10005
