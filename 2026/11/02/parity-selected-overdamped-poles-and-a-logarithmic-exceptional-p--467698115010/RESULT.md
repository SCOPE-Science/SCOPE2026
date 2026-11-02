# Parity-selected overdamped poles and a logarithmic exceptional-point shift in terminally lossy quantum paths

## Finding
For a uniform finite quantum path with a single irreversible terminal absorber, the exact number of purely damped spectral modes is controlled by path parity. For odd lengths there is exactly one simple purely imaginary eigenvalue at every positive absorption strength. For even lengths there are none below a unique critical strength, a second-order exceptional point at the critical strength, and exactly two distinct purely imaginary eigenvalues above it. The even-length critical strength decreases strictly with path length and has an explicit logarithmically corrected approach to its infinite-length limit.

Write \(g=\kappa/(2J)\). For every even \(N\ge2\), define
\[
G_N(u)=\frac{\cosh((N+1)u)}{\sinh(Nu)},\quad u>0,\qquad
g_N=\min_{u>0}G_N(u).
\]
The minimum exists and has a unique minimizer \(u_N>0\). The number of eigenvalues on the *strict negative imaginary axis*, counted as distinct locations, is zero for \(0<g<g_N\), one for \(g=g_N\), and two for \(g>g_N\). At equality the single eigenvalue is algebraically double and geometrically simple, hence is a genuine second-order exceptional point. For odd \(N\ge3\), there is exactly one such eigenvalue, algebraically simple, for every \(g>0\).

For even lengths, \(g_N>1\), the thresholds strictly decrease as the even length grows, and
\[
\boxed{g_N=1+\frac{\log(4N)+1+o(1)}{2N}\qquad(N\to\infty\text{ through even integers}).}
\]
For instance, \(g_2=2\), \(g_4=1.553026040673962\ldots\), and \(g_6=1.392028805631664\ldots\). The physical absorption-strength threshold is \(\kappa_N=2Jg_N\).

## Assumptions and scope
Let \(N\ge2\) be an integer, \(J>0\) a real hopping amplitude, and \(\kappa>0\) the total irreversible population-loss rate at the terminal site. On the one-excitation Hilbert space with orthonormal basis \(\{|j\rangle:1\le j\le N\}\), consider the non-Hermitian survival-sector operator
\[
H_N=J\sum_{j=1}^{N-1}\bigl(|j\rangle\langle j+1|+|j+1\rangle\langle j|\bigr)-\frac{i\kappa}{2}|N\rangle\langle N|.
\]
Here a purely damped pole means an eigenvalue \(\lambda=-i\omega\), with \(\omega>0\). The exceptional point is a degeneracy of \(H_N\), not a claim about the jump-inclusive Lindblad Liouvillian. The result makes no assertion about possible spectral collisions away from the imaginary axis, nor about the optimal rate for mean absorption time.

## Proof
**Characteristic polynomial.** Let \(x=\lambda/(2J)\) and \(g=\kappa/(2J)\). A determinant expansion of the tridiagonal matrix, using the last-site diagonal \(-i\kappa/2\), gives
\[
\det(\lambda I-H_N)=J^N\bigl[U_N(x)+ig\,U_{N-1}(x)\bigr],
\]
where \(U_k\) denotes the Chebyshev polynomial of the second kind: \(U_0=1\), \(U_1=2x\), and \(U_{k+1}=2xU_k-U_{k-1}\). If \(H_Nv=\lambda v\), taking the imaginary part of \(v^*H_Nv\) shows
\[
\operatorname{Im}\lambda=-\frac\kappa2\frac{|v_N|^2}{\|v\|^2}<0.
\]
The strict inequality holds because an eigenvector with \(v_N=0\) would vanish identically by backward use of the nonzero off-diagonal couplings. Therefore every imaginary-axis eigenvalue has the form \(\lambda=-2iJ\sinh u\) for a unique \(u>0\).

**Even parity.** For \(N=2m\), direct substitution into the Chebyshev recurrence yields
\[
U_{2m}(-i\sinh u)=(-1)^m\frac{\cosh((2m+1)u)}{\cosh u},\qquad
U_{2m-1}(-i\sinh u)=i(-1)^m\frac{\sinh(2mu)}{\cosh u}.
\]
Consequently the characteristic equation on the imaginary axis is exactly \(g=G_N(u)\). Its logarithmic derivative and second derivative are
\[
(\log G_N)'=(N+1)\tanh((N+1)u)-N\coth(Nu),
\]
\[
(\log G_N)''=(N+1)^2\operatorname{sech}^2((N+1)u)+N^2\operatorname{csch}^2(Nu)>0.
\]
The first derivative tends to negative infinity at zero and to \(1\) at infinity. Thus it has exactly one zero \(u_N\), the nondegenerate global minimum. As \(G_N\) diverges at both endpoints, horizontal lines at height \(g\) meet its graph zero, one, or two times as claimed. At the minimum, the characteristic polynomial has a zero of exactly order two: locally it is a nonvanishing analytic factor times \(g-G_N(u)\), whose second derivative in \(u\) is nonzero, while \(d\lambda/du=-2iJ\cosh u\neq0\). Every eigenvalue of an irreducible tridiagonal chain has a one-dimensional eigenspace because its first coordinate determines all others. Hence the algebraically double eigenvalue is defective, with one Jordan block of size two.

