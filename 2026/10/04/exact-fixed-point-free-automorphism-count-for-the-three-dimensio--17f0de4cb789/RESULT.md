# Exact fixed-point-free automorphism count for the three-dimensional Heisenberg Lie algebra
## Finding
Let \(q\) be a prime power and let \(\mathfrak h_3(\mathbb F_q)\) have basis \(x,y,z\) with
\[
[x,y]=z,\qquad [x,z]=[y,z]=0.
\]
The number of automorphisms \(\varphi\) whose only fixed vector is \(0\) is
\[
q^3(q+1)(q-2)^2.
\]
Since
\[
\lvert\operatorname{Aut}(\mathfrak h_3(\mathbb F_q))\rvert=q^3(q-1)^2(q+1),
\]
the fixed-point-free proportion is
\[
\left(\frac{q-2}{q-1}\right)^2.
\]
Thus \(\mathfrak h_3(\mathbb F_2)\) has no fixed-point-free automorphism, while \(\mathfrak h_3(\mathbb F_q)\) has such automorphisms for every \(q>2\).

## Assumptions and scope
The field is an arbitrary finite field \(\mathbb F_q\); no restriction on the characteristic is required. Fixed-point-free means that \(\varphi(v)=v\) implies \(v=0\). The statement concerns Lie algebra automorphisms of the three-dimensional Heisenberg algebra, not automorphisms of the discrete or finite Heisenberg group.

## Proof
The center and derived algebra of \(\mathfrak h_3(\mathbb F_q)\) are both \(\mathbb F_q z\). Hence every automorphism induces some \(A\in\mathrm{GL}_2(\mathbb F_q)\) on the quotient \(\mathfrak h_3/\mathbb F_q z\). Conversely, every \(A\in\mathrm{GL}_2(\mathbb F_q)\) and every pair of central shifts in \(\mathbb F_q^2\) define an automorphism, with
\[
\varphi(z)=\det(A)z.
\]
Therefore there are exactly \(q^2\) automorphisms above each \(A\), and
\[
\lvert\operatorname{Aut}(\mathfrak h_3(\mathbb F_q))\rvert=q^2\lvert\mathrm{GL}_2(\mathbb F_q)\rvert=q^3(q-1)^2(q+1).
\]
Relative to \(\mathbb F_q^2\oplus\mathbb F_q z\), the matrix of \(\varphi-I\) is block triangular with diagonal blocks \(A-I\) and \(\det(A)-1\). Thus \(\varphi\) is fixed-point-free exactly when
\[
\det(A-I)\ne0\qquad\text{and}\qquad\det(A)\ne1.
\]
Fix \(\delta\in\mathbb F_q^\times\setminus\{1\}\). The determinant fiber \(\{A\in\mathrm{GL}_2(\mathbb F_q):\det A=\delta\}\) has size
\[
\lvert\mathrm{SL}_2(\mathbb F_q)\rvert=q(q^2-1).
\]
Inside this fiber, a matrix has eigenvalue \(1\) exactly when its characteristic polynomial is \((t-1)(t-\delta)\). Since \(\delta\ne1\), it is diagonalizable and conjugate to \(\operatorname{diag}(1,\delta)\). Its centralizer in \(\mathrm{GL}_2(\mathbb F_q)\) has order \((q-1)^2\), so its conjugacy class has size
\[
\frac{\lvert\mathrm{GL}_2(\mathbb F_q)\rvert}{(q-1)^2}=q(q+1).
\]
Hence, for each \(\delta\ne1\), the number of admissible matrices is
\[
q(q^2-1)-q(q+1)=q(q+1)(q-2).
\]
There are \(q-2\) choices of \(\delta\), so the number of admissible quotient matrices is \(q(q+1)(q-2)^2\). Multiplying by the \(q^2\) central shifts proves the formula.

## Verification
The proof is symbolic and valid for every prime power. The accompanying `verify.py` exhaustively enumerates quotient matrices for \(\mathbb F_2,\mathbb F_3,\mathbb F_4,\mathbb F_5,\mathbb F_7\), checks the order of \(\mathrm{GL}_2\), checks the admissible-matrix formula, and obtains `CHECK_OK`. These finite computations are consistency checks, not substitutes for the general proof.

## Relationship to prior work
Burde and Dekimpe study fixed-point-free automorphisms of finite-dimensional Lie algebras in characteristic zero. Their low-dimensional classification states that the complex three-dimensional Heisenberg algebra admits fixed-point-free automorphisms and determines possible finite orders, but it does not enumerate such automorphisms over finite fields. Liu and Tang study automorphism groups and distinguished automorphism subgroups of Heisenberg Lie algebras over commutative rings; the inspected full-text HTML gives inner, central, and involutionary automorphism constructions, but no fixed-point-free finite-field census was located. Hayat, López-Aguayo, and Abbas count fixed-point-free automorphisms for certain finite abelian groups; that is an analogous counting problem on different algebraic objects and does not imply the Lie-algebra formula here.

## Limitations
This result treats only the three-dimensional Heisenberg Lie algebra. It does not give the corresponding count for higher-dimensional Heisenberg Lie algebras, nor does it classify fixed-point-free automorphisms by order. Older automorphism-group literature could in principle contain an equivalent enumeration under different terminology despite the targeted searches reported here.

## References
1. D. Burde and K. Dekimpe, *Fixed-point-free automorphisms of solvable Lie algebras*, arXiv:2604.27916v1, first submitted 2026-04-30. Primary MSC: 17B30, 17B08.
2. L. Liu and L. Tang, *The automorphism groups of Heisenberg Lie (super)algebras*, Journal of Mathematics 38 (2018), 502-510, DOI:10.13548/J.SXZZ.20170518.003.
3. U. Hayat, D. López-Aguayo, and A. Abbas, *Fixed Points of Automorphisms of Certain Non-Cyclic p-Groups and the Dihedral Group*, Symmetry 10 (2018), 238, DOI:10.3390/sym10070238.
