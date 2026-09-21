# Same-model review

**Same-model review: passed. Independent audit: not yet performed.**

## Correctness — PASS

The main input from the literature is the standard formula
\[
\psi(P\rtimes H)
=
|P|\psi(H)+(\psi(P)-|P|)\psi(C_H(P))
\]
for a cyclic \(p\)-group \(P\) acted on by a coprime group \(H\). Rewriting it as
\[
\psi(P\rtimes H)
=
\psi(P)\psi(C_H(P))
+
|P|\bigl(\psi(H)-\psi(C_H(P))\bigr)
\]
and using \(\gcd(\psi(P),p)=1\) gives the centralizer-difference gcd identity directly.

For \(H=C_{q^\beta}\) with action image \(q^\gamma\), the action kernel has order \(q^{\beta-\gamma}\). Exact subtraction of the cyclic prime-power formula gives
\[
\psi(C_{q^\beta})-\psi(C_{q^{\beta-\gamma}})
=
q^{2(\beta-\gamma)+1}\frac{q^{2\gamma}-1}{q+1}.
\]
Because \(q^\gamma\mid p-1\),
\[
\psi(C_{p^\alpha})
=
1+(p-1)\sum_{i=1}^{\alpha}p^{2i-1}
\equiv1\pmod q,
\]
so the displayed \(q\)-power can be removed inside the gcd. Finally,
\[
\frac{q^{2\gamma}-1}{q+1}<q^{2\gamma}
<
p^2-p+1
\le\psi(C_{p^\alpha}),
\]
which proves strict nondivisibility.

The cyclic-by-cyclic corollary was checked separately for its two group-theoretic reductions. If the action image is a \(q\)-group, all prime-to-\(q\) components of the cyclic complement lie in the kernel and split off as a coprime direct factor. If image and kernel orders are coprime, the cyclic complement itself splits as the faithful image-order factor times the kernel. The faithful case is excluded by the same gcd criterion and the inequality \(\psi(C_d)-1<d^2\le(p-1)^2\).

The verification artifact independently checks the exact gcd identity and strict obstruction for 4544 compatible parameter tuples with \(p<200\), \(\alpha\le4\), and \(\beta\le8\). This finite computation supports, but is not used in place of, the symbolic proof.

## Originality — PASS, to the best of our knowledge

The 2014 Harrington–Jones–Lamarche paper was inspected for the definition, abelian classification, coprime direct-product lemma, and its discussion of the unknown nonabelian case. Lazorec's 2020 preprint / 2021 journal paper was inspected through the ZM-group section, including Lemma 2.1(iii), Proposition 2.4, and the square-free-order open problem.

The closest prior statement found is Lazorec's Proposition 2.4. For \(ZM(p^\alpha,n,r)\) it proves nondivisibility under an exponent-size hypothesis of the form
\[
\alpha\ge\max_{q_i\mid p-1}\beta_i.
\]
The present prime-power-complement theorem has no comparison between \(\alpha\) and \(\beta\), gives an exact gcd formula, and depends only on the size \(q^\gamma\) of the action image. In particular it applies, for example, with \(\alpha=1\) and arbitrarily large \(\beta\), where that exponent-size hypothesis need not hold.

Targeted searches used the terms psi-divisible / \(\psi\)-divisible, sum of element orders, ZM-groups, cyclic-by-cyclic and cyclic semidirect products, prime-power complements, faithful cyclic actions, action kernels, and equivalent gcd/divisibility formulations. They located the original 2014 and 2021 papers, the 2023 psi-divisibility-graph paper, and a 2026 graph paper restricted to cyclic \(p\)-groups, but no statement of the exact gcd formula or the action-image criterion proved here.

The 2023 paper still explicitly states that no nonabelian psi-divisible finite group is known. This is consistent with, but does not establish, originality of the present obstruction.

Residual risk remains because the proof is short once the known semidirect-product formula is available. An equivalent observation may occur implicitly in an unindexed source, in a differently phrased metacyclic-group calculation, or as an unstated corollary of earlier formulas. No concrete evidence of such prior coverage was found.

## Value — PASS

The result gives a closed-form arithmetic obstruction rather than another isolated example. It completely removes the exponent-size restriction on the prime-power-complement slice of the previously studied \(ZM(p^\alpha,n,r)\) family, and it shows that the kernel depth \(\beta-\gamma\) disappears from the relevant gcd. The cyclic-by-cyclic corollary additionally rules out all prime-power action images and all coprime image/kernel decompositions.

This advances a documented older question without claiming to solve it. The remaining cyclic-by-cyclic region is explicit: the action image must involve at least two primes and must share a prime divisor with its kernel size before these arguments cease to decide psi-divisibility.
