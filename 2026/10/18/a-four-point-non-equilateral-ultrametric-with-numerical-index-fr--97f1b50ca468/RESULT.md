# A four-point non-equilateral ultrametric with numerical index \(\frac12\)
## Finding
There is a four-point non-equilateral metric space \(M\) whose **real** Lipschitz-free space has numerical index precisely \(\frac12\). Explicitly, for \(M=\{0,1,2,3\}\), assign \(d(0,1)=\frac12\) and \(d(i,j)=1\) to the five other distinct unordered pairs. Then
\[
n\bigl(\mathcal F(M)\bigr)=\frac12.
\]
This is the *smallest possible cardinality* of a non-equilateral metric attaining this value: the known complete three-point theorem rules out all non-equilateral metrics with at most three points. The four-point metric is an ultrametric (its only short edge is contained in triangles with the other two edges both equal to \(1\)).

## Assumptions and scope
All scalars are real. Let \(\delta_3=0\) and \(e_i=\delta_i\), \(i\in\{0,1,2\}\). The dual unit ball is the polytope of pinned real Lipschitz potentials
\[
Q=\{(f_0,f_1,f_2): |f_i|\le 1\ (i=0,1,2),\ |f_0-f_1|\le\tfrac12,\ |f_0-f_2|\le1,\ |f_1-f_2|\le1\}.
\]
The primal unit ball is the convex hull of the twelve oriented normalized molecules
\[
m_{ij}=\frac{\delta_i-\delta_j}{d(i,j)},\quad i,j\in M,\ i\ne j.
\]
For a real Banach space \(X\), the numerical radius of \(T:X\to X\) is
\[
v(T)=\sup\{|f(Tx)|:x\in S_X,\ f\in S_{X^*},\ f(x)=1\},
\quad n(X)=\inf_{\|T\|=1}v(T).
\]
The theorem concerns only this fixed four-point metric and the classical Banach-space numerical index, not a continuum of short-edge lengths or complex scalars.

## Proof
**1. Finite-dimensional reduction.** The dual polytope \(Q\) is the intersection of the twelve rational directed pair-difference inequalities \(f_i-f_j\le d(i,j)\), with \(f_3=0\). Its vertices can be reconstructed by solving every nonsingular triple of active boundary hyperplanes and retaining the feasible intersections. The exact procedure in `artifacts/verify.py` enumerates all such triples, uses Cramer's rule over rational numbers, and obtains exactly \(18\) distinct vertices. This is also consistent with the independently known six-state classification for a single shortened pair; no facet-count novelty is asserted here.

For any linear operator \(T\) on \(\mathcal F(M)\), compact polyhedral duality gives
\[
\|T\|=\max_{i\ne j,\ f\in\operatorname{ext}Q}|f(Tm_{ij})|.
\]
The finite-dimensional numerical-radius formula is
\[
v(T)=\max_{i\ne j,\ f\in\operatorname{ext}Q,\ f(m_{ij})=1}|f(Tm_{ij})|.
\]
To see the latter, write any unit vector \(x\) as a convex combination of molecules. If \(g\) norms \(x\), every molecule in this combination with positive weight is also normed by \(g\). On the exposed face of \(Q\) simultaneously norming those molecules, the linear functional \(g\mapsto g(Tx)\) is maximized in absolute value at a vertex of that face, hence at a vertex of \(Q\). Conversely, every displayed molecule and supporting functional is a valid norming pair. Thus the two finite maxima are exact, without restricting an arbitrary operator.

**2. Rational certificate of the universal inequality.** Identify the nine entries of \(T\) with a vector in \(\mathbb R^9\). The pairing \(f(Tm_{ij})\) is the dot product with the rank-one tensor \(f\otimes m_{ij}\). The checker reconstructs the \(18\) dual vertices, the \(56\) positively oriented supporting molecule–functional pairings, and their \(112\) signed numerical-radius rows. It then checks a complete certificate for each of the \(12\cdot18=216\) possible operator-norm pairing rows.

The accompanying file `artifacts/certificates.json` contains, for each objective tensor \(f\otimes m_{ij}\), a **nonnegative rational linear combination** of the \(112\) signed supporting tensors which agrees coefficient-by-coefficient with that objective and whose coefficients have sum at most \(2\). The verifier checks the identity of all nine coefficients and the bound on their total weight, not merely the value on a selected operator. Each supporting row has absolute pairing at most \(v(T)\), and therefore every objective pairing obeys
\[
|f(Tm_{ij})|\le2v(T),\qquad\text{hence}\qquad \|T\|\le2v(T).
\]
The companion certificate is fully included, and the independent finite arithmetic reconstruction needs only Python's standard library. Thus the lower bound \(n(\mathcal F(M))\ge\frac12\) is proved for every linear operator, not inferred from sampled matrices.

