# Full fixed-space spectrum and field-order rigidity for standard filiform Lie automorphisms

## Finding
Let \(q\) be any prime power, let \(m\ge3\), and let \(\mathfrak f_m(q)\) be the \((m+1)\)-dimensional Lie algebra over \(\mathbb F_q\) with basis \(t,e_1,\ldots,e_m\) and only nonzero basis brackets
\[
[t,e_i]=e_{i-1}\quad (2\le i\le m).
\]
For \(\phi\in\operatorname{Aut}(\mathfrak f_m(q))\), set \(\operatorname{fixdim}(\phi)=\dim_{\mathbb F_q}\ker(\phi-I)\). The complete fixed-space enumerator is
\[
\mathcal F_{m,q}(z)=\sum_{\phi\in\operatorname{Aut}(\mathfrak f_m(q))}z^{\operatorname{fixdim}(\phi)}.
\]
Put \(Q=q-1\) and, for integers \(r\ge1\) and \(0\le j<r\), let
\[
L_j(m,r)=\max\!\left(0,\left\lceil\frac{m-j}{r}\right\rceil\right).
\]
Define \(M_0(z)=1\) and, for \(L\ge1\),
\[
M_L(z)=\sum_{d=1}^{L-1}(q-1)q^{-d}z^d+q^{1-L}z^L.
\]
Define \(w_s=(q-1)q^{-s}\) for \(1\le s<m\), \(w_m=q^{1-m}\), and
\[
H_m(z)=\sum_{s=1}^{m}w_s\bigl((1-q^{-s})z^s+q^{-s}z^{s+1}\bigr).
\]
Then the exact fixed-space polynomial for every \(q\) and \(m\ge3\) is
\[
\boxed{\mathcal F_{m,q}(z)=q^{2m-1}\left[(q-2)z+H_m(z)+\sum_{\substack{r\mid q-1\\r>1}}\varphi(r)\left((q-1-r)+\sum_{j=0}^{r-1}M_{L_j(m,r)}(z)\right)\right].}
\]
Here \(\varphi\) is Euler's totient function; when \(q=2\), the divisor sum is empty. The rational expressions inside the brackets become nonnegative integer coefficients after multiplication by \(q^{2m-1}\). In particular,
\[
|\operatorname{Aut}(\mathfrak f_m(q))|=(q-1)^2q^{2m-1}
\]
and the exact number of fixed-point-free automorphisms is
\[
\boxed{q^{2m-1}\sum_{\substack{r\mid q-1\\r>1}}\varphi(r)\bigl(q-1-\min(m,r)\bigr).}
\]
A fixed-point-free automorphism exists **if and only if** \(q-1\) is composite or \(m<q-1\). In particular, for each fixed \(q\), the fixed-point-free proportion stabilizes as soon as \(m\ge q-1\): it is zero if \(q-1\) is prime or \(q=2\), and positive if \(q-1\) is composite. The algebra in dimension three (the Heisenberg case \(m=2\)) is deliberately excluded: its automorphism group has a different structure.

## Assumptions and scope
All results hold in every field characteristic, including characteristic two. The algebra is a finite-dimensional nilpotent Lie algebra of maximal class: the abelian ideal \(V=\langle e_1,\ldots,e_m\rangle\) has codimension one and \(\operatorname{ad}(t)|_V\) is one nilpotent Jordan block. The fixed-point space is the fixed space of the **underlying linear map**, not the set of fixed automorphisms of some external action. A fixed-point-free automorphism has no nonzero fixed vector. The polynomial counts distinct \(\mathbb F_q\)-linear Lie automorphisms, without quotienting by conjugacy.

## Proof
**1. The abelian ideal and all automorphisms.** The derived ideal is \([\mathfrak f_m,\mathfrak f_m]=\langle e_1,\ldots,e_{m-1}\rangle\). Every codimension-one ideal contains this derived ideal. If a codimension-one ideal \(W\ne V\) were abelian, it would contain some \(w=a t+v\) with \(a\ne0\), and it contains \(e_2\) because \(m\ge3\). But \([w,e_2]=ae_1\ne0\), a contradiction. Thus \(V\) is the unique abelian ideal of codimension one and is characteristic.

Consequently every automorphism has \(\phi(t)=at+v\) and \(\phi|_V=B\), where \(a\in\mathbb F_q^\times\), \(v\in V\), and \(B\) is invertible. Let \(N(e_i)=e_{i-1}\) for \(i\ge2\), \(N(e_1)=0\). Preservation of brackets is exactly \(BN=aNB\). Given \(a\), the image \(B(e_m)=\sum_{i=1}^m b_i e_i\) determines all of \(B\) by
\[
B(e_j)=a^{m-j}N^{m-j}B(e_m),\qquad 1\le j\le m.
\]
The matrix is invertible exactly when \(b_m\ne0\). Thus there are \((q-1)q^{m-1}\) choices of \(B\), and independently \(q^m\) choices of \(v\). This proves the automorphism-group order. The diagonal entries of \(\phi\), in the basis \(t,e_1,\ldots,e_m\), are \(a\) and \(b_m a^j\) for \(0\le j<m\).

