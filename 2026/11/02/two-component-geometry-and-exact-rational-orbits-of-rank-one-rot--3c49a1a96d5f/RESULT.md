# Two-component geometry and exact rational orbits of rank-one Rota–Baxter operators on \(\mathfrak{sl}_2\)

## Finding
Let \(k\) be any field of characteristic different from \(2\), and put \(\mathfrak g=\mathfrak{sl}_2(k)\). A weight-zero Lie Rota–Baxter operator is a linear map \(R:\mathfrak g\to\mathfrak g\) satisfying
\[
[R(x),R(y)]=R([R(x),y]+[x,R(y)])\qquad(x,y\in\mathfrak g).
\]
Let \(\mathcal R_1\) be the **reduced projective variety** of nonzero rank-one such operators in \(\mathbb P(\operatorname{End}(\mathfrak g))\). Then \(\mathcal R_1\) has exactly two geometrically irreducible smooth surfaces: a diagonal Veronese surface \(D\simeq\mathbb P^2_k\), and a tangent-incidence surface \(F\simeq\mathbb P^1_k\times\mathbb P^1_k\). Their reduced intersection is a smooth conic \(D\cap F\simeq\mathbb P^1_k\); this intersection is exactly the singular locus of the reduced union as a set. All identifications are over \(k\).

For every odd prime power \(q\), the number of **nonzero rank-one** weight-zero Lie Rota–Baxter operators on \(\mathfrak{sl}_2(\mathbb F_q)\), as actual linear maps, is
\[
\boxed{(q-1)(2q^2+2q+1)=2q^3-q-1.}
\]
Conjugation by \(\operatorname{Aut}(\mathfrak g)\simeq\operatorname{PGL}_2(\mathbb F_q)\) partitions these maps into exactly \(2q+1\) orbits: one orbit of size \(q(q^2-1)\); for each nonzero \(\tau\in\mathbb F_q\), one orbit of size \(q(q+1)/2\) and one of size \(q(q-1)/2\); and two orbits each of size \((q^2-1)/2\). These are all the orbits, with no exceptional odd characteristic.

## Assumptions and scope
Set \(B(x,y)=\operatorname{tr}(xy)\), a nondegenerate invariant symmetric bilinear form on \(\mathfrak g\) when \(\operatorname{char}k\ne2\). A nonzero rank-one endomorphism can be written as
\[
R_{v,w}(x)=B(w,x)v,\qquad v,w\in\mathfrak g\setminus\{0\}.
\]
The ordered pair is unique up to \((v,w)\mapsto(cv,c^{-1}w)\) for \(c\in k^\times\); its projective class corresponds uniquely to the pair of projective lines \(([v],[w])\in\mathbb P(\mathfrak g)\times\mathbb P(\mathfrak g)\). Thus the projectivized rank-one locus is canonically a closed reduced subvariety of the Segre variety. The theorem does **not** classify rank-two or rank-three Rota–Baxter operators, the zero operator, the nonreduced defining scheme, or characteristic-two operators.

Put \(Q=\{[w]\in\mathbb P(\mathfrak g):B(w,w)=0\}\). In matrix coordinates
\[
w=\begin{pmatrix}a&b\\c&-a\end{pmatrix},\qquad Q:\ a^2+bc=0.
\]
This is a smooth split conic. The two reduced components in the Segre coordinates are exactly
\[
D=\{([v],[w]):[v]=[w]\},\qquad
F=\{([v],[w]):[w]\in Q,\ B(v,w)=0\}.
\]
The second condition says that \([v]\) lies on the projective tangent line to \(Q\) at \([w]\).

## Proof
**1. Reduction of the operator equation.** Since \([v,v]=0\), substituting \(R_{v,w}\) into the Rota–Baxter identity gives, for every \(x,y\),
\[
0=\bigl(B(w,x)B(w,[v,y])-B(w,y)B(w,[v,x])\bigr)v.
\]
By trace invariance, \(B(w,[v,y])=B([w,v],y)\). As \(B(w,-)\) is a nonzero functional, the vanishing of this alternating wedge is equivalent to \(B([w,v],-)=\lambda B(w,-)\) for some scalar \(\lambda\). Nondegeneracy therefore gives the exact criterion
\[
\boxed{R_{v,w}\text{ is Rota–Baxter}\iff [w,v]\in kw.}
\]
No classification theorem is assumed in this reduction.

