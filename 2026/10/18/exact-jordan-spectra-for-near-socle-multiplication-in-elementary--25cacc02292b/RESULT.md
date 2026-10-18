# Exact Jordan spectra for near-socle multiplication in elementary abelian \(2\)-group algebras

## Finding

Let \(q=2^e\) with \(e\ge1\), let \(n\ge6\), and write
\[
A=\mathbb F_q[(C_2)^n]\cong\mathbb F_q[x_1,\ldots,x_n]/(x_1^2,\ldots,x_n^2)=\bigwedge_{\mathbb F_q} V,\qquad\dim V=n.
\]
Choose the standard grading by the variables \(x_i=g_i-1\). For every homogeneous element \(u\in A_{n-3}\), left multiplication \(L_u:A\to A\) satisfies \(L_u^2=0\). Fix a volume functional on \(\bigwedge^n V\) and define the alternating trilinear form
\[
\alpha_u(v,w,z)=\operatorname{vol}(u\wedge v\wedge w\wedge z).
\]
Put \(r(u)=\operatorname{rank}(V\to\bigwedge^2 V^*,\ v\mapsto\iota_v\alpha_u)\). For nonzero \(u\),
\[
\operatorname{rank}L_u=2+2r(u),\qquad
\operatorname{JType}(L_u)=\bigl(2^{\,2+2r(u)},1^{\,2^n-4-4r(u)}\bigr).
\]
For \(u=0\), the Jordan type is \(1^{2^n}\). The possible nonzero values of \(r(u)\) are **exactly** \(3\) and all integers between \(5\) and \(n\), inclusive. Thus multiplication rank \(10\) is impossible, even though ranks \(8\) and \(12\) occur for every \(n\ge6\).

The multiplicity of each nonzero Jordan type is an explicit finite sum. Define the Gaussian coefficient \(\genfrac{[}{]}{0pt}{}{m}{j}_q\) and
\[
F_m(q)=\sum_{j=0}^m(-1)^{m-j}q^{\binom{m-j}{2}}\genfrac{[}{]}{0pt}{}{m}{j}_q\,q^{\binom j3},\quad F_0(q)=1.
\]
Then the number of elements with \(r(u)=r\) is
\[
N_{n,q}(r)=\genfrac{[}{]}{0pt}{}{n}{r}_qF_r(q)\quad (r\in\{3,5,\ldots,n\}),
\]
and \(N_{n,q}(r)=0\) for other nonzero values. Together with the single zero element, these counts sum to \(q^{\binom n3}\), the number of elements in \(A_{n-3}\).

## Assumptions and scope

All fields have order a power of two; the degree and grading are essential. The theorem concerns **all coefficients** of homogeneous elements of degree exactly \(n-3\) in the regular module, and not arbitrary inhomogeneous elements, odd-characteristic exterior algebras, or general modules. A Jordan block of size \(j\) is denoted \(j\) in the partition; the exponent on a part denotes multiplicity. The \(q\)-Gaussian coefficient counts subspaces. We use the convention \(\binom j3=0\) for \(j<3\).

## Proof

**Step 1: Identify the group algebra and the perfect pairing.** Each element \(x_i=g_i-1\) has square zero in characteristic two, and distinct \(x_i\) commute. The resulting truncated-polynomial algebra has basis of square-free monomials and is the exterior algebra as an associative algebra in characteristic two. Multiplication followed by the chosen volume map is a perfect pairing \(A_i\times A_{n-i}\to\mathbb F_q\). Consequently, exterior multiplication \(A_{n-3}\to (\bigwedge^3 V)^*\) is an isomorphism. Because every positive-degree element of the truncated algebra squares to zero in characteristic two, \(L_u^2=0\).

**Step 2: Determine the complete multiplication rank.** Homogeneity confines the possibly nonzero graded maps for \(L_u\) to
\[
A_0\to A_{n-3},\quad A_1\to A_{n-2},\quad A_2\to A_{n-1},\quad A_3\to A_n.
\]
The first and last have rank \(1\) when \(u\ne0\), by the perfect pairing. Under the perfect pairing, the middle two maps are transposes. The map on \(A_1\) is the transpose of the contraction \(V\to\bigwedge^2V^*\), hence each middle map has rank \(r(u)\). Their targets are in different graded pieces, so the ranks add, giving \(2+2r(u)\). A square-zero operator with rank \(R\) on a vector space of dimension \(2^n\) has precisely \(R\) Jordan blocks of size two and \(2^n-2R\) singleton blocks.

