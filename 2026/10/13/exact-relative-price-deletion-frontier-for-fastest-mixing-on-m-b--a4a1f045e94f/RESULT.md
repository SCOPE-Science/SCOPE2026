# Exact relative-price deletion frontier for fastest mixing on Möbius ladders

## Finding
For each integer \(n\ge3\), the budget-one fastest symmetric continuous-time Markov process on a Möbius ladder with price \(t>0\) for each antipodal rung and unit price for each cycle edge admits an exact globally complete optimizer classification, **even when all individual edge rates are independent**.

Put
\[
p=4\sin^2\!\left(\frac{\pi}{2n}\right),\qquad
q=4\sin^2\!\left(\frac{\pi}{n}\right),\qquad
\delta=q-p>0,\qquad t_c=\frac{4}{p}=\csc^2\!\left(\frac{\pi}{2n}\right).
\]
For \(0<t<t_c\), exactly one allocation maximizes the Laplacian gap:
\[
w_j^*=\frac{2}{n(4+t\delta)},\qquad
a_j^*=\frac{\delta}{n(4+t\delta)},\qquad
\gamma^*=\frac{2q}{n(4+t\delta)}.
\]
For \(t>t_c\), exactly one allocation maximizes it:
\[
w_j^*=\frac{1}{2n},\qquad a_j^*=0,\qquad \gamma^*=\frac{p}{2n}.
\]
At \(t=t_c\), **all** maximizing allocations have constant rim conductance \(w_j=b\) and constant rung conductance \(a_j=a\), with
\[
\frac{p}{2nq}\le b\le\frac{1}{2n},\qquad
a=\frac{1-2nb}{nt_c},\qquad\gamma^*=\frac{p}{2n}.
\]
There are no nonsymmetric optima in any regime. Every rim edge remains active; all rungs are active below the threshold, optional at the threshold, and absent above it.

## Assumptions and scope
The graph has vertex set \(\mathbb Z/(2n)\mathbb Z\), \(2n\) undirected cycle edges \(\{j,j+1\}\) (indices modulo \(2n\)), and \(n\) undirected opposite pairs \(\{j,j+n\}\) for \(0\le j<n\). Write \(w_j\ge0\) for each cycle-edge conductance, \(a_j\ge0\) for each rung conductance, and require
\[
B+tA=1,\qquad B=\sum_{j=0}^{2n-1}w_j,\qquad A=\sum_{j=0}^{n-1}a_j,\quad t>0.
\]
The weighted Laplacian is \(L=\sum_{\{i,j\}\in E}\omega_{ij}(e_i-e_j)(e_i-e_j)^\mathsf T\); the target \(\gamma=\lambda_2(L)\) is the smallest eigenvalue of \(L\) restricted to vectors orthogonal to the constants. Zero edge rates are allowed but the optimum always connects the graph. This is a **continuous-time** objective, not discrete-time minimization of the absolute nontrivial transition eigenvalue.

## Proof
**Step 1 (two universal Fourier certificates).** Let \(\theta=\pi/n\), and set \(z_j^{(k)}=(\cos(kj\theta),\sin(kj\theta))\) for \(j\in\mathbb Z/(2n)\mathbb Z\) and \(k=1,2\). For \(n\ge3\), both real coordinate vectors are orthogonal to constants and have squared norm \(n\). Their averaged Rayleigh quotient therefore bounds \(\lambda_2\) from above. Using \(\|z_j^{(1)}-z_{j+1}^{(1)}\|^2=p\), \(\|z_j^{(1)}-z_{j+n}^{(1)}\|^2=4\), while \(\|z_j^{(2)}-z_{j+1}^{(2)}\|^2=q\) and \(z_j^{(2)}=z_{j+n}^{(2)}\), gives
\[
\gamma\le \min\!\left\{\frac{qB}{2n},\frac{pB+4A}{2n}\right\}
=\frac1{2n}\min\!\left\{qB,\;pB+\frac{4}{t}(1-B)\right\},\qquad 0\le B\le1.
\]
This inequality is valid for **arbitrary independent nonnegative edge rates**.

**Step 2 (sharp scalar envelope).** When \(t<4/p\), the second affine term has negative slope and the first positive slope, so their minimum is uniquely maximized at \(B^*=4/[4+t(q-p)]\). When \(t>4/p\), both affine terms increase with \(B\), and the unique maximizing total cycle budget is \(B=1\). At equality \(t=4/p\), the second affine term is constant and all \(B\in[p/q,1]\) are maximizing. These values yield the asserted formulas for \(a=A/n\), \(b=B/(2n)\), and \(\gamma^*\).

**Step 3 (attainment with the whole spectrum).** For constant cycle rate \(b\) and constant rung rate \(a\), Fourier vectors \(e^{i\pi kj/n}\), \(k=0,\ldots,2n-1\), diagonalize \(L\), with eigenvalues
\[
\lambda_k=b\bigl(2-2\cos(\pi k/n)\bigr)+a\bigl(1-(-1)^k\bigr).
\]
Among positive even frequencies the smallest value is \(qb\); among odd frequencies the smallest value is \(pb+2a\). Thus \(\lambda_2=\min\{qb,pb+2a\}\), which saturates the universal envelope in each case above.

