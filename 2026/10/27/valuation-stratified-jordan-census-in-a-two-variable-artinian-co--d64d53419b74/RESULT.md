# Valuation-stratified Jordan census in a two-variable Artinian complete intersection

## Finding
Let \(n\ge 2\) and let \(q=p^e\) be an arbitrary prime power. Set
\[
A_{n,q}=\mathbb F_q[x,y]/(x^2,y^n),\qquad \mathfrak m=(x,y)A_{n,q}.
\]
For \(u\in\mathfrak m\), denote by \(M_u\) multiplication by \(u\) on the \(2n\)-dimensional vector space \(A_{n,q}\). Each \(u\) has the unique form \(u=f(y)+xg(y)\), with \(f\in y\mathbb F_q[y]/(y^n)\) and \(g\in\mathbb F_q[y]/(y^n)\). Write \(a=v_y(f)\in\{1,\ldots,n\}\) and \(b=v_y(g)\in\{0,\ldots,n\}\), with the valuation of zero defined to be \(n\).

Define \((z)_+=\max(z,0)\), \(c=\min(a,b)\), and for each integer \(k\ge1\) let
\[
r_k(a,b)=\begin{cases}
2(n-ka)_+,&p\mid k,\\
(n-(k-1)a-c)_+ +(n-(k+1)a+c)_+,&p\nmid k.
\end{cases}
\]
Then **all powers of all radical multiplication operators have their ranks determined by these two valuations**:
\[
\boxed{\operatorname{rank}_{\mathbb F_q}(M_u^k)=r_k(a,b).}
\]
Put \(w_n(t)=(q-1)q^{n-t-1}\) for \(0\le t<n\), and \(w_n(n)=1\). The exact joint-rank enumerator is
\[
\boxed{\mathcal J_{n,q}(Z_1,\ldots,Z_n)
=\sum_{u\in\mathfrak m}\prod_{k=1}^{n} Z_k^{\operatorname{rank}(M_u^k)}
=\sum_{a=1}^{n}\sum_{b=0}^{n}w_n(a)w_n(b)
\prod_{k=1}^{n}Z_k^{r_k(a,b)}.}
\]
This is a complete finite-field census of nilpotent Jordan partitions, not just of generic elements: with \(r_0=2n\) and \(r_{n+1}=r_{n+2}=0\), the multiplicity of blocks of size \(j\), for \(1\le j\le n+1\), is \(r_{j-1}-2r_j+r_{j+1}\). In particular, the coefficients of the displayed polynomial determine the exact count of every Jordan partition.

The Hilbert function of \(A_{n,q}\) has conjugate partition \((n+1,n-1)\). Exactly
\[
\boxed{\begin{cases}(q-1)^2q^{2n-3},&p\nmid n,\\0,&p\mid n\end{cases}}
\]
radical elements have this strong-Lefschetz Jordan partition. Equivalently, its exact probability under uniform sampling from \(\mathfrak m\) is \((1-q^{-1})^2\) when \(p\nmid n\), and zero when \(p\mid n\). The existence/nonexistence aspect agrees with established modular Lefschetz theory; the all-element joint-rank census is the primary claim here.

## Assumptions and scope
The field can have any prime-power order, including nonprime finite fields. The quotient length satisfies \(n\ge2\); no assumption on the relation between \(p\) and \(n\) is made. All ranks are vector-space ranks over \(\mathbb F_q\), not ranks over the coefficient ring \(\mathbb F_q[y]/(y^n)\). The maximum nilpotent Jordan block has size at most \(n+1\), since \(\mathfrak m^{n+1}=0\).

## Proof
**1. Block-matrix realization.** Write \(R=\mathbb F_q[y]/(y^n)\). As an \(R\)-module, \(A_{n,q}=R\oplus xR\). For \(u=f+xg\), its multiplication endomorphism is represented by
\[
B_u=\begin{pmatrix}f&0\\g&f\end{pmatrix}\quad\text{over }R.
\]
By commutativity of \(R\), for each positive integer \(k\),
\[
B_u^k=\begin{pmatrix}f^k&0\\k f^{k-1}g&f^k\end{pmatrix}.
\]
The integer coefficient is interpreted in characteristic \(p\). In particular, the lower-left entry is zero if \(p\mid k\).

**2. Invariant factors when \(p\nmid k\).** Lift the displayed matrix to the discrete valuation ring \(\mathbb F_q[[y]]\). When \(f\ne0\), the valuation of the first invariant factor is
\[
d_1=\min(ka,(k-1)a+b)=(k-1)a+\min(a,b),
\]
and the determinant has valuation \(2ka\), so the second invariant factor has valuation
\[
d_2=2ka-d_1=(k+1)a-\min(a,b).
\]
The first equality follows from the gcd of the matrix entries in a discrete valuation ring; the second from the determinant. These expressions remain valid for computing ranks modulo \(y^n\) when \(g=0\), by assigning \(b=n\). If \(f=0\), then at \(k=1\) the matrix is equivalent to \(\operatorname{diag}(g,0)\), and at \(k\ge2\) it is zero; taking \(a=n\) in the stated formula gives precisely these truncated ranks. Thus no zero-element exception has been omitted.

Multiplication by \(y^d\) on \(R\) has \(\mathbb F_q\)-rank \((n-d)_+\). Hence the two invariant factors have total rank \((n-d_1)_++(n-d_2)_+\), exactly the asserted second branch of \(r_k\). When \(p\mid k\), the matrix is diagonal with two copies of multiplication by \(f^k\), giving \(2(n-ka)_+\). This proves the power-rank formula in every characteristic and at every boundary valuation.

