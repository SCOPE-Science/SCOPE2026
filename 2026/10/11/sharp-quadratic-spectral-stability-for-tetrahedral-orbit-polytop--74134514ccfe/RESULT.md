# Sharp quadratic spectral stability for tetrahedral orbit polytopes
## Finding
For every regular orbit polytope \(Q_w=\operatorname{conv}(\Gamma w)\) in the pure rotational tetrahedral family, write the normalized stochastic weights as \(x_1,x_2,x_3\ge0\) with
\[
x_1+2x_2+2x_3=1.
\]
Let \(\lambda_1(w)>\lambda_2(w)>\lambda_3(w)\) be the three multiplicity-three eigenvalues coming from the cubic factor of the source stochastic matrix. Then
\[
\lambda_1(w)^2\ge x_1^2+2x_2^2+2x_3^2
=\frac15+(x_1-\tfrac15)^2+2(x_2-\tfrac15)^2+2(x_3-\tfrac15)^2.
\]
Equality in the first inequality holds if and only if \(x_2=x_3\). In particular, \(\lambda_1(w)\ge1/\sqrt5\), with equality if and only if \(x_1=x_2=x_3=1/5\). Also \(\lambda_3(w)\le-1/\sqrt5\), with equality at the same uniform-weight point. Therefore the second-largest-eigenvalue modulus of the associated symmetric random walk is at least \(1/\sqrt5\), uniquely attained in this geometric family by the regular icosahedron.

## Assumptions and scope
The group \(\Gamma\subset SO(3)\) is the order-\(12\) pure rotational tetrahedral group used in arXiv:2410.02494v1. The theorem concerns its regular orbit-polytopes, for which the group acts simply transitively on twelve vertices and the source gives nonnegative weights satisfying \(x_1+2(x_2+x_3)=1\). Regular boundary strata where one weight vanishes are included. The collapsed tetrahedron and octahedron orbits, whose stochastic matrices have smaller size, are excluded.

## Proof
Put
\[
a=x_1,\qquad s=x_2+x_3,\qquad d=x_2-x_3.
\]
Thus \(a+2s=1\), \(0\le a\le1\), and \(|d|\le s\). The cubic factor displayed in arXiv:2410.02494v1 is the characteristic polynomial of
\[
B=\begin{pmatrix}
a&s&d\\
s&-a&d\\
d&d&-a
\end{pmatrix}.
\]
Indeed,
\[
p(t)=\det(tI-B)=t^3+at^2-(a^2+s^2+2d^2)t-a(a^2+s^2)-2sd^2.
\]
Hence the ordered eigenvalues of \(B\) are \(\lambda_1,\lambda_2,\lambda_3\).

Set \(L=\sqrt{a^2+s^2+d^2}\). Using \(L^2=a^2+s^2+d^2\) and \(2s=1-a\),
\[
p(L)=d^2(a-L-2s)=d^2(2a-1-L).
\]
For \(a\le1/2\) the last factor is nonpositive. For \(a\ge1/2\),
\[
L^2-(2a-1)^2=\frac{(11a-3)(1-a)+4d^2}{4}\ge0,
\]
so it is again nonpositive. Therefore \(p(L)\le0\). Since the monic cubic is positive for every \(t>\lambda_1\), it follows that \(L\le\lambda_1\), and hence
\[
\lambda_1^2\ge a^2+s^2+d^2=x_1^2+2x_2^2+2x_3^2.
\]
If equality holds, then \(p(L)=0\). If \(d\ne0\), this would force \(L=2a-1\); the displayed nonnegative identity then forces \(a=1\) and \(d=0\), a contradiction. Thus equality forces \(d=0\), or \(x_2=x_3\). Conversely, when \(d=0\), \(B\) is the direct sum of \(\begin{pmatrix}a&s\\s&-a\end{pmatrix}\) and \((-a)\), so \(\lambda_1=L\).

