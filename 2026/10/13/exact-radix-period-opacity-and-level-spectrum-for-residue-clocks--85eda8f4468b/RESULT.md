# Exact radix–period opacity and level spectrum for residue clocks

## Finding

For integers \(b\ge 2\) and \(m\ge 1\), let \(u_{b,m}(n)=n\bmod m\), with residues treated as \(m\) distinct letters, and let \(\varpi_b\) denote normalized prefix-metric opacity complexity in radix \(b\) as defined by Allouche and Yao [1]. Define
\[
\ell_b(m)=\min\{L\in\mathbb Z:L\ge2,\ b^L-b\ge m\}.
\]
Then the exact complexity is
\[
\boxed{\displaystyle \varpi_b(u_{b,m})=\begin{cases}0,&b\mid m,\\2^{2-\ell_b(m)},&b\nmid m.\end{cases}}
\]
In particular, the canonical residue clock is transparent precisely when the input radix divides its period. For every fixed \(b\ge2\) and every integer \(L\ge2\), the positive opacity level \(2^{2-L}\) is realized by exactly \((b-1)^2b^{L-2}\) positive integer values of \(m\). The statement is unchanged by an injective relabeling of the \(m\) residue letters.

## Assumptions and scope

The automaton reads most-significant-digit-first base-\(b\) expansions. Its transitions act on residues by \(\delta(r,d)=(br+d)\bmod m\) for \(0\le d<b\), its initial state is \(0\), and its state-output map is the identity on residues. The initial zero-loop makes it an internal automaton and allows arbitrary leading zeroes in path comparisons, as required by the path-based opacity definition [1]. For \(m=1\), the residue clock is constant; for \(b\mid m\), its opacity is zero. The comparison output alphabet for the prefix metric is the input digit alphabet, independently of the number of original residue letters, as in the original automaton-based definition [1, Sections 2–3].

A path is *inhomogeneous* if it visits one state through incoming edges with two different digit labels. By [1, Theorems 1–2], for an accessible minimal automaton the normalized opacity is zero if no such path exists, and otherwise is \(2^{2-L}\), where \(L\) is the smallest length of an inhomogeneous path. These background facts are not asserted as new results.

## Proof

**Minimality.** The residue automaton computes \(u_{b,m}\) on every standard digit expansion. Each of its \(m\) states is reachable, by reading the expansion of that residue (including \(0\) at the initial state). Distinct states have distinct immediate outputs, so the automaton is minimal. Consequently, [1, Theorem 1] identifies its opacity with the opacity complexity of the residue clock.

**Characterizing collisions.** Take any path of length \(L\) with digit word \(d_1d_2\cdots d_L\), where \(d_j\in\{0,\ldots,b-1\}\). Let \(v_i\) be the nonnegative integer represented by the first \(i\) digits, for \(1\le i\le L\). The state reached after digit \(i\) is \(v_i\bmod m\); its incoming label is \(d_i=v_i\bmod b\). Hence the path is inhomogeneous precisely when there are \(1\le i<j\le L\) such that
\[
v_j-v_i\equiv0\pmod m,\qquad v_j-v_i\not\equiv0\pmod b.
\]
Since \(v_j=b^{j-i}v_i+t\) for some \(0\le t<b^{j-i}\), this difference is nonnegative. If \(b\mid m\), the two displayed congruences cannot simultaneously hold. Thus every path is homogeneous and \(\varpi_b(u_{b,m})=0\). Indeed in this case the digit label can be decoded globally from the reached state as \(d_i=v_i\bmod b\).

**Sharp lower bound on collision depth.** If \(b\nmid m\) and an inhomogeneous pair exists, the positive difference is a multiple of \(m\), so it is at least \(m\). Because \(0\le v_i\le b^i-1\),
\[
0<v_j-v_i=(b^{j-i}-1)v_i+t\le b^j-b^i\le b^L-b.
\]
Therefore every inhomogeneous path has length at least \(\ell_b(m)\).

