# Exact resonance corrections and rank revival in cycle–clique quantum mixing

## Finding

For all integers \(n\geq5\) and \(q\geq3\), let \(G_{n,q}=C_n\square K_q\) be the unweighted Cartesian product of a cycle and a clique. Its continuous-time adjacency quantum walk has the infinite-time average mixing matrix
\[
\widehat M_{n,q}=\lim_{T\to\infty}\frac1T\int_0^T e^{itA(G_{n,q})}\circ\overline{e^{itA(G_{n,q})}}\,dt.
\]
This result determines every eigenvalue of \(\widehat M_{n,q}\), with a natural Fourier eigenbasis, and identifies exactly when long-time mixing of a Cartesian product fails to factor into the average mixing matrices of its two factors.

Set \(B_n(0)=n\). For \(1\leq h<n\), define
\[
B_n(h)=\begin{cases}1,&n\text{ odd},\\2,&n\text{ even and }h\text{ even},\\0,&n\text{ even and }h\text{ odd}.\end{cases}
\]
Define \(C_{n,q}(h)\), for \(0\leq h<n\), by the **complete** table
\[
C_{n,q}(h)=\begin{cases}
1,&q=3,\ 3\mid n,\ n\text{ odd},\ h\in\{n/3,2n/3\},\\
2,&q=3,\ 3\mid n,\ n\text{ even},\ h\in\{n/3,2n/3\},\\
1,&q=4,\ 2\mid n,\ h=n/2,\\
0,&\text{otherwise}.
\end{cases}
\]
For every Fourier index \(0\leq h<n\), \(0\leq j<q\), the corresponding eigenvalue of \(\widehat M_{n,q}\) is exactly
\[
\boxed{\rho_{h,0}=\frac{B_n(h)}n,\qquad
\rho_{h,j}=\frac{(q-2)B_n(h)+2C_{n,q}(h)}{nq}\quad(1\leq j<q).}
\]
Multiplicity is one **per indexed Fourier character**, so equal displayed values are to be counted with their full character multiplicities. In particular all these eigenvalues are rational and nonnegative. They imply the sharp rank law
\[
\boxed{\operatorname{rank}\widehat M_{n,q}=\begin{cases}
nq,&n\text{ odd},\\
nq/2+3,&n\equiv2\pmod4\text{ and }q=4,\\
nq/2,&n\text{ even in all other cases}.
\end{cases}}
\]
Thus \(C_6\square K_4\) has rank \(15\) on \(24\) vertices, and \(C_{10}\square K_4\) has rank \(23\) on \(40\) vertices. The three modes that reappear in these cases each have eigenvalue exactly \(1/(2n)\); this is also the least strictly positive eigenvalue in the exceptional case.

Write \(F_h\) for the rank-one Fourier projection on \(\mathbb Z_n\), with entries \((F_h)_{ab}=n^{-1}e^{2\pi ih(a-b)/n}\), and \(P_q^\perp=I_q-J_q/q\). Then the **exact product-factorization law** is
\[
\begin{aligned}
\widehat M_{n,q}&=\widehat M(C_n)\otimes\widehat M(K_q)+R_{n,q},\\
R_{n,q}&=\begin{cases}
\displaystyle\frac{2t_n}{3n}(F_{n/3}+F_{2n/3})\otimes P_3^\perp,&q=3,\ 3\mid n,\\
\displaystyle\frac1{2n}F_{n/2}\otimes P_4^\perp,&q=4,\ 2\mid n,\\
0,&\text{otherwise},
\end{cases}
\end{aligned}
\]
where \(t_n=1\) for odd \(n\) and \(t_n=2\) for even \(n\). The two nonzero correction cases are mutually exclusive, and every nonzero correction is positive semidefinite. Consequently, factorization holds **if and only if** neither \(q=3\) with \(3\mid n\), nor \(q=4\) with \(2\mid n\), occurs. Not every failure of factorization increases rank: the rank revival is peculiar to \(q=4\) and \(n\equiv2\pmod4\).

