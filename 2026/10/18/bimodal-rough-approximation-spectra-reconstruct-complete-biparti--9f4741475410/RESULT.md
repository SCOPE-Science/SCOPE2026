# Bimodal rough-approximation spectra reconstruct complete bipartite tolerance quotients

## Finding
Fix positive integers \(m,n\). Consider the family of finite equivalence/tolerance frames described below, having \(m+n\) equivalence classes, with a complete bipartite tolerance relation between classes. For each subset \(X\) form its two approximations \((L(X),V(X))\). Count each **distinct output pair once**, not with multiplicity equal to the number of subsets producing it. If \(\ell(Y)\) denotes the number of equivalence classes comprising the definable set \(Y\), then the exact bivariate image spectrum is
\[
P_{m,n}(s,t)=1+t^{m+n}(1+s)^{m+n}
 +\sum_{j=1}^{m-1}\binom mj(1+s)^j t^{n+j}
 +\sum_{j=1}^{n-1}\binom nj(1+s)^j t^{m+j}.
\]
Empty sums are zero. Thus the exact number of output pairs is
\[
|\mathcal R_{m,n}|=2^{m+n}+3^m+3^n-2^m-2^n-1.
\]
The lower-coordinate profile is
\[
Q_{m,n}(s)=P_{m,n}(s,1)
=(1+s)^{m+n}+(2+s)^m+(2+s)^n
 -(1+s)^m-(1+s)^n-1.
\]
This profile determines the unordered pair \(\{m,n\}\) uniquely. Hence two members of this family have the same bivariate spectrum at every pair of degrees (equivalently the same lower-coordinate profile) **if and only if** their loop-deleted quotient tolerance graphs are isomorphic complete bipartite graphs.

## Assumptions and scope
Let \(U\) be a finite nonempty set and \(E\) an equivalence relation. Each \(E\)-class has at least two elements. Partition the distinct \(E\)-classes into nonempty collections \(\mathcal A\) and \(\mathcal B\) with \(|\mathcal A|=m\) and \(|\mathcal B|=n\). Define \(T\) by \(uTv\) if and only if \(uEv\), or the \(E\)-classes of \(u\) and \(v\) lie on opposite sides. Thus \(T\) is reflexive, symmetric, and \(E\)-compatible; it is not generally transitive. Its quotient on the \(E\)-classes has all loops and precisely the edges of \(K_{m,n}\).

For \(X\subseteq U\), write \(L(X)=\{u\in U:E[u]\subseteq X\}\) and \(V(X)=\{u\in U:T[u]\cap X\ne\varnothing\}\). Let \(\mathcal R_{m,n}=\{(L(X),V(X)):X\subseteq U\}\), and for an \(E\)-saturated set \(Y\) let \(\ell(Y)\) be its number of constituent \(E\)-classes. Both \(L(X)\) and \(V(X)\) are \(E\)-saturated. Define \(P_{m,n}(s,t)=\sum_{(L,V)\in\mathcal R_{m,n}}s^{\ell(L)}t^{\ell(V)}\). These exponents count **blocks**, not elements of \(U\).

The assertions hold for every choice of finite class sizes at least two, with no equality-of-size requirement. The class-size hypothesis is essential: singleton classes need not admit the partial intersection used in the proof.

## Proof
**1. Reduce truth sets to active and full classes.** Index the \(E\)-classes by the vertices \(I=\mathcal A\sqcup\mathcal B\) of the looped quotient graph. To a subset \(X\) associate its active indices \(D(X)=\{i:X\cap E_i\ne\varnothing\}\) and fully included indices \(F(X)=\{i:E_i\subseteq X\}\). Then \(F(X)\subseteq D(X)\). Conversely, every pair \(F\subseteq D\subseteq I\) is realized: include whole blocks for \(F\), choose one but not all elements in each block of \(D\setminus F\), and avoid all blocks outside \(D\). The choice exists because every block contains at least two points. Exactly the indices \(F\) constitute \(L(X)\).

**2. Identify the upper output.** By the construction of \(T\), its neighborhood on class indices is \(\{i\}\cup\mathcal B\) for \(i\in\mathcal A\) and \(\{i\}\cup\mathcal A\) for \(i\in\mathcal B\). Consequently \(V(X)\) consists of precisely the classes in the closed neighborhood \(N[D(X)]\) of \(D(X)\). The output pair is therefore completely determined by \((F,N[D])\), and every pair with \(F\subseteq D\) is attainable.

**3. Enumerate outputs without counting repeated inputs.** If \(D=\varnothing\), then necessarily \(F=\varnothing\), giving one output of degree \((0,0)\). If \(D\) meets both sides, or contains an entire side, then \(N[D]=I\). For **every** \(F\subseteq I\), the same full upper output is attainable by selecting \(D=I\) and realizing \(F\subseteq D\) as above. Thus the *distinct* full-upper outputs contribute \(t^{m+n}(1+s)^{m+n}\), independently of how many active sets produced each.

