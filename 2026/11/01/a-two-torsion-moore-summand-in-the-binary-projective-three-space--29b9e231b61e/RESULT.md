# A two-torsion Moore summand in the binary projective three-space cap complex

## Finding
Let \(K=C_p(3,2)\) denote the simplicial complex of all subsets of the fifteen points of the binary projective space \(\operatorname{PG}(3,2)\) that contain no complete projective line. There is an integral homotopy equivalence
\[
K\simeq M(\mathbb Z/2,3)\vee\bigvee^{77}S^4,
\]
where \(M(\mathbb Z/2,3)=S^3\cup_2 e^4\) is the Moore space obtained by a degree-two attaching map. In particular,
\[
\widetilde H_3(K;\mathbb Z)\cong\mathbb Z/2,\qquad
\widetilde H_4(K;\mathbb Z)\cong\mathbb Z^{77},
\]
and all other reduced integral homology groups vanish.

## Assumptions and scope
Identify the fifteen points of \(\operatorname{PG}(3,2)\) with the nonzero vectors \(1,\ldots,15\in\mathbb F_2^4\), encoded by their four binary digits. The thirty-five lines are the unordered triples \(\{a,b,a\oplus b\}\) with distinct nonzero \(a,b\), where \(\oplus\) is coordinatewise addition modulo two. A set is a face of \(K\) if and only if it does not contain any such line. The empty face is included conventionally but the verification program enumerates nonempty faces. All statements concern this ordinary unaugmented geometric realization; no equivariance assertion is made.

The nonempty face vector, indexed by dimensions zero through seven, is
\[
(15,105,420,945,1008,420,120,15),
\]
for a total of \(3048\) nonempty faces. Every face is encoded by a fifteen-bit positive integer, with point \(i\) corresponding to bit \(i-1\).

## Proof
**1. Exhaustive face generation.** For each integer mask from \(1\) through \(2^{15}-1\), test whether it contains any of the \(35\) distinct line masks; retain exactly those that contain none. This gives the displayed face vector. The attached standalone verifier implements this definition from scratch, without using a face list embedded in the certificate.

**2. Certified acyclic matching.** In `morse_certificate.json`, the `pairs` field lists \(1484\) distinct lower–upper mask pairs \((\sigma,\tau)\); every upper face has exactly one extra point. The `critical` field lists the remaining \(80\) nonempty faces. The verifier checks that the pairs and critical faces partition all \(3048\) nonempty faces, with no repeated member. Precisely one critical face has dimension zero, one has dimension three, and \(78\) have dimension four. No other critical faces remain.

Orient every unmatched Hasse edge of the face poset from the higher-dimensional face to its codimension-one face; reverse the \(1484\) matched edges. The resulting directed graph has \(3048\) vertices and \(13770\) arrows. Exhaustive topological sorting visits all \(3048\) vertices, proving acyclicity. Thus Forman's discrete Morse construction gives a CW complex homotopy equivalent to \(K\) with one cell each in dimensions zero and three, plus \(78\) cells in dimension four, and no other cells. In particular its three-skeleton is \(S^3\).

**3. Signed attaching degrees.** Use increasing point order to orient every simplex. If \(\tau\) is a matched upper four-face and \(\sigma\) its matched lower three-face, the incidence coefficient \([\tau:\sigma]\) is \(\pm1\). Define the coefficient \(P(\sigma)\) of the unique critical three-face in the algebraic Morse reduction recursively as follows. It is one on that critical face, zero on any other critical three-face, and zero on a three-face matched as an upper face. When \(\sigma\) is matched as a lower face to \(\tau\), let
\[
P(\sigma)=-[\tau:\sigma]\sum_{\substack{\rho<\tau\\\rho\ne\sigma}}[\tau:\rho]P(\rho).
\]
The directed-acyclicity certificate guarantees that these gradient-path recursions terminate. Each critical four-face \(\omega\) has integer Morse boundary coefficient
\[
d(\omega)=\sum_{\sigma<\omega}[\omega:\sigma]P(\sigma).
\]
Exact evaluation over all \(78\) critical four-faces yields the signed coefficient histogram
\[
-4:3,\quad -2:18,\quad 0:32,\quad 2:20,\quad 4:4,\quad 6:1.
\]
In particular, the greatest common divisor of the \(78\) integer attaching degrees is exactly \(2\). The executable verifier reproduces all coefficients from the full certificate rather than assuming the histogram.

