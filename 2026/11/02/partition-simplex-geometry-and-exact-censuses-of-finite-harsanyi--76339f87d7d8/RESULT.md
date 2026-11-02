# Partition-simplex geometry and exact censuses of finite Harsanyi probability frames

## Finding
For every finite labelled carrier, the Harsanyi introspection condition determines a canonical partition of states into identical-belief types. The resulting real parameter space has one convex component per set partition. Both the fixed-denominator labelled census and the isomorphism-class census have exact generating functions, and the fraction of grid kernels satisfying introspection has an explicit polynomial decay in the denominator.

More precisely, write \(\operatorname{Part}([n])\) for the set partitions of \([n]=\{1,\dots,n\}\), and let \(\Delta_{s-1}\) be the usual probability simplex on \(s\) labelled coordinates. The space \(\mathcal H_n\) of Harsanyi kernels is a disjoint union of \(\prod_{B\in\pi}\Delta_{|B|-1}\), one for each \(\pi\in\operatorname{Part}([n])\). The component with \(k\) blocks has dimension \(n-k\); in particular there are exactly \(B_n\) connected components, where \(B_n\) is the Bell number.

For a positive integer \(d\), let \(A_{n,d}\) count \(n\times n\) Harsanyi kernels with entries multiples of \(1/d\), allowing zeros. Then
\[
A_{n,d}=\sum_{\pi\in\operatorname{Part}([n])}\prod_{B\in\pi}\binom{d+|B|-1}{|B|-1},\quad
\sum_{n\ge0}A_{n,d}\frac{z^n}{n!}=
\exp\left(\sum_{s\ge1}\binom{d+s-1}{s-1}\frac{z^s}{s!}\right),
\]
with the formal empty-carrier convention \(A_{0,d}=1\). The exact number with \(k\) different belief types is the partial Bell polynomial
\[
A_{n,d,k}=\frac{n!}{k!}[z^n]\left(\sum_{s\ge1}\binom{d+s-1}{s-1}\frac{z^s}{s!}\right)^k.
\]
Let \(p_{\le s}(d)\) denote the number of ordinary integer partitions of \(d\) into at most \(s\) positive parts. The number of kernels up to simultaneous relabelling of rows and columns is
\[
O_{n,d}=[z^n]\prod_{s=1}^n(1-z^s)^{-p_{\le s}(d)}.
\]
For fixed \(n\ge2\),
\[
A_{n,d}=\frac{d^{n-1}}{(n-1)!}+O_n(d^{n-2}),\quad
\frac{A_{n,d}}{\binom{d+n-1}{n-1}^{n}}
\sim ((n-1)!)^{n-1}d^{-(n-1)^2}.
\]
The latter fraction uses the uniform distribution over all \(n\)-row stochastic matrices on the indicated grid, not a probability distribution on a continuum.

## Assumptions and scope
The world set \([n]\), \(n\ge1\), carries the full power-set sigma-algebra. A Markov kernel is a real matrix \(K\) with \(K_{ij}\ge0\) and \(\sum_jK_{ij}=1\) for every \(i\). A *belief type* is the entire row vector \(K_{i\bullet}\). Write \([i]_K=\{j:K_{j\bullet}=K_{i\bullet}\}\). The finite Harsanyi condition is \(\sum_{j\in[i]_K}K_{ij}=1\) for every \(i\), equivalently \(K_{ij}>0\Rightarrow K_{i\bullet}=K_{j\bullet}\). No common-prior, positivity-of-all-entries, self-loop, irreducibility, or full-support assumption is imposed. A denominator-grid kernel has \(dK_{ij}\) an integer for every entry; \(d\) need not be the reduced denominator.

## Proof
**Canonical partition and realization.** Equality of row vectors partitions the world set into nonempty blocks \(\pi_K\). The Harsanyi condition states that all positive coordinates of a row in block \(B\) belong to \(B\). As the row sums to one, its restriction to \(B\) is a point of \(\Delta_{|B|-1}\). Thus every such matrix is represented by a unique set partition and a probability vector for each block.

Conversely choose any set partition \(\pi\) and a probability vector \(q_B\) on each block \(B\). Give every row indexed by \(i\in B\) the vector \(q_B\) on coordinates in \(B\), with zeros outside \(B\). Rows inside each block are identical. Rows belonging to distinct blocks are necessarily different because their nonempty supports lie in disjoint coordinate sets. Consequently the equality classes are exactly the chosen blocks, and the Harsanyi condition holds. This construction and its inverse are affine homeomorphisms on each partition stratum.

Each stratum is a compact convex product of simplices in the Euclidean space of real matrices. Distinct strata are disjoint compact sets; there are only finitely many. They therefore have strictly positive pairwise distances and are precisely the connected components. The dimension of the stratum \(\pi\) is \(\sum_{B\in\pi}(|B|-1)=n-|\pi|\).

**Labelled enumeration.** On a block of size \(s\), multiplying its probability vector by \(d\) gives an \(s\)-tuple of nonnegative integers summing to \(d\). The stars-and-bars count is \(\binom{d+s-1}{s-1}\). The independent choices across blocks give the partition sum. The exponential formula for labelled assemblies of independently weighted blocks gives the displayed exponential generating function. Restricting assemblies to exactly \(k\) blocks gives the partial Bell polynomial. These are identities for every positive integer \(n,d\), not interpolation from finite tables.

