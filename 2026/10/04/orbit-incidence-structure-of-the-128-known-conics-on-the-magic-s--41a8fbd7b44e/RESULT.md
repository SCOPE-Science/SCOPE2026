# Orbit-incidence structure of the 128 known conics on the magic-square surface
## Finding
Let
\[
V\subset\mathbf P^8
\]
be the surface of complex \(3\times3\) magic squares of squares, in the coordinate order
\[
(A,B,C,D,M,E,F,G,H),
\]
and let \(\mathscr C\) denote the 128 rational conics forming the three-distinct-entry locus \(Z_3\) described by Auel--Singer.

Then \(\operatorname{Aut}(V)\) acts transitively on \(\mathscr C\). Since
\[
|\operatorname{Aut}(V)|=2048,
\]
the stabilizer of every conic has order
\[
16.
\]

Every conic \(C\in\mathscr C\) contains exactly four of the 256 trivial points and exactly six singular points of \(V\). With the three singular orbits labelled as in Auel--Singer, the six nodes consist of
\[
4\text{ points of type }p_1
\qquad\text{and}\qquad
2\text{ points of type }p_3,
\]
and no point of type \(p_2\).

Consequently the incidence multiplicities are uniform:
\[
\begin{array}{c|c}
\text{point orbit} & \text{number of conics in }\mathscr C\text{ through one point}\\
\hline
\text{trivial points, size }256 & 2\\
p_1\text{-nodes, size }128 & 4\\
p_2\text{-nodes, size }64 & 0\\
p_3\text{-nodes, size }64 & 4.
\end{array}
\]

This statement concerns the 128 conics already identified in \(Z_3\). It does not assert that they are all conics on \(V\); that exhaustiveness question is explicitly left open in the initiating paper.

## Assumptions and scope
All varieties are over \(\mathbf C\). We use the equations and notation of Auel--Singer, arXiv:2609.09351v1.

Their automorphism theorem gives
\[
\operatorname{Aut}(V)\cong D_4\ltimes (\mu_2^9/\mu_2),
\]
so the sign-change subgroup has order \(256\) and the full automorphism group has order \(2048\). They also show that the singular locus has 256 points in three automorphism orbits of sizes
\[
128,\ 64,\ 64,
\]
represented by points denoted here by \(p_1,p_2,p_3\), and that the trivial locus consists of 256 points in one automorphism orbit.

Their Section 3.1 gives two diagonal families of 64 rational conics each. One family has squared pattern
\[
\begin{pmatrix}
a^2&b^2&c^2\\
c^2&a^2&b^2\\
b^2&c^2&a^2
\end{pmatrix},
\qquad
b^2+c^2=2a^2,
\]
and the other is obtained by reversing the cyclic orientation. Together these are precisely the 128 components of \(Z_3\).

## Proof
Consider the canonical conic in the first diagonal family,
\[
C_0:\ [a:b:c]\longmapsto
[a:b:c:c:a:b:b:c:a],
\qquad
b^2+c^2=2a^2.
\]

First we determine its orbit. The sign-change subgroup
\[
S=\mu_2^9/\mu_2
\]
has order \(256\). A sign change preserves \(C_0\) exactly when the three coordinates carrying \(a\), the three carrying \(b\), and the three carrying \(c\) each receive a common sign. Modulo the global sign, this stabilizer has order
\[
2^3/2=4.
\]
Therefore the \(S\)-orbit of \(C_0\) has size
\[
256/4=64,
\]
which is the whole first diagonal family. A reflection in the square symmetry group \(D_4\) reverses cyclic orientation, carrying the first family to the second. Hence the full automorphism group is transitive on all 128 conics. Orbit--stabilizer now gives
\[
|\operatorname{Stab}(C_0)|=2048/128=16.
\]

Next consider trivial points. A point of \(C_0\) is trivial exactly when all nine squared entries agree, equivalently
\[
a^2=b^2=c^2.
\]
Projectively this gives the four sign classes
\[
[1:\pm1:\pm1].
\]
Thus \(C_0\), and hence every conic in \(\mathscr C\), contains exactly four trivial points.

