# Normal forms and sharp separation rank of resonant Fock Berezin fixed points

## Finding
Fix complex \(a,b\) with \(\kappa=\overline a b\in2\pi i\mathbb Z\setminus\{0\}\). Every Gaussian Berezin-fixed mixed exponential polynomial
\[F_R(z)=R(z,\overline z)e^{\overline a z+b\overline z}\]
has the explicit polynomial normal form below. The space with \(\deg R\le m\) has dimension \(m+1\), and every nonzero member of degree \(d\) has minimal analytic–antianalytic product length exactly \(d+1\). In particular, the fixed polynomials of separation rank at most \(r\) constitute a vector space of dimension exactly \(r\), rather than merely admitting an upper bound on degree.

## Assumptions and scope
Use the Gaussian Fock normalization \(d\mu(t)=\pi^{-1}e^{-|t|^2}dA(t)\), and the Gaussian Berezin transform \(\mathcal B F(z)=\int_{\mathbb C}F(z+t)d\mu(t)\), defined for the polynomial–exponential symbols considered. Regard \(z\) and \(w\) as independent complex variables in the polynomial \(R(z,w)\); only after the algebraic computation set \(w=\overline z\). Let \(\mathcal P_m\) be all complex polynomials in \(z,w\) of total degree at most \(m\). For a nonzero such symbol, *separation rank* is the least integer \(r\) for which it is a sum of \(r\) products \(f_j(z)\overline{g_j(z)}\) with entire \(f_j,g_j\) (equivalently, the least separable rank of the entire two-variable extension). All assertions refer to one nonzero *mixed* frequency \((\overline a,b)\), with \(\overline a b\) a nonzero integral multiple of \(2\pi i\).

Define new independent polynomial coordinates and a locally nilpotent differential operator by
\[u=\overline a z-bw,\qquad v=z/b,\qquad Q=\kappa(1-\partial_u)^{-1}\partial_u^2=\kappa\sum_{j\ge0}\partial_u^{j+2}.\]
Every displayed differential series acts as a finite sum on each polynomial. **Complete normal form:**
\[\mathcal B F_R=F_R\quad\Longleftrightarrow\quad R(z,w)=\left(e^{vQ}h\right)(u)\quad\text{for one and only one }h\in\mathbb C[u].\]

## Proof
**Berezin equation.** The Gaussian integral applied to each monomial times the exponential gives, as in Qin–Liu–Huang, Equation (3.9),
\[\mathcal B F_R(z)=e^\kappa e^{\overline a z+b\overline z}\left(e^D R\right)(z,\overline z),\qquad D=\partial_z\partial_w+b\partial_z+\overline a\partial_w.\]
Here \(D\) strictly lowers total polynomial degree. At resonance \(e^\kappa=1\), local nilpotence implies \(e^D R=R\) if and only if \(DR=0\): indeed \(e^D-I=D\sum_{j\ge0}D^j/(j+1)!\), and the sum is a polynomial in \(D\) with constant coefficient one, hence invertible on each \(\mathcal P_m\). Independence of the two variables on the totally real diagonal justifies passing from \(w=\overline z\) to the polynomial identity.

**Normal form and dimension.** Since \(b\ne0\), the coordinate transformation is invertible. Direct differentiation gives
\[D=(1-\partial_u)\partial_v-\kappa\partial_u^2.\]
The inverse \((1-\partial_u)^{-1}\) exists on polynomials because \(\partial_u\) is locally nilpotent. Consequently \(DR=0\) is equivalent to the polynomial evolution equation \(\partial_vR=QR\). All its polynomial solutions are uniquely \(R=e^{vQ}h(u)\), where \(h(u)=R(u,0)\). Since \(Q\) lowers polynomial degree by at least two, \(e^{vQ}h\) is a finite polynomial and has the same total degree as nonzero \(h\). Therefore \(h\mapsto R\) is a degree-preserving linear isomorphism between \(\mathbb C[u]_{\le m}\) and \(\ker D\cap\mathcal P_m\), establishing dimension \(m+1\). A canonical basis consists of the images of \(1,u,\ldots,u^m\).

