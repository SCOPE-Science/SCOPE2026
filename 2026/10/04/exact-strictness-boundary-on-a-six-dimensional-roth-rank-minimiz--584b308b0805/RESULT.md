# Exact strictness boundary on a six-dimensional Roth rank-minimization cell
## Finding
Let \(K\) be any field, \(A=J_2(0)\oplus J_1(0)\), and
\[
C=\begin{pmatrix}a&p&q\\0&b&0\\0&r&c\end{pmatrix}\in K^{3\times3}.
\]
Put \(\tau=a+b\) and \(\kappa=c\). For the Lin--Wimmer quantities \(\alpha(A,A,C)=\min_X\operatorname{rank}(AX-XA-C)\) and \(\gamma(A,A,C)=\min_{P\in\mathrm{GL}_6(K)}\operatorname{rank}(PM_C-M_0P)\), one has \(\gamma=0\) exactly when \((\tau,\kappa)=(0,0)\), and \(\gamma=1\) otherwise; while \(\alpha=0\) when \((\tau,\kappa)=(0,0)\), \(\alpha=1\) when exactly one of \(\tau,\kappa\) is nonzero, and \(\alpha=2\) when \(\tau\kappa\ne0\). Hence strict rank minimization occurs exactly on \(\tau\kappa\ne0\). Over \(\mathbb F_q\), exactly \(q^4(q-1)^2\) of the \(q^6\) matrices in this cell are strict.

This gives a complete boundary, over every field, for the natural linear cell \(\operatorname{Diag}_3(K)+\operatorname{im}(X\mapsto AX-XA)\). In particular, the isolated matrix used in the recent counterexample belongs to a Zariski-open strict locus in this cell rather than being an exceptional point.

## Assumptions and scope
Let \(K\) be an arbitrary field; no characteristic assumption is used. Set \(A=J_2(0)\oplus J_1(0)\). The cell considered is precisely the set of matrices
\[
C=\begin{pmatrix}a&p&q\\0&b&0\\0&r&c\end{pmatrix}.
\]
For \(M_C=\begin{pmatrix}A&C\\0&A\end{pmatrix}\) and \(M_0=\begin{pmatrix}A&0\\0&A\end{pmatrix}\), define
\[
\alpha=\min_{X\in K^{3\times3}}\operatorname{rank}(AX-XA-C),\qquad
\gamma=\min_{P\in\mathrm{GL}_6(K)}\operatorname{rank}(PM_C-M_0P).
\]

## Proof
Write \(\delta(X)=AX-XA\). Direct multiplication gives
\[
\delta(X)=\begin{pmatrix}
x_{21}&-x_{11}+x_{22}&x_{23}\\
0&-x_{21}&0\\
0&-x_{31}&0
\end{pmatrix}.
\]
Choosing \(x_{21}=-b\), \(-x_{11}+x_{22}=p\), \(x_{23}=q\), and \(-x_{31}=r\) gives
\[
C-\delta(X)=\operatorname{diag}(\tau,0,\kappa),\qquad \tau=a+b,\quad \kappa=c.
\]
Replacing \(C\) by \(C-\delta(X)\) leaves both minima unchanged. For \(\alpha\), this is the change of variable in the Sylvester residual. For \(\gamma\), if \(S=\begin{pmatrix}I&X\\0&I\end{pmatrix}\), then \(M_{C-\delta(X)}=SM_CS^{-1}\); substituting \(Q=PS^{-1}\) shows that the ranks minimized in \(\gamma\) are unchanged.

It therefore suffices to take \(C=\operatorname{diag}(\tau,0,\kappa)\). The residual has columns
\[
\begin{pmatrix}x_{21}-\tau\\0\\0\end{pmatrix},\quad
\begin{pmatrix}x_{22}-x_{11}\\-x_{21}\\-x_{31}\end{pmatrix},\quad
\begin{pmatrix}x_{23}\\0\\-\kappa\end{pmatrix}.
\]
If \(\tau\kappa\ne0\) and the rank were at most one, the nonzero third column would force the first column to be zero, hence \(x_{21}=\tau\); the second column would then have nonzero second coordinate \(-\tau\), while every multiple of the third column has second coordinate zero, a contradiction. Thus \(\alpha\ge2\), and \(X=0\) gives \(\alpha\le2\). If exactly one of \(\tau,\kappa\) is nonzero, the canonical \(C\) has rank one, so \(\alpha\le1\), while \(\alpha=0\) is impossible because \(\tau\) and \(\kappa\) are invariants of \(C\) modulo \(\operatorname{im}\delta\). If both vanish, \(\alpha=0\). This proves the formula for \(\alpha\).