We now locate the singular points on \(C_0\). Use the six quadratic equations in the Auel--Singer Gröbner presentation:
\[
\begin{aligned}
q_1&=3A^2-2F^2-2G^2+H^2,\\
q_2&=3B^2-2F^2+G^2-2H^2,\\
q_3&=3C^2+F^2-2G^2-2H^2,\\
q_4&=3D^2+2F^2-G^2-4H^2,\\
q_5&=3E^2-4F^2-G^2+2H^2,\\
q_6&=3M^2-F^2-G^2-H^2.
\end{aligned}
\]
The Jacobian minor using the columns
\[
(A,B,C,D,M,E)
\]
restricts to \(C_0\) as
\[
-6^6a^2b^2c^2.
\]
Therefore every point of \(C_0\) with
\[
abc\ne0
\]
is smooth on \(V\). Any singular point of \(C_0\) must therefore lie in one of the three disjoint zero sets \(a=0\), \(b=0\), or \(c=0\).

If \(a=0\), then \(c^2=-b^2\), giving two projective points. Their squared magic-square pattern is, up to scale and a square symmetry, the published pattern of the \(p_3\)-orbit. If \(b=0\), then \(c^2=2a^2\), again giving two projective points, now with the published \(p_1\)-pattern. If \(c=0\), then \(b^2=2a^2\), giving two further points of type \(p_1\). Thus
\[
C_0\cap\operatorname{Sing}(V)
\]
contains exactly six points, four of type \(p_1\) and two of type \(p_3\). Since the full automorphism group preserves each singular orbit, the same split holds on every conic in \(\mathscr C\).

For completeness, a type-\(p_2\) node cannot lie on one of these conics. Every point of a conic in \(\mathscr C\) has at most three distinct squared coordinate values, whereas the displayed representative of the \(p_2\)-orbit has five distinct squared values. Thus the \(p_2\)-orbit is disjoint from \(Z_3\).

Finally double-count incidences. Transitivity on each point orbit and on \(\mathscr C\) makes every incidence multiplicity constant. The trivial-point incidence count is
\[
128\cdot4=256\cdot2.
\]
For the \(p_1\)-orbit,
\[
128\cdot4=128\cdot4.
\]
For the \(p_3\)-orbit,
\[
128\cdot2=64\cdot4.
\]
The \(p_2\)-incidence count is zero. This proves all asserted multiplicities.

## Verification
The accompanying `verify.py` independently checks the finite arithmetic and symbolic identities used in the proof. It verifies:

- the sign-change orbit size \(64\), the full conic orbit size \(128\), and stabilizer order \(16\);
- the four projective trivial sign classes;
- the conic parametrization identity \(b^2+c^2=2a^2\);
- the Jacobian minor
\[
-6^6a^2b^2c^2;
\]
- the six zero-coordinate boundary points and their \(4+2\) singular-orbit split;
- all three nonzero incidence multiplicities by exact double counting.

The script is not a substitute for the published geometric inputs: the automorphism group, singular-orbit classification, and identification of the 128 conics with \(Z_3\) are taken from the cited source. The stored replay output ends in `VERIFY_OK`.

## Relationship to prior work
Auel--Singer determine the full automorphism group of \(V\), classify the 256 singular points into three orbits, identify the 256 trivial points, and exhibit the 128 rational conics making up \(Z_3\). In Appendix A they explicitly state that these are known conics and leave open whether they exhaust all conics on \(V\).

The present statement extracts additional structure from those ingredients: the 128 known conics form a single automorphism orbit with stabilizer 16, and their incidences with the trivial and singular point orbits are exactly the uniform multiplicities above. Targeted searches for the exact orbit, stabilizer, singular-incidence split, and equivalent incidence-design formulation did not locate a prior statement of this result.

Bruin--Thomas--Várilly-Alvarado prove quasi-hyperbolicity of the magic-square surface, giving the broader finiteness context for low-genus curves. Their result does not determine the conic orbit or these point--conic incidence numbers.

## Limitations
The result is about the 128 conics already present in \(Z_3\). It does not prove that \(V\) has no other conics and therefore does not resolve the conic-exhaustiveness question in Auel--Singer.

No scheme structure of the conic Hilbert locus is asserted. The theorem is set-theoretic on the known conics and on the finite point orbits. It also does not classify intersections between pairs of conics away from the distinguished trivial and singular points.

The originality comparison is limited by the possibility of an unindexed computation or discussion of the same incidence bookkeeping; no such statement was located in the checked primary literature or searches.

## References
1. A. Auel, B. Singer, *The algebraic geometry of 3-by-3 magic squares of squares*, arXiv:2609.09351v1, 2026.
2. N. Bruin, M. Thomas, A. Várilly-Alvarado, *Explicit computation of symmetric differentials and its application to quasihyperbolicity*, Algebra & Number Theory 16 (2022), 1377--1405; arXiv:1912.08908.
