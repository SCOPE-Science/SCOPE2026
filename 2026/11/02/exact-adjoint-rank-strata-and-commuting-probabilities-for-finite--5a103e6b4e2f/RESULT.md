# Exact adjoint-rank strata and commuting probabilities for finite modular Witt algebras

## Finding
Let \(p\ge 5\) be prime, \(q=p^e\) with \(e\ge1\), and let \(W=\operatorname{Der}_{\mathbb F_q}(\mathbb F_q[x]/(x^p))\). Write every element as \(f(x)\partial\), with \(\partial=d/dx\), and put \(v(f)=\operatorname{ord}_x f\) for \(f\ne0\). Define \(d(0)=1\), \(d(v)=v\) when \(1\le v\le(p-1)/2\), and \(d(v)=v-1\) when \((p+1)/2\le v\le p-1\).

**Theorem.** For every nonzero \(f\in\mathbb F_q[x]/(x^p)\), the Lie centralizer of \(f\partial\) has dimension \(d(v(f))\) over \(\mathbb F_q\). The zero derivation has centralizer dimension \(p\). In particular the complete adjoint-rank generating polynomial is
\[
\mathcal A_{p,q}(z)=1+(q-1)\sum_{v=0}^{p-1}q^{p-v-1}z^{p-d(v)}.
\]
The number of ordered commuting pairs is exactly
\[
\#\{(X,Y)\in W^2:[X,Y]=0\}
=q^{p-2}\left(q^3+\frac{p-1}{2}(q^2-1)\right).
\]
Equivalently the commuting probability for two independent uniform elements is
\[
\operatorname{cp}(W)=q^{1-p}+\frac{p-1}{2}\frac{q^2-1}{q^{p+2}}.
\]
Both formulas include the zero element and all finite extensions of \(\mathbb F_p\).

## Assumptions and scope
All algebras and centralizer dimensions are over the finite field \(\mathbb F_q\), whose characteristic is the same prime \(p\) as the truncation exponent. The ring is \(R=\mathbb F_q[x]/(x^p)\). Since the derivative of \(x^p\) is zero in characteristic \(p\), \(\partial\) is a well-defined derivation of \(R\), and \(W=R\partial\) has dimension \(p\). The bracket is
\[
[f\partial,g\partial]=(fg'-gf')\partial.
\]
For a nonzero polynomial class, the valuation \(v(f)\) is the least index of a nonzero coefficient in its unique representative of degree less than \(p\). No comparison is asserted for other truncated exponents or for characteristic two or three.

## Proof
**Case \(v(f)=0\).** Then \(f\) is a unit. Writing \(g=fh\), one gets \(fg'-gf'=f^2h'\). Thus commutation is equivalent to \(h'=0\). Because every coefficient \(1,\ldots,p-1\) is invertible in \(\mathbb F_q\), the derivative kernel in \(R\) consists exactly of constants. The centralizer has dimension one.

