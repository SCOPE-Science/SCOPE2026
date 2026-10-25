# An exact all-dimensional local spectrum and Lambert-W rate for vertex-cyclic away-step descent

## Finding
For each integer \(n\ge3\), apply exact-line-search vertex-cyclic polyhedral coordinate descent **with away steps** (PolyCDwA, Algorithm 2 in Mazumder--Wang) to the standard simplex \(\Delta_n\) and the isotropic strongly convex objective \(f(x)=\tfrac12\|x-u\|_2^2\), where \(u=\mathbf1/n\). One sweep visits \(e_1,\ldots,e_n\) in that order. Its sweep map \(F_n\) is smooth near \(u\). On the tangent hyperplane \(H=\{h:\sum_i h_i=0\}\), the Jacobian \(T_n=DF_n(u)|_H\) has the **exact characteristic polynomial**
\[
\det(zI_H-T_n)=\frac{z}{(n-1)^n}\frac{(1+(n-1)z)^n-n^n z^{n-1}}{(z-1)^2}.
\]
The displayed quotient is a polynomial: the numerator has a double zero at \(z=1\). The zero eigenvalue is simple and all \(n-2\) nonzero eigenvalues are simple and lie strictly in the open unit disk. In particular,
\[
\sigma(T_3)=\{0,-1/8\},\qquad
\sigma(T_4)=\{0,(-7+4\sqrt2\,i)/81,(-7-4\sqrt2\,i)/81\}.
\]
Let \(\rho_n=\rho(T_n)\). For every \(q\) with \(\rho_n<q<1\), there is a neighborhood of \(u\) and a finite constant \(C_q\) such that
\[
\|F_n^{\,k}(x)-u\|_2\le C_q q^k\|x-u\|_2\qquad(k\ge0).
\]
No smaller uniform neighborhood rate \(q<\rho_n\) is possible. The all-dimensional rate has the exact limit
\[
\lim_{n\to\infty}\rho_n=\frac1{|W_1(-e^{-1})|}
=0.12383032271899503288\ldots,
\]
where \(W_1\) is the first upper nonreal branch of the Lambert \(W\) function (the conjugate is on \(W_{-2}\)).

## Assumptions and scope
The standard simplex is \(\Delta_n=\{x\in\mathbb R^n:x_i\ge0,\sum_i x_i=1\}\), with vertices \(e_1,\ldots,e_n\). The objective has unique minimizer \(u=\mathbf1/n\). Starting at an interior point, exact-line-search PolyCDwA visits the vertices cyclically and updates
\[
x^+=x+\alpha(e_j-x),\quad
\alpha=\arg\min_{a\in[-x_j/(1-x_j),\,1]}f(x+a(e_j-x)).
\]
The simplex barycentric coefficients of the algorithm are uniquely the current coordinates \(x_i\). The claim concerns **local** convergence of full sweeps, not a global rate, and exact arithmetic. The rule is PolyCDwA with permitted away steps, **not** ordinary PolyCD restricted to \(\alpha\ge0\). In the neighborhood used, all inner unconstrained minimizers lie strictly inside their away-step intervals.

## Proof
**Step 1 (the local derivative).** Let \(w_j=e_j-u\in H\). For \(x\) near \(u\), exact minimization over the allowed interval gives
\[
\alpha_*(x)=-\frac{\langle x-u,e_j-x\rangle}{\|e_j-x\|_2^2}.
\]
At \(u\), this is zero; the lower bound is strictly negative and the upper bound strictly positive, so this expression applies smoothly in a common small neighborhood, including all intermediate iterates. Differentiating the update at \(u\) in tangent directions produces
\[
P_jh=h-\frac{n}{n-1}\langle w_j,h\rangle w_j.
\]
Since \(\|w_j\|^2=(n-1)/n\), \(P_j\) is the orthogonal projection onto \(\{h\in H:h_j=0\}\). Therefore \(T_n=P_nP_{n-1}\cdots P_1|_H\). In coordinates, \(P_j\) sets coordinate \(j\) to zero and adds \(h_j/(n-1)\) to each other coordinate.

