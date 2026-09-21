# Exact Coxeter periodicity for radical-cube-zero linear Nakayama algebras

## Result

For \(n\ge 3\), let \(C_n=C_{n,3}\) be the \(n\times n\) upper-triangular matrix with
\[
(C_n)_{ij}=1\quad\text{if }0\le j-i\le 2,
\]
and zero otherwise, and set
\[
M_n=-C_n^{-1}C_n^{T}.
\]
This is the Coxeter matrix of the linear Nakayama algebra \(A_n/J^3\).

Then
\[
\boxed{M_n\text{ is periodic}\iff n\not\equiv 9,11\pmod {12}.}
\]
When it is periodic, its exact period is
\[
\operatorname{per}(M_n)=
\begin{cases}
\operatorname{lcm}(2,3,n/2+1),&n\text{ even},\\[2mm]
2(n+2),&n\equiv1,7\pmod{12},\\[2mm]
4,&n=3,\\
8,&n=5,\\[1mm]
\operatorname{lcm}(n+1,n+3),&n\equiv3,5\pmod{12},\ n>5.
\end{cases}
\]
For \(n\equiv9,11\pmod{12}\), the eigenvalue \(1\) has algebraic multiplicity two and geometric multiplicity one. In fact it is the only repeated eigenvalue that is not semisimple: over \(\mathbb C\), \(M_n\) has exactly one nontrivial \(2\times2\) Jordan block, at eigenvalue \(1\). Hence these matrices have infinite order despite having cyclotomic characteristic polynomial.

This settles the case \(r=3\) of the periodicity question for the Coxeter matrices \(M_{n,r}\) of the truncated linear Nakayama algebras \(A_n/J^r\).

## Odd dimensions: the Coxeter polynomial

Write
\[
p_n(x)=\det(xI-M_n).
\]
A known recurrence for the Coxeter polynomials of \(A_n/J^3\) is
\[
p_n(x)=x^n+x^{n-1}-x^3p_{n-6}(x)+x+1\qquad(n\ge6).
\]
For odd \(n\), it gives the following closed forms.

If \(n\equiv1\pmod6\), then
\[
\boxed{p_n(x)=\frac{(1+x)(1+x^{n+2})}{1+x^3}.}
\]
If \(n=6m+3\) or \(n=6m+5\), put
\[
a=\frac{n+1}{2},\qquad b=\frac{n+3}{2},\qquad \varepsilon=(-1)^m.
\]
Then
\[
\boxed{p_n(x)=\frac{(1+x)(1+\varepsilon x^a)(1+\varepsilon x^b)}{1+x^3}.}
\]
The displayed quotients are polynomials. These formulas follow by induction in steps of six from
\[
p_1=x+1,\qquad p_3=(x+1)(x^2+1),\qquad p_5=(x+1)(x^4+1).
\]
Indeed, for \(n\equiv1\pmod6\), multiplying the recurrence by \(1+x^3\) reduces the induction step to
\[
(1+x)\big((1+x^3)(1+x^{n-1})-x^3(1+x^{n-4})\big)
=(1+x)(1+x^{n+2}).
\]
For the other two odd residue classes, replacing \(\varepsilon\) by \(-\varepsilon\) at \(n-6\) gives
\[
(1+x)\big((1+x^3)(1+x^{a+b-3})-x^3(1-\varepsilon x^{a-3})(1-\varepsilon x^{b-3})\big)
=(1+x)(1+\varepsilon x^a)(1+\varepsilon x^b).
\]

### Periodic odd residue classes

Suppose first that \(n\equiv1\pmod6\). Then \(n+2\) is an odd multiple of three, so \(1+x^3\) divides \(1+x^{n+2}\). Thus
\[
p_n(x)=\frac{x^{n+2}+1}{x^2-x+1}.
\]
For \(n\ge7\) this polynomial is squarefree, all its roots are \(2(n+2)\)-th roots of unity, and a primitive \(2(n+2)\)-th root remains after the cancellation. Hence \(M_n\) is diagonalizable and has exact period \(2(n+2)\).

Now let \(n=6m+3\) or \(6m+5\) with \(m\) even, equivalently \(n\equiv3,5\pmod{12}\). Then \(\varepsilon=1\). Exactly one of \(a,b\) is a multiple of three with odd quotient, so \(1+x^3\) divides the corresponding factor \(1+x^a\) or \(1+x^b\). Since \(a,b\) are consecutive, the remaining roots are simple. For \(n>5\), primitive roots of orders \(2a=n+1\) and \(2b=n+3\) both survive the cancellation. Therefore
\[
\operatorname{per}(M_n)=\operatorname{lcm}(n+1,n+3).
\]
The two small cases are \(p_3=(x+1)(x^2+1)\), giving period \(4\), and \(p_5=(x+1)(x^4+1)\), giving period \(8\).

### The Jordan obstruction for \(n\equiv9,11\pmod{12}\)

Here \(m\) is odd, so \(\varepsilon=-1\). Consequently
\[
p_n(x)=\frac{(1+x)(1-x^a)(1-x^b)}{1+x^3}.
\]
Because \(a,b\) are consecutive, \(x=1\) is a root of multiplicity exactly two and every other root is simple. It remains to determine the eigenspace dimension at \(1\).

