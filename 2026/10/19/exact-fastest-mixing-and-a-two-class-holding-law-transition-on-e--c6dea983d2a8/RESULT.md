# Exact fastest mixing and a two-class holding-law transition on even squared cycles

## Finding
For every even integer \(n\ge8\), let \(C_n^2\) be the square of the undirected cyclic graph: vertices are residues modulo \(n\), with edges of offsets \(\pm1\) and \(\pm2\). Among **all** real symmetric, nonnegative, row-stochastic transition matrices supported on its edges and diagonal, the minimum second-largest eigenvalue modulus (SLEM) is given below. No assumption of translational invariance is made on competitors.

Write \(c=\cos(2\pi/n)\), \(q=2(1-c)\), \(j=\lceil n/4\rceil\), and \(d=\cos(2\pi j/n)\). Define \(K(x)=2q(1-x)+4(1-x^2)\), \(E=4q\), and \(M=K(d)\). A globally fastest-mixing kernel is the circulant with weight \(a=2q/(E+M)\) on **each** of the two nearest-neighbor edges, weight \(b=2/(E+M)\) on **each** second-neighbor edge, and holding weight \(h=1-2a-2b>0\). Its optimum is
\[
\mu_*=\frac{M-E}{M+E},\qquad 1-\mu_*=4a=\frac{8q}{E+M}.
\]
This choice is the **unique** direction-invariant minimizer, but uniqueness among all unrestricted kernels is not asserted.

The holding law splits sharply according to \(n\bmod4\). If \(4\mid n\),
\[
 a=h=\frac{q}{2+3q},\qquad b=\frac{1}{2+3q},\qquad 1-\mu_*=\frac{4q}{2+3q}.
\]
If \(n\equiv2\pmod4\), let \(s=\sin(\pi/n)\). Then
\[
 a=\frac{2s^2}{1+5s^2+2s^3},\quad b=\frac{1}{2(1+5s^2+2s^3)},\quad h=\frac{s^2(1+2s)}{1+5s^2+2s^3},\quad 1-\mu_*=\frac{8s^2}{1+5s^2+2s^3}.
\]
In particular, the optimally tuned holding probability is exactly equal to the per-edge nearest-neighbor transition probability when \(4\mid n\), whereas their ratio is \((1+2\sin(\pi/n))/2\) when \(n\equiv2\pmod4\). Along even orders the optimal spectral gap satisfies \(n^2(1-\mu_*)\to8\pi^2\), while \(n^2h\to2\pi^2\) along orders divisible by four and \(n^2h\to\pi^2\) along orders congruent to two modulo four.

## Assumptions and scope
All transition matrices are real, symmetric, entrywise nonnegative, stochastic, and supported only on the diagonal and graph edges of \(C_n^2\). No irreducibility or laziness restriction is imposed on competitors. The quantity \(\mu(P)\) is the spectral norm of \(P-J/n\), equivalently the largest absolute eigenvalue away from the stationary constant eigenvector (counting any additional eigenvalue \(1\)). All conclusions hold for every even integer \(n\ge8\), without upper bound.

## Proof
**1. Symmetry reduction.** Average any feasible \(P\) over the cyclic shifts and reflection of the vertices. The result \(\overline P\) remains feasible and is circulant, with a common nearest-neighbor probability \(a\ge0\), a common second-neighbor probability \(b\ge0\), and \(2a+2b\le1\). Since \(P\mapsto\|P-J/n\|_{\rm op}\) is convex and invariant under orthogonal permutation conjugation, \(\mu(\overline P)\le\mu(P)\). Thus a global minimizer exists in this two-dimensional family.

**2. Fourier spectrum.** For \(k=1,\ldots,n/2\), set \(x_k=\cos(2\pi k/n)\). Fourier diagonalization gives
\[
\lambda_k=1-aU(x_k)-bV(x_k),\quad U(x)=2(1-x),\quad V(x)=4(1-x^2).
\]
At the first frequency \(k=1\), \(U(c)=q\) and \(V(c)=2(1+c)q\). At the antipodal frequency \(k=n/2\), \(U(-1)=4\) and \(V(-1)=0\). Hence for \(a=qb\) the corresponding spectral drops agree:
\[
q a+2(1+c)qb=4qb=4a=Eb.
\]
Here the elementary identity \(q+2(1+c)=4\) was used.

**3. Discrete spectral extremes.** On \(a=qb\), the spectral drop at cosine coordinate \(x\) is \(bK(x)\), where \(K(x)=4+2q-2qx-4x^2\) is strictly concave and has continuous maximum at \(x=-q/4\). On the ordered cosine grid \(x_1>\cdots>x_{n/2}=-1\), concavity forces the minimum of \(K\) among the nonconstant frequencies to be one of the two endpoints. These endpoint values agree at \(E=4q\).

