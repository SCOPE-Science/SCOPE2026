# Unique quasi norm attainment forces compactness on \(c_0(\Gamma)\)

## Finding

Let \(\Gamma\) be any index set, \(\mathbb K\) be either \(\mathbb R\) or \(\mathbb C\), and \(Y\) be any Banach space over \(\mathbb K\). A bounded operator \(S:c_0(\Gamma;\mathbb K)\to Y\) is **uniquely quasi norm-attaining** (UQNA) if there is \(u\in Y\) with \(\|u\|=\|S\|\) such that each sequence \((x_n)\) in the closed unit ball satisfying \(\|Sx_n\|\to\|S\|\) has a subsequence whose images converge to \(\theta u\) for one \(\theta\in\mathbb K\) with \(|\theta|=1\). For the zero operator this convention gives UQNA automatically.

**Theorem.** Every UQNA operator \(S:c_0(\Gamma;\mathbb K)\to Y\) is compact. Moreover,
\[
\overline{\operatorname{UQNA}(c_0(\Gamma),Y)}^{\|\cdot\|}
 =\mathcal K(c_0(\Gamma),Y).
\]
Consequently every \(T\in\mathcal L(c_0(\Gamma),Y)\) satisfies
\[
\operatorname{dist}(T,\operatorname{UQNA}(c_0(\Gamma),Y))
 =\operatorname{dist}(T,\mathcal K(c_0(\Gamma),Y))=\|T\|_{\mathrm{ess}}.
\]
If \(\Gamma\) is infinite, the identity on \(c_0(\Gamma)\) has distance exactly \(1\) from UQNA operators.

## Assumptions and scope

The space \(c_0(\Gamma;\mathbb K)\) comprises scalar families tending to zero off finite sets: for each \(\varepsilon>0\), only finitely many coordinates have modulus at least \(\varepsilon\). It carries the supremum norm. The coordinate truncation \(P_F\) associated to a finite \(F\subset\Gamma\) retains the entries in \(F\) and sets the others to zero. It has finite rank and \(\|P_F\|\le1\). Its Banach dual is \(\ell_1(\Gamma;\mathbb K)\): any bounded scalar functional is represented by an absolutely summable family. No countability assumption is made on \(\Gamma\) and no geometric assumption on \(Y\) is made.

UQNA is weaker than ordinary strong norm attainment: the distinguished image \(u\) need not be attained at a point of the original unit ball. The theorem concerns operator-norm closure and the usual compact-operator ideal; it does not assert that every compact operator is itself UQNA.

## Proof

**1. A supporting functional saturates the operator norm.** The zero operator is compact. Suppose \(S\ne0\) is UQNA, let \(r=\|S\|>0\), and fix a distinguished \(u\in Y\) with \(\|u\|=r\) from the definition. By Hahn--Banach choose \(y^*\in Y^*\) with \(\|y^*\|=1\) and \(y^*(u)=r\), with this value real and positive also in the complex case. Set \(f=y^*\circ S\in(c_0(\Gamma))^*=\ell_1(\Gamma)\). Clearly \(\|f\|\le r\).

Choose any sequence \((v_n)\) in the unit ball with \(\|Sv_n\|\to r\), which exists by the definition of the norm. The UQNA condition yields a subsequence with \(Sv_{n_j}\to\theta u\) for a unimodular \(\theta\). Therefore \(|f(v_{n_j})|\to|\theta y^*(u)|=r\); hence \(\|f\|=r\).

**2. A calibrated uniqueness implication.** For any sequence \((w_n)\) in the unit ball such that \(\operatorname{Re}f(w_n)\to r\), one has
\[
\boxed{\quad Sw_n\longrightarrow u\quad\text{in norm}.\quad}
\]
Indeed, \(\operatorname{Re}f(w_n)\le\|Sw_n\|\le r\) forces \(\|Sw_n\|\to r\). Apply UQNA to an arbitrary subsequence of \((w_n)\): some further subsequence satisfies \(Sw_{n_j}\to\theta u\). On this further subsequence, \(\operatorname{Re}f(w_{n_j})\to\operatorname{Re}(\theta y^*(u))=r\operatorname{Re}\theta\). Since the left side tends to \(r\), the unimodular scalar is \(\theta=1\) (also over the reals). Thus every subsequence of \((Sw_n)\) has a further subsequence converging to \(u\), which implies the full sequence converges to \(u\). This argument does not posit that \(S\) attains its norm.

**3. Finite coordinate truncations approximate \(S\) in operator norm.** Write \(f(x)=\sum_{\gamma\in\Gamma}b_\gamma x_\gamma\), where \(\sum_\gamma|b_\gamma|=r\). Choose increasing finite subsets \(F_n\subset\Gamma\) with
\[
\tau_n:=\sum_{\gamma\notin F_n}|b_\gamma|\longrightarrow0.
\]
Define \(a_n\in c_0(\Gamma)\) supported on \(F_n\) by \((a_n)_\gamma=\overline{b_\gamma}/|b_\gamma|\) when \(b_\gamma\ne0\), and zero otherwise; over \(\mathbb R\) this is the sign of \(b_\gamma\). Then \(\|a_n\|\le1\) and \(f(a_n)=r-\tau_n\) is nonnegative real.

