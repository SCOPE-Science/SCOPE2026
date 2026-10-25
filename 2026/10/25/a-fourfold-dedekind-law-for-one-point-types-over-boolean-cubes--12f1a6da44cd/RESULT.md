# A fourfold Dedekind law for one-point types over Boolean cubes
## Finding
Let \(\mathbb P\) be the countable universal homogeneous partial order. Individually name an induced Boolean inclusion lattice \(B_n=(2^{[n]},\subseteq)\), where \(n\ge0\), and let \(t_n\) be the number of complete **nonalgebraic** one-types over these parameters. Let \(M_n\) be the number of downsets of \(B_n\), equivalently the \(n\)-th Dedekind number, and put
\[
a_s=\sum_{j=0}^{s}(-1)^{s-j}\binom{s}{j}M_j.\]
Then for every \(n\ge0\),
\[
\boxed{t_n=\sum_{s=0}^{n}\binom ns a_s M_{n-s}-2^n.}
\]
Equivalently, writing \(\mathcal M(z)=\sum_{n\ge0}M_nz^n/n!\), the following is an identity of **formal** power series (no positive radius of convergence is asserted):
\[
\boxed{\sum_{n\ge0}t_n\frac{z^n}{n!}=e^{-z}\mathcal M(z)^2-e^{2z}.}
\]
There is also a sharp two-scale asymptotic law:
\[
\boxed{t_n=4M_n+2nM_{n-1}+o(nM_{n-1})\qquad(n\longrightarrow\infty).}
\]
In particular, \(t_n/M_n\longrightarrow4\), although \(M_n\) itself has no known elementary closed form. The number of complete types **including equality types** is \(t_n+2^n\). The initial values of \(t_n\), for \(n=0,\ldots,8\), are
\[
3,\ 6,\ 18,\ 86,\ 808,\ 32408,\ 31415246,\ 9658838479282,\ 224521748953386029538636.
\]
## Assumptions and scope
The parameter set is a fixed, individually named copy of the entire finite Boolean lattice; automorphisms of the Boolean lattice do not identify parameter names. Order means inclusion, and a downset means a subset closed under moving downwards, **not** necessarily closed under joins. The empty downset is allowed. An extension point is distinct from every named point. \(B_0\) has one vertex. Homogeneity and the finite one-point extension property of \(\mathbb P\) identify complete nonalgebraic one-types with admissible labeled extensions. The asymptotic invokes the classical Dedekind-number estimate \(\log_2M_m=(1+o(1))\binom m{\lfloor m/2\rfloor}\), and is therefore conditional only on an established result, not a new proof of that estimate.
## Proof
**Step 1: admissible extensions.** For a new point \(x\), set \(L=\{p\in B_n:p<x\}\) and \(U=\{p\in B_n:x<p\}\). These prescribe a consistent partial order exactly when \(L\) is a downset, \(U\) is an upset, and every \(\ell\in L\) is **strictly** below every \(u\in U\). Conversely, these conditions construct a finite extension. The extension property realizes it and homogeneity equates precisely the identical labeled relation patterns.

**Step 2: the union-of-ideals decomposition.** For each downset \(L\) put \(S(L)=\bigcup_{X\in L}X\subseteq[n]\); the union is empty for \(L=\varnothing\). For any \(S\subseteq[n]\), downsets with \(S(L)\subseteq S\) are exactly the downsets of \(B_{|S|}\), in number \(M_{|S|}\). Inclusion-exclusion therefore shows that the number of downsets with \(S(L)=S\) is \(a_{|S|}\), including the two cases \(L=\varnothing\) and \(L=\{\varnothing\}\) for \(S=\varnothing\). In particular \(a_0=2\), \(a_1=1\), and \(a_s\ge0\).

Fix such an \(L\) with union \(S\). Any \(u\in U\) must contain \(S\). All upsets of the upper interval \([S,[n]]\), a Boolean lattice on \(n-|S|\) coordinates, are possible **except** that \(U\) may not contain \(S\) if \(S\in L\). The only downset \(L\) with union \(S\) and \(S\in L\) is the principal downset \(\downarrow S\); in that one case precisely the full upper interval is excluded. Consequently the number of admissible \((L,U)\) pairs with this union \(S\) is \(a_{|S|}M_{n-|S|}-1\). Summing over all \(2^n\) choices of \(S\) proves the exact formula, including the boundary \(n=0\).

**Step 3: formal transform.** Binomial inversion in Step 2 gives \(\mathcal A(z)=\sum a_sz^s/s!=e^{-z}\mathcal M(z)\). Multiplication of exponential generating functions converts the exact convolution into \(\mathcal A(z)\mathcal M(z)-e^{2z}\), proving the formal identity.

