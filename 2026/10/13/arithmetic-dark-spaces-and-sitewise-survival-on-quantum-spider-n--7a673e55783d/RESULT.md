# Arithmetic dark spaces and sitewise survival on quantum spider networks

## Finding

Consider a spider tree with a central hub \(o\) and \(k\geq3\) arms of lengths \(L_1,\ldots,L_k\geq1\). Let \(n_i=L_i+1\), \(N=1+\sum_iL_i\), and, for every integer \(q\geq2\), define
\[
 r_q=\#\{i:q\mid n_i\},\qquad W_q=\sum_{i:q\mid n_i}\frac1{n_i},\qquad (x)_+=\max(x,0).
\]
The Hilbert space has an orthonormal vertex basis. With uniform real nonzero hopping \(J\), let \(A\) be the unweighted adjacency matrix and \(K=JA-i\gamma|o\rangle\langle o|\), where \(\gamma>0\). The unnormalized conditional quantum evolution is \(\rho_t=e^{-itK}\rho e^{itK^\dagger}\).

Let \(\mathcal D\) be the maximal subspace on which this evolution does not lose norm. Then
\[
 \boxed{\dim\mathcal D=\sum_{q=2}^{\max_i n_i}\varphi(q)(r_q-1)_+.}
\]
For every initial density matrix \(\rho\), the eventual survival is exactly \(\operatorname{tr}(P_{\mathcal D}\rho)\), and convergence of its survival probability to this value is exponential at a rate depending on the fixed graph, \(J\), and \(\gamma\). Consequently, for the maximally mixed initial state,
\[
 \boxed{P_{\rm absorption}=1-\frac{1}{N}\sum_{q\ge2}\varphi(q)(r_q-1)_+.}
\]
Here \(\varphi\) is Euler's totient function; all terms outside \(2\le q\le\max_i n_i\) vanish.

More precisely, let \((i,s)\) be the vertex on arm \(i\) at distance \(1\le s\le L_i\) from the hub. Write \(c_q(s)=\sum_{1\le a<q,\,\gcd(a,q)=1}\cos(2\pi as/q)\) for the integer-valued Ramanujan sum. The exact survival probability from that localized initial vertex is
\[
 \boxed{S(i,s)=\frac{1}{n_i}\sum_{\substack{q\mid n_i\\q\ge2}}\left(1-\frac{n_i^{-1}}{W_q}\right)\bigl(\varphi(q)-c_q(s)\bigr).}
\]
At the hub, survival is zero. Set
\[
 h_i=\mathop{\mathrm{lcm}}_{j\ne i}\gcd(n_i,n_j).
\]
Then there is **complete eventual absorption** from a localized site \((i,s)\) if and only if \(h_i\mid s\). All initial states are eventually absorbed if and only if the integers \(n_1,\ldots,n_k\) are pairwise coprime.

## Assumptions and scope

The graph is finite, connected, unweighted and open-ended, with a single hub and at least three internally disjoint path arms. Every edge has the same nonzero real hopping coefficient. The one loss site is the hub; its rate is strictly positive. No onsite disorder, extra bonds, or additional absorbers are assumed. The survival probability is the remaining squared norm of the no-jump evolution, equivalently the trace of the unnormalized state. The initial density matrix may be arbitrary; the displayed sitewise formula specializes to vertex basis states. The divisor-counting sum is finite for every graph.

## Proof

**1. Zero-hub eigenvectors.** For a Hermitian adjacency eigenvector with zero hub component, each arm is an independent open Dirichlet path. Its normalized eigenmodes, indexed by \(1\le b<n_i\), are
\[
 u_{i,b}(s)=\sqrt{\frac2{n_i}}\sin\left(\frac{\pi bs}{n_i}\right),\qquad
 \lambda_{i,b}=2J\cos\left(\frac{\pi b}{n_i}\right).
\]
Since cosine is strictly monotone on \((0,\pi)\) and \(J\ne0\), the same eigenvalue occurs on several arms exactly when the reduced fractions \(b/n_i=a/q\) are equal. Fix such a fraction with \(\gcd(a,q)=1\). Its eigenvalue occurs precisely on those arms for which \(q\mid n_i\). The remaining hub eigenvalue equation is
\[
 \sum_{i:q\mid n_i}\alpha_i\sqrt{\frac2{n_i}}\sin(\pi a/q)=0.
\]
Every coefficient is nonzero, so this equation defines a codimension-one subspace of the \(r_q\) participating arm modes. The dark eigenspace at this eigenvalue has dimension \((r_q-1)_+\). Different primitive fractions generate different eigenvalues, and the number of primitive fractions with denominator \(q\) is \(\varphi(q)\). Summing gives the stated dimension. Conversely every adjacency eigenvector having zero hub component arises from this Dirichlet-arm construction, so there are no missing dark eigenspaces.

**2. Local projection weight.** At fixed primitive \(a/q\), let \(e_i\) denote the normalized arm-supported Dirichlet eigenvector for each participating arm. The hub condition restricts their coefficient vector to the hyperplane perpendicular to
\[
 v_i=\sqrt{\frac2{n_i}}\sin(\pi a/q).
\]
The orthogonal projector onto that hyperplane is \(I-vv^*/\lVert v\rVert^2\). Its diagonal in the arm-mode index \(i\) is \(1-n_i^{-1}/W_q\), since all participating coefficients share the same nonzero sine factor. Hence the spectral projector contributes at site \((i,s)\)
\[
 \frac2{n_i}\sin^2(\pi as/q)\left(1-\frac{n_i^{-1}}{W_q}\right).
\]
Summing over reduced \(a/q\) and invoking the exact identity
\[
 \sum_{\substack{1\le a<q\\\gcd(a,q)=1}}2\sin^2(\pi as/q)=\varphi(q)-c_q(s)
\]
yields the claimed formula for \(S(i,s)\). The hub has projection zero by construction. Summing all sitewise projection weights recovers \(\operatorname{tr}P_{\mathcal D}=\dim\mathcal D\).

