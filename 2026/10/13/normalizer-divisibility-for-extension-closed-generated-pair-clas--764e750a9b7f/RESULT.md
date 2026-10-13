# Normalizer divisibility for extension-closed generated-pair classes
## Finding
Let \(\mathcal C\) be an isomorphism-closed class of finite groups satisfying three hypotheses:

1. every finite cyclic group lies in \(\mathcal C\);
2. every subgroup of a group in \(\mathcal C\) lies in \(\mathcal C\);
3. if \(N\triangleleft H\) with \(N\in\mathcal C\) and \(H/N\in\mathcal C\), then \(H\in\mathcal C\).

For a finite group \(G\), \(x\in G\), and \(K\le G\), define
\[
\mathcal C_G(x)=\{g\in G:\langle x,g\rangle\in\mathcal C\}.
\]
Then
\[
|N_G(\langle x\rangle)\cap K|\mid|\mathcal C_G(x)\cap K|.
\]

In particular, for any set of primes \(\pi\), let
\[
\operatorname{Sep}_{G,\pi}(x)=\{g\in G:\langle x,g\rangle\text{ is }\pi\text{-separable}\}.
\]
Then
\[
|N_G(\langle x\rangle)\cap K|\mid|\operatorname{Sep}_{G,\pi}(x)\cap K|.
\]
Taking \(\pi=\{p\}\) gives the corresponding divisibility for \(p\)-solvable generated subgroups.

