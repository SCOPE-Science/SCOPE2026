# Four commutator-fiber strata in \(T_3(\mathbb F_q)\)
## Finding
Let \(q\) be a prime power, let \(T=T_3(\mathbb F_q)\), and for
\[
C=\begin{pmatrix}0&x&y\\0&0&z\\0&0&0\end{pmatrix}
\]
write
\[
N(C)=\#\{(A,B)\in T^2:[A,B]=C\}.
\]
Every additive commutator in \(T\) is strictly upper triangular, every strictly upper triangular matrix occurs as a commutator, and the fiber size has exactly four values:
\[
N(C)=
\begin{cases}
q^5\big((q^2+q-1)^2+q^2(q-1)\big),&C=0,\\
q^5(q^2-1)(q^2+2q-1),&x=z=0,\ y\ne0,\\
q^5(q^2-1)(q^2+q-1),&xz=0,\ (x,z)\ne(0,0),\\
q^5(q^2-1)^2,&xz\ne0.
\end{cases}
\]
Consequently the commuting probability of \(T\) is
\[
\operatorname{Pr}(T)=\frac{q^4+3q^3-2q^2-2q+1}{q^7}.
\]
The multiplicities of the four target strata inside the commutator image are respectively
\[
1,\qquad q-1,\qquad 2q(q-1),\qquad q(q-1)^2.
\]

## Assumptions and scope
The algebra is the six-dimensional associative algebra of all upper triangular \(3\times3\) matrices over an arbitrary finite field \(\mathbb F_q\). The bracket is the additive Lie commutator \([A,B]=AB-BA\). The result counts ordered pairs \((A,B)\); it does not concern group commutators in the unitriangular or Borel group. No restriction on the characteristic is used.

## Proof
Write
\[
A=\begin{pmatrix}a_1&p&h\\0&a_2&r\\0&0&a_3\end{pmatrix},\qquad
B=\begin{pmatrix}b_1&s&t\\0&b_2&u\\0&0&b_3\end{pmatrix}.
\]
Set
\[
\alpha=a_1-a_2,\quad \beta=a_2-a_3,\quad
\gamma=b_1-b_2,\quad \delta=b_2-b_3.
\]
For fixed \(\alpha,\beta\), the diagonal of \(A\) has \(q\) choices, and similarly the diagonal of \(B\) has \(q\) choices. Thus it is enough to count the remaining ten effective coordinates and multiply the answer by \(q^2\). Direct multiplication gives
\[
[A,B]_{12}=\alpha s-\gamma p,
\]
\[
[A,B]_{23}=\beta u-\delta r,
\]
\[
[A,B]_{13}=(\alpha+\beta)t-(\gamma+\delta)h+pu-sr.
\]

For \(c\in\mathbb F_q\), let \(D(c)\) be the number of ordered pairs of vectors \(w,v\in\mathbb F_q^2\) with \(\det(w,v)=c\). Then
\[
D(0)=q^3+q^2-q=q(q^2+q-1),
\]
and, for \(c\ne0\),
\[
D(c)=q(q^2-1),
\]
because a nonzero determinant fiber is a coset of \(\operatorname{SL}_2(\mathbb F_q)\).

Fix the target coordinates \((x,y,z)\). Before solving the last displayed equation, the first two equations have
\[
M=D(x)D(z)
\]
solutions in \((\alpha,\gamma,p,s,\beta,\delta,r,u)\). Unless
\[
\alpha+\beta=0\quad\text{and}\quad \gamma+\delta=0,
\]
the last equation is one nonzero linear equation in \((t,h)\), hence has exactly \(q\) solutions.

