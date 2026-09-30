# Smallest failure of surjectivity in the divisor embedding for finite-line congruences
## Finding
Let \(L_n\) be the reflexive finite line frame on \(\{0,\ldots,n\}\), with \(xRy\) exactly when \(|x-y|\le 1\). For a proper congruence \(\rho\) of \(L_n\), Areces--Campercholi--Penazzi--Sánchez Terraf define its frequency \(f_\rho\) and prove that
\[
\theta\longmapsto f_\theta
\]
is a lattice embedding of the principal ideal \((\rho]=\{\theta:\theta\subseteq\rho\}\) into the divisor lattice of \(f_\rho\).

This embedding need not be surjective. The smallest line on which surjectivity can fail is \(L_5\), the six-vertex line. Moreover, on \(L_5\) there are exactly two failures. In the folding notation of the source they are
\[
\rho_1=\langle 1;1\rangle,\qquad \rho_3=\langle 1;3\rangle.
\]
Both have frequency \(4\), but
\[
(\rho_1]=(\{\operatorname{Id},\rho_1\}),\qquad
(\rho_3]=(\{\operatorname{Id},\rho_3\}),
\]
so their frequency images are \(\{1,4\}\), omitting the divisor \(2\). Every proper congruence of every \(L_n\) with \(0\le n\le4\) has a surjective frequency embedding, and every other proper congruence of \(L_5\) does as well.

Thus the divisor embedding theorem is sharp already on six vertices: it cannot in general be strengthened from “lattice embedding” to “isomorphism onto the full divisor lattice.”
## Assumptions and scope
A congruence means a bisimulation equivalence of the reflexive line frame. “Proper” means different from the universal relation. The notation \(\langle k;\bar r\rangle\) is the source notation: \(k\) is the step and \(\bar r\) lists the rests. For such a congruence on \(L_n\),
\[
f=\frac{n-|\bar r|}{k}.
\]
The claim concerns only the surjectivity of the source's frequency embedding on principal ideals and the minimal line on which it fails.
## Proof
The source's classification theorem says that every proper nonidentity congruence of \(L_n\) is a folding \(\langle k;\bar r\rangle\) satisfying its divisibility and spacing conditions. Applying those conditions for \(n\le5\) gives the following complete lists of proper nonidentity congruences, together with their frequencies:

- \(L_0,L_1\): none.
- \(L_2\): \(\langle1\rangle\) with frequency \(2\).
- \(L_3\): \(\langle1\rangle\) with frequency \(3\), and \(\langle1;1\rangle\) with frequency \(2\).
- \(L_4\): \(\langle1\rangle\) with frequency \(4\), \(\langle1;1\rangle\) and \(\langle1;2\rangle\) with frequency \(3\), and \(\langle2\rangle\) with frequency \(2\).
- \(L_5\): \(\langle1\rangle\) with frequency \(5\); \(\langle1;1\rangle,\langle1;2\rangle,\langle1;3\rangle\) with frequency \(4\); \(\langle1;1,3\rangle\) with frequency \(3\); and \(\langle2;2\rangle\) with frequency \(2\).

The frequency embedding is injective and its image is a sublattice of the divisor lattice. Therefore a congruence of prime frequency automatically has a surjective image. For \(L_4\), the only composite frequency is \(4\), and
\[
\langle2\rangle\subseteq\langle1\rangle,
\]
so frequencies \(1,2,4\) all occur below \(\langle1\rangle\). Hence surjectivity holds for every proper congruence through \(L_4\).

On \(L_5\), the unique frequency-\(2\) congruence is
\[
\sigma=\langle2;2\rangle,
\]
whose blocks are \(\{0,5\},\{1,4\},\{2,3\}\). The central-rest frequency-\(4\) congruence \(\langle1;2\rangle\) has blocks \(\{0,2,3,5\},\{1,4\}\), so \(\sigma\subseteq\langle1;2\rangle\) and its divisor image is \(\{1,2,4\}\).

For the two side-rest congruences,
\[
\rho_1:\ \{0,3,5\}\mid\{1,2,4\},
\qquad
\rho_3:\ \{0,2,5\}\mid\{1,3,4\}.
\]
The relation \(\sigma\) identifies \(2\) with \(3\), while each \(\rho_i\) separates \(2\) from \(3\). Hence \(\sigma\nsubseteq\rho_1\) and \(\sigma\nsubseteq\rho_3\). Since \(\sigma\) is the unique frequency-\(2\) congruence of \(L_5\), and the frequency map is injective on each principal ideal, no intermediate congruence can have frequency \(2\). The only possible divisor frequencies below either \(\rho_i\) are therefore \(1\) and \(4\), proving
\[
(\rho_i]=\{\operatorname{Id},\rho_i\}\quad(i\in\{1,3\}).
\]
This also shows that these are exactly the two failures on \(L_5\). Reversal of the line exchanges them.
## Verification
The accompanying verifier independently enumerates every set partition of the vertex sets of \(L_0,\ldots,L_5\), tests the bisimulation-equivalence condition directly from the reflexive adjacency relation, computes refinement and frequency from the resulting partitions, and compares each principal-ideal frequency image with the full divisor set. It confirms surjectivity for all proper congruences through \(L_4\), identifies exactly the two stated defects on \(L_5\), checks that the unique frequency-\(2\) congruence is \(\langle2;2\rangle\), and terminates with `VERIFY_OK`.
## Relationship to prior work
Areces, Campercholi, Penazzi, and Sánchez Terraf classify all congruences of finite line frames and prove that, below any proper congruence \(\rho\), frequency gives a lattice embedding into the positive divisors of \(f_\rho\). Their theorem is stated as an embedding, not as a surjectivity or isomorphism result. The present finding determines the first point where surjectivity actually fails and classifies all failures at that smallest size.

Targeted searches for the exact six-vertex obstruction, for surjectivity of the frequency embedding, and for a smallest counterexample found the original finite-line-frame paper but no source stating this sharpness result or a stronger equivalent.
## Limitations
The minimality statement is only with respect to the number of vertices in finite reflexive line frames. It does not classify all larger lines whose principal ideals have nonsurjective frequency images, nor does it give a general criterion for surjectivity. Originality is best-of-knowledge after targeted searches and is not a proof that no inaccessible or differently phrased source contains the same observation. Independent audit, formal proof-assistant verification, and expert attestation have not been performed.
## References
1. C. Areces, M. Campercholi, D. Penazzi, and P. Sánchez Terraf, “The Lattice of Congruences of a Finite Line Frame,” arXiv:1504.01789v1, first public version 2015-04-08. See especially the complete folding classification and the frequency embedding theorem.
2. C. Areces, M. Campercholi, D. Penazzi, and P. Sánchez Terraf, “The lattice of congruences of a finite line frame,” Journal of Logic and Computation 27(8), 2653–2688, doi:10.1093/logcom/exx026.
