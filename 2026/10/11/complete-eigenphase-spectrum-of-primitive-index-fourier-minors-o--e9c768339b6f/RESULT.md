# Complete eigenphase spectrum of primitive-index Fourier minors over odd moduli

## Finding

Let \(N\ge3\) be odd, let \(U_N=(\mathbb Z/N\mathbb Z)^\times\), and form the **unit-indexed principal compression of the unitary discrete Fourier transform**
\[
A_N=\bigl(N^{-1/2}\exp(2\pi i xy/N)\bigr)_{x,y\in U_N}.
\]
Rows and columns use the same order of units; simultaneous reorderings do not change the spectrum. This matrix is normal. Its complete **complex eigenvalue multiset**, including multiplicity, is given by the following prime-power rule.

Write \(N=\prod_j q_j\), where \(q_j=p_j^{k_j}\) are pairwise coprime prime powers. Define \(b_j\in U_{q_j}\) by
\[
b_j(N/q_j)\equiv1\pmod {q_j}.
\]
For a local pair \((q,b)=(p^k,b)\), define a multiset \(\mathcal M_{q,b}\):

* If \(k\ge2\), put \(h=(p-1)p^{k-2}\) and \(r=(p-1)^2p^{k-2}\). The eigenvalue \(0\) occurs \(h\) times, and **each** of \(1,-1,i,-i\) occurs \(r/4\) times.
* If \(k=1\), let \(s=(\frac bp)\in\{-1,1\}\) be the Legendre symbol. The eigenvalue \(-p^{-1/2}\) occurs once. If \(p\equiv1\pmod4\), the respective multiplicities of \(1,-1,i,-i\) are
  \[
  \frac{p-3+2s}{4},\quad\frac{p-3-2s}{4},\quad
  \frac{p-1}{4},\quad\frac{p-1}{4}.
  \]
  If \(p\equiv3\pmod4\), those multiplicities are
  \[
  \frac{p-3}{4},\quad\frac{p-3}{4},\quad
  \frac{p-1+2s}{4},\quad\frac{p-1-2s}{4}.
  \]

**Complete global rule:** the eigenvalues of \(A_N\) are all products \(\prod_j\lambda_j\), with \(\lambda_j\in\mathcal M_{q_j,b_j}\). Multiply their local multiplicities and add contributions when distinct tuples produce the same numerical eigenvalue. This is an explicit, finite, prime-factorization formula for every odd modulus, without unspecified spectral roots.

The associated local eigenspaces also have **explicit orthogonal projectors**. Define the local matrix \(A=A_{q,b}\) with entries \(q^{-1/2}e^{2\pi ibxy/q}\). If \(k\ge2\), partition \(U_q\) into its fibers modulo \(p^{k-1}\) and let \(K\) subtract the mean within each fiber. Then \(P_0=I-K\), and for \(\lambda\in\{1,-1,i,-i\}\),
\[
P_\lambda=\frac14\sum_{j=0}^3\lambda^{-j}A^jK.
\]
If \(k=1\), let \(Q\) be orthogonal projection onto the constant vector and put \(E=I-Q\). Then \(Q\) projects onto the \(-p^{-1/2}\) eigenspace, and
\[
P_\lambda=\frac14\sum_{j=0}^3\lambda^{-j}A^jE
\]
projects onto the respective fourth-root eigenspace. The Chinese remainder identification converts tensor products of these local projectors into a complete global eigenspace decomposition; projectors for coincident product eigenvalues are summed.

For clarity, a consequence of the full spectral law is the arithmetic conditioning formula. If \(r(N)\) denotes the rank, then
\[
r(N)=\prod_{p^1\parallel N}(p-1)\prod_{p^k\parallel N,\ k\ge2}(p-1)^2p^{k-2}.
\]
Every positive singular value is a product of local values \(1\) or \(p^{-1/2}\), and the ratio of the largest to the smallest **positive** singular value is
\[
\kappa_{\mathrm{nz}}(A_N)=\sqrt{\prod_{p^1\parallel N}p}.
\]
Thus the unit-indexed principal Fourier matrix is nonsingular exactly for squarefree odd \(N\), in which case its condition number is \(\sqrt N\). This rank and conditioning consequence is not the primary novelty claim: the finding concerns the **complex eigenphases and their complete eigenspaces**, which are not determined by singular values alone.

## Assumptions and scope

