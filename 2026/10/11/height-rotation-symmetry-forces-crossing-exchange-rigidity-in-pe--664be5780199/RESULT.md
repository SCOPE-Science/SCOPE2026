# Height-rotation symmetry forces crossing-exchange rigidity in petal diagrams

## Finding

For every odd integer \(N\ge5\), exactly \(\varphi(N)-2\) cyclic petal words are fixed by the height-rotation move \(\mathsf R\) and have **neither** an applicable crossing exchange \(\mathsf X\) nor an applicable trivial-petal deletion \(\mathsf T^-\). Each such word is also fixed up to cyclic rotation by \(\mathsf S\). Starting from one, a sequence of the standard isotopy moves reaching a word with fewer petals must first reach at least \(N+2\) petals.

More precisely, the height-rotation-fixed cyclic words are exactly
\[
 p_s=(\,0,s,2s,\ldots,(N-1)s\,)\pmod N,
 \qquad s\in(\mathbb Z/N\mathbb Z)^\times.
\]
There are \(\varphi(N)\) of them; every one admits no \(\mathsf X\), and precisely those with \(s\not\equiv \pm1\pmod N\) admit no \(\mathsf T^-\). These are statements about the **move calculus**, not assertions that all of the knots are unknotted, distinct, or represented with nonminimal petal number.

## Assumptions and scope

A petal word of odd length \(N=2n+1\) is a permutation \(p=(p_0,\dots,p_{N-1})\) of \(\{0,\dots,N-1\}\), considered up to cyclic shift of positions. Write \(\mathsf R(p)_j=p_j+1\pmod N\) and \(\mathsf S(p)_j=N-1-p_{N-1-j}\). Both preserve knot type and petal count, as in Vernitski [1, Section 3]. A deletion \(\mathsf T^-\) removes a cyclically adjacent pair whose distinct values are consecutive **integers** \(m,m+1\), shifting all higher values down by two. A crossing exchange \(\mathsf X\), at some basepoint, requires two cyclically adjacent position pairs with unordered height sets \(\{m,w+1\}\) and \(\{m+1,w\}\), for integers \(0\le m\), \(w\ge m+2\), \(w+1\le N-1\), together with a further nesting condition. The proof below only needs these necessary height-pair conditions. The moves \(\mathsf T^+\) and \(\mathsf T^-\) change petal count by exactly \(2\), while \(\mathsf X,\mathsf R,\mathsf S\) preserve it.

## Proof

**Classification of the fixed cyclic words.** Suppose \(\mathsf R(p)\) equals \(p\) up to cyclic shift. There is a shift \(\ell\pmod N\) with \(p_{j+\ell}\equiv p_j+1\pmod N\) for all \(j\). If \(g=\gcd(\ell,N)>1\), iterate this relation \(N/g\) times: it gives \(p_j\equiv p_j+N/g\pmod N\), a contradiction. Therefore \(\ell\) is invertible modulo \(N\), and writing \(s\ell\equiv1\pmod N\) gives \(p_{j+1}\equiv p_j+s\pmod N\). Cyclically start at the unique zero to obtain \(p_s\). Conversely, for every unit \(s\), height rotation of \(p_s\) is the cyclic shift by \(s^{-1}\), so this is a complete classification with \(\varphi(N)\) distinct words.

**No crossing exchanges.** Every cyclically adjacent pair of heights in \(p_s\) has difference \(\pm s\pmod N\). If a crossing exchange existed, its two necessary pairs would have positive height differences \(d+1\) and \(d-1\), where \(d=w-m\ge2\). Hence
\[
 d+1\equiv \epsilon s\pmod N,
 \qquad d-1\equiv\eta s\pmod N,
 \qquad \epsilon,\eta\in\{1,-1\}.
\]
Their difference gives \(2\equiv(\epsilon-\eta)s\pmod N\). Since \(N\) is odd and at least \(5\), equal signs are impossible. Opposite signs force \(s\equiv\pm1\pmod N\). For these two residual steps, an adjacent height difference is \(\pm1\pmod N\); thus each of the required differences \(d+1,d-1\), both in \(\{1,\ldots,N-1\}\), must lie in \(\{1,N-1\}\). As they differ by \(2\), this is impossible for odd \(N\ge5\): a pair of distinct elements of \(\{1,N-1\}\) differs by \(N-2\ne2\). Thus **no** unit-step \(p_s\) admits \(\mathsf X\). The nesting condition is immaterial because the necessary pairs already fail.

