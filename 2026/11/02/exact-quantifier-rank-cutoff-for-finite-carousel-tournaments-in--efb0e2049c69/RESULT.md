# Exact quantifier-rank cutoff for finite carousel tournaments in three-variable logic

## Finding

Let \(R_n\) be the tournament on \(\mathbb Z/n\mathbb Z\), for an odd integer \(n\ge3\), in the language containing equality and one binary arc relation \(E\), with
\[
 E(i,j)\quad\Longleftrightarrow\quad (j-i\bmod n)\in\{1,\ldots,(n-1)/2\}.
\]
Write \(R_m\equiv_q^{\mathrm{FO}^3}R_n\) when the structures satisfy exactly the same first-order sentences of quantifier rank at most \(q\) using only three reusable variable symbols and **no counting quantifiers**.

**Theorem.** For every integer \(q\ge2\) and all odd \(m,n\ge3\),
\[
 R_m\equiv_q^{\mathrm{FO}^3}R_n
 \quad\Longleftrightarrow\quad
 \bigl(m=n<2^q-1\bigr)\ \text{or}\ \bigl(m,n\ge2^q-1\bigr).
\]
The same classification holds if three-variable logic is replaced by unrestricted first-order logic at rank \(q\). Hence the family has exactly \(2^{q-1}-1\) rank-\(q\) theories, with sharp largest minimum representative size \(2^q-1\). At ranks zero and one all structures in the family agree. For different odd orders \(3\le m<n\), the minimum distinguishing quantifier rank is
\[
 \left\lfloor\log_2(m+1)\right\rfloor+1,
\]
and a distinguishing sentence exists with just three variables.

## Assumptions and scope

The universe has exactly \(n\) vertices for each odd \(n\ge3\). The arc symbol is a binary *relation*, not a successor function; no vertex, order, colour, inverse, counting quantifier, or arithmetic operation is named. Quantifier rank counts nested first-order quantifiers; reusing any of the same three variable names is permitted. The theorem is a classification at each finite rank, not an assertion that different finite tournaments are elementarily equivalent at unrestricted rank.

## Proof

### 1. Two natural interval counts

Put \(n=2h+1\). For an oriented pair \(E(x,y)\), let \(d\in\{1,\ldots,h\}\) be its clockwise distance and set
\[
 a(x,y)=d-1,\qquad b(x,y)=h-d.
\]
The set \(\{z:E(x,z)\wedge E(z,y)\}\) is exactly the clockwise open interval from \(x\) to \(y\), so its size is \(a(x,y)\). The set \(\{z:E(x,z)\wedge E(y,z)\}\) has size \(b(x,y)\). Thus every oriented pair obeys
\[
 a(x,y)+b(x,y)=h-1.
\]
Conversely, each \(a\in\{0,\ldots,h-1\}\), together with \(b=h-1-a\), is realized by some oriented pair. These identities follow immediately by rotating \(x\) to zero and taking \(y=d\).

### 2. Threshold formulas using three variables

For each \(r\ge0\), put \(T_r=2^r-1\). For every \(0\le s\le T_r\), construct two formulas \(A_{r,s}(x,y)\) and \(B_{r,s}(x,y)\), of quantifier rank at most \(r\), each using only \(x,y,z\), such that on any \(R_n\)
\[
 A_{r,s}(x,y)\iff E(x,y)\ \text{and}\ a(x,y)\ge s,
\]
\[
 B_{r,s}(x,y)\iff E(x,y)\ \text{and}\ b(x,y)\ge s.
\]
At level zero, \(A_{0,0}=B_{0,0}=E(x,y)\). To pass from \(r\) to \(r+1\), inherit the formula for \(s\le T_r\). For \(T_r<s\le2T_r+1=T_{r+1}\), choose \(u,v\in\{0,\ldots,T_r\}\) with \(u+v+1=s\). Define
\[
 A_{r+1,s}(x,y):=E(x,y)\wedge\exists z\bigl(E(x,z)\wedge E(z,y)
 \wedge A_{r,u}(x,z)\wedge A_{r,v}(z,y)\bigr),
\]
and
\[
 B_{r+1,s}(x,y):=E(x,y)\wedge\exists z\bigl(E(x,z)\wedge E(y,z)
 \wedge A_{r,u}(y,z)\wedge B_{r,v}(x,z)\bigr).
\]
These are syntactically three-variable formulas: whenever a recursive subformula is written with arguments other than \((x,y)\), alpha-rename its bound variables to the remaining name among \(x,y,z\). Binding the third variable inside one conjunct does not bind the same name in its sibling conjunct.