The Fourier sign is **positive**: \(e_q(t)=\exp(2\pi it/q)\). With the negative sign all eigenvalues are complex conjugated. The normalization is \(1/\sqrt N\), not \(1/\sqrt{\varphi(N)}\). Every prime dividing \(N\) is odd; even moduli and arbitrary nonunit-indexed minors are excluded. The Legendre symbol and the modular inverses in the formula are intrinsic finite arithmetic data. In particular, the local twists \(b_j\) must not be silently replaced by \(1\) in a composite modulus.

## Proof

**1. Local Gram and square identity.** Fix an odd prime \(p\), an exponent \(k\ge1\), \(q=p^k\), and \(b\in U_q\). On \(\mathbb C^{U_q}\), put \(A_{x,y}=q^{-1/2}e_q(bxy)\), let \(R f(x)=f(-x)\), and let \(c_q(t)=\sum_{u\in U_q}e_q(ut)\) be the Ramanujan sum. Direct multiplication gives
\[
AA^*=A^*A=K,\qquad K_{x,z}=\frac{c_q(x-z)}q,
\qquad A^2=KR.
\]
The equalities hold because multiplication by the unit \(b\) permutes \(U_q\) and because \(c_q\) is real and even. Thus \(A\) is normal. The prime-power Ramanujan identity, obtained by subtracting all multiples of \(p\) from the full additive-character sum, is
\[
c_{p^k}(t)=
\begin{cases}
(p-1)p^{k-1},&p^k\mid t,\\
-p^{k-1},&p^{k-1}\mid t\text{ but }p^k\nmid t,\\
0,&p^{k-1}\nmid t.
\end{cases}
\]
For \(k=1\) it says \(K=I-J/p\) on the \(p-1\) unit coordinates. For \(k\ge2\) it says \(K=\bigoplus (I_p-J_p/p)\) across the \((p-1)p^{k-2}\) fibers modulo \(p^{k-1}\). Here \(J\) is the all-ones matrix of the indicated size. In particular \(K\) is an orthogonal projection when \(k\ge2\), and its rank is \((p-1)^2p^{k-2}\). It commutes with reflection \(R\).

**2. Repeated prime factors.** Suppose \(k\ge2\). Normality, \(A^*A=K\), and \(K^2=K\) show that \(A\) vanishes on \(\ker K\) and is unitary on \(\operatorname{ran}K\). There \(A^2=R\) and \(A^4=I\); hence the only nonzero eigenvalues are \(1,-1,i,-i\). Reflection sends each fiber labelled by a unit modulo \(p^{k-1}\) to the fiber with opposite label. No label is fixed because \(p\) is odd. Therefore
\[
\operatorname{tr}(A^2)=\operatorname{tr}(KR)=0.
\]
Also \(\operatorname{tr}A=0\). Indeed, split every unit into \(x=x_0+p^{k-1}t\) with \(p\nmid x_0\) and \(t\in\mathbb F_p\). Since \(2(k-1)\ge k\),
\[
e_q\bigl(b(x_0+p^{k-1}t)^2\bigr)
=e_q(bx_0^2)e_p(2bx_0t),
\]
and the sum over \(t\) vanishes because \(p\nmid2bx_0\). The two trace identities force equal \(1\)- and \(-1\)-multiplicities and equal \(i\)- and \(-i\)-multiplicities; the vanishing of \(\operatorname{tr}(A^2)\) forces the total real-root and imaginary-root multiplicities to agree. All four therefore equal one quarter of \(\operatorname{rank}K\). The zero multiplicity is \(\dim\ker K=(p-1)p^{k-2}\).

**3. First-power prime factors.** For \(k=1\), the constant vector has eigenvalue \(-p^{-1/2}\), since \(\sum_{y\ne0}e_p(bxy)=-1\) for each nonzero \(x\). On its orthogonal complement \(E\), \(K=I\) and \(A^2=R\), so the possible eigenvalues are again fourth roots of unity. As negation fixes no nonzero residue, \(\operatorname{tr}(R|_E)=-1\). If \(m_\lambda\) denotes a root multiplicity, this yields
\[
m_1+m_{-1}=\frac{p-3}{2},\qquad
m_i+m_{-i}=\frac{p-1}{2}.
\]
The remaining difference is evaluated by a **classical quadratic Gauss sum**:
\[
\operatorname{tr}(A|_E)
=p^{-1/2}\sum_{x\bmod p}e_p(bx^2)
=\left(\frac bp\right)
\begin{cases}1,&p\equiv1\pmod4,\\i,&p\equiv3\pmod4.\end{cases}
\]
The signs in this formula correspond to the stipulated positive Fourier convention. Equating the real and imaginary parts of \(m_1-m_{-1}+i(m_i-m_{-i})\) gives exactly the displayed integer multiplicities.

