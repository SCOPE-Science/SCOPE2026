# Baire-Class-One Join and Sharp Discontinuity for Equational-Theory Spaces

## Finding

Let \(\Sigma\) be any countable algebraic signature, let \(\mathrm{Eq}_\Sigma\) be its countable set of equations, and let \(\mathscr E_\Sigma\subseteq 2^{\mathrm{Eq}_\Sigma}\) be the space of equational theories with the subspace product topology. The join operation

\[J(\Phi,\Psi)=\operatorname{Th}(\Phi\cup\Psi)\]

is of Baire class one: it is a pointwise limit of continuous maps. It is not continuous, even when \(\Sigma\) consists of a single unary function symbol.

## Assumptions and scope

A theory is coded by the set of equations it contains. Basic open sets specify membership or non-membership of finitely many equations. For a set of equations \(S\), \(\operatorname{Th}(S)\) denotes the least equational theory containing \(S\). The result assumes ordinary finitary equational logic and a countable signature. No claim is made for uncountable signatures or for continuity at every individual input pair.

## Proof

Enumerate the equations as an increasing exhaustion by finite sets \(E_0\subseteq E_1\subseteq\cdots\), with union \(\mathrm{Eq}_\Sigma\). Define

\[J_m(\Phi,\Psi)=\operatorname{Th}\big((\Phi\cap E_m)\cup(\Psi\cap E_m)\big).\]

For each fixed \(m\), the value of \(J_m\) depends only on the finitely many membership bits indexed by \(E_m\). It therefore has finite range and is continuous. Equational consequence is finitary: if an equation \(e\) belongs to \(J(\Phi,\Psi)\), a finite derivation uses only finitely many premises from \(\Phi\cup\Psi\), and all those premises occur in \(E_m\) for sufficiently large \(m\). Thus \(e\in J_m(\Phi,\Psi)\) eventually. If \(e\notin J(\Phi,\Psi)\), then \(e\notin J_m(\Phi,\Psi)\) for every \(m\), since each approximating premise set is a subset of \(\Phi\cup\Psi\). Hence \(J_m(\Phi,\Psi)\to J(\Phi,\Psi)\) in the product topology for every pair, proving that \(J\) is Baire class one.

For discontinuity, use the signature with one unary function \(f\). For each integer \(n\ge2\), let \(T_n=\operatorname{Th}(f^n(x)\approx x)\), and let \(T_{\mathrm{triv}}\) be the equational theory of all unary algebras, containing only universally valid identities. Every term is of the form \(f^a(x_i)\). For an identity involving different variables, a model with two disjoint \(n\)-cycles refutes it. For \(f^a(x)\approx f^b(x)\) with \(a\ne b\), validity in all models of \(f^n(x)=x\) holds exactly when \(n\) divides \(|a-b|\). A fixed nonzero integer has only finitely many positive divisors, so every nontrivial equation is eventually absent from \(T_n\); therefore \(T_n\to T_{\mathrm{triv}}\).

Put \(\Psi=\operatorname{Th}(f^2(x)\approx f(x))\). In every model of \(\Psi\), idempotence gives \(f^n(x)=f(x)\) for all \(n\ge1\). Combining this with \(T_n\) forces \(f(x)=x\), so \(f(x)\approx x\) belongs to \(J(T_n,\Psi)\) for every \(n\ge2\). But \(J(T_{\mathrm{triv}},\Psi)=\Psi\) does not contain that equation: a nonidentity constant map on a two-element set is idempotent. Thus the indicated output coordinate fails to converge along \(T_n\to T_{\mathrm{triv}}\), proving that \(J\) is discontinuous.

## Verification

The approximation argument checks each equation coordinate and uses only finite-premise equational derivations. In the witness, the unary terms are exactly the iterates \(f^a(x_i)\); the divisibility test is both necessary (an \(n\)-cycle witnesses failure) and sufficient (every map with \(f^n=\mathrm{id}\) has period dividing \(n\)). The discontinuity witness is an explicit model-theoretic counterexample, not a finite search or an asymptotic inference.

## Relationship to prior work

Aguilera, Bezhanishvili, and Takahashi code equational theories as reals and prove that intervals of equational theories in a countable language are \(\Pi^0_1\) classes, yielding a countability-or-continuum dichotomy. Their paper also records the finitary closure rules for equational theories. Those results motivate the topology used here but do not state a regularity theorem for the join map or give the unary-function discontinuity witness. The present result concerns the operation on the theory space, rather than the cardinality of a fixed interval.

## Limitations

The proof depends on the finitary character of equational consequence and countability of the equation set. It establishes Baire class one globally and discontinuity somewhere, but it does not classify the continuity points of the join map or determine a sharper pointwise oscillation invariant.

## References

1. J. P. Aguilera, N. Bezhanishvili, and T. Takahashi, “The Cardinalities of Intervals of Equational Theories and Logics,” arXiv:2603.27203, first posted 2026-03-28. https://arxiv.org/abs/2603.27203
