# A unique vacancy–fragmentation covariance transition in random circular arc covering

## Finding

For \(n\ge 2\) equal clockwise random arcs on a unit circle, the covariance between the **number** \(K\) of uncovered gaps and their **total length** \(U\) changes from negative to positive exactly once as their common length \(a\) increases. At each finite \(n\) the transition is unique, including the exceptional case \(a_2=1/2\). Its limiting coverage-depth boundary is the unique positive root \(c_*\) of \(e^c=1+c+c^2\), and it admits an explicit finite-size correction.

The exact joint second-moment expression is
\[
 C_n(a):=\operatorname{Cov}(K,U)=(1-a)^n+(n-1)(1-2a)_+^n-n(1-a)^{2n-1}.
\]
For \(n=2\), \(C_n(a)=0\) precisely at \(a=1/2\). For every \(n\ge3\), precisely one \(a_n\in(0,1/2)\) satisfies \(C_n(a_n)=0\). At all finite \(n\), \(C_n(a)<0\) when \(0<a<a_n\), and \(C_n(a)>0\) when \(a_n<a<1\).

As \(n\to\infty\),
\[
 a_n=\frac{c_*}{n}+\frac{c_*/2-c_*^2}{n^2}+O(n^{-3}),\qquad c_*=1.793282132900761\ldots,
\]
and at each fixed \(c>0\),
\[
 C_n(c/n)\longrightarrow e^{-c}-(1+c+c^2)e^{-2c}.
\]
This quantifies a change in the association between fragmentation and the unobserved proportion of a circular substrate: below the critical coverage depth the two measures covary negatively, and above it positively.

## Assumptions and scope

The circle has circumference one. The \(n\ge2\) arc starting points are independent and uniform around it; every arc extends clockwise from its start through length \(a\) with \(0<a<1\). Identical starts occur with probability zero. Let \(X_1,\ldots,X_n\) be the successive clockwise spacings. Their joint law is \(\operatorname{Dirichlet}(1,\ldots,1)\) on the simplex \(X_i>0\), \(\sum_iX_i=1\). Put \(x_+=\max\{x,0\}\). Then
\[
 K=\sum_{i=1}^n\mathbf1_{\{X_i>a\}},\qquad U=\sum_{i=1}^n(X_i-a)_+.
\]
If all points are covered, both statistics are zero. The covariance is not divided by a variance or standardized. Boundary \(a=0\) is excluded because it gives a degenerate deterministic gap count; \(a=1\) is excluded because it gives complete coverage.

## Proof

**Step 1: moments.** Uniform simplex spacings satisfy, for \(0\le s,t\le1\) and distinct \(i,j\),
\[
 \Pr(X_i>s)=(1-s)^{n-1},\qquad
 \Pr(X_i>s,X_j>t)=(1-s-t)_+^{n-1}.
\]
Tail integration gives
\[
 \mathbb E K=n(1-a)^{n-1},\qquad
 \mathbb E U=(1-a)^n.
\]
For diagonal terms, \(\mathbb E[\mathbf1_{\{X_i>a\}}(X_i-a)_+]=(1-a)^n/n\). For \(i\ne j\), integrating the bivariate tail in the excess variable gives \(\mathbb E[\mathbf1_{\{X_i>a\}}(X_j-a)_+]=(1-2a)_+^n/n\). Summing these terms proves
\[
 \mathbb E[KU]=(1-a)^n+(n-1)(1-2a)_+^n
\]
and therefore the displayed covariance formula. These identities are exact for every stated \(n\) and \(a\), including \(a=1/2\).

**Step 2: uniqueness of the sign transition.** On \(1/2\le a<1\) we have
\[
 C_n(a)=(1-a)^n\bigl(1-n(1-a)^{n-1}\bigr).
\]
For \(n\ge3\), \(\frac{n}{2^{n-1}}<1\), so this is strictly positive. For \(n=2\) it is strictly positive for \(a>1/2\), zero at \(a=1/2\).

