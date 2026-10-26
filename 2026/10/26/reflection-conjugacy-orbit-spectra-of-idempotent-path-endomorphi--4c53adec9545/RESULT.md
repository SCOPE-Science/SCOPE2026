# Reflection-conjugacy orbit spectra of idempotent path endomorphisms

## Finding

Write \(P_n\) for the simple undirected path on \([n]=\{1,\ldots,n\}\). For each \(n\ge2\), the rank-refined idempotents in \(\operatorname{End}(P_n)\) have a complete, explicit orbit distribution under conjugation by graph automorphisms. Let \(A_k\) be the adjacency matrix of \(P_k\) and set
\[
w_k(t)=\mathbf e_1^{\mathsf T}A_k^t\mathbf1\quad(k\ge2,\ t\ge0).
\]
Thus \(w_k(t)\) counts length-\(t\) nearest-neighbor walks on \([k]\) starting at vertex \(1\), with the endpoint unrestricted. For every \(2\le k\le n\), put \(d=n-k\). Then
\[
I_{n,k}=\sum_{a=0}^{d}w_k(a)w_k(d-a),\qquad
S_{n,k}=\begin{cases}w_k(d/2),&d\text{ even},\\0,&d\text{ odd}.\end{cases}
\]
Here \(I_{n,k}\) is the number of idempotents with image size \(k\), and \(S_{n,k}\) is the number of those invariant under conjugation by the nontrivial path automorphism. The numbers of conjugacy orbits of sizes \(1\) and \(2\) are, respectively, \(S_{n,k}\) and \((I_{n,k}-S_{n,k})/2\). Every rank \(2,\ldots,n\) occurs.

Two finite-matrix resolvents encode the entire fixed-rank deficiency series:
\[
\sum_{d\ge0}I_{k+d,k}z^d
=\left(\mathbf e_1^{\mathsf T}(I-zA_k)^{-1}\mathbf1\right)^2,
\qquad
\sum_{d\ge0}S_{k+d,k}z^d
=\mathbf e_1^{\mathsf T}(I-z^2A_k)^{-1}\mathbf1.
\]
For fixed \(d\ge0\), the values stabilize as soon as \(n>2d\) (with \(n\ge2\)):
\[
I_{n,n-d}=\sum_{a=0}^{d}\binom a{\lfloor a/2\rfloor}\binom{d-a}{\lfloor(d-a)/2\rfloor},
\]
\[
S_{n,n-d}=\begin{cases}0,&d\text{ odd},\\\binom{d/2}{\lfloor d/4\rfloor},&d\text{ even}.\end{cases}
\]

## Assumptions and scope

An ordinary graph endomorphism \(f:[n]\to[n]\) satisfies \(|f(i+1)-f(i)|=1\) for every \(1\le i<n\). It is **not** a weak endomorphism: adjacent vertices never collapse. Rank means the cardinality of the image, not a minimal semigroup generating-set size. Idempotence means \(f\circ f=f\). For \(n\ge2\), the automorphism group has two elements: the identity and reversal \(\rho(i)=n+1-i\). It acts by \(f\mapsto\rho\circ f\circ\rho\). All enumerations are for labeled paths and count actual transformations, not just their kernels.

## Proof

**Step 1: image and fixed interval.** An edge-preserving image of a connected path is a connected vertex set containing at least two vertices, hence an interval \([b,b+k-1]\) of length \(k\ge2\). If \(f^2=f\), every point of its image is fixed: for \(y=f(x)\), \(f(y)=f(f(x))=f(x)=y\). Conversely, an endomorphism that fixes its image is idempotent. Thus every rank-\(k\) idempotent is exactly a retraction onto a unique interval \([b,b+k-1]\).

**Step 2: independent exterior walks.** Fix the image interval and let \(a=b-1\) and \(c=n-(b+k-1)\), so \(a,c\ge0\) and \(a+c=n-k=d\). The values on the image interval are prescribed to be the identity. Reading the domain positions to the left of \(b\) outward, their images make a length-\(a\) nearest-neighbor walk in the target interval, beginning at its left endpoint. Reading to the right outward, they make a length-\(c\) walk from the right endpoint. Reflection of the target interval shows that the latter count is also \(w_k(c)\). The two choices have no additional compatibility constraint and determine the transformation uniquely. Therefore each such interval supports \(w_k(a)w_k(c)\) idempotents. Summing over its \(d+1\) positions gives the asserted \(I_{n,k}\). Positivity follows by alternating between adjacent target vertices on each tail.

