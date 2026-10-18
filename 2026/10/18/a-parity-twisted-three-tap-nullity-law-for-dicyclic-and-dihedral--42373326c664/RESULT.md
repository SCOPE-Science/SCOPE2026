# A parity-twisted three-tap nullity law for dicyclic and dihedral groups

## Finding
For each integer \(m\geq2\), let
\[
Q_{4m}=\langle a,b\mid a^{2m}=1,\ b^2=a^m,\ bab^{-1}=a^{-1}\rangle
\]
be the dicyclic group, and let \(D_{4m}\) be the dihedral group obtained by replacing \(b^2=a^m\) with \(b^2=1\). Both have \(4m\) elements, indexed as \(a^i b^\epsilon\), with \(0\leq i<2m\) and \(\epsilon\in\{0,1\}\). For any unordered three-element set \(S\), write \(T_S f(x)=\sum_{s\in S}f(s^{-1}x)\) on complex-valued functions on the corresponding group, and write \(\nu_Q(S)\), \(\nu_D(S)\) for its complex nullities. Compare the operators for the *same three coordinate labels* in the two groups.

**Exact nullities.** Put \(N=2m\). If the three taps all lie in one coset of \(\langle a\rangle\), choose their three exponents \(t,t+u,t+v\pmod N\), and put \(g=\gcd(N,u,v)\), \(q=N/g\). Then
\[
\nu_Q(S)=\nu_D(S)=\begin{cases}4g,&3\mid q\text{ and }\{(u/g)\bmod3,(v/g)\bmod3\}=\{1,2\},\\0,&\text{otherwise.}\end{cases}
\]
If the taps occupy both cosets, define \(u\pmod N\), nonzero, to be the exponent difference of the two taps in the same coset. Set \(g_m=\gcd(m,u)\) and \(g_N=\gcd(N,u)\). Then
\[
\nu_Q(S)=\begin{cases}2g_m,&3\mid m/g_m,\\0,&\text{otherwise,}\end{cases}
\qquad
\nu_D(S)=\begin{cases}2g_N,&3\mid N/g_N,\\0,&\text{otherwise.}\end{cases}
\]
The singular supports are **identical under the coordinate correspondence**, but their positive nullities differ: exactly for mixed-coset supports with \(v_2(u)>v_2(m)\), the dicyclic nullity is **half** the dihedral nullity; in every other case the two nullities coincide. Here \(v_2(k)\) is the exponent of \(2\) dividing a nonzero integer \(k\); the condition is well defined on the nonzero residue \(u\pmod{2m}\).

**Exact singular-support incidence counts.** Write \(r=v_3(m)\), \(s=v_2(m)\). The counts of singular supports wholly in one coset, in mixed cosets, and among the mixed supports with *strictly halved* dicyclic nullity are, respectively,
\[
C_{\rm pure}=\frac{2m^3}{3}(1-3^{-2r}),\qquad
C_{\rm mixed}=8m^3(1-3^{-r}),\qquad
C_{\rm half}=\frac{4m^3}{2^s}(1-3^{-r}).
\]
All are integers. In particular, every unweighted three-tap convolution is invertible precisely when \(3\nmid m\). When \(3\mid m\), a fraction \(2^{-(s+1)}\) of the *singular mixed-coset supports* experience a strict halving of nullity. For example, at \(m=3\) the \(220\) possible supports contain \(160\) singular supports, \(72\) of which have halved nullity, while at \(m=6\) the corresponding numbers are \(2024\), \(1280\), and \(288\).

## Assumptions and scope
Each support comprises three **distinct** group elements with scalar coefficient \(+1\); neither inverse closure nor exclusion of the identity is assumed. The convolution acts over \(\mathbb C\), not in the residue characteristic of a parameter. The comparison between groups uses their fixed shared exponent/coset coordinate system, not an asserted group isomorphism. The parameter \(m\) is any integer at least \(2\). The terms "dicyclic" and \(Q_{4m}\) are used even when \(m\) is not a power of \(2\).

