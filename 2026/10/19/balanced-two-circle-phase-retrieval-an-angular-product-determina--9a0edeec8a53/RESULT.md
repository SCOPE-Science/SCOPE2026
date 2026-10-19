# Balanced two-circle phase retrieval: an angular-product determinant and all optimal grids

## Finding

**Theorem (balanced sampling determinant, global design, and the quadratic converse).** Fix an integer \(d\ge2\) and \(0<r<1\). Let \(U=\{u_1,\ldots,u_{2d}\}\) and \(V=\{v_1,\ldots,v_{2d}\}\) be two sets of pairwise distinct numbers of modulus one, and write \(u_j=e^{i\theta_j}\) and \(v_j=e^{i\phi_j}\). Measure the \(4d\) squared magnitudes
\[
\bigl\{|P(u_j)|^2:1\le j\le2d\bigr\}\quad\text{and}\quad
\bigl\{|P(rv_j)|^2:1\le j\le2d\bigr\}
\]
of an arbitrary complex polynomial \(P\) of degree at most \(d\).

Define the real \(4d\)-square sampling matrix \(M\) as follows. Its columns consist of the \(2d-1\) coefficients of degrees \(0,\ldots,d-1\) on the outer circle, the analogous \(2d-1\) coefficients on the inner circle, and two shared highest-harmonic coordinates. In the respective ordered bases \(1,\cos t,\sin t,\ldots,\cos((d-1)t),\sin((d-1)t)\), each outer row has these outer columns evaluated at \(\theta_j\), zero inner columns, and final entries \((\cos(d\theta_j),\sin(d\theta_j))\). Each inner row has zero outer columns, its inner basis evaluated at \(\phi_j\), and final entries \((r^d\cos(d\phi_j),r^d\sin(d\phi_j))\).

Writing \(\Delta(U)=\prod_{1\le i<j\le2d}(u_j-u_i)\) and \(\Pi_U=\prod_{j=1}^{2d}u_j\), and analogously for \(V\), one has the **exact determinant identity**
\[
\boxed{\;|\det M|=2^{1-2d}r^d\,|\Delta(U)\Delta(V)|\,|\Pi_U-\Pi_V|.\;}
\]
Consequently, \(M\) is invertible exactly when \(\Pi_U\ne\Pi_V\). Under this condition the measurements uniquely determine every polynomial \(P\) up to multiplication by a scalar of modulus one.

For the Hermitian lifting \(H\longmapsto (a(z)^TH\overline{a(z)})_{z\in U\cup rV}\), with \(a(z)=(1,z,\ldots,z^d)^T\), the real rank equals \(4d\) if \(\Pi_U\ne\Pi_V\), and exactly \(4d-1\) otherwise. Its real nullity is respectively \((d-1)^2\) and \((d-1)^2+1\).

Among all admissible choices of the two angular sets, the **sharp maximum determinant** is
\[
\boxed{\;\max_{U,V}|\det M|=2^{2-2d}r^d(2d)^{2d}.\;}
\]
Equality holds precisely when each set is the vertex set of a regular \(2d\)-gon and \(\Pi_V=-\Pi_U\). Equivalently, the two regular grids have relative rotation \((2k+1)\pi/(2d)\), modulo rotations fixing each grid.

At degree \(d=2\) the angular-product condition is also **necessary** for universal phase retrieval: when \(\Pi_U=\Pi_V\), distinct quadratic polynomials not related by a global phase give exactly the same eight squared-magnitude samples. In particular, all configurations of four outer and four inner distinct angles are classified by this single product equality.

## Assumptions and scope

All coefficients are complex; the two circles have distinct positive radii, normalized to \(1\) and \(r\). Every within-circle sampling node is distinct. Different circles do not share points. Samples are labeled; their order only affects the sign, not the absolute determinant. The coordinate system defining \(M\) is explicit and fixes determinant normalization. The exact optimal-design statement maximizes \(|\det M|\), not the smallest singular value or the nonlinear noise tolerance. Necessity of the angular-product condition for phase retrieval is proved only when \(d=2\); in all dimensions the condition is sufficient and exactly characterizes *linear interpolation of the two intensity profiles*.

## Proof

