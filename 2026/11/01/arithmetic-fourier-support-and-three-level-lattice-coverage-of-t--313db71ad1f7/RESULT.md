# Arithmetic Fourier support and three-level lattice coverage of the four-dimensional cross-polytope

## Finding
Let \(B=\{x\in\mathbb R^4:\|x\|_1\le1\}\). For each \(k\in\mathbb Z^4\) put \(\widehat B(k)=\int_B e^{-2\pi i k\cdot x}\,dx\). The exact Fourier transform, invariant under signed coordinate permutations, has the following disjoint cases (in every displayed family \(a,b\) are integers and all specified inequalities apply):

\[
\widehat B(k)=\begin{cases}
2/3,&k=0,\\
2/(\pi^2b^2),&(|k_1|,\ldots,|k_4|)\sim(0,0,0,b),\ b\ge1,\\
1/(2\pi^2(b^2-a^2)),&(|k_1|,\ldots,|k_4|)\sim(a,a,a,b),\ a\ge1,\ b\ge0,\ b\ne a,\\
-1/(4\pi^2a^2),&(|k_1|,\ldots,|k_4|)\sim(a,a,a,a),\ a\ge1,\\
0,&\text{otherwise}.
\end{cases}
\]

Here \(\sim\) denotes permutation. Consequently \(\widehat B(k)\ne0\) exactly when at least three absolute coordinate values agree. The nonzero support in an integer-frequency cube has the sharp count
\[
\#\{k\in[-N,N]^4\cap\mathbb Z^4:\widehat B(k)\ne0\}=64N^2-8N+1\qquad(N\in\mathbb Z_{\ge0}).
\]

For each integer \(m\ge1\), define the integer-lattice translation multiplicity
\[
P_m(u)=\sum_{z\in\mathbb Z^4}\mathbf1_{\{\|u-z\|_1<m\}}\quad(u\in\mathbb R^4).
\]
Away from the boundaries of all translated copies of \(B\) and \(mB\),
\[
P_m(u)=m^2P_1(u)+\frac23(m^4-m^2).
\]
On the torus \(\mathbb R^4/\mathbb Z^4\), \(P_1\) has exactly three levels \(0,1,2\) on sets of normalized measures \(1/2,1/3,1/6\), respectively. Thus \(P_m\) has exactly the three levels \(C_m,C_m+m^2,C_m+2m^2\), with \(C_m=\frac23(m^4-m^2)\), on the same respective fractions. These are almost-everywhere assertions, not values assigned on the finitely many translated facet hyperplanes.

## Assumptions and scope
Lebesgue volume is normalized by the standard lattice fundamental cell of volume one. The Fourier convention is the negative-frequency exponential stated above. Coordinate frequency vectors are integral, so the phase at a pole of the Laplace transform is a full integer turn. The four-dimensional cross-polytope is the closed \(\ell^1\) unit ball; using an open ball for lattice multiplicities changes only boundary values. The radius parameter \(m\) and frequency-cube half-width \(N\) are integers.

## Proof
**1. Laplace transform.** Write \(F(R;k)=\int_{\|x\|_1\le R}e^{-2\pi i k\cdot x}\,dx\). For \(\operatorname{Re}s>0\), Fubini and the one-dimensional exponential transform give
\[
\int_0^\infty e^{-sR}F(R;k)\,dR
=\frac1s\prod_{j=1}^4\int_{\mathbb R}e^{-s|x|-2\pi i k_jx}\,dx
=\frac{16s^3}{\prod_{j=1}^4(s^2+4\pi^2k_j^2)}=:R_k(s).
\]
Inverse Laplace transformation at radius one equals the sum of residues of \(e^sR_k(s)\) at its poles. This follows directly from the standard Bromwich contour for a rational transform of a compactly supported integral function (or by partial fractions), and no numerical integration is used.

**2. Pole cancellation and explicit coefficients.** The rational function \(R_k\) is odd and decays as \(s^{-5}\). Its poles are at \(s=0\) and at \(s=\pm2\pi i|k_j|\); because \(k_j\) is integral, \(e^s=1\) at each pole. At paired nonzero poles, oddness makes coefficients of even-order principal parts opposite, so their contributions cancel. All simple-part contributions sum to zero by the residue theorem applied to the rational function \(R_k\) (there is no pole at infinity). Thus the only surviving contributions arise from principal parts of order at least three, either at zero or at nonzero poles where at least three absolute coordinate frequencies coincide.

For a nonzero value \(a\) repeated three times and distinct fourth absolute value \(b\), the coefficient of the cubic pole at \(s=2\pi ia\) is \(2/[4\pi^2(b^2-a^2)]\). The matching cubic coefficient at the negative pole is the same; multiplying each by \(1/2!\) in the inverse Laplace residue and adding gives the third case above. If all four absolute values equal a nonzero \(a\), the cubic-pole coefficient at either sign is \(-1/(4\pi^2a^2)\), while the fourth-order principal parts cancel. For three zero coordinates and a single nonzero absolute coordinate \(b\), the cubic coefficient at zero is \(16/(4\pi^2b^2)\), giving half that amount. Finally, at zero frequency the origin has a fifth-order pole with coefficient \(16\), yielding \(16/4!=2/3\). These exhaust all multiplicity patterns and prove the entire Fourier table.

