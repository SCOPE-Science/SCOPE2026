# Uniform finite satisfiability gaps for every equation of bounded commutative BCK-algebras

## Finding
For every integer \(k\geq 1\), every equation \(t(x_1,\ldots,x_k)=s(x_1,\ldots,x_k)\) of the bounded commutative BCK-algebra language \((\cdot,0,1)\) has a **finite satisfiability gap** among finite bounded commutative BCK-algebras: there exists \(\varepsilon>0\), depending on the equation but not on the algebra, such that its degree of satisfiability is either \(1\) or at most \(1-\varepsilon\).

This gap has a fully quantitative form. If the equation fails in the \(n_0\)-element standard commutative BCK chain \(C_{n_0}\), with \(n_0\geq2\), and the two terms together contain \(L\geq1\) variable occurrences, then one may take
\[
\boxed{\varepsilon=\bigl(16L(n_0-1)\bigr)^{-k}.}
\]
In particular **every** equation in any fixed finite number of variables has such a gap, rather than only the particular excluded-middle, positive-implicativity and implicativity identities previously studied. This is a uniform dichotomy, not an assertion that all equations are identities.

## Assumptions and scope
The operation is the BCK subtraction \(a\cdot b\), and bounded commutative BCK-algebras include designated least and greatest elements \(0,1\). In the standard real model the operation is \(a\cdot b=\max\{a-b,0\}\). The finite \(n\)-element chain is the grid \(C_n=\{0,1/(n-1),\ldots,1\}\) under this operation. Variables are independently uniformly sampled with replacement. All finite bounded commutative BCK-algebras, including finite direct products of chains, are in scope; arbitrary noncommutative or unbounded BCK-algebras are not. An equation in zero variables is trivially either universally valid or universally false and is excluded from the quantitative formula. If \(L=0\) then the terms are constant and the gap assertion is immediate.

For a finite algebra \(A\), write \(d_A(t=s)\) for the number of satisfying ordered \(k\)-tuples divided by \(|A|^k\). A finite satisfiability gap means there exists \(\varepsilon>0\) with \(d_A(t=s)\in\{1\}\cup[0,1-\varepsilon]\) for every such \(A\).

## Proof
**Finite-chain reduction.** The standard finite-structure theorem identifies every finite bounded commutative BCK-algebra with a finite direct product of the standard chains \(C_n\); equivalently, bounded commutative BCK-algebras are the MV-algebras, and finite MV-algebras are products of finite Łukasiewicz chains. For each equation, degrees of satisfiability multiply under finite direct products, since the equation holds componentwise. It therefore suffices to find a common gap over individual chains. If an equation fails in any finite algebra, it fails in a chain factor; select any such \(C_{n_0}\).

**Lipschitz bound.** For a term \(v\), let \(\ell(v)\) count variable occurrences, with multiplicity. The term operation on \([0,1]^k\) satisfies
\[
|v(\mathbf{x})-v(\mathbf{y})|\leq \ell(v)\|\mathbf{x}-\mathbf{y}\|_\infty.
\]
Induction proves this: constants have Lipschitz constant zero, variables one, and the function \((a,b)\mapsto\max\{a-b,0\}\) is Lipschitz in its arguments with the sum of their individual changes. Hence \(h=t-s\) is \(L=\ell(t)+\ell(s)\)-Lipschitz.

**A robust rational counterexample.** Choose a violating \(\mathbf{u}\in C_{n_0}^k\). All term values at \(\mathbf{u}\) are integer multiples of \(1/(n_0-1)\), so \(|h(\mathbf{u})|\geq1/(n_0-1)\). Put \(Q=L(n_0-1)\geq1\) and \(\delta=1/(4Q)\). For every \(\mathbf{x}\) with \(\|\mathbf{x}-\mathbf{u}\|_\infty\leq\delta\), the Lipschitz estimate gives \(|h(\mathbf{x})|\geq3/(4(n_0-1))>0\). Choose in each coordinate a one-sided interval of length \(\delta\) with one endpoint at \(u_i\) and wholly inside \([0,1]\). Their Cartesian product \(B\) is a violating box of volume \(\delta^k\).

**Uniform counting on every finite chain.** Consider \(C_n\). If \(n-1\geq2/\delta=8Q\), each interval of length \(\delta\) contains at least \((n-1)\delta-1\geq(n-1)\delta/2\) grid points. Dividing by \(n\) gives a fraction at least \(\delta/4\) in each coordinate, hence at least \((\delta/4)^k=(16Q)^{-k}\) of all tuples violate the equation. If \(n-1<8Q\) and any tuple violates, at least one of the \(n^k\) tuples does, so the violating fraction is at least \(n^{-k}\geq(8Q+1)^{-k}\geq(16Q)^{-k}\). If no tuple violates, its degree is \(1\). Therefore every chain has either full satisfaction or degree at most \(1-(16Q)^{-k}\), with the same constant. Finally, the product of chain degrees is either \(1\) or at most this upper bound, completing the proof.

**Effective form.** Given a concrete chain witness and the term syntax, the displayed gap is an explicit rational number. Existence of a chain witness for every equation that fails on the standard continuum also follows directly from continuity and density of finite rational grids; one does not need this stronger existence assertion for the finite-algebra theorem.

## Verification
The standalone file `verify.py` enumerates all evaluations of the positive-implicativity equation \((x\cdot y)\cdot y=x\cdot y\) on chains with \(2\leq n\leq50\). It confirms that the first violating chain has size \(3\), exactly one of its nine input pairs violates, and every checked violating chain respects the bound \(\varepsilon=1/25600\) obtained from \(k=2\), \(n_0=3\), and \(L=5\). The finite tests illustrate the theorem but cannot replace its general argument.

## Relationship to prior work
C. Matthew Evans, *Satisfiability degrees for BCK-algebras*, arXiv:2209.13704 (first public 2022-09-27), proves finite satisfiability gaps for specific identities and supplies a sufficient condition in Theorem 3.2, based on attainment of a maximum nonunit chain satisfiability degree. Remark 4.4 discusses the lack of a characterization of formulas with a finite gap in the bounded commutative setting. The argument here does not assume that the maximum is attained; it gives a uniform explicit estimate for arbitrary term equations in every arity. The MV-algebra term-equivalence and finite-chain product structure are pre-existing facts, not claimed here. The general degree-of-satisfiability framework and the contrast with Heyting-algebra behavior are likewise due to Bumpus and Kocsis, arXiv:2110.11515.

## Limitations
This is an existence and explicit lower-bound result for a fixed equation, not a sharp best-gap calculation. The constant can be very small. It excludes relations with quantifiers, quasi-identities, variable-dependent equations, noncommutative BCK-algebras, and arbitrary infinite algebras. Finite computational examples are only corroborative. A possible earlier formulation in MV-algebra probability or logic literature remains a priority risk; no claim of independently certified novelty or external verification is made.

## References
1. C. M. Evans, *Satisfiability degrees for BCK-algebras*, arXiv:2209.13704, first publicly posted 2022-09-27; especially Theorem 2.2, Lemma 3.1, Theorem 3.2 and Remark 4.4.
2. M. Abbadini, P. Jipsen, T. Kroupa, and S. Vannucci, *A finite axiomatization of positive MV-algebras*, arXiv:2112.03190, first publicly posted 2021-12-06 (supporting MV background only).
3. B. M. Bumpus and Z. A. Kocsis, *Degree of satisfiability in Heyting algebras*, arXiv:2110.11515, first publicly posted 2021-10-21 (the earlier degree-of-satisfiability framework).
