# Three–five resonance and exact extinction-depth census for binary parity on generalized Petersen graphs

## Finding
For every integer \(n\ge5\), the synchronous open-neighbour binary parity map on the generalized Petersen graph \(P(n,2)\) admits a complete nilpotent/invertible decomposition with an exact transient-depth census. Write
\[
 k=2^{\nu_2(n)},\qquad r=n/k,\qquad
 \alpha=\mathbf1_{3\mid r},\quad \beta=\mathbf1_{5\mid r},\qquad
 d=2n-4k(\alpha+\beta).
\]
The zero-primary part has precisely \(2\alpha\) Jordan blocks of size \(2k\) and \(4\beta\) blocks of size \(k\). The remaining \(d\)-dimensional part is invertible. Consequently the recurrent-state count is
\[
 R_n=2^d,
\]
and the sharp maximal time at which a configuration first becomes periodic is
\[
 T_n=\max(2k\alpha,k\beta).
\]
For **every** integer \(t\ge0\), the number of configurations that have entered their eventual periodic orbit by time \(t\) is
\[
 H_n(t)=2^{d+2\alpha\min(t,2k)+4\beta\min(t,k)}.
\]
In particular, the map is a permutation exactly when \(\gcd(n,15)=1\). If \(T_n>0\), the fraction requiring the last possible transient update is \(3/4\) when \(3\mid n\); it is \(15/16\) when \(3\nmid n\) and \(5\mid n\). For each recurrent state the eventual-time map has exactly \(2^{4k(\alpha+\beta)}\) preimages.

## Assumptions and scope
The graph \(P(n,2)\) has vertices \(a_i,b_i\) for \(i\in\mathbb Z/n\mathbb Z\), with undirected edges \(a_i a_{i+1}\), \(a_i b_i\), and \(b_i b_{i+2}\). The restriction \(n\ge5\) ensures a simple cubic graph and distinct open neighbours. Configurations lie in \(\mathbb F_2^{2n}\). Simultaneously, the state at each vertex is replaced by the binary sum of its three neighbours' previous states, *without* including its own previous state. An initial configuration has **depth** \(t\) if \(t\) is the least nonnegative time after which it is on a periodic orbit. Here 'recurrent' means a configuration already on such an orbit at time zero; no specific primitive periods are asserted.

## Proof
**1. Laurent representation and singular roots.** Identify each ring's configurations with \(R=\mathbb F_2[x,x^{-1}]/(x^n-1)\), with shift \(x\), and put \(u=x+x^{-1}\). The transition is multiplication by
\[
 M(x)=\begin{pmatrix}u&1\\1&u^2\end{pmatrix},\qquad
 \det M=u^3+1.
\]
A direct calculation in characteristic two yields
\[
 x^3\det M=(x^2+x+1)(x^4+x^3+x^2+x+1).
\]
Thus the only singular frequencies over an algebraic closure are the two primitive cube roots and the four primitive fifth roots; the cyclotomic factors are squarefree. Since \(n=kr\), where \(r\) is odd and \(k\) is a power of two, \(x^n-1=(x^r-1)^k\). Each allowed frequency therefore occurs on a local truncated ring of length \(k\). Frequencies outside these six roots support an invertible operator. This local splitting is valid over a finite splitting field; ranks and Jordan multiplicities of the zero-primary part do not change under scalar extension.

**2. Primitive cube roots.** At a primitive cube root \(\zeta\), \(u(\zeta)=1\). The element \(z=u+1\) is a local uniformizer, because \(du/dx=1+x^{-2}\) is nonzero at \(\zeta\). Substituting \(u=1+z\) gives the exact identity
\[
 M^2=z\,U,\qquad
 U=\begin{pmatrix}z&1+z\\1+z&z^3\end{pmatrix}.
\]
The reduction of \(U\) modulo \(z\) is the exchange matrix, hence \(U\) is invertible. On the truncated local ring \(K[z]/(z^k)\), this implies
\[
 \operatorname{rank}M^{2j}=2\max(k-j,0).
\]
Further, \(M\) has Smith exponents \(0,1\) over the local discrete valuation ring: one entry is a unit and \(\det M\) has a simple zero. Because \(U\) is a commuting unit, for each odd exponent the rank is
\[
 \operatorname{rank}M^{2j+1}=\max(2k-2j-1,0).
\]
Together these equal \(\max(2k-t,0)\) for every nonnegative integer \(t\). Hence each primitive cube root contributes **one nilpotent Jordan block of length \(2k\)**. There are two such roots when \(3\mid r\).

**3. Primitive fifth roots.** At a primitive fifth root \(\zeta\), the value \(u(\zeta)\) satisfies \(u^2+u+1=0\), so \(\operatorname{tr}M=u+u^2=1\), while \(\det M=0\). Thus the characteristic polynomial of the reduced matrix has distinct eigenvalues \(0\) and \(1\). The characteristic-polynomial factors lift uniquely to coprime linear factors over the complete local ring (or by the elementary spectral idempotents/Hensel lifting). One eigenvalue is a unit. The other has order exactly one as a local uniformizer, because \(\det M\) has a simple zero at \(\zeta\). On a length-\(k\) truncated ring, the nilpotent part is therefore **one Jordan block of length \(k\)**, while the other \(k\)-dimensional part remains invertible. There are four primitive fifth roots when \(5\mid r\).