**2. The case \(a=1\).** Identify \(V\) with \(R=\mathbb F_q[u]/(u^m)\), with \(N\) acting as multiplication by \(u\). When \(a=1\), \(B\) is multiplication by an arbitrary unit \(b f(u)\), with \(b\in\mathbb F_q^\times\) and \(f\in U:=1+uR\). If \(b\ne1\), then \(B-I\) is invertible, so \(\dim\ker(\phi-I)=1\), producing \((q-2)z\) in the normalized bracket.

When \(b=1\), write \(s\) for the smallest positive exponent with a nonzero coefficient in \(f(u)-1\), or \(s=m\) if \(f=1\). Its exact probability under uniform \(f\in U\) is \(w_s\). Multiplication by \(f-1\) has kernel dimension \(s\) and image codimension \(s\). In the block equation \((\phi-I)(x t+y)=xv+(B-I)y\), a uniform \(v\in V\) lies in this image with probability \(q^{-s}\). Therefore the fixed-space dimension equals \(s+1\) with probability \(q^{-s}\) and \(s\) otherwise, proving \(H_m(z)\).

**3. Semilinear normalization when \(a\ne1\).** Let \(r=\operatorname{ord}_{\mathbb F_q^\times}(a)>1\), so \(r\mid q-1\) and \(r\) is prime to the characteristic. In the polynomial model, \(B=b f(u)\sigma\), where \(b=b_m\ne0\), \(f\in U=1+uR\), and \(\sigma(u)=au\). The following elementary cyclic-unit lemma is used. Every \(f\in U\) has a **unique invariant factor** \(c\in U^\sigma\) and some \(h\in U\) such that
\[
f=c\,h/\sigma(h),\qquad U^\sigma=\{1+c_1u^r+c_2u^{2r}+\cdots\}.
\]
Indeed, the norm \(\mathcal N(f)=\prod_{i=0}^{r-1}\sigma^i(f)\) is invariant. The finite group \(U\) has order \(q^{m-1}\), a power of the characteristic, so taking \(r\)-th roots is uniquely possible in \(U\). Put \(c=\mathcal N(f)^{1/r}\in U^\sigma\), and \(g=f/c\), so \(\mathcal N(g)=1\). The product \(h_0=\prod_{i=0}^{r-1}\sigma^i(g)^{r-1-i}\) satisfies \(h_0/\sigma(h_0)=g^r\). Its unique \(r\)-th root \(h\) satisfies \(h/\sigma(h)=g\). Uniqueness of \(c\) follows from its norm formula. Thus multiplication by \(h\) conjugates \(bc\sigma\) to \(B\). Moreover, the map \(f\mapsto c\) is a surjective group homomorphism \(U\to U^\sigma\), so a uniform \(f\) gives a uniform invariant factor \(c\).

**4. The fixed-space distribution.** Decompose the polynomial space by residues modulo \(r\):
\[
R=\bigoplus_{j=0}^{r-1}u^j\mathbb F_q[u^r]\pmod{u^m}.
\]
The \(j\)-th summand has dimension \(L_j(m,r)\). On it \(bc\sigma\) is multiplication by \(ba^j c\). If \(ba^j\ne1\), it has no fixed vectors. Since \(a\) has order \(r\), at most one residue \(j\) can satisfy \(ba^j=1\). For \(b\notin\langle a\rangle\), there is no such residue, giving \(q-1-r\) choices of \(b\) with fixed-space dimension zero. Each \(b\in\langle a\rangle\) selects exactly one \(j\in\{0,\ldots,r-1\}\). On this summand, the fixed-space dimension is the nullity of multiplication by \(c-1\). A uniform invariant \(c=1+c_1u^r+c_2u^{2r}+\cdots\) has independent uniform coefficients, and hence its kernel dimension on a length-\(L\) summand equals \(d<L\) with probability \((q-1)q^{-d}\) and equals \(L\) with probability \(q^{1-L}\). If \(L=0\), the dimension is zero. This is exactly \(M_L(z)\). For \(a\ne1\), the quotient direction \(t\) has eigenvalue different from one, so its off-diagonal vector \(v\) does not change the fixed dimension.

