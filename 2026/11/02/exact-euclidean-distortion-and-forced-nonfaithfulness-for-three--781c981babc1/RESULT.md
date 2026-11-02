# Exact Euclidean distortion and forced nonfaithfulness for three-subset Kneser graphs

## Finding
For each integer \(n\ge 8\), give the three-subset Kneser graph \(KG(n,3)\) its unweighted shortest-path metric. Its exact least distortion in any real Hilbert space is
\[
 c_2(KG(n,3))=\begin{cases}
 \sqrt{3}, & n=8,\\
 2\sqrt{1-\binom{n-4}{2}^{-1}}, & n\ge 9.
 \end{cases}
\]
There is an exceptional rigidity transition. For \(n=8\), no optimally distorted embedding is *faithful*: even though triples intersecting in one or two elements both have graph distance \(2\), their Euclidean distances cannot be equal in any optimal embedding. An optimal, permutation-invariant squared-distance pattern, indexed by intersection sizes \(0,1,2\), is \((3,5,4)\). For \(n=9\), both faithful and nonfaithful optimal patterns occur, namely \((18/5,4,4)\) and \((18/5,5,4)\). For every \(n\ge10\), all optimally normalized embeddings are faithful, with Euclidean squared distances \(4(1-\binom{n-4}{2}^{-1})\) for disjoint triples and \(4\) for all other distinct triples. Thus their pairwise distances, and hence their Euclidean configurations up to congruence, are uniquely determined for \(n\ge10\).

## Assumptions and scope
Vertices are the \(\binom n3\) three-element subsets of \([n]\); distinct vertices are adjacent if and only if disjoint. All edges have length \(1\). For a map \(f\) into a real Hilbert space, distortion at most \(C\ge1\) means that some \(s>0\) satisfies \(s d(S,T)\le\|f(S)-f(T)\|\le Cs d(S,T)\) for every distinct pair. We rescale to \(s=1\), called *noncontracting normalization*. A map is *faithful* when the Euclidean distance depends only on the graph distance, not the particular vertices.

For \(n\ge8\), disjoint triples have graph distance \(1\). Every other distinct pair intersects in one or two labels, so its union contains at most five labels; since at least three remain, a triple disjoint from both gives a path of length two. These pairs have graph distance exactly \(2\). No conclusion is claimed for smaller \(n\), weighted graphs, or fixed-dimensional target spaces.

## Proof
**1. Invariant squared-distance matrices.** Fix \(n\ge8\), and abbreviate \(N=\binom n3\). For every Hilbert embedding \(f\) rescaled noncontractingly, its squared-distance matrix \(D\) is conditionally negative semidefinite: for every vector \(z\in\mathbb R^N\) with \(\sum z_S=0\), one has \(z^TDz\le0\). Equivalently, its centered Gram matrix \(-HDH/2\) is positive semidefinite, where \(H=I-\mathbf1\mathbf1^T/N\). Conversely, every real symmetric hollow matrix with that positivity is a squared Euclidean distance matrix: factor its centered Gram matrix and use the zero diagonal to recover all pairwise squared distances. Average the squared-distance matrices over every permutation of \([n]\). The averaged matrix is again a squared Euclidean distance matrix and satisfies the same distortion bounds. It takes a constant value \(x_s\) on every unordered pair of distinct triples with intersection size \(s\in\{0,1,2\}\), and consequently
\[
 1\le x_0\le C^2, \qquad
 4\le x_1,x_2\le4C^2. \tag{1}
\]
This averaging is applied to *squared distances*, rather than to embedding maps, and does not assume that the original embedding is faithful.

