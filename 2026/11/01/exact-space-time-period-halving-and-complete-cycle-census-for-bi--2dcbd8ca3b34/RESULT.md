# Exact space–time period halving and complete cycle census for binary ring-coupled cat maps

## Finding
Let \(m\ge 2\), \(n=2^m\), and \(S\) be the cyclic one-site shift on \(\mathbb F_2^n\). On the binary phase space \(\mathbb F_2^n\times\mathbb F_2^n\), put \(C=S+S^{-1}\) and define
\[
T(q,p)=(q+Cp,\;Cq+(I+C^2)p).
\]
For a phase state \(z=(q,p)\), let \(d(z)\) be the smallest positive integer for which \(S^{d(z)}q=q\) and \(S^{d(z)}p=p\). Necessarily \(d(z)\) divides \(n\), so it is a power of two. **The least positive temporal period of every state is exactly**
\[
\boxed{\pi(z)=\max\{1,\,d(z)/2\}.}
\]
More precisely, for every integer \(j\ge0\),
\[
\operatorname{Fix}(T^{2^j})=
\{(q,p):S^{2^{j+1}}q=q,\quad S^{2^{j+1}}p=p\},
\]
and for every positive integer \(t\), \(\operatorname{Fix}(T^t)=\operatorname{Fix}(T^{2^{\nu_2(t)}})\).

Consequently the number of states of period dividing \(2^j\) is
\[
F_j=2^{2\min(n,2^{j+1})}.
\]
There are exactly \(16\) fixed states; for \(1\le j\le m-1\), there are
\[
E_j=2^{2^{j+2}}-2^{2^{j+1}}
\]
states of primitive temporal period \(2^j\), forming exactly \(E_j/2^j\) cycles. Every other period is absent. In particular the order of \(T\) as a permutation is precisely \(n/2\).

## Assumptions and scope
The ring contains exactly \(n=2^m\ge4\) sites with periodic boundary conditions. Every position and momentum coordinate belongs to the field \(\mathbb F_2\), not to a continuum or to a higher-modulus ring. Matrix sums, products, kernels, and iterates in the statement are evaluated in characteristic two. The matrix \(C=S+S^{-1}\) is the loopless nearest-neighbor circulant coupling, whose integer lift is the standard symmetric coupled-cat-map form with no onsite term. Here \(S\) acts identically on each of the two phase blocks, and the least common spatial period is taken jointly, not separately for positions and momenta.

## Proof
Write the phase update as the block matrix
\[
M=\begin{pmatrix}I&C\\C&I+C^2\end{pmatrix}=L^2,
\qquad L=\begin{pmatrix}0&I\\I&C\end{pmatrix}.
\]
The matrix \(L\) is invertible, because
\[
L^{-1}=\begin{pmatrix}C&I\\I&0\end{pmatrix}
\]
in characteristic two. Define \(D=\operatorname{diag}(C,C)\). Direct multiplication gives
\[
M-I=DL=LD=\begin{pmatrix}0&C\\C&C^2\end{pmatrix}.
\]
Since \(D\) and \(L\) commute and \(L\) is invertible, the kernel of \((M-I)^r=D^r L^r\) equals the kernel of \(D^r\) for every positive integer \(r\).

For \(j\ge0\), the characteristic-two Frobenius identity yields
\[
M^{2^j}-I=(M-I)^{2^j}.
\]
Furthermore, since \(S\) is invertible,
\[
C=S^{-1}(S+I)^2,\qquad
C^{2^j}=S^{-2^j}(S+I)^{2^{j+1}}
=S^{-2^j}(S^{2^{j+1}}+I).
\]
Thus \(C^{2^j}v=0\) exactly when \(S^{2^{j+1}}v=v\). Applying this to both phase blocks proves the displayed fixed-point identity for every \(j\ge0\). In particular \(M^{n/2}=I\): indeed \(S^n=I\), and \(n/2\) is a positive power of two.