**Step 3: Determine the possible contraction ranks.** If a nonzero alternating trilinear form has contraction kernel \(K\), it descends uniquely to an alternating trilinear form on \(V/K\) with zero contraction kernel. There can be no such nonzero form in dimensions one or two. In dimension four, any three-form is a contraction of a nonzero volume four-form by some vector, and that vector lies in the contraction kernel; therefore contraction rank four is impossible. Full-contraction-rank examples are \(e^{123}\) in dimension three; \(e^{123}+e^{145}\) in dimension five; \(e^{123}+e^{456}\) in dimension six; and \(e^{123}+e^{145}+e^{167}\) in dimension seven. Their contractions are linearly independent (direct coefficient inspection). A direct sum of forms supported on independent subspaces has full contraction rank equal to the sum of those dimensions. Every integer \(r\ge8\) is \(5+3a\), \(6+3a\), or \(7+3a\) for some nonnegative integer \(a\), so all \(r\ge5\) arise. Extending by zero on \(n-r\) coordinates realizes every such contraction rank \(r\le n\), as well as rank three.

**Step 4: Count every fiber.** Write \(F_m(q)\) for the number of three-forms on \(\mathbb F_q^m\) with zero contraction kernel. For every \(m\), each three-form uniquely determines its contraction kernel, and forms with kernel dimension \(m-j\) are obtained by choosing that subspace and pulling back a full-contraction-rank form from the quotient. Thus
\[
q^{\binom m3}=\sum_{j=0}^{m}\genfrac{[}{]}{0pt}{}{m}{j}_q F_j(q).
\]
Möbius inversion in the lattice of subspaces, whose interval Möbius function on an \(h\)-space is \((-1)^h q^{\binom h2}\), yields the displayed finite sum for \(F_m(q)\). There are \(\genfrac{[}{]}{0pt}{}{n}{r}_q\) possible contraction kernels of codimension \(r\); multiplying by \(F_r(q)\) gives \(N_{n,q}(r)\). Uniqueness of the kernel partition proves the total-sum identity. The zero form corresponds to \(u=0\).

## Verification

The attached `verify.py` provides independent executable checks using exact finite-field arithmetic. In \(6\) variables over \(\mathbb F_2\), **all** \(2^{20}=1{,}048{,}576\) degree-three forms were exhaustively enumerated with an independent bit-matrix contraction-rank routine. The frequencies by multiplication rank \(0,8,12,14\) are respectively \(1,1395,54684,992496\), matching the formula. The script also constructs full exterior-multiplication matrices for \(90\) reproducibly sampled forms in each of four tests: \((n,q)=(6,2),(7,2),(6,4),(7,4)\), and checks the rank equality. The Gaussian recurrence and sum identities are checked for \(6\le n\le11\) and \(q=2,4,8\). Execute `python3 verify.py`. Finite tests are consistency checks; the preceding algebraic argument is the proof for every \(n\) and \(q\) in scope.

## Relationship to prior work

Carlson, Friedlander, and Pevtsova (2007) study Jordan types in representations of finite group schemes and elementary abelian groups, especially modules of constant Jordan type. The result here concerns the coefficient-by-coefficient Jordan-type **distribution** for multiplication by elements of a specific high homogeneous degree in a fixed regular module; it is not an implication of constancy of Jordan type along projective points. Cohen and Helminck classify alternating trilinear forms in dimensions at most seven over suitable fields, including finite fields; their explicit orbits imply bounded-dimensional special cases of the count of contraction kernels, not the all-dimensional counting theorem stated here. Hora and Pudlák's 2015 work gives an explicit classification in dimension eight over the binary field. It potentially covers that special case and discusses general radical invariants, so the extent of implicit general coverage is a residual literature risk. This result derives an unbounded-dimensional frequency formula without classifying full linear-group orbits. Related work on Jordan types of Artinian algebras develops general properties but does not, in the material checked, state this fixed graded-coefficient census.

## Limitations

The theorem applies only in characteristic two and only to homogeneous degree \(n-3\), for \(n\ge6\); no analogous claim is made for different degrees or general modules. The count is a finite Gaussian sum, not a closed product formula for the full-support term. Special dimensions and fields may already be covered by prior orbit classifications. All novelty statements are conditional on the documented primary-literature and database comparisons; no claim of exhaustive bibliographic coverage or independent validation is made.

## References

1. J. F. Carlson, E. M. Friedlander, J. Pevtsova, *Modules of constant Jordan type*, arXiv:0707.3845v1 (first public posting 25 July 2007), https://arxiv.org/abs/0707.3845.
2. A. M. Cohen and A. G. Helminck, *Trilinear alternating forms on a vector space of dimension 7*, CWI Report PM-R8402 (1984); journal version, *Communications in Algebra* 16 (1988), https://pure.tue.nl/ws/files/2438505/335710.pdf.
3. J. Hora and P. Pudlák, *Classification of 8-dimensional trilinear alternating forms over GF(2)*, *Communications in Algebra* 43 (2015), 3459–3471, https://doi.org/10.1080/00927872.2014.927475.
4. J. F. Carlson, E. M. Friedlander, J. Pevtsova, *Representations of elementary abelian p-groups and bundles on Grassmannians*, arXiv:1106.4474v1 (2011), https://arxiv.org/abs/1106.4474.
5. A. Iarrobino, P. Macias Marques, C. McDaniel, *Artinian algebras and Jordan type*, arXiv:1802.07383 (2018), https://arxiv.org/abs/1802.07383.