**Isomorphism classes.** An isomorphism is a permutation of the world set applied simultaneously to row and column indices. It permutes blocks of the equality partition, and within a block it permutes the coordinates of its single belief vector. Hence a block of size \(s\) is classified by its multiset of \(s\) nonnegative integer weights summing to \(d\), equivalently by an ordinary partition of \(d\) into at most \(s\) positive parts. There are \(p_{\le s}(d)\) such block colors. An isomorphism class is precisely an unordered multiset of independently colored blocks, so the ordinary generating function of the classes is the displayed Euler-type product. No further identification is possible, since differing weight multisets cannot be related by a coordinate permutation.

**Fixed-carrier asymptotics.** For a partition with \(k\) blocks, its weight is a polynomial in \(d\) of degree \(\sum_B(|B|-1)=n-k\). Exactly one partition, the single block, contributes degree \(n-1\); its leading coefficient is \(1/(n-1)!\). Every other partition contributes degree at most \(n-2\), proving the expansion for \(A_{n,d}\). All stochastic grid kernels number \(\binom{d+n-1}{n-1}^{n}\), whose leading term is \(d^{n(n-1)}/((n-1)!)^n\). Division proves the asymptotic probability formula.

**Relation with ordinary stochastic idempotence.** For a Harsanyi kernel and any \(i,k\), every \(j\) with \(K_{ij}>0\) has \(K_{jk}=K_{ik}\). Therefore \((K^2)_{ik}=\sum_jK_{ij}K_{jk}=K_{ik}\sum_jK_{ij}=K_{ik}\). The converse fails on three states for
\[
K=\begin{pmatrix}1&0&0\\0&1&0\\1/2&1/2&0\end{pmatrix}.
\]
Its square equals itself, but its third row assigns positive probability to states with different belief rows. On one or two states every stochastic idempotent matrix is Harsanyi: in the two-state case an idempotent stochastic matrix has rank one (equal rows) or rank two (identity), since its nonzero eigenvalues are all one. The three-state example is therefore minimal.

## Verification
The accompanying independent exact-arithmetic `checker.py` checks the semantic support condition directly, and separately enumerates set partitions to evaluate the formula. For \(n=1,2,3,4\) and \(d=1,2,3\), every eligible stochastic grid matrix was tested (all twelve cases). The labelled counts by \(d=1,2,3\), respectively, are: \(n=1\): \((1,1,1)\); \(n=2\): \((3,4,5)\); \(n=3\): \((10,16,23)\); \(n=4\): \((41,80,133)\). For \(n\le3\) and \(d\le3\), the code independently enumerated simultaneous-permutation orbits and matched the isomorphism formula. It also verified the deterministic (\(d=1\)) count against the standard idempotent-map formula for \(n\le7\) and checked the displayed three-state stochastic-idempotent counterexample. All checks reported `ALL_CHECKS_OK`. Finite tests are not asserted to prove the universal statements; the proofs above do that.

To reproduce: run `python3 checker.py` with only the Python standard library. The code is independent of the theorem's generating-function derivation for the direct semantic enumeration; orbit enumeration uses brute simultaneous permutations on small carriers.

## Relationship to prior work
Chopoghloo, Pourmahdian, and Zoghifard (2026, Example 4.2 and Proposition 4.3) characterize Harsanyi self-knowledge through probability-modal validity; Section 5 explicitly treats finite rational Markov processes. These results supply the natural definable class considered here, but the inspected relevant sections do not state the fixed-denominator full kernel census, the partition-simplex component count, or the isomorphism product.

Zhou (2014, Sections 2–3) develops the same probabilistic introspection semantics and counts maximally consistent *language types* in certain finite modal fragments; Theorems 3.25–3.26 concern finite canonical logical spaces, not all stochastic kernels on a fixed labelled carrier and denominator grid. The familiar theory of idempotent stochastic matrices is broader because \(K^2=K\) is necessary but, starting at three worlds, not sufficient. In particular an older canonical-form result for idempotent substochastic matrices is not by itself the present census unless it additionally imposes Harsanyi support and derives the labeled/orbit formulas.

## Limitations
The classification concerns one-agent finite full-powerset type spaces, with no valuations counted and no multi-agent common-prior requirement. The orbit formula fixes the exact denominator grid, not a bound on the reduced denominator. The dimension and connected-component assertions use the Euclidean topology on real stochastic matrices; they do not describe an infinite-state moduli space. The older stochastic-idempotent classification literature could contain an equivalent special-case enumeration under alternate language; the inspected evidence does not establish historical uniqueness. Independent mathematical audit has not been performed.

## References
1. S. Chopoghloo, M. Pourmahdian, and R. Zoghifard, *Goldblatt-Thomason Theorem for Probability Logic*, arXiv:2606.31865, first public June 30, 2026; EPTCS 447 (2026), 203–221, DOI:10.4204/EPTCS.447.12; especially Example 4.2, Proposition 4.3, and Section 5.
2. C. Zhou, *Probability Logic for Harsanyi Type Spaces*, Logical Methods in Computer Science 10(2:13) (2014), arXiv:1405.6355; especially Sections 2–3 and Theorems 3.25–3.26.
3. C. E. Robinson Jr., *Green's relations for substochastic matrices*, Linear Algebra and its Applications 80 (1986), 39–53, DOI:10.1016/0024-3795(86)90276-4; related broader idempotent classification (only its abstract was inspected).
