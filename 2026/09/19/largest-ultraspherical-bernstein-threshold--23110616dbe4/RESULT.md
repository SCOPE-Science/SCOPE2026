# Exact Hermite-edge threshold for complete Bernstein scaling of the largest ultraspherical zero

## Statement

Let \(z_{n,1}(\lambda)\) be the largest positive zero of the Gegenbauer polynomial
\(C_n^\lambda\), with the reduced interpretation at \(\lambda=0\), and let \(h_n>0\)
be the largest positive zero of the physicists' Hermite polynomial \(H_n\).
For \(d\ge 1/2\), define
\[
G_{n,d}(\lambda)=\sqrt{\lambda+d}\,z_{n,1}(\lambda),\qquad
F_{n,d}(s)=G_{n,d}(s-\tfrac12),\qquad s>0.
\]
Set
\[
d_n^\star=\frac{2h_n^2+2n-1}{4}.
\]

**Theorem.** For every \(n\ge2\) and \(d\ge1/2\),
\[
F_{n,d}\in\mathcal{CBF}
\quad\Longleftrightarrow\quad
F_{n,d}'\text{ is completely monotone}
\quad\Longleftrightarrow\quad
d\le d_n^\star.
\]
For \(n\ge4\), all derivative inequalities are strict throughout the full admissible
range \(1/2\le d\le d_n^\star\):
\[
(-1)^{r-1}F_{n,d}^{(r)}(s)>0,\qquad r\ge1,\ s>0.
\]
For \(n=2,3\), the endpoint \(d=d_n^\star\) gives the constant cases already visible
from the elementary formulas, so strictness fails only there.

Combined with the exact nonlargest-zero classification in Castillo's Theorem A.3,
this gives the complete square-root scale phase diagram: for \(k\ge2\) the threshold
is \(d=k-\tfrac12\), while for the largest zero \(k=1\) it is the Hermite-edge value
\(d_n^\star\).

For \(n\ge4\), this strictly enlarges the sufficient interval
\(d\le\lceil n/2\rceil\) proved in Proposition A.4 of the source paper.

## Proof

The source paper establishes, for every fixed real \(d\), the convergent Laurent
expansion
\[
G_{n,d}(\lambda)
=
h_n+\frac{c_{n,d}}{\lambda}+O(\lambda^{-2}),
\qquad
c_{n,d}
=
\frac{h_n\{4d-(2h_n^2+2n-1)\}}{8}.
\tag{1}
\]
It also proves that for the largest zero the upper boundary orientation is
nonnegative at every regular real boundary point, and that the local algebraic
growth exponents at the finitely many exceptional points are strictly below one.
Those boundary and local-growth arguments are independent of the numerical upper
bound on \(d\); Proposition A.4 uses its stated range only to ensure \(c_{n,d}<0\).

### Sufficiency below the threshold