**4. Projectors and global assembly.** In case \(k\ge2\), \(A^4=K\), \(A\) is zero on \(\ker K\), and the four nonzero eigenvalues are fourth roots. Finite Fourier inversion on this four-point spectrum therefore gives the asserted \(P_\lambda\); the complement is \(I-K\). The same identity on \(E\) gives the \(k=1\) projectors, with \(Q\) accounting for the isolated eigenvalue. These projections are orthogonal because \(A\) is normal.

For coprime prime powers \(q_j\), the Chinese remainder identification \(U_N\cong\prod_jU_{q_j}\) transforms the phase exactly:
\[
e_N(xy)=\prod_j e_{q_j}(b_jx_jy_j),
\qquad b_j(N/q_j)\equiv1\pmod{q_j}.
\]
The normalization also factors. Thus the *same* coordinate permutation on rows and columns takes \(A_N\) to \(\bigotimes_j A_{q_j,b_j}\). The tensor product of the local orthogonal spectral decompositions proves the complete product-multiset rule and all stated eigenspace projectors. Finally, normality identifies singular values with eigenvalue moduli; multiplying the local lists yields the rank and conditioning formulas. The proof covers every odd \(N\ge3\).

## Verification

The standalone `CHECKER.py` uses only the Python standard library. Run `python CHECKER.py` with Python 3.8 or later. It verifies local matrix-square identities and the first four power traces against the proposed eigenvalue lists for several odd prime powers and both quadratic-residue twists, and checks the exact Chinese-remainder phase congruence over several composite odd moduli. A separate numerical eigensolver comparison, on nineteen prime-power and composite moduli through \(125\), found a maximum eigenvalue discrepancy below \(7\times10^{-15}\) in the tested floating-point environment. These finite tests corroborate, but do **not** substitute for, the all-modulus algebraic proof above. The only cited external identity in the proof is the standard quadratic Gauss-sum evaluation.

## Relationship to prior work

Ramanujan-sum analysis provides the arithmetic exponential-sum framework; the classical four-eigenphase decomposition of the **full** discrete Fourier transform motivates the spectral question. Known work on rank-deficient Fourier submatrices concerns rank geometry; later work on principal Fourier minors studies general invertibility and a squarefree conjecture. The statement here is about a *specific natural principal minor*: all unit residue indices, with **all complex eigenvalues, their multiplicities, and explicit orthogonal projectors**, for every odd modulus. The squarefree invertibility consequence is only a special-family fact, not a resolution of conjectures for arbitrary principal minors. An older paper on rank-deficient Fourier submatrices was located but its complete text was not accessible for direct comparison; an equivalent eigenphase formula there is a residual historical-priority risk.

## Limitations

The theorem excludes even moduli, other index masks, and negative-sign Fourier matrices unless eigenvalues are conjugated. Its arithmetic condition number is for the **nonzero** singular spectrum when the matrix is singular. No claim of exhaustive historical novelty or independent mathematical certification is made. The finite numerical checker does not prove universal statements; the proof uses the classical quadratic Gauss-sum sign evaluation.

## References

1. M. Planat, M. Minarovjech and M. Saniga, *Ramanujan sums analysis of long-period sequences and \(1/f\) noise*, arXiv:0812.2170v1, publicly posted 2008-12-11. https://arxiv.org/html/0812.2170v1
2. B. K. P. Horn, *Interesting eigenvectors of the Fourier transform*, Transactions of the Royal Society of South Africa 65 (2010), 100–106, DOI:10.1080/0035919X.2010.510665. https://people.csail.mit.edu/bkph/papers/Interesting_Eigenvectors_of_the_Fourier_Transform.pdf
3. A. Caragea and D. G. Lee, *On the principal minors of Fourier matrices*, arXiv:2409.09793. https://arxiv.org/html/2409.09793v3
4. S. Delvaux and M. Van Barel, *Rank-deficient submatrices of Fourier matrices*, K.U. Leuven technical report TW470 (2006), later Linear Algebra and its Applications 429 (2008), 1587–1605, DOI:10.1016/j.laa.2008.04.043. https://www.cs.kuleuven.be/publicaties/rapporten/tw/TW470.abs.html
