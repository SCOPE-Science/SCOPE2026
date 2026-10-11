# Exact Gabor tomography rank for hyperbolic quadratic shells over odd finite fields

## Finding

Let \(q\) be any odd prime power, \(r\geq2\), \(V=\mathbb F_q^r\oplus\mathbb F_q^r\), and \(Q(x,y)=x\cdot y\). Let \(B(v,w)=Q(v+w)-Q(v)-Q(w)\), and let \(g=\mathbf1_S\), where \(S=\{v\in V:Q(v)=1\}\). Fix any nontrivial additive character \(\psi\) of \(\mathbb F_q\). The full time-frequency orbit of \(g\) defines an intensity-lifting operator on all complex matrices of dimension \(N=q^{2r}\).

**Exact ambiguity-zero classification.** Write \(\chi\) for the quadratic character extended by \(\chi(0)=0\). For every \(a,b\in V\), put
\[
A_g(a,b)=\sum_{x\in V}g(x)g(x-a)\psi(B(b,x)).
\]
Then \(A_g(a,b)\ne0\) for all \(b\) when \(a=0\). When \(a\ne0\) and \(Q(a)=0\), it vanishes if and only if \(B(a,b)\ne0\). When \(t=Q(a)\ne0\), define \(c=1-t/4\) and \(w=b-\frac{B(a,b)}{2t}a\in a^\perp\). Its remaining zeros are **exactly**
\[
A_g(a,b)=0\quad\Longleftrightarrow\quad
\begin{cases}
w\ne0\ \text{and}\ Q(w)=0,&c=0,\\
\chi(cQ(w))=-1,&c\ne0.
\end{cases}
\]
In particular, this classification is independent of the selected nontrivial additive character.

**Exact lifting rank and kernel.** Set \(m=2r\), \(N=q^m\),
\[
I=q^{m-1}+(q-1)q^{r-1}-1,\qquad J=q^{m-1}-q^{r-1},
\]
\[
C_4=N-q^{m-1}+q,\qquad C_*=N-\frac{q-1}{2}q^{m-1}.
\]
For \(T_ag(x)=g(x-a)\), \(M_bg(x)=\psi(B(b,x))g(x)\), and \(W_{a,b}=M_bT_a\), define
\[
\mathcal L_g(X)_{u,v}=\operatorname{tr}\!\left(X\,|W_{u,v}g\rangle\langle W_{u,v}g|\right),\quad
(u,v)\in V\times V.
\]
Then the **exact complex rank** is
\[
\boxed{\operatorname{rank}_{\mathbb C}\mathcal L_g
=N+Iq^{m-1}+J\left[C_4+(q-2)C_*-\frac{q-1}{2}q^r\right].}
\]
The complex nullity is \(N^2-\operatorname{rank}_{\mathbb C}\mathcal L_g\), and the entire kernel is the complex linear span of the Weyl matrices \(W_{a,b}\) for the pairs in the preceding ambiguity-zero classification. For fixed odd \(q\),
\[
\lim_{r\to\infty}\frac{\operatorname{rank}_{\mathbb C}\mathcal L_g}{q^{4r}}=
\frac{(q-1)(q+2)}{2q^2}.
\]

## Assumptions and scope

All vector spaces, quadratic forms, characters, and matrix entries above are over the named finite field except that Fourier amplitudes and lifted operators are complex. The bilinear form \(B\) is nondegenerate. The window is an **unweighted indicator** (not a normalized vector), but positive scalar normalization does not change rank. The dimension condition \(r\ge2\) ensures that the isotropic section is a nondegenerate, even-dimensional quadratic sphere of dimension at least two; this is used essentially. The result is about **injectivity on all complex operators**, not a statement about (nonlinear) phase retrieval of pure signals.

## Proof

**1. Fourier transforms of quadratic level sets.** Consider any nondegenerate quadratic space \((U,Q_U)\) over \(\mathbb F_q\), and use its polar form \(B_U\). For \(h\in U\), write
\[
F_c(h)=\sum_{z:Q_U(z)=c}\psi(B_U(h,z)).
\]
Additive-character orthogonality followed by completion of squares yields for \(h\ne0\)
\[
F_c(h)=\frac{G_U}{q}\sum_{s\in\mathbb F_q^\times}
\chi(s)^{\dim U}\psi\left(-cs-\frac{Q_U(h)}{s}\right),
\]
where \(G_U=\sum_{z\in U}\psi(Q_U(z))\ne0\) is a quadratic Gauss product. This identity follows because \(\sum_z\psi(sQ_U(z)+B_U(h,z))=\chi(s)^{\dim U}G_U\psi(-Q_U(h)/s)\). At \(h=0\), \(F_c(0)\) is the (positive) cardinality of the level set in all instances used here.

