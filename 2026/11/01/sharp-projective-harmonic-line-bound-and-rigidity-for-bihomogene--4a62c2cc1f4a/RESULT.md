# Sharp projective harmonic-line bound and rigidity for bihomogeneous plurisubharmonic forms

## Finding
For each integer \(m\ge1\), a nonzero plurisubharmonic bihomogeneous form \(F\) of bidegree \((m,m)\) on \(\mathbb C^2\) is harmonic on at most \(m\) distinct complex lines through the origin. This is sharp. Equality holds precisely for
\[
F(z)=c\,|L_1(z)\cdots L_m(z)|^2,
\qquad c>0,
\]
where the \(L_j\) are pairwise nonproportional complex linear forms. Thus, within this class, restriction-harmonicity on \(m+1\) distinct origin lines forces \(F\equiv0\).

## Assumptions and scope
A real polynomial \(F:\mathbb C^2\to\mathbb R\) is bihomogeneous of bidegree \((m,m)\) if it is a sum of monomials involving exactly \(m\) holomorphic and exactly \(m\) antiholomorphic factors. Equivalently,
\[
F(\lambda z)=|\lambda|^{2m}F(z)
\quad (z\in\mathbb C^2,\ \lambda\in\mathbb C).
\]
Plurisubharmonicity means that the Hermitian Levi matrix \( (F_{z_j\bar z_k})_{j,k=1}^2\) is positive semidefinite everywhere. A complex origin line corresponds to a point of \(\mathbb{CP}^1\). “Harmonic on a line” means harmonicity for the entire one-variable restriction; for homogeneous forms, this is equivalent to vanishing on that line. The theorem applies to all such nonzero forms, without strict positivity, nondegeneracy, genericity, or coefficient sign hypotheses. The degree \(m\) is fixed but arbitrary.

## Proof
**1. Sign and exceptional directions.** For any nonzero vector \(v\), restrict to the line through \(v\):
\[
t\longmapsto F(tv)=|t|^{2m}F(v).
\]
For \(t\ne0\), its planar Laplacian is \(4m^2|t|^{2m-2}F(v)\). Subharmonicity of this restriction therefore forces \(F(v)\ge0\). The restriction is harmonic exactly when \(F(v)=0\). Thus the exceptional directions coincide with projective zeros of the nonnegative form \(F\).

**2. Logarithmic subharmonicity.** The crucial analytic fact is that \(\log F\), interpreted as \(-\infty\) on its zero set, is plurisubharmonic. For completeness, on the positivity set let \(H=(F_{z_j\bar z_k})\). Euler's bihomogeneity identities imply
\[
\sum_k\bar z_kF_{z_j\bar z_k}=mF_{z_j},\qquad
\sum_{j,k}z_j\bar z_kF_{z_j\bar z_k}=m^2F.
\]
Cauchy–Schwarz for the positive semidefinite Hermitian form \(H\) gives, for every \(\xi\in\mathbb C^2\),
\[
\left|\sum_j\xi_jF_{z_j}\right|^2
\le F\sum_{j,k}\xi_j\bar\xi_kF_{z_j\bar z_k}.
\]
This is exactly the Levi positivity of \(\log F\) where \(F>0\). The extension across zeros is supplied by the standard log-plurisubharmonicity theorem for nonnegative complex-homogeneous plurisubharmonic forms, as proved by D'Angelo [3, Theorem 1]; that theorem applies to zeros and does not require strict positivity. Consequently, for any affine projective chart, \(u(w)=\tfrac12\log F(1,w)\) is a subharmonic function on \(\mathbb C\), with value \(-\infty\) at zeros.

**3. At most \(m\) lines.** Choose any affine chart whose point at infinity is not a zero, which is possible because the nonzero polynomial \(F\) takes a positive value at some direction. Write \(f(w)=F(1,w)\). Polynomial growth gives
\[
u(w)=\tfrac12\log f(w)\le m\log^+|w|+O_F(1)
\quad (|w|\to\infty).
\]
Let \(\mu=(2\pi)^{-1}\Delta u\) be the positive Riesz measure. The circular-mean/Jensen formula, centered at any point where \(u\) is finite, gives \(\mu(\mathbb C)\le m\): indeed a mass exceeding \(m\) on one compact disk would force the circular means to grow faster than \(m\log R+O(1)\). At a zero \(w_0\) of \(f\), real smoothness and nonnegativity imply \(\nabla f(w_0)=0\) and \(0\le f(w)\le C|w-w_0|^2\) locally. Hence
\[
u(w)\le\log|w-w_0|+O(1).
\]
The local Jensen formula (or the subharmonic Lelong number characterization) therefore yields \(\mu(\{w_0\})\ge1\). Every projective zero is in the chosen affine chart, so there can be at most \(m\) distinct projective zeros.

