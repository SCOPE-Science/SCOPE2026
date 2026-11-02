# All-arity finite-field commuting counts for the one-variable Witt Lie algebra

## Finding
Let \(p\ge2\) be a prime, \(q=p^e\) with \(e\ge1\), and \(W_p(q)=\operatorname{Der}_{\mathbb F_q}(\mathbb F_q[t]/(t^p))\), equipped with its ordinary Lie bracket. For every integer \(m\ge0\), let \(C_{p,q}(m)\) count **ordered, pairwise commuting** \(m\)-tuples in \(W_p(q)\), including the unique empty tuple.

Write \(s=\lfloor(p-1)/2\rfloor\). The exact all-arity count is
\[
\boxed{C_{p,q}(m)=1+(q^m-1)\left[q^{p-1}+\sum_{r=1}^{s}q^{p-2r+(r-1)m}+\sum_{r=s+1}^{p-1}q^{(p-r-1)m}\right].}
\]
Empty sums are zero, so this includes characteristic two. More precisely, if \(H_a=t^a\mathbb F_q[t]/(t^p)\,\partial_t\) for \(1\le a\le p\), the count of pairwise commuting \(m\)-tuples entirely in the filtered Lie subalgebra \(H_a\) is
\[
\boxed{C_{p,q}^{(a)}(m)=1+(q^m-1)\left[\sum_{r=a}^{s}q^{p-2r+(r-1)m}+\sum_{r=\max(a,s+1)}^{p-1}q^{(p-r-1)m}\right].}
\]
Here \(H_p=0\). Both formulas are point counts, not just variety dimensions or generating-function asymptotics.

In particular, for odd \(p\), the commuting-pair count is
\[
C_{p,q}(2)=q^{p+1}+\frac{p-1}{2}(q^2-1)q^{p-2},
\]
while for \(p=2\) it is \(q^3+q^2-q\). For example \(C_{5,5}(2)=21625\) and \(C_{5,5}(3)=186125\).

## Assumptions and scope
Throughout, \(R=k[t]/(t^p)\) with \(k=\mathbb F_q\), \(\operatorname{char}k=p\), and \(\partial_t\) is the well-defined derivation \(d/dt\) of \(R\) (because \(\partial_t(t^p)=0\)). All derivations are uniquely \(f\partial_t\) with \(f\in R\). Define \(\nu(f)\in\{0,\ldots,p-1\}\) to be the smallest index of a nonzero coefficient of \(f\), and \(\nu(0)=p\). The Lie bracket is
\[
[f\partial_t,g\partial_t]=(fg'-gf')\partial_t.
\]
The count is for labeled ordered tuples; no quotient by automorphisms or conjugacy is taken. No nonzero or restricted-nilpotent condition is imposed on the individual derivations.

## Proof
**1. Centralizers and leading terms.** Write \(H_r=t^r R\partial_t\) for \(0\le r\le p\). Let \(0\ne f\in R\) and \(r=\nu(f)\). If \(r=0\), \(f\) is a unit and
\[
fg'-gf'=f^2(g/f)',
\]
so the centralizer of \(f\partial_t\) is exactly \(k f\partial_t\), because the kernel of differentiation on \(R\) is \(k\).

For \(r\ge1\), if \(g\ne0\) has least nonzero coefficient of degree \(j\), the coefficient of \(t^{r+j-1}\) in \(fg'-gf'\) is \((j-r)f_r g_j\), provided \(r+j-1<p\). Since \(0\le j,r<p\), this is nonzero whenever \(j\ne r\). Consequently, if \(1\le r\le s\), every commuting \(g\) is uniquely \(cf+h\) with \(c\in k\) and \(h\in t^{p-r+1}R\). Conversely, each such \(g\) commutes, by degree. Thus
\[
Z_{W_p(q)}(f\partial_t)=k f\partial_t\oplus H_{p-r+1}\qquad(1\le r\le s).
\]
If \(r\ge s+1\), the same leading-coefficient argument and the degree cutoff instead give
\[
Z_{W_p(q)}(f\partial_t)=H_{p-r+1}.
\]
In particular, \(H_r\) is abelian when \(r\ge s+1\), since \([H_r,H_r]\subseteq H_{2r-1}=0\).

**2. A disjoint decomposition by minimal valuation.** For an ordered commuting tuple that is not identically zero, put \(r=\min_i\nu(f_i)\). Different minima define disjoint strata. If \(r=0\), all entries lie on the same one-dimensional line \(kf\), with \(f\) normalized to have constant coefficient one. There are \(q^{p-1}\) such lines and \(q^m-1\) nonzero scalar tuples: the contribution is \(q^{p-1}(q^m-1)\).

