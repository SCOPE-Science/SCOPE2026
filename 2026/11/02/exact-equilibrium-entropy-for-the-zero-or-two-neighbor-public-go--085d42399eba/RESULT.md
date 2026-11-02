# Exact equilibrium entropy for the zero-or-two-neighbor public-goods game on triangular toroidal strips

## Finding
For every integer \(n\ge3\), let \(G_n=C_3\square C_n\) be the simple Cartesian product of a triangle and a cycle, with vertices distinguished by their row and column coordinates. Each vertex chooses \(0\) (inactive) or \(1\) (active), and its unique best response is \(1\) exactly when it has \(0\) or \(2\) active neighbors. Let \(E_n\) be the number of pure Nash equilibria, counting labeled-vertex action profiles.

There is an explicit integer \(64\times64\) transfer matrix \(M\), defined in the next section, such that
\[
E_n=\operatorname{tr}(M^n).
\]
Writing \(z\) for the characteristic-polynomial variable, its *complete* characteristic polynomial is
\[
\begin{aligned}
\det(zI-M)={}&z^{25}(z-1)^{10}(z+1)^5(z^2+z+1)^4\\
&\cdot(z^3-z^2-1)(z^3-z^2+1)\\
&\cdot(z^5+z^3-z^2+z-1)^2.
\end{aligned}
\]
If \(\lambda\) is the unique positive root of \(z^3-z^2-1=0\), then
\[
E_n\sim\lambda^n,\qquad \lambda\approx1.465571231876768,
\]
so the equilibrium entropy per column is exactly \(\log\lambda\), and per player is \((\log\lambda)/3\). The exact counts for \(n=3,4,5,6,7,8,9,10,11,12\) are, respectively, \(21,9,3,45,3,33,75,39,69,153\).

## Assumptions and scope
The network is a simple, undirected, unweighted, four-regular graph with three *distinct* vertices per column and \(n\ge3\) columns; columns \(i-1\) and \(i+1\) are distinct vertices even at \(n=3\). All players have identical strict best-response pattern
\[
T(k)=\begin{cases}1,&k\in\{0,2\},\\0,&\text{otherwise}.\end{cases}
\]
There is no stochastic choice, no indifference and no averaging over graph automorphisms. The output counts one equilibrium for each assignment to the \(3n\) individually located vertices.

Identify a column with its three-bit integer \(c\in\{0,\ldots,7\}\), with \(c_j\in\{0,1\}\) the row-\(j\) bit, \(j\in\{0,1,2\}\). Index the transfer states by ordered pairs \((p,c)\) of adjacent columns, hence \(64\) states. Define
\[
M_{(p,c),(c',q)}=\mathbf1_{\{c'=c\}}\prod_{j=0}^{2}
\mathbf1_{\left\{c_j=\mathbf1_{\{p_j+q_j+c_{j+1}+c_{j+2}\in\{0,2\}\}}\right\}},
\]
where the row subscripts are interpreted modulo three. This entry is either zero or one and is fully explicit.

## Proof
**Transfer bijection.** A player at row \(j\) in column \(i\) has precisely the two other rows of the same column plus row \(j\) in the preceding and following columns as neighbors. Therefore that player's action equals its strict best response exactly when the displayed local condition holds with \((p,c,q)=(c_{i-1},c_i,c_{i+1})\). The \(n\) local conditions simultaneously hold if and only if the closed walk of length \(n\) through transfer states \((c_{i-1},c_i)\) uses permitted transitions at every column. Its starting state is determined by the labeled column zero, so this is a bijection, not a quotient by rotations. Counting closed walks gives \(E_n=\operatorname{tr}(M^n)\) for every \(n\ge3\).

**Exact finite determinant.** Applying exact integer characteristic-polynomial elimination to the specified \(64\times64\) matrix yields the factored polynomial in the Finding. This finite identity can be verified directly with the complete `verify.py` program: it constructs every one of the \(4096\) potential matrix entries from the local Boolean rule, computes \(\det(zI-M)\) symbolically, and checks equality against the displayed product. The resulting matrix has exactly \(69\) nonzero entries. This is a *finite exact arithmetic identity* rather than inference from a list of sample counts; the program supplies an independently replayable determinant certificate.