If \(\dim U\) is even and \(c\ne0\), the sum contains exactly \(q-1\) complex \(p\)-th roots of unity, where \(q=p^f\). A vanishing integer sum of these roots would have equal multiplicity in each of the \(p\) residue classes, by irreducibility of \(1+X+\cdots+X^{p-1}\) over \(\mathbb Q\). That would force \(p\mid q-1\), a contradiction. Thus \(F_c(h)\ne0\) in even dimensions, including \(h=0\) for the nonempty levels used below.

If \(\dim U\) is odd and \(h\ne0\), let \(H=Q_U(h)\). The essential sum is the Salié-type sum
\[
T(c,H)=\sum_{s\ne0}\chi(s)\psi(-cs-H/s).
\]
When \(c=0\), substitution \(u=1/s\) and a quadratic Gauss-sum evaluation show \(T(0,H)=0\) exactly when \(H=0\). When \(c\ne0\), an exact Fourier transform in \(H\) gives
\[
T(c,H)=K(c,\psi)\sum_{z\in\mathbb F_q:\,z^2=4cH}\psi(z),
\qquad K(c,\psi)\ne0.
\]
For completeness, the additive Fourier transforms of the left and right sums at a nonzero dual frequency \(u\) are respectively \(q\chi(u)\psi(-c/u)\) and \(\chi(uc)G_\psi\psi(-c/u)\), where \(G_\psi=\sum_z\psi(z^2)\ne0\); both transforms vanish at \(u=0\). Thus \(K(c,\psi)=q\chi(c)/G_\psi\). The root sum is zero precisely if \(cH\) is a nonsquare: it is \(1\) when \(H=0\), and when \(cH\ne0\) is square it is \(\psi(z)+\psi(-z)\ne0\), since roots of unity of odd prime order cannot be antipodal. This proves the two exact odd-dimensional zero conditions. No upper bound on a character sum is being substituted for a zero test.

**2. Intersections of the shell with its translates.** Since
\[
Q(x)=Q(x-a)=1\quad\Longleftrightarrow\quad
Q(x)=1\ \text{and}\ B(a,x)=Q(a),
\]
we split by \(a\). For \(a=0\), the ambiguity function is \(F_1(b)\) on the even-dimensional space \(V\), hence never zero by Step 1. If \(a\ne0\) and \(Q(a)=0\), take a Witt pair containing \(a\). The intersection consists precisely of \(x=sa+z\), where \(s\in\mathbb F_q\), \(z\) ranges over the level-one sphere in a nondegenerate hyperbolic space of dimension \(m-2\). Summing over \(s\) forces \(B(a,b)=0\); once it holds, the remaining even-dimensional level-one Fourier transform is nonzero. If \(t=Q(a)\ne0\), write \(x=a/2+y\). The two equations reduce to \(y\in a^\perp\), \(Q(y)=1-t/4=c\). The restriction \(a^\perp\) is nondegenerate of odd dimension \(m-1\). The phase separates as \(\psi(B(b,a)/2)\) times its quadratic-sphere transform at \(w\). Step 1 gives precisely the stated \(c=0\) and \(c\ne0\) cases, with \(w=0\) always nonvanishing.

**3. Counting surviving ambiguity coefficients.** For \(Q(x,y)=x\cdot y\) in dimension \(m=2r\), the number of vectors of norm zero is \(q^{m-1}+(q-1)q^{r-1}\). Every prescribed nonzero norm is represented by exactly \(J=q^{m-1}-q^{r-1}\) vectors. The first formula also follows by splitting \(x=0\) from \(x\ne0\), and the second follows from the same linear-equation count. Hence there are \(I\) nonzero isotropic shifts and \(J\) shifts of each nonzero norm.

For \(a=0\), all \(N\) frequencies survive. Each nonzero isotropic \(a\) has \(q^{m-1}\) frequencies satisfying \(B(a,b)=0\), hence contributes \(q^{m-1}\). Fix \(a\) with \(t=Q(a)\ne0\). Each \(w\in a^\perp\) has \(q\) preimages \(b\in V\). The odd-dimensional quadratic-form point counts in \(a^\perp\) are
\[
\#\{w:Q(w)=0\}=q^{m-2},\qquad
\#\{w:Q(w)=h\}=q^{m-2}+\chi(-th)q^{r-1}\quad(h\ne0).
\]
They follow directly by the same quadratic Gauss-sum calculation, using that the determinant of the restriction has quadratic square class \((-1)^r/t\), because the ambient form is hyperbolic.

