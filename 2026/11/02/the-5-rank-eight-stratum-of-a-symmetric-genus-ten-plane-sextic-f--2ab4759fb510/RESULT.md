# The 5-rank-eight stratum of a symmetric genus-ten plane-sextic family

## Finding
Let \(k\) be algebraically closed of characteristic \(5\). For every \(t\in k\), let \(C_t\subset\mathbf P^2_k\) be the degree-six plane curve
\[
 F_t=X^6+Y^6+Z^6+t(X^3Y^3+Y^3Z^3+Z^3X^3)=0.
\]
The curve is smooth precisely when \(t\notin\{2,3,4\}\subset\mathbf F_5\); hence every smooth member has genus \(10\). On the entire smooth locus, its Hasse--Witt rank, Jacobian \(5\)-rank, and \(a\)-number are exactly
\[
\begin{array}{c|ccc}
 t&\operatorname{rank}(H_t)&f(J(C_t))&a(J(C_t))\\\hline
0&0&0&10\\
 t\ne0&8&8&2.
\end{array}
\]
The nonzero row refers only to \(t\notin\{0,2,3,4\}\). In particular the Fermat member is superspecial, while **every other smooth member has a stable Frobenius image of dimension eight**, not merely a one-step matrix of rank eight.

## Assumptions and scope
All statements are over an algebraically closed field of characteristic exactly \(5\). The curve is defined by the displayed coefficient-marked homogeneous equation; no moduli-space assertion about all projectively isomorphic models is made. We use the standard convention that the \(5\)-rank of the Jacobian is the stable dimension of the semilinear Frobenius on \(H^1(C_t,\mathcal O_{C_t})\) and that its \(a\)-number is the dimension of the kernel of Cartier on \(H^0(C_t,\Omega^1)\). By Serre duality, the Cartier and Hasse--Witt matrices are transposes up to Frobenius-twisted basis conventions, so \(a=10-\operatorname{rank}H\).

The family has a natural \((\mu_3)^2\rtimes S_3\)-action by diagonal cube roots of unity and coordinate permutations; its distinguished coefficient \(t=-10\) in characteristic zero occurs in the quasi-Galois sextic studied by Fukasawa, Miura, and Takahashi. In characteristic five, this distinguished coefficient specializes to \(t=0\). The present finding concerns the characteristic-five variation of the entire symmetric coefficient family, **not** an asserted new result for the classical characteristic-zero sextic or the previously studied Fermat curve alone.

## Proof
**Smoothness.** Set \(U=X^3\), \(V=Y^3\), \(W=Z^3\). Since \(6\equiv1\) and \(3\ne0\) modulo \(5\), the three partial derivatives vanish precisely when
\[
 X^2(2U+t(V+W))=Y^2(2V+t(U+W))=Z^2(2W+t(U+V))=0.
\]
If all three coordinates are nonzero, the resulting linear system in \((U,V,W)\) has matrix with diagonal entries \(2\) and off-diagonal entries \(t\), with eigenvalues \(2-t\) (twice) and \(2+2t\) (once). Nontrivial solutions exist exactly for \(t=2\) or \(t=-1=4\). In either case there are kernel vectors with all coordinates nonzero. If exactly one coordinate, say \(X\), vanishes, the remaining two equations have a nontrivial solution exactly when \(4-t^2=0\), i.e. \(t=2\) or \(t=-2=3\); both nonzero remaining coordinates can be chosen. No point with exactly one nonzero coordinate is critical. Euler's identity, \(6F_t=XF_X+YF_Y+ZF_Z\), implies each projective critical point lies on \(C_t\), since \(6\equiv1\pmod5\). Thus the exceptional set is exactly \(\{2,3,4\}\). The genus of every smooth plane sextic is \((6-1)(6-2)/2=10\).

**Hasse--Witt coefficient formula.** Let
\[
\mathcal I=\{(i,j,k)\in\mathbf Z_{>0}^3:i+j+k=6\}.
\]
It contains ten triples. The exact sequence \(0\to\mathcal O_{\mathbf P^2}(-6)\xrightarrow{F_t}\mathcal O_{\mathbf P^2}\to\mathcal O_{C_t}\to0\) identifies \(H^1(C_t,\mathcal O_{C_t})\) with \(H^2(\mathbf P^2,\mathcal O(-6))\). In the standard Čech monomial basis indexed by \(\alpha\in\mathcal I\), the absolute Frobenius is represented, up to transposition depending on whether rows index source or target, by the \(10\times10\) matrix
\[
 M_{\alpha\beta}=[X^{5\alpha_1-\beta_1}Y^{5\alpha_2-\beta_2}Z^{5\alpha_3-\beta_3}]F_t^4.
\]
Indeed, Frobenius first raises a reciprocal monomial to its fifth power, and multiplication by \(F_t^4\) returns it to degree \(-6\); the Čech cohomology projection retains precisely reciprocal monomials with strictly positive exponents. This derives the coefficient rule without numerical testing.