**Sharp separation rank.** Let \(\deg R=d\), and let \(c\ne0\) be the leading coefficient of \(h\). The leading homogeneous part of \(R\) equals \(c(\overline a z-bw)^d\), because every term with a positive power of \(vQ\) has lower total degree. Write \(R=\sum_{j,k=0}^d r_{jk}z^jw^k\), and let \(M=(r_{jk})_{0\le j,k\le d}\). Since \(r_{jk}=0\) for \(j+k>d\), reversing the columns makes \(M\) triangular. Its diagonal entries become \(r_{j,d-j}=c\binom dj\overline a^{\,j}(-b)^{d-j}\), all nonzero. Thus \(\operatorname{rank}M=d+1\). The monomial row expansion represents \(R\) as a sum of at most \(d+1\) separable polynomial terms. Conversely any representation as \(r\) products of entire functions, after removing the everywhere-nonzero exponential factor, gives an entire separable expansion of \(R\). Taking Taylor coefficients of orders \(0,\ldots,d\) in both variables expresses \(M\) as the sum of \(r\) outer products, whence \(r\ge\operatorname{rank}M=d+1\). This proves the exact rank, including the case \(d=0\).

**Rank filtration.** Because separation rank equals one plus degree, the rank-at-most-\(r\) fixed symbols coincide exactly with the degree-at-most-\(r-1\) fixed subspace, whose dimension is \(r\). For a concrete nontrivial example choose \(\overline a=1\), \(b=2\pi i\), \(\kappa=2\pi i\). Taking \(h(u)=u^2\) gives \(R(z,w)=(z-2\pi i w)^2+2z\). It is fixed and requires exactly three separable terms.

## Verification
All decisive assertions are proved for every finite polynomial degree. In particular, \((1-\partial_u)^{-1}\) and \(e^{vQ}\) are not infinite-convergence assumptions: their action terminates on every polynomial. The coefficient matrix determinant equals \((\overline a b)^{d(d+1)/2}c^{d+1}\prod_{j=0}^d\binom dj\) (up to the harmless convention for row/column ordering), which is nonzero. Reproduce finite symbolic checks with `python check.py`; the checker verifies the differential equation and this determinant for the canonical solutions of degrees zero through eight. The finite checks do not replace the all-degree proof.

## Relationship to prior work
Qin, Liu, and Huang, arXiv:2610.22136v1, provide the exponential-polynomial Berezin formula and correct a two-product commuting Toeplitz characterization. Their proof uses an anti-diagonal coefficient-rank argument to force degree at most one for a difference of **two** product terms. The present result classifies *every* polynomial fixed point at a resonant mixed frequency by an explicit one-variable differential normal form and determines the **exact minimum product count at every degree**. The older work of Bauer, Choe, and Koo gives a general characterization of Gaussian Berezin fixed points via Laplacian eigenfunctions; that qualitative framework is not claimed as new here.

## Limitations
The theorem is one-variable, one-frequency, polynomial-exponential, and requires a nonzero resonance \(\overline a b\in2\pi i\mathbb Z\). It does not classify cancellations among several distinct frequencies or bounded Toeplitz operators, nor does it claim results about nonpolynomial fixed points. The 2015 full text could not be inspected in this examination; its broader description creates residual historical-priority uncertainty. The proof and symbol-space rank assertion have not undergone independent review.

## References
Qin, J., Liu, Y., and Huang, S., *Commuting Toeplitz operators with harmonic symbols on the Fock space*, arXiv:2610.22136v1 (first posted 15 October 2026), Section 3, Proposition 3.1 and Equation (3.9). https://arxiv.org/html/2610.22136v1

Bauer, W., Choe, B. R., and Koo, H., *Commuting Toeplitz operators with pluriharmonic symbols on the Fock space*, Journal of Functional Analysis 268 (2015), 3017–3060, DOI 10.1016/j.jfa.2015.03.003. Full text not inspected here.
