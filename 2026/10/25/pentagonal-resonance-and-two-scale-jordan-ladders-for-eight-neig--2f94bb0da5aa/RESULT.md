# Pentagonal resonance and two-scale Jordan ladders for eight-neighbour parity on rectangular tori

## Finding
Fix integers \(a,b\geq0\), let \(k=2^a\), \(\ell=2^b\), \(m=5k\), \(n=5\ell\), \(K=\max(k,\ell)\), and \(L=\min(k,\ell)\). For the synchronous eight-neighbour binary-parity map \(F\) on the torus \(\mathbb Z/m\mathbb Z\times\mathbb Z/n\mathbb Z\), the invertible recurrent summand has dimension \(16k\ell\). The nilpotent Jordan blocks of \(F\) have the following exact multiset:

- If \(K=1\), nine blocks of size \(1\).
- If \(K\geq2\), \(8L\) blocks of size \(K\), and \(2L\) blocks of size \(K/2\).

Consequently every orbit becomes periodic after at most \(K\) updates, and this uniform bound for the specified torus is attained. There are exactly \(2^{16k\ell}\) recurrent binary configurations, and every recurrent phase has exactly \(2^{9k\ell}\) preimages under \(F^K\). For every integer \(t\geq0\), the number \(N_{\leq t}\) of configurations periodic by time \(t\) is
\[
N_{\leq t}=
\begin{cases}
2^{16},&K=1,\ t=0,\\
2^{25},&K=1,\ t\geq1,\\
2^{16k\ell+8L\min(t,K)+2L\min(t,K/2)},&K\geq2.
\end{cases}
\]
For \(K\geq2\), the fraction requiring all \(K\) updates before periodicity is exactly \(1-2^{-8L}\). At \(m=n=5\), the corresponding fraction is \(1-2^{-9}\).

## Assumptions and scope
Vertices are the pairs \((i,j)\) of integers modulo \(m\) and \(n\). Their eight distinct neighbours are \((i+u,j+v)\) with \(u,v\in\{-1,0,1\}\) and \((u,v)\ne(0,0)\). The state space is the binary vector space \(\mathbb F_2^{mn}\). Each vertex's new bit is the exclusive-or of its eight neighbours' previous bits; no own-state term is included. The specified circumferences \(m=5\cdot 2^a\), \(n=5\cdot2^b\) are both at least five, so this is the simple strong-product graph. A configuration has transient length \(t\) when \(t\) is the smallest nonnegative integer for which \(F^t\) lies on a periodic orbit.

## Proof
Work initially over an algebraic closure \(\mathbb F\) of \(\mathbb F_2\), and identify the state space with the group algebra
\[
\mathcal A=\mathbb F[x^{\pm1},y^{\pm1}]/(x^{5k}-1,y^{5\ell}-1).
\]
The update is multiplication by the Laurent polynomial
\[
f(x,y)=(1+x+x^{-1})(1+y+y^{-1})+1.
\]
This equals the sum of the eight required monomials in characteristic two. Because \(k,\ell\) are powers of two and \(5\) is odd, the Chinese-remainder decomposition gives \(25\) local factors indexed by fifth roots \((\zeta,\eta)\), each isomorphic to
\[
R_{\zeta,\eta}=\mathbb F[u,v]/(u^k,v^\ell),\qquad
x=\zeta(1+u),\ y=\eta(1+v).
\]
Put \(\lambda=\zeta+\zeta^{-1}\) and \(\mu=\eta+\eta^{-1}\). As \(\zeta\) ranges over the fifth roots, \(\lambda=0\) once and each of the two roots \(\alpha,\beta\) of \(z^2+z+1=0\) twice. In particular \(\alpha+\beta=\alpha\beta=1\). The constant coefficient of \(f\) on \(R_{\zeta,\eta}\) is \(\lambda+\mu+\lambda\mu\), which vanishes precisely for the pair \((0,0)\) and the eight ordered pairs of trace types \((\alpha,\beta)\), \((\beta,\alpha)\). Multiplication by \(f\) is a unit on the other sixteen local factors; these have total dimension \(16k\ell\) and comprise the invertible recurrent summand.

Assume without loss of generality \(k=K\geq\ell=L\). At any of the eight nontrivial zero factors, the reduction \(h(u)=f(\zeta(1+u),\eta)\) has a simple zero at \(u=0\). Indeed, the coefficient of \(u\) is \(\lambda(1+\mu)\ne0\), since \(\lambda\in\{\alpha,\beta\}\) and \(\mu\) is the other root. Thus \(h(u)=cu+O(u^2)\), \(c\ne0\). The \(KL\) elements \(v^j f^t\), with \(0\leq j<L\) and \(0\leq t<K\), form a basis: under the filtration by powers of \(v\), their respective leading coefficients for a fixed \(j\) are \(h(u)^t\), a basis of \(\mathbb F[u]/(u^K)\). Furthermore \(f^K=0\) on that local factor: the positive-degree part has zero \(K\)-th power by the Frobenius identity and \(u^K=v^K=0\). Multiplication by \(f\) therefore shifts each chain \(v^j,v^j f,\ldots,v^j f^{K-1}\), proving exactly \(L\) Jordan blocks of size \(K\) per nontrivial zero factor, or \(8L\) in total.

