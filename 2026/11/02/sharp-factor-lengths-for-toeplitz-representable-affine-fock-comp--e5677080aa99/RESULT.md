# Sharp factor lengths for Toeplitz-representable affine Fock composition operators

## Finding

Let \(\mathcal F^2_\alpha\) be the one-variable Gaussian Fock space with any fixed \(\alpha>0\). Define \(\mathfrak G_\alpha\) to be the family of **composition operators** \(C_{\mu z+c}\) that each agree with a Toeplitz operator having one bounded measurable symbol on \(\mathcal F^2_\alpha\). A factorization of length \(n\) is a product of exactly \(n\) operators from \(\mathfrak G_\alpha\); factors are **not** allowed to be arbitrary Toeplitz operators.

For \(n\ge1\) and \(-\pi\le\theta\le\pi\), put
\[
 B_n(\theta)=\begin{cases}
 \cos^n(\theta/n),&|\theta|<n\pi/2,\\
 0,&|\theta|\ge n\pi/2.
 \end{cases}
\]
For every \(0<\rho<1\), every \(b\in\mathbb C\), and \(\lambda=\rho e^{i\theta}\), the following are equivalent:

* \(C_{\lambda z+b}\) is a product of exactly \(n\) members of \(\mathfrak G_\alpha\).
* Either \(b=0\) and \(\rho\le B_n(\theta)\), or \(b\ne0\) and \(\rho<B_n(\theta)\).

In the equality case \(\rho=B_n(\theta)>0\), every factorization has all slopes on the boundary of the closed disk \(\{\mu:|\mu-1/2|\le1/2\}\); in particular every intercept is zero. Up to the two conjugate choices of angle when \(\lvert\theta\rvert=\pi\), every factor slope equals \(e^{i\theta/n}\cos(\theta/n)\). Thus the boundary is rigid, not merely inaccessible to translated targets.

Consequently, defining
\[
 m(\rho,\theta)=\min\{n\ge1:\rho\le B_n(\theta)\},
\]
which is finite, the minimal number of factors is
\[
 \ell(C_{\lambda z+b})=\begin{cases}
 m(\rho,\theta),&b=0\text{ or }\rho<B_{m(\rho,\theta)}(\theta),\\
 m(\rho,\theta)+1,&b\ne0\text{ and }\rho=B_{m(\rho,\theta)}(\theta).
 \end{cases}
\]
For every fixed \(0<|\theta|\le\pi\), as \(\rho\uparrow1\), both the centered and translated lengths obey the sharp leading asymptotic
\[
 \ell(C_{\rho e^{i\theta}z+b})\sim\frac{\theta^2}{2(-\log\rho)}.
\]
The result is independent of the Gaussian scale \(\alpha\). No product of finitely many generators equals a nonzero rank-one constant-map composition operator \(C_b\), or a nonidentity unimodular rotation composition operator. The identity belongs to \(\mathfrak G_\alpha\).

For example, \(C_{(i/2)z}\) has length two, but \(C_{(i/2)z+b}\) has length three for every \(b\ne0\). Similarly, \(C_{-z/8}\) has length three and \(C_{-z/8+b}\) has length four for every nonzero \(b\).

## Assumptions and scope

The Hilbert space \(\mathcal F^2_\alpha\) consists of entire functions square-integrable against \((\alpha/\pi)e^{-\alpha|z|^2}\,dA(z)\). For an entire affine map \(\varphi(z)=\mu z+c\), the composition operator is \(C_\varphi f=f\circ\varphi\). A bounded-symbol Toeplitz operator is \(T_g=P_\alpha M_g\) with \(g\in L^\infty(\mathbb C)\). Equality of factors means equality as bounded operators on this space.