**Step 1: identify the full linear intensity-profile space.** For any Hermitian \((d+1)\)-square matrix \(H=(H_{jk})_{0\le j,k\le d}\), the real trigonometric polynomial
\[
F_\rho(t)=\sum_{j,k=0}^d H_{jk}\rho^{j+k}e^{i(j-k)t}
\]
is the intensity of a polynomial when \(H\) has rank one and is positive semidefinite. In general the coefficient of \(e^{ikt}\), for \(0\le k\le d\), is
\[
\widehat F_\rho(k)=\sum_{j=0}^{d-k}H_{j+k,j}\rho^{2j+k}.
\]
For every \(0\le k<d\), choosing the terms indexed by \(j=0,1\) gives an invertible two-by-two coefficient transformation between the circles \(\rho=1\) and \(\rho=r\): its determinant is a nonzero multiple of \(r^2-1\). For \(k=d\) there is only one complex coefficient, with \(\widehat F_r(d)=r^d\widehat F_1(d)\). The off-diagonal and diagonal Hermitian entries can be chosen independently, so the full real Hermitian image is exactly the space of pairs of real trigonometric polynomials of degree at most \(d\) obeying this single complex leading-harmonic relation. This space has dimension \(4d\). In its explicit coordinate basis, the sampling operator is precisely \(M\).

**Step 2: determine the only interpolation resonance.** Evaluation of real degree-at-most-\(d\) trigonometric polynomials at \(2d\) distinct angles has rank \(2d\), since multiplying a vanishing polynomial by \(z^d\) yields an ordinary polynomial of degree at most \(2d\) with those distinct roots. Therefore its real kernel is one-dimensional, generated up to a nonzero real scalar by
\[
Q_U(t)=\prod_{j=1}^{2d}2\sin\frac{t-\theta_j}{2}.
\]
The coefficient of \(e^{idt}\) in \(Q_U\) is \((-i)^{2d}\exp(-i\sum_j\theta_j/2)\), so its phase modulo real scaling depends only on \(\Pi_U^{-1/2}\). The analogous inner-circle null polynomial has top coefficient proportional to \(\Pi_V^{-1/2}\). A nonzero pair of these polynomials can satisfy the leading-harmonic relation from Step 1 exactly when their coefficient directions coincide as real lines, namely when \(\Pi_U=\Pi_V\). Hence \(\operatorname{rank}M\) equals \(4d\) off resonance and \(4d-1\) at resonance. Surjectivity established in Step 1 gives the asserted Hermitian lifting ranks and nullities.

**Step 3: the determinant constant.** For a set of \(2d\) angles, let \(T_U\) be the real \(2d\)-by-\((2d-1)\) evaluation matrix for harmonics below \(d\), and let \(W_U=\prod_{i<j}2\sin((\theta_j-\theta_i)/2)\). The ordinary complex Vandermonde identity, after changing the columns \(e^{\pm ikt}\) to \(\cos kt,\sin kt\), gives
\[
\bigl(\det[T_U,\cos(d\theta)],\det[T_U,\sin(d\theta)]\bigr)
=\varepsilon_U 2^{1-d}W_U\bigl(\sin(S_U/2),-\cos(S_U/2)\bigr),
\]
where \(S_U=\sum_j\theta_j\) and \(\varepsilon_U\in\{-1,1\}\) is an orientation sign. Expand \(\det M\) along the two shared last columns. The result, up to sign, is
\[
 r^d2^{2-2d}W_U W_V\sin((S_U-S_V)/2).
\]
Since \(|W_U|=|\Delta(U)|\) and \(|\Pi_U-\Pi_V|=2|\sin((S_U-S_V)/2)|\), this is exactly the claimed absolute determinant, with the factor \(2^{1-2d}\).

**Step 4: global optimality.** Each \(2d\)-square complex Fourier Vandermonde matrix with rows \((1,u_j,\ldots,u_j^{2d-1})\) has row norm \(\sqrt{2d}\). Hadamard's determinant inequality yields \(|\Delta(U)|\le(2d)^d\), with equality precisely when its rows are pairwise orthogonal; distinct unit nodes then form a regular \(2d\)-gon. The same applies to \(V\). Finally \(|\Pi_U-\Pi_V|\le2\), with equality exactly at \(\Pi_V=-\Pi_U\). These three bounds can be attained simultaneously, proving both the maximum and *all* maximizing configurations.