**Matching witness.** Let \(L=\ell_b(m)\) and \(K=b^{L-1}-1\). Since \(m\le b^L-b=bK\), choose an integer \(c\in\{0,\ldots,b-1\}\) for which \(cK\le m\le(c+1)K\), and put \(t=m-cK\in[0,K]\). Such a choice exists because the consecutive closed integer intervals cover \([0,bK]\). Read first the digit \(c\), followed by the \((L-1)\)-digit base-\(b\) expansion of \(t\), padded with leading zeroes as needed. The first prefix has value \(c\), whereas the final prefix has value
\[
v_L=b^{L-1}c+t=c+m.
\]
They arrive at the same state modulo \(m\), but their incoming labels differ because \(v_L-c=m\not\equiv0\pmod b\). Thus an inhomogeneous path of length \(L\) exists. The lower bound is attained, and [1, Theorem 2] gives the formula for \(\varpi_b\).

**Exact level multiplicities.** For \(L=2\), exactly the nonmultiples of \(b\) in \(1\le m\le b^2-b\) have depth \(L\): their number is \((b-1)^2\). For \(L\ge3\), the corresponding periods are exactly the nonmultiples of \(b\) in
\[
b^{L-1}-b<m\le b^L-b.
\]
This interval has \((b-1)b^{L-1}\) integers, of which precisely \((b-1)b^{L-2}\) are divisible by \(b\). Their difference is \((b-1)^2b^{L-2}\). These levels are distinct, completing the classification.

## Verification

Run `python3 verify.py` with Python 3 and no third-party packages. It directly enumerates digit paths (not using the closed formula as the collision test) for every radix \(2\le b\le6\), every modulus \(1\le m\le80\), and every path length at most six, comparing shortest observed collision depths to the formula. Separately, it constructs and checks the formula's explicit witness for radices \(2,3,4,5,7,10\) and \(1\le m\le1000\) with \(b\nmid m\), and directly recounts all periods at opacity levels \(L=2,3,4\) for \(2\le b\le8\). These finite checks corroborate but do not replace the proof for unbounded \(b,m,L\).

## Relationship to prior work

Allouche and Yao [1] defined normalized prefix-metric opacity of an automatic sequence and proved the general shortest-inhomogeneous-path formula (Theorems 1–2). Their publicly accessible 2024 preprint evaluates the transparent two-periodic example, but does not give the simultaneous sharp depth formula or level multiplicities for all radices and distinct-symbol periods. The later Acta Informatica article [2] is a revised publication of that work; the publicly visible publisher preview includes a period-three automaton figure but not enough of the revised text to establish whether it contains a broader classification. Individual small-period examples and the general shortest-path principle are acknowledged as prior contributions, not part of the originality claim.

The present statement adds the arithmetic minimization of path-collision depth over all input words and two independent parameters, plus the exact spectrum count. The classification is about maximal-information periodic residue clocks, not arbitrary periodic words in which letters may repeat inside the least period.

## Limitations

The opacity is specifically the normalized **prefix-metric** version of [1]. Other metrics, including the quadratic-semimetric notion discussed there, are not addressed. The output residue alphabet has \(m\) distinct symbols; the formula need not apply to noninjective projections of these symbols. The result uses [1]'s structural opacity theorem, but the needed arithmetic witness and optimality are proved here. The 2026 revised journal text was not fully accessible in the source comparison, so an unindexed or revised-text equivalent remains a priority risk.

## References

[1] J.-P. Allouche and J.-Y. Yao, *Opacity complexity of automatic sequences. The general case*, arXiv:2404.13601v1, publicly submitted 21 April 2024. https://arxiv.org/pdf/2404.13601

[2] J.-P. Allouche and J.-Y. Yao, *Opacity complexity of automatic sequences: the general case*, Acta Informatica 63, article 7 (2026), DOI:10.1007/s00236-026-00521-6. https://doi.org/10.1007/s00236-026-00521-6
