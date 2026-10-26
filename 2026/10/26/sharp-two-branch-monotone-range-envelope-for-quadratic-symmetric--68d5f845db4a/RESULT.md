# Sharp two-branch monotone range envelope for quadratic symmetric Jacobi projection

## Finding
Let \(\alpha>-1\) and let \(P_{2,\alpha}\) be the \(L^2\)-orthogonal projection onto the polynomials of degree at most two on \([-1,1]\), for the probability measure
\[d\mu_\alpha(t)=c_\alpha(1-t^2)^\alpha\,dt,\qquad c_\alpha=\frac{\Gamma(\alpha+3/2)}{\sqrt\pi\,\Gamma(\alpha+1)}.\]
Define \(q=2\alpha+3>1\), \(r=\sqrt{q+3}\), \(u=1/(r+1)\), \(v=-1/(r-1)\),
\[H(a)=\mu_\alpha([a,1]),\qquad T(a)=c_\alpha(1-a^2)^{\alpha+1},\]
and the explicit two branch values
\[E(q)=H(u)+T(u)\left(\frac q{q-1}+\frac{r-1}{2}\right),\]
\[I(q)=H(v)+\frac{T(v)}{q-1}\left(r-\frac1{r+1}\right),\qquad M(q)=\max\{E(q),I(q)\}.\]
For every real measurable nondecreasing \(f:[-1,1]\to[0,1]\), with its usual almost-everywhere interpretation, the polynomial \(P_{2,\alpha}f\) satisfies the **sharp, attained** bounds
\[\boxed{1-M(q)\ \le\ (P_{2,\alpha}f)(z)\ \le\ M(q)\quad\text{for all }z\in[-1,1].}\]
If \(E(q)>I(q)\), the unique upper extremizing step (up to \(\mu_\alpha\)-null changes) is \(f(t)=\mathbf1_{\{t\ge u\}}\), attaining the maximum at \(z=1\). If \(I(q)>E(q)\), it is \(f(t)=\mathbf1_{\{t\ge v\}}\), attaining the maximum at \(z=u\). At a tie these two and only these two step/evaluation pairs attain the upper bound. The lower extremizers are their reflected complements: replace \(f(t)\) by \(1-f(-t)\) and \(z\) by \(-z\). Moreover,
\[\lim_{q\downarrow1} E(q)=1,\qquad\lim_{q\downarrow1}I(q)=\frac43,\]
whereas at \(q=3\) (uniform weight),
\[E(3)=\frac{27+3\sqrt6}{25},\qquad I(3)=\frac{27}{50}+\frac{6\sqrt6}{25}<E(3).\]
Thus the optimal extremizing geometry changes at least once as the weight varies. **No assertion is made that the crossing is unique.**

## Assumptions and scope
The weight is symmetric Jacobi (ultraspherical), \(\alpha>-1\), and the input is a real nondecreasing essentially bounded function with values in \([0,1]\). Projection is the ordinary orthogonal polynomial truncation at degree two, not a shape-constrained least-squares fit, and estimates hold for its continuous polynomial representative even at endpoints. All constants are defined by the displayed incomplete beta integrals; there is no numerical fitting. General nonsymmetric Jacobi measures and higher polynomial degrees are outside the claim.

## Proof
**1. Reproducing kernel.** Symmetry and beta integration give \(\mathbb E[t^2]=1/q\) and \(\mathbb E[t^4]=3/[q(q+2)]\). Hence the orthogonal basis \(1,t,t^2-1/q\) has squared norms \(1,1/q,2(q-1)/[q^2(q+2)]\), respectively. Its kernel is
\[K(z,t)=1+qzt+\frac{q^2(q+2)}{2(q-1)}\left(z^2-\frac1q\right)\left(t^2-\frac1q\right).\]
For the upper-tail step \(f_a(t)=\mathbf1_{\{t\ge a\}}\), let \(F(z,a)=P_{2,\alpha}f_a(z)\). Integration by parts (differentiate \((1-t^2)^{\alpha+1}\) and \(t(1-t^2)^{\alpha+1}\)) gives
\[F(z,a)=H(a)+\frac{T(a)}{q-1}\left[qz+\frac{q(q+2)}2a\left(z^2-\frac1q\right)\right].\tag{1}\]
This formula is valid for every \(a,z\in[-1,1]\), with endpoint values interpreted by limits.

**2. Exhaust the evaluation variable.** For fixed \(a\ge0\), equation (1) is convex in \(z\); and \(F(1,a)-F(-1,a)=2qT(a)/(q-1)>0\) for interior \(a\), so its maximum occurs at \(z=1\). For \(-1/(q+2)<a<0\), (1) is concave with its vertex to the right of \(1\), so again \(z=1\) maximizes. For \(-1\le a\le-1/(q+2)\), the maximizing vertex is \(z_*(a)=-1/[(q+2)a]\in(0,1]\). Consequently all candidate maxima lie either on the endpoint branch \(F(1,a)\) or on \(\Phi(a)=F(z_*(a),a)\).

