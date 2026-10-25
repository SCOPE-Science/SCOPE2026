# A bounded three-level self-adjoint semigroup with no positive operator time on ℓ²

## Finding
On the real coordinate Hilbert lattice \(H=\ell^2(\mathbb N;\mathbb R)\) there exists a bounded, self-adjoint, nonpositive generator \(A\), with spectrum exactly \(\{0,-1,-2\}\) and a simple dominant eigenvalue \(0\) whose normalized eigenvector has strictly positive coordinates, such that:

1. For every two fixed coordinates \(i,j\), the coefficient \(\langle e^{tA}e_j,e_i\rangle\) is strictly positive for all sufficiently large \(t\) (and every diagonal coefficient is strictly positive for all \(t\ge0\));
2. For every fixed \(t>0\), at least one coefficient is negative, so \(e^{tA}\) is **not** a positive operator;
3. Nevertheless \(e^{tA}\to P\) in operator norm, where \(P\) is a rank-one orthogonal projection with every matrix coefficient strictly positive.

Thus \(\{t\ge0:e^{tA}\ge0\}=\{0\}\), despite a three-point spectrum, a strictly positive dominant eigenvector, norm convergence to a strictly positive-coefficient projection, and eventual positivity of every individual matrix coefficient. The theorem is an existence statement on a countable coordinate Hilbert lattice; it does not claim that all positive initial vectors become eventually positive.

## Explicit operator
For \(k\ge1\), put
\[
c_k=\sqrt{\frac32}\,2^{-k},\qquad
v_{2k-1}=v_{2k}=c_k,\qquad
q_k=\frac{e_{2k-1}-e_{2k}}{\sqrt2}.
\]
The vector \(v\) is strictly positive and has norm one, since
\(\sum_{k\ge1}2c_k^2=3\sum_{k\ge1}4^{-k}=1\). The \(q_k\) form an orthonormal family perpendicular to \(v\). Define the orthogonal projections
\[
P_1=v\otimes v,\qquad
P_2=\sum_{k\ge1}q_k\otimes q_k,\qquad
P_3=I-P_1-P_2,
\]
where the sum converges in the strong operator topology, and put
\[
\boxed{A=-P_2-2P_3.}
\]
Here \((x\otimes y)z=x\langle y,z\rangle\). All three mutually orthogonal projections are nonzero: \(P_1\) has rank one, \(P_2\) infinite rank, and \(P_3\) contains symmetric pair vectors perpendicular to \(v\). Thus \(A\) is bounded, real, self-adjoint and nonpositive; \(\|A\|=2\), and \(\sigma(A)=\{0,-1,-2\}\) with the claimed simple top eigenspace.

## Proof of the three assertions
Functional calculus gives, for every real \(t\ge0\),
\[
e^{tA}=P_1+e^{-t}P_2+e^{-2t}P_3
=e^{-2t}I+(1-e^{-2t})P_1+(e^{-t}-e^{-2t})P_2.
\tag{1}
\]
For \(i\ne j\) not belonging to the same adjacent pair \(\{2k-1,2k\}\), the \(P_2\) coefficient vanishes and (1) gives
\[
\langle e^{tA}e_j,e_i\rangle=(1-e^{-2t})v_iv_j>0\quad(t>0).
\]
For the paired indices \(i=2k-1,j=2k\), the \(P_2\) coefficient is \(-1/2\), so
\[
\langle e^{tA}e_{2k},e_{2k-1}\rangle
=(1-e^{-2t})\left(c_k^2-\frac{1}{2(1+e^t)}\right).
\tag{2}
\]
For each fixed \(k\), the bracket in (2) increases strictly to \(c_k^2>0\) as \(t\to\infty\). In fact, for \(k\ge2\), it vanishes exactly at
\[
\tau_k=\log\left(\frac{1}{2c_k^2}-1\right)
=\log\left(\frac{4^k}{3}-1\right),
\tag{3}
\]
whereas for \(k=1\) it is already positive for every \(t>0\). The diagonal coefficients in (1) are positive for all times, by the spectral resolution \(\langle e^{tA}e_i,e_i\rangle=\sum_{r=1}^3e^{\lambda_rt}\|P_re_i\|^2>0\). This proves assertion 1.

