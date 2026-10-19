# Binary quadratic level sets give fully injective real Gabor tomography, with a unique projective-design resonance

## Finding

Let \(m\ge1\), \(V=\mathbb F_2^{2m}\), \(N=|V|=2^{2m}\), and let \(Q:V\to\mathbb F_2\) be a quadratic form with \(Q(0)=0\) and **nondegenerate polar form** \(B(x,y)=Q(x+y)+Q(x)+Q(y)\). Fix \(\varepsilon\in\mathbb F_2\). The quadratic Gauss sign and the level-set parameters are
\[
\sigma=2^{-m}\sum_{x\in V}(-1)^{Q(x)}\in\{-1,1\},\qquad
\rho=(-1)^\varepsilon\sigma,\qquad
K=2^{2m-1}+\rho2^{m-1},\quad L=2^{2m-2}+\rho2^{m-1},\quad h=2^{m-1}.
\]
Let \(g=\mathbf1_{\{Q=\varepsilon\}}/\sqrt K\in\mathbb R^V\). For \(a\in V\) and \(b\in V^*\), put \((T_af)(x)=f(x+a)\), \((M_bf)(x)=(-1)^{b(x)}f(x)\), and \(g_{a,b}=M_bT_ag\). Define the **real symmetric intensity-lifting map**
\[
\mathcal A:\operatorname{Sym}_N(\mathbb R)\longrightarrow\mathbb R^{N^2},\qquad
\bigl(\mathcal A(X)\bigr)_{a,b}=\operatorname{tr}(Xg_{a,b}g_{a,b}^{\mathsf T}).
\]
Its exact normal-operator spectrum, including multiplicities and any coincident values, is
\[
\operatorname{spec}(\mathcal A^*\mathcal A)=
\left\{\begin{array}{ll}
N & \text{multiplicity }1,\\
N(L/K)^2 & \text{multiplicity }2(N-1),\\
N(h/K)^2 & \text{multiplicity }(N-1)(N/2-1)
\end{array}\right\}.
\]
For **every \(m\ge2\)**, \(L>0\): the map is injective on all real symmetric matrices, has rank \(N(N+1)/2\), and reconstructs every real signal from these \(N^2\) phaseless Gabor samples uniquely up to its global sign. Its sharp singular-value condition number is
\[
\kappa(\mathcal A)=\frac Kh=2^m+\rho.
\]
For \(m=1\) the same spectrum holds; when \(\rho=1\) the map is injective with condition number \(3\), whereas when \(\rho=-1\) its rank is \(N=4\) and its nullity in the symmetric domain is \(6\).

The uniform \(N^2\)-element orbit \(\{g_{a,b}\}\), with multiplicities retained, is a **real projective \(2\)-design if and only if** \(m=2\) and \(\rho=-1\). Thus the unique design case within this entire quadratic-level family has \(N=16\), \(K=6\), and provides \(256\) explicit signed-translation/modulation vectors with the exact second-moment identity
\[
\frac1{256}\sum_{a,b}|\langle u,g_{a,b}\rangle|^4
=\frac{3\|u\|^4}{16\cdot18}\qquad(u\in\mathbb R^{16}).
\]
Equivalently, the frame operator of the lifted measurements has eigenvalues \(16\) once and \(16/9\) with multiplicity \(135\). One model is \(Q(x,y)=x\cdot y\) on \(\mathbb F_2^2\oplus\mathbb F_2^2\), taking the level \(\varepsilon=1\).

## Assumptions and scope

All characters are real Walsh characters. The group \(V\) is elementary abelian of even binary dimension, and its quadratic polar form is nonsingular. The inner product on \(\mathbb R^V\) is the unweighted counting inner product. The parameter \(\rho\) captures both quadratic Arf/Gauss types and either level of \(Q\). Every window has unit \(\ell^2\)-norm. The operator \(\mathcal A^*\) is the transpose with respect to Euclidean measurement coordinates and the Frobenius inner product on \(\operatorname{Sym}_N(\mathbb R)\); it is **not** an operator on all complex matrices. In particular, phase recovery here means recovery of **real** signals up to sign, not arbitrary complex signals up to complex phase. Repeated orbit vectors, if any, are counted with their indexing multiplicities in the design definition.

