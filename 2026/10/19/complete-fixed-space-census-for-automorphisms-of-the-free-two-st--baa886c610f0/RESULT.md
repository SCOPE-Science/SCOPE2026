# Complete fixed-space census for automorphisms of the free two-step Lie algebra on three generators

## Finding

Let \(q\) be any prime power, let \(V=\mathbb F_q^3\), and let \(L=V\oplus\bigwedge^2 V\) carry the two-step nilpotent Lie bracket \([v+w,v'+w']=v\wedge v'\). Thus \(L\) is the six-dimensional free two-step nilpotent Lie algebra on three generators. For \(0\le d\le6\), define
\[
F_{q,d}=\#\{\phi\in\operatorname{Aut}_{\mathbb F_q}(L):\dim\ker(\phi-I_L)=d\},\qquad
\mathcal F_q(T)=\sum_{d=0}^6 F_{q,d}T^d.
\]
The following finite formulas determine every coefficient of \(\mathcal F_q(T)\) using only \(q\), finite sums, and products; they apply without a restriction on characteristic.

Set
\[
z=q^2+q+1,\quad
S=q^3(q^3-1)(q^2-1),\quad
U=zq^3(q^2-1),\quad V_0=zq^2,\quad B=zq^2(q^2-1).
\]
(The auxiliary letter \(V_0\) is a number, not the vector space \(V\).) Define \(D_2=z(q^2-1)\), \(D_1=U-(q+1)D_2-z\), and \(D_0=S-D_1-D_2-1\). Define a finite table \(D(a,c)\), with unspecified entries zero, by
\[
D(0,0)=D_0,\quad D(1,1)=D_1,\quad D(2,2)=D_2,\quad D(3,3)=1.
\]
For \(e\in\{0,1\}\), put
\[
a_1=U-(q+1)V_0,\quad c_1=a_1+qze,\quad c_2=V_0-ze,\quad c_3=e
\]
and define \(E_e(a,c)\), again zero outside the displayed positions, by
\[
\begin{array}{c|c}
(a,c)&E_e(a,c)\\\hline
(0,0)&S-a_1-c_1+B-c_2-c_3\\
(0,1)&c_1-V_0-B\\
(0,2)&c_2\\
(0,3)&c_3\\
(1,0)&a_1-B\\
(1,1)&B\\
(2,1)&V_0
\end{array}.
\]
Write \(\epsilon_q=1\) if \(q\) is odd and \(\epsilon_q=0\) if \(q\) is even, and set
\[
P_q(a,c)=D(a,c)+(q-2-\epsilon_q)E_0(a,c)+\epsilon_q E_1(a,c).
\]
For \(0\le t\le\min(a,c)\), let
\[
R_q(a,c,t)=\binom{a}{t}_q\binom{c}{t}_q
\prod_{i=0}^{t-1}(q^t-q^i),
\]
where the Gaussian binomial coefficients have their usual finite-subspace-count meaning, and an empty product equals \(1\). Then the complete answer is
\[
\boxed{\mathcal F_q(T)=
\sum_{a=0}^3\sum_{c=0}^3 P_q(a,c)q^{9-ac}
\sum_{t=0}^{\min(a,c)}R_q(a,c,t)T^{a+c-t}.}
\]
Every integer dimension \(d=0,1,\ldots,6\) occurs for every prime power \(q\). In particular, the number of **fixed-point-free automorphisms** (those fixing only \(0\)) has the closed form
\[
\boxed{F_{q,0}=q^{12}\big(q^6-3q^5+q^4+4q^3+q^2-3q-8-\epsilon_q\big).}
\]
The parity term arises from the scalar transformation \(-I_V\), whose exterior-square action is the identity when \(q\) is odd. Two normalization identities are
\[
\mathcal F_q(1)=q^9|\mathrm{GL}_3(\mathbb F_q)|,
\qquad \sum_{d=0}^6 q^dF_{q,d}=3q^9|\mathrm{GL}_3(\mathbb F_q)|.
\]
For instance,
\[
\mathcal F_2(T)=24576+25088T+29120T^2+6216T^3+966T^4+49T^5+T^6.
\]

## Assumptions and scope

The algebra is the **free** nilpotent Lie algebra of class exactly two on three generators, over \(\mathbb F_q\). The Lie bracket is alternating, also in characteristic two; no division by two or identification with a group via the Baker–Campbell–Hausdorff formula is used. The counted objects are individual \(\mathbb F_q\)-linear Lie automorphisms, rather than conjugacy classes or automorphisms of an associated finite group. The fixed space means the kernel of \(\phi-I_L\) as an ordinary linear map on all six dimensions. The finite-field parameter ranges through every prime power, including nonprime extension fields.

## Proof

**1. Exhaustive automorphism coordinates.** The commutator subalgebra is exactly \(\bigwedge^2V\) and is characteristic. Every automorphism induces some \(g\in\mathrm{GL}(V)\) on \(L/[L,L]\), and conversely any \(g\in\mathrm{GL}(V)\), together with any \(f\in\mathrm{Hom}(V,\bigwedge^2V)\), defines the unique automorphism
\[
\phi_{g,f}=\begin{pmatrix}g&0\\f&\bigwedge^2g\end{pmatrix}
\]
in the chosen direct-sum coordinates. Indeed, bracket preservation forces the lower-right block to be \(\bigwedge^2g\), and the image of any generating basis may have arbitrary central additions. Its determinant is nonzero. There are \(q^9|\mathrm{GL}_3(\mathbb F_q)|\) automorphisms.

**2. Fixed-space reduction.** For each \(g\) let
\[
a=\dim\ker(g-I_V),\qquad
c=\dim\ker((\bigwedge^2g)-I_{\wedge^2V}).
\]
Put \(U_g=\ker(g-I_V)\) and \(W_g=(\bigwedge^2V)/\operatorname{im}((\bigwedge^2g)-I)\). By rank-nullity, \(\dim W_g=c\). The natural map from \(\operatorname{Hom}(V,\bigwedge^2V)\) to \(\operatorname{Hom}(U_g,W_g)\), obtained by restricting \(f\) and taking the quotient, is surjective. Its fibers all have \(q^{9-ac}\) elements. If the resulting map has rank \(t\), solving \(\phi_{g,f}(v,w)=(v,w)\) shows that \(v\) lies in its kernel (dimension \(a-t\)) and \(w\) has a \(c\)-dimensional affine choice for each such \(v\). Thus \(\dim\ker(\phi_{g,f}-I_L)=a+c-t\). The number of rank-\(t\) maps between spaces of dimensions \(a,c\) is exactly \(R_q(a,c,t)\).

**3. Reducing the two eigenvalue conditions.** The exterior pairing yields the canonical \(\mathrm{GL}(V)\)-equivariant identification \(\bigwedge^2V\simeq V^*\otimes\det V\). Consequently \(\bigwedge^2g\) has the same fixed-space dimension as \(\det(g)g^{-\mathsf T}\), and therefore
\[
c=\dim\ker(g-\det(g)I_V).
\]
This equality is valid in characteristic two. It reduces the question to joint eigenspace dimensions for the eigenvalues \(1\) and \(\det(g)\) inside \(\mathrm{GL}_3(\mathbb F_q)\).

**4. Pointwise fixed-subspace moments.** Fix a nonzero determinant \(\lambda\). Exactly \(S=|\mathrm{SL}_3(\mathbb F_q)|\) matrices have this determinant. For any prescribed scalar eigenvalue \(\mu\in\{1,\lambda\}\), let \(b=\dim\ker(g-\mu I_V)\). Counting pairs consisting of such a matrix and a pointwise scalar-\(\mu\) eigenspace of dimension one or two gives
\[
\sum_{\det g=\lambda}\binom b1_q=zq^2|\mathrm{SL}_2(\mathbb F_q)|=U,
\qquad
\sum_{\det g=\lambda}\binom b2_q=zq^2=V_0.
\]
To see the first identity, choose one of the \(z\) lines, then a block matrix with prescribed scalar on that line: there are \(q^2\) cross-block choices and \(|\mathrm{SL}_2(\mathbb F_q)|\) quotient blocks of the required determinant. The second follows analogously for a fixed plane, with a unique quotient scalar. The dimension-three contribution is one precisely when \(\mu^3=\lambda\) and \(g=\mu I_V\). For \(\lambda=1\), the two eigenvalues coincide and \(a=c\); binomial inversion gives the four entries of \(D\).

For \(\lambda\ne1\), the eigenvalue \(1\) has possible eigenspace dimensions \(a\in\{0,1,2\}\), whose multiplicities at dimensions two and one are \(V_0\) and \(a_1\). For the eigenvalue \(\lambda\), the dimension-three contribution is \(e=1\) exactly when \(\lambda=-1\ne1\), so its dimension-two and dimension-one multiplicities are \(c_2=V_0-ze\) and \(c_1=a_1+qze\). The only matrices simultaneously having both eigenspaces nonzero have Jordan decomposition either \(I_2\oplus(\lambda)\) or \(J_2(1)\oplus(\lambda)\). Their \(\mathrm{GL}_3\)-conjugacy-class sizes are respectively
\[
\frac{|\mathrm{GL}_3|}{|\mathrm{GL}_2|(q-1)}=V_0,
\qquad
\frac{|\mathrm{GL}_3|}{q(q-1)^2}=B.
\]
This class-size calculation remains valid over characteristic two because \(\lambda\ne1\). Subtracting these two intersections from the marginal eigenspace multiplicities gives **all seven** entries of \(E_e\); there are no other possible pairs \((a,c)\). When \(q\) is odd exactly one nonidentity determinant equals \(-1\), and otherwise no such determinant exists. The remaining number of nonidentity determinants is \(q-2-\epsilon_q\). This establishes the table \(P_q(a,c)\) and then, using Step 2, the claimed rank-distribution formula.

**5. Closed coefficient, positivity, and normalization.** Fixed-point-freeness requires \(a=c=0\) because \(a+c-t\ge\max(a,c)\), so \(F_{q,0}=q^9P_q(0,0)\). Direct substitution and collection of the displayed finite terms gives the closed polynomial stated above. All table entries count matrices, hence are nonnegative integers, and each \(R_q(a,c,t)\) counts linear maps. Summing all coefficients gives \(q^9|\mathrm{GL}_3|\). Every dimension from zero to six occurs: the identity matrix \(g\), suitable central shears \(f\), and representatives with \((a,c)=(0,0)\) and \((1,1)\) realize the indicated degrees directly (the finite formula also gives strictly positive coefficients for all prime powers). Finally \(\operatorname{Aut}(L)\) has exactly three orbits on the elements of \(L\): zero, nonzero central elements, and noncentral elements. The action on nonzero bivectors is transitive, while an arbitrary central shear moves any noncentral vector through its entire central fiber. Burnside's lemma therefore gives the weighted normalization identity.

## Verification

The standalone Python 3 script `verify.py` uses only the standard library. Invoke `python3 verify.py` in the directory containing this document and that script. It exhaustively enumerates every invertible \(3\times3\) matrix over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_4\) to compare the complete table \(P_q(a,c)\) with independent Gaussian elimination, and independently checks the exterior-square fixed-space identity. It additionally enumerates **all** automorphisms of \(L\) over \(\mathbb F_2\) (\(168\cdot 2^9=86016\)) and compares all seven coefficients with direct rank computation of the six-dimensional automorphism matrix. Exact arithmetic checks cover eleven further prime-power field orders, including odd and even characteristics; those are consistency checks, not exhaustive matrix enumeration beyond the stated sizes. The expected success marker is `VERIFY_OK_FREE_CLASS2_FIXEDSPACE_CENSUS`. The proof, not the finite computation, covers the general theorem.

