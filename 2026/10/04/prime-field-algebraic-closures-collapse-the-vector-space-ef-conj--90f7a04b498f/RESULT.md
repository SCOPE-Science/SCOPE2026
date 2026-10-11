# Prime-field algebraic closures collapse the vector-space EF conjecture

## Finding

Let \(P\) be either \(\mathbb{Q}\) or \(\mathbb{F}_p\), let \(F=\overline P\), and use Kim Scott's vector-space language \(L_{VS}\): unary scalar/vector sort predicates, scalar addition and multiplication with constants \(0,1\), vector addition with \(0_v\), and scalar multiplication. For integers \(1\le m<n\), write
\[
V_m=(F^m,F),\qquad V_n=(F^n,F).
\]

Then Spoiler's least winning round in the Ehrenfeucht--Fraïssé game on \(V_m,V_n\) is exactly
\[
m+2.
\]
Equivalently, \(V_m\equiv_{m+1}V_n\) but \(V_m\not\equiv_{m+2}V_n\).

Scott explicitly left the exact same-field algebraically-closed case open and conjectured the value \(2m+1\). Thus the conjecture is false for every \(m\ge2\) when the common field is the algebraic closure of its prime field; for \(m=1\), both expressions equal \(3\).

## Assumptions and scope

The game and language are exactly those defined in Scott's paper. In particular, \(L_{VS}\) does **not** require a scalar inverse symbol. The upper-bound argument below uses only scalar addition, multiplication and the constants \(0,1\): over \(\mathbb F_p\) every prime-field coefficient is a closed scalar term, while over \(\mathbb Q\) denominators are cleared and an integer-coefficient relation is written as an equality between two terms with nonnegative integer coefficients.

The claim is only for \(F=\overline{\mathbb Q}\) or \(F=\overline{\mathbb F_p}\); it does not assert an exact value for algebraically closed fields of positive transcendence degree.

The quantifier-rank interpretation is Scott's: a winning strategy through round \(q\) is equivalent to agreement on formulas of quantifier rank at most \(q\) in the corresponding infinitary setting. No statement about formula length or number of variables is made.

## Proof

For the lower bound, Duplicator survives \(m+1\) rounds. Respond to every scalar move by the identical scalar. As long as at most \(m\) vector moves have occurred, maintain an \(F\)-linear isomorphism between the \(F\)-spans of the paired vector plays. This is always extendible: if a new vector lies in the current span, use the same linear combination on the other side; if it is independent, the smaller space still has room while fewer than \(m+1\) independent vector moves have occurred.

The only remaining case is that all first \(m+1\) moves are vectors, so no scalar variable has been named. Every closed scalar term in \(L_{VS}\) evaluates in the prime field \(P\); consequently, preserving the full \(P\)-linear relation space of the selected vectors is more than enough to preserve every well-typed atomic equality between vector terms. The sort predicates and the fixed values assigned to ill-typed totalized operations are preserved as well. Since \([F:P]=\infty\), both \(F^m\) and \(F^n\) have infinite dimension over \(P\). Any finite \(P\)-linear partial isomorphism therefore extends over the last played vector. Hence Duplicator survives round \(m+1\).

For the upper bound, Spoiler first plays \(m+1\) \(F\)-linearly independent vectors \(v_1,\ldots,v_{m+1}\) in \(F^n\). If Duplicator has not already lost, the replies \(w_1,\ldots,w_{m+1}\) lie in \(F^m\), hence satisfy a nonzero \(F\)-linear relation
\[
c_1w_1+\cdots+c_{m+1}w_{m+1}=0.
\]
Normalize so that one coefficient, say \(c_j\), equals \(1\). Because \(F\) is algebraic over \(P\), the field
\[
K=P(c_1,\ldots,c_{m+1})
\]
is a finite extension of \(P\). It is simple: this is the primitive element theorem in characteristic zero and the cyclicity of finite-field extensions in characteristic \(p\). Choose \(\alpha\) with \(K=P(\alpha)=P[\alpha]\).

If \(P=\mathbb F_p\), choose polynomials \(h_i\in\mathbb F_p[X]\) with \(h_i(\alpha)=c_i\) and \(h_j=1\). Their coefficients are represented by closed scalar terms obtained from \(0,1\) and addition. Thus the dependence is an atomic vector equation whose coefficients are scalar terms in the single variable \(\alpha\).

If \(P=\mathbb Q\), choose polynomials \(f_i\in\mathbb Q[X]\) with \(f_i(\alpha)=c_i\) and \(f_j=1\). Multiply all \(f_i\) by one common positive denominator \(d\), obtaining \(g_i\in\mathbb Z[X]\) with \(g_i(\alpha)=dc_i\) and \(g_j=d\). Write
\[
g_i=g_i^+-g_i^-,
\]
where \(g_i^\pm\in\mathbb Z_{\ge0}[X]\). The dependence is then the atomic equality
\[
\sum_i g_i^+(\alpha)\ast w_i
=
\sum_i g_i^-(\alpha)\ast w_i,
\]
and every coefficient occurring on either side is built using only \(0,1,+,\cdot\).

On round \(m+2\), Spoiler plays \(\alpha\) on the side containing the \(w_i\). Let \(\beta\) be Duplicator's scalar response. The corresponding atomic equation cannot hold on \(v_1,\ldots,v_{m+1}\). In the finite-field case, their \(F\)-linear independence would force every \(h_i(\beta)\) to be zero, contradicting \(h_j=1\). In characteristic zero it would force every difference \(g_i^+(\beta)-g_i^-(\beta)\) to vanish, contradicting the distinguished constant difference \(g_j=d\ne0\). Thus Spoiler wins on round \(m+2\).

Combining the bounds gives the exact value \(m+2\).

## Verification

The critical syntax point is that the proof needs no inverse operation in \(L_{VS}\). The only denominator-clearing occurs externally when selecting an equivalent integer-coefficient dependence in characteristic zero; the atomic formula itself uses only the scalar operations actually present in Scott's language.

The finite symbolic sanity check in `verify.py` constructs, for \(2\le m\le8\), \(m+1\) vectors in \(\mathbb Q(\sqrt2)^m\) that are \(\mathbb Q\)-linearly independent but \(\mathbb Q(\sqrt2)\)-linearly dependent, and confirms that naming \(\sqrt2\) exposes the dependence. It is corroborative only; the all-\(m\) theorem is the argument above.

## Relationship to prior work

Scott defines \(L_{VS}\), proves the upper bound
\[
m+1+\min\!\bigl(m,\operatorname{mingen}(F/P)\bigr),
\]
proves only an \(m\)-round lower bound in the same-field case, and lists the exact algebraically-closed same-field game as an open problem with conjectured value \(2m+1\). The theorem above specializes to prime-field algebraic closures, improves the lower bound to \(m+1\), and exposes any dependence after one scalar move by using a primitive generator of the finite coefficient field.

Searches for the exact conjecture, its \(m+2\) specialization, and equivalent vector-space EF formulations did not locate a later source settling this case. This is best-of-knowledge evidence, not a proof of priority.

## Limitations

The exact value may depend on how many scalar parameters are needed to expose a dependence when the common algebraically closed field has positive transcendence degree. This result does not classify that regime. Priority risk remains for unindexed notes, theses, or later work not surfaced by the searches performed.

## References

1. Kim Scott, *A Partial Characterization of Ehrenfeucht-Fraïssé Games on Fields and Vector Spaces*, Research Science Institute / MIT, 2005 compendium; standalone copy dated 2007-07-31.
2. Research Science Institute 2005 Compendium, containing the same work.