**3. Full partition and enumeration.** The identity \(\mathfrak m^{n+1}=0\) gives \(r_{n+1}=r_{n+2}=0\). For a nilpotent linear operator, \(r_{j-1}-r_j\) counts blocks of size at least \(j\); taking a second difference yields the number of blocks of size exactly \(j\). The number of series of valuation \(t<n\) in \(R\) is \((q-1)q^{n-t-1}\), while the zero series is unique. The \(y\)-constant of \(f\) is constrained to vanish, so \(a\ge1\), whereas \(b\ge0\) is unrestricted. Thus each valuation pair occurs exactly \(w_n(a)w_n(b)\) times. Summing its entire power-rank profile gives the stated multivariate polynomial. Its evaluation at all variables equal to one is \(q^{n-1}q^n=q^{2n-1}\), the number of radical elements.

**4. Strong-Lefschetz Jordan stratum.** The Hilbert function is \((1,2,\ldots,2,1)\), with conjugate partition \((n+1,n-1)\). A block of size \(n+1\) occurs if and only if \(u^n\ne0\), since multiplication by \(u^n\) sends \(1\) to \(u^n\). From \(f\in yR\),
\[
u^n=f^n+nxf^{n-1}g=nxf^{n-1}g.
\]
This is nonzero exactly when \(p\nmid n\), \(a=1\), and \(b=0\). For that valuation pair, direct substitution into the proven rank formula yields \(r_k=(n+1-k)_++(n-1-k)_+\) for every \(k\), so the full partition is \((n+1,n-1)\). Conversely, the partition forces \(u^n\ne0\) and thus the same conditions. There are exactly \(w_n(1)w_n(0)=(q-1)^2q^{2n-3}\) such elements; division by \(q^{2n-1}\) gives the probability. This completes the proof.

## Verification
Run `python3 check_jordan_val.py` with Python 3 and no external packages. The program independently constructs each multiplication matrix by truncated-polynomial convolution, iterates its powers, computes the finite-field rank by Gaussian elimination, reconstructs the Jordan partition, and checks the displayed formula and the sharp strong-Lefschetz count. It exhausts twelve configurations with \(q\in\{2,3,4,5\}\) and \(2\le n\le6\) as listed in the script, using explicit arithmetic in \(\mathbb F_4\). It printed `ALL_TWO_VARIABLE_JORDAN_CHECKS_PASSED`. Exhaustive checks at finitely many parameters do not prove the general statement; Steps 1–4 are the proof.

For illustration, at \((q,n)=(2,3)\), the radical has 32 elements, of which exactly 8 have Jordan type \((4,2)\). At \((q,n)=(3,3)\), all 243 radical elements have nilpotency index at most three, so none has type \((4,2)\).

## Relationship to prior work
Iarrobino, Macias Marques and McDaniel develop general Jordan-type loci for Artinian algebras, explicitly including arbitrary maximal-ideal elements, and survey the tensor-product theory. The present statement specializes to a fixed complete intersection but adds an exact finite-field distribution for **all nonhomogeneous** radical elements, resolved simultaneously by the ranks of every power. Altafi, Iarrobino and Khatami study possible Jordan types of **linear forms** in height-two complete intersections, in characteristic zero or sufficiently large positive characteristic; their classification neither fixes the all-radical finite-field counts nor applies unchanged to all small characteristics. Nicklasson's positive-characteristic classification already determines whether a monomial complete intersection is strong Lefschetz; that known existence criterion is not presented as novel here.

A public quantitative result on lifts of a nilpotent Jordan block over dual numbers counts indices of matrices \(J_n+\varepsilon B\) over a coefficient ring with square-zero element. That operator family is not the regular multiplication family considered here, its nilpotency index can reach \(2n\), and its stated distribution does not imply this joint Jordan-partition law. No exact previously published all-element valuation census for this fixed family was found in the targeted comparisons. This is a limited priority assessment, not a guarantee of historical uniqueness.

## Limitations
The theorem treats the specified two-generator complete intersections with one square-zero generator; the same two-valuation formula is not asserted for \(\mathbb F_q[x,y]/(x^d,y^n)\) when \(d>2\), or for other Artinian algebras. It does not classify Jordan degree types, automorphism orbits, or arbitrary module actions. The invariant-factor argument is elementary once the block matrix is identified, and older treatments of modular tensor products or commuting nilpotent operators may contain equivalent consequences not identified in the literature comparison. Independent mathematical review remains outstanding.

## References
1. A. Iarrobino, P. Macias Marques, C. McDaniel, *Artinian algebras and Jordan type*, arXiv:1802.07383, first posted 2018-02-21; https://arxiv.org/abs/1802.07383.
2. N. Altafi, A. Iarrobino, L. Khatami, *Complete intersection Jordan types in height two*, arXiv:1810.00716, first posted 2018-10-01; https://arxiv.org/abs/1810.00716.
3. L. Nicklasson, *The strong Lefschetz property of monomial complete intersections in two variables*, arXiv:1703.07970, first posted 2017-03-23; https://arxiv.org/abs/1703.07970.
4. N. Altafi, A. Iarrobino, P. Macias Marques, *Jordan type of an Artinian algebra, a survey*, arXiv:2307.00957, first posted 2023-07-03; https://arxiv.org/abs/2307.00957.
5. *Exact nilpotency-index distribution for Jordan lifts over finite dual numbers*, public research result, https://github.com/Resultary/2026/tree/main/2026/10/4/SCOPE-exact-nilpotency-index-distribution-for-jordan-lifts-over-finite--a669645ca0b7.
