# Graded homomorphisms and retraction spectra of permutation-idempotent Yang–Baxter algebras

## Finding

For any field \(K\) and integers \(m,n\ge 2\), let
\[
 A_n(K)=K\langle x_1,\ldots,x_n\rangle/\bigl(x_i x_j-x_1x_j:2\le i\le n,\ 1\le j\le n\bigr)
\]
with its word-length grading. Write \(V_n=(A_n)_1\), \(\varepsilon_n(\sum_i a_i x_i)=\sum_i a_i\), and \(H_n=\ker\varepsilon_n\). A homomorphism is understood throughout to be a **unital, degree-preserving \(K\)-algebra homomorphism**.

**Theorem (a joint graded-homomorphism and retraction classification).**

1. All graded homomorphisms \(A_n\to A_m\) are determined uniquely by their degree-one maps \(F:V_n\to V_m\). Such a linear map extends if and only if
   \[\varepsilon_m\circ F=c\varepsilon_n\quad\text{for some unique }c\in K.\]
   Hence their degree-one matrices form a vector space of dimension \(1+n(m-1)\). Over \(\mathbb F_q\), there are exactly \(q^{1+n(m-1)}\) such homomorphisms.
2. For \(n=m\), fix \(x_1\) as a complement to \(H_n\). Every graded endomorphism has a unique block matrix
   \[F=\begin{pmatrix}c&0\\u&B\end{pmatrix},\qquad u\in H_n,\ B\in\operatorname{End}_K(H_n).\]
   It is a retraction (composition-idempotent endomorphism) if and only if
   \[c\in\{0,1\},\qquad B^2=B,\qquad Bu=(1-c)u.\]
   All retractions whose \(c=0\) and degree-one rank is \(r\) have image isomorphic, as graded algebras, to \(K\oplus K^r\) with the positive-degree part in degree one and square-zero multiplication. All retractions with \(c=1\) and degree-one rank \(r\) have image isomorphic to \(A_r(K)\), necessarily with \(1\le r\le n\). In the one-generator boundary case, define \(A_1(K)=K[t]\) with \(t\) in degree one; the square-zero image at \(r=0\) is \(K\).
3. Under conjugation by graded algebra automorphisms, exactly one retraction occurs for each pair \((c,r)\) with \(c=0\) and \(0\le r\le n-1\), or \(c=1\) and \(1\le r\le n\). Thus there are exactly \(2n\) conjugacy classes. The graded automorphism group is the group of block matrices above with \(c\ne0\) and \(B\in\operatorname{GL}(H_n)\).
4. Over \(\mathbb F_q\), the exact labeled counts for those two types, at degree-one rank \(r\), are
   \[
   N_{n,q}(0,r)={n-1\brack r}_q q^{r(n-r)},\qquad
   N_{n,q}(1,r)={n-1\brack r-1}_q q^{r(n-r)}.
   \]
   The Gaussian coefficient is zero when its lower index is out of range. Consequently the complete rank polynomial for graded algebra retractions is
   \[
   \\(R_{n,q}\\)(T)=\sum_{r=0}^{n}q^{r(n-r)}\left({n-1\brack r}_q+{n-1\brack r-1}_q\right)T^r.
   \]
   It is palindromic of degree \(n\). For instance, \(R_{4,2}(T)=1+64T+224T^2+64T^3+T^4\).

These conclusions apply uniformly to the Yang–Baxter algebras of all permutation-idempotent solutions with \(n\) generators, via the established canonical presentation of Gateva-Ivanova and Majid.

## Assumptions and scope

No characteristic or algebraic-closure hypothesis is imposed. Only unital homomorphisms respecting word-length grading are classified; neither arbitrary ungraded algebra maps nor morphisms of the underlying set-theoretic Yang–Baxter solutions are covered. Retraction rank means rank of the induced **degree-one linear map**, not rank on the infinite-dimensional underlying vector space. Here \(n,m\ge2\) and \(q\) is any prime power.

