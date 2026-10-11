# Exact coordinate constants and unconditionality threshold for retractional bases on comb ultrametrics

## Finding
Let \((a_i)_{i\geq0}\) be any strictly decreasing sequence of positive real numbers. On \(M=\{s_0,s_1,\ldots\}\), choose base point \(s_0\) and distances \(d(s_i,s_j)=a_{\min\{i,j\}}\) for distinct indices. In the real Lipschitz-free space \(\mathcal F(M)\), let
\[
b_j=\delta(s_j)-\delta(s_{j-1})\quad(j\geq1).
\]
This is the monotone basis obtained from the nearest-point retractions onto initial segments. Its exact sign-unconditional and coordinate-suppression constants, interpreted as extended real numbers, are respectively
\[
U=1+\sup_{\ell\geq0}\frac{\sum_{i>\ell}a_i}{a_\ell},\qquad
K=\sup_{\ell\geq0}\frac{\sum_{r\geq0}a_{\ell+2r}}{a_\ell}.
\]
The following three conditions are equivalent: \((b_j)\) is unconditional; \(U<\infty\) (equivalently \(K<\infty\)); and there exist an integer \(N\geq1\) and \(0<q<1\) such that \(a_{\ell+N}\leq q a_\ell\) for every \(\ell\geq0\). In particular, for \(a_i=\rho^i\), \(0<\rho<1\),
\[
U=\frac1{1-\rho},\qquad K=\frac1{1-\rho^2}.
\]
There are also strictly decreasing uniformly positive sequences—for example \(a_i=1+(i+1)^{-1}\)—for which the same monotone basis is conditional.

For the finite comb \(M_n=\{s_0,\ldots,s_n\}\), with strictly decreasing \(a_0,\ldots,a_{n-1}>0\), the exact corresponding constants are
\[
U_n=1+\max_{0\leq\ell<n}\frac{\sum_{i=\ell+1}^{n-1}a_i}{a_\ell},\qquad
K_n=\max_{0\leq\ell<n}\frac{\sum_{r\geq0:\,\ell+2r<n}a_{\ell+2r}}{a_\ell}.
\]

## Assumptions and scope
All spaces and coefficients are real. The free-space norm is the usual Arens–Eells norm, dual to the Lipschitz seminorm of real functions vanishing at \(s_0\). A coordinate projection \(P_S\), for \(S\subseteq\mathbb N\), is initially defined on finite linear combinations by keeping exactly the coefficients indexed by \(S\). The suppression constant is \(\sup_{S\text{ finite}}\|P_S\|\), interpreted as infinity if no uniform bound exists; the sign constant is the supremum of norms of finite-section sign multipliers. When these bounds are finite, the corresponding operators extend continuously as appropriate and the constants equal the usual global unconditional and suppression constants.

The basis is a Schauder basis regardless of unconditionality: for \(r_k(s_j)=s_{\min\{j,k\}}\), every \(r_k\) is a one-Lipschitz retraction and \(r_kr_m=r_{\min\{k,m\}}\). The induced free-space projections are norm one and converge strongly to the identity on the dense span of Dirac vectors. Their successive differences are exactly the basis vectors \(b_j\). The assertion that the nearest-point construction gives these retractions uses strict descent of the distance sequence: for \(j>k\), \(s_k\) is the unique closest point of \(\{s_0,\ldots,s_k\}\) to \(s_j\).

## Proof
**1. Exact finite-dimensional norm.** Fix \(n\geq1\), put \(c_0=0\), and consider \(v=\sum_{j=1}^n c_jb_j\). Build a finite real tree with terminal leaves \(s_0,\ldots,s_n\) all at height zero. The internal nodes at heights \(a_i/2\) for \(0\leq i<n\) form one descending chain, with consecutive vertical edge lengths \((a_i-a_{i+1})/2\); attach \(s_i\), for \(i<n\), to the internal node at height \(a_i/2\), and attach \(s_n\) at height \(a_{n-1}/2\). The resulting leaf distances are exactly those of \(M_n\).

Every edge of this tree carries the unique signed mass flow between its two components. Since a real-valued one-Lipschitz function on the leaves extends one-Lipschitzly to the whole tree, choosing the gradient sign independently on each edge proves that the transportation norm is the sum of edge lengths times absolute flows. Thus
\[
2\|v\|=\sum_{i=0}^{n-1}a_i|c_i-c_{i+1}|+a_{n-1}|c_n|+\sum_{i=0}^{n-2}(a_i-a_{i+1})|c_{i+1}|.\tag{1}
\]
The leaf mass at \(s_i\), for \(i<n\), is \(c_i-c_{i+1}\), and that at \(s_n\) is \(c_n\); the inner-chain flow on the edge from height \(a_i/2\) to height \(a_{i+1}/2\) is \(c_{i+1}\). This also directly verifies every term of (1), including the terminal boundary.

**2. Reduction to molecules.** The unit ball of a finite real Lipschitz-free space is the closed absolutely convex hull of the normalized molecules. Consequently, the norm of any coefficient multiplier equals the maximum of its effect on \((\delta(s_k)-\delta(s_\ell))/a_\ell\) over \(0\leq\ell<k\leq n\). The molecule has basis coefficients equal to one for \(\ell<j\leq k\) and zero otherwise.

