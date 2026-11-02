# Decomposable associative Yang–Baxter tensors: square-zero rigidity and exact elementary-operator rank spectra

## Finding

Let \(k\) be any field, \(n\geq2\), and \(A=M_n(k)\). The (Aguiar-convention) associative Yang–Baxter equation (AYBE) on \(A\otimes_k A\) is
\[
r_{13}r_{12}-r_{12}r_{23}+r_{23}r_{13}=0.
\]
A nonzero tensor \(r\) is **decomposable** if \(r=U\otimes V\) with nonzero matrices \(U,V\). This is tensor rank one, **not** matrix rank one. The following classification is valid over every field, including characteristic two.

**Classification.** Such \(r\) solves AYBE if and only if there exist unique scalars \(\lambda,\mu\in k\), relative to its chosen nonzero factors, with
\[
 U^2=\lambda U,\qquad V^2=\mu V,\qquad VU=\lambda V+\mu U,\qquad \lambda\mu=0.
\tag{1}
\]
There are three disjoint types: (N) \(U^2=V^2=VU=0\); (L) \(r=E\otimes B\), where \(E^2=E\ne0\), \(B^2=0\ne B\), and \(BE=B\); and (R) \(r=B\otimes E\), where \(E^2=E\ne0\), \(B^2=0\ne B\), and \(EB=B\). In types L and R the idempotent representative in its factor line is unique. The zero tensor is the only additional decomposable-or-zero solution.

**Rigidity.** Every such nonzero tensor satisfies \(r^2=0\) in \(A\otimes A\). Its associated elementary linear map
\[
 \beta_r:A\longrightarrow A,\qquad \beta_r(X)=UXV
\]
is a nonzero weight-zero Rota–Baxter operator with \(\beta_r^2=0\), and \(\operatorname{rank}\beta_r=(\operatorname{rank}U)(\operatorname{rank}V)\le n\lfloor n/2\rfloor\). The bound is attained for every \(n\ge2\). Conversely, **every nonzero elementary multiplier** \(X\mapsto UXV\) satisfying the weight-zero Rota–Baxter identity comes from exactly one nonzero decomposable AYBE tensor, under the canonical isomorphism \(A\otimes A\cong\operatorname{End}_k(A)\).

**Full rank enumerator over finite fields.** Let \(k=\mathbb F_q\), for any prime power \(q\), let \({m\brack j}_q\) denote the Gaussian binomial coefficient (zero if \(j<0\) or \(j>m\)), and set
\[
 g_j(q)=|\operatorname{GL}_j(\mathbb F_q)|=\prod_{i=0}^{j-1}(q^j-q^i),\qquad
 Q_j(q)={n\brack j}_q{n-j\brack j}_q g_j(q),\qquad t=\lfloor n/2\rfloor.
\]
Here \(Q_j(q)\) counts the rank-\(j\) square-zero matrices in \(M_n(\mathbb F_q)\). The exact rank-generating polynomial of all elementary weight-zero Rota–Baxter maps, including zero, equivalently of all decomposable-or-zero AYBE tensors, is
\[
\boxed{\begin{aligned}
 H_{n,q}(z)={}&1+\sum_{a=1}^{t}\sum_{b=1}^{t}
 \frac{Q_a(q){n-a\brack b}_q{n-b\brack b}_q g_b(q)}{q-1}\,z^{ab}\\
 &+2\sum_{b=1}^{t}Q_b(q)\sum_{s=b}^{n}
 {n-b\brack n-s}_q q^{s(n-s)}z^{sb}.
\end{aligned}}
\tag{2}
\]
Precisely, the coefficient of \(z^j\) is the number of these linear operators of vector-space rank \(j\). The first double sum counts type N; the second sum counts types L and R. These are disjoint and exhaustive, with no overcount. In particular, for \(n=2\),
\[
 H_{2,q}(z)=1+(q^2-1)(2q+1)z+2(q^2-1)z^2.
\]
For \(n=3,q=2\), the polynomial is \(1+357z+504z^2+42z^3\). This determination holds for all characteristics and all matrix sizes.

## Assumptions and scope

The full matrix algebra is unital and associative, and tensor legs use the ordinary algebra multiplication. No skew-symmetry, nondegeneracy, or spectral parameter is assumed. All vector-space ranks of \(\beta_r\) are ranks on \(M_n(k)\), of dimension \(n^2\). A nonzero decomposable tensor is unique up to factor rescaling \((U,V)\mapsto(cU,c^{-1}V)\) with \(c\in k^\times\). The finite-field formula counts individual labeled tensors/operators, not similarity or projective classes. It does not count arbitrary nondecomposable tensors or arbitrary (non-elementary) Rota–Baxter maps.

## Proof