Corollary 3.1 of Lin--Lu--Zu (2026) gives the precise generator recognition theorem:
\[
 \mathfrak G_\alpha=\{C_{\mu z+c}:\mu\ne0,\ \Re\mu>|\mu|^2,\ c\in\mathbb C\}
 \ \cup\ \{C_{\mu z}:\mu\ne0,\ \Re\mu=|\mu|^2\}.
\]
This cited recognition theorem is **prior input**. The novel assertion assessed here is the exact product geometry, minimal factor length, equality rigidity, and boundary translation cost obtained from that class. The requirement that **each factor is itself a composition operator** is essential; arbitrary products of bounded-symbol Toeplitz operators are outside the claim.

## Proof

**1. Polar form of permitted slopes.** Completing the square in \(\Re\mu\ge|\mu|^2\) gives the disk of diameter \([0,1]\). Each allowed nonzero slope has the unique polar form \(\mu=r e^{it}\), with \(-\pi/2<t<\pi/2\) and \(0<r\le\cos t\). If \(r=\cos t\), the corresponding generator is permitted only with intercept zero; if \(r<\cos t\), every intercept is permitted. These facts are exactly the preceding generator recognition theorem.

**2. Necessary slope inequality.** Suppose a length-\(n\) product has target slope \(\lambda=\rho e^{i\theta}\). Let the factor slopes have phases \(t_1,\ldots,t_n\in(-\pi/2,\pi/2)\) and radii \(r_j\le\cos t_j\). Because affine composition multiplies slopes,
\[
 \rho=\prod_{j=1}^n r_j\le\prod_{j=1}^n\cos t_j
 \le\cos^n\left(\frac1n\sum_{j=1}^n t_j\right).
\]
The second inequality follows from strict concavity of \(\log\cos t\) on \((-\pi/2,\pi/2)\). The sum of the phases equals \(\theta+2\pi k\) for some integer \(k\). Since \(|\theta+2\pi k|\ge|\theta|\) and \(\cos\) decreases with absolute angle in this interval, the last expression is at most \(B_n(\theta)\). If \(|\theta|\ge n\pi/2\), such a phase sum is impossible; that is precisely the zero branch in the definition of \(B_n\).

**3. Necessity of a zero target intercept on the slope boundary.** If \(\rho=B_n(\theta)>0\), equality holds in every preceding inequality. Strict concavity forces all phases equal to a shortest-winding phase \(\pm|\theta|/n\); equality in the product-radius inequality forces \(r_j=\cos t_j\) for every \(j\). Each factor therefore lies on the boundary of the generator disk and has intercept zero by the cited recognition theorem. A composition of such maps fixes zero, so the target intercept is zero. For \(|\theta|<\pi\), the shortest winding is unique; for \(|\theta|=\pi\), the two opposite windings are possible. This establishes the stated rigidity.

**4. Sharp realizations.** When \(0<\rho<B_n(\theta)\), choose every factor slope to be
\[
 \mu=\rho^{1/n}e^{i\theta/n}.
\]
Then \(|\mu|<\cos(\theta/n)\), so \(\Re\mu>|\mu|^2\), and arbitrary intercepts are allowed. Choose \(n-1\) affine maps \(z\mapsto\mu z\) and one final outer affine map \(z\mapsto\mu z+b\). Their composite is \(z\mapsto\lambda z+b\). The corresponding composition operators appear in reverse order, which does not change the number of factors. At \(\rho=B_n(\theta)>0\) with \(b=0\), instead take every slope \(\mu=e^{i\theta/n}\cos(\theta/n)\) and every intercept zero. This gives the endpoint exactly and proves both equivalences.

