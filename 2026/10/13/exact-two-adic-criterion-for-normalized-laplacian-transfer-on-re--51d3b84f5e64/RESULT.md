# Exact two-adic criterion for normalized-Laplacian transfer on regular double cones

## Finding

Let \(H\) be any simple unweighted \(k\)-regular graph on \(m\geq1\) vertices, with \(0\leq k<m\); it need not be connected. Attach two new vertices \(u,v\), each adjacent to every vertex of \(H\), and join \(u\) to \(v\) if and only if \(\varepsilon=1\), where \(\varepsilon\in\{0,1\}\). Call the resulting connected graph \(G_\varepsilon\). The Hamiltonian is the symmetric normalized Laplacian \(\mathcal L=I-D^{-1/2}AD^{-1/2}\), and the continuous-time walk is \(U(t)=e^{-it\mathcal L}\).

Put
\[
a=m(k+4)+2\varepsilon,\qquad b=(k+2)(m+2\varepsilon),\qquad
p=\frac a{\gcd(a,b)},\quad q=\frac b{\gcd(a,b)}.
\]
The two distinguished vertices exhibit **perfect state transfer** at some finite positive time, meaning \(|\langle v|U(t)|u\rangle|^2=1\), **if and only if** \(p\) is even and \(q\) is odd. Equivalently,
\[
\boxed{\nu_2\bigl(m(k+4)+2\varepsilon\bigr)>\nu_2\bigl((k+2)(m+2\varepsilon)\bigr),}
\]
where \(\nu_2(n)\) is the exponent of \(2\) dividing a positive integer \(n\). In precisely those cases, the least positive perfect-transfer time is
\[
\boxed{t_{\min}=\frac{\pi q(m+\varepsilon)}{m+2\varepsilon},}
\]
and **every** other positive perfect-transfer time is an odd integer multiple of \(t_{\min}\).

For all \(t\in\mathbb R\), an exact formula for the transfer probability is
\[
\boxed{
P_\varepsilon(t)=\frac14\left|w+(1-w)e^{-it\theta_s}-e^{-it\theta_a}\right|^2,\quad
w=\frac{2(m+\varepsilon)}{2(m+\varepsilon)+m(k+2)},
}
\]
with
\[
\theta_s=\frac{m(k+4)+2\varepsilon}{(m+\varepsilon)(k+2)},\qquad
\theta_a=\frac{m+2\varepsilon}{m+\varepsilon}.
\]
In particular, for nonadjacent distinguished vertices (\(\varepsilon=0\)), perfect transfer occurs **exactly when** \(k\equiv0\pmod4\), independently of \(m\), and then \(t_{\min}=\pi(k+2)/2\). In contrast, if \(\varepsilon=1\), no perfect transfer occurs for \(k\equiv0\pmod4\), but it does occur, for instance, when \(H=C_5\) and \(\varepsilon=1\), at least time \(6\pi\). Thus inserting just the edge \(uv\) can change transfer feasibility in either direction, although the base graph is unchanged.

## Assumptions and scope

All graphs are finite, simple, unweighted, undirected. The base graph has exactly \(m\) vertices and common internal degree \(k\). The two distinguished vertices have degree \(d=m+\varepsilon\), while every base vertex has degree \(R=k+2\); these are strictly positive. The theorem concerns transfer **between the distinguished vertices only** under the **symmetric normalized-Laplacian continuous-time model**, not under the combinatorial Laplacian, adjacency operator, a discrete-time walk, or an arbitrary irregular base graph. The parameter \(\varepsilon=0\) denotes two nonadjacent apexes; \(\varepsilon=1\) denotes an edge between them. The positive-time assertions quantify over **every** admissible integer pair \((m,k)\), every \(k\)-regular base graph \(H\), and both \(\varepsilon\) values.

## Proof

