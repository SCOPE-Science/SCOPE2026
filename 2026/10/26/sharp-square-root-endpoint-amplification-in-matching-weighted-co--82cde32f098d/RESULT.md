# Sharp square-root endpoint amplification in matching-weighted complete bipartite graphs

## Finding
For each integer \(n\ge3\), give the \(n\) matching edges of \(K_{n,n}\) conductance \(x^2>0\) and every other edge unit conductance. Write \(Q_{n,x}\) for the Euclidean-orthogonal cut projection in square-root-conductance edge coordinates and \(P_{n,x}=I-Q_{n,x}\) for its cycle complement. Set
\[
 d=n-1+x^2,\qquad h=n-2+2x^2,\qquad U=\frac{2d^2-n}{ndh},\qquad W=\frac{2d(1-x^2)-n}{ndh}.
\]
Define four explicit nonnegative column sums
\[
\begin{aligned}
 C_D&=\frac{x^2(2d+n-2)+x(n-1)(2d+n-4)}{dh},\\
 C_O&=\frac{x(2d+n-4)}{dh}+U+|W|+\frac{2(n-2)}n+\frac{(n-2)(n-3)}{dh},\\
 Z_D&=1+C_D-\frac{2x^2(2d-1)}{dh},\\
 Z_O&=1+C_O-2U.
\end{aligned}
\]
Then the **exact induced real endpoint operator norms**, for every \(n\ge3\) and every \(x>0\), are
\[
\|Q_{n,x}\|_{1\to1}=\|Q_{n,x}\|_{\infty\to\infty}=\max\{C_D,C_O\},
\qquad
\|P_{n,x}\|_{1\to1}=\|P_{n,x}\|_{\infty\to\infty}=\max\{Z_D,Z_O\}.
\]
The symbols \(D,O\) designate matching and nonmatching source-edge classes, respectively. In particular, the sign-sensitive term \(W\) reverses precisely when \(2d(1-x^2)=n\).

There is a sharp common square-root amplification law when the positive matching conductance is optimized independently for each size. Let \(\alpha_*\) be the unique positive root of \(4\alpha^3+12\alpha^2+3\alpha-3=0\) and set
\[
 \kappa=\frac{\sqrt{\alpha_*}(3+2\alpha_*)}{(1+\alpha_*)(1+2\alpha_*)}=0.9543494948\ldots.
\]
Then
\[
\boxed{\lim_{n\to\infty}\frac{1}{\sqrt n}\sup_{x>0}\|Q_{n,x}\|_{1\to1}
=\lim_{n\to\infty}\frac{1}{\sqrt n}\sup_{x>0}\|P_{n,x}\|_{1\to1}=\kappa.}
\]
Already \(x^2=\alpha_* n\) realizes \(\kappa\sqrt n+O(1)\) for each projection. By contrast at uniform conductance \(x=1\), the exact norms are \(3-4/n+2/n^2\) and \(4-8/n+4/n^2\), respectively.

## Assumptions and scope
Let \(A_1,\ldots,A_n\) and \(B_1,\ldots,B_n\) be the parts. Orient every edge \((A_i,B_j)\) from the first to second part; its conductance is \(c_{ij}=x^2\) if \(i=j\), otherwise \(1\). Let \(B\) be the vertex-edge incidence matrix with columns \(e_{A_i}-e_{B_j}\), and let \(C=\operatorname{diag}(c_{ij})\). With \(L=BCB^T\) and Moore–Penrose inverse \(L^+\), define \(Q=C^{1/2}B^TL^+BC^{1/2}\), \(P=I-Q\). These are self-adjoint idempotents on the real Euclidean edge space, and the graph is connected for all specified parameters. Norms are induced by the standard edge-coordinate \(\ell_1\) and \(\ell_\infty\) norms; they are not minimum norms over arbitrary projections.

