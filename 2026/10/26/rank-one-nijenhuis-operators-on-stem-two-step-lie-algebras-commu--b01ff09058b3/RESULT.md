# Rank-one Nijenhuis operators on stem two-step Lie algebras: commutator-rank census

## Finding
Let \(k=\mathbb F_q\) and let \(\mathfrak g\) be a finite-dimensional **stem two-step nilpotent Lie algebra**: its center \(Z\) equals its nonzero derived algebra \([\mathfrak g,\mathfrak g]\). Write \(d=\dim(\mathfrak g/Z)\ge2\), \(c=\dim Z\ge1\), and \(D=d+c\). For every \(0\ne b\in Z^*\), the commutator defines the alternating form
\[
B_b(\bar x,\bar y)=b([x,y]),\qquad r_b=\operatorname{rank}B_b.
\]
The exact number of nonzero vector-space-rank-one Nijenhuis operators is
\[
\boxed{\mathcal N_1(\mathfrak g;q)=\frac{(q^d-1)(q^D-1)+q^d\sum_{0\ne b\in Z^*}(q^{D-r_b-1}-1)}{q-1}.}
\]
Moreover, exactly \((q^d-1)q^{D-1}\) of these have nonzero square. The formula is intrinsic: it depends only on the rank distribution of the commutator pencil \(\{B_b:b\in Z^*\}\), the field order, and the two dimensions.

For the free two-step algebra \(\mathfrak f_{d,2}=V\oplus\Lambda^2 V\), \(d\ge2\), put \(c=\binom d2\), \(D=d+c\), and
\[
A_{d,s}(q)={d\brack2s}_q q^{s(s-1)}\prod_{j=1}^s(q^{2j-1}-1), \qquad 1\le s\le\lfloor d/2\rfloor.
\]
Here \({d\brack 2s}_q\) is the Gaussian binomial coefficient. A closed formula without a pencil enumeration is
\[
\boxed{\mathcal N_1(\mathfrak f_{d,2};q)=\frac{(q^d-1)(q^D-1)+q^d\sum_{s=1}^{\lfloor d/2\rfloor}A_{d,s}(q)(q^{D-2s-1}-1)}{q-1}.}
\]
For example, the free rank-three example has \(833\) such operators over \(\mathbb F_2\), including \(224\) with nonzero square. It is not inferred from finite extrapolation.

## Assumptions and scope
A Lie Nijenhuis operator is a linear map \(N\colon\mathfrak g\to\mathfrak g\) satisfying, for **every** \(x,y\in\mathfrak g\),
\[
[Nx,Ny]=N([Nx,y]+[x,Ny]-N[x,y]).
\]
The Lie bracket is alternating, also in characteristic two. Vector-space rank one means \(N\ne0\) with one-dimensional image. Throughout, \(q\) is any prime power; no odd-characteristic assumption is used. For the criterion below a vector-space complement \(\mathfrak g=V\oplus Z\) may be chosen, but the resulting classification is independent of this choice.

## Proof
**1. Reduction to a scalar two-form.** Every nonzero rank-one linear map is \(N(x)=f(x)w\) with \(0\ne f\in\mathfrak g^*\), \(0\ne w\in\mathfrak g\). Two ordered pairs determine the same map exactly when \((f,w)\mapsto(af,a^{-1}w)\) for \(a\in k^\times\). Define \(g(y)=f([w,y])\), \(h(x,y)=f([x,y])\), and \(\lambda=f(w)\). Since \([w,w]=0\), the displayed Nijenhuis identity is equivalent, for all \(x,y\), to
\[
f(x)g(y)-f(y)g(x)=\lambda h(x,y). \tag{1}
\]
This is an identity of alternating bilinear forms, not merely a test on chosen vectors.

**2. Exact case split.** If \(f|_Z=0\), then \(f([\mathfrak g,\mathfrak g])=0\), hence \(g=h=0\). Equation (1) holds for **every** \(w\ne0\). Suppose instead \(b=f|_Z\ne0\). Since \(Z=[\mathfrak g,\mathfrak g]\), the form \(h\ne0\). Choose \(z_0\in Z\) with \(f(z_0)\ne0\), and substitute \(x=z_0\) into (1). Both \(g(z_0)\) and \(h(z_0,y)\) vanish because \(Z\) is central; thus \(g(y)=0\) for all \(y\). Substitution into (1), using \(h\ne0\), gives \(\lambda=0\). Conversely, \(g=0\) and \(\lambda=0\) imply (1). With \(w=v+z\) in \(V\oplus Z\), the equality \(g=0\) is exactly \(v\in\operatorname{rad}(B_b)\), while \(\lambda=0\) means \(f(w)=0\). This proves necessity and sufficiency without assuming a field characteristic. The second class has \(N^2(x)=f(x)f(w)w=0\).