The discrete maximum is attained at \(k=j=\lceil n/4\rceil\). For \(n=4r\), the grid contains \(x_j=0\); its immediate negative neighbor is \(-\sin(2\pi/n)\) and the inequality \(1-\cos(2\pi/n)\le\sin(2\pi/n)\) makes \(K(0)\ge K(-\sin(2\pi/n))\); all remaining grid nodes lie still farther from the concave quadratic's maximizer. For \(n=4r+2\), the two closest-to-zero grid nodes are \(\pm s\) with \(s=\sin(\pi/n)\), and the maximum of \(K\) is at the negative one: \(K(-s)>K(s)\), while all other nodes are farther from \(-s^2\) (as \(q=4s^2\)), so cannot improve it. This proves \(Eb\le aU(x_k)+bV(x_k)\le Mb\) for all nonconstant frequencies, with both extremes attained.

**4. Construction and feasibility.** Set \(b=2/(E+M)\), \(a=qb\). Then the extreme nontrivial eigenvalues equal \(\pm(M-E)/(M+E)\). The displayed residue-class formulas follow by inserting \(d=0\) when \(4\mid n\) or \(d=-s\) when \(n\equiv2\pmod4\). Every displayed weight is nonnegative and \(h>0\); hence the proposed kernel is feasible.

**5. Global lower bound, not relying on an ansatz.** For arbitrary circulant feasible \((a,b)\), write \(v_k=(U(x_k),V(x_k))\). Because \(-1<d<c<1\), we can express \(v_j=A v_1+Bv_{n/2}\), where
\[
A=\frac{V(d)}{V(c)}>0,\qquad B=\frac{U(d)-A U(c)}4>0.
\]
The strict positivity of \(B\) follows from \(U(x)/V(x)=1/[2(1+x)]\) for \(-1<x<1\). If this kernel has SLEM at most \(\mu\), its three Fourier inequalities imply \(v_1\cdot(a,b)\ge1-\mu\), \(v_{n/2}\cdot(a,b)\ge1-\mu\), and \(v_j\cdot(a,b)\le1+\mu\). Therefore
\[
(A+B)(1-\mu)\le1+\mu.
\]
Evaluation at the vector \((a,b)=(q,1)\) shows \(A+B=K(d)/(4q)=M/E\). Thus \(\mu\ge(M-E)/(M+E)\), proving optimality of the candidate, even before other frequencies are considered. Equality forces the three independent constraints to be tight; since \(v_1\) and \(v_{n/2}\) are linearly independent, the circulant optimizer is unique.

**6. Asymptotics.** Use \(q=4\pi^2/n^2+O(n^{-4})\), \(s=\pi/n+O(n^{-3})\), and the exact residue formulas. Then the spectral gaps satisfy \(1-\mu_*=8\pi^2/n^2+O(n^{-3})\), and holding weights have the two stated, distinct subsequential limits.

## Verification
Run `python verify.py` with Python 3, NumPy and SciPy installed. The program checks the exact residue identities numerically, recomputes the full circulant spectrum and solves the independent linear-programming minimax problem over both edge-orbit probabilities for all even orders 8 through 120. These tests are corroborative: the unbounded-order result follows from the proof above, not from enumeration or floating-point experiments.

## Relationship to prior work
Boyd, Diaconis and Xiao derived the general fastest-mixing stochastic-matrix problem and its convex/Semidefinite formulation. Boyd, Diaconis, Parrilo and Xiao analyzed symmetry reductions and gave formulas for ordinary cycles and certain products; their cycle case uses the distance-one graph, not the square-of-cycle graph analyzed here. A separately available odd-order squared-cycle solution has a different antipodal spectral geometry: this theorem addresses the remaining even orders and their mod-four holding-probability dichotomy. The comparison concerns mathematical implication, not title similarity. General SDP solvability does not entail the explicit all-order optimizer, three-contact dual certificate or parity-dependent asymptotic holding law without further analysis.

## Limitations
Only symmetric stochastic kernels on the squared-cycle support are optimized; directed/nonreversible chains, higher-radius steps and mixing-time constants are outside the claim. Unrestricted optimizer uniqueness is not proved. Literature searches cannot exclude equivalent formulations in unindexed circulant or Markov-chain literature. The verification tests are finite and numerical and do not independently certify the analytical proof.

## References
1. S. Boyd, P. Diaconis, L. Xiao, "Fastest Mixing Markov Chain on a Graph," *SIAM Review* 46 (2004), 667–689; original open paper: https://web.stanford.edu/~boyd/papers/pdf/fmmc.pdf (dated 2004-10-29 in original version).
2. S. Boyd, P. Diaconis, P. Parrilo, L. Xiao, "Fastest Mixing Markov Chain on Graphs with Symmetries," Microsoft Research technical report MSR-TR-2007-52, April 2007: https://www.microsoft.com/en-us/research/wp-content/uploads/2016/02/tr-2007-52.pdf.
