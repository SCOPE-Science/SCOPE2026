# Exact failure counts and width-depth transition for nested Sasaki weakening

## Finding

Let \(m\ge 2\) be even. Let \(H_m\) be the height-two orthomodular lattice with bottom \(0\), top \(1\), and \(m\) atoms paired by a fixed-point-free orthocomplement \(a\mapsto a^\perp\). Thus \(H_m\) is the horizontal sum of \(m/2\) four-element Boolean algebras; its cardinality is \(m+2\). Implication is the Sasaki hook \(x\to_S y=x^\perp\vee(x\wedge y)\).

For each integer \(d\ge1\), define the right-associated nested weakening formula
\[
W_d(p_0,\ldots,p_d)=p_0\to_S\bigl(p_1\to_S(\cdots(p_d\to_S p_0)\cdots)\bigr).
\]
An assignment is a *failure* if the value of this formula is not \(1\). We count assignments to the \(d+1\) distinct variables; the second appearance of \(p_0\) has its previously assigned value.

**Exact full-valuation census.** Among the \((m+2)^{d+1}\) assignments with every variable ranging over \(H_m\), the number of failures is
\[
F_{\mathrm{full}}(m,d)=m^{d+1}-m^d-m2^{d-1}.
\]
**Exact atomic-valuation census.** Among the \(m^{d+1}\) assignments with every variable ranging over atoms, the number of failures is
\[
F_{\mathrm{atom}}(m,d)=(m-1)^{d+1}+(-1)^d-\frac m2(1+(-1)^d).
\]
Both expressions are nonnegative integers and hold including the Boolean boundary \(m=2\), where they vanish identically.

**Width-depth transition.** Let even integers \(m\to\infty\) and positive integers \(d=d(m)\) obey \(d/m\to t\) in the extended interval \([0,\infty]\). Under independent uniform sampling of the indicated variables, the respective failure probabilities converge to
\[
\Pr_{\mathrm{full}}(W_d\ne1)\longrightarrow e^{-2t},\qquad
\Pr_{\mathrm{atom}}(W_d\ne1)\longrightarrow e^{-t},
\]
where both limiting expressions are interpreted as zero at \(t=\infty\). In particular, fixed positive depth and increasing width give failure probability tending to one, whereas at each fixed width the failure probability tends to zero with depth. These are combinatorial uniform-valuation probabilities, not physical state probabilities.

## Assumptions and scope

Every pair of distinct atoms in \(H_m\) has meet \(0\) and join \(1\). Each atom \(a\) has a unique distinct partner \(a^\perp\), and \(0^\perp=1\). Since the only proper order relations are \(0<a<1\), orthomodularity follows directly. This construction exists for every even \(m\ge2\), with a specified atom-complement pairing; the formulas do not depend on how the atoms are labelled or paired. We do not identify assignments under automorphisms.

In the term \(W_d\), all \(p_i\) are distinct variables for \(0\le i\le d\), except the deliberate reuse of \(p_0\) at the rightmost end. For the full model the variables are independent uniform elements of \(H_m\); for the atomic model they are independent uniform atoms. The designation *failure* is specific to this formula's evaluation and is not a measure of truth in an external quantum-mechanical state.

## Proof

**Step 1: evaluate the hook.** Directly from the lattice operations,
\[
0\to_S y=1,\qquad 1\to_S y=y.
\]
For an atom \(a\),
\[
a\to_S y=\begin{cases}1&y=1\text{ or }y=a,\\a^\perp&\text{otherwise.}\end{cases}
\]
If \(p_0=0\), the outer hook gives \(1\). If \(p_0=1\), the innermost hook has consequent \(1\), so all hooks up to the root also yield \(1\). Thus every failure has \(p_0\) atomic.

**Step 2: transfer from the rightmost end.** Fix \(p_0=a\) atomic and set \(y_0=a\). Recursively set \(y_j=p_{d-j+1}\to_S y_{j-1}\) for \(1\le j\le d\). Once the state reaches \(1\), all remaining hooks keep it at \(1\). From any atomic state \(y\), the next hook is either \(1\) or another atom, never \(0\). The final formula \(a\to_S y_d\) fails precisely when \(y_d\) is an atom distinct from \(a\).

Index the \(m\) atoms and let \(P\) be the permutation matrix sending each atom to its orthocomplement, and \(J\) the all-ones matrix. In the **full** ensemble, the atom-to-atom count matrix is
\[
K_{\mathrm{full}}=J+I-P.
\]
Indeed, each atom \(y\) has two inputs producing state \(y\) (the inputs \(1\) and \(y^\perp\)), no inputs producing \(y^\perp\), and one input producing each of the other \(m-2\) atoms; the two inputs \(0\) and \(y\) produce \(1\). Every row sum of \(K_{\mathrm{full}}\) is \(m\), whereas the two top-producing choices account for the remainder of the \(m+2\) inputs.

In the **atomic** ensemble, the matrix instead is
\[
K_{\mathrm{atom}}=J-P.
\]
Here the input \(y\) produces \(1\); among the other \(m-1\) inputs, exactly one produces each atom other than \(y^\perp\), including \(y\) itself. Every row sum is \(m-1\).

