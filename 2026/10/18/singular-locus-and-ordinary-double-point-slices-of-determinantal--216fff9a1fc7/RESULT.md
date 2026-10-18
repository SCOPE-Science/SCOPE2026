# Singular locus and ordinary-double-point slices of determinantal first-jet principal components

## Finding
Fix integers \(3\le m\le n\). The principal component \(P_{m,n}\) of first jets on the rank-one determinantal cone has dimension \(2(m+n-1)\) and satisfies
\[
\operatorname{Sing}(P_{m,n})_{\mathrm{red}}=\{(X,Y):X=0,\ \operatorname{rank}(Y)\le2\}.
\]
This singular support is irreducible of dimension \(2(m+n-2)\), hence of codimension two. At every point where \(X=0\) and \(\operatorname{rank}(Y)=2\), there is a Zariski-local product presentation with a smooth \(2(m+n-2)\)-fold and the surface cone \(a^2+bc=0\). Therefore the generic transverse surface singularity is \(A_1\), has Hilbert--Samuel multiplicity two, and \(P_{m,n}\) itself is normal and Cohen--Macaulay.

## Assumptions and scope
Work over an algebraically closed field \(K\) of characteristic zero. Let \(X=(x_{ij})\) and \(Y=(y_{ij})\) be arbitrary \(m\times n\) matrices. The rank-at-most-one cone \(D_{m,n}\subset\mathbb A^{mn}\) is defined by its \(2\times2\) minors. Its first jet scheme is cut out by the constant and linear coefficients in all minors of \(X+tY\). Define \(P_{m,n}\) as the *reduced scheme-theoretic closure* of jets over \(D_{m,n}\setminus\{0\}\), rather than the entire (reducible) first jet scheme.

For increasing row indices \(i<j\) and column indices \(k<l\), define
\[
\Delta_{ij;kl}=x_{ik}x_{jl}-x_{il}x_{jk},\qquad
E_{ij;kl}=x_{ik}y_{jl}+y_{ik}x_{jl}-x_{il}y_{jk}-y_{il}x_{jk}.
\]
Write \(\Psi\) for the family of \(3\times3\) minors of \(Y\). Košir--Sethuraman, Theorem 2.4 and Proposition 3.3 [2], establish that the prime defining ideal of \(P_{m,n}\) is exactly \((\Delta,E,\Psi)\). The Cohen--Macaulay property of this coordinate ring is Jonov's Theorem 1.2 [3]. These external inputs are explicitly distinguished from the additional local calculation below.

## Proof
**Dimension and smooth locus away from the zero section.** The nonzero rank-one cone \(D_{m,n}\setminus\{0\}\) is smooth of dimension \(m+n-1\). First jets on any smooth \(d\)-fold form a rank-\(d\) vector bundle (the tangent bundle), so the principal component has dimension \(2(m+n-1)\) and is smooth at every point with \(X\ne0\). The ideal above also gives
\[
P_{m,n}\cap\{X=0\}=\{X=0,\operatorname{rank}(Y)\le2\}
\]
as schemes, because \(\Delta\) and \(E\) vanish identically when \(X=0\), leaving precisely \(\Psi\).