**3. Sharp Fourier support count.** For \(N\ge1\), the nonzero origin contributes one frequency. Among nonzero frequencies with three repeated nonzero absolute values, all-four-equal frequencies contribute \(16N\); a distinct zero fourth coordinate contributes \(32N\); a distinct positive fourth absolute value contributes \(64N(N-1)\). Three zero coordinates and one nonzero contribute \(8N\). Their sum is \(1+64N^2-8N\). It also holds at \(N=0\).

**4. Exact integer-radius scaling.** The \(k\)-th torus Fourier coefficient of \(P_m\) equals \(m^4\widehat B(mk)\). For \(k\ne0\), every nonzero term in the four cases above is homogeneous of degree minus two in the integer frequencies, so \(\widehat B(mk)=m^{-2}\widehat B(k)\) (and the zero coefficients stay zero). Hence \(\widehat{P_m}(k)=m^2\widehat{P_1}(k)\) for \(k\ne0\). At \(k=0\), the coefficients are the volumes \(\frac23m^4\) and \(\frac23\). Uniqueness of Fourier coefficients in \(L^1(\mathbb R^4/\mathbb Z^4)\) proves \(P_m=m^2P_1+\frac23(m^4-m^2)\) almost everywhere. Because these integer-valued functions are constant on every connected component away from their translated facet hyperplanes, the identity also holds everywhere off those boundaries.

**5. Three-level distribution.** Three distinct integer lattice points within open \(\ell^1\)-distance one of the same point would have all pairwise integer \(\ell^1\)-distances less than two, hence exactly one. The nearest-neighbor graph on \(\mathbb Z^4\) is bipartite, so no such triple exists. Thus \(P_1\in\{0,1,2\}\) away from boundaries. Each pair of distinct open unit balls can overlap in positive four-volume only if its displacement is one of the eight coordinate unit vectors. For displacement \(e_1\), slice integration gives
\[
\operatorname{vol}(B\cap(e_1+B))=\frac43\int_0^1\min(t,1-t)^3\,dt=\frac1{24}.
\]
By periodic unfolding, the measure of \(P_1=2\) is \(\int_{[0,1]^4}\binom{P_1}2\,du=\frac12\cdot8\cdot\frac1{24}=\frac16\). The mean of \(P_1\) is \(\operatorname{vol}B=2/3\), so the measure of \(P_1=1\) is \(2/3-2(1/6)=1/3\), and the remaining measure is \(1/2\). Since each fraction is positive, all three levels occur. Scaling from Step 4 gives the remaining assertions.

## Verification
The reproducible standalone script `checks.py` uses symbolic Laurent-coefficient calculations to compare twelve distinct frequency patterns with the closed transform table, exhaustively checks the support count for \(N=0,1,2\), and directly enumerates lattice translates for 300 deterministically sampled pairs of torus point and radius \(m=1,2,3,4,5\). The script passed all these tests using Python 3 and SymPy. This is finite corroboration; Steps 1–5 give the infinite proof.

## Relationship to prior work
Borda, *Lattice points in algebraic cross-polytopes and simplices* (public preprint 2016-08-08), supplies general contour and residue methods for polyhedral Fourier transforms and emphasizes higher-order poles, but its irrational/algebraic-axis lattice-counting theorem is not the explicit repeated equal-axis four-dimensional integer-frequency classification here. Gravin–Robins–Shiryaev, *Translational tilings by a polytope, with multiplicity* (2011), studies constant-multiplicity translational tiling. The three distinct nonconstant lattice-overlap levels here are a different assertion. A lower-dimensional integer-frequency octahedron calculation has related structural features but does not state the four-dimensional residue table, quadratic support count, or three-level fractions.

## Limitations
The result concerns only the standard unit-axis four-dimensional cross-polytope, integer frequencies, and integral dilation radii. Statements about translate counts exclude all translated facet boundaries. It does not claim a general-dimensional theorem, arbitrary irrational axes, or uniqueness in all existing literature. Search-based originality review is bounded; an earlier equivalent specialization of general Fourier–polytope formulas remains possible. No independent mathematical validation has been performed.

## References
1. B. Borda, *Lattice points in algebraic cross-polytopes and simplices*, arXiv:1608.02417 (first publicly posted 2016-08-08), https://arxiv.org/abs/1608.02417 ; accessible full text https://real.mtak.hu/89745/1/1608.02417v2.pdf.
2. N. Gravin, S. Robins, D. Shiryaev, *Translational tilings by a polytope, with multiplicity*, arXiv:1103.3163 (first publicly posted 2011-03-16), https://arxiv.org/abs/1103.3163.
