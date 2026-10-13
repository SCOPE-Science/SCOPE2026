# A characteristic-two point-count jump for transposed-Leibniz products on triangular matrices

## Finding
Let \(K\) be a field and \(L=\mathfrak t_2(K)\) be the Lie algebra of upper triangular two-by-two matrices, with the commutator bracket. Fix its Lie bracket, but allow its commutative multiplication to vary. Call a bilinear product \(\cdot\) **admissible** when it is commutative, associative, and satisfies the polynomial transposed Leibniz identity
\[
2u\cdot[v,w]=[u\cdot v,w]+[v,u\cdot w]\qquad(u,v,w\in L).
\]
The zero product is counted. No division by \(2\) is implicit: in characteristic two the displayed identity is interpreted literally.

**Theorem.** For every prime power \(q\), the number of distinct admissible products on the fixed three-dimensional vector space \(\mathfrak t_2(\mathbf F_q)\), **not modulo isomorphism**, is
\[
\boxed{\#\mathcal T_2(\mathbf F_q)=
\begin{cases}
q^4+q^3-q^2,&q\text{ odd},\\
q^6+2q^5-q^4-q^2,&q\text{ even}.
\end{cases}}
\]
The underlying reduced parameter varieties have dimensions \(4\) in odd characteristic and \(6\) in characteristic two. In odd characteristic the variety is a product of an affine line and a two-by-two rank-at-most-one determinantal cone. In characteristic two it has a six-dimensional open locus obtained by splitting off an idempotent central summand; its square-zero-central boundary is controlled by characters and associative extensions of trace-zero two-dimensional commutative algebras.

For fixed \(q\), extension-field counts follow by substituting \(q^r\) in the formula. Thus the point-count zeta functions are
\[
Z_q(T)=\begin{cases}
\dfrac{1-q^2T}{(1-q^3T)(1-q^4T)},&q\text{ odd},\\[6pt]
\dfrac{(1-q^2T)(1-q^4T)}{(1-q^5T)^2(1-q^6T)},&q\text{ even}.
\end{cases}
\]

## Assumptions and scope
Put \(x=E_{11}\), \(y=E_{12}\), and \(z=E_{11}+E_{22}\), so \(x,y,z\) form a basis in every characteristic and
\[
[x,y]=y,\qquad [x,z]=[y,z]=0.
\]
A product means a symmetric bilinear map \(L\times L\to L\), considered with this fixed basis. Nothing is classified modulo the automorphism group. The polynomial identity above is used even when \(2=0\); this is an integral/polynomial specialization, not the characteristic-zero \(\frac12\)-derivation interpretation. The theorem applies to every finite field; the parameter descriptions and dimension assertions apply to arbitrary fields of the specified characteristics. The empty/nonzero-product convention is avoided by explicitly including the zero multiplication.

## Proof
**Odd characteristic.** Expansion of the transposed identity on basis triples is equivalent to the unique five-parameter multiplication table
\[
\begin{aligned}
x\cdot x&=e x+b y+c z,&x\cdot y&=e y,&x\cdot z&=i z,\\
y\cdot y&=0,&y\cdot z&=0,&z\cdot z&=s z.
\end{aligned}
\]
(The parameter letters range independently over \(K\), before associativity is imposed.) Commutativity is built in. Its full associativity condition is just
\[
i(e-i)+cs=0.\]
The change of variables \((e,i,c,s)\mapsto(i,e-i,c,s)\) is invertible. The equation is the vanishing determinant of a two-by-two matrix, with the parameter \(b\) free. The number of rank-zero or rank-one two-by-two matrices over \(\mathbf F_q\) is
\[
1+\frac{(q^2-1)^2}{q-1}=q^3+q^2-q.
\]
Multiplying by \(q\) gives the odd-characteristic formula. This determinantal cone is geometrically irreducible of dimension \(3\), so the full parameter variety is geometrically irreducible of dimension \(4\).