**3. Exhaust the step variable.** Differentiation at fixed \(z\) gives \(\partial_aF(z,a)=-c_\alpha(1-a^2)^\alpha K(z,a)\) in the open interval. At \(z=1\),
\[K(1,a)=\frac q2[(q+2)a^2+2a-1].\]
Its two roots are \(v=-1/(r-1)\) and \(u=1/(r+1)\). The signs show that the endpoint branch decreases, then increases, then decreases, with the only interior local maximum at \(a=u\). Its global maximum is therefore \(\max\{1,E(q)\}\), as \(F(1,-1)=1\) and \(F(1,1)=0\).
On the interior-vertex branch, the envelope derivative is \(\Phi'(a)=-c_\alpha(1-a^2)^\alpha K(z_*(a),a)\). An exact factorization is
\[K(z_*(a),a)=-\frac{q\big((q+2)a^2-2a-1\big)\big((q+2)a^2+2a-1\big)}{2a^2(q-1)(q+2)}.\]
The only critical points in \((-1,-1/(q+2))\) are \(v\) (strict local maximum) and \(-u\) (strict local minimum), in that order. The other boundary values are \(\Phi(-1)=1\) and \(\Phi(-1/(q+2))=F(1,-1/(q+2))\le\max\{1,E(q)\}\). Since \(\Phi\) rises strictly from \(1\) to \(\Phi(v)=I(q)>1\), the global step/evaluation maximum is exactly \(M(q)=\max\{E(q),I(q)\}\). Substituting \(z=1,a=u\) and \(z=u,a=v\) into (1) proves the displayed formulas.

**4. All monotone inputs and equality.** Every nondecreasing \(f\in[0,1]\) has, up to null changes, a positive Stieltjes representation \(f(t)=c+\int\mathbf1_{\{t\ge a\}}\,d\nu(a)\), with \(c\ge0\), \(\nu\ge0\), and \(c+\nu([-1,1])\le1\). As \(P1=1\), equation (1) and \(M>1\) imply \(Pf(z)\le c+M\nu([-1,1])\le M\). Strictness away from the two maximizer pairs forces the claimed equality cases, including at ties. Reflection invariance yields \(P(1-f(-\cdot))(z)=1-Pf(-z)\), giving the sharp lower bound and its equality cases.

**5. Weight limits.** As \(q\downarrow1\), \(\alpha+1=(q-1)/2\downarrow0\), the symmetric beta law concentrates half its mass at each endpoint, while \(T(u)/(q-1)\to1/2\), \(T(v)/(q-1)\to1/2\), \(u\to1/3\), and \(v\to-1\). The moving cutoff \(v\) approaches \(-1\) only polynomially in \(q-1\), so \(H(v)\to1/2\) as well. Formula (1) therefore gives \(E\to1\) and \(I\to4/3\). At \(q=3\), \(c_\alpha=1/2\) and \(H(a)=(1-a)/2\), giving the two stated radicals by substitution. Continuity proves at least one crossing.

## Verification
The standalone `verify_jacobi.py` checks the kernel factorizations exactly with symbolic algebra, verifies both \(q=3\) radical formulas, compares the candidate envelope with sampled step optima at ten parameter values, and independently quadratures the projection kernel against several discontinuous steps. The direct quadrature and symbolic checks passed. The proof above, not finite numerical exploration, establishes the universal quantifiers and equality cases.

## Relationship to prior work
Kaber (2006) proves the parameter-independent **large-degree** Gibbs constant for expansions of the fixed sign function, rather than the **degree-two global** range envelope over all bounded nondecreasing functions and all jump positions. Kopotun–Leviatan–Prymak–Shevchuk (2011) survey constrained shape-preserving approximation, whereas the current object is the unmodified orthogonal projector and its worst range violation. Calderón–Urbina (2012) study Jacobi-series Abel summability and kernels; their operator and conclusions are different. The basic Jacobi orthogonality and reproducing-kernel ingredients are classical, while the two-branch exact global maximization and equality classification are the asserted contribution.

## Limitations
Originality has been assessed against accessible literature and current indexed findings, not certified exhaustively; an unindexed equivalent theorem remains possible. The crossing set \(\{q:E(q)=I(q)\}\) is characterized exactly through the two formulas, but its uniqueness and a closed-form threshold are **not established**. The result neither proves shape preservation nor controls higher degrees or nonsymmetric Jacobi weights. Numerical tests are corroboration, not proof.

## References
- S. M. Kaber, *The Gibbs Phenomenon for Jacobi Expansions*, Communications in Applied Analysis **10** (2006), 133–148. https://www.acadsol.eu/en/articles/10/2/3.pdf
- K. A. Kopotun, D. Leviatan, A. Prymak and I. A. Shevchuk, *Uniform and Pointwise Shape Preserving Approximation by Algebraic Polynomials*, arXiv:1109.0968, initial version 2011-09-05. https://arxiv.org/abs/1109.0968
- C. P. Calderón and W. Urbina, *On Abel Summability of Jacobi Polynomials Series, the Watson Kernel and Applications*, arXiv:1207.4524, initial version 2012-07-18. https://arxiv.org/abs/1207.4524
- J. M. Davis and P. Hagelstein, *Gibbs phenomena for some classical orthogonal polynomials*, Journal of Mathematical Analysis and Applications **505** (2022), 125574. https://doi.org/10.1016/j.jmaa.2021.125574