We claim
\[
\|S(I-P_{F_n})\|\longrightarrow0.
\]
Otherwise there are \(\varepsilon>0\), a subsequence of indices (relabeled \(n\)), and \(z_n\in c_0(\Gamma)\) supported outside \(F_n\) with \(\|z_n\|\le1\) and \(\|Sz_n\|\ge\varepsilon\). Because supports are disjoint, both \(a_n+z_n\) and \(a_n-z_n\) belong to the unit ball. The coefficient tail estimate yields, simultaneously,
\[
\operatorname{Re}f(a_n\pm z_n)
 \ge r-\tau_n-|f(z_n)|\ge r-2\tau_n\longrightarrow r.
\]
By Step 2 both \(S(a_n+z_n)\to u\) and \(S(a_n-z_n)\to u\). Subtracting gives \(2Sz_n\to0\), contradicting \(\|Sz_n\|\ge\varepsilon\). Hence the claim holds. As each \(SP_{F_n}\) has finite rank, \(S\) is a norm limit of finite-rank operators and is compact. This also proves compactness when \(\Gamma\) is uncountable: only the (countable) support of \(f\) needs to be exhausted.

**4. Exact closure and distance.** Corollary 3.11(a) of Choi--Choi--Jung--Martín [1] asserts that UQNA compact operators are norm dense in \(\mathcal K(X,Y)\) for arbitrary Banach spaces \(X,Y\). Taking \(X=c_0(\Gamma)\), Step 3 yields \(\operatorname{UQNA}(X,Y)\subseteq\mathcal K(X,Y)\), while that corollary yields \(\mathcal K(X,Y)\subseteq\overline{\operatorname{UQNA}(X,Y)}\). The compact-operator class is closed in operator norm, proving equality of closures. Distances to a set and to its closure coincide, so the distance formula follows by the definition of the essential norm.

**5. Sharp identity distance.** If \(\Gamma\) is infinite, choose pairwise distinct \(\gamma_n\in\Gamma\). The coordinate vectors \(e_{\gamma_n}\) are weakly null in \(c_0(\Gamma)\), since all scalar functionals belong to \(\ell_1(\Gamma)\). Each compact \(K:c_0(\Gamma)\to c_0(\Gamma)\) takes this weakly null sequence to a norm-null sequence; hence
\[
\|I-K\|\ge\limsup_{n\to\infty}\|e_{\gamma_n}-Ke_{\gamma_n}\|=1.
\]
Taking \(K=0\) gives the reverse inequality. The closure identity then gives \(\operatorname{dist}(I,\operatorname{UQNA})=1\). In finite dimension the identity is compact and the distance is \(0\).

## Verification

The supporting-functional argument, calibrated uniqueness implication, opposing disjoint-support perturbation and norm-limit-of-finite-rank step are complete analytic arguments valid for every index set and over both scalar fields. All quantifiers in the UQNA definition are sequential and the proof requires only a sequence of finite coefficient truncations; this is possible because each member of \(\ell_1(\Gamma)\) has at most countable support. The only imported substantive ingredient is the published compact-UQNA density theorem [1, Corollary 3.11(a)]. No numerical experiment, finite-dimensional test, software certificate or unstated compactness implication is substituted for a proof.

A boundary check is the scalar-valued case: every bounded scalar functional on \(c_0(\Gamma)\) is rank-one and is UQNA, consistent with the classification. Another boundary is any finite \(\Gamma\), when all bounded operators are compact but not necessarily themselves UQNA. For infinite \(\Gamma\), the exact distance for the identity remains \(1\) with either scalar field.

## Relationship to prior work

The earliest public version of [1] was submitted April 23, 2020 (arXiv:2004.11025v1, primary MSC 46B04). It introduces UQNA in Definition 3.9, establishes density of UQNA compact operators in all compact operators in Corollary 3.11(a), and shows in Example 7.8 that the identity on \(c_0\) cannot be approximated by UQNA operators. Its proof of that example assumes an approximant at distance below \(1/4\); it neither supplies the compactness classification nor determines the sharp distance \(1\).

The later work [2] introduces the stronger range strongly exposing (RSE) condition, shows \(\operatorname{RSE}=\operatorname{NA}\cap\operatorname{UQNA}\) (Proposition 2.3), and establishes a finite-rank restriction for RSE operators on subspaces of \(c_0\) (Proposition 3.16 and its proof). This restriction does **not** imply compactness of UQNA operators that need not attain their norms. The theorem here is a direct UQNA-specific compactness statement, including non-norm-attaining cases, and combines it with [1] to classify the closure in every target Banach space.

## Limitations

The theorem is a characterization of the norm closure of UQNA operators on the stated domain, not an assertion that every compact operator is UQNA or that UQNA operators must have finite rank. It does not classify norm attainment of individual compact operators, nor does it provide a uniform finite truncation rate independent of the operator. Equality with essential norm is exact for all bounded operators on the domain, while computing that essential norm for a specific operator may remain difficult. Originality comparisons cover the identified primary publications and indexed related records; unindexed equivalent formulations remain a residual bibliographic possibility. No independent audit is claimed.

## References

[1] Geunsu Choi, Yun Sung Choi, Mingu Jung, Miguel Martín, *On quasi norm attaining operators between Banach spaces*, arXiv:2004.11025v1 (submitted April 23, 2020), Definition 3.9, Corollary 3.11(a), Example 7.8. https://arxiv.org/pdf/2004.11025 ; https://arxiv.org/abs/2004.11025

[2] Geunsu Choi, Helena del Río, Audrey Fovelle, Mingu Jung, Miguel Martín, *Range absolutely strongly exposing operators between Banach spaces*, arXiv:2503.18581 (submitted March 24, 2025), Proposition 2.3 and Proposition 3.16. https://arxiv.org/pdf/2503.18581