## Proof
**1. Complete Fourier-block decomposition.** Let \(z\) run over the \(N\)-th roots of unity. On \(\mathbb C^2\) set
\[
A_z=\begin{pmatrix}z&0\\0&z^{-1}\end{pmatrix},\qquad
B_z=\begin{pmatrix}0&z^m\\1&0\end{pmatrix}.
\]
These matrices satisfy \(A_z^N=I\), \(B_z^2=A_z^m=z^mI\) and \(B_zA_zB_z^{-1}=A_z^{-1}\), hence give an induced representation \(\rho_z\) of \(Q_{4m}\). Fourier transformation on the two cosets of the index-two cyclic subgroup \(\langle a\rangle\) decomposes the full \(4m\)-dimensional regular representation into precisely these \(N\) two-dimensional fibers, including the reducible ones when \(z=\pm1\). Therefore
\[
\nu_Q(S)=\sum_{z^N=1}\dim_{\mathbb C}\ker\Bigl(\sum_{t\in S}\rho_z(t)\Bigr).
\]
For \(D_{4m}\) the same decomposition holds with the upper-right entry of \(B_z\) equal to \(1\), because the reflection square is the identity.

**2. Three taps in one coset.** Multiplying a block on the left and/or right by an invertible group-representation matrix preserves nullity. The three rotation taps, or three reflection taps after factoring out an invertible \(B_z\), reduce to \(1+a^u+a^v\). Their block is diagonal with entries \(F_z=1+z^u+z^v\) and \(\overline{F_z}\). The sum of three unit complex numbers vanishes if and only if their values, after factoring out one, are \(1,\omega,\omega^2\), where \(\omega\) is a primitive cubic root of unity. With \(g=\gcd(N,u,v)\), the character-image map has period \(q=N/g\); the desired two ordered pairs occur exactly when \(3\mid q\) and the displayed two normalized exponent residues are \(\{1,2\}\). In that event precisely \(2g\) roots \(z\) give a **zero two-dimensional block**. Thus the nullity is \(4g\), with identical reasoning for the dihedral group.

**3. Two taps in one coset.** Multiplication by a group element reduces either mixed configuration to \(1+a^u+a^v b\) without affecting nullity; \(u\) is the same-coset displacement up to sign. The dicyclic fiber is
\[
M_z=\begin{pmatrix}1+z^u&z^{v+m}\\z^{-v}&1+z^{-u}\end{pmatrix},
\qquad \det M_z=|1+z^u|^2-z^m.
\]
If \(z^m=-1\), this determinant is strictly positive. If \(z^m=1\), it vanishes exactly when \(z^u\in\{\omega,\omega^2\}\), because \(|1+w|=1\) for a unit \(w\) precisely at the two primitive cubic roots. Every singular block has rank one: both off-diagonal entries are nonzero. The allowed roots now form \(\mu_m\), and exactly \(2\gcd(m,u)\) satisfy this cubic condition if \(3\mid m/\gcd(m,u)\); otherwise there are none. This proves the dicyclic mixed formula. For dihedral blocks the determinant is \(|1+z^u|^2-1\) for every \(z\in\mu_N\), yielding the same formula with \(N\) instead of \(m\).

The two divisibility tests are equivalent because \(3\)-adic orders in \(m\) and \(2m\) coincide. Also \(\gcd(2m,u)/\gcd(m,u)\) equals \(2\) precisely when \(v_2(u)>v_2(m)\), and otherwise equals \(1\). This proves the identical singular-support incidence and the exact parity-halving law.