If \(1\le r\le s\), all entries belong to the common abelian centralizer of an entry with valuation \(r\). Modulo the tail \(H_{p-r+1}\), their images span a **uniquely determined** line. Normalize its degree-\(r\) coefficient to one. The quotient \(H_r/H_{p-r+1}\) has dimension \(p-2r+1\), so there are exactly \(q^{p-2r}\) such normalized lines. Fixing one line and its normalized lift \(f\), the tuple entries have the form \(c_i f+h_i\) with \(h_i\in H_{p-r+1}\); at least one \(c_i\) is nonzero. Since the tail has dimension \(r-1\), this stratum contributes
\[
q^{p-2r}(q^m-1)q^{(r-1)m}.
\]
This normalization is essential: choosing a full representative \(f\) without quotienting by the tail would overcount.

If \(s+1\le r\le p-1\), \(H_r\) itself is abelian. The commuting tuples with minimum valuation exactly \(r\) are **all** tuples in \(H_r^m\setminus H_{r+1}^m\), numbering
\[
q^{(p-r)m}-q^{(p-r-1)m}=(q^m-1)q^{(p-r-1)m}.
\]
Adding all disjoint nonzero strata and the zero tuple proves the first boxed formula for every \(m\ge1\); when \(m=0\), both sides equal one.

**3. Filtered algebras and the pair simplification.** The same strata with \(r\ge a\) give the second boxed formula, since \(H_a\) is a Lie subalgebra. For odd \(p=2s+1\), setting \(m=2\) yields \(s\) copies of \(q^{p-2}\) in the middle sum and a geometric series \(1+q^2+\cdots+q^{2(s-1)}\) in the last. Canceling the geometric series against \(q^2-1\) gives the stated closed pair formula. The \(p=2\) case is a direct substitution.

## Verification
The standalone `verify.py` constructs the adjoint matrices from \([t^i\partial_t,t^j\partial_t]=(j-i)t^{i+j-1}\partial_t\) modulo \(t^p\), performs finite-field row reduction, enumerates **actual** centralizer vectors, and for each commuting ordered pair computes the common-centralizer dimension to count all commuting ordered triples. It does not use the claimed all-arity formula to construct centralizers. Exhaustive pair and triple counts agree with the formulas over \(\mathbb F_2\), \(\mathbb F_4\), \(\mathbb F_3\), \(\mathbb F_9\), and \(\mathbb F_5\). Run `python3 verify.py`; the required success marker is `WITT_ALL_ARITY_POINT_COUNT_OK`.

## Relationship to prior work
Yao and Chang's 2013 arXiv paper *Nilpotent commuting varieties of the Witt algebra* (Lemma 2.3 and Theorems 3.6, 4.3) already provides centralizer descriptions and irreducible-component results over algebraically closed fields, with a restriction to nilpotent entries in the geometric theorems. **Neither those centralizer facts nor those geometric results are claimed new.** The 2018 *Commuting variety of Witt algebra* studies the geometric commuting-pair locus; the 2021 *Commuting variety of \(r\)-tuples over the Witt algebra* gives irreducible components and dimensions for unrestricted tuples. Component geometry alone does not specify the number of finite-field points or resolve intersections of its strata. The result claimed here is the **disjoint arithmetic count for every finite field and every arity, together with all standard filtered Lie subalgebras**. The proof establishes it independently by an explicit normalized-line enumeration.

## Limitations
This is not a new classification of centralizers, components, or orbit types. It counts points of the commuting locus but does not describe its scheme structure or cohomology, or the distribution by conjugacy classes. Its proof uses the special truncation exponent equal to the field characteristic; general \(k[t]/(t^N)\) requires further resonance analysis and is not covered. Finite checks are supporting evidence only; publication priority has not been independently certified. The full 2018 and 2021 texts could not be materially inspected in this assessment, so an unobserved equivalent finite-field count remains a historical risk.

## References
1. Y.-F. Yao and H. Chang, *Nilpotent commuting varieties of the Witt algebra*, arXiv:1301.5667v1, first posted 2013-01-23, especially Lemma 2.3 and Sections 3–4. https://arxiv.org/pdf/1301.5667
2. Y.-F. Yao and H. Chang, *Commuting variety of Witt algebra*, Frontiers of Mathematics in China 13 (2018), 1179–1187, DOI:10.1007/s11464-018-0725-9. https://journal.hep.com.cn/fmc/EN/10.1007/s11464-018-0725-9
3. Y.-F. Yao and Y. Zhang, *Commuting variety of \(r\)-tuples over the Witt algebra*, Journal of East China Normal University (Natural Science), 2021(3), 1–7, DOI:10.3969/j.issn.1000-5641.2021.03.001. https://xblk.ecnu.edu.cn/EN/10.3969/j.issn.1000-5641.2021.03.001
