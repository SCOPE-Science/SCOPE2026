# Exact task-size-conditioned collision spectrum of Reed–Solomon tags

## Finding

Let \(q\) be a prime power, let \(1\le K\le T\le q\), and let \(E\subseteq\mathbb F_q\) have \(|E|=T\). Fix one negative query message represented by a polynomial \(f_0\in\mathbb F_q[X]\) of degree below \(K\). Choose a Boolean task uniformly from the tasks that mark precisely \(S\) of the other \(q^K-1\) messages positive, for \(0\le S\le q^K-1\). Each message is identified with one polynomial of degree below \(K\). Given a uniform evaluation point \(U\in E\), the receiver declares positive exactly when the received tag \(f_0(U)\) equals the tag of some positive message.

Put \(M=q^K-1\) and, for \(0\le r\le T\), define
\[
 A_r=\sum_{t=0}^{\min(r,K-1)}(-1)^t\binom rt(q^{K-t}-1).
\]
Then the **exact number** of size-\(S\) tasks whose false-positive probability is \(j/T\) equals
\[
 \boxed{H_j=\binom Tj\sum_{h=0}^{j}(-1)^h\binom jh\binom{A_{T-j+h}}S},\qquad 0\le j\le T.
\]
Here \(\binom ab=0\) if \(b>a\). In particular, \(H_j\) is a nonnegative integer, \(\sum_{j=0}^T H_j=\binom MS\), and \(H_j\) depends only on \((q,K,T,S)\), not on the evaluation positions or the fixed negative word. The exact false-positive law is \(\Pr(P_{\rm FP}=j/T)=H_j/\binom MS\).

The largest possible collision count is \(\min\{T,S(K-1)\}\) for every \(K\ge2\). When \(S(K-1)\le T\), the number of tasks attaining this sharp worst case is exactly
\[
 \boxed{H_{S(K-1)}=\binom{T}{S(K-1)}\frac{(S(K-1))!}{S!((K-1)!)^S}(q-1)^S}.
\]
For \(K=1\), every false-positive probability is zero; the spectrum formula remains valid, but the separate displayed extremizer formula is intended only for \(K\ge2\).

Write \(a=\binom{A_1}S/\binom MS\) and, when \(T\ge2\), \(b=\binom{A_2}S/\binom MS\). The exact expectation and variance of the **probability over the random task**, not of an individual Bernoulli decoder output, are
\[
 \boxed{\mathbb E[P_{\rm FP}]=1-a},\qquad
 \boxed{\operatorname{Var}(P_{\rm FP})=\frac{a(1-a)+(T-1)(b-a^2)}{T}},
\]
where the second formula uses \(b=a\) if \(T=1\). For each fixed \(K\ge2\) and each fixed \(\alpha\ge0\), letting prime powers \(q\to\infty\), \(T=q\), and \(S=\lfloor\alpha q\rfloor\) gives
\[
 \boxed{P_{\rm FP}\xrightarrow{\Pr}1-e^{-\alpha}}.
\]
Thus a typical size-\(\lfloor\alpha q\rfloor\) task can have a smaller error than the sharp worst-case limit \(\min\{1,\alpha(K-1)\}\). For example, at \(K=2\) and \(\alpha=1\), the worst possible error equals one, whereas the random-task error tends in probability to \(1-e^{-1}\).

## Assumptions and scope

The channel is noiseless. The evaluation coordinate is chosen uniformly from \(E\); task-positive messages form a uniformly sampled **unordered set of \(S\) distinct messages**, conditioned on the fixed query being negative. The map from messages to degree-less-than-\(K\) polynomials is bijective. In a binary-message implementation of this full-message-space model one can take \(q\) a power of two and message length \(K\log_2q\); the theorem is algebraic and permits every prime power. The task ensemble is random; the same formulas are not asserted for particular deterministic rank-test or exact-Hamming-weight task families.

The coefficient normalization is ordinary evaluation \(f(U)\) (no column multipliers); nonzero column scaling would not alter collisions. Repeated selected evaluation points are excluded. The empty positive set \(S=0\) is permitted. The exact extremizer count uses the convention \(0!=1\), and is stated only for \(K\ge2\).

## Proof

**Step 1: reduction to root unions.** Subtract \(f_0\) from each positive polynomial. Translation is a bijection from positive messages to \(S\)-subsets of the \(M=q^K-1\) nonzero polynomials of degree below \(K\). For a set \(F\) of these differences, let
\[
 R(F)=\{x\in E:\text{some }g\in F\text{ has }g(x)=0\}.
\]
The conditional false-positive probability equals \(|R(F)|/T\), so task collisions are unions of polynomial-zero sets.

**Step 2: no-hit counts.** Fix \(r\) distinct points of \(E\). By Lagrange interpolation, the vector space of degree-less-than-\(K\) polynomials vanishing at \(t<K\) prescribed distinct points has dimension \(K-t\), hence \(q^{K-t}-1\) nonzero members. If \(t\ge K\), it has no nonzero member. Inclusion–exclusion over the \(r\) forbidden zero positions therefore gives exactly \(A_r\) nonzero polynomials nonvanishing at all forbidden positions. In particular \(A_0=M\).

**Step 3: complete spectrum.** For a fixed \(j\)-element set \(J\subseteq E\), there are \(\binom{A_{T-j}}S\) positive families whose root-union lies inside \(J\). Inclusion–exclusion over the requirement that each point of \(J\) be hit gives
\[
 \#\{F:R(F)=J\}=\sum_{h=0}^j(-1)^h\binom jh\binom{A_{T-j+h}}S.
\]
This expression depends on \(J\) only through \(j\), so multiplying by \(\binom Tj\) proves the spectrum formula and the independence from positions. Every family has exactly one root-union, proving nonnegativity and total normalization.