**5. Minimal length and asymptotic cost.** For any fixed \(0<|\theta|\le\pi\), \(B_n(\theta)\) is strictly increasing in integer \(n\) once positive, and approaches one. Indeed, putting \(t=|\theta|/x\in(0,\pi/2)\), differentiation gives
\[
 \frac{d}{dx}\bigl[x\log\cos(|\theta|/x)\bigr]
 =\log\cos t+t\tan t>0,
\]
because the right-hand side is zero at \(t=0\) and its derivative is \(t\sec^2t>0\). For \(\theta=0\), \(B_n(0)=1\). Thus \(m(\rho,\theta)\) exists and, if its threshold is saturated, one more factor makes the inequality strict. This proves the length formula. Taylor expansion gives
\[
 -n\log\cos(\theta/n)=\frac{\theta^2}{2n}+O_\theta(n^{-3}).
\]
The threshold inequalities for \(m\) and \(m-1\) imply \(m\sim\theta^2/(2(-\log\rho))\) as \(\rho\uparrow1\), and adding at most one factor preserves this leading asymptotic.

**6. Excluded endpoint operators.** Every generator has a nonzero slope, hence so does every finite composition; the constant-map rank-one composition operator is never reached. All permitted slopes have modulus at most one, and modulus one occurs only at slope one with zero intercept. Therefore a product with unimodular slope is necessarily the identity. Finally, the affine maps defining bounded composition operators with \(|\lambda|>1\), or with \(|\lambda|=1\) and nonzero intercept, do not exist as bounded operators on this Fock space; they are not being classified.

## Verification

The analytical argument above is the proof. The standalone standard-library Python program `scripts/verify.py` performs deterministic checks of the sharp phase-radius inequality, strict threshold growth, explicit affine-product witnesses, boundary examples, and the asymptotic length scale. It executed successfully with **79,629 finite assertions**. Finite arithmetic and random sampling do not establish the universal theorem; in particular the rigid equality statement follows from strict concavity rather than computation.

## Relationship to prior work

Lin, Lu, and Zu (arXiv:2607.04102, Corollary 3.1) completely characterize which individual affine Fock composition operators admit bounded measurable Toeplitz symbols and supply the explicit symbol. The present result uses that characterization as a premise to determine the multiplicative word metric of the constrained composition-operator semigroup; its sharp boundary and translation penalty are additional conclusions.

Bauer, Fulsche, and Rodriguez Rodriguez (arXiv:2405.20792, Section 3.3) study membership of affine composition operators in the **Toeplitz algebra**, which is a broader and different operator class. Chalendar and Partington (arXiv:2106.00427) classify iteration and continuous semigroups of Fock composition operators without imposing bounded-symbol Toeplitz representability on each factor. Cho, Park, and Zhu (arXiv:1212.0045) consider boundedness of products with analytic and conjugate-analytic Toeplitz symbols, rather than shortest products of affine composition operators that are individually bounded-symbol Toeplitz. These results supply context but do not imply an exact \(B_n(\theta)\) word ball under the present generator restriction.

## Limitations

The result is for one complex variable and Gaussian Fock norms. It classifies the **restricted factorization problem** where each Toeplitz factor is also an affine composition operator, not arbitrary Toeplitz factorization. It depends on the published single-factor recognition theorem; no claim of originality is made for that premise. Although published and indexed sources were compared, an equivalent product-set statement under different terminology may exist. The result has not received an independent mathematical audit.

## References

1. Z. Lin, Y. Lu and C. Zu, *A Fourier Criterion for Recognizing Toeplitz Operators on Fock Spaces*, arXiv:2607.04102, first posted 2026-07-05, especially Corollary 3.1. https://arxiv.org/abs/2607.04102
2. W. Bauer, R. Fulsche and M. A. Rodriguez Rodriguez, *Operators in the Fock-Toeplitz algebra*, arXiv:2405.20792, first posted 2024-05-31, Section 3.3. https://arxiv.org/abs/2405.20792
3. I. Chalendar and J. R. Partington, *Weighted composition operators on the Fock space: iteration and semigroups*, arXiv:2106.00427, first posted 2021-06-01. https://arxiv.org/abs/2106.00427
4. H. R. Cho, J.-D. Park and K. Zhu, *Products of Toeplitz operators on the Fock space*, arXiv:1212.0045, first posted 2012-11-30. https://arxiv.org/abs/1212.0045
