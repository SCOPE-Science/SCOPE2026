# Modulo-three reversibility and a two-adic transient census for parity dynamics on circular prisms

## Finding

For every integer \(n\ge 3\), place one binary state at each vertex \((i,j)\) of the circular prism \(C_n\square K_2\), where \(i\in\mathbb Z/n\mathbb Z\) and \(j\in\{0,1\}\). Update all states simultaneously by the parity of their three distinct open neighbours:
\[
(F_n x)_{i,j}=x_{i-1,j}+x_{i+1,j}+x_{i,1-j}\pmod 2.
\]
Write \(\tau(x)\) for the least nonnegative number of iterations after which \(x\) lies on a periodic orbit.

**Reversibility, recurrence, and maximum transient.** If \(3\nmid n\), the update is a permutation: all \(2^{2n}\) configurations are periodic. If \(3\mid n\), put \(k=2^{\nu_2(n)}\). Then the recurrent set is a binary vector space of dimension \(2n-4k\), hence has exactly \(2^{2n-4k}\) configurations. The largest possible entry time is exactly
\[
T_n=\begin{cases}2,&k=1,\\k,&k\ge2.\end{cases}
\]
Every recurrent configuration has a basin of exactly \(2^{4k}\) initial configurations, including itself.

**Full entry-time census.** For \(3\mid n\), define
\[
\delta_t=\begin{cases}2\min(t,2),&k=1,\\4\min(t,k),&k\ge2.\end{cases}
\]
Then, for all integers \(t\ge0\),
\[
\#\{x:\tau(x)\le t\}=2^{2n-4k+\delta_t},
\]
and the number with \(\tau(x)=t\) is obtained by subtracting consecutive cumulative counts, with \(\#\{x:\tau(x)=0\}=2^{2n-4k}\). In particular, **exactly \(15/16\)** of all configurations have the maximal entry time when \(6\mid n\); for odd multiples of three, the corresponding proportion is **\(3/4\)**.

**Exact temporal orbit census.** Set \(g_n(z)=z^n+1\) and \(H_m(z)=(z^2+z+1)^m+z^m\), computed over \(\mathbb F_2[z]\). For every integer \(m\ge1\), put
\[
D_{n,m}=\begin{cases}
\deg\gcd(g_n,H_m^2),&m\text{ odd},\\
2\deg\gcd(g_n,H_m),&m\text{ even}.
\end{cases}
\]
Then
\[
\#\operatorname{Fix}(F_n^m)=2^{D_{n,m}}.
\]
Consequently, the number of configurations with *least* period \(m\) is
\[
\sum_{d\mid m}\mu(m/d)\,2^{D_{n,d}},
\]
and division by \(m\) gives the number of distinct primitive cycles. These formulas apply with no restriction on \(m\) or on the parity of \(n\).

## Assumptions and scope

The cycle \(C_n\) is simple, with \(n\ge3\), so the two rim neighbours and one vertical neighbour are always distinct. Arithmetic on binary states and on polynomials is over \(\mathbb F_2\). The update has no self-input. All configurations are labelled; graph-automorphism classes are not being counted. The orbit-entry time is the first time the trajectory reaches its eventual periodic orbit, not the period of that orbit. The formulas concern finite prisms only, not the two-row full shift over an infinite lattice.

## Proof

**1. The triangular polynomial matrix.** Encode the two rows by polynomials \(u(z),v(z)\) in \(R=\mathbb F_2[z]/(z^n+1)\). Since \(z\) is a unit in \(R\), cyclic left/right neighbours correspond to multiplication by \(z\) and \(z^{-1}\). Put \(c=z+z^{-1}\), \(d=c+1=z^{-1}(z^2+z+1)\). In the invertible coordinate change \((u,v)\mapsto(u,s=u+v)\), the update becomes
\[
J=\begin{pmatrix}d&1\\0&d\end{pmatrix}
\quad\text{on }R^2.
\]
Because the off-diagonal elementary matrix squares to zero and commutes with \(dI\), for every \(m\ge1\),
\[
J^m=\begin{pmatrix}d^m&(m\bmod 2)d^{m-1}\\0&d^m\end{pmatrix}.
\]

**2. The sole singular factor and its nilpotent index.** Write \(P=z^2+z+1\). Since \(d=z^{-1}P\), the operator is invertible exactly when \(P\) is coprime to \(z^n+1\). The roots of \(P\) are the nontrivial cubic roots of unity; therefore \(P\mid z^n+1\) exactly when \(3\mid n\). For \(3\mid n\), write \(n=kq\) with \(k=2^{\nu_2(n)}\) and \(q\) odd. The identity \(z^n+1=(z^q+1)^k\) and the nonvanishing derivative of \(z^q+1\) show that \(P\) occurs with multiplicity precisely \(k\). The Chinese-remainder decomposition separates a \(P\)-primary module of binary dimension \(4k\) from a complementary module of dimension \(2n-4k\). On the complement, \(d\), hence \(J\), is invertible, so every state is periodic. On the \(P\)-primary component, \(d\) is nilpotent of exact index \(k\). If \(k=1\), the matrix reduces to a nonzero square-zero matrix and has nilpotent index two. If \(k\ge2\), then \(k\) is even, \(J^k=0\), and \(J^{k-1}\ne0\) because its diagonal entry \(d^{k-1}\ne0\). This proves the recurrence and sharp maximum-entry-time assertions.

**3. Exact transient multiplicities and basins.** The \(P\)-primary ring has residue field \(\mathbb F_4\) and uniformizer \(d\); it has length \(k\) over \(\mathbb F_4\). When \(k\ge2\) is even and \(t<k\), the kernel of \(J^t\) has dimension \(2t\) over \(\mathbb F_4\): for even \(t\) this follows from \(J^t=d^tI\); for odd \(t\), the equation \(d^t s=0\) gives \(t\) free coordinates in \(s\), and \(d^t u=d^{t-1}s\) is solvable because \(d^{t-1}s\) lies in \((d^{k-1})\subseteq(d^t)\), with \(t\) independent choices for the kernel of multiplication by \(d^t\). Thus the binary kernel dimension is \(4t\) until saturation at \(4k\). When \(k=1\), the kernel dimensions at times zero, one, and two are respectively zero, two, and four over \(\mathbb F_2\). The invertible complement contributes all \(2^{2n-4k}\) choices at every entry time. This proves the cumulative census and, by difference, the exact entry-time distribution. The eventual image of \(J^{T_n}\) is the invertible complement; each point in that image has exactly \(2^{4k}\) preimages under \(J^{T_n}\). As the restriction of \(J\) to that complement is bijective, each periodic point has the same basin size. The proportions at maximal time follow from the penultimate kernel dimensions.

**4. Exact fixed-point and primitive-period formulas.** Multiplication by any polynomial \(f\) on \(R\) has binary kernel dimension \(\deg\gcd(g_n,f)\). The equation \(J^m x=x\) is represented by \(J^m+I\). When \(m\) is even, this matrix is diagonal with both diagonal entries \(d^m+1\), giving kernel dimension \(2\deg\gcd(g_n,H_m)\). When \(m\) is odd, its matrix has diagonal \(d^m+1\) and off-diagonal \(d^{m-1}\). These entries generate the unit ideal because \((d^m+1)+d\,d^{m-1}=1\). Its Smith factors over the Laurent polynomial ring are therefore \(1\) and \((d^m+1)^2\). Multiplication by \(z\) is a unit modulo \(g_n\), so \(d^m+1\) is associated to \(H_m\), giving kernel dimension \(\deg\gcd(g_n,H_m^2)\). A binary linear kernel of dimension \(D_{n,m}\) contains \(2^{D_{n,m}}\) configurations. Finally, Möbius inversion over divisors of \(m\) converts fixed-point counts into least-period counts. This completes the proof for all \(n\ge3\) and \(m\ge1\).

## Verification

The accompanying standalone program `prism_xor_check.py` implements the polynomial-gcd predictions and direct binary adjacency-matrix powers by separate algorithms. It checks 726 matrix-rank identities over prism circumferences 3 through 24, and exhaustively follows all 87,360 labelled states for circumferences 3 through 8, recovering the predicted exact first-entry distributions. Its recorded output is in `verification_output.txt`. The finite checks corroborate; the universal statements follow from the polynomial-module proof above.

## Relationship to prior work

Polynomial superposition and finite-field linear cellular automata are classical; see Moore (1997) for the additive-polynomial method and the broader treatment of linear cellular automata in Byszewski and Cornelissen (2022). General reversible cellular automata with periodic boundary conditions are investigated by Chang and Su (2016), on trees rather than prisms. The 2008 study by Ganguly, Sikdar, and Chaudhuri addresses cycle structures of additive and affine cellular automata; only its bibliographic description and abstract were accessible for comparison here. The present statement supplies the explicit all-circumference modulo-three criterion, the sharp two-adic transient and basin law, and the parity-dependent polynomial-gcd period census for this specific cubic graph family. These claims are not assertions of a general new polynomial or matrix method.

## Limitations

The classification is for synchronous open-neighbour parity over \(\mathbb F_2\), not thresholded or self-inclusive updates. It does not give a simplified classification of which individual primitive periods can occur; instead it gives exact counts for any queried period. The originality comparison is bounded by the accessible literature: a possibly equivalent specialization in an unindexed source, including the inaccessible full text of the 2008 additive-automaton cycle paper, has not been ruled out. No independent external verification is claimed.

## References

1. C. Moore, *Quasi-Linear Cellular Automata*, first submitted 20 January 1997, arXiv:adap-org/9701001, https://arxiv.org/abs/adap-org/9701001.
2. N. Ganguly, B. K. Sikdar and P. Pal Chaudhuri, *Exploring Cycle Structures of Additive Cellular Automata*, *Fundamenta Informaticae* 87 (2008), 137–154, https://doi.org/10.3233/FUN-2008-87202.
3. C.-H. Chang and J.-Y. Su, *Reversibility of Linear Cellular Automata on Cayley Trees with Periodic Boundary Condition*, originally submitted 5 March 2016, arXiv:1603.01679, https://arxiv.org/abs/1603.01679.
4. J. Byszewski and G. Cornelissen, *Multiband Linear Cellular Automata and Endomorphisms of Algebraic Vector Groups*, first submitted 5 November 2022, arXiv:2211.02866, https://arxiv.org/abs/2211.02866.
