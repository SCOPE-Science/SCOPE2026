# The radical-depth spectrum of one-dimensional subalgebras in degree-four exterior quotients

## Finding

Let \(q\) be any prime power, \(n\ge 4\), and \(V\cong\mathbb F_q^n\). In the graded, unital, associative exterior-algebra quotient
\[
A=\bigwedge V\big/\bigoplus_{j\ge5}\bigwedge^j V
=\bigoplus_{j=0}^{4}\bigwedge^j V,
\]
write \(J=\bigoplus_{j=1}^{4}\bigwedge^j V\) for the radical. A **one-dimensional subalgebra** means a nonzero \(\mathbb F_q\)-line \(L\subseteq A\) with \(L\cdot L\subseteq L\); it need not contain the unit. Its radical depth is \(0\) for the unit line \(\mathbb F_q1\), or the unique \(j\in\{1,2,3,4\}\) with \(L\subseteq J^j\) and \(L\nsubseteq J^{j+1}\) otherwise.

Put \(c_i=\binom ni\), \(h=c_3+c_4\), and let
\[
G=\begin{bmatrix}n\\2\end{bmatrix}_q
=\frac{(q^n-1)(q^{n-1}-1)}{(q^2-1)(q-1)}.
\]
The **complete radical-depth enumerator** \(\mathcal L_{n,q}(T)=\sum_{j=0}^4 s_jT^j\), where \(s_j\) counts lines of depth \(j\), is specified by \(s_0=1\) and
\[
\begin{aligned}
s_3&=\frac{(q^{c_3}-1)q^{c_4}}{q-1},&
s_4&=\frac{q^{c_4}-1}{q-1},\\
s_1&=\frac{q^h\bigl((q^n-1)+(q-1)G(q^2-1)\bigr)}{q-1},&
s_2&=q^hG
\end{aligned}
\qquad(q\text{ odd}),
\]
and
\[
\begin{aligned}
s_1&=\frac{(q^n-1)q^{c_2+h}}{q-1},&
s_2&=\frac{(q^{c_2}-1)q^h}{q-1},\\
s_3&=\frac{(q^{c_3}-1)q^{c_4}}{q-1},&
s_4&=\frac{q^{c_4}-1}{q-1}
\end{aligned}
\qquad(q\text{ even}).
\]
In particular, the total number of one-dimensional subalgebras is
\[
\mathcal L_{n,q}(1)=
\begin{cases}
\displaystyle 1+\frac{q^h\bigl(q^n+(q-1)Gq^2\bigr)-1}{q-1},&q\text{ odd},\\[2mm]
\displaystyle 1+\frac{q^{c_1+c_2+c_3+c_4}-1}{q-1},&q\text{ even}.
\end{cases}
\]
Over \(\mathbb F_3\) with \(n=4\), the depth counts are \((s_0,s_1,s_2,s_3,s_4)=(1,262440,31590,120,1)\), totaling \(294152\). For \(\mathbb F_2\), they are \((1,30720,2016,30,1)\), totaling \(32768\).

## Assumptions and scope

All statements hold for every prime power \(q\), including nonprime fields, with no restriction on the parity of \(n\). The quotient is by *all* homogeneous components of degrees at least five. Multiplication is the exterior wedge product, truncated to degrees at most four. No commutativity of the full algebra is assumed when \(q\) is odd; the subalgebras counted have dimension exactly one and are not required to be unital.

Every \(x\in J\) has unique homogeneous decomposition \(x=a+b+c+d\), with \(a\in\bigwedge^1 V\), \(b\in\bigwedge^2 V\), \(c\in\bigwedge^3 V\), and \(d\in\bigwedge^4 V\). When \(q\) is odd, the nonzero square-zero elements satisfy exactly
\[
b=0\quad\text{or}\quad b=u\wedge v\ne0,\quad a\in\operatorname{span}_{\mathbb F_q}\{u,v\},
\]
with arbitrary \(c,d\). When \(q\) is even, **every** element of \(J\) is square-zero. This is a geometric classification of all permitted line generators, not merely a formula.

## Proof

**Step 1: reduction to square-zero elements.** The quotient is a finite-dimensional local algebra with radical \(J\); in particular all of \(J\) is nilpotent and every \(x\notin J\) is invertible. If \(L=\mathbb F_qx\) is a one-dimensional subalgebra, \(x^2=\lambda x\) for some \(\lambda\in\mathbb F_q\). For \(x\in J\setminus\{0\}\), nilpotence forces \(\lambda=0\): otherwise \(x^k=\lambda^{k-1}x\ne0\) for all positive integers \(k\). For a unit \(x=\alpha 1+y\), \(\alpha\ne0\), \(y\in J\), scalar comparison gives \(\lambda=\alpha\), so \(x(x-\alpha1)=0\), hence \(y=0\). Thus \(\mathbb F_q1\) is the only non-radical line, and all other lines are square-zero radical lines. Each radical line has exactly \(q-1\) nonzero generators.

**Step 2: homogeneous squaring.** Exterior sign commutation gives, modulo degrees greater than four,
\[
(a+b+c+d)^2=2a\wedge b+b\wedge b.
\]
The two terms lie in different homogeneous degrees (three and four). In characteristic two, the exterior algebra is a commutative algebra in which every positive-degree basis monomial has square zero; the Frobenius square of every element of \(J\) therefore vanishes. For odd \(q\), square-zero is equivalent to \(a\wedge b=0\) and \(b\wedge b=0\), independently of \(c,d\).

