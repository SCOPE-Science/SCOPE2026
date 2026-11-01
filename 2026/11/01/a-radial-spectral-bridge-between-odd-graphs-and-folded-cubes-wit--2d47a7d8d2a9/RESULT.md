# A radial spectral bridge between odd graphs and folded cubes, with a shared sharp negative-type exponent

## Finding
Let \(k\ge2\) be an integer. The odd graph \(O_{k+1}=KG(2k+1,k)\) has as vertices the \(k\)-subsets of \([2k+1]\), with disjoint subsets adjacent. The folded cube \(F_{2k+1}\) has vertices \(\mathbb F_2^{2k+1}/\langle\mathbf1\rangle\), with adjacency induced by changing one binary coordinate. Both carry their shortest-path distances. For any function \(\phi:\{0,1,\ldots,k\}\to\mathbb R\) with \(\phi(0)=0\), write \(M^G_\phi=(\phi(d_G(u,v)))_{u,v\in V(G)}\).

**Universal radial spectral bridge.** For every such \(k\) and \(\phi\), one eigenvalue of \(M^{O_{k+1}}_\phi\) on the top Johnson harmonic sector equals an eigenvalue of \(M^{F_{2k+1}}_\phi\) on the Walsh sector of even weight \(j=k\) when \(k\) is even, and \(j=k+1\) when \(k\) is odd. Their common eigenvalue is
\[
\Lambda_k(\phi)=\sum_{t=1}^k [z^t]\bigl((1+(-1)^kz)(1-z^2)^k\bigr)\,\phi(t).
\]
The two designated multiplicities are respectively \(\binom{2k+1}{k}-\binom{2k+1}{k-1}\) and \(\binom{2k+1}{k}\). The equality is of eigenvalues, not entire spectra.

**Shared sharp threshold.** Specializing to \(k=3\), let \(\alpha\) be the unique positive real satisfying
\[
3(3^\alpha-2^\alpha)=1,\qquad 0<\alpha<\frac23
\]
(approximately \(0.516584374300590\)). For both the \(35\)-vertex graph \(O_4=KG(7,3)\) and the \(64\)-vertex folded cube \(F_7\), the powered distance \(d^p\) is conditionally negative definite **if and only if** \(0\le p\le\alpha\). At \(p=\alpha\), the minimum dimensions of Euclidean realizations with squared distances \(d^\alpha\) are respectively \(20\) and \(28\). Equivalently, \(\exp(-s d^p)\) is a positive-semidefinite kernel for every \(s>0\) exactly when \(0\le p\le\alpha\).

## Assumptions and scope
The graphs are finite, simple, unweighted, and carry **vertex** shortest-path metrics; no metric-graph edge interiors are included. For \(p=0\), set \(d^0(u,v)=0\) on the diagonal and \(1\) off the diagonal. Conditional negative definiteness means \(\sum_{u,v}c_uc_vd(u,v)^p\le0\) for every real coefficient vector satisfying \(\sum_uc_u=0\). The universal bridge applies to arbitrary real radial profiles; only its \(k=3\) corollary asserts equality of sharp negative-type exponents. It does **not** imply equal thresholds for all \(k\).

## Proof
**1. The odd-graph top harmonic.** Put \(n=2k+1\), and for \(0\le i\le k\), let \(A_i\) be the Johnson relation matrix joining \(k\)-sets with intersection size \(k-i\). The standard Johnson-scheme eigenvalue formula (also recorded in Aalipour et al., Theorem 3.9) on harmonic level \(s\) is
\[
P_i(s)=\sum_{h=0}^{s}(-1)^h\binom{s}{h}\binom{k-s}{i-h}\binom{k+1-s}{i-h}.
\]
At \(s=k\), only \(h=i\) survives, giving \(P_i(k)=(-1)^i\binom{k}{i}\). The level's multiplicity is \(\binom{2k+1}{k}-\binom{2k+1}{k-1}\), by the rank of the nested subset-incidence matrices. The odd-graph distance formula is
\[
d_{O_{k+1}}(S,T)=\min\{2(k-|S\cap T|),\;2|S\cap T|+1\}.
\]
Thus the relation at even distance \(t=2r\le k\) is \(A_r\), and the relation at odd distance \(t=2r+1\le k\) is \(A_{k-r}\). Their top-harmonic coefficients are respectively \((-1)^r\binom{k}{r}\) and \((-1)^{k-r}\binom{k}{r}\).

**2. The folded-cube Walsh harmonic.** On \(\mathbb F_2^n\), characters indexed by even-cardinality \(J\subseteq[n]\) descend to the antipodal quotient. The characters of a fixed weight \(j=|J|\) form an eigenspace of dimension \(\binom nj\) for every radial matrix. The coefficient of distance \(t\), for \(1\le t\le k\), on such a character is the \(t\)-th coefficient of
\[
(1-z)^j(1+z)^{n-j}.
\]
This follows directly by summing \((-1)^{|J\cap S|}\) over the \(t\)-subsets \(S\), with one representative from each antipodal class. Choose the even integer \(j=k+(k\bmod2)\). If \(k\) is even the generating polynomial is \((1+z)(1-z^2)^k\); if \(k\) is odd it is \((1-z)(1-z^2)^k\). The coefficients at \(2r\) and \(2r+1\) are exactly those from step 1. This proves the universal identity, for each independent value \(\phi(t)\) rather than merely for powered distances.

