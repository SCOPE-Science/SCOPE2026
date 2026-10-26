# Sharp nil-clean index and conic decomposition fibers in two-by-two finite-field matrix rings

## Finding
For a prime power \(q\geq 2\), write \(F=\mathbb F_q\). For each \(A\in M_2(F)\), let
\[
h_q(A)=\#\{E\in M_2(F):E^2=E,\ (A-E)^2=0\}.
\]
Then the nil-clean index of \(M_2(F)\) is **exactly** \(2q-1\). More precisely, writing \(\tau=\operatorname{tr}A\) and \(\delta=\det A\):

* If \(A^2=0\) or \((A-I)^2=0\), then \(h_q(A)=1\). These conditions are disjoint.
* Otherwise, if \(\tau=1\) and \(A\) is not scalar, then
\[
h_q(A)=\begin{cases}2q-1,&\delta=0,\\q+1-r(A),&\delta\ne0,\end{cases}
\]
where \(r(A)\in\{0,1,2\}\) is the number of *distinct rational eigenvalues* of \(A\), equivalently the number of roots of \(t^2-t+\delta\) in \(F\).
* In every other case \(h_q(A)=0\).

For non-scalar \(A\) of trace one, the decomposition fiber is a plane affine conic: it is two intersecting affine lines when \(\delta=0\) and a smooth affine conic obtained by deleting \(r(A)\) rational points at infinity from a projective conic when \(\delta\ne0\). This describes the fiber geometry over every field characteristic.

The *complete global multiplicity distribution* is specified by the polynomial \(\Phi_q(z)=\sum_{A\in M_2(F)}z^{h_q(A)}\). For odd \(q\),
\[
\begin{aligned}
\Phi_q(z)={}&(q^4-q^3-2q^2+1)+2q^2z\\
&+\frac{q(q+1)(q-3)}2z^{q-1}+(q^2-1)z^q\\
&+\frac{q(q-1)^2}2z^{q+1}+q(q+1)z^{2q-1}.
\end{aligned}
\]
For even \(q\),
\[
\begin{aligned}
\Phi_q(z)={}&(q^4-q^3-2q^2)+2q^2z\\
&+q(q+1)(q/2-1)z^{q-1}\\
&+q(q-1)(q/2)z^{q+1}+q(q+1)z^{2q-1}.
\end{aligned}
\]
Coincident exponents, notably for \(q=2\) and \(q=3\), are combined by polynomial addition.

## Assumptions and scope
The field is any \(\mathbb F_q\), with no restriction on the prime characteristic or extension degree. The decomposition is **additive** and noncommuting: \(A=E+N\), with \(E^2=E\) and \(N^2=0\). In dimension two nilpotency and square-zero are equivalent. Matrices and decompositions are counted as labeled matrices rather than similarity classes. A scalar matrix means a multiple of \(I\). The nil-clean index is the maximum over all \(A\) of the number of such idempotents \(E\).

## Proof
**Step 1: separation by trace.** Every idempotent \(E\) on a two-dimensional vector space has rank \(0,1\), or \(2\). Rank zero forces \(E=0\), whence \(A=N\) and \(A^2=0\); rank two forces \(E=I\), whence \((A-I)^2=0\). If \(\operatorname{rank}E=1\), then \(\operatorname{tr}E=1\), while nilpotency of \(N=A-E\) forces \(\operatorname{tr}A=1\). No scalar \(A=\lambda I\) admits a rank-one solution, since \(\lambda I-E\) has eigenvalues \(\lambda\) and \(\lambda-1\), which cannot both be zero. The two scalar-idempotent cases are disjoint: a matrix and its shift by \(I\) cannot both be nilpotent. Thus, outside the scalar-idempotent cases, only non-scalar trace-one matrices need consideration.

