# Isomorphism and automorphism spectra of maximal one-nodal curves with elliptic normalization

## Finding
Let \(p\geq 5\) be a prime, put \(k=\mathbb F_{p^2}\) and \(n=p-1\), and fix a maximal elliptic curve \(E/k\), meaning \(\#E(k)=(p+1)^2\). Consider **unpointed \(k\)-isomorphism classes** of geometrically integral, projective curves \(C/k\) of geometric genus one and arithmetic genus two, with normalization \(k\)-isomorphic to \(E\), attaining the Aubry--Perret bound \(\#C(k)=p^2+2p+2\). Let \(m=\#\operatorname{Aut}_{\bar k}(E,O)\). Then \(m\in\{2,4,6\}\), and the complete class and automorphism-order census is as follows:

| \(m\) | Number of classes | \(\#\operatorname{Aut}_k(C)=2\) | Order \(4\) | Order \(8\) |
|---|---:|---:|---:|---:|
| \(2\) | \((n^2+2)/2\) | \((n^2-4)/2\) | \(3\) | \(0\) |
| \(4\) | \((n^2+4)/4\) | \((n^2-4)/4\) | \(1\) | \(1\) |
| \(6\) | \((n^2+2)/6\) | \((n^2-4)/6\) | \(1\) | \(0\) |

In particular, the numbers depend only on \(p\) and on the origin-fixing geometric automorphism order \(m\), not on a particular maximal elliptic model. Here \(m=4\) is possible only for \(j(E)=1728\) and \(p\equiv3\pmod4\); \(m=6\) only for \(j(E)=0\) and \(p\equiv2\pmod3\). The table classifies every curve with the stated normalization and invariants, not merely those obtained from a chosen plane equation or projection.

## Assumptions and scope
All isomorphisms and automorphisms in the table are defined over \(k\). The origin \(O\) is used on the normalization only to calculate automorphism orbits; neither \(C\) nor its normalization is required to carry a marked point. A singularity called a nonsplit node means one rational singular point whose preimage in the normalization is one degree-two closed point; after extending scalars to \(\bar k\), it is an ordinary node with two conjugate branches. No assertion is made for nonsquare base fields, characteristic two or three, arithmetic genus other than two, or normalizations not \(k\)-isomorphic to the chosen \(E\).

## Proof
**1. Every maximal curve is a unique pinching of a degree-two point.** For geometric genus \(g=1\) and arithmetic genus \(\pi=2\), the Aubry--Perret bound is \(p^2+1+2p+1=p^2+2p+2\). The normalization has at most \(p^2+2p+1\) rational points. For a curve attaining the bound, the difference from its normalization must be exactly one; all the arithmetic-genus defect \(\pi-g=1\) is concentrated at one rational singularity with no rational point lying above it. The normalization preimage must therefore be a closed point \(P\) of degree two, with local normalization ring \(\mathcal O_{E,P}\), maximal ideal \(\mathfrak m_P\), and unique colength-one subring containing the base field
\[\mathcal O_{C,s}=k+\mathfrak m_P\subset\mathcal O_{E,P}.\]
After scalar extension to \(\bar k\), the residue algebra \(\mathbb F_{p^4}\otimes_k\bar k\) splits as two copies of \(\bar k\); the completed local ring becomes the pairs of power series with equal constant terms, isomorphic to \(\bar k[[u,v]]/(uv)\). Thus the singularity is an ordinary geometric node. This is also the equality case of Aubry--Iezzi's degree-two-point criterion (their Proposition 5.2). Conversely, pinching any degree-two closed point \(P\) of \(E\) by that local subring produces a geometrically integral projective curve of arithmetic genus two with one nonsplit node and one extra rational point. Thus it is maximal. The normalization and singular subring determine this curve uniquely up to \(k\)-isomorphism. Hence the desired classes are the degree-two closed points of \(E\) modulo \(\operatorname{Aut}_k(E)\).

**2. Frobenius reduces pinching points to nonzero torsion differences.** The \(p^2\)-Frobenius of maximal \(E\) has characteristic polynomial \((T+p)^2\). Since an elliptic-curve endomorphism algebra has no nonzero nilpotents, Frobenius equals multiplication by \(-p\). Consequently,
\[E(\mathbb F_{p^4})=E[p^2-1],\qquad E(k)=E[p+1].\]
Every degree-two closed point can be written as an unordered Frobenius pair \(\{Q,FQ\}\) with \(Q\in E(\mathbb F_{p^4})\setminus E(k)\). Define \(D=FQ-Q=-(p+1)Q\). Multiplication by \(p+1\) maps \(E[p^2-1]\) onto \(E[n]\) with kernel \(E[p+1]\), so \(D\) ranges over precisely \(E[n]\setminus\{0\}\). Two choices with the same \(D\) differ by translation by a point in \(E(k)\). Swapping the two conjugate branches sends \(D\) to \(-D\).

**3. Quotient by all unpointed automorphisms.** Write \(G=\operatorname{Aut}_{\bar k}(E,O)\), so \(\#G=m\). Every member of \(G\) is defined over \(k\): the \(p^2\)-Frobenius \([-p]\) commutes with every geometric endomorphism, and the corresponding Galois action is trivial. Moreover,
\[\operatorname{Aut}_k(E)=E(k)\rtimes G,\qquad -1\in G.\]
An element \(R+\alpha\), with \(R\in E(k)\) and \(\alpha\in G\), takes a degree-two pair with difference \(D\) to a pair with difference \(\alpha D\). The unordered-pair ambiguity \(D\leftrightarrow-D\) is already included in \(G\). Hence the isomorphism classes are exactly the \(G\)-orbits on \(E[n]\setminus\{0\}\). If \(G_D\) is the stabilizer of \(D\), a direct count of the two possible targets \(Q\) and \(FQ\) shows
\[\#\operatorname{Aut}_k(C)=2\,\#G_D.\]
Indeed, when \(D\neq-D\), the group elements sending \(D\) to \(D\) or \(-D\) form two cosets of \(G_D\), each giving one translation. When \(D=-D\), there is one coset, but each of its elements admits two distinct translations interchanging or fixing the branches.

**4. Fixed-point counts and orbit sizes.** The \(n\)-torsion is \(E[n]\cong(\mathbb Z/n\mathbb Z)^2\) and \(n\) is even. Thus inversion fixes exactly the three nonzero two-torsion points. If \(m=2\), Burnside gives \((n^2-1+3)/2=(n^2+2)/2\) orbits; three are singleton inversion-fixed orbits, yielding three order-four automorphism groups. All others have order two.

If \(m=4\), each element of order four has precisely one nonzero fixed point on \(E[n]\): the kernel of its difference from the identity has degree two. The two elements of order four fix the same nonzero two-torsion point. Burnside gives \((n^2-1+3+1+1)/4=(n^2+4)/4\) orbits. One orbit has stabilizer order four (curve automorphism order eight), a second orbit of size two has stabilizer order two (order four), and all remaining orbits have trivial stabilizer (order two).

If \(m=6\), supersingularity forces \(p\equiv2\pmod3\), hence \(3\nmid n\). Elements of order three have no nonzero fixed \(n\)-torsion because their difference from the identity has degree three. Elements of order six have no fixed nonzero points because that difference has degree one. Only inversion contributes the three nonzero fixed points. Burnside gives \((n^2-1+3)/6=(n^2+2)/6\) orbits. The three nonzero two-torsion points form one orbit of size three, giving curve automorphism order four; all remaining orbits are free and have curve automorphism order two. This establishes every entry of the table.

As a consistency check, the orbit-stabilizer identity recovers the total number of degree-two closed points:
\[\sum_{[C]}\frac{m(p+1)^2}{\#\operatorname{Aut}_k(C)}=\frac{(p^2-1)^2-(p+1)^2}{2}.\]

## Verification
The included `verify_orbits.py` enumerates the action of the cyclic groups of orders \(2\), \(4\), and \(6\) on the nonzero pairs modulo \(n=p-1\), and verifies the class counts, orbit sizes, and predicted automorphism orders at ten admissible sample pairs \((p,m)\). It additionally counts points by direct arithmetic in quadratic finite fields for the maximal elliptic examples in characteristics \(5\), \(7\), and \(11\). The saved script returns `VERIFY_OK` and `FULL_VERIFY_OK`. These finite checks are consistency tests; the proof of the formulas for all permitted primes is the Frobenius-and-Burnside argument above.

## Relationship to prior work
Hilario--Salomão--Martins (2026), especially Theorem 3.4, construct explicit genus-one-normalization maximal singular curves with a nonsplit node and study gonality. Aubry--Iezzi (2015; 2017) establish the degree-two pinching construction and criteria for maximal singular curves. Their results supply the existence and local geometry used here; neither inspected treatment determines the unpointed \(k\)-isomorphism-class census or its full \(k\)-automorphism-order distribution for a fixed maximal elliptic normalization. The present orbit calculation also includes degree-two points with rational \(x\)-coordinate, which the interpolation construction in the 2026 paper explicitly sets aside. General moduli-of-nodal-curves principles motivate the quotient interpretation but do not by themselves evaluate these finite-field orbit frequencies.

## Limitations
The conclusion is conditional on a fixed maximal elliptic curve \(E/k\), not a sum over all such elliptic normalizations. Counts are of unpointed curves up to \(k\)-isomorphism, not of embedded projective models or arithmetic twists of a fixed curve. The methods use a square finite field, odd prime at least five, and precisely one nonsplit node. Independent verification of mathematical priority and validity has not been carried out.

## References
1. C. Hilario, R. Salomão and R. Vidal Martins, *Maximal singular curves over finite fields from elliptic and hyperelliptic curves*, arXiv:2609.22557 (first public 2026-09-18), particularly §§2.2, 3.3, 4.3.
2. Y. Aubry and A. Iezzi, *On the maximum number of rational points on singular curves over finite fields*, arXiv:1501.03676 (2015), especially Proposition 5.2 and Theorem 5.3.
3. Y. Aubry and A. Iezzi, *Optimal and maximal singular curves*, arXiv:1510.01853 (2015; published 2017).
