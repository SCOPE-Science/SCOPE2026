# Arithmetic reversibility and dyadic transient clocks for binary parity dynamics on generalized Petersen graphs

## Finding
For every integer \(n\ge 7\), consider the synchronous binary open-neighbor parity automaton \(F_n\) on the cubic generalized Petersen graph \(GP(n,3)\). Put \(e=2^{\nu_2(n)}\) and \(\beta=\mathbf 1_{5\mid n}\). If \(5\nmid n\), every configuration is periodic from time zero. If \(5\mid n\), the rank of the \(t\)-th update for every integer \(t\ge0\) is
\[
\operatorname{rank}_{\mathbb F_2} F_n^t=2n-4\min(2t,e).
\]
Consequently exactly \(2^{2n-4e}\) initial configurations are periodic at time zero, and the number that have entered their eventual cycles by time \(t\) is
\[
C_n(t)=2^{2n-4e+4\min(2t,e)}.
\]
The number entering for the **first** time at \(t\ge1\) is exactly \(C_n(t)-C_n(t-1)\), and the sharp maximum first-entry time is \(\lceil e/2\rceil\). All periodic points are retained in the invertible component; no assertion about the lengths or number of their individual cycles is made.

More precisely, the nilpotent primary component has \(\mathbb F_2\)-dimension \(4e\). For \(e=1\) its Jordan form is four zero Jordan blocks of size one; for \(e\ge2\) it is eight zero Jordan blocks, each of size \(e/2\). The exact fixed-point count, valid whether or not \(5\mid n\), is
\[
\#\operatorname{Fix}(F_n)=2^{\min(4,e)+4\beta}.
\]
These formulas expose an arithmetic discontinuity: if \(n=5\cdot2^s\), \(s\ge1\), the maximum entrance time is \(n/10\), with only proportion \(2^{-4n/5}\) initially periodic; odd multiples of five instead have entrance time one and initially periodic proportion \(1/16\), and numbers not divisible by five have no transients.

## Assumptions and scope
The labelled graph \(GP(n,3)\) has vertices \(u_i,v_i\) indexed by \(i\in\mathbb Z/n\mathbb Z\), and edges \(u_i u_{i+1}\), \(u_i v_i\), and \(v_i v_{i+3}\). The restriction \(n\ge7\) ensures the displayed graph is simple and cubic. Configurations belong to \(\mathbb F_2^{2n}\). At each synchronous step, every vertex takes the sum modulo two of the current states of its three neighbors; its own current state is **not** separately included. A configuration first enters periodic behavior at time \(t\) if its state at time \(t\) belongs to a cycle of this finite deterministic map, but its state at time \(t-1\) does not, when \(t\ge1\). A state on a cycle at time zero has entrance time zero.

## Proof
Work in \(R=\mathbb F_2[z,z^{-1}]/(z^n-1)\), in which \(z\) is invertible. Identify the outer and inner color vectors with \(R\oplus R\). The update map is multiplication by
\[
B(z)=\begin{pmatrix}r&1\\1&s\end{pmatrix},\qquad r=z+z^{-1},\quad s=z^3+z^{-3}.
\]
Write \(\phi(z)=z^4+z^3+z^2+z+1\), the degree-four irreducible fifth cyclotomic polynomial over \(\mathbb F_2\): the multiplicative order of two modulo five is four. A direct expansion in characteristic two gives
\[
\det B=1+rs=z^{-4}(z^8+z^6+z^4+z^2+1)=z^{-4}\phi(z)^2.
\]
If \(5\nmid n\), then \(\phi\) does not divide \(z^n-1\), so the determinant is a unit in \(R\). Thus \(B\) is invertible and every point of the finite state space is periodic from time zero.

Suppose \(5\mid n\). Write \(n=em\) with \(e=2^{\nu_2(n)}\) and \(m\) odd. In characteristic two, \(z^n-1=(z^m-1)^e\); because \(m\) is odd, the polynomial \(z^m-1\) has no multiple roots. Hence \(\phi\) occurs with multiplicity exactly \(e\). By the Chinese remainder theorem, \(R\) splits into the \(\phi\)-primary factor \(R_\phi=\mathbb F_2[z]/(\phi^e)\) and a complementary factor on which \(B\) has unit determinant. The map is therefore invertible on the complementary two-copy factor, of binary dimension \(2n-8e\).

On \(R_\phi\), put \(\tau=r+s\). At a primitive fifth root \(\zeta\), \(r+s=\zeta+\zeta^2+\zeta^3+\zeta^4=1\), so \(\tau\equiv1\pmod\phi\). The characteristic polynomial of \(B\) is \(Y^2+\tau Y+\det B\), reducing to \(Y(Y+1)\pmod\phi\). Its two simple roots lift uniquely through the powers of \(\phi\) in the finite local ring \(R_\phi\): denote the lifted roots by \(a\equiv0\) and \(b\equiv1\pmod\phi\). Since \(b-a\) is a unit, the polynomial factors into comaximal linear factors and the characteristic identity gives an invariant direct-sum decomposition into rank-one free eigenspaces. One can see this explicitly using the two complementary idempotent projectors \((B-bI)/(a-b)\) and \((B-aI)/(b-a)\), which reduce modulo \(\phi\) to rank-one projectors. Each image is a projective rank-one module over the local ring and hence free of rank one. Further, \(a b=\det B=z^{-4}\phi^2\) and \(b\) is a unit. Therefore \(a\) equals \(\phi^2\) times a unit in \(R_\phi\), including the case where \(\phi^2=0\) in this quotient. Thus the complete zero-primary action is multiplication by \(\phi^2\), up to an invertible factor, on **one** copy of the \(4e\)-dimensional ring \(R_\phi\). The other \(R_\phi\) factor is invertible. Its stable invertible dimension together with the complementary factor is therefore \(2n-4e\).

