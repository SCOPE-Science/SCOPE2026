# Fibonacci census and geometric recovery-duality law for finite prelinear quasi-Nelson chains

## Finding

Write \(F_0=0\), \(F_1=1\), and \(F_{j+2}=F_{j+1}+F_j\). For every integer \(n\ge2\), consider the nontrivial prelinear quasi-Nelson algebras whose lattice order is a chain with \(n\) elements, in the bounded commutative integral residuated-lattice signature. Isomorphism is in the full algebraic signature. Every such algebra admits a unique maximum-consistency operator \(\circ\) and a unique minimum-undeterminedness operator \(\bullet\). Define its recovery-duality defect by
\[
J(A)=\bigl|\{x\in A:\bullet x\ne\neg\circ x\}\bigr|,
\]
where \(\neg x=x\to0\).

**Exact classification.** The number of isomorphism classes of \(n\)-element prelinear quasi-Nelson chains, with or without their uniquely determined recovery operators, is exactly \(F_n\). For \(n\ge3\) and \(0\le j\le n-2\), the number with \(J(A)=j\) is
\[
 c_{n,j}=\begin{cases}
  F_{n-2-j},&0\le j\le n-3,\\
  1,&j=n-2.
 \end{cases}
\]
Thus \(F_{n-2}\) chains have dual recoveries and \(F_{n-1}\) have nondual recoveries when \(n\ge3\). The two-element chain has defect zero.

**Limiting law.** Choose one of these \(F_n\) isomorphism classes uniformly and denote the defect by \(J_n\). With \(\varphi=(1+\sqrt5)/2\), for every fixed integer \(j\ge0\),
\[
\lim_{n\to\infty}\Pr(J_n=j)=\varphi^{-(j+2)}.
\]
This is a probability distribution on the nonnegative integers. In particular, the limiting proportion of dual-recovery chains is \(\varphi^{-2}\), while the limiting nondual proportion is \(\varphi^{-1}\). The limiting geometric law has mean \(\varphi\) and variance \(\varphi^3\). These are limits under *uniform sampling of full algebra isomorphism classes*, not of all binary tables or all labelled relational models.

## Assumptions and scope

Represent the unique \(n\)-element bounded chain as \(C_n=\{0,1,\ldots,n-1\}\), with its displayed integer order and with top \(T=n-1\). A weak negation is an order-reversing map \(d:C_n\to C_n\) satisfying \(d(T)=0\) and \(d(d(x))\ge x\) for every \(x\). These conditions force \(d(0)=T\). Define
\[
 x\mathbin{*}y=\begin{cases}0,&x\le d(y),\\ \min(x,y),&x>d(y),\end{cases}
\qquad
 x\to y=\begin{cases}T,&x\le y,\\ \max(d(x),y),&x>y.\end{cases}
\]
Meet, join, and constants are those of the chain. These operations give precisely the finite weak-nilpotent-minimum chains, and \(d(x)=x\to0\). A prelinear quasi-Nelson chain is one additionally satisfying the Nelson equation
\[
 \bigl(((x*x)\to y)\wedge(((\neg y)*(\neg y))\to\neg x)\bigr)
 \to(x\to y)=T
\]
for all \(x,y\). This is the algebraic translation of the Nelson axiom in the cited primary literature.

The maximum-consistency operator on a chain is \(\circ x=T\) exactly when \(x\wedge\neg x=0\), and zero otherwise. The minimum-undeterminedness operator is \(\bullet0=\bullet T=0\) and \(\bullet x=T\) for every \(0<x<T\). The latter two descriptions agree with the unique operators characterized in the motivating recovery-operator paper. The statement concerns these precise two operators, not arbitrary weaker recovery connectives.

## Proof

**1. Reduction to weak negations.** In a bounded commutative integral residuated chain, the weak-nilpotent-minimum equation says
\[
 (x*y\to0)\vee((x\wedge y)\to(x*y))=T.
\]
Because the lattice is a chain, one of the two implications equals \(T\); thus \(x*y\) is either zero or \(\min(x,y)\). The residual negation \(d(y)=y\to0\) is antitone, and residuation gives \(d(d(y))\ge y\). Furthermore, \(x*y=0\) exactly when \(x\le d(y)\). Conversely, every weak negation produces the displayed operation: the condition \(x>d(y)\) is equivalent to \(y>d(x)\), by antitonicity and double-negation inflation. The nonzero product is the minimum, so iterated products are nonzero exactly when all participating pairs are compatible; hence multiplication is associative. It is monotone, commutative, and has unit \(T\). Its finite residuum is exactly the displayed implication; this follows by maximizing the \(z\) with \(x*z\le y\). It therefore satisfies the required bounded residuated-lattice and weak-nilpotent-minimum equations.