**Case \(1\le v\le(p-1)/2\).** Write \(f=x^vu\) with \(u\) a unit. If \(g\ne0\) has valuation \(w<v\), the lowest coefficient of \(fg'-gf'\) occurs in degree \(v+w-1<p\) and equals the product of the nonzero leading coefficients with \(w-v\), which is nonzero in characteristic \(p\). Hence every centralizing \(g\) is divisible by \(x^v\), and can be written as \(g=fh\) with \(h\) uniquely specified modulo \(x^{p-v}\). Then \(fg'-gf'=f^2h'\). Since \(f^2=x^{2v}u^2\) and \(2v<p\), this expression vanishes precisely when \(h'\) is divisible by \(x^{p-2v}\). Writing \(h=\sum_{i=0}^{p-v-1}h_ix^i\), this requires \(h_i=0\) for \(1\le i\le p-2v\), while \(h_0\) and the \(v-1\) coefficients with \(p-2v+1\le i\le p-v-1\) are arbitrary. Thus the centralizer dimension is \(v\). The condition is independent of the choice of representative of \(h\), since changing it by a multiple of \(x^{p-v}\) changes \(f^2h'\) by a multiple of \(x^p\).

**Case \((p+1)/2\le v\le p-1\).** Put \(k=p-v+1\). If \(g\) has valuation \(w<k\), then \(w<v\) and \(w+v-1<p\). The same leading-coefficient argument shows \([f\partial,g\partial]\ne0\). Conversely, for every \(g\in x^kR\), both \(fg'\) and \(gf'\) vanish in \(R\), since their terms have degree at least \(v+k-1=p\). The centralizer is exactly \(x^kR\), of dimension \(p-k=v-1\).

**Enumeration.** Exactly \((q-1)q^{p-v-1}\) nonzero polynomials have valuation \(v\), giving the rank polynomial because \(\operatorname{rank}(\operatorname{ad}_{f\partial})=p-d(v)\). The zero derivation contributes the constant term one. Summing the centralizer sizes yields
\[
\begin{aligned}
\#\{(X,Y):[X,Y]=0\}
&=q^p+(q-1)\sum_{v=0}^{p-1}q^{p-v-1+d(v)}\\
&=q^p+(q-1)\left(q^p+\frac{p-1}{2}q^{p-1}+\frac{p-1}{2}q^{p-2}\right)\\
&=q^{p-2}\left(q^3+\frac{p-1}{2}(q^2-1)\right).
\end{aligned}
\]
Division by \(|W|^2=q^{2p}\) gives the probability.

## Verification
The standalone program `verify.py` builds the \(p\times p\) adjoint matrix from the Lie bracket, uses independent modular Gaussian elimination to calculate its rank, and checks the theorem for every one of the \(5^5=3125\) elements over \(\mathbb F_5\). It also checks a deterministic sample of \(961\) further elements in characteristics \(7,11,13\), distributed over every valuation class. It verifies that the exhaustive \(p=q=5\) commuting-pair count is \(21625\). Run with `python3 verify.py` using Python 3 standard library only. Finite calculations are consistency tests, not a proof for every \(p,q\); the preceding argument is the infinite-family proof.

## Relationship to prior work
Yao and Chang (2018) analyze the geometric irreducible components and dimensions of the Witt algebra's commuting-pair variety over algebraically closed fields. Yao and Zhang (2021) extend this geometric approach to commuting tuples. Their accessible statements concern geometric components rather than the finite-field adjoint-rank and point-count polynomial derived above. Fulman and Guralnick (2018) enumerate commuting pairs for classical matrix, unitary and symplectic Lie algebras over finite fields, not the modular one-variable Witt family. The valuation criterion, full finite-field rank strata, and resulting explicit commutation probability are the subject of the present theorem.

## Limitations
The proof assumes the truncation exponent equals the odd prime characteristic and does not cover higher-dimensional Jacobson–Witt algebras or arbitrary truncated polynomial exponents. The available summaries of Yao–Chang and Yao–Zhang establish geometric questions but their complete primary texts could not be retrieved; an implicit equivalent finite-field specialization in those texts remains a publication-priority risk. The reported source comparison is best-knowledge, not a claim of global priority or independent validation.

## References
1. Y.-F. Yao and H. Chang, *Commuting variety of Witt algebra*, Frontiers of Mathematics in China **13** (2018), 1179–1187. DOI: 10.1007/s11464-018-0725-9; online 2018-10-29.
2. Y. Yao and Y. Zhang, *Commuting variety of r-tuples over the Witt algebra*, Journal of East China Normal University (Natural Science) **2021** (3), 1–7. DOI: 10.3969/j.issn.1000-5641.2021.03.001; online 2021-05-25.
3. J. Fulman and R. Guralnick, *Enumeration of Commuting Pairs in Lie Algebras over Finite Fields*, Annals of Combinatorics **22** (2018), 295–316. DOI: 10.1007/s00026-018-0390-4; online 2018-04-27.