To rule out odd factors in the least temporal period, first note that \(S^n=I\) and \(n=2^m\) imply \((S+I)^n=S^n+I=0\). Consequently \(C\), then \(D\), and then \(M-I=DL\) are nilpotent. Therefore \(M\) is unipotent. If \(t=2^j u\) with \(u\) odd, put \(A=M^{2^j}\). Then
\[
M^t-I=(A-I)(I+A+\cdots+A^{u-1}).
\]
The second factor is an invertible polynomial in the unipotent matrix \(A\), since its constant value at \(A=I\) is \(uI=I\) in characteristic two. It commutes with \(A-I\), hence the kernels of \(M^t-I\) and \(A-I\) coincide. This proves the statement for arbitrary \(t\).

Because the possible common spatial periods are exactly divisors of \(n\), the first temporal power \(2^j\) fixing \(z\) has \(2^{j+1}\ge d(z)\), proving \(\pi(z)=\max\{1,d(z)/2\}\). A binary word fixed by shift \(S^{2^{j+1}}\) is determined by exactly \(\min(n,2^{j+1})\) free bits; choosing the two blocks independently gives \(F_j=2^{2\min(n,2^{j+1})}\). Subtracting successive cumulative counts gives \(E_0=F_0=2^4=16\) and \(E_j=F_j-F_{j-1}\) for \(1\le j\le m-1\); division by \(2^j\) counts primitive cycles. There are phase vectors of full spatial period \(n\) (for example a single \(1\) among all sites in one block), so the maximal temporal period \(n/2\) is attained and the permutation order is exactly \(n/2\). This completes the proof.

## Verification
Run `python3 verify_binary_cycles.py` with Python 3 and no third-party dependencies. The standalone program exhaustively enumerates every one of the \(2^8=256\) states at \(n=4\) and every one of the \(2^{16}=65,536\) states at \(n=8\), comparing the true least temporal period with half the common spatial period. It independently computes fixed-point counts using binary matrix ranks at \(n=4,8,16,32\). The exact output is:

`exhaustive 4 states 256 period census [(1, 16), (2, 240)]`

`exhaustive 8 states 65536 period census [(1, 16), (2, 240), (4, 65280)]`

`rank-and-order 4 passed; order 2`, `rank-and-order 8 passed; order 4`, `rank-and-order 16 passed; order 8`, `rank-and-order 32 passed; order 16`, followed by `ALL CHECKS PASSED`.

The all-size result is established by the preceding algebra, not by the finite checks.

## Relationship to prior work
Manolas and Floratos [1] give the coupled-cat-map block matrix and matrix-Fibonacci period method. Their Section 4.1 investigates periodicity of the evolution matrix on finite toroidal lattices and reports numerical period spectra, without the present every-state space–time period correspondence or the dyadic-ring cycle census. Axenides, Floratos, and Nicolis [2], Section 6, formulate a general algorithm for matrix order using Fibonacci matrix polynomials, also without an explicit nearest-neighbor binary-ring classification. Alderson, Dubertrand, and Shudo [3] count periodic orbits for a different coupled chain, with the displayed counting argument restricted to odd chain lengths; the present family has even length \(n=2^m\). General finite-field linear-algebraic techniques are used, not claimed as original. No unqualified priority claim is made against uninspected specialized cellular-automaton literature.

## Limitations
The proof uses both the binary field and dyadic site count essentially: \((S+I)^n=0\) and characteristic-two Frobenius identities do not transfer unchanged to odd site counts or to general phase modulus \(2^s\), \(s>1\). It does not assert that a finite permutation has positive entropy, and does not classify periodic trajectories on the full real torus. The formula concerns the specific nearest-neighbor coupling \(C=S+S^{-1}\) with no onsite term and does not immediately extend to arbitrary circulant couplings. Relevant historical-priority questions may remain in specialized finite-ring linear dynamics.

## References
[1] K. Manolas and E. Floratos, *Coupled Arnol'd cat maps on circulant graphs*, arXiv:2605.00965, first public version 2026-05-01, Section 3 and Section 4.1. https://arxiv.org/abs/2605.00965 ; https://arxiv.org/html/2605.00965v2

[2] M. Axenides, E. Floratos, and S. Nicolis, *Arnol'd cat map lattices*, arXiv:2208.03267, Section 6. https://arxiv.org/html/2208.03267v3

[3] W. Alderson, R. Dubertrand, and A. Shudo, *Classical transport in a maximally chaotic chain*, *Journal of Physics A* 58 (2025), article 165201, Section 3.3. https://arxiv.org/abs/2411.19828