The published PBW basis is \(\{1\}\cup\{x_1^{d-1}x_j:d\ge1,\ 1\le j\le n\}\). Its linear independence is essential: identifying every positive-degree component with \(V_n\), multiplication of positive-degree homogeneous elements represented by \(u,v\in V_n\) becomes \(u\cdot v=\varepsilon_n(u)v\), where the product lives in the component whose degree is the sum of input degrees.

## Proof

**Homomorphism criterion.** Let \(F:V_n\to V_m\) be the degree-one part of a prospective graded homomorphism. For every defining relation, preservation of the relation means
\[
 F(x_i-x_1)F(x_j)=\bigl(\varepsilon_m(Fx_i)-\varepsilon_m(Fx_1)\bigr)\,F(x_j)=0
\]
in the target's degree-two PBW coordinates. If \(F\ne0\), some column \(F(x_j)\) is nonzero; independence of the normal degree-two words forces the first scalar to vanish for every \(i\). Thus \(\varepsilon_m F=c\varepsilon_n\) with \(c=\varepsilon_m(Fx_1)\). If \(F=0\), take \(c=0\). Conversely this equation annihilates every defining relation, so the universal property of the presented algebra extends \(F\) uniquely. The scalar \(c\) is unique because \(\varepsilon_n\ne0\). A choice of the \(n\) images yields \(nm\) coordinates constrained by \(n-1\) independent equalities of their coordinate sums, leaving dimension \(nm-(n-1)=1+n(m-1)\).

**Behavior in higher degrees.** In the PBW identification \((A_n)_d\cong V_n\), for \(d\ge1\), the induced degree-\(d\) map is
\[F_d=c^{d-1}F.\]
Indeed, \(x_1^{d-1}v\) maps to \(F(x_1)^{d-1}F(v)\), and the positive-degree multiplication rule gives exactly that expression. For \(d=1\), the scalar is interpreted as \(1\), including \(c=0\).

**Retraction equations and images.** An algebra endomorphism generated in degree one obeys \(\varphi^2=\varphi\) if and only if \(F^2=F\). The compatibility \(\varepsilon_n F=c\varepsilon_n\) gives \(F(Kx_1)\subseteq Kx_1+H_n\) and \(F(H_n)\subseteq H_n\), hence the displayed block matrix. Multiplying it by itself yields \(c^2=c\), \(B^2=B\), \(cu+Bu=u\). Over a field, the first equation gives \(c=0\) or \(1\).

When \(c=0\), \(\operatorname{im}F\subseteq H_n\), \(\operatorname{rank}F=\operatorname{rank}B=r\), and \(F_d=0\) for every \(d\ge2\). Thus the image is \(K\oplus\operatorname{im}F\), a square-zero extension in degree one. When \(c=1\), the image is present in all positive degrees, each isomorphic to \(\operatorname{im}F\), of dimension \(r=1+\operatorname{rank}B\). The restricted functional \(\varepsilon_n\) is onto on \(\operatorname{im}F\) since \(\varepsilon_n F=\varepsilon_n\); choose a basis \(y_1,\ldots,y_r\) of this image with \(\varepsilon_n(y_1)=1\) and \(\varepsilon_n(y_i)=0\) for \(i>1\). Their products satisfy \(y_i y_j=y_1 y_j\). The normal products \(y_1^{d-1}y_j\) are independent in every degree because the ambient degree-\(d\) PBW identification maps them to the linearly independent \(y_j\). Therefore the image is precisely \(A_r(K)\), not merely a quotient of it.

**Conjugacy.** An invertible graded homomorphism is characterized by \(c\ne0\) and invertible \(B\). Conjugation by a shear \(S=\left(\begin{smallmatrix}1&0\\v&I\end{smallmatrix}\right)\) sends the lower-left block \(u\) of \(F\) to \(u+(cI-B)v\). For \(c=0\), \(Bu=u\), so set \(v=u\); for \(c=1\), \(Bu=0\), so set \(v=-u\). Either choice removes \(u\). Every idempotent endomorphism \(B\) is conjugate under \(\operatorname{GL}(H_n)\) to the projection onto a subspace of dimension \(\operatorname{rank}B\). The scalar \(c\) and \(r=\operatorname{rank}F\) are conjugacy invariants, establishing all and only the stated \(2n\) orbits.

