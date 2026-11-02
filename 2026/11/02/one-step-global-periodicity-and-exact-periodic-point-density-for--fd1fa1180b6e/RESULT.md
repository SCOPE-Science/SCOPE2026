# One-step global periodicity and exact periodic-point density for the rounded \(45^\circ\) lattice rotation

## Finding
For nearest-integer coordinatewise quantization of Euclidean rotation by \(\pi/4\), the entire integer lattice enters a periodic cycle after **at most one** iteration. With \(R\) the quantized rotation and \(Q\) an exact counterclockwise quarter-turn, the global algebraic identity is
\[
R^3=Q\circ R.
\]
Every nonzero point in \(R(\mathbb Z^2)\) has **least period eight**; the origin is the only fixed point and the only periodic point of a different period. The one-step entrance time is optimal. In centered expanding lattice squares the exact natural density of periodic points is \(2\sqrt2-2\), and that of the points requiring one transient step is \(3-2\sqrt2\). Every lattice target has zero, one, or two preimages, with exact densities \(3-2\sqrt2\), \(4\sqrt2-5\), and \(3-2\sqrt2\), respectively.

## Assumptions and scope
Write \(U=2^{-1/2}\begin{pmatrix}1&-1\\1&1\end{pmatrix}\) and \(Q=U^2=\begin{pmatrix}0&-1\\1&0\end{pmatrix}\). On \(\mathbb Z^2\), define \(R(z)=\mathcal N(Uz)\), with \(\mathcal N(v)=(\lfloor v_1+1/2\rfloor,\lfloor v_2+1/2\rfloor)\). For integer \(z\), each coordinate of \(Uz\) is an integer divided by \(\sqrt2\); it is never an integer plus one half, so the tie convention has no effect. A point is called periodic when \(R^p(z)=z\) for some positive integer \(p\). Natural densities are limits of fractions over \([-N,N]^2\cap\mathbb Z^2\) as integer \(N\to\infty\).

## Proof
**1. Diamond stability.** Let \(S=(-1/2,1/2)^2\), let \(c=1/\sqrt2\), and define \(D=US=\{(s,t):|s|+|t|<c\}\). If \(v\in D\) and neither coordinate is a half-integer, then \(v-\mathcal N(v)\in D\). Indeed at most one coordinate of \(v\) has magnitude above \(1/2\), because \(2(1/2)>c\). If neither does, the nearest integer is zero and the assertion is immediate. Otherwise, after signed-coordinate permutation, \(v_1>1/2\), \(\mathcal N(v)=(1,0)\), and
\[
|v_1-1|+|v_2|=1-v_1+|v_2|<1+c-2v_1<c.
\]
The inequalities are strict; the boundary case \(v_1=1/2\) was excluded.

**2. Exact two-step action on the image.** Given \(z\in\mathbb Z^2\), put \(w=R(z)\) and \(e=Uz-w\in S\). Put \(v=Ue\in D\), \(q=\mathcal N(v)\), and \(r=v-q\). The coordinates of \(v\) cannot be half-integers: \(v=Qz-Uw\), so each is an integer minus an integer divided by \(\sqrt2\). By the preceding lemma \(r\in D\). Since \(Uw=Qz-v\), nearest-integer translation-equivariance gives \(R(w)=Qz-q\). Therefore
\[
U R(w)=U(Qz-q)=Qw+Ur.
\]
But \(Ur\in U D=U^2S=QS=S\). It follows that \(R^2(w)=Qw\) for every \(w\in R(\mathbb Z^2)\), or equivalently \(R^3=Q\circ R\) on all lattice points.

**3. Periods and optimal entrance.** The map \(R\) commutes with \(Q\), since \(UQ=QU\) and nearest-integer rounding is equivariant under signed-coordinate permutations at all attainable non-tie points. Thus on \(Y=R(\mathbb Z^2)\), \(R^{2j}(w)=Q^jw\), and in particular \(R^4(w)=-w\) and \(R^8(w)=w\). For nonzero \(w\), no proper divisor of eight is a period because \(R^4(w)\neq w\); hence the least period is eight. If \(R(z)=0\), both coordinates of \(Uz\) have absolute value less than \(1/2\), which forces \(\|z\|_2^2<1/2\), hence \(z=0\). Therefore every nonzero orbit enters an eight-cycle within one step. The bound is sharp: \(R(2,0)=(1,1)\) but \(R^8(2,0)\neq(2,0)\), as is verified by eight exact rotations (or by the checker).

**4. Exact density of preimage multiplicities.** For \(w\in\mathbb Z^2\), the number of inverse images under \(R\) is the number of lattice points in \(U^{-1}w+D\), since \(U^{-1}S=D\) (both are the same diamond). A diamond of \(\ell^1\)-radius \(c\) cannot contain three lattice points: all pairwise Manhattan distances would be integers strictly below \(2c=\sqrt2\), hence at most one, but the nearest-neighbor lattice graph has no triangle. Accordingly, multiplicities are in \(\{0,1,2\}\).

