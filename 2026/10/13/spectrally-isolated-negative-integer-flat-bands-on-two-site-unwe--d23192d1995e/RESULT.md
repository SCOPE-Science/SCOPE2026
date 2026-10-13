# Spectrally isolated negative-integer flat bands on two-site unweighted periodic graphs

## Finding
For every integer \(r\ge 3\), there exists a connected, simple, undirected, unweighted, \((2r^2-r)\)-regular, one-dimensional periodic graph with **exactly two vertices in each fundamental cell** whose adjacency spectrum consists of a unique flat band at \(-r\) and one nonconstant spectral interval **strictly separated** from that flat band. In particular, every negative integer at most \(-3\) can be realized as a spectrally isolated flat band with a compactly supported eigenfunction in this two-site class.

One particularly small exact witness, with \(r=3\), has the full adjacency spectrum
\[
\sigma(A)=\{-3\}\mathbin{\cup}[-1,15].
\]
Thus the spectral isolation gap of this 15-regular graph is **exactly two**; it has only two vertex orbits and admits a flat-band eigenfunction on six vertices. The general all-integer negative-band realization without guaranteed isolation is not claimed here as new; the contribution concerns guaranteed positive separation and the exact explicitly separated example.

## Assumptions and scope
The adjacency operator has all nonzero hopping amplitudes equal to one, with no onsite potential or magnetic phase. Graph vertices are \((A,j)\) and \((B,j)\) for \(j\in\mathbb Z\); every edge is undirected and distinct. The period-one \(\mathbb Z\)-action shifts the cell index. Only the isolated flat band and the nonflat continuum in the specified graph are classified; no universal lower bound on the isolation gap independent of \(r\) is claimed.

For any two finite integer sets \(X,Y\), each of cardinality \(r\), assume both have distinct ordered nonzero differences, all \(r^2\) mixed differences \(x-y\) are distinct, and \(0,1\in X\), \(0\in Y\). Construct edges
\[
(A,j)\sim(A,j+x-x')\ (x\ne x'),\qquad
(B,j)\sim(B,j+y-y')\ (y\ne y'),
\]
and
\[
(A,j)\sim(B,j+x-y)\quad(x\in X,\ y\in Y).
\]
Take each undirected edge only once. Define Laurent polynomials \(P(z)=\sum_{x\in X}z^x\) and \(Q(z)=\sum_{y\in Y}z^y\).

## Proof
**Step 1: The rank-one fiber and graph properties.** Distinct ordered differences give \(r(r-1)\) internal neighbours per layer; distinct mixed differences give \(r^2\) neighbours in the other layer. As both internal difference sets are symmetric and exclude zero, and mixed shifts are distinct, the graph is simple, undirected, loopless and \((2r^2-r)\)-regular. The edge shift \(1\) in the first layer connects all \(A\)-vertices, and the mixed shift \(0\) connects each \(B\)-vertex to an \(A\)-vertex, so it is connected.

The Bloch fiber for \(|z|=1\), using the conventions implied by these edge shifts, is exactly
\[
H(z)=\begin{pmatrix}
P(z)P(z^{-1})-r&P(z)Q(z^{-1})\\
P(z^{-1})Q(z)&Q(z)Q(z^{-1})-r
\end{pmatrix}.
\]
Thus \(H(z)+rI_2\) is the positive-semidefinite rank-one outer product of \((P(z),Q(z))^{\mathsf T}\) with its conjugate transpose. Its two eigenvalues are
\[
\lambda_{\rm flat}(z)=-r,\qquad
\lambda_{\rm disp}(z)=-r+|P(z)|^2+|Q(z)|^2.
\]
The Laurent-polynomial vector \((-Q(z^{-1}),P(z^{-1}))^{\mathsf T}\) lies in the kernel of \(H(z)+rI_2\). Its inverse Fourier transform is a nonzero eigenfunction supported on \(r\) vertices of each layer, hence on exactly \(2r\) vertices. Widely spaced translates are independent, giving infinite multiplicity.

**Step 2: Distinct displacement labels in an infinite family.** Put
\[
X_r=\{0,1,4,4^2,\ldots,4^{r-2}\}.
\]
Every positive difference is either \(4^a\), or \(4^a-4^b\) with \(a>b\ge0\). The first kind has fourth-power valuation \(a\) and unit congruent to \(1\pmod4\); the second has valuation \(b\) and unit congruent to \(3\pmod4\). These invariants distinguish the kinds, and the valuation and remaining magnitude uniquely identify each pair. Therefore all ordered nonzero differences are distinct.

