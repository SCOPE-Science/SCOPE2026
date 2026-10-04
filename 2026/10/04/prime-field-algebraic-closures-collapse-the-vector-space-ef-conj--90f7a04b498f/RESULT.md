# Prime-field algebraic closures collapse the vector-space EF conjecture
## Finding
Let \(P\) be either \(\mathbb{Q}\) or \(\mathbb{F}_p\), let \(F=\overline P\), and use Kim Scott's vector-space language \(L_{VS}\): the scalar field operations, unary scalar/vector sort predicates, vector addition, and scalar multiplication. For integers \(1\le m<n\), write \(V_m=(F^m,F)\) and \(V_n=(F^n,F)\).

Then Spoiler's least winning round in the Ehrenfeucht--Fraïssé game on \(V_m,V_n\) is exactly
\[
 m+2.
\]
Equivalently, \(V_m\equiv_{m+1}V_n\) but \(V_m\not\equiv_{m+2}V_n\).

Scott explicitly left the exact same-field algebraically-closed case open and conjectured the value \(2m+1\). Thus the conjecture is false for every \(m\ge2\) when the common field is the algebraic closure of its prime field; for \(m=1\), both expressions equal \(3\).

## Assumptions and scope
The game and language are exactly those defined in Scott's paper. In particular, scalar inverse is a function symbol, so every element of a simple finite extension \(P(\alpha)\) can be represented by a scalar term in \(\alpha\). The claim is only for \(F=\overline{\mathbb Q}\) or \(F=\overline{\mathbb F_p}\); it does not assert an exact value for algebraically closed fields of positive transcendence degree.

The quantifier-rank interpretation is Scott's: a winning strategy through round \(q\) is equivalent to agreement on formulas of quantifier rank at most \(q\) in the corresponding infinitary setting. No statement about formula length or number of variables is made.

## Proof
For the lower bound, Duplicator survives \(m+1\) rounds. Respond to every scalar move by the identical scalar. As long as at most \(m\) vector moves have occurred, maintain an \(F\)-linear isomorphism between the \(F\)-spans of the paired vector plays. This is always extendible: if a new vector lies in the current span, use the same linear combination on the other side; if it is independent, the smaller space still has room while fewer than \(m+1\) independent vector moves have occurred.

The only remaining case is that all first \(m+1\) moves are vectors, so no scalar variable has been named. On the final move, preserve only the \(P\)-linear atomic type. This is enough because every closed scalar term evaluates in \(P\), hence every well-typed vector term in the selected vector variables is a \(P\)-linear combination of them; the sort predicates and the fixed values of nonsensical mixed operations are also preserved. The previously paired vector tuples induce a \(P\)-linear partial isomorphism. Since \([F:P]=\infty\), both \(F^m\) and \(F^n\) have infinite dimension over \(P\), so that finite \(P\)-linear partial isomorphism extends over the last played vector. Therefore Duplicator survives round \(m+1\).

For the upper bound, Spoiler first plays \(m+1\) \(F\)-linearly independent vectors \(v_1,\ldots,v_{m+1}\) in \(F^n\). If Duplicator has not already lost, the replies \(w_1,\ldots,w_{m+1}\) lie in \(F^m\), hence satisfy a nonzero \(F\)-linear relation
\[
 c_1w_1+\cdots+c_{m+1}w_{m+1}=0.
\]
Normalize so that one nonzero coefficient is \(1\). Because \(F\) is algebraic over \(P\), the field \(K=P(c_1,\ldots,c_{m+1})\) is a finite extension of \(P\). It is simple: in characteristic zero this is the primitive element theorem for number fields, and in characteristic \(p\) every finite extension of \(\mathbb F_p\) is a finite field and hence simple. Choose \(\alpha\) with \(K=P(\alpha)\). Each \(c_i\) is therefore the value of a scalar field term \(t_i(\alpha)\).

On round \(m+2\), Spoiler plays \(\alpha\) on the side containing the \(w_i\). Whatever scalar \(\beta\) Duplicator chooses, the atomic equation
\[
 t_1(\alpha)\!\ast w_1+_v\cdots+_v t_{m+1}(\alpha)\!\ast w_{m+1}=0_v
\]
holds there. The corresponding equation on \(v_1,\ldots,v_{m+1}\) cannot hold: their \(F\)-linear independence would force every coefficient \(t_i(\beta)\) to be zero, but the normalized coefficient term is identically \(1\). Thus Spoiler wins on round \(m+2\).

Combining the bounds gives the exact value \(m+2\).

## Verification
The proof was checked separately for the two potentially delicate points: the last scalar-free vector round only needs preservation of \(P\)-linear relations, and the exposing coefficient field is finite and simple over \(P\). A finite symbolic sanity check in `verify.py` constructs, for \(2\le m\le8\), \(m+1\) vectors in \(\mathbb Q(\sqrt2)^m\) that are \(\mathbb Q\)-linearly independent but \(\mathbb Q(\sqrt2)\)-linearly dependent, and confirms that naming \(\sqrt2\) exposes the dependence. It returned `VERIFY_OK m=2..8 qlinear_independence_and_named_scalar_exposure`.

The finite check is corroborative only; the general proof above is not an extrapolation from those cases.

## Relationship to prior work
Scott defines \(L_{VS}\), proves an upper bound \(m+1+\min(m,\operatorname{mingen}(F/P))\), proves only an \(m\)-round lower bound in the same-field case, and then lists the exact algebraically-closed same-field game as an open problem with conjectured value \(2m+1\). The present claim specializes to the prime-field algebraic closure and uses a finite primitive generator for the actual dependence coefficients to reduce the upper bound to \(m+2\), together with a matching \(m+1\)-round Duplicator strategy.

Searches in the published-finding corpus finding database and public web search for the exact conjecture, its \(m+2\) specialization, and equivalent vector-space EF formulations did not locate a later source settling this case. This is evidence of non-coverage, not a proof of priority.

## Limitations
The exact value may depend on how many field parameters are needed to expose a dependence relation when the common algebraically closed field has transcendence. This finding does not classify that regime. Priority risk remains for unindexed notes, theses, or later work not surfaced by the searches performed.

The 2005 RSI compendium shows the project circulated in 2005 but gives no day-level publication date. For machine metadata, the earliest exact public date verified in this run is the Intel public project record dated 2006-03-14; the standalone mathematical paper bears 2007-07-31.

## References
1. Kim Scott, *A Partial Characterization of Ehrenfeucht-Fraïssé Games on Fields and Vector Spaces*, Research Science Institute / MIT, standalone copy dated 2007-07-31: https://web.mit.edu/rsi/www/pdfs/papers/2005/2005-kscott.pdf
2. Intel, public project record naming Scott's work, 2006-03-14: https://www.intel.com/pressroom/archive/releases/2006/20060314edu.htm
3. Research Science Institute 2005 Compendium, containing the same work in the 2005 volume: https://web.mit.edu/rsi/www/pdfs/papers/compendiums/rsicomp2005.pdf