**3. Complete-absorption classification.** Each term in the unsummed sine-square formula is nonnegative. If \(r_q=1\), the projector factor vanishes. If \(r_q\ge2\), that factor is strictly positive, and the sum of sine squares over all primitive numerators vanishes precisely when \(q\mid s\): one primitive numerator is \(a=1\), for which \(\sin(\pi s/q)=0\) precisely under that divisibility condition. The contributing denominators for arm \(i\) are precisely the divisors \(q\ge2\) of some \(\gcd(n_i,n_j)\), with \(j\ne i\). Their simultaneous divisibility of \(s\) is equivalent to \(h_i\mid s\). Global absence of dark eigenvectors is equivalent to \(r_q\le1\) for every \(q\ge2\), equivalently pairwise coprimality of the shifted arm lengths.

**4. Long-time dynamics.** Let \(\mathcal D\) be the orthogonal sum of the constructed zero-hub adjacency eigenspaces. It is invariant under both \(JA\) and the projection \(|o\rangle\langle o|\), hence so is its orthogonal complement. On \(\mathcal D\), \(K=JA\) is Hermitian and evolution is unitary. If a nonzero eigenvector \(w\) of \(K\) in \(\mathcal D^\perp\) had a purely real eigenvalue, taking the imaginary part of its Rayleigh quotient would give \(-\gamma|\langle o,w\rangle|^2=0\). Thus \(w\) would have zero hub component and would be an adjacency eigenvector, hence would belong to \(\mathcal D\), a contradiction. Dissipativity makes every eigenvalue's imaginary part nonpositive; therefore each eigenvalue on the finite-dimensional bright block has strictly negative imaginary part. Jordan normal form gives exponentially decaying evolution on that block. Orthogonality of the two invariant blocks proves, for every density matrix, that the surviving trace converges to \(\operatorname{tr}(P_{\mathcal D}\rho)\). Substituting \(\rho=I_N/N\) proves the absorption formula.

## Verification

A standalone `verify_spider.py` reconstructs independent real symmetric adjacency matrices and obtains their dark spectral projectors by numerical diagonalization and removal of the hub-visible component in each eigenspace. For all \(182\) nondecreasing length tuples of \(3\) or \(4\) arms, with each length in \(\{1,\ldots,6\}\), it compares the arithmetic dark rank, every sitewise probability, the trace identity and all zero-site predictions. The computed \(2534\) site probabilities agree within \(3\cdot10^{-9}\). Install the dependency in `requirements.txt`, then run `python3 verify_spider.py`. These finite checks are corroboration only; the four-step proof establishes the all-integer result.

## Relationship to prior work

The quantum transport literature already establishes that degenerate eigenmodes and non-Hermitian traps can suppress coherent transport; this includes work by Mülken and Blumen on finite trees, Agliari on randomly trapped networks, and Anishchenko, Blumen and Mülken on ordinary star graphs. More recently, Vieira and Amorim explicitly exhibit root-dark eigenspaces and study controlled root occupation in equal-arm star/spider-like configurations. Those physical mechanisms and the elementary ordinary-star special case are not claimed as new. The result here evaluates the complete dark dimension and every localized surviving probability on **all heterogeneous finite spiders**, with an arithmetic zero-site and global coprimality classification. Related Laplacian nodal-control results for starlike trees do not directly imply this adjacency-dynamics theorem, because the vertex-degree correction is not scalar on these trees.

## Limitations

An equivalent closed-form characterization might exist in less searchable spectral graph or graph-controllability literature; independent publication-priority assessment has not been performed. The theorem does not supply a universal relaxation-rate bound, nor address weighted/nonuniform hopping, onsite disorder, multiple traps, non-Markovian loss, or arbitrary trees. The embedded numerical comparisons are finite and do not independently certify the infinite family.

## References

1. O. Mülken and A. Blumen, *Efficiency of quantum and classical transport on graphs* (2006), arXiv:quant-ph/0602120, https://arxiv.org/abs/quant-ph/0602120 (first posted 2006-02-15).
2. E. Agliari, *Trapping of Continuous-Time Quantum walks on Erdos-Renyi graphs* (2011), arXiv:1102.3994, https://arxiv.org/abs/1102.3994.
3. A. Anishchenko, A. Blumen, O. Mülken, *Enhancing the spreading of quantum walks on star graphs by additional bonds* (2011), arXiv:1111.7065, https://arxiv.org/abs/1111.7065.
4. R. Vieira and E. P. M. Amorim, *Control of vertex probability via edge-weight modulation in continuous-time quantum walks*, arXiv:2404.04094, https://arxiv.org/abs/2404.04094 (first posted 2024-04-05).
5. G. Parlangeli, *Laplacian Controllability and Observability of Multi-Agent Systems: Recent Advances in Tree Graphs* (2025), freely accessible full text at https://www.mdpi.com/1999-4893/18/5/239. (Different Laplacian model.)