## Proof
**Laplacian decomposition.** Put \(t=x^2\), \(d=n-1+t\), \(h=n-2+2t\). The vertex Laplacian in the \(A/B\) ordering is
\[
 L=\begin{pmatrix}dI&-J-(t-1)I\\-J-(t-1)I&dI\end{pmatrix}.
\]
Its mutually orthogonal invariant spaces are the constant vectors (eigenvalue zero), the vectors constant with opposite signs on the parts (eigenvalue \(2d\)), the two equal mean-zero coordinate blocks (eigenvalue \(n\)), and the two opposite mean-zero blocks (eigenvalue \(h\)). Hence all nonzero inverse eigenvalues are \(1/(2d)\), \(1/n\), and \(1/h\); no singular denominators occur for \(n\ge3\), \(t>0\).

**Transfer-current entries.** For a source edge \((A_i,B_j)\), denote the voltage drop on target edge \((A_k,B_l)\) under a unit unsymmetrized current by \(V_{ij}(k,l)=(e_{A_k}-e_{B_l})^TL^+(e_{A_i}-e_{B_j})\). Direct substitution into the preceding eigenspace decomposition gives, if \(i=j\),
\[
 V_{ii}(k,l)=-\frac1{dh}+\frac{\mathbf 1_{k=i}+\mathbf1_{l=i}}h,
\]
and if \(i\ne j\),
\[
 V_{ij}(k,l)=-\frac1{dh}
 +\frac{d}{nh}(\mathbf1_{k=i}+\mathbf1_{l=j})
 +\frac{1-t}{nh}(\mathbf1_{k=j}+\mathbf1_{l=i}).
\]
These are exact identities for every target edge. The orthogonal projection entry is \(Q_{(k,l),(i,j)}=\sqrt{c_{kl}c_{ij}}V_{ij}(k,l)\).

**Matching-edge source.** For \(i=j\), the own voltage drop is \((2d-1)/(dh)>0\); drops along the \(2(n-1)\) incident nonmatching edges are \((d-1)/(dh)>0\); the other \(n-1\) matching and \((n-1)(n-2)\) nonmatching drops are \(-1/(dh)<0\). Multiply by the respective conductance-square-root products \(t\) or \(x\), then sum absolute values. This gives exactly \(C_D\). The own diagonal is \(Q_{ee}=t(2d-1)/(dh)\), so the corresponding \(P\) column sum is \(1+C_D-2Q_{ee}=Z_D\).

**Nonmatching-edge source.** For \(i\ne j\), the own voltage is \(U=(2d^2-n)/(ndh)>0\), and the reverse edge \((A_j,B_i)\) has voltage \(W=(2d(1-t)-n)/(ndh)\). Each of the two other incident-edge classes with \(n-2\) members has voltage \(A=(d^2-n)/(ndh)>0\) or \(B_0=(d(1-t)-n)/(ndh)<0\), respectively. These inequalities follow from \(d>n-1\ge2\), \((n-1)^2>n\) and \(d(1-t)<n\) for every \(n\ge3,t>0\). Moreover \(A-B_0=1/n\). The \((n-2)(n-3)\) remaining nonmatching edges carry voltage \(-1/(dh)\). The two incident matching edges carry \((d-1)/(dh)>0\), while the \(n-2\) other matching edges carry \(-1/(dh)\). Multiplying by \(x\) for each matching target and grouping all signs gives \(C_O\). The own diagonal is \(Q_{ee}=U\), giving \(Z_O\). The two edge classes exhaust all columns, so the maximum of their absolute sums is the \(\ell_1\)-operator norm. Since both projections are real symmetric, their \(\ell_\infty\) operator norms coincide with their \(\ell_1\) norms.

