# Exact fixed-concurrence envelope for Bell-diagonal Hilbert–Schmidt geometric discord
## Finding
For a two-qubit Bell-diagonal state
\[\rho=\sum_{j=1}^4 p_j\lvert B_j\rangle\langle B_j\rvert,\qquad p_j\ge0,\qquad \sum_jp_j=1,\]
let \(C\) denote concurrence and let \(D_G\) be the unnormalized one-sided Hilbert–Schmidt geometric discord, so a Bell state has \(D_G=1/2\). Then for every fixed \(C\in[0,1]\) the set of attainable discord values is exactly one interval.

For \(C>0\),
\[D_{\min}(C)=\frac{C^2}{2},\]
while \(D_{\min}(0)=0\). The exact upper boundary is
\[D_{\max}(C)=\begin{cases}
\dfrac{1+2C+5C^2}{16},&0\le C\le\dfrac1{13},\\[4pt]
\dfrac{(1+2C)^2}{18},&\dfrac1{13}\le C\le1.
\end{cases}\]
The two upper extremal families exchange optimality exactly at \(C=1/13\).

For \(C>0\), a lower-bound extremizer, up to permutation of the Bell basis, has probabilities
\[\left(\frac{1+C}2,\frac{1-C}2,0,0\right).\]
For \(0\le C\le1/13\), an upper-bound extremizer is
\[\left(\frac{1+C}2,\frac{1-C}4,\frac{1-C}4,0\right),\]
and for \(1/13\le C\le1\), an upper-bound extremizer is
\[\left(\frac{1+C}2,\frac{1-C}6,\frac{1-C}6,\frac{1-C}6\right).\]
At \(C=0\), classical Bell-diagonal axis states attain the lower endpoint, and the rank-three family above attains the upper endpoint \(1/16\).

## Assumptions and scope
The statement concerns only two-qubit Bell-diagonal density operators and the squared Hilbert–Schmidt geometric discord introduced for two-qubit states by Dakić, Vedral, and Brukner and studied in the Bell-diagonal setting by subsequent work. The normalization is the unnormalized convention
\[D_G(\rho)=\frac14\left(c_1^2+c_2^2+c_3^2-\max_i c_i^2\right)\]
for a Bell-diagonal correlation vector \((c_1,c_2,c_3)\). Thus a Bell state has discord \(1/2\). No monotonicity or operational-resource interpretation of the Hilbert–Schmidt quantity is asserted.

## Proof
Assume first \(C>0\). Exactly one Bell eigenvalue exceeds \(1/2\); relabel it as
\[p_1=\frac{1+C}2.\]
Write the other three eigenvalues as \(q_1,q_2,q_3\), so
\[q_1+q_2+q_3=\frac{1-C}2.\]
For a fixed Bell vertex, the three absolute correlation coordinates are, up to permutation,
\[r_i=|c_i|=C+2q_i,\qquad i=1,2,3.\]
Consequently
\[C\le r_i\le1,\qquad r_1+r_2+r_3=1+2C.\]
Conversely, every triple satisfying these relations determines nonnegative \(q_i=(r_i-C)/2\) with the required sum, so this is an exact parametrization of the fixed-concurrence slice.

Order the coordinates as \(x\ge y\ge z\). The Bell-diagonal discord becomes
\[D_G=\frac{y^2+z^2}{4}.\]
The feasible set in the \((y,z)\)-plane is the triangle determined by
\[z\ge C,\qquad y\ge z,\qquad 2y+z\le1+2C.\]
Its three vertices correspond to
\[(x,y,z)=(1,C,C),\]
\[(x,y,z)=\left(\frac{1+C}2,\frac{1+C}2,C\right),\]
and
\[(x,y,z)=\left(\frac{1+2C}3,\frac{1+2C}3,\frac{1+2C}3\right).\]
The lower bound follows immediately from \(y,z\ge C\), with equality at the first vertex.

