# Exact minimal dimensions for power-quasinormality index sets
## Finding
For \(T\in M_N(\mathbb C)\), define
\[
\mathcal{PQ}(T)=\{n\in\mathbb N:[T^n,T^*T]=0\}.
\]
For positive integers \(d,q\), let \(\mu(d,q)\) be the least positive integer \(N\) for which some \(T\in M_N(\mathbb C)\) satisfies
\[
\mathcal{PQ}(T)=\{d(q+k):k\in\mathbb N_0\}.
\]
Then
\[
\mu(1,1)=1,
\]
\[
\mu(1,q)=q\quad(q\ge2),
\]
\[
\mu(d,1)=2\quad(d\ge2),
\]
and
\[
\mu(d,q)=(q-1)d+3\quad(d,q\ge2).
\]
Thus the complete arithmetic-tail classification of power-quasinormality index sets has an exact finite-dimensional realization cost.

## Assumptions and scope
All Hilbert spaces are finite-dimensional complex Hilbert spaces, equivalently the operators are complex square matrices. The integer \(N\) is required to be positive. The definition of \(n\)-power quasinormality is \([T^n,T^*T]=0\). No assertion is made about minimal dimension for infinite-dimensional realizations, real matrices, or other generalized-normality classes.

## Proof
Zhou and Yang prove that every nonempty power-quasinormality index set has the unique form
\[
\{d(q+k):k\in\mathbb N_0\},
\]
and provide two elementary building blocks. For \(d\ge2\), their matrix
\[
S_d=\begin{bmatrix}1&1\\0&\omega_d\end{bmatrix},
\qquad \omega_d=e^{2\pi i/d},
\]
satisfies \(\mathcal{PQ}(S_d)=d\mathbb N\). The nilpotent Jordan block \(J_r\) of order \(r\) satisfies
\[
\mathcal{PQ}(J_r)=\{k\in\mathbb N:k\ge r\}.
\]
The latter is the same calculation used in their Example 3.9, with the block order renamed from \(dq\) to an arbitrary \(r\): for \(1\le k<r\), applying the commutator to the \((k+1)\)-st standard basis vector gives a nonzero vector, while \(J_r^k=0\) for \(k\ge r\).

For the upper bounds, \(\mu(1,1)\le1\) follows from any scalar matrix. If \(q\ge2\), then \(J_q\) realizes \(\{q,q+1,\ldots\}\), so \(\mu(1,q)\le q\). If \(d\ge2\), then \(S_d\) realizes \(d\mathbb N\), so \(\mu(d,1)\le2\). Finally, let \(d,q\ge2\) and put
\[
r=(q-1)d+1.
\]
By the direct-sum identity for power-quasinormality index sets,
\[
\mathcal{PQ}(S_d\oplus J_r)
=d\mathbb N\cap\{k:k\ge r\}
=\{dq,d(q+1),d(q+2),\ldots\}.
\]
Hence \(\mu(d,q)\le(q-1)d+3\).

For the lower bounds, suppose \(T\in M_N(\mathbb C)\) realizes the target set and put \(m=dq\), its least element. Since \(m\in\mathcal{PQ}(T)\), Zhou and Yang's finite-dimensional equivalence implies that \(T^m\) is normal. Their Proposition 2.4 gives, relative to
\[
\mathbb C^N=\operatorname{ran}T^m\oplus\ker (T^*)^m,
\]
a block form
\[
T=\begin{bmatrix}A&X\\0&B\end{bmatrix},
\]
where \(A\) is injective, \(A^*X=0\), and \(B^m=0\). In finite dimension \(A\) is invertible, so \(A^*\) is invertible and therefore \(X=0\). Thus
\[
T=A\oplus B,
\]
with \(A\) invertible and \(B\) nilpotent.