Since
\[
M_n-I=-C_n^{-1}(C_n^T+C_n),
\]
the \(1\)-eigenspace is the kernel of \(B_n=C_n+C_n^T\). If \(v\in\ker B_n\) and \(v_1=A,\ v_2=B\), the first two equations give
\[
v_3=-2A-B,\qquad v_4=A-B.
\]
The interior rows give the recurrence
\[
v_{i-2}+v_{i-1}+2v_i+v_{i+1}+v_{i+2}=0.
\]
It produces the 12-periodic coefficient pattern
\[
\begin{array}{c|rrrrrrrrrrrr}
i&1&2&3&4&5&6&7&8&9&10&11&12\\ \hline
v_i&A&B&-2A-B&A-B&2A+2B&-2A&-A-2B&2A+B&B&-A-B&0&0.
\end{array}
\]
For \(n\equiv9\pmod{12}\), the last two boundary equations both reduce to \(A+B=0\). For \(n\equiv11\pmod{12}\), they reduce to \(A=0\) (with the other equation redundant). Thus \(\dim\ker(M_n-I)=1\) in both cases. Since the algebraic multiplicity of \(1\) is two, \(M_n\) has a \(2\times2\) Jordan block at \(1\) and therefore cannot have finite order. Since all other roots of \(p_n\) are simple, this is the unique nontrivial Jordan block.

## Even dimensions

Write \(n=2m\), with \(m\ge2\). A known derived-equivalent model for \(A_{2m}/J^3\) is
\[
A_m\otimes A_2,
\]
where \(A_s\) denotes the path algebra of the linearly oriented Dynkin quiver of type \(A_s\). Coxeter transformations are preserved up to conjugacy by derived equivalence. Moreover, for tensor products of Cartan matrices,
\[
\Phi_{A_m\otimes A_2}=-\Phi_{A_m}\otimes\Phi_{A_2}.
\]
Let \(h=m+1\), let \(\zeta\) be a primitive \(h\)-th root of unity and \(\omega\) a primitive cube root. The eigenvalues are
\[
-\zeta^i\omega^j,\qquad 1\le i\le m,\quad j=1,2.
\]
The matrix is diagonalizable. If a positive integer \(q\) kills all these eigenvalues, ratios with fixed \(j\) force \(h\mid q\), ratios with fixed \(i\) force \(3\mid q\), and then the sign forces \(2\mid q\). Conversely every multiple of \(\operatorname{lcm}(2,3,h)\) kills every eigenvalue. Hence
\[
\operatorname{per}(M_{2m})=\operatorname{lcm}(2,3,m+1).
\]

## Context and comparison with the literature

The periodicity problem for the matrices \(M_{n,r}\) was explicitly posed in 2020, including the request to determine for fixed \(r\) which \(n\) are periodic and the exact period. The same source identifies \(M_{n,r}\) as the Coxeter matrices of \(A_n/J^r\) and notes that these periods are derived invariants.

Earlier work of de la Peña proves that every \(A_n/J^3\) has cyclotomic Coxeter polynomial. A later open exposition by the same author recalls that argument in detail, including the derived equivalence used above for even \(n\) and the six-step Coxeter-polynomial recurrence. Cyclotomicity alone does not imply that the Coxeter matrix is periodic: the residue classes \(n\equiv9,11\pmod{12}\) give an explicit infinite family where the obstruction is a single unipotent Jordan block.

Targeted searches through current literature on linear Nakayama algebras and Coxeter matrices did not locate this \(r=3\) classification or the exact period formulas. The 2020 periodicity question currently has no posted answer.

## Reproducibility

`artifacts/verify.py` constructs \(C_n\) and \(M_n\) exactly over the rationals with SymPy, checks the closed Coxeter-polynomial formulas for odd \(n\) in a finite test range, checks the predicted finite orders by exact matrix powers in a finite test range, and verifies the algebraic/geometric multiplicity defect at the first nonperiodic cases. These computations support but are not used in place of the general proof above.

## Limitations

- The classification here treats \(r=3\) only; it does not solve the corresponding problem for \(r\ge4\).
- Originality is asserted only to the best of our knowledge.
- The full text of de la Peña's 2014 article was not inspected. Its 2019 chapter explicitly recalls the \(A_n/J^3\) argument as a proof of cyclotomicity and supplies the recurrence used here, and the later 2020 question still asks for the exact periodicity classification, but an equivalent statement in older literature remains a residual originality risk.
- A 2012 table of computed periods cited by the 2020 question was not used as evidence of a general formula; a tabulated data pattern would not by itself replace the classification and proof above.

## References

1. M. Marczinzik, *Periodics of Coxeter matrices for truncated Nakayama algebras*, MathOverflow question 369054 (2020). https://mathoverflow.net/questions/369054/periodics-of-coxeter-matrices-for-truncated-nakayama-algebras
2. J.-A. de la Peña, *Algebras whose Coxeter polynomials are products of cyclotomic polynomials*, Algebras and Representation Theory 17 (2014), 905--930. https://doi.org/10.1007/s10468-013-9424-0 ; preprint https://arxiv.org/abs/1310.1557
3. J.-A. de la Peña, *Cyclotomic and Littlewood Polynomials Associated to Algebras*, in Polynomials (2019). https://doi.org/10.5772/intechopen.82309
4. V. Klász, M. Kleinau, R. Marczinzik, *Classification of Auslander-Gorenstein monomial algebras: The acyclic case* (2026). https://arxiv.org/abs/2604.02146
5. V. Calvo Cortes, H. Frost, *Dyck Paths, Configuration Spaces and Polytopes For Linear Nakayama algebras* (2026). https://arxiv.org/abs/2602.04571