**4. Rigidity at saturation.** Suppose there are exactly \(m\) zeros \(w_1,\ldots,w_m\). They consume at least \(m\) units of Riesz mass, and the total mass is at most \(m\). It follows that
\[
\mu=\sum_{j=1}^m\delta_{w_j}.
\]
Thus \(h(w):=u(w)-\sum_{j=1}^m\log|w-w_j|\) is distributionally harmonic, hence harmonic, on the whole plane. Since the point at infinity was chosen so that \(F(0,1)>0\), bihomogeneity yields
\[
f(w)=|w|^{2m}\big(F(0,1)+o(1)\big)
\quad(|w|\to\infty).
\]
Therefore \(h\) is bounded at infinity and is constant by the harmonic Liouville theorem. Exponentiating proves
\[
f(w)=c\prod_{j=1}^m|w-w_j|^2,\qquad c>0.
\]
Bihomogeneous homogenization gives \(F(z_1,z_2)=c\prod_{j=1}^m|z_2-w_jz_1|^2\). Reversing the projective coordinate change proves the asserted product of linear forms in any coordinates.

**5. Sharpness.** For any \(m\) distinct projective lines, choose linear equations \(L_j=0\) and set \(F=|L_1\cdots L_m|^2\). This is plurisubharmonic (as the squared modulus of a holomorphic polynomial), has bidegree \((m,m)\), and vanishes exactly on those \(m\) lines. The bound and the rigidity are sharp. \(\square\)

## Verification
The proof is fully analytic and uniform in the arbitrary positive integer \(m\); finite examples are not used to infer an infinite statement. Every invoked step has a direct test: Euler identities and the Levi Cauchy–Schwarz inequality on \(F>0\); D'Angelo's global log-plurisubharmonicity theorem at zeros; Jensen's circular means for the \(m\log|w|\) growth constraint; quadratic vanishing at a zero of a nonnegative smooth function; and harmonic Liouville rigidity at exact mass saturation. As simple boundary cases, \(F(z)=|z_1|^2\) has one exceptional line when \(m=1\), while \(F(z)=|z_1z_2|^2\) has two when \(m=2\).

## Relationship to prior work
Xu [1, Theorems 1.3 and 4.1–4.2] proves a Forelli-type rigidity statement using harmonicity on all, or almost all, complex lines under different regularity assumptions. The present finite-degree theorem instead gives an exact *finite number* of admissible harmonic lines and an equality classification for balanced homogeneous plurisubharmonic forms. Bharali and Stensønes [2, Proposition 2.2] and Simon [4, Proposition 2.1] prove that homogeneous non-pluriharmonic polynomials have only finitely many exceptional harmonic lines or hyperplanes; their cited results do not state this sharp degree-dependent upper bound or the maximal-case modulus-square factorization. D'Angelo [3, Theorem 1] is the essential pre-existing logarithmic-plurisubharmonicity tool, not a novelty claim. The new step combines that tool with a projective Riesz-mass budget and treats the equality case.

## Limitations
The bound is asserted only for balanced bidegree \((m,m)\) forms on \(\mathbb C^2\), not for arbitrary real-homogeneous polynomials, general smooth functions, or higher complex dimensions. It does not improve Xu's weighted Bergman-kernel equality theorem and does not classify all exceptional higher-dimensional hyperplanes. The claim is a mathematical deduction from classical logarithmic-plurisubharmonicity plus a new sharp Jensen saturation argument; a historical implicit occurrence of this specific deduction remains a priority risk. No independent audit or external mathematical certification is claimed here.

## References
[1] W. Xu, *A Characterization of Pluriharmonic Functions via \(p\)-Bergman Kernels and A Forelli-type Result*, arXiv:2609.32402v1, first public September 26, 2026. https://arxiv.org/pdf/2609.32402

[2] G. Bharali and B. Stensønes, *Plurisubharmonic Polynomials and Bumping*, Mathematische Zeitschrift **261** (2009), 39–63, DOI: 10.1007/s00209-008-0312-y. Author-hosted full text: https://math.iisc.ac.in/~bharali/C3bump_submit.pdf

[3] J. P. D'Angelo, *Bordered Complex Hessians*, Erwin Schrödinger Institute Preprint ESI 970 (2000), Theorem 1. https://www.esi.ac.at/preprints/esi970.pdf

[4] L. Simon, *Homogeneous Plurisubharmonic Polynomials in Higher Dimensions*, Journal of Geometric Analysis **31** (2021), 11584–11602, DOI: 10.1007/s12220-021-00697-y. https://link.springer.com/article/10.1007/s12220-021-00697-y