**3. All centered eigenvalues when \(k=3\).** Put \(a=2^p\), \(b=3^p\). On \(\mathbf1^\perp\), the odd graph \(O_4\) has three eigenvalues with multiplicities:
\[
5a-3b-3\quad[6],\qquad 2-3b\quad[14],\qquad 3b-3a-1\quad[14].
\]
The folded cube \(F_7\) has
\[
3+a-5b\quad[21],\qquad 3b-3a-1\quad[35],\qquad 9a-5b-5\quad[7].
\]
The odd-graph entries follow by inserting the \(k=3\) Johnson eigenvalues \(P_i(s)\) into its three distance shells. The folded entries follow from even-weight Walsh characters of weights \(2,4,6\). The row-sum eigenvalues (excluded from the centered subspace) are \(4+12a+18b\) and \(7+21a+35b\), respectively. The displayed multiplicities sum to \(34\) and \(63\), so no sector is omitted.

**4. The first and only negative-type obstruction.** Define \(g(p)=3(3^p-2^p)-1\). This function is strictly increasing for \(p\ge0\), because \(3^p\log3>2^p\log2\); it satisfies \(g(0)=-1\). Moreover, \(3^{2/3}>2\) and \(2^{2/3}<5/3\), whence \(g(2/3)>0\). Therefore \(g\) has exactly one positive root \(\alpha<2/3\).

For \(p\ge0\), the elementary inequality
\[
 b\ge\tfrac32 a-\tfrac12
\]
holds: the difference is zero at \(p=0\) and has positive derivative since \(\log3>\tfrac32\log2\). For \(0\le p\le\alpha\), \(a<5/3\) and \(b\ge a\), so
\[
5a-3b-3\le\tfrac12a-\tfrac32<0,\qquad 2-3b<0,
\]
\[
3+a-5b\le3-4a<0,\qquad 9a-5b-5\le\tfrac32a-\tfrac52<0.
\]
The sole remaining centered eigenvalue is \(g(p)\), negative before \(\alpha\), zero at \(\alpha\), and positive after it. This proves both full classifications for every real \(p\ge0\).

**5. Endpoint rank and kernel statement.** With \(H=I-\mathbf1\mathbf1^T/|V|\), the Euclidean Gram matrix associated to squared distances \(d^\alpha\) is \(-\tfrac12 HD_\alpha H\). At the root it has ranks \(6+14=20\) and \(21+7=28\). The Schoenberg kernel equivalence follows from conditional negative definiteness on a finite set.

## Verification
The accompanying `check.py` is standalone except for NumPy. It constructs both graphs from adjacency, computes all shortest-path distances by breadth-first search, checks the odd-graph and folded-cube metric formulas, and compares full independently diagonalized matrices against the displayed spectral multiplicities for eight values of \(p\), including the critical root. It also checks the exact coefficient-by-coefficient radial bridge for \(2\le k\le25\), and numerically confirms endpoint nullities \(14\) and \(35\). The reported run passed all checks. The exact proof above, not this bounded computation, establishes the universal and all-real-parameter assertions.

To reproduce from the directory containing this document and `check.py`, run `python3 check.py` after installing NumPy.

## Relationship to prior work
Sánchez (arXiv:1108.0451, first posted 2011-08-02) gives general finite-metric negative-type criteria and computes complete-bipartite examples. Aalipour et al. (arXiv:1509.01196, first posted 2015-09-03), Section 3.2, provide the odd-graph distance formula and Eberlein/Johnson relation spectra; this **already supplies** the general machinery for the odd-graph half of the calculation. Mančinska et al. (arXiv:1808.02051, 2018-08-06), Section 2, describe folded cubes as antipodal hypercube quotients and cubelike Cayley graphs. None of the inspected passages states the coefficientwise cross-family radial spectral identity or the shared sharp negative-type boundary with distinct endpoint ranks. The contribution is specifically this cross-family correspondence and its sharp consequence, not the prior Johnson/Walsh diagonalization techniques themselves.

## Limitations
No statement is made about coincidences of entire spectra, cospectrality, or equality of negative-type exponents at other graph orders. The historical originality review is bounded; earlier equivalent descriptions in distance-regular association-scheme literature remain possible. The self-review correctness/originality/value review is not independent external validation. The computational checks sample finitely many values of \(p\) and \(k\); the theorem's quantifiers are proved analytically.

## References
1. S. Sánchez, *On the supremal p-negative type of a finite metric space*, arXiv:1108.0451 (first version 2011-08-02), https://arxiv.org/abs/1108.0451.
2. G. Aalipour et al., *On the distance spectra of graphs*, arXiv:1509.01196 (first version 2015-09-03), especially Section 3.2 and Theorem 3.9, https://arxiv.org/abs/1509.01196.
3. L. Mančinska, I. Pivotto, D. E. Roberson, G. Royle, *Cores of Cubelike Graphs*, arXiv:1808.02051 (first version 2018-08-06), especially the folded-cube definition in Section 2, https://arxiv.org/abs/1808.02051.