**2. Complete eigenvalue test.** Let \(A_i\) be the symmetric zero-diagonal matrix indexed by triples with \((A_i)_{S,T}=1\) precisely when \(|S\cap T|=3-i\), for \(i=1,2,3\). Thus \(D=x_0A_3+x_1A_2+x_2A_1\). For \(j\in\{0,1,2,3\}\), put
\[
 U_j=\operatorname{span}\{u_T: T\subseteq[n],\ |T|=j\},
 \quad u_T(S)=\mathbf1_{T\subseteq S},\quad
 W_j=U_j\cap U_{j-1}^{\perp},\quad U_{-1}=\{0\}.
\]
The incidence spaces are nested, \(U_3=\mathbb R^N\), and hence \(\mathbb R^N=W_0\oplus W_1\oplus W_2\oplus W_3\) with \(W_0\) the constants. Each \(A_i\) preserves every \(U_j\), since \((A_i u_T)(S)\) depends only on \(\ell=|S\cap T|\), and the functions \(\binom\ell t\) with \(t\le j\) are linear combinations of incidence indicators of subsets of \(T\). Symmetry then makes each \(W_j\) invariant. Its scalar eigenvalue is the coefficient of \(\binom\ell j\) in the binomial-basis expansion of \((A_i u_T)(S)\), namely
\[
 P_j(i)=\sum_{\ell=0}^{j}(-1)^{j-\ell}\binom j\ell
 \binom{3-\ell}{3-i-\ell}\binom{n-3-j+\ell}{i-j+\ell},\tag{2}
\]
with out-of-range binomial coefficients understood as zero. Formula (2) follows by counting triples \(R\) with \(|R\cap S|=3-i\) and \(T\subseteq R\), then taking the \(j\)-th finite difference in \(\ell\). Direct simplification gives the following eigenvalues on \(W_1,W_2,W_3\), with columns corresponding in order to \(A_3,A_2,A_1\):
\[
\begin{array}{c|ccc}
  & A_3 & A_2 & A_1\\ \hline
 W_1 & -L & (n-4)(n-9)/2 & 2n-9\\
 W_2 & n-5 & 11-2n & n-7\\
 W_3 & -1 & 3 & -3
\end{array},\qquad L=\binom{n-4}{2}.\tag{3}
\]
The usual Euclidean-distance criterion is therefore equivalent to all three scalar row products with \((x_0,x_1,x_2)\) being nonpositive. This is both a necessary and a sufficient test, because all nonconstant eigenspaces of \(D\) appear in (3).

**3. Exact distortion for \(n\ge9\).** The first row of (3) gives
\[
 Lx_0\ge \frac{(n-4)(n-9)}2x_1+(2n-9)x_2
 \ge4\left(\frac{(n-4)(n-9)}2+2n-9\right)=4(L-1).
\]
Here both coefficients are nonnegative; for \(n=9\) the first is zero. With (1) this yields \(C^2\ge4(1-L^{-1})\). Conversely choose
\[
 (x_0,x_1,x_2)=(4(1-L^{-1}),4,4).
\]
The first scalar product in (3) is zero, the second equals \(-4-4(n-5)/L<0\), and the third equals \(-x_0<0\). Hence this pattern is a genuine Euclidean squared-distance matrix. It respects (1) with \(C^2=4(1-L^{-1})\), proving sharpness.

**4. The exceptional case \(n=8\).** The \(W_1\) and \(W_3\) tests respectively read \(-6x_0-2x_1+7x_2\le0\) and \(-x_0+3x_1-3x_2\le0\). Three times the first plus twice the second eliminates \(x_1\), giving \(-20x_0+15x_2\le0\). Thus \(x_0\ge3x_2/4\ge3\), so \(C^2\ge3\). For \((x_0,x_1,x_2)=(3,5,4)\), the three scalar products in (3) equal \((0,-12,0)\), and (1) holds with \(C^2=3\). The squared Euclidean embedding exists and the lower bound is sharp.

