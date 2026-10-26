# A size cut shifts the crisp-intermediate threshold to \(\kappa\)

## Finding

Let \(\mathcal M\) be a transitive set model of \(\mathrm{ZFC}+\mathrm{GCH}\), with domain \(M\), and let \(\kappa\) be an infinite cardinal of \(\mathcal M\). Write \(\delta(a)\) for the constant function on \(M\) with value \(a\). Equip \(\mathfrak M=M^M\) with the pointwise Boolean-valued semantics: the truth value of a formula at functions \(f_1,\ldots,f_m\) is the set of states \(i\in M\) at which the corresponding formula holds in \(\mathcal M\), and a formula is true when that set is all of \(M\).

Define the transitive-closure size-cut domain

\[
\mathfrak N^{\mathrm{tc}}_\kappa=\delta[M]\cup\left\{f\in M^M:\forall i\in M,\ |\operatorname{tc}^{\mathcal M}(f(i))|^{\mathcal M}\ge\kappa\right\},
\]

where \(\operatorname{tc}^{\mathcal M}(x)\) is the transitive closure computed in \(\mathcal M\), and the superscript on cardinality indicates the cardinal computed there. Quantifiers in \(\mathfrak N^{\mathrm{tc}}_\kappa\) range over this domain, with the same pointwise truth values.

**Theorem.** The structure \(\mathfrak N^{\mathrm{tc}}_\kappa\) satisfies ZFC. Moreover, for every infinite cardinal \(\lambda\) of \(\mathcal M\), there exists a crisp intermediate cardinal between \(\delta(\lambda)\) and \(2^{\delta(\lambda)}\) in \(\mathfrak N^{\mathrm{tc}}_\kappa\) if and only if \(\lambda\ge\kappa\).

Here \(f\le_{\Box}g\) means \(f(i)\le g(i)\) in \(\mathcal M\) for every \(i\in M\), and \(f<_{\Box}g\) means \(f\le_{\Box}g\) but not \(g\le_{\Box}f\). Under GCH, \(2^{\delta(\lambda)}=\delta(\lambda^+)\). Thus the theorem gives a complete threshold classification for the existence of an intermediate in each infinite-cardinal interval: the threshold is inclusive for the size cut.

## Assumptions and scope

The ground structure is a transitive set model of \(\mathrm{ZFC}+\mathrm{GCH}\); \(\kappa\) and \(\lambda\) are infinite cardinals of that model. No forcing extension or additional large-cardinal assumption is used. The classification is for the single size-cut domain defined above, not for every possible filtration or every choice of size measure.

## Proof

Because \(\delta[M]\subseteq\mathfrak N^{\mathrm{tc}}_\kappa\subseteq\mathfrak M\), the pointwise transfer lemma for subdomains containing every constant function applies. For every formula \(\varphi(\vec f)\) with parameters from \(\mathfrak N^{\mathrm{tc}}_\kappa\), its truth value is

\[
\llbracket\varphi(\vec f)\rrbracket_{\mathfrak N^{\mathrm{tc}}_\kappa}
=\{i\in M:\mathcal M\models\varphi(\vec f(i))\}.
\]

Consequently every ZFC axiom and every instance of each ZFC scheme has truth value \(M\), since \(\mathcal M\models\mathrm{ZFC}\). Hence \(\mathfrak N^{\mathrm{tc}}_\kappa\models\mathrm{ZFC}\).

First suppose \(\lambda\ge\kappa\). Choose a state \(i_0\in M\) and define \(\eta_\lambda\in M^M\) by

\[
\eta_\lambda(i)=\begin{cases}\lambda,&i=i_0,\\\lambda^+,&i\ne i_0.\end{cases}
\]

For an ordinal cardinal \(\rho\), the transitive closure has \(\mathcal M\)-cardinality \(\rho\); hence both coordinate values \(\lambda\) and \(\lambda^+\) meet the size threshold \(\kappa\). Thus \(\eta_\lambda\in\mathfrak N^{\mathrm{tc}}_\kappa\), and it is a cardinal function by pointwise interpretation of the cardinal predicate. The domain has at least two states, so \(\eta_\lambda\) is nonconstant. At every state, \(\lambda\le\eta_\lambda(i)\le\lambda^+\). At any state other than \(i_0\), the value is strictly greater than \(\lambda\); at \(i_0\), it is strictly less than \(\lambda^+\). Therefore