All remaining nonempty active sets lie in a single side and are proper subsets of that side. If \(D\subsetneq\mathcal A\) has size \(j\), where \(1\le j<m\), then \(N[D]=D\cup\mathcal B\), of size \(n+j\). This neighborhood determines \(D\) uniquely; the allowable full sets \(F\subseteq D\) contribute \((1+s)^j\). There are \(\binom mj\) choices of \(D\). The analogous proper subsets of \(\mathcal B\) contribute \(\binom nj(1+s)^jt^{m+j}\). These upper sets cannot equal \(I\), nor can two distinct one-sided proper active sets produce the same upper set: each includes all vertices of exactly the *opposite* side and a proper subset of its own side. This proves the displayed polynomial, with no collisions overlooked.

**4. Evaluate and reconstruct.** Substituting \(s=t=1\) into the polynomial gives the count by the binomial theorem. Putting \(t=1\) and summing the two proper-subset families gives the stated formula for \(Q_{m,n}(s)\). Its degree is \(k=m+n\), with coefficient of \(s^k\) equal to one. Subtract the universal full-upper contribution by defining
\[
J(s)=Q_{m,n}(s)-(1+s)^k+1
=\big((2+s)^m-(1+s)^m\big)+\big((2+s)^n-(1+s)^n\big).
\]
For every positive integer \(d\), the polynomial \((2+s)^d-(1+s)^d\) has degree \(d-1\) and positive leading coefficient \(d\); in particular, leading terms cannot cancel. Therefore \(\deg J+1=\max\{m,n\}\). Knowing \(k\) then gives \(\min\{m,n\}=k-\deg J-1\). This proves reconstruction and the claimed if-and-only-if. The quotient graph \(K_{m,n}\) is determined up to isomorphism by this unordered pair, including the edge case \(m=n=1\).

## Verification
Run the included stand-alone Python 3 file `verify.py` from the same directory as this document. It uses the standard library, enumerates all raw truth assignments for 19 small parameter-and-block-size families, computes outputs directly from the two relations, and independently compares the resulting bivariate multiplicity maps with the closed formula. It also verifies the inverse fingerprint for 120 unordered width pairs. A successful run reports:

```
VERIFY_OK brute_cases 19 valuations 20656 distinct_pairs 923 inverse_profiles 120
```

The mathematical proof above, not the finite computation, covers all positive integers \(m,n\) and all allowed class sizes.

## Relationship to prior work
Järvinen, Kovács and Radeleczki [1] define exactly this type of lower-equivalence/upper-compatible-tolerance approximation pair and prove general completeness and lattice-theoretic properties for \(RS(E,T)\), including a singleton-block obstruction. That broader structural framework is antecedent and is not claimed here. The result above instead computes the entire block-rank generating polynomial and solves the inverse-spectrum problem for the natural complete-bipartite quotient family. Their Theorem 3.1 does not state these enumerations or inverse identification.

Järvinen and Radeleczki [2] give a three-valued-function viewpoint on related rough approximation pairs, but not the two-operator complete-bipartite spectrum. Wang and Zhu [3] encode covering-based approximations using bipartite graphs; their bipartite *incidence* construction is not the E-compatible tolerance quotient used here. Javaid and collaborators [4] study graph rough sets via automorphism-orbit similarity, again with a different pair of relations and objectives. No priority claim is made beyond these inspected comparisons; an equivalent earlier enumeration under different terminology remains possible.

## Limitations
The spectrum counts distinct lower/upper output pairs and grades them by equivalence-class numbers, **not** by underlying-element cardinalities and **not** by how many input subsets realize them. The result is restricted to completely bipartite quotient tolerances and to blocks of size at least two; changing either condition may change the answer. The spectrum determines the unordered bipartition widths, not the multiplicities of elements *inside* individual equivalence classes. Finite verification is not a proof of unrestricted statements. Independent mathematical and literature-priority validation has not been performed.

## References
[1] J. Järvinen, L. Kovács and S. Radeleczki, *Defining rough sets using tolerances compatible with an equivalence*, arXiv:1811.09609 (first posted 2018-11-21), *Information Sciences* 496 (2019), 264–283.

[2] J. Järvinen and S. Radeleczki, *Defining rough sets as core-support pairs of three-valued functions*, arXiv:2011.03461 (2020).

[3] J. Wang and W. Zhu, *An approach to covering-based rough sets through bipartite graphs*, FUZZ-IEEE (2014), 1213–1218, doi:10.1109/FUZZ-IEEE.2014.6891666.

[4] I. Javaid, S. Ali, S. U. Rehman and A. Shah, *Rough sets in graphs using similarity relations*, *AIMS Mathematics* 7 (2022), 5790–5807, doi:10.3934/math.2022320.