## Assumptions and scope

Graphs are simple, finite and unweighted; adjacency, not Laplacian or normalized adjacency, is the Hamiltonian. The cycle has \(n\geq5\) vertices and the clique has \(q\geq3\), both integers. Matrix tensor factors follow the vertex order \((a,b)\in\mathbb Z_n\times\mathbb Z_q\). The symbol \(\circ\) is entrywise multiplication and the bar complex conjugation. Every limit exists by the finite spectral decomposition. The theorem is an exact infinite-time Cesàro-average statement, not an assertion of uniform mixing at any particular time. The smallest cases \(n=3,4\) also obey the formulas but are excluded from the claimed family because of their special identifications with previously studied Cartesian graph families.

The two factor matrices in the formula are explicitly
\[
\widehat M(K_q)=\left(1-\frac2q\right)I_q+\frac2{q^2}J_q,
\]
and
\[
\widehat M(C_n)=\begin{cases}
\displaystyle\frac{n-1}{n^2}J_n+\frac1n I_n,&n\text{ odd},\\
\displaystyle\frac{n-2}{n^2}J_n+\frac1n(I_n+T^{n/2}),&n\text{ even},
\end{cases}
\]
where \(T\) is the cyclic one-step shift on \(\mathbb Z_n\). These established factor formulas are reproduced to fix normalization.

## Proof

**1. Fourier decomposition and multiplicity counts.** The product is a Cayley graph on \(\Gamma=\mathbb Z_n\times\mathbb Z_q\). Its normalized characters are \(N^{-1/2}\chi_{r,s}\), where \(N=nq\), \(\chi_{r,s}(a,b)=e^{2\pi i(ra/n+sb/q)}\), and
\[
E_{r,s}=\lambda_r+\kappa_s,\qquad
\lambda_r=2\cos(2\pi r/n),\qquad
\kappa_s=\begin{cases}q-1,&s=0,\\-1,&s\ne0.\end{cases}
\]
For \(z\in\Gamma\) the time-dependent transition amplitude from the identity to \(z\) is \(N^{-1}\sum_{r,s}e^{itE_{r,s}}\chi_{r,s}(z)\). Integrating the absolute square in time retains *all and only* ordered equal-energy pairs. Fourier transformation of the resulting translation-invariant mixing kernel therefore gives
\[
\rho_{h,j}=\frac1N\#\{(r,s)\in\mathbb Z_n\times\mathbb Z_q:E_{r,s}=E_{r-h,s-j}\}.\tag{1}
\]
The factor \(1/N\), not \(1/N^2\), follows from the orthogonality sum over the \(N\) vertices. In particular \(\rho_{0,0}=1\).

Equal cyclic energies satisfy \(\lambda_r=\lambda_{r-h}\) if and only if \(h\equiv0\pmod n\) or \(2r\equiv h\pmod n\), because equality of real cosines means their arguments are congruent up to sign. Hence the number of solutions \(r\) is exactly \(B_n(h)\). For \(j=0\), any of the \(q\) transverse indices keeps its transverse energy, and (1) yields \(\rho_{h,0}=B_n(h)/n\).

For \(j\ne0\), exactly \(q-2\) choices of \(s\) have both \(s\ne0\) and \(s-j\ne0\), contributing \((q-2)B_n(h)\). The remaining two choices \(s=0,j\) have different transverse energies and require a cyclic energy gap of magnitude \(q\). Define
\[
C_{n,q}(h)=\#\{r\in\mathbb Z_n:\lambda_{r-h}-\lambda_r=q\}.\tag{2}
\]
The two signs of the energy gap contribute equally: the involution \(r\mapsto h-r\), together with \(\lambda_{-r}=\lambda_r\), bijects their solutions. Thus (1) becomes
\[
\rho_{h,j}=\frac{(q-2)B_n(h)+2C_{n,q}(h)}{nq},\qquad j\ne0.\tag{3}
\]