\[
\delta(\lambda)<_{\Box}\eta_\lambda<_{\Box}\delta(\lambda^+)=2^{\delta(\lambda)},
\]

where the last equality uses GCH. This proves existence for every \(\lambda\ge\kappa\).

Now suppose \(\lambda<\kappa\), and assume toward a contradiction that a cardinal function \(\xi\in\mathfrak N^{\mathrm{tc}}_\kappa\) satisfies

\[
\delta(\lambda)<_{\Box}\xi<_{\Box}\delta(\lambda^+).
\]

If \(\xi\) is constant, this is impossible because there is no cardinal strictly between a cardinal and its successor. If \(\xi\) is nonconstant, then by the size-cut definition every coordinate \(\xi(i)\) has transitive-closure cardinality at least \(\kappa\). Since each \(\xi(i)\) is itself a cardinal, this means \(\xi(i)\ge\kappa\) for every state. But \(\lambda<\kappa\) implies \(\lambda^+\le\kappa\), while \(\xi<_{\Box}\delta(\lambda^+)\) implies \(\xi(i)\le\lambda^+\) for every state. If \(\lambda^+<\kappa\), these bounds are incompatible. If \(\lambda^+=\kappa\), they force \(\xi(i)=\lambda^+\) at every state, so \(\xi=\delta(\lambda^+)\), contradicting strictness. Thus no intermediate exists for \(\lambda<\kappa\), proving the classification.

For comparison, the primary source's rank-cut domain has no intermediate when \(\lambda\le\kappa\) (Proposition 4.9) and has one when \(\lambda>\kappa\) (Proposition 4.10). The size-cut classification therefore shifts the threshold exactly at the boundary: it admits an intermediate already for \(\lambda=\kappa\). \(\square\)

## Verification

The proof has two exhaustive cases for infinite cardinals: \(\lambda\ge\kappa\), where the explicit one-state witness works, and \(\lambda<\kappa\), where the size restriction and adjacent-cardinal interval rule out every nonconstant candidate. The ZFC claim follows from the pointwise transfer lemma because all constant functions are retained. GCH is used only to identify the power-set cardinal with the successor cardinal. No finite computation is used as evidence for the infinite claim.

## Relationship to prior work

The primary source, *Models of Arbitrary Sets* (arXiv:2610.23219v1), proves that its rank-cut domain satisfies ZFC and has no crisp intermediate between a constant infinite cardinal \(\lambda\) and \(2^\lambda\) when \(\lambda\le\kappa\) (Proposition 4.9). It also proves existence when \(\lambda>\kappa\) (Proposition 4.10), and that any subdomain between the constant functions and the full pointwise model satisfies ZFC (Proposition 4.11). Its final section explicitly proposes a transitive-closure size cut as a direction for future investigation. The present theorem gives the complete intermediate-existence threshold for that specific size cut and shows that it is inclusive, \(\lambda\ge\kappa\), rather than strict, \(\lambda>\kappa\).

Horsten's *Boolean-valued sets as arbitrary objects* provides earlier conceptual background for interpreting set-theoretic values across states, but it does not state this filtered-domain cardinal-interpolation classification.

## Limitations

The result assumes a transitive set model of \(\mathrm{ZFC}+\mathrm{GCH}\) and treats one transitive-closure size cut. It does not classify other size measures, other semantic environments, or the possible profiles of intermediate cardinals beyond existence. The originality assessment is literature-based rather than a proof of global priority; independent audit and independent validation have not been performed.

## References

1. P. T. Yago, S. Jockwich Martinez, and G. Venturi, “Models of Arbitrary Sets,” arXiv:2610.23219v1 (submitted 16 October 2026), especially §§4.5–4.6 and §5.3. arXiv:2610.23219v1
2. L. Horsten, “Boolean-valued sets as arbitrary objects,” arXiv:2002.02181 (2020), §§3–4. arXiv:2002.02181