**Step 5: reconstruct the polynomial up to phase.** When \(M\) is invertible, equal samples of \(P,Q\) imply equality of their entire intensity functions on both circles by Step 1. If \(Q\equiv0\), at least \(2d\ge d+1\) distinct outer zeros force \(P\equiv0\). Otherwise let \(F=P/Q\), a rational function, and \(F^\#(z)=\overline{F(\overline z)}\). Equality of squared moduli on a circle of radius \(\rho\) gives the rational identity \(F(z)F^\#(\rho^2/z)=1\). Using \(\rho=1,r\) shows \(F^\#(w)=F^\#(r^2w)\). A nonzero rational function invariant under multiplication by \(0<r^2<1\) is constant, as follows by inspecting its Laurent series at zero. Thus \(P=cQ\), and the modulus equality gives \(|c|=1\).

**Step 6: the sharp quadratic converse.** For \(d=2\) at resonance, the Hermitian lifting map acts on a real nine-dimensional space and has rank seven. Its kernel therefore contains a two-dimensional real subspace. The determinant of Hermitian matrices is a continuous, odd real cubic on the unit circle of any such two-plane; it vanishes at some nonzero matrix \(H\). Any nonzero positive or negative semidefinite matrix in the sampling kernel is impossible: its zero quadratic form on the four distinct outer Vandermonde evaluation vectors forces it to vanish, since those vectors span \(\mathbb C^3\). Therefore \(H\) is necessarily indefinite and of rank two. Its positive and negative spectral parts are nonzero rank-one positive matrices with identical measurements, producing two non-phase-equivalent quadratics. For example, the same cardinal-grid angles on both circles give the ambiguity \(P(z)=1+iz^2\) and \(Q(z)=1-iz^2\).

## Verification

The bundled `verify_balanced.py` directly constructs \(M\) and the separately built real Hermitian lifting matrix, tests the exact determinant against numerical matrices for degrees one through five, and checks resonant and nonresonant ranks. Its exact symbolic section over rational and quadratic-algebraic numbers verifies the predicted rank distinction and explicit quadratic ambiguity. Execution from the bundled path reports 113 passed checks and maximum relative determinant error below \(8.0\times10^{-13}\). Finite checks confirm normalization and boundary examples; the all-degree claims and uniqueness are proved above without extrapolation from experiments.

## Relationship to prior work

Pohl, Li, and Boche (2017) establish recovery of polynomial coefficients from a minimal total number of magnitude samples on two concentric circles using **\(2d+1\)** points on the first and **\(2d-1\)** on the second, where \(d\) is the polynomial degree. That construction is a neighboring allocation, not the balanced \(2d+2d\) configuration. The present theorem obtains a complete parameter criterion and determinant for the balanced allocation, plus all globally determinant-optimal placements. Chalendar and Partington (2024) analyze continuous-circle holomorphic modulus uniqueness, not this finite placement criterion. Bodmann and Hammen (2013) demonstrate the optimal \(4d\) sample count through a different low-redundancy frame construction; that count alone is not claimed to be new.

## Limitations

No claim of phase-retrieval failure at angular-product resonance is made for degrees greater than two. The Hermitian *lifting* loses one rank at every degree, which by itself does not prove a rank-two kernel obstruction in higher dimensions. Maximization of \(|\det M|\) is a D-optimality statement in the stated Fourier coordinates; it does not imply optimal nonlinear conditioning. The proof assumes exact distinct sample locations and exact squared magnitudes; explicit perturbation bounds are not asserted. Bibliographic originality remains subject to a possible older equivalent finite-trigonometric-interpolation or cyclic Vandermonde identity.

## References

1. V. Pohl, N. Li, and H. Boche, *Phase retrieval in spaces of analytic functions on the unit disk*, SampTA 2017, DOI `10.1109/SAMPTA.2017.8024411`, author presentation dated July 4, 2017.
2. I. Chalendar and J. R. Partington, *Phase retrieval on circles and lines*, arXiv:2403.16255, initially public March 24, 2024; Canadian Mathematical Bulletin 67 (2024), 927–935.
3. B. G. Bodmann and N. Hammen, *Stable phase retrieval with low-redundancy frames*, arXiv:1302.5487, initially public February 22, 2013.