**2. Exhaustive arithmetic classification of cross-band gaps.** The numbers \(\lambda_r\) are totally real algebraic integers. All of their algebraic conjugates are again sums of a root of unity and its inverse, hence lie in \([-2,2]\). Suppose \(\alpha,\beta\) are two such energies with \(\alpha-\beta=q\ge3\). For \(q\ge5\) this is impossible since both lie in \([-2,2]\). When \(q=4\), the only possibility is \((\alpha,\beta)=(2,-2)\). The value \(-2\) occurs exactly when \(n\) is even, at index \(n/2\), while \(2\) occurs only at index \(0\). Consequently (2) equals one exactly at \(h=n/2\) for even \(n\) and is zero elsewhere.

When \(q=3\), every algebraic conjugate of \(\alpha\) lies in \([1,2]\): apply each Galois embedding to \(\beta=\alpha-3\) and use \(\beta^\sigma\ge-2\). Therefore \(\alpha-1\) is an algebraic integer with all conjugates in \([0,1]\). If it vanishes, \(\alpha=1\). If nonzero, its absolute algebraic norm is a positive integer at most one, hence all conjugates are one and \(\alpha=2\). These are the *only* possibilities, yielding exactly
\[
(\alpha,\beta)=(2,-1)\quad\text{or}\quad(1,-2).\tag{4}
\]
The first pair occurs precisely when \(3\mid n\) (the indices of \(-1\) are \(n/3,2n/3\)); its ordered difference in (2) gives one solution for each \(h=n/3,2n/3\). The second requires \(6\mid n\) (the indices of \(1\) are \(n/6,5n/6\), and \(-2\) occurs at \(n/2\)); it contributes one additional solution at each of those same \(h\). If \(3\nmid n\), neither pair occurs. This proves the complete stated table for \(C_{n,q}(h)\), without assuming that numerical enumeration exhausts the possible cosine equalities.

**3. Spectrum, factorization, and rank.** Equations (1)–(4) establish every displayed Fourier eigenvalue. Taking \(C_{n,q}\equiv0\) in (3) produces exactly the product of the Fourier eigenvalues of \(\widehat M(C_n)\) and \(\widehat M(K_q)\). At the exceptional frequencies the remaining eigenvalue correction is \(2C_{n,q}(h)/(nq)\), for every \(j\ne0\). Since \(F_h\) projects onto precisely the \(h\)-th Fourier mode and \(P_q^\perp\) onto the nonzero clique Fourier modes, this yields the matrix identity and the stated necessary and sufficient factorization criterion. The correction is nonzero exactly in the table's two resonance cases and is positive semidefinite.

For odd \(n\), every \(B_n(h)\) is positive and \(q-2\ge1\), so all \(nq\) modes are positive. For even \(n\), all \(h\) even modes are positive and all \(h\) odd modes initially vanish: this contributes \(nq/2\) positive modes. A \(q=3\) resonance has \(h=n/3\) or \(2n/3\); whenever \(n\) is even and divisible by three, these frequencies are even, so it cannot revive a zero mode. A \(q=4\) resonance has \(h=n/2\), which is odd precisely when \(n\equiv2\pmod4\). It then revives exactly the three nontrivial transverse modes, each by \(2/(4n)=1/(2n)\), yielding the additional rank three. In that case all other positive nontrivial eigenvalues are at least \(1/n\) (and \(\rho_{0,0}=1\)), proving the asserted least positive eigenvalue.

## Verification

The attached `verify.py` independently constructs the full adjacency matrix of each graph from its edge definition, diagonalizes it numerically, groups equal energies, constructs the average as the sum of spectral-projector entrywise squares, and compares **all matrix entries** and **all Fourier eigenvalues** with the rational formulas above. It also verifies normalization, the rank, the exact presence of a correction, and the two explicit rank-revival examples. Run `OPENBLAS_NUM_THREADS=1 python3 verify.py` with Python 3 and NumPy installed.