**Sharp optimized asymptotics.** All nonmatching columns are uniformly bounded independently of \(n\ge3\) and \(x>0\). Indeed \(0\le U\le1\) and \(|W|\le1\) because \(Q\) is an orthogonal projection and its diagonal entries do not exceed one; the first term in \(C_O\) is bounded by \(3x/h\le3/(2\sqrt{2(n-2)})\); and the final two terms are at most \(2\) and \(1\). Thus \(C_O\le6+3/(2\sqrt2)\). For \(C_D\) the first term is at most \(3t/h\le3/2\), while its second term, upon setting \(t=n\alpha\), equals \(\sqrt n F_n(\alpha)\), with
\[
 F_n(\alpha)=\frac{\sqrt\alpha(1-1/n)(3-6/n+2\alpha)}{(1-1/n+\alpha)(1-2/n+2\alpha)}.
\]
For \(n\ge4\), these continuous functions converge uniformly on \([0,\infty)\) to
\[
 F(\alpha)=\frac{\sqrt\alpha(3+2\alpha)}{(1+\alpha)(1+2\alpha)}.
\]
To verify uniformity directly, use locally uniform convergence on every compact interval and the bounds \(F_n(\alpha)=O(\sqrt\alpha)\) as \(\alpha\downarrow0\) and \(F_n(\alpha)=O(\alpha^{-1/2})\) as \(\alpha\to\infty\), with constants uniform for \(n\ge4\). The derivative has the sign of \(-4\alpha^3-12\alpha^2-3\alpha+3\), so \(F\) has exactly one positive maximizer \(\alpha_*\). This proves \(\sup_x\|Q_{n,x}\|/\sqrt n\to\kappa\). For every column, \(\sum_f|P_{fe}|=1+\sum_f|Q_{fe}|-2Q_{ee}\) with \(0\le Q_{ee}\le1\); hence \(|\|P\|_{1\to1}-\|Q\|_{1\to1}|\le1\), establishing the identical normalized limit and the assertion for \(x^2=\alpha_*n\). At \(x=1\), edge transitivity (or the formulas above) yields the two stated constant-order expressions. \(\square\)

## Verification
The included `matching_biclique_checker.py` uses exact rational arithmetic, independently builds a grounded weighted vertex Laplacian, solves the linear system for **every** source edge, and compares every absolute cut/cycle projection column sum against the four analytical formulas. It checks \(24\) weighted graph configurations for \(n=3,4,5,6\) and \(x=1/4,1/2,1,3/2,2,4\), totaling \(516\) columns. It also checks the orthogonal projection diagonal identity \(\sum_f Q_{fe}^2=Q_{ee}\). The execution output is `MATCHED_BICLIQUE_EXACT_OK graphs=24 columns=516`. Finite checks support, but do not replace, the general proof. The asymptotic stationary cubic has one positive root by strict monotonicity of that cubic on \([0,\infty)\).

## Relationship to prior work
Dilworth, Kutzarova and Ostrovskii (2023, arXiv:2305.12582), study invariant and minimal cycle-space projections, primarily for discrete tori and Hamming graphs, with the same broad Banach-space motivation. Their work does not state this all-parameter matching-weighted biclique transfer-current norm classification or the optimized square-root law. Their 2018 paper (arXiv:1807.03814) treats graph Lipschitz-free spaces, particularly recursively defined diamond and Laakso families, rather than this electrical projection family. Gurel-Gurevich, Nachmias and Sachdeva (2026, arXiv:2605.24130) bound the spectral operator norm of the entrywise absolute weighted transfer-current matrix; that norm is not the largest absolute column sum studied here. In particular its logarithmic bound cannot imply a logarithmic bound on the present \(\ell_1\) norm. Standard spectral Laplacian inversion is an ingredient, not claimed original.

## Limitations
The graph family is balanced complete bipartite with positive matching conductances constant on the matching and unit conductances elsewhere. The projections are the canonical Euclidean-orthogonal operators in square-root-conductance coordinates. This does not characterize minimum projection norms among all projections, all weighted graphs, or intermediate \(\ell_p\) norms. The formula covers every finite positive \(x\), whereas the scaling limit concerns optimization over \(x\) as \(n\to\infty\). The originality comparison cannot exclude uncatalogued equivalent electrical-network calculations.

## References
1. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Cycle spaces: invariant projections and applications to transportation cost*, arXiv:2305.12582 (first public 2023-05-21).
2. S. J. Dilworth, D. Kutzarova and M. I. Ostrovskii, *Lipschitz free spaces on finite metric spaces*, arXiv:1807.03814 (first public 2018-07-10).
3. O. Gurel-Gurevich, A. Nachmias and S. Sachdeva, *A Tight Bound on Localization of Electrical Flows*, arXiv:2605.24130 (2026).