**Deletions and the second symmetry.** Consecutive letters of \(p_s\), including the wrap-around pair, differ by \(\pm s\pmod N\). If two heights are consecutive integers, their difference modulo \(N\) is \(\pm1\), so \(s\equiv\pm1\). Conversely, at steps \(\pm1\), consecutive integers occur (indeed, all but the cyclic wrap pair), and deletion applies. The only deletion-free fixed words are therefore the \(\varphi(N)-2\) unit steps other than \(\pm1\). Finally, \(\mathsf S(p_s)_j\equiv sj+s-1\pmod N\), another cyclic shift of \(p_s\) since \(s\) is a unit. Thus \(\mathsf R\), \(\mathsf S\) and \(\mathsf X\) cannot leave the cyclic class of such a deletion-free word; \(\mathsf T^-\) cannot start. Any move path to fewer petals must begin its change of petal number with \(\mathsf T^+\), reaching \(N+2\). This proves the claim.

## Verification

The proof works symbolically for **every** odd \(N\ge5\); the finite checks are regression tests, not substitutes for the modular argument. Run `python3 verify.py`, which enumerates every invertible step and every possible basepoint and crossing-exchange parameter for \(N\in\{3,5,7,9,11,13\}\), and checks the predicted crossing-exchange and deletion obstructions and the \(\mathsf R,\mathsf S\) symmetries. The test also checks all \(720\) normalized seven-petal words to recover the published \(50\) same-petal-count move components [1, Table 2]. No claim about knot identification beyond the cited known examples is needed.

## Relationship to prior work

Colton, Glover, Hughes and Sandberg [2] introduce trivial additions/deletions and crossing exchanges and establish their isotopy invariance and completeness. Vernitski [1, Section 3] defines the two additional isotopies \(\mathsf R,\mathsf S\), and [1, Results A–C] studies hard **unknot** diagrams up to nine petals, notably identifying isolated nine-petal examples and tabulating the seven-petal component graph. Those results do not state the all-odd-length classification of height-rotation-fixed words or the \(\varphi(N)-2\) rigidity count. The word \((0,2,4,6,1,3,5)\) occurs as the case \((N,s)=(7,2)\); no new knot-type identification is asserted. The contribution is the complete all-length fixed-locus theorem, including the obstruction for **all** units, not a new knot table.

## Limitations

A word with no deletion is not necessarily a *nonminimal hard representation* of its knot: the knot may already have minimal petal number \(N\). Knot type, pairwise knot inequivalence, existence of a later deletion after stabilization, and the minimum stabilization excess **above** two are not established. The result is specific to the move set \(\{\mathsf T^\pm,\mathsf X,\mathsf R,\mathsf S\}\) of [1]; adding new petal-number-preserving moves may remove its obstruction. Originality is checked against accessible primary literature and indexed results, not established by absence of search hits alone.

## References

[1] Alexei Vernitski, *Some petal diagrams of the unknot are hard*, arXiv:2610.01596v1 (first public 2026-10-01), Sections 3, 5, 6, 7; https://arxiv.org/abs/2610.01596 .

[2] Leslie Colton, Cory Glover, Mark Hughes and Samantha Sandberg, *A Reidemeister type theorem for petal diagrams of knots*, arXiv:1812.08930v1 (2018), Sections 1–2; https://arxiv.org/abs/1812.08930 .
