# Exact finite-grid binary Kronecker radius of \(\{1,2,3\}\)
## Finding
For every integer \(N\ge 5\), define
\[
\beta_N=\max_{\varepsilon\in\{0,\tfrac12\}^3}\ \min_{k\in\mathbb Z_N}\ \max_{j=1,2,3}\left\|\frac{jk}{N}-\varepsilon_j\right\|_{\mathbb R/\mathbb Z},
\]
where \(\|x\|_{\mathbb R/\mathbb Z}\) is distance to the nearest integer. Then
\[
\beta_N=
\begin{cases}
\tfrac14,&N\equiv0\pmod4,\\
\tfrac{N+2}{4N},&N\equiv2\pmod4,\\
\tfrac{N+3}{4N},&N\ \text{odd}.
\end{cases}
\]
Thus restricting the character parameter for the three-term arithmetic progression \(\{1,2,3\}\) from the full circle to the \(N\)-point cyclic grid produces an exact, residue-class-dependent discretization penalty above the continuous binary radius \(\tfrac14\).

The two target patterns \(\varepsilon=(0,\tfrac12,0)\) and \(\varepsilon=(\tfrac12,\tfrac12,\tfrac12)\) already determine the maximum. Writing their minimax errors as \(m_{010}(N)\) and \(m_{111}(N)\), respectively,
\[
m_{010}(N)=
\begin{cases}
\tfrac14,&N\equiv0\pmod4,\\
\tfrac{N+3}{4N},&N\equiv1\pmod4,\\
\tfrac{N+2}{4N},&N\equiv2\pmod4,\\
\tfrac{N+1}{4N},&N\equiv3\pmod4,
\end{cases}
\]
and
\[
m_{111}(N)=
\begin{cases}
\tfrac14,&N\equiv0\pmod4,\\
\tfrac{N+1}{4N},&N\equiv1\pmod4,\\
\tfrac{N+2}{4N},&N\equiv2\pmod4,\\
\tfrac{N+3}{4N},&N\equiv3\pmod4.
\end{cases}
\]
Their maximum is the displayed formula for \(\beta_N\).

## Assumptions and scope
The group is the finite cyclic group \(\mathbb Z_N\), identified with the grid \(\{k/N:k\in\mathbb Z_N\}\) in the circle. The target phases are binary, namely \(0\) or \(\tfrac12\). The result is an angular approximation statement; no assertion is made here about the chordal \(\varepsilon\)-Kronecker constant obtained after exponentiation.

## Proof
For a binary target \(b=(b_1,b_2,b_3)\in\{0,1\}^3\), put
\[
g_b(x)=\max_{1\le j\le3}\left\|jx-\frac{b_j}2\right\|_{\mathbb R/\mathbb Z}.
\]
Every \(g_b\) satisfies \(g_b(1-x)=g_b(x)\), so it suffices to consider \(0\le x\le\tfrac12\).

For \(b=010\), direct evaluation gives
\[
g_{010}(x)=
\begin{cases}
\max(\tfrac12-2x,3x),&0\le x\le\tfrac16,\\
1-3x,&\tfrac16\le x\le\tfrac14,\\
x,&\tfrac14\le x\le\tfrac12.
\end{cases}
\]
The first interval has continuous minimum \(\tfrac3{10}\). For \(N\ge17\), a minimizing grid point therefore lies adjacent to \(\tfrac14\). Writing \(N=4q+r\), \(0\le r<4\), evaluation at \(q/N\) and \((q+1)/N\) gives exactly the four cases above for \(m_{010}(N)\).

For \(b=111\),
\[
g_{111}(x)=
\begin{cases}
\tfrac12-x,&0\le x\le\tfrac14,\\
3x-\tfrac12,&\tfrac14\le x\le\tfrac13,\\
\max(2x-\tfrac12,\tfrac32-3x),&\tfrac13\le x\le\tfrac12.
\end{cases}
\]
The last interval has continuous minimum \(\tfrac3{10}\). The same adjacent-grid-point calculation for \(N\ge17\) gives the four cases for \(m_{111}(N)\). Exact finite arithmetic verifies those formulas for \(5\le N\le16\).

For the other six binary targets, explicit continuous witnesses give error at most \(\tfrac15\):
\[
000:\ x=0,\quad
101:\ x=\tfrac12,\quad
001:\ x=\tfrac25,\quad
100:\ x=\tfrac1{10},\quad
011:\ x=\tfrac13,\quad
110:\ x=\tfrac16.
\]
Each \(g_b\) is \(3\)-Lipschitz. Choosing a grid point within \(1/(2N)\) of its witness gives
\[
\min_{k\in\mathbb Z_N}g_b(k/N)\le \tfrac15+\frac3{2N}\le\tfrac14
\]
for \(N\ge30\). Hence these six targets cannot exceed the two decisive targets. Exact enumeration covers \(5\le N\le29\), completing the proof.

## Verification
The standalone verifier uses exact integer arithmetic on denominator \(2N\). It enumerates all eight binary targets and all grid points, checks the theorem for \(5\le N\le200\), checks both decisive closed formulas, and explicitly covers the finite proof remainder \(5\le N\le29\). The computation corroborates but does not extrapolate the infinite claim.

## Relationship to prior work
Hare and Ramsey study Kronecker constants for finite subsets of the integer dual of the circle. Their full treatment of arithmetic progressions records the continuous angular value \(\alpha(\{1,2,3\})=\tfrac14\). Their later paper treats binary Kronecker constants for three-element integer sets, again with the approximating parameter ranging over the full circle. The present statement instead restricts the parameter to the finite subgroup \(N^{-1}\mathbb Z/\mathbb Z\), so the exact mod-\(4\) discretization penalty is not implied by those continuous formulas.

## Limitations
The theorem concerns only the arithmetic progression \(\{1,2,3\}\), binary targets, and angular distance. It does not classify arbitrary three-character subsets, arbitrary target phases, or chordal Kronecker constants. An equivalent finite-cyclic formula could exist under different terminology.

## References
1. K. E. Hare and L. T. Ramsey, “Upper and Lower Bounds for Kronecker Constants of Three-Element Sets of Integers,” arXiv:1108.3802v2, first public submission 2011-08-19.
2. K. E. Hare and L. T. Ramsey, “Kronecker Constants for Finite Subsets of Integers,” Journal of Fourier Analysis and Applications 18 (2012), 326–366, doi:10.1007/s00041-011-9195-0.
3. K. E. Hare and L. T. Ramsey, “Exact Kronecker Constants of Three Element Sets,” Acta Mathematica Hungarica 146 (2015), 306–331, doi:10.1007/s10474-015-0529-2.
