# A five-dimensional nilpotent-free subspace of \(M_3(\mathbb F_3)\)
## Finding
There exists a five-dimensional \(\mathbb F_3\)-linear subspace \(W\le M_3(\mathbb F_3)\) whose only nilpotent element is zero. An explicit choice is \[W=\{M(a,b,c,d,e):a,b,c,d,e\in\mathbb F_3\},\] where \[M(a,b,c,d,e)=\begin{pmatrix}a&b&c\\d&e&2a+b+c+2e\\2c+d+e&2a+b+d+2e&2b+c+2d+2e\end{pmatrix}.\] Consequently the maximum dimension of a nilpotent-free subspace of \(M_3(\mathbb F_3)\) is at least \(5\), one dimension below the \(6\)-dimensional target in Wigderson's Conjecture 8. No maximality or nonexistence of a six-dimensional example is claimed.

## Assumptions and scope
All matrices and linear combinations are over \(\mathbb F_3\). A matrix is called nilpotent if some positive power is zero. The claim is only an existence and lower-bound statement for \(3\times3\) matrices over \(\mathbb F_3\); it does not determine the maximum dimension.

## Proof
For \((a,b,c,d,e)\in\mathbb F_3^5\), define
\[
M(a,b,c,d,e)=\begin{pmatrix}
a&b&c\\
d&e&2a+b+c+2e\\
2c+d+e&2a+b+d+2e&2b+c+2d+2e
\end{pmatrix}.
\]
The five coefficient matrices obtained by setting one parameter equal to \(1\) and the other four equal to \(0\) are linearly independent; equivalently, row reduction of their flattened \(5\times9\) coefficient matrix has rank \(5\). Hence the displayed family is a five-dimensional subspace \(W\).

It remains to show that no nonzero member is nilpotent. There are exactly \(3^5=243\) parameter tuples. The accompanying verifier exhausts all of them. For every tuple it checks two equivalent criteria independently: first, whether \(M^3=0\); second, whether all three non-leading coefficients of the characteristic polynomial vanish, computed as \((\operatorname{tr}M,s_2(M),\det M)\). For a \(3\times3\) matrix, either condition is equivalent to nilpotency. Both checks identify exactly one tuple, \((0,0,0,0,0)\). Thus the only nilpotent element of \(W\) is zero.

## Verification
Run `python3 verify_f3_five_space.py`. The archived output is `VERIFY_OK total=243 nonzero=242 nilpotent_total=1 nilpotent_nonzero=0 zero_charpoly=1 basis_rank=5`. The computation uses exact arithmetic modulo \(3\), enumerates the complete finite domain, recomputes the basis rank, and cross-checks the matrix-cube and characteristic-polynomial tests.

## Relationship to prior work
Wigderson's 2026 paper *Duality for matrix space questions* formulates Conjecture 8: over every finite field, there should be a subspace of dimension \(n^2-\binom{n}{2}\) containing no nonzero nilpotent matrix. For \(n=3\), the target is dimension \(6\). The paper explicitly states that such finite-field constructions are unclear. Its finite-field extension construction yields a totally nonsingular subspace of dimension \(n\), hence dimension \(3\) here. The present explicit five-space narrows that construction gap for the smallest odd field without settling the conjectural six-dimensional case.

## Limitations
No claim is made that dimension \(5\) is maximal. In particular, the computation does not exclude a six-dimensional nilpotent-free subspace of \(M_3(\mathbb F_3)\). The literature comparison found no statement implying or tabulating this exact five-dimensional construction, but an equivalent construction under a change of coordinates or matrix-space equivalence may exist outside the inspected sources.

## References
1. Yuval Wigderson, *Duality for matrix space questions*, arXiv:2609.29177v1, 24 September 2026. See Conjecture 8 and Proposition 9.