If \(t=4\), the zeros are the nonzero isotropic \(w\), so the number of surviving \(b\)'s is
\[
q\left(q^{m-1}-q^{m-2}+1\right)=C_4.
\]
For \(t\notin\{0,4\}\), exactly \((q-1)/2\) nonzero norms \(h\) satisfy \(\chi(ch)=-1\). Their total number of vectors in \(a^\perp\) is
\[
\frac{q-1}{2}\left[q^{m-2}-\chi\bigl(t(t-4)\bigr)q^{r-1}\right],
\]
so the number of surviving \(b\)'s is
\[
C_*+\frac{q-1}{2}\chi\bigl(t(t-4)\bigr)q^r.
\]
Finally, for a quadratic polynomial with two distinct roots over an odd field,
\(\sum_{t\in\mathbb F_q}\chi(t(t-4))=-1\); the terms at \(0\) and \(4\) vanish. Summing over all norm levels \(t\) gives the displayed rank expression.

**4. From ambiguity support to lifting rank and kernel.** The \(N^2\) operators \(W_{a,b}\) form an orthogonal basis for the \(N^2\)-dimensional complex matrix space. Conjugation by another Weyl operator multiplies \(W_{a,b}\) by a phase-space character. Accordingly, evaluation against the entire orbit of the rank-one operator \(|g\rangle\langle g|\) is a discrete Fourier transform of the Weyl-coordinate vector, with diagonal multipliers proportional to \(\langle g,W_{a,b}g\rangle\). Those multipliers differ from \(A_g(a,b)\) only by a unit-modulus factor and conjugation/reindexing, which preserve its vanishing set. Fourier inversion proves both the exact rank (the number of nonzero multipliers) and the Weyl-span description of the kernel. The asymptotic ratio follows by dividing the exact expression by \(N^2\), retaining its degree-\(2m\) terms.

## Verification

Run `python3 checks/verify.py` (Python 3, NumPy). For \(q=3,r=2\), the checker exhaustively evaluates all \(6{,}561\) ambiguity coefficients using **exact cyclotomic residue counts**, obtaining rank \(3393\) and nullity \(3168\). At \(q=5,r=2\), it evaluates all \(390{,}625\) pairs and obtains rank \(208225\), nullity \(182400\). At \(q=3,r=3\), it evaluates all \(531{,}441\) pairs and obtains rank \(285741\), nullity \(245700\). A separate \(\mathbb F_9\) implementation checks \(501\) exactly computed character sums, covering all four geometric cases. The total is \(929{,}128\) coefficient checks. No numerical tolerance is used for these zero tests.

The exhaustive computations are finite checks at the named parameters, **not** proofs of the universal theorem. The preceding Gauss-sum, Witt-decomposition, and orbit-diagonalization arguments establish the unrestricted claim.

## Relationship to prior work

Iosevich and Koh's 2007 work derives finite-field sphere Fourier transforms and estimates in restriction theory [1]; their 2008 treatment extends the framework to general quadratic surfaces [2]. Bojarovska and Flinth provide the finite Gabor phase-retrieval ambiguity-function framework and Weyl analysis [3]. These are methodological antecedents. The result here specializes to hyperbolic level-one indicators in arbitrary even dimension and supplies the full **translated-intersection ambiguity-zero classification**, every Weyl kernel direction, and a closed-form **complex operator-lifting rank**. These exact outcomes are not claimed to be established by [1]–[3]. Equivalence to another historical result remains a residual literature risk; the formulation makes no claim of independently certified priority.

## Limitations

This statement assumes \(q\) odd, \(r\ge2\), and exactly the hyperbolic level-one indicator. It does not classify weighted windows, characteristic-two forms, dimension two, arbitrary quadratic-form isometry classes, or nonlinear pure-state phase retrieval. The operator kernel is over all complex matrices, not the cone of rank-two Hermitian differences. Computations were independently checked for several small fields but are not infinite-dimensional proof certificates. The literature comparison is not exhaustive, and independent mathematical audit has not been performed.

## References

1. A. Iosevich and D. Koh, *Extension Theorems for Spheres in the Finite Field Setting*, arXiv:0712.1627v1 (first publicly posted December 11, 2007), https://arxiv.org/abs/0712.1627.
2. A. Iosevich and D. Koh, *Extension theorems for Fourier transform associated with non-degenerate quadratic surfaces*, arXiv:0804.4505v1 (April 28, 2008), https://arxiv.org/abs/0804.4505.
3. Z. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1 (March 19, 2015), https://arxiv.org/abs/1503.05800.