**Step 1: invariant subspaces.** Let \(N=D^{-1/2}AD^{-1/2}=I-\mathcal L\), and define the orthonormal vectors
\[
|s\rangle=(|u\rangle+|v\rangle)/\sqrt2,\quad
|a\rangle=(|u\rangle-|v\rangle)/\sqrt2,\quad
|c\rangle=\sum_{x\in V(H)}|x\rangle/\sqrt m.
\]
The antisymmetric vector is an eigenvector of \(N\) with eigenvalue \(-\varepsilon/d\); consequently its \(\mathcal L\)-eigenvalue is \(\theta_a=1+\varepsilon/d=(m+2\varepsilon)/d\). Regularity makes \(\operatorname{span}\{|s\rangle,|c\rangle\}\) invariant under \(N\), with restriction
\[
B=\begin{pmatrix}
\varepsilon/d&\sqrt{2m/(dR)}\\
\sqrt{2m/(dR)}&k/R
\end{pmatrix}.
\]
Since \(N D^{1/2}\mathbf1=D^{1/2}\mathbf1\), this block has eigenvalue \(1\), with eigenvector proportional to \(\sqrt{2d}|s\rangle+\sqrt{mR}|c\rangle\). Its other eigenvalue is determined either from the trace or determinant:
\[
\lambda=\frac{\varepsilon}{d}-\frac2R,
\qquad
\det B=\frac{\varepsilon k-2m}{dR}=\lambda.
\]
Thus the nonstationary symmetric \(\mathcal L\)-eigenvalue is
\[
\theta_s=1-\lambda=\frac{m}{d}+\frac2R
=\frac{m(k+4)+2\varepsilon}{dR}.
\]
The squared overlap of \(|s\rangle\) with the stationary eigenvector is \(w=2d/(2d+mR)\), so \(0<w<1\), and the other symmetric eigencomponent has weight \(1-w>0\). All other base-graph eigenvectors have zero overlap with either distinguished vertex, regardless of disconnectedness of \(H\).

**Step 2: exact transition amplitude.** Because \(|u\rangle=(|s\rangle+|a\rangle)/\sqrt2\) and \(|v\rangle=(|s\rangle-|a\rangle)/\sqrt2\), the block diagonalization yields
\[
\langle v|U(t)|u\rangle
=\frac12\bigl(w+(1-w)e^{-it\theta_s}-e^{-it\theta_a}\bigr).
\]
This is the claimed probability formula, and proves that only the apex/base parameters \((m,k,\varepsilon)\) enter the answer. It is valid even when eigenvalues from distinct invariant subspaces coincide: no distinct-eigenvalue assumption was used.

**Step 3: phase alignment and exact time set.** The triangle inequality, using \(0<w<1\), shows \(|\langle v|U(t)|u\rangle|\leq1\). Equality requires, and is achieved exactly when, the three nonzero summands align in phase. Because the first has positive real phase \(1\), this means
\[
e^{-it\theta_s}=1,\qquad e^{-it\theta_a}=-1.
\]
Therefore \(t\theta_a/\pi\) must be a positive odd integer \(j\) and \(t\theta_s/\pi\) must be an even integer. Now
\[
\frac{\theta_s}{\theta_a}=\frac{a}{b}=\frac pq,\qquad \gcd(p,q)=1.
\]
For an odd \(j\), the rational number \(jp/q\) is an even integer **if and only if** \(q\mid j\), \(q\) is odd, and \(p\) is even. This proves the necessary-and-sufficient criterion, and shows that all valid \(j\) are the odd multiples of \(q\). Dividing \(\pi j\) by \(\theta_a\) gives exactly the stated first time and subsequent odd multiples. Reducing \(a,b\) by their greatest common divisor proves the equivalent \(2\)-adic formulation.

**Step 4: the two edge regimes.** If \(\varepsilon=0\), the ratio is \((k+4)/(k+2)\). Reduction shows its numerator is even and denominator odd exactly when \(k\) is divisible by \(4\); then \(\theta_a=1\) and the least time is \(\pi(k+2)/2\). If \(\varepsilon=1\) and \(k\equiv0\pmod4\), the numerator \(m(k+4)+2\) is \(2\pmod4\), whereas the denominator \((k+2)(m+2)\) is divisible by \(2\), so the strict \(2\)-adic inequality fails. Finally, \((m,k,\varepsilon)=(5,2,1)\) has \((a,b)=(32,28)\), hence \((p,q)=(8,7)\) and \(t_{\min}=6\pi\). The five-cycle is a \(2\)-regular simple base graph, providing the promised connected-apex example. \(\square\)