**Characteristic two: the complete equations.** Direct expansion of the same integral identity, now with \(2=0\), gives ten free linear parameters and the table
\[
\begin{aligned}
x\cdot x&=e x+b y+c z,&x\cdot y&=k x+e y+f z,\\
y\cdot y&=j x+k y+l z,&x\cdot z&=i z,\\
y\cdot z&=o z,&z\cdot z&=s z.
\end{aligned}
\]
The full associativity conditions, necessary and sufficient, are the following six equations:
\[
\begin{aligned}
ek+bj&=0,\\
bl+c(k+o)+fi&=0,\\
bo+cs+ei+i^2&=0,\\
jc+(e+i)l+fo&=0,\\
ki+eo+fs+oi&=0,\\
ji+ko+ls+o^2&=0.
\end{aligned}
\tag{1}
\]
All signs here are additions in characteristic two.

**The quotient algebra.** The line \(Kz\) is an ideal for every multiplication of this form. The quotient \(B=L/Kz\), with basis denoted again by \(x,y\), has multiplication
\[
x^2=e x+b y,\qquad xy=k x+e y,\qquad y^2=j x+k y.
\tag{2}
\]
Each left-multiplication operator of \(B\) has trace zero; conversely, every trace-zero commutative multiplication in dimension two has exactly this form. Its associativity is equivalent to \(ek+bj=0\). Consequently the number of possible quotients over \(\mathbf F_q\) is the rank-one determinantal count
\[
B_q=q^3+q^2-q.
\tag{3}
\]
The trace-zero condition is invariant under all invertible changes of basis of \(B\).

**Case \(s\ne0\).** The element \(t=s^{-1}z\) is idempotent, and multiplication by \(t\) is an idempotent linear operator with image \(Kt\). Subtracting suitable multiples of \(z\) from \(x,y\) yields elements annihilated by \(t\). They span a complementary subalgebra naturally isomorphic to \(B\); hence the product is the orthogonal direct sum of \(B\) with \(Kt\). For any associative quotient \(B\), any nonzero \(s\), and any \((i,o)\in K^2\), this determines \(c,f,l\) uniquely through the third, fifth and sixth equations in (1), and the remaining equations follow automatically. Hence
\[
N_{s\ne0}=(q-1)q^2 B_q=q^6-2q^4+q^3.
\tag{4}
\]
In particular this open locus has dimension \(3+2+1=6\) and is geometrically irreducible.

**Case \(s=0\).** Now \(Kz\) is square-zero. Multiplication by elements of \(B\) on this ideal defines a linear map \(\alpha:B\to K\) with \(\alpha(x)=i\) and \(\alpha(y)=o\). Associativity involving one factor \(z\) says precisely that \(\alpha\) is a (possibly zero) multiplicative character of \(B\):
\[
i^2=ei+bo,\qquad io=ki+eo,\qquad o^2=ji+ko.
\tag{5}
\]
If \(\alpha=0\), all \(B_q\) associative quotients are permitted. For a fixed nonzero \(\alpha\), change the basis of \(B\) to make \(\alpha(x)=1\), \(\alpha(y)=0\). The trace-zero condition is basis-invariant, and (5) forces \(e=1\), \(k=j=0\), leaving exactly \(q\) possibilities for \(b\). Thus the total number of pairs \((B,\alpha)\) is
\[
C_q=B_q+(q^2-1)q=2q^3+q^2-2q.
\tag{6}
\]
For each such pair, associativity of the extension with respect to the remaining coefficients \((c,f,l)\) is the linear system
\[
\begin{pmatrix}k+o&i&b\\j&o&e+i\end{pmatrix}
\begin{pmatrix}c\\f\\l\end{pmatrix}=0.
\tag{7}
\]
All its two-by-two minors vanish: in order of column pairs they equal \(ko+o^2+ij\), \(ek+ki+eo+oi+bj\), and \(ei+i^2+bo\), each zero by (2), (5) and associativity of \(B\). The matrix has rank zero only when \(B\) is the zero multiplication and \(\alpha=0\). Therefore one pair has \(q^3\) extensions, and each of the other \(C_q-1\) pairs has \(q^2\) extensions. Hence
\[
N_{s=0}=q^3+(C_q-1)q^2=2q^5+q^4-q^3-q^2.
\tag{8}
\]
Adding (4) and (8) yields the even-characteristic count. The square-zero boundary has dimension at most \(5\): the zero-character fiber has dimension at most \(3+2=5\), and the nonzero-character fibers have dimensions \(2+1+2=5\). The open locus (4) has dimension \(6\), so the total reduced parameter variety has dimension \(6\).