Let \(F_r(z)=\sum_{x\in X_r}z^x\). For a positive integer \(M>\max X_r\), take \(Y_r=M X_r\), \(P=F_r\), \(Q(z)=F_r(z^M)\). Scaling preserves unique differences. If \(x-My=x'-My'\), then \(x-x'=M(y-y')\) with \(|x-x'|<M\), which forces \(x=x'\) and \(y=y'\). Therefore the mixed differences are distinct and the construction in Step 1 applies.

**Step 3: Noncoincident polynomial zeros enforce a genuine spectral gap.** The finite nonzero complex zero set \(Z_r\) of \(F_r\) contains no \(1\), because \(F_r(1)=r\). Let \(L\) be the least common multiple of the orders of all roots of unity in \(Z_r\) (or \(L=1\) if none exist). For every positive multiple \(M\) of \(L\), a root-of-unity zero \(\zeta\) satisfies \(\zeta^M=1\notin Z_r\). For any zero \(\alpha\) which is not a root of unity and any \(\beta\in Z_r\), the equality \(\alpha^M=\beta\) holds for at most one positive integer \(M\), since equality at two exponents would make \(\alpha\) a root of unity. There are finitely many pairs \((\alpha,\beta)\), hence only finitely many forbidden exponents. Consequently every sufficiently large multiple \(M\) of \(L\) produces coprime polynomials \(F_r(z)\) and \(F_r(z^M)\) over \(\mathbb C\), and may be chosen larger than \(\max X_r\).

For any such \(M\), continuity and compactness of the unit circle yield the **strictly positive** number
\[
g_r=\min_{|z|=1}\bigl(|F_r(z)|^2+|F_r(z^M)|^2\bigr)>0.
\]
The dispersive eigenvalue has range \([-r+g_r,\,2r^2-r]\), because the circle is connected and the maximum at \(z=1\) equals \(2r^2-r\). This band is nonconstant: for \(z\ne1\), the distinct monomials \(1,z\) in \(F_r(z)\) ensure \(|F_r(z)|<r\), while \(|F_r(z^M)|\le r\). The spectrum is exactly
\[
\boxed{\sigma(A_r)=\{-r\}\mathbin{\cup}[-r+g_r,\,2r^2-r],\qquad g_r>0.}
\]
The \(-r\) band is therefore isolated, and no other band is flat.

**Step 4: A sharp 15-regular example.** Independently choose \(X=\{0,1,4\}\) and \(Y=\{0,2,7\}\). The positive internal differences are respectively \(\{1,3,4\}\) and \(\{2,5,7\}\), while all mixed differences are distinct:
\[
X-Y=\{-7,-6,-3,-2,-1,0,1,2,4\}.
\]
For \(z=e^{it}\), the nonflat energy is
\[
\lambda_{\rm disp}(t)=3+2\bigl(\cos t+\cos 2t+\cos3t+\cos4t+\cos5t+\cos7t\bigr).
\]
Write \(a=\cos t\), \(b=\cos3t\), \(c=\cos4t\). The product-to-sum identities give the exact sum-of-nonnegative-products certificate
\[
\begin{aligned}
\lambda_{\rm disp}(t)+1
&=4(1+ab+ac+bc)\\
&=2\bigl((1+a)(1+b)(1+c)+(1-a)(1-b)(1-c)\bigr)\ge0.
\end{aligned}
\]
At \(t=\pi\), \((a,b,c)=(-1,-1,1)\) and equality holds; at \(t=0\), the dispersive band reaches \(15\). Its range is exactly \([-1,15]\). The other band stays identically at \(-3\), so their distance is exactly \(2\).

## Verification
The self-contained standard-library Python program `artifacts/verify.py` checks exact displacement multiplicities, Laurent coefficient identities and compact-support eigenstate recurrences for small cell sizes. It computes modular polynomial greatest common divisors for \(r=2,3,4,5\), establishing coprimality for those **particular** displayed choices of \(M\), and independently expands the exact trigonometric certificate for the sharp \(r=3\) example. Run `python3 artifacts/verify.py` from the extracted package. The infinite existence theorem depends on the complex-root argument in Step 3, not on enumeration or floating-point root searches.

## Relationship to prior work
Sabri and Youssef (2023), Section 5, study unweighted adjacency flat bands with two vertices per fundamental cell, including their integrality and the special values \(0,-1,-2\). Their full paper does not assert isolated realization of every integer \(-r\) in a two-site graph. The existence of arbitrary negative-integer flat bands without separation is also not part of the novel claim: the essential new ingredient is a simultaneous-zero avoidance lemma, which forces a **strict** spectral gap; the explicit second construction gives the complete separated spectrum of a concrete 15-regular graph.

Toikka and Andreanov (2018) supply broad criteria for flat bands in finite-range tight-binding lattices, including two-band systems, but their general parameter conditions do not present this unweighted simple-graph all-negative-isolated family or the sharp spectrum of the displayed example. Faust and Liu (2025) prove generic *absence* of flat bands when edge weights and potentials vary; the graphs here have specially constrained unit weights, so generic absence does not exclude them. These comparisons are based on the mathematical statements, not merely matching titles.

## Limitations
For general \(r\), the selected integer \(M\) is existence-based; no optimal hopping range, optimal graph degree, or explicit uniform lower bound for \(g_r\) is claimed. The spectral gap refers to the unperturbed adjacency operator, not preservation of exact flatness under arbitrary perturbations. The numerical and finite symbolic checks do not establish the quantified theorem; the complete argument is in the proof above. Equivalent all-integer *gapped* two-site constructions under different terminology have not been conclusively excluded by finite literature searching.

## References
1. M. Sabri and P. Youssef, *Flat bands of periodic graphs*, arXiv:2304.06465, first available 2023-04-13, https://arxiv.org/abs/2304.06465 (especially Sections 2, 3 and 5).
2. L. A. Toikka and A. Andreanov, *Necessary and sufficient conditions for flat bands in M-dimensional N-band lattices with complex-valued nearest-neighbour hopping*, arXiv:1810.01076, https://arxiv.org/abs/1810.01076.
3. M. Faust and W. Liu, *Rare Flat Bands for Periodic Graph Operators*, arXiv:2503.03632, https://arxiv.org/abs/2503.03632.
4. M. Faust and I. Kachkovskiy, *Absence of flat bands for discrete periodic graph operators with generic potentials*, arXiv:2509.01927, https://arxiv.org/abs/2509.01927.
