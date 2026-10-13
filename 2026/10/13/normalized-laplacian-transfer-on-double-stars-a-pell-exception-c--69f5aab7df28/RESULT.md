# Normalized-Laplacian transfer on double stars: a Pell-exception classification

## Finding

Let \(D_{p,q}\), for integers \(p,q\ge1\), be the tree with two adjacent hubs, the first incident to \(p\) pendant leaves and the second to \(q\) pendant leaves. Define
\[
\mathcal E=\bigl\{q\ge1:q(q+1)=6h^2\text{ for some integer }h\ge1\bigr\}.
\]
Then the normalized-Laplacian quantum walk admits **pretty good state transfer (PGST)** between distinct vertices if and only if
\[
(p=2\text{ and }q\notin\mathcal E)\quad\text{or}\quad(q=2\text{ and }p\notin\mathcal E).
\]
Every transferring pair is exactly the two pendant leaves adjacent to a hub carrying two leaves. **No double star with \(p,q\ge1\) admits perfect state transfer (PST)** between distinct vertices. The exceptional set is infinite:
\[
\mathcal E=\{2,24,242,2400,23762,\ldots\},\qquad
q_r=\frac{(5+\sqrt{24})^r+(5-\sqrt{24})^r-2}{4},\quad r\ge1.
\]
Consequently the double-star family supplies a complete diameter-three-tree resolution of the qualitative PST obstruction, and a sharper PGST distinction with infinitely many arithmetic exceptions.

## Assumptions and scope

All graphs are finite, simple, connected, undirected and unweighted. Write \(A\) for adjacency, \(D\) for diagonal degrees, and
\[
H=I-D^{-1/2}AD^{-1/2},\qquad U(t)=e^{-itH}.
\]
PST between distinct vertices \(a,b\) requires \(|U(t)_{ba}|=1\) at some finite \(t>0\). PGST means there exist positive \(t_j\to\infty\) with \(|U(t_j)_{ba}|\to1\). The theorem concerns this normalized Laplacian, **not** the combinatorial Laplacian or the unnormalized adjacency Hamiltonian. No assertion is made about trees beyond the diameter-three double-star family or about rates of convergence.

## Proof

**1. Spectrum and leaf-difference subspaces.** Set \(B=I-H=D^{-1/2}AD^{-1/2}\). On the four-dimensional subspace consisting of vectors constant on each pendant-leaf group, use the orthonormal ordered basis given by the normalized first-leaf sum, first hub, second hub and normalized second-leaf sum. Its matrix is the real Jacobi matrix
\[
Q=\begin{pmatrix}
0&\sqrt{p/(p+1)}&0&0\\
\sqrt{p/(p+1)}&0&1/\sqrt{(p+1)(q+1)}&0\\
0&1/\sqrt{(p+1)(q+1)}&0&\sqrt{q/(q+1)}\\
0&0&\sqrt{q/(q+1)}&0
\end{pmatrix}.
\]
Its characteristic polynomial factors exactly as
\[
\det(xI-Q)=(x^2-1)\left(x^2-\frac{pq}{(p+1)(q+1)}\right).
\]
Define \(c=\sqrt{pq/((p+1)(q+1))}\in(0,1)\). The remaining \(p+q-2\) eigenvectors are leaf differences (whose coordinates sum to zero within one leaf group) with \(B\)-eigenvalue zero, equivalently \(H\)-eigenvalue one. Thus the four simple quotient eigenvalues of \(H\) are \(0,1-c,1+c,2\), all distinct from one. The first and last coordinates of every quotient eigenvector are nonzero: in the irreducible tridiagonal matrix \(Q\), a zero endpoint coordinate forces all coordinates to vanish by propagation along nonzero off-diagonal entries. The same propagation, using that the four eigenvalues of \(Q\) are nonzero, shows both hub coordinates are nonzero.

**2. Restrictions on transfer pairs.** The normalized Laplacian has the unique positive eigenvector \(D^{1/2}{\bf1}\) at eigenvalue zero. Hence unit-fidelity transfer, or a convergent PGST sequence, has global phase tending to \(+1\), and the two vertices must have the same degree. In addition, for each spectral projection \(E_\lambda\), PGST forces \(E_\lambda e_a=\pm E_\lambda e_b\), because the limiting unimodular eigenphases must map the spectral projections of the two coordinate vectors exactly.

A pendant leaf cannot transfer to either hub, whose degree is at least two. Two leaves attached to different hubs cannot be strongly cospectral when either hub has at least two leaves: their projections into the \(B\)-zero leaf-difference subspace have disjoint supports and unequal nonzero vectors (or one zero and one nonzero). Two distinct leaves at the same hub with \(p\) leaves can be strongly cospectral only if \(p=2\): their orthogonal projections onto that leaf-difference space are \(e_a-p^{-1}\sum_{i\text{ in group}}e_i\) and \(e_b-p^{-1}\sum_{i\text{ in group}}e_i\); these are neither identical nor negatives unless \(p=2\). Two hubs have equal degree only when \(p=q\). When \(p=q=1\), both pairs of equal-degree vertices are interchanged by graph reflection, and are handled in the next paragraph. These exhaust all distinct-vertex pairs.

**3. The balanced-hub and four-path obstruction.** Suppose \(p=q=r\ge1\). Reflection interchanging the hubs sends the eigenvectors of \(H\)-eigenvalue zero to themselves, and reverses those of \(H\)-eigenvalues \(1-c=1/(r+1)\) and two; all these projections are nonzero at either hub. PGST between hubs would therefore require simultaneously
\[
e^{-it_j/(r+1)}\longrightarrow-1,\qquad e^{-2it_j}\longrightarrow-1.
\]
But the second phase is the \(2(r+1)\)-st power of the first, which would converge to \(+1\). Contradiction. For \(r=1\), the graph is the four-vertex path. The two pendant endpoints likewise have opposite reflection parity at eigenvalues \(1/2\) and two, so the same contradiction excludes their transfer. This disposes of every possible hub or cross-side transfer; the sole remaining candidates are sibling leaves at a hub of size two.

