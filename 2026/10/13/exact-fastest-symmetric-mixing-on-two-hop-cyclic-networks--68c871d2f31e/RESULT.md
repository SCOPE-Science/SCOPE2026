# Exact fastest symmetric mixing on two-hop cyclic networks

## Finding
For every integer \(n\ge5\), the square \(C_n^2\) of the cycle has vertices \(\mathbb Z/n\mathbb Z\) and undirected edges joining vertices at cyclic distance one or two. Self-loops are permitted. Consider **all** real symmetric, entrywise nonnegative, row-stochastic transition matrices \(P\) supported on this graph and its loops; individual allowed entries need not be equal. Write \(J=\mathbf1\mathbf1^{\mathsf T}/n\). The fastest-mixing objective is the second-largest eigenvalue modulus
\[
\rho(P)=\|P-J\|_2=\max_{2\le k\le n}|\lambda_k(P)|.
\]
Define
\[
\ell=\sin^2\frac{\pi}{n},\quad r=\sin^2\frac{\pi\lfloor n/2\rfloor}{n},\quad
j=\left\lfloor\frac{n+2}{4}\right\rfloor,\quad u=\sin^2\frac{\pi j}{n},
\qquad d=\ell r+u(\ell+r-u).
\]
Then the **unrestricted global optimum** is
\[
\boxed{\min_P\rho(P)=\rho_n^*=\frac{u(\ell+r-u)-\ell r}{u(\ell+r-u)+\ell r}}.
\]
It is attained by the circulant transition matrix
\[
\boxed{P_*=hI+a(S+S^{-1})+b(S^2+S^{-2}),\qquad
a=\frac{\ell+r-1}{2d},\quad b=\frac1{8d},\quad h=1-2a-2b,}
\]
where \(S\) is the one-place cyclic shift. All three probabilities \(a,b,h\) are strictly positive. This is the **unique optimizer among edge-class-uniform circulant walks**; uniqueness is not asserted for every unrestricted (possibly nonuniform) optimal matrix.

For \(n=5\), the support is the complete graph, \(a=b=h=1/5\), and \(\rho_5^*=0\). For \(n=6\), \(a=b=h=1/5\) and \(\rho_6^*=1/5\). For \(n\ge6\) the slowest modes at \(k=1\) and \(k=\lfloor n/2\rfloor\) attain \(+\rho_n^*\), and the mode at \(k=j\) attains \(-\rho_n^*\). Finally,
\[
\boxed{1-\rho_n^*=\frac{8\pi^2}{n^2}+O(n^{-4}).}
\]
This improves the leading-order discrete-time spectral gap by a factor of four compared with the optimally weighted walk using nearest-neighbor edges alone.

## Assumptions and scope
The graph is undirected, \(n\ge5\), and transitions may use a self-loop, either distance-one neighbor, or either distance-two neighbor. Each edge probability is nonnegative, symmetric between its endpoints, and each row sums to one. Self-loop probabilities are allowed to vary across vertices in the unrestricted problem. The performance measure is the operator-norm contraction on the subspace orthogonal to constants, not solely the second-largest eigenvalue or a continuous-time Laplacian gap. No irreducibility or positive-holding assumption is imposed on competitors; the constructed optimizer happens to satisfy both.

## Proof
**1. Reduction without losing globality.** The feasible set is convex. For a symmetric stochastic \(P\), \(\rho(P)=\|P-J\|_2\). If \(Q\) is any dihedral graph automorphism, conjugating by its permutation matrix preserves stochasticity, symmetry, support, and \(\rho\). Averaging the conjugates over the dihedral group does not increase the operator norm. The average has one holding probability \(h\), one probability \(a\) on each distance-one edge, and one probability \(b\) on each distance-two edge. Therefore it is sufficient for the optimum value to minimize over \(a,b\ge0\) with \(2a+2b\le1\); one can then set \(h=1-2a-2b\).

**2. Fourier eigenvalues.** Let \(t_k=\sin^2(\pi k/n)\), for \(1\le k\le m=\lfloor n/2\rfloor\). Fourier diagonalization gives the nonconstant eigenvalues
\[
q_{a,b}(t_k)=1-4a t_k-16b t_k(1-t_k).
\]
The \(t_k\) are strictly increasing, from \(\ell=t_1\) to \(r=t_m\). In particular the minimax objective is \(\max_{1\le k\le m}|q_{a,b}(t_k)|\).

