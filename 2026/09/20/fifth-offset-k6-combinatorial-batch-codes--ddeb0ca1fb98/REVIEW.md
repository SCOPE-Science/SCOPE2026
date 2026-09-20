# Review: exact fifth-offset storage for k=6 combinatorial batch codes

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness

**PASS.** The lower bound applies the published degree and deletion lemmas to an optimal \((m+5,N,6,m)\)-CBC. For \(m\ge10\), the hypotheses \(2\le6\le m<m+5\) hold, so some item has degree \(d\ge2\). Shen, Jia and Zhang prove \(N(m+4,6,m)=m+16\) for \(m\ge8\); therefore the deletion inequality gives
\[
N(m+5,6,m)\ge N(m+4,6,m)+d\ge m+18.
\]

The upper bound is supplied by an explicit \((15,28,6,10)\)-CBC. Its dual supports have total size 28. Exact enumeration of every request set of one through six items checks the Hall inequalities; the minimum union sizes are \(1,2,3,4,5,6\), respectively. Repeatedly adjoining one new singleton item on one new server gives a \((m+5,m+18,6,m)\)-CBC for every \(m\ge10\). The two bounds match.

The server-block and dual-support descriptions were cross-checked: they encode the same incidence relation and both have total storage 28. The compact artifact independently checks all 9948 request subsets of the base code.

## Originality

**PASS, to the best of our knowledge.** The closest exact ordinary-CBC literature found proceeds through the preceding diagonals: Jia, Zhang and Yuan (2016) give \(N(m+3,6,m)=m+13\) for \(m\ge8\), while Shen, Jia and Zhang (2018) give \(N(m+4,6,m)=m+16\) for \(m\ge8\). The 2019 continuation located in this line treats \(k=5\), not the \(k=6\), \(n=m+5\) diagonal. A 2023 survey of combinatorial batch codes was also checked as a later status source.

Searches used the exact and spaced forms of \(N(m+5,6,m)\), the base parameters \(N(15,6,10)\) and \((15,28,6,10)\), the phrases “combinatorial batch code”, “optimal CBC”, “restricted Hall condition”, and the prospective value \(m+18\). No checked source states the theorem or the base construction.

The most recent closely related item found is Guo and Zhang (2026), *On generalized combinatorial batch codes*. Its abstract introduces a broader model with repeated requests and failed servers and reports exact storage only for extreme or other special generalized parameter sets. The full text was not accessible in the checked sources. Because ordinary CBCs are a specialization of the generalized framework, this inaccessible full text is the principal residual originality risk; nothing in the available abstract or metadata states or visibly implies the equality \(N(m+5,6,m)=m+18\).

## Value

**PASS.** The result advances the exact \(k=6\) ordinary-CBC sequence from offsets \(n=m+3\) and \(n=m+4\) to the next diagonal \(n=m+5\), giving a new infinite exact family rather than a single small parameter value. The proof also supplies a compact reusable base construction at \((15,28,6,10)\) and shows that the known monotonicity machinery is already strong enough to certify its optimality throughout the family.

## Limitations

- Originality is a best-effort literature claim rather than an exhaustive database guarantee.
- The result does not settle \(m=8\) or \(m=9\) on the \(n=m+5\) diagonal.
- The 2026 generalized-CBC paper was not inspected in full; its abstract and metadata were checked, and its inaccessible body remains a possible source of stronger or overlapping results.
- The finite Hall verification establishes the base construction; the infinite extension and lower bound rely on the cited published lemmas and exact \(n=m+4\) theorem.