**2. Exact Nelson criterion.** A weak negation \(d\) satisfies the Nelson equation precisely when
\[
 \tag{N}\forall x\in\{1,\ldots,n-2\}:\quad x\le d(x)\ \Longrightarrow\ d(x-1)>d(x).
\]
To verify this equivalence, the Nelson equation is automatic if \(x\le y\), or if \(x>y\) and \(x>d(x)\), since then \(x*x=x\). In the remaining case \(x>y\), \(x\le d(x)\), the first conjunct on the left is \(T\) and \(x\to y=d(x)\). Because \(d\) is antitone, \(d(y)\ge d(x)\). If equality holds, \((d(y)*d(y))\to d(x)=T\), so the equation fails: \(d(x)<T\) for positive \(x\), by double-negation inflation. If \(d(y)>d(x)\), antitonicity and \(x\le d(x)\) give
\[
 d(d(y))\le d(d(x))\le d(x)<d(y).
\]
Therefore \(d(y)*d(y)=d(y)\), and \((d(y)*d(y))\to d(x)=d(x)\), exactly as required. Thus the equation holds iff \(d(y)>d(x)\) for all \(0\le y<x\le d(x)\). Since \(d\) is nonincreasing, consecutive strictness (N) is equivalent to all these inequalities. The case \(y=0\) is automatic.

**3. Fibonacci decomposition.** Let \(p_n\) be the number of weak negations satisfying (N) on \(C_n\). The base cases are \(p_2=1\) and \(p_3=2\). For \(n\ge4\), put \(r=d(1)\). Double-negation inflation forces \(r\le n-2\). There are two disjoint cases.

If \(r\le n-3\), then \(d(n-2)=0\); otherwise the positive integer \(d(n-2)\) would satisfy \(d(d(n-2))\le d(1)=r<n-2\). Deleting the penultimate point and replacing the former top by the new top transforms
\[
 (n-1,d(1),\ldots,d(n-3),0,0)
 \longleftrightarrow
 (n-2,d(1),\ldots,d(n-3),0).
\]
The weak-negation inequalities and (N) are preserved in both directions, so this case is in bijection with the admissible maps on \(C_{n-1}\).

If \(r=n-2\), then double-negation inflation gives \(d(n-2)\ge1\). Suppose it were at least two. With \(z=d(n-2)\ge2\), we would have \(d(z)\ge n-2\), and antitonicity would force \(d(z)=d(1)=n-2\). But \(z\le d(z)\) would then contradict (N). Hence \(d(n-2)=1\), and (N) also forces \(1\le d(i)\le n-3\) for \(2\le i\le n-3\). Remove the paired points \(1\) and \(n-2\), and reindex the remaining points by subtracting one from each old interior index and each positive interior output. Explicitly, the resulting weak negation \(e\) on \(C_{n-2}\) has
\[
 e(0)=n-3,\quad e(n-3)=0,\quad
 e(j)=d(j+1)-1\qquad(1\le j\le n-4).
\]
Conversely, from any admissible \(e\) on \(C_{n-2}\), set
\[
 d(0)=n-1,\quad d(1)=n-2,\quad d(n-2)=1,\quad d(n-1)=0,
 \quad d(i)=e(i-1)+1\quad(2\le i\le n-3).
\]
Checking separately whether \(e(j)=0\) proves double-negation inflation; checking whether \(j\le e(j)\) proves (N). Thus this case is in bijection with the admissible maps on \(C_{n-2}\). Consequently \(p_n=p_{n-1}+p_{n-2}\), and the base cases give \(p_n=F_n\). Any chain isomorphism preserves the linear ordering, so different displayed negations define nonisomorphic full algebras.

