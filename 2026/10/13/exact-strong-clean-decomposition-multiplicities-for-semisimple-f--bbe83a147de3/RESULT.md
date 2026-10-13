# Exact strong-clean decomposition multiplicities for semisimple finite-field matrices
## Finding
Let \(A\in M_n(\mathbb F_q)\) be semisimple. Factor its characteristic polynomial as
\[
\chi_A(t)=\prod_f f(t)^{m_f},
\]
where the product is over distinct monic irreducible polynomials \(f\in\mathbb F_q[t]\), and put \(d_f=\deg f\). For a prime power \(Q\), define
\[
H_Q(m)=\sum_{k=0}^{m}{m\brack k}_Q Q^{k(m-k)},
\]
where \({m\brack k}_Q\) is the Gaussian binomial coefficient.

The exact number \(s(A)\) of strongly clean decompositions
\[
A=E+U,\qquad E^2=E,\qquad U\in GL_n(\mathbb F_q),\qquad EU=UE,
\]
is
\[
s(A)=\prod_{f\notin\{t,t-1\}}H_{q^{d_f}}(m_f).
\]
On the \(t\)-primary summand the idempotent is forced to be the identity, and on the \(t-1\)-primary summand it is forced to be zero.

Two consequences are immediate. A semisimple matrix has a unique strongly clean decomposition exactly when \(A^2=A\). If \(A\) is regular semisimple and exactly \(s\) irreducible factors of \(\chi_A\) are different from \(t\) and \(t-1\), then \(s(A)=2^s\).

## Assumptions and scope
Semisimple means that the \(\mathbb F_q[t]\)-module obtained from the action of \(A\) is semisimple, equivalently that the minimal polynomial of \(A\) is squarefree. The theorem counts decompositions of a fixed matrix; it does not count semisimple similarity classes or all strongly clean matrices.

## Proof
A strongly clean decomposition is determined by its idempotent \(E\), because then \(U=A-E\). The condition \(EU=UE\) is equivalent to \(EA=AE\). Thus \(s(A)\) is the number of idempotents in the centralizer of \(A\) for which \(A-E\) is invertible.

Semisimplicity gives the primary decomposition
\[
V=\bigoplus_f V_f,
\qquad
V_f\cong K_f^{m_f},
\qquad
K_f=\mathbb F_q[t]/(f)\cong\mathbb F_{q^{d_f}}.
\]
Accordingly,
\[
\operatorname{End}_{\mathbb F_q[t]}(V)
\cong
\prod_f M_{m_f}(K_f).
\]
A commuting idempotent therefore decomposes as a tuple \((E_f)_f\). On \(\ker E_f\), the operator \(A-E_f\) equals \(A\), while on \(\operatorname{im}E_f\) it equals \(A-I\). If \(f=t\), then \(A\) vanishes on \(V_f\), so invertibility forces \(\ker E_f=0\), hence \(E_f=I\). If \(f=t-1\), then \(A-I\) vanishes on \(V_f\), so invertibility forces \(\operatorname{im}E_f=0\), hence \(E_f=0\). For every other irreducible \(f\), both \(A\) and \(A-I\) are invertible on \(V_f\), so every idempotent in \(M_{m_f}(K_f)\) is admissible.

It remains to count idempotents in \(M_m(\mathbb F_Q)\). A rank-\(k\) idempotent is uniquely determined by a direct-sum decomposition \(\mathbb F_Q^m=W\oplus Z\), where \(W\) is its image and \(Z\) its kernel. There are \({m\brack k}_Q\) choices for \(W\), and after fixing \(W\), there are \(Q^{k(m-k)}\) complements \(Z\). Hence the number of rank-\(k\) idempotents is
\[
{m\brack k}_Q Q^{k(m-k)},
\]
and summing over \(k\) gives \(H_Q(m)\). Multiplication over the independent primary factors proves the formula.

For every \(m\ge1\), \(H_Q(m)\ge2\), because both zero and the identity are idempotent. Therefore uniqueness occurs precisely when no irreducible factor other than \(t\) and \(t-1\) occurs. Under semisimplicity this is equivalent to the minimal polynomial dividing \(t(t-1)\), hence to \(A^2=A\). If \(A\) is regular semisimple, every \(m_f=1\), and each nonspecial factor contributes \(H_{q^{d_f}}(1)=2\), yielding \(2^s\).

## Verification
The accompanying checker exhaustively enumerates commuting idempotents and tests invertibility of \(A-E\) for representative matrices. It verifies
\[
H_3(2)=14,\qquad H_5(2)=32,\qquad H_4(2)=22,
\]
including scalar matrices over \(\mathbb F_3\) and \(\mathbb F_5\), a quadratic irreducible companion matrix over \(\mathbb F_2\), a doubled quadratic block in \(M_4(\mathbb F_2)\), and mixed \(0\)-, \(1\)-, and irreducible-primary summands. It also independently enumerates all idempotents of \(M_2(\mathbb F_4)\) and obtains \(22\).

## Relationship to prior work
The classical strong-cleanness literature characterizes existence of strongly clean decompositions. Chen, Yang and Zhou give criteria for \(2\times2\) matrices over commutative local rings. Borooah, Diesl and Dorsey give the invariant-summand characterization of strongly clean endomorphisms and broad factorization criteria for matrix rings over commutative local rings. A later paper on uniquely strongly clean triangular matrix rings studies ring-wide uniqueness in a different setting.

The present statement is an exact multiplicity refinement on the canonical semisimple finite-field stratum. The full-text existence paper was inspected, including its invariant-decomposition lemma and matrix-factorization results; the exact product of finite-field idempotent counts above is not stated there. Targeted searches for decomposition counts, centralizer idempotents, semisimple matrices, and uniqueness found no statement implying this formula.

## Limitations
The formula is proved only for semisimple matrices. Nonsemisimple primary components have nonsemisimple centralizer algebras, so the independent idempotent count used here no longer applies directly. The literature search cannot exclude an equivalent formula under different terminology; this remains the principal originality risk.

## References
1. J. Chen, X. Yang, Y. Zhou, *When is the \(2\times2\) matrix ring over a commutative local ring strongly clean?*, Journal of Algebra 301 (2006), DOI: 10.1016/j.jalgebra.2005.08.005.
2. G. Borooah, A. J. Diesl, T. J. Dorsey, *Strongly clean matrix rings over commutative local rings*, Journal of Pure and Applied Algebra 212 (2008), DOI: 10.1016/j.jpaa.2007.05.020.
3. H. Chen, O. Gurgun, H. Kose, *Uniquely Strongly Clean Triangular Matrix Rings*, arXiv:1307.7339.
