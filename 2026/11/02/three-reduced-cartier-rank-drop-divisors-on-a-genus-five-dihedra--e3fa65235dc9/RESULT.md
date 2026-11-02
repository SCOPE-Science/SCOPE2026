# Three reduced Cartier rank-drop divisors on a genus-five dihedral family

## Finding

For every prime \(p\ge13\) and every algebraically closed field \(k\) of characteristic \(p\), consider the smooth genus-five curve
\[
H_A:\quad y^2=x^{12}+Ax^6+1,\qquad A\in k,\quad A^2\ne4.
\]
Set \(m=(p-1)/2\), and let \(P_d(t)\) be the classical Legendre polynomial, normalized by \(P_d(1)=1\). Write \(L_d(A)=P_d(A/2)\) after reduction modulo \(p\). Define the ordered triple of degrees
\[
(d_1,d_2,d_3)=
\begin{cases}
(r,2r,3r),&p=6r+1,\\
(r-1,2r-1,3r-1),&p=6r-1.
\end{cases}
\]
Then the geometric \(p\)-rank of the Jacobian of \(H_A\) is exactly
\[
\boxed{f_p(H_A)=2\mathbf1_{L_{d_1}(A)\ne0}+2\mathbf1_{L_{d_2}(A)\ne0}+\mathbf1_{L_{d_3}(A)\ne0}.}
\]
In the standard basis of holomorphic differentials, the unrooted Cartier--Manin matrix \(H\) has determinant
\[
\boxed{\det H=(-1)^{d_3}L_{d_1}(A)^2L_{d_2}(A)^2L_{d_3}(A).}
\]
For each \(i\in\{1,2,3\}\), the rank-drop divisor defined by \(L_{d_i}=0\) is reduced, lies wholly in the smooth parameter locus, and consists of exactly \(d_i\) distinct geometric parameters. Its contribution to the determinant divisor has multiplicity \(2,2,1\), respectively; at intersections the multiplicities add. The three reduced divisor degrees add to \(p-1\) when \(p\equiv1\pmod6\) and \(p-2\) when \(p\equiv5\pmod6\), counted separately, not as the cardinality of their union. The total determinant-divisor degree is \(3(p-1)/2\) in the first congruence class and \((3p-7)/2\) in the second.

For example, in characteristic \(13\) the three polynomial degrees are \((2,4,6)\) and their pairwise greatest common divisors are constants. There are precisely six nonordinary parameters with \(p\)-rank three, six with \(p\)-rank four, and all remaining smooth parameters have rank five. In characteristic \(19\) the degrees are \((3,6,9)\), and only the first and third divisors intersect: they share the parameter \(A=0\), which has \(p\)-rank two. The other nonordinary parameters consist of eight with rank three and eight with rank four. These examples count \(A\)-parameters over an algebraic closure, not curve-isomorphism classes.

## Assumptions and scope

All ranks are geometric, over an algebraically closed field. The parameter \(A\) ranges over all of \(k\) except \(\pm2\), with no restriction to \(\mathbb F_p\). The polynomial on the right side of the equation has degree twelve, and its derivative is \(6x^5(2x^6+A)\); for \(p\ge13\) it is squarefree precisely when \(A^2\ne4\). Hence its smooth projective model has genus five. Each displayed \(L_d\) is an element of the prime-field polynomial ring \(\mathbb F_p[A]\) interpreted over \(k\).

The \(p\)-rank is the dimension over \(\mathbb F_p\) of the geometric \(p\)-torsion of the Jacobian. Equivalently it is the stable rank of Cartier on holomorphic differentials. It is not, in general, the rank of a single Cartier matrix; the equality here is established using its special one- and two-cycle structure.

## Proof

**Step 1: the complete coefficient matrix.** Put \(m=(p-1)/2\), \(z=x^6\), and
\[
(z^2+Az+1)^m=\sum_{s=0}^{2m}T_{m,s}(A)z^s.
\]
Reciprocity of the parent polynomial gives \(T_{m,s}=T_{m,2m-s}\). The usual holomorphic basis is \(\omega_i=x^{i-1}dx/y\), for \(1\le i\le5\). The unrooted Cartier--Manin coefficients are
\[
H_{ij}=[x^{pi-j}](x^{12}+Ax^6+1)^m,
\]
where an out-of-range coefficient is zero. Thus \(H_{ij}\ne0\) only if \(pi-j\equiv0\pmod6\). If \(p=6r+1\), this forces \(j=i\) and the five diagonal entries are
\[
T_{m,r},\ T_{m,2r},\ T_{m,3r},\ T_{m,2r},\ T_{m,r}.
\]
If \(p=6r-1\), this forces \(j=6-i\) and the five antidiagonal entries, in increasing \(i\), are
\[
T_{m,r-1},\ T_{m,2r-1},\ T_{m,3r-1},\ T_{m,2r-1},\ T_{m,r-1}.
\]
In each case the three indices are \(d_1,d_2,d_3\), all at most \(m\).