**1. Necessary and sufficient equations.** For \(r=U\otimes V\), direct multiplication in \(A^{\otimes3}\) turns AYBE exactly into
\[
 U^2\otimes V\otimes V-U\otimes VU\otimes V+U\otimes U\otimes V^2=0.\tag{3}
\]
Since \(U,V\ne0\), applying a functional on the first tensor factor that annihilates \(U\) shows \(U^2\in kU\); write \(U^2=\lambda U\). (If \(U^2\notin kU\), such a functional can take value one on \(U^2\), contradicting \(V\otimes V\ne0\).) Equation (3) now reads
\[
 U\otimes\big((\lambda V-VU)\otimes V+U\otimes V^2\big)=0.
\]
Project the third factor modulo \(kV\); this implies \(V^2\in kV\), say \(V^2=\mu V\). Equation (3) then gives \(VU=\lambda V+\mu U\). Compare \((VU)U\) with \(V(U^2)\) using associativity: their difference is \(\lambda\mu U\), hence \(\lambda\mu=0\). Conversely, the four relations in (1) directly annul (3).

If both scalars vanish, the pair is type N. If \(\lambda\ne0\), normalize \(E=\lambda^{-1}U\), \(B=\lambda V\) to obtain type L. If \(\mu\ne0\), normalize \(E=\mu^{-1}V\), \(B=\mu U\) to obtain type R. The three types cannot overlap because a nonzero square-zero matrix cannot be a nonzero scalar multiple of an idempotent.

**2. Operator interpretation and sharp rank bound.** The map \(\Theta:A\otimes A\to\operatorname{End}_k(A)\) sending \(U\otimes V\) to \(X\mapsto UXV\) is a vector-space isomorphism. For matrix units, \(\Theta(E_{ij}\otimes E_{k\ell})(X)=X_{jk}E_{i\ell}\), which gives every coordinate matrix unit on \(\operatorname{End}_k(A)\). Likewise, the map \(A^{\otimes3}\to\operatorname{Hom}_k(A\otimes A,A)\) sending \(U\otimes V\otimes W\) to \((X,Y)\mapsto UXVYW\) is an isomorphism, because \(E_{ij}XE_{k\ell}YE_{mp}=X_{jk}Y_{\ell m}E_{ip}\), a coordinate basis. The weight-zero Rota–Baxter defect of \(\Theta(r)\) is therefore exactly the image of (3) under this latter isomorphism. This proves the stated equivalence, not merely the forward implication.

From (1), \(r^2=U^2\otimes V^2=\lambda\mu r=0\), and \(\beta_r^2(X)=U^2XV^2=0\). Vectorization gives \(\operatorname{rank}\beta_r=\operatorname{rank}U\cdot\operatorname{rank}V\). In N both factor ranks are at most \(t\). In L or R the square-zero factor has rank at most \(t\), while the idempotent factor has rank at most \(n\). Thus the upper bound is \(nt\), attained by \(r=I_n\otimes B\) with \(B\) of square-zero rank \(t\).

**3. Count of rank-fixed square-zero matrices.** A rank-\(j\) square-zero matrix \(T\) has image \(W\), kernel \(K\) with \(W\subseteq K\), \(\dim W=j\), \(\dim K=n-j\), and is determined by an isomorphism \(k^n/K\to W\). Choose \(W\) in \({n\brack j}_q\) ways, \(K\) in \({n-j\brack j}_q\) ways, and the isomorphism in \(g_j(q)\) ways. This proves the formula for \(Q_j(q)\) and its characteristic-independent validity.

**4. Type N finite-field fibers.** Fix a square-zero \(U\) of rank \(a\), with image \(W\). For a rank-\(b\) square-zero \(V\), the condition \(VU=0\) means \(W\subseteq\ker V\). We can choose \(\ker V\) as a codimension-\(b\) subspace containing \(W\) in \({n-a\brack b}_q\) ways, choose \(\operatorname{im}V\) as a \(b\)-subspace of \(\ker V\) in \({n-b\brack b}_q\) ways, and then choose \(k^n/\ker V\to\operatorname{im}V\) as an isomorphism in \(g_b(q)\) ways. There are \(Q_a(q)\) possible \(U\)'s. Exactly \(q-1\) ordered pairs of nonzero factors represent any given decomposable tensor, so division by \(q-1\) yields the first coefficient sum in (2). Its operator rank is \(ab\).

