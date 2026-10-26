# Sharp rare-decomposability law and conditional splitting for finite-field star-quiver representations

## Finding

Fix a prime power \(q\) and an integer \(r\ge3\). For each \(n\ge1\), take the **inward star quiver** with \(n\) individually labeled source vertices of dimension one, each with a single arrow into one sink of dimension \(r\). Draw its arrow vectors independently and uniformly from \(\mathbb F_q^r\setminus\{0\}\). Let \(\mathcal D_n\) denote decomposability of the resulting representation.

Define the finite projective-point counts
\[
D=\frac{q^r-1}{q-1},\qquad H=\frac{q^{r-1}-1}{q-1},\qquad M=H+1,\qquad K=Dq^{r-1}.
\]
As \(n\to\infty\) with \(q,r\) fixed,
\[
\boxed{\Pr(\mathcal D_n)=K\left(\frac MD\right)^n+O_{q,r}\!\left(\left(\frac HD\right)^n\right).}
\]
In particular, the relative error is \(O_{q,r}((H/M)^n)\). Conditionally on \(\mathcal D_n\), with probability \(1-O_{q,r}((H/M)^n)\), the representation has a **unique direct-sum decomposition** into exactly two indecomposables, of sink dimensions \(1\) and \(r-1\), respectively. On that dominant event, the one-dimensional sink summand contains exactly those source vertices whose arrow images lie on one specified one-dimensional vector line \(L\) (one projective point); the other summand has sink a uniquely determined complementary hyperplane \(W\).

Let \(J_n\) be the number of sources assigned to the line summand on this event, with any convention on the exceptional event. Then
\[
\left\|\mathcal L(J_n\mid\mathcal D_n)-\mathrm{Bin}\!\left(n,\frac1M\right)\right\|_{\mathrm{TV}}
=O_{q,r}\!\left(\left(\frac HM\right)^n\right).
\]
Thus its conditional fluctuations have asymptotic mean \(n/M\), variance \(n(M-1)/M^2\), and normalized standard normal limit.

## Assumptions and scope

All arrows are nonzero; the source vertices remain labeled; \(q,r\) are fixed while \(n\to\infty\); \(q\) may be any prime power, including even characteristic. An indecomposable is an object having no nontrivial direct-sum decomposition in the category of representations of the quiver over \(\mathbb F_q\). Two decompositions are considered the same if they give the same direct summands as subrepresentations at every labeled source and at the sink. All asymptotic constants may depend on \(q,r\). The distribution statement concerns *random labeled representations*, not uniform isomorphism classes.

## Proof

**1. Endomorphism/idempotent criterion.** An endomorphism consists of a linear map \(T\) at the sink and scalars \(c_i\) at the source vertices satisfying \(Tv_i=c_i v_i\) for every nonzero arrow vector \(v_i\). It is an idempotent precisely when \(T^2=T\) and each \(c_i\) is zero or one. Thus a nontrivial idempotent exists exactly when \(V=U\oplus W\) is a proper nontrivial decomposition into the zero and one eigenspaces of \(T\), with every arrow image in \(U\cup W\). Since the \(v_i\) are nonzero, neither \(T=0\) nor \(T=I\) gives a nontrivial endomorphism idempotent. A finite-dimensional quiver representation decomposes if and only if its endomorphism ring has a nontrivial idempotent. This establishes the geometric criterion, including the case when all arrows lie in a proper subspace (take an unused sink complement).

**2. Maximal projective covers.** Each \(v_i\) induces an independent uniform projective point among the \(D\) points of \(\mathbb P(V)\), because each projective point has exactly \(q-1\) nonzero representatives. For a direct sum \(V=U\oplus W\) of dimensions \(a\) and \(r-a\), the allowed set of points is the disjoint union \(\mathbb P(U)\cup\mathbb P(W)\), of size
\[
C_a=\frac{q^a-1}{q-1}+\frac{q^{r-a}-1}{q-1}.
\]
The convexity of the exponential gives \(C_a\le M\), with equality **only** at \(a=1\) or \(a=r-1\). Every other complementary-subspace cover has at most \(M-1=H\) points. An unused-sink event (all vectors span a proper subspace) likewise has a hyperplane containing them and therefore a cover of exactly \(H\) points. There are finitely many such proper subspaces and direct-sum pairs for fixed \(q,r\), independently of \(n\).

**3. Number and distinctness of the maximizers.** A maximal cover is
\[
C(L,W)=\mathbb P(L)\mathbin{\dot\cup}\mathbb P(W),
\quad \dim L=1,\quad\dim W=r-1,\quad L\not\subseteq W.
\]
There are \(D\) choices of the vector line \(L\). Among the hyperplanes, exactly \(q^{r-1}\) avoid \(L\): the number of all hyperplanes is \(D\), the number through \(L\) is \(H\), and \(D-H=q^{r-1}\). Hence there are exactly \(K=Dq^{r-1}\) such pairs.