**4. Exact recovery defect.** For \(r=d(1)\), the weak-negation inequalities give \(d(i)>0\) exactly when \(1\le i\le r\), while \(d(i)=0\) when \(i>r\). Indeed, for \(r>0\) the inequality \(d(r)\ge1\) follows from \(d(d(1))\ge1\), and for \(i>r\) a positive \(d(i)\) would imply \(d(d(i))\le d(1)=r<i\). Hence the explosive elements are exactly \(\{0,r+1,\ldots,n-1\}\). For each interior element, \(\bullet x=T\) and \(\neg\circ x\) equals zero if and only if that element is explosive. Thus
\[
 J=n-2-r.
\]
At fixed \(r\ge1\), repeatedly use the first branch of the Fibonacci decomposition until the resulting chain has exactly \(r+2\) elements, then use its second branch. This gives \(F_r\) possibilities (including \(r=1\), where the sole possibility is explicit). For \(r=0\), there is exactly one map, \(d=(n-1,0,\ldots,0)\). Substituting \(r=n-2-j\) gives the stated exact distribution. Its zero-defect and positive-defect counts sum to \(F_n\), with the stated \(n=2\) boundary case.

**5. Limit.** Binet's Fibonacci formula implies \(F_{n-2-j}/F_n\to\varphi^{-(2+j)}\) for each fixed \(j\). The limiting masses sum to one because \(1-\varphi^{-1}=\varphi^{-2}\). Pointwise convergence to a distribution of total mass one implies convergence in distribution here. The standard geometric series gives the stated mean and variance of the limiting law. No moment convergence of \(J_n\) is needed for this conclusion.

## Verification

The accompanying standalone `checker.py` enumerates all antitone weak negations on \(C_n\) and separately computes products, finite residua, and the original Nelson axiom, without using (N) as the acceptance test. It then compares that original axiom with (N), verifies associativity and residuation, and recomputes all defects directly from the two unary recovery operations. For every \(2\le n\le11\), it confirms \(p_n=F_n\) and every cell of the proposed defect distribution. Execute with `python checker.py` in the directory containing the file. The run returns `ALL_CHECKS_OK`. The unrestricted result is proved symbolically above; finite verification is not presented as a proof at larger orders.

## Relationship to prior work

Flaminio, Godo, and Rivieccio (2026) introduce and analyze consistency/undeterminedness expansions of prelinear quasi-Nelson algebras. Their Sections 3 and 4 identify the unique recovery operations on chains, and Section 5 studies their possible interactions and failures of duality. These are the algebraic definitions used here. The present result instead counts the finite chain structures and quantifies their duality defects exactly and asymptotically; this enumeration is not asserted in the inspected sections of that paper.

Flaminio and Rivieccio (2022) establish the underlying prelinear quasi-Nelson variety and describe its twist-structure and standard-chain semantics. Its repository abstract was accessible, but a full manuscript fetch was not, leaving a residual priority risk for equivalent finite enumerations. Noguera, Esteva, and Gispert (2008) study weak-nilpotent-minimum chains and their negation representation; this is broader than the present Nelson-restricted enumeration and does not by itself state the Fibonacci defect law in the inspected material. Standard Fibonacci and geometric-distribution identities are background tools, not claimed as new mathematics.

## Limitations

The finite classification is for **totally ordered** nontrivial prelinear quasi-Nelson algebras only; it does not count products, arbitrary nonchain algebras, or all possible non-maximal recovery operators. The distribution samples isomorphism classes uniformly, not homomorphisms or algebra terms. No claim of absolute literature priority or independent review is made. Equivalence to an older classification under different terminology remains possible, notably in work on prelinear twist structures. The checked finite computations stop at eleven elements.

## References

1. T. Flaminio, L. Godo and U. Rivieccio, *Recovery operators in quasi-Nelson logic: the prelinear case* (2026), arXiv:2606.31277, first arXiv posting 2026-06-30. https://arxiv.org/abs/2606.31277 ; full HTML https://arxiv.org/html/2606.31277 . Relevant sections: 2.1, 3, 4, 5.
2. T. Flaminio and U. Rivieccio, *Prelinearity in (quasi-)Nelson logic*, Fuzzy Sets and Systems 445 (2022), 66–89. DOI:10.1016/j.fss.2022.03.021. Repository record: https://espacio-pre.uned.es/entities/publication/90518e23-0177-4f45-99ec-7bd1258c0689 . Full text was not accessible for a definitive priority comparison.
3. C. Noguera, F. Esteva and J. Gispert, *On triangular norm based axiomatic extensions of the Weak Nilpotent Minimum logic*, Mathematical Logic Quarterly 54 (2008), 387–409. DOI:10.1002/malq.200710054. Author manuscript: https://usiena-air.unisi.it/retrieve/e0feeaab-8738-44d2-e053-6605fe0a8db0/draft10.pdf .
