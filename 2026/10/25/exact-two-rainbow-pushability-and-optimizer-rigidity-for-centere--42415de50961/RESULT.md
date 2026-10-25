# Exact two-rainbow pushability and optimizer rigidity for centered affine-regular pentagons

## Finding
Let \(P\subset\mathbb R^2\) be any centered affine-regular pentagon: an invertible linear image of the Euclidean regular pentagon with its vertex centroid at the origin. Let \(\pi_2(P)\) be the supremum, over independent \(P\)-vertex-valued random variables \(X,Y\) satisfying \(\mathbb EX+\mathbb EY=0\), of the probability that \(X,Y\) lie in a common edge. Then
\[
\boxed{\pi_2(P)=\frac{73+\sqrt5}{110}=0.6839642543\ldots.}
\]

Every maximizing ordered pair of vertex distributions is obtained from the explicit distributions below by a dihedral symmetry of the pentagon and, optionally, interchanging the two distributions. There are exactly ten distinct maximizing ordered pairs. This gives the complete optimizer classification, not only the extremal probability.

## Assumptions and scope
The two vertices are chosen **independently**, with potentially different probability laws. Each law has five nonnegative masses summing to one; the **sum** of their expectations vanishes, not necessarily each expectation separately. The distinguished center is the origin (the vertex centroid). Indices of consecutive pentagon vertices are taken modulo five. Two selected vertices lie on a common edge exactly when they coincide or their indices differ by one modulo five.

By invertible linear invariance of the definition (Martínez-Sandoval–Olvera-Sampieri, Section 3.1), it suffices to use the following affinely normalized pentagon. Put \(t=(\sqrt5-1)/2\) and
\[
 u_0=(1,0),\quad u_1=(0,1),\quad u_2=(-1,t),\quad
 u_3=(-t,-t),\quad u_4=(t,-1).
\]
This is an invertible linear image of the usual regular pentagon: its vertex sequence obeys the regular-pentagon recurrence \(u_{j+1}=t u_j-u_{j-1}\) and its centroid is zero.

## Proof
**1. Affine probability problem.** Write \(p_i=\Pr(X=u_i)\), \(q_i=\Pr(Y=u_i)\), and \(z=(p_0,\ldots,p_4,q_0,\ldots,q_4)\). The feasible polytope is
\[
\mathcal F=\{z\ge0:Az=(1,1,0,0)^\mathsf T\},
\]
where the first two rows of \(A\) sum the respective five masses and the last two rows are the two coordinates of \(\sum_i(p_i+q_i)u_i\). Define the symmetric \(5\times5\) cyclic matrix \(B\) by \(B_{ij}=1\) exactly if \(i=j\), \(i=j+1\), or \(i=j-1\pmod5\). For \(H=\begin{pmatrix}0&B\\ B&0\end{pmatrix}\), independence gives the exact objective
\[
 F(z)=\Pr(X,Y\text{ share an edge})=p^\mathsf TBq=\tfrac12z^\mathsf THz.
\]
The compact nonempty polytope \(\mathcal F\) has an optimizer.

**2. Minimal-support quadratic principle.** Among all maximizers choose one with the fewest positive coordinates, with support \(S\). On the affine face \(Az=b\), \(z_i=0\) for \(i\notin S\), choose a particular solution \(z_0\) and a basis matrix \(N\) of its tangent space (the kernel of the restricted \(A\)). The restricted Hessian \(G=N^\mathsf TH_SN\) must be *negative definite*, unless the tangent space is zero dimensional. Indeed, relative interior optimality makes the restricted gradient zero and Hessian negative semidefinite. If a nonzero tangent vector belonged to its Hessian kernel, the quadratic objective would be constant along the entire feasible line segment in that direction; moving to one endpoint would set an additional coordinate to zero, contradicting minimal support. Hence a positive-dimensional minimal-support optimizer is the **unique** affine stationary point on its support and has \(G\) negative definite.

**3. Exact finite exhaustion.** There are \(2^{10}-1=1023\) nonempty support masks. Under the dihedral action on the five vertex labels and exchange of the two probability laws, these form exactly 77 support orbits. The complete exact-field checker `verify_exact.py` enumerates those 77 representatives, over \(\mathbb Q(\sqrt5)\) with rational arithmetic. For each mask it solves the affine equations, obtains a tangent basis, checks negative definiteness by Sylvester's leading-principal-minor criterion, finds the unique stationary point, and retains it only if every mass on its support is *strictly* positive. This is an exhaustive global upper-bound argument by Step 2; no finite floating-point search is promoted to an infinite proof.

Only eleven representative masks survive. The mask is hexadecimal, with bits \(0\)–\(4\) referring to \(p\) and bits \(5\)–\(9\) to \(q\). Their stationary objective values are:

| Mask | Exact objective |
|---|---|
| `0x175` | \((73+\sqrt5)/110\) |
| `0xba` | \(3/4-\sqrt5/20\) |
| `0x16d` | \(4/5-\sqrt5/10\) |
| `0xab` | \(29/40-17\sqrt5/200\) |
| `0xa9` | \(7/5-2\sqrt5/5\) |
| `0xaa` | \(7/10-\sqrt5/10\) |
| `0x7c` | \(1/4-\sqrt5/20\) |
| `0x6d` | \(47/40-19\sqrt5/40\) |
| `0x6e` | \(11/40-3\sqrt5/40\) |
| `0x69` | \(1-2\sqrt5/5\) |
| `0x6c` | \(3/10-\sqrt5/10\) |

