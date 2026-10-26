# Arithmetic algebraicity trichotomy for Anosov–quarter-turn synchronization

## Finding
Let \(A=\begin{pmatrix}a&b\\c&d\end{pmatrix}\in\operatorname{SL}_2(\mathbb Z)\) have \(t=\operatorname{tr}(A)>2\), and let \(J=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\). The induced automorphisms \(f_A(x)=Ax\) and \(g_J(x)=Jx\) act on \(\mathbb T^2=\mathbb R^2/\mathbb Z^2\). Set \(\delta=b-c\) and \(N_n=\#\{x\in\mathbb T^2:f_A^n(x)=g_J^n(x)\}\), allowing \(N_n=\infty\).

**Complete classification.** The pair is synchronously tame (all \(N_n<\infty\)) if and only if \(\delta\ne-2\). For tame pairs, \(N_{2k}=\operatorname{tr}(A^{2k})-2(-1)^k\) for \(k\ge1\). Write \(U_0=0\), \(U_1=1\), \(U_{n+1}=tU_n-U_{n-1}\). For odd \(n=2k+1\):
\[
N_n=\begin{cases}
2,&\delta=0,\\
|\delta|U_n+2\operatorname{sgn}(\delta)(-1)^k+2\mathbf 1_{\{\delta=-1,\,n=1\}},&\delta\ne0,-2.
\end{cases}
\]
Consequently the entire count sequence depends only on the two integers \((t,\delta)\), not the individual entries of \(A\).

Put \(\lambda=(t+\sqrt{t^2-4})/2>1\) and \(D_t(z)=1-(t^2-2)z^2+z^4\). For any tame pair let \(Z_{A,J}(z)=\exp(\sum_{n\ge1}N_nz^n/n)\), initially as a germ at zero. Exactly one of the following occurs.

* **Symmetric case \(\delta=0\).** The zeta function is algebraic but nonrational:
\[
Z_{A,J}(z)=\frac{(1+z)(1+z^2)}{(1-z)\sqrt{D_t(z)}}.
\]
Its synchronization growth has no common root limit: \(\liminf_{n\to\infty}N_n^{1/n}=1\) and \(\limsup_{n\to\infty}N_n^{1/n}=\lambda\).
* **Nonsymmetric tame case \(\delta\ne0,-2\).** The zeta function is transcendental over \(\mathbb C(z)\), and \(\lim_{n\to\infty}N_n^{1/n}=\lambda\). More explicitly, the germ with value one at zero is
\[
Z_{A,J}(z)=\frac{1+z^2}{\sqrt{D_t(z)}}\exp\!\left(\frac{|\delta|}{\sqrt{t^2-4}}\big[\operatorname{arctanh}(\lambda z)-\operatorname{arctanh}(\lambda^{-1}z)\big]+2\operatorname{sgn}(\delta)\arctan z+2\mathbf 1_{\{\delta=-1\}}z\right).
\]
* **Singular case \(\delta=-2\).** Already \(N_1=\infty\), so the finite-count synchronization zeta function is undefined.

These three cases all occur with integer matrices of positive hyperbolic trace. The standard symmetric cat matrix \(A=\begin{pmatrix}2&1\\1&1\end{pmatrix}\) has \(N_1=2\), \(N_2=9\), and therefore also violates the order-two Gauss–Dold divisibility condition \(2\mid(N_2-N_1)\).

## Assumptions and scope
All matrices are integral, invertible of determinant one, and have real trace strictly greater than two. Thus \(f_A\) is a smooth Anosov torus automorphism and \(g_J\) is the finite-order quarter-turn; they do not commute because \(A\) cannot be a scalar matrix. The coordinate frame in which \(J\) is the displayed quarter-turn is fixed; \(\delta\) is defined relative to this frame. Synchronization is simultaneous comparison of the two \(n\)-th iterates on the **same initial point**, not periodic points of a single map. The statements hold for every positive integer \(n\), with no asymptotic exception except the explicitly marked \(n=1\) count when \(\delta=-1\).

## Proof
**1. Counting by determinant.** For any integer two-by-two matrix \(M\) with \(\det M\ne0\), the kernel of its torus endomorphism has exactly \(|\det M|\) points; for \(\det M=0\) its kernel contains a positive-dimensional subtorus and is infinite. Here the coincidence set is exactly the kernel of \(A^n-J^n\).

Since \(\det A=1\), Cayley–Hamilton gives \(A^n=U_nA-U_{n-1}I\), and hence \((A^n)_{12}-(A^n)_{21}=\delta U_n\). For odd \(n=2k+1\), \(J^n=(-1)^kJ\); direct two-by-two determinant expansion gives
\[
\det(A^n-J^n)=2+(-1)^k\delta U_n.
\]
For even \(n=2k\), \(J^n=(-1)^kI\) and
\[
\det(A^n-J^n)=2-(-1)^k\operatorname{tr}(A^n).
\]
The eigenvalues of \(A\) are \(\lambda>1\) and \(\lambda^{-1}<1\). Therefore \(U_n=(\lambda^n-\lambda^{-n})/(\lambda-\lambda^{-1})\), with \(U_1=1\), \(U_3=t^2-1\ge8\), and strictly increasing positive \(U_n\). Similarly \(\operatorname{tr}(A^n)>2\). The even determinants never vanish, and an odd determinant can vanish only if \(n=1\) and \(\delta=-2\). Resolving absolute values for odd \(n\) gives the displayed formula, including the sole exception \(\delta=-1,n=1\). This establishes tameness and all counts.

**2. Exact zeta.** With \(T_n=\operatorname{tr}(A^n)=\lambda^n+\lambda^{-n}\), the even terms sum formally to
\[
\sum_{k\ge1}\frac{[T_{2k}-2(-1)^k]z^{2k}}{2k}
=-\tfrac12\log D_t(z)+\log(1+z^2).
\]
When \(\delta=0\), the odd terms sum to \(\sum_{k\ge0}2z^{2k+1}/(2k+1)=\log((1+z)/(1-z))\). Exponentiating gives the algebraic formula.

When \(\delta\ne0,-2\), the odd count formula separates into the series of \(|\delta|U_n\), the alternating \(2\operatorname{sgn}(\delta)(-1)^k\), and the exceptional singleton. Using \(U_n=(\lambda^n-\lambda^{-n})/\sqrt{t^2-4}\), the three integrated generating series are, respectively,
\[
\frac{|\delta|}{\sqrt{t^2-4}}[\operatorname{arctanh}(\lambda z)-\operatorname{arctanh}(\lambda^{-1}z)],\quad
2\operatorname{sgn}(\delta)\arctan z,\quad
2\mathbf1_{\{\delta=-1\}}z.
\]
Adding them to the even part and exponentiating proves the second formula, with analytic branches normalized to vanish in the exponent at zero.

**3. Algebraicity boundary.** For symmetric \(A\), \(D_t(z)=(1-\lambda^2z^2)(1-\lambda^{-2}z^2)\) has four simple real roots, none canceled by the numerator. Consequently the stated zeta is algebraic but not rational.

For \(\delta\ne0,-2\), the logarithmic derivative \(Z'_{A,J}/Z_{A,J}=\sum_{n\ge1}N_nz^{n-1}\) is rational. Its residue at \(z=i\) equals
\[
\operatorname{Res}_{z=i}\frac{Z'_{A,J}(z)}{Z_{A,J}(z)}=1-i\operatorname{sgn}(\delta).
\]
Indeed the even contribution \(\log(1+z^2)\) supplies residue one and the alternating odd contribution \(2\operatorname{sgn}(\delta)\arctan z\) supplies residue \(-i\operatorname{sgn}(\delta)\). All remaining logarithmic derivatives are regular at \(i\), since \(D_t(i)=t^2>0\) and \(\lambda\) is real. An algebraic germ over \(\mathbb C(z)\) has a Puiseux expansion near each finite singularity, so every residue of its logarithmic derivative is a **rational number** (the leading Puiseux exponent). The nonreal residue above is impossible for an algebraic function. Hence the zeta is transcendental.

**4. Growth boundary.** If \(\delta=0\), the odd synchronization counts are exactly two while \(N_{2k}=\lambda^{2k}+\lambda^{-2k}-2(-1)^k\) grows exponentially, giving lower and upper root limits \(1\) and \(\lambda\). If \(\delta\ne0,-2\), both odd and even subsequences have positive leading multiples of \(\lambda^n\) (the odd multiple is \(|\delta|/\sqrt{t^2-4}\)); a finite initial exception cannot affect the limit. Thus the common root limit is \(\lambda\).

## Verification
Run `python3 verify.py` (Python standard library only). The verifier checks 11 explicit hyperbolic matrices (including powers of the cat matrix), each through 32 time steps, using direct integer matrix powers independent of the closed-form recurrence. It also checks exact coefficient identities for the algebraic zeta in symmetric cases, the parity decomposition in nonsymmetric cases, singularity at the specified exceptional parameter, and the non-Dold witness \(N_1=2,N_2=9\). The analytic residue/Puiseux argument is a proof, not a finite computation. All tests print `VERIFY_OK`.

## Relationship to prior work
Miles, *Synchronization points and associated dynamical invariants* (2013), Section 3 and Theorem 3.1, already proves the general determinant identity and rationality of the **ordinary** synchronization-count generating function for nonsingular two-torus automorphism pairs; those facts are not claimed as new here. That general theorem does not determine the analytic type of the exponential synchronization zeta for all hyperbolic quarter-turn pairs, nor the exceptional symmetry boundary with missing root-growth limit.

Fel'shtyn and Slomiany, *Synchronization points: growth, asymptotics, congruences, and the synchronization zeta function* (arXiv:2601.21888, first released January 29, 2026), give rationality under commuting hypotheses and an algebraic/nonrational example on a finite three-point space (Remark 26). Their rationality theorem for commuting Anosov diffeomorphisms does not apply here. Their general finite-set formula concerns different underlying spaces and cannot classify the hyperbolic toral family.

Fel'shtyn and Slomiany, *The Reidemeister and the Nielsen numbers: growth rate, asymptotic behavior, dynamical zeta functions and the Gauss congruences* (arXiv:2603.08527, Theorem 22(ii)–(v)), assume simultaneous triangularizability of the relevant pairs to infer rationality and existence of growth. Here \(J\) has only eigenvalues \(\pm i\), whereas \(A\) has distinct positive real eigenvalues, with no shared complex eigenline; hence those triangularizability hypotheses fail. This is a genuine boundary, not a contradiction to that result.

The identified contribution is the **complete arithmetic trichotomy of synchronization zeta algebraicity and growth for every positive-trace hyperbolic toral automorphism paired with the quarter-turn**, together with its explicit monodromy residue. Earlier determinant formulas are foundational inputs rather than displaced discoveries.

## Limitations
The trichotomy fixes the quarter-turn \(J\) and the integer coordinate frame, and does not classify arbitrary finite-order partners, matrices with trace \(\le2\), nonlinear perturbations, or other manifolds. The claim is a self-contained theorem conditional only on the explicit linear assumptions, not a claim that all noncommuting zeta functions are transcendental. Bibliographic priority under alternate coincidence/Nielsen terminology remains subject to further independent review. No independent mathematical audit has been performed.

## References
1. R. Miles, *Synchronization points and associated dynamical invariants*, Trans. Amer. Math. Soc., 2013, DOI: 10.1090/S0002-9947-2013-05829-1. Author-posted full text: https://www.researchgate.net/publication/260059770_Synchronization_points_and_associated_dynamical_invariants
2. A. Fel'shtyn and M. Slomiany, *Synchronization points: growth, asymptotics, congruences, and the synchronization zeta function*, arXiv:2601.21888, initial public version January 29, 2026. https://arxiv.org/abs/2601.21888
3. A. Fel'shtyn and M. Slomiany, *The Reidemeister and the Nielsen numbers: growth rate, asymptotic behavior, dynamical zeta functions and the Gauss congruences*, arXiv:2603.08527, Theorem 22. https://arxiv.org/abs/2603.08527
