# Sharp zero forcing and maximum nullity for long-arm spider powers

## Finding
Let \(m\ge 3\), \(k\ge 3\), and \(\ell\ge k+1\) be integers satisfying \(2(\ell+1)\ge3k\). Let \(T=S_m(\ell)\) be the spider consisting of one center and \(m\) internally disjoint arms, each with \(\ell\) noncentral vertices. Let \(T^k\) join distinct vertices of \(T\) at tree distance at most \(k\). Then
\[
\boxed{Z(T^k)=M(T^k)=(m-1)k.}
\]
Here \(Z\) is the ordinary zero forcing number (a black vertex with exactly one white neighbor forces that neighbor), while \(M\) is the maximum nullity of a real symmetric matrix with **exactly** the off-diagonal zero pattern of the graph. In particular, this settles the predicted equality for all allowed arm lengths when \(k=3\) or \(k=4\), and for the indicated long-arm region at every higher power.

## Assumptions and scope
All graphs are finite, simple and undirected. The distance-power definition includes **all** edges at distances \(1,\ldots,k\), not only edges at distance exactly \(k\). An admissible symmetric matrix must have a nonzero entry at each edge and a zero entry at every nonedge; diagonal entries are unconstrained. The proof works over the real numbers. No assertion is made for the unproved short-arm strip \(k+1\le\ell\) and \(2(\ell+1)<3k\), or for unequal arms. The choice \(m\ge3\) makes the result specifically about branched trees, rather than the path case.

## Proof
**1. The upper bound.** Name the arms \(v_{i,1},\ldots,v_{i,\ell}\), with depths measured from the center \(c\). Initially blacken the last \(k\) vertices of each of the first \(m-1\) arms. This uses \((m-1)k\) vertices. Process each of those arms independently from the outside inward: for \(t=\ell-k,\ell-k-1,\ldots,1\), the black vertex \(v_{i,t+k}\) forces \(v_{i,t}\). Indeed, its distance to any other arm or to the center is greater than \(k\), and all other vertices within distance \(k\) on its own arm are already black. All first \(m-1\) arms are now black. Next \(v_{1,k}\) forces the center. In sequence, for \(j=1,\ldots,k-1\), the vertex \(v_{1,k-j}\) forces \(v_{m,j}\); all its other neighbors are already black. The center forces \(v_{m,k}\), after which for \(t=k+1,\ldots,\ell\) the vertex \(v_{m,t-k}\) forces \(v_{m,t}\). Hence \(Z(T^k)\le(m-1)k\). This explicit sequence also appears as Proposition 9 in the motivating paper [1].

**2. Repeated eigenvalues.** Write \(A\) for the ordinary adjacency matrix of \(T\) and define
\[
\lambda_j=-2\cos\!\left(\frac{j\pi}{\ell+1}\right),\quad 1\le j\le\ell,\qquad
p(x)=\prod_{j=1}^{k}(x-\lambda_j).
\]
For each \(j\), let \(f_j(d)=(-1)^d\sin(jd\pi/(\ell+1))\), for \(d=1,\ldots,\ell\). It satisfies \(f_j(d-1)+f_j(d+1)=\lambda_j f_j(d)\) with zero boundary values at depths \(0\) and \(\ell+1\). For any coefficients \(\alpha_1,\ldots,\alpha_m\) summing to zero, define a vector equal to \(\alpha_i f_j(d)\) on the depth-\(d\) vertex of arm \(i\) and zero at the center. The adjacency equation holds at the center because \(\sum_i\alpha_i=0\), and elsewhere by the path recurrence. Therefore each \(\lambda_j\) is an eigenvalue of \(A\) with multiplicity at least \(m-1\). The \(k\) eigenvalues are distinct, so
\[
\operatorname{null}(p(A))\ge (m-1)k.
\]

**3. A nonnegative factorization.** The condition \(2(\ell+1)\ge3k\) is exactly \(\lambda_k\le1\). Every strictly positive root \(c\) among the first \(k\) roots has \(0<c\le1\) and a distinct negative partner \(-c\) in the same root set: the partner has index \(\ell+1-j<j\). Any zero root contributes one factor \(x\). Every leftover negative root \(-d\) contributes \(x+d\), with \(d>0\). In particular \(\lambda_1\) is an unpaired negative root, because its positive partner has index \(\ell>k\). Thus, with \(q\ge0\), \(z\in\{0,1\}\), and \(a\ge1\),
\[
p(x)=x^z\prod_{h=1}^{q}(x^2-c_h^2)\prod_{i=1}^{a}(x+d_i),
\quad 0<c_h\le1,\ d_i>0,\quad 2q+z+a=k.
\]
The matrix factors \(A\), \(A+d_iI\), and \(A^2-c_h^2I\) are entrywise nonnegative. To see the last claim, off-diagonal entries of \(A^2\) count walks of length two, while its diagonal entries are \(\deg_T(v)\ge1\), so subtracting \(c_h^2\le1\) leaves nonnegative entries. At any nonleaf vertex (degree at least two), these diagonal entries are **strictly** positive. Hence \(p(A)\) is entrywise nonnegative.