**3. The decisive sampled frequency.** Set \(T=\ell+r\) and \(g(t)=t(T-t)\). Then \(g\) is concave and satisfies \(g(\ell)=g(r)=\ell r\), so \(g(t_k)\ge\ell r\) for all sampled frequencies. Its discrete maximum occurs at \(j=\lfloor(n+2)/4\rfloor\): indeed,
\[
g(t_{k+1})-g(t_k)=(t_{k+1}-t_k)(T-t_k-t_{k+1}),
\qquad t_k+t_{k+1}=1-\cos\frac{(2k+1)\pi}{n}\cos\frac{\pi}{n}.
\]
Thus it suffices to establish \(t_{j-1}+t_j\le T\le t_j+t_{j+1}\), omitting the unavailable left inequality when \(j=1\). To verify every size, put \(\theta=\pi/n\). If \(n\equiv0\pmod4\), \(T=1+\sin^2\theta\), the left sum is less than one, and the right sum is \(1+\sin\theta\cos\theta\ge T\) because \(\theta\le\pi/8\). If \(n\equiv2\pmod4\), the left sum is one, and the right sum is \(1+\sin(2\theta)\cos\theta\ge T\) because \(\sin\theta\le2\cos^2\theta\) for \(n\ge6\). If \(n\) is odd, set \(z=\sin(\theta/2)\). Then \(T=1+z^2(3-4z^2)>1\), and the left sum (when it exists) is less than one. If \(n\equiv1\pmod4\), the right sum is \(1+z\cos\theta\); the required inequality follows from \((1-z)(1-2z-4z^2)\ge0\), since \(z\le\sin(\pi/10)=(\sqrt5-1)/4\). If \(n\equiv3\pmod4\), the right sum is \(1+\sin(3\theta/2)\cos\theta\); the inequality follows from \(z\le\cos\theta\), valid for \(n\ge7\). The only boundary tie is the five-vertex case. Hence \(g(t_k)\le g(u)\) for every \(k\).

**4. Candidate and feasibility.** Put \(d=\ell r+g(u)\). The displayed \(a,b\) give
\[
q_{a,b}(t)=1-\frac{2}{d}g(t).
\]
Since \(\ell r\le g(t_k)\le g(u)\), every nontrivial Fourier eigenvalue lies between \(-\rho_n^*\) and \(+\rho_n^*\), and the endpoints of this interval are attained. Also \(d>0\). For even \(n\), \(T-1=\ell>0\); for odd \(n\), \(T-1=z^2(3-4z^2)>0\). Thus \(a,b>0\). To verify that \(h>0\), note
\[
4dh=4d-4T+3=:H.
\]
For \(n\equiv0,2,1,3\pmod4\), respectively, exact substitution gives
\[
H=2\sin^2\theta,\qquad
H=\sin^2\theta(1+2\sin\theta),\qquad
H=z^2(4z^2-3)(4z^2+2z-3),\qquad
H=z^2(4z^2-3)(4z^2-2z-3).
\]
All four expressions are strictly positive in their allowed size ranges (for odd sizes \(0<z\le\sin(\pi/10)<1/2\)). Therefore the proposed weights are feasible and give the claimed SLEM.

**5. Optimality and orbit-uniform uniqueness.** Suppose \(n\ge6\), so \(\ell<u<r\), and let \(\widetilde q\) be the Fourier polynomial of any other feasible orbit-uniform walk with SLEM at most \(\rho_n^*\). The polynomial \(v=\widetilde q-q_{a,b}\) is of the form \(v(t)=t(A+Bt)\). At the three active modes the signs of \(q_{a,b}\) are respectively \(+,-,+\), which forces
\[
v(\ell)\le0,\qquad v(u)\ge0,\qquad v(r)\le0.
\]
But \(v(t)/t=A+Bt\) is affine. At the strict interior point \(u\) it is a strict convex combination of its values at \(\ell\) and \(r\). Thus all three inequalities can hold only if \(A=B=0\). The candidate is the unique orbit-uniform minimizer. When \(n=5\), the minimum zero is attained and its two distinct sampled Fourier values force the two polynomial coefficients uniquely, again fixing \(a,b\). The group-averaging argument in step 1 proves the **same minimum SLEM globally for all nonuniform competitors**, without asserting all of them are identical.

