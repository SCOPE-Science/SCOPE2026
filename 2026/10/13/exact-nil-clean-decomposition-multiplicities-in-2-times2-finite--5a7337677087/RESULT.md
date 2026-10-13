# Exact nil-clean decomposition multiplicities in \(2\times2\) finite-field matrix rings

## Finding
For a prime power \(q\), define the nil-clean decomposition multiplicity of \(A\in M_2(\mathbb F_q)\) by
\[
\nu(A)=\#\{E\in M_2(\mathbb F_q):E^2=E\text{ and }A-E\text{ is nilpotent}\}.
\]
Let \(e(A)\) be the number of \(A\)-invariant projective lines in \(\mathbb P^1(\mathbb F_q)\). Then
\[
\boxed{\nu(A)=\mathbf 1_{A\text{ nilpotent}}+\mathbf 1_{A-I\text{ nilpotent}}+\mathbf 1_{\operatorname{tr}A=1}\bigl(q+1-e(A)+q\,\mathbf 1_{\det A=0}\bigr).}
\]
This gives an elementwise multiplicity law, not only an existence criterion.

Consequently, every nilpotent matrix and every matrix \(I+N\) with \(N\) nilpotent has a unique nil-clean decomposition. Every other nil-clean matrix has trace \(1\). In odd characteristic the sole trace-one matrix with no nil-clean decomposition is \(\tfrac12 I\); in characteristic two there is no scalar trace-one matrix. Hence
\[
\#\{A:\nu(A)>0\}=
\begin{cases}
q^3+2q^2,&q\text{ even},\\
q^3+2q^2-1,&q\text{ odd}.
\end{cases}
\]
For \(q=2\), this equals \(16\), recovering the exceptional fact that all of \(M_2(\mathbb F_2)\) is nil-clean while also resolving the number of decompositions element by element.

Within the trace-one hyperplane the exact profile is as follows. Distinct rows may yield the same numerical multiplicity at small \(q\) (notably \(q=2\)).

| trace-one type | \(\nu(A)\) | number of matrices |
|---|---:|---:|
| \(\det A=0\) | \(2q-1\) | \(q(q+1)\) |
| split, two distinct nonzero eigenvalues; \(q\) even | \(q-1\) | \(q(q+1)(q-2)/2\) |
| split, two distinct nonzero eigenvalues; \(q\) odd | \(q-1\) | \(q(q+1)(q-3)/2\) |
| nonscalar repeated root; \(q\) odd | \(q\) | \(q^2-1\) |
| irreducible characteristic polynomial; \(q\) even | \(q+1\) | \(q^2(q-1)/2\) |
| irreducible characteristic polynomial; \(q\) odd | \(q+1\) | \(q(q-1)^2/2\) |
| scalar \(\tfrac12 I\); \(q\) odd | \(0\) | \(1\) |

## Assumptions and scope
The field is the finite field \(\mathbb F_q\), with \(q\) an arbitrary prime power. Nil-clean means a decomposition \(A=E+N\) with \(E^2=E\) and \(N\) nilpotent; commutation of \(E\) and \(N\) is not required. The theorem is specific to \(2\times2\) matrices. The invariant \(e(A)\) counts projective eigenlines over the ground field, so it equals \(q+1\) for scalar matrices, \(2\) for split semisimple nonscalars, \(1\) for a nonscalar repeated-root Jordan class, and \(0\) for irreducible characteristic polynomial.

## Proof
Every idempotent in \(M_2(\mathbb F_q)\) has rank \(0\), \(1\), or \(2\). Rank \(0\) contributes exactly when \(A\) is nilpotent, via \(E=0\). Rank \(2\) contributes exactly when \(A-I\) is nilpotent, via \(E=I\).

Now take a rank-one idempotent \(E\). Then \(\operatorname{tr}E=1\) and \(\det E=0\). If \(A-E\) is nilpotent, then necessarily \(\operatorname{tr}A=1\). Conversely, assume \(\operatorname{tr}A=1\). A \(2\times2\) matrix is nilpotent exactly when its trace and determinant vanish, so \(A-E\) is nilpotent exactly when \(\det(A-E)=0\). Using \(\operatorname{adj}(A)=\operatorname{tr}(A)I-A\),
\[
\det(A-E)=\det A-1+\operatorname{tr}(AE).
\]
Thus, with \(d=\det A\) and \(c=1-d\), the rank-one contribution is the number of rank-one idempotents satisfying \(\operatorname{tr}(AE)=c\).

Write a rank-one idempotent as \(E=u\varphi\), where \(u\ne0\), \(\varphi(u)=1\), and two pairs differing by \(u\mapsto au\), \(\varphi\mapsto a^-1\varphi\) represent the same idempotent. Fix the image line \(L=\langle u\rangle\). The condition becomes \(\varphi(Au)=c\).

