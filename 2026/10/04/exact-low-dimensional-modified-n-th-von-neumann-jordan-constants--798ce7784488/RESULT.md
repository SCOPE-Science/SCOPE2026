# Exact low-dimensional modified n-th von Neumann–Jordan constants for the square plane

## Finding
For every integer \\(n\\ge 2\\), let \\(\\overline C_{mNJ}^{(n)}(X)\\) denote the upper modified \\(n\\)-th von Neumann--Jordan constant, namely the supremum over \\(x_1,\\ldots,x_n\\in S_X\\) of
\\[
\\frac{1}{n2^{n-1}}\\sum_{\\theta_2,\\ldots,\\theta_n\\in\\{-1,1\\}}
\\left\\|x_1+\\sum_{j=2}^n\\theta_jx_j\\right\\|^2.
\\]
For the real square plane \\(X=\\ell_\\infty^2\\), define
\\[
a_0=0,\\qquad a_r=\\mathbb E\\left|\\sum_{j=1}^r\\varepsilon_j\\right|
=\\frac{r}{2^{r-1}}\\binom{r-1}{\\lfloor(r-1)/2\\rfloor}\\quad(r\\ge1),
\\]
where the \\(\\varepsilon_j\\) are independent signs. Then
\\[
\\overline C_{mNJ}^{(n)}(\\ell_\\infty^2)
=1+\\frac{2}{n}\\max_{0\\le k\\le n}a_ka_{n-k}.
\\]
Writing \\(n=2r+1\\) or \\(n=2r\\), this is
\\[
\\overline C_{mNJ}^{(2r+1)}(\\ell_\\infty^2)
=1+\\frac{2a_ra_{r+1}}{2r+1},
\\]
and
\\[
\\overline C_{mNJ}^{(2r)}(\\ell_\\infty^2)
=\\begin{cases}
1+\\dfrac{a_r^2}{r},&r\\text{ odd},\\\\
1+\\dfrac{a_ra_{r+1}}{r},&r\\text{ even}.
\\end{cases}
\\]
In particular,
\\[
\\lim_{n\\to\\infty}\\overline C_{mNJ}^{(n)}(\\ell_\\infty^2)=1+\\frac{2}{\\pi}.
\\]

## Assumptions and scope
The space is real and two-dimensional with norm \\(\\|(s,t)\\|_\\infty=\\max\\{|s|,|t|\\}\\). The integer \\(n\\) is arbitrary with \\(n\\ge2\\). The result concerns the modified upper constant, whose vectors are individually constrained to the unit sphere; no assertion is made here about the unmodified upper or either lower constant.

## Proof
For \\(x_1,\\ldots,x_n\\) in the closed unit ball, the displayed objective is a convex function of the product variable: every summand is the square of a norm composed with an affine map. A convex function on the product of the two-dimensional square balls has a maximizer at a product of extreme points. Since all extreme points \\((\\pm1,\\pm1)\\) lie on the sphere, the sphere supremum equals the maximum over those vertices.

Write a vertex as \\(x_j=(\\alpha_j,\\beta_j)\\) with \\(\\alpha_j,\\beta_j\\in\\{-1,1\\}\\), and set \\(\\sigma_j=\\alpha_j\\beta_j\\). Introducing an additional independent sign for the first vector does not change the average, because the squared norm is invariant under a simultaneous sign reversal. After absorbing \\(\\alpha_j\\) into independent Rademacher signs \\(R_j\\), the objective becomes
\\[
\\frac1n\\mathbb E\\max\\left\\{\\left(\\sum_{j=1}^nR_j\\right)^2,
\\left(\\sum_{j=1}^n\\sigma_jR_j\\right)^2\\right\\}.
\\]
If exactly \\(k\\) of the \\(\\sigma_j\\) equal \\(1\\), put \\(A\\) equal to the sum of the corresponding \\(R_j\\)'s and \\(B\\) equal to the sum of the other \\(R_j\\)'s. Then the two coordinates are \\(A+B\\) and \\(A-B\\), and
\\[
\\max\\{(A+B)^2,(A-B)^2\\}=A^2+B^2+2|AB|.
\\]
Independence therefore gives
\\[
\\frac1n\\mathbb E\\max\\{(A+B)^2,(A-B)^2\\}
=1+\\frac2n a_ka_{n-k}.
\\]
This proves the max formula.

The random-walk absolute moments satisfy \\(a_{2q-1}=a_{2q}=:c_q\\) and
\\[
\\frac{c_{q+1}}{c_q}=\\frac{2q+1}{2q},
\\]
so \\((c_q)\\) is strictly increasing and log-concave. Balancing the two \\(c\\)-indices therefore maximizes the product. For odd \\(n=2r+1\\) this yields \\(a_ra_{r+1}\\). For even \\(n=2r\\), the odd choices of \\(k\\) dominate the even choices, and balancing yields \\(a_r^2\\) when \\(r\\) is odd and \\(a_ra_{r+1}\\) when \\(r\\) is even. This proves the piecewise formulas.

Finally, the central-binomial estimate from Stirling's formula gives \\(a_r\\sim\\sqrt{2r/\\pi}\\). Substitution in either parity formula gives the limit \\(1+2/\\pi\\).

## Verification
The proof is symbolic and covers every \\(n\\ge2\\). The bundled checker independently evaluates the closed form for \\(a_r\\), checks the parity formulas through \\(n=12\\), and exhaustively enumerates every sign pattern of square vertices through \\(n=8\\). It returns `VERIFY_OK`. These finite checks are regression tests, not the proof of the infinite statement.

## Relationship to prior work
Ciesielski and Płuciennik introduced the upper modified \\(n\\)-th von Neumann--Jordan constant in this form and obtained exact formulas for sequence spaces in several dimension regimes. Their high-exponent formula for \\(\\ell_m^p\\), extended in the proof to \\(2<p\\le\\infty\\), assumes \\(m\\ge2^{n-1}\\). At \\(p=\\infty\\) that regime gives the value \\(n\\), so it does not determine the fixed two-dimensional space \\(\\ell_\\infty^2\\) once \\(n\\ge3\\). The present result supplies the missing fixed-dimension endpoint profile and shows a qualitatively different bounded limit \\(1+2/\\pi\\).

## Limitations
No classification of all maximizing \\(n\\)-tuples is claimed; the proof determines the value and enough extremal sign patterns to attain it. The literature search found no equivalent low-dimensional formula, but an obscure or unindexed independent occurrence cannot be ruled out.

## References
1. M. Ciesielski and R. Płuciennik, "On some modifications of n-th von Neumann--Jordan constant for Banach spaces," arXiv:1811.01652, first public version 2018-11-05; Banach Journal of Mathematical Analysis 14 (2020), 650--673, doi:10.1007/s43037-019-00033-1.