**Local form on the rank-two stratum.** Fix a point with \(\operatorname{rank}(Y)=2\). After fixed row and column permutations, work on the principal open subset where the leading \(2\times2\) block \(A\) of \(Y\) is invertible. In block form write
\[
Y=\begin{pmatrix}A&B\\C&D\end{pmatrix},\qquad S=D-CA^{-1}B.
\]
The invertible regular matrices
\[
L(Y)=\begin{pmatrix}A^{-1}&0\\-CA^{-1}&I_{m-2}\end{pmatrix},
\qquad R(Y)=\begin{pmatrix}I_2&-A^{-1}B\\0&I_{n-2}\end{pmatrix}
\]
turn \(Y\) into \(\operatorname{diag}(I_2,S)\). Since rank conditions and coefficients of the minors of \(X+tY\) are unchanged up to invertible linear combinations under \((X,Y)\mapsto(LXR,LYR)\), this is a regular invertible change of ambient coordinates on the chart. The \(3\times3\) minors of \(Y\) generate the ideal \((S_{ij})\) there: each entry \(S_{ij}\) occurs as a minor containing the first two pivot rows and columns, and every \(3\times3\) minor vanishes when \(S=0\). Thus, in the *scheme* under study, \(Y'\) becomes \(\operatorname{diag}(I_2,0)\), while the entries of \(A,B,C\) give free coordinates on the smooth rank-two matrix locus of dimension
\[
4+2(n-2)+2(m-2)=2(m+n-2).
\]
Now the polarized minors \(E(X',Y')=0\) force \(X'\) to vanish outside the leading \(2\times2\) block, and force the trace of that block to vanish. Hence
\[
X'=\begin{pmatrix}a&b&0\\c&-a&0\\0&0&0\end{pmatrix}
\]
with evident zero-block notation for general \(m,n\). All remaining \(2\times2\) minors of \(X'\) vanish except for one equivalent equation \(-a^2-bc=0\). This gives the asserted *scheme-level* local isomorphism to a smooth rank-two-matrix chart times \(\operatorname{Spec}K[a,b,c]/(a^2+bc)\). The quadratic cone is singular exactly at \(a=b=c=0\); its Jacobian equations are \(2a,b,c\). In characteristic zero this is an isolated ordinary double point (surface rational double point \(A_1\)) of multiplicity two.

**The full singular support.** The above charts prove that every point with \(X=0\) and \(\operatorname{rank}(Y)=2\) is singular. This is dense in the irreducible determinantal variety \(\{X=0,\operatorname{rank}(Y)\le2\}\). Since the singular locus of a finite-type variety is closed, its lower-rank boundary is also singular. Conversely all points outside that fiber have \(X\ne0\), where the principal component is smooth. The determinantal rank-two variety of \(m\times n\) matrices has dimension \(2(m+n-2)\), giving the stated codimension two and irreducibility.

**Normality.** The coordinate ring is a domain by the prime description of Košir--Sethuraman [2]. Jonov's Cohen--Macaulay theorem [3] proves Serre's condition \(S_2\). Since the singular locus has codimension two, this domain is regular in codimension one (condition \(R_1\)). By Serre's criterion it is normal. The proof uses no finite-data extrapolation.

## Verification
Execute the embedded independent arithmetic check with `python3 check_transverse_jet.py`. For all ten pairs \(3\le m\le n\le6\) and for both test matrices \(Y=\operatorname{diag}(I_r,0)\), \(r=1,2\), the script constructs the full linearized polarized-minor system \(E\) and the differential of the \(3\times3\)-minor system \(\Psi\), then computes their exact ranks modulo \(101\). The 20 cases reproduce the expected excess tangent dimensions: one for rank two, and strictly positive excess for rank one. The checker verifies local tangent arithmetic only; the general argument is the algebraic chart computation given above, with no reliance on modular rank checks for characteristic-zero correctness.

## Relationship to prior work
Košir--Sethuraman [1] established the component picture, including the existence of the nonprincipal component; [2] established the prime generating ideal used here. Jonov [3] proved Cohen--Macaulayness; Ghorpade--Jonov--Sethuraman [4] computed Hilbert series, multiplicity, and the Gorenstein criterion. Yuen [5] and Docampo [6] study components and related jet-scheme invariants. The additional result here is the complete reduced *singular support of the principal component*, the uniform scheme-theoretic \(A_1\) local model along its rank-two stratum, and the deduction of *normality of this component*, as distinct from normality of the entire reducible jet scheme. These conclusions are derived using an explicit rank-two pivot calculation; no inspected source was found to state them. An inaccessible Smith--Weyman preprint on resolutions of tangent schemes remains a literature-overlap risk.

## Limitations
The singular locus is identified with its **reduced** scheme structure; no claim is made about the globally defined Jacobian singular subscheme or about local analytic types at \(\operatorname{rank}(Y)\le1\). The ordinary-double-point local model holds precisely over the rank-two stratum. The theorem is formulated in characteristic zero; characteristic-two behavior and other determinantal ranks or higher jet orders are not claimed. The theorem is mathematically reviewed but has not undergone independent external audit. The older Smith--Weyman preprint could not be inspected in full.

## References
[1] T. Košir and B. A. Sethuraman, *Determinantal varieties over truncated polynomial rings*, arXiv:math/0212051v1 (public 3 December 2002), https://arxiv.org/abs/math/0212051.

[2] T. Košir and B. A. Sethuraman, *A Gröbner basis for the 2 × 2 determinantal ideal mod t²*, Journal of Algebra 292 (2005), Theorem 2.4 and Proposition 3.3, DOI:10.1016/j.jalgebra.2004.12.005. Lawful author preprint: https://www.csun.edu/~asethura/papers/Groebner2x2modt2.pdf.

[3] B. Jonov, *Initial complex associated to a jet scheme of a determinantal variety*, arXiv:1006.3883v1, Theorem 1.2, https://arxiv.org/abs/1006.3883.

[4] S. Ghorpade, B. Jonov and B. A. Sethuraman, *Hilbert series of certain jet schemes of determinantal varieties*, arXiv:1210.3841v1, https://arxiv.org/abs/1210.3841.

[5] C. Yuen, *Jet schemes of determinantal varieties*, arXiv:math/0608632, https://arxiv.org/abs/math/0608632.

[6] R. Docampo, *Arcs on determinantal varieties*, arXiv:1011.1930, https://arxiv.org/abs/1011.1930.
