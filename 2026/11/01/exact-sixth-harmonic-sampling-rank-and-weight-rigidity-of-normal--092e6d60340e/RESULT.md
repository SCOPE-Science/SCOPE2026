# Exact sixth-harmonic sampling rank and weight rigidity of normalized type-B root systems

## Finding
For every integer \(n\ge3\), let \(X_n\subset S^{n-1}\) be the normalized type-\(B_n\) root configuration consisting of all \(2n\) coordinate directions \(\pm e_i\) and all \(2n(n-1)\) long-root directions \((\pm e_i\pm e_j)/\sqrt2\), \(i<j\). Let \(E_{n,6}\) evaluate all real spherical harmonics of **exact degree six** at these \(2n^2\) points. Then
\[
\operatorname{rank}E_{n,6}=\begin{cases}6,&n=3,\\13,&n=4,\\n^2-1,&n\ge5.\end{cases}
\]
Equivalently, the kernel of the transpose evaluation on **antipodally symmetric** real weight arrays has dimension \(3\) for \(n=3,4\), and dimension \(1\) for all \(n\ge5\). In the latter case every such array annihilating all exact-degree-six harmonics is proportional to the orbit-constant array having weight \(16-n\) on each short root and weight \(4\) on each long root. The same orbit-constant relation holds for \(n=3,4\), but is not unique there.

A strictly positive real weight array on **all** the roots annihilating degree-six spherical harmonics exists exactly for \(3\le n\le15\). A nonzero nonnegative array exists exactly for \(3\le n\le16\); at \(n=16\) the invariant one is supported on the long roots. These existence conclusions also hold without requiring antipodal symmetry. The orbit-constant weight equation is a consequence of known invariant-harmonic methods; the distinguishing assertion here is the complete absence of additional non-invariant weight relations in all dimensions \(n\ge5\), together with the sharp small-dimensional rank exceptions and the full Gram decomposition.

## Assumptions and scope
Every root is a distinct unit vector, the sphere is the Euclidean sphere in \(\mathbb R^n\), and \(\mathcal H_6\) is the real vector space of restrictions of homogeneous degree-six harmonic polynomials. Equal evaluations at antipodes are unavoidable in even degree. Thus select the \(n^2\) projective representatives
\[
P_n=\{e_i:1\le i\le n\}\cup\{(e_i\pm e_j)/\sqrt2:1\le i<j\le n\}.
\]
The rank of evaluation on \(P_n\) equals that on \(X_n\). A weight on \(X_n\) is antipodally symmetric when \(w(v)=w(-v)\). The word 'positive' means strictly positive at every vertex. The finite dimensional computations below make no claim about degrees other than six.

Put \(D=(n-1)(n+1)(n+3)\). Define the zonal polynomial normalized by \(G_n(1)=1\):
\[
G_n(t)=\frac{(n+4)(n+6)(n+8)t^6-15(n+4)(n+6)t^4+45(n+4)t^2-15}{D}.
\]
By the spherical harmonic addition theorem, \(K_n=(G_n(p\cdot q))_{p,q\in P_n}\) is a strictly positive scalar multiple of \(E_{n,6}E_{n,6}^{\mathsf T}\) in an orthonormal harmonic basis. In particular it is positive semidefinite, and its rank equals the desired evaluation rank.

## Proof
**1. Exact entries.** Set \(x=G_n(0)\), \(y=G_n(1/2)\) and \(z=G_n(1/\sqrt2)\). Direct expansion gives
\[
x=-\frac{15}{D},\qquad y=\frac{n^3-42n^2+224n+672}{64D},\qquad z=\frac{(n-2)(n^2-10n-36)}{8D}.
\]
Let \(m=\binom n2\), let \(B\) be the \(n\times m\) unsigned incidence matrix of the complete graph on \(n\) vertices, and write \(A_1=B^{\mathsf T}B-2I\) for the adjacency matrix on unordered pairs sharing exactly one endpoint. We use \(J\) for the appropriately sized all-one matrix. The \(m\) long-root coordinate *differences*, formed from the two signs of each representative pair, have constant Gram eigenvalue
\[
a=1-x=\frac{(n+4)(n^2-n+3)}D>0.
\]
They are orthogonal, for \(K_n\), to the shorts and to all pair coordinate *sums*. This follows directly from the fact that \(G_n\) is even and the squared inner products involving another pair do not distinguish the two signs.

In the orthonormal coordinate basis of short roots and normalized sums of the two long-root representatives on each pair, the complementary \((n+m)\)-dimensional Gram block is exactly
\[
\begin{pmatrix}
(1-x)I_n+xJ_n&\sqrt2\,[xJ_{n,m}+(z-x)B]\\
\sqrt2\,[xJ_{m,n}+(z-x)B^{\mathsf T}]&(1-x)I_m+2(y-x)A_1+2xJ_m
\end{pmatrix}.
\]
All entries can be checked from squared dot products \(0,1/4,1/2,1\) among representatives.

**2. Pair-deviation and standard sectors.** Since \(BB^{\mathsf T}=(n-2)I_n+J_n\), \(B\) has full row rank for every \(n\ge3\). Its kernel has dimension \(m-n=n(n-3)/2\). On this kernel, \(A_1=-2I\) and \(J=0\). The Gram eigenvalue is therefore
\[
c=1+3x-4y=\frac{15(n-4)(n+4)(n+6)}{16D},
\]
with that multiplicity. This sector is absent at \(n=3\), has zero eigenvalue (multiplicity two) at \(n=4\), and is strictly positive for \(n\ge5\).

