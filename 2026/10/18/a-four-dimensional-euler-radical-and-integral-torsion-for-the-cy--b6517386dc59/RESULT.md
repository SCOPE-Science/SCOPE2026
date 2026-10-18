# A four-dimensional Euler radical and integral torsion for the cyclic skew plane action

## Finding
For each integer \(n\ge3\) let \(\mu_n\) act on \(\mathbb A^2_{\mathbb C}\) by \(\zeta\cdot(x,y)=(\zeta x,\zeta^2y)\). The integer polar matrix \(H_n\) of its Euler quadratic form has nullity
\[
\dim_{\mathbb Q}\ker(H_n)=\begin{cases}1,&n\text{ odd},\\2,&n\text{ even and }6\nmid n,\\4,&6\mid n.\end{cases}
\]
For every integer \(k\ge1\), the *entire* integral cokernel in the maximal-radical family is
\[
\operatorname{coker}_{\mathbb Z}(H_{6k})\simeq\mathbb Z^4\oplus\mathbb Z/k\mathbb Z\oplus\mathbb Z/(3k)\mathbb Z.
\]
In particular, its torsion subgroup has order \(3k^2\). A cyclic action with unequal coordinate weights thus has a four-dimensional exceptional Euler radical at exactly the multiples of six, with explicit unbounded integral torsion.

## Assumptions and scope
The base field is \(\mathbb C\). Write \(e_i\) for the basis element of the integral character lattice \(\mathbb Z^n\) indexed by \(i\in\mathbb Z/n\mathbb Z\), and let \(S e_i=e_{i+1}\). The Euler quadratic form is the canonical form defined by Bachhuber--Gholampour's coefficient theorem, extended from representation multiplicities to the full character lattice. Its *integral polar form* is \(B_Q(a,b)=Q(a+b)-Q(a)-Q(b)\), not the associated half-polar symmetric matrix. The corresponding matrix is
\[
H_n=2I-S-S^{-1}-S^2-S^{-2}+S^3+S^{-3}.
\]
Terms are counted with multiplicity even when powers of \(S\) coincide at small \(n\). We make no assertion about the remaining torsion groups when \(6\nmid n\), nor about existence or components of individual moduli schemes.

## Proof
**Step 1: Euler matrix.** For the action of weights \(1,2\), the standard representation is \(\chi_1+\chi_2\) and the canonical character is \(\chi_3\). The coefficient theorem for the Euler quadratic form has positive pair weights \(\tfrac12\) at shifts \(\pm1,\pm2\) and negative pair weights \(-\tfrac12\) at shifts \(\pm3\), interpreted additively when some classes coincide. Polarizing \(Q\) gives precisely the displayed integer matrix.

**Step 2: Nullity.** Put
\[
f(t)=(t-1)^2(t+1)^2(t^2-t+1)=t^6-t^5-t^4+2t^3-t^2-t+1.
\]
The operator identity \(S^3H_n=f(S)\) follows by multiplication. Over \(\mathbb C\), the cyclic shift \(S\) has each \(n\)-th root of unity as a simple eigenvalue. The distinct complex roots of \(f\) are \(1,-1,e^{i\pi/3},e^{-i\pi/3}\). Among them, \(1\) always occurs, \(-1\) occurs precisely when \(2\mid n\), and both primitive sixth roots occur precisely when \(6\mid n\). Their numbers yield the claimed rational nullities. Root multiplicities in \(f\) do not multiply kernel dimensions, because \(S\) is diagonalizable.

**Step 3: Integral companion presentation.** The integer module \(\mathbb Z^n\) with cyclic shift corresponds to \(\mathbb Z[t]/(t^n-1)\). Multiplication by \(t^3\) is invertible in this ring; hence
\[
\operatorname{coker}(H_n)\cong\mathbb Z[t]/(t^n-1,f(t)).
\]
Since \(f\) is monic of degree six, \(R=\mathbb Z[t]/(f)\) is a free abelian group of rank six, in basis \(1,t,\dots,t^5\). Let \(C\) represent multiplication by \(t\) on \(R\). Therefore \(\operatorname{coker}(H_n)\cong\operatorname{coker}(C^n-I_6)\) as abelian groups, with no localization or rationalization.

**Step 4: Exact Smith factors for multiples of six.** Direct multiplication in the stated basis gives
\[
D=C^6-I_6=\begin{pmatrix}
-2&-1&-2&-1&-2&-1\\
1&-1&1&-1&1&-1\\
1&2&1&2&1&2\\
-2&-1&-2&-1&-2&-1\\
1&-1&1&-1&1&-1\\
1&2&1&2&1&2
\end{pmatrix}.
\]
Its square is zero, as is also forced by \(f(t)\mid(t^6-1)^2\). Consequently \(C^{6k}-I_6=(I_6+D)^k-I_6=kD\) for *every* integer \(k\ge1\). The matrix \(D\) has rank two; its entries have greatest common divisor one; and its nonzero \(2\times2\) minors have greatest common divisor three. Indeed, it has only two column types, with nonzero minors of magnitude three, and at least one entry of magnitude one. Its Smith form is thus \(\operatorname{diag}(1,3,0,0,0,0)\), so that \(kD\) has Smith form \(\operatorname{diag}(k,3k,0,0,0,0)\). The claimed abelian group decomposition follows.

## Verification
The accompanying `verify.py` uses only Python's standard library. It checks the companion-matrix identity, \(D^2=0\), rank and determinantal divisors exactly; repeats the multiplication identity for \(1\le k\le12\); and computes rational nullity of \(H_n\) exactly for \(3\le n\le60\). Execution: `python3 verify.py`. These bounded computations are auxiliary reproducibility checks: the factorization, companion reduction and square-zero argument above establish the universal statements for all indicated integers.

## Relationship to prior work
Bachhuber and Gholampour, *G-Equivariant Hilbert Schemes and Quadratic Forms*, arXiv:2610.12736v1 (posted 2026-10-08), Theorem 4.6, supplies the Euler-form coefficients for all abelian planar quotient stacks and their classification. Those general coefficient statements imply the starting matrix; in the inspected main text they do not give the integral cokernel or these nullity and sixth-divisibility conclusions. Telloni and Williams study Smith forms for circulant polynomial matrices by related general techniques; their featured theorem restricts associated polynomials to the squarefree case, whereas this \(f(t)\) has repeated roots. Williams' classification of Smith forms of selected circulant graph adjacency matrices likewise does not directly provide this signed Euler-form cokernel. These works motivate the exact integral question but cannot alone be taken as novelty certificates.

## Limitations
This establishes the nullity for all \(n\ge3\) and the full integral cokernel only when \(6\mid n\). The result is an arithmetic classification of a specific Euler lattice and does not give freeness of the associated moduli spaces, a general result for other coordinate weights, or the Smith groups for nonmultiples of six. An equivalent integer-circulant calculation could appear in older or unindexed literature; no uniqueness or independent validation is claimed.

## References
- S. J. Bachhuber and A. Gholampour, *G-Equivariant Hilbert Schemes and Quadratic Forms*, arXiv:2610.12736v1 (2026-10-08), especially Theorem 4.6 and Sections 6--7. https://arxiv.org/html/2610.12736v1
- A. I. Telloni and G. Williams, *Smith forms of circulant polynomial matrices* (2014 preprint). https://repository.essex.ac.uk/9703/1/TelloniWilliams-SmithFormsCirculants.pdf
- G. Williams, *Smith forms for adjacency matrices of circulant graphs*, Linear Algebra Appl. 443 (2014), 21--33. https://repository.essex.ac.uk/8578/