**Step 2 (an exact eigenvalue equation).** For an input \(h\in H\), let \(s_j\) be its coordinate \(j\) immediately before projection \(P_j\), and \(S_j=\sum_{i=1}^j s_i\), with \(S_0=0\). The initial and output coordinates are exactly
\[
h_j=s_j-\frac{S_{j-1}}{n-1},\qquad (T_nh)_j=\frac{S_n-S_j}{n-1}.
\]
If \(T_nh=zh\) with \(z\ne0\), these identities yield
\[
[1+(n-1)z]S_j-nzS_{j-1}=S_n.
\]
Necessarily \(S_n\ne0\): otherwise the recursion forces all \(S_j=0\), and hence \(h=0\). The coefficient \(1+(n-1)z\) cannot vanish for an eigenvalue, since the first equation would give \(S_n=0\). For \(z\ne1\), put \(r=nz/[1+(n-1)z]\). Solving the recurrence gives \(S_j=S_n(1-r^j)/(1-z)\); setting \(j=n\) forces \(r^n=z\). Equivalently,
\[
(1+(n-1)z)^n=n^n z^{n-1}.
\]
Conversely, for any nonzero solution of this equation other than \(z=1\), the recurrence with \(S_n=1\) reconstructs a nonzero \(h\in H\) and the eigen-equation, so the condition is sufficient.

The polynomial \(B_n(z)=(1+(n-1)z)^n-n^n z^{n-1}\) has a root of multiplicity **exactly two** at \(z=1\): \(B_n(1)=B_n'(1)=0\) and \(B_n''(1)=n^{n-1}(n-1)>0\). Its other roots are simple: if both \(B_n(z)\) and \(B_n'(z)\) vanish at a nonzero \(z\), division of the respective equations yields \(nz=1+(n-1)z\), hence \(z=1\). Thus the nonunit nonzero solutions contribute exactly \(n-2\) simple eigenvalues. Since \(\dim H=n-1\), the remaining eigenvalue is \(0\), with multiplicity one, proving the displayed characteristic polynomial. Substituting \(n=3,4\) gives the claimed explicit eigenvalues.

**Step 3 (strict contractivity and local sharpness).** Each \(P_j\) is an orthogonal projection and thus nonexpansive. If \(\|T_nh\|=\|h\|\), equality at every stage means \(h\) is fixed by every \(P_j\); hence all its coordinates vanish and \(h=0\). Compactness of the unit sphere in \(H\) gives \(\|T_n\|<1\), so all eigenvalues are strictly inside the unit disk. For each \(q>\rho_n\) one can choose an equivalent norm on \(H\) in which \(\|T_n\|<q\); continuity of \(DF_n\) then proves the stated local geometric estimate, with Euclidean norm-equivalence constants. Conversely, a bound with \(q<\rho_n\) valid on an entire neighborhood would, after differentiation of its \(k\)-fold iterate at \(u\), imply \(\|T_n^k\|\le C q^k\) for every \(k\). The spectral-radius formula contradicts this.

**Step 4 (the Lambert-W limit).** Divide the eigenvalue equation by \((nz)^{n}\) for \(z\ne0\) and define
\[
h_n(z)=\left(1+\frac{1-z}{nz}\right)^n-\frac1z.
\]
On every compact subset of \(\mathbb C\setminus\{0\}\), it converges uniformly to \(h(z)=\exp((1-z)/z)-1/z\). The zeros of \(h\) are exactly \(z=-1/W_k(-e^{-1})\). The double zero \(z=1\) corresponds to the coalesced real branches \(W_0,W_{-1}\); all other zeros are simple and nonreal. By Rouché's theorem on a small circle around \(1\), the two exact zeros of \(h_n\) there exhaust the limiting double zero, so no eigenvalue other than the removed double root can approach \(1\). At each other zero, Hurwitz's theorem supplies nonunit polynomial roots converging to it. Conversely, by compactness and the strict finite-dimensional projection bound, every limit of nonzero eigenvalues staying a positive distance from \(0\) is such a nonunit zero of \(h\).

