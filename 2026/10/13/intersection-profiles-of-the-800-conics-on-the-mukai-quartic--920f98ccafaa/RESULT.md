# Intersection profiles of the 800 conics on the Mukai quartic
## Finding
Let \(X\subset\mathbb{P}^3\) be the Mukai quartic carrying the 800 irreducible conics constructed in Degtyarev's Leech-lattice model. For two distinct conics \(C,D\) from this configuration, the intersection number \(C\cdot D\) is always one of
\[
0,\;1,\;2,\;4.
\]
Across all \(\binom{800}{2}=319600\) unordered pairs, the complete distribution is
\[
N_0=72240,\qquad N_1=174720,\qquad N_2=72240,\qquad N_4=400.
\]

There are exactly two local intersection profiles. A class \(A\) of \(480\) conics has
\[
(n_0,n_1,n_2,n_4)=(179,440,179,1),
\]
while a class \(B\) of \(320\) conics has
\[
(n_0,n_1,n_2,n_4)=(183,432,183,1).
\]
The two-class quotient refines these profiles: for \(C\in A\), the counts inside \(A\) are \( (115,248,115,1)\) and the counts against \(B\) are \( (64,192,64,0)\); for \(C\in B\), the counts inside \(B\) are \( (87,144,87,1)\) and the counts against \(A\) are \( (96,288,96,0)\), in each case ordered by intersection multiplicities \(0,1,2,4\).

Naskręcki proves that the projective automorphism group splits the 800 conics into orbits of sizes \(160,160,480\). Because intersection profiles are projective invariants, the unique \(480\)-orbit is exactly \(A\), and the two \(160\)-orbits together form \(B\). Each conic has a unique multiplicity-\(4\) partner; these \(400\) pairs are the residual pairs in plane sections.

## Assumptions and scope
The result concerns the 800 irreducible conics on the complex Mukai quartic, equivalently the extremal 800-conic quartic identified in the cited literature. The computation uses Degtyarev's explicit Leech-lattice realization: square-\(4\) Leech vectors satisfying the five displayed linear pairing conditions in the source determine the conic classes. The result does not assert analogous profiles for other Barth--Bauer quartics or for the other large quartic configurations classified later.

Intersection numbers are numerical intersection products on the smooth K3 surface. No assertion is made here about the local distribution of intersection points for a pair beyond what follows from the numerical intersection number.

## Proof
Use the normalization of the Leech lattice in which the standard integer coordinate dot product is divided by \(8\). Degtyarev chooses vectors \(\bar h,a,u_1,u_2,u_3\) with Gram matrix
\[
\begin{pmatrix}
4&2&0&0&0\\
2&4&2&0&1\\
0&2&4&2&-1\\
0&0&2&4&0\\
0&1&-1&0&4
\end{pmatrix}
\]
and takes the conic vectors \(\ell\) among the square-\(4\) Leech vectors satisfying
\[
\ell\cdot\bar h=2,\qquad \ell\cdot a=1,\qquad
\ell\cdot u_1=\ell\cdot u_2=\ell\cdot u_3=0.
\]
The exact enumeration in the accompanying verifier reconstructs the extended binary Golay code, all \(196560\) minimal Leech vectors in the three standard coordinate families, and filters them by these conditions. It obtains exactly \(800\) vectors, split as \(192\) vectors of the \((\mp3,\pm1^{23})\)-type and \(608\) of the octad \((\pm2^8,0^{16})\)-type, matching the source construction.

For such a vector define \(x_\ell=\ell-\bar h/2\in\bar h^\perp\). In the Néron--Severi realization the Leech orthogonal summand carries the negative form and the conic class is represented by \(x_\ell+h/2\). Hence, for two conic vectors \(\ell,m\),
\[
C_\ell\cdot C_m
=-x_\ell\cdot x_m+\frac14h^2
=2-\ell\cdot m.
\]
The verifier exhausts the \(319600\) unordered pairs and gives the four global counts stated above. It also counts, for each of the \(800\) vertices, how many other conics have each of the four intersection numbers. Exactly two profiles occur, with multiplicities \(480\) and \(320\), and a second pass gives the displayed same-class and cross-class quotient counts.