**3. Sharpness.** On the basis \((e_0,e_1,e_2)\), define \(T=\operatorname{diag}(1,1,-1)\). Substitution into the same exact finite norming-pair formula yields \(v(T)=1\) and \(\|T\|=2\), both verified with rational arithmetic. In particular, for the molecule \(m_{02}=e_0-e_2\) and dual vertex \(f=(1,\frac12,1)\), the pairing \(f(Tm_{02})=2\), giving the lower bound on \(\|T\|\). Therefore \(T/2\) has norm \(1\) and numerical radius \(\frac12\). Combining both bounds gives the asserted index.

**4. Minimal metric cardinality.** A two-point Lipschitz-free space is one-dimensional and has numerical index \(1\). Cobollo, Guirao and Montesinos proved that the real Lipschitz-free space of a three-point metric has numerical index \(\frac12\) **if and only if** its metric is equilateral. Our metric is non-equilateral and has four points, so its cardinality is minimal among all non-equilateral metric witnesses to numerical index \(\frac12\).

## Verification
Run `python3 artifacts/verify.py` from the folder containing this result and its `artifacts` subfolder. Expected line: `VERIFY_OK vertices=18 supporting=56 objectives=216 bound=2 radius=1 norm=2`. The replayer checks every polytope vertex, all \(216\) rational dual identities, nonnegative coefficients, coefficient sums, and the exact values of the sharp operator. All computations use `fractions.Fraction`; no floating-point tolerance, unbounded search, or external solver is needed at replay time. `artifacts/certificates.json` records all required rational certificates, and `artifacts/verify.py` reconstructs the defining geometry rather than merely trusting stored coordinates.

## Relationship to prior work
Cobollo, Guirao and Montesinos (2023) completely determine the numerical index of Lipschitz-free spaces on **three** points and prove that their numerical-index-\(\frac12\) instances are precisely equilateral. The present four-point witness locates the exact first failure of this rigidity. Established computations for equilateral metrics of all finite sizes apply to the \(d(0,1)=1\) endpoint but do not determine this strictly non-equilateral metric. An earlier five-point wheel example also has index \(\frac12\), but cannot imply four-point minimality.

The published exact *Hilbert distortion* formula for the one-short-pair four-point metric studies this **same family** but a different invariant, namely its Banach–Mazur distance to Euclidean space; no numerical-index equality follows from that result. Likewise, a published general *facet count* for independently shortened matching pairs includes this metric and explains its \(18\) dual vertices, but the number of facets does not determine the numerical index. The known numerical index formula for a four-point equiradial **star** uses three short edges (not one); the weighted four-cycle deformation has a different distance table; and the triangle obstruction for unweighted graph metrics or minimum-distance equilateral triples does not apply because the present unique minimum distance is \(\frac12\), not \(1\). These comparisons concern statements and parameter coverage, rather than names alone.

## Limitations
Only the specified real four-point metric is claimed. The argument does not establish a formula for a variable short-edge length or for arbitrary four-point ultrametrics. Its finite certificate is exhaustive **for this rational three-dimensional polytope**, not for all four-point metrics. The bibliographic novelty assessment is necessarily subject to obscure equivalent polyhedral presentations and papers not indexed in the searches; no independent scientific review has been performed.

## References
1. Ch. Cobollo, A. J. Guirao, V. Montesinos, *The numerical index of 2-dimensional Lipschitz-free spaces*, arXiv:2304.13183v1, first public 2023-04-25, particularly Corollary 5.3 (two-dimensional free spaces, three metric points).
2. D. Sain, K. Paul, P. Bhunia, S. Bag, *On the numerical index of polyhedral Banach spaces*, arXiv:1809.04778v2 (2018); general polyhedral numerical-index techniques.
3. *A five-point non-equilateral Lipschitz-free space with numerical index one half*, public mathematical record 9265557f0f91 (2026).
4. *Exact numerical index of four-point equiradial star Lipschitz-free spaces*, public mathematical record 7e5bebb360bb (2026).
5. *Minimum-distance triangles force numerical index one half for finite graph free spaces*, public mathematical record 27231dd8f5c9 (2026).
6. *Exact numerical index along the short-edge four-cycle deformation*, public mathematical record 961105f89184 (2026).
7. *Exact Hilbert distortion along a one-edge deformation of the four-point equilateral metric*, public mathematical record f6a1d49d869f (2026).
8. *Facet enumeration for equilateral metrics with independently shortened pairs*, public mathematical record 3bd6d7048744 (2026).