## Relationship to prior work

Kofinas, Metaftsis, and Papistas (2009) treat relatively free nilpotent groups and their Lie algebras in characteristic zero; their discussion of free generators supplies historical context but not finite-field fixed-space counts. Kofinas and Papistas (2010) investigate generation of automorphism groups of relatively free nilpotent Lie algebras over \(\mathbb Q\). Benito and Roldán-López (2019), in their Proposition 1 and Corollary 1 and subsequent examples, explicitly parametrize automorphisms of free nilpotent Lie algebras by maps on generators, over characteristic-zero fields. The present arithmetic refinement counts the fixed-space dimension of **every** automorphism for a specific free six-dimensional algebra and every finite field, including characteristic two. Earlier counts for the three-dimensional Heisenberg Lie algebra concern a different Lie algebra (two generators and a one-dimensional commutator), and therefore do not supply this distribution. The base automorphism parametrization itself is not claimed as new.

## Limitations

The formula is specific to rank three and nilpotency class two; it does not count conjugacy classes, groups obtained by exponentiation, or fixed spaces for arbitrary quotients of free Lie algebras. The result is a same-document mathematical derivation supported by finite computations, not an independently refereed theorem. An equivalent count may exist in earlier finite linear group or modular Lie automorphism literature under another formulation. A relevant 2010 primary article was accessible only through its abstract in this examination; no claim of exclusion based on its full text is made. The displayed finite enumeration is not treated as proof for arbitrary prime powers.

## References

1. C. Kofinas, V. Metaftsis, and A. I. Papistas, *Relatively free nilpotent torsion-free groups and their Lie algebras*, arXiv:0903.1573, first posted 2009-03-09, https://arxiv.org/pdf/0903.1573.
2. C. E. Kofinas and A. I. Papistas, *Automorphisms of Relatively Free Nilpotent Lie Algebras*, Communications in Algebra 38 (2010), 1575–1593, https://doi.org/10.1080/00927870903004360.
3. P. Benito and J. Roldán-López, *Derivations and automorphisms of free nilpotent Lie algebras and their quotients*, arXiv:1911.01897, first posted 2019-11-05, https://arxiv.org/pdf/1911.01897.
4. R. M. Bryant and A. I. Papistas, *On the fixed points of a finite group acting on a relatively free Lie algebra*, Glasgow Mathematical Journal 42 (2000), 167–181, https://doi.org/10.1017/S0017089500020024.