The first value is strictly larger than all ten others, as checked by exact signs in the same quadratic field. Therefore every *minimal-support* global maximizer has a support in the orbit of `0x175`. The final step below excludes any additional, larger-support maximizers.

**4. Attainment and rigidity.** Put
\[
 a=\frac{45-3\sqrt5}{110},\qquad
 b=\frac{30-2\sqrt5}{110},\qquad
 c=\frac{35+5\sqrt5}{110}.
\]
All three are positive, \(a+b+c=1\), and \(2b+ta-(1+t)c=0\). The two probability vectors
\[
 p=(b,0,c,0,a),\qquad q=(b,a,0,c,0)
\]
are therefore normalized and collectively centered: \(\sum_i(p_i+q_i)u_i=0\). Their common-edge probability is
\[
 b^2+c^2+2a(b+c)=\frac{73+\sqrt5}{110}.
\]
This proves sharpness. The top support orbit consists of exactly ten distinct masks. On each, the restricted Hessian is strictly negative definite, so its positive stationary distribution is unique. It remains to rule out maximizers of nonminimal support that might lie on flat portions of a higher-dimensional support face. At the displayed maximizer on mask `0x175`, write the full objective gradient as \(Hz\) and use a Lagrange multiplier \(\lambda\) satisfying \((Hz)_i=(A^{\mathsf T}\lambda)_i\) on its six positive coordinates. The **reduced gradients** on the four absent coordinates, in order \(1,3,7,9\), are exactly
\[
\frac{5-4\sqrt5}{55},\quad -a,\quad -a,\quad \frac{5-4\sqrt5}{55},
\]
all strictly negative. Hence every feasible first-order motion that introduces an absent coordinate has strictly negative directional derivative: the contribution of the positive coordinates cancels by the affine constraints, and the absent contributions are negative.

If a larger-support global maximizer existed, its restricted Hessian could not be strictly negative definite (the exact list has no other globally attaining strict stationary mask). Its restricted Hessian is negative semidefinite by local maximality and therefore has a null direction, along which the objective is constant. Following such a flat feasible segment to an endpoint reduces the support. Iterating must reach a minimal-support maximizer on the top orbit, and the final flat segment would introduce an absent coordinate into that maximizer, contradicting the strict reduced-gradient inequality. The same argument applies to every dihedral/interchange image. Thus **all** maximizers are the ten symmetry-related pairs.

## Verification
Run `python3 verify_exact.py` in an environment with the Python 3.10+ standard library. The script uses exact rational pairs \(a+b\sqrt5\), implements sign tests by rational-square comparisons, and prints the eleven surviving representative masks and their exact values. Its assertions verify the maximum and all integer/radical calculations. The checker carries out 77 support-orbit cases representing all 1023 nonempty supports; the reduction to these cases is justified in Step 2 and explicitly implemented in the script. A separate numerical constrained optimization was used solely as a sanity check, not as evidence for the global upper bound.

## Relationship to prior work
Martínez-Sandoval and Olvera-Sampieri (arXiv:2610.17157, first posted 2026-10-12) introduce \(\pi_r(P)\), prove its affine invariance, compute its cubical values, give a general facet-depth bound, and explicitly ask for exact values on further centered polytopes (Sections 3, 4, and 7). Their cubical calculation and general bound do **not** determine this pentagonal value. The centered affine-regular pentagon is the first odd regular polygon beyond the triangle and lacks the antipodal vertex pairing used in centrally symmetric constructions. Unlike values for centered cross-polytopes and affine-regular hexagons, this value comes from a strictly concave two-dimensional stationary problem and is a nontrivial quadratic irrational. Published studies of affine diameters and of geometric frame optimization for the regular pentagon involve different observables and do not imply this maximum probability.

## Limitations
The statement assumes the distinguished balancing point is the vertex centroid; translation to an arbitrary other interior point changes the constraint and is not covered. It settles \(r=2\) only, and it does not classify arbitrary (non-affine-regular) pentagons or other polygons. The finite exact checker, while designed as an exhaustive proof component, has not undergone an independent external audit. Overlap with unindexed earlier literature cannot be excluded by bibliographic searches alone.

## References
1. Leonardo Martínez-Sandoval and Ariadna Olvera-Sampieri, *Pushed colorful polytopal KKMS Theorem and orthogonal star transversals*, arXiv:2610.17157, first posted 2026-10-12. https://arxiv.org/abs/2610.17157 (especially Sections 3.1, 4.1–4.2, and 7).
2. Public mathematical record, *Affine-diameter multiplicity law for affine-regular pentagons*, https://github.com/published-finding corpus/2026/tree/main/2026/10/11/SCOPE-affine-diameter-multiplicity-law-for-affine-regular-pentagons--79c71e04b203 (different invariant; checked for overlap).
3. Public mathematical record, *The regular pentagon uniquely maximizes total two-volume for five-vector Parseval frames*, https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-the-regular-pentagon-uniquely-maximizes-total-2-volume-for-five--e4efa70f2feb (different optimization and constraints).