For \(0<a<1/2\) put \(x=(1-2a)/(1-a)\), so \(0<x<1\) and \(1-a=1/(2-x)\). Dividing the covariance by the strictly positive \((1-a)^n\) gives
\[
 g_n(x)=1-\frac{n}{(2-x)^{n-1}}+(n-1)x^n.
\]
Differentiation yields
\[
 g_n'(x)=n(n-1)\left(x^{n-1}-(2-x)^{-n}\right).
\]
Its sign is the sign of \(h_n(x)-1\) where \(h_n(x)=x^{n-1}(2-x)^n\). For \(0<x<1\),
\[
 \frac{h_n'(x)}{h_n(x)}=\frac{n-1}{x}-\frac{n}{2-x},
\]
so \(h_n\) increases up to \(x_0=2(n-1)/(2n-1)\), then decreases. It satisfies \(h_n(0)=0\), \(h_n(1)=1\), and \(h_n(x_0)>1\) (the last inequality follows because its derivative is negative just left of one). Thus exactly one \(x_1\in(0,x_0)\) satisfies \(h_n(x_1)=1\): \(g_n\) decreases on \((0,x_1)\) and increases on \((x_1,1)\). Moreover \(g_n(1)=0\), hence \(g_n<0\) on \((x_1,1)\). For \(n\ge3\), \(g_n(0)=1-n/2^{n-1}>0\), so precisely one root occurs in \((0,x_1)\), with the claimed strict signs after reversing the monotone change of variable from \(a\) to \(x\). For \(n=2\), \(g_n(0)=0\) and \(g_n<0\) throughout \((0,1)\); its only interior-in-\(a\) zero is \(a=1/2\). At small \(a\), a Taylor expansion independently gives \(C_n(a)=-n(n-1)a^2/2+O_n(a^3)\), confirming the negative orientation.

**Step 3: sharp critical scaling.** Fix \(c>0\) and substitute \(a=c/n\). Uniformly for \(c\) in any compact subset of \((0,\infty)\), logarithmic expansions of the binomial factors yield
\[
 C_n(c/n)=f_0(c)+\frac{f_1(c)}{n}+O(n^{-2}),
\]
where
\[
 f_0(c)=e^{-c}-(1+c+c^2)e^{-2c},\qquad
 f_1(c)=-\frac{c^2}{2}e^{-c}+c^2\left(1-c+\frac{3c^2}{2}\right)e^{-2c}.
\]
The ratio \((e^c-1-c)/c^2=\sum_{k=2}^\infty c^{k-2}/k!\) is strictly increasing from \(1/2\) to infinity for \(c>0\). Hence \(f_0\) changes sign exactly once at the positive \(c_*\) satisfying \(e^{c_*}=1+c_*+c_*^2\). For this root \(c_*>1\), and direct differentiation and substitution give
\[
 f_0'(c_*)=c_*(c_*-1)e^{-2c_*}>0,\quad
 f_1(c_*)=c_*^2(c_*-1)(c_*-1/2)e^{-2c_*}.
\]
The unique finite-\(n\) root, bracketed using values at \(c_*-\varepsilon\) and \(c_*+\varepsilon\), therefore satisfies \(na_n\to c_*\). Expanding its equation around \(c_*\) gives
\[
 na_n=c_*-\frac{f_1(c_*)}{nf_0'(c_*)}+O(n^{-2})
 =c_*+\frac{c_*/2-c_*^2}{n}+O(n^{-2}),
\]
which proves the claimed \(a_n\) expansion. The first displayed compact-uniform expansion also proves the fixed-depth covariance limit.

## Verification

The standalone file `verify.py` implements the exact covariance with rational arithmetic, exact integer-composition approximations to uniform simplex spacings, and numerical bisection of the unique root. Running it with Python 3 (no external packages) produced `verification_output.txt`; all checks passed. The exact rational sign checks cover \(2\le n\le20\); the independent lattice-composition comparison checks \(n\in\{3,4,5\}\), discretization lengths \(80\) and \(160\), and two thresholds for \(n=4\). Numerical roots were checked for \(n\in\{2,3,4,5,10,25,50,100\}\). Finite tests corroborate, but do **not** establish, the general uniqueness or asymptotic theorem; those follow from the symbolic analytic proof above.

## Relationship to prior work

Uniform circular coverings and the marginal statistics of vacancy and gap counts are classical. Holst–Hüsler studied joint asymptotic laws in the equal-arc setting. Huillet's author-shared full text gives the exact number-of-gaps law in Proposition 4 and the vacancy marginal law in Proposition 5, together with connected-component size laws and several scaling regimes; no finite-sample covariance sign theorem or sharp threshold correction was located in the inspected full text. Moriarty–Marchesi–Metcalfe provide approximation bounds for the gap-count distribution, with motivating applications to genomic and metagenomic fragment coverage, rather than the exact joint sign transition.

Crucially, Huffer's earlier work explicitly studies joint moments of vacancy and number of gaps for random arcs of random sizes; taking constant arc lengths may already yield the covariance expression above. Thus the moment formula **is not claimed as a novel independent distributional result**. The separate claim requiring new analysis is the **global unique sign transition for every finite sample size** and its two-term critical scaling. The full Huffer article and associated technical report were not accessible for a conclusive priority comparison, leaving a substantial historical-overlap risk. Additional primary text could show this classification is known; no claim of established historical uniqueness is made.

## Limitations

Only equal deterministic clockwise arc lengths, independent uniform starts, and a circle are covered. Nothing is asserted for unequal or random arc lengths, nonuniform points, or a linear interval; nor for correlations standardized by changing variances. The source-overlap assessment is not an independent priority certification; Huffer's joint-moment theory is a plausible dominating source whose complete historical scope could not be checked. The second-order scaling is asymptotic for the exact unique root, not an error guarantee for an arbitrary finite \(n\). No interpretation of finite numerical checks as an infinite proof is intended.

## References

- L. Holst and J. Hüsler, “On the random coverage of the circle,” *Journal of Applied Probability* **21** (1984), 558–566. DOI: 10.2307/3213617.
- F. W. Huffer, “Some results concerning random arcs on the circle,” *Journal of Applied Probability* **25** (1988), 833–838; earlier Stanford technical report dated June 1987. DOI: 10.2307/3214306.
- T. E. Huillet, “Random covering of the circle: the size of the connected components,” *Advances in Applied Probability* **35** (2003), 563–582. DOI: 10.1239/aap/1059486818.
- T. E. Huillet, “Random covering of the circle: the configuration-space of the free deposition process,” *Journal of Physics A* **36** (published 25 November 2003), 12143–12155. DOI: 10.1088/0305-4470/36/49/002.
- J. Moriarty, J. R. Marchesi, and A. Metcalfe, “Bounds on the distribution of the number of gaps when circles and lines are covered by fragments,” *BMC Bioinformatics* **8** (2007), article 70. DOI: 10.1186/1471-2105-8-70.
