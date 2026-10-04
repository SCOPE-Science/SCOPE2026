# An \(n^{-1/4}\) finite-window approach to the two-state sliding-count obstruction
## Finding
For every sufficiently large integer \(n\), define
\[
\rho_n=1-\sqrt{2}\,n^{-1/4},\qquad
r_n=1-\rho_n^2,\qquad
u_n=\exp(-n^2),
\]
\[
\varepsilon_n=2^{-1/2}n^{-3/4},\qquad
x_n=\frac{1-\varepsilon_n}{\rho_n}.
\]
Consider the irreducible reversible two-state chain
\[
P_n=\begin{pmatrix}1-u_n&u_n\\ r_n&1-r_n\end{pmatrix},
\]
where \(u_n=\exp(-n^2)\). From a stationary trajectory \((X_t)\), let
\[
K_t=\sum_{j=0}^{n-1}X_{t+j}\in\{0,\ldots,n\}
\]
and let \(\widetilde P_n\) be the reversible projected count kernel defined by the stationary edge law of \((K_0,K_1)\). For the count test
\[
f_n(0)=0,\qquad f_n(k)=x_n^k\quad(1\le k\le n),
\]
the normalized Rayleigh quotient satisfies
\[
\frac{n\,\mathcal E_{\widetilde P_n}(f_n,f_n)}
{\operatorname{Gap}(P_n)\operatorname{Var}(f_n(K_0))}
=\frac14+\frac1{\sqrt2}n^{-1/4}+O(n^{-1/2}).
\]
The variational principle therefore gives
\[
\frac{n\operatorname{Gap}(\widetilde P_n)}{\operatorname{Gap}(P_n)}
\le \frac14+\frac1{\sqrt2}n^{-1/4}+O(n^{-1/2}).
\]
Thus the singular two-state obstruction approaching \(1/4\) can be realized by an explicit finite kernel and finite window at a quantified rate in the window length.

More generally, set
\[
\rho_n=1-A n^{-1/4},\qquad
\varepsilon_n=B n^{-3/4},
\]
for fixed \(A,B>0\), retain \(u_n=\exp(-n^2)\), and use \(x_n=(1-\varepsilon_n)/\rho_n\). Then the same calculation gives
\[
\frac{n\,\mathcal E_{\widetilde P_n}(f_n,f_n)}
{\operatorname{Gap}(P_n)\operatorname{Var}(f_n(K_0))}
=\frac14+C(A,B)n^{-1/4}+O(n^{-1/2}),
\]
where
\[
C(A,B)=\frac A4+\frac1{8B}+\frac{B}{2A^2}.
\]
Among this balanced two-parameter scaling class, \(C(A,B)\) has the unique minimum \(1/\sqrt2\), attained at \(A=\sqrt2\) and \(B=1/\sqrt2\).

## Assumptions and scope
The base chain has states \(\{0,1\}\), transition probabilities \(0\to1\) equal to \(u\) and \(1\to0\) equal to \(r\), with \(0<u,r<1\). Its stationary mass at state \(1\) is \(u/(u+r)\), its nonconstant eigenvalue is \(1-u-r\), and its right spectral gap is \(u+r\). The projected kernel is the stationary one-step projection of the sliding count, not a claim that the count process itself is Markov at all lags.

The theorem concerns a particular explicit witness sequence and a particular exponential family of Rayleigh tests. The stated minimization of \(C(A,B)\) is only within the balanced scaling \(\rho_n=1-A n^{-1/4}\), \(\varepsilon_n=B n^{-3/4}\) with fixed positive \(A,B\). No global optimality over all chains or all tests is asserted.

## Proof
Write \(s=1-r\) and first hold \(n,r,x\) fixed while \(u\downarrow0\). A path with positive first-order mass away from the all-zero path contains exactly one entrance \(0\to1\), except when it starts in state \(1\), in which case the stationary initial mass itself contributes the unique factor of \(u\). Direct path enumeration gives, for \(1\le k<n\),
\[
\lim_{u\downarrow0}\frac{\Pr(K_0=k)}u
=s^{k-1}\bigl(2+(n-k-1)r\bigr),
\]
and
\[
\lim_{u\downarrow0}\frac{\Pr(K_0=n)}u=\frac{s^{n-1}}r.
\]
The two terms in the first display are the rare block touching the left or right window boundary; each of the \(n-k-1\) possible internal blocks contributes an additional factor \(r\).

Because \(K_1-K_0=X_n-X_0\), an upward count edge \(k\to k+1\) has, to first order, a unique path consisting of zeros followed by ones. Hence, for \(0\le k<n\),
\[
\lim_{u\downarrow0}\frac{\Pr(K_0=k,K_1=k+1)}u=s^k.
\]
For \(f(0)=0\), \(f(k)=x^k\), let \(y=sx^2\). Since the projected kernel is reversible and changes the count by at most one, its Dirichlet form is the sum of edge conductances times squared increments. Therefore
\[
\mathcal E_{\widetilde P_n}(f,f)=uD_0+O(u^2),
\]
with
\[
D_0=x^2+(x-1)^2\sum_{k=1}^{n-1}y^k.
\]
The mean of \(f(K_0)\) is \(O(u)\), so its square is second order. The variance has first-order coefficient
\[
\operatorname{Var}(f(K_0))=uM_0+O(u^2),
\]
where
\[
M_0=x^2\left[
\sum_{j=0}^{n-2}\bigl(2+(n-j-2)r\bigr)y^j
+\frac{y^{n-1}}r
\right].
\]
Consequently the normalized Rayleigh quotient extends continuously to the rare-entrance boundary with exact limiting value
\[
R_n^0(r,x)=\frac{nD_0}{rM_0}.
\]