At any fixed \(t>0\), \(c_k^2=(3/2)4^{-k}\to0\), while \(1/(2(1+e^t))>0\). Choose \(k\) so that \(c_k^2<1/(2(1+e^t))\); then (2) is strictly negative. Since \(e_{2k}\) is a positive vector, its image has a negative coordinate, so \(e^{tA}\) is not cone-preserving. At \(t=0\) the identity is positive. Equivalently, \(\tau_k\to\infty\), and the pairwise eventual-positivity thresholds admit no uniform finite bound. This proves assertion 2.

Finally (1) and orthogonality yield
\[
\|e^{tA}-P_1\|=e^{-t}\quad(t\ge0),
\]
while \(\langle P_1e_j,e_i\rangle=v_iv_j>0\) for every pair. The coordinate entries of this strictly positive-coefficient limit have no uniform strictly positive lower bound, which is why operator-norm convergence does not force positivity of the approximants. This proves assertion 3 and the theorem.

## Relationship to established mathematics
Johnson, Lins and Walch [1, Theorem 5.3] proved in 2010 that continuous conventional powers of a **finite** doubly nonnegative matrix with at most three spectral values remain doubly nonnegative at every exponent at least one. Applying their theorem to \(B=e^{t_0A}\) shows that if a finite-dimensional three-spectral self-adjoint exponential is positive at \(t_0>0\), it remains positive for every later time. Consequently a finite-dimensional three-level no-gap law is **not** claimed as new here. The earlier manuscript version of this record included that law and a four-point path-power illustration; those broader claims are excluded from the corrected finding because the relevant finite-dimensional mechanism was already available. The original versions remain in the source history.

Daners, Glück and Kennedy [2, Example 5.7] already exhibited a **bounded three-spectrum** generator on \(C([-1,1])\) whose semigroup is individually eventually strongly positive but is not uniformly eventually positive; their Example 5.8 treats a compact-resolvent \(C(K)\) space. These examples establish the general phenomenon and motivate the present Hilbert-lattice realization. Their ordered Banach space is different and their generator is not a self-adjoint operator on coordinate \(\ell^2\) with the explicitly prescribed orthogonal pair projections (1)–(3). The phenomenon of nonuniformity itself is **not** claimed as new.

Dobrick [3] constructed self-adjoint, compact-resolvent eventually positive semigroups on coordinate Hilbert spaces; the generators have unbounded spectra. An independently published analysis [4] of Dobrick's construction supplies an all-positive-time nonpositivity witness. Because an infinite-dimensional compact-resolvent generator cannot have this bounded three-point spectrum, these results do not mathematically entail the present spectral-minimal bounded witness. A close unindexed analogue or an elementary adaptation of [2] is nevertheless a genuine priority risk.

Guillot, Khare and Rajaratnam [5] proved the critical exponent for arbitrary doubly nonnegative matrices; its finite-dimensional conclusion and associated path examples are prior work, not a component of this corrected finding.

## Verification and limitations
The proof uses exact projection identities, the convergent geometric norm formula, and the sign of (2), not a finite experiment. The original accompanying `verify_spectral_times.py` remains as a historical arithmetic consistency check for the original broader package and is **not** a certificate for the new infinity-of-coordinates assertion. The three eigenvalues and exact norm convergence are proved above. This example does not have compact resolvent and no uniform lower bound on the matrix coefficients of its leading projection; the stronger property of individual eventual strong positivity for **every** nonzero positive initial vector is not asserted.

## References
[1] C. R. Johnson, B. Lins and O. Walch, *The critical exponent for continuous conventional powers of doubly nonnegative matrices*, arXiv:1008.3568, Theorem 5.3, https://arxiv.org/abs/1008.3568 .

[2] D. Daners, J. Glück and J. B. Kennedy, *Eventually positive semigroups of linear operators*, J. Math. Anal. Appl. 433 (2016), 1561–1593, Examples 5.7–5.8; arXiv:1511.09020, https://arxiv.org/abs/1511.09020 .

[3] A. Dobrick, *Individual and Uniform Eventual Positivity of Self-Adjoint Semigroups*, arXiv:2609.00425, https://arxiv.org/abs/2609.00425 .

[4] *Only time zero is positive for a compact-resolvent self-adjoint eventually positive semigroup*, published mathematical record (2026-10-11), https://github.com/Resultary/2026/tree/main/2026/10/11/SCOPE-only-time-zero-is-positive-for-a-compact-resolvent-self-adjoint--a48e4f5dd463 .

[5] D. Guillot, A. Khare and B. Rajaratnam, *The critical exponent conjecture for powers of doubly nonnegative matrices*, arXiv:1303.4701, https://arxiv.org/abs/1303.4701 .