**3. Signs.** Applying (1) to basis coefficients \(\sigma_j\in\{-1,1\}\) on one such interval gives
\[
\left\|\sum_{j=\ell+1}^k\sigma_jb_j\right\|=
a_\ell+\sum_{i=\ell+1}^{k-1}a_i\mathbf1_{\{\sigma_i\ne\sigma_{i+1}\}}.\tag{2}
\]
An alternating sign pattern changes sign at every internal edge. Taking the maximum over \(\ell,k\) proves the formula for \(U_n\).

**4. Coordinate suppression.** If the multiplier selects coefficients in a subset of \(\{\ell+1,\ldots,k\}\), split the selected positions into maximal consecutive runs beginning at indices \(u_1<\cdots<u_t\). Formula (1) reduces exactly to
\[
\left\|\sum_{j=\ell+1}^k\mathbf1_{\{j\in S\}}b_j\right\|
=\sum_{h=1}^{t}a_{u_h-1}.\tag{3}
\]
Run starts differ by at least two. As \((a_i)\) decreases, the largest possible total is obtained by runs starting at \(\ell+1,\ell+3,\ldots\), which are realized by alternating singleton selections. Maximization over \(\ell\) gives \(K_n\).

**5. Passage to infinity and threshold.** Molecules supported on initial finite sections are dense in \(\mathcal F(M)\). The finite-section formulas are compatible under the canonical isometric embeddings \(\mathcal F(M_n)\subseteq\mathcal F(M)\), so taking increasing suprema of the finite constants proves the two asserted infinite formulas, without assuming unconditionality in advance.

If \(B=\sup_{\ell}\sum_{i>\ell}a_i/a_\ell<\infty\), monotonicity implies \(Na_{\ell+N}\leq\sum_{i=\ell+1}^{\ell+N}a_i\leq Ba_\ell\); choose an integer \(N>2B\) and \(q=1/2\). Conversely, if \(a_{\ell+N}\leq q a_\ell\) uniformly, partition the tail into blocks of length \(N\) to obtain \(\sum_{i>\ell}a_i\leq (N/(1-q))a_\ell\). Finally, since \((a_i)\) is decreasing, the sum of all tail terms is bounded above by twice the sum over alternate indices. Therefore finiteness of the suppression formula is equivalent to finiteness of the sign formula. The stated examples follow from geometric sums and direct divergence of tail ratios. This completes the proof.

## Verification
The included standalone `verify_ultrametric.py` reconstructs the tree-flow formula with exact rational arithmetic, enumerates all sign multipliers and all coordinate selectors for fifteen distinct finite combs with one through five non-root points, and checks both exact maximum formulas. It additionally compares sixty signed-flow norms against independent finite-dimensional Lipschitz-dual linear programs solved with HiGHS through SciPy. Command: `python verify_ultrametric.py`. Observed output: `COMB_ULTRAMETRIC_VERIFIED cases 15 LP 60`. Python 3.11+ and a HiGHS-enabled SciPy installation are required for the optional LP section. All infinite-dimensional assertions above are proved analytically; finite enumeration alone does not establish them.

## Relationship to prior work
Cúth and Doucha established the monotone retractional-basis construction and \(\ell_1\)-isomorphism for separable ultrametric free spaces. These facts supply the natural basis here, but do not state formulas (2)–(3) or the uniform block-decay equivalence. Godard's tree-metric framework supplies a compatible general method for computing free-space norms, but not the coefficient-selector extremum on this family. Novotný proved general obstructions to unconditional retractional bases in certain metric spaces, including Euclidean nets; that does not settle this class of ultrametrics or its positive regime. Albiac, Ansorena, Cúth and Doucha studied related bases for different metric families and free \(p\)-spaces. The present assertion is specifically about the canonical nearest-predecessor basis, **not** whether the underlying free space has some other unconditional basis.

## Limitations
The exact formulas concern one prescribed enumeration and its retractional basis on strictly decreasing comb ultrametrics; they do not classify all retractional bases on arbitrary ultrametrics. The finite statements require \(n\geq1\), and all constants are for real scalars. The limit metric may be incomplete when \(a_i\to0\), but passing to its metric completion does not change the free space generated by the dense original points. The proof does not claim an unconditional-basis obstruction for the space itself, which remains isomorphic to \(\ell_1\) by established work. Earlier equivalent formulations of this exact selector problem may exist.

## References
- M. Cúth and M. Doucha, *Lipschitz-free spaces over ultrametric spaces*, arXiv:1411.2434 (public 10 November 2014), especially Section 1, Lemma 6, Theorems 1–2.
- A. Godard, *Tree metrics and their Lipschitz-free spaces*, arXiv:0904.3178 (public 21 April 2009), especially Section 3.
- M. Novotný, *Some Remarks on Schauder Bases in Lipschitz Free Spaces*, arXiv:1905.13188 (public 30 May 2019), especially Section 4.
- F. Albiac, J. L. Ansorena, M. Cúth and M. Doucha, *Embeddability of \(\ell_p\) and bases in Lipschitz free \(p\)-spaces for \(0<p\leq1\)*, arXiv:1905.07201 (public 17 May 2019), especially Section 5.