Now put \(s=\rho^2\), \(x=(1-\varepsilon)/\rho\), so
\[
y=(1-\varepsilon)^2.
\]
For the balanced scaling \(\rho=1-A n^{-1/4}\), \(\varepsilon=B n^{-3/4}\), we have
\[
y^n=\exp\bigl(-2B n^{1/4}+o(1)\bigr).
\]
Thus replacing the finite geometric sums in \(D_0\) and \(M_0\) by their infinite-tail closed forms produces an error smaller than every algebraic order. Using
\[
\sum_{j\ge0}y^j=\frac1{1-y},\qquad
\sum_{j\ge0}j y^j=\frac y{(1-y)^2},
\]
and expanding in \(h=n^{-1/4}\) yields
\[
R_n^0
=\frac14+\left(\frac A4+\frac1{8B}+\frac{B}{2A^2}\right)h+O(h^2).
\]
For the explicit chain, \(u_n=\exp(-n^2)\). There are at most \(2^{n+1}\) binary paths relevant to the window edge law, while \(x_n^{2n}=\exp(O(n^{3/4}))\) and \(r_n^{-1}=O(n^{1/4})\). Every term omitted from the first-order rare-entrance expansion contains either one extra factor of \(u_n\), a stationary-normalization correction of order \(u_n/r_n\), or a factor from \((1-u_n)^j-1\) bounded by \(nu_n\). Hence the difference between the actual normalized quotient and \(R_n^0\) is smaller than every negative power of \(n\). This proves the stated expansion for the fully finite sequence.

Finally, for fixed \(A>0\), the last two terms in \(C(A,B)\) are uniquely minimized at \(B=A/2\), giving \(C(A,A/2)=A/4+1/(2A)\). The latter is uniquely minimized for \(A>0\) at \(A=\sqrt2\), giving \(B=1/\sqrt2\) and \(C=1/\sqrt2\).

## Verification
The accompanying `verify.py` independently checks the first-order path coefficients by exact rational enumeration for several finite windows, reconstructs the exact rare-limit energy and variance coefficients, and evaluates the finite geometric-sum formula at increasing window lengths. It also checks that the scaled first correction converges to \(1/\sqrt2\) for the explicit tuning. The script uses only the Python standard library and prints `VERIFY_OK` on success.

These finite checks support the algebra but are not used as a substitute for the asymptotic proof. The proof of the infinite sequence rests on the explicit path expansion, exact geometric sums, and analytic Taylor expansion above.

## Relationship to prior work
Xiang and Zhang, arXiv:2609.27836v1, define the projected sliding-window occupation-count kernel and prove the uniform comparison
\[
\frac1{1080m}\le c_m^\star\le q_{m-2},\qquad q_0=\frac14.
\]
Their Section 11 constructs nested rare-state witnesses through an ordered sequence of singular limits. In the two-state case they obtain the limiting product-test quotient \((1+\rho)^{-2}\to1/4\). Their Section 12.2 states that the construction proves neither attainment by a finite parameter choice nor a quantitative convergence rate for the finite witnesses, and Section 12.1 leaves the exact two-state constant open. The result here stays within their two-state rare-state family but supplies a single explicit finite sequence indexed by \(n\) and computes its first quantitative correction.

The earlier Xiang--Xin--Zhang preprint arXiv:2608.08678 studies the same stationary count kernel under strict positivity and establishes fixed-kernel \(n^{-1}\) behavior. The later paper explicitly distinguishes that fixed-kernel theory from its singular rare-state obstruction. No implication from the fixed-kernel result gives the explicit rare-state \(n^{-1/4}\) approach derived here.

Classical one-dimensional discrete Hardy inequalities, such as Miclo's 1999 work cited by Xiang and Zhang, can analyze birth--death gaps, but the accepted claim is a quantitative Rayleigh-witness construction rather than a new Hardy criterion.

## Limitations
The inequality is an upper bound on the projected spectral gap obtained from one test function. It does not identify the actual projected gap of the witness sequence. It does not prove \(c_2^\star=1/4\), and it does not exclude another two-state or higher-state family with a smaller limiting constant or a faster finite-window approach.

The coefficient \(1/\sqrt2\) is optimal only in the stated balanced scaling family. The choice \(u_n=\exp(-n^2)\) is intentionally very small so that the rare-entrance expansion is uniform at the displayed algebraic orders; no claim is made that this entrance scale is efficient or necessary.

The full text of arXiv:2608.08678 was not directly retrievable during the comparison check. Its abstract-level description and the later paper's explicit related-work discussion were inspected; this leaves a residual literature-access risk, recorded in the review metadata.

## References
1. Yanjin Xiang and Zhihua Zhang, *Optimal State-Space Order for Spectral Gaps of Sliding-Window Occupation Counts*, arXiv:2609.27836v1, first public 2026-08-19.
2. Yanjin Xiang, Yuchen Xin, and Zhihua Zhang, *Conditionally Resampled Sliding-Window Count Kernels: Spectral-Gap Bounds and Poincaré Inequalities*, arXiv:2608.08678, 2026.
3. Laurent Miclo, *An example of application of discrete Hardy's inequalities*, Markov Processes and Related Fields 5(3):319--330, 1999.