**Step 4 (edgewise rigidity, including the boundary).** Every maximizing allocation saturates the first-harmonic averaged Rayleigh bound \((pB+4A)/(2n)\), not merely the scalar max: check the two affine terms at the maximizing \(B\) in each regime. Since each of the separate cosine and sine Rayleigh quotients is at least \(\lambda_2\), both must equal \(\lambda_2\). Hence both first-harmonic coordinate vectors are genuine eigenvectors. Let \(J\) rotate \(\mathbb R^2\) by \(\pi/2\). Their joint eigenvector equation at vertex \(j\), where \(a_{j\bmod n}\) is the opposite-edge rate, is
\[
\left[(1-\cos\theta)(w_{j-1}+w_j)+2a_{j\bmod n}\right]z_j^{(1)}
+\sin\theta(w_{j-1}-w_j)Jz_j^{(1)}=\gamma z_j^{(1)}.
\]
Since \(\sin\theta>0\) and \(z_j^{(1)},Jz_j^{(1)}\) are independent, \(w_{j-1}=w_j\) for every \(j\); all cycle rates are the same. The remaining coefficient then implies all rung rates are the same. Thus no nonsymmetric allocation can achieve the envelope, and the scalar cases in Step 2 exhaust all optima.

**Step 5 (network-size boundary).** Since \(p\sim\pi^2/n^2\), \(q\sim4\pi^2/n^2\), we have \(t_c\sim4n^2/\pi^2\). At any fixed price \(t>0\) and sufficiently large \(n\), the first branch applies, yielding
\[
w_j^*\sim\frac1{2n},\qquad a_j^*\sim\frac{3\pi^2}{4n^3},\qquad
\gamma^*\sim\frac{2\pi^2}{n^3},\qquad
nt a_j^*=O(n^{-2}).
\]
The budget-one bare \(2n\)-cycle has gap \(p/(2n)\sim\pi^2/(2n^3)\), so the gap ratio tends to exactly \(4\) despite the vanishing fraction spent on rungs.

## Verification
The standalone Python file `check_mobius.py` builds the actual weighted Laplacian, checks the two Fourier upper bounds for nonsymmetric random feasible assignments, compares numerical eigenvalues with the closed formulas, and verifies the full critical family. Execute `python check_mobius.py` in an environment with NumPy installed. Its fixed-seed run covers \(3\le n\le12\), nine price cases per size, 2,700 feasible nonsymmetric perturbations, and 70 critical-family choices. These finite computations are supplementary; Steps 1–5 provide the proof for all permitted integer sizes and positive real prices.

As an exact sanity check, \(n=3\), \(t=1\) gives \(p=1\), \(q=3\), both edge classes at conductance \(1/9\), and \(\gamma^*=1/3\). The pure cycle with the same budget has gap \(1/6\), while the deletion threshold is \(t_c=4\).

## Relationship to prior work
Sun, Boyd, Xiao, and Diaconis (2006) formulate the general priced continuous-time fastest-mixing Markov process as a semidefinite program and explicitly treat paths and cycles (their Sections 1, 5.2, and 5.3). That framework includes this optimization as an *instance*, but the inspected results do not provide its Möbius-ladder formulas, deletion-price threshold, or proof that all independent edge rates are forced to be symmetric. Boyd, Diaconis, Parrilo, and Xiao (2009) develop representation and Fourier reductions for **discrete-time** fastest-mixing chains, including cycle and wheel examples; the discrete-time modulus objective and stochastic row constraints differ from the current objective. Azimi and Farrokhi Derakhshandeh Ghouchan (2023, Section 5) study Möbius-ladder Laplacian pseudoinverses, resistances, and the Kirchhoff index for a prescribed unweighted graph, not variable-price spectral-gap allocation. Classical circulant diagonalization underlies Step 3, but does not by itself establish optimality or edgewise rigidity. An unlocated specialized result in other literature remains possible.

## Limitations
The result concerns fixed Möbius-ladder topology, unit total **linear price-weighted conductance**, and the continuous-time symmetric Laplacian gap. It does not assert the optimal discrete-time stochastic matrix, arbitrary stationary distributions, resistance minimization, or mixing times with constants. Finite numerical tests cannot certify the universal proof; the theorem is analytical. Historical originality remains subject to further independent literature review.

## References
1. J. Sun, S. Boyd, L. Xiao, P. Diaconis, *The Fastest Mixing Markov Process on a Graph and a Connection to a Maximum Variance Unfolding Problem*, SIAM Review 48(4), 681–699 (2006); electronically public 2006-11-02; DOI:10.1137/S0036144504443821; full text: https://web.stanford.edu/~boyd/papers/pdf/fmmp.pdf.
2. S. Boyd, P. Diaconis, P. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs with Symmetries*, SIAM J. Optim. 20(2), 792–819 (2009); arXiv:0709.0955v1; full text: https://web.stanford.edu/~boyd/papers/pdf/fast_mix_symm.pdf.
3. A. Azimi, M. Farrokhi Derakhshandeh Ghouchan, *Explicit formulas for matrices associated to ladder, circular ladder, and Möbius ladder graphs*, arXiv:2306.10497v1 (2023); https://arxiv.org/html/2306.10497v1.
