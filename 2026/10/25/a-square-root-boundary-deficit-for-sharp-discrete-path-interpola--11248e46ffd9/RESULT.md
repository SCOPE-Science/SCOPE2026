# A square-root boundary deficit for sharp discrete path interpolation

## Finding

Let \(P_N\) be the unweighted path on \(N\ge2\) vertices, indexed by \(0,\ldots,N-1\). For a real or complex vector \(u\) with \(\sum_{j=0}^{N-1}u_j=0\), put
\[
\|u\|_2^2=\sum_{j=0}^{N-1}|u_j|^2,\qquad
\|Du\|_2^2=\sum_{j=0}^{N-2}|u_{j+1}-u_j|^2.
\]
The sharp constant \(K_N\) in
\[
\|u\|_\infty^2\le K_N\|u\|_2\|Du\|_2
\]
has the following exact expression. For \(x>0\) set \(\eta=2\operatorname{arsinh}(x/2)\), and define
\[
F_N(x)=\frac{2x\cosh(\eta/2)\cosh((N-\tfrac12)\eta)}
{\sinh\eta\,\sinh(N\eta)}-\frac2{Nx}.
\]
Then
\[
\boxed{K_N=\max_{x>0}F_N(x).}
\]
At each fixed \(x\), the two path endpoints, and no interior vertices when \(N\ge3\), maximize the resolvent diagonal. All nonzero equality vectors arise as scalar multiples of the mean-zero endpoint Green vectors \((L_N+x^2I)^{-1}(e_0-N^{-1}{\bf1})\) or their reversed copies, where \(x\) maximizes \(F_N\), and \(L_N=D^*D\).

The constants are strictly increasing with path length and obey
\[
\boxed{0<K_N<K_{N+1}<2,\qquad \lim_{N\to\infty}K_N=2.}
\]
More precisely, the sharp finite-size boundary deficit has the expansion
\[
\boxed{K_N=2-2\sqrt2\,N^{-1/2}+\tfrac12N^{-1}
+\tfrac{\sqrt2}{8}N^{-3/2}+O(N^{-2}).}
\]
For all sufficiently large \(N\), the maximizing parameter is unique and
\[
x_N=\sqrt2\,N^{-1/2}+\tfrac12N^{-1}+O(N^{-3/2}).
\]
For example \(K_2=1/(2\sqrt2)\). The square-root deficit comes from interaction between a Neumann-type endpoint and the global mean-zero constraint; its scale differs from a periodic boundary geometry.

## Assumptions and scope

All vertices and edges have counting/unnormalized weights; no factors of \(N^{-1}\) appear in either norm. The maximum is taken over nonzero mean-zero vectors, and the edge-difference norm is positive on that space. The eigenvalue-zero constant mode is projected away. Complex vectors use Hermitian inner products. The asymptotic claims hold as positive integer \(N\to\infty\). No uniqueness of \(x\) is asserted at small \(N\).

## Proof

**1. Green variational identity.** Fix a vertex \(j\), write \(b_j=e_j-N^{-1}{\bf1}\), and restrict \(L_N=D^*D\) to the mean-zero space. By weighted Cauchy–Schwarz,
\[
|u_j|^2=|\langle b_j,u\rangle|^2
\le G_{N,j}(x^2)\bigl(\|Du\|_2^2+x^2\|u\|_2^2\bigr),
\]
where \(G_{N,j}(x^2)=\langle b_j,(L_N+x^2I)^{-1}b_j\rangle\). Equality holds precisely for a multiple of \((L_N+x^2I)^{-1}b_j\). Since
\[
\frac1{\|Du\|_2\|u\|_2}
=\max_{x>0}\frac{2x}{\|Du\|_2^2+x^2\|u\|_2^2},
\]
it follows, by taking suprema over \(u\) and \(x\), that the best point-evaluation constant is \(\max_{x>0}2xG_{N,j}(x^2)\). Both endpoint limits of this continuous function are zero: near \(x=0\), the restricted resolvent is bounded, and near infinity its diagonal is \(O(x^{-2})\).

**2. All evaluation vertices.** Let \(\eta=2\operatorname{arsinh}(x/2)>0\). Direct substitution in the interior recurrence
\[
(x^2+2)v_j-v_{j-1}-v_{j+1}=0
\]
and the endpoint recurrences with diagonal \(1+x^2\) shows that the diagonal of the full resolvent is
\[
R_{N,j}(x^2)=\frac{\cosh((j+\tfrac12)\eta)
\cosh((N-j-\tfrac12)\eta)}
{\sinh\eta\,\sinh(N\eta)}.
\]
The normalization follows from the jump at the source; equivalently it can be checked by a discrete Wronskian. Since \((L_N+x^2I)^{-1}{\bf1}=x^{-2}{\bf1}\), centering gives \(G_{N,j}=R_{N,j}-1/(Nx^2)\). The product in the numerator equals
\[
\tfrac12\{\cosh(N\eta)+\cosh((N-2j-1)\eta)\}.
\]
Its largest value is attained at exactly the two endpoints (which coincide if \(N=2\)). This proves the formula for \(K_N\) and the extremizer description.