The normalization gives the exact decomposition
\[
x_1^2+2x_2^2+2x_3^2=\frac15+(x_1-\tfrac15)^2+2(x_2-\tfrac15)^2+2(x_3-\tfrac15)^2,
\]
which has unique minimum \(1/5\) at uniform weights.

For \(\lambda_3\), the leading \(2\times2\) principal block of \(B\) has eigenvalues \(\pm r\), where
\[
r=\sqrt{a^2+s^2}=\sqrt{\frac15+\frac54(a-\tfrac15)^2}.
\]
Cauchy interlacing yields \(\lambda_3\le-r\le-1/\sqrt5\). Global equality forces \(a=1/5\); at this positive value, any \(d\ne0\) couples the bottom eigenvector of the principal block to the third coordinate, making the lower eigenvalue strictly smaller than \(-r\). Hence equality also forces \(d=0\).

Finally, for geometric coordinates \(a_g\ge b_g\ge|c_g|\), the source weight numerators satisfy
\[
N_2-N_3=2a_g^2c_g,
\qquad
N_1-N_2=(a_g+b_g-c_g)(a_g^2-a_gb_g-b_g^2-b_gc_g).
\]
Uniform weights therefore force \(c_g=0\) and \(a_g^2-a_gb_g-b_g^2=0\), so \(a_g/b_g=\varphi=(1+\sqrt5)/2\). Thus the unique geometric equality point is the regular icosahedron \(Q_{(\varphi,1,0)}\).

## Verification
The proof is symbolic and covers all admissible real weights. The accompanying `verify.py` reconstructs the cubic coefficients exactly on a rational grid, checks the completed-square identity exactly, and numerically diagonalizes the symmetric \(3\times3\) block as a sanity check. That finite computation is not used as an infinite proof.

## Relationship to prior work
Ivrissimtzis, Lange, Liu and Peyerimhoff derive the weight formulas, the twelve-state stochastic matrix and its factored characteristic polynomial. Their tetrahedral-group subsection reports from plots and Maple calculations that the regular icosahedron globally minimizes \(\lambda_1\), and that this minimum coincides with the global maximum of \(\lambda_3\). Their discussion explicitly states that this subsection relies on Maple computations rather than formal proofs. The present theorem does not claim that already reported global extremum as new; it supplies the sharp quadratic stability inequality, the equality line \(x_2=x_3\), a short formal proof, and the corresponding two-sided mixing consequence.

The earlier work of Ivrissimtzis and Peyerimhoff gives a qualitative critical-point/equilaterality framework for vertex-transitive spectral representations. The fastest-mixing work of Boyd, Diaconis, Parrilo and Xiao gives general symmetry-reduction and block-diagonalization methods. The inspected statements in those sources do not imply the explicit tetrahedral-orbit inequality above.

## Limitations
The theorem is specific to the three-weight regular tetrahedral-orbit stochastic matrices whose cubic factor appears in arXiv:2410.02494v1. It does not establish an analogous stability law for arbitrary finite groups, arbitrary vertex-transitive polytopes, or collapsed lower-vertex boundary orbits. Literature searches are evidence for originality, not a proof of exhaustive publication novelty.

## References
1. I. Ivrissimtzis, C. Lange, S. Liu, N. Peyerimhoff, *Polyhedral volume ratios, Izmestiev's Colin de Verdiere matrices and Spectral Gaps*, arXiv:2410.02494v1, 2024.
2. I. Ivrissimtzis, N. Peyerimhoff, *Spectral representations of vertex transitive graphs, Archimedean solids and finite Coxeter groups*, Groups Geom. Dyn. 7 (2013), 591--615, arXiv:1106.2509.
3. S. Boyd, P. Diaconis, P. Parrilo, L. Xiao, *Fastest Mixing Markov Chain on Graphs With Symmetries*, SIAM J. Optim. 20 (2009), 792--819, arXiv:0709.0955.
