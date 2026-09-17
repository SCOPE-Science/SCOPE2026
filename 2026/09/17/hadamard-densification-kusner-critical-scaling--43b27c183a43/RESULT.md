# Hadamard densification and critical dimension scaling in Xiong's Kusner counterexamples

## Summary

Nathan Xiong's recent construction gives, for every \(p>4\), an equilateral set of \(8m\) points in \(\ell_p^{8m-2}\), using Sylvester Hadamard matrices of order \(m=2^k\). Two refinements are proved here.

1. The Sylvester matrix can be replaced by **any normalized Hadamard matrix of order \(m\)**, with the back block built as \(H_4\otimes H\). The same scalar equation and the same four distance calculations remain valid.
2. Near the critical exponent \(p=4\), this Hadamard-generalized template has an exact first-order dimension scale. If \(\varepsilon=p-4\downarrow0\), the least ambient dimension achievable in this template is
   \[
   D_{\rm XH}(4+\varepsilon)=\left(\frac{8}{c}+o(1)\right)\frac1\varepsilon,
   \qquad
   c=\sqrt2\log(1+\sqrt2)-\frac74\log2
   =0.0334429143005567\ldots.
   \]
   Thus \(8/c=239.2136022627\ldots\). In particular, if
   \[
   D(p):=\min\{n:e(\ell_p^n)\ge n+2\},
   \]
   then
   \[
   D(4+\varepsilon)\le \left(239.2136022627\ldots+o(1)\right)\varepsilon^{-1}.
   \]

The upper bound uses Paley Hadamard matrices of order \(q+1\) for primes \(q\equiv3\pmod4\), together with the prime number theorem in arithmetic progressions. The matching lower bound is only for the stated Xiong--Hadamard template, not for arbitrary equilateral configurations.

## Definitions