For the multiplicity-\(4\) statement, a plane containing a conic \(C\) cuts the quartic as \(C+\widetilde C\), where \(\widetilde C\sim h-C\) is the residual conic. Since \(C\cdot h=2\) and \(C^2=-2\),
\[
C\cdot\widetilde C=C\cdot(h-C)=4.
\]
The enumeration shows that every conic has exactly one multiplicity-\(4\) neighbor, so the \(400\) numerical pairs are exactly these residual plane-section pairs. The residual involution also explains the equality \(n_0=n_2\): replacing \(D\) by \(h-D\) changes \(C\cdot D\) from \(m\) to \(2-m\).

Finally, projective automorphisms preserve intersection products. Naskręcki's orbit sizes are \(160,160,480\). An orbit of size \(480\) cannot lie in the \(320\)-element profile class, so it equals the \(480\)-element class \(A\); the remaining two \(160\)-orbits exhaust \(B\).

## Verification
Run `python3 artifacts/verify.py` from the package root. The script uses only the Python standard library and exact integer arithmetic. It reconstructs the Golay code and checks its weight enumerator, reconstructs the relevant Leech minimal vectors, checks the source Gram matrix and conic constraints, verifies that exactly \(800\) conic vectors survive, computes all pairwise intersection numbers, checks both local profiles and the two-class quotient counts, and verifies that the multiplicity-\(4\) relation is a perfect matching of \(400\) pairs.

The computation is exhaustive for the source's finite Leech-vector model; it is not a numerical sample. The identification of the \(160+160+480\) projective orbit sizes is a published premise from Naskręcki rather than something rederived by the verifier.

## Relationship to prior work
Degtyarev's 2021 paper constructs the 800 conics through the Leech lattice and proves their effectiveness and irreducibility. Naskręcki gives explicit equations for all 800 conics and proves that the projective group has three conic orbits of sizes \(160,160,480\). The later 2024 classification proves that \(800\) is the sharp maximum and that the extremal quartic is unique up to projective equivalence.

The inspected statements do not give the complete pairwise intersection-number census, the two local profiles, or the profile-to-projective-orbit identification above. Naskręcki displays an adjacency graph only for a selected 20-conic Néron--Severi basis, not the full 800-conic configuration. The 2024 work treats configurations as graphs. Its version-1 main text was searched for the profile numbers and graph-profile terminology, and the later companion PDF `4tab.pdf` was searched for the distinctive profile numbers; no statement of these invariants was located. The exposed GAP file `GAP/2/4Leech.txt` reconstructs the standard Leech-vector families and residual duality, but does not state the claimed numerical profile. Other ancillary files remain a residual literature risk.

## Limitations
The originality conclusion is literature-bounded. The companion PDF and the most directly relevant exposed Leech GAP file were inspected, but the 2024 arXiv entry contains many additional ancillary files. An equivalent machine-readable profile could still occur elsewhere in that corpus. The claim is therefore the exact mathematical invariant stated and proved above, not a claim that no prior data set could be postprocessed to recover it.

The calculation uses the published Leech-lattice model and does not independently reprove the global Torelli step establishing that those \(800\) lattice classes are precisely the irreducible conics on the smooth quartic. That geometric realization is a premise from the cited source.

## References
1. A. Degtyarev, *800 conics on a smooth quartic surface*, arXiv:2102.08163v1; Journal of Pure and Applied Algebra 226 (2022), 107077.
2. B. Naskręcki, *Explicit equations of 800 conics on a Barth-Bauer quartic*, arXiv:2108.13402v1.
3. A. Degtyarev, *Conics on smooth quartic surfaces*, arXiv:2407.00493v1.