For later use, the real Weyl matrix is \(W_{a,b}=M_bT_a\). It satisfies \(W_{a,b}^{\mathsf T}=(-1)^{b(a)}W_{a,b}\). In particular, exactly the matrices with \(b(a)=0\) are symmetric, and these form an orthogonal basis of \(\operatorname{Sym}_N(\mathbb R)\) under the Frobenius inner product.

## Proof

**1. Quadratic Walsh transform and level sizes.** The polarization identity gives
\[
G^2=\sum_{x,a\in V}(-1)^{Q(x)+Q(x+a)}
=\sum_{a\in V}(-1)^{Q(a)}\sum_{x\in V}(-1)^{B(x,a)}=N,
\]
since nondegeneracy makes the inner sum vanish for \(a\ne0\). Thus \(G=\sigma2^m\) for a sign \(\sigma\). For each linear functional \(b\in V^*\) there is a unique \(h_b\in V\) such that \(b(x)=B(x,h_b)\). Translation by \(h_b\) proves the exact Walsh transform
\[
\sum_{x\in V}(-1)^{Q(x)+b(x)}=\sigma2^m(-1)^{Q(h_b)}.
\]
Expanding the indicator \(\mathbf1_{\{Q=\varepsilon\}}=(1+(-1)^\varepsilon(-1)^Q)/2\) now gives its size \(K\) as stated. In particular \(K>0\).

**2. Complete ambiguity amplitudes.** Work first with the unnormalized indicator and define
\[
A(a,b)=\sum_{x\in V}\mathbf1_{\{Q(x)=\varepsilon\}}\mathbf1_{\{Q(x+a)=\varepsilon\}}(-1)^{b(x)}.
\]
Write \(j_a\in V^*\) for \(j_a(x)=B(x,a)\). Expanding both indicators, using \(Q(x+a)=Q(x)+Q(a)+j_a(x)\), and applying the preceding Walsh formula yields the *exact* identity
\[
4A(a,b)=N\bigl(\mathbf1_{b=0}+(-1)^{Q(a)}\mathbf1_{b=j_a}\bigr)
+\rho2^m(-1)^{Q(h_b)}\bigl(1+(-1)^{b(a)}\bigr).
\]
For the second term, use \(h_{b+j_a}=h_b+a\) and \(Q(h_b+a)=Q(h_b)+Q(a)+b(a)\). Evaluating the identity gives the entire disjoint case division:
\[
\begin{array}{c|c}
\text{index}&A(a,b)\\\hline
 a=0,\ b=0&K\\
 a=0,\ b\ne0&\rho h(-1)^{Q(h_b)}\\
 a\ne0,\ b=0&L\\
 a\ne0,\ b=j_a&(-1)^{Q(a)}L\\
 a\ne0,\ b\notin\{0,j_a\},\ b(a)=0&\rho h(-1)^{Q(h_b)}\\
 a\ne0,\ b(a)=1&0.
\end{array}
\]
The two special functionals are distinct when \(a\ne0\), because \(B\) is nondegenerate. They obey \(b(a)=0\) since \(B\) is alternating. The normalized window has Weyl coefficient \(A(a,b)/K\). This evaluation is a finite algebraic identity, not a numerical character-sum estimate.