For \(p>4\) and \(a>1\), set
\[
R=a^p+2,\qquad
A=(a+1)^p+(a-1)^p+2,\qquad
B=2a^p+2^p,
\]
and
\[
\Phi_p(a)=\frac{2A-B}{2^{p-1}R}.
\]
Xiong's scalar condition is
\[
\Phi_p(a)=1+\frac1m. \tag{1}
\]
His four vectors are
\[
q_{00}=(a,1,1,0),\quad q_{10}=(-1,a,0,1),\quad
q_{01}=(-1,0,a,-1),\quad q_{11}=(0,-1,1,a).
\]
They satisfy, for distinct \(i,i'\in\mathbf F_2^2\),
\[
\|q_i\pm q_{i'}\|_p^p=
\begin{cases}A,&i+i'\in\{10,01\},\\B,&i+i'=11.\end{cases} \tag{2}
\]

A Hadamard matrix \(H\) of order \(m\) has entries \(\pm1\) and \(HH^T=mI\). Normalize it so a distinguished column \(t=0\) is all \(+1\). Let \(H_4\) be the character table of \(\mathbf F_2^2\), and put \(K=H_4\otimes H\).

The **Xiong--Hadamard template** is Xiong's construction with the front Walsh matrix replaced by \(H\), and the back Walsh matrix replaced by \(K\), retaining the same two deleted columns and the same weights \(\alpha,\beta\).

## Theorem 1: arbitrary Hadamard orders work

**Claim.** Suppose a Hadamard matrix of order \(m\) exists and there is \(a>1\) satisfying (1). Then the Xiong--Hadamard template gives \(8m\) equilateral points in \(\ell_p^{8m-2}\).

### Construction

For a row \(s\) of \(H\) and \(i\in\mathbf F_2^2\), define the front vector
\[
U_{i,s}=(H_{s,1}q_i,\ldots,H_{s,m}q_i)\in\mathbb R^{4m}.
\]
Index rows of \(K\) by \((i,s)\) and columns by \((j,t)\), where \(i,j\in\mathbf F_2^2\) and \(s,t\in[m]\), with \(t=0\) the normalized column of \(H\). Delete columns \((00,0)\) and \((11,0)\); multiply columns \((10,0)\) and \((01,0)\) by \(\beta\), and all remaining columns by \(\alpha\). The resulting row is \(V_{i,s}\in\mathbb R^{4m-2}\). Set
\[
X_{\sigma,i,s}=(\sigma U_{i,s},V_{i,s}),\qquad \sigma\in\{\pm1\}.
\]
As in Xiong, choose
\[
\alpha^p=R/4,\qquad \beta^p=m(A-B)/2^p. \tag{3}
\]
The inequality \(A>B\) for \(p>2,a>1\) is unchanged.

### Distance counts

Only Hadamard orthogonality is needed.

* If \(i=i'\) and \(s\ne s'\), two rows of \(H\) agree in \(m/2\) positions and differ in \(m/2\). Hence the front contribution is \(2^{p-1}mR\), independently of the two signs.
* If \(i\ne i'\), each front block is a signed copy of \(q_i\pm q_{i'}\), so (2) gives front contribution \(mA\) or \(mB\), exactly as in Xiong.
* In the back block, distinct rows of \(K\) differ in exactly \(2m\) columns. If \(i=i'\), none of the four \(t=0\) columns differ, so all \(2m\) differing coordinates carry weight \(\alpha\).
* If \(i\ne i'\), exactly two of the four \(t=0\) columns differ. Consequently \(2m-2\) differing columns have \(t\ne0\). For \(i+i'=10\) or \(01\), exactly one of the two retained \(\beta\)-columns differs; for \(i+i'=11\), both differ. These are precisely Xiong's back-coordinate counts.

Substituting (1) and (3) therefore reproduces the four common \(p\)-th-power distances \(2^pmR\). This proves the claim.

## Theorem 2: the critical scale at \(p=4\)

For \(p\) sufficiently close to \(4\) from above, define
\[
M(p)=\max_{a\ge1}\Phi_p(a).
\]
Then
\[
M(4+\varepsilon)=1+c\varepsilon+O(\varepsilon^2), \tag{4}
\]
where
\[
c=\sqrt2\log(1+\sqrt2)-\frac74\log2>0. \tag{5}
\]

### Proof of the expansion

At \(p=4\), direct simplification gives
\[
\Phi_4(a)=\frac{a^4+12a^2-4}{4(a^4+2)}
=1-\frac{3(a^2-2)^2}{4(a^4+2)}. \tag{6}
\]
Thus \(a_0=\sqrt2\) is the unique global maximizer, \(M(4)=1\), and
\[
\partial_a\Phi_4(a_0)=0,\qquad \partial_a^2\Phi_4(a_0)=-2.
\]
Also \(\Phi_p(a)\to2^{2-p}\) as \(a\to\infty\), uniformly for \(p\) in a sufficiently small compact neighborhood of \(4\). Hence the strict global maximum in (6) persists near \(a_0\). The implicit-function theorem gives a smooth maximizing branch \(a_*(p)=\sqrt2+O(p-4)\), and the envelope expansion yields
\[
M'(4)=\partial_p\Phi_p(a)\big|_{(p,a)=(4,\sqrt2)}.
\]
Writing \(x=1+\sqrt2\) and using \(\sqrt2-1=x^{-1}\), differentiation gives
\[
\partial_p\Phi_p(a)\big|_{(4,\sqrt2)}
=\sqrt2\log(1+\sqrt2)-\frac74\log2=c,
\]
which proves (4).

For completeness, positivity can be shown without decimal evaluation. Put \(t=\sqrt2-1\). The positive artanh series gives
\[
\log(1+\sqrt2)=2\left(t+\frac{t^3}{3}+\cdots\right)>\frac78,
\]
while \(\log2<7/10\) (because the first four terms of \(e^{7/10}\) already exceed 2) and \(\sqrt2>7/5\). Hence \((7/(4\sqrt2))\log2<7/8\), proving \(c>0\).

## Theorem 3: asymptotically optimal dimension inside the template

Let \(D_{\rm XH}(p)\) be the least ambient dimension \(8m-2\) obtainable from the Xiong--Hadamard template.

Any valid template instance satisfies (1), so
\[
\frac1m=\Phi_p(a)-1\le M(p)-1.
\]
Therefore, by (4),
\[
m\ge \frac1{M(p)-1}=\frac{1+o(1)}{c\varepsilon}. \tag{7}
\]
This yields the template lower bound
\[
D_{\rm XH}(4+\varepsilon)\ge\left(\frac8c+o(1)\right)\varepsilon^{-1}. \tag{8}
\]

For the matching upper bound, set \(x=(M(p)-1)^{-1}\). The prime number theorem in arithmetic progressions implies that there is a prime \(q\equiv3\pmod4\) with
\[
q>x,\qquad q=(1+o(1))x.
\]
Paley's construction supplies a Hadamard matrix of order \(m=q+1\). Then \(m>x\), so \(1+1/m<M(p)\). Xiong's endpoint value \(\Phi_p(1)<1\), together with continuity and a maximizer attaining \(M(p)\), provides an \(a>1\) satisfying (1). Theorem 1 applies, and
\[
m=(1+o(1))x=\frac{1+o(1)}{c\varepsilon}.
\]
Combining with (8),
\[
D_{\rm XH}(4+\varepsilon)=\left(\frac8c+o(1)\right)\varepsilon^{-1}. \tag{9}
\]
Since every template construction is an actual equilateral set of \(n+2\) points in dimension \(n\), the global threshold \(D(p)\) obeys the same expression as an upper bound.

## Concrete check away from the asymptotic regime

At \(p=5\), Paley type I with \(q=43\) gives a Hadamard matrix of order \(m=44\), which is not a power of two. Solving (1) gives
\[
a\approx1.3112524053903019.
\]
The resulting construction has 352 points in \(\mathbb R^{350}\). A direct floating-point enumeration of all pairwise fifth-power distances gives a maximum relative discrepancy below \(5\times10^{-16}\). This is only a consistency check; the general proof above is exact. It is not competitive with Chalmers' 58-point construction in \(\ell_5^{56}\).

## Interpretation and limitations

The result explains the singular behavior of Xiong's family as \(p\downarrow4\): equation (6) has a nondegenerate tangency at \(a=\sqrt2\), and the excess height above 1 grows linearly with \(p-4\). The required Hadamard order is therefore of order \((p-4)^{-1}\). Replacing dyadic Sylvester orders by asymptotically dense Paley orders removes the factor-of-two granularity and exposes the exact first-order constant of this template.

No lower bound of order \((p-4)^{-1}\) is claimed for arbitrary equilateral configurations. A different construction could violate Kusner's bound in substantially smaller dimension. The result is a quantitative refinement of Xiong's construction, not an optimality theorem for \(e(\ell_p^n)\) itself.

## References

1. N. Xiong, *Kusner's conjecture is false for \(p>4\)*, arXiv:2609.14794 (2026).
2. L. R. Chalmers, *A counterexample to Kusner's conjecture on equilateral sets*, arXiv:2608.14013 (2026).
3. H.-J. Ge, Z. Xu, Y. Zhou, *Kusner's conjecture: Exact values and linear bounds*, arXiv:2606.03987 (2026).
4. K. J. Swanepoel, *A problem of Kusner on equilateral sets*, Arch. Math. (Basel) 83 (2004), 164--170, doi:10.1007/s00013-003-4840-8.
5. K. J. Swanepoel, R. Villa, *Maximal Equilateral Sets*, Discrete Comput. Geom. 50 (2013), 354--373, doi:10.1007/s00454-013-9523-z. This earlier work is a relevant precedent for using non-dyadic Hadamard orders and asymptotic estimates in a different equilateral-set problem near \(p=2\).
6. R. E. A. C. Paley, *On Orthogonal Matrices*, J. Math. Phys. 12 (1933), 311--320, doi:10.1002/sapm1933121311.
7. Prime number theorem in arithmetic progressions, used only through the standard corollary that primes \(q\equiv3\pmod4\) can be chosen with successive multiplicative gap \(1+o(1)\).

## Reproducibility

`artifacts/verify_p5_paley44.py` reconstructs the non-dyadic \(p=5,m=44\) example, checks the Hadamard identity, solves the scalar equation by bisection, and verifies all pairwise distances numerically. The formulas (6), (5), and the value \(8/c\) can be checked independently by symbolic differentiation or direct algebra.