For \(D\), the only nonempty overlaps with nonzero lattice translates are for the four unit coordinate vectors. With \(a=c-1/2\), the overlap area with \(D+(1,0)\) is
\[
\int_{-a}^{a}(2c-1-2|y|)\,dy=2a^2=\frac{3-2\sqrt2}{2}.
\]
The same holds for each signed unit coordinate vector. On the unit torus, the measure of the region covered by exactly two translates of \(D\) is half the sum of these four pairwise overlap areas, namely \(4a^2=3-2\sqrt2\). The mean multiplicity is \(\operatorname{area}(D)=1\). Therefore the uncovered region also has measure \(3-2\sqrt2\), and the singly covered region has measure \(4\sqrt2-5\).

Finally, the fractional lattice sequence \(U^{-1}w\pmod{\mathbb Z^2}\), \(w\in[-N,N]^2\cap\mathbb Z^2\), is uniformly distributed on the torus: for each nonzero Fourier frequency \((h_1,h_2)\), the phase coefficients in the two integer indices are \((h_1-h_2)/\sqrt2\) and \((h_1+h_2)/\sqrt2\), at least one irrational, so the Weyl character average tends to zero. The multiplicity regions have piecewise-linear boundaries of measure zero, permitting transfer of their areas to exact natural densities. The periodic points are precisely \(Y\), by the previous step: the densities of image, nonimage, and two-to-one targets are thus \(2\sqrt2-2\), \(3-2\sqrt2\), and \(3-2\sqrt2\), respectively. This completes the proof.

## Verification
The accompanying standalone `check_round45.py` computes \(\mathcal N(m/\sqrt2)\) using the integer square-root formula \(\operatorname{sgn}(m)\left\lfloor\frac{\lfloor\sqrt{2m^2}\rfloor+1}{2}\right\rfloor\), without floating-point rounding. It checks the global-identity specialization, least periods, and the sharp transient witness for all \(103{,}041\) lattice seeds in the square of radius \(160\), and for \(20{,}000\) additional exact large-integer seeds. The infinite-lattice identity and density theorem are proved analytically above, not inferred from these finite tests.

## Relationship to prior work
Hannusch and Pethő, *Rotation on the digital plane* (arXiv:2109.01828; first publicly submitted 2021-09-04; journal DOI below), study both floor and nearest-integer digital rotations. Their Theorem 5.2 addresses periodic **floor** rotation along selected horizontal-axis seeds; Section 6 mentions nearest rounding in the context of noninjectivity and nonsurjectivity but does not state this all-lattice orbit classification, the exact nine-step idempotence identity, or the exact density formula. The noninjectivity phenomenon they establish is consistent with the existence of one-step transients here. Akiyama and Pethő (2013) work with a different reversible shift-radix rotation \((x,y)\mapsto(y,-\lfloor x+\lambda y\rfloor)\), not this orthogonal nearest-integer map. Kozyakin et al. (1997) and Vladimirov (2015) study statistical properties of quantized planar rotations and do not supply a directly identified implication of the exact present special-angle theorem from the inspected material.

## Limitations
The global conclusion depends on the exact angle \(\pi/4\), on the square integer lattice, and on **nearest-integer** quantization. It does not follow for coordinatewise floor quantization, arbitrary angles, or arbitrary lattices. Finite tests alone cannot certify the stated infinite conclusions. The 1997 rotation survey and a 2021 seminar on rounded planar rotations were only partially accessible for detailed comparison, so publication-priority assessment retains an explicit residual risk. The result has not received independent mathematical validation.

## References
1. C. Hannusch and A. Pethő, *Rotation on the digital plane*, arXiv:2109.01828 (public version submitted 2021-09-04); *Periodica Mathematica Hungarica* 86 (2023), 564–577, DOI: 10.1007/s10998-022-00480-8 (online 2022-07-16).
2. S. Akiyama and A. Pethő, *Discretized rotation has infinitely many periodic orbits*, *Nonlinearity* 26 (2013), 871–880, DOI: 10.1088/0951-7715/26/3/871; arXiv:1206.3868.
3. V. Kozyakin, N. Kuznetsov, A. Pokrovskii and I. Vladimirov, *Some problems in analysis of discretizations of continuous dynamical systems*, *Nonlinear Analysis* 30 (1997), 767–778, DOI: 10.1016/S0362-546X(96)00232-5.
4. I. G. Vladimirov, *Quantized linear systems on integer lattices: a frequency-based approach*, arXiv:1501.04237 (2015).
