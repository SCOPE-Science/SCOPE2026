# Positive flat-band classification for an unequal-edge magnetic tubular ladder

## Finding
For \(k>0\), define \(D_h:\sin(kh)=0\), \(D_r:\sin(kr)=0\), and \(D_s:\sin(ks)=0\). The magnetic ladder defined below has an infinite-multiplicity eigenvalue \(k^2\) if and only if at least one condition holds:

1. \(D_h\) and \((D_r\text{ or }D_s)\).
2. \(D_r\) and \(D_s\) with \(\cos(kr)=\cos(ks)\).
3. Exactly one rung \(d\in\{r,s\}\) is Dirichlet, the other rung \(e\) and the rails are not Dirichlet, \(\cos A=0\), and
   \[2\cot(kh)+\cot(ke)-\cos(kd)\csc(ke)=0.\]

No energy \(k^2=0\) is flat. This criterion is independent of whether the edge-length ratios are rational, except insofar as the displayed Dirichlet equalities occur.

## Assumptions and scope
The graph has vertices \(T_n,B_n\) for each \(n\in\mathbb Z\). Rails connect \(T_n\) to \(T_{n+1}\) and \(B_n\) to \(B_{n+1}\), each with length \(h>0\). Two distinct transverse edges connect \(T_n\) to \(B_n\), with respective lengths \(r,s>0\); multiple edges are permitted. All edges carry the positive magnetic Laplacian with continuous vertex values and magnetic Kirchhoff outward-derivative sums zero. The two rail phase increments in the chosen gauge are \(+A\) and \(-A\), while both transverse edges have zero magnetic potential. We use Bloch multiplier \(e^{it}\), \(t\in[-\pi,\pi)\). The magnetic convention is fixed by the pair of horizontal contributions \(2k(\cos(t\pm A)-\cos(kh))/\sin(kh)\); replacing \(A\) by \(-A\) leaves all results unchanged.

A flat band means \(k^2\) is a fiber eigenvalue for almost every Bloch phase; equivalently the infinite periodic operator has an \(L^2\) eigenvalue of infinite multiplicity. We classify all such energies, not their band gaps or density of states.

## Proof
For an edge of length \(L\) with endpoint values \(U,V\), if \(\sin(kL)\ne0\), the outward derivative at the initial endpoint is \(k(V\csc(kL)-U\cot(kL))\). If \(\sin(kL)=0\), the endpoint values instead obey \(V=\varepsilon U\), where \(\varepsilon=\cos(kL)\in\{+1,-1\}\), and the initial-end derivative is a free variable \(p\), while the opposite-end outward derivative is \(-\varepsilon p\). These statements follow directly by solving \(-f''=k^2f\) on the edge and include every Dirichlet singularity.

First suppose none of the three edge lengths is Dirichlet. With \(c_L=\cos(kL)\) and \(s_L=\sin(kL)\), the two Bloch vertex values satisfy the homogeneous system
\[
\begin{pmatrix}
2(\cos(t+A)-c_h)/s_h-c_r/s_r-c_s/s_s & 1/s_r+1/s_s\\
1/s_r+1/s_s & 2(\cos(t-A)-c_h)/s_h-c_r/s_r-c_s/s_s
\end{pmatrix}\binom{U_T}{U_B}=0.
\]
Its determinant, as a trigonometric polynomial in \(t\), has coefficient \(2/s_h^2\ne0\) in front of \(\cos(2t)\), since \(\cos(t+A)\cos(t-A)=[\cos(2t)+\cos(2A)]/2\). No such energy is an eigenvalue of a positive-measure set of fibers.

Suppose next \(D_h\) holds. For all Bloch phases except finitely many, horizontal propagation at momentum \(k\) forces \(U_T=U_B=0\). Non-Dirichlet transverse edges then vanish. Each rail may support one independent sine amplitude, and each Dirichlet transverse edge may support one. The two Kirchhoff equations constrain these amplitudes independently with nonzero coefficients on the two rail amplitudes for generic \(t\). Hence their kernel dimension equals the number of transverse Dirichlet edges, and is positive exactly under condition 1. This also proves sufficiency without dividing by a vanishing sine.

Now suppose \(\sin(kh)\ne0\). If both transverse edges are Dirichlet, writing \(\varepsilon_r=\cos(kr)\), \(\varepsilon_s=\cos(ks)\), their endpoint constraints are \(U_B=\varepsilon_r U_T=\varepsilon_s U_T\). If the parities differ then \(U_T=U_B=0\), all rail amplitudes vanish, and the two transverse sine amplitudes are constrained by the nonsingular matrix \(\bigl(\begin{smallmatrix}1&1\\varepsilon_r&\varepsilon_s\end{smallmatrix}\bigr)\). Hence no eigenfunction exists. If the parities agree, choosing the two transverse sine amplitudes oppositely gives a nonzero eigenfunction with both vertex values zero, supported inside one cell for every \(t\); this proves condition 2. Non-Dirichlet rails cannot generate another possible flat energy in the parity-mismatched case.