**2. The two incidence possibilities.** If \([w,v]=0\), the centralizer of any nonzero traceless \(2\times2\) matrix \(v\) in \(\mathfrak{sl}_2(k)\) is exactly \(kv\): its associative centralizer is \(kI+kv\), and the trace equation removes the scalar matrix because \(2\ne0\). Hence \([w]=[v]\), the diagonal surface \(D\).

Otherwise \([w,v]=\lambda w\) with \(\lambda\ne0\). Invariance yields
\[
\lambda B(w,w)=B([w,v],w)=0,
\qquad\lambda B(w,v)=B([w,v],v)=0.
\]
So \([w]\in Q\) and \(B(v,w)=0\). Conversely, every nonzero nilpotent traceless matrix \(w\) is conjugate over \(k\) to the matrix unit \(E_{12}\). In that basis \(w^\perp=\langle E_{12},\operatorname{diag}(1,-1)\rangle\), and this two-plane normalizes the line \(kw\). Thus \(B(v,w)=0\) and \(B(w,w)=0\) imply \([w,v]\in kw\). This proves the exact reduced set-theoretic decomposition \(\mathcal R_1=D\cup F\), with both constituents defined by explicit algebraic incidence equations.

**3. Geometry.** The diagonal is \(\mathbb P^2\) and becomes its quadratic Veronese embedding under the Segre map. The split conic \(Q\) is the Veronese image of \(\mathbb P^1\). Via the characteristic-not-two identification of traceless matrices with binary quadratic forms, \([w]\in Q\) means \(w\) is a square \(\ell^2\), while its polar tangent line consists exactly of quadratic forms \(\ell m\). Therefore the morphism
\[
\mathbb P^1\times\mathbb P^1\longrightarrow F,
\qquad ([\ell],[m])\longmapsto([\ell m],[\ell^2])
\]
is an isomorphism, including on its diagonal. Its diagonal \([m]=[\ell]\) is exactly \(D\cap F\simeq Q\). Both components are smooth, their intersection is smooth, and a reduced union of distinct smooth components is singular along their nonempty intersection and smooth off it. Thus the reduced singular locus has underlying set \(Q\). We make no claim about multiplicities of the unreduced operator-equation scheme.

**4. Finite-field counts.** Over \(\mathbb F_q\) with \(q\) odd, \(D\) has \(q^2+q+1\) projective points, \(F\) has \((q+1)^2\), and \(D\cap F\) has \(q+1\). Inclusion–exclusion gives \(2q^2+2q+1\) projective rank-one maps. Each such line of endomorphisms has exactly \(q-1\) nonzero operators, proving the stated \(2q^3-q-1\) formula without extrapolation from computations.

**5. Exact conjugacy-orbit spectrum.** The rational automorphism group is \(\operatorname{PGL}_2(\mathbb F_q)\), acting by conjugation. Decompose the set into the disjoint strata \(F\setminus D\), \(D\setminus Q\), and \(Q\).

On \(F\setminus D\), the ordered binary linear factors \(([\ell],[m])\) are distinct. The projective-linear group acts transitively on ordered pairs of distinct points of \(\mathbb P^1\); their stabilizer is a split torus. For the representative \(R(x)=B(E_{12},x)\operatorname{diag}(1,-1)\), conjugation by \(\operatorname{diag}(t,1)\) scales \(R\) by every \(t\in\mathbb F_q^\times\). Hence all \((q-1)q(q+1)=q(q^2-1)\) actual operators on this stratum form one free orbit.

On \(D\setminus Q\), all operators have the form \(R(x)=cB(v,x)v\) with \(B(v,v)\ne0\), and their nonzero endomorphism trace \(\tau=\operatorname{tr}(R)=cB(v,v)\) is conjugation-invariant. Nonisotropic projective lines \([v]\) comprise exactly two \(\operatorname{PGL}_2(\mathbb F_q)\)-orbits: split and nonsplit characteristic polynomials, equivalently the two square classes of \(v^2\). The line stabilizer sends a representative \(v\) to \(\pm v\), hence fixes the coefficient fiber. For every \(\tau\ne0\) there is exactly one orbit in each class. Counting split and nonsplit nonisotropic lines gives the sizes \(q(q+1)/2\) and \(q(q-1)/2\), respectively.

Finally \(Q(\mathbb F_q)\) is one orbit of \(q+1\) nilpotent projective lines. A stabilizer of \([E_{12}]\) scales \(E_{12}\) by every \(t\in\mathbb F_q^\times\), so it scales the symmetric rank-one operator \(B(E_{12},-)E_{12}\) by \(t^2\). There are exactly two coefficient-square-class orbits, each of size \((q+1)(q-1)/2\). Adding all orbit counts produces \(2q+1\) orbits and recovers the total count, completing the classification.