For \(\gamma\), Roth's theorem gives \(\gamma=0\) exactly when \(\alpha=0\). Hence \(\gamma=1\) automatically in the cases with \(\alpha=1\). Suppose now \(\tau\kappa\ne0\). The invertible diagonal matrix \(T=\operatorname{diag}(\tau,\tau,\kappa)\) commutes with \(A\), so conjugation by \(\operatorname{diag}(I_3,T)\) reduces \(\operatorname{diag}(\tau,0,\kappa)\) to \(\operatorname{diag}(1,0,1)\) without changing \(\gamma\). For that normalized matrix, the explicit invertible matrix
\[
P_0=\begin{pmatrix}
1&0&0&0&0&0\\
0&1&0&1&0&0\\
0&0&0&0&1&0\\
0&0&1&0&0&0\\
0&0&0&0&0&1\\
0&1&0&0&0&0
\end{pmatrix}
\]
has determinant \(1\) and makes \(P_0M_C-M_0P_0\) rank one. Thus \(\gamma\le1\); it cannot be zero because \(\alpha=2\). Hence \(\gamma=1\).

Over \(\mathbb F_q\), the three off-diagonal free entries contribute \(q^3\) choices, the pair \((a,b)\) has \(q(q-1)\) choices with \(a+b\ne0\), and \(c\) has \(q-1\) nonzero choices, giving \(q^4(q-1)^2\) strict matrices.

## Verification
The proof is field-independent and uses only explicit matrix identities, rank-one linear dependence, and Roth's zero-case equivalence. The accompanying `verify.py` exhausts the four effective residual variables for every \((\tau,\kappa)\) over \(\mathbb F_2,\mathbb F_3,\mathbb F_5,\mathbb F_7\), and separately checks that \(P_0\) is invertible and has rank-one intertwiner defect in each field. It prints `VERIFY_OK primes=2,3,5,7`.

## Relationship to prior work
Shi, Zhang, and Zhang (arXiv:2609.07113v1, 7 September 2026) give the single normalized point \(A=J_2(0)\oplus J_1(0)\), \(C=\operatorname{diag}(1,0,1)\), proving \(\alpha=2\) and \(\gamma=1\) over every field. They prove dimensional minimality over \(\mathbb C\) and explicitly leave a more precise characterization of strictness as a natural remaining problem. The result here classifies the entire six-dimensional linear cell containing their point and gives its exact equality/strictness boundary. Ferrante and Wimmer's 2013 sufficient spectral theorem does not cover this Jordan type: its repeated zero eigenvalue is neither semisimple nor nonderogatory, as the 2026 paper also observes.

## Limitations
This does not classify all \(C\in K^{3\times3}\); three quotient coordinates, represented by the entries \(c_{21},c_{23},c_{31}\), are fixed to zero in the present cell. No claim is made about dimensional minimality over fields other than \(\mathbb C\). The literature search did not locate an equivalent published classification, but absence from the searched sources is not a proof of novelty; in particular, the full text of the 2013 Ferrante--Wimmer article was not available in the inspected open sources.

## References
1. S. Shi, J. Zhang, Y. Zhang, *A \(3\times3\) counterexample to Lin and Wimmer's rank-minimization conjecture associated with Roth's similarity theorem*, arXiv:2609.07113v1, 2026, DOI 10.48550/arXiv.2609.07113.
2. A. Ferrante, H. K. Wimmer, *Roth's similarity theorem and rank minimization in the presence of nonderogatory or semisimple eigenvalues*, Linear and Multilinear Algebra 61 (2013), 217--231, DOI 10.1080/03081087.2012.672570.
3. M. Lin, H. K. Wimmer, *The generalized Sylvester matrix equation, rank minimization and Roth's equivalence theorem*, Bulletin of the Australian Mathematical Society 84 (2011), 441--443, DOI 10.1017/S0004972711002334.
