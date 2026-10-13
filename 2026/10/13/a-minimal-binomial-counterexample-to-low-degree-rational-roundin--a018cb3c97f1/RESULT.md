# A minimal binomial counterexample to low-degree rational-rounding factorization
## Finding
Let \(0<p<1\), let \(X\sim\operatorname{Bin}(3,p)\), and define
\[
Y=\left\lfloor\frac{3X}{2}\right\rfloor.
\]
Then \(Y\) cannot be represented as a sum of independent random variables each supported on \(\{0,1,2,3\}\). Equivalently, its probability-generating polynomial cannot be factored into nonconstant polynomials with nonnegative coefficients and degrees at most \(3\).

Consequently, Conjecture 4.8 of Tang and Tang is false already for \((j,k)=(3,2)\) and a three-trial binomial random variable. Moreover, \(n=3\) is minimal within the binomial family \(X\sim\operatorname{Bin}(n,p)\) at this pair \((j,k)\): for \(n\le2\), the rounded variable itself has support contained in \(\{0,1,2,3\}\).

## Assumptions and scope
The parameter satisfies \(0<p<1\). The source paper calls a random variable strongly Rayleigh when its probability-generating polynomial is real stable, and records that every Poisson-binomial law is strongly Rayleigh. Thus \(X\sim\operatorname{Bin}(3,p)\) lies inside the conjecture's hypothesis.

The conclusion concerns the conjectured representation of \(\lfloor jX/k\rfloor\) as a sum of independent variables taking values in \(\{0,1,\ldots,j\}\). It does not assert anything about optimal approximation in Wasserstein distance, nor does it challenge the source's positive result for \(j=2\).

## Proof
The four possible values of \(X\) are sent by \(x\mapsto\lfloor3x/2\rfloor\) as
\[
0\mapsto0,\qquad 1\mapsto1,\qquad 2\mapsto3,\qquad 3\mapsto4.
\]
Therefore the probability-generating polynomial of \(Y\) is
\[
G_p(z)=(1-p)^3+3p(1-p)^2z+3p^2(1-p)z^3+p^3z^4.
\]
Write its coefficients as \(a_0,\ldots,a_4\). For \(0<p<1\), one has
\[
a_0,a_1,a_3,a_4>0,\qquad a_2=0.
\]

Assume for contradiction that \(Y=Z_1+\cdots+Z_m\), where the \(Z_r\) are independent and each is supported on \(\{0,1,2,3\}\). Their generating polynomials \(F_r(z)\) have nonnegative coefficients and degree at most \(3\), and
\[
G_p(z)=\prod_r F_r(z).
\]
Because \(a_0>0\), every factor has a positive constant coefficient. Because \(a_4>0\), the sum of the factor degrees is \(4\), so at least two factors are nonconstant.

The coefficient of \(z^2\) in a product of nonnegative-coefficient polynomials is a sum of nonnegative terms. Since that coefficient is zero, no factor can contain a positive \(z^2\) coefficient, and two distinct factors cannot both contain a positive \(z\) coefficient. Since \(a_1>0\), exactly one nonconstant factor contains a \(z\) term. The degree partition of \(4\), together with the same zero-quadratic-coefficient condition, then forces the nonconstant factors to have degrees \(1\) and \(3\); the cubic factor can contain neither a \(z\) nor a \(z^2\) term. Hence, after absorbing positive constants,
\[
G_p(z)=C(1+uz)(1+vz^3)
\]
for some \(C,u,v>0\). Every polynomial of this form satisfies
\[
a_0a_4=a_1a_3.
\]
But the displayed coefficients of \(G_p\) give
\[
a_0a_4=p^3(1-p)^3,
\qquad
a_1a_3=9p^3(1-p)^3,
\]
which is impossible for \(0<p<1\). This proves the nonfactorization and hence the failure of the conjectured independent-sum representation.

For minimality inside the binomial family at \((j,k)=(3,2)\), if \(n=1\) or \(n=2\), then
\[
0\le\left\lfloor\frac{3X}{2}\right\rfloor\le3,
\]
so the rounded variable itself is a single random variable supported on \(\{0,1,2,3\}\). Thus \(n=3\) is the first binomial size at which failure is possible, and it fails for every nondegenerate \(p\).

## Verification
The argument is exact and uses only nonnegativity of probability-generating coefficients and support arithmetic. No numerical root calculation or finite search is used.

The critical implication was replayed directly from the coefficient pattern: a positive constant and leading coefficient, positive linear and cubic coefficients, and zero quadratic coefficient force the only possible nontrivial low-degree support decomposition to be \({0,1}+{0,3}\). Such a product necessarily has \(a_0a_4=a_1a_3\), whereas the binomial rounding has the ratio \(a_1a_3/(a_0a_4)=9\) throughout \(0<p<1\).

## Relationship to prior work
Tang and Tang identify Poisson-binomial variables with strongly Rayleigh laws and study rational rounding. Their Theorem 4.7, attributed to an unpublished manuscript of Liggett, shows that \(\lfloor2X/3\rfloor\) remains a sum of independent variables supported on \(\{0,1,2\}\). They then formulate Conjecture 4.8 asserting the analogous degree-\(j\) factorization for every \(j,k\ge1\).

Immediately after the conjecture they note that, for general nonnegative-coefficient polynomials, the classes defined by the interlacing representation and by degree-at-most-three positive factorization are already incomparable. That observation does not settle their conjecture, because the conjecture concerns the special subclass actually produced by rounding a strongly Rayleigh random variable. The present example belongs to that special subclass and therefore gives a direct counterexample.

Targeted searches for the conjecture, the exact rounded binomial \(\lfloor3\operatorname{Bin}(3,p)/2\rfloor\), its coefficient pattern, and degree-three factorization found no published statement of this counterexample. The 2018 Liggett manuscript cited by Tang and Tang is unpublished and was not available for direct full-text inspection; this remains the principal literature risk.

## Limitations
The result disproves the universal conjecture but does not classify all pairs \((j,k)\) or all strongly Rayleigh inputs for which low-degree factorization survives. It also does not address the best approximate factorization or Wasserstein approximation after exact factorization fails.

The originality assessment is based on targeted database searches and full inspection of the relevant part of the public Tang--Tang preprint. An equivalent observation may exist in unpublished correspondence or literature using different terminology; the cited Liggett manuscript is the main unresolved source risk.

## References
1. W. Tang and F. Tang, “The Poisson binomial distribution -- Old & New,” arXiv:1908.10024v1, first public 2019-08-27, especially Corollary 4.2, Theorem 4.7, Conjecture 4.8, and the discussion of the classes \(P_3\) and \(Q_3\).
