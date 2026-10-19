# Five-sector even-harmonic sampling on the 600-cell and its unique tight rank-59 degree

## Finding
Let \(\Gamma\subset S^3\) be the group of 120 unit icosian quaternions (the vertices of the regular 600-cell), let \(H=\Gamma/\{\pm1\}\cong A_5\), and choose one unit quaternion \(q_h\) representing each \(h\in H\). For every even integer \(\ell\ge0\), evaluate the complex homogeneous spherical-harmonic space \(\mathcal H_\ell(S^3)\), with probability-normalized surface \(L^2\)-norm, at these 60 points. Let \(E_\ell:\mathcal H_\ell\to\mathbb C^{60}\), with the usual unweighted sum inner product on its target, and set \(G_\ell=E_\ell E_\ell^*\).

**Complete five-sector spectrum.** Put \(\varphi=(1+\sqrt5)/2\), \(\varphi'=1-\varphi\), and \(k=\ell/2\). Define
\[
 a=(-1)^k,\quad b=\begin{cases}1&k\equiv0\ (3),\\0&k\equiv1\ (3),\\-1&k\equiv2\ (3),\end{cases}
\]
\[
 c=(1,\varphi,0,-\varphi,-1)_{k\bmod5},\qquad
 d=(1,\varphi',0,-\varphi',-1)_{k\bmod5}.
\]
In the following five rows, the columns are the dimension \(d_\rho\), and character values on the identity, order-two, order-three and the two order-five classes of \(A_5\):

| \(\rho\) | \(d_\rho\) | \(\chi_\rho(2)\) | \(\chi_\rho(3)\) | \(\chi_\rho(5A)\) | \(\chi_\rho(5B)\) |
|---|---:|---:|---:|---:|---:|
| \(\mathbf1\) | 1 | 1 | 1 | 1 | 1 |
| \(V_3\) | 3 | -1 | 0 | \(\varphi\) | \(\varphi'\) |
| \(V'_3\) | 3 | -1 | 0 | \(\varphi'\) | \(\varphi\) |
| \(V_4\) | 4 | 0 | 1 | -1 | -1 |
| \(V_5\) | 5 | 1 | -1 | 0 | 0 |

For each row set
\[
 m_\rho(\ell)=\frac{d_\rho(\ell+1)+15a\chi_\rho(2)+20b\chi_\rho(3)+12c\chi_\rho(5A)+12d\chi_\rho(5B)}{60}.
\]
These numbers are nonnegative integers, and **the entire spectrum including zeros** is
\[
 \boxed{\lambda_\rho(\ell)=\frac{60(\ell+1)m_\rho(\ell)}{d_\rho},\qquad\text{multiplicity }d_\rho^2.}
\]
If eigenvalues coincide their multiplicities add. In particular,
\[
 \operatorname{rank}E_\ell=\sum_{m_\rho(\ell)>0}d_\rho^2.
\]

The exact ranks for \(0\le\ell<60\), \(\ell\) even, are:

| \(\ell\) | 0 | 2 | 4 | 6 | 8 | 10 | 12 | 14 | 16 | 18 | 20 | 22 | 24 | 26 | 28 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| rank | 1 | 9 | 25 | 25 | 41 | 43 | 51 | 59 | 50 | 59 | 60 | 59 | 60 | 59 | 59 |

| \(\ell\) | 30 | 32 | 34 | 36 | 38 | 40 | 42 | 44 | 46 | 48 | 50 | 52 | 54 | 56 | 58 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| rank | 60 | 60 | 59 | 60 | 59 | 60 | 60 | 60 | 59 | 60 | 60 | 60 | 60 | 60 | 59 |

For **every even \(\ell\ge60\)** the rank is 60. Thus degree 20 is the first individually surjective even degree; rank decreases at degree 22 and again at several later degrees; and degree 58 is the last rank-deficient even degree.

**Unique tight codimension-one exception.** Among all even degrees whose evaluation rank is 59, exactly \(\ell=58\) has equal nonzero singular values. At this degree
\[
 \boxed{G_{58}=3540\left(I_{60}-\frac1{60}\mathbf1\mathbf1^*\right).}
\]
Consequently, an arbitrary 60-component data vector is interpolable at degree 58 exactly when its entries sum to zero, and every such vector has a minimum-norm harmonic interpolant of squared \(L^2(S^3)\)-norm \(\lVert y\rVert_2^2/3540\).

At every full-rank even degree \(\ell\ge60\), the squared spectral condition number tends to \(1\) as \(\ell\to\infty\), with error \(O(1/\ell)\). Exact orthogonality of all 60 sample kernels never occurs in an even degree, since \(U_\ell(0)=(-1)^{\ell/2}\ne0\) and some distinct sample lines are perpendicular.

## Assumptions and scope
The icosian group is the finite subgroup \(\Gamma\) of unit quaternions whose elements form the 600-cell. The set of 60 antipodal lines is naturally the group \(H=A_5\), not an arbitrary 60-point subset of the sphere. The theorem concerns each **individual**, homogeneous, **even** degree; it does not concern the cumulative degree band, odd-degree oriented evaluations, weighted nodes, or arbitrary deformations. The full target inner product is \(\sum_h u_h\overline{v_h}\), not the mean over 60 samples. Each degree has source dimension \((\ell+1)^2\).

## Proof
**1. The normalized reproducing kernel.** Identify \(S^3\) with \(SU(2)\). The degree-\(\ell\) harmonics are the \((\ell+1)^2\) matrix coefficients of the irreducible \(SU(2)\)-module \(W_\ell=\mathrm{Sym}^\ell(\mathbb C^2)\). Orthogonality of matrix coefficients for Haar probability measure gives
\[
 K_\ell(p,q)=(\ell+1)\operatorname{tr}W_\ell(q^{-1}p)
 =(\ell+1)U_\ell(\operatorname{Re}(q^{-1}p)),
\]
where \(U_0(t)=1\), \(U_1(t)=2t\), \(U_{j+1}(t)=2tU_j(t)-U_{j-1}(t)\). In particular \(K_\ell(p,p)=(\ell+1)^2\), and the normalization is fixed, not a free scalar. For even \(\ell\), the character \(\operatorname{tr}W_\ell\) is invariant under \(q\mapsto-q\), so the kernel on selected icosians depends only on \(h,k\in H\).

**2. Restriction to \(A_5\).** The five conjugacy-class sizes in \(H\) are \(1,15,20,12,12\). The induced \(SU(2)\) rotation half-angles of representatives are respectively \(0,\pi/2,\pi/3,\pi/5,2\pi/5\). The formula \(\operatorname{tr}W_\ell(g)=\sin((\ell+1)\theta)/\sin\theta\) gives the five character values \((\ell+1,a,b,c,d)\) in the finding. Orthogonality against each irreducible \(A_5\) character yields the displayed integer multiplicities \(m_\rho\); the character-table orthogonality also proves completeness of the five components. This is the full \(\Gamma\)-representation restriction, not merely its invariant subspace.

**3. Spectrum and interpolation.** For \(h,k\in H\), the sample Gram entry is \(G_\ell(h,k)=(\ell+1)\sum_\rho m_\rho\chi_\rho(h^{-1}k)\). On the \(d_\rho^2\)-dimensional matrix-coefficient sector, convolution by \(\chi_\rho\) with unnormalized summation acts as \(60/d_\rho\); on other sectors it vanishes, by Schur orthogonality. This proves all five squared-singular-value formulas. Let
\[
 (P_\rho y)(h)=\frac{d_\rho}{60}\sum_{k\in H}\chi_\rho(h^{-1}k)y(k),
\qquad
 G_\ell^+=\sum_{m_\rho>0}\frac{d_\rho}{60(\ell+1)m_\rho}P_\rho.
\]
These \(P_\rho\) are mutually orthogonal projectors. The data \(y\) are attainable exactly when \(P_\rho y=0\) for every zero-multiplicity sector. In that case
\[
 F_y(x)=\sum_{h\in H}(G_\ell^+y)(h)K_\ell(x,q_h)
\]
is a harmonic interpolant and is the unique interpolant of minimum source norm, with \(\lVert F_y\rVert_2^2=\langle y,G_\ell^+y\rangle\). This proves constructive sufficiency, not just a rank statement.

**4. Finite ranks and the permanent cutoff.** Each of \(a,b,c,d\) depends only on \(k=\ell/2\) modulo \(2,3,5\), respectively. Therefore the character inner product obeys
\[
 m_\rho(\ell+60)=m_\rho(\ell)+d_\rho.
\]
It suffices to compute the five nonnegative integer multiplicities for the 30 even representatives \(\ell=0,2,\ldots,58\). Substituting their finite residues into the explicit formula gives exactly the two displayed rank tables. For any even \(\ell\ge60\), write \(\ell=60t+r\) with \(t\ge1\) and \(r\) one of those 30 even residues. Then \(m_\rho(\ell)=m_\rho(r)+td_\rho>0\) for all five irreducibles. This proves full rank for all and only the asserted degrees, with no appeal to finite numerical extrapolation.

**5. The unique rank-59 tight degree.** A rank-59 sample operator is missing only the 1-dimensional trivial \(A_5\) sector, with all other sectors present. Equality of its four positive eigenvalues requires \(m_3/3=m_{3'}/3=m_4/4=m_5/5\). Equivalently, the class function \(\operatorname{tr}W_\ell\) must be constant on all four nonidentity conjugacy classes: it is a combination of the regular and trivial characters. Its common nonidentity value must equal \(a=\pm1\). The periodic class values then force either \(k\equiv0\pmod{30}\) (value \(+1\)) or \(k\equiv29\pmod{30}\) (value \(-1\)). The first case has no rank-59 degree (rank 1 for \(\ell=0\), full rank for positive multiples of 60). The second has rank 59 only at \(k=29\), i.e. \(\ell=58\), by the multiplicity shift above. There \(\chi_{58}(1)=59\) and \(\chi_{58}(g)=-1\) for all nonidentity \(g\in A_5\). Hence \(G_{58}\) has diagonal \(59^2\) and off-diagonal \(-59\), exactly \(3540I_{60}-59\mathbf1\mathbf1^*\), proving the displayed projector identity and minimum-norm formula.

**6. Conditioning.** For each fixed character row the correction \(m_\rho(\ell)-d_\rho(\ell+1)/60\) is bounded and 60-periodic in \(\ell\). Consequently all full-rank eigenvalues are \((\ell+1)^2+O(\ell+1)\), uniformly across the five sectors, and their largest-to-smallest ratio is \(1+O(1/\ell)\).

## Verification
The accompanying `check_600cell.py` reconstructs the 120 quaternions, verifies their norms, antipodal pairing and multiplication closure in the exact ring \(\mathbb Z[\varphi]/2\), independently checks class counts on 60 lines, checks the \(A_5\) character orthogonality and all integer multiplicities, and compares direct 60-by-60 Gegenbauer Gram eigenvalues with the predicted five spectral sectors for each even degree from 0 through 60. It verifies the tight projector identity and the full-rank/last-defect assertions. The unrestricted rank result is proved by the explicit period shift and not inferred from numerical tests. Run with `python check_600cell.py`; numerical diagonalization requires NumPy as declared in `requirements.txt`.

## Relationship to prior work
The identification of the 600-cell with the binary icosahedral group and its quaternionic class geometry is classical; Koca–Al-Ajmi–Koca (arXiv:0906.2109, submitted 11 June 2009) gives explicit quaternionic representatives and class structure. Hirao–Nozaki–Tasaka (arXiv:2507.01358, Theorem 1.2(iii), 2025) **already determines exactly the even degrees with vanishing global harmonic sums** on the 600-cell, including degree 58; this is equivalent to detecting the missing **trivial** character sector. Those vanishings, and the previously established 11-design property, are explicitly not presented here as novel. The present claim instead gives every **nontrivial** sector, all singular values and pointwise interpolation images, and characterizes the unique tight codimension-one sampling degree.

An earlier 600-cell cumulative-band calculation identifies the first surjective band containing degrees zero through seven, but band surjectivity does not imply individual-degree surjectivity at 20 or thereafter. Earlier representation theory of the icosahedral group (Backhouse–Gard, 1974) underlies the character methods; its abstract asserts representation restriction and symmetrization, without a visible claim about the normalized 60-line sampling Gram or minimum-norm recovery. The 1974 full article could not be compared line by line, leaving publication-priority risk for implicit equivalent spectral deductions.

## Limitations
The spectral result concerns one even harmonic degree at a time, not an arbitrary spectral band, odd harmonics, perturbed nodes, or nonuniform weights. It determines finite pointwise interpolation and exact conditioning, not a new characterization of spherical-design strength. The group-character decomposition and standard reproducing kernel are prior ingredients. The representation-theoretic technique is classical; the combination and exact interpolation classification are the proposed addition. Earlier work might contain an equivalent class-matrix decomposition, particularly in the not fully accessible 1974 source. Independent verification by another mathematical researcher has not been undertaken.

## References
1. M. Koca, M. Al-Ajmi, N. O. Koca, *Quaternionic Representation of Snub 24-Cell and its Dual Polytope Derived From \(E_8\) Root System*, arXiv:0906.2109 (first version 2009-06-11), https://arxiv.org/html/0906.2109v2 .
2. M. Hirao, H. Nozaki, K. Tasaka, *Spherical designs for finite quaternionic unit groups and their applications to modular forms*, arXiv:2507.01358 (first version 2025-07-02), https://arxiv.org/pdf/2507.01358 ; *Algebraic Combinatorics* 9 (2026), 1157–1178, DOI 10.5802/alco.505.
3. N. B. Backhouse and P. Gard, *The representation theory of the icosahedral group*, *Journal of Physics A* 7 (1974), 2101–2108, DOI 10.1088/0305-4470/7/17/004 (abstract inspected; full text unavailable).
4. H. Cohn and A. Kumar, *Universally optimal distribution of points on spheres*, first public version arXiv:math/0607446 (2006-07-19), *Journal of the American Mathematical Society* 20 (2007), 99–148, DOI 10.1090/S0894-0347-06-00546-7 (600-cell as an exceptional configuration and spherical-design reference, not a source of individual-degree spectra).
