# Exact angular-resonance threshold for balanced concentric phase-retrieval grids

## Finding

For each integer \(d\ge1\), two regular \(2d\)-gons on concentric circles form a universally injective intensity-sampling set for all complex polynomials of degree at most \(d\) **exactly** when their radii differ and their relative angular displacement avoids a discrete resonance. This gives a complete geometric classification, not just a sufficient construction.

Precisely, fix \(r_1,r_2>0\), \(\phi_1,\phi_2\in\mathbb R\), and put
\[
\Omega=\bigcup_{j=1}^{2}\big\{r_j\exp\big(i(\phi_j+\pi k/d)\big):k=0,\ldots,2d-1\big\}.
\]
For every pair of polynomials \(p,q\in\mathbb C[z]\) of degree at most \(d\), the implication
\[
\bigl(|p(\zeta)|=|q(\zeta)|\text{ for all }\zeta\in\Omega\bigr)
\quad\Longrightarrow\quad q=\lambda p\text{ for some }|\lambda|=1
\]
holds **if and only if**
\[
\boxed{r_1\ne r_2\quad\text{and}\quad\sin\bigl(d(\phi_2-\phi_1)\bigr)\ne0.}
\]
Under these conditions the \(4d\) sample points are all distinct. The criterion includes polynomials of degree strictly smaller than \(d\), coefficients that vanish, and the zero polynomial.

## Assumptions and scope

Samples are noiseless pointwise magnitudes in the entire complex plane; the radii are strictly positive and known. No zero-free assumption, real-coefficient restriction, genericity assumption on the unknown polynomial, or condition on roots is imposed. Angles are considered modulo \(2\pi\). All polynomial degrees \(d\ge1\) are covered. No assertion is made about quantitative conditioning, reconstruction error with noise, or global minimality of \(4d\) measurements among all possible configurations.

## Proof

**Step 1: the shared Nyquist coefficient.** Write
\(p(z)=\sum_{m=0}^{d}a_mz^m\). On the circle of radius \(r>0\), its squared modulus is a trigonometric polynomial of degree at most \(d\):
\[
|p(re^{it})|^2=\sum_{k=-d}^{d}b_{r,k}e^{ikt},\qquad
b_{r,k}=r^k\sum_{m=0}^{d-k}a_{m+k}\overline{a_m}r^{2m}\quad(0\le k\le d),
\]
with \(b_{r,-k}=\overline{b_{r,k}}\). In particular,
\[
b_{r,d}=r^d v,\qquad v=a_d\overline{a_0},
\]
and the same complex \(v\) occurs on **both** circles after dividing by the known power of the radius.

Define the \(2d\)-point discrete Fourier statistic
\[
T_j(k)=\frac1{2d}\sum_{\ell=0}^{2d-1}
 |p(r_je^{i(\phi_j+\pi\ell/d)})|^2e^{-i\pi k\ell/d}.
\]
For \(0\le k<d\), root-of-unity orthogonality yields
\[
T_j(k)=e^{ik\phi_j}b_{r_j,k}.
\]
The two top harmonics alias into a single real Nyquist statistic:
\[
T_j(d)=2r_j^d\operatorname{Re}\bigl(ve^{id\phi_j}\bigr).
\]
Thus each ring determines all intensity Fourier coefficients except the individual complex top coefficient, and its Nyquist observation gives one real linear equation for \(v\).

**Step 2: resolve the alias.** Setting \(v=u+iw\) and \(\alpha_j=d\phi_j\), the two observed real quantities \(T_j(d)/(2r_j^d)\) are
\[
\begin{pmatrix}\cos\alpha_1&-\sin\alpha_1\\
\cos\alpha_2&-\sin\alpha_2\end{pmatrix}
\begin{pmatrix}u\\w\end{pmatrix}.
\]
The determinant is \(-\sin(\alpha_2-\alpha_1)\). When it is nonzero, the two measurements determine \(v\) uniquely, and therefore determine all coefficients \(b_{r_j,k}\) for \(-d\le k\le d\), on both circles. Consequently, any two polynomials with equal sampled squared magnitudes have equal squared magnitudes **at every point on both full circles**.

