# Complete ordering polytope for three pairwise-independent continuous observations

## Result

Let \(X_1,X_2,X_3\) be pairwise independent real random variables with the
same atomless distribution function \(F\).  For distinct \(a,b,c\in\{1,2,3\}\),
write
\[
\pi_{abc}:=\Pr(X_a<X_b<X_c),
\]
and let
\[
q_i:=\Pr\!\left(X_i=\max(X_1,X_2,X_3)\right).
\]

Then the complete set of possible strict-ordering laws is
\[
\boxed{
(\pi_{123},\pi_{132},\pi_{213},\pi_{231},\pi_{312},\pi_{321})
=(a,b,c,b,c,a)
}
\]
where
\[
\boxed{
0\le a,b,c\le \frac14,\qquad a+b+c=\frac12.
}
\]
Every point of this triangle is attainable by pairwise-independent random
variables with the prescribed common atomless marginal law.

Equivalently, the extreme-rank probabilities satisfy
\[
\boxed{
q_1+q_2+q_3=1,\qquad \frac14\le q_i\le\frac12,
}
\]
and every such triple is attainable.  Moreover,
\[
\Pr(X_i=\min(X_1,X_2,X_3))=q_i
\]
for each label \(i\).  Thus pairwise independence forces a reversal symmetry
of the six ordering probabilities even though it does not force
exchangeability.

The relation between the two parameterizations is
\[
a=\frac12-q_2,\qquad
b=\frac12-q_3,\qquad
c=\frac12-q_1.
\]

## Proof

Because the common law is atomless, ties occur with probability zero.  Fix a
label \(i\), and let \(j,k\) be the other two labels.  Conditional on
\(X_i=x\), pairwise independence gives
\[
\Pr(X_j<x\mid X_i=x)=\Pr(X_k<x\mid X_i=x)=F(x)
\]
for almost every \(x\).  The Fréchet bounds for the intersection of two events
with common marginal probability \(F(x)\) therefore give
\[
\max(0,2F(x)-1)
\le
\Pr(X_j<x,\ X_k<x\mid X_i=x)
\le F(x).
\]
Since \(F(X_i)\sim U(0,1)\),
\[
\int_0^1\max(0,2u-1)\,du
\le q_i\le
\int_0^1u\,du,
\]
hence
\[
\frac14\le q_i\le\frac12.
\]

Let
\[
A=\{X_i>X_j\},\qquad B=\{X_i>X_k\}.
\]
Pairwise independence and identical atomless marginals imply
\(\Pr(A)=\Pr(B)=1/2\).  Therefore
\[
\Pr(X_i\text{ is minimum})
=\Pr(A^c\cap B^c)
=1-\Pr(A\cup B)
=\Pr(A\cap B)
=q_i.
\]
Exactly one coordinate is the maximum, so \(q_1+q_2+q_3=1\).

Now put
\[
(a,b,c,d,e,f)
=(\pi_{123},\pi_{132},\pi_{213},\pi_{231},\pi_{312},\pi_{321}).
\]
The three pairwise comparison identities
\[
\Pr(X_1<X_2)=\Pr(X_1<X_3)=\Pr(X_2<X_3)=\frac12
\]
become
\[
a+b+e=\frac12,\qquad
a+b+c=\frac12,\qquad
a+c+d=\frac12.
\]
Together with \(a+b+c+d+e+f=1\), these imply
\[
d=b,\qquad e=c,\qquad f=a.
\]
Also
\[
q_1=a+b,\qquad q_2=b+c,\qquad q_3=a+c.
\]
Using \(a+b+c=1/2\), the lower bounds \(q_i\ge1/4\) are exactly
\[
a,b,c\le\frac14.
\]
This proves necessity.

For sufficiency, first take independent \(U,V\sim U(0,1)\) and define
\[
(X_1,X_2,X_3)=(U,V,(U+V)\bmod1).
\]
Every pair is independent and uniform: each relevant two-coordinate map is a
Haar-measure-preserving surjective homomorphism of the two-torus.  If
\(U+V<1\), then \(X_3=U+V>\max(U,V)\); if \(U+V>1\), then
\(X_3=U+V-1<\min(U,V)\).  Splitting each of those two triangles by \(U<V\)
shows
\[
(\pi_{123},\pi_{132},\pi_{213},\pi_{231},\pi_{312},\pi_{321})
=\left(\frac14,0,\frac14,0,\frac14,\frac14\right),
\]
so
\[
(q_1,q_2,q_3)=\left(\frac14,\frac14,\frac12\right).
\]
Permuting the coordinate labels gives the other two vertices
\[
\left(\frac12,\frac14,\frac14\right),\qquad
\left(\frac14,\frac12,\frac14\right)
\]
of the feasible \(q\)-triangle.

For any admissible \(q=(q_1,q_2,q_3)\), set
\[
\lambda_i=4q_i-1.
\]
Then \(\lambda_i\ge0\) and \(\sum_i\lambda_i=1\).  Mix the three vertex laws
with weights \(\lambda_i\).  Each vertex law has exactly the same product
distribution on every coordinate pair, so the mixture remains pairwise
independent with uniform marginals and has the desired ordering law.
Applying the marginal quantile map \(F^{-1}\) coordinatewise transports the
construction to any prescribed atomless common law.  This proves sharpness
and complete attainability.

## Two-calibration-score rank inference

