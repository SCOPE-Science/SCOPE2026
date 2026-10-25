# Exact Euclidean facial distance of hypersimplices and a rank-driven minimizing-face transition

## Finding
For integers \(n\ge4\) and \(2\le k\le n-2\), let the (non-simplex) hypersimplex be
\[
\Delta_{k,n}=\{x\in[0,1]^n:\sum_{i=1}^n x_i=k\},\qquad t=\min\{k,n-k\}.
\]
Its *Euclidean facial distance* (also called pyramidal width) is
\[
\Phi(P)=\min_{\varnothing\ne F\subsetneq P\text{ a face}}
\operatorname{dist}\big(F,\operatorname{conv}(\operatorname{vert}(P)\setminus\operatorname{vert}(F))\big).
\]
Define the positive integer
\[
H(n,t)=\begin{cases}
n(n-2)-(n-2t)^2,&n\le4t,\\
\lfloor n^2/4\rfloor+2n(t-1),&n\ge4t.
\end{cases}
\]
The two branches agree at \(n=4t\). Then the exact answer is
\[
\boxed{\Phi(\Delta_{k,n})=\sqrt{\frac{n}{H(n,t)}}.}
\]
This is a simultaneous exact evaluation for all intermediate ranks, not an asymptotic bound. The diameter is \(\sqrt{2t}\), so the dimensionless geometric condition number is \(\sqrt{n/[2tH(n,t)]}\).

There is a sharp transition in which faces realize this minimum. Every nonvertex face is specified uniquely by fixing \(a\) coordinates to zero and \(b\) coordinates to one, leaving a positive-dimensional smaller hypersimplex. By complementing coordinates, assume \(k\le n/2\). The minimizing faces have exactly the following pairs \((a,b)\):

- When \(n\le4k\): precisely \((n-k-1,k-1)\), hence only edges.
- When \(n>4k\) is even: precisely \((k-1+n/2,k-1)\).
- When \(n>4k\) is odd: precisely \((k-1+\lfloor n/2\rfloor,k-1)\) and \((k-1+\lceil n/2\rceil,k-1)\).

Every coordinate permutation of the indicated face types attains the minimum, and no other face does. For \(k>n/2\), exchange the roles of fixed zeros and fixed ones. At \(n=4k+1\), edges and two-dimensional faces both minimize; further into the sparse-rank regime, minimizers have increasing dimension. This transition has no analogue in a description that considers facet distances alone.

## Assumptions and scope
All distances are ambient Euclidean distances in \(\mathbb R^n\), or equivalently intrinsic Euclidean distances in the hyperplane \(\sum_i x_i=k\). The values \(n,k\) are integers in the stated ranges. The full-dimensional ambient Euclidean ball is not involved. Every proper nonempty face is included, not merely facets or vertices. The known simplex endpoints \(k=1\) and \(k=n-1\) are intentionally excluded from the principal assertion.

## Proof
**1. Face classification.** A proper positive-dimensional face is obtained by fixing disjoint coordinate sets \(A,B\) to zero and one, respectively. Put \(a=|A|\), \(b=|B|\), \(r=n-a-b\), and \(j=k-b\). It is positive dimensional precisely when
\[
0\le a\le n-k-1,\quad 0\le b\le k-1,\quad a+b\ge1,
\quad 1\le j\le r-1.
\]
Its face dimension is \(r-1\). Indeed the residual coordinates form \(\Delta_{j,r}\), and the only facet inequalities of a nontrivial hypersimplex are coordinate inequalities. A zero-dimensional face is a binary vertex.

**2. Exact distance from a positive-dimensional face.** Let \(F\) have parameters \((a,b,r,j)\), and write \(Q_F=\operatorname{conv}(\operatorname{vert}(\Delta_{k,n})\setminus\operatorname{vert}(F))\). Both convex sets and the Euclidean metric are invariant under permutations within \(A,B\), and the remaining coordinate block \(R\). Averaging any closest pair under these permutations cannot increase its distance. Thus the closest pair may be chosen block-constant, with the point of \(F\) equal to
\[
x=(0\text{ on }A,\ 1\text{ on }B,\ j/r\text{ on }R).
\]
For the point \(y\in Q_F\), define nonnegative total violations
\[
u=\sum_{i\in A}y_i,\qquad v=\sum_{i\in B}(1-y_i).
\]
Every vertex outside \(F\) violates at least one prescribed zero or one, so \(u+v\ge1\). As \(\sum_i y_i=k\), the remaining block averages differ by \((u-v)/r\). Cauchy--Schwarz (or block averaging) therefore gives
\[
\|x-y\|^2\ge \frac{u^2}{a}+\frac{v^2}{b}+\frac{(u-v)^2}{r},
\]
with a term omitted when its block is empty. The constrained quadratic minimum over \(u,v\ge0\), \(u+v\ge1\) occurs at \(u+v=1\), and direct completion of squares yields
\[
\min\|x-y\|^2=\frac{n}{r(a+b)+4ab}
=\frac{n}{n(a+b)-(a-b)^2}.
\]
For \(a,b>0\), the minimizing violation totals are explicitly
\[
u=\frac{a(r+2b)}{r(a+b)+4ab},\qquad
v=\frac{b(r+2a)}{r(a+b)+4ab}.
\]
If \(a=0\), take \((u,v)=(0,1)\); if \(b=0\), take \((1,0)\). To see that the quadratic relaxation is exact rather than merely a bound, take a convex mixture of two uniform vertex classes: vertices with exactly one of the fixed-zero coordinates changed to one, and vertices with exactly one fixed-one coordinate changed to zero. In the first class the remaining \(r\) coordinates have exactly \(j-1\) ones; in the second they have \(j+1\) ones. Both classes exist because \(1\le j\le r-1\). Give these classes total masses \(u\) and \(v\), omitting an empty class. Their averaged point is in \(Q_F\) and attains the displayed bound with the indicated \(x\). Consequently the exact squared face distance is
\[
\boxed{\operatorname{dist}(F,Q_F)^2=\frac{n}{n(a+b)-(a-b)^2}.}
\]