**3. Strict increase and universal upper bound.** Put
\[
R_\infty(x^2)=\frac{\sqrt{x^2+4}-x}{2x},\qquad
H_x(z)=\frac1z-\frac{2\sinh\eta}{e^{2z\eta}-1}\quad(z\ge1).
\]
Elementary hyperbolic identities, or geometric-series summation for the reflected Green kernel, yield
\[
G_{N,0}(x^2)=R_\infty(x^2)-\frac{H_x(N)}{x^2}.
\]
Differentiation gives
\[
H_x'(z)=-z^{-2}+\frac{\eta\sinh\eta}{\sinh^2(z\eta)}<0
\]
for every \(z\ge1\), because \(\sinh(z\eta)\ge z\sinh\eta\) and \(\sinh\eta>\eta\). Moreover \(H_x(z)\to0\) from above as \(z\to\infty\). Consequently, at every fixed \(x>0\), \(G_{N,0}\) is strictly increasing in \(N\) and is strictly below \(R_\infty\). Therefore
\[
0<K_N<K_{N+1}\le \sup_{x>0}2xR_\infty(x^2)
=\sup_{x>0}(\sqrt{x^2+4}-x)=2.
\]
The upper bound is strict: \(F_N\) attains its maximum at a positive finite \(x\), where the last inequality is strict.

**4. The boundary asymptotic.** Rewriting the exact expression gives
\[
F_N(x)=\sqrt{x^2+4}-x-\frac2{Nx}
+\frac{4\sinh\eta}{x(e^{2N\eta}-1)}.
\]
Take \(x=\sqrt{2/N}\). Then \(N\eta\asymp\sqrt N\), so the final term is exponentially small, and
\[
K_N\ge2-2\sqrt2\,N^{-1/2}+O(N^{-1}).
\]
In combination with \(K_N<2\), this shows \(K_N\to2\). For any maximizing \(x_N\), the inequality
\[
F_N(x_N)<\sqrt{x_N^2+4}-x_N
\]
forces \(x_N=O(N^{-1/2})\), using the lower bound just established. Furthermore \(N\eta_N\to\infty\): otherwise, on a bounded subsequence \(N\eta_N\to a\ge0\), the exact hyperbolic formula gives the strict limit \(2(\coth a-1/a)<2\), with continuous value zero at \(a=0\), contradicting \(K_N\to2\).

Now \(2N\sinh\eta_N/(e^{2N\eta_N}-1)=o(1)\), so the exact representation in step 3 and the lower bound imply \(x_N=\Omega(N^{-1/2})\). Thus \(x_N\asymp N^{-1/2}\), and the exponential term, together with all fixed-order derivatives, is smaller than every power of \(N^{-1}\) throughout the possible maximizing window. In this window, differentiate the remaining smooth objective:
\[
0=\frac{x_N}{\sqrt{x_N^2+4}}-1+\frac2{Nx_N^2}
+O(N^A e^{-c\sqrt N})
\]
for fixed positive \(A,c\). With \(\varepsilon=N^{-1/2}\), implicit expansion of the derivative around \(x=\sqrt2\,\varepsilon\) gives
\[
x_N=\sqrt2\,\varepsilon+\tfrac12\varepsilon^2
+\frac5{8\sqrt2}\varepsilon^3+O(\varepsilon^4).
\]
The second derivative is \(-\Theta(\sqrt N)\) on this window, proving eventual uniqueness. Substitution into \(\sqrt{x^2+4}-x-2/(Nx)\) yields
\[
K_N=2-2\sqrt2\,\varepsilon+\tfrac12\varepsilon^2
+\tfrac{\sqrt2}{8}\varepsilon^3+O(\varepsilon^4),
\]
which proves the result. The direct two-vertex computation gives \(K_2=1/(2\sqrt2)\).

## Verification

The accompanying `check.py` compares the hyperbolic Green diagonal against both a direct tridiagonal linear solve and an independent discrete-cosine spectral sum for all vertices of \(2\le N\le12\) at four positive parameters. It verifies endpoint dominance, exact constants at small sizes, strict increase on a selection of sizes, and the predicted large-size expansion. These tests are finite corroboration, not substitutes for the all-size argument above. Run `python3 check.py` in a standard Python 3 environment.

## Relationship to prior work

Ilyin, Laptev and Zelik (2014) develop sharp Green-function variational methods for discrete interpolation on the whole lattice, including the sharp one-dimensional bulk coefficient \(1\). Their studied underlying space is \(\mathbb Z^d\), whereas the theorem here concerns mean-zero finite paths with free endpoints; the new constant tends to \(2\), with a square-root length deficit. The half-line Dirichlet point-evaluation problem has a different boundary condition and no finite-path mean-zero constraint. General discrete Green-function formulae provide background but do not by themselves evaluate the nonlinear product-norm optimization or its finite-size expansion.

## Limitations

This result concerns the first-difference quadratic energy and the supremum over vertex values on the *unweighted path*. It does not establish a corresponding law on arbitrary trees, weighted paths, or Dirichlet boundary conditions. The exact formula is a one-variable maximum, not a closed radical for every finite \(N\). The proof establishes uniqueness of the maximizing parameter only for sufficiently large \(N\). Searches cannot exclude an equivalent unpublished or unindexed calculation.

## References

1. A. Ilyin, A. Laptev and S. Zelik, *Sharp interpolation inequalities for discrete operators and applications*, arXiv:1407.0675v1, first public 2014-07-02, especially Sections 1, 2 and 5. https://arxiv.org/html/1407.0675v1
2. A. Beveridge, *A Hitting Time Formula for the Discrete Green's Function*, arXiv:1505.06989v1, first public 2015-05-26. https://arxiv.org/abs/1505.06989