**Odd parity.** For \(N=2m+1\), the same Chebyshev identities give the imaginary-axis root equation
\[
g=\frac{\sinh((N+1)u)}{\cosh(Nu)}.
\]
This right-hand side rises strictly from zero to infinity: its logarithmic derivative is \((N+1)\coth((N+1)u)-N\tanh(Nu)>0\). Hence every \(g>0\) has one and only one root, and it is algebraically simple by the nonzero derivative.

**Length monotonicity.** For any fixed \(u>0\), the function \(G_N(u)\) decreases strictly as the positive real parameter \(N\) increases, since
\[
\partial_N\log G_N(u)=u\bigl[\tanh((N+1)u)-\coth(Nu)\bigr]<0.
\]
Evaluating at the unique minimizer for the shorter even chain shows strict decrease of \(g_N\) along even lengths. Since \(\cosh((N+1)u)>\sinh(Nu)\), every \(g_N>1\). Choosing \(u=(\log N)/N\) shows \(\limsup g_N\le1\), hence \(g_N\downarrow1\).

**Sharp finite-size asymptotic.** Set \(q_N=e^{-2Nu_N}\), \(r_N=e^{-2u_N}=q_N^{1/N}\). The minimizer equation is equivalent, by elementary hyperbolic identities, to
\[
1=(2N+1)q_N+(2N+1-q_N)q_Nr_N.
\]
For all relevant \(N\), \((4N+2)^{-1}<q_N<(2N+1)^{-1}\). Therefore \(r_N\to1\), and the preceding identity implies \(q_N\sim(4N)^{-1}\). Consequently
\[
u_N=\frac{\log(4N)+o(1)}{2N}.
\]
Finally
\[
 g_N=e^{u_N}\frac{1+q_Nr_N}{1-q_N}
 =1+u_N+2q_N+o(N^{-1})
 =1+\frac{\log(4N)+1+o(1)}{2N}.
\]
All limits are along even positive integers. This completes the proof.

## Verification
A standalone script, `check_passive_chain_ep.py`, reconstructs the finite matrix independently of the Chebyshev recurrence and compares determinants, purely imaginary eigenvalue residuals, parity counts, threshold ordering, and sample large-length asymptotic values. Executing it with Python, NumPy, and SciPy passed 495 numerical checks; representative dimensionless thresholds are \(g_2=2\), \(g_4\approx1.55302604\), \(g_6\approx1.39202881\), \(g_{10}\approx1.25429098\), and \(g_{100}\approx1.03542380\). The all-length theorem, multiplicity assertion, and asymptotic coefficient are proved analytically above; finite tests are not substitutes for those proofs.

## Relationship to prior work
Coherent transport with irreversible traps on finite paths was studied by Mülken and collaborators (arXiv:0705.3700, first submitted 25 May 2007). Their paper develops survival statistics and examines a linear chain with two terminal traps; its inspected discussion does not furnish the one-terminal imaginary-axis pole count or logarithmic finite-length exceptional-point law. Rudner and Levitov (arXiv:0807.2048) study losses on a whole sublattice of a bipartite lattice and a topological transport transition, rather than a lone terminal sink. Downing and Saroka (arXiv:2112.04305; Communications Physics 4, 254 (2021)) treat arbitrary oligomer lengths with balanced gain on one endpoint and loss on the other; their parity-dependent exceptional points concern a different matrix for all \(N\ge3\). The two-site example here can be related to the familiar gain/loss dimer by subtracting a uniform imaginary scalar, and is not separately claimed as historically novel. Riberi (arXiv:2605.08056) solves a semi-infinite boundary-absorbing walk and identifies a boundary-localized mode, without establishing the finite-chain parity law in the material accessible for comparison. The finite-chain integrated mean-capture-time identities studied elsewhere are not equivalent to the exceptional-point classification proved here.

## Limitations
The theorem determines the *purely imaginary axis* portion of the finite spectrum and the exceptional point located there; it does not assert that no other exceptional points exist off that axis. It applies to a uniform, nearest-neighbor, zero-onsite-energy chain with exactly one Markovian terminal loss and excludes nonuniform couplings, trapping at multiple sites, disorder, and feedback. Some related older and newer complete texts were unavailable for exhaustive historical-priority comparison; mathematical correctness is distinct from a definitive claim of publication priority. No independent validation has been performed.

## References
1. O. Mülken, A. Blumen, T. Amthor, C. Giese, M. Reetz-Lamour, and M. Weidemüller, “Survival Probabilities in Coherent Exciton Transfer with Trapping,” *Physical Review Letters* **99**, 090601 (2007); arXiv:0705.3700; https://arxiv.org/abs/0705.3700 .
2. M. S. Rudner and L. S. Levitov, “Topological Transition in a Non-Hermitian Quantum Walk,” *Physical Review Letters* **102**, 065703 (2009); arXiv:0807.2048; https://arxiv.org/abs/0807.2048 .
3. C. A. Downing and V. A. Saroka, “Exceptional points in oligomer chains,” *Communications Physics* **4**, 254 (2021); arXiv:2112.04305; https://www.nature.com/articles/s42005-021-00757-3 .
4. F. Riberi, “An Exactly Solvable Absorbing Quantum Walk,” arXiv:2605.08056 (2026); https://arxiv.org/abs/2605.08056 .
5. P. E. Parris, “One-dimensional quantum transport in the presence of traps,” *Physical Review B* **40**, 4928–4937 (1989); https://doi.org/10.1103/PhysRevB.40.4928 .
