# A sharp generic five-unitary first-round threshold for two-qubit random-unitary channels
## Finding
Let \(m\ge2\), let \(p_1,\ldots,p_m>0\) with \(\sum_i p_i=1\), and let \(U_1,\ldots,U_m\in U(4)\) act on \(\mathbb C^2\otimes\mathbb C^2\). Define
\[
\mathcal E(\rho)=\sum_{i=1}^m p_iU_i\rho U_i^\dagger,
\qquad
V_m=\operatorname{{span}}_\mathbb C\{{U_i^\dagger U_j:1\le i,j\le m\}}.
\]
For Haar-almost every ordered \(m\)-tuple the following sharp dichotomy holds.

For \(m\in\{{2,3,4\}}\),
\[
\dim V_m=m^2-m+1,
\qquad
V_m\cap(M_2\otimes I_2)=V_m\cap(I_2\otimes M_2)=\mathbb C I_4.
\]
Consequently neither party has an informative first local measurement in Cohen's channel-LOCC criterion, so the channel is not implementable by LOCC even with infinitely many rounds.

For every \(m\ge5\),
\[
V_m=M_4(\mathbb C)
\]
for Haar-almost every tuple. Hence both local intersections equal their full four-dimensional local matrix algebras, and each party has nontrivial positive two-outcome first local measurements. Thus the first-round linear obstruction vanishes. This does **not** imply that the channel is LOCC.

The threshold is therefore exactly five random unitaries for two qubits.

## Assumptions and scope
The unitaries are sampled from product Haar measure on \(U(4)^m\). The probabilities are arbitrary but strictly positive; they do not affect the pair-product span because the Kraus operators \(K_i=\sqrt{{p_i}}U_i\) only rescale \(U_i^\dagger U_j\) by nonzero factors.

The conclusion for \(m\le4\) concerns full LOCC impossibility because Cohen's theorem says that if no party can perform a first nontrivial local measurement, then no finite- or infinite-round LOCC protocol exists. The conclusion for \(m\ge5\) is intentionally weaker: it says only that this particular first-round obstruction disappears.

"Haar-almost every" permits exceptional algebraic families, including specially structured product or commuting unitaries.

## Proof
Write
\[
\mathcal A=M_2(\mathbb C)\otimes I_2,
\qquad
\mathcal B=I_2\otimes M_2(\mathbb C).
\]
Both have complex dimension \(4\) and contain \(I_4\).

First, every diagonal pair product is the same operator:
\[
U_i^\dagger U_i=I_4.
\]
Therefore
\[
\dim V_m\le \min\{{16,\,m(m-1)+1\}}.
\]
For \(m=2,3,4\), the upper bounds are respectively \(3,7,13\).

The attached exact verifier constructs five unitaries \(U_1,\ldots,U_5\) over \(\mathbb Q(i)\) by taking \(U_1=I_4\) and, for four explicitly listed Hermitian Gaussian-rational matrices \(H_r\),
\[
U_{{r+1}}=(I_4-iH_r)(I_4+iH_r)^{{-1}}.
\]
The Cayley transform makes each \(U_{{r+1}}\) unitary. Reduction modulo the prime \(1009\), with \(i\mapsto469\) and \(469^2\equiv-1\pmod{{1009}}\), gives the exact rank certificate
\[
\begin{{array}}{{c|c|c|c}}
m&\dim V_m&\dim(V_m+\mathcal A)&\dim(V_m+\mathcal B)\\\hline
2&3&6&6\\
3&7&10&10\\
4&13&16&16\\
5&16&16&16
\end{{array}}.
\]
A nonzero minor after this reduction is a nonzero minor over \(\mathbb Q(i)\). The theoretical upper bounds above therefore force the displayed characteristic-zero ranks. In particular, for the first three prefixes,
\[
\dim(V_m\cap\mathcal A)=\dim(V_m\cap\mathcal B)
=\dim V_m+4-\dim(V_m+\mathcal A)=1,
\]
and for the five-unitary witness \(V_5=M_4(\mathbb C)\).