**Step 3: the nonstandard bivector criterion and its boundary.** Over any field of characteristic different from two, a bivector has a basis in which
\[
b=\lambda_1u_1\wedge v_1+\cdots+\lambda_ru_r\wedge v_r
\]
with all \(\lambda_i\ne0\) and the listed vectors independent (normal form of an alternating tensor/matrix). Consequently
\[
b\wedge b=2\sum_{1\le i<j\le r}\lambda_i\lambda_j
u_i\wedge v_i\wedge u_j\wedge v_j.
\]
These degree-four monomials are linearly independent and nonzero in the quotient; therefore \(b\wedge b=0\) if and only if \(r\le1\). Equivalently, \(b\) is zero or decomposable. For nonzero \(b=u\wedge v\), choosing a complement to the plane \(W=\operatorname{span}\{u,v\}\) shows \(a\wedge b=0\) if and only if \(a\in W\). No general-position assumption is involved.

**Step 4: finite-field parameter count.** There are \(G\) two-dimensional subspaces \(W\le V\), and exactly \(q-1\) nonzero decomposable bivectors lying on the projective Plücker point of each \(W\). For \(b=0\), all \(q^n\) values of \(a\) work. For each of the \((q-1)G\) nonzero choices of \(b\), precisely \(q^2\) vectors \(a\in W\) work. The arbitrary pairs \((c,d)\) contribute \(q^h\). Hence, for odd \(q\), the radical square-zero element count is \(q^h\bigl(q^n+(q-1)Gq^2\bigr)\); for even \(q\), it is \(q^{c_1+c_2+c_3+c_4}\).

**Step 5: radical-depth refinement.** For odd \(q\), elements of least nonzero homogeneous degree one arise either from \(b=0,a\ne0\) (\(q^n-1\) possibilities) or from decomposable \(b\ne0\) with \(a\in W\setminus\{0\}\) (\((q-1)G(q^2-1)\) possibilities), multiplied by \(q^h\). Those of least degree two have \(a=0\), nonzero decomposable \(b\), and arbitrary \(c,d\), yielding \((q-1)Gq^h\). In both characteristics, least degree three gives \((q^{c_3}-1)q^{c_4}\), and least degree four gives \(q^{c_4}-1\). In characteristic two all choices of higher-degree coefficients are allowed; thus the least-degree-one and least-degree-two counts are \((q^n-1)q^{c_2+h}\) and \((q^{c_2}-1)q^h\). Dividing the nonzero-element counts by \(q-1\), and adjoining the unit line, proves every coefficient and the total.

## Verification

The standalone pure-Python program `checker.py` independently multiplies all exterior basis monomials with the correct permutation sign, truncates products above degree four, and verifies both the square-zero condition and the line-depth predictions. It exhaustively tests complete radical element sets for \((n,q)=(2,3),(3,2),(3,3),(4,2)\), and the determining degree-one/degree-two coefficient sets for \((4,2),(4,3),(3,3),(3,5)\). The smaller \(n<4\) examples are boundary/sanity checks; the asserted theorem starts at \(n=4\). Running `python3 checker.py` prints `VERIFY_OK` if every test passes. The universal theorem follows from Steps 1–5, not from finite enumeration.

## Relationship to prior work

McCullough and Mere [1] investigate homological and Koszul properties of quotients of exterior algebras, giving the general algebraic setting but not a count of one-dimensional subalgebras. Domokos and Zubor [2], especially Section 2, classify structural features of square-zero *subspaces* in the odd part while analyzing maximal commutative subalgebras; their statements do not give the radical-depth spectrum of all individual square-zero lines, including even-degree contributions. Bovdi and Leung [3] study maximal commutative subalgebras of the full Grassmann algebra, not the complete one-dimensional subalgebra census of the degree-four quotient. Benito, Gubarev and Pozhidaev [4], Section 4.4, treat the two-generator Grassmann algebra in a Rota–Baxter classification; the current Plücker obstruction only appears when degree four survives. Regev [5] studies finite-field Grassmann polynomial identities and codimensions; only the abstract, not full article, was accessible, and possible related statements there remain a residual risk. The formula also uses the classical Plücker description of decomposable bivectors, which is **not** claimed to be new.

## Limitations

This is a count of **all one-dimensional associative subalgebras** and their radical filtration depths, not a census of higher-dimensional subalgebras or automorphism orbits. It concerns quotients truncated precisely above degree four, not arbitrary higher truncations. The finite tests use prime fields, while the theoretical proof covers prime powers. Prior results in equivalent Grassmann/Plücker terminology could reproduce the enumerator; the accessible sources reviewed did not settle that possibility.

## References

[1] J. McCullough and Z. Mere, *G-Quadratic, LG-Quadratic, and Koszul Quotients of Exterior Algebras*, arXiv:2105.13457v1 (first posted 2021-05-27), Sections 1–6; primary MSC 16S37, 13P10. https://arxiv.org/abs/2105.13457

[2] M. Domokos and M. Zubor, *Commutative subalgebras of the Grassmann algebra*, arXiv:1403.2916v2, Sections 2 and 7. https://arxiv.org/html/1403.2916v2

[3] V. A. Bovdi and H.-H. Leung, *Maximal commutative subalgebras of a Grassmann algebra*, arXiv:1803.03457v1, Sections 2–4. https://arxiv.org/html/1803.03457v1

[4] P. Benito, V. Gubarev and A. Pozhidaev, *Rota–Baxter Operators on Quadratic Algebras*, arXiv:1801.07037v1, Section 4.4. https://arxiv.org/pdf/1801.07037

[5] A. Regev, *Grassmann algebras over finite fields*, Communications in Algebra **19** (1991), 1829–1849, DOI:10.1080/00927879108824231 (abstract only inspected).