Because \(A\) is injective and has a nonempty index set, subtraction and addition closure imply
\[
\mathcal{PQ}(A)=e\mathbb N
\]
for some positive integer \(e\). Since \(B^m=0\), every \(k\ge m\) belongs to \(\mathcal{PQ}(B)\), so for all \(k\ge m\), membership in \(\mathcal{PQ}(T)\) is the same as membership in \(\mathcal{PQ}(A)\). The target tail is exactly the multiples of \(d\); two sets of positive multiples that agree from some point onward have the same generator. Hence \(e=d\).

If \(d\ge2\), the invertible sector \(A\) has dimension at least \(2\), because every one-dimensional operator is scalar and has power-quasinormality index set \(\mathbb N\). If also \(q\ge2\), then \((q-1)d\in\mathcal{PQ}(A)\) but \((q-1)d\notin\mathcal{PQ}(T)\). Therefore \((q-1)d\notin\mathcal{PQ}(B)\). If \(B^{(q-1)d}=0\), that exponent would automatically belong to \(\mathcal{PQ}(B)\), a contradiction. Thus
\[
B^{(q-1)d}\ne0.
\]
A nilpotent operator on an \(s\)-dimensional space satisfies \(B^s=0\), so the nilpotent sector has dimension at least \((q-1)d+1\). Consequently
\[
N\ge2+(q-1)d+1=(q-1)d+3.
\]
This matches the construction.

If \(d=1\) and \(q\ge2\), the same argument shows that the injective sector, if nonzero, has index set \(\mathbb N\). Since \(q-1\) is excluded from the target, the nilpotent sector must satisfy \(B^{q-1}\ne0\), hence it alone has dimension at least \(q\). Thus \(N\ge q\), matching \(J_q\). If \(d\ge2\) and \(q=1\), no one-dimensional matrix can realize \(d\mathbb N\), while \(S_d\) does so in dimension \(2\). The case \(d=q=1\) is immediate.

## Verification
The proof is symbolic and uses only the cited structural statements plus elementary finite-dimensional linear algebra. The boundary cases \(d=1\) and \(q=1\) are treated separately, so the formula does not silently apply a nonexistent periodic or nilpotent sector. The key lower-bound implication is one-way and exact: if \(B^k=0\), then \(k\in\mathcal{PQ}(B)\); therefore an excluded exponent forces \(B^k\ne0\), which forces a nilpotency index exceeding \(k\). No finite experiment is used as proof.

## Relationship to prior work
Zhou and Yang characterize all nonempty power-quasinormality index sets and, in Example 3.9, realize the tail \(\{dq,d(q+1),\ldots\}\) using \(S_d\oplus J_{dq}\), of dimension \(dq+2\). Their paper does not state a minimal-dimension problem; the full text contains no occurrence of the word "minimal". The present result determines the optimum and, for \(d,q\ge2\), replaces the nilpotent block of order \(dq\) by the smallest possible cutoff block of order \((q-1)d+1\), lowering the construction size by \(d-1\) and proving that no further reduction is possible.

Ko and Lee study structural and local spectral properties of \(n\)-power quasinormal operators and operator matrices, but the inspected material does not formulate power-quasinormality index sets or a minimal realization dimension. Earlier work of Sid Ahmed introduces the class and related properties rather than this realization invariant.

## Limitations
The originality search did not identify an earlier equivalent minimal-dimension theorem, but older work on \(n\)-power normal matrices could conceivably encode the same lower bound in different terminology. The result is restricted to complex matrices. It does not classify all dimension-minimizing matrices up to unitary similarity; it determines only the exact minimum dimension.

## References
1. Jing-Bin Zhou and Shihai Yang, *Power quasinormal operators and the root problem*, arXiv:2609.09775v1, first posted 2026-09-09. Relevant items: Proposition 2.4, Theorem 2.10, Proposition 3.1, Theorem 3.3, Example 3.9.
2. Eungil Ko and Mee Jung Lee, *Remarks on n-power quasinormal operators*, Filomat 37 (2023), no. 11, 3371–3381, DOI: 10.2298/FIL2311371K.
3. Ould Ahmed Mahmoud Sid Ahmed, *On the class of n-power quasi-normal operators on Hilbert space*, Bulletin of Mathematical Analysis and Applications 3 (2011), no. 2, 213–228.