**Step 3: diagonalize without approximations.** Define
\[
U=J/m,\qquad V=(I-P)/2,\qquad S=(I+P)/2-U.
\]
As \(P^2=I\), \(P\mathbf1=\mathbf1\), and \(m\) is even, these are pairwise annihilating idempotents with sum \(I\), and every diagonal entry of \(U\), \(V\), \(S\) equals respectively \(1/m\), \(1/2\), \(1/2-1/m\). One has
\[
K_{\mathrm{full}}=mU+2V,\qquad
K_{\mathrm{atom}}=(m-1)U+V-S.
\]
Consequently for all integers \(d\ge1\),
\[
(K_{\mathrm{full}}^d)_{aa}=m^{d-1}+2^{d-1},
\]
and
\[
(K_{\mathrm{atom}}^d)_{aa}=\frac{(m-1)^d-(-1)^d}{m}
+\frac{1+(-1)^d}{2}.
\]
Since an atom row of \(K_{\mathrm{full}}^d\) sums to \(m^d\), and an atom row of \(K_{\mathrm{atom}}^d\) sums to \((m-1)^d\), the number of failure assignments for each fixed initial atom is the respective row sum minus its diagonal entry. Multiplication by the \(m\) choices of \(p_0=a\) proves both exact census formulas. In particular the Boolean case \(m=2\) is included without extrapolating from experiments.

**Step 4: critical scaling.** For full valuations, divide the exact count by \((m+2)^{d+1}\) to obtain
\[
\left(\frac{m}{m+2}\right)^{d+1}
\left(1-\frac1m-\frac{2^{d-1}}{m^d}\right).
\]
For atomic valuations, dividing by \(m^{d+1}\) gives
\[
\left(1-\frac1m\right)^{d+1}
+\frac{(-1)^d-(m/2)(1+(-1)^d)}{m^{d+1}}.
\]
As even \(m\to\infty\), the parenthetic full-model correction tends uniformly to \(1\) for all \(d\ge1\), and the atomic correction tends uniformly to zero. If \(d/m\to t<\infty\), the leading factors tend to \(e^{-2t}\) and \(e^{-t}\); for \(d/m\to\infty\), both tend to zero by elementary exponential bounds. For each fixed \(m\ge2\), the bases \(m/(m+2)\) and \((m-1)/m\) lie below one and the correction terms vanish, so both probabilities tend to zero as \(d\to\infty\). For each fixed \(d\), letting \(m\to\infty\) makes both probabilities tend to one. This proves the stated noncommuting limits.

## Verification

The accompanying standalone `checker.py` implements orthocomplement, meet, join, Sasaki implication, and right-nested evaluation using the lattice tables, independently of the transfer matrices. It exhaustively checks all full and all-atom assignments for even atom counts \(m=2,4,6,8\) and depths \(d=1,2,3,4\). It separately constructs a direct finite-state count and compares it with the two closed expressions, also testing larger \(m\) and \(d\). Run `python checker.py`; the expected final marker is `ALL_CHECKS_OK`. Direct evaluation is an independent finite consistency check, not the proof of the unbounded parameter theorem.

For illustration, when \(m=4\), the full failure counts for depths \(d=1,2,3,4\) are \(8,40,176,736\), while atomic counts are \(8,24,80,240\). All counts refer to labelled assignments and are obtained by the exact formulas.

## Relationship to prior work

Tokuo (2026), Section 5.5, proves ordinary currying fails under the Sasaki hook and provides the familiar six-element countermodel to the depth-one scheme \(p_0\to_S(p_1\to_S p_0)\). That establishes nonvalidity, not the uniform failure census as a function of arbitrary even atom count and nesting depth, nor the distinct double-scaling laws for full and atomic sampling. These are the additional claims proved here. The choice of the Sasaki hook and the orthomodular semantics comes directly from Tokuo's Definitions 2.1 and Section 5.5. Coecke and Smets (2001) establish the more general logical limitations of the Sasaki hook and its dynamic interpretation. Aguilera and Massas (2026) axiomatize a system combining intuitionistic and quantum implications. Neither contribution, in the inspected material, states the present count-and-scaling theorem. Failure of a database or keyword search is not a proof of historical novelty.

## Limitations

The exact formulas apply to height-two finite orthomodular horizontal sums, not to arbitrary orthomodular lattices or Hilbert lattices of larger height. The additional depth counts measure assignments for one syntactic family of nested weakening formulas; they neither prove an independence result between different quantum logics nor count inequivalent formulas. The probabilistic limit uses independent *uniform* valuations on finite carriers, not a quantum state, born-rule distribution, or physical measurement process. Related formulas may already exist under an unindexed term-function, automata, quantum-logic or transfer-matrix presentation. Independent historical and mathematical validation has not been performed.

## References

1. Kenji Tokuo, *A Lambda Calculus Based on Quantum Logic* (2026), arXiv:2610.34266v1, first posted 2026-10-25, especially Sections 2.1 and 5.5. https://arxiv.org/html/2610.34266v1
2. Bob Coecke and Sonja Smets, *The Sasaki Hook is not a [Static] Implicative Connective but Induces a Backward [in Time] Dynamic One that Assigns Causes* (2001), arXiv:quant-ph/0111076. https://arxiv.org/abs/quant-ph/0111076
3. Juan P. Aguilera and Guillaume Massas, *Conditionals and Modalities in Constructive Quantum Logics* (2026), arXiv:2606.31853; EPTCS 447, 16–34. https://doi.org/10.4204/EPTCS.447.2