For the first recurrence, a point \(z\) on the clockwise interval \((x,y)\) splits its \(a(x,y)\) interior points into \(a(x,z)\), the point \(z\), and \(a(z,y)\). For the second, a common outneighbour \(z\) of \(x,y\) splits the \(b(x,y)\) points into \(a(y,z)\), the point \(z\), and \(b(x,z)\). The relevant identities are
\[
 a(x,y)=a(x,z)+1+a(z,y),\qquad
 b(x,y)=a(y,z)+1+b(x,z)
\]
when \(z\) lies in the respective selected region. Every possible split of the nonnegative total occurs as \(z\) traverses that region. Induction proves the claimed formula semantics, ranks, and variable bound.

Fix \(q\ge2\), write \(r=q-2\), \(T=T_r\), and let \(1\le H\le2T+1\). Choose \(s,t\le T\) with \(s+t=H-1\). The three-variable sentence
\[
 \Theta_{q,H}:=\exists x\exists y\bigl(E(x,y)\wedge A_{r,s}(x,y)
 \wedge B_{r,t}(x,y)\bigr)
\]
has quantifier rank at most \(q\). By the preceding pair-sum identity it is true in \(R_{2h+1}\) **if and only if** \(h\ge H\). Consequently every half-order \(h<2T+1=2^{q-1}-1\) is distinguished from each larger half-order by choosing \(H=h+1\). This proves all the claimed lower bounds with three variables.

### 3. Uniform upper bound by an antipodal-circle game

It remains to prove that two odd orders at least \(2^q-1\) agree even in unrestricted rank-\(q\) first-order logic. Represent each vertex \(i\) of \(R_n\) by the *even* position \(2i\) on a cyclic array of \(2n\) positions. Its formal antipode is \(\sigma(2i)=2i+n\), an odd position. Then \(E(i,j)\) holds exactly when the even representative of \(j\) lies strictly clockwise between the representative of \(i\) and its antipode. The cyclic order of any selected representatives together with all their antipodes therefore determines every arc and equality among selected vertices.

For \(r\ge0\) put \(L_r=2^{r+1}-1\). After a game move with \(r\) rounds remaining, maintain the circular order, labels, and original/antipode parity of every selected marked point. Between consecutive marks, require corresponding positive integer gap lengths either to be exactly equal, or both to be at least \(L_r\) and to have equal parity. Gaps in antipodal positions are paired and have identical lengths. This invariant is sufficient for a partial isomorphism: the order of each selected representative and each selected antipode is preserved.

Here is the elementary split lemma. If corresponding gaps are equal, a newly inserted even representative is copied at the same offset. If lengths \(\ell,\ell'\) have the same parity and are both at least \(L_r=2L_{r-1}+1\), any split \(\ell=u+v\) into positive lengths with prescribed endpoint parities admits a split \(\ell'=u'+v'\), with the same respective parities, such that each sublength is either equal to its counterpart when that counterpart is below \(L_{r-1}\), or both are at least \(L_{r-1}\). Indeed, if one of \(u,v\) is below \(L_{r-1}\), copy it and leave at least \(L_{r-1}+2\) on the other side. Otherwise choose \(u'\) to be the least integer at least \(L_{r-1}\) of the required parity (one of \(L_{r-1},L_{r-1}+1\)); the remainder is also at least \(L_{r-1}\), and parity follows from \(\ell\equiv\ell'\pmod2\). The lemma also covers the first nontrivial stage \(L_0=1\).