**Step 4: the first two asymptotic scales.** Write \(c_m=\binom m{\lfloor m/2\rfloor}\). The established Dedekind estimate gives \(\log_2 M_m=(1+o(1))c_m\). Since \(c_m\) has nondecreasing first differences, for all integers \(2\le s\le n-2\),
\[
c_s+c_{n-s}\le c_2+c_{n-2}=\bigl(\tfrac12+o(1)\bigr)c_{n-1}.
\]
The same Dedekind estimate (treating bounded indices separately) therefore yields the **uniform** bound
\[
\max_{2\le s\le n-2}M_sM_{n-s}\le2^{(1/2+o(1))c_{n-1}}=o\!\left(2^{-n}M_{n-1}\right).
\]
Moreover the binomial-inversion formula and monotonicity of \(M_j\) give
\[
a_n=M_n-nM_{n-1}+O(2^n M_{n-2}),\qquad a_{n-1}=M_{n-1}+O(2^n M_{n-2}).
\]
The error terms are \(o(M_{n-1})\), again because \(\log_2M_{n-2}=(\tfrac12+o(1))c_{n-1}\). Isolating the terms with \(s\in\{0,1,n-1,n\}\) in the exact convolution, and using \(M_0=a_0=2\), \(M_1=3\), and \(a_1=1\), gives
\[
t_n=2M_n+2a_n+nM_{n-1}+3na_{n-1}
+\sum_{s=2}^{n-2}\binom ns a_s M_{n-s}-2^n.
\]
As \(0\le a_s\le M_s\), the sum is \(o(M_{n-1})\) by the displayed uniform bound (the factor \(2^n\) is harmless). Substitution yields \(t_n=4M_n+2nM_{n-1}+o(nM_{n-1})\). This is an infinite assertion proved using the known Dedekind asymptotic, not inferred from finite numerical experiments.
## Verification
The accompanying `verify.py` is a standalone Python standard-library program. For each \(n=0,1,2,3,4\), it independently constructs every downset, complements downsets to obtain upsets, checks disjointness and all strict cross-relations of each ordered pair, and compares that brute-force count with the binomial-inversion formula. It obtains \(3,6,18,86,808\) and reproduces the displayed higher numerical values from the independently known Dedekind numbers \(M_5,\ldots,M_8\). Running `python3 verify.py` prints `ALL_TESTS_PASS`. These tests do not establish the formula for arbitrary \(n\); Steps 1–4 do.
## Relationship to prior work
The one-point extension description via downsets and upsets is standard for the generic poset, and is explicitly used in earlier work on finite-poset extensions. A published general type-counting result also establishes the associated generic-poset counting problem to be #P-complete; that result does **not** state the present Boolean-cube convolution or its two-scale asymptotic. De Causmaecker and De Wannemacker (2014) develop decompositions of antichains and Dedekind numbers, including spanning-antichain counts. Their theory supplies the Dedekind-number background but the inspected paper does not count these generic-poset types. Earlier exact counts for named two-chain rectangular grids contain the \(n=2\) Boolean square as a special case, but do not include Boolean cubes of arbitrary dimension. The present contribution is the exact cross-domain transform and the asymptotic fourfold law with its first correction; none of the general one-point-extension characterization, Dedekind numbers, or classical Dedekind asymptotics is presented as new.
## Limitations
No elementary formula for Dedekind numbers is claimed. The formal generating function has zero radius of analytic convergence. The asymptotic uses a classical deep estimate for Dedekind numbers, and no fully effective finite-\(n\) error constant is supplied. Exhaustive verification ends at \(n=4\). Specialized or unindexed prior literature could contain an equivalent formula or asymptotic; the literature and database searches below cannot rule that out.
## References
1. I. Dolinka and D. Mašulović, “A universality result for endomorphism monoids of some ultrahomogeneous structures,” arXiv:1009.2892, first posted 2010-09-15, especially the finite-poset one-point extension discussion. https://arxiv.org/abs/1009.2892
2. P. Pál Pach, M. Pinsker, G. Pluhár, A. Pongrácz, C. Szabó, “Reducts of the random partial order,” arXiv:1111.7109, first posted 2011-11-30. https://arxiv.org/abs/1111.7109
3. P. De Causmaecker and S. De Wannemacker, “On the number of antichains of sets in a finite universe,” arXiv:1407.4288, first posted 2014-07-16; see Sections 2, 4–6 and the cited classical Dedekind asymptotics. https://arxiv.org/abs/1407.4288
4. “Finite-parameter 1-type counting in the random poset is #P-complete,” public mathematical record (2026), full result and proof consulted: https://github.com/published-finding corpus/2026/tree/main/2026/10/4/SCOPE-finite-parameter-1-type-counting-in-the-random-poset-is-p-comple--3b955f4020e1