Because \(y^2+z^2\) is convex, its maximum on this triangle is attained at a vertex. The first vertex cannot maximize for \(C<1\). The other two give
\[D_{\mathrm{face}}=\frac{1+2C+5C^2}{16},\qquad D_{\mathrm{iso}}=\frac{(1+2C)^2}{18}.\]
Their difference factors as
\[D_{\mathrm{iso}}-D_{\mathrm{face}}=\frac{(1-C)(13C-1)}{144}.\]
Hence the face family is maximal for \(0\le C\le1/13\), and the isotropic family is maximal for \(1/13\le C\le1\). Equality also occurs at the common Bell-state endpoint \(C=1\).

At \(C=0\), the Bell-diagonal separable region is the octahedron \(|c_1|+|c_2|+|c_3|\le1\). With \(x\ge y\ge z\ge0\), maximizing \((y^2+z^2)/4\) over \(x+y+z\le1\) gives \((x,y,z)=(1/2,1/2,0)\) and value \(1/16\), while an axis state gives zero.

Finally, each fixed-
concurrence feasible slice is connected and \(D_G\) is continuous, so its image is a connected subset of the real line containing both endpoints. Therefore every value between the displayed lower and upper bounds is attained.

## Verification
The proof uses only the Bell-basis eigenvalue formula for concurrence and the standard closed Bell-diagonal formula for Hilbert–Schmidt geometric discord. The algebraic reduction was independently replayed in `verify.py` using exact rational arithmetic. The script checks the two extremal formulas, the factorization producing the crossover \(C=1/13\), and an exact rational grid of Bell-diagonal probability vectors against the claimed bounds. The grid is supplementary evidence; the infinite statement rests on the analytic triangle argument above.

## Relationship to prior work
Luo and Fu give the general Hilbert–Schmidt geometric-discord framework, and Yao et al. specialize it to Bell-diagonal states, writing the discord as one quarter of the two smallest squared correlation coordinates. Yao et al. also quote the sharp Bell-violation interval at fixed concurrence, identify Werner and rank-two Bell-diagonal extremizers for that different optimization, and record the Werner relation between concurrence and geometric discord. Their theorem optimizes Bell violation at fixed discord, not geometric discord at fixed concurrence.

Lang and Caves give the tetrahedral geometry and concurrence/entropic-discord level surfaces for Bell-diagonal states; their discord is the entropy-based discord rather than the Hilbert–Schmidt distance. Later work explicitly notes that a separable Bell-diagonal state can have normalized geometric discord \(1/8\), exceeding the separable Werner value \(1/9\); in the present unnormalized convention this is the endpoint \(1/16\) versus \(1/18\). That observation is consistent with the low-concurrence face branch but does not provide the full fixed-concurrence envelope or the \(1/13\) crossover.

## Limitations
The result is restricted to Bell-diagonal two-qubit states and to the squared Hilbert–Schmidt geometric discord. Hilbert–Schmidt geometric discord is known to have undesirable monotonicity behavior under local operations on the unmeasured subsystem, so the theorem should be read as an exact state-space geometry statement rather than a claim that \(D_G\) is a universally valid resource monotone. The literature search found no statement of this exact fixed-concurrence envelope, but absence from the inspected sources is not a proof of global bibliographic uniqueness.

## References
1. B. Dakić, V. Vedral, and Č. Brukner, “Necessary and sufficient condition for non-zero quantum discord,” arXiv:1004.0190; Phys. Rev. Lett. 105, 190502 (2010).
2. S. Luo and S. Fu, “Geometric measure of quantum discord,” Phys. Rev. A 82, 034302 (2010), DOI 10.1103/PhysRevA.82.034302.
3. M. D. Lang and C. M. Caves, “Quantum Discord and the Geometry of Bell-Diagonal States,” arXiv:1006.2775; Phys. Rev. Lett. 105, 150501 (2010).
4. Y. Yao et al., “Bell violation versus geometric measure of quantum discord and their dynamical behavior,” arXiv:1303.4830.
5. F. M. Paula, T. R. de Oliveira, and M. S. Sarandy, “Geometric quantum discord through the Schatten 1-norm,” arXiv:1302.7034; Phys. Rev. A 87, 064101 (2013).
6. “Maximizing quantum discord from interference in multi-port fiber beamsplitters,” npj Quantum Information (2021), DOI 10.1038/s41534-021-00502-2.