It remains to identify the largest modulus of these limiting nonunit zeros. For \(w=a+ib\) with \(b>0\) and \(we^w=-e^{-1}\), imaginary-part cancellation and the negative real sign require \(\sin b>0\), \(a=-b\cot b\), and
\[
\Phi(b)=\log\frac{b}{\sin b}-b\cot b+1=0.
\]
Differentiation gives \(b\Phi'(b)=(1-b\cot b)^2+b^2>0\). There is no solution in \((0,\pi)\): \(\Phi(0^+)=0\) and \(\Phi\) is strictly increasing. For each integer \(m\ge1\), exactly one solution occurs in \((2m\pi,(2m+1)\pi)\), since \(\Phi\) increases from \(-\infty\) to \(+\infty\). Moreover \(a=-1-\log|w|\) and therefore
\[
b^2=|w|^2-(1+\log|w|)^2.
\]
For \(|w|>1\), the right side is strictly increasing with \(|w|\), since its derivative is \(2(|w|^2-1-\log|w|)/|w|>0\). The smallest \(|w|\) among nonreal Lambert branches thus comes from the first pair with \(b\in(2\pi,3\pi)\): \(W_1(-e^{-1})\) and its conjugate \(W_{-2}(-e^{-1})\). Their reciprocal modulus is the largest modulus among the nonunit zeros of \(h\). The compactness and zero-continuity arguments above prove convergence of the finite spectral radii to this value.

## Verification
The standalone `check_polycd_spectrum.py` reconstructs the exact projected Jacobian with symbolic rational arithmetic and checks the characteristic polynomial for every \(3\le n\le8\). It also compares the derivative against the actual nonlinear away-step sweep at 70 perturbed interior points and computes numerical spectra for dimensions \(3,4,6,10,20,40\). Executed successfully with NumPy 2.3.5 and SymPy 1.14.0, reporting `VERIFY_OK exact characteristic polynomials n=3..8 and 70 nonlinear differential checks`. A separate high-precision evaluation of \(W_1(-e^{-1})\) corroborated the displayed limit. Finite calculations are cross-checks; the claims for all dimensions and the limiting constant rest on the proof.

## Relationship to prior work
Mazumder and Wang (2023) introduced PolyCDwA, its exact feasible away-step interval and a general global linear-convergence theorem. Those algorithmic and convergence results are **not** claimed as new. The present theorem specializes the original update to a canonical isotropic simplex model but establishes a complete **local sweep spectrum in every dimension**, the real-to-complex transition from \(n=3\) to \(n=4\), and an explicit Lambert-W limiting contraction factor. Sun and Ye (2016) analyze cyclic coordinate descent and Kaczmarz equivalences and worst-case dimension effects; a later general Kaczmarz formulation gives a triangular-Gram iteration representation. These general tools do not state this PolyCDwA specialization's evaluated characteristic polynomial or its Lambert-W limit in the inspected materials. Absence from inspected sources is not proof of global novelty.

## Limitations
The result is for exact line search with away steps, a single full vertex cycle, a **local** neighborhood of the center, the isotropic Euclidean quadratic, and exact arithmetic. The spectral radius is the sharp uniform local **linear** rate, not an assertion that every individual trajectory converges at exactly that rate. The general PolyCDwA algorithm and its global linear convergence are prior work; classical cyclic-projection identities could offer an alternative derivation and remain a residual overlap risk.

## References
1. R. Mazumder and H. Wang, *A Cyclic Coordinate Descent Method for Convex Optimization on Polytopes*, arXiv:2303.07642, first public version 2023-03-14, especially Algorithm 2 and Theorem 3.2. https://arxiv.org/abs/2303.07642
2. R. Sun and Y. Ye, *Worst-case Complexity of Cyclic Coordinate Descent: \(O(n^2)\) Gap with Randomized Version*, arXiv:1604.07130. https://arxiv.org/abs/1604.07130
3. *Tight Convergence Bounds for the Classical Kaczmarz Method*, arXiv:2609.32034, section on the general triangular-Gram iteration representation. https://arxiv.org/abs/2609.32034
4. R. M. Corless et al., *On the Lambert W Function*, Advances in Computational Mathematics 5 (1996), 329--359.
