# Quartic orbit growth in the generic 2-nilpotent Lazard Lie algebra

## Finding
Fix a prime power \(q\), and let \(\mathbf L=\mathbf L_{2,\mathbb F_q}\) be the Fraïssé limit of finite 2-nilpotent Lazard Lie algebras over \(\mathbb F_q\). Write \(P_2=[\mathbf L,\mathbf L]\), as holds in the generic limit. Let \(i_n\) and \(o_n\) denote, respectively, the numbers of automorphism orbits on injective ordered \(n\)-tuples and on all ordered \(n\)-tuples.

Put
\[
m=\binom n2,
\qquad
N=n+\binom n2,
\qquad
G_s(q)=\sum_{d=0}^{s}{s\brack d}_q,
\]
where \(G_s(q)\) is the Galois number, the total number of subspaces of \(\mathbb F_q^s\).

There is an exact orbit classification on the natural level-1 independent stratum: if \(a=(a_1,\ldots,a_n)\) has linearly independent images in \(\mathbf L/P_2\), then its orbit is determined exactly by
\[
K(a)=\ker\!\left(\Lambda^2\mathbb F_q^n\longrightarrow P_2(\langle a\rangle),\quad e_i\wedge e_j\mapsto[a_i,a_j]\right).
\]
Every subspace of \(\Lambda^2\mathbb F_q^n\) occurs. Hence that stratum has exactly
\[
\boxed{G_m(q)}
\]
automorphism orbits.

For the complete ordered-tuple profile one has
\[
\boxed{G_m(q)\le i_n\le o_n\le G_N(q)G_n(q)}.
\]
Consequently
\[
\boxed{\log_q i_n=\log_q o_n=\frac{n^4}{16}+O(n^3).}
\]
Thus the generic class-2 Lazard Lie algebra has a quartic logarithmic oligomorphic profile, and the leading constant \(1/16\) is already forced by the exterior-square relation space of tuples independent modulo the commutator layer.

## Assumptions and scope
The structure is taken in the Lazard-series language used for the Fraïssé class, over the fixed finite field \(\mathbb F_q\). The source construction gives a homogeneous, uniformly locally finite Fraïssé limit; in the limit the distinguished second level is the commutator subalgebra.

The exact formula \(G_m(q)\) concerns only tuples whose images modulo \(P_2\) are linearly independent. The full orbit profile is not claimed to equal a Galois number. What is proved for all tuples is the two-sided bound above and the sharp leading asymptotic for its logarithm.

## Proof
Let \(V=\mathbb F_q^n\) with ordered basis \(e_1,\ldots,e_n\). The free 2-step nilpotent Lie algebra on \(V\) has underlying vector space
\[
F_2(V)=V\oplus\Lambda^2V,
\]
with \([u,v]=u\wedge v\) and central commutator layer \(\Lambda^2V\).

Suppose first that \(a=(a_1,\ldots,a_n)\) is linearly independent modulo \(P_2\). The canonical homomorphism
\[
\phi_a:F_2(V)\to\langle a\rangle,
\qquad e_i\mapsto a_i,
\]
is surjective. Its kernel meets the degree-1 part trivially: a relation \(\sum_i c_i a_i\in P_2\) would give a linear dependence among the images of the \(a_i\) in \(\mathbf L/P_2\). Therefore
\[
\ker\phi_a=K(a)\le\Lambda^2V.
\]
Moreover \(P_2(\langle a\rangle)\) is exactly the span of the brackets \([a_i,a_j]\), so the marked generated structure is precisely the quotient \(F_2(V)/K(a)\), with the ordered images of the free generators distinguished.

If two such tuples have the same subspace \(K\), their marked generated finite substructures are isomorphic coordinate by coordinate. Homogeneity of the Fraïssé limit extends that marked isomorphism to an automorphism, so the tuples are in the same orbit. Conversely an automorphism preserves every bracket relation, hence preserves \(K(a)\). Thus \(K\) is a complete orbit invariant on this stratum.

Every \(K\le\Lambda^2V\) occurs: the quotient \(F_2(V)/K\), with its natural Lazard series, is a finite member of the age, so it embeds into \(\mathbf L\). The images of the free generators remain independent modulo the second level. This proves the exact count \(G_m(q)\), and in particular the lower bound \(G_m(q)\le i_n\).

For an arbitrary ordered tuple \(a\), use the universal map
\[
\phi:F_2(V)\to\langle a\rangle.
\]
Let
\[
K=\ker\phi,
\qquad
Q=\phi^{-1}\!\big(P_2(\langle a\rangle)\big).
\]
The pair \((K,Q)\) determines the marked generated Lazard Lie algebra: \(F_2(V)/K\) gives the Lie algebra and \(Q/K\) gives its distinguished second level. Hence it gives an upper-bound encoding of tuple orbits.