**Step 4: worst case and exact equality count.** A nonzero polynomial of degree below \(K\) has at most \(K-1\) roots, so \(|R(F)|\le\min\{T,S(K-1)\}\). For \(K\ge2\), partition as many evaluation sites as required into at most \(S\) disjoint nonempty groups of size at most \(K-1\), and take their monic root-product polynomials. Add other distinct nonzero polynomials if fewer than \(S\) have been used. The root union is maximal, proving sharpness. In the unsaturated case \(S(K-1)\le T\), equality forces every one of the \(S\) polynomial zero sets to have exactly \(K-1\) evaluation roots and forces those root sets to be disjoint. Each \((K-1)\)-element root set specifies precisely \(q-1\) nonzero scalar multiples of its monic product. Choosing the \(S(K-1)\) roots and partitioning into \(S\) unlabeled blocks gives the exact extremizer formula.

**Step 5: moments and limit.** Let \(I_x\) be the indicator that some selected polynomial vanishes at \(x\). Then \(P_{\rm FP}=T^{-1}\sum_{x\in E}I_x\). A single point is avoided with probability \(a\) and two distinct points are jointly avoided with probability \(b\). Therefore \(\mathbb E I_x=1-a\), \(\operatorname{Var}(I_x)=a(1-a)\), and \(\operatorname{Cov}(I_x,I_y)=b-a^2\), yielding the displayed moments. For fixed \(K\ge2\) and \(S=\lfloor\alpha q\rfloor\), the ratios of binomial coefficients can be written as products of \(S\) factors. Since \(M=q^K-1\), \(A_1=q^K-q^{K-1}\), and \(A_2=q^{K-2}(q-1)^2\), those products converge to \(a=e^{-\alpha}\) and \(b=e^{-2\alpha}\), respectively. The variance tends to zero and the mean tends to \(1-e^{-\alpha}\). Chebyshev's inequality proves convergence in probability. The case \(\alpha=0\) follows directly from \(S=0\).

## Verification

An independent exact-integer verifier enumerates every distinct positive-family subset for 113 parameter grids over prime fields of sizes \(2\), \(3\), and \(5\), including empty and full task sets where computationally feasible. It compares the entire observed histogram with the theorem, directly recomputes the exact mean and variance, tests the sharp maximum, and checks the explicit unsaturated extremizer count. Run `python3 verification/verify.py`; no nonstandard packages are required. One nontrivial check gives \((H_0,H_1,H_2,H_3)=(1,15,12,0)\) at \((q,K,T,S)=(3,2,3,2)\), with mean error \(13/28\) and variance \(27/784\). The finite runs verify instances, not the infinite-parameter proof.

## Relationship to prior work

He, Yu and Zhu's October 2026 Boolean-function-computation construction uses Reed–Solomon tagging and proves a uniform worst-case error upper bound \(\min\{1,S(K-1)/T\}\). Its numerical section compares observed errors for particular fixed task families but does not give the full population distribution over all tasks with a prescribed positive-set cardinality. The worst-case bound itself is credited rather than claimed new. The statement here supplies sharpness, the exact extremal population, the complete random-task error law and its limiting typical value.

Classical higher tuple-support enumerators (Kaplan and earlier work) and MDS support-weight calculations provide a more general coding-theoretic language in which this collision union is naturally expressed. They are substantial conceptual prior coverage. The present calculation explicitly removes repeated and zero word choices and obtains the closed task-conditioned spectrum by a two-level inclusion–exclusion. The distinction is an explicit finite-task probability law, not the invention of a new general support-enumerator formalism. Potential derivability from older enumerator identities and unpublished specialized calculations remains a priority risk.

Liu, Chen, Zheng and Chen (October 2026) compute distributions of supports of **linear subcodes** of twisted Reed–Solomon codes. A positive Boolean task here is an arbitrary \(S\)-element subset of nonzero codewords, not a vector subspace; the counting objects and weights differ. Their formulas are therefore not directly the stated task-subset distribution.

## Limitations

The population theorem applies to the uniform ensemble of all fixed-size positive sets and noiseless tags, not to every individual task family or to channel decoding errors. It does not improve worst-case coding rates or the universal union bound. The asymptotic statement fixes \(K\) and uses the full field as evaluation set. Priority with respect to equivalent formulas implicit in classical higher support enumerators or unindexed literature has not been independently established. No independent audit is asserted.

## References

1. Yangshuo He, Guanding Yu and Jingge Zhu, *Task-Oriented Boolean Function Computation: Practical Code Constructions*, arXiv:2610.01228, first submitted 2026-10-01, especially Section III (tagging and finite-blocklength bound): https://arxiv.org/abs/2610.01228.
2. Nathan Kaplan, *MacWilliams Identities for m-Tuple Weight Enumerators*, arXiv:1205.1277, first submitted 2012-05-07, especially Sections 1 and 2: https://arxiv.org/abs/1205.1277.
3. Chao Liu, Hao Chen, Dabin Zheng and Yaqi Chen, *Generalized Hamming Weights and Subcode Support Weight Distributions of Twisted Reed–Solomon Codes*, arXiv:2610.16283, first submitted 2026-10-12, especially Section 4: https://arxiv.org/abs/2610.16283.