**5. Types L and R finite-field fibers.** Fix a rank-\(b\) square-zero matrix \(B\); there are \(Q_b(q)\) choices. For a rank-\(s\) idempotent \(E\), \(BE=B\) is equivalent to \(\ker E\subseteq\ker B\): decompose \(k^n=\operatorname{im}E\oplus\ker E\). There are \({n-b\brack n-s}_q\) possible \((n-s)\)-dimensional kernels of \(E\) inside the \((n-b)\)-dimensional space \(\ker B\), and \(q^{s(n-s)}\) complementary image subspaces for each fixed kernel. Necessarily \(b\le s\le n\). Thus type L contributes \(Q_b(q){n-b\brack n-s}_q q^{s(n-s)}\) operators of rank \(sb\). Transposition and exchange of the two factors bijects L with R, yielding the factor two. There is no division by \(q-1\) here, since the unique nonzero idempotent representative normalizes the corresponding factor. Together with type N and the zero map, this proves (2).

## Verification

The standalone `verify.py` uses only the Python standard library. It reconstructs finite-field multiplication (prime fields and the genuine extension \(\mathbb F_4=\mathbb F_2[u]/(u^2+u+1)\)), original matrix multiplication and the **unreduced** three-tensor AYBE equations. For \((n,q)=(2,2),(2,3),(2,4)\), it checks the original equations on **every nonzero ordered factor pair**, independently comparing their truth values with (1), then checks exact rank distributions and the formula. For \((n,q)=(3,2)\), it exhausts the reduced classification equations and checks the full original AYBE equations for every admitted pair. It does not claim an exhaustive original-equation evaluation for all rejected pairs at \((3,2)\).

The exact totals of nonzero decomposable tensors are respectively \(21,72,165,903\). The corresponding nil–nil and mixed contributions are \((3,18),(8,64),(15,150),(189,714)\). The rank profiles are recorded in `checks.txt`. These finite experiments support, but do not replace, the arbitrary-field proof above. Reproduce by running `python3 verify.py`.

## Relationship to prior work

Aguiar (arXiv:math/0211074v1, 5 November 2002; in the full revised text, Section 2, equation (2.8), and Section 4, Proposition 4.3) supplies the AYBE convention, the infinitesimal-bialgebra interpretation and the implication to weight-zero Rota–Baxter operators. The current result does **not** claim those foundations or Aguiar's example \(I\otimes B\) with \(B^2=0\) as new; it provides the exhaustive decomposable classification and all-dimension finite-field rank counts.

Schedler (arXiv:math/0212258v1, 18 December 2002) classifies a **spectral-parameter trigonometric** family over complex matrix algebras, not the finite-field enumeration of constant decomposable solutions in arbitrary dimension. Bai–Guo–Ni (arXiv:0910.3261v1, 17 October 2009, Sections 1 and 3) develops extended \(\mathcal O\)-operator correspondences; that general equivalence does not supply the explicit Gaussian-binomial rank distribution. Sokolov (arXiv:1212.6421v1, 27 December 2012, Sections 1–3) and Zobnin (arXiv:1310.1193v1, 4 October 2013) treat **skew-symmetric** constant solutions, primarily over complex matrices, whereas the decomposable tensors counted here are not assumed skew and admit many idempotent-factor examples. The earlier all-size finite-field count of rank-one-as-a-linear-operator Rota–Baxter maps on full matrix algebras treats a different stratum: the present maps \(X\mapsto UXV\) may have any rank from one to \(n\lfloor n/2\rfloor\). The rank-one intersection is not claimed independently new.

## Limitations

Only decomposable-or-zero AYBE tensors and elementary two-sided multipliers are enumerated. No assertion is made about the full AYBE solution scheme, general sums of elementary operators, conjugacy orbits, or nonreduced scheme structures. Publication priority is provisional: an unlocated general theorem about elementary matrix Rota–Baxter operators or decomposable AYBE tensors might subsume the result. Finite-field checks are not proofs of the universal formula, and independent audit has not been performed.

## References

1. M. Aguiar, *Infinitesimal bialgebras, pre-Lie and dendriform algebras*, arXiv:math/0211074, first submitted 2002-11-05, https://arxiv.org/html/math/0211074v3.
2. T. Schedler, *Trigonometric solutions of the associative Yang-Baxter equation*, arXiv:math/0212258, first submitted 2002-12-18, https://arxiv.org/abs/math/0212258.
3. C. Bai, L. Guo, X. Ni, *O-operators on associative algebras and associative Yang-Baxter equations*, arXiv:0910.3261, first submitted 2009-10-17, https://arxiv.org/abs/0910.3261.
4. V. Sokolov, *Classification of constant solutions for associative Yang-Baxter equation on gl(3)*, arXiv:1212.6421, first submitted 2012-12-27, https://arxiv.org/html/1212.6421v1.
5. A. Zobnin, *Anti-Frobenius Algebras and Associative Yang-Baxter Equation*, arXiv:1310.1193, first submitted 2013-10-04, https://arxiv.org/abs/1310.1193.