Order the ten triples as
\[
\begin{split}
\alpha_0&=(1,1,4),\ \alpha_1=(1,2,3),\ \alpha_2=(1,3,2),\ \alpha_3=(1,4,1),\\
\alpha_4&=(2,1,3),\ \alpha_5=(2,2,2),\ \alpha_6=(2,3,1),\ \alpha_7=(3,1,2),\\
\alpha_8&=(3,2,1),\ \alpha_9=(4,1,1).
\end{split}
\]
Expand \(F_t^4\) by the multinomial theorem over \(\mathbf F_5[t]\). Exactly twelve of the hundred matrix entries are nonzero. Define
\[
 A=-t(t-2)^2(t+2),\qquad B=2t(t+2),\qquad D=2t(t-2)^3.
\]
Their positions are
\[
\begin{array}{ll}
M_{1,4}=M_{4,1}=M_{2,6}=M_{6,2}=M_{7,8}=M_{8,7}=A,&\\
M_{0,5}=M_{3,5}=M_{9,5}=B,&\\
M_{5,0}=M_{5,3}=M_{5,9}=D.&
\end{array}
\]
All unlisted entries vanish identically. The six coordinates indexed by \(1,2,4,6,7,8\) are three invertible transposition blocks whenever \(A\ne0\). On the four remaining coordinates, define \(u=e_0+e_3+e_9\) and \(v=e_5\). The action of the displayed matrix is
\[
 M(u)=3D\,v,\qquad M(v)=B\,u,
\]
while \(e_0-e_3\) and \(e_0-e_9\) lie in its kernel. The displayed two-dimensional summand is therefore invertible precisely when \(BD\ne0\). The same invariant decomposition applies to the transpose matrix; Frobenius twists modify only the nonzero scalar coefficients, not the summands.

At \(t=0\), all three of \(A,B,D\) vanish, so the Hasse--Witt matrix is zero. At any smooth \(t\ne0\), the exclusions \(t\notin\{2,3,4\}\) guarantee \(A,B,D\ne0\). The matrix has rank \(6+2=8\) and decomposes into an eight-dimensional Frobenius-stable invertible summand plus a two-dimensional killed summand. Since every field automorphism twist of a nonzero scalar is again nonzero, **every semilinear Frobenius iterate has rank eight** on the nonzero smooth stratum. The stable rank is therefore eight, proving the \(5\)-rank formula. The \(a\)-number follows from \(a=10-\operatorname{rank}H\), and zero Hasse--Witt matrix at \(t=0\) gives the superspecial assertion.

## Verification
The supplementary stand-alone program `verify_hasse_sextic.py` uses Python's standard library only. It enumerates all multinomial terms of \(F_t^4\), checks every coefficient of the full symbolic \(10\times10\) matrix over \(\mathbf F_5[t]\), and compares it against the twelve-entry formula above. As a separate finite test it constructs \(\mathbf F_{25}\), checks the matrix ranks for all \(22\) smooth parameters in that field, and computes five iterated Frobenius-twisted products. Running

```shell
python3 verify_hasse_sextic.py
```

prints `SYMMETRIC_SEXTIC_CHAR5_HASSE_AND_STABLE_RANK_ALL_F25_SMOOTH_PARAMETERS_PASS`. The universal statements rest on the polynomial identity and invariant-block argument above, not on extrapolation from the finite-field test.

## Relationship to prior work
Fukasawa, Miura, and Takahashi, *Quasi-Galois points, II: Arrangements*, Section 4 and Theorems 4.1 and 4.3, study the characteristic-zero symmetry configuration and identify the distinguished sextic with parameter \(-10\). Their work also develops the general six-monomial form underlying this symmetric subfamily. It does not compute characteristic-five Hasse--Witt matrices or a Jacobian \(5\)-rank stratification. Borges and Gonçalves, *The p-rank of curves of Fermat type*, study p-ranks for Fermat-type covers \(y^m=x^n+1\) and other specific families. Their results describe important background but do not state the rank-eight formula for the varying mixed-monomial sextic above. Badr and Bars, *The stratification by automorphism groups of smooth plane sextic curves*, discuss the same distinguished sextic in their Remark 9.11, but their results concern automorphism groups in characteristic zero or characteristic greater than twenty-one and consequently do not imply any characteristic-five Hasse--Witt calculation. The superspecial behavior of the degree-six Fermat member in characteristic five is classical and is **not** claimed as new. The additional conclusion is the complete uniform non-Fermat stratum and the exact jump across it.

## Limitations
The classification is only in characteristic five and only for the displayed coefficient-marked plane-sextic family. It determines the \(5\)-rank and \(a\)-number, not the full Ekedahl--Oort type, Newton polygon, or complete zeta function. The three singular parameter fibers are excluded; their normalizations are not classified. No assertion is made about mixed-characteristic deformation, independent peer validation, or priority over all unindexed literature.

## References
1. S. Fukasawa, K. Miura, and T. Takahashi, *Quasi-Galois points, II: Arrangements*, arXiv:2211.16033, first public version November 29, 2022; especially Section 4, Theorems 4.1 and 4.3. https://arxiv.org/abs/2211.16033
2. H. Borges and C. Gonçalves, *The p-rank of curves of Fermat type*, arXiv:2212.03987, first public version December 7, 2022. https://arxiv.org/abs/2212.03987
3. T. Kodama and T. Washio, *Hasse-Witt matrices of Fermat curves*, Manuscripta Mathematica **60** (1988), 185–195. https://doi.org/10.1007/BF01161928
4. E. Badr and F. Bars, *The stratification by automorphism groups of smooth plane sextic curves*, Annali di Matematica Pura ed Applicata **204** (2025), 2005–2048, published online February 15, 2025; Remark 9.11 and hypotheses of Theorem 2.1. https://doi.org/10.1007/s10231-025-01558-z
5. Standard Hasse--Witt Čech-cohomology coefficient formula for smooth plane curves; its needed form is derived explicitly in the proof above.