**Step 3: fixed maps and orbit sizes.** Suppose \(\rho f\rho=f\). Since conjugation reflects the image interval, that interval must be centered, which is possible exactly when \(d\) is even. The centered interval has two exterior tails of equal length \(d/2\). Choosing the images on the left tail arbitrarily as an endpoint-started walk of that length forces the right-tail images by \(f(n+1-i)=n+1-f(i)\). Conversely this construction gives an invariant idempotent, so exactly \(w_k(d/2)\) occur. The group of order two has orbits of sizes one and two; the formulas follow.

**Step 4: resolvents.** For a fixed image length \(k\), writing \(W_k(z)=\sum_{t\ge0}w_k(t)z^t\), the convolution in Step 2 gives \(\sum_{d\ge0}I_{k+d,k}z^d=W_k(z)^2\). The matrix geometric series \((I-zA_k)^{-1}=\sum_{t\ge0}A_k^tz^t\) holds in integer formal power series and yields the first resolvent. Step 3 similarly gives \(\sum_{d\ge0}S_{k+d,k}z^d=W_k(z^2)\).

**Step 5: fixed-deficiency stabilization.** When \(k>d\), no walk of length \(t\le d\) beginning at target vertex \(1\) can step beyond the far endpoint \(k\): reaching it is possible only on the final step when \(k=d+1\). It is therefore a simple nearest-neighbor walk on the nonnegative half-line starting at zero, confined to nonnegative heights. For any \(t\ge0\), the reflection principle (or the ballot-path identity, summing over all permissible final heights) counts these walks as \(\binom t{\lfloor t/2\rfloor}\). Under \(n>2d\), one has \(k=n-d>d\). Substitution into the previous two formulas gives the stabilized expressions, including the parity boundary. This completes the proof.

## Verification

The standalone source `path_check.py` independently generates every nearest-neighbor self-map of the labeled path, tests idempotence by direct composition, computes its rank and its conjugate under reversal, and forms actual two-element orbits. It then compares these census data with the matrix-walk convolution formulas for all \(2\le n\le14\). This exhaustive test covers \(5515\) idempotents and independently checks stable-deficiency instances with \(0\le d\le10\). Run `python3 path_check.py`; the exact stdout is supplied as `path_check.out`. These computations verify only the stated finite cases, not the universal theorem; the proof above is independent of exhaustive enumeration.

## Relationship to prior work

Dimitrova–Fernandes–Koppitz–Quinteiro (first public arXiv version 22 October 2018) establish the structural theory and minimal generating ranks of \(\operatorname{End}(P_n)\) and weak variants. Their Proposition 1.1 provides the edge-preservation walk criterion, while their principal theorems concern monoid generating rank, regularity, and cardinalities, not the joint idempotent-image-rank and automorphism-conjugacy orbit distribution. The proof here uses the criterion but counts a different semigroup invariant.

The Lin–Zeng work on endomorphism-induced path congruences counts kernels, not idempotent retractions classified by images and conjugation. Eggleton–Morayne count graph homomorphisms between paths, supporting the classical bounded-walk ingredient; their advertised invariant is total homomorphism count, not this retraction orbit spectrum. The complete-rank and orbit formulas here are not claimed to be new general walk-counting identities. Similar published results for cycle endomorphism monoids use the different cyclic topology, where the two outside tails are joined and cannot be chosen independently.

## Limitations

No result is asserted for weak endomorphisms, partial endomorphisms, paths with loops, or other graphs. Only conjugation by graph automorphisms is classified, not larger equivalences such as Green relations. A past specialist article by Michels and Knauer on congruence classes of paths and cycles was available only as an abstract; the possibility of an implicit idempotent count or symmetry refinement in its inaccessible full text remains a priority risk. The formulas are proved algebraically; finite tests cannot establish originality or correctness in all sizes. No independent mathematical audit has been performed.

## References

1. I. Dimitrova, V. H. Fernandes, J. Koppitz, T. M. Quinteiro, *Ranks of monoids of endomorphisms of a finite undirected path*, arXiv:1810.09307v1 (22 October 2018); DOI: 10.1007/s40840-019-00762-4.
2. Z. Lin and J. Zeng, *On the number of congruence classes of paths*, arXiv:1112.4026v1 (2011).
3. R. B. Eggleton and M. Morayne, *A Note on Counting Homomorphisms of Paths*, Graphs and Combinatorics 30 (2014), 159–170, DOI: 10.1007/s00373-012-1261-0 (first online 24 November 2012).
4. M. A. Michels and U. Knauer, *The congruence classes of paths and cycles*, Discrete Mathematics 309 (2009), 5352–5359, DOI: 10.1016/j.disc.2008.11.022 (abstract inspected; full text unavailable).
