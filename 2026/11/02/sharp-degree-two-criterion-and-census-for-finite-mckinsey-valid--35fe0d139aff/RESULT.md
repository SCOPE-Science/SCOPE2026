# Sharp degree-two criterion and census for finite McKinsey-valid frames

## Finding

Let \(n\geq1\). On a fixed labelled \(n\)-element set \(W\), consider directed Kripke relations \(R\subseteq W\times W\) with every successor set \(R(w)=\{v:wRv\}\) of size at most two (loops allowed). Such a frame validates the McKinsey axiom \(\Box\Diamond p\to\Diamond\Box p\) at every world under every valuation if and only if **every world has a successor with exactly one successor**:

\[
\forall w\in W\quad\exists v\in R(w)\quad |R(v)|=1.
\]

The number \(N_n\) of these labelled relations is exactly

\[
N_n=\sum_{k=1}^{n}\binom nk k^k
\left(\binom n2-\binom{n-k}2\right)^{n-k},
\]

where the term with exponent zero is interpreted as one. In particular
\(N_1,N_2,N_3,N_4,N_5=(1,6,75,1612,52795)\). Write \(W_0\) for the principal real Lambert function, so \(W_0(n)e^{W_0(n)}=n\). The logarithmic asymptotic is

\[
\log N_n=n\log n+nW_0(n)-n+O\left(\frac n{\log n}\right)
=2n\log n-n\log\log n-n+O\left(\frac{n\log\log n}{\log n}\right).
\]

Among all \((1+n+\binom n2)^n\) at-most-two-outdegree frames, the fraction that validates the axiom consequently satisfies

\[
\log\frac{N_n}{(1+n+\binom n2)^n}
=-n\log\log n+(\log2-1)n+O\left(\frac{n\log\log n}{\log n}\right).
\]

The degree-two hypothesis is structurally sharp: an explicit six-world frame of maximum outdegree three validates the axiom although its distinguished world has no successor of outdegree one.

## Assumptions and scope

All Kripke semantics are the usual classical Boolean semantics for one normal modal operator. Frame validity quantifies over every valuation of the propositional letter \(p\) and every world. Relations may have self-loops and need not be transitive, serial, reflexive, symmetric, or weakly transitive. The counting formula fixes all \(n\) distinct vertex labels and counts relations, not isomorphism classes. All logarithms are natural. The first and second asymptotic equalities concern \(n\to\infty\) only; exact counts hold for every integer \(n\ge1\).

## Proof

**1. Local splitting lemma.** For an arbitrary directed frame and a designated world \(w\), the axiom fails at \(w\) under a valuation \(P\subseteq W\) precisely when the sets \(R(v)\), for \(v\in R(w)\), all meet both \(P\) and its complement: the first intersection condition is \(\Box\Diamond p\), and the second ensures that no \(v\in R(w)\) satisfies \(\Box p\). This equivalence also handles empty successor sets: if \(R(w)=\varnothing\), both intersection requirements are vacuous, while \(\Diamond\Box p\) is false, so the axiom fails at \(w\).

Suppose now that the entire frame has maximum outdegree two. If a world \(w\) has a successor \(v\) whose successor set is empty, the antecedent \(\Box\Diamond p\) is false under every valuation and the axiom holds at \(w\). If instead \(w\) has a successor \(v\) with \(R(v)=\{u\}\), then any valuation satisfying \(\Box\Diamond p\) at \(w\) satisfies \(p\) at \(u\), hence \(\Box p\) at \(v\), and thus \(\Diamond\Box p\) at \(w\). Finally, if \(w\) has nonempty successor set and every successor \(v\) has two distinct successors, build the undirected graph whose edges are these \(R(v)\). It has at most two edges, and therefore is bipartite. Its two-color classes define a valuation under which each \(R(v)\) meets both classes. By the splitting equivalence the axiom fails at \(w\).

Thus local validity at \(w\), assuming \(R(w)\ne\varnothing\), is equivalent to having a successor whose outdegree is zero or one. For global validity, no world can have outdegree zero (a dead end itself falsifies the axiom). Therefore, all worlds have positive outdegree and the criterion simplifies exactly to the stated existence of an outdegree-one successor. Conversely that criterion itself implies that no world is a dead end and gives global validity by the preceding argument.

**2. Exact labelled census.** Let \(S=\{v\in W:|R(v)|=1\}\) have cardinality \(k\). Global validity implies \(k\ge1\). For each \(s\in S\), the unique successor must lie in \(S\); otherwise \(s\) would have no outdegree-one successor. This gives \(k^k\) independent choices. Each world outside \(S\) must have exactly two distinct successors and at least one successor in \(S\). Its possible successor sets number

\[
A(n,k)=\binom n2-\binom{n-k}2=\frac{k(2n-k-1)}2.
\]

These choices are independent across the remaining \(n-k\) worlds. Choosing \(S\) in \(\binom nk\) ways and summing proves the formula. The decomposition is unique because \(S\) is recoverable as the set of singleton-successor rows; no relations are counted twice. For \(k=n\), \(n-k=0\) and there are simply \(n^n\) labelled total functions.