For explicit representatives, take \(h=\operatorname{diag}(1,-1)\), \(e=E_{12}\), fix any nonsquares \(\delta,\eta\in\mathbb F_q^\times\), and put \(v_\delta=\begin{pmatrix}0&\delta\\1&0\end{pmatrix}\). Every orbit is represented uniquely by one entry of the following table, where \(\tau\in\mathbb F_q^\times\):

| Representative \(R(x)\) | Parameter choices | Orbit size |
| --- | --- | --- |
| \(B(e,x)h\) | one | \(q(q^2-1)\) |
| \(\tfrac{\tau}{2}B(h,x)h\) | \(q-1\) nonzero values of \(\tau\) | \(q(q+1)/2\) each |
| \(\tfrac{\tau}{2\delta}B(v_\delta,x)v_\delta\) | \(q-1\) nonzero values of \(\tau\) | \(q(q-1)/2\) each |
| \(B(e,x)e\), \(\eta B(e,x)e\) | two square classes | \((q^2-1)/2\) each |


## Verification
The standalone file `check_rankone_sl2_rb.py` implements the standard \(E_{12},E_{21},H\) Lie bracket directly over \(\mathbb F_3,\mathbb F_5,\mathbb F_7\) and the genuine degree-two extension \(\mathbb F_9=\mathbb F_3[t]/(t^2+1)\). It enumerates all pairs of projective lines and checks that the original Rota–Baxter identity is equivalent to both the commutator-line criterion and the two-component incidence criterion. All predicted component counts and nonzero rank-one map counts agree. Over \(\mathbb F_3\) and \(\mathbb F_5\), it also computes every orbit by explicit conjugation with all elements of \(\operatorname{PGL}_2\) and checks the predicted orbit-size multisets. Its complete output is `check_rankone_sl2_rb.txt`.

The finite checks establish the reported small-field data only; the arbitrary-field surface decomposition and all-odd-prime-power formulas follow from the preceding proof.

## Relationship to prior work
Pei, Bai and Guo (arXiv:1311.0612, first version November 4, 2013), Section 2 and Theorem 2.1, classify all weight-zero Lie Rota–Baxter operators on \(\mathfrak{sl}_2(\mathbb C)\) through 22 explicit matrix forms up to scalar multiplication. That is stronger in **operator rank coverage** over \(\mathbb C\); its complex-field matrix classification is not claimed here as new. It does not give the rational-point count over arbitrary odd finite fields, the \(\operatorname{PGL}_2(\mathbb F_q)\) orbit-size distribution, or the split two-surface incidence model over every field of characteristic different from two. The present theorem derives those invariants directly from the rank-one equation, without treating complex parameter lists as finite-field classifications.

Pei, Bai and Guo (arXiv:1306.3046, first version June 13, 2013) develop Rota–Baxter operators on operads, a general framework rather than a finite-field rank-one orbit census. Burde and Gubarev (arXiv:1805.05104, 2018) study weight-one Rota–Baxter and post-Lie structures on semisimple Lie algebras, a different weight and enumeration problem. The latter is contextual and not the archival source governing this slot.

## Limitations
The result deliberately concerns **nonzero rank-one** weight-zero Lie Rota–Baxter operators, not all ranks. The geometric statement refers to the **reduced** projective solution locus, not to the nilpotent or embedded structure of the polynomial-equation scheme; its singular-locus statement is set-theoretic. The characteristic-two case is excluded because the trace pairing becomes degenerate and \(\mathfrak{sl}_2\) ceases to have the same structure. The explicit orbit classification requires odd finite fields; for arbitrary characteristic-not-two fields only the geometric part is asserted.

## References
1. J. Pei, C. Bai, and L. Guo, *Rota-Baxter operators on \(\mathfrak{sl}(2,\mathbb C)\) and solutions of the classical Yang-Baxter equation*, arXiv:1311.0612v1 (2013-11-04), Section 2, Theorem 2.1. https://arxiv.org/abs/1311.0612
2. J. Pei, C. Bai, and L. Guo, *Splitting of operads and Rota-Baxter operators on operads*, arXiv:1306.3046v1 (2013-06-13). https://arxiv.org/abs/1306.3046
3. D. Burde and V. Gubarev, *Rota--Baxter operators and post-Lie algebra structures on semisimple Lie algebras*, arXiv:1805.05104v1 (2018-05-14). https://arxiv.org/abs/1805.05104