For \(3\le n\le16\), \(3\le q\le8\), the executed checks covered 84 graphs, 4,389 Fourier eigenmodes and 296,709 matrix entries. The maximum absolute matrix discrepancy was about \(1.11\times10^{-15}\). Exact rational assertions include \(\rho_{3,1}=1/12\) for \((n,q)=(6,4)\), and \(\rho_{5,1}=1/20\) for \((10,4)\). A separate wider numerical sweep covered 138 graphs through \(n=25\) and 10,626 modes. These are finite corroborations, not the infinite-family proof: that is furnished by the preceding group/Fourier and algebraic-integer arguments.

## Relationship to prior work

Godsil [1] established the spectral-projector formula for average mixing and derived the exact cycle average. Coutinho, Godsil, Guo and Zhan [2] developed general average-mixing rank theory. Lo, Rajaram, Schepens, Sullivan, Tamon and Ward [3] studied continuous-time mixing on circulant bunkbeds, including path–circulant Cartesian products and average near-uniformity; their results do not specify this cycle–clique product's complete average-mixing spectrum or distinguish the two exact cross-band resonance families. Baptista, Coutinho and Marques [4] studied nontrivial covariance and trace effects in Cartesian-product mixing: the product of the factor averages need not be the average of the product walk. The present formulas classify exactly when that obstruction occurs within the cycle–clique family and determine its spectral, rather than merely trace, consequences. Coutinho, Baptista, Godsil, Spier and Werner [5] provided general exact methods for quantum walks with integral Hamiltonians, including average mixing. These established algorithms do not themselves state the present closed uniform-parameter resonance table. Earlier classifications of cycles, prisms, cube–clique products and path–clique products treat related but different parameter families; small-order graph coincidences are not presented as new here.

The use of elementary Fourier theory, spectral projectors, cosine parity and algebraic integers is standard. The claim is their exact synthesis into the resonance corrections, necessary/sufficient factorization test, and all-parameter rank law for this graph family, not a new spectral-projector principle. Unlocated equivalent formulations and stronger general product theorems remain originality risks.

## Limitations

The result is for the unweighted, finite, undirected adjacency-Hamiltonian Cartesian product \(C_n\square K_q\). It does not prove instantaneous uniform mixing, fractional revival, optimal mixing times, robustness under perturbation, or analogous rank statements for other graph products, Hamiltonian weights, or Laplacian walks. It supplies no claim that the formulas cannot follow from a more general theorem in literature not inspected. The numerical verifier tests only the finite sample documented above; all unrestricted quantifiers rest on the explicit proof. Independent external audit has not been performed.

## References

[1] Chris Godsil, *Average Mixing of Continuous Quantum Walks*, arXiv:1103.2578 (2011), https://arxiv.org/abs/1103.2578.

[2] Gabriel Coutinho, Chris Godsil, Krystal Guo and Hanmeng Zhan, *A New Perspective on the Average Mixing Matrix*, arXiv:1709.03591 (2017), https://arxiv.org/abs/1709.03591.

[3] Peter Lo, Siddharth Rajaram, Diana Schepens, Daniel Sullivan, Christino Tamon and Jeffrey Ward, *Mixing of Quantum Walk on Circulant Bunkbeds*, arXiv:quant-ph/0509059 (2005), https://arxiv.org/abs/quant-ph/0509059.

[4] Pedro Baptista, Gabriel Coutinho and Ana Cláudia Marques, *Unexpected Averages of Mixing Matrices*, arXiv:2308.16378 (2023), https://arxiv.org/abs/2308.16378.

[5] Gabriel Coutinho, Pedro Ferreira Baptista, Chris Godsil, Thomás Jung Spier and Reinhard Werner, *Irrational quantum walks*, arXiv:2208.08971v1 (public 2022-08-18; primary MSC 81P68), https://arxiv.org/abs/2208.08971.