Let \(S_1,S_2\) be two calibration scores and \(S_3\) a test score, with a
common atomless distribution and only pairwise independence assumed.  For
the usual upper-tail rank p-value
\[
p=\frac{1+\mathbf 1\{S_1\ge S_3\}+\mathbf 1\{S_2\ge S_3\}}{3},
\]
there is a \(q\in[1/4,1/2]\) such that
\[
\boxed{
\Pr(p=1/3)=q,\qquad
\Pr(p=2/3)=1-2q,\qquad
\Pr(p=1)=q.
}
\]
Conversely every \(q\in[1/4,1/2]\) is attainable.

Hence the sharp worst-case CDF over the pairwise-independent class is
\[
\boxed{
\sup\Pr(p\le\alpha)=
\begin{cases}
0,&0\le\alpha<1/3,\\
1/2,&1/3\le\alpha<2/3,\\
3/4,&2/3\le\alpha<1,\\
1,&\alpha\ge1.
\end{cases}
}
\]
In particular, at the first attainable conformal level, nominal
miscoverage \(1/3\) can become \(1/2\).

A continuously randomized rank version makes the small-level distortion
visible.  Let \(W\sim U(0,1)\) be independent and put
\[
\widetilde p=
\frac{\#\{i\in\{1,2\}:S_i\ge S_3\}+W}{3}.
\]
Under an exchangeable atomless triple, \(\widetilde p\) is exactly uniform.
Under pairwise independence its sharp worst-case CDF is
\[
\boxed{
\sup\Pr(\widetilde p\le\alpha)=
\begin{cases}
\frac32\alpha,&0\le\alpha\le1/3,\\
\frac12,&1/3\le\alpha\le1/2,\\
\frac32\alpha-\frac14,&1/2\le\alpha\le2/3,\\
\frac14+\frac34\alpha,&2/3\le\alpha\le1.
\end{cases}
}
\]
Thus, for example, a nominal randomized level \(0.05\) can have exact
worst-case rejection probability \(0.075\).

## Relation to prior work

Kemperman (1997) developed sharp bounds for distributions and moments of
order statistics when each \(k\)-tuple is independent.  Okolewski (2017)
extended this program to prescribed \(k\)-tuple copulas and linear
combinations of order-statistic distribution functions.  Okolewski and
Błażejczyk-Okolewska (2025) established sharp bounds for linear
combinations of joint distribution and reliability functions of selected
order statistics under \(k\)-independence.  These are the closest sources
found for limited-independence ordering questions.

The result above concerns a different, label-sensitive object: which named
observation occupies each rank, rather than the distribution of the sorted
values.  The proof uses only pairwise independence, conditional Fréchet
bounds, and an explicit torus construction; none of those ingredients is
claimed as new by itself.

Standard conformal rank validity is based on exchangeability.  Work on
conformal prediction beyond exchangeability develops alternative weighted
or robustness guarantees for specific nonexchangeable settings.  The
contribution here is the exact three-score identification region under the
different structural assumption of pairwise independence.

## Verification

`artifacts/verify_ordering_polytope.py` checks the algebraic polytope
parameterization and its convex-mixture weights exactly using rational
arithmetic.  It also enumerates finite cyclic-torus analogues of the vertex
construction, verifies exact pairwise-uniform two-coordinate tables, and
shows the strict-order probabilities converging to the continuous
\((1/4,0,1/4,0,1/4,1/4)\) vertex as the grid is refined.  The recorded
output is in `artifacts/verification_output.txt`.

## Limitations

- The theorem is specific to three observations.  It does not characterize
  labeled rank laws for four or more pairwise-independent observations.
- Exact sharpness is over all pairwise-independent common-margin laws; the
  extremal torus laws are not exchangeable and their joint distribution is
  singular with respect to three-dimensional Lebesgue measure.
- The rank-inference corollary concerns two calibration scores plus one test
  score.  It does not provide a general finite-sample conformal theorem for
  arbitrary calibration size under pairwise independence.
- The randomized p-value above is an independently jittered rank transform,
  included to expose continuous-level calibration error; it should not be
  confused with tie-randomization in a continuous-score conformal procedure.
- The full text of Kemperman (1997) and Okolewski (2017) was not inspected.
  Their abstracts describe sharp symmetric order-statistic bounds, so an
  older equivalent label-sensitive formulation under different terminology
  remains a residual originality risk.

## References

1. J. H. B. Kemperman, “Bounding Moments of an Order Statistic When Each
   K-Tuple is Independent,” in *Distributions with Given Marginals and
   Moment Problems*, 1997, pp. 291–304.
   https://doi.org/10.1007/978-94-011-5532-8_34
2. A. Okolewski, “Distribution bounds for order statistics when each
   k-tuple has the same piecewise uniform copula,” *Statistics* 51 (2017),
   969–987. https://doi.org/10.1080/02331888.2017.1289533
3. A. Okolewski and B. Błażejczyk-Okolewska, “Tight Bounds for Joint
   Distribution Functions of Order Statistics Under k-Independence,”
   *Entropy* 27 (2025), 1250. https://doi.org/10.3390/e27121250
4. V. Vovk, A. Gammerman, and G. Shafer, *Algorithmic Learning in a Random
   World*, Springer, 2005. https://doi.org/10.1007/b106715
5. R. F. Barber, E. J. Candès, A. Ramdas, and R. J. Tibshirani,
   “Conformal prediction beyond exchangeability,” *Annals of Statistics*
   51 (2023), 816–845. https://doi.org/10.1214/23-AOS2276