Different pairs yield different projective point sets: if \(W'\ne W\) is another hyperplane, \(\mathbb P(W')\setminus\mathbb P(W)\) has \(q^{r-2}\ge2\) points, but \(C(L,W)\setminus\mathbb P(W)\) has only the single point \(\mathbb P(L)\). Consequently the unique hyperplane whose complete projective point set is contained in \(C(L,W)\) is \(W\), and \(L\) is its unique remaining point. Any two different maximal covers meet in at most \(M-1=H\) points.

**4. Rare-event enumeration.** Let \(E_{L,W}\) be the event that every arrow projective point belongs to \(C(L,W)\). Then \(\Pr(E_{L,W})=(M/D)^n\). The union bound and two-term Bonferroni bound, using the pairwise intersection estimate, show
\[
\Pr\left(\bigcup_{L,W} E_{L,W}\right)=K(M/D)^n+O_{q,r}((H/D)^n).
\]
Every decomposable configuration not in this union lies in some lower-cardinality cover of at most \(H\) projective points (Step 2). Since there are finitely many, its probability is \(O_{q,r}((H/D)^n)\). Combining these facts proves the sharp probability law.

**5. Rigidity of the exceptional splitting.** In any particular maximal-cover event, the probability that every one of its \(M\) projective points actually occurs is at least \(1-M((M-1)/M)^n\). On complete occupancy the projective support is exactly \(C(L,W)\): there is no other maximal cover containing it (Step 3) and no nonmaximal cover, because those have at most \(H<M\) points. Therefore the idempotent criterion gives the **unique** nontrivial splitting into two factors; a third factor or finer splitting would induce another proper bipartition. Both factors are indecomposable since any further splitting induces a second idempotent/direct-sum cover. This is an explicit uniqueness assertion about summands, not just a general Krull–Schmidt isomorphism statement.

**6. Binomial leaf allocation.** Given \(E_{L,W}\), the \(n\) sampled projective points are independent uniform points of its \(M\) elements; each lies on \(L\) with probability \(1/M\). Its line-leaf count is therefore **exactly** \(\mathrm{Bin}(n,1/M)\). Summing the \(K\) identical conditional laws and bounding exceptional events/overlaps from Steps 4–5 yields total-variation error at most a constant times \((H/M)^n\). The ordinary binomial central-limit theorem completes the assertion.

## Verification

The standalone script `quiver_matroid_verify.py` tests the geometric decomposability criterion by enumerating every subset of projective points over three prime-field configurations: \((q,r)=(2,3),(3,3),(2,4)\). It checks rank-partition decomposability, independent idempotent-based decomposition of the \((2,3)\) case, and exact finite sums by Stirling-surjection weights. Execute `python3 quiver_matroid_verify.py`; the actual output is in `quiver_matroid_verify_output.txt`. It exhausts \(41{,}088\) projective support subsets (and a separate \(128\)-support idempotent test). These finite checks do **not** prove the asymptotic assertion, which follows from the finite-cover and intersection argument above.

## Relationship to prior work

Kinser and Weist (2018) give geometric and homological families/normal forms for indecomposable quiver representations, with an explicit \(n\)-subspace-quiver discussion focused on central dimension two. They do not state the above distribution for central dimension at least three. Kelly and Oxley (1984, Section 4) prove that random finite-field column matroids become connected in a growing-row-rank regime and give upper bounds using unions of subspaces; their full text explicitly assumes a sequence of row dimensions increasing and permits zero columns. Our fixed \(r\) theorem has a different regime, conditions away zero columns and identifies the exact leading constant, dominant decompositions, and conditional binomial law. Gao, Mausberg, and Nelson (2024) study the evolving random matroid with growing row dimension and connectivity thresholds, not this fixed-rank rare-event distribution. Schofield (1992) addresses canonical decompositions of general quiver representations, not the finite-field labeled probability or conditional leaf profile. Standard matroid connectivity and quiver idempotent decomposability are premises, not claimed as new.

## Limitations

The result does not concern zero arrow vectors, dimensions \(r\le2\), dimensions \(r\) or field sizes \(q\) varying with \(n\), or uniform sampling of isomorphism classes. The finite checks use prime fields; the proof covers all prime powers. Published work on random representable matroids includes related qualitative connectivity assertions and subspace-union bounds, so it remains possible that an earlier implicit specialization yields part of the sharp formula. No independent mathematical audit or external certification has been performed.

## References

1. R. Kinser and T. Weist, *Tree normal forms for quiver representations*, arXiv:1810.04977v1 (first public 2018-10-11), Section 4.4, https://arxiv.org/abs/1810.04977 .
2. D. G. Kelly and J. G. Oxley, *On Random Representable Matroids*, Studies in Applied Mathematics 71 (1984), 181–205, Section 4, https://www.math.lsu.edu/~oxley/kelly_oxley_84.pdf .
3. P. Gao, J. Mausberg and P. Nelson, *Evolution of random representable matroids: minors, circuits, connectivity and the critical number*, arXiv:2404.17024v1 (2024-04-25), https://arxiv.org/abs/2404.17024 .
4. A. Schofield, *General Representations of Quivers*, Proc. London Math. Soc. 65 (1992), 46–64, https://doi.org/10.1112/plms/s3-65.1.46 .