**4. Exact support, including all intermediate distances.** Take distinct vertices \(u,v\) at tree distance \(r\), where \(1\le r\le k\). Because \(r\ge z\) and \(a\ge1\), there exist integers \(0\le j\le q\) and \(0\le s\le a\) with
\[
r-z=2j+s.
\]
Indeed, the integer intervals \([2j,2j+a]\), as \(j\) ranges from \(0\) to \(q\), cover all integers from \(0\) to \(2q+a\). Choose a factor ordering (permitted because the factors are polynomials in the same matrix) in which \(j\) of the quadratic factors traverse consecutive length-two segments of the unique \(u\)-to-\(v\) path, \(s\) of the positive-shift linear factors traverse length-one edges, and the \(z\) adjacency factors traverse one edge each. The remaining shifted linear factors act diagonally with strictly positive weight \(d_i\). The remaining quadratic factors act diagonally at a nonleaf endpoint of the path, with weight \(\deg_T(w)-c_h^2>0\). Such an endpoint exists: both endpoints cannot be leaves because two distinct leaves of this spider have distance \(2\ell>k\). Reorder the factors so these idle quadratic steps occur at that nonleaf endpoint and then advance along the path. The matrix product expansion therefore contains a strictly positive contribution to \(p(A)_{uv}\). All other contributions are nonnegative, so \(p(A)_{uv}>0\).

For \(\operatorname{dist}_T(u,v)>k\), every off-diagonal entry of \(A^d\) is zero for \(0\le d\le k\), because no walk of length \(d\) exists. Since \(p\) has degree \(k\), \(p(A)_{uv}=0\). Thus \(p(A)\) has exactly the off-diagonal support of \(T^k\), and belongs to \(\mathcal S(T^k)\).

**5. Conclusion.** By the standard nullity–zero-forcing inequality \(M(G)\le Z(G)\) and the explicit forcing set,
\[
(m-1)k\le \operatorname{null}(p(A))\le M(T^k)\le Z(T^k)\le(m-1)k.
\]
Every inequality is an equality, as claimed. All quantifiers were fixed in advance; no finite-data extrapolation is involved.

## Verification
A standalone Python 3 standard-library program, `verify.py`, constructs the spider and its distance power independently. It numerically forms the stated degree-\(k\) polynomial from the path eigenvalues, checks the required off-diagonal support of \(p(A)\), tests the explicit arm-antisymmetric kernel modes, and performs an independent greedy zero-forcing process. The program tests \(m\in\{3,4,5\}\), \(k\in\{3,\ldots,9\}\), and three allowed lengths for each pair: the smallest eligible \(\ell\), that length plus one, and that length plus three. All 63 finite instances pass. This is corroboration only: the proof of the universal claim is Steps 1–5, not the computed cases.

Run using `python3 verify.py` in the directory containing the file. Expected terminator: `VERIFY_OK`. No external dependencies are required.

## Relationship to prior work
Abiad, Flagg, Ghasemi Nezhad and Zeijlemaker [1] introduced the spider-power equality as Conjecture 10. Their Proposition 9 proves only the matching upper bound; their Theorem 20 provides a general polynomial-eigenvalue multiplicity *conditional* lower-bound method, with a nonvanishing requirement on all shorter-distance edges. The new contribution is the explicit choice of \(k\) path eigenvalues and the **uniform positive-factor certificate** satisfying that missing support condition over the stated infinite parameter range. Thus this is a resolved parameter region, not a purportedly new version of the general spectral method.

DeAlba and collaborators [2] determine minimum rank for ordinary powers of paths and study strict powers of trees. Those results do not supply this exact ordinary-power formula for branched spiders and \(k\ge3\). These are statement-level comparisons; comprehensive priority beyond the inspected literature is not certified.

## Limitations
The proof does **not** resolve the remaining regime \(k+1\le\ell\) and \(2(\ell+1)<3k\), where some paired path eigenvalues have magnitude greater than one and the crucial entrywise nonnegativity argument may fail. The theorem concerns equal-arm spiders and ordinary zero forcing, not irregular-arm spiders, positive semidefinite zero forcing, or arbitrary trees. No independence, external certification, or complete historical priority is claimed.

## References
[1] A. Abiad, M. Flagg, S. Ghasemi Nezhad, S. Zeijlemaker, *The Zero Forcing Number of Graph Powers*, arXiv:2610.03892, first version 2026-10-02, especially Proposition 9, Conjecture 10, Theorem 20. https://arxiv.org/abs/2610.03892

[2] L. M. DeAlba, J. Grout, S. Kirkland, J. J. McDonald, A. Yielding, *Minimum Rank of Powers of Trees*, Electronic Journal of Linear Algebra 23 (2012), 151–163, especially Sections 3 and 4. https://journals.uwyo.edu/index.php/ela/article/download/1023/1023/1023