**3. Vertices cannot minimize.** Fix any vertex, with \(k\) ones and \(n-k\) zeros. Every other vertex exchanges at least one one and one zero. Permutation averaging therefore gives a lower bound \(1/k+1/(n-k)\) for the squared distance to the convex hull of the other vertices; averaging all one-exchange neighboring vertices attains it. Hence
\[
\operatorname{dist}(\{v\},Q_{\{v\}})^2=\frac{n}{k(n-k)}.
\]
For \(t=\min\{k,n-k\}\ge2\), the edge orbit with \((a,b)=(n-k-1,k-1)\) has denominator \(4t(n-t)-2n\), and
\[
4t(n-t)-2n-t(n-t)=3t(n-t)-2n>0
\]
for \(n\ge2t\), \(t\ge2\). Thus some nonvertex face always has strictly smaller distance than any vertex.

**4. Sharp maximization and minimizer classification.** It remains to maximize
\[
H_{a,b}=n(a+b)-(a-b)^2
\]
over the integer rectangle \(0\le a\le n-k-1\), \(0\le b\le k-1\), excluding \((0,0)\). By replacing \(k\) by \(n-k\), assume \(k\le n/2\). For any \(b<k-1\),
\[
H_{a,b+1}-H_{a,b}=n+2(a-b)-1\ge n-2k+3>0.
\]
Thus every maximizer has \(b=k-1\). For this fixed value, \(H_{a,k-1}\) is a strictly concave quadratic in \(a\) whose unconstrained maximum lies at \(a=k-1+n/2\). When \(n\le4k\), this point is at or beyond the permitted upper endpoint \(n-k-1\), which is therefore the unique integer maximizer. Substitution yields \(n(n-2)-(n-2k)^2\). When \(n>4k\), the maximizing permitted integers are the nearest one or two integers to \(k-1+n/2\); substitution yields \(\lfloor n^2/4\rfloor+2n(k-1)\). The preceding strict monotonicity and strict concavity give exactly the minimizing-face classes stated in the finding. This completes the proof.

## Verification
The companion `verify.py` uses exact rational arithmetic to check the block-constant face witnesses and sharp integer maximization for 465 rank cases and 50,840 positive-dimensional face orbits, together with 140 explicit small-dimensional mixtures of vertices lying outside each face. Eight additional independent numerical convex-quadratic programs minimize over convex combinations of enumerated vertices (using SciPy) and match the derived exact distances. Running `python verify.py` with Python 3, NumPy and SciPy yields the reported summary. The exact certificates are algebraic identities and exhaustive within the stated finite test domains; they do not replace the proof for arbitrary \(n,k\).

## Relationship to prior work
Deza, Martínez-Rubio, Peña and Wirth (2026) introduce a sharp universal facial-distance-to-diameter inequality and compute the Birkhoff-polytope case. Peña and Wirth (2026) develop general calculus rules, lower bounds for simplex-like \(0/1\)-polytopes, and exact values for simplices, cubes and crosspolytopes. Ferroni and Schröter (2023 preprint; later revision) enumerate hypersimplex faces by their coordinate structure. These results provide the definition, motivation, and face description used here, but none of the inspected statements gives this intermediate-rank exact facial distance or the rank-dependent minimizing-face transition. The known simplex case is excluded from the main theorem. In particular, the bounds for simplex-like polytopes do not imply equality at this exact family-dependent value, and the universal inequality does not determine the minimizing face types.

## Limitations
The principal theorem concerns the standard Euclidean geometry of nontrivial uniform-matroid base polytopes only; arbitrary matroid base polytopes, non-Euclidean norms, and affine distortions are not treated. The eight convex-program tests use finite numerical optimization and are supporting checks, not formal proofs of the infinite classification. Historical priority remains provisional because equivalent calculations could be stated in optimization literature using pyramidal width or another condition-number normalization; a fully comprehensive archival priority review is not claimed. A portion of the cited September 2026 primary source was unavailable in the accessible HTML view; its main theorem and initial proof were read, not all appendices.

## References
1. A. Deza, D. Martínez-Rubio, J. F. Peña, E. Wirth, *Facial distance and diameter*, arXiv:2609.32440v1, first public 2026-09-26. https://arxiv.org/abs/2609.32440
2. J. Peña, E. Wirth, *Calculus of the Facial Distance*, arXiv:2608.28971v1, first public 2026-08-29. https://arxiv.org/abs/2608.28971
3. L. Ferroni, B. Schröter, *Face enumeration for split matroid polytopes*, arXiv:2310.05487, originally published 2023-10-09. https://arxiv.org/abs/2310.05487
4. G. Iommazzo, D. Martínez-Rubio, F. Criado, E. Wirth, *Linear Convergence of the Frank-Wolfe Algorithm over Product Polytopes*, arXiv:2505.11259 (2025). https://arxiv.org/abs/2505.11259
