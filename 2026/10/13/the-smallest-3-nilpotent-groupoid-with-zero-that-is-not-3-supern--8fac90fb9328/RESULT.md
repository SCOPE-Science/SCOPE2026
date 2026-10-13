# The smallest 3-nilpotent groupoid with zero that is not 3-supernilpotent has four elements
## Finding
Among groupoids with zero, the minimum cardinality of a \(3\)-nilpotent algebra that is not \(3\)-supernilpotent is \(4\).

A minimum example is
\[
G=\{0,a,b,c\},
\]
with multiplication
\[
c\cdot c=b,\qquad b\cdot b=a,
\]
and every other product equal to \(0\). Thus
\[
G^2=\{0,a,b\},\qquad (G^2)^2=\{0,a\}\neq\{0\}.
\]

## Assumptions and scope
A groupoid with zero means a binary algebra \((G,\cdot,0)\) in which \(0\cdot x=x\cdot0=0\) for every \(x\in G\). Nilpotency and supernilpotency are in the term-condition-commutator sense used by Đurđev and Mudrinski. Their Theorem 4.7 characterizes \(3\)-nilpotency by vanishing of polynomial terms of depth at least \(3\), and their Proposition 5.3 states that a groupoid with zero is \(3\)-supernilpotent exactly when it is \(3\)-nilpotent and \((G^2)^2=\{0\}\).

The claim concerns the first separating level \(n=3\). It does not assert minimum cardinalities for \(n\ge4\).

## Proof
For the four-element example, the values of terms of exact depth \(1\) lie in \(\{0,a,b\}\). A term of exact depth \(2\) must have a child of exact depth \(1\). The only way such a term can be nonzero is to multiply two occurrences of \(b\), giving \(a\). Hence every exact-depth-\(2\) value lies in \(\{0,a\}\). Since both \(0\) and \(a\) annihilate all of \(G\), every term of exact depth \(3\) vanishes. Any term of larger depth contains a depth-\(3\) subtree, so it also vanishes. By Theorem 4.7, \(G\) is \(3\)-nilpotent.

On the other hand, \(b=c\cdot c\) belongs to \(G^2\) and \(b\cdot b=a\neq0\). Therefore \((G^2)^2\neq\{0\}\), so Proposition 5.3 implies that \(G\) is not \(3\)-supernilpotent.

It remains to prove minimality. Suppose that a \(3\)-nilpotent groupoid with zero \(H\) is not \(3\)-supernilpotent. Proposition 5.3 gives \(u,v\in H^2\) with
\[
u\cdot v=w\neq0.
\]
Choose \(x,y,z,t\in H\) with \(x\cdot y=u\) and \(z\cdot t=v\). Because \(H\) is \(3\)-nilpotent, Theorem 4.7 applied to
\[
((x\cdot y)\cdot(z\cdot t))\cdot s
\quad\text{and}\quad
s\cdot((x\cdot y)\cdot(z\cdot t))
\]
shows that \(w\) annihilates every \(s\in H\) on both sides. In particular \(u\neq w\) and \(v\neq w\), since otherwise \(u\cdot v=w\) would contradict that annihilation.

If \(u\neq v\), then \(0,u,v,w\) are four distinct elements. If \(u=v\) and \(|H|\le3\), then the only possible nonzero elements are \(u\) and \(w\). Since \(u\in H^2\), write \(r\cdot s=u\). Neither factor can be \(0\) or \(w\), because both annihilate every element. Hence \(r=s=u\), so \(u\cdot u=u\). But \(u=v\) and \(u\cdot v=w\) also give \(u\cdot u=w\), a contradiction. Therefore \(|H|\ge4\).

## Verification
A standalone exhaustive checker is included as `check_minimal.py`. It enumerates all \(3^4=81\) labeled groupoids with zero on three elements, tests exact term-depth value sets, and finds no \(3\)-nilpotent/non-\(3\)-supernilpotent separator. It also checks the displayed four-element multiplication table and prints `CHECK_OK`.

The finite enumeration is only a cross-check. The lower bound for all groupoids of cardinality at most \(3\) is proved symbolically above.

## Relationship to prior work
Đurđev and Mudrinski prove the exact criterion
\[
\text{\(3\)-supernilpotent}\iff
\text{\(3\)-nilpotent and }(G^2)^2=\{0\},
\]
and give, for every \(n\ge3\), a separating groupoid \(H_n\) of cardinality \(2^n\). At \(n=3\) their construction therefore has \(8\) elements. The inspected paper does not state a minimum-cardinality result, and searches in that text for “minimal”, “smallest”, “four-element”, and “cardinality” did not reveal such a statement.

Earlier work on semigroups with zero proves coincidence of nilpotency and supernilpotency in the associative setting, so it does not cover the nonassociative four-element separator here.

## Limitations
The minimum \(4\) is proved only for groupoids with an absorbing zero and only for the \(n=3\) notions used in the cited paper. No claim is made about minimum separating examples for higher \(n\), for richer operation signatures, or for algebras without an absorbing zero.

The originality check found no covering statement in the inspected sources or targeted searches, but absence from searched literature is not a proof of global novelty.

## References
1. I. Đurđev and N. Mudrinski, “(Super)nilpotency and solvability in algebras with zero,” arXiv:2610.03348v1, 2026. See Theorem 3.9, Theorem 4.7, Proposition 5.3, and Example 5.4.
2. J. Radović and N. Mudrinski, “Higher commutators in semigroups with zero,” Algebra Universalis 84 (2023), Article 12, DOI: 10.1007/s00012-023-00809-5.
3. J. Radović and N. Mudrinski, “Supernilpotent semigroups,” Portugaliae Mathematica 81 (2024), 307–320, DOI: 10.4171/PM/2118.