**4. Assembly and counting.** The complete zero-primary Jordan decomposition consists of \(2\alpha\) blocks of size \(2k\) and \(4\beta\) blocks of size \(k\). Their total dimension is \(4k(\alpha+\beta)\), leaving \(d\) invertible dimensions. The nilpotent rank after \(t\) steps is
\[
 2\alpha\max(2k-t,0)+4\beta\max(k-t,0).
\]
A state becomes periodic by time \(t\) exactly when its nilpotent coordinate lies in the kernel of the \(t\)-th nilpotent power. Counting these kernels gives \(H_n(t)\) above. The largest nilpotent block gives the sharp time \(T_n\) (zero if no such block exists). At time \(T_n\), every recurrent state is reached by precisely one invertible-component preimage times all \(2^{4k(\alpha+\beta)}\) nilpotent coordinates. Finally, when \(\alpha=1\), the largest block has multiplicity two, so \(1-H_n(T_n-1)/H_n(T_n)=1-2^{-2}=3/4\); when \(\alpha=0,\beta=1\), its multiplicity is four and the fraction is \(1-2^{-4}=15/16\). This proves every assertion.

## Verification
The accompanying standalone standard-library Python program, `verification/verify_gp.py`, builds the open-neighbour transition matrix directly from the graph definition, computes binary ranks of all successive powers, and compares them with
\[
 \operatorname{rank}F_n^t=d+2\alpha\max(2k-t,0)+4\beta\max(k-t,0).
\]
It checked \(642\) exact rank instances covering all \(5\le n\le96\), and exhaustively classified all \(2^{10}\) states for \(n=5\) and all \(2^{12}\) states for \(n=6\). The recorded output in `verification/verification_output.txt` ends in `GP_PARITY_VERIFICATION_OK states= 5120`. The exhaustive experiments corroborate, but do not replace, the all-parameter local-algebra proof.

For illustrations, \(n=5\) gives \(64\) recurrent states and sharp depth one; \(n=6\) gives \(16\) recurrent states and sharp depth four. These values are obtained independently by the displayed formulas and by direct exhaustive simulation.

## Relationship to prior work
The real adjacency spectra of generalized Petersen graphs are described by Gera and Stănică (2011), and refined in Dudek (arXiv:1412.3531, first posted 11 December 2014). Oliveira and Vinagre (arXiv:1511.03513, first posted 11 November 2015) also study real spectral zeroes of \(I\)-graphs, including generalized Petersen graphs. Those real-spectrum calculations do not determine characteristic-two higher-power ranks or the all-state basin-depth census; the distinction is essential because reduction modulo two may merge eigenvalues and create nilpotent chains.

Torrence and Torrence (2016) give a particularly relevant binary-field study of Lights Out on Petersen graphs. Their **\(\sigma^+\)** transition matrix is the *closed-neighbour* matrix \(A+I\), used as a one-step button-response map, whereas here the repeated synchronous map is **the open-neighbour adjacency matrix** \(A\). Their nonsingularity criterion and finite nullity table are not statements about the Jordan blocks of \(A\), the ranks of its powers, or depth distributions; these differences were checked against their full accessible article. Earlier linear cellular-automaton techniques are general background, not claimed as new here.

## Limitations
Only transient depths and periodic-state totals are classified. The primitive periods **within** the invertible component are not enumerated. The novelty assessment is bounded by the inspected accessible literature and searchable records; it cannot exclude an unindexed equivalent or a hidden specialization of broader results. Finite computational checks do not constitute proof for untested sizes. The argument assumes \(n\ge5\), simple undirected adjacency, and coefficients in \(\mathbb F_2\); other states, neighbourhoods and update schedules are outside the claim.

## References
- Gera, R., and Stănică, P., *The spectrum of generalized Petersen graphs*, Australasian Journal of Combinatorics **49** (2011), 39–45. https://ajc.maths.uq.edu.au/pdf/49/ajc_v49_p039.pdf
- Dudek, A. W., *On the Spectrum of the Generalised Petersen Graphs*, arXiv:1412.3531v1 (first publicly submitted 2014-12-11). https://arxiv.org/abs/1412.3531
- Oliveira, F., and Vinagre, C., *The spectrum of an I-graph*, arXiv:1511.03513v1 (first publicly submitted 2015-11-11). https://arxiv.org/abs/1511.03513
- Torrence, B., and Torrence, R., *An iterative strategy for Lights Out on Petersen graphs*, Involve **9** (2016), 719–734. https://msp.org/involve/2016/9-5/involve-v9-n5-p01-p.pdf