**6. Large-network comparison.** We have \(\ell=\pi^2/n^2+O(n^{-4})\), \(r=1+O(n^{-2})\), and \(u=1/2+O(n^{-1})\). Consequently \(d=1/4+O(n^{-2})\) and \(1-\rho_n^*=2\ell r/d=8\pi^2/n^2+O(n^{-4})\). If only nearest-neighbor edges are allowed, the optimal orbit-uniform Fourier polynomial is \(1-4at\), with endpoint balancing at \(a=1/[2(\ell+r)]\), a feasible choice because \(T=\ell+r>1\). Its exact SLEM is \((r-\ell)/(r+\ell)\), so the leading gap is \(2\pi^2/n^2\). Dihedral averaging establishes unrestricted optimality for this comparator as well.

## Verification
Run `python3 verify.py` from the directory containing the complete companion script. The checker uses only the Python standard library. It verifies exact rational values for the six-vertex case; compares the formulas against all sampled modes for sizes five through ninety-nine; checks 30,996 alternative feasible orbit-uniform designs; directly reconstructs 3,281 Fourier eigenvector entries; and checks the leading asymptotic law at five larger sizes. It prints

`VERIFY_OK spectra=2446 feasible_grid_comparisons=30996 eigenvector_entries=3281 asymptotic_cases=5`

A separate SciPy linear-programming calculation compared the proposed optimum with all constraints for each \(5\le n\le100\); the largest absolute numerical discrepancy was below \(3\times10^{-16}\). These finite checks do not prove the infinite-size theorem. The proof is the analytic argument above.

## Relationship to prior work
Boyd, Diaconis, and Xiao (2004) introduced the symmetric fastest-mixing Markov-chain/SLEM optimization and its semidefinite formulation, including the option of self-loops. Boyd, Diaconis, Parrilo, and Xiao (2009) established graph-automorphism reduction and gave an explicit one-hop cycle solution. Those general tools motivate the problem, but the inspected derivations do not give the distance-one/distance-two closed-form optimum or the interior negative-eigenmode contact exhibited here. The general SDP can of course solve any fixed finite instance numerically.

Saha and Das (2025) computed the unweighted adjacency and Laplacian spectra for exactly \(C_n^2\); that unweighted spectral information is prior work and is not claimed as new. It does not optimize independently weighted symmetric stochastic transitions or the SLEM. A published degree-two cyclic Carathéodory–Fejér result treats nonnegative sampled trigonometric polynomials with fixed constant coefficient and a maximized first harmonic. Its objective and normalization differ from the three-contact SLEM minimax here; the results cannot be identified by matching polynomial degree alone. A separate previous continuous-time optimization of the same underlying graph maximized only a budgeted Laplacian second eigenvalue, without a discrete-time negative-eigenvalue constraint. That optimization does not imply the present SLEM minimizer.

## Limitations
The result applies to symmetric discrete-time stochastic matrices with uniform stationary distribution and exactly the one-hop/two-hop support. No analogous claim is made for directed, nonsymmetric, prescribed-nonuniform-stationary, or continuous-time chains. The specific orbit-uniform optimizer is unique, but a classification of **all** potentially nonuniform unrestricted optimizers is not asserted. The improvement factor refers to the SLEM spectral gap, not to an exact finite-time total-variation mixing-time ratio. Historical literature may contain an equivalent specialization under a different term; the closest inspected full papers and targeted searches did not establish one. Independent validation is outstanding.

## References
1. S. Boyd, P. Diaconis, and L. Xiao, “Fastest Mixing Markov Chain on a Graph,” *SIAM Review* **46** (2004), 667–689, DOI 10.1137/S0036144503423264; first electronically published 2004-10-29. Full text: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf.
2. S. Boyd, P. Diaconis, P. Parrilo, and L. Xiao, “Fastest Mixing Markov Chain on Graphs with Symmetries,” *SIAM Journal on Optimization* **20** (2009), 792–819, DOI 10.1137/070689413. Full text: https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf.
3. N. Saha and M. Das, “The Square Graph of a Cycle Graph,” *Communications in Mathematics and Applications* **16** (2025), 1107–1117, DOI 10.26713/cma.v16i4.3246. Full text: https://www.rgnpublications.com/journals/index.php/cma/article/download/3246/1927/13255.
4. “Exact degree-two discretized Carathéodory–Fejér extremals on every cyclic grid,” published mathematical record (2026), https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-exact-degree-two-discretized-carath-odory-fej-r-extremals-on-eve--eab032f7bf08.