**3. Count the two classes.** There are \(q^d-1\) nonzero \(f\) annihilating \(Z\), and for each such \(f\) there are \(q^D-1\) nonzero \(w\). For fixed \(b\ne0\), there are \(q^d\) linear extensions \(f\) of \(b\). The subspace \(\operatorname{rad}B_b\oplus Z\) has dimension \(d-r_b+c=D-r_b\), and \(f\) restricts to a nonzero functional on it because \(b\ne0\). Its kernel therefore has \(q^{D-r_b-1}\) elements, of which one is zero. Divide both case totals by \(q-1\) for the free scalar action on parameter pairs. This proves the main formula.

Only the first class can have nonzero square. For every \(f\ne0\) annihilating \(Z\), exactly \((q-1)q^{D-1}\) choices of \(w\) satisfy \(f(w)\ne0\). Dividing by \(q-1\) yields \((q^d-1)q^{D-1}\).

**4. The free case.** For \(\mathfrak f_{d,2}\), the central dual is \((\Lambda^2V)^*\), the space of alternating forms on \(V\). An alternating form of rank \(2s\) has a radical of dimension \(d-2s\). There are \({d\brack 2s}_q\) choices of this radical, and after quotienting by it the number of nondegenerate alternating forms on a \(2s\)-space is
\[
|\operatorname{GL}_{2s}(q)|/|\operatorname{Sp}_{2s}(q)|=q^{s(s-1)}\prod_{j=1}^{s}(q^{2j-1}-1).
\]
The formula also holds for characteristic two because these forms are alternating, not arbitrary skew-symmetric matrices. Partition the nonzero \(b\) by rank and substitute to obtain the closed Gaussian-binomial expression.

## Verification
The included standalone `verify_rankone_nijenhuis.py` enumerates **all** nonzero parameter pairs \((f,w)\) in six small prime-field examples. It checks the Nijenhuis torsion independently on every basis pair, then compares the resulting operator counts after scalar quotienting with the rank-pencil formula. A seventh exhaustive case over \(\mathbb F_5\) is also checked. Verified totals include \(21\) on the three-dimensional Heisenberg algebra over \(\mathbb F_2\), \(833\) on the free rank-three class-two algebra over \(\mathbb F_2\), \(289\) on a five-dimensional two-center example over \(\mathbb F_2\), and \(4010\) on that example over \(\mathbb F_3\). The checker also independently verifies the non-square-zero counts. These finite checks corroborate but do not prove the general result. The four-step algebraic argument above covers all prime powers and all indicated stem algebras.

## Relationship to prior work
Liu–Sheng–Zhou–Bai (2016, arXiv:1601.02356v1) provides general Nijenhuis-operator theory and constructions on \(n\)-Lie algebras. Its available full text was inspected through its setup, construction sections, and examples; it does not state a finite-field rank-one census for stem class-two ordinary Lie algebras. Fulman–Goldstein (arXiv:1211.0504, first posted 2012) studies rank distributions of finite-field matrices, including alternating forms, but not Nijenhuis operators on Lie algebras. Their matrix-rank ingredients, and the classical symplectic orbit formula, are not claimed as novel.

An earlier classification of all Nijenhuis operators on Heisenberg algebras already covers the one-dimensional-center Heisenberg special case; **that case is explicitly not asserted to be new here**. A prior rank-one classification on forms of \(\mathfrak{sl}_2\) concerns a different, nonnilpotent Lie algebra. The distinct contribution considered here is the uniform commutator-pencil count for arbitrary stem two-step algebras together with its free-family closed formula. No claim of absolute publication priority is made; older or broader general Lie Nijenhuis classifications could imply the result indirectly.

## Limitations
The theorem counts vector-space-rank-one operators only; it does not classify higher ranks, automorphism-conjugacy classes, or nonreduced operator schemes. The free-family formula uses known counts of alternating forms. The finite checker covers selected small prime fields, not extension fields; the proof covers all prime powers. The literature comparison is bounded and independent external validation has not been performed.

## References
1. J. Liu, Y. Sheng, Y. Zhou, C. Bai, *Nijenhuis operators on \(n\)-Lie algebras*, arXiv:1601.02356v1 (11 January 2016), https://arxiv.org/html/1601.02356v1 .
2. J. Fulman, L. Goldstein, *Stein's method and the rank distribution of random matrices over finite fields*, arXiv:1211.0504v1 (2 November 2012), https://arxiv.org/html/1211.0504v4 .
3. Classical symplectic orbit-stabilizer formula for nondegenerate alternating forms over finite fields (used as an established counting identity).
