# Scientific review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The argument was checked at each implication and at the inheritance/complementability points that are easy to overstate.

First, a strictly singular operator fixes no copy of \(c_0\). By the classical Bessaga--Pełczyński theorem, this makes it unconditionally converging. Pfitzner's theorem that C*-algebras have Pełczyński property (V) therefore implies weak compactness.

Second, Akemann--Wright's Theorem 3.3 was inspected in the primary 1979 paper: a weakly compact derivation is \(\operatorname{ad}d\) with \(d\) in a restricted direct sum of pairwise orthogonal ideals \(I_n\cong K(H_n)\). If every nonzero component belongs to a finite-dimensional \(I_n\), the partial inner derivations have finite-dimensional range and converge in operator norm, so the derivation is compact. Hence a weakly compact noncompact derivation has a nonzero component \(k\in K(H)\) with \(H\) infinite-dimensional.

Third, for a unit vector \(y\) with \(a=\|k^*y\|>0\), compactness of \(k\) gives a finite-codimensional \(M\subset H\) with \(\|k|_M\|<a/2\). On the rank-one fiber \(\theta_{x,y}\),
\[
[k,\theta_{x,y}]=\theta_{kx,y}-\theta_{x,k^*y},
\]
so \(\|[k,\theta_{x,y}]\|>(a/2)\|x\|\) for \(x\in M\). Choosing a separable infinite-dimensional closed \(M_0\subset M\) yields an \(\ell_2\) witness.

Complementability was checked explicitly rather than inferred from a basis. If \(p=\theta_{y,y}\), right multiplication by \(p\) is a norm-one projection from \(A\) onto \(Ap=I_np\cong H\). Orthogonal projection of \(H\) onto \(M_0\) induces a norm-one projection of \(Ap\) onto the rank-one witness, so the witness is 1-complemented in \(A\).

For non-weakly-compact derivations, property (V) gives the complementary branch: non-weak compactness forces failure of unconditional convergence, hence a fixed copy of \(c_0\).

Finally, the implications compact \(\Rightarrow\) finitely strictly singular \(\Rightarrow\) strictly singular are standard for Banach-space operators. No approximation-property assumption is needed for compact \(\Rightarrow\) FSS.

## Originality

**PASS, to the best of our knowledge.** The main prior results were separated from the claimed contribution.

- Akemann--Wright (1979), inspected at theorem/proof level, characterize compact and weakly compact derivations on C*-algebras. Their Theorem 3.3 is a principal input here.
- Pfitzner (1994) proved property (V) for C*-algebras. Krulišová (2017) explicitly states this theorem and gives a quantitative strengthening.
- Lindström--Saksman--Tylli (2005) and Mathieu--Tradacete (2020) study strict singularity of multiplication operators on spaces of operators. Their stated results are adjacent but do not identify the derivation-specific collapse claimed here.
- General strict-singularity and property-(V) theory supplies the classical implication from strict singularity to weak compactness for operators with C*-algebra domain.

Searches using the phrases and variants "strictly singular derivation", "finitely strictly singular derivation", "strictly singular inner derivation", "commutator strictly singular", "weakly compact derivation strictly singular", and combinations with C*-algebra terminology did not locate an exact statement of
\[
\delta\in\mathcal{SS}\iff\delta\in\mathcal{FSS}\iff\delta\in\mathcal K
\]
for derivations \(A\to A\), nor the two-branch fixed-copy statement.

The originality risk is not zero. The conclusion is a short synthesis of two classical structural theorems plus a rank-one argument, so it could appear as an unadvertised corollary in older derivation, elementary-operator, or Banach-operator-ideal literature. Pfitzner's 1994 article itself was not exhaustively read for derivation-specific consequences, and the 2005/2020 multiplication papers were not exhaustively checked line by line. No concrete evidence of prior coverage was found.

## Value

**PASS.** Weakly compact and compact derivations are classically different: a nonzero compact implementer on an infinite-dimensional elementary ideal gives a weakly compact, generally noncompact commutator. The theorem pinpoints strict singularity exactly at the compact boundary despite that gap.

The proof also gives structural information stronger than a yes/no equivalence. Every noncompact derivation has a canonical kind of infinite-dimensional witness: a copy of \(c_0\) if weak compactness already fails, or a 1-complemented Hilbert subspace if weak compactness holds. The rank-one fiber mechanism can be reused whenever compact commutator components occur inside an elementary ideal.

## Scientific limitations

The theorem concerns derivations \(A\to A\). Derivations into general Banach \(A\)-bimodules need not admit the Akemann--Wright structure used here. The witness dichotomy is isomorphic, not quantitative in terms of a global norm or essential norm of \(\delta\). Originality remains to the best of our knowledge, with the older derivation and elementary-operator literature as the main residual risk.