There are \(\varphi(r)\) choices of multiplier \(a\) of order \(r\). Combining their contributions with the case \(a=1\), and multiplying by the \(q^{2m-1}\) free choices of nilpotent coefficients and translation for each \((a,b)\), yields the boxed polynomial.

**5. The fixed-point-free boundary.** For any \(a\) of order \(r>1\), the number of values \(b\) avoiding \(ba^j=1\) for \(0\le j<m\) is \(q-1-\min(m,r)\), which gives the fixed-point-free count. This is positive for some \(r>1\) exactly when \(q-1\) has a nontrivial proper divisor or \(m<q-1\). The eventual stabilization and its arithmetic dichotomy follow immediately.

## Verification
The standalone file `verify.py` enumerates both generator images \(\phi(t)\) and \(\phi(e_m)\), with no assumed invariant ideal, reconstructs images of the remaining basis vectors by iterated brackets, checks all defining relations, and computes actual matrix rank and fixed-space nullity over \(\mathbb F_2\), \(\mathbb F_3\), \(\mathbb F_4\), and \(\mathbb F_5\). It independently compares the complete nullity histogram against the formula. Checked \((q,m)\) pairs are \((2,3),(2,4),(3,3),(3,4),(4,3),(5,3)\). It also tests the existence dichotomy over several prime fields and \(\mathbb F_4\). Execute `python3 verify.py` with the Python standard library. The expected final message is `VERIFY_OK: independent generator enumeration and field-order threshold`. As a sample, for \((q,m)=(5,3)\), the verified counts at fixed-space dimensions \(0,1,2,3,4\) are respectively \(12500,35750,1605,144,1\).

The exhaustive computations establish only their listed finite instances. The preceding argument establishes the general statement for all prime powers and dimensions within scope.

## Relationship to prior work
Avetisyan's 2018 *Jordanable almost Abelian Lie algebras* (arXiv:1811.01252, Proposition 11) describes automorphism groups for general Jordanable almost-abelian Lie algebras other than the Heisenberg algebra. This general structural theorem is acknowledged and is not claimed as new. The result here develops the nontrivial **complete finite-field fixed-space distribution** and the explicit arithmetic existence boundary using the cyclic-unit factorization above; neither is stated in that inspected source.

Burde and Dekimpe's 2026 *Fixed-point-free automorphisms of solvable Lie algebras* (arXiv:2604.27916, Theorems 5.7 and 6.5) proves existence criteria over \(\mathbb C\); the finite-field phase transition here is not a characteristic-zero existence result and cannot follow by simply specializing those theorems. Published published-finding corpus entries on the three-dimensional Heisenberg algebra and on adjoint-rank statistics of filiform Lie algebras concern different dimensions or different operators, not this fixed-space enumerator.

## Limitations
The theorem does not apply to the three-dimensional Heisenberg algebra (\(m=2\)), to nonstandard filiform Lie algebras, or to nonlinear or semilinear Lie automorphisms. The formula counts fixed vector **dimensions**, not conjugacy classes of automorphisms or their exact orders. The original automorphism-matrix structure is published; originality is asserted only for the specific finite-field distribution, cyclic-unit counting, and arithmetic boundary as established here. Other treatments of cyclic semilinear operators or older automorphism-characteristic-polynomial literature could contain equivalent results; a negative search is not a uniqueness certificate. No independent mathematical audit has been performed.

## References
1. Zhirayr Avetisyan, *Jordanable almost Abelian Lie algebras*, arXiv:1811.01252 (first submitted 2018-11-03), especially Proposition 11, available author-uploaded full text at https://www.researchgate.net/publication/328757708_Jordanable_almost_Abelian_Lie_algebras .
2. Dietrich Burde and Karel Dekimpe, *Fixed-point-free automorphisms of solvable Lie algebras*, arXiv:2604.27916 (first submitted 2026-04-30), especially Theorems 5.7 and 6.5; open author manuscript at https://homepage.univie.ac.at/dietrich.burde/papers/burde_83_fpf.pdf .
3. Vanderlei Lopes de Jesus and Csaba Schneider, *The center and invariants of standard filiform Lie algebras*, arXiv:2209.11897 (2022-09-24); a related but different invariant problem.
4. Published published-finding corpus record: *Exact fixed-point-free automorphism count for the three-dimensional Heisenberg Lie algebra*, identifier 2026/10/4/SCOPE-exact-fixed-point-free-automorphism-count-for-the-three-dimensio--17f0de4cb789 .
5. Published published-finding corpus record: *Adjoint-rank spectra of two maximal-class filiform Lie algebras*, identifier 2026/10/4/SCOPE-adjoint-rank-spectra-of-two-maximal-class-filiform-lie-algebras--48cdbeaf7d86 .