**Step 2: Legendre identity, without experimental extrapolation.** The standard generating series for Legendre polynomials is
\[
\sum_{s\ge0}P_s(t)z^s=(1-2tz+z^2)^{-1/2}.
\]
Since \(m\equiv-1/2\pmod p\), the binomial expansion of \((1+Az+z^2)^m\) agrees, through \(z^m\), with the expansion of \((1+Az+z^2)^{-1/2}\): all denominators from the binomial coefficients up to this order are invertible modulo \(p\). Comparing coefficients and using \(P_s(-t)=(-1)^sP_s(t)\) yields the exact polynomial identity
\[
\boxed{T_{m,s}(A)=(-1)^sP_s(A/2)}\qquad(0\le s\le m).
\]
Substitution into Step 1 proves the displayed determinant formula. The reversing permutation in dimension five has sign \((-1)^{10}=1\), and the parity of the product of the five coefficient signs equals the parity of \(d_3\).

**Step 3: stable Cartier rank.** Cartier is Frobenius-inverse-semilinear over \(k\). In the first congruence class its matrix preserves each one-dimensional coordinate line. In the second it exchanges the basis lines indexed \(i\) and \(6-i\), with equal coefficients on each paired orbit by reciprocity. On each such orbit the action is bijective if its Legendre coefficient is nonzero, while it is zero if the coefficient vanishes. Consequently the stable Cartier image is exactly the direct sum of the invertible orbits, of dimensions \(2,2,1\). This establishes the all-parameter \(p\)-rank formula, including simultaneous zeros.

**Step 4: each rank-drop divisor is reduced.** The leading coefficient of \(L_d(A)\) is \(4^{-d}\binom{2d}{d}\), nonzero modulo \(p\) because \(d\le m\). Thus its degree is \(d\). Furthermore, \(L_d(2)=1\) and \(L_d(-2)=(-1)^d\), excluding both singular parameters. The Legendre differential equation becomes
\[
(A^2-4)L_d''(A)+2A L_d'(A)-d(d+1)L_d(A)=0.
\]
At a putative double root \(a\notin\{\pm2\}\), this equation forces \(L_d''(a)=0\); differentiating repeatedly forces all derivatives up to order \(d\) to vanish. Here \(d<p\), so this contradicts that \(L_d\) has degree \(d\). The roots are therefore simple. The divisor and degree statements follow from Step 2 and the determinant factorization; shared roots between different factors are counted with their combined multiplicities.

**Step 5: exact small-characteristic intersection examples.** Reducing the three Legendre polynomials modulo \(13\) and applying the Euclidean algorithm gives pairwise gcd degrees \((0,0,0)\); modulo \(19\) it gives \((0,1,0)\), with the sole nontrivial gcd equal to \(A\) after monic normalization. The asserted stratum counts follow immediately from separability and the weights \((2,2,1)\). The provided executable checker reproduces these exact finite-field gcd certificates.

## Verification

The accompanying \(\texttt{verify.py}\) uses only Python's standard library. It reconstructs the Legendre polynomials by recurrence and the coefficient polynomials by binomial enumeration, checks their equality and squarefreeness for all forty-four primes \(5\le p<200\), and builds the complete five-by-five Hasse--Witt matrix for every smooth \(A\in\mathbb F_p\). It compares its rank and the rank of the fifth iterate against the formula and checks the two gcd examples. The completed run printed \(\texttt{VERIFY\_OK}\). Finite checks do not replace Steps 1--4, which establish the conclusion over all algebraic closures and all primes in scope.

## Relationship to prior work

Ohashi and Kudo (2026), Section 4.3, equation (4.13) and Proposition 4.9, introduce exactly this genus-five family and give an isogeny of its Jacobian to a product of elliptic curves. Their Proposition 4.11 and Algorithm 3 characterize and enumerate *superspecial* members using three truncated hypergeometric conditions, with a different auxiliary parameter. These existing results are acknowledged: the curve family, the decomposition, the general Hasse--Witt method, and the superspecial criterion are not claimed as new. The finding here is a direct, normalized, all-prime and all-parameter formula for the **complete geometric \(p\)-rank**, together with three explicit separable rank-drop divisors, their degrees and scheme-theoretic multiplicities and exact low-prime intersections. The superspecial criterion alone does not give the rank of each nonsuperspecial member or the reduced divisor multiplicities. A broader elliptic-factor computation might subsume this refinement, and no claim of definitive historical priority is made.

The classical Legendre equation and its generating series are used as known identities. The earlier literature on supersingular Legendre elliptic curves (e.g. Auer--Top, 2002) concerns related Hasse invariants, but does not by itself specify this genus-five rank-drop divisor decomposition. Ohashi's manuscript *Superspecial curves of generalized Legendre form*, cited in the motivating article, was not inspected in full, so possible broader coverage is a residual originality risk.

## Limitations

The analysis is for algebraically closed fields of prime characteristic at least thirteen; it does not count rational points of these divisors over a given finite subfield, count curve-isomorphism classes, determine complete Newton polygons or Ekedahl--Oort types, or supply a uniform classification of how all three Legendre root sets intersect for arbitrary primes. The formula does determine \(p\)-rank at every such intersection. The priority comparison is a supported same mathematical model literature assessment, not independent validation.

## References

1. R. Ohashi and M. Kudo, *On superspecial hyperelliptic curves of genus 5 whose automorphism groups contain \((\mathbb Z/2\mathbb Z)^3\)*, arXiv:2603.21569v1 (first public 2026-03-23), especially Section 4.3 and Algorithm 3. https://arxiv.org/html/2603.21569v1
2. R. Auer and J. Top, *Legendre elliptic curves over finite fields*, Journal of Number Theory **95** (2002), 303--312.
3. R. Ohashi, *Superspecial curves of generalized Legendre form*, referenced in [1], publication details and full text not verified.
