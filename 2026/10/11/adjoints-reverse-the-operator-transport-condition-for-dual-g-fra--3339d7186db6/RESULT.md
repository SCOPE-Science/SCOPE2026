# Adjoints reverse the operator transport condition for dual \(g\)-frames

## Finding
Theorem 3.1 of Fu--Zhang gives an operator method for transporting a dual or approximately dual pair of \(g\)-frames. It assumes
\[
O_2O_1^*=I
\]
for exact duality, or
\[
\|I-O_2O_1^*\|<1
\]
for approximate duality, and concludes that
\[
\{\Lambda_jO_1\}_{j\in J}
\quad\text{and}\quad
\{\Gamma_jO_2\}_{j\in J}
\]
form the corresponding transformed pair.

The condition has the adjoints in the wrong places.

Let
\[
H=\ell^2(\mathbb N),
\qquad
V_j=\mathbb C,
\]
and take the standard coordinate \(g\)-frame
\[
\Lambda_jx=\Gamma_jx=x_j.
\]
It is Parseval and dual to itself.

Let \(S\) be the unilateral shift
\[
S(x_1,x_2,x_3,\ldots)
=(0,x_1,x_2,\ldots)
\]
and choose
\[
O_1=O_2=S^*.
\]
Then
\[
O_2O_1^*=S^*S=I,
\]
so the theorem's exact hypothesis is satisfied.

However,
\[
\Lambda_jO_1x=\Gamma_jO_2x=x_{j+1}.
\]
Thus
\[
\sum_{j=1}^{\infty}|\Lambda_jO_1x|^2
=
\|x\|^2-|x_1|^2.
\]
For \(x=e_1\), this sum is zero. The transformed family is therefore not a \(g\)-frame at all. The exact-dual conclusion fails, and because the exact hypothesis also satisfies the theorem's approximate hypothesis with defect zero, the approximate-dual conclusion fails as well.

The correct transport quantity is \(O_2^*O_1\), not \(O_2O_1^*\).

## Assumptions and scope
The counterexample uses a separable infinite-dimensional Hilbert space, exactly as allowed by the paper. Each coefficient space is one-dimensional, so the example is already an ordinary frame example inside the \(g\)-frame formalism.

No convergence subtlety is involved. Both transformed sequences are Bessel, and all synthesis and analysis maps are standard unilateral-shift operators.

The failure is genuinely infinite-dimensional for the exact branch. In finite dimension, the identity
\[
O_2O_1^*=I
\]
forces both operators to be invertible and then also implies
\[
O_2^*O_1=I.
\]
The unilateral shift separates the two one-sided inverse conditions in infinite dimension.

## Proof
Let \(T_\Lambda\) denote the synthesis operator of \(\{\Lambda_j\}\). For the right-composed family \(\{\Lambda_jO_1\}\),
\[
(\Lambda_jO_1)^*=O_1^*\Lambda_j^*.
\]
Therefore its synthesis operator is
\[
T_{\Lambda O_1}=O_1^*T_\Lambda.
\]
Similarly,
\[
T_{\Gamma O_2}=O_2^*T_\Gamma.
\]

If \(\Lambda\) and \(\Gamma\) are dual, then
\[
T_\Gamma T_\Lambda^*=I.
\]
Consequently the mixed operator of the transformed pair is
\[
T_{\Gamma O_2}T_{\Lambda O_1}^*
=
O_2^*T_\Gamma T_\Lambda^*O_1
=
O_2^*O_1.
\]
This proves the exact equivalence
\[
\{\Lambda_jO_1\},\{\Gamma_jO_2\}\text{ are dual}
\quad\Longleftrightarrow\quad
O_2^*O_1=I.
\]
Because the opposite mixed product is the adjoint, the two approximate-duality defects have the same norm. Hence the corresponding exact criterion for the transported pair to satisfy the usual approximate-duality norm test is
\[
\|I-O_2^*O_1\|<1.
\]

For the explicit example, the original synthesis operator is the identity identification of \(\ell^2\) with itself. With
\[
O_1=O_2=S^*,
\]
the transformed synthesis operator is \(S\), so the transformed mixed operator is
\[
SS^*=I-P_{\operatorname{span}\{e_1\}}.
\]
It is neither the identity nor within operator-norm distance strictly less than one from the identity. This agrees with the direct failure of the lower frame bound.

## Verification
The complete statement and proof of Theorem 3.1 were inspected in the open-access version of record, together with the paper's definitions of synthesis operator, dual \(g\)-frame, and approximately dual \(g\)-frame.

The proof explicitly assigns \(O_1T_\Lambda\) as the synthesis operator of \(\{\Lambda_jO_1\}\). The defining synthesis formula instead gives \(O_1^*T_\Lambda\). The same adjoint reversal occurs for \(O_2\).

The shift identities are exact:
\[
S^*S=I,
\qquad
SS^*=I-P_{\operatorname{span}\{e_1\}}.
\]
The transformed coefficient energy is exactly
\[
\|S^*x\|^2=\|x\|^2-|x_1|^2.
\]
No numerical approximation, truncation, or finite-dimensional extrapolation is used.

## Relationship to prior work
The source cites the 2014 paper introducing approximate duality of \(g\)-frames as foundational background. Accessible metadata and abstract material for that predecessor describe the approximate-duality framework, but did not expose this operator-transport theorem or a correction of the 2018 statement.

A later 2020 paper develops an operator-theoretic approach to approximate duality for ordinary Hilbert-space frames. Its accessible abstract confirms that bounded-operator constructions are a central theme, but the available material inspected here did not contain the source-specific adjoint correction.

Targeted searches for the exact theorem, the condition \(O_2O_1^*=I\), the corrected condition \(O_2^*O_1=I\), unilateral-shift counterexamples, and errata did not locate an indexed correction of Theorem 3.1.

The paper's Corollary 3.1, which uses one unitary operator for both factors, remains valid: unitarity satisfies both possible adjoint orders.

## Limitations
The finding corrects Theorem 3.1 and does not reassess the paper's later characterization or perturbation theorems.

The counterexample is infinite-dimensional. That is essential for violating the exact branch under the source's one-sided inverse condition; the theorem's ambient setting explicitly includes this case.

An unindexed erratum, thesis remark, or informal author correction may contain the same observation.

## References
1. Y.-L. Fu and W. Zhang, *Characterization and stability of approximately dual \(g\)-frames in Hilbert spaces*, Journal of Inequalities and Applications 2018, Article 192, DOI 10.1186/s13660-018-1779-7.
2. A. Khosravi and M. Mirzaee Azandaryani, *Approximate duality of \(g\)-frames in Hilbert spaces*, Acta Mathematica Scientia 34(3) (2014), 639--652, DOI 10.1016/S0252-9602(14)60036-9.
3. M. Mirzaee Azandaryani, *An operator theory approach to the approximate duality of Hilbert space frames*, Journal of Mathematical Analysis and Applications 489 (2020), Article 124177, DOI 10.1016/j.jmaa.2020.124177.