In the game, first remove the moving pebble and its antipode, if previously placed. Merging adjacent gaps preserves the current gap condition because sums of entirely equal small gaps agree exactly, whereas any sum containing a large gap remains large, and parity is additive. Inserting a new selected vertex splits one gap and, simultaneously, its antipodal partner gap into the same two lengths; the split lemma supplies the matching even position and its forced odd antipode, lowering the threshold to \(L_{r-1}\). Repeated selections are answered by repeated selections, preserving equality. Thus the invariant is maintained through the prescribed rounds, regardless of the number of available pebbles.

After the first vertex is selected, the two gaps in the doubled circle both have length \(n\); if \(n,n'\ge 2^q-1=L_{q-1}\), they satisfy the invariant with \(q-1\) rounds remaining. Duplicator therefore wins the full \(q\)-round Ehrenfeucht–Fraïssé game, proving unrestricted rank-\(q\) equivalence. In particular, three-variable rank-\(q\) equivalence follows.

### 4. Exact number of classes and distinguishing rank

Since \(h=(n-1)/2\), the stable half-order condition \(h\ge2^{q-1}-1\) is precisely \(n\ge2^q-1\). All smaller allowed odd orders are singleton rank-\(q\) classes by Step 2. Their number plus the stable class is \(2^{q-1}-1\). The bound \(2^q-1\) is attained by that stable class and cannot be decreased. For \(m<n\), the smallest \(q\) with \(m<2^q-1\) is \(\lfloor\log_2(m+1)\rfloor+1\), yielding the final formula.

## Verification

The standalone `verify.py` has two logically distinct finite checks. First it evaluates the recursive threshold formulas directly on carousel tournaments of every odd order from three through 49, for ranks zero through four and all permitted thresholds, checking 18,600 predicate instances against the closed forms for \(a,b\). Second, independently of those formulas, it computes exact three-variable logical rank types by repeated quantifier-extension refinement for every odd order from three through 39 and every rank zero through five. It recovers class counts one, one, one, three, seven, fifteen and thresholds three, three, three, seven, fifteen, 31. The accompanying `verification_output.txt` records the output of running the script. These finite tests corroborate but do not establish any general infinite assertion; the proof in Steps 1–4 supplies that assertion.

## Relationship to prior work

Coregliano (arXiv:1503.04124, publicly posted March 13, 2015) defines and studies the balanced locally transitive carousel tournaments, including their four two-point extension regions, but studies tournament limits and subgraph-density statistics rather than exact first-order quantifier-rank theories. Grohe and Otto (CSL 2012) develop the general finite-variable pebble-game setting and its relations to algebraic approximations; their results do not specialize to this exact rank threshold. Earlier finite-rank calculations for carousel tournaments establish only individual ranks; the distinguishing addition here is **a uniform sharp lower bound for every rank**, with explicit three-variable formulas that match the independently derivable full-first-order upper bound.

## Limitations

This theorem applies only to the standard odd-order balanced locally transitive carousel tournaments with their pure directed-edge relation. It does not classify arbitrary locally transitive tournaments, labelled or coloured tournaments, tournaments under counting logic, or arbitrary digraphs. The displayed finite programs are not independent mathematical audits. Historical-priority conclusions are limited to the primary sources and similarity searches inspected; a stronger unpublished or differently named theorem could subsume the classification.

## References

1. L. N. Coregliano, *Quasi-Carousel Tournaments*, arXiv:1503.04124, version initially public March 13, 2015. https://arxiv.org/abs/1503.04124
2. M. Grohe and M. Otto, *Pebble Games and Linear Equations*, Computer Science Logic (CSL 2012), pp. 289–304, DOI:10.4230/LIPIcs.CSL.2012.289. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.CSL.2012.289
3. A. Goodall, J. Nešetřil and P. Ossona de Mendez, *Strongly polynomial sequences as interpretations*, arXiv:1405.2449, first public May 10, 2014. https://arxiv.org/abs/1405.2449