**5. Optimal-embedding rigidity.** Let \(f\) be *any* optimal embedding, scaled noncontractingly, and average its squared distances as in step 1. At \(n=8\), the equality chain \(3\ge x_0\ge3x_2/4\ge3\) forces \(x_0=3\) and \(x_2=4\). As these are respectively the upper and lower pointwise bounds for their orbit types, *every* original disjoint pair has squared Euclidean distance \(3\), and every original pair intersecting in two elements has squared distance \(4\). The equality equations in the \(W_1\) and \(W_3\) inequalities then force the *averaged* squared distance for intersection-one pairs to be \(x_1=5\). Hence the embedding cannot be faithful: graph-distance-two pairs have two incompatible orbit averages. For \(n=9\), both \((18/5,4,4)\) and \((18/5,5,4)\) satisfy (1) and all three nonpositivity tests in (3), with the same optimal distortion, establishing simultaneous existence of faithful and nonfaithful optima. For \(n\ge10\), both positive coefficients on \(x_1,x_2\) in the first eigenvalue inequality force the averaged orbit values \(x_1=x_2=4\), while \(x_0=C^2\) is forced by the sharp lower bound. Every original pair then attains the same orbit bound, so these precise squared distances hold pointwise. A centered Euclidean Gram matrix is uniquely determined by its complete pair distances, proving congruence up to an ambient isometry. \(\square\)

## Verification
The accompanying `verify_kneser.py` uses only standard-library exact integer and rational arithmetic. Run it with `python3 verify_kneser.py`. It checks the finite-difference eigenvalues (2) against (3) for every integer \(8\le n\le60\), verifies all positivity and normalization inequalities for the proposed patterns, checks two distinct optimal patterns at \(n=9\), and constructs the full centered Gram matrices for \(n=8,9,10\), verifying positive semidefiniteness by exact rational congruence elimination. It also checks graph distances for every vertex pair in those cases. The analytic arguments in steps 1–5, not these finitely many calculations, establish the result for all \(n\ge8\).

## Relationship to prior work
Robertson, *Negative Type and Bi-lipschitz Embeddings into Hilbert Space* (2023), establishes a general semidefinite characterization of finite Hilbert distortion and supplies explicit bipartite-graph and Hamming-cube examples, but does not give the present exact constants or the \(KG(8,3)\) nonfaithfulness phenomenon. Vallentin, *Optimal Distortion Embeddings of Distance Regular Graphs into Euclidean Spaces* (first preprint 2005), derives sharp results for distance-regular Johnson graphs, Hamming graphs and all strongly regular graphs. Cioabă, Gupta, Ihringer and Kurihara, *The Least Euclidean Distortion Constant of a Distance-Regular Graph* (first preprint 2021), revisit those distance-regular results and focus on faithful embeddings. These known formulas cannot be invoked for \(KG(n,3)\), \(n\ge8\): pairs of nonadjacent vertices intersecting in one and two labels have respectively \(\binom{n-5}{3}\) and \(\binom{n-4}{3}\) common neighbors, so this diameter-two graph is not strongly regular or distance regular. The analogous two-subset Kneser family *is* strongly regular and is not a new claim here. The present proof instead resolves a three-orbit Euclidean embedding problem and captures optimal nonfaithfulness at the smallest admissible parameter.

## Limitations
The theorem gives unrestricted real-Hilbert distortion, not the minimum target dimension or all coordinate realizations. For \(n=8\), it fixes two pointwise orbit classes and an average in the third; it does not classify every noninvariant optimal embedding. Earlier equivalent results under alternative association-scheme or metric-embedding terminology remain a historical priority risk despite targeted comparisons. The rigidity classification concerns distances after noncontracting normalization, not uniqueness of the embedding map before Euclidean congruence. This is not an independently audited result.

## References
- G. Robertson, *Negative Type and Bi-lipschitz Embeddings into Hilbert Space*, arXiv:2309.16070v1 (first submitted 2023-09-27), https://arxiv.org/html/2309.16070v1.
- F. Vallentin, *Optimal Distortion Embeddings of Distance Regular Graphs into Euclidean Spaces*, arXiv:math/0509716 (first submitted 2005-09-30), https://arxiv.org/abs/math/0509716.
- S. M. Cioabă, H. Gupta, F. Ihringer and H. Kurihara, *The Least Euclidean Distortion Constant of a Distance-Regular Graph*, arXiv:2109.09708 (first submitted 2021-09-20), https://arxiv.org/abs/2109.09708.
- I. J. Schoenberg, *Remarks to Maurice Fréchet's article...*, Annals of Mathematics **36** (1935), 724–732 (finite squared-Euclidean distance criterion).