On the common \((n-1)\)-dimensional zero-sum coordinate representation, the Gram has the \(2\times2\) symmetric block
\[
S=\begin{pmatrix}
a&\sqrt{2(n-2)}(z-x)\\
\sqrt{2(n-2)}(z-x)&a+2(n-4)(y-x)
\end{pmatrix},
\]
repeated \(n-1\) times. Its exact determinant is
\[
\det S=\frac{15n(n-3)(n+4)^2(n+6)(n+8)}{32D^2}.
\]
Since the upper left entry \(a\) is positive, this block has rank one at \(n=3\) and rank two for every \(n\ge4\). These formulas account for all \(n-1\) nontrivial eigen-directions of \(BB^{\mathsf T}\).

**3. Orbit-constant sector.** The remaining two-dimensional sector, spanned by normalized all-one vectors on shorts and pairs, has Gram block
\[
T=\begin{pmatrix}
1+(n-1)x&\sqrt{2nm}\,[x+2(z-x)/n]\\
\sqrt{2nm}\,[x+2(z-x)/n]&a+4(n-2)(y-x)+2mx
\end{pmatrix}.
\]
The upper left entry is
\[
T_{11}=\frac{(n-2)(n+6)}{(n+1)(n+3)}>0,
\]
and direct expansion yields \(\det T=0\) for all \(n\ge3\) (the lower right entry is \((n-16)^2(n-2)(n+6)/(16D)\)). Consequently this block has rank exactly one. Its null vector, expressed as weights per *projective representative*, assigns \(16-n\) to each short representative and \(4\) to each long representative; direct substitution in both orbit row sums verifies annihilation. The same per-vertex weights on both antipodes produce the null relation on \(X_n\).

**4. Rank and positive weights.** The difference sector contributes \(m\) to rank, the pair-deviation sector contributes \(m-n\) unless \(n=3\) (absent) or \(n=4\) (zero), the standard sector contributes \((n-1)\) for \(n=3\) and \(2(n-1)\) for \(n\ge4\), and the constant sector contributes one. This yields \(6,13,n^2-1\), as stated. For \(n\ge5\), the only projective null direction is the stated orbit-constant one; for \(n=3,4\) exactly two further directions occur.

The displayed invariant weights are strictly positive precisely when \(3\le n\le15\), and nonnegative and nonzero when \(3\le n\le16\). Conversely, average any nonnegative real weight array over the signed-permutation group. Its average is invariant and remains nonzero if the original array is nonzero; if the original array was strictly positive, so is its average. Every invariant exact-degree-six annihilator is proportional to the displayed vector, so no such weights exist beyond these bounds, even without assuming invariance or antipodal symmetry. This completes the proof.

## Verification
A self-contained exact-rational Python verifier is supplied as `verify_b6.py`; run `python3 verify_b6.py` beside this file. It constructs the projective Gram entries directly from squared inner products, checks all displayed rational eigen-sector identities for dimensions \(3\le n\le22\), verifies the orbit null-weight identities, and independently computes exact rational matrix ranks in dimensions \(3,4,5,6\). Successful execution prints `TYPE_B_SIXTH_HARMONIC_EXACT_CHECK_OK 304`. These finite checks are consistency tests; the proof for all \(n\ge3\) is the algebraic block decomposition and sign argument above.

## Relationship to prior work
Bajnok's hyperoctahedral orbit-design theory and Nozaki–Sawa's invariant cubature analysis provide the relevant degree-six invariant harmonic equation on type-\(B\) orbits, and already imply the **orbit-constant** short/long weight ratio and its positivity transition; these are not claimed as new isolated discoveries. Bannai–Okuda–Tagami establish the exact harmonic-index design framework, using the same general addition-kernel principle. The present result concerns a distinct question: the *entire*, non-invariant exact-degree-six sampling map on the union of the two unit root orbits, including all additional possible weight relations, exceptional dimensions, and explicit spectral-sector multiplicities. Known long-root-only sampling results concern a proper subconfiguration and do not supply the mixed short–long rank and rigidity. A survey of the most relevant accessible texts and mathematical research records found no directly covering complete-rank statement; absence of a match is not a proof of first discovery.

## Limitations
The result addresses the normalized union of short and long type-\(B\) roots, not the two unnormalized Euclidean shells nor simultaneous degree-\(\le6\) design equations. The unique-null-vector assertion requires antipodally symmetric weights because odd antisymmetric weights annihilate all even harmonics automatically. The Gram formulas are normalized by \(G_n(1)=1\), not by an orthonormal basis convention, although ranks are convention-independent. The existence/positivity thresholds for invariant weights are already consequences of prior invariant theory. Full independent mathematical validation and an exhaustive historical priority check have not been performed.

## References
1. B. Bajnok, “Orbits of the hyperoctahedral group as Euclidean designs,” *Journal of Algebraic Combinatorics* **25** (2007), 375–397, DOI:10.1007/s10801-006-0042-3; published online 2006-11-14. Lawful author-paper access: arXiv:2406.04023 (later upload of this earlier work).
2. H. Nozaki and M. Sawa, “Note on cubature formulae and designs obtained from group orbits,” arXiv:1102.4891 (first public 2011-02-24), *Canadian Journal of Mathematics* **64** (2012), 1359–1377.
3. E. Bannai, T. Okuda, and M. Tagami, “Spherical designs of harmonic index \(t\),” arXiv:1308.5101 (2013-08-23).
4. C. Zhu et al., “More on spherical designs of harmonic index \(t\),” arXiv:1507.05373 (2015-07-20).