**Zeta functions.** The same structural arguments hold over each field \(\mathbf F_{q^r}\). Substituting \(q^r\) into the two polynomial counts and using
\[
\exp\left(\sum_{r\ge1}\frac{a^rT^r}{r}\right)=(1-aT)^{-1}
\]
gives the two displayed rational functions.

## Verification
A standalone standard-library script, `verify.py`, is included. Run `python3 verify.py` from the extracted file directory. It checks the dimensions of the linear compatibility spaces over \(\mathbf F_2\) and \(\mathbf F_3\), evaluates the defining identities on every basis triple for all ten-parameter candidates over \(\mathbf F_2\) and all five-parameter candidates over \(\mathbf F_3\), and independently counts admissible tables over \(\mathbf F_2,\mathbf F_4,\mathbf F_3,\mathbf F_5,\mathbf F_7\). It further enumerates quotient/character/rank strata over \(\mathbf F_{2^r}\) for \(r=1,2,3,4\). The run returned `VERIFY_OK`, including total counts \(108,5872,323520,18808576\) for the four characteristic-two test fields. These finite computations check the algebra and arithmetic, but the all-fields theorem follows from the preceding symbolic proof, not from interpolation.

## Relationship to prior work
The motivating work of Kaygorodov and Khrypchenko, *Transposed Poisson structures on the Lie algebra of upper triangular matrices* (arXiv:2305.00727, first posted 2023-05-01), proves a classification up to isomorphism for upper triangular Lie algebras **over characteristic-zero fields**, including the rank-two case in Theorem 12. Its complex/characteristic-zero classification is prior coverage, not a claimed new classification here. Their later work on Lie incidence algebras (arXiv:2309.00332, Theorem 3.20 and Example 3.22) also assumes characteristic zero and recovers that case. Beites–Fernández Ouaridi–Kaygorodov describe all complex three-dimensional transposed Poisson algebras, again up to isomorphism. The original polynomial identity is Definition 1.2 of Bai–Bai–Guo–Wu (arXiv:2005.01110).

The new claim is the uniform **fixed-bracket, labeled finite-field count and dimension jump**, especially the characteristic-two square-zero extension count. No cited characteristic-zero isomorphism classification entails that formula across the characteristic-two fiber. The odd-characteristic determinantal description supplies the comparison side and is not presented as a new complex classification. Related parameter varieties or finite-field counts may exist under terminology from commutative associative extensions or modular Lie-compatible products; equivalence has not been ruled out absolutely.

## Limitations
The count is for products on one fixed Lie algebra, not for isomorphism classes, automorphism orbits, or moduli stacks. The characteristic-two theory is explicitly the specialization of the **polynomial** transposed Leibniz identity, and some conventions that require division by two would exclude that characteristic; the statement does not identify those theories. The result describes rational points and dimensions, not a full decomposition of the characteristic-two scheme into irreducible components or its nonreduced structure. The verifier covers only the listed finite fields and is not a substitute for the proof. Originality assessment is limited to the actually inspected literature and available published records.

## References
1. I. Kaygorodov and M. Khrypchenko, *Transposed Poisson structures on the Lie algebra of upper triangular matrices*, arXiv:2305.00727v1 (2023-05-01), especially Theorem 12. https://arxiv.org/pdf/2305.00727
2. I. Kaygorodov and M. Khrypchenko, *Transposed Poisson structures on Lie incidence algebras*, arXiv:2309.00332v1 (2023-09-01), especially Theorem 3.20 and Example 3.22. https://arxiv.org/pdf/2309.00332
3. P. D. Beites, A. Fernández Ouaridi and I. Kaygorodov, *The algebraic and geometric classification of transposed Poisson algebras*, Rev. R. Acad. Cienc. Exactas Fís. Nat. Ser. A-Mat. 117 (2023), article 55, DOI 10.1007/s13398-022-01385-4. https://doi.org/10.1007/s13398-022-01385-4
4. C. Bai, R. Bai, L. Guo and Y. Wu, *Transposed Poisson algebras, Novikov-Poisson algebras and 3-Lie algebras*, arXiv:2005.01110v1 (2020-05-03), Definition 1.2. https://arxiv.org/pdf/2005.01110