It remains to count the exceptional base points. Put \(w=(\alpha,\gamma)\), \(v=(p,s)\), and \(v'=(r,u)\). Under \(\beta=-\alpha\) and \(\delta=-\gamma\), the first two equations become
\[
\det(w,v)=x,\qquad \det(w,v')=-z.
\]
Let \(K(x,z)\) be the number of such triples before imposing the \(13\)-entry, and let \(H(x,y,z)\) be the number also satisfying \(\det(v,v')=y\). If \((x,z)\ne(0,0)\), then \(w\ne0\), each of the two determinant equations has \(q\) solutions, and therefore
\[
K(x,z)=q^4-q^2.
\]
Choose \(e\) with \(\det(w,e)=1\). Then uniquely
\[
v=A_0w+xe,\qquad v'=B_0w-ze,
\]
and
\[
\det(v,v')=-A_0z-xB_0.
\]
Because \((x,z)\ne(0,0)\), the equation \(\det(v,v')=y\) has \(q\) choices of \((A_0,B_0)\) for each nonzero \(w\). Hence
\[
H(x,y,z)=q(q^2-1).
\]
Since \(qH=K\), the exceptional correction cancels whenever \((x,z)\ne(0,0)\).

If \(x=z=0\), the choice \(w=0\) contributes \(q^4\) to \(K\), while nonzero \(w\) contributes \(q^2\) choices each. Thus
\[
K(0,0)=2q^4-q^2.
\]
For \(y\ne0\), only \(w=0\) contributes to \(H\), giving
\[
H(0,y,0)=q(q^2-1).
\]
For \(y=0\), the \(w=0\) contribution is \(D(0)\), and every nonzero \(w\) contributes \(q^2\), so
\[
H(0,0,0)=q^4+q^3-q.
\]

Therefore the effective fiber size is
\[
q(M-K)+q^2H=qM+q(qH-K).
\]
Substitution of the preceding formulas yields the four effective fiber sizes
\[
q^3\big((q^2+q-1)^2+q^2(q-1)\big),
\]
\[
q^3(q^2-1)(q^2+2q-1),\qquad
q^3(q^2-1)(q^2+q-1),\qquad
q^3(q^2-1)^2.
\]
Multiplying by the two omitted diagonal-shift factors gives the stated \(q^5\)-formulas. Every displayed number is positive, so every strictly upper triangular target is attained. The zero-target fiber divided by \(|T|^2=q^12\) gives the commuting probability. Finally, the four target strata have cardinalities \(1\), \(q-1\), \(2q(q-1)\), and \(q(q-1)^2\), whose weighted fiber sum is \(q^12\), as required.

## Verification
The proof is symbolic and valid over every finite field. The accompanying `artifacts/verify.py` independently enumerates all ten effective coordinates for \(q=2,3,5\), compares every target fiber with the closed formulas, performs a direct six-coordinate matrix-pair enumeration for \(q=2\), and checks the weighted fiber identity for integer \(q\) from \(2\) through \(20\). A successful replay ends with `VERIFY_OK`.

The finite computations are consistency checks only. The arbitrary-prime-power statement follows from determinant-fiber counts and linear equations over \(\mathbb F_q\), not from interpolation.

## Relationship to prior work
Dolinar's 2007 paper studies maps on upper triangular matrix Lie algebras that preserve the Lie product and therefore establishes the same bracket as a natural structural object; its published statement is a preserver classification in characteristic zero, not a finite-field fiber count. Wang's 2014 Borel-subalgebra paper studies maps preserving zero Lie products, again qualitatively rather than by counting fixed commutator fibers. Buckley and MacHale's finite-ring work defines commuting probability and develops comparison theorems for subrings and quotients; its full text treats the zero commutator statistically but does not give the three nonzero commutator strata above.

The present calculation is the complete fixed-target commutator distribution for the first upper-triangular matrix algebra in which the radical product contributes to the bracket: the term \(pu-sr\) in the \(13\)-coordinate is exactly what separates the central nonzero fiber from the other nonzero fibers.

## Limitations
The formula is specific to \(T_3(\mathbb F_q)\). It does not assert a corresponding four-stratum law for \(T_n(\mathbb F_q)\) with \(n\ge4\), where several higher superdiagonals interact. The literature search located general Lie-product preserver results and finite-ring commuting-probability theory, but no exact fixed-target \(T_3(\mathbb F_q)\) fiber table; absence from searched sources is not a proof that no unindexed equivalent exists. The full text of the closest 2007 upper-triangular Lie-product paper was not openly available during the comparison, so its abstract, bibliographic record, and theorem statement were inspected rather than every page.

## References
1. G. Dolinar, “Maps on upper triangular matrices preserving Lie products,” *Linear and Multilinear Algebra* 55 (2007), 191–198. DOI: 10.1080/03081080600635484. Published online 23 November 2006.
2. D. Wang, “Invertible linear maps on Borel subalgebras preserving zero Lie products,” *Journal of Algebra* 406 (2014), 321–336. DOI: 10.1016/j.jalgebra.2014.02.023.
3. S. M. Buckley and D. MacHale, “Commuting probability for subrings and quotient rings,” *Journal of Algebra Combinatorics Discrete Structures and Applications* 4 (2017), 189–196. DOI: 10.13069/jacodesmath.284962.