**Leading eigenvalue.** The directed graph of \(M\) contains a unique largest strongly connected component on the following \(18\) states (states indexed by \(8p+c\)):
\[
\{11,13,19,22,25,26,29,30,37,38,41,43,44,46,50,51,52,53\}.
\]
Its characteristic polynomial is
\[
(z+1)^2(z^3-z^2-1)(z^3-z^2+1)(z^5+z^3-z^2+z-1)^2.
\]
This component is strongly connected by direct reachability in the explicitly specified finite graph; `verify.py` checks forward and backward reachability from every state. It contains directed simple cycles of lengths \(3\) and \(8\), with state sequences \((29,46,51)\) and \((11,30,53,41,13,46,51,25)\), respectively. Consequently its period is one. Perron–Frobenius theory makes its spectral radius a simple strictly dominant positive eigenvalue.

The cubic \(z^3-z^2-1\) has exactly one positive real root, lying in \((1,2)\). The cubic \(z^3-z^2+1\) is positive throughout the nonnegative real axis, attaining its minimum \(23/27\) at \(z=2/3\). The quintic \(Q(z)=z^5+z^3-z^2+z-1\) is strictly increasing on the nonnegative real axis, because
\[
Q'(z)=5z^4+2z^2+(z-1)^2>0\quad(z\ge0),
\]
and its one positive root lies in \((0,1)\). Thus the only positive root of the \(18\)-state component polynomial exceeding one is \(\lambda\); Perron–Frobenius identifies it as that component's spectral radius. Every other recurrent component has eigenvalues only among the roots of \(z^2-1\) and \(z^3-1\), as is also directly checked by the full factorization. Hence all other eigenvalues of \(M\) have modulus strictly below \(\lambda\). Since \(\lambda\) has algebraic multiplicity one, its contribution to \(\operatorname{tr}(M^n)\) is exactly \(\lambda^n\), proving \(E_n\sim\lambda^n\).

## Verification
Run `python verify.py` with Python at least 3.10 and SymPy at least 1.12. It rebuilds the transfer matrix from the game rule, proves the characteristic factorization by exact symbolic arithmetic, computes the ten integer traces for \(n=3,\ldots,12\), checks the \(18\)-state strongly connected block and the two explicit coprime cycle lengths, and independently brute-force enumerates all \(2^{3n}\) action profiles for \(n=3,4,5,6\). The brute-force computation checks every player's best response directly against all four actual neighbors and does not use the transfer matrix to decide validity. Every indicated check passed in a fresh execution.

The finite exhaustive tests independently check the encoding; they are not used as proof for arbitrary \(n\). The transfer bijection, exact characteristic-polynomial identity and Perron–Frobenius argument establish the infinite family.

## Relationship to prior work
Gilboa and Nisan's 2022 paper posed the complexity of exactly this nonmonotone zero-or-two-neighbor best-response pattern as an open problem. Gilboa (2023) and, independently, Klimm and Stahlberg (2023) established general NP-completeness for the pattern; Klimm and Stahlberg also describe active components of equilibria as singletons or cycles. These results are prior and not claimed here. The specific \(C_3\square C_n\) labeled-equilibrium sequence, factored transfer polynomial, and leading growth constant are the proposed new claims.

The choice of width three is structural rather than an arbitrary truncation: on every graph of maximum degree three, this particular pattern coincides with the parity-of-neighbor-count response and the fixed-point equations reduce to linear equations over \(\mathbf F_2\). In the first four-regular periodic strip \(C_3\square C_n\), the difference at four active neighbors makes that linear reduction invalid. The theorem supplies an explicit exact benchmark immediately beyond that parity-solvable regime.

## Limitations
No assertion is made for strips of larger width, heterogeneous players, weighted or directed edges, or action profiles modulo row/column symmetry. The transfer technique is standard; the claim of new mathematical information concerns its evaluated instance and the exact asymptotic, not the abstract existence of a finite transfer representation. An unindexed equivalent enumeration or an existing general specialized enumeration theorem remains an originality risk. No independent audit or external validation has been performed.

## References
- M. Gilboa and N. Nisan, *Complexity of Public Goods Games on Graphs*, arXiv:2207.04238, first public version July 9, 2022. https://arxiv.org/abs/2207.04238
- M. Gilboa, *A Characterization of Complexity in Public Goods Games*, arXiv:2301.11580, first public version January 27, 2023. https://arxiv.org/abs/2301.11580
- M. Klimm and M. J. Stahlberg, *Complexity of equilibria in binary public goods games on undirected graphs*, arXiv:2301.11849, first public version January 27, 2023. https://arxiv.org/abs/2301.11849