**4. Necessary and sufficient phases for a size-two sibling pair.** By symmetry take \(p=2\), and let \(a,b\) be its leaves. Their antisymmetric vector \((e_a-e_b)/\sqrt2\) has \(H\)-eigenvalue one; their symmetric vector \((e_a+e_b)/\sqrt2\) has nonzero projections onto each of the four quotient eigenspaces, where the two leaves project identically. Since the phase at eigenvalue zero is \(+1\), the exact necessary and sufficient PGST phase conditions are
\[
e^{-it_j}\to-1,\quad e^{-2it_j}\to+1,\quad
 e^{-it_j(1-c)}\to+1,\quad e^{-it_j(1+c)}\to+1,
\quad c=\sqrt{\frac{2q}{3(q+1)}}.
\]
Equivalently one must approximate odd multiples of \(\pi\) simultaneously in \(t\) and \(tc\), modulo \(2\pi\). If \(c\) is irrational, choose \(t_j=(2k_j+1)\pi\), with \(k_j\to\infty\), and use density of the irrational circle rotation \((2k+1)c\bmod2\) to obtain \(e^{it_jc}\to-1\). This proves PGST. Exact PST at finite time would require \(t\) and \(tc\) both odd multiples of \(\pi\), forcing \(c\) rational.

**5. Rational phases and the Pell exceptions.** Suppose \(c\) is rational. Then \(6q(q+1)\) is a perfect square, say \(k^2\); since six divides \(k^2\), six divides \(k\), say \(k=6h\). Therefore \(q(q+1)=6h^2\), and conversely this equation gives \(c=2h/(q+1)\) rational. Equivalently, setting \(X=2q+1\) yields the positive Pell equation \(X^2-24h^2=1\). The elementary Pell-unit description (fundamental solution \(5+\sqrt{24}\)) gives \(X+h\sqrt{24}=(5+\sqrt{24})^r\) for \(r\ge1\), hence exactly the displayed exceptional set. Its members are even: the sequence \(X_r\) obeys \(X_0=1\), \(X_1=5\), \(X_{r+1}=10X_r-X_{r-1}\), so \(X_r\equiv1\pmod4\) and \(q_r=(X_r-1)/2\) is even. Consequently \(c=2h/(q+1)\), in lowest terms, has **even numerator and odd denominator**, whereas exact or limiting odd/odd phase matching would require a rational \(c\) with **both numerator and denominator odd**. More explicitly, any sequence with \(e^{-it_j}\to-1\) and \(e^{-it_jc}\to-1\), for reduced \(c=a/b\), would imply by taking integer powers \(e^{-it_ja}\to(-1)^a\) and also \(e^{-it_jc b}\to(-1)^b\); these are the same phase, forcing \((-1)^a=(-1)^b\). The even/odd parity contradiction excludes PGST for every \(q\in\mathcal E\). It also excludes PST in the rational case; the irrational case has no PST as already shown. Interchanging \(p,q\) completes the proof. \(\square\)

## Verification

Run `python3 verify.py` with NumPy installed for the full independent finite replay. It checks 400 exact-rational Jacobi characteristic polynomials, 100 numerical normalized-Laplacian spectra, all Pell exceptions through parameter 100000, parity obstructions for the first three exceptions, and explicit high-fidelity time witnesses for five nonexceptional parameters. The checks are finite and do not substitute for the all-parameter proof above. The verifier reports `VERIFY_OK` or raises an assertion on discrepancy.

## Relationship to prior work

Coutinho and Baptista (arXiv:2209.04668v1, 2022, Sections 3–5) establish general normalized-Laplacian PST criteria, exclude several classes of trees and conjecture that no nontrivial tree other than the two- and three-vertex paths admits PST; their paper does not classify double-star PGST or its Pell exceptional set. Kirkland, Monterde and Plosker (arXiv:2201.02720, Sections 2, 5, 6) establish general weighted-graph twin transfer conditions, which also apply to normalized adjacency regarded as weighted adjacency, but do not give the double-star normalized-Laplacian parameter classification. Fan and Godsil (arXiv:1206.0082) analyze adjacency-Hamiltonian PGST on double stars, a different operator. The present contribution is the **explicit exhaustive normalized-Laplacian transfer classification on this infinite natural family**, including the infinite exceptional Pell sequence and the parameter-uniform no-PST result, not the general spectral definitions or approximation theorem.

## Limitations

Only simple unweighted double stars with positive leaf counts are covered. This does not resolve normalized-Laplacian PST on all trees, quantify minimal transfer times or establish novelty beyond the primary-literature comparison. The general weighted-twin transfer criteria provide overlapping machinery, so an explicit earlier application to this exact operator and family under different terminology remains a residual originality risk. The computer checks only finitely many instances. Independent external validation has not been performed.

## References

- G. Coutinho and P. F. Baptista, *Quantum Walks in the Normalized Laplacian*, arXiv:2209.04668v1 (first public 2022-09-10); primary MSC 81P68.
- S. Kirkland, H. Monterde and S. Plosker, *Quantum state transfer between twins in weighted graphs*, arXiv:2201.02720 (first public 2022-01-08).
- C. Fan and C. Godsil, *Pretty good state transfer on double stars*, arXiv:1206.0082 (2012).
- H. Alvir et al., *Perfect State Transfer in Laplacian Quantum Walk*, arXiv:1409.5840 (2014).