**4. Census.** Let \(r=v_3(m)=v_3(N)\). In a single cyclic coset, fix one of the three taps as anchor, with ordered nonzero displacements \(u,v\). For each \(t\in\{0,\ldots,r-1\}\), the necessary and sufficient criterion is that \(v_3(u)=v_3(v)=t\) and that \(u/3^t\) and \(v/3^t\) have opposite nonzero residues modulo \(3\). Exactly \(2(N/3^{t+1})^2\) ordered pairs have this property. There are \(N\) anchors and two cosets, and each unordered triple is counted six times. Hence
\[
C_{\rm pure}=\frac{2N}{6}\sum_{t=0}^{r-1}2\Bigl(\frac{N}{3^{t+1}}\Bigr)^2
=\frac{N^3}{12}(1-3^{-2r})
=\frac{2m^3}{3}(1-3^{-2r}).
\]
For mixed cosets, a displacement \(u\pmod N\) leads to singularity exactly when it is **not** divisible by \(3^r\). There are \(N(1-3^{-r})\) such nonzero residues. The unordered pair contributes \(N/2\) choices per displacement, the opposite-coset singleton contributes \(N\) choices, and either coset may carry the pair. Thus
\[
C_{\rm mixed}=2\cdot\frac{N}{2}\cdot N\cdot N(1-3^{-r})=N^3(1-3^{-r}).
\]
Write \(s=v_2(m)\). The strictly-halved cases also require \(2^{s+1}\mid u\). Among residues modulo \(N=2^{s+1}(m/2^s)\), precisely \((m/2^s)(1-3^{-r})\) have both conditions. Therefore
\[
C_{\rm half}=N^2\frac{m}{2^s}(1-3^{-r})=\frac{4m^3}{2^s}(1-3^{-r}),
\]
as stated. When \(r=0\), all three counts vanish. This completes the proof.

## Verification
The standalone `check.py` independently constructs the full regular-convolution matrices from the dicyclic multiplication law and computes exact ranks over \(\mathbb Q\), without using Fourier blocks. Running `python check.py 9` exhaustively checks every three-element support for \(2\leq m\leq9\) and verifies the positive-nullity formulas and the two singular-support census formulas; its output is `run.log`.

The standalone `twist_check.py` compares the **same labeled triple** in the dihedral and dicyclic group laws, tests parity-halving and the three closed support counts for \(2\leq m\leq12\) by complete combinatorial enumeration, and additionally computes both complex-equivalent ranks over \(\mathbb Q\) for *every* triple at \(m=3\) and \(m=6\). Its output is `twist.log`. Both scripts require Python 3 and SymPy and should be run from their containing directory. They use exact rational arithmetic. These exhaustive bounded computations check finite instances only; the claims for all \(m\geq2\) follow from the preceding proof.

## Relationship to prior work
Paudel and Pinner [1, equation (17)] recall the general dicyclic group-determinant factorization, including the essential central-twist factor. Their object is the set and minimal size of integer group-determinant values, rather than a complete complex nullity and support census for three coefficient-one taps. Dai and Li [2] develop general Wedderburn/idempotent decompositions for dihedral and generalized quaternion group algebras. Behajaina and Legrand [3] characterize *integral spectra of inverse-closed Cayley graphs* over generalized dicyclic groups; their hypotheses do not include arbitrary three-tap nonsymmetric or identity-containing operators and their conclusion is integrality rather than singular-support incidence and exact nullities.

The Fourier block decomposition is standard. The distinguishing statement here is the explicit **paired parity-nullity comparison** between the split and nontrivially central-twisted extensions, together with the exact number of supports on which the twist halves the nullity. The corresponding dihedral formulas are a related, simpler calculation but do not alone determine which of its singular Fourier modes survive the central twist. A general determinant factorization can be specialized to detect zero determinants; by itself it does not tabulate multiplicities of kernel modes or enumerate the halving strata.

## Limitations
The result applies only to distinct **unweighted three-element supports** on these cyclic-index-two groups, with rank over \(\mathbb C\). It does not address arbitrary tap coefficients, other finite groups, or rank over positive-characteristic coefficient fields. The derivation specializes known representation formulas and does not claim them as new. The broad group-determinant and Cayley-spectral literature leaves a residual possibility of an equivalent unlocated special-case formulation; no independent audit has been performed. Finite verification is not substituted for the general proof.

## References
1. B. Paudel and C. Pinner, *Minimal Group Determinants For Dicyclic Groups*, arXiv:2102.04536v1, first publicly posted 2021-02-08, especially equation (17). https://arxiv.org/pdf/2102.04536
2. L. Dai and Y. Li, *Primitive decompositions of idempotents of the group algebras of dihedral groups and generalized quaternion groups*, arXiv:2205.00435v1, first posted 2022-05-01. https://arxiv.org/pdf/2205.00435
3. A. Behajaina and F. Legrand, *On Cayley graphs over generalized dicyclic groups*, arXiv:2202.11398v1, first posted 2022-02-23; see Section 3. https://arxiv.org/pdf/2202.11398