**3. Operator diagonalization.** The matrices \(\{W_{a,b}\}\) are an orthogonal real basis of all \(N\times N\) matrices with \(\operatorname{tr}(W_{a,b}^{\mathsf T}W_{c,d})=N\mathbf1_{(a,b)=(c,d)}\). Their transpose parity is \((-1)^{b(a)}\); hence \(\{W_{a,b}:b(a)=0\}\) is an orthogonal basis of the *symmetric* subspace. Conjugation by the Weyl orbit multiplies each \(W_{a,b}\) by a character of the index group \(V\times V^*\), and these characters are mutually orthogonal. Expanding the rank-one seed \(gg^{\mathsf T}\) into this symmetric Weyl basis and summing the conjugated projectors therefore shows
\[
\mathcal A^*\mathcal A(W_{a,b})=N\left|\frac{A(a,b)}K\right|^2W_{a,b}
\qquad\text{when }b(a)=0.
\]
The multiplier formula can also be checked directly by the Frobenius pairing: \(\operatorname{tr}(W_{a,b}g_{c,d}g_{c,d}^{\mathsf T})\) is the signed phase-space character at \((c,d)\) times \(A(a,b)/K\). Fourier orthogonality gives its stated square. The \(b(a)=1\) matrices are skew and therefore **do not belong to the domain**; their zero ambiguity does not imply any loss of injectivity on symmetric matrices.

The identity matrix \(W_{0,0}\) contributes eigenvalue \(N\) once. For each of the \(N-1\) nonzero shifts there are exactly two special symmetric frequencies \(0,j_a\), giving \(2(N-1)\) eigenvalues \(N(L/K)^2\). The remaining symmetric basis elements number \((N-1)(N/2-1)\): they come from \(N-1\) nonzero frequencies at zero shift plus \((N-1)(N/2-2)\) nonspecial frequencies at nonzero shifts. They have ambiguity modulus \(h\). These multiplicities sum to \(N(N+1)/2\), proving the entire spectrum, including the cases where \(L=0\) or \(L=h\). For \(m\ge2\), \(L\ge h>0\) and \(K>L\), so the map is injective, the largest singular value is \(\sqrt N\), and the smallest is \(\sqrt N\,h/K\). This proves the sharp condition number. At \(m=1\), \(L\) is \(2\) or \(0\); the announced endpoint ranks and condition number follow directly.

If \(u,v\in\mathbb R^V\) have identical intensity vectors, then \(uu^{\mathsf T}-vv^{\mathsf T}\) belongs to \(\ker\mathcal A\). In the injective cases \(uu^{\mathsf T}=vv^{\mathsf T}\), which forces \(v=u\) or \(v=-u\) (also including the zero vector). Hence injective real phase retrieval follows without invoking a converse for noninjective cases.

**4. Projective \(2\)-design criterion and its unique occurrence.** Tightness of the entire Gabor orbit gives \(\sum_{a,b}g_{a,b}g_{a,b}^{\mathsf T}=NI\). A uniform family of unit vectors in \(\mathbb R^N\) is a real projective \(2\)-design if and only if its projector-lifting operator agrees with the orthogonally invariant second-moment operator; with \(N^2\) vectors this operator is
\[
\mathcal S(X)=\frac{N}{N+2}\bigl(2X+\operatorname{tr}(X)I\bigr).
\]
Indeed, the right side acts by \(N\) on scalars and by \(2N/(N+2)\) on traceless symmetric matrices. Both nontrivial Weyl sectors exist for all \(m\ge1\); hence the computed spectrum can be scalar on the traceless subspace only if \(L^2=h^2\). Since \(L\ge0\), this is \(L=h\), equivalently \(2^{m-1}+\rho=1\). For \(m\ge1\), \(\rho\in\{-1,1\}\), the unique solution is \(m=2,\rho=-1\). Here \(N=16,K=6,L=h=2\), so both traceless eigenvalues equal \(16/9=2N/(N+2)\), proving the exact design identity and the stated fourth moment. This equivalence is at the level of all symmetric tensors, not merely an observed equality of a few sampled fourth moments.

## Verification