At the remaining factor \(\zeta=\eta=1\), write \(x=1+u\), \(y=1+v\), and put \(A=u^2/(1+u)\), \(B=v^2/(1+v)\). The local update is \(f=A+B+AB\). If \(K\geq2\), then \(f^{K/2}=0\), since \(A^{K/2}=B^{K/2}=0\) in the truncated algebra. The \(KL\) elements \(u^\epsilon v^j f^t\), for \(\epsilon\in\{0,1\}\), \(0\leq j<L\) and \(0\leq t<K/2\), form a basis. Indeed, their leading coefficients in the \(v\)-filtration are \(u^\epsilon A(u)^t\), whose distinct lowest powers are \(u^{2t+\epsilon}\), ranging across all \(K\) exponents. Hence there are exactly \(2L\) Jordan blocks of size \(K/2\). If \(K=1\), the local ring at this factor is one-dimensional and \(f=0\), giving one size-one block. Together with the eight nontrivial zero factors, this proves the asserted nilpotent block multiset.

The base extension does not change ranks of matrices defined over \(\mathbb F_2\), so the ranks and block multiplicities hold over \(\mathbb F_2\). The Fitting decomposition identifies a state as eventually periodic precisely when its nilpotent coordinate has vanished. Counting the kernel of the \(t\)-th nilpotent iterate gives the stated formula for \(N_{\leq t}\). The largest block provides a state of transient length \(K\). Every fibre over a recurrent phase under \(F^K\) is an affine copy of the \(9k\ell\)-dimensional nilpotent summand. For \(K\geq2\), the difference of kernel dimensions between times \(K\) and \(K-1\) is \(8L\), proving the last-step fraction; for \(K=1\) it is nine. This completes the proof.

## Verification
The standalone `VERIFY.py` implements the eight periodic neighbours directly and tests the ranks of all iterates through the predicted stabilization time using binary Gaussian elimination, independently of the local-algebra argument. It verifies all predicted ranks for nine toroidal sizes up to \(40\times40\), along with the nine-versus-sixteen decomposition of fifth-root trace pairs in \(\mathbb F_4\). The supplied `VERIFIER_OUTPUT.txt` records an execution. These finite checks corroborate, but do not replace, the algebraic proof for arbitrary \(a,b\).

## Relationship to prior work
Martin, Odlyzko and Wolfram (1984), especially Section 4D, develop the general bivariate polynomial formalism for additive two-dimensional periodic automata, including eight-neighbour rules. Ekhad, Sloane and Zeilberger's March 2015 odd-rule classification treats precisely the same Moore local polynomial as Odd-rule 757, but on the infinite square lattice with the growth sequence from a single active cell, rather than a finite-torus all-state attractor census. Siap, Akin and Uguz (2013) consider a different, axial-offset, periodic rule over the ternary field. Omirov, Redjepov and Usmonov (2024) investigate finite Moore cellular automata with mixed boundary conditions and reversibility matrices. None of these inspected results states the fifth-root zero-mode count, the two distinct Jordan ladder scales on these binary tori, or the resulting sharp transient census. The broad polynomial machinery is credited as prior art; the specific finite-ring calculation is the contribution.

## Limitations
The theorem is restricted to the indicated \(5\)-times-a-power-of-two rectangular tori and the exactly eight-neighbour XOR rule. It does not determine primitive cycle lengths within the invertible recurrent summand, and it gives no analogous formula for arbitrary circumferences, changed self-interaction, or nonlinear rules. Historical noncoverage is based on accessible primary texts and searches, not an exhaustive proof of novelty; an unindexed equivalent may exist. No independent mathematical audit has been performed.

## References
1. O. Martin, A. M. Odlyzko, S. Wolfram, *Algebraic Properties of Cellular Automata*, Communications in Mathematical Physics **93** (1984), 219–258. Original complete text: https://www-users.cse.umn.edu/~odlyzko/doc/arch/cellular.automata.pdf (especially Section 4D).
2. S. B. Ekhad, N. J. A. Sloane, D. Zeilberger, *Odd-Rule Cellular Automata on the Square Grid*, first author posting dated 2015-03-12, https://sites.math.rutgers.edu/~zeilberg/mamarim/mamarimhtml/3x3.html ; arXiv:1503.04249v1 (2015-03-13), https://arxiv.org/abs/1503.04249 (especially Sections 2–4, Odd-rule 757).
3. I. Siap, H. Akin, S. Uguz, *2-D Reversible Cellular Automata with Nearest and Prolonged Next Nearest Neighborhoods under Periodic Boundary*, European Journal of Pure and Applied Mathematics **6** (2013), 315–334, https://www.ejpam.com/ejpam/article/view/2011.
4. B. A. Omirov, Sh. B. Redjepov, J. B. Usmonov, *2D Moore CA with new boundary conditions and its reversibility*, arXiv:2406.06195v1 (2024), https://arxiv.org/abs/2406.06195.