If \(1/2\le d<d_n^\star\), then \(c_{n,d}<0\). The same boundary-minimum argument as
in Proposition A.4 therefore gives
\[
\operatorname{Im}G_{n,d}(z)>0,\qquad \operatorname{Im}z>0.
\]
After the shift \(s=\lambda+1/2\), \(F_{n,d}\) is holomorphic on
\(\mathbb C\setminus(-\infty,0]\), positive on \((0,\infty)\), and maps the upper
half-plane to itself. The Pick--Bernstein characterization therefore gives
\(F_{n,d}\in\mathcal{CBF}\), hence \(F_{n,d}'\) is completely monotone.

### The critical endpoint

Let \(d_m\uparrow d_n^\star\). For each \(m\), \(F_{n,d_m}\) is a complete Bernstein
function. On every compact subset of \(\mathbb C\setminus(-\infty,0]\),
\[
\sqrt{s+d_m-\tfrac12}\longrightarrow
\sqrt{s+d_n^\star-\tfrac12}
\]
uniformly, while the zero branch is independent of \(d\). Hence
\(F_{n,d_m}\to F_{n,d_n^\star}\) locally uniformly. The upper-half-plane mapping
property and nonnegativity on \((0,\infty)\) pass to the limit, so the
Pick--Bernstein characterization again yields
\[
F_{n,d_n^\star}\in\mathcal{CBF}.
\]
For \(n\ge4\) this endpoint function is nonconstant: the largest-zero branch has the
nonremovable square-root singularity described in the source paper, and
\(d_n^\star>\lceil n/2\rceil\ge2\), so the scaling factor does not cancel the first
such singularity. Since the function also has a finite limit at infinity, its
complete Bernstein representation has nonzero measure and zero linear coefficient.
The differentiated representation then makes every displayed derivative inequality
strict.

For \(n=2,3\), the source paper gives the explicit formulas and exact endpoint
constants; they agree with \(d_2^\star=1\) and \(d_3^\star=2\).

### Necessity above the threshold

If \(d>d_n^\star\), then \(c_{n,d}>0\). Differentiating (1) along the positive real
axis gives
\[
G_{n,d}'(\lambda)
=
-\frac{c_{n,d}}{\lambda^2}+O(\lambda^{-3})<0
\]
for all sufficiently large \(\lambda\). Every complete Bernstein function is
nondecreasing, and a completely monotone derivative is in particular nonnegative.
Thus neither property can hold. This proves the exact threshold.

## Size of the improvement

The threshold is much larger than the sufficient endpoint in Proposition A.4.
Indeed the Hermite bounds used there already imply
\[
d_n^\star>\left\lceil\frac n2\right\rceil,\qquad n\ge4.
\]
More precisely, let \(a_1=-2.338107\ldots\) be the largest (least negative) zero of
the Airy function \(\operatorname{Ai}\). The standard Hermite edge asymptotic
\[
h_n=(2n+1)^{1/2}
+2^{-1/3}a_1(2n+1)^{-1/6}
+O(n^{-5/6})
\]
gives
\[
d_n^\star
=
\frac{3n}{2}+\frac14
+2^{-1/3}a_1(2n+1)^{1/3}
+O(n^{-1/3}).
\]
In particular \(d_n^\star/n\to3/2\), whereas the previously proved sufficient
endpoint is asymptotic to \(n/2\).

The first nontrivial exact examples are
\[
d_4^\star=\frac{10+\sqrt6}{4}=3.112372\ldots,\qquad
d_5^\star=\frac{14+\sqrt{10}}4=4.290569\ldots.
\]

## Context and originality

Castillo (2026) proves complete Bernstein properties for several distinguished
ultraspherical-zero scalings. Appendix A separates the scale parameter \(d\).
Theorem A.3 gives an exact if-and-only-if threshold for every nonlargest positive
zero. Proposition A.4 proves only the sufficient range
\(1/2\le d\le\lceil n/2\rceil\) for the largest zero and explicitly states that no
optimality of the upper endpoint is claimed. The source also supplies the arbitrary-\(d\)
Laurent coefficient and all boundary geometry needed above.

Earlier work of Ahmed--Muldoon--Spigler and Elbert--Siafarikas establishes
first-derivative monotonicity for particular scales, notably
\[
d_n=\frac{2n^2+1}{4n+2},
\]
rather than an exact classification of all square-root scales by complete
Bernstein behavior.

To the best of our knowledge, no prior source located in searches for ultraspherical
or Gegenbauer zeros, square-root scalings, complete monotonicity, complete Bernstein
functions, largest-zero scale optimization, and Hermite-edge thresholds states the
classification \(d\le d_n^\star\).

## Limitations

The theorem concerns the one-parameter square-root family
\(\sqrt{\lambda+d}\,z_{n,1}(\lambda)\). It does not classify arbitrary positive
multiplicative scales, nor does it optimize finite-order derivative inequalities
outside the complete-monotonicity regime. The threshold is expressed through the
largest Hermite zero; no elementary closed form exists in general. The originality
assessment is literature-based rather than exhaustive.

## References

1. K. Castillo, *Complete Bernstein functions and scaled ultraspherical zeros*,
   arXiv:2609.19186 (2026). https://arxiv.org/abs/2609.19186
2. NIST Digital Library of Mathematical Functions, §18.16(v), Hermite zeros.
   https://dlmf.nist.gov/18.16
3. S. Ahmed, M. E. Muldoon, R. Spigler, *Inequalities and numerical bounds for
   zeros of ultraspherical polynomials*, SIAM J. Math. Anal. 17 (1986), 1000--1007.
   https://doi.org/10.1137/0517070
4. Á. Elbert, P. D. Siafarikas, *Monotonicity properties of the zeros of
   ultraspherical polynomials*, J. Approx. Theory 97 (1999), 31--39.
5. W. Gautschi, *On the Ismail--Letessier--Askey monotonicity conjecture for zeros
   of ultraspherical polynomials*, in *Frontiers in Orthogonal Polynomials and
   q-Series* (2018), 251--266. https://doi.org/10.1142/9789813228887_0013