## Assumptions and scope
All groups are finite. Extension-closed means precisely hypothesis 3 above. A finite group is \(\pi\)-separable if it has a normal series whose factors are \(\pi\)-groups or \(\pi'\)-groups. No quotient-closure, direct-product closure, saturation, or formation hypothesis is used.

The abstract theorem recovers the soluble case by taking \(\mathcal C\) to be the class of soluble groups, but it is not restricted to soluble generated subgroups. For example, \(p\)-solvable groups may have nonsoluble \(p'\)-factors.

## Proof
Write
\[
H=N_G(\langle x\rangle)\cap K,\qquad A=\mathcal C_G(x)\cap K.
\]
Conjugation by \(H\) preserves \(A\): if \(h\in H\) and \(a\in A\), then \(\langle x,a^h\rangle=\langle x^h,a^h\rangle\) is conjugate to \(\langle x,a\rangle\) because \(\langle x^h\rangle=\langle x\rangle\).

The case \(K=1\) is immediate. We induct on \(|K|\). Choose \(T\le H\), maximal subject to the two conditions
\[
T\triangleleft K
\]
and
\[
\langle x,a,T\rangle\in\mathcal C\quad\text{for every }a\in A.
\]
Such a subgroup exists because \(T=1\) is admissible.

First we show
\[
(H/T)\cap Z(K/T)=1.
\]
Let \(D/T=(H/T)\cap Z(K/T)\). Then \(D\triangleleft K\), \(T\le D\le H\). Suppose \(D>T\), and fix \(a\in A\). Set \(U=\langle x,a,T\rangle\). By the choice of \(T\), \(U\in\mathcal C\). Since \(D\le H\), the group \(D\) normalizes \(\langle x\rangle\); since \(D/T\le Z(K/T)\), we have \([D,a]\le T\); and since \(T\triangleleft K\), \(D\) normalizes \(T\). Hence \(U\triangleleft UD\).

Moreover, \(UD/U\cong D/(D\cap U)\) is a quotient of the finite abelian group \(D/T\). The hypotheses on \(\mathcal C\) imply that every finite abelian group lies in \(\mathcal C\): refine an abelian group by a normal series with cyclic prime-order factors and apply extension closure. Thus \(UD/U\in\mathcal C\), and extension closure gives \(UD=\langle x,a,D\rangle\in\mathcal C\). This holds for every \(a\in A\), contradicting maximality of \(T\). Therefore the displayed central intersection is trivial.

Next, if \(a\in A\) and \(t\in T\), then
\[
\langle x,at\rangle\le\langle x,a,T\rangle\in\mathcal C,
\]
so subgroup closure gives \(at\in A\). Consequently \(A\) is a union of right \(T\)-cosets. Put \(\overline H=H/T\) and \(\overline A=A/T\). The group \(\overline H\) acts on \(\overline A\) by conjugation.

Take a nonidentity \(\overline h\in\overline H\), and let \(L/T=C_{K/T}(\overline h)\). The triviality of \((H/T)\cap Z(K/T)\) implies \(L<K\). The fixed points of \(\overline h\) on \(\overline A\) are exactly
\[
C_{\overline A}(\overline h)=(A\cap L)/T,
\]
while
\[
C_{\overline H}(\overline h)=(H\cap L)/T.
\]
By induction applied with the subgroup \(L\),
\[
|H\cap L|\mid|A\cap L|,
\]
and therefore
\[
|C_{\overline H}(\overline h)|\mid|C_{\overline A}(\overline h)|.
\]

Burnside's orbit-counting lemma now gives
\[
\sum_{\overline h\in\overline H}|C_{\overline A}(\overline h)|\equiv0\pmod{|\overline H|}.
\]
For every nonidentity conjugacy class represented by \(\overline h\), its contribution is
\[
\frac{|\overline H|}{|C_{\overline H}(\overline h)|}|C_{\overline A}(\overline h)|,
\]
which is divisible by \(|\overline H|\) by the preceding divisibility. Hence the identity contribution \(|\overline A|\) is divisible by \(|\overline H|\). Since \(|A|=|T||\overline A|\) and \(|H|=|T||\overline H|\), it follows that \(|H|\mid|A|\), as required.

For the corollary, the class of finite \(\pi\)-separable groups contains every cyclic group, is closed under subgroups by intersecting a \(\pi/\pi'\)-series with a subgroup, and is closed under extensions by splicing a series for the normal subgroup with the lifted series for the quotient. Thus the theorem applies.

## Verification
The proof is symbolic and finite-group-theoretic; it does not rely on an enumeration. The critical points checked directly are: the maximal subgroup \(T\) exists; the central preimage \(D\) is normal in \(K\); the quotient \(UD/U\) is abelian; \(A\) is \(T\)-coset-saturated; the fixed-point sets are exactly the intersections with the preimage of \(C_{K/T}(\overline h)\); and the nonidentity conjugacy-class contributions in Burnside's sum are multiples of \(|\overline H|\).

The argument also explains why a superficially similar bounded-derived-length statement need not follow: the class of groups of derived length at most a fixed bound is not closed under arbitrary extensions, and the motivating source records failure of its corresponding normalizer analogue at derived length two.

## Relationship to prior work
Sabatini proves the relative divisibility
\[
|N_G(\langle x\rangle)\cap K|\mid|\operatorname{Sol}_G(x)\cap K|
\]
for the ordinary solubilizer and supplies the induction through a maximal normal subgroup and Burnside counting. The theorem above isolates the exact closure mechanism used by that proof and yields new instances, notably \(\pi\)-separable and \(p\)-solvable generated-pair sets. The inspected source does not formulate this extension-closed-class theorem or these corollaries.

Akbari et al. discuss adapting solubilizer computations to other subgroup-closed classes such as abelian or nilpotent classes. Their discussion is algorithmic and does not give the normalizer-cardinality divisibility proved here; moreover, subgroup closure alone is insufficient for the proof above.

Garonzi, Lucchini and Otmen study generalized sets \(\mathcal F_G(x)=\{g:\langle x,g\rangle\in\mathcal F\}\) for classes with different closure hypotheses and focus on measure/large-set phenomena. The inspected paper does not state the finite relative normalizer divisibility above.

## Limitations
No claim is made for classes lacking subgroup closure or extension closure. The theorem does not assert that the three stated closure assumptions are necessary. The originality comparison is limited by terminology: an equivalent result could occur in formation or Fitting-class literature under a different name for generated-pair sets. No such statement was found in the targeted searches described in the review record.

## References
1. L. Sabatini, *Arithmetic properties of solubilizers*, arXiv:2610.03151v1, 2026.
2. A. Akbari et al., *The Number of Solvabilizers in Finite Groups*, arXiv:2511.11544v1, 2025.
3. M. Garonzi, A. Lucchini and E. A. Otmen, *Profinite groups with many elements with large nilpotentizer and generalizations*, Monatshefte für Mathematik, 2025, DOI:10.1007/s00605-025-02112-y.
