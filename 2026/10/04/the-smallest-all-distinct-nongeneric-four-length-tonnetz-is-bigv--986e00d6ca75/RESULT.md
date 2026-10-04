# The smallest all-distinct nongeneric four-length Tonnetz is \(\bigvee^{6} S^{2}\vee\bigvee^{2} S^{3}\)
## Finding
For the generalized Tonnetz \(T=\mathrm{Tonn}^{10,4}(1,2,3,4)\) of Jevtić--Živaljević, \(T\simeq \bigvee^{6} S^{2}\vee\bigvee^{2} S^{3}\). Hence even for the smallest possible four-entry positive length vector with pairwise distinct entries, reducedness plus pairwise distinctness does not replace the subset-sum genericity hypothesis used in the generic torus theorem.

## Assumptions and scope
Let \(L=(1,2,3,4)\), let \(n=\sum_i l_i=10\), and let \(T=\mathrm{Tonn}^{10,4}(L)\) be the simplicial complex of Jevtić--Živaljević: for each \(x\in\mathbb Z_{10}\) and permutation \(\sigma\in\Sigma_4\), a maximal-simplex candidate is the four-element set of successive partial sums
\[
\Delta(x;\sigma)=\{x,\ x+l_{\sigma(1)},\ x+l_{\sigma(1)}+l_{\sigma(2)},\ x+l_{\sigma(1)}+l_{\sigma(2)}+l_{\sigma(3)}\}\pmod{10}.
\]
The vector is reduced because \(\gcd(1,2,3,4)=1\), and its four entries are pairwise distinct. It is not generic in the source's subset-sum sense because \(1+2=3\). The sum \(10\) is minimal among four pairwise-distinct positive integers, and the multiset \(\{1,2,3,4\}\) is the unique multiset attaining that minimum.

## Proof
Direct reconstruction from the definition gives exactly \(60\) distinct tetrahedral facets and face vector
\[
(f_0,f_1,f_2,f_3)=(10,45,100,60),
\]
so \(T\) has \(215\) nonempty faces. On the face poset, process the vertices in the order \((9,3,6,7,0,4,5,1,2,8)\). At each stage, pair every still-unmatched face \(F\) not containing the current vertex \(v\) with \(F\cup\{v\}\) whenever that coface is still unmatched. This produces \(103\) pairs. Reversing precisely the matched Hasse covers and orienting all unmatched covers downward gives an acyclic directed graph on all \(215\) faces; the check uses all \(630\) Hasse covers.

The unmatched faces are one vertex, six triangles, and two tetrahedra, with no critical edges. Explicitly, they are
\[
\{9\},
\]
\[
\{0,3,6\},\ \{1,3,4\},\ \{2,3,6\},\ \{2,4,7\},\ \{3,4,8\},\ \{4,5,7\},
\]
and
\[
\{1,2,4,8\},\ \{2,4,5,8\}.
\]
Discrete Morse theory therefore gives a CW complex homotopy equivalent to \(T\) with one \(0\)-cell, six \(2\)-cells, two \(3\)-cells, and no \(1\)-cells.

Independently, exact rational elimination on the simplicial boundary matrices gives
\[
\operatorname{rank}(\partial_1)=9,\qquad \operatorname{rank}(\partial_2)=36,\qquad \operatorname{rank}(\partial_3)=58,
\]
so the rational Betti vector is \((1,0,6,2)\). In the Morse CW complex, \(C_3\) has rank \(2\) and \(H_3(-;\mathbb Q)\) has dimension \(2\); hence the cellular boundary \(C_3\to C_2\) has rank zero over \(\mathbb Q\), and therefore is the zero integral homomorphism. The \(2\)-skeleton is \(\bigvee^6 S^2\). Since it is simply connected, the Hurewicz map \(\pi_2\to H_2\) is an isomorphism. Thus each \(3\)-cell attaching map, whose cellular homology class is zero, is null-homotopic. Attaching the two \(3\)-cells therefore wedges on two \(3\)-spheres, proving
\[
T\simeq \bigvee^6 S^2\vee\bigvee^2 S^3.
\]

## Verification
The standalone verifier `verify_tonn_10_4_1234.py` reconstructs the facets from the defining partial-sum formula rather than from a stored face list. It checks reducedness, pairwise distinctness, the explicit nongeneric relation \(1+2=3\), the full face vector, all Morse pairs, the full set of critical cells, acyclicity on all \(630\) Hasse covers, and exact rational boundary ranks. A successful replay prints `VERIFY_OK` after reporting \(60\) facets, \(215\) nonempty faces, \(103\) Morse pairs, critical counts \((1,0,6,2)\), boundary ranks \((9,36,58)\), and Betti vector \((1,0,6,2)\).

## Relationship to prior work
Jevtić and Živaljević define \(\mathrm{Tonn}^{n,k}(L)\) and prove that a generic reduced length vector yields a \((k-1)\)-torus; they explicitly emphasize that genericity is essential to their manifold argument and cite the non-generic \(k=3\) classification as the relevant lower-dimensional boundary literature. Their paper does not state this \(k=4\), \(L=(1,2,3,4)\) homotopy type. Michael J. Catanzaro's *Generalized Tonnetze* classifies arbitrary triadic, hence \(2\)-dimensional, Tonnetz-type complexes and therefore does not imply the present tetrahedral case. Jason Yust studies three-dimensional musical Tonnetze constructed from networks of multiple tetrachord types in Fourier phase spaces; the inspected construction and tables are not the Jevtić--Živaljević complex \(\mathrm{Tonn}^{10,4}(1,2,3,4)\), and no equivalent statement was located in the inspected text.

The point of the example is not merely that nongeneric vectors can behave differently: \((1,2,3,4)\) is the unique smallest all-distinct positive four-length multiset, yet its subset-sum collision changes the generic \(3\)-torus conclusion to a simply connected mixed-dimensional wedge of spheres.

## Limitations
This result concerns one exact finite generalized Tonnetz and does not classify nongeneric four-length vectors. It does not claim that every musical construction called a three-dimensional Tonnetz is equivalent to the Jevtić--Živaljević definition. The literature comparison was targeted at the defining paper, the known arbitrary-triad classification, and a prominent three-dimensional tetrachord construction; obscure or differently indexed computations may still exist. The homotopy conclusion uses the verified finite complex and discrete-Morse certificate; it is not extrapolated to an infinite family.

## References
1. F. D. Jevtić and R. T. Živaljević, *Generalized Tonnetz and discrete Abel-Jacobi map*, arXiv:2002.09184 (first public version 2020-02-21); Topological Methods in Nonlinear Analysis, DOI 10.12775/TMNA.2020.049.
2. M. J. Catanzaro, *Generalized Tonnetze*, arXiv:1612.03519.
3. J. Yust, *Geometric Generalizations of the Tonnetz and their Relation to Fourier Phase Spaces*, in *Mathematical Music Theory*, DOI 10.1142/9789813235311_0013.