Finally suppose exactly one transverse edge of length \(d\) is Dirichlet and the other, of length \(e\), is not, while \(s_h\ne0\). Let \(\varepsilon=\cos(kd)\). Its endpoint relation forces \(U_B=\varepsilon U_T\). Zero vertex values force all edge amplitudes zero, so a nonzero state requires \(U_T\ne0\). Denote by \(p\) the free initial derivative on this transverse Dirichlet edge. The two Kirchhoff equations are
\[
0=U_T\left[2k\frac{\cos(t+A)-c_h}{s_h}-k\cot(ke)+\varepsilon k\csc(ke)\right]+p,
\]
\[
0=\varepsilon U_T\left[2k\frac{\cos(t-A)-c_h}{s_h}-k\cot(ke)+\varepsilon k\csc(ke)\right]-\varepsilon p.
\]
Eliminating \(p\) and dividing by \(2kU_T\) gives
\[
2\frac{\cos t\cos A-c_h}{s_h}-\cot(ke)+\varepsilon\csc(ke)=0.
\]
This holds on a positive-measure set of \(t\) exactly when \(\cos A=0\) and condition 3 holds. Conversely those conditions make it valid for every \(t\), and choosing \(U_T=1\) determines a nonzero Bloch eigenfunction at each phase.

At zero momentum, a zero-energy magnetic eigenfunction must be covariantly constant along every edge. Any nonzero such Bloch state exists only at isolated compatible Bloch phases, never on a positive-measure set, so zero is not a flat band. These cases exhaust all Dirichlet/non-Dirichlet combinations and establish necessity and sufficiency.

## Verification
The included standalone `verify.py` symbolically checks the nonvanishing second-harmonic coefficient, the cancellation of the rail phases in the one-rung matching condition, the parity-mismatch rank, and an exact flux-resonant example.

Take \(h=3/4\), \(r=1\), \(s=2\arctan(1/2)/\pi\), \(A=\pi/2\), and \(k=\pi\). Only the rung of length \(r\) is Dirichlet. Since \(\cot(3\pi/4)=-1\), \(\cot(2\arctan(1/2))=3/4\), and \(\csc(2\arctan(1/2))=5/4\), the resonance equation reads \(-2+3/4+5/4=0\). Thus \(\pi^2\) is a flat-band eigenvalue caused purely by the half-flux cancellation, not by a rail–rung Dirichlet intersection or a two-rung Dirichlet cycle. The equality case \(h=r=s=1\) recovers all the source's \((\pi n)^2\) flat bands.

## Relationship to prior work
Kiselev and Ryadovkin, *Phase Transition in a Periodic Tubular Structure*, arXiv:2303.00872 (public 2023-03-02), later SIAM J. Appl. Math. 84 (2024), 890–914, analyzes the equal-length graph \(h=r=s=1\). In Section 5, Lemma 5.1 and Theorem 5.2 classify its flat Dirichlet levels \((\pi n)^2\) and its continuous bands for all magnetic phases. The present result concerns a new three-length deformation: it gives an if-and-only-if classification with a magnetic resonance that is invisible in the equal-length specialization. The source's general Bloch formalism is used, but its equal-length spectral classification is not claimed as new.

The 2006 spectral analysis by Brüning, Geyler and Pankrashkin considers a different, two-dimensional magnetic square graph. The 2020 two-leg tight-binding ladder of Huang, Hosur and Pal has a different finite-dimensional hopping Hamiltonian rather than Kirchhoff metric-edge equations. Those theories do not immediately imply the displayed three-length matching classification.

## Limitations
The result concerns only two equal-length rail orbits and two parallel transverse edges with the specified magnetic gauge, not arbitrary metric tubes. It determines flat-band *energies*, not a complete formula for Bloch-band multiplicities, global gap geometry, or normalized eigenstate density. A literature-equivalent matching formula under other conventions remains possible. Positive energies are classified exactly; zero is excluded by covariant-constancy and Bloch-phase compatibility.

## References
1. A. V. Kiselev and K. Ryadovkin, *Phase Transition in a Periodic Tubular Structure*, arXiv:2303.00872 (first public 2023-03-02), SIAM Journal on Applied Mathematics 84 (2024), 890–914, DOI 10.1137/23M157274X, Sections 3 and 5.
2. J. Brüning, V. Geyler and K. Pankrashkin, *Cantor and Band Spectra for Periodic Quantum Graphs with Magnetic Fields*, Communications in Mathematical Physics 269 (2007), 87–105, DOI 10.1007/s00220-006-0050-0.
3. Y. Huang, P. Hosur and H. K. Pal, *Quasi-flat-band physics in a two-leg ladder model and its relation to magic-angle twisted bilayer graphene*, Physical Review B 102 (2020), 155429, DOI 10.1103/PhysRevB.102.155429.