**3. Logarithmic asymptotics.** Write \(T_{n,k}=\binom nk k^k A(n,k)^{n-k}\). For \(1\le k\le n\), the elementary estimates \(\binom nk\le(en/k)^k\) and \(A(n,k)\le nk\) give

\[
\log T_{n,k}\le n\log n+k+(n-k)\log k.
\]

The continuous function \(f(k)=k+(n-k)\log k\) on \(1\le k\le n\) is maximized at \(k_*=n/W_0(n)\), since \(f'(k)=n/k-\log k\) and \(f''(k)=-n/k^2-1/k<0\). Its value there is \(nW_0(n)-n+n/W_0(n)\). Summation of at most \(n\) terms yields

\[
\log N_n\le n\log n+nW_0(n)-n+\frac n{W_0(n)}+\log n.
\]

Conversely take \(k=\lfloor n/W_0(n)\rfloor\), for sufficiently large \(n\). Since \(\binom nk\ge(n/k)^k\) and \(A(n,k)\ge k(n-k)\),

\[
\log T_{n,k}\ge n\log n+(n-k)\log k+(n-k)\log(1-k/n).
\]

Here \(k=n/W_0(n)+O(1)\), \(\log k=W_0(n)+O(W_0(n)/n)\), and \((n-k)\log(1-k/n)=O(n/W_0(n))\). Hence the lower bound is \(n\log n+nW_0(n)-n-O(n/W_0(n)+\log n)\). Combining gives the first asymptotic, as \(W_0(n)\sim\log n\). The usual expansion \(W_0(n)=\log n-\log\log n+O(\log\log n/\log n)\) gives the second. Finally \(\log\bigl((1+n+\binom n2)^n\bigr)=2n\log n-n\log2+O(1)\), proving the proportion estimate.

**4. Sharpness at outdegree three.** On the world set \(\{0,1,2,3,4,5\}\), define rows

\[
R(0)=\{1,2,3\},\quad R(1)=\{0,4\},\quad
R(2)=\{4,5\},\quad R(3)=\{5,0\},\quad
R(4)=\{4\},\quad R(5)=\{5\}.
\]

The three neighborhoods \(R(1),R(2),R(3)\) are the edges of a triangle, which has no splitting into two colors meeting every edge. Consequently there is no valuation falsifying the McKinsey axiom at world \(0\). At each of worlds \(1,2,3,4,5\), a singleton-successor world is accessible, so the axiom also holds there. Yet all three successors of \(0\) have outdegree two. This disproves extension of the criterion to maximum outdegree three.

## Verification

A standalone Python checker enumerates every labelled relation with outdegree at most two for carrier sizes \(n=1,2,3,4\). It independently evaluates the axiom under every Boolean valuation at every world, checks agreement with the structural criterion, and compares the result with the exact formula. The accepted counts are \(1,6,75,1612\) among, respectively, \(2,16,343,14641\) possible frames. It additionally verifies directly that the six-world sharpness example validates the axiom while failing the degree-two criterion. The script uses only the Python standard library, and can be executed as `python checker.py`. These finite checks are corroborative; the argument above is the proof for all \(n\).

## Relationship to prior work

Van Benthem, ten Cate and Yang, Section 5.4 and Theorem 26 of arXiv:2603.12171, show that checking the McKinsey axiom on unrestricted finite frames is coNP-complete by translating falsity into set splitting. The local splitting step above adopts that semantic perspective but uses the two-edge limit to obtain a sharp first-order-style structural condition, followed by a full labelled enumeration and asymptotics; those quantitative conclusions are not in their stated theorem. Chen and Ma (2024), *The McKinsey Axiom on Weakly Transitive Frames*, show that on the different, overlapping class of weakly transitive frames global validity is equivalent to Lemmon's singleton-or-terminal-successor condition. The present claim does not assert that observation is new on the weakly transitive subclass. It instead applies to arbitrary degree-two directed frames without a weak-transitivity assumption, supplies a counting theorem, and exhibits the precise failure at degree three. The scope differences must be maintained when assessing historical priority.

## Limitations

The classification does not characterize arbitrary frames, maximum-outdegree-three frames, or unlabelled isomorphism classes. It counts graphs permitting loops and with no additional modal frame axioms. The logarithmic asymptotic is not an asymptotic with a determined multiplicative constant. Exhaustive checker computations terminate at \(n=4\), and do not certify the arbitrary-size claims. Earlier unindexed work may contain an equivalent degree-bounded statement or count, so publication priority is not independently established. No external/independent audit has been performed.

## References

1. Johan van Benthem, Balder ten Cate, Xi Yang, *When do modal definability and preservation theorems transfer to the finite?*, arXiv:2603.12171v1, first submitted 12 March 2026, especially Section 5.4 and Theorem 26. https://arxiv.org/html/2603.12171v1
2. Qian Chen and Minghui Ma, *The McKinsey Axiom on Weakly Transitive Frames*, *Studia Logica* 113 (2025), 1543–1566; original 2024 DOI 10.1007/s11225-024-10145-x. https://doi.org/10.1007/s11225-024-10145-x