**Step 2: exact conic model.** Every non-scalar trace-one \(A\) has minimal polynomial \(t^2-t+\delta\) of degree two, so it is similar over \(F\) to the companion matrix
\[
A_\delta=\begin{pmatrix}0&-\delta\\1&1\end{pmatrix}.
\]
Every rank-one idempotent \(E\) has trace one and determinant zero. Write
\[
E=\begin{pmatrix}s&u\\v&1-s\end{pmatrix}.
\]
For the trace-zero matrix \(A_\delta-E\), square-zero is equivalent to determinant zero. Direct computation gives
\[
\det(A_\delta-E)=\delta(1-v)+u-s;
\]
so \(u=s-\delta+\delta v\). The remaining equation \(\det E=0\) is precisely
\[
C_\delta:\quad s^2+sv+\delta v^2-s-\delta v=0.
\]
Conversely every \((s,v)\in C_\delta(F)\) produces a unique decomposition. Therefore \(h_q(A)=\# C_\delta(F)\).

**Step 3: conic geometry and point counts.** If \(\delta=0\), then \(C_0\) has equation \(s(s+v-1)=0\): it is the union of two affine lines with exactly one intersection, hence has \(2q-1\) points. If \(\delta\ne0\), its projective closure has homogeneous equation
\[
\widehat C_\delta:\quad s^2+sv+\delta v^2-sw-\delta vw=0.
\]
It contains the rational point \([0:0:1]\). It is nonsingular over every algebraic closure: a simultaneous zero of all partial derivatives has \(s=-\delta v\) and \(w=v\), and then the equation yields \(\delta^2v^2=0\), forcing \(s=v=w=0\), impossible projectively. A smooth projective conic containing a rational point is isomorphic over \(F\) to \(\mathbb P^1\); thus it has exactly \(q+1\) rational points. At infinity the equation is \(s^2+sv+\delta v^2=0\). Every point at infinity has \(v\ne0\), and \(t=-s/v\) is a root of \(t^2-t+\delta\). There are exactly \(r(A)\) distinct rational points at infinity. Hence \(\# C_\delta(F)=q+1-r(A)\). The same argument includes characteristic two.

**Step 4: histogram.** The nilpotent matrices in \(M_2(F)\) are exactly \(q^2\) matrices, and their translates by \(I\) are disjoint: these contribute \(2q^2\) matrices with fiber size one. For fixed trace one and determinant \(\delta\), a non-scalar matrix is cyclic. Its conjugacy class has size \(q(q+1)\) for a split squarefree characteristic polynomial, \(q(q-1)\) for an irreducible quadratic, and \(q^2-1\) for a repeated root; in the last case there is also exactly one scalar matrix, whose fiber is zero. For odd \(q\), \(\delta=0\) is split squarefree; among \(\delta\ne0\), there are \((q-3)/2\) split squarefree values, \((q-1)/2\) irreducible values, and one repeated-root value. For even \(q\), among \(\delta\ne0\) there are \(q/2-1\) split squarefree values and \(q/2\) irreducible values, with no repeated roots because the derivative of \(t^2-t+\delta\) is nonzero. Multiply each parameter count by the corresponding conjugacy-class size and put its contribution at exponent \(2q-1\), \(q-1\), \(q+1\), or \(q\), respectively. Add the \(2q^2\) singleton-fiber matrices and subtract the resulting nonzero-fiber count from \(q^4\) to obtain both displayed polynomials, including their constant terms. The largest fiber is \(2q-1\), achieved by any rank-one idempotent \(A\) (trace one, determinant zero). For \(q\ge3\), the other positive fiber sizes are at most \(q+1\le2q-1\); equality at \(q=2\) is harmless. This proves the stated nil-clean index and distribution.

## Verification
The accompanying standard-library Python program `nil_clean_fibers_checker.py` exhaustively enumerates all matrices and idempotents for fields of sizes \(2,3,4,5,7,8,9,11\), including nonprime finite fields via explicit quotient-polynomial arithmetic. It compares every individual fiber with the theorem, every histogram with the closed formulas, and every conic point count. The executed output ended `NIL_CLEAN_FIBER_EXHAUSTIVE_OK`. These finite computations are independent checks of bounded cases; the proof above establishes all prime powers.

## Relationship to prior work
Basnet and Bhattacharyya defined the nil-clean index and proved the general lower bound \(\operatorname{Nin}(M_n(S))\ge2|S|^{n-1}-1\); their Proposition 4.4 evaluates the \(2\)-element field case. For \(n=2\), the present exact value matches and sharpens that bound over **every** finite field and determines the full fiber geometry and histogram. Breaz, Călugăreanu, Danchev and Micu characterize **when the entire matrix algebra is nil-clean**, not how many decompositions an individual nil-clean matrix has. Cîmpean and Danchev study the **weakly** nil-clean index and analyze special \(2\times2\) cases, including the weakly nil-clean index over \(\mathbb F_3\); this is a different counting invariant. The earlier \(\mathbb F_2\) nil-clean index and its special-case counts are not presented as new.

## Limitations
This theorem only concerns \(2\times2\) matrices over finite fields and additive idempotent-plus-nilpotent decompositions. It does not treat higher dimensions, general finite rings, multiplicative idempotent–nilpotent factorizations, commuting (strongly nil-clean) summands, or weakly nil-clean sums. Smoothness refers to the projective conic over the field when \(\delta\ne0\), not to any family scheme across the parameter \(\delta\). Computational evidence only exhausts the listed finite fields; independently confirmed publication priority is not claimed.

## References
1. S. Breaz, G. Călugăreanu, P. Danchev and T. Micu, *Nil-clean matrix rings*, arXiv:1310.0416 (public preprint, 2013-10-01), https://arxiv.org/abs/1310.0416.
2. D. K. Basnet and J. Bhattacharyya, *Nil clean index of rings*, International Electronic Journal of Algebra **15** (2014), 145–156, Proposition 4.4, https://www.ieja.net/files/papers/volume-15/12-V15-2014.pdf; DOI: 10.24330/ieja.266244.
3. A. Cîmpean and P. Danchev, *Weakly nil-clean index and uniquely weakly nil-clean rings*, International Electronic Journal of Algebra **21** (2017), https://www.ieja.net/files/papers/volume-21/12-V21-2017.pdf.
4. T. Schoonmaker, *Clean Indices of Common Rings* (2018), https://scholarsarchive.byu.edu/etd/7027/ (abstract consulted; full dissertation unavailable for comparison).