Each rank condition is the nonvanishing of at least one minor whose entries are real-analytic functions of the unitary matrix entries. Since the displayed witness makes the relevant minor nonzero, that minor is not identically zero on the connected real-analytic manifold \(U(4)^m\). The zero set of a nonzero real-analytic function has Haar measure zero. Hence the maximal ranks certified by the witness hold Haar-almost surely for \(m=2,3,4,5\). For \(m>5\), the first five unitaries already span \(M_4(\mathbb C)\) almost surely, so the same conclusion persists.

It remains to translate the span statement into a first local measurement. Cohen's construction places every root POVM element in the span of the Kraus pair products. If \(V_m\cap\mathcal A=\mathbb C I_4\) and likewise for \(\mathcal B\), every possible first local effect is scalar, so neither party can make an informative first measurement.

Conversely, suppose \(V_m=M_4(\mathbb C)\). Choose any nonzero traceless Hermitian \(X\in M_2\). Then \(X\otimes I_2\in V_m\). For the linear map
\[
\Phi(C)=\sum_{{i,j}}C_{{ij}}K_i^\dagger K_j,
\]
Hermitian targets admit Hermitian coefficient preimages because \(\Phi(C^\dagger)=\Phi(C)^\dagger\). Also \(\Phi(I_m)=I_4\). Thus for sufficiently small \(\varepsilon>0\), both
\[
C_\pm=\frac12I_m\pm\varepsilon D
\]
are positive semidefinite and map to the two local effects
\[
E_\pm=\frac12I_4\pm\varepsilon(X\otimes I_2),
\qquad E_++E_-=I_4.
\]
This is a nontrivial first local measurement. The same argument applies to Bob.

## Verification
`verify_generic_random_unitary.py` is a standalone standard-library exact checker. It carries out the finite-field reduction of the explicit Cayley witness, verifies \(469^2\equiv-1\pmod{{1009}}\), inverts all required Cayley denominators, and recomputes the pair-product and local-sum ranks for both parties. Its required output begins with `VERIFY_OK` and reports the four rank rows above.

The finite-field calculation is not being used as a numerical experiment for the generic theorem. It certifies a single exact nonvanishing witness; the Haar-almost-sure statement then follows from the analytic-minor argument.

## Relationship to prior work
Cohen introduced the linear first-measurement obstruction for quantum channels and tested random-unitary channels numerically. For each parameter choice he sampled 100 random unitary sets. In the two-qubit case he reported that no party could measure first below global dimension \(D=4\), that neither party could measure first at \(N_u=D=4\) in the sampled instances, and that the obstruction disappeared numerically for \(N_u>D\). He described this as a sharp transition around \(N_u=D\) and as evidence about almost all random-unitary channels with few unitaries.

The result here supplies the missing analytic two-qubit statement. It proves that the sampled \(m=4\) behavior is generic, proves that \(m=5\) already forces the pair-product span to be all of \(M_4(\mathbb C)\) generically, and turns the observed transition into an exact Haar-almost-sure threshold.

A later paper by Cohen gives general bounds on resources and numbers of local-measurement outcomes in LOCC channel protocols, but does not state a random-unitary pair-product-span threshold. Targeted searches using the source title, random-unitary terminology, pair-product spans, first-measurement aliases, and the exact two-qubit threshold did not locate an implication-equivalent theorem.

## Limitations
The proof is specialized to two qubits. It does not classify the critical value \(N_u=D\) for higher local dimensions or multipartite systems, where Cohen's numerics show different behavior. It also does not prove that generic channels with \(m\ge5\) are LOCC; it proves only that the first-round linear obstruction no longer rules them out.

The genericity statement is measure-theoretic. Exceptional structured tuples may have smaller pair-product span or larger local intersections than the generic values.

## References
1. S. M. Cohen, “General approach to quantum channel impossibility by local operations and classical communication,” arXiv:1606.00029 (first public version 31 May 2016); Phys. Rev. Lett. 118, 020501 (2017), DOI:10.1103/PhysRevLett.118.020501.
2. S. M. Cohen, “Strong bounds on required resources for quantum channels by local operations and classical communication,” arXiv:1904.10980 (2019).