**4. Identification of the homotopy type.** Because the Morse three-skeleton is \(S^3\), each attaching map of a four-cell represents an integer in \(\pi_3(S^3)\cong\mathbb Z\), exactly its Morse boundary degree. Smith reduction of the one-by-seventy-eight degree row, using a self-homotopy equivalence of the wedge of attaching spheres, changes that row to \((2,0,\ldots,0)\). Its mapping cone is \(M(\mathbb Z/2,3)\vee\bigvee^{77}S^4\), proving the claimed homotopy equivalence. The integral homology follows from this CW model; no inference from finite mod-prime experiments is needed.

## Verification
Run `python3 verify_cap.py` in the same directory as `morse_certificate.json`, using Python 3's standard library. It checks complete face enumeration, pair/critical partition, every matched face incidence, the entire oriented Hasse graph, its acyclicity, and the full signed Morse differential; successful execution ends `VERIFY_OK`. The recorded complete output is in `verification_output.txt`.

Independently run `python3 verify_modular.py`, which uses no matching certificate. Exact boundary-matrix ranks over \(\mathbb F_2\), \(\mathbb F_3\), and \(\mathbb F_5\) agree with the predicted integral homology: mod-two reduced Betti numbers are \(1\) in degree three and \(78\) in degree four; for the odd fields only degree four has rank \(77\). Successful execution ends `MODULAR_VERIFY_OK`, with output in `modular_output.txt`. Modular agreement is a cross-check, not a substitute for the signed integral Morse calculation.

## Relationship to prior work
Forbes, Grannell and Griggs (2004) introduced and enumerated independent point sets in Steiner triple systems. The projective incidence lines here form a Steiner triple system of order fifteen, so their set-enumeration theory is directly related, but the inspected paper establishes no integral homotopy or torsion decomposition for this complex.

Lew (2017), Section 6.2, specifically introduced cap simplicial complexes \(C_p(n,q)\) and tabulated several examples including \(C_p(2,2)\), \(C_p(2,3)\), and \(C_p(3,3)\). Those are different spaces; the inspected section does not compute \(C_p(3,2)\). In particular, the known three-primary torsion of the ternary projective-plane cap complex does not imply the binary three-space's two-primary Moore summand. The result concerns the cap complex, not a neighborhood, incidence, matching, or independence complex of another graph.

## Limitations
The claim is restricted to the single fifteen-point binary projective three-space cap complex. The provided finite certificate proves a homotopy classification for this specified object, not a general theorem for all finite projective spaces. No complete automorphism-group action on integral homology, minimal Morse matching, or equivariant splitting is asserted. A mathematically equivalent unindexed prior computation is not excluded by the available literature searches. Independent mathematical auditing has not been performed.

## References
1. A. D. Forbes, M. J. Grannell and T. S. Griggs, *Independent Sets in Steiner Triple Systems*, Ars Combinatoria **72** (2004), 161–169. Public article and date record: https://combinatorialpress.com/ars-articles/volume-072-ars-articles/independent-sets-in-steiner-triple-systems/ (31 July 2004).
2. Alan Lew, *Spectral Gaps of Generalized Flag Complexes*, MSc thesis, Technion, December 2017, Section 6.2, pp. 61–65. https://www.math.cmu.edu/~alanlew/files/theses/msc%20thesis.pdf.
3. Robin Forman, *Morse Theory for Cell Complexes*, Advances in Mathematics **134** (1998), 90–145. Background for acyclic matchings and Morse CW models.