**Finite-field counts.** Put \(h=n-1\). Rank-\(s\) projections \(B\) on \(H_n\cong\mathbb F_q^h\) correspond bijectively to ordered decompositions into an image \(U\) of dimension \(s\) and a complementary kernel. There are \({h\brack s}_q\) choices for \(U\) and \(q^{s(h-s)}\) complements. For \(c=0\), \(Bu=u\) means \(u\in U\): \(q^s\) choices, \(r=s\). For \(c=1\), \(Bu=0\) means \(u\) belongs to the kernel: \(q^{h-s}\) choices, \(r=s+1\). Substitution proves both formulas. Gaussian symmetry \({n-1\brack r}_q={n-1\brack n-1-r}_q\) interchanges the two summands under \(r\mapsto n-r\), proving palindromicity. The rank labels and counts include the zero-on-generators endomorphism and identity, each once.

## Verification

The supplied standalone `checker.py` directly checks every defining quadratic relation in target degree-two PBW coordinates and composition idempotence of every candidate degree-one matrix; it then compares rank-and-scalar frequencies with the closed formula. The complete prime-field matrix enumerations cover \((n,q)=(2,2),(2,3),(2,5),(3,2),(3,3),(4,2)\). Rectangular homomorphism enumerations cover \((n,m,q)=(2,3,2),(3,2,2),(2,2,3),(3,2,3)\). All tests return `VERIFY_OK`. The general result is the preceding symbolic proof, not an inference from these finite samples. Reproduce with `python3 checker.py` using the Python standard library.

## Relationship to prior work

Gateva-Ivanova and Majid established the canonical quadratic presentation and PBW basis in their 2023 Theorem 3.4 and treated Veronese and Segre maps. Their 2024 Proposition 5.3 extends the structural viewpoint and repeats this canonical presentation. Colazzo–Jespers–Kubat–Van Antwerpen–Verwimp supplied an earlier structural study of finite idempotent Yang–Baxter solutions and their monoid algebras. These results are the premises credited above. The present theorem concerns *all degree-preserving algebra homomorphisms*, the complete classification of their composition-idempotent members, image isomorphism types, conjugacy classes, and finite-field rank counts; Veronese morphisms alter the grading and are not instances of the restricted graded retractions. Literature comparisons remain subject to the risk that equivalent algebra-map results appear under alternative terminology.

## Limitations

Only the canonical permutation-idempotent class is treated, not all left-nondegenerate idempotent Yang–Baxter solutions. The parameter counts are of labeled graded algebra maps and retracting endomorphisms, not isomorphism classes of set-theoretic solutions or total ungraded endomorphisms. Finite checks cover small prime fields; the arbitrary-field and arbitrary-prime-power assertions rely on proof. No general uniqueness, independence, or exhaustive bibliographic certification is asserted.

## References

1. T. Gateva-Ivanova and S. Majid, *Quadratic algebras associated to permutation idempotent solutions of the YBE*, arXiv:2308.11427, first posted 2023-08-22; Theorem 3.4, Corollaries 3.5–3.6, Sections 6–7. https://arxiv.org/abs/2308.11427
2. T. Gateva-Ivanova and S. Majid, *Quadratic algebras and idempotent braided sets*, arXiv:2409.02939, first posted 2024-08-23; Proposition 5.3 and Sections 6–7. https://arxiv.org/abs/2409.02939
3. I. Colazzo, E. Jespers, Ł. Kubat, A. Van Antwerpen and C. Verwimp, *Finite idempotent set-theoretic solutions of the Yang–Baxter equation*, arXiv:2212.07361, first posted 2022-12-14; Example 3.15 and Corollary 3.17. https://arxiv.org/abs/2212.07361