The vector space \(F_2(V)\) has dimension \(N=n+m\), so there are at most \(G_N(q)\) possibilities for \(K\). Since
\[
P_2(F_2(V))+K\subseteq Q,
\]
the choice of \(Q\) over a fixed \(K\) is a choice of a subspace of
\[
F_2(V)/(P_2(F_2(V))+K),
\]
whose dimension is at most \(n\). Thus there are at most \(G_n(q)\) choices for \(Q\), proving
\[
o_n\le G_N(q)G_n(q).
\]
The middle inequality \(i_n\le o_n\) is immediate.

Finally, for fixed \(q\ge2\), Gaussian-binomial estimates give
\[
\log_q G_s(q)=\frac{s^2}{4}+O(s).
\]
Indeed the middle Gaussian coefficient is at least \(q^{\lfloor s^2/4\rfloor}\), while each coefficient is at most \(q^{d(s-d)+d}\), so
\[
q^{\lfloor s^2/4\rfloor}\le G_s(q)\le (s+1)q^{\lfloor s^2/4\rfloor+s}.
\]
Since \(m=n(n-1)/2\) and \(N=n(n+1)/2\), the lower and upper bounds both have logarithm \(n^4/16+O(n^3)\). This proves the claimed full-profile asymptotic.

## Verification
A standalone verifier checks the finite linear-algebra shadow of the proof without using the closed formulas as its only route. It enumerates every subspace in reduced row-echelon form for \(\mathbb F_2^s\) through \(s=6\) and \(\mathbb F_3^s\) through \(s=4\), and compares those enumerations with the Gaussian-binomial sum.

For \(n\le4\) over \(\mathbb F_2\), it separately enumerates every possible kernel \(K\le\Lambda^2\mathbb F_2^n\), forms the corresponding quotient bracket signature, recovers the kernel from that signature, and verifies that distinct kernels give distinct marked signatures. It also checks the elementary Galois-number bounds used in the asymptotic proof for \(q\in\{2,3,4,5\}\) through dimension \(24\).

Running `python3 verification.py` performs 120 checks and prints `VERIFY_OK`. The exact level-1 independent counts for \(q=2\), \(n=1,\ldots,6\), are
\[
1,\ 2,\ 16,\ 2825,\ 229755605,\ 623476476706836148.
\]
These computations are consistency checks; the infinite orbit statement follows from the free-object quotient description and Fraïssé homogeneity.

## Relationship to prior work
D'Elbée, Müller, Ramsey, and Siniora construct the relevant generic nilpotent Lie algebras using free amalgamation in a Lazard-series language and establish the homogeneous finite-field setting used here. The standard algebraic description of a free 2-step nilpotent Lie algebra as \(V\oplus\Lambda^2V\) is also prior.

The Galois number \(G_s(q)\), meaning the total number of subspaces of \(\mathbb F_q^s\), is classical and is not claimed as new. The new point is the model-theoretic calibration: on the natural independent stratum, automorphism orbits are exactly those subspaces of the exterior-square relation space, and this exact stratum count forces, together with a free-object upper encoding, the leading quartic term \(n^4/16\) for the entire ordered-tuple orbit profile.

Targeted literature and semantic-index checks found the generic-Lie-algebra framework, free 2-step algebra structure, and Galois-number enumeration separately, but no source stating this exact orbit/subspace bijection or the resulting full-profile logarithmic asymptotic.

## Limitations
No exact formula is asserted for \(i_n\) or \(o_n\) outside the level-1 independent stratum. The upper bound deliberately counts many pairs \((K,Q)\) that need not arise as valid marked quotients, because only the leading logarithmic term is needed.

The orbit/subspace correspondence is a short consequence of standard free 2-step Lie algebra and Fraïssé-homogeneity facts, so unindexed folklore remains a residual originality risk. The Galois numbers, Gaussian coefficients, and the description \(V\oplus\Lambda^2V\) are prior mathematics and are explicitly excluded from the novelty claim.

## References
1. Christian d'Elbée, Isabel Müller, Nicholas Ramsey, and Daoud Siniora, *Model-theoretic properties of nilpotent groups and Lie algebras*, arXiv:2310.17595, first submitted 26 October 2023; Journal of Algebra 662 (2025), 640–701, DOI 10.1016/j.jalgebra.2024.08.012.
2. Leandro Cagliero, Luis Gutiérrez Frez, and Fernando Szechtman, *Free 2-step nilpotent Lie algebras and indecomposable representations*, Communications in Algebra 46 (2018), 2990–3005, DOI 10.1080/00927872.2017.1404086.
3. Thomas W. Cusick, *Finite Vector Spaces and Certain Lattices*, Electronic Journal of Combinatorics 5 (1998), R17, DOI 10.37236/1355.