If \(L\) is not \(A\)-invariant, then \(u,Au\) form a basis, so there is exactly one functional \(\varphi\) with \(\varphi(u)=1\) and \(\varphi(Au)=c\). Hence each noninvariant line contributes exactly one idempotent.

If \(L\) is invariant with eigenvalue \(\lambda\), then \(\varphi(Au)=\lambda\) for every \(\varphi\) satisfying \(\varphi(u)=1\). There are exactly \(q\) such rank-one idempotents with image \(L\), and they all qualify exactly when \(\lambda=c\). Therefore the rank-one contribution is
\[
q+1-e(A)+q m_c,
\]
where \(m_c\) is the number of invariant lines carrying eigenvalue \(c\). Because \(\operatorname{tr}A=1\), the characteristic polynomial is \(t^2-t+d\). Substitution of \(c=1-d\) gives
\[
c^2-c+d=d^2.
\]
Hence \(c\) is an eigenvalue exactly when \(d=0\). In that case the eigenvalues are \(0\) and \(1\), so exactly one invariant line carries \(c=1\). Thus \(m_c=\mathbf 1_{d=0}\), proving the boxed formula.

For the census, there are \(q^2\) nilpotent \(2\times2\) matrices: zero plus \((q+1)(q-1)=q^2-1\) nonzero rank-one nilpotents. Translation by \(I\) gives another disjoint family of \(q^2\) matrices. The trace-one hyperplane has \(q^3\) matrices. Every nonscalar trace-one matrix has at most two invariant lines and hence positive rank-one contribution; in odd characteristic the unique scalar trace-one matrix is \(\tfrac12 I\), for which \(e(A)=q+1\) and the contribution is zero. This yields the stated locus sizes.

The finer class counts are standard \(2\times2\) similarity counts. The determinant-zero trace-one class is the conjugacy class of \(\operatorname{diag}(0,1)\), of size \(q(q+1)\). Each split distinct-eigenvalue class has size \(q(q+1)\); the number of unordered nonzero pairs \(\{\lambda,1-\lambda}\) is \((q-2)/2\) for even \(q\) and \((q-3)/2\) for odd \(q\). In odd characteristic the single repeated-root polynomial gives one nonscalar Jordan class of size \(q^2-1\). Each irreducible quadratic trace-one class has size \(q(q-1)\); there are \(q/2\) such polynomials for even \(q\) and \((q-1)/2\) for odd \(q\). These numbers sum to \(q^3\) in each parity.

## Verification
The accompanying `verify.py` exhaustively enumerates all matrices and all idempotents over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_5\), and \(\mathbb F_7\), and independently over \(\mathbb F_4\) using a direct polynomial-basis implementation. It checks the boxed formula for every matrix and checks the predicted trace-one type census and total nil-clean locus. This finite computation tests representative odd, even, prime, and nonprime prime-power fields; the proof above supplies the argument for all prime powers.

## Relationship to prior work
Breaz, Călugăreanu, Danchev, and Micu proved the ring-level theorem that \(M_n(K)\) is nil-clean for some positive \(n\) exactly when the field \(K\) is \(\mathbb F_2\). Their paper gives constructive decompositions in the binary case, but not an elementwise multiplicity profile over arbitrary finite fields.

Rajeswari and Gupta later gave necessary and sufficient conditions for a \(2\times2\) matrix over an integral domain to be nil-clean. Their Theorem 3.1 reduces nontrivial nil-cleanness to a trace-one condition plus solvability of equations describing a rank-one idempotent. That result is an existence characterization; it does not count the admissible idempotents, does not specialize the count to finite fields, and does not give the finite-field census above. The present proof uses projective image lines to count all solutions exactly.


## Limitations
No claim is made for \(n>2\), where the geometry of idempotent ranks and nilpotent Jordan types is substantially richer. The computational checks are finite tests and are not used as an infinite proof. The 2018 integral-domain characterization is close prior work for existence; originality here is the exact finite-field multiplicity formula, its class-by-class profile, and the resulting locus count. A residual literature risk is that an exact finite-field count may have appeared under different terminology not surfaced by the searches; no such source was found in the inspected literature or published-finding corpus comparisons.

## References
1. S. Breaz, G. Călugăreanu, P. Danchev, T. Micu, “Nil-clean matrix rings,” arXiv:1310.0416v1 (1 October 2013); later Linear Algebra and its Applications 439 (2013), 3115–3119, DOI 10.1016/j.laa.2013.08.027.
2. M. T. Koşan, T. K. Lee, Y. Zhou, “When is every matrix over a division ring a sum of an idempotent and a nilpotent?”, Linear Algebra and its Applications 450 (2014), 7–12, DOI 10.1016/j.laa.2014.02.047.
3. K. N. Rajeswari, U. Gupta, “Characterization of \(2\times2\) nil-clean matrices over integral domains,” Journal of Algebra Combinatorics Discrete Structures and Applications 5 (2018), 117–127, DOI 10.13069/jacodesmath.451229.