The self-contained standard-library Python checker `checks/verify.py` evaluates the actual integer ambiguity coefficient \(A(a,b)\), for every \((a,b)\), for all \(m\in\{1,2,3\}\), both quadratic Gauss signs, and both level values. It checks every coefficient against the predicted absolute-value class and all symmetry/rank counts: in dimensions \(N=4,16,64\), respectively, there are \(N^2=16,256,4096\) coefficients per case, for a total of \(2(16+256+4096)\times2=17{,}472\) exact coefficient tests. In each \(16\)-dimensional design case, it *independently forms the actual orbit vectors* and checks on every basis element of the \(136\)-dimensional symmetric matrix space the exact integer identity
\[
36\sum_{a,b}\operatorname{tr}(X g_{a,b}g_{a,b}^{\mathsf T})\,g_{a,b}g_{a,b}^{\mathsf T}
=64X+32\operatorname{tr}(X)I.
\]
Run from the package root: `python3 checks/verify.py`; expected final output: `VERIFY_OK`. This finite verification checks the published formulas at these dimensions without floating-point tolerances. It is **not** an exhaustive proof over all \(m\) or all quadratic forms; Steps 1–4 provide the arbitrary-dimensional proof.

## Relationship to prior work

Bhattacharya and Smith [1] describe the classic Hadamard difference-set parameters, including \((16,6,2)\), and their combinatorial factorizations; this supplies the natural small-dimensional antecedent but does not calculate time-frequency intensity-lifting spectra or real projective moments. Bojarovska and Flinth [2, Section 2] establish a Weyl-diagonalization approach to finite Gabor phase retrieval over **cyclic groups**, and [2, Proposition 2.2] treats difference-set indicators under a small-intersection hypothesis. That particular hypothesis fails for binary groups of order at least four, and their full **complex** ambiguity-nonvanishing condition cannot hold for real characteristic-two windows: the antisymmetric Weyl coefficients always vanish. Their work does not imply the present **real symmetric** injectivity, exact two-sector conditioning, or projective-design criterion. Leopardi [3] proves structural results for quadratic bent functions, Hadamard difference sets, and real Clifford monomial bases; those facts motivate the construction but do not analyze the full conjugation orbit of level-set *projectors*.

For closer contemporary comparisons, the published result *Exact Gabor tomography rank for hyperbolic quadratic shells over odd finite fields* [4] explicitly assumes odd characteristic and counts complex operator directions, while *Dual symplectic graphs govern first-Walsh-band sampling on binary quadrics* [5] treats **linear restriction to a fixed first-Walsh band**, not real phaseless Gabor measurements of the entire signal space. Neither result implies the formula for the full symmetric lifting operator, its sharp condition number, or the unique \(16\)-dimensional design resonance. These are implication and domain comparisons, not novelty assertions based only on title wording.

## Limitations

The theorem covers nondegenerate binary quadratic level sets and **real** signal recovery only. It makes no claim that this real orbit recovers arbitrary complex signals; its complex-linear operator span is generally deficient. Nor does it classify degeneracies of an arbitrary Boolean level set, phase retrieval using fewer than \(N^2\) measurements, or robustness beyond the exact linear-lifting condition number. Although the spectrum is analytically proved, the checker exhausts only the stated finite examples. Literature searches and primary-text comparisons cannot certify absolute priority; an equivalently formulated stronger historical general theorem remains a residual risk. Independent mathematical audit has not been performed.

## References

1. C. Bhattacharya and K. W. Smith, *Factoring (16,6,2) Hadamard Difference Sets*, Electronic Journal of Combinatorics 15 (2008), R112, publicly published August 31, 2008, https://doi.org/10.37236/836.
2. I. Bojarovska and A. Flinth, *Phase Retrieval from Gabor Measurements*, arXiv:1503.05800v1, first public posting March 19, 2015; Section 2, https://arxiv.org/abs/1503.05800.
3. P. Leopardi, *Twin bent functions, strongly regular Cayley graphs, and Hurwitz–Radon theory*, arXiv:1504.02827v1, first posted April 11, 2015, https://arxiv.org/abs/1504.02827.
4. *Exact Gabor tomography rank for hyperbolic quadratic shells over odd finite fields*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-exact-gabor-tomography-rank-for-hyperbolic-quadratic-shells-over--b9e240edb677.
5. *Dual symplectic graphs govern first-Walsh-band sampling on binary quadrics*, published research record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-dual-symplectic-graphs-govern-first-walsh-band-sampling-on-binar--f73b283fd6aa.