**Step 3: two complete circles force phase uniqueness.** Let \(p,q\) be nonzero polynomials with equal moduli on the two circles. The quotient \(R=p/q\) is a rational function. Let \(R^\#(z)=\overline{R(\overline z)}\), also rational. On \(|z|=r\), the relation \(\overline z=r^2/z\) and \(|R(z)|=1\) give, by rational identity,
\[
R(z)R^\#(r^2/z)=1.
\]
Applying this to \(r_1\) and \(r_2\) and eliminating \(R\) yields
\[
R^\#(w)=R^\#(\eta w),\qquad \eta=r_2^2/r_1^2.
\]
If \(r_1\ne r_2\), then \(\eta>0\) and \(\eta\ne1\). A rational function invariant under this dilation is constant: expand its Laurent series about zero, and observe that each coefficient of degree \(k\ne0\) must vanish because \(\eta^k\ne1\). Thus \(R\) is constant. Its modulus is one at any sample where the nonzero polynomial does not vanish, so \(q=\lambda p\) with \(|\lambda|=1\). If either polynomial is identically zero, the other vanishes at all \(2d\) distinct points of one ring; since \(2d>d\), it is also zero.

**Step 4: both conditions are necessary.** If \(r_1=r_2=r\), choose any real \(t>0\) with \(t\ne r\). The polynomials
\[
p(z)=z-t,\qquad q(z)=(t/r)z-r
\]
have equal modulus on the **entire** circle \(|z|=r\) and are not unimodular scalar multiples. Hence no pair of polygonal samples on that single circle suffices.

If \(\sin(d(\phi_2-\phi_1))=0\), choose
\[
p(z)=1+i e^{-id\phi_1}z^d,\qquad q(z)=1-i e^{-id\phi_1}z^d.
\]
For every sampled argument, \(e^{id(t-\phi_1)}\in\{-1,1\}\); therefore \(|p|^2=|q|^2=1+r_j^{2d}\) at all samples, although the polynomials are not unimodular multiples. This holds regardless of whether the two positive radii are equal or distinct. The two explicit obstructions prove necessity and finish the theorem.

## Verification

The included standalone program `checker.py` uses only the Python standard library. Running `python3 checker.py` checks the finite Fourier identities, top-coefficient recovery, and both exact nonuniqueness constructions on random coefficients for degrees one through twelve. It uses deterministic randomness and numerical tolerances; it does **not** certify the quantified all-degree theorem. The proof above is algebraic and independent of those tests.

## Relationship to prior work

Bodmann and Hammen constructed universal \(4n-4\)-measurement phase retrieval using two *intersecting*, nonconcentric circles (with \(n=d+1\) coefficient dimensions). Pohl, Li, and Boche already proved universal polynomial retrieval at the same \(4d\) budget using two *concentric* circles with an **unbalanced** allocation of \(2d+1\) arbitrary points on one and \(2d-1\) on the other. Thus neither the measurement count nor the general two-circle uniqueness mechanism is claimed as new here. The present assertion instead completely classifies the **balanced, equally spaced** \(2d+2d\) design and proves its sharp angular resonance obstruction for every degree. The earlier degree-two balanced case is a special case and is not separately claimed.

Grohs, Liehr, and Rathmair study an infinite-dimensional Fock-space phase-retrieval problem involving perturbed Liouville sets, rather than this finite-degree, exact two-orbit Nyquist classification.

## Limitations

Only the stated balanced regular-polygon sampling family is classified; other point allocations, irregular angles, and noise-stability rates are not covered. An exact phase-retrieval criterion does not automatically give a uniformly conditioned inverse when the two radii nearly coincide or the sine factor is small. The cited literature establishes earlier related constructions and continuous-circle rigidity. The novelty assessment remains subject to specialist historical-priority checking, particularly obscure variants of two-circle finite interpolation.

## References

1. P. Grohs, L. Liehr, and M. Rathmair, *Phase retrieval in Fock space and perturbation of Liouville sets*, arXiv:2308.00385v1 (first public version August 1, 2023), https://arxiv.org/abs/2308.00385 .
2. V. Pohl, N. Li, and H. Boche, *Phase retrieval in spaces of analytic functions on the unit disk*, SampTA (2017), DOI:10.1109/SAMPTA.2017.8024411; complete author-uploaded text at https://www.researchgate.net/publication/319475708_Phase_retrieval_in_spaces_of_analytic_functions_on_the_unit_disk .
3. B. G. Bodmann and N. Hammen, *Stable phase retrieval with low-redundancy frames*, arXiv:1302.5487v1 (February 22, 2013), https://arxiv.org/abs/1302.5487 .