For any integer \(t\ge0\), the principal ideal generated by \(\phi^{2t}\) in \(R_\phi\) has binary dimension \(4\max(e-2t,0)\), and its kernel has dimension \(4\min(2t,e)\). This proves the rank formula. If \(e=1\), multiplication by \(\phi^2\) is zero on a four-dimensional space, giving four size-one Jordan blocks. If \(e\ge2\), \(e\) is even and multiplying by \(\phi^2\) advances by two positions in each of four length-\(e\) local chains, giving eight length-\(e/2\) zero Jordan blocks. Consequently the nilpotent index is exactly \(\lceil e/2\rceil\).

For a linear map on a finite-dimensional vector space over a finite field, a state is eventually periodic exactly when its zero-primary component has become zero. Thus the set that has entered a cycle by time \(t\) has dimension \((2n-4e)+4\min(2t,e)\), proving the population formulas and sharpness of the entrance time. When \(5\nmid n\), the same statement has trivial zero-primary factor.

For the fixed-point count, solve \((B+I)w=0\). Its off-diagonal entry is the unit one, so elimination identifies its kernel with the scalar kernel of its determinant. Another direct expansion gives
\[
\det(B+I)=(r+1)(s+1)+1=rs+r+s=z^{-4}(z+1)^4\phi(z).
\]
Multiplication by a polynomial \(q(z)\) on \(\mathbb F_2[z]/(z^n-1)\) has kernel dimension \(\deg\gcd(q(z),z^n-1)\). The factor \(z+1\) occurs in \(z^n-1\) to exponent exactly \(e\), and \(\phi\) occurs to exponent \(e\) if and only if five divides \(n\). These distinct irreducible factors give fixed-space dimension \(\min(4,e)+4\beta\), establishing the last formula.

## Verification
The proof is algebraic and valid for every \(n\ge7\); a finite state computation is not substituted for an infinite-family proof. The accompanying `check_gp3.py` and `check_gp3.cpp` separately construct the actual labelled graph and calculate exact binary update-matrix ranks, fixed-space dimensions and first-entry thresholds for **every integer \(7\le n\le120\)**. The Python checker uses integer bit-vector pivot elimination; the C++ checker independently uses row-bitset Gaussian elimination. The C++ checker also evaluates the update on **all \(2^{20}=1,048,576\) labelled binary states** of \(GP(10,3)\), confirming 4,096 distinct one-step images and 64 fixed states. Their exact saved outputs accompany this document. These computations are independent checks of the formulas within the tested finite range, not certification of untested graph sizes.

## Relationship to prior work
Gera and Stănică (2011) establish real spectral formulae for generalized Petersen adjacency matrices using a two-component Fourier decomposition; that structural antecedent does not give the characteristic-two Jordan decomposition or exact first-periodic-entry populations. Zaidenberg (2006) develops a general positive-characteristic convolution framework; its general theory does not state these graph-family-specific cyclotomic-square and dyadic-transient formulas. General binary parity rules on other graph families, including prism graphs and generalized Petersen graphs with inner step two, do not imply the skip-three conclusions for all \(n\ge7\). In particular, the repeated factor \(\phi^2\) and a nonunit characteristic-two local eigenvalue whose valuation is two are essential to the half-speed transient clock. Published mathematical searches and targeted research-record comparisons identified no directly covering theorem; this is not a claim of exhaustive originality across all unindexed literature.

Dudek (2014 preprint, 2016 journal version) studies generalized Petersen adjacency eigenvalue gaps and expansion rather than modular binary state dynamics; his results do not assert the local Jordan structure derived here.

## Limitations
The model is strictly the open-neighbor XOR rule on simple \(GP(n,3)\) with \(n\ge7\). It is not a majority/threshold rule, not the closed-neighbor parity rule, and not the entire class of generalized Petersen graphs. No formulas for the number or lengths of all primitive nonzero-period cycles are claimed; only the exact fixed-point and eventually-periodic populations and entrance times are determined. Prior literature on Lights Out and binary cellular automata may contain unindexed equivalent formulations. Mathematical originality has not been independently audited.

## References
1. G. Gera and P. Stănică, “The spectrum of generalized Petersen graphs”, *Australasian Journal of Combinatorics* **49** (2011), 39–45. Full text: https://ajc.maths.uq.edu.au/pdf/49/ajc_v49_p039.pdf .
2. A. W. Dudek, “On the Spectrum of the Generalised Petersen Graphs”, arXiv:1412.3531, first posted 2014-12-11, later *Graphs and Combinatorics* **32** (2016), 1843–1850. https://arxiv.org/abs/1412.3531 .
3. M. Zaidenberg, “Convolution equations on lattices: periodic solutions with values in a prime characteristic field”, first arXiv submission 2006-06-29, arXiv:math-ph/0606070. https://arxiv.org/abs/math-ph/0606070 .