## Verification

The accompanying `verify.py` runs with standard Python 3 only. It uses exact rational arithmetic to check the two block-eigenvalue identities, the reduced eigenvalue ratio, stationary projection bounds, parity equivalence, the special nonadjacent-cone formula, and explicit examples. The check covers all graphical \((m,k)\) with \(1\leq m<100\), both apex-edge choices, for 7,450 parameter cases. It outputs `VERIFY_OK exact_reduced_eigenvalues_and_valuation_tests=7450 examples=6`. The finite check is a computational consistency test; the unrestricted result follows from the analytical proof above.

## Relationship to prior work

Coutinho and Baptista [1] establish the general normalized-Laplacian spectral conditions for state transfer (notably Theorem 5), but do not resolve the two-parameter double-cone families or the edge-controlled parity transition. Their broad spectral criterion underlies the phase-alignment method here; this result determines explicitly when the criterion is satisfied and gives all transfer times. Monterde [2] analyzes strong cospectrality and double cones for generalized adjacency and normalized-adjacency formulations, but does not supply the normalized-Laplacian **perfect-transfer** criterion in this form. Kirkland, Monterde, and Plosker [3] classify transfer on double cones for adjacency, ordinary Laplacian, and signless Laplacian Hamiltonians; none is the degree-normalized Hamiltonian used here. Alvir and collaborators [4] show that a **nonadjacent-apex** double cone has ordinary-Laplacian transfer based on a congruence of the **base order**, independent of internal degree; the normalized result here instead depends on the base **degree** and changes when the apex edge is added. Kirkland and Monterde [5] investigate joins for ordinary adjacency and Laplacian operators. Monterde's earlier thesis [6] contains double-cone classifications, but its introduction explicitly restricts its transfer Hamiltonians to adjacency and ordinary Laplacian; it does not cover the degree-normalized problem. These operator differences are substantive for the typically nonregular graphs considered here.

## Limitations

The theorem does not extend without modification to an irregular base graph or weighted/nonuniform apex couplings. It does not characterize transfer between arbitrary other vertex pairs, pretty-good transfer without perfect transfer, or any physical noise/decoherence mechanism. The spectral quotient itself and general phase-parity tools are established techniques; the asserted contribution is the **exact complete parameter classification for the normalized Hamiltonian on both regular double-cone types**, including the change upon toggling the apex edge. An unindexed equivalent calculation in specialized quantum-walk literature cannot be categorically excluded from a literature search, and independent review has not been performed. The closest available 2021 thesis has been inspected and pertains to different Hamiltonians.

## References

[1] G. Coutinho and P. Ferreira Baptista, *Quantum Walks in the Normalized Laplacian*, arXiv:2209.04668 (first public version 2022-09-10), https://arxiv.org/abs/2209.04668 ; Theorem 5 and Sections 2–4.

[2] H. Monterde, *Strong Cospectrality and Twin Vertices in Weighted Graphs*, arXiv:2111.01265, https://arxiv.org/abs/2111.01265 ; Sections 3 and 6.

[3] S. Kirkland, H. Monterde, and S. Plosker, *Quantum State Transfer Between Twins in Weighted Graphs*, arXiv:2201.02720, https://arxiv.org/abs/2201.02720 ; Sections 2, 3, and 5.

[4] R. Alvir et al., *Perfect State Transfer in Laplacian Quantum Walk*, arXiv:1409.5840, https://arxiv.org/abs/1409.5840 ; double-cone and normalized-Laplacian assertions refer to different parts of the source.

[5] S. Kirkland and H. Monterde, *Quantum Walks on Join Graphs*, arXiv:2312.06906, https://arxiv.org/abs/2312.06906 ; adjacency and ordinary-Laplacian join dynamics.

[6] H. Monterde, *Quantum State Transfer between Twins in Graphs*, MSc thesis, University of Manitoba (2021), https://mspace.lib.umanitoba.ca/server/api/core/bitstreams/9187af27-1f05-419a-b9e4-b9e50fa4465d/content ; introduction and Chapter 6.
